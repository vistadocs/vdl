---
title: Consult/Request Tracking Technical Manual (GMRC*3.0*189)
doc_type: TM
doc_label: Technical Manual
doc_layer: anchor
doc_subject: 
app_code: GMRC
app_name: "CPRS: Consult/Request Tracking"
section: CLI
app_status: active
pkg_ns: GMRC
patch_ver: 3.0
patch_id: GMRC*3.0
group_key: "GMRC:GMRC:3.0"
file_numbers: []
security_keys: []
menu_options: 142
description: "> NOTE: The revision history cycle begins once changes or enhancements are requested after the document has been baselined."
audience: 
keywords: 
  - span
  - href
  - class
  - even
  - consult
  - gmrc
  - table
  - consults
  - style
  - width
page_count: 0
word_count: 42863
section_count: 0
table_count: 62
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: November 2024
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Consult_Request_Tracking/constm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Consult_Request_Tracking/constm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=62"
---

---
title: |
  <span id="_Hlk169094107" class="anchor"></span>

  Consult/Request Tracking 3.0

  Technical Manual
---

![](consult-request-tracking-technical-manual-gmrc-3-0-189/001.png)

November 2024

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

<span id="_Toc179978524" class="anchor"></span>Revision History

> **NOTE:** The revision history cycle begins once changes or enhancements are requested after the document has been baselined.

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 18%" />
<col style="width: 45%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Patch</th>
<th>Description</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>11/2024</td>
<td>GMRC*3.0*189</td>
<td><p>Sections updated to include changes for patch GMRC*3.0*189.</p>
<p>Updated Revision History, Table of Contents, New Features section.</p></td>
<td></td>
</tr>
<tr class="even">
<td>08/2024</td>
<td>GMRC*3.0*206</td>
<td>Updated for 508 compliance</td>
<td>CPRS Development Team</td>
</tr>
<tr class="odd">
<td>11/2023</td>
<td>GMRC*3.0*185</td>
<td><p>Document content transferred to latest OIT template.</p>
<p>Sections updated to include changes for patch GMRC*3.0*185.</p>
<p>Applied section numbering schema throughout for greater ease of reference.</p>
<p>Converted ‘computer screen’ content to figures to comply with accessibility requirements and greater ease of reference.</p>
<p>Updated Revision History, Table of Contents, index, section 5.35 Interfacility Consults When Used With Cerner-Converted Sites, and HL7 field descriptions.</p>
<p>Redrew Figure 8-1: Consult Request Tracking File Diagram in Visio for greater clarity and maintainability.</p></td>
<td></td>
</tr>
<tr class="even">
<td>08/2023</td>
<td>GMRC*3.0*199</td>
<td><p>Updated for GMRC*3.0*199.</p>
<p>Updated Figure 5-46: Running an IFC Possible Erroneous Comment Report.</p>
<p>Added bulleted SCR and CSV descriptive text to section 5.31.</p>
<p>Added section 5.31.1. Viewing the Possible Erroneous Comment Report in Excel.</p></td>
<td></td>
</tr>
<tr class="odd">
<td>03/2023</td>
<td>GMRC*3. <a href="#_Toc144362940">0*193</a></td>
<td><p><a href="#_Toc144362940">Updated for GMRC*3.<span>0*193</span></a></p>
<p><a href="#_Toc144362940"><span>Added IFC Possible Erroneous Comments Report to menu options on Table 5-1, Table 5-4, Table 7-1 Figure 7-4, and Figure 7-7.</span></a></p></td>
<td></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>01/ 2023</span></a></td>
<td><a href="#_Toc144362940"><span>GMRC*3.0*184</span></a></td>
<td><p><a href="#_Toc144362940"><span>Sections updated to include changes for patch GMRC*3.0*184.</span></a></p>
<p><a href="#_Toc144362940"><span>Updated Revision History, Table of Contents, Interfacility Consults When Used With Cerner Converted Sites section and HL7 field descriptions.</span></a></p></td>
<td></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>04/2022</span></a></td>
<td><a href="#_Toc144362940"><span>GMRC*3.</span><span>0*186</span></a></td>
<td><p><a href="#_Toc144362940"><span>Describes the new field to be displayed when editing or entering a community care consult service (Figure 5-10)</span></a></p>
<p><a href="#_Toc144362940"><span>Review and approval of changes in section 2 and Figure 5-10.</span></a></p></td>
<td></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>09/2021</span></a></td>
<td><a href="#_Toc144362940"><span>GMRC*3.0*176</span></a></td>
<td><p><a href="#_Toc144362940"><span>Update for GMRC*3.0*176</span></a></p>
<p><a href="#_Toc144362940"><span>Refer to section 5.</span><span>39: On an incoming HL7 message from a Cerner-converted site, if the urgency code in ORC.7.</span><span>6 is “S” (STAT), which gets converted to “N” (NEXT AVAILABLE”).</span></a></p></td>
<td></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>05/ 2021</span></a></td>
<td><a href="#_Toc144362940"><span>GMRC*3.0*84</span></a></td>
<td><p><a href="#_Toc144362940"><span>NSR 20110210: Described GMRC*3.0*84 in section 2.</span> <span>Added information about Prosthetics Consult Updated to the list of consult notifications in section 7.</span><span>6 to the deletion of notifications and the implementation and maintenance sections in Appendix A: Install, Planning, and Implementation Checklist</span><span>.</span></a></p>
<p><a href="#_Toc144362940"><span>Added information about enabling the Prosthetics Consult Updated notification and deleted redundant information throughout.</span></a></p></td>
<td></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>03/ 2021</span></a></td>
<td><a href="#_Toc144362940"><span>GMRC*3.</span><span>0*170</span></a></td>
<td><p><a href="#_Toc144362940"><span>Replaced sentence in section 6.</span><span>2 with: “<strong>Error! Reference source not found.</strong>.”</span></a></p>
<p><a href="#_Toc144362940"><span>Updated Title page, Revision History, Table of Contents, Index, and Footers (Title, ii, vi, 217, all)</span></a></p></td>
<td></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>REDACTED</span></a></td>
<td><a href="#_Toc144362940"><span>GMRC*3.0*145</span></a></td>
<td><p><a href="#_Toc144362940"><span>Added section 2.</span><span>2, which describes patch GMRC*3.0*145.</span></a></p>
<p><a href="#_Toc144362940"><span>Revised dates on Title page and footers</span></a></p></td>
<td></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>REDACTED</span></a></td>
<td><a href="#_Toc144362940"><span>GMRC*3.</span><span>0*154</span></a></td>
<td><a href="#_Toc144362940"><span>Section 5.</span><span>35 and Appendix F</span></a></td>
<td></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>REDACTED</span></a></td>
<td><a href="#_Toc144362940"><span>GMRC*3.</span><span>0*88</span></a></td>
<td><p><a href="#_Toc144362940"><span>Changes for Consults in v31b.</span></a></p>
<p><a href="#_Toc144362940"><span>Added an item to Figure 5-1 to Define FSC HCP Mail Group.</span></a></p>
<p><a href="#_Toc144362940"><span>Added notes in section 5 that update users can order tracking consults.</span></a></p>
<p><a href="#_Toc144362940"><span>Added a reference in Figure 7.</span><span>16 to the GMRC FSC HCP SUPPORT EMAIL parameter.</span></a></p>
<p><a href="#_Toc144362940"><span>Provided a full definition in Table 14-11 of the GMRC FSC SUPPORT EMAIL PARAMETER.</span></a></p>
<p><a href="#_Toc144362940"><span>Listed in Table 9-1 the above parameter in an option list by options and display name.</span></a></p></td>
<td></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>REDACTED</span></a></td>
<td><a href="#_Toc144362940"><span>GMRC*3.0*139</span></a></td>
<td><a href="#_Toc144362940"><span>Added to DST Consult handling in section 2.</span><span>3 and section 14.</span><span>20.</span></a></td>
<td></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>REDACTED</span></a></td>
<td><a href="#_Toc144362940"><span>GMRC*3.</span><span>0*123</span></a></td>
<td><a href="#_Toc144362940"><span>Added details for new patch in Table 14-7, section 14.</span><span>3.</span><span>3, section 14.4.</span><span>3, and section 14.5.</span></a></td>
<td></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>REDACTED</span></a></td>
<td><a href="#_Toc144362940"><span>GMRC*3.</span><span>0*124</span></a></td>
<td><p><a href="#_Toc144362940"><span>Adds Decision Support Tool (DST) comment to a Consult when a Consult Order is signed and there is a DST comment listed in the Order. See section 14-20</span></a></p>
<p><a href="#_Toc144362940"><span>and Table D-6.</span></a></p></td>
<td></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>REDACTED</span></a></td>
<td><a href="#_Toc144362940"><span>GMRC*3.</span><span>0*112</span></a></td>
<td><a href="#_Toc144362940"><span>Added details for new patch.</span></a></td>
<td></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>REDACTED</span></a></td>
<td><a href="#_Toc144362940"><span>GMRC*3.0*113</span></a></td>
<td><a href="#_Toc144362940"><span>Added details for Cancelled To Discontinued Consults. See section 6.</span><span>3.</span></a></td>
<td></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>REDACTED</span></a></td>
<td><a href="#_Toc144362940"><span>GMRC*3.</span><span>0*110</span></a></td>
<td><a href="#_Toc144362940"><span>Added text and new screen shot to show the new field “UCID Display” on the order detail. See section 5.</span><span>34.</span></a></td>
<td></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>REDACTED</span></a></td>
<td><a href="#_Toc144362940"><span>GMRC*3.</span><span>0*107</span></a></td>
<td><a href="#_Toc144362940"><span>Added details for new GMRC Reports to support the ADMIN KEY consults for consults that are Administratively released by Policy.</span></a></td>
<td></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>REDACTED</span></a></td>
<td><a href="#_Toc144362940"><span>GMRC*3.0*99 and GMRC*3.0*106</span></a></td>
<td><a href="#_Toc144362940"><span>Added features and setup for new logical link. See Table 14-3, Table 14-6, and section 14.</span><span>4.</span><span>2.</span></a></td>
<td></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>REDACTED</span></a></td>
<td><a href="#_Toc144362940"><span>GMRC*3.</span><span>0*89</span></a></td>
<td><a href="#_Toc144362940"><span>Added information related to new functionality: Consult Closure Tool, Secondary Printer option for SF 513, and printing age and cell phone number on SF 513.</span></a></td>
<td></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>REDACTED</span></a></td>
<td><a href="#_Toc144362940"><span>GMRC*3.0*83</span></a></td>
<td><a href="#_Toc144362940"><span>Added information about the new MUMPS cross reference AG to be used only by the Scheduling Package.</span></a></td>
<td></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>REDACTED</span></a></td>
<td><a href="#_Toc144362940"><span>GMRC*3.0*81</span></a></td>
<td><a href="#_Toc144362940"><span>Changed Earliest Appropriate Date to Clinically Indicated Date. See section 5.</span><span>12.</span></a></td>
<td></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>REDACTED</span></a></td>
<td><a href="#_Toc144362940"><span>GMRC*3.</span><span>0*75</span></a></td>
<td><a href="#_Toc144362940"><span>Added information on components of a bi-directional interface that will connect Consults and HCPS. Refer to Table 14-2, Table 14-5, and section 14.</span><span>3.</span><span>1.</span></a></td>
<td></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>REDACTED</span></a></td>
<td><a href="#_Toc144362940"><span>GMRC*3*73</span></a></td>
<td><a href="#_Toc144362940"><span>ICD-10 Updates. Added info about changes made for the ICD-10 project.</span></a></td>
<td></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>REDACTED</span></a></td>
<td><a href="#_Toc144362940"><span>Clarified “Service Team to Notify” field in Add Consult Services option.</span></a></td>
<td><a href="#_Toc144362940"><span>Refer to section 5.</span><span>2 and Table 5-1.</span></a></td>
<td></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>REDACTED</span></a></td>
<td><a href="#_Toc144362940"><span>GMRC*3.</span><span>0*76</span></a></td>
<td><p><a href="#_Toc144362940"><span>Added notes that the Ordering Provider will NOT receive an alert; added note that the clinician who requested the order is notified electronically.</span></a></p>
<p><a href="#_Toc144362940"><span>Noted EARLIEST APPROPRIATE DATE will be used in place of DATE OF REQUEST.</span></a></p></td>
<td></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>REDACTED</span></a></td>
<td><a href="#_Toc144362940"><span>GMRC*3.0*74</span></a></td>
<td><a href="#_Toc144362940"><span>Added Define Fee Services (GMRC FEE PARAM) option and GMRC FEE SERVICES parameter and supporting GMRCFP* routines.</span></a></td>
<td></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>REDACTED</span></a></td>
<td><a href="#_Toc144362940"><span>GMRC*3.0*71</span></a></td>
<td><a href="#_Toc144362940"><span>Modified description for CONSULT/REQUEST UPDATED.</span></a></td>
<td></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>REDACTED</span></a></td>
<td><a href="#_Toc144362940"><span>Earliest Appropriate Date</span></a></td>
<td><a href="#_Toc144362940"><span>Refer to section 5-12.</span></a></td>
<td></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>REDACTED</span></a></td>
<td><a href="#_Toc144362940"><span>GMRC*3.</span><span>0*63</span></a></td>
<td><a href="#_Toc144362940"><span>Modified report format.</span></a></td>
<td></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>REDACTED</span></a></td>
<td><a href="#_Toc144362940"><span>Patch 60</span></a></td>
<td><p><a href="#_Toc144362940"><span>Performance Monitor Report. Refer to section 5-12, Figure 5-18</span></a></p>
<p><a href="#_Toc144362940"><span>, Figure 5-19</span></a></p>
<p><a href="#_Toc144362940"><span>, and Figure 5-20</span></a></p>
<p><a href="#_Toc144362940"><span>.</span></a></p></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>Patch 41</span></a></td>
<td><a href="#_Toc144362940"><span>Performance Monitor</span></a></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>Include Patch 22</span></a></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>Include Patch 23</span></a></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>Include Patch 17</span></a></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>Include Patch 21</span></a></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>Include Patch 15, 19, and 20</span></a></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>Include Patches 13, 14, 16, and 18</span></a></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>Add Patches 6 thru 8, 11, and 12</span></a></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>Include Patches 1 thru 5</span></a></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>Originally released</span></a></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

[[  
Table of Contents](#_Toc144362940)](#_Toc144362940)

[[The Consult/Request Tracking package (Consults) has been developed to improve the quality of patient care by providing an efficient mechanism for clinicians to order consults and requests using Computerized Patient Record System (CPRS) Order Entry, and to permit hospital services to track the progress of a consult order from the point of receipt through its final resolution.](#_Toc144362940)](#_Toc144362940)

[[This manual provides technical descriptions of Consults tracking routines, protocols, files, globals, options, security data, menu diagrams and any other information required to effectively set up and use the Consults package.](#_Toc144362940)](#_Toc144362940)

[[From time-to-time, improvements are made to the Consults package. The latest information about Consults, as well as the latest version of this manual, is posted on the Consults Web Page at: vista.med.va.gov/consults.](#_Toc144362940)](#_Toc144362940)

[[Information in this manual is technical in nature and is intended to be used by Veterans Affairs Medical Center (VAMC) Information Resource Management Service (IRMS) staff members and Clinical Application Coordinators (CAC's).](#_Toc144362940)](#_Toc144362940)

[[  
](#_Toc144362940)](#_Toc144362940)

[[This patch, part of the software release for CPRS graphical user interface (GUI) v32a, introduces the new PROSTHETICS CONSULT UPDATED notification. This notification will be generated whenever users add comments to or take the schedule action upon a prosthetics consult in CPRS GUI.](#_Toc144362940)](#_Toc144362940)

[[This patch, part of the larger CPRS GUI v31 Mission Act release, assists with implementing the Decision Support Tool (DST) and Consult Toolbox (CTB) directly into CPRS GUI. Please consult the DST and CTB user manuals on the Veterans Health Information System and Technology Architecture (VistA) Document Library for detailed information regarding use of these features.](#_Toc144362940)](#_Toc144362940)

[[This patch adds auto-forwarding functionality. When the DST transmits the auto-forward information to CPRS, the existing CPRS remote procedure call (RPC) process will detect the auto-forward request and forward the order to a new consult location, which is referenced in the REQUEST SERVICE file (#123.5).](#_Toc144362940)](#_Toc144362940)

[[This patch adds functionality for IFC order communication between non-converted VistA sites and converted Cerner sites. Data required by Cerner are extracted from HL7 order messages and saved in the REQUEST/CONSULTATION file (#123) for later use, so VDIF (Veterans Data Integration and Federation) is no longer required to do so. PID and OBR segments are added to outgoing HL7 messages destined for Cerner populated per Cerner requirements. Cumulative comments are sent to converted sites except if the IFC is for Prosthetics.](#_Toc144362940)](#_Toc144362940)

[[This patch loads data required by Cerner in PID and OBR segments for IFCs entered prior to the release of GMRC\*3.0\*184. It adds functionality for IFC order communication between non-converted VistA sites and converted Cerner sites. Prosthetics data required by Cerner are extracted from HL7 order messages and saved in the REQUEST/CONSULTATION file (#123) for later use, so VDIF (Veterans Data Integration and Federation) is no longer required to do so. Cumulative comments are sent to converted sites for 5 additional CPRS actions not included in patch 184. Finally, the VistA instance station number replaces the ORDERING FACILITY (field \#.05 of file \#123) in the outgoing OBR segment.](#_Toc144362940)](#_Toc144362940)

[[  
](#_Toc144362940)](#_Toc144362940)

[[This patch adds the following functionality for IFCs exchanged between non-converted VistA sites and Cerner:](#_Toc144362940)](#_Toc144362940)

- 
- 
- 
- 
- 
- 
- 

> [[Recognizes when an IFC order sent by VistA to Cerner is received but not processed by Cerner, queues the order for re-transmission the next day by adding the order to the IFC MESSAGE LOG (file \#123.6) with an error code 203 – Patient not in Cerner.For IFC orders incoming from Cerner to VistA, modifies the processing when the referenced patient is not found in the PATIENT file (#2) by calling the proxy add API introduced by DG\*5.3\*1096.Researching issues for IFCs between VistA and Cerner is hampered by the quick purging of HL7 records from VistA. GMRC\*3\*189 calls APIs to record HL7 messages for IFCs sent by Cerner to a non-converted VistA site or by VistA to Cerner in the HL7 message repository provided by EHM\*1\*10.Increases the size of the REMOTE CONSULT FILE ENTRY field (#.06) of the REQUEST/CONSULTATION file (#123) from 12 to 20 digits to handle longer Cerner order numbers expected in the future. Recognizes when a patient is missing from the converted VistA that corresponds to the Cerner ordering site and calls the proxy add API introduced by DG\*5.3\*1096.When a comment is entered on a consult post-complete, the patch changes the comment status sent in OBX-11 from Preliminary (P) to Changed (C).GMRC\*3\*154 introduced a mechanism for the IFC interface to proxy add a patient to Cerner before transmitting a new order. The proxy add API operates asynchronously in part with the update to the Treating Facility List being done after a return value is sent back to the calling routine. As a result, the new order messages cannot always be routed to Cerner after the API is called. GMRC\*3\*189 generates a 205 error (waiting for treating facility to update) and re-queues the new order for transmission the next time the Background Processor runs.When the proxy add process fails, patch GMRC\*3\*189 generates a Mailman message to the IFC PATIENT ERROR MESSAGES mail group.](#_Toc144362940)](#_Toc144362940)

[[The Consults package provides an interface with CPRS Order Entry which permits clerks or clinicians to enter, edit, and review consults and requests within the CPRS package.](#_Toc144362940)](#_Toc144362940)

- 
- 
- 
- 

[[  
](#_Toc144362940)](#_Toc144362940)

[[This technical manual provides IRMS/ADPAC personnel with technical descriptions of Consults routines, files, options, and other necessary information required to effectively implement and use the Consults package.](#_Toc144362940)](#_Toc144362940)

[[This manual should assist you in:](#_Toc144362940)](#_Toc144362940)

- 
- 
- 
- 

[[  
](#_Toc144362930)](#_Toc144362940)

[[A checklist is provided to help you install, plan, and implement the Consults package (see Appendix A). Use the checklist in conjunction with the detailed information provided in this "Implementation and Maintenance" section.](#_Toc144362930)](#_Toc144362940)

[[The tools required to implement and maintain the Consults package are found in the Consult Management \[GMRC MGR\] menu. Refer to Table 5-1, which lists and defines all of the options distributed with the Consults package](#_Toc144362930)](#_Toc144362940)

[[<span id="_Toc169170345" class="anchor"></span>Table 5‑1: Consult Management \[GMRC MGR} Menu Options](#_Toc144362930)](#_Toc144362940)

| [[Menu Option](#_Toc144362930)](#_Toc144362940) | [[Menu Option Description](#_Toc144362930)](#_Toc144362940)                            |
|-------------------------------------------------|----------------------------------------------------------------------------------------|
| [[RPT](#_Toc144362930)](#_Toc144362940)         | [[Consult Tracking Reports ...](#_Toc144362930)](#_Toc144362940)                       |
| [[ST](#_Toc144362930)](#_Toc144362940)          | [[Completion Time Statistics](#_Toc144362930)](#_Toc144362940)                         |
| [[PC](#_Toc144362930)](#_Toc144362940)          | [[Service Consults Pending Resolution](#_Toc144362930)](#_Toc144362940)                |
| [[CC](#_Toc144362930)](#_Toc144362940)          | [[Service Consults Completed](#_Toc144362930)](#_Toc144362940)                         |
| [[CP](#_Toc144362930)](#_Toc144362940)          | [[Service Consults Completed or Pending Resolution](#_Toc144362930)](#_Toc144362940)   |
| [[IFC](#_Toc144362930)](#_Toc144362940)         | [[IFC Requests](#_Toc144362930)](#_Toc144362940)                                       |
| [[IP](#_Toc144362930)](#_Toc144362940)          | [[IFC Requests By Patient](#_Toc144362930)](#_Toc144362940)                            |
| [[IR](#_Toc144362930)](#_Toc144362940)          | [[IFC Requests by Remote Ordering Provider](#_Toc144362930)](#_Toc144362940)           |
| [[NU](#_Toc144362930)](#_Toc144362940)          | [[Service Consults with Consults Numbers](#_Toc144362930)](#_Toc144362940)             |
| [[PI](#_Toc144362930)](#_Toc144362940)          | [[Print IFC Requests](#_Toc144362930)](#_Toc144362940)                                 |
| [[PL](#_Toc144362930)](#_Toc144362940)          | [[Print Consults by Provider, Location, or Procedure](#_Toc144362930)](#_Toc144362940) |
| [[PM](#_Toc144362930)](#_Toc144362940)          | [[Consult Performance Monitor Report](#_Toc144362930)](#_Toc144362940)                 |
| [[PR](#_Toc144362930)](#_Toc144362940)          | [[Print Service Consults by Status](#_Toc144362930)](#_Toc144362940)                   |
| [[SC](#_Toc144362930)](#_Toc144362940)          | [[Service Consults By Status](#_Toc144362930)](#_Toc144362940)                         |
| [[TS](#_Toc144362930)](#_Toc144362940)          | [[Print Completion Time Statistics Report](#_Toc144362930)](#_Toc144362940)            |
| [[SS](#_Toc144362930)](#_Toc144362940)          | [[Set up Consult Services](#_Toc144362930)](#_Toc144362940)                            |
| [[SU](#_Toc144362930)](#_Toc144362940)          | [[Service User Management](#_Toc144362930)](#_Toc144362940)                            |
| [[CS](#_Toc144362930)](#_Toc144362940)          | [[Consult Service Tracking](#_Toc144362930)](#_Toc144362940)                           |
| [[RX](#_Toc144362930)](#_Toc144362940)          | [[Pharmacy TPN Consults](#_Toc144362930)](#_Toc144362940)                              |
| [[TP](#_Toc144362930)](#_Toc144362940)          | [[Print Test Page](#_Toc144362930)](#_Toc144362940)                                    |
| [[GU](#_Toc144362930)](#_Toc144362940)          | [[Group update of consult/procedure requests](#_Toc144362930)](#_Toc144362940)         |
| [[UA](#_Toc144362930)](#_Toc144362940)          | [[Determine users' update authority](#_Toc144362930)](#_Toc144362940)                  |
| [[UN](#_Toc144362930)](#_Toc144362940)          | [[Determine if user is notification recipient](#_Toc144362930)](#_Toc144362940)        |
| [[NR](#_Toc144362930)](#_Toc144362940)          | [[Determine notification recipients for a service](#_Toc144362930)](#_Toc144362940)    |
| [[TD](#_Toc144362930)](#_Toc144362940)          | [[Test Default Reason for Request](#_Toc144362930)](#_Toc144362940)                    |
| [[LH](#_Toc144362930)](#_Toc144362940)          | [[List Consult Service Hierarchy](#_Toc144362930)](#_Toc144362940)                     |
| [[PR](#_Toc144362930)](#_Toc144362940)          | [[Setup procedures](#_Toc144362930)](#_Toc144362940)                                   |
| [[CP](#_Toc144362930)](#_Toc144362940)          | [[Copy Prosthetics services](#_Toc144362930)](#_Toc144362940)                          |
| [[CCT](#_Toc144362930)](#_Toc144362940)         | [[Menu for Closure Tools…](#_Toc144362930)](#_Toc144362940)                            |
| [[EDT](#_Toc144362930)](#_Toc144362940)         | [[Consult Closure Tool Edit Configuration](#_Toc144362930)](#_Toc144362940)            |
| [[INQ](#_Toc144362930)](#_Toc144362940)         | [[Consult Closure Tool Inquire Configuration](#_Toc144362930)](#_Toc144362940)         |
| [[RUN](#_Toc144362930)](#_Toc144362940)         | [[Consult Closure Tool Run Configuration](#_Toc144362930)](#_Toc144362940)             |
| [[DS](#_Toc144362930)](#_Toc144362940)          | [[Duplicate Sub-Service](#_Toc144362930)](#_Toc144362940)                              |
| [[FS](#_Toc144362930)](#_Toc144362940)          | [[Define Fee Services](#_Toc144362930)](#_Toc144362940)                                |
| [[IFC](#_Toc144362930)](#_Toc144362940)         | [[IFC Management Menu](#_Toc144362930)](#_Toc144362940)                                |
| [[TI](#_Toc144362930)](#_Toc144362940)          | [[Test IFC implementation](#_Toc144362930)](#_Toc144362940)                            |
| [[LI](#_Toc144362930)](#_Toc144362940)          | [[List incomplete IFC transactions](#_Toc144362930)](#_Toc144362940)                   |
| [[IFC](#_Toc144362930)](#_Toc144362940)         | [[IFC Requests](#_Toc144362930)](#_Toc144362940)                                       |
| [[TR](#_Toc144362930)](#_Toc144362940)          | [[IFC Transaction Report](#_Toc144362930)](#_Toc144362940)                             |
| [[LK](#_Toc144362930)](#_Toc144362940)          | [[Locate IFC by Remote Cslt \#](#_Toc144362930)](#_Toc144362940)                       |
| [[BK](#_Toc144362930)](#_Toc144362940)          | [[Monitor IFC background job parameters](#_Toc144362930)](#_Toc144362940)              |
| [[EC](#_Toc144362930)](#_Toc144362940)          | [[IFC Possible Erroneous Comment Report](#_Toc144362930)](#_Toc144362940)              |
| [[IP](#_Toc144362930)](#_Toc144362940)          | [[IFC Requests By Patient](#_Toc144362930)](#_Toc144362940)                            |
| [[IR](#_Toc144362930)](#_Toc144362940)          | [[IFC Requests by Remote Ordering Provider](#_Toc144362930)](#_Toc144362940)           |
| [[PI](#_Toc144362930)](#_Toc144362940)          | [[Print IFC Requests](#_Toc144362930)](#_Toc144362940)                                 |

[[To get you started placing “CONSULT...” orders via CPRS, the option above which requires immediate attention is the Set up Consult Services (SS) option. Before setting up services, you should define your service hierarchy and determine service functionality.](#_Toc144362930)](#_Toc144362940)

[[Whenever a value is defined for the SERVICE USAGE field in the Set up Consults Services \[GMRC SETUP REQUEST SERVICES\] option, the Service entry will NOT be selectable to send consults to in the CPRS ordering process. Instead, entries in this field reserve the service for special uses within the Consults flow of information.](#_Toc144362930)](#_Toc144362940)

[[Service Usages cause functioning as follows:](#_Toc144362930)](#_Toc144362940)

- 
- 
- 
- 

| [[Functionality Enabled](#_Toc144362934)](#_Toc144362940)                                                                                                                                            | [[Related Fields That May Be Completed](#_Toc144362934)](#_Toc144362940) | [[Related Fields That May be Completed](#_Toc144362934)](#_Toc144362940)        |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| [[Feature](#_Toc144362934)](#_Toc144362940)                                                                                                                                                          | [[Field \#](#_Toc144362934)](#_Toc144362940)                             | [[Field Name](#_Toc144362934)](#_Toc144362940)                                  |
|                                                                                                                                                                                                      |                                                                          |                                                                                 |
| [[Ordering consults from the "ALL SERVICES" hierarchy in CPRS and Review of Consults via the Consults options distributed to users.](#_Toc144362934)](#_Toc144362940)                                | [[.01](#_Toc144362934)](#_Toc144362940)                                  | [[NAME](#_Toc144362934)](#_Toc144362940)                                        |
|                                                                                                                                                                                                      | [[2](#_Toc144362934)](#_Toc144362940)                                    | [[SERVICE USAGE](#_Toc144362934)](#_Toc144362940)                               |
|                                                                                                                                                                                                      | [[10](#_Toc144362934)](#_Toc144362940)                                   | [[SUB-SERVICE/SPECIALTY (multiple)](#_Toc144362934)](#_Toc144362940)            |
| [[Automatic print of a Consultation Form (SF 513) at the service receiving the consult when CPRS order entry releases the order.](#_Toc144362934)](#_Toc144362940)                                   | [[123.09](#_Toc144362934)](#_Toc144362940)                               | [[SERVICE PRINTER](#_Toc144362934)](#_Toc144362940)                             |
| [[Service/Specialty update of Consults activity with automatic notification to the requesting service and to the original requester of the order upon resolution.](#_Toc144362934)](#_Toc144362940)  | [[.06](#_Toc144362934)](#_Toc144362940)                                  | [[UNRESTRICTED ACCESS](#_Toc144362934)](#_Toc144362940)                         |
|                                                                                                                                                                                                      | [[123.03](#_Toc144362934)](#_Toc144362940)                               | [[NOTIFY SERVICE ON DC](#_Toc144362934)](#_Toc144362940)                        |
|                                                                                                                                                                                                      | [[123.04](#_Toc144362934)](#_Toc144362940)                               | [[SERVICE INDIVIDUAL TO NOTIFY](#_Toc144362934)](#_Toc144362940)                |
|                                                                                                                                                                                                      | [[123.08](#_Toc144362934)](#_Toc144362940)                               | [[SERVICE TEAM TO NOTIFY (multiple)](#_Toc144362934)](#_Toc144362940)           |
|                                                                                                                                                                                                      | [[123.1](#_Toc144362934)](#_Toc144362940)                                | [[UPDATE USERS W/O NOTIFICATIONS (multiple)](#_Toc144362934)](#_Toc144362940)   |
|                                                                                                                                                                                                      | [[123.3](#_Toc144362934)](#_Toc144362940)                                | [[UPDATE TEAMS W/O NOTIFICATIONS (multiple)](#_Toc144362934)](#_Toc144362940)   |
| [[Service/Specialty update of Consults activity with automatic notification to the requesting service and to the original requester of the order upon resolution.](#_Toc144362934)](#_Toc144362940)  | [[123.35](#_Toc144362934)](#_Toc144362940)                               | [[UPDATE USER CLASSES W/O NOTIFS (multiple)](#_Toc144362934)](#_Toc144362940)   |
| [[Automatic notification to service individuals or teams when CPRS releases the order. Assuming these users have the "NEW SERVICE CONSULT" notification turned on.](#_Toc144362934)](#_Toc144362940) | [[123.08](#_Toc144362934)](#_Toc144362940)                               | [[SERVICE INDIVIDUAL TO NOTIFY](#_Toc144362934)](#_Toc144362940)                |
|                                                                                                                                                                                                      | [[123.1](#_Toc144362934)](#_Toc144362940)                                | [[SERVICE TEAM(S) TO NOTIFY (multiple)](#_Toc144362934)](#_Toc144362940)        |
|                                                                                                                                                                                                      | [[123.2](#_Toc144362934)](#_Toc144362940)                                | [[NOTIFICATION BY PATIENT LOCATION (multiple)](#_Toc144362934)](#_Toc144362940) |
| [[Ability to administratively complete consults, either singly or by date range.](#_Toc144362934)](#_Toc144362940)                                                                                   | [[123.33](#_Toc144362934)](#_Toc144362940)                               | [[ADMINISTRATIVE UPDATE USER (multiple)](#_Toc144362934)](#_Toc144362940)       |
|                                                                                                                                                                                                      | [[123.34](#_Toc144362934)](#_Toc144362940)                               | [[ADMINISTRATIVE UPDATE TEAM (multiple)](#_Toc144362934)](#_Toc144362940)       |
|                                                                                                                                                                                                      | [[123.5](#_Toc144362934)](#_Toc144362940)                                | [[SPECIAL UPDATES INDIVIDUAL](#_Toc144362934)](#_Toc144362940)                  |
| [[Ability to administratively complete consults, either singly or by date range.](#_Toc144362934)](#_Toc144362940)                                                                                   | [[123.33](#_Toc144362934)](#_Toc144362940)                               | [[ADMINISTRATIVE UPDATE USER (multiple)](#_Toc144362934)](#_Toc144362940)       |
|                                                                                                                                                                                                      | [[123.34](#_Toc144362934)](#_Toc144362940)                               | [[ADMINISTRATIVE UPDATE TEAM (multiple)](#_Toc144362934)](#_Toc144362940)       |
|                                                                                                                                                                                                      | [[123.5](#_Toc144362934)](#_Toc144362940)                                | [[SPECIAL UPDATES INDIVIDUAL](#_Toc144362934)](#_Toc144362940)                  |
| [[Inter-Facility Service Configuration.](#_Toc144362934)](#_Toc144362940)                                                                                                                            | [[123.5134](#_Toc144362934)](#_Toc144362940)                             | [[IFC ROUTING SITE](#_Toc144362934)](#_Toc144362940)                            |
| [[IFC REMOTE NAME](#_Toc144362934)](#_Toc144362940)                                                                                                                                                  |                                                                          |                                                                                 |
| [[IFC SENDING FACILITY](#_Toc144362934)](#_Toc144362940)                                                                                                                                             |                                                                          |                                                                                 |
| [[IFC COORDINATOR](#_Toc144362934)](#_Toc144362940)                                                                                                                                                  |                                                                          |                                                                                 |
| [[Secondary Consult Service Printer for Consultation Form (SF 513)](#_Toc144362934)](#_Toc144362940)                                                                                                 | [[689](#_Toc144362934)](#_Toc144362940)                                  | [[SECONDARY PRINTER](#_Toc144362934)](#_Toc144362940)                           |

[[  
](#_Toc144362934)](#_Toc144362940)

[[The Set Up Consult Services command creates and maintains new records in the REQUEST SERVICES (#123.5) file. The following fields are involved:](#_Toc144362934)](#_Toc144362940)

- 
- 
- 
- 
- - 
  - 
  - 
  - 
  - 
  - 
  - 
  - 
  - 
  - 
  - 
  - 
  - - 
    - 
    - 
- 
- 

> [[SERVICE NAME: This is the Name of a service or specialty which may receive consult/requests. This may also be a name which represents a group of services or specialties.ABBREVIATED PRINT NAME: This is a commonly known Abbreviation for this Service/Specialty. This name is used to build Consult Notifications and must be 7 characters or less in length.INTERNAL NAME: This is an alternate name for the service. This name does not appear on printouts or displays but can be used to access the service through the Setup Services (SS) option, or with FileMan.SYNONYM: Identifies the commonly known names and abbreviations for the Service named in the .01 Name field. Synonyms identified here are used in the look-up of services at “Select Service/Specialty:” prompts as well as during ordering in CPRS.SERVICE USAGE: Whenever a value is defined in the SERVICE USAGE field, the Service entry will NOT be selectable to send consults TO in the OE/RR ordering process. Service Usages cause functioning as follows:GROUPER ONLY: Allows a service to be used for grouping other services together for review purposes, and aids in defining the service hierarchy (e.g., ALL SERVICES, INPATIENT SERVICES, OUTSIDE SERVICES). During the order process, a user selecting a grouper only service will be shown the service hierarchy under that service grouper. A Grouper ONLY service should never be a "TO" Service on a consult.TRACKING ONLY: Allows a service to be defined in a hierarchy but will not allow users ordering consults in OE/RR to be able to see or select a service marked for TRACKING ONLY. (e.g., Psychology may be defined with its Service Usage blank, and its Sub-specialty multiple defined with services of which some or all may be "TRACKING ONLY" services. This hierarchy facilitates the situation when a service, such as Psychology, prefers a common location for all related consults to be sent to. A Tracking user at the common location then "Forwards" the request to one of the sub-service TRACKING ONLY services for completion.) Update users for the service can see and order directly to a tracking service.DISABLED: Disabled services are not selectable for ordering or tracking. Existing requests for a disabled service may still be processed to completion.SERVICE PRINTER: Allows the service/specialty to identify a device that will be used for printing Consult Forms (SF 513) 'automatically' at the service when the consult/request order is released by CPRS. If the device is not defined, the Consult Form will not print unless a default service copy device is defined for the Consults package for the ordering location. The default service copy device parameter can be found by using the Print Parameters for Wards/Clinics \[OR PARAM PRINTS (LOC)\] option.SECONDARY PRINTER: Allows the service/specialty to identify a secondary printer device that will be used for printing Consult Forms (SF 513) at a second location when the consult/request order is released by CPRS and during any print request for SF 513.NOTIFY SERVICE ON DC: Controls when members configured to receive notifications for this service in the Consult hierarchy will be alerted to a consult being discontinued. This field can be set to ALWAYS, NEVER, or REQUESTOR ACTION. REQUESTOR ACTION stipulates notification only if the user discontinuing the consult is not an update user for the consulting service.REPRINT 513 ON DC: This field will determine if the SF 513 should reprint to the consulting service when a consult is discontinued. Again, the three choices are ALWAYS, NEVER, or REQUESTOR ACTION. REQUESTOR ACTION stipulates reprinting only if the user discontinuing the consult is not an update user for the consulting service.PROVISIONAL DX PROMPT: Used by CPRS to determine how to prompt for the provisional diagnosis when ordering consults for this service. If this field is set to OPTIONAL, the user will be prompted for the provisional diagnosis but may bypass answering the prompt. If the field is set to SUPPRESS, the user will not be presented with the provisional diagnosis prompt. If set to REQUIRED, the user must answer the prompt to continue placing the order.PROVISIONAL DX INPUT: Determines the method that CPRS uses to prompt the user for input of the provisional diagnosis when ordering a consult. If set to FREE TEXT, the user may type any text from 2-80 characters in length. If set to LEXICON, the user will be required to select a coded diagnosis from the Clinical Lexicon.PREREQUISITE: This word-processing field is utilized to communicate pre-requisite information to the ordering person prior to ordering a consult to this service. This field is presented to the ordering person upon selecting a Consult service and allows them to abort the ordering at that time if they choose. TIU objects may be embedded within this field which are resolved for the current patient during ordering. Any TIU objects must be contained within vertical bars (e.g. \|BLOOD PRESSURE\|).DEFAULT REASON FOR REQUEST: The default text used as the reason for request when ordering a consult for this service. This field allows a boilerplate of text to be imported into the reason for request when placing consult orders for this service. If the user places an order using a quick order having boilerplate text, that text supersedes any default text stored in this field. This field may contain any text including TIU objects. TIU Objects must be enclosed in vertical bars (e.g. \|PATIENT NAME\|).RESTRICT DEFAULT REASON EDIT: If a DEFAULT REASON FOR REQUEST exists for this service this field effects the ordering person's ability to edit the default reason while placing an order. This variable can be set to UNRESTRICTED, NO EDITING, or ASK ON EDIT ONLY. If the third value, ASK ON EDIT ONLY, is used, the user is only allowed to edit the default reason if the order is edited before releasing to the service.The following three fields are only filled in if this is an Inter-Facility consult. The first two are used if you are a requesting facility. The third, IFC SENDING FACILITY, is used if you are a consulting facility.IFC ROUTING SITE: This field contains the VA facility that will perform consults requested for this service. When a consult for this service is ordered, it will automatically be routed to the VA facility in this field.IFC REMOTE NAME: This field contains the name of the service that will be requested at the VAMC defined in the IFC ROUTING SITE field. Enter the name of the service exactly as it is named at the remote facility. If this name does not match the name of the service at the routing site, the request will fail to be filed at the remote site. This will delay or prohibit the performance and processing of this request.IFC SENDING FACILITY: This is a multiple containing the facilities from which your site may receive Inter-Facility Consults for this consult. As with all IFC fields, they must be an exact match.SERVICE INDIVIDUAL TO NOTIFY: A user may be identified in this field as having primary responsibility for receiving consults and tracking them through to completion or discontinuance. This individual will receive a "NEW SERVICE CONSULT" notification type when a new order is released to the service through CPRS. The user must have the "NEW SERVICE CONSULT/REQUEST" notification type enabled.SERVICE TEAM TO NOTIFY: The name of the Service Team that is to receive notifications of actions taken on a consult. A team of users may be identified (from the OE/RR LIST file \#100.21) who will receive a "NEW SERVICE CONSULT" notification when a new order is released to the service through OE/RR. The individuals on the teams must have the "NEW SERVICE CONSULT/REQUEST" notification type turned "ON". Team members will be able to perform update tracking capabilities.Note: The service team does not receive the CONSULT/REQUEST UPDATED notification if another member of that team or an update user is the user adding the comment. (Remedy Ticket 903302 pointed this out.)](#_Toc144362934)](#_Toc144362940)

- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 
- 

[[  
](#_Toc144361798)](#_Toc144362940)

[[  
](#_Toc144361799)](#_Toc144362940)

[[Use the following steps to send a consult to HCPS or to CCRA:](#_Toc144361799)](#_Toc144362940)

1.  
2.  
3.  

> [[Select SS Set Up Consult Services.Set up a new consult service that contains ‘NON VA CARE HCPS’ (e.g., NON VA CARE HCPS HEMODIALYSIS). Note that the service name must contain “NON VA CARE HCPS” as the prefix in order to be processed by HCPS. This naming convention was created to adhere to existing Non VA Care (NVC) naming and reporting standards. All NVC services begin with “NON VA CARE”. “HCPS” was also added to identify the transactions that will be sent to HCPS. All services that are intended to be sent to HCPS must contain “HCPS” after “NON VA CARE” (e.g., NON VA CARE HCPS…). To send consults to CCRA, the consult service needs to begin with “COMMUNITY CARE-“. This exact naming will allow the system to transfer community care consults to CCRA’s HealthShare Referral Manager (HSRM) application. Similarly, for DOD, the service name needs to begin with “DOD TREATMENT”.When setting up a community care consult service, you will be prompted to enter a community care clinic to use when making an appointment. When editing or entering a community care consult service, you will be prompted with the following:SELECT HOSPITAL LOCATION NAME: This field is only displayed if the consult service is for a community care consult. If entering or editing a community care consult, select a community care clinic that will be used when scheduling appointments.](#_Toc144361799)](#_Toc144362940)

4.  
5.  

[[Associate the new consult service with the appropriate template.When the template is selected from the Order a Consult screen, it will be routed to HCPS once filled out and accepted.  
](#_Toc144361799)](#_Toc144362940)

1.  
2.  

[[  
](#_Toc144361801)](#_Toc144362940)

[[<span id="_Toc169170022" class="anchor"></span>Figure 5‑7: Quick Order Example (continued)](#_Toc144361801)](#_Toc144362940)

[[![](consult-request-tracking-technical-manual-gmrc-3-0-189/009.png)](#_Toc144361802)](#_Toc144362940)

[[  
](#_Toc144361802)](#_Toc144362940)

[[  
](#_Toc144361803)](#_Toc144362940)

[[This option is used to make the most needed changes after a service has been created. This option changes fields that are all in records in the REQUEST SERVICES (#123.5) file. They include the following:](#_Toc144361803)](#_Toc144362940)

- 
- 

> [[SERVICE INDIVIDUAL TO NOTIFY: An individual who will receive a default notification of any action taken on a consult.SERVICE TEAM TO NOTIFY: The name of the Service Team that is to receive notifications of any actions taken on a consult.Note: The service team does not receive the CONSULT/REQUEST UPDATED notification if another member of that team or an update user is the user adding the comment. (Remedy Ticket 903302 pointed this out.)](#_Toc144361803)](#_Toc144362940)

- 
- 
- 
- 
- 
- 
- 

[[  
](#_Toc144361803)](#_Toc144362940)

- 
- 
- 
- 
- 
- 
- 

> [[SERVICE INDIVIDUAL TO NOTIFYSERVICE TEAM TO NOTIFYNOTIFICATION BY PT LOCATIONNOTIFICATION BY PT LOCATION, INDIVIDUAL and/or TEAMUPDATE USERS W/O NOTIFICATIONSUPDATE TEAMS W/O NOTIFICATIONSUPDATE USER CLASS W/O NOTIFS](#_Toc144361806)](#_Toc144362940)

[[  
](#_Toc144361807)](#_Toc144362940)

[[  
](#_Toc144361809)](#_Toc144362940)

[[A Group Update can only be performed by an individual who has been set as the Special Updates Individual with the Set Up Consult Service (SS) or Service User Management (SU) option of the Consult Management (GMRC MGR) menu. This option should be exercised with great care because it can affect a large number of consults.](#_Toc144361809)](#_Toc144362940)

[[Refer to Figures 5-15 and 5-16. In this example, all consults before the first of the year that are not complete are discontinued for a specific service:](#_Toc144361809)](#_Toc144362940)

[[  
](#_Toc144361809)](#_Toc144362940)

[[<span id="_Toc169170030" class="anchor"></span>Figure 5‑15: Discontinued Service End-of-Year Consults Example](#_Toc144361809)](#_Toc144362940)

[[![](consult-request-tracking-technical-manual-gmrc-3-0-189/017.png)](#_Toc144361810)](#_Toc144362940)

[[  
](#_Toc144361810)](#_Toc144362940)

[[  
](#_Toc144361812)](#_Toc144362940)

[[This report was added with Consults patch GMRC\*3\*41 to satisfy performance monitor reporting requirements of the Veterans Integrated Service Network (VISN) Support Services Center (VSSC). For FY08, the VHA Deputy Undersecretary for Health for Operations and Management has published updates to the monitor definitions, and patch GMRC\*3.](#_Toc144361812)[0\*60 implements those updates.](#_Toc144362940)](#_Toc144362940)

- 
- 
- 
- 

[[  
](#_Toc144361814)](#_Toc144362940)

[[This provides three different reports under one menu option \[GMRC PRINT BY SEARCH\]. The option asks for search criteria: Sending Provider, Location, or Procedure. You can further limit the search by entering a date range and CPRS status. The option also prompts for report format. The report format can be one of the following:](#_Toc144361815)](#_Toc144362940)

- 
- 
- 

[[  
](#_Toc144361816)](#_Toc144362940)

[[<span id="_Toc169170037" class="anchor"></span>Figure 5‑22: EKG Consult Generation Example (continued)](#_Toc144361816)](#_Toc144362940)

[[![](consult-request-tracking-technical-manual-gmrc-3-0-189/024.png)](#_Toc144361817)](#_Toc144362940)

[[  
](#_Toc144361818)](#_Toc144362940)

[[  
](#_Toc144361821)](#_Toc144362940)

| [[Object Name](#_Toc144361821)](#_Toc144362940)                   | [[Object Name](#_Toc144361821)](#_Toc144362940)          |
|-------------------------------------------------------------------|----------------------------------------------------------|
| [[ACTIVE MEDICATIONS](#_Toc144361821)](#_Toc144362940)            | [[PATIENT HEIGHT](#_Toc144361821)](#_Toc144362940)       |
| [[ACTIVE MEDICATIONS](#_Toc144361821)](#_Toc144362940)            | [[PATIENT NAME](#_Toc144361821)](#_Toc144362940)         |
| [[ACTIVE MEDS COMBINED](#_Toc144361821)](#_Toc144362940)          | [[PATIENT RACE](#_Toc144361821)](#_Toc144362940)         |
| [[ALLERGIES/ADR](#_Toc144361821)](#_Toc144362940)                 | [[PATIENT RELIGION](#_Toc144361821)](#_Toc144362940)     |
| [[BLOOD PRESSURE](#_Toc144361821)](#_Toc144362940)                | [[PATIENT SEX](#_Toc144361821)](#_Toc144362940)          |
| [[CURRENT ADMISSION](#_Toc144361821)](#_Toc144362940)             | [[PATIENT SSN](#_Toc144361821)](#_Toc144362940)          |
| [[DETAILED ACTIVE MEDS](#_Toc144361821)](#_Toc144362940)          | [[PATIENT WEIGHT](#_Toc144361821)](#_Toc144362940)       |
| [[DETAILED RECENT MEDS](#_Toc144361821)](#_Toc144362940)          | [[PULSE](#_Toc144361821)](#_Toc144362940)                |
| [[NOW](#_Toc144361821)](#_Toc144362940)                           | [[RECENT MEDICATIONS](#_Toc144361821)](#_Toc144362940)   |
| [[PAIN](#_Toc144361821)](#_Toc144362940)                          | [[RECENT MEDS COMBINED](#_Toc144361821)](#_Toc144362940) |
| [[PATIENT AGE](#_Toc144361821)](#_Toc144362940)                   | [[RESPIRATION](#_Toc144361821)](#_Toc144362940)          |
| [[PATIENT DATE OF BIRTH](#_Toc144361821)](#_Toc144362940)         | [[TEMPERATURE](#_Toc144361821)](#_Toc144362940)          |
| [[PATIENT DATE OF DEATH+ Status](#_Toc144361821)](#_Toc144362940) | [[TODAY'S DATE](#_Toc144361821)](#_Toc144362940)         |

[[Further information about objects can be obtained at the following VA intranet address: REDACTED.](#_Toc144361821)](#_Toc144362940)

[[Refer to Figure 5-27. In the following example, we first use the SS option to enter a default reason for request as such.](#_Toc144361821)](#_Toc144362940)

[[  
](#_Toc144361821)](#_Toc144362940)

[[The Copy Prosthetics Services option of the Consult Management menu is provided to assist you in configuring the prosthetics services at your medical center. . . .](#_Toc144361824)](#_Toc144362940)

[[The four (4) nationally exported services for Prosthetics include:](#_Toc144361824)](#_Toc144362940)

- 
- 
- 
- 
- 
- 
- 
- 
1.  
2.  

[[  
](#_Toc144361825)](#_Toc144362940)

[[The Consult Closure Tool provides options to identify consult requests that are incorrectly left in Pending status and efficiently closes out those consults. Search parameters can be configured in the tool, providing a list that allows you to close out consults by attaching a relevant note within the tool. There are also options to export the search results from the tool to a printable format and update a team list in CPRS.](#_Toc144361825)](#_Toc144362940)

[[The VistA Consult Closure tool consists of three components:](#_Toc144361825)](#_Toc144362940)

- 
- 
- 

[[Edit Configuration: Enables the user to configure the tool to identify pending consults based on search parameters, including clinics, orders, consult services, and procedures. The user also selects relevant note titles to use in closing pending consults. One or more valid configurations must be created prior to using the Run Configuration option.Inquire Configuration: Enables the user to print and view the configuration to ensure that it is set up properly. Run Configuration: Enables the user to select eligible note titles to close an open consult, perform the closure action, and/or create team lists that are viewable in CPRS.](#_Toc144361825)](#_Toc144362940)

[[The Consult Closure Tool is located in the GMRC MGR menu. This menu is normally allocated to IRMS/ADPAC personnel.](#_Toc144361825)](#_Toc144362940)

1.  
2.  

[[Navigate to the GMRC MGR menu option.Type “CCT” to open the Menu for Closure Tools.](#_Toc144361825)](#_Toc144362940)

[[The following options appear:](#_Toc144361825)](#_Toc144362940)

- 
- 
- 

[[EDT Consult Closure Tool Edit ConfigurationNQ Consult Closure Tool Inquire ConfigurationRUN Consult Closure Tool Run Configuration](#_Toc144361825)](#_Toc144362940)

[[The first step is to set up the configuration(s) using the Consult Closure Tool Edit Configuration menu option.](#_Toc144361825)](#_Toc144362940)

[[The key points when setting up a Consult Closure configuration include:](#_Toc144361825)](#_Toc144362940)

- 
- 
- 
- 
1.  
2.  
3.  
4.  
5.  
6.  
7.  
8.  
9.  
10. 
11. 
12. 
13. 
14. 
15. 

[[In the GMRC MGR menu, type "CCT" and then press Enter to open the Menu for Closure Tools. Type "EDT" and then press Enter.At the initial Consult Closure Tool Edit Configuration prompt, enter the new or existing configuration name. For a new configuration, type “Yes” when asked if you want to add this as a new consult configuration. Press Enter. The Configuration Editor screen opens with the Config Name field highlighted and editable.In the Days Cons -\> Apt field, enter the maximum number of days between the date of the consult entry and the clinic appointment. The tool will search for pending consults that fall within this time period. A shorter interval will make the tool run faster. In the CPRS Team field, enter the name of the CPRS team that will be populated when this configuration is run. The team must already exist.In the Days Appt -\> Note field, enter the maximum number of days between the clinic appointment date and the date of the eligible note that can be associated with the consult in the Run Configuration option. In the Inactive field, enter NO (the default option) to make this configuration active. If a configuration is marked inactive, it is not selectable when running the Consult Closure Tool. It is still selectable in the Edit and Inquire options. (optional) In the Consults - Service field, enter the name(s) of the consult service(s) to be used as search parameters. (optional) In the Consults - Procedure field, enter the Procedure(s) to be used as search parameters. The Consults-Procedure field is for Medicine package procedure requests that do not use the Clinical Procedure (CP) interface. (optional) In the Consults – Order Item field, enter specific orderable item(s) to be used as search parameters. (optional) In the Consults – Clinical Procedure field, enter the Clinical Procedure(s) to be used as search parameters. In the Clinics field, enter the Clinics to be used as search parameters. In lieu of entering individual clinics, you can enter the relevant Stop Code(s) to capture all associated clinics if they have already been correctly mapped in VistA. Adding more clinics broadens your search (operating as a Boolean "OR"), as the patient only has to be associated with one of them for their consult request to be returned when running the configuration. In the Note Titles field, enter all eligible note titles to be associated with pending consults during Run Configuration. Define an appropriately comprehensive set of note titles, but be aware that an overly broad list might result in a higher likelihood of incorrect association with a pending consult. This step is key as it allows non-consult class TIU documents that have been completed subsequent to a consult request to be associated with the consult, thus converting that pending consult’s status to Completed. Press \<PF1\>E to save and exit. This returns you to the CCT menu. For a complete list of help options, press \<PF1\>H.If the configuration is incomplete, you are notified when saving the configuration. Once the search configuration is completed, you are able to run a report using the Run Configuration option.](#_Toc144361826)](#_Toc144362940)

[[  
](#_Toc144361826)](#_Toc144362940)

[[Once a configuration is created, it can be viewed and printed using the Consult Closure Tool Inquire Configuration menu option. This option is useful for verifying that the configuration is set up properly. At the Menu for Closure Tools, type "INQ" to view the configuration information.](#_Toc144361826)](#_Toc144362940)

[[  
](#_Toc144361827)](#_Toc144362940)

[[To run a configuration:](#_Toc144361827)](#_Toc144362940)

1.  
2.  
3.  
4.  
5.  
6.  
7.  

[[  
](#_Toc144361827)](#_Toc144362940)

- 
- 
- 

[[  
](#_Toc144361828)](#_Toc144362940)

[[Consult closure for patient: CPRSPatient,One 09/25/1933  
MEDICAL SERVICE OTHER (p) 11/12/2010](#_Toc144361829)](#_Toc144362940)

[[Select the note to close the consult ](#_Toc144361829)](#_Toc144362940)

> [[0 - Do not close the consult ](#_Toc144361829)](#_Toc144362940)

> [[1 - Note 01: 10-10ED EMERGENCY DEPARTMENT NOTE ](#_Toc144361829)](#_Toc144362940)

> [[2 - Redisplay the consult/progress note(s)](#_Toc144361829)](#_Toc144362940)

> [[^ - Exit the Consult Closure Tool ](#_Toc144361829)](#_Toc144362940)

[[Select NOTE TO CLOSE CONSULT: 2//.](#_Toc144361829)](#_Toc144362940)

[[In the Consult closure screen (pictured above), you can select from the following options: a) Do not close the consult, b) Close the consult with one of the identified notes, c) Return to the consult/note display screen for further review, or d) Exit the Consult Closure Tool. If you select option a), then no action is taken on the consult and the tool automatically displays the next consult. If you select option b), then the tool closes the consult with the selected note and automatically displays the next patient’s Consult Narrative. This process continues until all consults are processed or you exit the Consult Closure Tool.](#_Toc144361829)](#_Toc144362940)

[[The Duplicate Sub-Service option of the Consult Management menu is provided to assist you in debugging your service hierarchy. It displays services that are listed as a sub-service of more than one service. Having a service as a sub-service of more than one service has several undesirable effects. These include:](#_Toc144361830)](#_Toc144362940)

1.  
2.  

[[Reports that span more than one level of the hierarchy inaccurately report statistics.Notification recipients may be inaccurately determined.  
](#_Toc144361830)](#_Toc144362940)

[[The Inter-Facility Consults reports are available on the Consult Tracking Reports menu \[GMRC REPORTS\] and the IFC Management Menu \[GMRC IFC MGMT\]. Currently four Inter-Facility Consults reports show up on this menu. Refer to Table 5-4.](#_Toc144361834)](#_Toc144362940)

[[<span id="_Toc169170348" class="anchor"></span>Table 5‑4: Inter-Facility Consults Report Descriptions](#_Toc144361834)](#_Toc144362940)

| [[Report Synonym](#_Toc144361834)](#_Toc144362940) | [[Report Name](#_Toc144361834)](#_Toc144362940)                              | [[Option Name](#_Toc144361834)](#_Toc144362940)                        |
|----------------------------------------------------|------------------------------------------------------------------------------|------------------------------------------------------------------------|
| [[IFC](#_Toc144361834)](#_Toc144362940)            | [[IFC Requests](#_Toc144361834)](#_Toc144362940)                             | [[\[GMRC IFC RPT CONSULTS\]](#_Toc144361834)](#_Toc144362940)          |
| [[IP](#_Toc144361834)](#_Toc144362940)             | [[IFC Requests by Patient](#_Toc144361834)](#_Toc144362940)                  | [[\[GMRC IFC RPT CONSULTS BY PT\]](#_Toc144361834)](#_Toc144362940)    |
| [[PI](#_Toc144361834)](#_Toc144362940)             | [[Print IFC Requests](#_Toc144361834)](#_Toc144362940)                       | [[\[GMRC IFC PRINT RPT NUMBERED\]](#_Toc144361834)](#_Toc144362940)    |
| [[IR](#_Toc144361834)](#_Toc144362940)             | [[IFC Requests by Remote Ordering Provider](#_Toc144361834)](#_Toc144362940) | [[\[GMRC IFC RPT CONSULTS BY REMPR\]](#_Toc144361834)](#_Toc144362940) |
| [[EC](#_Toc144361834)](#_Toc144362940)             | [[IFC Possible Erroneous Comment Report](#_Toc144361834)](#_Toc144362940)    | [[\[GMRC IFC ERR COMM RPT\]](#_Toc144361834)](#_Toc144362940)          |

[[This report provides such information as:](#_Toc144361834)](#_Toc144362940)

- 
- 
- 
- 

[[Total Requests to ServiceTotal Requests Scheduled to ServiceTotal Requests Completed to ServiceMean Days Completed to Service  
](#_Toc144361834)](#_Toc144362940)

[[  
](#_Toc144361835)](#_Toc144362940)

[[There are five actions you can do besides the default actions (like Next Screen, Previous Screen, Quit, \>, \<, …). These include the following:](#_Toc144361835)](#_Toc144362940)

- 
- 
- 
- 
- 

[[  
](#_Toc144361836)](#_Toc144362940)

[[  
](#_Toc144361837)](#_Toc144362940)

[[  
](#_Toc144361838)](#_Toc144362940)

[[  
](#_Toc144361839)](#_Toc144362940)

- 
- 
- 
- 
- 

[[Change Service: Change Service action allows you to re-display the report for a different service.Number on/off: Number on/off action changes the format of the report to include the consult number. To do this, it preserves the other columns but makes them narrower.Description of Data: Description of Data action gives a detailed description for applicable data columns.Status: Status action allows you to change which statuses are displayed in the report. In the following example the statuses displayed are changed from All Statuses to just the Pending, Active, and Scheduled consults.Print List: Displays the print list.  
](#_Toc144361840)](#_Toc144362940)

- 
- 
- 
- 

[[Note: The larger the selected time range the longer the report takes. It is not recommended to use large time ranges. Note: The total count found is at the top of the report and each instance found is numbered.](#_Toc144361841)](#_Toc144362940)

[[  
](#_Toc144361841)](#_Toc144362940)

[[To view the Possible Erroneous Comment Report in Excel:](#_Toc144361842)](#_Toc144362940)

1.  
2.  
3.  
4.  
5.  
6.  
7.  
8.  
9.  

[[The user must modify their terminal settings. Adjust the terminal settings to allow output to be as wide as possible (999 or max allowed characters). Copy and paste the report into a text editor (word, notepad, etc...) or output the report to a log .txt file. Combine all wrapped text lines into one field. Save the file.Open the file in Excel. Select Delimited with Headers, and then click Next\>. Select Other, enter \| in the text field, and then click Next\>.Locate the Data Preview box, select all text, and then click Finish. Manipulate the columns for display/wrap as desired.](#_Toc144361842)](#_Toc144362940)

[[A new GRMC Patch for “Admin Key Reporting” has been created to generate three (3) new GRMC Reports.](#_Toc144361842)](#_Toc144362940)

- 
- 
- 

[[Patch GMRC\*3.0\*110 has a post-install routine that does the following:](#_Toc144361842)](#_Toc144362940)

1.  
2.  

[[Reads the Station ID, extracts the first three characters (STA3N), and then updates the GMRC UNIQUE CONSULT SITE ID with this STA3N.Finds all consult records in file \#123 (REQUEST/CONSULTATION) that have an existing UCID, starting with 01/01/2018 and going forward, and changes the first three characters of that UCID to the ID constructed in step 1 above.](#_Toc144361842)](#_Toc144362940)

[[Patch GMRC\*3.](#_Toc144361842)[0\*110: When a user clicks on a Consult Order on the CPRS Orders tab, and right-clicks to show the Order Details, the display will now show the Unique Consult ID (UCID) which is in file \#123 (REQUEST/CONSULTATION) in field \#80 (UNIQUE CONSULT ID). The UCID is a tracking number used by Community Care.](#_Toc144362940)](#_Toc144362940)

[[The release of GMRC\*3.0\*154 adds three new components to the Interfacility Consults (IFC) system.](#_Toc144362940)](#_Toc144362940)

1.  
2.  
3.  

[[VDIF (Veterans Data Integration and Federation) integrationMPI Patient RegistrationCerner Mail Groups](#_Toc144362940)](#_Toc144362940)

[[When a facility has been “converted” to Cerner, it will be necessary for the Interfacility Consults (IFC) system to recognize that the HL7 message should no longer be routed to the VistA instance but should be routed to the VDIF (Veterans Data Integration and Federation) router. If the status of the treating facility is “converted”, the system will reference the Parameter GMRC IFC REGIONAL ROUTER file (#8989.5). This Parameter contains the Logical Link (GMRC IFC1 – GMRC IFC6) used to connect to one of the six VDIF (Veteran Data Integration and Federation) Regional Routers. The Logical Link will be substituted in the HL7 message in order to route the message to Cerner, rather than the VistA instance.](#_Toc144362940)](#_Toc144362940)

1.  
2.  

[[Check with MPI and retrigger the addReplay the consult message from VDIF](#_Toc144362930)](#_Toc144362940)

[[A “converted” facility is not able to process HL7 application negative acknowledgement (NAK) in the same manner as a “nonconverted” facility. Due to this technical limitation, four new mail groups (file \#3.](#_Toc144362930)[8) have been created to notify subscribers of application negative acknowledgements.](#_Toc144362940)](#_Toc144362940)

- 
- 
- 
- 

[[The release of GMRC\*3.0\*176 contains one modified routine, GMRCIACT, in the Interfacility Consults (IFC) system. The modification is as follows:](#_Toc144362940)](#_Toc144362940)

- 

[[When an Urgency of "Urgent" is picked in Cerner, ORC7.6 in the HL7 message contains an urgency code which is mapped to an entry in the PROTOCOL file (#101). When the field is equal to "S" meaning "STAT", this patch will change the urgency text to "NEXT AVAILABLE”.](#_Toc144362940)](#_Toc144362940)

[[  
](#_Toc144362940)](#_Toc144362940)

[[A new patch has been created that has several components as follows:](#_Toc144362940)](#_Toc144362940)

- 
- - 
  - 
  - 
- 
- 
- 

[[A new option, GMRC CHANGE STATUS X TO DC. This is not a user option; it is only present to facilitate the overnight job that converts consults from “Cancelled” to “Discontinued”.A new multi-valued parameter, CSLT CANCELLED TO DISCONTINUED, that contains three fields as follows:Is the overnight cancelled to discontinued job active?How many days back to start with?How many days back to end with?A new index called “ASTATUS” on file \#123 (REQUEST/CONSULTATION), field \#40 (REQUEST PROCESSING ACTIVITY), sub-fields \#.01 (DATE/TIME OF ACTION) and \#1 (ACTIVITY).A new entry in file \#19.2 (OPTION SCHEDULING), GMRC CHANGE STATUS X TO DC, which causes an overnight job to run which discontinues any consults that were cancelled within the day range specified in the second bullet in this list.A new menu option, GMRC CX TO DC PARAMETER EDIT, which allows a user to edit the parameter outlined in the second bullet in this list.](#_Toc144362940)](#_Toc144362940)

[[There are no new roll and scroll or GUI screens associated with this patch, but FileMan may be used as outlined below.](#_Toc144362940)](#_Toc144362940)

[[The GMRC CHANGE STATUS X TO DC overnight job is executed by TaskMan according to the schedule referred to in the OPTION SCHEDULING file as outlined in 4.](#_Toc144362940) [Above. It uses the new index referred to in 3 above to find consults that were cancelled in the date range (T-“days back to start with”) to (T-“days back to end with”), this processing being in reverse chronological order. Each consult fitting the parameter criteria is evaluated as to whether the consult was resubmitted and then cancelled again on a later date. If there is no later cancellation date, the consult is discontinued. Note that the overnight job is disabled when the patch is installed – the Is the overnight cancelled to discontinued job active? Parameter is set to NO.](#_Toc144362941)](#_Toc144362940)

[[A temporary file is used to log any consults that have been discontinued. The temporary file is set to be purged after 60 days.](#_Toc144362941)](#_Toc144362940)

[[  
](#_Toc144362941)](#_Toc144362940)

[[The new ASTATUS index is created during the installation of the patch. During a post-install process, it is necessary to add to the index all existing consult records in file \#123. In a production environment this could go into the millions. It is not advisable to do this in the foreground during the patch installation, so the job of doing this is transferred into the background using TaskMan.](#_Toc144362941)](#_Toc144362940)

[[The background job will pause periodically to avoid consuming system resources. The pause interval is set to 50,000 and resumes processing after a pause of 1800 (30 minutes).](#_Toc144362941)](#_Toc144362940)

[[  
](#_Toc144361843)](#_Toc144362940)

[[The Inter-Facility Consults Options \[GMRC IFC MGMT\] menu is part of the Consults Management \[GMRC MGR\] menu. Refer to Table 7-1, which lists the menu options available to the user.](#_Toc144361843)](#_Toc144362940)

[[<span id="_Toc169170349" class="anchor"></span>Table 7‑1: Inter-Facility Consults Management Menu Options](#_Toc144361843)](#_Toc144362940)

| [[Synonym](#_Toc144361843)](#_Toc144362940) | [[Name](#_Toc144361843)](#_Toc144362940)                                       | [[Command](#_Toc144361843)](#_Toc144362940)                            |
|---------------------------------------------|--------------------------------------------------------------------------------|------------------------------------------------------------------------|
| [[TI](#_Toc144361843)](#_Toc144362940)      | [[Test IFC implementation](#_Toc144361843)](#_Toc144362940)                    | [[\[GMRC IFC TEST SETUP\]](#_Toc144361843)](#_Toc144362940)            |
| [[LI](#_Toc144361843)](#_Toc144362940)      | [[List incomplete IFC transactions](#_Toc144361843)](#_Toc144362940)           | [[\[GMRC IFC INC TRANS\]](#_Toc144361843)](#_Toc144362940)             |
| [[IFC](#_Toc144361843)](#_Toc144362940)     | [[Inter-Facility Consult Requests](#_Toc144361843)](#_Toc144362940)            | [[\[GMRC IFC RPT CONSULTS\]](#_Toc144361843)](#_Toc144362940)          |
| [[TR](#_Toc144361843)](#_Toc144362940)      | [[IFC Transaction Report](#_Toc144361843)](#_Toc144362940)                     | [[\[GMRC IFC TRANS\]](#_Toc144361843)](#_Toc144362940)                 |
| [[LK](#_Toc144361843)](#_Toc144362940)      | [[Locate IFC by Remote Cslt \#](#_Toc144361843)](#_Toc144362940)               | [[\[GMRC IFC REMOTE NUMBER\]](#_Toc144361843)](#_Toc144362940)         |
| [[BK](#_Toc144361843)](#_Toc144362940)      | [[Monitor IFC background job parameters](#_Toc144361843)](#_Toc144362940)      | [[\[GMRC IFC BKG PARAM MON\]](#_Toc144361843)](#_Toc144362940)         |
| [[EC](#_Toc144361843)](#_Toc144362940)      | [[IFC Possible Erroneous Comment Report](#_Toc144361843)](#_Toc144362940)      |                                                                        |
| [[IP](#_Toc144361843)](#_Toc144362940)      | [[Inter-facility Consult Requests By Patient](#_Toc144361843)](#_Toc144362940) | [[\[GMRC IFC RPT CONSULTS BY PT\]](#_Toc144361843)](#_Toc144362940)    |
| [[IR](#_Toc144361843)](#_Toc144362940)      | [[IFC Requests by Remote Ordering Provider](#_Toc144361843)](#_Toc144362940)   | [[\[GMRC IFC RPT CONSULTS BY REMPR\]](#_Toc144361843)](#_Toc144362940) |
| [[PI](#_Toc144361843)](#_Toc144362940)      | [[Print Inter-facility Consult Requests](#_Toc144361843)](#_Toc144362940)      | [[\[GMRC IFC PRINT RPT NUMBERED\]](#_Toc144361843)](#_Toc144362940)    |

[[Inter-Facility Consult Requests (IFC), Inter-Facility Consult Requests by Patient (IP), Print Inter-Facility Consult Requests (PI), and IFC Requests by Remote Ordering Provider (IR) are covered under the Inter-Facility Consults Reports section above.](#_Toc144361843)](#_Toc144362940)

[[Refer to Figure 7-1, which shows how to use the Test IFC Implementation option to check the setup of a procedure or consult service.](#_Toc144361843)](#_Toc144362940)

[[  
](#_Toc144361843)](#_Toc144362940)

- 
- 
- 
- 
- 

[[301 – Service not matched to receiving facility. You need to coordinate with the consulting facility. The consulting facility needs to use the Setup Service (SS) option to make sure your facility is correctly listed in the IFC SENDING FACILITY field.401 – Procedure not matched to receiving facility. You need to coordinate with the consulting facility. The consulting facility needs to use the Setup Procedure (PR) option to make sure your facility is correctly listed in the IFC SENDING FACILITY field.501 – Error in procedure name. Could not find a matching procedure at the consulting facility. You probably need to verify the spelling and use the Setup Procedure (PR) option to make sure the IFC REMOTE PROCEDURE NAME is correct in your Procedure file (#123.3).601 – Multiple services matched to procedure. At the consulting facility, the RELATED SERVICES multiple must only contain a single value.701 – Error in Service name. Could not find a matching service at the consulting facility. You probably need to verify the spelling and use the Setup Service (SS) option to make sure the IFC REMOTE NAME is correct in your Request Services (#123.5).](#_Toc144361844)](#_Toc144362940)

[[Note: Any error occurring within the VistA HL7 messaging system is also indicated in this option.](#_Toc144361844)](#_Toc144362940)

[[GMRC IFC INC TRANS is a tool for reviewing incomplete Inter-Facility Consult (IFC) Transactions. With this option you can retransmit an action that is not yet resolved.](#_Toc144361844)](#_Toc144362940)

[[  
](#_Toc144361844)](#_Toc144362940)

[[This option can accept the following inputs when selecting a consult request:](#_Toc144361844)](#_Toc144362940)

- 
- 
- 
- 

[[  
](#_Toc144361845)](#_Toc144362940)

[[<span id="_Toc169170066" class="anchor"></span>Figure 7‑3: List Incomplete IFC Transactions Example (continued)](#_Toc144361845)](#_Toc144362940)

[[![](consult-request-tracking-technical-manual-gmrc-3-0-189/053.png)](#_Toc144361846)](#_Toc144362940)

[[  
](#_Toc144361846)](#_Toc144362940)

- 
- 
- 
- 
- 
- 
- 

[[ALL to list all entries.The consult number to list that single consult.The patient name to select a consult from the consults on file for that patient.The to or from service to select a consult from the consults to or from that service.The date of request to select a consult originated on that date.The CPRS status, such as PENDING or PARTIAL RESULTS, to select a consult with that status.The sending provider to select a consult originated by that provider.](#_Toc144361846)](#_Toc144362940)

[[Refer to Figures 7-4 and 7-5 on the following page, which list all entries in the IFC Transaction Log.](#_Toc144361846)](#_Toc144362940)

[[  
](#_Toc144361846)](#_Toc144362940)

[[There are five (5) Consults notifications:](#_Toc144361850)](#_Toc144362940)

- 
- 
- 
- 
- 
- 

[[The Consult Service Tracking (GMRC SERVICE TRACKING) option is a generic “User” option that:](#_Toc144361850)](#_Toc144362940)

- 
- 
- 
- 
- 
- 
- 
- 

[[Service Individual to Notify—123.08Service Team(s) to Notify—123.08Update Users W/O Notifications—123.1Update Teams W/O Notifications—123.3Administrative update users—123.33Administrative update teams—123.34](#_Toc144361850)](#_Toc144362940)

[[The Text Integration Utilities package is essential for completing consults under V. 3.](#_Toc144361850)[0. It gives you several benefits not previously available. Among them are the ability to use boilerplate for selected consult types and the ability to file results in the TIU data base.](#_Toc144362940)](#_Toc144362940)

[[In this section we first review the process of Consults resulting. Then we present two different document definition hierarchies that may be used for Consults results. Finally, we present the TIU options you need to set up the TIU part of Consults Resulting.](#_Toc144362940)](#_Toc144362940)

[[The diagram, Consults Resulting Process, shows the consults process with emphasis on the resulting phase. To complete a consult, three things must happen:](#_Toc144362940)](#_Toc144362940)

- 
- 
- 

[[You should have TIU already set up on your system and be familiar with the Text Integration Utilities (TIU) Implementation Guide.](#_Toc144362940)](#_Toc144362940)

[[We present here two document hierarchies found useful by hospitals in the VHA system. Strategy A creates Consults as an independent class under Clinical Documents. Strategy B creates Consults as a document class under Progress Notes.](#_Toc144362940)](#_Toc144362940)

- 
- 

[[Provides a CLEAR separation of Consults from Progress Notes and minimizes the number of choices for the end-user.Simple, with few concerns for maintainability (e.g., no question as to whether heritable methods and properties of Progress Notes were appropriately overridden, etc.).](#_Toc144362940)](#_Toc144362940)

- 
- 

[[Not necessarily consistent with the way providers have been documenting their Consult Results in the past. (i.e., if they have been using PN titles to "result" consults and referring to the notes on the SF 513's in the past, this will be a departure from that practice).Limits flexibility of access to the information. (i.e., if set-up this way, they may only access the data through Integrated Document Management options on the TIU-side, and through the Consults tab of the CPRS chart).](#_Toc144362940)](#_Toc144362940)

- 
- 

[[Consistent with the way many providers have been documenting their Consult Results in the past. (i.e., if they have been using PN titles to "result" consults, they may continue to do so, with the results showing up on both the 509 and SF 513).Enhances flexibility of access to the information. (i.e., if set-up this way, they may access the data through any option on the TIU side, as well as through EITHER the Consults or Progress Notes tabs of the CPRS chart).](#_Toc144362940)](#_Toc144362940)

- 
- 

[[  
](#_Toc144361851)](#_Toc144362940)

[[Occasionally, a consult result is linked to the wrong consult. If this is detected prior to signature, it is possible for the author of a consult result to re-direct the record to a different consult request by any of several methods:](#_Toc144361856)](#_Toc144362940)

1.  
2.  
3.  
4.  

[[Through the Link to Request action, when processing the alert for the unsigned Consult Result.Through the Individual Patient Document option.You may choose the Link action from the All My Unsigned Documents Option.From the CPRS Chart.](#_Toc144361856)](#_Toc144362940)

[[There are examples of the above four methods in the Consult/Request Tracking User Manual.](#_Toc144361856)](#_Toc144362940)

[[  
](#_Toc144361856)](#_Toc144362940)

[[  
](#_Toc144361857)](#_Toc144362940)

[[<span id="_Toc169170078" class="anchor"></span>Figure 7‑15: TIU Maintenance Example (continued)](#_Toc144361857)](#_Toc144362940)

[[![](consult-request-tracking-technical-manual-gmrc-3-0-189/065.png)](#_Toc144361858)](#_Toc144362940)

[[The Procedures module of Consult/Request Tracking has been enhanced. The two major enhancements are:](#_Toc144361858)](#_Toc144362940)

1.  
2.  

[[A complete change to the method of creating and activating procedures for use in CPRS and Consult/Request Tracking is introduced including a new file to store the procedures data.The ability to link results stored in the VistA Medicine package to a procedure request has been re-established.  
](#_Toc144361858)](#_Toc144362940)

- 
- 
- 
- 
- 
- 
- 
- 
- 

[[INTERNAL NAME in an alternate name for the service. This name does not appear on printouts or displays but can be used to access the service through the Setup Services (SS) option, or with FileMan.RELATED SERVICES: The RELATED SERVICES field in the procedure setup indicates which services from the Consult hierarchy will receive and process procedures of this type. If more than one related service is entered in this field the ordering person will have to choose which service to direct the procedure to. The users that will be notified and the users allowed to update procedure requests of this type are determined by the receiving service.TYPE OF PROCEDURE: The TYPE OF PROCEDURE field in the procedure setup essentially turns on the interface to the Medicine package for this type of procedure. The field is a pointer to the PROCEDURE/SUBSPECIALTY (#697.2) file in the Medicine package. If this field is not set, no medicine procedure results may be linked to this type of procedure request. PROVISIONAL DX PROMPT: Used by CPRS to determine how to prompt for the provisional diagnosis when ordering this procedure. If this field is set to OPTIONAL, the user will be prompted for the provisional diagnosis but may bypass answering the prompt. If the field is set to SUPPRESS, the user will not be presented with the provisional diagnosis prompt. If set to REQUIRED, the user must answer the prompt to continue placing the order.PROVISIONAL DX INPUT: Determines the method that CPRS uses to prompt the user for input of the provisional diagnosis when ordering this procedure. If set to FREE TEXT, the user may type any text from 2-80 characters in length. If set to LEXICON, the user will be required to select a coded diagnosis from the Clinical Lexicon.PREREQUISITE: This word-processing field is utilized to communicate pre-requisite information to the ordering person prior to ordering this procedure. This field is presented to the ordering person upon selecting a procedure and allows them to abort the ordering at that time if they choose. TIU objects may be embedded within this field which are resolved for the current patient during ordering. Any TIU objects must be contained within vertical bars (e.g. \|BLOOD PRESSURE\| ).DEFAULT REASON FOR REQUEST: The default text used as the reason for request when ordering this procedure. This field allows a boilerplate of text to be imported into the reason for request when placing orders for this procedure. If the user places an order using a quick order having boilerplate text, that text supersedes any default text stored in this field. This field may contain any text including TIU objects. TIU Objects must be enclosed in vertical bars (e.g. \|PATIENT NAME\| ).RESTRICT DEFAULT REASON EDIT: If a DEFAULT REASON FOR REQUEST exists for this service this field effects the ordering person's ability to edit the default reason while placing an order. This variable can be set to UNRESTRICTED, NO EDITING, or ASK ON EDIT ONLY. If the third value, ASK ON EDIT ONLY, is used, the user is only allowed to edit the default reason if the order is edited before releasing to the service.IFC ROUTING SITE: This field contains the VA facility that will perform consults requested for this service. When a consult for this service is ordered, it will automatically be routed to the VA facility in this field.](#_Toc144361859)](#_Toc144362940)

- 
- 

[[IFC REMOTE NAME: This field contains the name of the service that will be requested at the VAMC defined in the IFC ROUTING SITE field. Enter the name of the service exactly as it is named at the remote facility. If this name does not match the name of the service at the routing site, the request will fail to be filed at the remote site. This will delay or prohibit the performance and processing of this request.IFC SENDING FACILITY: This is a multiple containing the facilities from which your site may receive Inter-Facility Consults for this consult. As with all IFC fields, they must be an exact match.](#_Toc144361859)](#_Toc144362940)

[[In the Consult Service Tracking option and in CPRS list manager Consults tab, medicine results can be associated with the procedure request by using the complete/update action. If the selected item is a procedure and is configured for medicine resulting, users will be given the option of attaching medicine procedure result and/or writing a TIU document. In the CPRS GUI, associating medicine procedure results will be done via a separate menu item on the Action Menu of the Consults tab](#_Toc144361859)](#_Toc144362940)

[[This action provides a mechanism to disassociate a medicine result from a request that was linked by mistake. The ability to take this action is controlled by membership in a USR USER CLASS. A new field was exported for the REQUEST SERVICES (#123.5). Field (#1.](#_Toc144361859)[06) RESULT MGMT USER CLASS is a pointer to the USR USER CLASS (#8930) file and the appropriate user class of individuals who may take this action should be listed here. It is recommended that the user class entered here be in line with the business rule involving the LINK action as it pertains to TIU documents.](#_Toc144362930)](#_Toc144362940)

[[The action to disassociate a medicine result is provided through an action on the Consult Service Tracking option or the Consults tab of CPRS list manager and CPRS GUI.](#_Toc144362930)](#_Toc144362940)

[[There are two parameters associated with the Consults package:](#_Toc144362930)](#_Toc144362940)

- 
- 

[[GMRC CONSULT LIST DAYS GMRC FEE SERVICES.](#_Toc144362930)](#_Toc144362940)

[[  
](#_Toc144361860)](#_Toc144362940)

[[  
](#_Toc144361860)](#_Toc144362940)

[[Refer to Table 8-1. The following is a listing of the files contained in the Consults package. Listed for each file are its file number, name, global location, and an indicator as to whether or not data comes with the file.](#_Toc144361860)](#_Toc144362940)

[[<span id="_Toc169170350" class="anchor"></span>Table 8‑1: File Globals](#_Toc144361860)](#_Toc144362940)

| [[Synonym](#_Toc144361860)](#_Toc144362940) | [[Name](#_Toc144361860)](#_Toc144362940)                      | [[Global](#_Toc144361860)](#_Toc144362940)     | [[Data](#_Toc144361860)](#_Toc144362940) |
|---------------------------------------------|---------------------------------------------------------------|------------------------------------------------|------------------------------------------|
| [[123](#_Toc144361860)](#_Toc144362940)     | [[REQUEST/CONSULTATION FILE](#_Toc144361860)](#_Toc144362940) | [[^GMR(123,](#_Toc144361860)](#_Toc144362940)  | [[NO](#_Toc144361860)](#_Toc144362940)   |
| [[123.1](#_Toc144361860)](#_Toc144362940)   | [[REQUEST ACTION TYPES](#_Toc144361860)](#_Toc144362940)      | [[^GMR(123.1](#_Toc144361860)](#_Toc144362940) | [[YES](#_Toc144361860)](#_Toc144362940)  |
| [[123.3](#_Toc144361860)](#_Toc144362940)   | [[GMRC PROCEDURES](#_Toc144361860)](#_Toc144362940)           | [[^GMR(123.3](#_Toc144361860)](#_Toc144362940) | [[YES](#_Toc144361860)](#_Toc144362940)  |
| [[123.5](#_Toc144361860)](#_Toc144362940)   | [[REQUEST SERVICES](#_Toc144361860)](#_Toc144362940)          | [[^GMR(123.5](#_Toc144361860)](#_Toc144362940) | [[YES](#_Toc144361860)](#_Toc144362940)  |
| [[123.6](#_Toc144361860)](#_Toc144362940)   | [[IFC MESSAGE LOG](#_Toc144361860)](#_Toc144362940)           | [[^GMR(123.6](#_Toc144361860)](#_Toc144362940) | [[NO](#_Toc144361860)](#_Toc144362940)   |

[[  
](#_Toc144361860)](#_Toc144362940)

[[  
](#_Toc144361861)](#_Toc144362940)

| [[Option Name](#_Toc144361861)](#_Toc144362940)                 | [[Display Text](#_Toc144361861)](#_Toc144362940)                                    |
|-----------------------------------------------------------------|-------------------------------------------------------------------------------------|
| [[GMRC REPORTS](#_Toc144361861)](#_Toc144362940)                | [[Consults Tracking Reports](#_Toc144361861)](#_Toc144362940)                       |
| [[GMRC SETUP REQUEST SERVICES](#_Toc144361861)](#_Toc144362940) | [[Set up Consults Services](#_Toc144361861)](#_Toc144362940)                        |
| [[GMRC SERVICE USER MGMT](#_Toc144361861)](#_Toc144362940)      | [[Service User Management](#_Toc144361861)](#_Toc144362940)                         |
| [[GMRC SERVICE TRACKING](#_Toc144361861)](#_Toc144362940)       | [[Consults Service Tracking](#_Toc144361861)](#_Toc144362940)                       |
| [[GMRC PHARMACY TPN CONSULTS](#_Toc144361861)](#_Toc144362940)  | [[Pharmacy TPN Consults](#_Toc144361861)](#_Toc144362940)                           |
| [[GMRC PRINT TEST PAGE](#_Toc144361861)](#_Toc144362940)        | [[Print Test Page](#_Toc144361861)](#_Toc144362940)                                 |
| [[MRCSTSU](#_Toc144361861)](#_Toc144362940)                     | [[Group Update of Consults Requests](#_Toc144361861)](#_Toc144362940)               |
| [[GMRC UPDATE AUTHORITY](#_Toc144361861)](#_Toc144362940)       | [[Determine Users' Update Authority](#_Toc144361861)](#_Toc144362940)               |
| [[GMRC USER NOTIFICATION](#_Toc144361861)](#_Toc144362940)      | [[Determine if User is Notification Recipient](#_Toc144361861)](#_Toc144362940)     |
| [[GMRC NOTIFICATION RECIPS](#_Toc144361861)](#_Toc144362940)    | [[Determine Notification Recipients for a Service](#_Toc144361861)](#_Toc144362940) |
| [[GMRC TEST DEFAULT REASON](#_Toc144361861)](#_Toc144362940)    | [[Test Default Reason for Request](#_Toc144361861)](#_Toc144362940)                 |
| [[GMRC LIST HIERARCHY](#_Toc144361861)](#_Toc144362940)         | [[List Consult Service Hierarchy](#_Toc144361861)](#_Toc144362940)                  |
| [[GMRC PROCEDURE SETUP](#_Toc144361861)](#_Toc144362940)        | [[Setup Procedures](#_Toc144361861)](#_Toc144362940)                                |
| [[GMRC CLONE PROSTHETICS](#_Toc144361861)](#_Toc144362940)      | [[Copy Prosthetics services](#_Toc144361861)](#_Toc144362940)                       |
| [[GMRC CONSULT CLOSURE TOOL](#_Toc144361861)](#_Toc144362940)   | [[Menu for Closure Tools](#_Toc144361861)](#_Toc144362940)                          |
| [[GMRC DUPLICATE SUB-SERVICE](#_Toc144361861)](#_Toc144362940)  | [[Duplicate Sub-Service](#_Toc144361861)](#_Toc144362940)                           |
| [[GMRC FEE PARAM](#_Toc144361861)](#_Toc144362940)              | [[Define Fee Services](#_Toc144361861)](#_Toc144362940)                             |
| [[GMRC IFC MGMT](#_Toc144361861)](#_Toc144362940)               | [[IFC Management Menu](#_Toc144361861)](#_Toc144362940)                             |
| [[GMRC FSC HCP MAIL GROUP](#_Toc144361861)](#_Toc144362940)     | [[Define FSC HCP Mail Group](#_Toc144361861)](#_Toc144362940)                       |

[[<span id="_Toc169170352" class="anchor"></span>Table 9‑2: GMRC REPORTS Menu](#_Toc144361861)](#_Toc144362940)

| [[Option Name](#_Toc144361861)](#_Toc144362940)                    | [[Display Text](#_Toc144361861)](#_Toc144362940)                                       |
|--------------------------------------------------------------------|----------------------------------------------------------------------------------------|
| [[GMRC COMPLETION STATISTICS](#_Toc144361861)](#_Toc144362940)     | [[Completion Time Statistics](#_Toc144361861)](#_Toc144362940)                         |
| [[GMRC RPT PENDING CONSULTS](#_Toc144361861)](#_Toc144362940)      | [[Service Consults Pending Resolution](#_Toc144361861)](#_Toc144362940)                |
| [[GMRC RPT COMPLETE CONSULTS](#_Toc144361861)](#_Toc144362940)     | [[Service Consults Completed](#_Toc144361861)](#_Toc144362940)                         |
| [[GMRC RPT COMPLETE/PENDING](#_Toc144361861)](#_Toc144362940)      | [[Service Consults Completed or Pending Resolution](#_Toc144361861)](#_Toc144362940)   |
| [[GMRC IFC RPT CONSULTS](#_Toc144361861)](#_Toc144362940)          | [[IFC Requests](#_Toc144361861)](#_Toc144362940)                                       |
| [[GMRC IFC RPT CONSULTS BY PT](#_Toc144361861)](#_Toc144362940)    | [[IFC Requests By Patient](#_Toc144361861)](#_Toc144362940)                            |
| [[GMRC IFC RPT CONSULTS BY REMPR](#_Toc144361861)](#_Toc144362940) | [[IFC Requests by Remote Ordering Provider](#_Toc144361861)](#_Toc144362940)           |
| [[GMRC RPT NUMBERED CONSULTS](#_Toc144361861)](#_Toc144362940)     | [[Service Consults with Consults \#s](#_Toc144361861)](#_Toc144362940)                 |
| [[GMRC IFC PRINT RPT NUMBERED](#_Toc144361861)](#_Toc144362940)    | [[Print IFC Requests](#_Toc144361861)](#_Toc144362940)                                 |
| [[GMRC PRINT BY SEARCH](#_Toc144361861)](#_Toc144362940)           | [[Print Consults by Provider, Location, or Procedure](#_Toc144361861)](#_Toc144362940) |
| [[GMRC RPT PERF MONITOR](#_Toc144361861)](#_Toc144362940)          | [[Print Consult Performance Monitor Report](#_Toc144361861)](#_Toc144362940)           |
| [[GMRC PRINT RPT NUMBERED](#_Toc144361861)](#_Toc144362940)        | [[Print Service Consults by Status](#_Toc144361861)](#_Toc144362940)                   |
| [[GMRC RPT CONSULTS BY STATUS](#_Toc144361861)](#_Toc144362940)    | [[Service Consults By Status](#_Toc144361861)](#_Toc144362940)                         |
| [[GMRC PRINT COMPLETION STAT](#_Toc144361861)](#_Toc144362940)     | [[Print Completion Time Statistics Report](#_Toc144361861)](#_Toc144362940)            |

[[<span id="_Toc169170353" class="anchor"></span>Table 9‑3: GMRC GENERAL SERVICE USER Menu](#_Toc144361861)](#_Toc144362940)

| [[Option Name](#_Toc144361861)](#_Toc144362940)                | [[Display Text](#_Toc144361861)](#_Toc144362940)               |
|----------------------------------------------------------------|----------------------------------------------------------------|
| [[GMRC SERVICE TRACKING](#_Toc144361861)](#_Toc144362940)      | [[Consults Service Tracking](#_Toc144361861)](#_Toc144362940)  |
| [[GMRC RPT PENDING](#_Toc144361861)](#_Toc144362940)           | [[Service Consults Pending](#_Toc144361861)](#_Toc144362940)   |
| [[GMRC COMPLETION STATISTICS](#_Toc144361861)](#_Toc144362940) | [[Completion Time Statistics](#_Toc144361861)](#_Toc144362940) |

[[<span id="_Toc169170354" class="anchor"></span>Table 9‑4: GMRC PHARMACY USER Menu](#_Toc144361861)](#_Toc144362940)

| [[Option Name](#_Toc144361861)](#_Toc144362940)                | [[Display Text](#_Toc144361861)](#_Toc144362940)               |
|----------------------------------------------------------------|----------------------------------------------------------------|
| [[GMRC PHARMACY TPN CONSULTS](#_Toc144361861)](#_Toc144362940) | [[Pharmacy TPN Consults](#_Toc144361861)](#_Toc144362940)      |
| [[GMRC RPT PENDING](#_Toc144361861)](#_Toc144362940)           | [[Service Consults Pending](#_Toc144361861)](#_Toc144362940)   |
| [[GMRC COMPLETION STATISTICS](#_Toc144361861)](#_Toc144362940) | [[Completion Time Statistics](#_Toc144361861)](#_Toc144362940) |

[[<span id="_Toc169170355" class="anchor"></span>Table 9‑5: GMRC CONSULT CLOSURE TOOL Menu](#_Toc144361861)](#_Toc144362940)

| [[Option Name](#_Toc144361714)](#_Toc144362940)                 | [[Display Text](#_Toc144361714)](#_Toc144362940)                               |
|-----------------------------------------------------------------|--------------------------------------------------------------------------------|
| [[GMRC CONSULT CLOSE TOOL EDT](#_Toc144361714)](#_Toc144362940) | [[Consult Closure Tool Edit Configuration](#_Toc144361714)](#_Toc144362940)    |
| [[GMRC CONSULT CLOSE TOOL INQ](#_Toc144361714)](#_Toc144362940) | [[Consult Closure Tool Inquire Configuration](#_Toc144361714)](#_Toc144362940) |
| [[GMRC CONSULT CLOSE TOOL RUN](#_Toc144361714)](#_Toc144362940) | [[Consult Closure Tool Run Configuration](#_Toc144361714)](#_Toc144362940)     |

[[<span id="_Toc169170356" class="anchor"></span>Table 9‑6: GMRC IFC MGMT Menu](#_Toc144361714)](#_Toc144362940)

| [[Option Name](#_Toc144361714)](#_Toc144362940)                    | [[Display Text](#_Toc144361714)](#_Toc144362940)                             |
|--------------------------------------------------------------------|------------------------------------------------------------------------------|
| [[GMRC IFC TEST SETUP](#_Toc144361714)](#_Toc144362940)            | [[Test IFC implementation](#_Toc144361714)](#_Toc144362940)                  |
| [[GMRC IFC INC TRANS](#_Toc144361714)](#_Toc144362940)             | [[List incomplete IFC transactions](#_Toc144361714)](#_Toc144362940)         |
| [[GMRC IFC RPT CONSULTS](#_Toc144361714)](#_Toc144362940)          | [[IFC Requests](#_Toc144361714)](#_Toc144362940)                             |
| [[GMRC IFC TRANS](#_Toc144361714)](#_Toc144362940)                 | [[IFC Transaction Report](#_Toc144361714)](#_Toc144362940)                   |
| [[GMRC IFC REMOTE NUMBER](#_Toc144361714)](#_Toc144362940)         | [[Locate IFC by Remote Cslt \#](#_Toc144361714)](#_Toc144362940)             |
| [[GMRC IFC BKG PARAM MON](#_Toc144361714)](#_Toc144362940)         | [[Monitor IFC background job parameters](#_Toc144361714)](#_Toc144362940)    |
| [[GMRC IFC RPT CONSULTS BY PT](#_Toc144361714)](#_Toc144362940)    | [[IFC Requests By Patient](#_Toc144361714)](#_Toc144362940)                  |
| [[GMRC IFC RPT CONSULTS BY REMPR](#_Toc144361714)](#_Toc144362940) | [[IFC Requests by Remote Ordering Provider](#_Toc144361714)](#_Toc144362940) |
| [[GMRC IFC PRINT RPT NUMBERED](#_Toc144361714)](#_Toc144362940)    | [[Print IFC Requests](#_Toc144361714)](#_Toc144362940)                       |

[[  
](#_Toc144363043)](#_Toc144362940)

[[  
](#_Toc144362940)](#_Toc144362940)

[[No archiving or purging utilities are provided in this version for Consults distributed files.](#_Toc144362940)](#_Toc144362940)

[[  
](#_Toc144362940)](#_Toc144362940)

[[The Consults package is dependent upon other VA software to function correctly. Refer to Table 12-1.](#_Toc144362940)](#_Toc144362940)

[[<span id="_Toc169170357" class="anchor"></span>Table 12‑1: External Relations – Other VA Software](#_Toc144362940)](#_Toc144362940)

| [[Package](#_Toc144362940)](#_Toc144362940)    | [[Version](#_Toc144362940)](#_Toc144362940)                           | [[Notes](#_Toc144362940)](#_Toc144362940)                                           |
|------------------------------------------------|-----------------------------------------------------------------------|-------------------------------------------------------------------------------------|
| [[VA FileMan](#_Toc144362940)](#_Toc144362940) | [[21](#_Toc144362940)](#_Toc144362940)                                |                                                                                     |
| [[OE/RR](#_Toc144362940)](#_Toc144362940)      | [[3.0](#_Toc144362940)](#_Toc144362940)                               |                                                                                     |
| [[KERNEL](#_Toc144362940)](#_Toc144362940)     | [[8.](#_Toc144362940)[0 (+ Patches)](#_Toc144363002)](#_Toc144362940) | [[“Select Action:”prompts, and Alert capabilities](#_Toc144363002)](#_Toc144362940) |
| [[PIMS](#_Toc144363002)](#_Toc144362940)       | [[5.](#_Toc144363002)[3](#_Toc144362942)](#_Toc144362940)             | [[Calls to VADPT](#_Toc144362942)](#_Toc144362940)                                  |

[[Refer to Table 12-2.](#_Toc144362942)](#_Toc144362940)

[[<span id="_Toc169170358" class="anchor"></span>Table 12‑2: External Relations – Other VA Software](#_Toc144362942)](#_Toc144362940)

| [[DEA Number](#_Toc144362942)](#_Toc144362940) | [[Custodial Package](#_Toc144362942)](#_Toc144362940) | [[DBA Number](#_Toc144362942)](#_Toc144362940) | [[Custodial Package](#_Toc144362942)](#_Toc144362940) |
|------------------------------------------------|-------------------------------------------------------|------------------------------------------------|-------------------------------------------------------|
| [[147](#_Toc144362942)](#_Toc144362940)        | [[Medicine](#_Toc144362942)](#_Toc144362940)          | [[868](#_Toc144362942)](#_Toc144362940)        | [[OE/RR](#_Toc144362942)](#_Toc144362940)             |
| [[165](#_Toc144362942)](#_Toc144362940)        | [[OE/RR](#_Toc144362942)](#_Toc144362940)             | [[869](#_Toc144362942)](#_Toc144362940)        | [[OE/RR](#_Toc144362942)](#_Toc144362940)             |
| [[167](#_Toc144362942)](#_Toc144362940)        | [[Kernel](#_Toc144362942)](#_Toc144362940)            | [[870](#_Toc144362942)](#_Toc144362940)        | [[OE/RR](#_Toc144362942)](#_Toc144362940)             |
| [[169](#_Toc144362942)](#_Toc144362940)        | [[Kernel](#_Toc144362942)](#_Toc144362940)            | [[871](#_Toc144362942)](#_Toc144362940)        | [[OE/RR](#_Toc144362942)](#_Toc144362940)             |
| [[181](#_Toc144362942)](#_Toc144362940)        | [[OE/RR](#_Toc144362942)](#_Toc144362940)             | [[872](#_Toc144362942)](#_Toc144362940)        | [[OE/RR](#_Toc144362942)](#_Toc144362940)             |
| [[510](#_Toc144362942)](#_Toc144362940)        | [[VA FileMan](#_Toc144362942)](#_Toc144362940)        | [[873](#_Toc144362942)](#_Toc144362940)        | [[OE/RR](#_Toc144362942)](#_Toc144362940)             |
| [[615](#_Toc144362942)](#_Toc144362940)        | [[Medicine](#_Toc144362942)](#_Toc144362940)          | [[875](#_Toc144362942)](#_Toc144362940)        | [[OE/RR](#_Toc144362942)](#_Toc144362940)             |
| [[616](#_Toc144362942)](#_Toc144362940)        | [[Medicine](#_Toc144362942)](#_Toc144362940)          | [[2038](#_Toc144362942)](#_Toc144362940)       | [[OE/RR](#_Toc144362942)](#_Toc144362940)             |
| [[627](#_Toc144362942)](#_Toc144362940)        | [[OE/RR](#_Toc144362942)](#_Toc144362940)             | [[2638](#_Toc144362942)](#_Toc144362940)       | [[OE/RR](#_Toc144362942)](#_Toc144362940)             |
| [[628](#_Toc144362942)](#_Toc144362940)        | [[OE/RR](#_Toc144362942)](#_Toc144362940)             | [[2290](#_Toc144362942)](#_Toc144362940)       | [[OE/RR](#_Toc144362942)](#_Toc144362940)             |
| [[629](#_Toc144362942)](#_Toc144362940)        | [[OE/RR](#_Toc144362942)](#_Toc144362940)             | [[2699](#_Toc144362942)](#_Toc144362940)       | [[TIU](#_Toc144362942)](#_Toc144362940)               |
| [[630](#_Toc144362942)](#_Toc144362940)        | [[OE/RR](#_Toc144362942)](#_Toc144362940)             | [[2700](#_Toc144362942)](#_Toc144362940)       | [[OE/RR](#_Toc144362942)](#_Toc144362940)             |
| [[631](#_Toc144362942)](#_Toc144362940)        | [[OE/RR](#_Toc144362942)](#_Toc144362940)             | [[2713](#_Toc144362942)](#_Toc144362940)       | [[OE/RR](#_Toc144362942)](#_Toc144362940)             |
| [[632](#_Toc144362942)](#_Toc144362940)        | [[Kernel](#_Toc144362942)](#_Toc144362940)            | [[2761](#_Toc144362942)](#_Toc144362940)       | [[OE/RR](#_Toc144362942)](#_Toc144362940)             |
| [[635](#_Toc144362942)](#_Toc144362940)        | [[OE/RR](#_Toc144362942)](#_Toc144362940)             | [[2764](#_Toc144362942)](#_Toc144362940)       | [[OE/RR](#_Toc144362942)](#_Toc144362940)             |
| [[636](#_Toc144362942)](#_Toc144362940)        | [[OE/RR](#_Toc144362942)](#_Toc144362940)             | [[2849](#_Toc144362942)](#_Toc144362940)       | [[OE/RR](#_Toc144362942)](#_Toc144362940)             |
| [[637](#_Toc144362942)](#_Toc144362940)        | [[OE/RR](#_Toc144362942)](#_Toc144362940)             | [[3042](#_Toc144362942)](#_Toc144362940)       | [[MEDICINE](#_Toc144362942)](#_Toc144362940)          |
| [[638](#_Toc144362942)](#_Toc144362940)        | [[OE/RR](#_Toc144362942)](#_Toc144362940)             | [[3138](#_Toc144362942)](#_Toc144362940)       | [[CLINICAL PROC](#_Toc144362942)](#_Toc144362940)     |
| [[639](#_Toc144362942)](#_Toc144362940)        | [[OE/RR](#_Toc144362942)](#_Toc144362940)             | [[3168](#_Toc144362942)](#_Toc144362940)       | [[OE/RR](#_Toc144362942)](#_Toc144362940)             |
| [[640](#_Toc144362942)](#_Toc144362940)        | [[OE/RR](#_Toc144362942)](#_Toc144362940)             | [[3171](#_Toc144362942)](#_Toc144362940)       | [[OE/RR](#_Toc144362942)](#_Toc144362940)             |
| [[861](#_Toc144362942)](#_Toc144362940)        | [[OE/RR](#_Toc144362942)](#_Toc144362940)             | [[6184](#_Toc144362942)](#_Toc144362940)       | [[GMRC](#_Toc144362942)](#_Toc144362940)              |
| [[862](#_Toc144362942)](#_Toc144362940)        | [[OE/RR](#_Toc144362942)](#_Toc144362940)             |                                                |                                                       |
| [[863](#_Toc144362942)](#_Toc144362940)        | [[OE/RR](#_Toc144362942)](#_Toc144362940)             |                                                |                                                       |
| [[864](#_Toc144362942)](#_Toc144362940)        | [[OE/RR](#_Toc144362942)](#_Toc144362940)             |                                                |                                                       |
| [[865](#_Toc144362942)](#_Toc144362940)        | [[OE/RR](#_Toc144362942)](#_Toc144362940)             |                                                |                                                       |
| [[866](#_Toc144362942)](#_Toc144362940)        | [[OE/RR](#_Toc144362942)](#_Toc144362940)             |                                                |                                                       |
| [[867](#_Toc144362942)](#_Toc144362940)        | [[OE/RR](#_Toc144362942)](#_Toc144362940)             |                                                |                                                       |

[[  
](#_Toc144362942)](#_Toc144362940)

[[All options are independently evocable.](#_Toc144362942)](#_Toc144362940)

[[There are no package-wide variables exported with this package that require SACC exemption.](#_Toc144362942)](#_Toc144362940)

[[  
](#_Toc144362942)](#_Toc144362940)

[[Refer to Table 14-1, which lists HL7 fields used in transactions between OE/RR v.3.0 and the Consult package. Not every field will be used in every message.](#_Toc144362942)](#_Toc144362940)

[[<span id="_Toc169170359" class="anchor"></span>Table 14‑1: Private DBIA Agreements](#_Toc144362942)](#_Toc144362940)

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 32%" />
<col style="width: 34%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th><a href="#_Toc144362940"><span><strong>SEG</strong></span></a></th>
<th><a href="#_Toc144362940"><span><strong>SEQ</strong></span></a></th>
<th><a href="#_Toc144362940"><span><strong>Field Name</strong></span></a></th>
<th><a href="#_Toc144362940"><span><strong>Example</strong></span></a></th>
<th><a href="#_Toc144362940"><span><strong>HL7 Type</strong></span></a></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="#_Toc144362940"><span>MSH</span></a></td>
<td><a href="#_Toc144362940"><span>1</span></a></td>
<td><a href="#_Toc144362940"><span>Field Separator</span></a></td>
<td><a href="#_Toc144362940"><span>|</span></a></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>2</span></a></td>
<td><a href="#_Toc144362940"><span>Encoding Characters</span></a></td>
<td><a href="#_Toc144362940"><span>^~\&amp;</span></a></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>3</span></a></td>
<td><a href="#_Toc144362940"><span>Sending Application</span></a></td>
<td><a href="#_Toc144362940"><span>ORDER ENTRY</span></a></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>4</span></a></td>
<td><a href="#_Toc144362940"><span>Sending Facility</span></a></td>
<td><a href="#_Toc144362940"><span>660</span></a></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>9</span></a></td>
<td><a href="#_Toc144362940"><span>Message Type</span></a></td>
<td><a href="#_Toc144362940"><span>ORM</span></a></td>
<td><a href="#_Toc144362940"><span>ID</span></a></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>RF1</span></a></td>
<td><a href="#_Toc144362940"><span>1</span></a></td>
<td><a href="#_Toc144362940"><span>Referral Status</span></a></td>
<td><a href="#_Toc144362940"><span>IP^ADDED COMMENT</span></a></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>2</span></a></td>
<td><a href="#_Toc144362940"><span>Referral Priority</span></a></td>
<td><a href="#_Toc144362940"><span>ROUTINE</span></a></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>3</span></a></td>
<td><a href="#_Toc144362940"><span>Referral Type</span></a></td>
<td><a href="#_Toc144362940"><span>553^NON-VA COLONOSCOPY^^32563^NON-VA COLONOSCOPY v6.2</span></a></td>
<td><a href="#_Toc144362940"><span>coded element</span></a></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>5</span></a></td>
<td><a href="#_Toc144362940"><span>Referral Category</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td><a href="#_Toc144362940"><span>table 284</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>6</span></a></td>
<td><a href="#_Toc144362940"><span>Originating Referral Identifier</span></a></td>
<td><a href="#_Toc144362940"><span>486410</span></a></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>7</span></a></td>
<td><a href="#_Toc144362940"><span>Effective Date</span></a></td>
<td><a href="#_Toc144362940"><span>201403111904-0400</span></a></td>
<td><a href="#_Toc144362940"><span>timestamp</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>PRD</span></a></td>
<td><a href="#_Toc144362940"><span>1</span></a></td>
<td><a href="#_Toc144362940"><span>Provider Role</span></a></td>
<td><a href="#_Toc144362940"><span>RP</span></a></td>
<td><a href="#_Toc144362940"><span>table 286</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>2</span></a></td>
<td><a href="#_Toc144362940"><span>Provider Name</span></a></td>
<td><a href="#_Toc144362940"><span>CPRSPROVIDER^THREE^^^^^^^10000000046</span></a></td>
<td><a href="#_Toc144362940"><span>composite ID</span></a></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>3</span></a></td>
<td><a href="#_Toc144362940"><span>Provider Address</span></a></td>
<td><a href="#_Toc144362940"><span>1 STREET ADDRESS^^CITY^ST^00011</span></a></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>5</span></a></td>
<td><a href="#_Toc144362940"><span>Provider Communication Information</span></a></td>
<td><a href="#_Toc144362940"><span>^^^CPRS3@VA.GOV^^555^555-5555</span></a></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>IN1</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>1</span></a></td>
<td><a href="#_Toc144362940"><span><span>SetIDIN1</span></span></a></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>2</span></a></td>
<td><a href="#_Toc144362940"><span><span>InsurancePlanID</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Coded element</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>3</span></a></td>
<td><a href="#_Toc144362940"><span><span>InsuranceCompanyID</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>ID</span></a></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>4</span></a></td>
<td><a href="#_Toc144362940"><span><span>InsuranceCompanyName</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>5</span></a></td>
<td><a href="#_Toc144362940"><span><span>InsuranceCompanyAddress</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>address</span></a></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>6</span></a></td>
<td><a href="#_Toc144362940"><span><span>InsuranceCoContactPerson</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>7</span></a></td>
<td><a href="#_Toc144362940"><span><span>InsuranceCoPhoneNumber</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>8</span></a></td>
<td><a href="#_Toc144362940"><span><span>GroupNumber</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>9</span></a></td>
<td><a href="#_Toc144362940"><span><span>GroupName</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>10</span></a></td>
<td><a href="#_Toc144362940"><span><span>InsuredsGroupEmpID</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>11</span></a></td>
<td><a href="#_Toc144362940"><span><span>InsuredsGroupEmpName</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>12</span></a></td>
<td><a href="#_Toc144362940"><span><span>PlanEffectiveDate</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>date</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>13</span></a></td>
<td><a href="#_Toc144362940"><span><span>PlanExpirationDate</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>date</span></a></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>14</span></a></td>
<td><a href="#_Toc144362940"><span><span>AuthorizationInformation</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>15</span></a></td>
<td><a href="#_Toc144362940"><span><span>PlanType</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>16</span></a></td>
<td><a href="#_Toc144362940"><span><span>NameOfInsured</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>17</span></a></td>
<td><a href="#_Toc144362940"><span><span>InsuredsRelationshipToPatien</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>18</span></a></td>
<td><a href="#_Toc144362940"><span><span>InsuredsDateOfBirth</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>date</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>19</span></a></td>
<td><a href="#_Toc144362940"><span><span>InsuredsAddress</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>address</span></a></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>20</span></a></td>
<td><a href="#_Toc144362940"><span><span>AssignmentOfBenefits</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>21</span></a></td>
<td><a href="#_Toc144362940"><span><span>CoordinationOfBenefits</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>22</span></a></td>
<td><a href="#_Toc144362940"><span><span>CoordOfBenPriority</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>23</span></a></td>
<td><a href="#_Toc144362940"><span><span>NoticeOfAdmissionFlag</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>24</span></a></td>
<td><a href="#_Toc144362940"><span><span>NoticeOfAdmissionDate</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>date</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>25</span></a></td>
<td><a href="#_Toc144362940"><span><span>ReportOfEligibilityFlag</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>26</span></a></td>
<td><a href="#_Toc144362940"><span><span>ReportOfEligibilityDate</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>date</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>27</span></a></td>
<td><a href="#_Toc144362940"><span><span>ReleaseInformationCode</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>28</span></a></td>
<td><a href="#_Toc144362940"><span><span>PreAdmitCertPAC</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>29</span></a></td>
<td><a href="#_Toc144362940"><span><span>VerificationDateTime</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>date</span></a></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>30</span></a></td>
<td><a href="#_Toc144362940"><span><span>VerificationBy</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>31</span></a></td>
<td><a href="#_Toc144362940"><span><span>TypeOfAgreementCode</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>32</span></a></td>
<td><a href="#_Toc144362940"><span><span>BillingStatus</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>33</span></a></td>
<td><a href="#_Toc144362940"><span><span>LifetimeReserveDays</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>number</span></a></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>34</span></a></td>
<td><a href="#_Toc144362940"><span><span>DelayBeforeLRDay</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>number</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>35</span></a></td>
<td><a href="#_Toc144362940"><span><span>CompanyPlanCode</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>36</span></a></td>
<td><a href="#_Toc144362940"><span><span>PolicyNumber</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>37</span></a></td>
<td><a href="#_Toc144362940"><span><span>PolicyDeductible</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>number</span></a></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>38</span></a></td>
<td><a href="#_Toc144362940"><span><span>PolicyLimitAmount</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>number</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>39</span></a></td>
<td><a href="#_Toc144362940"><span><span>PolicyLimitDays</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>number</span></a></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>40</span></a></td>
<td><a href="#_Toc144362940"><span><span>RoomRateSemiPrivate</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>number</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>41</span></a></td>
<td><a href="#_Toc144362940"><span><span>RoomRatePrivate</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>number</span></a></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>42</span></a></td>
<td><a href="#_Toc144362940"><span><span>InsuredsEmploymentStatus</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>43</span></a></td>
<td><a href="#_Toc144362940"><span><span>InsuredsAdministrativeSex</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>44</span></a></td>
<td><a href="#_Toc144362940"><span><span>InsuredsEmployersAddress</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>address</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>45</span></a></td>
<td><a href="#_Toc144362940"><span><span>VerificationStatus</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>46</span></a></td>
<td><a href="#_Toc144362940"><span><span>PriorInsurancePlanID</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>47</span></a></td>
<td><a href="#_Toc144362940"><span><span>CoverageType</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>48</span></a></td>
<td><a href="#_Toc144362940"><span><span>Handicap</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>49</span></a></td>
<td><a href="#_Toc144362940"><span><span>InsuredsIDNumber</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>ID</span></a></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>50</span></a></td>
<td><a href="#_Toc144362940"><span><span>SignatureCode</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>51</span></a></td>
<td><a href="#_Toc144362940"><span><span>SignatureCodeDate</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>date</span></a></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>52</span></a></td>
<td><a href="#_Toc144362940"><span><span>InsuredsBirthPlace</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>53</span></a></td>
<td><a href="#_Toc144362940"><span><span>VIPIndicator</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>IN3</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>1</span></a></td>
<td><a href="#_Toc144362940"><span><span>SetIDIN3</span></span></a></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>2</span></a></td>
<td><a href="#_Toc144362940"><span><span>CertificationNumber</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>3</span></a></td>
<td><a href="#_Toc144362940"><span><span>CertifiedBy</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>4</span></a></td>
<td><a href="#_Toc144362940"><span><span>CertificationRequired</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>5</span></a></td>
<td><a href="#_Toc144362940"><span><span>Penalty</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>6</span></a></td>
<td><a href="#_Toc144362940"><span><span>CertificationDateTime</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>date</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>7</span></a></td>
<td><a href="#_Toc144362940"><span><span>CertificationModifyDateTime</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>date</span></a></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>8</span></a></td>
<td><a href="#_Toc144362940"><span><span>Operator</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>9</span></a></td>
<td><a href="#_Toc144362940"><span><span>CertificationBeginDate</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>date</span></a></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>10</span></a></td>
<td><a href="#_Toc144362940"><span><span>CertificationEndDate</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>date</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>11</span></a></td>
<td><a href="#_Toc144362940"><span><span>Days</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>number</span></a></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>12</span></a></td>
<td><a href="#_Toc144362940"><span><span>NonConcurCodeDescription</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>13</span></a></td>
<td><a href="#_Toc144362940"><span><span>NonConcurEffectiveDateTime</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>date</span></a></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>14</span></a></td>
<td><a href="#_Toc144362940"><span><span>PhysicianReviewer</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>15</span></a></td>
<td><a href="#_Toc144362940"><span><span>CertificationContact</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>16</span></a></td>
<td><a href="#_Toc144362940"><span><span>CertificationContactPhoneNum</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>17</span></a></td>
<td><a href="#_Toc144362940"><span><span>AppealReason</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>18</span></a></td>
<td><a href="#_Toc144362940"><span><span>CertificationAgency</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>19</span></a></td>
<td><a href="#_Toc144362940"><span><span>CertificationAgencyPhoneNumb</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>20</span></a></td>
<td><a href="#_Toc144362940"><span><span>PreCertificationRequirement</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>21</span></a></td>
<td><a href="#_Toc144362940"><span><span>CaseManager</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>22</span></a></td>
<td><a href="#_Toc144362940"><span><span>SecondOpinionDate</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>date</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>23</span></a></td>
<td><a href="#_Toc144362940"><span><span>SecondOpinionStatus</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>24</span></a></td>
<td><a href="#_Toc144362940"><span><span>SecondOpinionDocumentationRe</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>25</span></a></td>
<td><a href="#_Toc144362940"><span><span>SecondOpinionPhysician</span></span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>PID</span></a></td>
<td><a href="#_Toc144362940"><span>3</span></a></td>
<td><p><a href="#_Toc144362940"><span>Patient ID</span></a></p>
<p><a href="#_Toc144362940"><span>------------</span></a></p>
<p><a href="#_Toc144362940"><span>Between VistA and Cerner, this field includes the ICN and the EDIPI</span></a></p></td>
<td><p><a href="#_Toc144362940"><span>5340747</span></a></p>
<p><a href="#_Toc144362940"><span>-----------------------</span></a></p>
<p><a href="#_Toc144362940"><span>Between VistA and Cerner: Ex: 123456789V9999999^^^ICN^VETID~98765431^^^EDIPI^EDIPI</span></a></p></td>
<td><a href="#_Toc144362940"><span>composite ID</span></a></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>5</span></a></td>
<td><a href="#_Toc144362940"><span>Patient Name</span></a></td>
<td><a href="#_Toc144362940"><span>Doe,John H</span></a></td>
<td><a href="#_Toc144362940"><span>patient name</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>18</span></a></td>
<td><p><a href="#_Toc144362940"><span>Patient Account Number (FIN)</span></a></p>
<p><a href="#_Toc144362940"><span>-Populated for HL7 messages sent by VistA to Cerner</span></a></p></td>
<td></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>19</span></a></td>
<td><a href="#_Toc144362940"><span>SSN Number – Patient</span></a></td>
<td><a href="#_Toc144362940"><span>123456789</span></a></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>DG1</span></a></td>
<td><a href="#_Toc144362940"><span>3</span></a></td>
<td><a href="#_Toc144362940"><span>Diagnosis Code – DG1</span></a></td>
<td><a href="#_Toc144362940"><span>784.0^Headache</span></a></td>
<td><a href="#_Toc144362940"><span>coded element</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>PV1</span></a></td>
<td><a href="#_Toc144362940"><span>2</span></a></td>
<td><a href="#_Toc144362940"><span>Patient Class</span></a></td>
<td><a href="#_Toc144362940"><span>I</span></a></td>
<td><a href="#_Toc144362940"><span>table 4</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>3</span></a></td>
<td><a href="#_Toc144362940"><span>Patient Location</span></a></td>
<td><a href="#_Toc144362940"><span>32^234-4</span></a></td>
<td><a href="#_Toc144362940"><span>user table</span></a></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>7</span></a></td>
<td><a href="#_Toc144362940"><span>Attending Doctor</span></a></td>
<td><a href="#_Toc144362940"><span>1234^DOE, JOHN M</span></a></td>
<td><a href="#_Toc144362940"><span>composite ID</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>16</span></a></td>
<td><a href="#_Toc144362940"><span>VIP Indicator</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td><a href="#_Toc144362940"><span>user table</span></a></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>17</span></a></td>
<td><a href="#_Toc144362940"><span>Admitting Doctor</span></a></td>
<td><a href="#_Toc144362940"><span>1234^DOE, JOHN M</span></a></td>
<td><a href="#_Toc144362940"><span>composite ID</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>19</span></a></td>
<td><a href="#_Toc144362940"><span>Visit Number</span></a></td>
<td><a href="#_Toc144362940"><span>1241243</span></a></td>
<td><a href="#_Toc144362940"><span>composite ID</span></a></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>{ ORC}</span></a></td>
<td><a href="#_Toc144362940"><span>1</span></a></td>
<td><a href="#_Toc144362940"><span>Order Control</span></a></td>
<td><a href="#_Toc144362940"><span>NW</span></a></td>
<td><a href="#_Toc144362940"><span>table 119</span></a></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>2</span></a></td>
<td><a href="#_Toc144362940"><span>Placer Order Number</span></a></td>
<td><a href="#_Toc144362940"><span>234123;1^OR</span></a></td>
<td><a href="#_Toc144362940"><span>number^application</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>3</span></a></td>
<td><a href="#_Toc144362940"><span>Filler Order Number</span></a></td>
<td><a href="#_Toc144362940"><span>870745^GMRC</span></a></td>
<td><a href="#_Toc144362940"><span>number^application</span></a></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>5</span></a></td>
<td><a href="#_Toc144362940"><span>Order Status</span></a></td>
<td><a href="#_Toc144362940"><span>IP</span></a></td>
<td><a href="#_Toc144362940"><span>table 38</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>7</span></a></td>
<td><a href="#_Toc144362940"><span>Quantity/Timing</span></a></td>
<td><a href="#_Toc144362940"><span>^^^19940415^^R</span></a></td>
<td><p><a href="#_Toc144362940"><span>^^^timestamp^^priority</span></a></p>
<p><a href="#_Toc144362940"><span>coded per HL7 4.</span><span>4</span></a></p></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>9</span></a></td>
<td><a href="#_Toc144362940"><span>Date/Time of Transaction</span></a></td>
<td><a href="#_Toc144362940"><span>199404141425</span></a></td>
<td><a href="#_Toc144362940"><span>timestamp</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>10</span></a></td>
<td><a href="#_Toc144362940"><span>Entered By</span></a></td>
<td><a href="#_Toc144362940"><span>1166</span></a></td>
<td><a href="#_Toc144362940"><span>composite ID</span></a></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>12</span></a></td>
<td><a href="#_Toc144362940"><span>Ordering Provider</span></a></td>
<td><a href="#_Toc144362940"><span>1270</span></a></td>
<td><a href="#_Toc144362940"><span>composite ID</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>15</span></a></td>
<td><a href="#_Toc144362940"><span>Order Effective D/T</span></a></td>
<td><a href="#_Toc144362940"><span>199404141430</span></a></td>
<td><a href="#_Toc144362940"><span>timestamp</span></a></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>16</span></a></td>
<td><a href="#_Toc144362940"><span>Order Control Reason</span></a></td>
<td><a href="#_Toc144362940"><span>S^Service Correction^99ORN^^^</span></a></td>
<td><a href="#_Toc144362940"><span>coded element</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>NTE</span></a></td>
<td><a href="#_Toc144362940"><span>1</span></a></td>
<td><a href="#_Toc144362940"><span>Set ID</span></a></td>
<td><a href="#_Toc144362940"><span>16</span></a></td>
<td><a href="#_Toc144362940"><span>set ID</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>2</span></a></td>
<td><a href="#_Toc144362940"><span>Source of Comment</span></a></td>
<td><a href="#_Toc144362940"><span>L</span></a></td>
<td><a href="#_Toc144362940"><span>table 105</span></a></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>3</span></a></td>
<td><a href="#_Toc144362940"><span>Comment</span></a></td>
<td><a href="#_Toc144362940"><span>Cancelled by Service</span></a></td>
<td><a href="#_Toc144362940"><span>formatted text</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>OBR</span></a></td>
<td><a href="#_Toc144362940"><span>2</span></a></td>
<td><a href="#_Toc144362940"><span>Placer Order Number</span></a></td>
<td><a href="#_Toc144362940"><span>5587658;1^OR</span></a></td>
<td><a href="#_Toc144362940"><span>number^application</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>3</span></a></td>
<td><a href="#_Toc144362940"><span>Filler Order Number</span></a></td>
<td><a href="#_Toc144362940"><span>486410;GMRC^GMRC</span></a></td>
<td><a href="#_Toc144362940"><span>number^application</span></a></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>4</span></a></td>
<td><a href="#_Toc144362940"><span>Universal Service ID</span></a></td>
<td><a href="#_Toc144362940"><span>^^^58^Cardiology^99CON</span></a></td>
<td><a href="#_Toc144362940"><span>coded element</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>6</span></a></td>
<td><a href="#_Toc144362940"><span>Requested Date/Time</span></a></td>
<td><a href="#_Toc144362940"><span>20140311</span></a></td>
<td><a href="#_Toc144362940"><span>timestamp</span></a></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>16</span></a></td>
<td><a href="#_Toc144362940"><span>Cerner Ordering Provider</span></a></td>
<td><p><a href="#_Toc144362940"><span>For VistA to Cerner messages, the format of this field is:</span></a></p>
<p><a href="#_Toc144362940"><span>Provider NPI^provider last name^provider first name^provider middle name</span></a></p></td>
<td><a href="#_Toc144362940"><span>Free text</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>18</span></a></td>
<td><a href="#_Toc144362940"><span>Placer Field 1 (used for place of consultation</span></a></td>
<td><a href="#_Toc144362940"><span>B</span></a></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>19</span></a></td>
<td><p><a href="#_Toc144362940"><span>Placer Field 2 (used for attention)</span></a></p>
<p><a href="#_Toc144362940"><span>Between VistA and Cerner, populated with Field #508 Cerner Placer Field 1 in the REQUEST/CONSULTATION file (#123)</span></a></p></td>
<td><a href="#_Toc144362940"><span>1044</span></a></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>20</span></a></td>
<td><p><a href="#_Toc144362940"><span>Filler Field 1</span></a></p>
<p><a href="#_Toc144362940"><span>Between VistA and Cerner, populated with Field #511 OPT IN FOR FINAL STATUS in the REQUEST/CONSULTATION file (#123)</span></a></p></td>
<td><a href="#_Toc144362940"><span>Y or N</span></a></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>22</span></a></td>
<td><a href="#_Toc144362940"><span>Results Rpt/Status Change - Date/Time</span></a></td>
<td><a href="#_Toc144362940"><span>199404150635</span></a></td>
<td><a href="#_Toc144362940"><span>timestamp</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>25</span></a></td>
<td><a href="#_Toc144362940"><span>Result Status</span></a></td>
<td><a href="#_Toc144362940"><span>F</span></a></td>
<td><a href="#_Toc144362940"><span>table 123</span></a></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>27</span></a></td>
<td><p><a href="#_Toc144362940"><span>Quantity/Timing</span></a></p>
<p><a href="#_Toc144362940"><span>Between VistA and Cerner, component 4 populated with Field #512 PERFORMED DATE/TIME in the REQUEST/CONSULTATION file (#123)</span></a></p></td>
<td><a href="#_Toc144362940"><span>^^^202305030933+0600</span></a></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>32</span></a></td>
<td><a href="#_Toc144362940"><span>Principle Result Interpreter</span></a></td>
<td><a href="#_Toc144362940"><span>1345</span></a></td>
<td><a href="#_Toc144362940"><span>composite ID</span></a></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>ZSV</span></a></td>
<td><a href="#_Toc144362940"><span>1</span></a></td>
<td><a href="#_Toc144362940"><span>Request Service ID</span></a></td>
<td><a href="#_Toc144362940"><span>^^^12^Psychiatry^99CON</span></a></td>
<td><a href="#_Toc144362940"><span>coded element</span></a></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>2</span></a></td>
<td><a href="#_Toc144362940"><span>Consult Type</span></a></td>
<td><a href="#_Toc144362940"><span>Family Counseling</span></a></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>{ OBX }</span></a></td>
<td><a href="#_Toc144362940"><span>1</span></a></td>
<td><a href="#_Toc144362940"><span>Set ID</span></a></td>
<td><a href="#_Toc144362940"><span>1</span></a></td>
<td><a href="#_Toc144362940"><span>number</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>2</span></a></td>
<td><a href="#_Toc144362940"><span>Value Type</span></a></td>
<td><a href="#_Toc144362940"><span>TX</span></a></td>
<td><a href="#_Toc144362940"><span>table 125</span></a></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>3</span></a></td>
<td><a href="#_Toc144362940"><span>Observation ID</span></a></td>
<td><a href="#_Toc144362940"><span>2000.02^Reason for Request^AS4</span></a></td>
<td><a href="#_Toc144362940"><span>coded element</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td><a href="#_Toc144362940"><span>4</span></a></td>
<td><a href="#_Toc144362940"><span>Observation Sub-ID</span></a></td>
<td><a href="#_Toc144362940"><span>1</span></a></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="even">
<td></td>
<td><a href="#_Toc144362940"><span>5</span></a></td>
<td><a href="#_Toc144362940"><span>Observation Value</span></a></td>
<td><a href="#_Toc144362940"><span>r/o TB</span></a></td>
<td><a href="#_Toc144362940"><span>string</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>}</span></a></td>
<td><a href="#_Toc144362940"><span>8</span></a></td>
<td><a href="#_Toc144362940"><span>Abnormal Flag</span></a></td>
<td><a href="#_Toc144362940"><span>N</span></a></td>
<td><a href="#_Toc144362940"><span>table 78</span></a></td>
</tr>
</tbody>
</table>

[[The following items merit emphasis:](#_Toc144362941)](#_Toc144362940)

- 
- 
- 
- 
- 
- 
- 
- 
- - 
  - 
  - 
  - 
  - 
  - 
  - 
  - 
- - 
  - 
  - 
  - 
  - 
  - 
  - 
  - 
  - 
  - 
- 
- 
- - 
  - 
  - 
- 
- - 
  - 
  - 
- 

[[Sending Application is the name of the DHCP package generating the message; Sending Facility is the station number.Originating Referral Identifier is the IEN of the record entry in the Request/Consultation file.Patient ID is patient DFN (pointer to file 2)Patient Location, for an inpatient, is Hospital Location IEN^Room-Bed. For and outpatient, it is the Hospital Location IEN. In both cases it is the location from which the order is being placed.VIP Indicator is ‘R’ if patient is restricted/sensitive.Visit Number is the IEN of the visit in the Visit file.Placer Order Number is the OE/RR order number.Filler Order Number is the Consult order number.Order Status is needed when Consults releases an order; possible values from HL7 table 38 include the following:DC: Discontinued SC: Active A: Partial ResultsCM: Completed ZC: Scheduled CA: Cancelled (Denied)IP: PendingRP: DC’d due to EditQuantity/Timing will contain Clinically Indicated Date in the fourth ^-piece and urgency in the sixth ^-piece, whose possible values include:S: StatZ24: Within 24 hoursZW: Within 1 weekR: Routine Z48: Within 48 hoursZM: Within 1 monthZT: TodayZ72: Within 72 hoursZNA: Next availableZE: Emergency Entered By and Ordering Provider are IENs in the New Person file.Universal Service ID is a national code in the first part. The alternate code is a pointer to either the Request Services or GMRC Procedures file.Placer Field 1 will contain the place of consultation, as a set of codes. Possible values include:B: BedsideE: Emergency RoomOC: Consultant’s choicePlacer Field 2 will contain the IEN in the New Person file of the user to whom this consult should be directed.The OBX segment is used to transmit related data about the patient when placing a consult request; possible observation IDs include:Reason for Request (AS4 2000.02) = textProvisional Diagnosis (not coded) = textProvisional Diagnosis (coded element) = ICD ^ textObservation ID is used for ordering OBX segments.](#_Toc144362941)](#_Toc144362940)

[[Patch GMRC\*3.0\*75 added the capability of using the following HL7 protocols to enable the communications between the consult system communication with the Healthcare Claims Processing System (HCPS), which processes non-VA healthcare. Refer to Table 14-2.](#_Toc144362941)](#_Toc144362940)

[[<span id="_Toc169170360" class="anchor"></span>Table 14‑2: Patch GMRC\*3.0\*75 Protocol Description](#_Toc144362941)](#_Toc144362940)

| [[Protocol](#_Toc144361714)](#_Toc144362940)                | [[Description](#_Toc144361714)](#_Toc144362940)                                                                                                                     |
|-------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [[GMRC CONSULTS TO HCP](#_Toc144361714)](#_Toc144362940)    | [[Creates and sends an REF^12, REF^13, or REF^14 HL7 message to the HCPS application when a consult is generated for Non-VA Care.](#_Toc144361714)](#_Toc144362940) |
| [[GMRC HCP REF-I12 SERVER](#_Toc144361714)](#_Toc144362940) | [[Sends REF^I12 HL7 messages to the HCPS application for new Non-VA Care Referrals.](#_Toc144361714)](#_Toc144362940)                                               |
| [[GMRC HCP REF-I12 CLIENT](#_Toc144361714)](#_Toc144362940) | [[Sends REF^I12 HL7 messages to the HCPS application for new Non-VA Care referrals.](#_Toc144361714)](#_Toc144362940)                                               |
| [[GMRC HCP REF-I13 SERVER](#_Toc144361714)](#_Toc144362940) | [[Sends HL7 REF^I13 messages to CPRS application for updated Non-VA Care Referrals originating in HCPS (RAS).](#_Toc144361714)](#_Toc144362940)                     |
| [[GMRC HCP REF-I13 CLIENT](#_Toc144361714)](#_Toc144362940) | [[Sends HL7 REF^I13 messages from HCPS to CPRS application for updated Non-VA Care Referrals originating in HCPS (RAS).](#_Toc144361714)](#_Toc144362940)           |
| [[GMRC HCP RRI-I13 SERVER](#_Toc144361714)](#_Toc144362940) | [[Sends HL7 RRI^I13 messages to CPRS application for updated Non-VA Care Referrals originating in HCPS (RAS).](#_Toc144361714)](#_Toc144362940)                     |
| [[GMRC HCP RRI-I13 CLIENT](#_Toc144361714)](#_Toc144362940) | [[Sends HL7 RRI^I13 messages from HCPS to CPRS application for updated Non-VA Care Referrals originating in HCPS (RAS).](#_Toc144361714)](#_Toc144362940)           |
| [[GMRC HCP REF-I14 SERVER](#_Toc144361714)](#_Toc144362940) | [[Sends REF^I14 HL7 messages to the HCPS application for canceled or discontinued Non-VA Care referrals.](#_Toc144361714)](#_Toc144362940)                          |
| [[GMRC HCP REF-I14 CLIENT](#_Toc144361714)](#_Toc144362940) | [[Sends REF^I14 HL7 messages to the HCPS application for cancelled or discontinued Non-VA Care referrals.](#_Toc144361714)](#_Toc144362940)                         |

[[Patch GMRC\*3.0\*99 added the capability of using the following HL7 protocols to enable the communications between the consult system communication with CCRA for Non-VA COMMUNITY CARE consults. Refer to Table 14-3.](#_Toc144361714)](#_Toc144362940)

[[<span id="_Toc169170361" class="anchor"></span>Table 14‑3: Patch GMRC\*3.0\*99 Protocol Description](#_Toc144361714)](#_Toc144362940)

| [[Protocol](#_Toc144361714)](#_Toc144362940)                      | [[Description](#_Toc144361714)](#_Toc144362940)                                                                                                       |
|-------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| [[GMRC CCRA REF-I12 CLIENT](#_Toc144361714)](#_Toc144362940)      | [[Sends HL7 REF^I12 v2.5 messages from CCRA to HSRM application for new Non-VA Care Referrals.](#_Toc144361714)](#_Toc144362940)                      |
| [[GMRC CCRA REF-I13 CLIENT](#_Toc144361714)](#_Toc144362940)      | [[Sends HL7 REF^I13 v2.5 messages to CCRA application for updated Non-VA Care Referrals.](#_Toc144361714)](#_Toc144362940)                            |
| [[GMRC CCRA REF-I14 CLIENT](#_Toc144361714)](#_Toc144362940)      | [[Sends HL7 REF^I14 v2.5 messages from CPRS to CCRA application for canceled or discontinued Non-VA Care Referrals.](#_Toc144361714)](#_Toc144362940) |
| [[GMRC CCRA-HSRM REF-I12 SERVER](#_Toc144361714)](#_Toc144362940) | [[Sends HL7 REF^I12 v2.5 messages from CPRS to CCRA application for new Non-VA Care Referrals.](#_Toc144361714)](#_Toc144362940)                      |
| [[GMRC CCRA-HSRM REF-I13 SERVER](#_Toc144361714)](#_Toc144362940) | [[Sends HL7 REF^I13 v2.5 messages from CPRS to CCRA application for new Non-VA Care Referrals.](#_Toc144361714)](#_Toc144362940)                      |
| [[GMRC CCRA-HSRM REF-I14 SERVER](#_Toc144361714)](#_Toc144362940) | [[Sends HL7 REF^I14 v2.5 messages from CPRS to CCRA application for cancellation of Non-VA Care Referrals.](#_Toc144361714)](#_Toc144362940)          |

[[Patch GMRC\*3.0\*123 added the capability of using the following HL7 protocols to enable the communications between the consult system communication with CCRA for Non-VA COMMUNITY CARE consults. Refer to Table 14-4.](#_Toc144361714)](#_Toc144362940)

[[<span id="_Toc169170362" class="anchor"></span>Table 14‑4: Patch GMRC\*3.0\*123 Protocol Description](#_Toc144361714)](#_Toc144362940)

| [[Protocol](#_Toc144361714)](#_Toc144362940)                      | [[Description](#_Toc144361714)](#_Toc144362940)                                                                                                                              |
|-------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [[GMRC HSRM-CCRA REF-I13 CLIENT](#_Toc144361714)](#_Toc144362940) | [[Sends HL7 REF^I13 v2.5 messages from HSRM application to CPRS. This is to update the consult record with new status (scheduled/complete)](#_Toc144361714)](#_Toc144362940) |
| [[GMRC HSRM-CCRA REF-I13 SERVER](#_Toc144361714)](#_Toc144362940) | [[Sends HL7 REF^I12 v2.5 messages from HSRM application to CPRS This is for consult status updates from HSRM](#_Toc144361714)](#_Toc144362940)                               |
| [[GMRC HSRM-CCRA REF-I14 CLIENT](#_Toc144361714)](#_Toc144362940) | [[Sends HL7 REF^I14 v2.5 messages from HSRM application to CPRS. This message type is to send to VistA an update to cancel the consult](#_Toc144361714)](#_Toc144362940)     |
| [[GMRC HSRM-CCRA REF-I14 SERVER](#_Toc144361714)](#_Toc144362940) | [[Sends HL7 REF^I12 v2.5 messages from HSRM application to CPRS. This is for consult status updates - cancel appointment.](#_Toc144361714)](#_Toc144362940)                  |

[[Patch GMRC\*3.0\*75 added the capability of using the following HL7 application parameters to enable communication between the consult system and the HCPS. Refer to Table 14-5.](#_Toc144361714)](#_Toc144362940)

[[<span id="_Toc169170363" class="anchor"></span>Table 14‑5: Patch GMRC\*3.0\*75 Application Parameters](#_Toc144361714)](#_Toc144362940)

| [[Protocol](#_Toc144361714)](#_Toc144362940)         | [[Description](#_Toc144361714)](#_Toc144362940)                                              |
|------------------------------------------------------|----------------------------------------------------------------------------------------------|
| [[GMRC HCP SEND](#_Toc144361714)](#_Toc144362940)    | [[This parameter is used to set up the sending facility.](#_Toc144361714)](#_Toc144362940)   |
| [[GMRC HCP RECEIVE](#_Toc144361714)](#_Toc144362940) | [[This parameter is used to set up the receiving facility.](#_Toc144361714)](#_Toc144362940) |

[[Patch GMRC\*3.0\*99 added the capability of using the following HL7 application parameters to enable communication between the consult system and the CCRA. Refer to Table 14-6.](#_Toc144361714)](#_Toc144362940)

[[<span id="_Toc169170364" class="anchor"></span>Table 14‑6: Patch GMRC\*3.0\*99 Application Parameters](#_Toc144361714)](#_Toc144362940)

| [[Protocol](#_Toc144361714)](#_Toc144362940)          | [[Description](#_Toc144361714)](#_Toc144362940)                                              |
|-------------------------------------------------------|----------------------------------------------------------------------------------------------|
| [[GMRC CCRA SEND](#_Toc144361714)](#_Toc144362940)    | [[This parameter is used to set up the sending facility.](#_Toc144361714)](#_Toc144362940)   |
| [[GMRC CCRA RECEIVE](#_Toc144361714)](#_Toc144362940) | [[This parameter is used to set up the receiving facility.](#_Toc144361714)](#_Toc144362940) |

[[Patch GMRC\*3.0\*123 added the capability of using the following HL7 application parameters to enable communication between the consult system and the CCRA. Refer to Table 14-7.](#_Toc144361714)](#_Toc144362940)

[[<span id="_Toc169170365" class="anchor"></span>Table 14‑7: Patch GMRC\*3.0\*123 Application Parameters](#_Toc144361714)](#_Toc144362940)

| [[Protocol](#_Toc144361714)](#_Toc144362940)               | [[Description](#_Toc144361714)](#_Toc144362940)                                              |
|------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| [[GMRC HSRM-CCRA SEND](#_Toc144361714)](#_Toc144362940)    | [[This parameter is used to set up the sending facility.](#_Toc144361714)](#_Toc144362940)   |
| [[GMRC HSRM-CCRA RECEIVE](#_Toc144361714)](#_Toc144362940) | [[This parameter is used to set up the receiving facility.](#_Toc144361714)](#_Toc144362940) |

[[HL7 Logical Links include the following:](#_Toc144361714)](#_Toc144362940)

- 
- 
- - - 
  - 

[[GMRCHCP: This Logical link is used to setup the network path between Consults and Healthcare Claims Processing System (HCPS).GMRCCCRA: This Logical link is used to set up the network path between CPRS and CCRA. This was created by patch GMRC\*3.0\*99CCRA-NAK: This logical link is used to send HSRM an application NAK when a message is rejected because the user does not exist or have permissions in VistA to make updates. This was created by patch GMRC\*3.0\*123GMRC\*3.0\*99: To enable the HL7 interface link created by this patch, go into the VistA HL main menu, and select the Filer and Link Management Options. From there, select the SL Stop/Start Links option, as shown below.Once this logical link is thus enabled, messages can proceed through the interface.GMRC\*3.0\*106: This logical link is the same as the one for GMRC\*3.0\*99.](#_Toc144361714)](#_Toc144362940)

[[Patch GMRC\*3.0\*75 added the capability of using the following HL7 referral messages to enable communication between the consult system and HCPS.](#_Toc144361714)](#_Toc144362940)

- 
- 
- 
- 
- 

| [[Segment](#_Toc144361714)](#_Toc144362940) | [[Description](#_Toc144361714)](#_Toc144362940)            | [[Required/Optional](#_Toc144361714)](#_Toc144362940)            |
|---------------------------------------------|------------------------------------------------------------|------------------------------------------------------------------|
| [[MSH:](#_Toc144361714)](#_Toc144362940)    | [[Message Header](#_Toc144361714)](#_Toc144362940)         | [[REQUIRED](#_Toc144361714)](#_Toc144362940)                     |
| [[RF1](#_Toc144361714)](#_Toc144362940)     | [[Referral Information](#_Toc144361714)](#_Toc144362940)   | [[REQUIRED](#_Toc144361714)](#_Toc144362940)                     |
| [[PRD](#_Toc144361714)](#_Toc144362940)     | [[Provider Data](#_Toc144361714)](#_Toc144362940)          | [[REQUIRED](#_Toc144361714)](#_Toc144362940)                     |
| [[PID](#_Toc144361714)](#_Toc144362940)     | [[Patient Identification](#_Toc144361714)](#_Toc144362940) | [[REQUIRED](#_Toc144361714)](#_Toc144362940)                     |
| [[IN1](#_Toc144361714)](#_Toc144362940)     |                                                            | [[Patient Insurance (Optional)](#_Toc144361714)](#_Toc144362940) |
| [[IN3](#_Toc144361714)](#_Toc144362940)     |                                                            | [[Patient Insurance (Optional)](#_Toc144361714)](#_Toc144362940) |
| [[DG1](#_Toc144361714)](#_Toc144362940)     | [[Diagnosis](#_Toc144361714)](#_Toc144362940)              | [[OPTIONAL](#_Toc144361714)](#_Toc144362940)                     |
| [[OBR](#_Toc144361714)](#_Toc144362940)     | [[Observation Request](#_Toc144361714)](#_Toc144362940)    | [[REQUIRED](#_Toc144361714)](#_Toc144362940)                     |
| [[PV1](#_Toc144361714)](#_Toc144362940)     | [[Patient Visit](#_Toc144361714)](#_Toc144362940)          | [[REQUIRED](#_Toc144361714)](#_Toc144362940)                     |
| [[NTE](#_Toc144361714)](#_Toc144362940)     | [[Notes and Comments](#_Toc144361714)](#_Toc144362940)     | [[REQUIRED](#_Toc144361714)](#_Toc144362940)                     |

[[A standard HL7 v2.5 RRI message will be generated for status updates and/or changes made to an existing referral in HCPS. This event triggers a message to update CPRS with changes made in HCPS. The RRI message will contain the standard segments listed and described in Table 14-9.](#_Toc144361714)](#_Toc144362940)

[[<span id="_Toc169170367" class="anchor"></span>Table 14‑9: RRI Message Standard Segments](#_Toc144363004)](#_Toc144362940)

| [[Segment](#_Toc144361726)](#_Toc144362940) | [[Description](#_Toc144361726)](#_Toc144362940)                 | [[Required/Optional](#_Toc144361726)](#_Toc144362940) |
|---------------------------------------------|-----------------------------------------------------------------|-------------------------------------------------------|
| [[MSH](#_Toc144361726)](#_Toc144362940)     | [[Message Header](#_Toc144361726)](#_Toc144362940)              | [[REQUIRED](#_Toc144361726)](#_Toc144362940)          |
| [[RRI](#_Toc144361726)](#_Toc144362940)     | [[Return Referral Information](#_Toc144361726)](#_Toc144362940) | [[REQUIRED](#_Toc144361726)](#_Toc144362940)          |
| [[PRD](#_Toc144361726)](#_Toc144362940)     | [[Provider Data](#_Toc144361726)](#_Toc144362940)               | [[REQUIRED](#_Toc144361726)](#_Toc144362940)          |
| [[PID](#_Toc144361726)](#_Toc144362940)     | [[Patient Identification](#_Toc144361726)](#_Toc144362940)      | [[REQUIRED](#_Toc144361726)](#_Toc144362940)          |
| [[DG1](#_Toc144361726)](#_Toc144362940)     | [[Diagnosis](#_Toc144361726)](#_Toc144362940)                   | [[OPTIONAL](#_Toc144361726)](#_Toc144362940)          |
| [[OBR](#_Toc144361726)](#_Toc144362940)     | [[Observation Request](#_Toc144361726)](#_Toc144362940)         | [[REQUIRED](#_Toc144361726)](#_Toc144362940)          |
| [[PV1](#_Toc144361726)](#_Toc144362940)     | [[Patient Visit](#_Toc144361726)](#_Toc144362940)               | [[REQUIRED](#_Toc144361726)](#_Toc144362940)          |
| [[NTE](#_Toc144361726)](#_Toc144362940)     | [[Notes and Comments](#_Toc144361726)](#_Toc144362940)          | [[REQUIRED](#_Toc144361726)](#_Toc144362940)          |

[[The following tables contain the HL7 message definition for the REF/RRI/ACK messages. Table columns include the following:](#_Toc144361726)](#_Toc144362940)

1.  
2.  
3.  
4.  
5.  
6.  
7.  

[[SEQ = HL7 sequence#LEN = HL7 field lengthDT = HL7 data typeR/O = R=Require, O=Optional, C=Conditional, NS=Not supportedTBL = HL7 table definitionElement Name = HL7 field nameVistA Description = information on what will be pulled from VistA for this element, or hard-coded data.](#_Toc144361726)](#_Toc144362940)

| [[SEQ](#_Toc144361727)](#_Toc144362940)  | [[LEN](#_Toc144361727)](#_Toc144362940)          | [[DT](#_Toc144361727)](#_Toc144362940)      | [[R/O](#_Toc144361727)](#_Toc144362940) | [[TBL#](#_Toc144361727)](#_Toc144362940) | [[Element Name](#_Toc144361727)](#_Toc144362940)                    | [[VistA Description](#_Toc144361727)](#_Toc144362940)                                                                              |
|------------------------------------------|--------------------------------------------------|---------------------------------------------|-----------------------------------------|------------------------------------------|---------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| [[1](#_Toc144361727)](#_Toc144362940)    | [[1](#_Toc144361727)](#_Toc144362940)            | [[ST](#_Toc144361727)](#_Toc144362940)      | [[R](#_Toc144361727)](#_Toc144362940)   |                                          | [[Field Separator](#_Toc144361727)](#_Toc144362940)                 | [[\|](#_Toc144361727)](#_Toc144362940)                                                                                             |
| [[2](#_Toc144361727)](#_Toc144362940)    | [[4](#_Toc144361727)](#_Toc144362940)            | [[ST](#_Toc144361727)](#_Toc144362940)      | [[R](#_Toc144361727)](#_Toc144362940)   |                                          | [[Encoding Characters](#_Toc144361727)](#_Toc144362940)             | [[^~\\](#_Toc144361727)](#_Toc144362940)                                                                                           |
| [[3](#_Toc144361727)](#_Toc144362940)    | [[15](#_Toc144361727)](#_Toc144362940)           | [[ST](#_Toc144361727)](#_Toc144362940)      | [[R](#_Toc144361727)](#_Toc144362940)   |                                          | [[Sending Application](#_Toc144361727)](#_Toc144362940)             | [[GMRC HCP SEND](#_Toc144361727)](#_Toc144362940)                                                                                  |
| [[4](#_Toc144361727)](#_Toc144362940)    | [[20](#_Toc144361727)](#_Toc144362940)           | [[ST](#_Toc144361727)](#_Toc144362940)      | [[R](#_Toc144361727)](#_Toc144362940)   |                                          | [[Sending Facility](#_Toc144361727)](#_Toc144362940)                | [[Sending Facility, from the FACILITY NAME field of the HL7 APPLICATION entry GMRC HCP SEND](#_Toc144361727)](#_Toc144362940)      |
| [[5](#_Toc144361727)](#_Toc144362940)    | [[30](#_Toc144361727)](#_Toc144362940)           | [[ST](#_Toc144361727)](#_Toc144362940)      | [[R](#_Toc144361727)](#_Toc144362940)   |                                          | [[Receiving Application](#_Toc144361727)](#_Toc144362940)           | [[GMRC HCP RECEIVE](#_Toc144361727)](#_Toc144362940)                                                                               |
| [[6](#_Toc144361727)](#_Toc144362940)    | [[30](#_Toc144361727)](#_Toc144362940)           | [[ST](#_Toc144361727)](#_Toc144362940)      | [[NS](#_Toc144361727)](#_Toc144362940)  |                                          | [[Receiving Facility](#_Toc144361727)](#_Toc144362940)              | [[Receiving Facility, from the FACILITY NAME field of the HL7 APPLICATION entry GMRC HCP RECEIVE](#_Toc144361727)](#_Toc144362940) |
| [[7](#_Toc144361727)](#_Toc144362940)    | [[26](#_Toc144361727)](#_Toc144362940)           | [[TS](#_Toc144361727)](#_Toc144362940)      | [[R](#_Toc144361727)](#_Toc144362940)   |                                          | [[Date/Time Of Message](#_Toc144361727)](#_Toc144362940)            | [[System date/time generated by the VistA HL7 package](#_Toc144361727)](#_Toc144362940)                                            |
| [[8](#_Toc144361727)](#_Toc144362940)    | [[40](#_Toc144361727)](#_Toc144362940)           | [[ST](#_Toc144361727)](#_Toc144362940)      | [[NS](#_Toc144361727)](#_Toc144362940)  |                                          | [[Security](#_Toc144361727)](#_Toc144362940)                        | [[Not used](#_Toc144361727)](#_Toc144362940)                                                                                       |
| [[9](#_Toc144361727)](#_Toc144362940)    | [[7](#_Toc144361727)](#_Toc144362940)            | [[CM](#_Toc144361727)](#_Toc144362940)      | [[R](#_Toc144361727)](#_Toc144362940)   | [[0076](#_Toc144361727)](#_Toc144362940) |                                                                     |                                                                                                                                    |
| [[0003](#_Toc144361727)](#_Toc144362940) | [[Message Type](#_Toc144361727)](#_Toc144362940) | [[REF^I12](#_Toc144361727)](#_Toc144362940) |                                         |                                          |                                                                     |                                                                                                                                    |
| [[10](#_Toc144361727)](#_Toc144362940)   | [[20](#_Toc144361727)](#_Toc144362940)           | [[ST](#_Toc144361727)](#_Toc144362940)      | [[R](#_Toc144361727)](#_Toc144362940)   |                                          | [[Message Control ID](#_Toc144361727)](#_Toc144362940)              | [[Facility and sequence number automatically generated by the VistA HL7 Package](#_Toc144361727)](#_Toc144362940)                  |
| [[11](#_Toc144361727)](#_Toc144362940)   | [[1](#_Toc144361727)](#_Toc144362940)            | [[ID](#_Toc144361727)](#_Toc144362940)      | [[R](#_Toc144361727)](#_Toc144362940)   |                                          | [[Processing ID](#_Toc144361727)](#_Toc144362940)                   | [[P for Production, T for Test](#_Toc144361727)](#_Toc144362940)                                                                   |
| [[12](#_Toc144361727)](#_Toc144362940)   | [[8](#_Toc144361727)](#_Toc144362940)            | [[ID](#_Toc144361727)](#_Toc144362940)      | [[R](#_Toc144361727)](#_Toc144362940)   | [[0104](#_Toc144361727)](#_Toc144362940) | [[Version ID](#_Toc144361727)](#_Toc144362940)                      | [[2.](#_Toc144361727)[5](#_Toc144362934)](#_Toc144362940)                                                                          |
| [[13](#_Toc144362934)](#_Toc144362940)   | [[15](#_Toc144362934)](#_Toc144362940)           | [[NM](#_Toc144362934)](#_Toc144362940)      | [[NS](#_Toc144362934)](#_Toc144362940)  |                                          | [[Sequence Number](#_Toc144362934)](#_Toc144362940)                 | [[Not used](#_Toc144362934)](#_Toc144362940)                                                                                       |
| [[14](#_Toc144362934)](#_Toc144362940)   | [[180](#_Toc144362934)](#_Toc144362940)          | [[ST](#_Toc144362934)](#_Toc144362940)      | [[NS](#_Toc144362934)](#_Toc144362940)  |                                          | [[Continuation Pointer](#_Toc144362934)](#_Toc144362940)            | [[Not used](#_Toc144362934)](#_Toc144362940)                                                                                       |
| [[15](#_Toc144362934)](#_Toc144362940)   | [[2](#_Toc144362934)](#_Toc144362940)            | [[ID](#_Toc144362934)](#_Toc144362940)      | [[R](#_Toc144362934)](#_Toc144362940)   | [[0155](#_Toc144362934)](#_Toc144362940) | [[Accept Acknowledgment Type](#_Toc144362934)](#_Toc144362940)      | [[AL=Always](#_Toc144362934)](#_Toc144362940)                                                                                      |
| [[16](#_Toc144362934)](#_Toc144362940)   | [[2](#_Toc144362934)](#_Toc144362940)            | [[ID](#_Toc144362934)](#_Toc144362940)      | [[R](#_Toc144362934)](#_Toc144362940)   | [[0155](#_Toc144362934)](#_Toc144362940) | [[Application Acknowledgment Type](#_Toc144362934)](#_Toc144362940) | [[AL=Always](#_Toc144362934)](#_Toc144362940)                                                                                      |
| [[17](#_Toc144362934)](#_Toc144362940)   | [[3](#_Toc144362934)](#_Toc144362940)            | [[ID](#_Toc144362934)](#_Toc144362940)      | [[R](#_Toc144362934)](#_Toc144362940)   | [[0399](#_Toc144362934)](#_Toc144362940) | [[Country Code](#_Toc144362934)](#_Toc144362940)                    | [[USA](#_Toc144362934)](#_Toc144362940)                                                                                            |

[[Note the following:](#_Toc144362934)](#_Toc144362940)

- 
- 

| [[SEQ](#_Toc144361728)](#_Toc144362940)                                                                         | [[LEN](#_Toc144361728)](#_Toc144362940) | [[DT](#_Toc144361728)](#_Toc144362940) | [[R/O](#_Toc144361728)](#_Toc144362940) | [[TBL#](#_Toc144361728)](#_Toc144362940) | [[Element Name](#_Toc144361728)](#_Toc144362940)                    | [[VistA Description](#_Toc144361728)](#_Toc144362940)                                                                                                                                                        |
|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------|----------------------------------------|-----------------------------------------|------------------------------------------|---------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [[1](#_Toc144361728)](#_Toc144362940)                                                                           | [[250](#_Toc144361728)](#_Toc144362940) | [[CE](#_Toc144361728)](#_Toc144362940) | [[O](#_Toc144361728)](#_Toc144362940)   | [[0283](#_Toc144361728)](#_Toc144362940) | [[Referral Status](#_Toc144361728)](#_Toc144362940)                 | [[NW^CPRS RELEASED ORDER](#_Toc144361728)](#_Toc144362940)                                                                                                                                                   |
| [[2](#_Toc144361728)](#_Toc144362940)                                                                           | [[250](#_Toc144361728)](#_Toc144362940) | [[CE](#_Toc144361728)](#_Toc144362940) | [[O](#_Toc144361728)](#_Toc144362940)   | [[0280](#_Toc144361728)](#_Toc144362940) | [[Referral Priority](#_Toc144361728)](#_Toc144362940)               | [[From File 123, Field 5 (Urgency). Values are: 1 WEEK, NEXT AVAILABLE, ROUTINE, STAT, TODAY, TOMORROW AM, WITHIN 1 MONTH, WITHIN 1 WEEK, WITHIN 24 HOURS, WITHIN 72 HOURS](#_Toc144361728)](#_Toc144362940) |
| [[3](#_Toc144361728)](#_Toc144362940)                                                                           | [[250](#_Toc144361728)](#_Toc144362940) | [[CE](#_Toc144361728)](#_Toc144362940) | [[O](#_Toc144361728)](#_Toc144362940)   |                                          | [[Referral Type](#_Toc144361728)](#_Toc144362940)                   | [[Service IEN^Service Name^^Template IEN](#_Toc144361728)](#_Toc144362940)                                                                                                                                   |
| [[^Template Name](#_Toc144361728)](#_Toc144362940)                                                              |                                         |                                        |                                         |                                          |                                                                     |                                                                                                                                                                                                              |
| [[Service IEN is pointer to File 123.5, Template IEN is pointer to File 8927.](#_Toc144361728)](#_Toc144362940) |                                         |                                        |                                         |                                          |                                                                     |                                                                                                                                                                                                              |
| [[4](#_Toc144361728)](#_Toc144362940)                                                                           | [[250](#_Toc144361728)](#_Toc144362940) | [[CE](#_Toc144361728)](#_Toc144362940) | [[NS](#_Toc144361728)](#_Toc144362940)  |                                          | [[Referral Disposition](#_Toc144361728)](#_Toc144362940)            | [[Not used](#_Toc144361728)](#_Toc144362940)                                                                                                                                                                 |
| [[5](#_Toc144361728)](#_Toc144362940)                                                                           | [[250](#_Toc144361728)](#_Toc144362940) | [[CE](#_Toc144361728)](#_Toc144362940) | [[O](#_Toc144361728)](#_Toc144362940)   | [[0284](#_Toc144361728)](#_Toc144362940) | [[Referral Category](#_Toc144361728)](#_Toc144362940)               | [[I for Inpatient, O for Outpatient based on File 123, field 14 (Service Rendered as In or Out). This could be different than the PV1.1 current patient status.](#_Toc144361728)](#_Toc144362940)            |
| [[6](#_Toc144361728)](#_Toc144362940)                                                                           | [[30](#_Toc144361728)](#_Toc144362940)  | [[EI](#_Toc144361728)](#_Toc144362940) | [[R](#_Toc144361728)](#_Toc144362940)   |                                          | [[Originating Referral Identifier](#_Toc144361728)](#_Toc144362940) | [[IEN to File 123](#_Toc144361728)](#_Toc144362940)                                                                                                                                                          |
| [[7](#_Toc144361728)](#_Toc144362940)                                                                           | [[26](#_Toc144361728)](#_Toc144362940)  | [[TS](#_Toc144361728)](#_Toc144362940) | [[O](#_Toc144361728)](#_Toc144362940)   |                                          | [[Effective Date](#_Toc144361728)](#_Toc144362940)                  | [[Referral Date of Request from File 123, field .01](#_Toc144361728)](#_Toc144362940)                                                                                                                        |
| [[8](#_Toc144361728)](#_Toc144362940)                                                                           | [[26](#_Toc144361728)](#_Toc144362940)  | [[TS](#_Toc144361728)](#_Toc144362940) | [[NS](#_Toc144361728)](#_Toc144362940)  |                                          | [[Expiration Date](#_Toc144361728)](#_Toc144362940)                 | [[Not used](#_Toc144361728)](#_Toc144362940)                                                                                                                                                                 |
| [[9](#_Toc144361728)](#_Toc144362940)                                                                           | [[26](#_Toc144361728)](#_Toc144362940)  | [[TS](#_Toc144361728)](#_Toc144362940) | [[NS](#_Toc144361728)](#_Toc144362940)  |                                          | [[Process Date](#_Toc144361728)](#_Toc144362940)                    | [[Not used](#_Toc144361728)](#_Toc144362940)                                                                                                                                                                 |
| [[10](#_Toc144361728)](#_Toc144362940)                                                                          | [[250](#_Toc144361728)](#_Toc144362940) | [[CE](#_Toc144361728)](#_Toc144362940) | [[NS](#_Toc144361728)](#_Toc144362940)  |                                          | [[Referral Reason](#_Toc144361728)](#_Toc144362940)                 | [[Not used](#_Toc144361728)](#_Toc144362940)                                                                                                                                                                 |
| [[11](#_Toc144361728)](#_Toc144362940)                                                                          | [[30](#_Toc144361728)](#_Toc144362940)  | [[EI](#_Toc144361728)](#_Toc144362940) | [[NS](#_Toc144361728)](#_Toc144362940)  |                                          | [[External Referral Identifier](#_Toc144361728)](#_Toc144362940)    | [[Not used](#_Toc144361728)](#_Toc144362940)                                                                                                                                                                 |

[[Refer to Table 14-12.](#_Toc144361728) [Note REF_I12 PRD - Provider Data Segment is the same for all message types.](#_Toc144363007)](#_Toc144362940)

[[<span id="_Toc169170370" class="anchor"></span>Table 14‑12: REF_I12 PRD - Provider Data Segment](#_Toc144363007)](#_Toc144362940)

| [[SEQ](#_Toc144361729)](#_Toc144362940)                              | [[LEN](#_Toc144361729)](#_Toc144362940) | [[DT](#_Toc144361729)](#_Toc144362940)  | [[R/O](#_Toc144361729)](#_Toc144362940) | [[TBL#](#_Toc144361729)](#_Toc144362940) | [[Element Name](#_Toc144361729)](#_Toc144362940)                          | [[VistA Description](#_Toc144361729)](#_Toc144362940)                                                                                   |
|----------------------------------------------------------------------|-----------------------------------------|-----------------------------------------|-----------------------------------------|------------------------------------------|---------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| [[1](#_Toc144361729)](#_Toc144362940)                                | [[250](#_Toc144361729)](#_Toc144362940) | [[CE](#_Toc144361729)](#_Toc144362940)  | [[R](#_Toc144361729)](#_Toc144362940)   | [[0286](#_Toc144361729)](#_Toc144362940) | [[Provider Role](#_Toc144361729)](#_Toc144362940)                         | [[RP for Referring Provider](#_Toc144361729)](#_Toc144362940)                                                                           |
| [[2](#_Toc144361729)](#_Toc144362940)                                | [[250](#_Toc144361729)](#_Toc144362940) | [[XPN](#_Toc144361729)](#_Toc144362940) | [[O](#_Toc144361729)](#_Toc144362940)   |                                          | [[Provider Name](#_Toc144361729)](#_Toc144362940)                         | [[Provider Last Name^Provider First Name^Provider Middle Initial^^^^^^Provider DUZ](#_Toc144361729)](#_Toc144362940)                    |
| [[Provider from File 123, field 10](#_Toc144361729)](#_Toc144362940) |                                         |                                         |                                         |                                          |                                                                           |                                                                                                                                         |
| [[3](#_Toc144361729)](#_Toc144362940)                                | [[250](#_Toc144361729)](#_Toc144362940) | [[XAD](#_Toc144361729)](#_Toc144362940) | [[O](#_Toc144361729)](#_Toc144362940)   |                                          | [[Provider Address](#_Toc144361729)](#_Toc144362940)                      | [[Street Address 1^Street Address 2^City^State^Zip from File 200, fields .111, .112, .114, .115, .116](#_Toc144361729)](#_Toc144362940) |
| [[4](#_Toc144361729)](#_Toc144362940)                                | [[60](#_Toc144361729)](#_Toc144362940)  | [[PL](#_Toc144361729)](#_Toc144362940)  | [[NS](#_Toc144361729)](#_Toc144362940)  |                                          | [[Provider Location](#_Toc144361729)](#_Toc144362940)                     | [[Not used](#_Toc144361729)](#_Toc144362940)                                                                                            |
| [[5](#_Toc144361729)](#_Toc144362940)                                | [[250](#_Toc144361729)](#_Toc144362940) | [[XTN](#_Toc144361729)](#_Toc144362940) | [[O](#_Toc144361729)](#_Toc144362940)   |                                          | [[Provider Communication Information](#_Toc144361729)](#_Toc144362940)    | [[^^^Email Address^^Office Phone Area Code^Office Phone Number from File 200, fields .151, .132](#_Toc144361729)](#_Toc144362940)       |
| [[6](#_Toc144361729)](#_Toc144362940)                                | [[250](#_Toc144361729)](#_Toc144362940) | [[CE](#_Toc144361729)](#_Toc144362940)  | [[NS](#_Toc144361729)](#_Toc144362940)  |                                          | [[Preferred Method of Contact](#_Toc144361729)](#_Toc144362940)           | [[Not used](#_Toc144361729)](#_Toc144362940)                                                                                            |
| [[7](#_Toc144361729)](#_Toc144362940)                                | [[100](#_Toc144361729)](#_Toc144362940) | [[PLN](#_Toc144361729)](#_Toc144362940) | [[NS](#_Toc144361729)](#_Toc144362940)  |                                          | [[Provider Identifiers](#_Toc144361729)](#_Toc144362940)                  | [[Not used](#_Toc144361729)](#_Toc144362940)                                                                                            |
| [[8](#_Toc144361729)](#_Toc144362940)                                | [[26](#_Toc144361729)](#_Toc144362940)  | [[TS](#_Toc144361729)](#_Toc144362940)  | [[NS](#_Toc144361729)](#_Toc144362940)  |                                          | [[Effective Start Date of Provider Role](#_Toc144361729)](#_Toc144362940) | [[Not used](#_Toc144361729)](#_Toc144362940)                                                                                            |
| [[9](#_Toc144361729)](#_Toc144362940)                                | [[26](#_Toc144361729)](#_Toc144362940)  | [[TS](#_Toc144361729)](#_Toc144362940)  | [[NS](#_Toc144361729)](#_Toc144362940)  |                                          | [[Effective End Date of Provider Role](#_Toc144361729)](#_Toc144362940)   | [[Not used](#_Toc144361729)](#_Toc144362940)                                                                                            |

[[Refer to Table 14-13. Note that REF_I12 PID-Patient Id Segment is generated by the VistA API, and is the same for all msg types.](#_Toc144361729)](#_Toc144362940)

[[<span id="_Toc169170371" class="anchor"></span>Table 14‑13: REF_I12 PID-Patient Id Segment](#_Toc144361729)](#_Toc144362940)

| [[SEQ](#_Toc144361730)](#_Toc144362940)                                                          | [[LEN](#_Toc144361730)](#_Toc144362940)                                                                                                                                                                                                                                       | [[DT](#_Toc144361730)](#_Toc144362940)  | [[R/O](#_Toc144361730)](#_Toc144362940) | [[TBL#](#_Toc144361730)](#_Toc144362940) | [[Element Name](#_Toc144361730)](#_Toc144362940)                                                 | [[VistA Description](#_Toc144361730)](#_Toc144362940)                                                                                                    |
|--------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|-----------------------------------------|------------------------------------------|--------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
|                                                                                                  | [[4](#_Toc144361730)](#_Toc144362940)                                                                                                                                                                                                                                         | [[SI](#_Toc144361730)](#_Toc144362940)  | [[O](#_Toc144361730)](#_Toc144362940)   |                                          | [[Set ID – PID](#_Toc144361730)](#_Toc144362940)                                                 | [[Sequential Number](#_Toc144361730)](#_Toc144362940)                                                                                                    |
| [[2](#_Toc144361730)](#_Toc144362940)                                                            | [[20](#_Toc144361730)](#_Toc144362940)                                                                                                                                                                                                                                        | [[CX](#_Toc144361730)](#_Toc144362940)  | [[R](#_Toc144361730)](#_Toc144362940)   |                                          | [[Patient ID](#_Toc144361730)](#_Toc144362940)                                                   | [[ICN, including V checksum for backwards compatibility](#_Toc144361730)](#_Toc144362940)                                                                |
| [[3](#_Toc144361730)](#_Toc144362940)                                                            | [[250](#_Toc144361730)](#_Toc144362940)                                                                                                                                                                                                                                       | [[CX](#_Toc144361730)](#_Toc144362940)  | [[R](#_Toc144361730)](#_Toc144362940)   |                                          | [[Patient Identifier List (list is not in any specified order)](#_Toc144361730)](#_Toc144362940) |                                                                                                                                                          |
| [[Following are PID.3.5 Identifier Type Codes:](#_Toc144361730)](#_Toc144362940)                 |                                                                                                                                                                                                                                                                               |                                         |                                         |                                          |                                                                                                  |                                                                                                                                                          |
| [[NI=ICN](#_Toc144361730)](#_Toc144362940)                                                       |                                                                                                                                                                                                                                                                               |                                         |                                         |                                          |                                                                                                  |                                                                                                                                                          |
| [[PI=Patient DFN](#_Toc144361730)](#_Toc144362940)                                               |                                                                                                                                                                                                                                                                               |                                         |                                         |                                          |                                                                                                  |                                                                                                                                                          |
| [[SS=SSN](#_Toc144361730)](#_Toc144362940)                                                       |                                                                                                                                                                                                                                                                               |                                         |                                         |                                          |                                                                                                  |                                                                                                                                                          |
| [[PN=Claim Number](#_Toc144361730)](#_Toc144362940)                                              | [[Integration Control Number (including V and checksum), Social Security Number, DFN, Claim Number, all entries in the ICN History Multiple, and all alias SSNs which will correspond directly to the alias name in the name field (pid-5).](#_Toc144361730)](#_Toc144362940) |                                         |                                         |                                          |                                                                                                  |                                                                                                                                                          |
| [[4](#_Toc144361730)](#_Toc144362940)                                                            | [[20](#_Toc144361730)](#_Toc144362940)                                                                                                                                                                                                                                        | [[CX](#_Toc144361730)](#_Toc144362940)  | [[NS](#_Toc144361730)](#_Toc144362940)  |                                          | [[Alternate Patient ID – PID](#_Toc144361730)](#_Toc144362940)                                   | [[Not used](#_Toc144361730)](#_Toc144362940)                                                                                                             |
| [[5](#_Toc144361730)](#_Toc144362940)                                                            | [[250](#_Toc144361730)](#_Toc144362940)                                                                                                                                                                                                                                       | [[XPN](#_Toc144361730)](#_Toc144362940) | [[R](#_Toc144361730)](#_Toc144362940)   |                                          | [[Patient Name](#_Toc144361730)](#_Toc144362940)                                                 | [[Patient Name and all Alias entries](#_Toc144361730)](#_Toc144362940)                                                                                   |
| [[6](#_Toc144361730)](#_Toc144362940)                                                            | [[250](#_Toc144361730)](#_Toc144362940)                                                                                                                                                                                                                                       | [[XPN](#_Toc144361730)](#_Toc144362940) | [[O](#_Toc144361730)](#_Toc144362940)   |                                          | [[Mother’s Maiden Name](#_Toc144361730)](#_Toc144362940)                                         | [[Mother’s Maiden Name](#_Toc144361730)](#_Toc144362940)                                                                                                 |
| [[7](#_Toc144361730)](#_Toc144362940)                                                            | [[26](#_Toc144361730)](#_Toc144362940)                                                                                                                                                                                                                                        | [[TS](#_Toc144361730)](#_Toc144362940)  | [[O](#_Toc144361730)](#_Toc144362940)   |                                          | [[Date/Time of Birth](#_Toc144361730)](#_Toc144362940)                                           | [[Date of Birth](#_Toc144361730)](#_Toc144362940)                                                                                                        |
| [[8](#_Toc144361730)](#_Toc144362940)                                                            | [[1](#_Toc144361730)](#_Toc144362940)                                                                                                                                                                                                                                         | [[IS](#_Toc144361730)](#_Toc144362940)  | [[O](#_Toc144361730)](#_Toc144362940)   | [[0001](#_Toc144361730)](#_Toc144362940) | [[Administrative Sex](#_Toc144361730)](#_Toc144362940)                                           | [[Sex](#_Toc144361730)](#_Toc144362940)                                                                                                                  |
| [[9](#_Toc144361730)](#_Toc144362940)                                                            | [[250](#_Toc144361730)](#_Toc144362940)                                                                                                                                                                                                                                       | [[XPN](#_Toc144361730)](#_Toc144362940) | [[NS](#_Toc144361730)](#_Toc144362940)  |                                          | [[Patient Alias](#_Toc144361730)](#_Toc144362940)                                                | [[Not used. Alias is passed in PID-5](#_Toc144361730)](#_Toc144362940)                                                                                   |
| [[10](#_Toc144361730)](#_Toc144362940)                                                           | [[250](#_Toc144361730)](#_Toc144362940)                                                                                                                                                                                                                                       | [[CE](#_Toc144361730)](#_Toc144362940)  | [[O](#_Toc144361730)](#_Toc144362940)   | [[0005](#_Toc144361730)](#_Toc144362940) | [[Race](#_Toc144361730)](#_Toc144362940)                                                         | [[Race Information. Example: 2106-3-SLF^^0005^2106-3^^CDC See Appendix A for coded values. 0005 and CDC are hardcoded.](#_Toc144361730)](#_Toc144362940) |
| [[11](#_Toc144361730)](#_Toc144362940)                                                           | [[250](#_Toc144361730)](#_Toc144362940)                                                                                                                                                                                                                                       | [[XAD](#_Toc144361730)](#_Toc144362940) | [[O](#_Toc144361730)](#_Toc144362940)   |                                          | [[Patient Address](#_Toc144361730)](#_Toc144362940)                                              | [[P=Permanent Address~N=Place of Birth~Confidential Address](#_Toc144361730)](#_Toc144362940)                                                            |
| [[12](#_Toc144361730)](#_Toc144362940)                                                           | [[4](#_Toc144361730)](#_Toc144362940)                                                                                                                                                                                                                                         | [[IS](#_Toc144361730)](#_Toc144362940)  | [[O](#_Toc144361730)](#_Toc144362940)   | [[0289](#_Toc144361730)](#_Toc144362940) | [[County Code](#_Toc144361730)](#_Toc144362940)                                                  | [[County](#_Toc144361730)](#_Toc144362940)                                                                                                               |
| [[13](#_Toc144361730)](#_Toc144362940)                                                           | [[250](#_Toc144361730)](#_Toc144362940)                                                                                                                                                                                                                                       | [[XTN](#_Toc144361730)](#_Toc144362940) | [[O](#_Toc144361730)](#_Toc144362940)   |                                          | [[Phone Number – Home](#_Toc144361730)](#_Toc144362940)                                          | [[Home Phone~Work Phone~Cell Phone~Pager^NET^INTERNET^email](#_Toc144361730)](#_Toc144362940)                                                            |
| [[14](#_Toc144361730)](#_Toc144362940)                                                           | [[250](#_Toc144361730)](#_Toc144362940)                                                                                                                                                                                                                                       | [[XTN](#_Toc144361730)](#_Toc144362940) | [[O](#_Toc144361730)](#_Toc144362940)   |                                          | [[Phone Number – Business](#_Toc144361730)](#_Toc144362940)                                      | [[Work Phone (backward compatibility)](#_Toc144361730)](#_Toc144362940)                                                                                  |
| [[15](#_Toc144361730)](#_Toc144362940)                                                           | [[250](#_Toc144361730)](#_Toc144362940)                                                                                                                                                                                                                                       | [[CE](#_Toc144361730)](#_Toc144362940)  | [[NS](#_Toc144361730)](#_Toc144362940)  | [[0296](#_Toc144361730)](#_Toc144362940) | [[Primary Language](#_Toc144361730)](#_Toc144362940)                                             | [[Not used](#_Toc144361730)](#_Toc144362940)                                                                                                             |
| [[16](#_Toc144361730)](#_Toc144362940)                                                           | [[250](#_Toc144361730)](#_Toc144362940)                                                                                                                                                                                                                                       | [[CE](#_Toc144361730)](#_Toc144362940)  | [[O](#_Toc144361730)](#_Toc144362940)   | [[0002](#_Toc144361730)](#_Toc144362940) | [[Marital Status](#_Toc144361730)](#_Toc144362940)                                               | [[Marital Status^^^^^^M](#_Toc144361730)](#_Toc144362940)                                                                                                |
| [[17](#_Toc144361730)](#_Toc144362940)                                                           | [[250](#_Toc144361730)](#_Toc144362940)                                                                                                                                                                                                                                       | [[CE](#_Toc144361730)](#_Toc144362940)  | [[O](#_Toc144361730)](#_Toc144362940)   | [[0006](#_Toc144361730)](#_Toc144362940) | [[Religion](#_Toc144361730)](#_Toc144362940)                                                     | [[Religious Preference (code)](#_Toc144361730)](#_Toc144362940)                                                                                          |
| [[18](#_Toc144361730)](#_Toc144362940)                                                           | [[250](#_Toc144361730)](#_Toc144362940)                                                                                                                                                                                                                                       | [[CX](#_Toc144361730)](#_Toc144362940)  | [[NS](#_Toc144361730)](#_Toc144362940)  |                                          | [[Patient Account Number](#_Toc144361730)](#_Toc144362940)                                       | [[Not used](#_Toc144361730)](#_Toc144362940)                                                                                                             |
| [[19](#_Toc144361730)](#_Toc144362940)                                                           | [[16](#_Toc144361730)](#_Toc144362940)                                                                                                                                                                                                                                        | [[ST](#_Toc144361730)](#_Toc144362940)  | [[R](#_Toc144361730)](#_Toc144362940)   |                                          | [[SSN Number – Patient](#_Toc144361730)](#_Toc144362940)                                         | [[SSN](#_Toc144361730)](#_Toc144362940)                                                                                                                  |
| [[20](#_Toc144361730)](#_Toc144362940)                                                           | [[25](#_Toc144361730)](#_Toc144362940)                                                                                                                                                                                                                                        | [[DLN](#_Toc144361730)](#_Toc144362940) | [[NS](#_Toc144361730)](#_Toc144362940)  |                                          | [[Driver’s License Number – Patient](#_Toc144361730)](#_Toc144362940)                            | [[Not used](#_Toc144361730)](#_Toc144362940)                                                                                                             |
| [[21](#_Toc144361730)](#_Toc144362940)                                                           | [[250](#_Toc144361730)](#_Toc144362940)                                                                                                                                                                                                                                       | [[CX](#_Toc144361730)](#_Toc144362940)  | [[NS](#_Toc144361730)](#_Toc144362940)  |                                          | [[Mother’s Identifier](#_Toc144361730)](#_Toc144362940)                                          | [[Not used](#_Toc144361730)](#_Toc144362940)                                                                                                             |
| [[22](#_Toc144361730)](#_Toc144362940)                                                           | [[250](#_Toc144361730)](#_Toc144362940)                                                                                                                                                                                                                                       | [[CE](#_Toc144361730)](#_Toc144362940)  | [[O](#_Toc144361730)](#_Toc144362940)   | [[0189](#_Toc144361730)](#_Toc144362940) | [[Ethnic Group](#_Toc144361730)](#_Toc144362940)                                                 | [[Ethnicity Information. Example: 2186-5-SLF^^0189^2186-5^^CDC](#_Toc144361730)](#_Toc144362940)                                                         |
| [[See Appendix A for coded values. 2186 and CDC are hardcoded.](#_Toc144361730)](#_Toc144362940) |                                                                                                                                                                                                                                                                               |                                         |                                         |                                          |                                                                                                  |                                                                                                                                                          |
| [[23](#_Toc144361730)](#_Toc144362940)                                                           | [[250](#_Toc144361730)](#_Toc144362940)                                                                                                                                                                                                                                       | [[ST](#_Toc144361730)](#_Toc144362940)  | [[O](#_Toc144361730)](#_Toc144362940)   |                                          | [[Birthplace](#_Toc144361730)](#_Toc144362940)                                                   | [[Place of birth city and place of birth state](#_Toc144361730)](#_Toc144362940)                                                                         |
| [[24](#_Toc144361730)](#_Toc144362940)                                                           | [[1](#_Toc144361730)](#_Toc144362940)                                                                                                                                                                                                                                         | [[ID](#_Toc144361730)](#_Toc144362940)  | [[O](#_Toc144361730)](#_Toc144362940)   | [[0136](#_Toc144361730)](#_Toc144362940) | [[Multiple Birth Indicator](#_Toc144361730)](#_Toc144362940)                                     | [[Multiple Birth Indicator \[Y for multiple birth\]](#_Toc144361730)](#_Toc144362940)                                                                    |

- 

[[Note (PID fields past PID.24 not used and not shown to save space.](#_Toc144361730)](#_Toc144362940)

[[  
](#_Toc144361730)](#_Toc144362940)

[[Refer to Table 14-14. REF_I12 DG1 - Diagnosis Segment is the same for all message types.](#_Toc144361730)](#_Toc144362940)

[[<span id="_Toc169170372" class="anchor"></span>Table 14‑14: REF_I12 DG1 - Diagnosis Segment](#_Toc144361730)](#_Toc144362940)

| [[SEQ](#_Toc144361731)](#_Toc144362940) | [[LEN](#_Toc144361731)](#_Toc144362940) | [[DT](#_Toc144361731)](#_Toc144362940) | [[R/O](#_Toc144361731)](#_Toc144362940) | [[TBL#](#_Toc144361731)](#_Toc144362940) | [[Element Name](#_Toc144361731)](#_Toc144362940)            | [[VistA Description](#_Toc144361731)](#_Toc144362940)                                                        |
|-----------------------------------------|-----------------------------------------|----------------------------------------|-----------------------------------------|------------------------------------------|-------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [[1](#_Toc144361731)](#_Toc144362940)   | [[4](#_Toc144361731)](#_Toc144362940)   | [[SI](#_Toc144361731)](#_Toc144362940) | [[R](#_Toc144361731)](#_Toc144362940)   |                                          | [[Set ID – DG1](#_Toc144361731)](#_Toc144362940)            | [[1](#_Toc144361731)](#_Toc144362940)                                                                        |
| [[2](#_Toc144361731)](#_Toc144362940)   | [[2](#_Toc144361731)](#_Toc144362940)   | [[ID](#_Toc144361731)](#_Toc144362940) | [[NS](#_Toc144361731)](#_Toc144362940)  |                                          | [[Diagnosis Coding Method](#_Toc144361731)](#_Toc144362940) | [[Not used](#_Toc144361731)](#_Toc144362940)                                                                 |
| [[3](#_Toc144361731)](#_Toc144362940)   | [[250](#_Toc144361731)](#_Toc144362940) | [[CE](#_Toc144361731)](#_Toc144362940) | [[R](#_Toc144361731)](#_Toc144362940)   | [[0051](#_Toc144361731)](#_Toc144362940) | [[Diagnosis Code – DG1](#_Toc144361731)](#_Toc144362940)    | [[Provisional Diagnosis Code^Diagnosis Description from File 123, field 30](#_Toc144361731)](#_Toc144362940) |
| [[4](#_Toc144361731)](#_Toc144362940)   | [[40](#_Toc144361731)](#_Toc144362940)  | [[ST](#_Toc144361731)](#_Toc144362940) | [[B](#_Toc144361731)](#_Toc144362940)   |                                          | [[Diagnosis Description](#_Toc144361731)](#_Toc144362940)   | [[Not Used](#_Toc144361731)](#_Toc144362940)                                                                 |
| [[5](#_Toc144361731)](#_Toc144362940)   | [[26](#_Toc144361731)](#_Toc144362940)  | [[TS](#_Toc144361731)](#_Toc144362940) | [[O](#_Toc144361731)](#_Toc144362940)   |                                          | [[Diagnosis Date/Time](#_Toc144361731)](#_Toc144362940)     | [[Not Used](#_Toc144361731)](#_Toc144362940)                                                                 |
| [[6](#_Toc144361731)](#_Toc144362940)   | [[2](#_Toc144361731)](#_Toc144362940)   | [[IS](#_Toc144361731)](#_Toc144362940) | [[R](#_Toc144361731)](#_Toc144362940)   | [[0052](#_Toc144361731)](#_Toc144362940) | [[Diagnosis Type](#_Toc144361731)](#_Toc144362940)          | [[“W” - Working](#_Toc144361731)](#_Toc144362940)                                                            |

- 

| [[SEQ](#_Toc144361732)](#_Toc144362940) | [[LEN](#_Toc144361732)](#_Toc144362940) | [[DT](#_Toc144361732)](#_Toc144362940) | [[R/O](#_Toc144361732)](#_Toc144362940) | [[TBL#](#_Toc144361732)](#_Toc144362940) | [[Element Name](#_Toc144361732)](#_Toc144362940)                 | [[VistA Description](#_Toc144361732)](#_Toc144362940)                                                            |
|-----------------------------------------|-----------------------------------------|----------------------------------------|-----------------------------------------|------------------------------------------|------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| [[1](#_Toc144361732)](#_Toc144362940)   | [[4](#_Toc144361732)](#_Toc144362940)   | [[SI](#_Toc144361732)](#_Toc144362940) | [[R](#_Toc144361732)](#_Toc144362940)   |                                          | [[Set ID – OBR](#_Toc144361732)](#_Toc144362940)                 | [[1](#_Toc144361732)](#_Toc144362940)                                                                            |
| [[2](#_Toc144361732)](#_Toc144362940)   | [[22](#_Toc144361732)](#_Toc144362940)  | [[EI](#_Toc144361732)](#_Toc144362940) | [[R](#_Toc144361732)](#_Toc144362940)   |                                          | [[Placer Order Number](#_Toc144361732)](#_Toc144362940)          | [[Order entry internal number;Orderable Item entry^OR from File 123, field .03](#_Toc144361732)](#_Toc144362940) |
| [[3](#_Toc144361732)](#_Toc144362940)   | [[22](#_Toc144361732)](#_Toc144362940)  | [[EI](#_Toc144361732)](#_Toc144362940) | [[R](#_Toc144361732)](#_Toc144362940)   |                                          | [[Filler Order Number](#_Toc144361732)](#_Toc144362940)          | [[Consult entry internal number;GMRC^GMRC](#_Toc144361732)](#_Toc144362940)                                      |
| [[4](#_Toc144361732)](#_Toc144362940)   | [[250](#_Toc144361732)](#_Toc144362940) | [[CE](#_Toc144361732)](#_Toc144362940) | [[R](#_Toc144361732)](#_Toc144362940)   |                                          | [[Universal Service Identifier](#_Toc144361732)](#_Toc144362940) | [[Hardcoded value of “ZZ”](#_Toc144361732)](#_Toc144362940)                                                      |
| [[5](#_Toc144361732)](#_Toc144362940)   | [[2](#_Toc144361732)](#_Toc144362940)   | [[ID](#_Toc144361732)](#_Toc144362940) | [[NS](#_Toc144361732)](#_Toc144362940)  |                                          | [[Priority – OBR](#_Toc144361732)](#_Toc144362940)               | [[Not used](#_Toc144361732)](#_Toc144362940)                                                                     |
| [[6](#_Toc144361732)](#_Toc144362940)   | [[26](#_Toc144361732)](#_Toc144362940)  | [[TS](#_Toc144361732)](#_Toc144362940) | [[O](#_Toc144361732)](#_Toc144362940)   |                                          | [[Requested Date/Time](#_Toc144361732)](#_Toc144362940)          | [[Clinically Indicated Date from File 123, field 17](#_Toc144361732)](#_Toc144362940)                            |

- 

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 13%" />
<col style="width: 10%" />
<col style="width: 22%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><a href="#_Toc144362940"><span>SEQ</span></a></th>
<th><a href="#_Toc144362940"><span>LEN</span></a></th>
<th><a href="#_Toc144362940"><span>DT</span></a></th>
<th><a href="#_Toc144362940"><span>R/O</span></a></th>
<th><a href="#_Toc144362940"><span>TBL#</span></a></th>
<th><a href="#_Toc144362940"><span>Element Name</span></a></th>
<th><a href="#_Toc144362940"><span>VistA Description</span></a></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="#_Toc144362940"><span>1</span></a></td>
<td><a href="#_Toc144362940"><span>4</span></a></td>
<td><a href="#_Toc144362940"><span>SI</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Set ID – PV1</span></a></td>
<td><a href="#_Toc144362940"><span>1</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>2</span></a></td>
<td><a href="#_Toc144362940"><span>1</span></a></td>
<td><a href="#_Toc144362940"><span>IS</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td><a href="#_Toc144362940"><span>0004</span></a></td>
<td><a href="#_Toc144362940"><span>Patient Class</span></a></td>
<td><a href="#_Toc144362940"><span>I: inpatient<br />
O: outpatient</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>3</span></a></td>
<td><a href="#_Toc144362940"><span>80</span></a></td>
<td><a href="#_Toc144362940"><span>PL</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Assigned Patient Location</span></a></td>
<td><a href="#_Toc144362940"><span>Location of last inpatient movement event from VAIP(5)</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>4</span></a></td>
<td><a href="#_Toc144362940"><span>2</span></a></td>
<td><a href="#_Toc144362940"><span>IS</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Admission Type</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>5</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>CX</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Preadmit Number</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>6</span></a></td>
<td><a href="#_Toc144362940"><span>80</span></a></td>
<td><a href="#_Toc144362940"><span>PL</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Prior Patient Location</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>7</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>XCN</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td><a href="#_Toc144362940"><span>0010</span></a></td>
<td><a href="#_Toc144362940"><span>Attending Doctor</span></a></td>
<td><p><a href="#_Toc144362940"><span>Attending Provider from VAIP(18</span></a></p>
<p><a href="#_Toc144362940"><span>)</span></a></p></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>8</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>XCN</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td><a href="#_Toc144362940"><span>0010</span></a></td>
<td><a href="#_Toc144362940"><span>Referring Doctor</span></a></td>
<td><a href="#_Toc144362940"><span>Not used (Referring provider sent in PRD segment)</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>9</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>XCN</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Consulting Doctor</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>10</span></a></td>
<td><a href="#_Toc144362940"><span>3</span></a></td>
<td><a href="#_Toc144362940"><span>IS</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Hospital Service</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>11</span></a></td>
<td><a href="#_Toc144362940"><span>80</span></a></td>
<td><a href="#_Toc144362940"><span>PL</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Temporary Location</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>12</span></a></td>
<td><a href="#_Toc144362940"><span>2</span></a></td>
<td><a href="#_Toc144362940"><span>IS</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Preadmit Test Indicator</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>13</span></a></td>
<td><a href="#_Toc144362940"><span>2</span></a></td>
<td><a href="#_Toc144362940"><span>IS</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Re-admission Indicator</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>14</span></a></td>
<td><a href="#_Toc144362940"><span>6</span></a></td>
<td><a href="#_Toc144362940"><span>IS</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Admit Source</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>15</span></a></td>
<td><a href="#_Toc144362940"><span>2</span></a></td>
<td><a href="#_Toc144362940"><span>IS</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Ambulatory Status</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>16</span></a></td>
<td><a href="#_Toc144362940"><span>2</span></a></td>
<td><a href="#_Toc144362940"><span>IS</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td><a href="#_Toc144362940"><span>0099</span></a></td>
<td><a href="#_Toc144362940"><span>VIP Indicator</span></a></td>
<td><a href="#_Toc144362940"><span>R if patient restricted/sensitive</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>17</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>XCN</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Admitting Doctor</span></a></td>
<td><a href="#_Toc144362940"><span>Primary Physician for admission from VAIP (13,5)</span></a></td>
</tr>
</tbody>
</table>

- 

| [[SEQ](#_Toc144361734)](#_Toc144362940) | [[LEN](#_Toc144361734)](#_Toc144362940)   | [[DT](#_Toc144361734)](#_Toc144362940) | [[R/O](#_Toc144361734)](#_Toc144362940) | [[TBL#](#_Toc144361734)](#_Toc144362940) | [[Element Name](#_Toc144361734)](#_Toc144362940)      | [[VistA Description](#_Toc144361734)](#_Toc144362940)                          |
|-----------------------------------------|-------------------------------------------|----------------------------------------|-----------------------------------------|------------------------------------------|-------------------------------------------------------|--------------------------------------------------------------------------------|
| [[1](#_Toc144361734)](#_Toc144362940)   | [[4](#_Toc144361734)](#_Toc144362940)     | [[SI](#_Toc144361734)](#_Toc144362940) | [[O](#_Toc144361734)](#_Toc144362940)   |                                          | [[Set ID – NTE](#_Toc144361734)](#_Toc144362940)      | [[Sequential Number 1-n](#_Toc144361734)](#_Toc144362940)                      |
| [[2](#_Toc144361734)](#_Toc144362940)   | [[8](#_Toc144361734)](#_Toc144362940)     | [[ID](#_Toc144361734)](#_Toc144362940) | [[O](#_Toc144361734)](#_Toc144362940)   | [[0105](#_Toc144361734)](#_Toc144362940) | [[Source of Comment](#_Toc144361734)](#_Toc144362940) | [[P for Placer](#_Toc144361734)](#_Toc144362940)                               |
| [[3](#_Toc144361734)](#_Toc144362940)   | [[65536](#_Toc144361734)](#_Toc144362940) | [[FT](#_Toc144361734)](#_Toc144362940) | [[O](#_Toc144361734)](#_Toc144362940)   |                                          | [[Comment](#_Toc144361734)](#_Toc144362940)           | [[Reason for Request from file 123, field 20](#_Toc144361734)](#_Toc144362940) |
| [[4](#_Toc144361734)](#_Toc144362940)   | [[250](#_Toc144361734)](#_Toc144362940)   | [[CE](#_Toc144361734)](#_Toc144362940) | [[O](#_Toc144361734)](#_Toc144362940)   |                                          | [[Comment Type](#_Toc144361734)](#_Toc144362940)      | [[Not used.](#_Toc144361734)](#_Toc144362940)                                  |

[[  
](#_Toc144361734)](#_Toc144362940)

[[  
](#_Toc144361862)](#_Toc144362940)

[[  
](#_Toc144361864)](#_Toc144362940)

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 8%" />
<col style="width: 12%" />
<col style="width: 8%" />
<col style="width: 20%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr class="header">
<th><a href="#_Toc144362940"><span>SEQ</span></a></th>
<th><a href="#_Toc144362940"><span>LEN</span></a></th>
<th><a href="#_Toc144362940"><span>DT</span></a></th>
<th><a href="#_Toc144362940"><span>R/O</span></a></th>
<th><a href="#_Toc144362940"><span>TBL#</span></a></th>
<th><a href="#_Toc144362940"><span>Element Name</span></a></th>
<th><a href="#_Toc144362940"><span>VistA Description</span></a></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="#_Toc144362940"><span>1</span></a></td>
<td><a href="#_Toc144362940"><span>1</span></a></td>
<td><a href="#_Toc144362940"><span>ST</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Field Separator</span></a></td>
<td><a href="#_Toc144362940"><span>|</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>2</span></a></td>
<td><a href="#_Toc144362940"><span>4</span></a></td>
<td><a href="#_Toc144362940"><span>ST</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Encoding Characters</span></a></td>
<td><a href="#_Toc144362940"><span>^~\&amp;</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>3</span></a></td>
<td><a href="#_Toc144362940"><span>15</span></a></td>
<td><a href="#_Toc144362940"><span>ST</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Sending Application</span></a></td>
<td><a href="#_Toc144362940"><span>GMRC HCP SEND</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>4</span></a></td>
<td><a href="#_Toc144362940"><span>20</span></a></td>
<td><a href="#_Toc144362940"><span>ST</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Sending Facility</span></a></td>
<td><a href="#_Toc144362940"><span>Sending Facility, from the FACILITY NAME field of the HL7 APPLICATION entry GMRC HCP SEND</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>5</span></a></td>
<td><a href="#_Toc144362940"><span>30</span></a></td>
<td><a href="#_Toc144362940"><span>ST</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Receiving Application</span></a></td>
<td><a href="#_Toc144362940"><span>GMRC HCP RECEIVE</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>6</span></a></td>
<td><a href="#_Toc144362940"><span>30</span></a></td>
<td><a href="#_Toc144362940"><span>ST</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Receiving Facility</span></a></td>
<td><a href="#_Toc144362940"><span>Receiving Facility, from the FACILITY NAME field of the HL7 APPLICATION entry GMRC HCP RECEIVE</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>7</span></a></td>
<td><a href="#_Toc144362940"><span>26</span></a></td>
<td><a href="#_Toc144362940"><span>TS</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Date/Time Of Message</span></a></td>
<td><a href="#_Toc144362940"><span>System date/time generated by the VistA HL7 package</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>8</span></a></td>
<td><a href="#_Toc144362940"><span>40</span></a></td>
<td><a href="#_Toc144362940"><span>ST</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Security</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>9</span></a></td>
<td><a href="#_Toc144362940"><span>7</span></a></td>
<td><a href="#_Toc144362940"><span>CM</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td><a href="#_Toc144362940"><span>0076<br />
0003</span></a></td>
<td><a href="#_Toc144362940"><span>Message Type</span></a></td>
<td><a href="#_Toc144362940"><span>REF^I13</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>10</span></a></td>
<td><a href="#_Toc144362940"><span>20</span></a></td>
<td><a href="#_Toc144362940"><span>ST</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Message Control ID</span></a></td>
<td><a href="#_Toc144362940"><span>Facility and sequence number automatically generated by the HL7 Package</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>11</span></a></td>
<td><a href="#_Toc144362940"><span>1</span></a></td>
<td><a href="#_Toc144362940"><span>ID</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Processing ID</span></a></td>
<td><a href="#_Toc144362940"><span>P for Production, T for Test</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>12</span></a></td>
<td><a href="#_Toc144362940"><span>8</span></a></td>
<td><a href="#_Toc144362940"><span>ID</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td><a href="#_Toc144362940"><span>0104</span></a></td>
<td><a href="#_Toc144362940"><span>Version ID</span></a></td>
<td><a href="#_Toc144362940"><span>2.</span><span>5</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>13</span></a></td>
<td><a href="#_Toc144362940"><span>15</span></a></td>
<td><a href="#_Toc144362940"><span>NM</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Sequence Number</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>14</span></a></td>
<td><a href="#_Toc144362940"><span>180</span></a></td>
<td><a href="#_Toc144362940"><span>ST</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Continuation Pointer</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>15</span></a></td>
<td><a href="#_Toc144362940"><span>2</span></a></td>
<td><a href="#_Toc144362940"><span>ID</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td><a href="#_Toc144362940"><span>0155</span></a></td>
<td><a href="#_Toc144362940"><span>Accept Acknowledgment Type</span></a></td>
<td><a href="#_Toc144362940"><span>AL=Always</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>16</span></a></td>
<td><a href="#_Toc144362940"><span>2</span></a></td>
<td><a href="#_Toc144362940"><span>ID</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td><a href="#_Toc144362940"><span>0155</span></a></td>
<td><a href="#_Toc144362940"><span>Application Acknowledgment Type</span></a></td>
<td><a href="#_Toc144362940"><span>AL=Always</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>17</span></a></td>
<td><a href="#_Toc144362940"><span>3</span></a></td>
<td><a href="#_Toc144362940"><span>ID</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td><a href="#_Toc144362940"><span>0399</span></a></td>
<td><a href="#_Toc144362940"><span>Country Code</span></a></td>
<td><a href="#_Toc144362940"><span>USA</span></a></td>
</tr>
</tbody>
</table>

[[Note the following:](#_Toc144362934)](#_Toc144362940)

- 
- 

<table style="width:100%;">
<colgroup>
<col style="width: 11%" />
<col style="width: 8%" />
<col style="width: 13%" />
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 18%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th><a href="#_Toc144362940"><span>SEQ</span></a></th>
<th><a href="#_Toc144362940"><span>LEN</span></a></th>
<th><a href="#_Toc144362940"><span>DT</span></a></th>
<th><a href="#_Toc144362940"><span>R/O</span></a></th>
<th><a href="#_Toc144362940"><span>TBL#</span></a></th>
<th><a href="#_Toc144362940"><span>Element Name</span></a></th>
<th><a href="#_Toc144362940"><span>VistA Description</span></a></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="#_Toc144362940"><span>1</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>CE</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td><a href="#_Toc144362940"><span>0283</span></a></td>
<td><a href="#_Toc144362940"><span>Referral Status</span></a></td>
<td><a href="#_Toc144362940"><span>SC^RECEIVED<br />
SC^SCHEDULED<br />
IP^RESUBMITTED<br />
IP^ADD COMMENT<br />
XX^FORWARDED<br />
CM^COMPLETE<br />
CM^ADDENDED</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>2</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>CE</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td><a href="#_Toc144362940"><span>0280</span></a></td>
<td><a href="#_Toc144362940"><span>Referral Priority</span></a></td>
<td><a href="#_Toc144362940"><span>From File 123, Field 5 (Urgency). Values are:<br />
1 WEEK, NEXT AVAILABLE, ROUTINE, STAT, TODAY, TOMORROW AM, WITHIN 1 MONTH, WITHIN 1 WEEK, WITHIN 24 HOURS, WITHIN 72 HOURS</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>3</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>CE</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Referral Type</span></a></td>
<td><a href="#_Toc144362940"><span>Service IEN^Service Name^^Template IEN<br />
^Template Name<br />
Service IEN is pointer to File 123.5, Template IEN is pointer to File 8927.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>4</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>CE</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Referral Disposition</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>5</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>CE</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td><a href="#_Toc144362940"><span>0284</span></a></td>
<td><a href="#_Toc144362940"><span>Referral Category</span></a></td>
<td><a href="#_Toc144362940"><span>I for Inpatient, O for Outpatient based on File 123, field 14 (Service Rendered as In or Out). This could be different than the PV1.1 current patient status.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>6</span></a></td>
<td><a href="#_Toc144362940"><span>30</span></a></td>
<td><a href="#_Toc144362940"><span>EI</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Originating Referral Identifier</span></a></td>
<td><a href="#_Toc144362940"><span>IEN to File 123</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>7</span></a></td>
<td><a href="#_Toc144362940"><span>26</span></a></td>
<td><a href="#_Toc144362940"><span>TS</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Effective Date</span></a></td>
<td><a href="#_Toc144362940"><span>Referral Date of Request from File 123, field .01</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>8</span></a></td>
<td><a href="#_Toc144362940"><span>26</span></a></td>
<td><a href="#_Toc144362940"><span>TS</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Expiration Date</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>9</span></a></td>
<td><a href="#_Toc144362940"><span>26</span></a></td>
<td><a href="#_Toc144362940"><span>TS</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Process Date</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>10</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>CE</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Referral Reason</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>11</span></a></td>
<td><a href="#_Toc144362940"><span>30</span></a></td>
<td><a href="#_Toc144362940"><span>EI</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>External Referral Identifier</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
</tbody>
</table>

- 

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 11%" />
<col style="width: 20%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><a href="#_Toc144362940"><span>SEQ</span></a></th>
<th><a href="#_Toc144362940"><span>LEN</span></a></th>
<th><a href="#_Toc144362940"><span>DT</span></a></th>
<th><a href="#_Toc144362940"><span>R/O</span></a></th>
<th><a href="#_Toc144362940"><span>TBL#</span></a></th>
<th><a href="#_Toc144362940"><span>Element Name</span></a></th>
<th><a href="#_Toc144362940"><span>VistA Description</span></a></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="#_Toc144362940"><span>1</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>CE</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td><a href="#_Toc144362940"><span>0286</span></a></td>
<td><a href="#_Toc144362940"><span>Provider Role</span></a></td>
<td><a href="#_Toc144362940"><span>RP for Referring Provider</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>2</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>XPN</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Provider Name</span></a></td>
<td><a href="#_Toc144362940"><span>Provider Last Name^Provider First Name^Provider Middle Initial^^^^^^Provider DUZ<br />
Provider from File 123, field 10</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>3</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>XAD</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Provider Address</span></a></td>
<td><a href="#_Toc144362940"><span>Street Address 1^Street Address 2^City^State^Zip from File 2, fields .111, .112, .114, .115, .116</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>4</span></a></td>
<td><a href="#_Toc144362940"><span>60</span></a></td>
<td><a href="#_Toc144362940"><span>PL</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Provider Location</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>5</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>XTN</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Provider Communication Information</span></a></td>
<td><a href="#_Toc144362940"><span>^^^Email Address^^Office Phone Area Code^Office Phone Number from File 2, fields .151, .132</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>6</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>CE</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Preferred Method of Contact</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>7</span></a></td>
<td><a href="#_Toc144362940"><span>100</span></a></td>
<td><a href="#_Toc144362940"><span>PLN</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Provider Identifiers</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>8</span></a></td>
<td><a href="#_Toc144362940"><span>26</span></a></td>
<td><a href="#_Toc144362940"><span>TS</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Effective Start Date of Provider Role</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>9</span></a></td>
<td><a href="#_Toc144362940"><span>26</span></a></td>
<td><a href="#_Toc144362940"><span>TS</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Effective End Date of Provider Role</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
</tbody>
</table>

- 

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 17%" />
<col style="width: 42%" />
</colgroup>
<thead>
<tr class="header">
<th><a href="#_Toc144362940"><span>SEQ</span></a></th>
<th><a href="#_Toc144362940"><span>LEN</span></a></th>
<th><a href="#_Toc144362940"><span>DT</span></a></th>
<th><a href="#_Toc144362940"><span>R/O</span></a></th>
<th><a href="#_Toc144362940"><span>TBL#</span></a></th>
<th><a href="#_Toc144362940"><span>Element Name</span></a></th>
<th><a href="#_Toc144362940"><span>VistA Description</span></a></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="#_Toc144362940"><span>1</span></a></td>
<td><a href="#_Toc144362940"><span>4</span></a></td>
<td><a href="#_Toc144362940"><span>SI</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Set ID – PID</span></a></td>
<td><a href="#_Toc144362940"><span>Sequential Number</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>2</span></a></td>
<td><a href="#_Toc144362940"><span>20</span></a></td>
<td><a href="#_Toc144362940"><span>CX</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Patient ID</span></a></td>
<td><a href="#_Toc144362940"><span>ICN, including V checksum for backwards compatibility</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>3</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>CX</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Patient Identifier List (list is not in any specified order):<br />
Following are PID.3.5 Identifier Type Codes:<br />
NI=ICN<br />
PI=Patient DFN<br />
SS=SSN<br />
PN=Claim Number</span></a></td>
<td><a href="#_Toc144362940"><span>Integration Control Number (including V and checksum), Social Security Number, DFN, Claim Number, all entries in the ICN History Multiple, and all alias SSNs which will correspond directly to the alias name in the name field (pid-5).</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>4</span></a></td>
<td><a href="#_Toc144362940"><span>20</span></a></td>
<td><a href="#_Toc144362940"><span>CX</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Alternate Patient ID – PID</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>5</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>XPN</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Patient Name</span></a></td>
<td><a href="#_Toc144362940"><span>Patient Name and all Alias entries</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>6</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>XPN</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Mother’s Maiden Name</span></a></td>
<td><a href="#_Toc144362940"><span>Mother’s Maiden Name</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>7</span></a></td>
<td><a href="#_Toc144362940"><span>26</span></a></td>
<td><a href="#_Toc144362940"><span>TS</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Date/Time of Birth</span></a></td>
<td><a href="#_Toc144362940"><span>Date of Birth</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>8</span></a></td>
<td><a href="#_Toc144362940"><span>1</span></a></td>
<td><a href="#_Toc144362940"><span>IS</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td><a href="#_Toc144362940"><span>1</span></a></td>
<td><a href="#_Toc144362940"><span>Administrative Sex</span></a></td>
<td><a href="#_Toc144362940"><span>Sex</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>9</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>XPN</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Patient Alias</span></a></td>
<td><a href="#_Toc144362940"><span>Not used. Alias is passed in PID-5</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>10</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>CE</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td><a href="#_Toc144362940"><span>5</span></a></td>
<td><a href="#_Toc144362940"><span>Race</span></a></td>
<td><a href="#_Toc144362940"><span>Race Information. Example: 2106-3-SLF^^0005^2106-3^^CDC See Appendix A for coded values. 0005 and CDC are hardcoded.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>11</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>XAD</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Patient Address</span></a></td>
<td><a href="#_Toc144362940"><span>P=Permanent Address~N=Place of Birth~Confidential Address</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>12</span></a></td>
<td><a href="#_Toc144362940"><span>4</span></a></td>
<td><a href="#_Toc144362940"><span>IS</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td><a href="#_Toc144362940"><span>289</span></a></td>
<td><a href="#_Toc144362940"><span>County Code</span></a></td>
<td><a href="#_Toc144362940"><span>County</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>13</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>XTN</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Phone Number – Home</span></a></td>
<td><a href="#_Toc144362940"><span>Home Phone~Work Phone~Cell Phone~Pager^NET^INTERNET^email</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>14</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>XTN</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Phone Number – Business</span></a></td>
<td><a href="#_Toc144362940"><span>Work Phone (backward compatibility)</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>15</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>CE</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td><a href="#_Toc144362940"><span>296</span></a></td>
<td><a href="#_Toc144362940"><span>Primary Language</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>16</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>CE</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td><a href="#_Toc144362940"><span>2</span></a></td>
<td><a href="#_Toc144362940"><span>Marital Status</span></a></td>
<td><a href="#_Toc144362940"><span>Marital Status^^^^^^M</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>17</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>CE</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td><a href="#_Toc144362940"><span>6</span></a></td>
<td><a href="#_Toc144362940"><span>Religion</span></a></td>
<td><a href="#_Toc144362940"><span>Religious Preference (code)</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>18</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>CX</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Patient Account Number</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>19</span></a></td>
<td><a href="#_Toc144362940"><span>16</span></a></td>
<td><a href="#_Toc144362940"><span>ST</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>SSN Number – Patient</span></a></td>
<td><a href="#_Toc144362940"><span>SSN</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>20</span></a></td>
<td><a href="#_Toc144362940"><span>25</span></a></td>
<td><a href="#_Toc144362940"><span>DLN</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Driver’s License Number – Patient</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>21</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>CX</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Mother’s Identifier</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>22</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>CE</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td><a href="#_Toc144362940"><span>189</span></a></td>
<td><a href="#_Toc144362940"><span>Ethnic Group</span></a></td>
<td><a href="#_Toc144362940"><span>Ethnicity Information. Example: 2186-5-SLF^^0189^2186-5^^CDC</span></a></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td><a href="#_Toc144362940"><span>See Appendix A for coded values. 2186 and CDC are hardcoded.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>23</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>ST</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Birthplace</span></a></td>
<td><a href="#_Toc144362940"><span>Place of birth city and place of birth state</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>24</span></a></td>
<td><a href="#_Toc144362940"><span>1</span></a></td>
<td><a href="#_Toc144362940"><span>ID</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td><a href="#_Toc144362940"><span>136</span></a></td>
<td><a href="#_Toc144362940"><span>Multiple Birth Indicator</span></a></td>
<td><a href="#_Toc144362940"><span>Multiple Birth Indicator [Y for multiple birth]</span></a></td>
</tr>
</tbody>
</table>

- 

| [[SEQ](#_Toc144361739)](#_Toc144362940) | [[LEN](#_Toc144361739)](#_Toc144362940) | [[DT](#_Toc144361739)](#_Toc144362940) | [[R/O](#_Toc144361739)](#_Toc144362940) | [[TBL#](#_Toc144361739)](#_Toc144362940) | [[Element Name](#_Toc144361739)](#_Toc144362940)            | [[VistA Description](#_Toc144361739)](#_Toc144362940)                                                        |
|-----------------------------------------|-----------------------------------------|----------------------------------------|-----------------------------------------|------------------------------------------|-------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [[1](#_Toc144361739)](#_Toc144362940)   | [[4](#_Toc144361739)](#_Toc144362940)   | [[SI](#_Toc144361739)](#_Toc144362940) | [[R](#_Toc144361739)](#_Toc144362940)   |                                          | [[Set ID – DG1](#_Toc144361739)](#_Toc144362940)            | [[1](#_Toc144361739)](#_Toc144362940)                                                                        |
| [[2](#_Toc144361739)](#_Toc144362940)   | [[2](#_Toc144361739)](#_Toc144362940)   | [[ID](#_Toc144361739)](#_Toc144362940) | [[NS](#_Toc144361739)](#_Toc144362940)  |                                          | [[Diagnosis Coding Method](#_Toc144361739)](#_Toc144362940) | [[Not used](#_Toc144361739)](#_Toc144362940)                                                                 |
| [[3](#_Toc144361739)](#_Toc144362940)   | [[250](#_Toc144361739)](#_Toc144362940) | [[CE](#_Toc144361739)](#_Toc144362940) | [[R](#_Toc144361739)](#_Toc144362940)   |                                          | [[Diagnosis Code – DG1](#_Toc144361739)](#_Toc144362940)    | [[Provisional Diagnosis Code^Diagnosis Description from File 123, field 30](#_Toc144361739)](#_Toc144362940) |
| [[4](#_Toc144361739)](#_Toc144362940)   | [[40](#_Toc144361739)](#_Toc144362940)  | [[ST](#_Toc144361739)](#_Toc144362940) | [[B](#_Toc144361739)](#_Toc144362940)   |                                          | [[Diagnosis Description](#_Toc144361739)](#_Toc144362940)   | [[Not Used](#_Toc144361739)](#_Toc144362940)                                                                 |
| [[5](#_Toc144361739)](#_Toc144362940)   | [[26](#_Toc144361739)](#_Toc144362940)  | [[TS](#_Toc144361739)](#_Toc144362940) | [[O](#_Toc144361739)](#_Toc144362940)   |                                          | [[Diagnosis Date/Time](#_Toc144361739)](#_Toc144362940)     | [[Not Used](#_Toc144361739)](#_Toc144362940)                                                                 |
| [[6](#_Toc144361739)](#_Toc144362940)   | [[2](#_Toc144361739)](#_Toc144362940)   | [[IS](#_Toc144361739)](#_Toc144362940) | [[R](#_Toc144361739)](#_Toc144362940)   | [[0052](#_Toc144361739)](#_Toc144362940) | [[Diagnosis Type](#_Toc144361739)](#_Toc144362940)          | [[“W” - Working](#_Toc144361739)](#_Toc144362940)                                                            |

- 

| [[SEQ](#_Toc144361740)](#_Toc144362940) | [[LEN](#_Toc144361740)](#_Toc144362940) | [[DT](#_Toc144361740)](#_Toc144362940) | [[R/O](#_Toc144361740)](#_Toc144362940) | [[TBL#](#_Toc144361740)](#_Toc144362940) | [[Element Name](#_Toc144361740)](#_Toc144362940)                 | [[VistA Description](#_Toc144361740)](#_Toc144362940)                                                                                                                                 |
|-----------------------------------------|-----------------------------------------|----------------------------------------|-----------------------------------------|------------------------------------------|------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [[1](#_Toc144361740)](#_Toc144362940)   | [[4](#_Toc144361740)](#_Toc144362940)   | [[SI](#_Toc144361740)](#_Toc144362940) | [[R](#_Toc144361740)](#_Toc144362940)   |                                          | [[Set ID – OBR](#_Toc144361740)](#_Toc144362940)                 | [[1](#_Toc144361740)](#_Toc144362940)                                                                                                                                                 |
| [[2](#_Toc144361740)](#_Toc144362940)   | [[22](#_Toc144361740)](#_Toc144362940)  | [[EI](#_Toc144361740)](#_Toc144362940) | [[R](#_Toc144361740)](#_Toc144362940)   |                                          | [[Placer Order Number](#_Toc144361740)](#_Toc144362940)          | [[Order entry internal number;Orderable Item entry^OR from File 123, field .03](#_Toc144361740)](#_Toc144362940)                                                                      |
| [[3](#_Toc144361740)](#_Toc144362940)   | [[22](#_Toc144361740)](#_Toc144362940)  | [[EI](#_Toc144361740)](#_Toc144362940) | [[R](#_Toc144361740)](#_Toc144362940)   |                                          | [[Filler Order Number](#_Toc144361740)](#_Toc144362940)          | [[Consult entry internal number;GMRC^GMRC for all comments and TIU note internal entry number; TIU^TIU for all signed progress notes and addendums.](#_Toc144361740)](#_Toc144362940) |
| [[4](#_Toc144361740)](#_Toc144362940)   | [[250](#_Toc144361740)](#_Toc144362940) | [[CE](#_Toc144361740)](#_Toc144362940) | [[R](#_Toc144361740)](#_Toc144362940)   |                                          | [[Universal Service Identifier](#_Toc144361740)](#_Toc144362940) | [[Hardcoded value of “ZZ”](#_Toc144361740)](#_Toc144362940)                                                                                                                           |
| [[5](#_Toc144361740)](#_Toc144362940)   | [[2](#_Toc144361740)](#_Toc144362940)   | [[ID](#_Toc144361740)](#_Toc144362940) | [[NS](#_Toc144361740)](#_Toc144362940)  |                                          | [[Priority – OBR](#_Toc144361740)](#_Toc144362940)               | [[Not used](#_Toc144361740)](#_Toc144362940)                                                                                                                                          |
| [[6](#_Toc144361740)](#_Toc144362940)   | [[26](#_Toc144361740)](#_Toc144362940)  | [[TS](#_Toc144361740)](#_Toc144362940) | [[O](#_Toc144361740)](#_Toc144362940)   |                                          | [[Requested Date/Time](#_Toc144361740)](#_Toc144362940)          | [[Clinically Indicated Date from File 123, field 17](#_Toc144361740)](#_Toc144362940)                                                                                                 |

[[Note the following:](#_Toc144361740)](#_Toc144362940)

- 
- 
- 
- 

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 11%" />
<col style="width: 9%" />
<col style="width: 21%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><a href="#_Toc144362940"><span>SEQ</span></a></th>
<th><a href="#_Toc144362940"><span>LEN</span></a></th>
<th><a href="#_Toc144362940"><span>DT</span></a></th>
<th><a href="#_Toc144362940"><span>R/O</span></a></th>
<th><a href="#_Toc144362940"><span>TBL#</span></a></th>
<th><a href="#_Toc144362940"><span>Element Name</span></a></th>
<th><a href="#_Toc144362940"><span>VistA Description</span></a></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="#_Toc144362940"><span>1</span></a></td>
<td><a href="#_Toc144362940"><span>4</span></a></td>
<td><a href="#_Toc144362940"><span>SI</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Set ID – PV1</span></a></td>
<td><a href="#_Toc144362940"><span>1</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>2</span></a></td>
<td><a href="#_Toc144362940"><span>1</span></a></td>
<td><a href="#_Toc144362940"><span>IS</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td><a href="#_Toc144362940"><span>0004</span></a></td>
<td><a href="#_Toc144362940"><span>Patient Class</span></a></td>
<td><a href="#_Toc144362940"><span>I: inpatient<br />
O: outpatient</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>3</span></a></td>
<td><a href="#_Toc144362940"><span>80</span></a></td>
<td><a href="#_Toc144362940"><span>PL</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Assigned Patient Location</span></a></td>
<td><a href="#_Toc144362940"><span>Location of last inpatient movement event from VAIP(5)</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>4</span></a></td>
<td><a href="#_Toc144362940"><span>2</span></a></td>
<td><a href="#_Toc144362940"><span>IS</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Admission Type</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>5</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>CX</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Preadmit Number</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>6</span></a></td>
<td><a href="#_Toc144362940"><span>80</span></a></td>
<td><a href="#_Toc144362940"><span>PL</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Prior Patient Location</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>7</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>XCN</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td><a href="#_Toc144362940"><span>0010</span></a></td>
<td><a href="#_Toc144362940"><span>Attending Doctor</span></a></td>
<td><p><a href="#_Toc144362940"><span>Attending Provider from VAIP(18</span></a></p>
<p><a href="#_Toc144362940"><span>)</span></a></p></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>8</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>XCN</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td><a href="#_Toc144362940"><span>0010</span></a></td>
<td><a href="#_Toc144362940"><span>Referring Doctor</span></a></td>
<td><a href="#_Toc144362940"><span>Not used (Referring provider sent in PRD segment)</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>9</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>XCN</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Consulting Doctor</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>10</span></a></td>
<td><a href="#_Toc144362940"><span>3</span></a></td>
<td><a href="#_Toc144362940"><span>IS</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Hospital Service</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>11</span></a></td>
<td><a href="#_Toc144362940"><span>80</span></a></td>
<td><a href="#_Toc144362940"><span>PL</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Temporary Location</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>12</span></a></td>
<td><a href="#_Toc144362940"><span>2</span></a></td>
<td><a href="#_Toc144362940"><span>IS</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Preadmit Test Indicator</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>13</span></a></td>
<td><a href="#_Toc144362940"><span>2</span></a></td>
<td><a href="#_Toc144362940"><span>IS</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Re-admission Indicator</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>14</span></a></td>
<td><a href="#_Toc144362940"><span>6</span></a></td>
<td><a href="#_Toc144362940"><span>IS</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Admit Source</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>15</span></a></td>
<td><a href="#_Toc144362940"><span>2</span></a></td>
<td><a href="#_Toc144362940"><span>IS</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Ambulatory Status</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>16</span></a></td>
<td><a href="#_Toc144362940"><span>2</span></a></td>
<td><a href="#_Toc144362940"><span>IS</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td><a href="#_Toc144362940"><span>0099</span></a></td>
<td><a href="#_Toc144362940"><span>VIP Indicator</span></a></td>
<td><a href="#_Toc144362940"><span>R if patient restricted/sensitive</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>17</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>XCN</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td><a href="#_Toc144362940"><span>0010</span></a></td>
<td><a href="#_Toc144362940"><span>Admitting Doctor</span></a></td>
<td><a href="#_Toc144362940"><span>Primary Physician for admission from VAIP(13,5)</span></a></td>
</tr>
</tbody>
</table>

[[Note the following:](#_Toc144361741)](#_Toc144362940)

- 
- 

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 9%" />
<col style="width: 7%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 17%" />
<col style="width: 36%" />
</colgroup>
<thead>
<tr class="header">
<th><a href="#_Toc144362940"><span>SEQ</span></a></th>
<th><a href="#_Toc144362940"><span>LEN</span></a></th>
<th><a href="#_Toc144362940"><span>DT</span></a></th>
<th><a href="#_Toc144362940"><span>R/O</span></a></th>
<th><a href="#_Toc144362940"><span>TBL#</span></a></th>
<th><a href="#_Toc144362940"><span>Element Name</span></a></th>
<th><a href="#_Toc144362940"><span>VistA Description</span></a></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="#_Toc144362940"><span>1</span></a></td>
<td><a href="#_Toc144362940"><span>4</span></a></td>
<td><a href="#_Toc144362940"><span>SI</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Set ID – NTE</span></a></td>
<td><a href="#_Toc144362940"><span>Sequential Number 1-n</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>2</span></a></td>
<td><a href="#_Toc144362940"><span>8</span></a></td>
<td><a href="#_Toc144362940"><span>ID</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td><a href="#_Toc144362940"><span>0105</span></a></td>
<td><a href="#_Toc144362940"><span>Source of Comment</span></a></td>
<td><a href="#_Toc144362940"><span>P for Placer<br />
L for Ancillary</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>3</span></a></td>
<td><a href="#_Toc144362940"><span>65536</span></a></td>
<td><a href="#_Toc144362940"><span>FT</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Comment</span></a></td>
<td><p><a href="#_Toc144362940"><span>Based on message type, Resubmitted consults messages (RF1.1= IP^RESUBMITTED) will contain Reason for Request from file 123, field 20</span></a></p>
<p><a href="#_Toc144362940"><span>, Completed or Addended (RF1.1= CM^COMPLETE CM^ADDENDED)<br />
will contain TIU Progress Note from file 8925 (signed notes/addendums only). All other I13 messages will contain Activity Comments from file 123, subfile 123.25 field 5.</span></a></p></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>4</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>CE</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Comment Type</span></a></td>
<td><a href="#_Toc144362940"><span>Not used.</span></a></td>
</tr>
</tbody>
</table>

- 

[[  
](#_Toc144361866)](#_Toc144362940)

[[  
](#_Toc144361868)](#_Toc144362940)

[[HCPS will update CPRS with information entered into HCPS via HL7 message RRI (Return Referral Information). The RRI^I13 message structure is exactly the same as the REF^I13 used by CPRS to send referral information to HCPS.](#_Toc144361868)](#_Toc144362940)

| [[SEQ](#_Toc144361743)](#_Toc144362940)  | [[LEN](#_Toc144361743)](#_Toc144362940)          | [[DT](#_Toc144361743)](#_Toc144362940)      | [[R/O](#_Toc144361743)](#_Toc144362940) | [[TBL#](#_Toc144361743)](#_Toc144362940) | [[Element Name](#_Toc144361743)](#_Toc144362940)                    | [[VistA Description](#_Toc144361743)](#_Toc144362940)                                                                              |
|------------------------------------------|--------------------------------------------------|---------------------------------------------|-----------------------------------------|------------------------------------------|---------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| [[1](#_Toc144361743)](#_Toc144362940)    | [[1](#_Toc144361743)](#_Toc144362940)            | [[ST](#_Toc144361743)](#_Toc144362940)      | [[R](#_Toc144361743)](#_Toc144362940)   |                                          | [[Field Separator](#_Toc144361743)](#_Toc144362940)                 | [[\|](#_Toc144361743)](#_Toc144362940)                                                                                             |
| [[2](#_Toc144361743)](#_Toc144362940)    | [[4](#_Toc144361743)](#_Toc144362940)            | [[ST](#_Toc144361743)](#_Toc144362940)      | [[R](#_Toc144361743)](#_Toc144362940)   |                                          | [[Encoding Characters](#_Toc144361743)](#_Toc144362940)             | [[^~\\](#_Toc144361743)](#_Toc144362940)                                                                                           |
| [[3](#_Toc144361743)](#_Toc144362940)    | [[15](#_Toc144361743)](#_Toc144362940)           | [[ST](#_Toc144361743)](#_Toc144362940)      | [[R](#_Toc144361743)](#_Toc144362940)   |                                          | [[Sending Application](#_Toc144361743)](#_Toc144362940)             | [[GMRC HCP SEND](#_Toc144361743)](#_Toc144362940)                                                                                  |
| [[4](#_Toc144361743)](#_Toc144362940)    | [[20](#_Toc144361743)](#_Toc144362940)           | [[ST](#_Toc144361743)](#_Toc144362940)      | [[R](#_Toc144361743)](#_Toc144362940)   |                                          | [[Sending Facility](#_Toc144361743)](#_Toc144362940)                | [[Sending Facility, from the FACILITY NAME field of the HL7 APPLICATION entry GMRC HCP SEND](#_Toc144361743)](#_Toc144362940)      |
| [[5](#_Toc144361743)](#_Toc144362940)    | [[30](#_Toc144361743)](#_Toc144362940)           | [[ST](#_Toc144361743)](#_Toc144362940)      | [[R](#_Toc144361743)](#_Toc144362940)   |                                          | [[Receiving Application](#_Toc144361743)](#_Toc144362940)           | [[GMRC HCP RECEIVE](#_Toc144361743)](#_Toc144362940)                                                                               |
| [[6](#_Toc144361743)](#_Toc144362940)    | [[30](#_Toc144361743)](#_Toc144362940)           | [[ST](#_Toc144361743)](#_Toc144362940)      | [[NS](#_Toc144361743)](#_Toc144362940)  |                                          | [[Receiving Facility](#_Toc144361743)](#_Toc144362940)              | [[Receiving Facility, from the FACILITY NAME field of the HL7 APPLICATION entry GMRC HCP RECEIVE](#_Toc144361743)](#_Toc144362940) |
| [[7](#_Toc144361743)](#_Toc144362940)    | [[26](#_Toc144361743)](#_Toc144362940)           | [[TS](#_Toc144361743)](#_Toc144362940)      | [[R](#_Toc144361743)](#_Toc144362940)   |                                          | [[Date/Time Of Message](#_Toc144361743)](#_Toc144362940)            | [[System date/time generated by the VistA HL7 package](#_Toc144361743)](#_Toc144362940)                                            |
| [[8](#_Toc144361743)](#_Toc144362940)    | [[40](#_Toc144361743)](#_Toc144362940)           | [[ST](#_Toc144361743)](#_Toc144362940)      | [[NS](#_Toc144361743)](#_Toc144362940)  |                                          | [[Security](#_Toc144361743)](#_Toc144362940)                        | [[Not used](#_Toc144361743)](#_Toc144362940)                                                                                       |
| [[9](#_Toc144361743)](#_Toc144362940)    | [[7](#_Toc144361743)](#_Toc144362940)            | [[CM](#_Toc144361743)](#_Toc144362940)      | [[R](#_Toc144361743)](#_Toc144362940)   | [[0076](#_Toc144361743)](#_Toc144362940) |                                                                     |                                                                                                                                    |
| [[0003](#_Toc144361743)](#_Toc144362940) | [[Message Type](#_Toc144361743)](#_Toc144362940) | [[RRI^I13](#_Toc144361743)](#_Toc144362940) |                                         |                                          |                                                                     |                                                                                                                                    |
| [[10](#_Toc144361743)](#_Toc144362940)   | [[20](#_Toc144361743)](#_Toc144362940)           | [[ST](#_Toc144361743)](#_Toc144362940)      | [[R](#_Toc144361743)](#_Toc144362940)   |                                          | [[Message Control ID](#_Toc144361743)](#_Toc144362940)              | [[Facility and sequence number automatically generated by the HL7 Package](#_Toc144361743)](#_Toc144362940)                        |
| [[11](#_Toc144361743)](#_Toc144362940)   | [[1](#_Toc144361743)](#_Toc144362940)            | [[ID](#_Toc144361743)](#_Toc144362940)      | [[R](#_Toc144361743)](#_Toc144362940)   |                                          | [[Processing ID](#_Toc144361743)](#_Toc144362940)                   | [[P for Production, T for Test](#_Toc144361743)](#_Toc144362940)                                                                   |
| [[12](#_Toc144361743)](#_Toc144362940)   | [[8](#_Toc144361743)](#_Toc144362940)            | [[ID](#_Toc144361743)](#_Toc144362940)      | [[R](#_Toc144361743)](#_Toc144362940)   | [[0104](#_Toc144361743)](#_Toc144362940) | [[Version ID](#_Toc144361743)](#_Toc144362940)                      | [[2.](#_Toc144361743)[5](#_Toc144362934)](#_Toc144362940)                                                                          |
| [[13](#_Toc144362934)](#_Toc144362940)   | [[15](#_Toc144362934)](#_Toc144362940)           | [[NM](#_Toc144362934)](#_Toc144362940)      | [[NS](#_Toc144362934)](#_Toc144362940)  |                                          | [[Sequence Number](#_Toc144362934)](#_Toc144362940)                 | [[Not used](#_Toc144362934)](#_Toc144362940)                                                                                       |
| [[14](#_Toc144362934)](#_Toc144362940)   | [[180](#_Toc144362934)](#_Toc144362940)          | [[ST](#_Toc144362934)](#_Toc144362940)      | [[NS](#_Toc144362934)](#_Toc144362940)  |                                          | [[Continuation Pointer](#_Toc144362934)](#_Toc144362940)            | [[Not used](#_Toc144362934)](#_Toc144362940)                                                                                       |
| [[15](#_Toc144362934)](#_Toc144362940)   | [[2](#_Toc144362934)](#_Toc144362940)            | [[ID](#_Toc144362934)](#_Toc144362940)      | [[R](#_Toc144362934)](#_Toc144362940)   | [[0155](#_Toc144362934)](#_Toc144362940) | [[Accept Acknowledgment Type](#_Toc144362934)](#_Toc144362940)      | [[AL=Always](#_Toc144362934)](#_Toc144362940)                                                                                      |
| [[16](#_Toc144362934)](#_Toc144362940)   | [[2](#_Toc144362934)](#_Toc144362940)            | [[ID](#_Toc144362934)](#_Toc144362940)      | [[R](#_Toc144362934)](#_Toc144362940)   | [[0155](#_Toc144362934)](#_Toc144362940) | [[Application Acknowledgment Type](#_Toc144362934)](#_Toc144362940) | [[AL=Always](#_Toc144362934)](#_Toc144362940)                                                                                      |
| [[17](#_Toc144362934)](#_Toc144362940)   | [[3](#_Toc144362934)](#_Toc144362940)            | [[ID](#_Toc144362934)](#_Toc144362940)      | [[R](#_Toc144362934)](#_Toc144362940)   | [[0399](#_Toc144362934)](#_Toc144362940) | [[Country Code](#_Toc144362934)](#_Toc144362940)                    | [[USA](#_Toc144362934)](#_Toc144362940)                                                                                            |

[[Note the following:](#_Toc144362934)](#_Toc144362940)

- 
- 

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 11%" />
<col style="width: 8%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 20%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><a href="#_Toc144362940"><span>SEQ</span></a></th>
<th><a href="#_Toc144362940"><span>LEN</span></a></th>
<th><a href="#_Toc144362940"><span>DT</span></a></th>
<th><a href="#_Toc144362940"><span>R/O</span></a></th>
<th><a href="#_Toc144362940"><span>TBL#</span></a></th>
<th><a href="#_Toc144362940"><span>Element Name</span></a></th>
<th><a href="#_Toc144362940"><span>VistA Description</span></a></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="#_Toc144362940"><span>1</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>CE</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td><a href="#_Toc144362940"><span>0283</span></a></td>
<td><a href="#_Toc144362940"><span>Referral Status</span></a></td>
<td><a href="#_Toc144362940"><span>SC^RECEIVED SC^SCHEDULED IP^RESUBMITTED IP^COMMENT XX^FORWARDED CM^COMPLETE CM^ADDENDED</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>2</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>CE</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td><a href="#_Toc144362940"><span>0280</span></a></td>
<td><a href="#_Toc144362940"><span>Referral Priority</span></a></td>
<td><a href="#_Toc144362940"><span>From File 123, Field 5 (Urgency). Values are: 1 WEEK, NEXT AVAILABLE, ROUTINE, STAT, TODAY, TOMORROW AM, WITHIN 1 MONTH, WITHIN 1 WEEK, WITHIN 24 HOURS, WITHIN 72 HOURS</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>3</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>CE</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Referral Type</span></a></td>
<td><a href="#_Toc144362940"><span>Service IEN^Service Name^^Template IEN<br />
^Template Name<br />
Service IEN is pointer to File 123.5, Template IEN is pointer to File 8927.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>4</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>CE</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Referral Disposition</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>5</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>CE</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td><a href="#_Toc144362940"><span>0284</span></a></td>
<td><a href="#_Toc144362940"><span>Referral Category</span></a></td>
<td><a href="#_Toc144362940"><span>I for Inpatient, O for Outpatient based on File 123, field 14 (Service Rendered as In or Out). This could be different than the PV1.1 current patient status.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>6</span></a></td>
<td><a href="#_Toc144362940"><span>30</span></a></td>
<td><a href="#_Toc144362940"><span>EI</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Originating Referral Identifier</span></a></td>
<td><a href="#_Toc144362940"><span>IEN to File 123</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>7</span></a></td>
<td><a href="#_Toc144362940"><span>26</span></a></td>
<td><a href="#_Toc144362940"><span>TS</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Effective Date</span></a></td>
<td><a href="#_Toc144362940"><span>Referral Date of Request from File 123, field .01</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>8</span></a></td>
<td><a href="#_Toc144362940"><span>26</span></a></td>
<td><a href="#_Toc144362940"><span>TS</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Expiration Date</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>9</span></a></td>
<td><a href="#_Toc144362940"><span>26</span></a></td>
<td><a href="#_Toc144362940"><span>TS</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Process Date</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>10</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>CE</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Referral Reason</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>11</span></a></td>
<td><a href="#_Toc144362940"><span>30</span></a></td>
<td><a href="#_Toc144362940"><span>EI</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>External Referral Identifier</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
</tbody>
</table>

- 

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 11%" />
<col style="width: 8%" />
<col style="width: 9%" />
<col style="width: 11%" />
<col style="width: 21%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><a href="#_Toc144362940"><span>SEQ</span></a></th>
<th><a href="#_Toc144362940"><span>LEN</span></a></th>
<th><a href="#_Toc144362940"><span>DT</span></a></th>
<th><a href="#_Toc144362940"><span>R/O</span></a></th>
<th><a href="#_Toc144362940"><span>TBL#</span></a></th>
<th><a href="#_Toc144362940"><span>Element Name</span></a></th>
<th><a href="#_Toc144362940"><span>VistA Description</span></a></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="#_Toc144362940"><span>1</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>CE</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td><a href="#_Toc144362940"><span>0286</span></a></td>
<td><a href="#_Toc144362940"><span>Provider Role</span></a></td>
<td><a href="#_Toc144362940"><span>RP for Referring Provider</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>2</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>XPN</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Provider Name</span></a></td>
<td><a href="#_Toc144362940"><span>Provider Last Name^Provider First Name^Provider Middle Initial^^^^^^Provider DUZ<br />
Provider from File 123, field 10</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>3</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>XAD</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Provider Address</span></a></td>
<td><a href="#_Toc144362940"><span>Street Address 1^Street Address 2^City^State^Zip from File 2, fields .111, .112, .114, .115, .116</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>4</span></a></td>
<td><a href="#_Toc144362940"><span>60</span></a></td>
<td><a href="#_Toc144362940"><span>PL</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Provider Location</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>5</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>XTN</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Provider Communication Information</span></a></td>
<td><a href="#_Toc144362940"><span>^^^Email Address^^Office Phone Area Code^Office Phone Number from File 2, fields .151, .132</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>6</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>CE</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Preferred Method of Contact</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>7</span></a></td>
<td><a href="#_Toc144362940"><span>100</span></a></td>
<td><a href="#_Toc144362940"><span>PLN</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Provider Identifiers</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>8</span></a></td>
<td><a href="#_Toc144362940"><span>26</span></a></td>
<td><a href="#_Toc144362940"><span>TS</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Effective Start Date of Provider Role</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>9</span></a></td>
<td><a href="#_Toc144362940"><span>26</span></a></td>
<td><a href="#_Toc144362940"><span>TS</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Effective End Date of Provider Role</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
</tbody>
</table>

- 

| [[SEQ](#_Toc144361746)](#_Toc144362940) | [[LEN](#_Toc144361746)](#_Toc144362940) | [[DT](#_Toc144361746)](#_Toc144362940)  | [[R/O](#_Toc144361746)](#_Toc144362940) | [[TBL#](#_Toc144361746)](#_Toc144362940) | [[Element Name](#_Toc144361746)](#_Toc144362940)                                                                                                                                           | [[VistA Description](#_Toc144361746)](#_Toc144362940)                                                                                                                                                                                                                         |
|-----------------------------------------|-----------------------------------------|-----------------------------------------|-----------------------------------------|------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [[1](#_Toc144361746)](#_Toc144362940)   | [[4](#_Toc144361746)](#_Toc144362940)   | [[SI](#_Toc144361746)](#_Toc144362940)  | [[R](#_Toc144361746)](#_Toc144362940)   |                                          | [[Set ID – PID](#_Toc144361746)](#_Toc144362940)                                                                                                                                           | [[Sequential Number](#_Toc144361746)](#_Toc144362940)                                                                                                                                                                                                                         |
| [[2](#_Toc144361746)](#_Toc144362940)   | [[20](#_Toc144361746)](#_Toc144362940)  | [[CX](#_Toc144361746)](#_Toc144362940)  | [[R](#_Toc144361746)](#_Toc144362940)   |                                          | [[Patient ID](#_Toc144361746)](#_Toc144362940)                                                                                                                                             | [[ICN, including V checksum for backwards compatibility](#_Toc144361746)](#_Toc144362940)                                                                                                                                                                                     |
| [[3](#_Toc144361746)](#_Toc144362940)   | [[250](#_Toc144361746)](#_Toc144362940) | [[CX](#_Toc144361746)](#_Toc144362940)  | [[R](#_Toc144361746)](#_Toc144362940)   |                                          | [[Patient Identifier List (list is not in any specified order) Following are PID.3.5 Identifier Type Codes: NI=ICN PI=Patient DFN SS=SSN PN=Claim Number](#_Toc144361746)](#_Toc144362940) | [[Integration Control Number (including V and checksum), Social Security Number, DFN, Claim Number, all entries in the ICN History Multiple, and all alias SSNs which will correspond directly to the alias name in the name field (pid-5).](#_Toc144361746)](#_Toc144362940) |
| [[4](#_Toc144361746)](#_Toc144362940)   | [[20](#_Toc144361746)](#_Toc144362940)  | [[CX](#_Toc144361746)](#_Toc144362940)  | [[NS](#_Toc144361746)](#_Toc144362940)  |                                          | [[Alternate Patient ID – PID](#_Toc144361746)](#_Toc144362940)                                                                                                                             | [[Not used](#_Toc144361746)](#_Toc144362940)                                                                                                                                                                                                                                  |
| [[5](#_Toc144361746)](#_Toc144362940)   | [[250](#_Toc144361746)](#_Toc144362940) | [[XPN](#_Toc144361746)](#_Toc144362940) | [[R](#_Toc144361746)](#_Toc144362940)   |                                          | [[Patient Name](#_Toc144361746)](#_Toc144362940)                                                                                                                                           | [[Patient Name and all Alias entries](#_Toc144361746)](#_Toc144362940)                                                                                                                                                                                                        |
| [[6](#_Toc144361746)](#_Toc144362940)   | [[250](#_Toc144361746)](#_Toc144362940) | [[XPN](#_Toc144361746)](#_Toc144362940) | [[O](#_Toc144361746)](#_Toc144362940)   |                                          | [[Mother’s Maiden Name](#_Toc144361746)](#_Toc144362940)                                                                                                                                   | [[Mother’s Maiden Name](#_Toc144361746)](#_Toc144362940)                                                                                                                                                                                                                      |
| [[7](#_Toc144361746)](#_Toc144362940)   | [[26](#_Toc144361746)](#_Toc144362940)  | [[TS](#_Toc144361746)](#_Toc144362940)  | [[O](#_Toc144361746)](#_Toc144362940)   |                                          | [[Date/Time of Birth](#_Toc144361746)](#_Toc144362940)                                                                                                                                     | [[Date of Birth](#_Toc144361746)](#_Toc144362940)                                                                                                                                                                                                                             |
| [[8](#_Toc144361746)](#_Toc144362940)   | [[1](#_Toc144361746)](#_Toc144362940)   | [[IS](#_Toc144361746)](#_Toc144362940)  | [[O](#_Toc144361746)](#_Toc144362940)   | [[0001](#_Toc144361746)](#_Toc144362940) | [[Administrative Sex](#_Toc144361746)](#_Toc144362940)                                                                                                                                     | [[Sex](#_Toc144361746)](#_Toc144362940)                                                                                                                                                                                                                                       |
| [[9](#_Toc144361746)](#_Toc144362940)   | [[250](#_Toc144361746)](#_Toc144362940) | [[XPN](#_Toc144361746)](#_Toc144362940) | [[NS](#_Toc144361746)](#_Toc144362940)  |                                          | [[Patient Alias](#_Toc144361746)](#_Toc144362940)                                                                                                                                          | [[Not used. Alias is passed in PID-5](#_Toc144361746)](#_Toc144362940)                                                                                                                                                                                                        |
| [[10](#_Toc144361746)](#_Toc144362940)  | [[250](#_Toc144361746)](#_Toc144362940) | [[CE](#_Toc144361746)](#_Toc144362940)  | [[O](#_Toc144361746)](#_Toc144362940)   | [[0005](#_Toc144361746)](#_Toc144362940) | [[Race](#_Toc144361746)](#_Toc144362940)                                                                                                                                                   | [[Race Information. Example: 2106-3-SLF^^0005^2106-3^^CDC See Appendix A for coded values. 0005 and CDC are hardcoded.](#_Toc144361746)](#_Toc144362940)                                                                                                                      |
| [[11](#_Toc144361746)](#_Toc144362940)  | [[250](#_Toc144361746)](#_Toc144362940) | [[XAD](#_Toc144361746)](#_Toc144362940) | [[O](#_Toc144361746)](#_Toc144362940)   |                                          | [[Patient Address](#_Toc144361746)](#_Toc144362940)                                                                                                                                        | [[P=Permanent Address~N=Place of Birth~Confidential Address](#_Toc144361746)](#_Toc144362940)                                                                                                                                                                                 |
| [[12](#_Toc144361746)](#_Toc144362940)  | [[4](#_Toc144361746)](#_Toc144362940)   | [[IS](#_Toc144361746)](#_Toc144362940)  | [[O](#_Toc144361746)](#_Toc144362940)   | [[0289](#_Toc144361746)](#_Toc144362940) | [[County Code](#_Toc144361746)](#_Toc144362940)                                                                                                                                            | [[County](#_Toc144361746)](#_Toc144362940)                                                                                                                                                                                                                                    |
| [[13](#_Toc144361746)](#_Toc144362940)  | [[250](#_Toc144361746)](#_Toc144362940) | [[XTN](#_Toc144361746)](#_Toc144362940) | [[O](#_Toc144361746)](#_Toc144362940)   |                                          | [[Phone Number – Home](#_Toc144361746)](#_Toc144362940)                                                                                                                                    | [[Home Phone~Work Phone~Cell Phone~Pager^NET^INTERNET^email](#_Toc144361746)](#_Toc144362940)                                                                                                                                                                                 |
| [[14](#_Toc144361746)](#_Toc144362940)  | [[250](#_Toc144361746)](#_Toc144362940) | [[XTN](#_Toc144361746)](#_Toc144362940) | [[O](#_Toc144361746)](#_Toc144362940)   |                                          | [[Phone Number – Business](#_Toc144361746)](#_Toc144362940)                                                                                                                                | [[Work Phone (backward compatibility)](#_Toc144361746)](#_Toc144362940)                                                                                                                                                                                                       |
| [[15](#_Toc144361746)](#_Toc144362940)  | [[250](#_Toc144361746)](#_Toc144362940) | [[CE](#_Toc144361746)](#_Toc144362940)  | [[NS](#_Toc144361746)](#_Toc144362940)  | [[0296](#_Toc144361746)](#_Toc144362940) | [[Primary Language](#_Toc144361746)](#_Toc144362940)                                                                                                                                       | [[Not used](#_Toc144361746)](#_Toc144362940)                                                                                                                                                                                                                                  |
| [[16](#_Toc144361746)](#_Toc144362940)  | [[250](#_Toc144361746)](#_Toc144362940) | [[CE](#_Toc144361746)](#_Toc144362940)  | [[O](#_Toc144361746)](#_Toc144362940)   | [[0002](#_Toc144361746)](#_Toc144362940) | [[Marital Status](#_Toc144361746)](#_Toc144362940)                                                                                                                                         | [[Marital Status^^^^^^M](#_Toc144361746)](#_Toc144362940)                                                                                                                                                                                                                     |
| [[17](#_Toc144361746)](#_Toc144362940)  | [[250](#_Toc144361746)](#_Toc144362940) | [[CE](#_Toc144361746)](#_Toc144362940)  | [[O](#_Toc144361746)](#_Toc144362940)   | [[0006](#_Toc144361746)](#_Toc144362940) | [[Religion](#_Toc144361746)](#_Toc144362940)                                                                                                                                               | [[Religious Preference (code)](#_Toc144361746)](#_Toc144362940)                                                                                                                                                                                                               |
| [[18](#_Toc144361746)](#_Toc144362940)  | [[250](#_Toc144361746)](#_Toc144362940) | [[CX](#_Toc144361746)](#_Toc144362940)  | [[NS](#_Toc144361746)](#_Toc144362940)  |                                          | [[Patient Account Number](#_Toc144361746)](#_Toc144362940)                                                                                                                                 | [[Not used](#_Toc144361746)](#_Toc144362940)                                                                                                                                                                                                                                  |
| [[19](#_Toc144361746)](#_Toc144362940)  | [[16](#_Toc144361746)](#_Toc144362940)  | [[ST](#_Toc144361746)](#_Toc144362940)  | [[R](#_Toc144361746)](#_Toc144362940)   |                                          | [[SSN Number – Patient](#_Toc144361746)](#_Toc144362940)                                                                                                                                   | [[SSN](#_Toc144361746)](#_Toc144362940)                                                                                                                                                                                                                                       |
| [[20](#_Toc144361746)](#_Toc144362940)  | [[25](#_Toc144361746)](#_Toc144362940)  | [[DLN](#_Toc144361746)](#_Toc144362940) | [[NS](#_Toc144361746)](#_Toc144362940)  |                                          | [[Driver’s License Number – Patient](#_Toc144361746)](#_Toc144362940)                                                                                                                      | [[Not used](#_Toc144361746)](#_Toc144362940)                                                                                                                                                                                                                                  |
| [[21](#_Toc144361746)](#_Toc144362940)  | [[250](#_Toc144361746)](#_Toc144362940) | [[CX](#_Toc144361746)](#_Toc144362940)  | [[NS](#_Toc144361746)](#_Toc144362940)  |                                          | [[Mother’s Identifier](#_Toc144361746)](#_Toc144362940)                                                                                                                                    | [[Not used](#_Toc144361746)](#_Toc144362940)                                                                                                                                                                                                                                  |
| [[22](#_Toc144361746)](#_Toc144362940)  | [[250](#_Toc144361746)](#_Toc144362940) | [[CE](#_Toc144361746)](#_Toc144362940)  | [[O](#_Toc144361746)](#_Toc144362940)   | [[0189](#_Toc144361746)](#_Toc144362940) | [[Ethnic Group](#_Toc144361746)](#_Toc144362940)                                                                                                                                           | [[Ethnicity Information. Example: 2186-5-SLF^^0189^2186-5^^CDC](#_Toc144361746)](#_Toc144362940)                                                                                                                                                                              |
|                                         |                                         |                                         |                                         |                                          |                                                                                                                                                                                            | [[See Appendix A for coded values. 2186 and CDC are hardcoded.](#_Toc144361746)](#_Toc144362940)                                                                                                                                                                              |
| [[23](#_Toc144361746)](#_Toc144362940)  | [[250](#_Toc144361746)](#_Toc144362940) | [[ST](#_Toc144361746)](#_Toc144362940)  | [[O](#_Toc144361746)](#_Toc144362940)   |                                          | [[Birthplace](#_Toc144361746)](#_Toc144362940)                                                                                                                                             | [[Place of birth city and place of birth state](#_Toc144361746)](#_Toc144362940)                                                                                                                                                                                              |
| [[24](#_Toc144361746)](#_Toc144362940)  | [[1](#_Toc144361746)](#_Toc144362940)   | [[ID](#_Toc144361746)](#_Toc144362940)  | [[O](#_Toc144361746)](#_Toc144362940)   | [[0136](#_Toc144361746)](#_Toc144362940) | [[Multiple Birth Indicator](#_Toc144361746)](#_Toc144362940)                                                                                                                               | [[Multiple Birth Indicator \[Y for multiple birth\]](#_Toc144361746)](#_Toc144362940)                                                                                                                                                                                         |

- 

| [[SEQ](#_Toc144361747)](#_Toc144362940) | [[LEN](#_Toc144361747)](#_Toc144362940) | [[DT](#_Toc144361747)](#_Toc144362940) | [[R/O](#_Toc144361747)](#_Toc144362940) | [[TBL#](#_Toc144361747)](#_Toc144362940) | [[Element Name](#_Toc144361747)](#_Toc144362940)            | [[VistA Description](#_Toc144361747)](#_Toc144362940)                                                        |
|-----------------------------------------|-----------------------------------------|----------------------------------------|-----------------------------------------|------------------------------------------|-------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [[1](#_Toc144361747)](#_Toc144362940)   | [[4](#_Toc144361747)](#_Toc144362940)   | [[SI](#_Toc144361747)](#_Toc144362940) | [[R](#_Toc144361747)](#_Toc144362940)   |                                          | [[Set ID – DG1](#_Toc144361747)](#_Toc144362940)            | [[1](#_Toc144361747)](#_Toc144362940)                                                                        |
| [[2](#_Toc144361747)](#_Toc144362940)   | [[2](#_Toc144361747)](#_Toc144362940)   | [[ID](#_Toc144361747)](#_Toc144362940) | [[NS](#_Toc144361747)](#_Toc144362940)  |                                          | [[Diagnosis Coding Method](#_Toc144361747)](#_Toc144362940) | [[Not used](#_Toc144361747)](#_Toc144362940)                                                                 |
| [[3](#_Toc144361747)](#_Toc144362940)   | [[250](#_Toc144361747)](#_Toc144362940) | [[CE](#_Toc144361747)](#_Toc144362940) | [[R](#_Toc144361747)](#_Toc144362940)   |                                          | [[Diagnosis Code – DG1](#_Toc144361747)](#_Toc144362940)    | [[Provisional Diagnosis Code^Diagnosis Description from File 123, field 30](#_Toc144361747)](#_Toc144362940) |
| [[4](#_Toc144361747)](#_Toc144362940)   | [[40](#_Toc144361747)](#_Toc144362940)  | [[ST](#_Toc144361747)](#_Toc144362940) | [[B](#_Toc144361747)](#_Toc144362940)   |                                          | [[Diagnosis Description](#_Toc144361747)](#_Toc144362940)   | [[Not Used](#_Toc144361747)](#_Toc144362940)                                                                 |
| [[5](#_Toc144361747)](#_Toc144362940)   | [[26](#_Toc144361747)](#_Toc144362940)  | [[TS](#_Toc144361747)](#_Toc144362940) | [[O](#_Toc144361747)](#_Toc144362940)   |                                          | [[Diagnosis Date/Time](#_Toc144361747)](#_Toc144362940)     | [[Not Used](#_Toc144361747)](#_Toc144362940)                                                                 |
| [[6](#_Toc144361747)](#_Toc144362940)   | [[2](#_Toc144361747)](#_Toc144362940)   | [[IS](#_Toc144361747)](#_Toc144362940) | [[R](#_Toc144361747)](#_Toc144362940)   | [[0052](#_Toc144361747)](#_Toc144362940) | [[Diagnosis Type](#_Toc144361747)](#_Toc144362940)          | [[“W” - Working](#_Toc144361747)](#_Toc144362940)                                                            |

- 

| [[SEQ](#_Toc144361748)](#_Toc144362940) | [[LEN](#_Toc144361748)](#_Toc144362940) | [[DT](#_Toc144361748)](#_Toc144362940) | [[R/O](#_Toc144361748)](#_Toc144362940) | [[TBL#](#_Toc144361748)](#_Toc144362940) | [[Element Name](#_Toc144361748)](#_Toc144362940)                 | [[VistA Description](#_Toc144361748)](#_Toc144362940)                                                                                                                                 |
|-----------------------------------------|-----------------------------------------|----------------------------------------|-----------------------------------------|------------------------------------------|------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [[1](#_Toc144361748)](#_Toc144362940)   | [[4](#_Toc144361748)](#_Toc144362940)   | [[SI](#_Toc144361748)](#_Toc144362940) | [[R](#_Toc144361748)](#_Toc144362940)   |                                          | [[Set ID – OBR](#_Toc144361748)](#_Toc144362940)                 | [[1](#_Toc144361748)](#_Toc144362940)                                                                                                                                                 |
| [[2](#_Toc144361748)](#_Toc144362940)   | [[22](#_Toc144361748)](#_Toc144362940)  | [[EI](#_Toc144361748)](#_Toc144362940) | [[R](#_Toc144361748)](#_Toc144362940)   |                                          | [[Placer Order Number](#_Toc144361748)](#_Toc144362940)          | [[Order entry internal number;Orderable Item entry^OR from File 123, field .03](#_Toc144361748)](#_Toc144362940)                                                                      |
| [[3](#_Toc144361748)](#_Toc144362940)   | [[22](#_Toc144361748)](#_Toc144362940)  | [[EI](#_Toc144361748)](#_Toc144362940) | [[R](#_Toc144361748)](#_Toc144362940)   |                                          | [[Filler Order Number](#_Toc144361748)](#_Toc144362940)          | [[Consult entry internal number;GMRC^GMRC for all comments and TIU note internal entry number; TIU^TIU for all signed progress notes and addendums.](#_Toc144361748)](#_Toc144362940) |
| [[4](#_Toc144361748)](#_Toc144362940)   | [[250](#_Toc144361748)](#_Toc144362940) | [[CE](#_Toc144361748)](#_Toc144362940) | [[R](#_Toc144361748)](#_Toc144362940)   |                                          | [[Universal Service Identifier](#_Toc144361748)](#_Toc144362940) | [[Hardcoded value of “ZZ”](#_Toc144361748)](#_Toc144362940)                                                                                                                           |
| [[5](#_Toc144361748)](#_Toc144362940)   | [[2](#_Toc144361748)](#_Toc144362940)   | [[ID](#_Toc144361748)](#_Toc144362940) | [[NS](#_Toc144361748)](#_Toc144362940)  |                                          | [[Priority – OBR](#_Toc144361748)](#_Toc144362940)               | [[Not used](#_Toc144361748)](#_Toc144362940)                                                                                                                                          |
| [[6](#_Toc144361748)](#_Toc144362940)   | [[26](#_Toc144361748)](#_Toc144362940)  | [[TS](#_Toc144361748)](#_Toc144362940) | [[O](#_Toc144361748)](#_Toc144362940)   |                                          | [[Requested Date/Time](#_Toc144361748)](#_Toc144362940)          | [[Clinically Indicated Date from File 123, field 17](#_Toc144361748)](#_Toc144362940)                                                                                                 |

- 

[[OBR fields past OBR.6 are not used and not shown to save space.Refer to Table 14-32. The PV1 segment data is created using the IN5^VADPT call to determine current inpatient status. See PIMS technical manual for definition of the returned array VAIP. Fields not returned by the IN5^VADPT API are not used in the PV1 segment.](#_Toc144361748)](#_Toc144362940)

[[<span id="_Toc169170390" class="anchor"></span>Table 14‑32: RRI_I13 PV1 – Patient Visit Segment (Same for all message types)](#_Toc144361748)](#_Toc144362940)

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 20%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><a href="#_Toc144362940"><span>SEQ</span></a></th>
<th><a href="#_Toc144362940"><span>LEN</span></a></th>
<th><a href="#_Toc144362940"><span>DT</span></a></th>
<th><a href="#_Toc144362940"><span>R/O</span></a></th>
<th><a href="#_Toc144362940"><span>TBL#</span></a></th>
<th><a href="#_Toc144362940"><span>Element Name</span></a></th>
<th><a href="#_Toc144362940"><span>VistA Description</span></a></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="#_Toc144362940"><span>1</span></a></td>
<td><a href="#_Toc144362940"><span>4</span></a></td>
<td><a href="#_Toc144362940"><span>SI</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Set ID – PV1</span></a></td>
<td><a href="#_Toc144362940"><span>1</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>2</span></a></td>
<td><a href="#_Toc144362940"><span>1</span></a></td>
<td><a href="#_Toc144362940"><span>IS</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td><a href="#_Toc144362940"><span>0004</span></a></td>
<td><a href="#_Toc144362940"><span>Patient Class</span></a></td>
<td><a href="#_Toc144362940"><span>I: inpatient<br />
O: outpatient</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>3</span></a></td>
<td><a href="#_Toc144362940"><span>80</span></a></td>
<td><a href="#_Toc144362940"><span>PL</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Assigned Patient Location</span></a></td>
<td><a href="#_Toc144362940"><span>Location of last inpatient movement event from VAIP(5)</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>4</span></a></td>
<td><a href="#_Toc144362940"><span>2</span></a></td>
<td><a href="#_Toc144362940"><span>IS</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Admission Type</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>5</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>CX</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Preadmit Number</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>6</span></a></td>
<td><a href="#_Toc144362940"><span>80</span></a></td>
<td><a href="#_Toc144362940"><span>PL</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Prior Patient Location</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>7</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>XCN</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td><a href="#_Toc144362940"><span>0010</span></a></td>
<td><a href="#_Toc144362940"><span>Attending Doctor</span></a></td>
<td><p><a href="#_Toc144362940"><span>Attending Provider from VAIP(18</span></a></p>
<p><a href="#_Toc144362940"><span>)</span></a></p></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>8</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>XCN</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td><a href="#_Toc144362940"><span>0010</span></a></td>
<td><a href="#_Toc144362940"><span>Referring Doctor</span></a></td>
<td><a href="#_Toc144362940"><span>Not used (Referring provider sent in PRD segment)</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>9</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>XCN</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Consulting Doctor</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>10</span></a></td>
<td><a href="#_Toc144362940"><span>3</span></a></td>
<td><a href="#_Toc144362940"><span>IS</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Hospital Service</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>11</span></a></td>
<td><a href="#_Toc144362940"><span>80</span></a></td>
<td><a href="#_Toc144362940"><span>PL</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Temporary Location</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>12</span></a></td>
<td><a href="#_Toc144362940"><span>2</span></a></td>
<td><a href="#_Toc144362940"><span>IS</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Preadmit Test Indicator</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>13</span></a></td>
<td><a href="#_Toc144362940"><span>2</span></a></td>
<td><a href="#_Toc144362940"><span>IS</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Re-admission Indicator</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>14</span></a></td>
<td><a href="#_Toc144362940"><span>6</span></a></td>
<td><a href="#_Toc144362940"><span>IS</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Admit Source</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>15</span></a></td>
<td><a href="#_Toc144362940"><span>2</span></a></td>
<td><a href="#_Toc144362940"><span>IS</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Ambulatory Status</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>16</span></a></td>
<td><a href="#_Toc144362940"><span>2</span></a></td>
<td><a href="#_Toc144362940"><span>IS</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td><a href="#_Toc144362940"><span>0099</span></a></td>
<td><a href="#_Toc144362940"><span>VIP Indicator</span></a></td>
<td><a href="#_Toc144362940"><span>R if patient restricted/sensitive</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>17</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>XCN</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td><a href="#_Toc144362940"><span>0010</span></a></td>
<td><a href="#_Toc144362940"><span>Admitting Doctor</span></a></td>
<td><a href="#_Toc144362940"><span>Primary Physician for admission from VAIP(13,5)</span></a></td>
</tr>
</tbody>
</table>

[[  
](#_Toc144361749)](#_Toc144362940)

[[Note the following:](#_Toc144361749)](#_Toc144362940)

- 
- 

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 11%" />
<col style="width: 6%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 23%" />
<col style="width: 28%" />
</colgroup>
<thead>
<tr class="header">
<th><a href="#_Toc144362940"><span>SEQ</span></a></th>
<th><a href="#_Toc144362940"><span>LEN</span></a></th>
<th><a href="#_Toc144362940"><span>DT</span></a></th>
<th><a href="#_Toc144362940"><span>R/O</span></a></th>
<th><a href="#_Toc144362940"><span>TBL#</span></a></th>
<th><a href="#_Toc144362940"><span>Element Name</span></a></th>
<th><a href="#_Toc144362940"><span>VistA Description</span></a></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="#_Toc144362940"><span>1</span></a></td>
<td><a href="#_Toc144362940"><span>4</span></a></td>
<td><a href="#_Toc144362940"><span>SI</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Set ID – NTE</span></a></td>
<td><a href="#_Toc144362940"><span>Sequential Number 1-n</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>2</span></a></td>
<td><a href="#_Toc144362940"><span>8</span></a></td>
<td><a href="#_Toc144362940"><span>ID</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td><a href="#_Toc144362940"><span>0105</span></a></td>
<td><a href="#_Toc144362940"><span>Source of Comment</span></a></td>
<td><a href="#_Toc144362940"><span>P for Placer<br />
L for Ancillary</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>3</span></a></td>
<td><a href="#_Toc144362940"><span>65536</span></a></td>
<td><a href="#_Toc144362940"><span>FT</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Comment</span></a></td>
<td><p><a href="#_Toc144362940"><span>Based on message type, Resubmitted consults messages (RF1.1= IP^RESUBMITTED) will contain Reason for Request from file 123, field 20</span></a></p>
<p><a href="#_Toc144362940"><span>, Completed or Addended (RF1.1= CM^COMPLETE CM^ADDENDED) will contain TIU Progress Note from file 8925 (signed notes/addendums only). All other I13 messages will contain Activity Comments from file 123, subfile 123.25 field 5.</span></a></p></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>4</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>CE</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Comment Type</span></a></td>
<td><a href="#_Toc144362940"><span>Not used.</span></a></td>
</tr>
</tbody>
</table>

- 

[[HCPS will send Notes/Comments/Status changes made in the Referral in HCPS.  
](#_Toc144362942)](#_Toc144362940)

[[  
](#_Toc144361870)](#_Toc144362940)

[[  
](#_Toc144361872)](#_Toc144362940)

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 11%" />
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 23%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><a href="#_Toc144362940"><span>SEQ</span></a></th>
<th><a href="#_Toc144362940"><span>LEN</span></a></th>
<th><a href="#_Toc144362940"><span>DT</span></a></th>
<th><a href="#_Toc144362940"><span>R/O</span></a></th>
<th><a href="#_Toc144362940"><span>TBL#</span></a></th>
<th><a href="#_Toc144362940"><span>Element Name</span></a></th>
<th><a href="#_Toc144362940"><span>VistA Description</span></a></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="#_Toc144362940"><span>1</span></a></td>
<td><a href="#_Toc144362940"><span>1</span></a></td>
<td><a href="#_Toc144362940"><span>ST</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Field Separator</span></a></td>
<td><a href="#_Toc144362940"><span>|</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>2</span></a></td>
<td><a href="#_Toc144362940"><span>4</span></a></td>
<td><a href="#_Toc144362940"><span>ST</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Encoding Characters</span></a></td>
<td><a href="#_Toc144362940"><span>^~\&amp;</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>3</span></a></td>
<td><a href="#_Toc144362940"><span>15</span></a></td>
<td><a href="#_Toc144362940"><span>ST</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Sending Application</span></a></td>
<td><a href="#_Toc144362940"><span>GMRC HCP SEND</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>4</span></a></td>
<td><a href="#_Toc144362940"><span>20</span></a></td>
<td><a href="#_Toc144362940"><span>ST</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Sending Facility</span></a></td>
<td><a href="#_Toc144362940"><span>Sending Facility, from the FACILITY NAME field of the HL7 APPLICATION entry GMRC HCP SEND</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>5</span></a></td>
<td><a href="#_Toc144362940"><span>30</span></a></td>
<td><a href="#_Toc144362940"><span>ST</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Receiving Application</span></a></td>
<td><a href="#_Toc144362940"><span>GMRC HCP RECEIVE</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>6</span></a></td>
<td><a href="#_Toc144362940"><span>30</span></a></td>
<td><a href="#_Toc144362940"><span>ST</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Receiving Facility</span></a></td>
<td><a href="#_Toc144362940"><span>Receiving Facility, from the FACILITY NAME field of the HL7 APPLICATION entry GMRC HCP RECEIVE</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>7</span></a></td>
<td><a href="#_Toc144362940"><span>26</span></a></td>
<td><a href="#_Toc144362940"><span>TS</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Date/Time Of Message</span></a></td>
<td><a href="#_Toc144362940"><span>System date/time generated by the VistA HL7 package</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>8</span></a></td>
<td><a href="#_Toc144362940"><span>40</span></a></td>
<td><a href="#_Toc144362940"><span>ST</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Security</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>9</span></a></td>
<td><a href="#_Toc144362940"><span>7</span></a></td>
<td><a href="#_Toc144362940"><span>CM</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td><a href="#_Toc144362940"><span>0076<br />
0003</span></a></td>
<td><a href="#_Toc144362940"><span>Message Type</span></a></td>
<td><a href="#_Toc144362940"><span>REF^I14</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>10</span></a></td>
<td><a href="#_Toc144362940"><span>20</span></a></td>
<td><a href="#_Toc144362940"><span>ST</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Message Control ID</span></a></td>
<td><a href="#_Toc144362940"><span>Facility and sequence number automatically generated by the VistA HL7 Package</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>11</span></a></td>
<td><a href="#_Toc144362940"><span>1</span></a></td>
<td><a href="#_Toc144362940"><span>ID</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Processing ID</span></a></td>
<td><a href="#_Toc144362940"><span>P for Production, T for Test</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>12</span></a></td>
<td><a href="#_Toc144362940"><span>8</span></a></td>
<td><a href="#_Toc144362940"><span>ID</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td><a href="#_Toc144362940"><span>0104</span></a></td>
<td><a href="#_Toc144362940"><span>Version ID</span></a></td>
<td><a href="#_Toc144362940"><span>2.</span><span>5</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>13</span></a></td>
<td><a href="#_Toc144362940"><span>15</span></a></td>
<td><a href="#_Toc144362940"><span>NM</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Sequence Number</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>14</span></a></td>
<td><a href="#_Toc144362940"><span>180</span></a></td>
<td><a href="#_Toc144362940"><span>ST</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Continuation Pointer</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>15</span></a></td>
<td><a href="#_Toc144362940"><span>2</span></a></td>
<td><a href="#_Toc144362940"><span>ID</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td><a href="#_Toc144362940"><span>0155</span></a></td>
<td><a href="#_Toc144362940"><span>Accept Acknowledgment Type</span></a></td>
<td><a href="#_Toc144362940"><span>AL=Always</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>16</span></a></td>
<td><a href="#_Toc144362940"><span>2</span></a></td>
<td><a href="#_Toc144362940"><span>ID</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td><a href="#_Toc144362940"><span>0155</span></a></td>
<td><a href="#_Toc144362940"><span>Application Acknowledgment Type</span></a></td>
<td><a href="#_Toc144362940"><span>AL=Always</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>17</span></a></td>
<td><a href="#_Toc144362940"><span>3</span></a></td>
<td><a href="#_Toc144362940"><span>ID</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td><a href="#_Toc144362940"><span>0399</span></a></td>
<td><a href="#_Toc144362940"><span>Country Code</span></a></td>
<td><a href="#_Toc144362940"><span>USA</span></a></td>
</tr>
</tbody>
</table>

[[Refer to Table 14-35.](#_Toc144362934)](#_Toc144362940)

[[<span id="_Toc169170393" class="anchor"></span>Table 14‑35: REF_I14 RF1 – Referral Information Segment](#_Toc144362934)](#_Toc144362940)

| [[SEQ](#_Toc144361752)](#_Toc144362940) | [[LEN](#_Toc144361752)](#_Toc144362940) | [[DT](#_Toc144361752)](#_Toc144362940) | [[R/O](#_Toc144361752)](#_Toc144362940) | [[TBL#](#_Toc144361752)](#_Toc144362940) | [[Element Name](#_Toc144361752)](#_Toc144362940)                    | [[VistA Description](#_Toc144361752)](#_Toc144362940)                                                                                                                                                        |
|-----------------------------------------|-----------------------------------------|----------------------------------------|-----------------------------------------|------------------------------------------|---------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [[1](#_Toc144361752)](#_Toc144362940)   | [[250](#_Toc144361752)](#_Toc144362940) | [[CE](#_Toc144361752)](#_Toc144362940) | [[O](#_Toc144361752)](#_Toc144362940)   | [[0283](#_Toc144361752)](#_Toc144362940) | [[Referral Status](#_Toc144361752)](#_Toc144362940)                 | [[CA^CANCELLED DC^DISCONTINUED](#_Toc144361752)](#_Toc144362940)                                                                                                                                             |
| [[2](#_Toc144361752)](#_Toc144362940)   | [[250](#_Toc144361752)](#_Toc144362940) | [[CE](#_Toc144361752)](#_Toc144362940) | [[O](#_Toc144361752)](#_Toc144362940)   | [[0280](#_Toc144361752)](#_Toc144362940) | [[Referral Priority](#_Toc144361752)](#_Toc144362940)               | [[From File 123, Field 5 (Urgency). Values are: 1 WEEK, NEXT AVAILABLE, ROUTINE, STAT, TODAY, TOMORROW AM, WITHIN 1 MONTH, WITHIN 1 WEEK, WITHIN 24 HOURS, WITHIN 72 HOURS](#_Toc144361752)](#_Toc144362940) |
| [[3](#_Toc144361752)](#_Toc144362940)   | [[250](#_Toc144361752)](#_Toc144362940) | [[CE](#_Toc144361752)](#_Toc144362940) | [[O](#_Toc144361752)](#_Toc144362940)   |                                          | [[Referral Type](#_Toc144361752)](#_Toc144362940)                   | [[Service IEN^Service Name^^Template IEN ^Template Name Service IEN is pointer to File 123.5, Template IEN is pointer to File 8927.](#_Toc144361752)](#_Toc144362940)                                        |
| [[4](#_Toc144361752)](#_Toc144362940)   | [[250](#_Toc144361752)](#_Toc144362940) | [[CE](#_Toc144361752)](#_Toc144362940) | [[NS](#_Toc144361752)](#_Toc144362940)  |                                          | [[Referral Disposition](#_Toc144361752)](#_Toc144362940)            | [[Not used.](#_Toc144361752)](#_Toc144362940)                                                                                                                                                                |
| [[5](#_Toc144361752)](#_Toc144362940)   | [[250](#_Toc144361752)](#_Toc144362940) | [[CE](#_Toc144361752)](#_Toc144362940) | [[O](#_Toc144361752)](#_Toc144362940)   | [[0284](#_Toc144361752)](#_Toc144362940) | [[Referral Category](#_Toc144361752)](#_Toc144362940)               | [[I for Inpatient, O for Outpatient based on File 123, field 14 (Service Rendered as In or Out). This could be different than the PV1.1 current patient status.](#_Toc144361752)](#_Toc144362940)            |
| [[6](#_Toc144361752)](#_Toc144362940)   | [[30](#_Toc144361752)](#_Toc144362940)  | [[EI](#_Toc144361752)](#_Toc144362940) | [[R](#_Toc144361752)](#_Toc144362940)   |                                          | [[Originating Referral Identifier](#_Toc144361752)](#_Toc144362940) | [[IEN to File 123](#_Toc144361752)](#_Toc144362940)                                                                                                                                                          |
| [[7](#_Toc144361752)](#_Toc144362940)   | [[26](#_Toc144361752)](#_Toc144362940)  | [[TS](#_Toc144361752)](#_Toc144362940) | [[O](#_Toc144361752)](#_Toc144362940)   |                                          | [[Effective Date](#_Toc144361752)](#_Toc144362940)                  | [[Referral Date of Request from File 123, field .01](#_Toc144361752)](#_Toc144362940)                                                                                                                        |
| [[8](#_Toc144361752)](#_Toc144362940)   | [[26](#_Toc144361752)](#_Toc144362940)  | [[TS](#_Toc144361752)](#_Toc144362940) | [[NS](#_Toc144361752)](#_Toc144362940)  |                                          | [[Expiration Date](#_Toc144361752)](#_Toc144362940)                 | [[Not used](#_Toc144361752)](#_Toc144362940)                                                                                                                                                                 |
| [[9](#_Toc144361752)](#_Toc144362940)   | [[26](#_Toc144361752)](#_Toc144362940)  | [[TS](#_Toc144361752)](#_Toc144362940) | [[NS](#_Toc144361752)](#_Toc144362940)  |                                          | [[Process Date](#_Toc144361752)](#_Toc144362940)                    | [[Not used](#_Toc144361752)](#_Toc144362940)                                                                                                                                                                 |
| [[10](#_Toc144361752)](#_Toc144362940)  | [[250](#_Toc144361752)](#_Toc144362940) | [[CE](#_Toc144361752)](#_Toc144362940) | [[NS](#_Toc144361752)](#_Toc144362940)  |                                          | [[Referral Reason](#_Toc144361752)](#_Toc144362940)                 | [[Not used](#_Toc144361752)](#_Toc144362940)                                                                                                                                                                 |
| [[11](#_Toc144361752)](#_Toc144362940)  | [[30](#_Toc144361752)](#_Toc144362940)  | [[EI](#_Toc144361752)](#_Toc144362940) | [[NS](#_Toc144361752)](#_Toc144362940)  |                                          | [[External Referral Identifier](#_Toc144361752)](#_Toc144362940)    | [[Not used](#_Toc144361752)](#_Toc144362940)                                                                                                                                                                 |

[[Refer to Table 14-36.](#_Toc144361752)](#_Toc144362940)

[[<span id="_Toc169170394" class="anchor"></span>Table 14‑36: REF_I14 PRD – Provider Data Segment (Same for all message types)](#_Toc144361752)](#_Toc144362940)

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 11%" />
<col style="width: 8%" />
<col style="width: 11%" />
<col style="width: 9%" />
<col style="width: 22%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th><a href="#_Toc144362940"><span>SEQ</span></a></th>
<th><a href="#_Toc144362940"><span>LEN</span></a></th>
<th><a href="#_Toc144362940"><span>DT</span></a></th>
<th><a href="#_Toc144362940"><span>R/O</span></a></th>
<th><a href="#_Toc144362940"><span>TBL#</span></a></th>
<th><a href="#_Toc144362940"><span>Element Name</span></a></th>
<th><a href="#_Toc144362940"><span>VistA Description</span></a></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="#_Toc144362940"><span>1</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>CE</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td><a href="#_Toc144362940"><span>0286</span></a></td>
<td><a href="#_Toc144362940"><span>Provider Role</span></a></td>
<td><a href="#_Toc144362940"><span>RP for Referring Provider</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>2</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>XPN</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Provider Name</span></a></td>
<td><a href="#_Toc144362940"><span>Provider Last Name^Provider First Name^Provider Middle Initial^^^^^^Provider DUZ<br />
Provider from File 123, field 10</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>3</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>XAD</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Provider Address</span></a></td>
<td><a href="#_Toc144362940"><span>Street Address 1^Street Address 2^City^State^Zip from File 200, fields .111, .112, .114, .115, .116</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>4</span></a></td>
<td><a href="#_Toc144362940"><span>60</span></a></td>
<td><a href="#_Toc144362940"><span>PL</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Provider Location</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>5</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>XTN</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Provider Communication Information</span></a></td>
<td><a href="#_Toc144362940"><span>^^^Email Address^^Office Phone Area Code^Office Phone Number from File 200, fields .151, .132</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>6</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>CE</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Preferred Method of Contact</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>7</span></a></td>
<td><a href="#_Toc144362940"><span>100</span></a></td>
<td><a href="#_Toc144362940"><span>PLN</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Provider Identifiers</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>8</span></a></td>
<td><a href="#_Toc144362940"><span>26</span></a></td>
<td><a href="#_Toc144362940"><span>TS</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Effective Start Date of Provider Role</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>9</span></a></td>
<td><a href="#_Toc144362940"><span>26</span></a></td>
<td><a href="#_Toc144362940"><span>TS</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Effective End Date of Provider Role</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
</tbody>
</table>

[[  
](#_Toc144361753)](#_Toc144362940)

[[Refer to Table 14-37. Note REF_I14 PID – Patient Id Segment is generated by the VistA API.](#_Toc144361753)](#_Toc144362940)

[[<span id="_Toc169170395" class="anchor"></span>Table 14‑37: REF_I14 PID – Patient Id Segment (Same for all message types)](#_Toc144361753)](#_Toc144362940)

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 19%" />
<col style="width: 43%" />
</colgroup>
<thead>
<tr class="header">
<th><a href="#_Toc144362940"><span>SEQ</span></a></th>
<th><a href="#_Toc144362940"><span>LEN</span></a></th>
<th><a href="#_Toc144362940"><span>DT</span></a></th>
<th><a href="#_Toc144362940"><span>R/O</span></a></th>
<th><a href="#_Toc144362940"><span>TBL#</span></a></th>
<th><a href="#_Toc144362940"><span>Element Name</span></a></th>
<th><a href="#_Toc144362940"><span>VistA Description</span></a></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="#_Toc144362940"><span>1</span></a></td>
<td><a href="#_Toc144362940"><span>4</span></a></td>
<td><a href="#_Toc144362940"><span>SI</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Set ID – PID</span></a></td>
<td><a href="#_Toc144362940"><span>Sequential Number</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>2</span></a></td>
<td><a href="#_Toc144362940"><span>20</span></a></td>
<td><a href="#_Toc144362940"><span>CX</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Patient ID</span></a></td>
<td><a href="#_Toc144362940"><span>ICN, including V checksum for backwards compatibility.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>3</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>CX</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Patient Identifier List (list is not in any specified order) Following are PID.3.</span><span>5 Identifier Codes: NI=ICN,<br />
PI=Patient DFN, SS=SSN<br />
PN=Claim Number</span></a></td>
<td><a href="#_Toc144362940"><span>Integration Control Number (including V and checksum), Social Security Number, DFN, Claim Number, all entries in the ICN History Multiple, and all alias SSNs which will correspond directly to the alias name in the name field (PID-5).</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>4</span></a></td>
<td><a href="#_Toc144362940"><span>20</span></a></td>
<td><a href="#_Toc144362940"><span>CX</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Alternate Patient ID – PID</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>5</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>XPN</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Patient Name</span></a></td>
<td><a href="#_Toc144362940"><span>Patient Name and all Alias entries</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>6</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>XPN</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Mother’s Maiden Name</span></a></td>
<td><a href="#_Toc144362940"><span>Mother’s Maiden Name</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>7</span></a></td>
<td><a href="#_Toc144362940"><span>26</span></a></td>
<td><a href="#_Toc144362940"><span>TS</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Date/Time of Birth</span></a></td>
<td><a href="#_Toc144362940"><span>Date of Birth</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>8</span></a></td>
<td><a href="#_Toc144362940"><span>1</span></a></td>
<td><a href="#_Toc144362940"><span>IS</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td><a href="#_Toc144362940"><span>0001</span></a></td>
<td><a href="#_Toc144362940"><span>Administrative Sex</span></a></td>
<td><a href="#_Toc144362940"><span>Sex</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>9</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>XPN</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Patient Alias</span></a></td>
<td><a href="#_Toc144362940"><span>Not used. Alias is passed in PID-5</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>10</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>CE</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td><a href="#_Toc144362940"><span>0005</span></a></td>
<td><a href="#_Toc144362940"><span>Race</span></a></td>
<td><a href="#_Toc144362940"><span>Race Information. Example: 2106-3-SLF^^0005^2106-3^^CDC See Appendix A for coded values. 0005 and CDC are hardcoded.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>11</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>XAD</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Patient Address</span></a></td>
<td><a href="#_Toc144362940"><span>P=Permanent Address~N=Place of Birth~Confidential Address</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>12</span></a></td>
<td><a href="#_Toc144362940"><span>4</span></a></td>
<td><a href="#_Toc144362940"><span>IS</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td><a href="#_Toc144362940"><span>0289</span></a></td>
<td><a href="#_Toc144362940"><span>County Code</span></a></td>
<td><a href="#_Toc144362940"><span>County</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>13</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>XTN</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Phone Number – Home</span></a></td>
<td><a href="#_Toc144362940"><span>Home Phone~Work Phone~Cell Phone~Pager^NET^INTERNET^email</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>14</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>XTN</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Phone Number – Business</span></a></td>
<td><a href="#_Toc144362940"><span>Work Phone (backward compatibility)</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>15</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>CE</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td><a href="#_Toc144362940"><span>0296</span></a></td>
<td><a href="#_Toc144362940"><span>Primary Language</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>16</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>CE</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td><a href="#_Toc144362940"><span>0002</span></a></td>
<td><a href="#_Toc144362940"><span>Marital Status</span></a></td>
<td><a href="#_Toc144362940"><span>Marital Status^^^^^^M</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>17</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>CE</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td><a href="#_Toc144362940"><span>0006</span></a></td>
<td><a href="#_Toc144362940"><span>Religion</span></a></td>
<td><a href="#_Toc144362940"><span>Religious Preference (code)</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>18</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>CX</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Patient Account Number</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>19</span></a></td>
<td><a href="#_Toc144362940"><span>16</span></a></td>
<td><a href="#_Toc144362940"><span>ST</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>SSN Number – Patient</span></a></td>
<td><a href="#_Toc144362940"><span>SSN</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>20</span></a></td>
<td><a href="#_Toc144362940"><span>25</span></a></td>
<td><a href="#_Toc144362940"><span>DLN</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Driver’s License Number – Patient</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>21</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>CX</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Mother’s Identifier</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>22</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>CE</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td><a href="#_Toc144362940"><span>0189</span></a></td>
<td><a href="#_Toc144362940"><span>Ethnic Group</span></a></td>
<td><a href="#_Toc144362940"><span>Ethnicity Information. Example: 2186-5-SLF^^0189^2186-5^^CDC<br />
See Appendix A for coded values. 2186 and CDC are hardcoded.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>23</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>ST</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Birthplace</span></a></td>
<td><a href="#_Toc144362940"><span>Place of birth city and place of birth state</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>24</span></a></td>
<td><a href="#_Toc144362940"><span>1</span></a></td>
<td><a href="#_Toc144362940"><span>ID</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td><a href="#_Toc144362940"><span>0136</span></a></td>
<td><a href="#_Toc144362940"><span>Multiple Birth Indicator</span></a></td>
<td><a href="#_Toc144362940"><span>Multiple Birth Indicator [Y for multiple birth]</span></a></td>
</tr>
</tbody>
</table>

- 

| [[SEQ](#_Toc144361755)](#_Toc144362940) | [[LEN](#_Toc144361755)](#_Toc144362940) | [[DT](#_Toc144361755)](#_Toc144362940) | [[R/O](#_Toc144361755)](#_Toc144362940) | [[TBL#](#_Toc144361755)](#_Toc144362940) | [[Element Name](#_Toc144361755)](#_Toc144362940)            | [[VistA Description](#_Toc144361755)](#_Toc144362940)                                                        |
|-----------------------------------------|-----------------------------------------|----------------------------------------|-----------------------------------------|------------------------------------------|-------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| [[1](#_Toc144361755)](#_Toc144362940)   | [[4](#_Toc144361755)](#_Toc144362940)   | [[SI](#_Toc144361755)](#_Toc144362940) | [[R](#_Toc144361755)](#_Toc144362940)   |                                          | [[Set ID – DG1](#_Toc144361755)](#_Toc144362940)            | [[1](#_Toc144361755)](#_Toc144362940)                                                                        |
| [[2](#_Toc144361755)](#_Toc144362940)   | [[2](#_Toc144361755)](#_Toc144362940)   | [[ID](#_Toc144361755)](#_Toc144362940) | [[NS](#_Toc144361755)](#_Toc144362940)  |                                          | [[Diagnosis Coding Method](#_Toc144361755)](#_Toc144362940) | [[Not used](#_Toc144361755)](#_Toc144362940)                                                                 |
| [[3](#_Toc144361755)](#_Toc144362940)   | [[250](#_Toc144361755)](#_Toc144362940) | [[CE](#_Toc144361755)](#_Toc144362940) | [[R](#_Toc144361755)](#_Toc144362940)   |                                          | [[Diagnosis Code – DG1](#_Toc144361755)](#_Toc144362940)    | [[Provisional Diagnosis Code^Diagnosis Description from File 123, field 30](#_Toc144361755)](#_Toc144362940) |
| [[4](#_Toc144361755)](#_Toc144362940)   | [[40](#_Toc144361755)](#_Toc144362940)  | [[ST](#_Toc144361755)](#_Toc144362940) | [[B](#_Toc144361755)](#_Toc144362940)   |                                          | [[Diagnosis Description](#_Toc144361755)](#_Toc144362940)   | [[Not used](#_Toc144361755)](#_Toc144362940)                                                                 |
| [[5](#_Toc144361755)](#_Toc144362940)   | [[26](#_Toc144361755)](#_Toc144362940)  | [[TS](#_Toc144361755)](#_Toc144362940) | [[O](#_Toc144361755)](#_Toc144362940)   |                                          | [[Diagnosis Date/Time](#_Toc144361755)](#_Toc144362940)     | [[Not used](#_Toc144361755)](#_Toc144362940)                                                                 |
| [[6](#_Toc144361755)](#_Toc144362940)   | [[2](#_Toc144361755)](#_Toc144362940)   | [[IS](#_Toc144361755)](#_Toc144362940) | [[R](#_Toc144361755)](#_Toc144362940)   | [[0052](#_Toc144361755)](#_Toc144362940) | [[Diagnosis Type](#_Toc144361755)](#_Toc144362940)          | [[“W” - Working](#_Toc144361755)](#_Toc144362940)                                                            |

- 

[[DG1 fields past DG1.6 are not used and are not shown to save space.](#_Toc144361755)](#_Toc144362940)

[[  
](#_Toc144361755)](#_Toc144362940)

[[Refer to Table 14-39.](#_Toc144361755)](#_Toc144362940)

[[<span id="_Toc169170397" class="anchor"></span>Table 14‑39: REF_I14 OBR – Observation Request Segment (Same for all message types)](#_Toc144361755)](#_Toc144362940)

| [[SEQ](#_Toc144361756)](#_Toc144362940) | [[LEN](#_Toc144361756)](#_Toc144362940) | [[DT](#_Toc144361756)](#_Toc144362940) | [[R/O](#_Toc144361756)](#_Toc144362940) | [[TBL#](#_Toc144361756)](#_Toc144362940) | [[Element Name](#_Toc144361756)](#_Toc144362940)                 | [[VistA Description](#_Toc144361756)](#_Toc144362940)                                                            |
|-----------------------------------------|-----------------------------------------|----------------------------------------|-----------------------------------------|------------------------------------------|------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| [[1](#_Toc144361756)](#_Toc144362940)   | [[4](#_Toc144361756)](#_Toc144362940)   | [[SI](#_Toc144361756)](#_Toc144362940) | [[R](#_Toc144361756)](#_Toc144362940)   |                                          | [[Set ID – OBR](#_Toc144361756)](#_Toc144362940)                 | [[1](#_Toc144361756)](#_Toc144362940)                                                                            |
| [[2](#_Toc144361756)](#_Toc144362940)   | [[22](#_Toc144361756)](#_Toc144362940)  | [[EI](#_Toc144361756)](#_Toc144362940) | [[R](#_Toc144361756)](#_Toc144362940)   |                                          | [[Placer Order Number](#_Toc144361756)](#_Toc144362940)          | [[Order entry internal number;Orderable Item entry^OR from File 123, field .03](#_Toc144361756)](#_Toc144362940) |
| [[3](#_Toc144361756)](#_Toc144362940)   | [[22](#_Toc144361756)](#_Toc144362940)  | [[EI](#_Toc144361756)](#_Toc144362940) | [[R](#_Toc144361756)](#_Toc144362940)   |                                          | [[Filler Order Number](#_Toc144361756)](#_Toc144362940)          | [[Consult entry internal number;GMRC^GMRC](#_Toc144361756)](#_Toc144362940)                                      |
| [[4](#_Toc144361756)](#_Toc144362940)   | [[250](#_Toc144361756)](#_Toc144362940) | [[CE](#_Toc144361756)](#_Toc144362940) | [[NS](#_Toc144361756)](#_Toc144362940)  |                                          | [[Universal Service Identifier](#_Toc144361756)](#_Toc144362940) | [[Hardcoded value of “ZZ”](#_Toc144361756)](#_Toc144362940)                                                      |
| [[5](#_Toc144361756)](#_Toc144362940)   | [[2](#_Toc144361756)](#_Toc144362940)   | [[ID](#_Toc144361756)](#_Toc144362940) | [[NS](#_Toc144361756)](#_Toc144362940)  |                                          | [[Priority – OBR](#_Toc144361756)](#_Toc144362940)               | [[Not used](#_Toc144361756)](#_Toc144362940)                                                                     |
| [[6](#_Toc144361756)](#_Toc144362940)   | [[26](#_Toc144361756)](#_Toc144362940)  | [[TS](#_Toc144361756)](#_Toc144362940) | [[O](#_Toc144361756)](#_Toc144362940)   |                                          | [[Requested Date/Time](#_Toc144361756)](#_Toc144362940)          | [[Clinically Indicated Date from File 123, field 17](#_Toc144361756)](#_Toc144362940)                            |

[[Note the following:](#_Toc144361756)](#_Toc144362940)

- 
- 
- 
- 

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 21%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th><a href="#_Toc144362940"><span>SEQ</span></a></th>
<th><a href="#_Toc144362940"><span>LEN</span></a></th>
<th><a href="#_Toc144362940"><span>DT</span></a></th>
<th><a href="#_Toc144362940"><span>R/O</span></a></th>
<th><a href="#_Toc144362940"><span>TBL#</span></a></th>
<th><a href="#_Toc144362940"><span>Element Name</span></a></th>
<th><a href="#_Toc144362940"><span>VistA Description</span></a></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="#_Toc144362940"><span>1</span></a></td>
<td><a href="#_Toc144362940"><span>4</span></a></td>
<td><a href="#_Toc144362940"><span>SI</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Set ID – PV1</span></a></td>
<td><a href="#_Toc144362940"><span>1</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>2</span></a></td>
<td><a href="#_Toc144362940"><span>1</span></a></td>
<td><a href="#_Toc144362940"><span>IS</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td><a href="#_Toc144362940"><span>0004</span></a></td>
<td><a href="#_Toc144362940"><span>Patient Class</span></a></td>
<td><a href="#_Toc144362940"><span>I: inpatient O: outpatient</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>3</span></a></td>
<td><a href="#_Toc144362940"><span>80</span></a></td>
<td><a href="#_Toc144362940"><span>PL</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Assigned Patient Location</span></a></td>
<td><a href="#_Toc144362940"><span>Location of last inpatient movement event from VAIP(5)</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>4</span></a></td>
<td><a href="#_Toc144362940"><span>2</span></a></td>
<td><a href="#_Toc144362940"><span>IS</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Admission Type</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>5</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>CX</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Preadmit Number</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>6</span></a></td>
<td><a href="#_Toc144362940"><span>80</span></a></td>
<td><a href="#_Toc144362940"><span>PL</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Prior Patient Location</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>7</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>XCN</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td><a href="#_Toc144362940"><span>0010</span></a></td>
<td><a href="#_Toc144362940"><span>Attending Doctor</span></a></td>
<td><p><a href="#_Toc144362940"><span>Attending Provider from VAIP(18</span></a></p>
<p><a href="#_Toc144362940"><span>)</span></a></p></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>8</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>XCN</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Referring Doctor</span></a></td>
<td><a href="#_Toc144362940"><span>Not used (Referring provider sent in PRD segment)</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>9</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>XCN</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Consulting Doctor</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>10</span></a></td>
<td><a href="#_Toc144362940"><span>3</span></a></td>
<td><a href="#_Toc144362940"><span>IS</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Hospital Service</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>11</span></a></td>
<td><a href="#_Toc144362940"><span>80</span></a></td>
<td><a href="#_Toc144362940"><span>PL</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Temporary Location</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>12</span></a></td>
<td><a href="#_Toc144362940"><span>2</span></a></td>
<td><a href="#_Toc144362940"><span>IS</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Preadmit Test Indicator</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>13</span></a></td>
<td><a href="#_Toc144362940"><span>2</span></a></td>
<td><a href="#_Toc144362940"><span>IS</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Re-admission Indicator</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>14</span></a></td>
<td><a href="#_Toc144362940"><span>6</span></a></td>
<td><a href="#_Toc144362940"><span>IS</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Admit Source</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>15</span></a></td>
<td><a href="#_Toc144362940"><span>2</span></a></td>
<td><a href="#_Toc144362940"><span>IS</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Ambulatory Status</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>16</span></a></td>
<td><a href="#_Toc144362940"><span>2</span></a></td>
<td><a href="#_Toc144362940"><span>IS</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td><a href="#_Toc144362940"><span>0099</span></a></td>
<td><a href="#_Toc144362940"><span>VIP Indicator</span></a></td>
<td><a href="#_Toc144362940"><span>R if patient restricted/sensitive</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>17</span></a></td>
<td><a href="#_Toc144362940"><span>250</span></a></td>
<td><a href="#_Toc144362940"><span>XCN</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td><a href="#_Toc144362940"><span>0010</span></a></td>
<td><a href="#_Toc144362940"><span>Admitting Doctor</span></a></td>
<td><a href="#_Toc144362940"><span>Primary Physician for admission from VAIP(13,5)</span></a></td>
</tr>
</tbody>
</table>

- 

| [[SEQ](#_Toc144361758)](#_Toc144362940) | [[LEN](#_Toc144361758)](#_Toc144362940)   | [[DT](#_Toc144361758)](#_Toc144362940) | [[R/O](#_Toc144361758)](#_Toc144362940) | [[TBL#](#_Toc144361758)](#_Toc144362940) | [[Element Name](#_Toc144361758)](#_Toc144362940)      | [[VistA Description](#_Toc144361758)](#_Toc144362940)                                       |
|-----------------------------------------|-------------------------------------------|----------------------------------------|-----------------------------------------|------------------------------------------|-------------------------------------------------------|---------------------------------------------------------------------------------------------|
| [[1](#_Toc144361758)](#_Toc144362940)   | [[4](#_Toc144361758)](#_Toc144362940)     | [[SI](#_Toc144361758)](#_Toc144362940) | [[O](#_Toc144361758)](#_Toc144362940)   |                                          | [[Set ID – NTE](#_Toc144361758)](#_Toc144362940)      | [[Sequential Number 1-n](#_Toc144361758)](#_Toc144362940)                                   |
| [[2](#_Toc144361758)](#_Toc144362940)   | [[8](#_Toc144361758)](#_Toc144362940)     | [[ID](#_Toc144361758)](#_Toc144362940) | [[O](#_Toc144361758)](#_Toc144362940)   | [[0105](#_Toc144361758)](#_Toc144362940) | [[Source of Comment](#_Toc144361758)](#_Toc144362940) | [[L for Ancillary](#_Toc144361758)](#_Toc144362940)                                         |
| [[3](#_Toc144361758)](#_Toc144362940)   | [[65536](#_Toc144361758)](#_Toc144362940) | [[FT](#_Toc144361758)](#_Toc144362940) | [[O](#_Toc144361758)](#_Toc144362940)   |                                          | [[Comment](#_Toc144361758)](#_Toc144362940)           | [[Activity Comments from file 123, subfile 123.25 field 5](#_Toc144361758)](#_Toc144362940) |
| [[4](#_Toc144361758)](#_Toc144362940)   | [[250](#_Toc144361758)](#_Toc144362940)   | [[CE](#_Toc144361758)](#_Toc144362940) | [[O](#_Toc144361758)](#_Toc144362940)   |                                          | [[Comment Type](#_Toc144361758)](#_Toc144362940)      | [[Not used.](#_Toc144361758)](#_Toc144362940)                                               |

[[  
](#_Toc144361758)](#_Toc144362940)

[[  
](#_Toc144361874)](#_Toc144362940)

[[Refer to Table 14-42.](#_Toc144361874)](#_Toc144362940)

[[<span id="_Toc169170400" class="anchor"></span>Table 14‑42: REF_IN1 Segment (Valid for all above REF messages)](#_Toc144361874)](#_Toc144362940)

| [[SEQ](#_Toc144361759)](#_Toc144362940) | [[LEN](#_Toc144361759)](#_Toc144362940) | [[DT](#_Toc144361759)](#_Toc144362940)            | [[R/O](#_Toc144361759)](#_Toc144362940) | [[TBL#](#_Toc144361759)](#_Toc144362940) | [[Element Name](#_Toc144361759)](#_Toc144362940)                 | [[VistA Description](#_Toc144361759)](#_Toc144362940)                 |
|-----------------------------------------|-----------------------------------------|---------------------------------------------------|-----------------------------------------|------------------------------------------|------------------------------------------------------------------|-----------------------------------------------------------------------|
| [[1](#_Toc144361759)](#_Toc144362940)   | [[4](#_Toc144361759)](#_Toc144362940)   |                                                   | [[R](#_Toc144361759)](#_Toc144362940)   |                                          | [[SetIDIN1](#_Toc144361759)](#_Toc144362940)                     | [[Set ID - IN1 XE "1](#_Toc144361759)](#_Toc144362940)                |
| [[2](#_Toc144361759)](#_Toc144362940)   | [[250](#_Toc144361759)](#_Toc144362940) | [[Coded element](#_Toc144361759)](#_Toc144362940) | [[R](#_Toc144361759)](#_Toc144362940)   |                                          | [[InsurancePlanID](#_Toc144361759)](#_Toc144362940)              | [[Insurance Plan ID](#_Toc144361759)](#_Toc144362940)                 |
| [[3](#_Toc144361759)](#_Toc144362940)   | [[250](#_Toc144361759)](#_Toc144362940) | [[ID](#_Toc144361759)](#_Toc144362940)            | [[R](#_Toc144361759)](#_Toc144362940)   |                                          | [[InsuranceCompanyID](#_Toc144361759)](#_Toc144362940)           | [[Insurance Company ID](#_Toc144361759)](#_Toc144362940)              |
| [[4](#_Toc144361759)](#_Toc144362940)   | [[250](#_Toc144361759)](#_Toc144362940) | [[string](#_Toc144361759)](#_Toc144362940)        | [[O](#_Toc144361759)](#_Toc144362940)   |                                          | [[InsuranceCompanyName](#_Toc144361759)](#_Toc144362940)         | [[Insurance Company Name](#_Toc144361759)](#_Toc144362940)            |
| [[5](#_Toc144361759)](#_Toc144362940)   | [[250](#_Toc144361759)](#_Toc144362940) | [[address](#_Toc144361759)](#_Toc144362940)       | [[O](#_Toc144361759)](#_Toc144362940)   |                                          | [[InsuranceCompanyAddress](#_Toc144361759)](#_Toc144362940)      | [[Insurance Company Address](#_Toc144361759)](#_Toc144362940)         |
| [[6](#_Toc144361759)](#_Toc144362940)   | [[250](#_Toc144361759)](#_Toc144362940) | [[string](#_Toc144361759)](#_Toc144362940)        | [[O](#_Toc144361759)](#_Toc144362940)   |                                          | [[InsuranceCoContactPerson](#_Toc144361759)](#_Toc144362940)     | [[Insurance Co Contact Person](#_Toc144361759)](#_Toc144362940)       |
| [[7](#_Toc144361759)](#_Toc144362940)   | [[250](#_Toc144361759)](#_Toc144362940) | [[string](#_Toc144361759)](#_Toc144362940)        | [[O](#_Toc144361759)](#_Toc144362940)   |                                          | [[InsuranceCoPhoneNumber](#_Toc144361759)](#_Toc144362940)       | [[Insurance Co Phone Number](#_Toc144361759)](#_Toc144362940)         |
| [[8](#_Toc144361759)](#_Toc144362940)   | [[12](#_Toc144361759)](#_Toc144362940)  | [[string](#_Toc144361759)](#_Toc144362940)        | [[O](#_Toc144361759)](#_Toc144362940)   |                                          | [[GroupNumber](#_Toc144361759)](#_Toc144362940)                  | [[Group Number](#_Toc144361759)](#_Toc144362940)                      |
| [[9](#_Toc144361759)](#_Toc144362940)   | [[250](#_Toc144361759)](#_Toc144362940) | [[string](#_Toc144361759)](#_Toc144362940)        | [[O](#_Toc144361759)](#_Toc144362940)   |                                          | [[GroupName](#_Toc144361759)](#_Toc144362940)                    | [[Group Name](#_Toc144361759)](#_Toc144362940)                        |
| [[10](#_Toc144361759)](#_Toc144362940)  | [[250](#_Toc144361759)](#_Toc144362940) | [[string](#_Toc144361759)](#_Toc144362940)        | [[O](#_Toc144361759)](#_Toc144362940)   |                                          | [[InsuredsGroupEmpID](#_Toc144361759)](#_Toc144362940)           | [[Insured's Group Emp ID](#_Toc144361759)](#_Toc144362940)            |
| [[11](#_Toc144361759)](#_Toc144362940)  | [[250](#_Toc144361759)](#_Toc144362940) | [[string](#_Toc144361759)](#_Toc144362940)        | [[O](#_Toc144361759)](#_Toc144362940)   |                                          | [[InsuredsGroupEmpName](#_Toc144361759)](#_Toc144362940)         | [[Insured's Group Emp Name](#_Toc144361759)](#_Toc144362940)          |
| [[12](#_Toc144361759)](#_Toc144362940)  | [[8](#_Toc144361759)](#_Toc144362940)   | [[date](#_Toc144361759)](#_Toc144362940)          | [[O](#_Toc144361759)](#_Toc144362940)   |                                          | [[PlanEffectiveDate](#_Toc144361759)](#_Toc144362940)            | [[Plan Effective Date](#_Toc144361759)](#_Toc144362940)               |
| [[13](#_Toc144361759)](#_Toc144362940)  | [[8](#_Toc144361759)](#_Toc144362940)   | [[date](#_Toc144361759)](#_Toc144362940)          | [[O](#_Toc144361759)](#_Toc144362940)   |                                          | [[PlanExpirationDate](#_Toc144361759)](#_Toc144362940)           | [[Plan Expiration Date](#_Toc144361759)](#_Toc144362940)              |
| [[14](#_Toc144361759)](#_Toc144362940)  | [[239](#_Toc144361759)](#_Toc144362940) | [[string](#_Toc144361759)](#_Toc144362940)        | [[O](#_Toc144361759)](#_Toc144362940)   |                                          | [[AuthorizationInformation](#_Toc144361759)](#_Toc144362940)     | [[Authorization Information](#_Toc144361759)](#_Toc144362940)         |
| [[15](#_Toc144361759)](#_Toc144362940)  | [[3](#_Toc144361759)](#_Toc144362940)   | [[string](#_Toc144361759)](#_Toc144362940)        | [[O](#_Toc144361759)](#_Toc144362940)   |                                          | [[PlanType](#_Toc144361759)](#_Toc144362940)                     | [[Plan Type](#_Toc144361759)](#_Toc144362940)                         |
| [[16](#_Toc144361759)](#_Toc144362940)  | [[250](#_Toc144361759)](#_Toc144362940) | [[string](#_Toc144361759)](#_Toc144362940)        | [[O](#_Toc144361759)](#_Toc144362940)   |                                          | [[NameOfInsured](#_Toc144361759)](#_Toc144362940)                | [[Name Of Insured](#_Toc144361759)](#_Toc144362940)                   |
| [[17](#_Toc144361759)](#_Toc144362940)  | [[250](#_Toc144361759)](#_Toc144362940) | [[string](#_Toc144361759)](#_Toc144362940)        | [[O](#_Toc144361759)](#_Toc144362940)   |                                          | [[InsuredsRelationshipToPatien](#_Toc144361759)](#_Toc144362940) | [[Insured's Relationship To Patient](#_Toc144361759)](#_Toc144362940) |
| [[18](#_Toc144361759)](#_Toc144362940)  | [[26](#_Toc144361759)](#_Toc144362940)  | [[date](#_Toc144361759)](#_Toc144362940)          | [[O](#_Toc144361759)](#_Toc144362940)   |                                          | [[InsuredsDateOfBirth](#_Toc144361759)](#_Toc144362940)          | [[Insured's Date Of Birth](#_Toc144361759)](#_Toc144362940)           |
| [[19](#_Toc144361759)](#_Toc144362940)  | [[250](#_Toc144361759)](#_Toc144362940) | [[address](#_Toc144361759)](#_Toc144362940)       | [[O](#_Toc144361759)](#_Toc144362940)   |                                          | [[InsuredsAddress](#_Toc144361759)](#_Toc144362940)              | [[Insured's Address](#_Toc144361759)](#_Toc144362940)                 |
| [[20](#_Toc144361759)](#_Toc144362940)  | [[2](#_Toc144361759)](#_Toc144362940)   | [[string](#_Toc144361759)](#_Toc144362940)        | [[O](#_Toc144361759)](#_Toc144362940)   |                                          | [[AssignmentOfBenefits](#_Toc144361759)](#_Toc144362940)         | [[Assignment Of Benefits](#_Toc144361759)](#_Toc144362940)            |
| [[21](#_Toc144361759)](#_Toc144362940)  | [[2](#_Toc144361759)](#_Toc144362940)   | [[string](#_Toc144361759)](#_Toc144362940)        | [[O](#_Toc144361759)](#_Toc144362940)   |                                          | [[CoordinationOfBenefits](#_Toc144361759)](#_Toc144362940)       | [[Coordination Of Benefits](#_Toc144361759)](#_Toc144362940)          |
| [[22](#_Toc144361759)](#_Toc144362940)  | [[2](#_Toc144361759)](#_Toc144362940)   | [[string](#_Toc144361759)](#_Toc144362940)        | [[O](#_Toc144361759)](#_Toc144362940)   |                                          | [[CoordOfBenPriority](#_Toc144361759)](#_Toc144362940)           | [[Coord Of Ben. Priority](#_Toc144361759)](#_Toc144362940)            |
| [[23](#_Toc144361759)](#_Toc144362940)  | [[1](#_Toc144361759)](#_Toc144362940)   | [[string](#_Toc144361759)](#_Toc144362940)        | [[O](#_Toc144361759)](#_Toc144362940)   |                                          | [[NoticeOfAdmissionFlag](#_Toc144361759)](#_Toc144362940)        | [[Notice Of Admission Flag](#_Toc144361759)](#_Toc144362940)          |
| [[24](#_Toc144361759)](#_Toc144362940)  | [[8](#_Toc144361759)](#_Toc144362940)   | [[date](#_Toc144361759)](#_Toc144362940)          | [[O](#_Toc144361759)](#_Toc144362940)   |                                          | [[NoticeOfAdmissionDate](#_Toc144361759)](#_Toc144362940)        | [[Notice Of Admission Date](#_Toc144361759)](#_Toc144362940)          |
| [[25](#_Toc144361759)](#_Toc144362940)  | [[1](#_Toc144361759)](#_Toc144362940)   | [[string](#_Toc144361759)](#_Toc144362940)        | [[O](#_Toc144361759)](#_Toc144362940)   |                                          | [[ReportOfEligibilityFlag](#_Toc144361759)](#_Toc144362940)      | [[Report Of Eligibility Flag](#_Toc144361759)](#_Toc144362940)        |
| [[26](#_Toc144361759)](#_Toc144362940)  | [[8](#_Toc144361759)](#_Toc144362940)   | [[date](#_Toc144361759)](#_Toc144362940)          | [[O](#_Toc144361759)](#_Toc144362940)   |                                          | [[ReportOfEligibilityDate](#_Toc144361759)](#_Toc144362940)      | [[Report Of Eligibility Date](#_Toc144361759)](#_Toc144362940)        |
| [[27](#_Toc144361759)](#_Toc144362940)  | [[2](#_Toc144361759)](#_Toc144362940)   | [[string](#_Toc144361759)](#_Toc144362940)        | [[O](#_Toc144361759)](#_Toc144362940)   |                                          | [[ReleaseInformationCode](#_Toc144361759)](#_Toc144362940)       | [[Release Information Code](#_Toc144361759)](#_Toc144362940)          |
| [[28](#_Toc144361759)](#_Toc144362940)  | [[15](#_Toc144361759)](#_Toc144362940)  | [[string](#_Toc144361759)](#_Toc144362940)        | [[O](#_Toc144361759)](#_Toc144362940)   |                                          | [[PreAdmitCertPAC](#_Toc144361759)](#_Toc144362940)              | [[Pre-Admit Cert (PAC)](#_Toc144361759)](#_Toc144362940)              |
| [[29](#_Toc144361759)](#_Toc144362940)  | [[26](#_Toc144361759)](#_Toc144362940)  | [[date](#_Toc144361759)](#_Toc144362940)          | [[O](#_Toc144361759)](#_Toc144362940)   |                                          | [[VerificationDateTime](#_Toc144361759)](#_Toc144362940)         | [[Verification Date/Time](#_Toc144361759)](#_Toc144362940)            |
| [[30](#_Toc144361759)](#_Toc144362940)  | [[250](#_Toc144361759)](#_Toc144362940) | [[string](#_Toc144361759)](#_Toc144362940)        | [[O](#_Toc144361759)](#_Toc144362940)   |                                          | [[VerificationBy](#_Toc144361759)](#_Toc144362940)               | [[Verification By](#_Toc144361759)](#_Toc144362940)                   |
| [[31](#_Toc144361759)](#_Toc144362940)  | [[2](#_Toc144361759)](#_Toc144362940)   | [[string](#_Toc144361759)](#_Toc144362940)        | [[O](#_Toc144361759)](#_Toc144362940)   |                                          | [[TypeOfAgreementCode](#_Toc144361759)](#_Toc144362940)          | [[Type Of Agreement Code](#_Toc144361759)](#_Toc144362940)            |
| [[32](#_Toc144361759)](#_Toc144362940)  | [[2](#_Toc144361759)](#_Toc144362940)   | [[string](#_Toc144361759)](#_Toc144362940)        | [[O](#_Toc144361759)](#_Toc144362940)   |                                          | [[BillingStatus](#_Toc144361759)](#_Toc144362940)                | [[Billing Status](#_Toc144361759)](#_Toc144362940)                    |
| [[33](#_Toc144361759)](#_Toc144362940)  | [[4](#_Toc144361759)](#_Toc144362940)   | [[number](#_Toc144361759)](#_Toc144362940)        | [[O](#_Toc144361759)](#_Toc144362940)   |                                          | [[LifetimeReserveDays](#_Toc144361759)](#_Toc144362940)          | [[Lifetime Reserve Days](#_Toc144361759)](#_Toc144362940)             |
| [[34](#_Toc144361759)](#_Toc144362940)  | [[4](#_Toc144361759)](#_Toc144362940)   | [[number](#_Toc144361759)](#_Toc144362940)        | [[O](#_Toc144361759)](#_Toc144362940)   |                                          | [[DelayBeforeLRDay](#_Toc144361759)](#_Toc144362940)             | [[Delay Before L.R. Day](#_Toc144361759)](#_Toc144362940)             |
| [[35](#_Toc144361759)](#_Toc144362940)  | [[8](#_Toc144361759)](#_Toc144362940)   | [[string](#_Toc144361759)](#_Toc144362940)        | [[O](#_Toc144361759)](#_Toc144362940)   |                                          | [[CompanyPlanCode](#_Toc144361759)](#_Toc144362940)              | [[Company Plan Code](#_Toc144361759)](#_Toc144362940)                 |
| [[36](#_Toc144361759)](#_Toc144362940)  | [[15](#_Toc144361759)](#_Toc144362940)  | [[string](#_Toc144361759)](#_Toc144362940)        | [[O](#_Toc144361759)](#_Toc144362940)   |                                          | [[PolicyNumber](#_Toc144361759)](#_Toc144362940)                 | [[Policy Number](#_Toc144361759)](#_Toc144362940)                     |
| [[37](#_Toc144361759)](#_Toc144362940)  | [[12](#_Toc144361759)](#_Toc144362940)  | [[number](#_Toc144361759)](#_Toc144362940)        | [[O](#_Toc144361759)](#_Toc144362940)   |                                          | [[PolicyDeductible](#_Toc144361759)](#_Toc144362940)             | [[Policy Deductible](#_Toc144361759)](#_Toc144362940)                 |
| [[38](#_Toc144361759)](#_Toc144362940)  | [[12](#_Toc144361759)](#_Toc144362940)  | [[number](#_Toc144361759)](#_Toc144362940)        | [[B](#_Toc144361759)](#_Toc144362940)   |                                          | [[PolicyLimitAmount](#_Toc144361759)](#_Toc144362940)            | [[Policy Limit - Amount](#_Toc144361759)](#_Toc144362940)             |
| [[39](#_Toc144361759)](#_Toc144362940)  | [[4](#_Toc144361759)](#_Toc144362940)   | [[number](#_Toc144361759)](#_Toc144362940)        | [[O](#_Toc144361759)](#_Toc144362940)   |                                          | [[PolicyLimitDays](#_Toc144361759)](#_Toc144362940)              | [[Policy Limit - Days](#_Toc144361759)](#_Toc144362940)               |
| [[40](#_Toc144361759)](#_Toc144362940)  | [[12](#_Toc144361759)](#_Toc144362940)  | [[number](#_Toc144361759)](#_Toc144362940)        | [[B](#_Toc144361759)](#_Toc144362940)   |                                          | [[RoomRateSemiPrivate](#_Toc144361759)](#_Toc144362940)          | [[Room Rate - Semi-Private](#_Toc144361759)](#_Toc144362940)          |
| [[41](#_Toc144361759)](#_Toc144362940)  | [[12](#_Toc144361759)](#_Toc144362940)  | [[number](#_Toc144361759)](#_Toc144362940)        | [[B](#_Toc144361759)](#_Toc144362940)   |                                          | [[RoomRatePrivate](#_Toc144361759)](#_Toc144362940)              | [[Room Rate - Private](#_Toc144361759)](#_Toc144362940)               |
| [[42](#_Toc144361759)](#_Toc144362940)  | [[250](#_Toc144361759)](#_Toc144362940) | [[string](#_Toc144361759)](#_Toc144362940)        | [[O](#_Toc144361759)](#_Toc144362940)   |                                          | [[InsuredsEmploymentStatus](#_Toc144361759)](#_Toc144362940)     | [[Insured's Employment Status](#_Toc144361759)](#_Toc144362940)       |
| [[43](#_Toc144361759)](#_Toc144362940)  | [[1](#_Toc144361759)](#_Toc144362940)   | [[string](#_Toc144361759)](#_Toc144362940)        | [[O](#_Toc144361759)](#_Toc144362940)   |                                          | [[InsuredsAdministrativeSex](#_Toc144361759)](#_Toc144362940)    | [[Insured's Administrative Sex](#_Toc144361759)](#_Toc144362940)      |
| [[44](#_Toc144361759)](#_Toc144362940)  | [[250](#_Toc144361759)](#_Toc144362940) | [[address](#_Toc144361759)](#_Toc144362940)       | [[O](#_Toc144361759)](#_Toc144362940)   |                                          | [[InsuredsEmployersAddress](#_Toc144361759)](#_Toc144362940)     | [[Insured's Employer's Address](#_Toc144361759)](#_Toc144362940)      |
| [[45](#_Toc144361759)](#_Toc144362940)  | [[2](#_Toc144361759)](#_Toc144362940)   | [[string](#_Toc144361759)](#_Toc144362940)        | [[O](#_Toc144361759)](#_Toc144362940)   |                                          | [[VerificationStatus](#_Toc144361759)](#_Toc144362940)           | [[Verification Status](#_Toc144361759)](#_Toc144362940)               |
| [[46](#_Toc144361759)](#_Toc144362940)  | [[8](#_Toc144361759)](#_Toc144362940)   | [[string](#_Toc144361759)](#_Toc144362940)        | [[O](#_Toc144361759)](#_Toc144362940)   |                                          | [[PriorInsurancePlanID](#_Toc144361759)](#_Toc144362940)         | [[Prior Insurance Plan ID](#_Toc144361759)](#_Toc144362940)           |
| [[47](#_Toc144361759)](#_Toc144362940)  | [[3](#_Toc144361759)](#_Toc144362940)   | [[string](#_Toc144361759)](#_Toc144362940)        | [[O](#_Toc144361759)](#_Toc144362940)   |                                          | [[CoverageType](#_Toc144361759)](#_Toc144362940)                 | [[Coverage Type](#_Toc144361759)](#_Toc144362940)                     |
| [[48](#_Toc144361759)](#_Toc144362940)  | [[2](#_Toc144361759)](#_Toc144362940)   | [[string](#_Toc144361759)](#_Toc144362940)        | [[O](#_Toc144361759)](#_Toc144362940)   |                                          | [[Handicap](#_Toc144361759)](#_Toc144362940)                     | [[Handicap](#_Toc144361759)](#_Toc144362940)                          |
| [[49](#_Toc144361759)](#_Toc144362940)  | [[250](#_Toc144361759)](#_Toc144362940) | [[ID](#_Toc144361759)](#_Toc144362940)            | [[O](#_Toc144361759)](#_Toc144362940)   |                                          | [[InsuredsIDNumber](#_Toc144361759)](#_Toc144362940)             | [[Insured's ID Number](#_Toc144361759)](#_Toc144362940)               |
| [[50](#_Toc144361759)](#_Toc144362940)  | [[1](#_Toc144361759)](#_Toc144362940)   | [[string](#_Toc144361759)](#_Toc144362940)        | [[O](#_Toc144361759)](#_Toc144362940)   |                                          | [[SignatureCode](#_Toc144361759)](#_Toc144362940)                | [[Signature Code](#_Toc144361759)](#_Toc144362940)                    |
| [[51](#_Toc144361759)](#_Toc144362940)  | [[8](#_Toc144361759)](#_Toc144362940)   | [[date](#_Toc144361759)](#_Toc144362940)          | [[O](#_Toc144361759)](#_Toc144362940)   |                                          | [[SignatureCodeDate](#_Toc144361759)](#_Toc144362940)            | [[Signature Code Date](#_Toc144361759)](#_Toc144362940)               |
| [[52](#_Toc144361759)](#_Toc144362940)  | [[250](#_Toc144361759)](#_Toc144362940) | [[string](#_Toc144361759)](#_Toc144362940)        | [[O](#_Toc144361759)](#_Toc144362940)   |                                          | [[InsuredsBirthPlace](#_Toc144361759)](#_Toc144362940)           | [[Insured's Birth Place](#_Toc144361759)](#_Toc144362940)             |
| [[53](#_Toc144361759)](#_Toc144362940)  | [[2](#_Toc144361759)](#_Toc144362940)   | [[string](#_Toc144361759)](#_Toc144362940)        | [[O](#_Toc144361759)](#_Toc144362940)   |                                          | [[VIPIndicator](#_Toc144361759)](#_Toc144362940)                 | [[VIP Indicator](#_Toc144361759)](#_Toc144362940)                     |

[[Refer to Table 14-43.](#_Toc144361759)](#_Toc144362940)

[[<span id="_Toc169170401" class="anchor"></span>Table 14‑43: REF_IN3 Segment (Valid for all above REF messages)](#_Toc144361759)](#_Toc144362940)

| [[SEQ](#_Toc144361760)](#_Toc144362940) | [[LEN](#_Toc144361760)](#_Toc144362940) | [[DT](#_Toc144361760)](#_Toc144362940)     | [[R/O](#_Toc144361760)](#_Toc144362940) | [[TBL#](#_Toc144361760)](#_Toc144362940) | [[Element Name](#_Toc144361760)](#_Toc144362940)                 | [[VistA Description](#_Toc144361760)](#_Toc144362940)                     |
|-----------------------------------------|-----------------------------------------|--------------------------------------------|-----------------------------------------|------------------------------------------|------------------------------------------------------------------|---------------------------------------------------------------------------|
| [[1](#_Toc144361760)](#_Toc144362940)   | [[4](#_Toc144361760)](#_Toc144362940)   |                                            | [[R](#_Toc144361760)](#_Toc144362940)   |                                          | [[SetIDIN3](#_Toc144361760)](#_Toc144362940)                     | [[Set ID - IN3 XE "1](#_Toc144361760)](#_Toc144362940)                    |
| [[2](#_Toc144361760)](#_Toc144362940)   | [[250](#_Toc144361760)](#_Toc144362940) | [[string](#_Toc144361760)](#_Toc144362940) | [[O](#_Toc144361760)](#_Toc144362940)   |                                          | [[CertificationNumber](#_Toc144361760)](#_Toc144362940)          | [[Certification Number](#_Toc144361760)](#_Toc144362940)                  |
| [[3](#_Toc144361760)](#_Toc144362940)   | [[250](#_Toc144361760)](#_Toc144362940) | [[string](#_Toc144361760)](#_Toc144362940) | [[O](#_Toc144361760)](#_Toc144362940)   |                                          | [[CertifiedBy](#_Toc144361760)](#_Toc144362940)                  | [[Certified By](#_Toc144361760)](#_Toc144362940)                          |
| [[4](#_Toc144361760)](#_Toc144362940)   | [[1](#_Toc144361760)](#_Toc144362940)   | [[string](#_Toc144361760)](#_Toc144362940) | [[O](#_Toc144361760)](#_Toc144362940)   |                                          | [[CertificationRequired](#_Toc144361760)](#_Toc144362940)        | [[Certification Required](#_Toc144361760)](#_Toc144362940)                |
| [[5](#_Toc144361760)](#_Toc144362940)   | [[23](#_Toc144361760)](#_Toc144362940)  | [[string](#_Toc144361760)](#_Toc144362940) | [[O](#_Toc144361760)](#_Toc144362940)   |                                          | [[Penalty](#_Toc144361760)](#_Toc144362940)                      | [[Penalty](#_Toc144361760)](#_Toc144362940)                               |
| [[6](#_Toc144361760)](#_Toc144362940)   | [[26](#_Toc144361760)](#_Toc144362940)  | [[date](#_Toc144361760)](#_Toc144362940)   | [[O](#_Toc144361760)](#_Toc144362940)   |                                          | [[CertificationDateTime](#_Toc144361760)](#_Toc144362940)        | [[Certification Date/Time](#_Toc144361760)](#_Toc144362940)               |
| [[7](#_Toc144361760)](#_Toc144362940)   | [[26](#_Toc144361760)](#_Toc144362940)  | [[date](#_Toc144361760)](#_Toc144362940)   | [[O](#_Toc144361760)](#_Toc144362940)   |                                          | [[CertificationModifyDateTime](#_Toc144361760)](#_Toc144362940)  | [[Certification Modify Date/Time](#_Toc144361760)](#_Toc144362940)        |
| [[8](#_Toc144361760)](#_Toc144362940)   | [[250](#_Toc144361760)](#_Toc144362940) | [[string](#_Toc144361760)](#_Toc144362940) | [[O](#_Toc144361760)](#_Toc144362940)   |                                          | [[Operator](#_Toc144361760)](#_Toc144362940)                     | [[Operator](#_Toc144361760)](#_Toc144362940)                              |
| [[9](#_Toc144361760)](#_Toc144362940)   | [[8](#_Toc144361760)](#_Toc144362940)   | [[date](#_Toc144361760)](#_Toc144362940)   | [[O](#_Toc144361760)](#_Toc144362940)   |                                          | [[CertificationBeginDate](#_Toc144361760)](#_Toc144362940)       | [[Certification Begin Date](#_Toc144361760)](#_Toc144362940)              |
| [[10](#_Toc144361760)](#_Toc144362940)  | [[8](#_Toc144361760)](#_Toc144362940)   | [[date](#_Toc144361760)](#_Toc144362940)   | [[O](#_Toc144361760)](#_Toc144362940)   |                                          | [[CertificationEndDate](#_Toc144361760)](#_Toc144362940)         | [[Certification End Date](#_Toc144361760)](#_Toc144362940)                |
| [[11](#_Toc144361760)](#_Toc144362940)  | [[6](#_Toc144361760)](#_Toc144362940)   | [[number](#_Toc144361760)](#_Toc144362940) | [[O](#_Toc144361760)](#_Toc144362940)   |                                          | [[Days](#_Toc144361760)](#_Toc144362940)                         | [[Days](#_Toc144361760)](#_Toc144362940)                                  |
| [[12](#_Toc144361760)](#_Toc144362940)  | [[250](#_Toc144361760)](#_Toc144362940) | [[string](#_Toc144361760)](#_Toc144362940) | [[O](#_Toc144361760)](#_Toc144362940)   |                                          | [[NonConcurCodeDescription](#_Toc144361760)](#_Toc144362940)     | [[Non-Concur Code/Description](#_Toc144361760)](#_Toc144362940)           |
| [[13](#_Toc144361760)](#_Toc144362940)  | [[26](#_Toc144361760)](#_Toc144362940)  | [[date](#_Toc144361760)](#_Toc144362940)   | [[O](#_Toc144361760)](#_Toc144362940)   |                                          | [[NonConcurEffectiveDateTime](#_Toc144361760)](#_Toc144362940)   | [[Non-Concur Effective Date/Time](#_Toc144361760)](#_Toc144362940)        |
| [[14](#_Toc144361760)](#_Toc144362940)  | [[250](#_Toc144361760)](#_Toc144362940) | [[string](#_Toc144361760)](#_Toc144362940) | [[O](#_Toc144361760)](#_Toc144362940)   |                                          | [[PhysicianReviewer](#_Toc144361760)](#_Toc144362940)            | [[Physician Reviewer](#_Toc144361760)](#_Toc144362940)                    |
| [[15](#_Toc144361760)](#_Toc144362940)  | [[48](#_Toc144361760)](#_Toc144362940)  | [[string](#_Toc144361760)](#_Toc144362940) | [[O](#_Toc144361760)](#_Toc144362940)   |                                          | [[CertificationContact](#_Toc144361760)](#_Toc144362940)         | [[Certification Contact](#_Toc144361760)](#_Toc144362940)                 |
| [[16](#_Toc144361760)](#_Toc144362940)  | [[250](#_Toc144361760)](#_Toc144362940) | [[string](#_Toc144361760)](#_Toc144362940) | [[O](#_Toc144361760)](#_Toc144362940)   |                                          | [[CertificationContactPhoneNum](#_Toc144361760)](#_Toc144362940) | [[Certification Contact Phone Number](#_Toc144361760)](#_Toc144362940)    |
| [[17](#_Toc144361760)](#_Toc144362940)  | [[250](#_Toc144361760)](#_Toc144362940) | [[string](#_Toc144361760)](#_Toc144362940) | [[O](#_Toc144361760)](#_Toc144362940)   |                                          | [[AppealReason](#_Toc144361760)](#_Toc144362940)                 | [[Appeal Reason](#_Toc144361760)](#_Toc144362940)                         |
| [[18](#_Toc144361760)](#_Toc144362940)  | [[250](#_Toc144361760)](#_Toc144362940) | [[string](#_Toc144361760)](#_Toc144362940) | [[O](#_Toc144361760)](#_Toc144362940)   |                                          | [[CertificationAgency](#_Toc144361760)](#_Toc144362940)          | [[Certification Agency](#_Toc144361760)](#_Toc144362940)                  |
| [[19](#_Toc144361760)](#_Toc144362940)  | [[250](#_Toc144361760)](#_Toc144362940) | [[string](#_Toc144361760)](#_Toc144362940) | [[O](#_Toc144361760)](#_Toc144362940)   |                                          | [[CertificationAgencyPhoneNumb](#_Toc144361760)](#_Toc144362940) | [[Certification Agency Phone Number](#_Toc144361760)](#_Toc144362940)     |
| [[20](#_Toc144361760)](#_Toc144362940)  | [[40](#_Toc144361760)](#_Toc144362940)  | [[string](#_Toc144361760)](#_Toc144362940) | [[O](#_Toc144361760)](#_Toc144362940)   |                                          | [[PreCertificationRequirement](#_Toc144361760)](#_Toc144362940)  | [[Pre-Certification Requirement](#_Toc144361760)](#_Toc144362940)         |
| [[21](#_Toc144361760)](#_Toc144362940)  | [[48](#_Toc144361760)](#_Toc144362940)  | [[string](#_Toc144361760)](#_Toc144362940) | [[O](#_Toc144361760)](#_Toc144362940)   |                                          | [[CaseManager](#_Toc144361760)](#_Toc144362940)                  | [[Case Manager](#_Toc144361760)](#_Toc144362940)                          |
| [[22](#_Toc144361760)](#_Toc144362940)  | [[8](#_Toc144361760)](#_Toc144362940)   | [[date](#_Toc144361760)](#_Toc144362940)   | [[O](#_Toc144361760)](#_Toc144362940)   |                                          | [[SecondOpinionDate](#_Toc144361760)](#_Toc144362940)            | [[Second Opinion Date](#_Toc144361760)](#_Toc144362940)                   |
| [[23](#_Toc144361760)](#_Toc144362940)  | [[1](#_Toc144361760)](#_Toc144362940)   | [[string](#_Toc144361760)](#_Toc144362940) | [[O](#_Toc144361760)](#_Toc144362940)   |                                          | [[SecondOpinionStatus](#_Toc144361760)](#_Toc144362940)          | [[Second Opinion Status](#_Toc144361760)](#_Toc144362940)                 |
| [[24](#_Toc144361760)](#_Toc144362940)  | [[1](#_Toc144361760)](#_Toc144362940)   | [[string](#_Toc144361760)](#_Toc144362940) | [[O](#_Toc144361760)](#_Toc144362940)   |                                          | [[SecondOpinionDocumentationRe](#_Toc144361760)](#_Toc144362940) | [[Second Opinion Documentation Received](#_Toc144361760)](#_Toc144362940) |
| [[25](#_Toc144361760)](#_Toc144362940)  | [[250](#_Toc144361760)](#_Toc144362940) | [[string](#_Toc144361760)](#_Toc144362940) | [[O](#_Toc144361760)](#_Toc144362940)   |                                          | [[SecondOpinionPhysician](#_Toc144361760)](#_Toc144362940)       | [[Second Opinion Physician](#_Toc144361760)](#_Toc144362940)              |

[[Patch GMRC\*3.0\*75 added the ability to use the following HL7 ACK messages to enable communications between the consult system communication with the Healthcare Claims Processing System (HCPS). Accept Acknowledgment (AA) will be sent for messages that are parsed correctly and sent to HCPS. Application Error (AE) will be sent when a parsing issue is discovered, such as missing a required field.](#_Toc144361760)](#_Toc144362940)

[[HL7 v2.5 ACK messages will be sent to HCPS in enhanced mode, as follows:](#_Toc144361760)](#_Toc144362940)

- 
- 
- 

| [[Segment](#_Toc144361761)](#_Toc144362940) | [[Segment Name](#_Toc144361761)](#_Toc144362940)           | [[Optional/Required](#_Toc144361761)](#_Toc144362940) |
|---------------------------------------------|------------------------------------------------------------|-------------------------------------------------------|
| [[MSH](#_Toc144361761)](#_Toc144362940)     | [[Message Header](#_Toc144361761)](#_Toc144362940)         | [[REQUIRED](#_Toc144361761)](#_Toc144362940)          |
| [[MSA](#_Toc144361761)](#_Toc144362940)     | [[Message Acknowledgment](#_Toc144361761)](#_Toc144362940) | [[REQUIRED](#_Toc144361761)](#_Toc144362940)          |
| [[ERR](#_Toc144361761)](#_Toc144362940)     | [[Error](#_Toc144361761)](#_Toc144362940)                  | [[OPTIONAL](#_Toc144361761)](#_Toc144362940)          |

[[The following tables contain the HL7 message definition for the ACK messages.](#_Toc144361761)](#_Toc144362940)

[[The table columns are as follows:](#_Toc144361761)](#_Toc144362940)

1.  
2.  
3.  
4.  
5.  
6.  
7.  

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 12%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 23%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><a href="#_Toc144362940"><span>SEQ</span></a></th>
<th><a href="#_Toc144362940"><span>LEN</span></a></th>
<th><a href="#_Toc144362940"><span>DT</span></a></th>
<th><a href="#_Toc144362940"><span>R/O</span></a></th>
<th><a href="#_Toc144362940"><span>TBL#</span></a></th>
<th><a href="#_Toc144362940"><span>Element Name</span></a></th>
<th><a href="#_Toc144362940"><span>Description</span></a></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="#_Toc144362940"><span>1</span></a></td>
<td><a href="#_Toc144362940"><span>1</span></a></td>
<td><a href="#_Toc144362940"><span>ST</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Field Separator</span></a></td>
<td><a href="#_Toc144362940"><span>|</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>2</span></a></td>
<td><a href="#_Toc144362940"><span>4</span></a></td>
<td><a href="#_Toc144362940"><span>ST</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Encoding Characters</span></a></td>
<td><a href="#_Toc144362940"><span>~^\&amp;</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>3</span></a></td>
<td><a href="#_Toc144362940"><span>15</span></a></td>
<td><a href="#_Toc144362940"><span>ST</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Sending Application</span></a></td>
<td><a href="#_Toc144362940"><span>GMRC HCP RECEIVE</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>4</span></a></td>
<td><a href="#_Toc144362940"><span>20</span></a></td>
<td><a href="#_Toc144362940"><span>ST</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Sending Facility</span></a></td>
<td><a href="#_Toc144362940"><span>Sending Facility</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>5</span></a></td>
<td><a href="#_Toc144362940"><span>30</span></a></td>
<td><a href="#_Toc144362940"><span>ST</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Receiving Application</span></a></td>
<td><a href="#_Toc144362940"><span>GMRC HCP SEND</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>6</span></a></td>
<td><a href="#_Toc144362940"><span>30</span></a></td>
<td><a href="#_Toc144362940"><span>ST</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Receiving Facility</span></a></td>
<td><a href="#_Toc144362940"><span>Receiving Facility</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>7</span></a></td>
<td><a href="#_Toc144362940"><span>26</span></a></td>
<td><a href="#_Toc144362940"><span>TS</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Date/Time Of Message</span></a></td>
<td><a href="#_Toc144362940"><span>System date/time</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>8</span></a></td>
<td><a href="#_Toc144362940"><span>40</span></a></td>
<td><a href="#_Toc144362940"><span>ST</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Security</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>9</span></a></td>
<td><a href="#_Toc144362940"><span>7</span></a></td>
<td><a href="#_Toc144362940"><span>CM</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td><a href="#_Toc144362940"><span>0076<br />
0003</span></a></td>
<td><a href="#_Toc144362940"><span>Message Type</span></a></td>
<td><a href="#_Toc144362940"><span>ACK</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>10</span></a></td>
<td><a href="#_Toc144362940"><span>20</span></a></td>
<td><a href="#_Toc144362940"><span>ST</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Message Control ID</span></a></td>
<td><a href="#_Toc144362940"><span>Return the Message Control ID from the REF^I1n message received from VistA</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>11</span></a></td>
<td><a href="#_Toc144362940"><span>1</span></a></td>
<td><a href="#_Toc144362940"><span>ID</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Processing ID</span></a></td>
<td><a href="#_Toc144362940"><span>P for Production, T for Test</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>12</span></a></td>
<td><a href="#_Toc144362940"><span>8</span></a></td>
<td><a href="#_Toc144362940"><span>ID</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td><a href="#_Toc144362940"><span>0104</span></a></td>
<td><a href="#_Toc144362940"><span>Version ID</span></a></td>
<td><a href="#_Toc144362940"><span>2.</span><span>5</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>13</span></a></td>
<td><a href="#_Toc144362940"><span>15</span></a></td>
<td><a href="#_Toc144362940"><span>NM</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Sequence Number</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>14</span></a></td>
<td><a href="#_Toc144362940"><span>180</span></a></td>
<td><a href="#_Toc144362940"><span>ST</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Continuation Pointer</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>15</span></a></td>
<td><a href="#_Toc144362940"><span>2</span></a></td>
<td><a href="#_Toc144362940"><span>ID</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td><a href="#_Toc144362940"><span>0155</span></a></td>
<td><a href="#_Toc144362940"><span>Accept Acknowledgment Type</span></a></td>
<td><a href="#_Toc144362940"><span>AL</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>16</span></a></td>
<td><a href="#_Toc144362940"><span>2</span></a></td>
<td><a href="#_Toc144362940"><span>ID</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td><a href="#_Toc144362940"><span>0155</span></a></td>
<td><a href="#_Toc144362940"><span>Application Acknowledgment Type</span></a></td>
<td><a href="#_Toc144362940"><span>NE</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>17</span></a></td>
<td><a href="#_Toc144362940"><span>3</span></a></td>
<td><a href="#_Toc144362940"><span>ID</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td><a href="#_Toc144362940"><span>0399</span></a></td>
<td><a href="#_Toc144362940"><span>Country Code</span></a></td>
<td><a href="#_Toc144362940"><span>USA</span></a></td>
</tr>
</tbody>
</table>

[[Refer to Table 14-46.](#_Toc144362934)](#_Toc144362940)

[[<span id="_Toc169170404" class="anchor"></span>Table 14‑46: ACK MSH - Message Header Segment](#_Toc144362934)](#_Toc144362940)

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 10%" />
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 27%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr class="header">
<th><a href="#_Toc144362940"><span>SEQ</span></a></th>
<th><a href="#_Toc144362940"><span>LEN</span></a></th>
<th><a href="#_Toc144362940"><span>DT</span></a></th>
<th><a href="#_Toc144362940"><span>R/O</span></a></th>
<th><a href="#_Toc144362940"><span>TBL#</span></a></th>
<th><a href="#_Toc144362940"><span>Element Name</span></a></th>
<th><a href="#_Toc144362940"><span>Description</span></a></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="#_Toc144362940"><span>1</span></a></td>
<td><a href="#_Toc144362940"><span>1</span></a></td>
<td><a href="#_Toc144362940"><span>ST</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Field Separator</span></a></td>
<td><a href="#_Toc144362940"><span>|</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>2</span></a></td>
<td><a href="#_Toc144362940"><span>4</span></a></td>
<td><a href="#_Toc144362940"><span>ST</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Encoding Characters</span></a></td>
<td><a href="#_Toc144362940"><span>~^\&amp;</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>3</span></a></td>
<td><a href="#_Toc144362940"><span>15</span></a></td>
<td><a href="#_Toc144362940"><span>ST</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Sending Application</span></a></td>
<td><a href="#_Toc144362940"><span>GMRC HCP RECEIVE</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>4</span></a></td>
<td><a href="#_Toc144362940"><span>20</span></a></td>
<td><a href="#_Toc144362940"><span>ST</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Sending Facility</span></a></td>
<td><a href="#_Toc144362940"><span>Sending Facility</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>5</span></a></td>
<td><a href="#_Toc144362940"><span>30</span></a></td>
<td><a href="#_Toc144362940"><span>ST</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Receiving Application</span></a></td>
<td><a href="#_Toc144362940"><span>GMRC HCP SEND</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>6</span></a></td>
<td><a href="#_Toc144362940"><span>30</span></a></td>
<td><a href="#_Toc144362940"><span>ST</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Receiving Facility</span></a></td>
<td><a href="#_Toc144362940"><span>Receiving Facility</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>7</span></a></td>
<td><a href="#_Toc144362940"><span>26</span></a></td>
<td><a href="#_Toc144362940"><span>TS</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Date/Time Of Message</span></a></td>
<td><a href="#_Toc144362940"><span>System date/time</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>8</span></a></td>
<td><a href="#_Toc144362940"><span>40</span></a></td>
<td><a href="#_Toc144362940"><span>ST</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Security</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>9</span></a></td>
<td><a href="#_Toc144362940"><span>7</span></a></td>
<td><a href="#_Toc144362940"><span>CM</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td><a href="#_Toc144362940"><span>0076<br />
0003</span></a></td>
<td><a href="#_Toc144362940"><span>Message Type</span></a></td>
<td><a href="#_Toc144362940"><span>ACK</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>10</span></a></td>
<td><a href="#_Toc144362940"><span>20</span></a></td>
<td><a href="#_Toc144362940"><span>ST</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Message Control ID</span></a></td>
<td><a href="#_Toc144362940"><span>Return the Message Control ID from the REF^I1n message received from VistA</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>11</span></a></td>
<td><a href="#_Toc144362940"><span>1</span></a></td>
<td><a href="#_Toc144362940"><span>ID</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Processing ID</span></a></td>
<td><a href="#_Toc144362940"><span>P for Production, T for Test</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>12</span></a></td>
<td><a href="#_Toc144362940"><span>8</span></a></td>
<td><a href="#_Toc144362940"><span>ID</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td><a href="#_Toc144362940"><span>0104</span></a></td>
<td><a href="#_Toc144362940"><span>Version ID</span></a></td>
<td><a href="#_Toc144362940"><span>2.</span><span>5</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>13</span></a></td>
<td><a href="#_Toc144362940"><span>15</span></a></td>
<td><a href="#_Toc144362940"><span>NM</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Sequence Number</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>14</span></a></td>
<td><a href="#_Toc144362940"><span>180</span></a></td>
<td><a href="#_Toc144362940"><span>ST</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Continuation Pointer</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>15</span></a></td>
<td><a href="#_Toc144362940"><span>2</span></a></td>
<td><a href="#_Toc144362940"><span>ID</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td><a href="#_Toc144362940"><span>0155</span></a></td>
<td><a href="#_Toc144362940"><span>Accept Acknowledgment Type</span></a></td>
<td><a href="#_Toc144362940"><span>AL</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>16</span></a></td>
<td><a href="#_Toc144362940"><span>2</span></a></td>
<td><a href="#_Toc144362940"><span>ID</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td><a href="#_Toc144362940"><span>0155</span></a></td>
<td><a href="#_Toc144362940"><span>Application Acknowledgment Type</span></a></td>
<td><a href="#_Toc144362940"><span>NE</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>17</span></a></td>
<td><a href="#_Toc144362940"><span>3</span></a></td>
<td><a href="#_Toc144362940"><span>ID</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td><a href="#_Toc144362940"><span>0399</span></a></td>
<td><a href="#_Toc144362940"><span>Country Code</span></a></td>
<td><a href="#_Toc144362940"><span>USA</span></a></td>
</tr>
</tbody>
</table>

[[  
](#_Toc144362934)](#_Toc144362940)

[[Refer to Table 14-47.](#_Toc144362934)](#_Toc144362940)

[[<span id="_Toc169170405" class="anchor"></span>Table 14‑47: ACK MSA - Message Acknowledgment Segment](#_Toc144362934)](#_Toc144362940)

| [[SEQ](#_Toc144361764)](#_Toc144362940) | [[LEN](#_Toc144361764)](#_Toc144362940) | [[DT](#_Toc144361764)](#_Toc144362940) | [[R/O](#_Toc144361764)](#_Toc144362940) | [[TBL#](#_Toc144361764)](#_Toc144362940) | [[Element Name](#_Toc144361764)](#_Toc144362940)                | [[Description](#_Toc144361764)](#_Toc144362940)                                        |
|-----------------------------------------|-----------------------------------------|----------------------------------------|-----------------------------------------|------------------------------------------|-----------------------------------------------------------------|----------------------------------------------------------------------------------------|
| [[1](#_Toc144361764)](#_Toc144362940)   | [[2](#_Toc144361764)](#_Toc144362940)   | [[ID](#_Toc144361764)](#_Toc144362940) | [[R](#_Toc144361764)](#_Toc144362940)   | [[0008](#_Toc144361764)](#_Toc144362940) | [[Acknowledgment Code](#_Toc144361764)](#_Toc144362940)         | [[AA for Application Accept AE for Application Error](#_Toc144361764)](#_Toc144362940) |
| [[2](#_Toc144361764)](#_Toc144362940)   | [[20](#_Toc144361764)](#_Toc144362940)  | [[ST](#_Toc144361764)](#_Toc144362940) | [[R](#_Toc144361764)](#_Toc144362940)   |                                          | [[Message Control ID](#_Toc144361764)](#_Toc144362940)          | [[Same as MSH.10 above](#_Toc144361764)](#_Toc144362940)                               |
| [[3](#_Toc144361764)](#_Toc144362940)   | [[80](#_Toc144361764)](#_Toc144362940)  | [[ST](#_Toc144361764)](#_Toc144362940) | [[NS](#_Toc144361764)](#_Toc144362940)  |                                          | [[Text Message](#_Toc144361764)](#_Toc144362940)                | [[Not supported](#_Toc144361764)](#_Toc144362940)                                      |
| [[4](#_Toc144361764)](#_Toc144362940)   | [[15](#_Toc144361764)](#_Toc144362940)  | [[NM](#_Toc144361764)](#_Toc144362940) | [[NS](#_Toc144361764)](#_Toc144362940)  |                                          | [[Expected Sequence Number](#_Toc144361764)](#_Toc144362940)    | [[Not used](#_Toc144361764)](#_Toc144362940)                                           |
| [[5](#_Toc144361764)](#_Toc144362940)   |                                         |                                        | [[NS](#_Toc144361764)](#_Toc144362940)  |                                          | [[Delayed Acknowledgment Type](#_Toc144361764)](#_Toc144362940) | [[Not used](#_Toc144361764)](#_Toc144362940)                                           |
| [[6](#_Toc144361764)](#_Toc144362940)   | [[250](#_Toc144361764)](#_Toc144362940) | [[CE](#_Toc144361764)](#_Toc144362940) | [[NS](#_Toc144361764)](#_Toc144362940)  |                                          | [[Error Condition](#_Toc144361764)](#_Toc144362940)             | [[Not used](#_Toc144361764)](#_Toc144362940)                                           |

[[Refer to Table 14-48.](#_Toc144361764)](#_Toc144362940)

[[<span id="_Toc169170406" class="anchor"></span>Table 14‑48: ACK ERR - Error Segment](#_Toc144361764)](#_Toc144362940)

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 9%" />
<col style="width: 21%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><a href="#_Toc144362940"><span>SEQ</span></a></th>
<th><a href="#_Toc144362940"><span>LEN</span></a></th>
<th><a href="#_Toc144362940"><span>DT</span></a></th>
<th><a href="#_Toc144362940"><span>R/O</span></a></th>
<th><a href="#_Toc144362940"><span>TBL#</span></a></th>
<th><a href="#_Toc144362940"><span>Element Name</span></a></th>
<th><a href="#_Toc144362940"><span>Description</span></a></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="#_Toc144362940"><span>1</span></a></td>
<td><a href="#_Toc144362940"><span>493</span></a></td>
<td><a href="#_Toc144362940"><span>ELD</span></a></td>
<td><a href="#_Toc144362940"><span>NS</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Error Code and Location</span></a></td>
<td><a href="#_Toc144362940"><span>Not used</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>2</span></a></td>
<td><a href="#_Toc144362940"><span>18</span></a></td>
<td><a href="#_Toc144362940"><span>ERL</span></a></td>
<td><a href="#_Toc144362940"><span>O</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>Error Location</span></a></td>
<td><a href="#_Toc144362940"><span>Segment^Sequence^Field^Fld Repetition^Component^Sub-component</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>3</span></a></td>
<td><a href="#_Toc144362940"><span>705</span></a></td>
<td><a href="#_Toc144362940"><span>CWE</span></a></td>
<td><a href="#_Toc144362940"><span>R</span></a></td>
<td><a href="#_Toc144362940"><span>0357</span></a></td>
<td><a href="#_Toc144362940"><span>HL7 Error Code</span></a></td>
<td><a href="#_Toc144362940"><span>Value^Description<br />
See table 0357 below.</span></a></td>
</tr>
</tbody>
</table>

- 

[[ERR fields past ERR.3 are not used and are not shown to save space.](#_Toc144361765)](#_Toc144362940)

[[  
](#_Toc144361765)](#_Toc144362940)

[[Refer to Table 14-49.](#_Toc144361765)](#_Toc144362940)

[[<span id="_Toc169170407" class="anchor"></span>Table 14‑49: HL7 Table 0357 - Message Error Condition Codes](#_Toc144361765)](#_Toc144362940)

| [[Value](#_Toc144361766)](#_Toc144362940) | [[Description](#_Toc144361766)](#_Toc144362940)                | [[Comment](#_Toc144361766)](#_Toc144362940)                                                                                                                                             |
|-------------------------------------------|----------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [[0](#_Toc144361766)](#_Toc144362940)     | [[Message Accepted](#_Toc144361766)](#_Toc144362940)           | [[Success. Optional, as the AA conveys success. Used for systems that must always return a status code.](#_Toc144361766)](#_Toc144362940)                                               |
| [[100](#_Toc144361766)](#_Toc144362940)   | [[Segment Sequence Error](#_Toc144361766)](#_Toc144362940)     | [[Error: The message segments were not in proper order, or required segments are missing.](#_Toc144361766)](#_Toc144362940)                                                             |
| [[101](#_Toc144361766)](#_Toc144362940)   | [[Required Field Missing](#_Toc144361766)](#_Toc144362940)     | [[Error: A required field is missing from a segment.](#_Toc144361766)](#_Toc144362940)                                                                                                  |
| [[102](#_Toc144361766)](#_Toc144362940)   | [[Data Type Error](#_Toc144361766)](#_Toc144362940)            | [[Error: The field contained data of the wrong data type, e.g., an NM field contained “FOO”.](#_Toc144361766)](#_Toc144362940)                                                          |
| [[103](#_Toc144361766)](#_Toc144362940)   | [[Table Value Not Found](#_Toc144361766)](#_Toc144362940)      | [[Error: A field of data type ID or IS was compared against the corresponding table, and no match was found.](#_Toc144361766)](#_Toc144362940)                                          |
| [[200](#_Toc144361766)](#_Toc144362940)   | [[Unsupported Message Type](#_Toc144361766)](#_Toc144362940)   | [[Rejection: The Message Type is not supported.](#_Toc144361766)](#_Toc144362940)                                                                                                       |
| [[201](#_Toc144361766)](#_Toc144362940)   | [[Unsupported Event Code](#_Toc144361766)](#_Toc144362940)     | [[Rejection: The Event Code is not supported.](#_Toc144361766)](#_Toc144362940)                                                                                                         |
| [[202](#_Toc144361766)](#_Toc144362940)   | [[Unsupported Processing ID](#_Toc144361766)](#_Toc144362940)  | [[Rejection: The Processing ID is not supported.](#_Toc144361766)](#_Toc144362940)                                                                                                      |
| [[203](#_Toc144361766)](#_Toc144362940)   | [[Unsupported Version ID](#_Toc144361766)](#_Toc144362940)     | [[Rejection: The Version ID is not supported.](#_Toc144361766)](#_Toc144362940)                                                                                                         |
| [[204](#_Toc144361766)](#_Toc144362940)   | [[Unknown Key Identifier](#_Toc144361766)](#_Toc144362940)     | [[Rejection: The ID of the patient, order, etc., was not found. Used for transactions other than additions, e.g., transfer of a non-existent patient.](#_Toc144361766)](#_Toc144362940) |
| [[205](#_Toc144361766)](#_Toc144362940)   | [[Duplicate Key Identifier](#_Toc144361766)](#_Toc144362940)   | [[Rejection: The ID of the patient, order, etc., already exists. Used in response to addition transactions (Admit, New Order, etc.)](#_Toc144361766)](#_Toc144362940)                   |
| [[206](#_Toc144361766)](#_Toc144362940)   | [[Application Record Locked](#_Toc144361766)](#_Toc144362940)  | [[Rejection: The transaction could not be performed at the application storage level, e.g., database locked.](#_Toc144361766)](#_Toc144362940)                                          |
| [[207](#_Toc144361766)](#_Toc144362940)   | [[Application Internal Error](#_Toc144361766)](#_Toc144362940) | [[Rejection: A catchall for internal errors not explicitly covered by other codes.](#_Toc144361766)](#_Toc144362940)                                                                    |

[[  
](#_Toc144361766)](#_Toc144362940)

[[For the Application NACK that GMRC \*3.0\*123 returns for Errors during processing of the REF I13/I14 messages, the MSA segment will be populated as shown in Table 14-50 below.](#_Toc144361766)](#_Toc144362940)

[[<span id="_Toc169170408" class="anchor"></span>Table 14‑50: MSA Message for NACK – Negative Application Acknowledgment Segment](#_Toc144361766)](#_Toc144362940)

| [[SEQ](#_Toc144361767)](#_Toc144362940) | [[LEN](#_Toc144361767)](#_Toc144362940) | [[DT](#_Toc144361767)](#_Toc144362940) | [[R/O](#_Toc144361767)](#_Toc144362940) | [[TBL#](#_Toc144361767)](#_Toc144362940) | [[Element Name](#_Toc144361767)](#_Toc144362940)                | [[Description](#_Toc144361767)](#_Toc144362940)                                                                                                                        |
|-----------------------------------------|-----------------------------------------|----------------------------------------|-----------------------------------------|------------------------------------------|-----------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [[1](#_Toc144361767)](#_Toc144362940)   | [[2](#_Toc144361767)](#_Toc144362940)   | [[ID](#_Toc144361767)](#_Toc144362940) | [[R](#_Toc144361767)](#_Toc144362940)   | [[0008](#_Toc144361767)](#_Toc144362940) | [[Acknowledgment Code](#_Toc144361767)](#_Toc144362940)         | [[AE for Application Error](#_Toc144361767)](#_Toc144362940)                                                                                                           |
| [[2](#_Toc144361767)](#_Toc144362940)   | [[20](#_Toc144361767)](#_Toc144362940)  | [[ST](#_Toc144361767)](#_Toc144362940) | [[R](#_Toc144361767)](#_Toc144362940)   |                                          | [[Message Control ID](#_Toc144361767)](#_Toc144362940)          | [[Same as MSH.10 of the Request Message](#_Toc144361767)](#_Toc144362940)                                                                                              |
| [[3](#_Toc144361767)](#_Toc144362940)   | [[80](#_Toc144361767)](#_Toc144362940)  | [[ST](#_Toc144361767)](#_Toc144362940) | [[NS](#_Toc144361767)](#_Toc144362940)  |                                          | [[Text Message](#_Toc144361767)](#_Toc144362940)                | [[Error Message Description](#_Toc144361767)](#_Toc144362940)                                                                                                          |
| [[4](#_Toc144361767)](#_Toc144362940)   | [[15](#_Toc144361767)](#_Toc144362940)  | [[NM](#_Toc144361767)](#_Toc144362940) | [[NS](#_Toc144361767)](#_Toc144362940)  |                                          | [[Expected Sequence Number](#_Toc144361767)](#_Toc144362940)    | [[Not used](#_Toc144361767)](#_Toc144362940)                                                                                                                           |
| [[5](#_Toc144361767)](#_Toc144362940)   |                                         |                                        | [[NS](#_Toc144361767)](#_Toc144362940)  |                                          | [[Delayed Acknowledgment Type](#_Toc144361767)](#_Toc144362940) | [[Not used](#_Toc144361767)](#_Toc144362940)                                                                                                                           |
| [[6](#_Toc144361767)](#_Toc144362940)   | [[250](#_Toc144361767)](#_Toc144362940) | [[CE](#_Toc144361767)](#_Toc144362940) | [[NS](#_Toc144361767)](#_Toc144362940)  |                                          | [[Error Condition](#_Toc144361767)](#_Toc144362940)             | [[Patient ICN^Patient NAME^Station ID^Consult ID^Date/Time Stamp when the REF I12/I13 Message is being processed on the VistA System](#_Toc144361767)](#_Toc144362940) |

[[GMRC HCP HL7 MESSAGE is used to report errors in HL7 message generation and processing for GMRC consults.](#_Toc144361767)](#_Toc144362940)

[[Table 14-51 identifies the HL7 fields passed in each kind of event associated with OE/RR. For each event there is an order control code and a set of fields listed. For any given event, however, some of the fields may be empty (observation sub-id, for example).](#_Toc144361767)](#_Toc144362940)

[[The protocols identified in the table use OE/RR namespacing conventions. The messages sent by OE/RR will use the OR namespaced protocols indicated. Individual packages may use whatever protocol names they wish.](#_Toc144361767)](#_Toc144362940)

[[  
](#_Toc144361767)](#_Toc144362940)

[[Refer to Table 14-51.](#_Toc144361767)](#_Toc144362940)

[[<span id="_Toc169170409" class="anchor"></span>Table 14‑51: Front Door – Consults](#_Toc144361767)](#_Toc144362940)

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 29%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th><a href="#_Toc144362940"><span>Action</span></a></th>
<th><a href="#_Toc144362940"><span>Request from OE/RR</span></a></th>
<th><a href="#_Toc144362940"><span>Consults Accepts</span></a></th>
<th><a href="#_Toc144362940"><span>Consults Rejects</span></a></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="#_Toc144362940"><span>Protocol</span></a></td>
<td><a href="#_Toc144362940"><span>OR EVSEND GMRC</span></a></td>
<td><a href="#_Toc144362940"><span>GMRC EVSEND OR</span></a></td>
<td><a href="#_Toc144362940"><span>GMRC EVSEND OR</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>Order Control</span></a></td>
<td><a href="#_Toc144362940"><span>NW (new order)</span></a></td>
<td><a href="#_Toc144362940"><span>OK (accepted)</span></a></td>
<td><a href="#_Toc144362940"><span>OC (canceled)</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>HL7 Fields</span></a></td>
<td><p><a href="#_Toc144362940"><span>MSH: 1,2,3,4,9<br />
PID: 3,5 PV1: 2,3,19</span></a></p>
<p><a href="#_Toc144362940"><span><br />
ORC: 1,2,7,10,12,15<br />
OBR: 4,18</span></a></p>
<p><a href="#_Toc144362940"><span>,19</span></a></p>
<p><a href="#_Toc144362940"><span><br />
OBX: 1,2,3,5</span></a></p></td>
<td><a href="#_Toc144362940"><span>MSH: 1,2,3,4,9<br />
PID: 3,5<br />
ORC: 1,2,3</span></a></td>
<td><a href="#_Toc144362940"><span>MSH: 1,2,3,4,9<br />
PID: 3,5<br />
ORC: 1,2,3,12,15,16 OBR: 4</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>Protocol</span></a></td>
<td><a href="#_Toc144362940"><span>OR EVSEND GMRC</span></a></td>
<td><a href="#_Toc144362940"><span>GMRC EVSEND OR</span></a></td>
<td><a href="#_Toc144362940"><span>GMRC EVSEND OR</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>Order Control</span></a></td>
<td><a href="#_Toc144362940"><span>CA (cancel)<br />
DC (discontinue)<br />
HD (hold)<br />
RL (release)</span></a></td>
<td><a href="#_Toc144362940"><span>CR (canceled)<br />
DR (discontinued)<br />
HR (held)<br />
OR (released)</span></a></td>
<td><a href="#_Toc144362940"><span>UC (unable to cancel)<br />
UD (unable to dc)<br />
UH (unable to hold)<br />
OC (order canceled)</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>HL7 Fields</span></a></td>
<td><a href="#_Toc144362940"><span>MSH: 1,2,3,4,9<br />
PID: 3,5<br />
ORC: 1,2,3,10,12,15,16</span></a></td>
<td><a href="#_Toc144362940"><span>MSH: 1,2,3,4,9<br />
PID: 3,5<br />
ORC: 1,2,3,5</span></a></td>
<td><a href="#_Toc144362940"><span>MSH: 1,2,3,4,9<br />
PID: 3,5<br />
ORC: 1,2,3,16</span></a></td>
</tr>
</tbody>
</table>

[[Back door orders are handled by sending OE/RR the ORM message for a Consult order with a ‘send number’ order control code. This permits OE/RR to store the order in its database and return the OE/RR order number to consults with a ‘number assigned’ order control code. OE/RR cannot actually reject Consult events. The ‘data errors’ order control code is just used as some way to communicate to Consults that OE/RR could not interpret the ORM message. This should generally not happen. Use of the ‘back door’ by packages for ordering is optional. It is still necessary to post an event when results are available.](#_Toc144361878)](#_Toc144362940)

[[  
](#_Toc144361878)](#_Toc144362940)

[[Refer to Table 14-52.](#_Toc144361878)](#_Toc144362940)

[[<span id="_Toc169170410" class="anchor"></span>Table 14‑52: Back Door – Consults](#_Toc144361878)](#_Toc144362940)

<table style="width:100%;">
<colgroup>
<col style="width: 23%" />
<col style="width: 28%" />
<col style="width: 24%" />
<col style="width: 23%" />
</colgroup>
<thead>
<tr class="header">
<th><a href="#_Toc144362940"><span>Action</span></a></th>
<th><a href="#_Toc144362940"><span>Event from Consults</span></a></th>
<th><a href="#_Toc144362940"><span>OE/RR Accepts</span></a></th>
<th><a href="#_Toc144362940"><span>OE/RR Rejects</span></a></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="#_Toc144362940"><span>Protocol</span></a></td>
<td><a href="#_Toc144362940"><span>GMRC EVSEND OR</span></a></td>
<td><a href="#_Toc144362940"><span>OR EVSEND GMRC</span></a></td>
<td><a href="#_Toc144362940"><span>OR EVSEND GMRC</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>Order Control</span></a></td>
<td><a href="#_Toc144362940"><span>SN (send number)</span></a></td>
<td><a href="#_Toc144362940"><span>NA (number assigned)</span></a></td>
<td><a href="#_Toc144362940"><span>DE (data errors)</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>HL7 Fields</span></a></td>
<td><p><a href="#_Toc144362940"><span>MSH: 1,2,3,4,9<br />
PID: 3,5<br />
PV1: 2,3,19</span></a></p>
<p><a href="#_Toc144362940"><span><br />
ORC: 1,3,7,10,12,15<br />
OBR: 4,18</span></a></p>
<p><a href="#_Toc144362940"><span>,19</span></a></p>
<p><a href="#_Toc144362940"><span><br />
OBX: 1,2,3,4,5</span></a></p></td>
<td><a href="#_Toc144362940"><span>MSH: 1,2,3,4,9<br />
PID: 3,5<br />
ORC: 1,2,3</span></a></td>
<td><a href="#_Toc144362940"><span>MSH: 1,2,3,4,9<br />
PID: 3,5<br />
ORC: 1,3,16</span></a></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>Protocol</span></a></td>
<td><a href="#_Toc144362940"><span>GMRC EVSEND OR</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>OR EVSEND GMRC</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>Order Control</span></a></td>
<td><a href="#_Toc144362940"><span>OC (cancel)<br />
OD (discontinue)<br />
OH (hold)<br />
RL (release)</span></a></td>
<td><a href="#_Toc144362940"><span>There is no return event. OE/RR must accept the instruction from Consults.</span></a></td>
<td><a href="#_Toc144362940"><span>DE (data errors)</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>HL7 Fields</span></a></td>
<td><a href="#_Toc144362940"><span>MSH: 1,2,3,4,9<br />
PID: 3,5<br />
ORC: 1,2,3,12,15,16<br />
OBR: 4</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>MSH: 1,2,3,4,9<br />
PID: 3,5<br />
ORC: 1,2,3,16</span></a></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>Protocol</span></a></td>
<td><a href="#_Toc144362940"><span>GMRC EVSEND OR</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>OR EVSEND GMRC</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>Order Control</span></a></td>
<td><a href="#_Toc144362940"><span>SC (accepted)</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>DE (data errors)</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>HL7 Fields</span></a></td>
<td><a href="#_Toc144362940"><span>MSH: 1,2,3,4,9<br />
PID: 3,5<br />
ORC: 1,2,3,5,12,15<br />
OBR: 4</span></a></td>
<td><a href="#_Toc144362940"><span>There is no return event. OE/RR must accept the instruction from Consults.</span></a></td>
<td><a href="#_Toc144362940"><span>MSH: 1,2,3,4,9<br />
PID: 3,5<br />
ORC: 1,2,3,16</span></a></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>Protocol</span></a></td>
<td><a href="#_Toc144362940"><span>GMRC EVSEND OR</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>OR EVSEND GMRC</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>Order Control</span></a></td>
<td><a href="#_Toc144362940"><span>XX (forwarded)</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>DE (data errors)</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>HL7 Fields</span></a></td>
<td><a href="#_Toc144362940"><span>MSH: 1,2,3,4,9 PID: 3,5 ORC: 1,2,3,7,10,12,15 OBX: 1,2,3,4,5</span></a></td>
<td><a href="#_Toc144362940"><span>There is no return event. OE/RR must accept the instruction from Consults.</span></a></td>
<td><a href="#_Toc144362940"><span>MSH: 1,2,3,4,9<br />
PID: 3,5<br />
ORC: 1,2,3,16</span></a></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>Protocol</span></a></td>
<td><a href="#_Toc144362940"><span>GMRC EVSEND OR</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>OR EVSEND GMRC</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>Order Control</span></a></td>
<td><a href="#_Toc144362940"><span>RE (completed)</span></a></td>
<td></td>
<td><a href="#_Toc144362940"><span>DE (data errors)</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>HL7 Fields</span></a></td>
<td><a href="#_Toc144362940"><span>MSH: 1,2,3,4,9<br />
PID: 3,5<br />
ORC: 1,2,3,12,15<br />
OBR: 4,7,22,25,32<br />
OBX: 1,2,3,4,5,8</span></a></td>
<td><a href="#_Toc144362940"><span>There is no return event. OE/RR must accept the instruction from Consults.</span></a></td>
<td><a href="#_Toc144362940"><span>MSH: 1,2,3,4,9<br />
PID: 3,5<br />
ORC: 1,2,3,16</span></a></td>
</tr>
</tbody>
</table>

[[  
](#_Toc144361769)](#_Toc144362940)

[[When Consults makes request services available for ordering, OE/RR needs to be notified. This is done via a protocol event point which should be defined by Consults. When this event point is invoked, an HL7 master file update message is sent. Information that should be available in this segment is listed in Table 14-53 below.](#_Toc144361769)](#_Toc144362940)

[[<span id="_Toc169170411" class="anchor"></span>Table 14‑53: Orderable Item Updates – Request Services](#_Toc144361769)](#_Toc144362940)

| [[SEG](#_Toc144361770)](#_Toc144362940)     | [[SEQ](#_Toc144361770)](#_Toc144362940) | [[Field Name](#_Toc144361770)](#_Toc144362940)              | [[Example](#_Toc144361770)](#_Toc144362940)                        | [[HL7 Type](#_Toc144361770)](#_Toc144362940)                                      |
|---------------------------------------------|-----------------------------------------|-------------------------------------------------------------|--------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| [[MSH](#_Toc144361770)](#_Toc144362940)     | [[1](#_Toc144361770)](#_Toc144362940)   | [[Field Separator](#_Toc144361770)](#_Toc144362940)         | [[\|](#_Toc144361770)](#_Toc144362940)                             | [[string](#_Toc144361770)](#_Toc144362940)                                        |
|                                             | [[2](#_Toc144361770)](#_Toc144362940)   | [[Encoding Characters](#_Toc144361770)](#_Toc144362940)     | [[^~\\](#_Toc144361770)](#_Toc144362940)                           | [[string](#_Toc144361770)](#_Toc144362940)                                        |
|                                             | [[3](#_Toc144361770)](#_Toc144362940)   | [[Sending Application](#_Toc144361770)](#_Toc144362940)     | [[CONSULTS](#_Toc144361770)](#_Toc144362940)                       | [[string](#_Toc144361770)](#_Toc144362940)                                        |
|                                             | [[4](#_Toc144361770)](#_Toc144362940)   | [[Sending Facility](#_Toc144361770)](#_Toc144362940)        | [[660](#_Toc144361770)](#_Toc144362940)                            | [[string](#_Toc144361770)](#_Toc144362940)                                        |
|                                             | [[9](#_Toc144361770)](#_Toc144362940)   | [[Message Type](#_Toc144361770)](#_Toc144362940)            | [[MFN](#_Toc144361770)](#_Toc144362940)                            | [[ID](#_Toc144361770)](#_Toc144362940)                                            |
|                                             |                                         |                                                             |                                                                    |                                                                                   |
| [[MFI](#_Toc144361770)](#_Toc144362940)     | [[1](#_Toc144361770)](#_Toc144362940)   | [[Master File ID](#_Toc144361770)](#_Toc144362940)          | [[123.5^Request Services^99DD](#_Toc144361770)](#_Toc144362940)    | [[coded element](#_Toc144361770)](#_Toc144362940)                                 |
|                                             | [[3](#_Toc144361770)](#_Toc144362940)   | [[File-Level Event Code](#_Toc144361770)](#_Toc144362940)   | [[REP](#_Toc144361770)](#_Toc144362940)                            | [[table 178](#_Toc144361770)](#_Toc144362940)                                     |
|                                             | [[6](#_Toc144361770)](#_Toc144362940)   | [[Response Level Code](#_Toc144361770)](#_Toc144362940)     | [[NE](#_Toc144361770)](#_Toc144362940)                             | [[table 179](#_Toc144361770)](#_Toc144362940)                                     |
|                                             |                                         |                                                             |                                                                    |                                                                                   |
| [[{ MFE](#_Toc144361770)](#_Toc144362940)   | [[1](#_Toc144361770)](#_Toc144362940)   | [[Record-Level Event Code](#_Toc144361770)](#_Toc144362940) | [[MAD](#_Toc144361770)](#_Toc144362940)                            | [[table 180](#_Toc144361770)](#_Toc144362940)                                     |
|                                             | [[4](#_Toc144361770)](#_Toc144362940)   | [[Primary Key](#_Toc144361770)](#_Toc144362940)             | [[^^^25^Cardiology Consult^99CON](#_Toc144361770)](#_Toc144362940) | [[coded element](#_Toc144361770)](#_Toc144362940)                                 |
|                                             |                                         |                                                             |                                                                    |                                                                                   |
| [[ZCS](#_Toc144361770)](#_Toc144362940)     | [[1](#_Toc144361770)](#_Toc144362940)   | [[Service Usage](#_Toc144361770)](#_Toc144362940)           | [[2](#_Toc144361770)](#_Toc144362940)                              | [[coded value (1=Grouper only, 2=Tracking only)](#_Toc144361770)](#_Toc144362940) |
|                                             |                                         |                                                             |                                                                    |                                                                                   |
| [[{ ZSY }](#_Toc144361770)](#_Toc144362940) | [[1](#_Toc144361770)](#_Toc144362940)   | [[Set ID](#_Toc144361770)](#_Toc144362940)                  | [[1](#_Toc144361770)](#_Toc144362940)                              | [[Numeric](#_Toc144361770)](#_Toc144362940)                                       |
| [[}](#_Toc144361770)](#_Toc144362940)       | [[2](#_Toc144361770)](#_Toc144362940)   | [[Synonym](#_Toc144361770)](#_Toc144362940)                 | [[CARD](#_Toc144361770)](#_Toc144362940)                           | [[string](#_Toc144361770)](#_Toc144362940)                                        |

[[Note the following:](#_Toc144361770)](#_Toc144362940)

- 
- 
- 
- 
- 

| [[SEG](#_Toc144361771)](#_Toc144362940)    | [[SEQ](#_Toc144361771)](#_Toc144362940) | [[Field Name](#_Toc144361771)](#_Toc144362940)              | [[Example](#_Toc144361771)](#_Toc144362940)                         | [[HL7 Type](#_Toc144361771)](#_Toc144362940)      |
|--------------------------------------------|-----------------------------------------|-------------------------------------------------------------|---------------------------------------------------------------------|---------------------------------------------------|
| [[MSH](#_Toc144361771)](#_Toc144362940)    | [[1](#_Toc144361771)](#_Toc144362940)   | [[Field Separator](#_Toc144361771)](#_Toc144362940)         | [[\|](#_Toc144361771)](#_Toc144362940)                              | [[string](#_Toc144361771)](#_Toc144362940)        |
|                                            | [[2](#_Toc144361771)](#_Toc144362940)   | [[Encoding Characters](#_Toc144361771)](#_Toc144362940)     | [[^~\\](#_Toc144361771)](#_Toc144362940)                            | [[string](#_Toc144361771)](#_Toc144362940)        |
|                                            | [[3](#_Toc144361771)](#_Toc144362940)   | [[Sending Application](#_Toc144361771)](#_Toc144362940)     | [[PROCEDURES](#_Toc144361771)](#_Toc144362940)                      | [[string](#_Toc144361771)](#_Toc144362940)        |
|                                            | [[4](#_Toc144361771)](#_Toc144362940)   | [[Sending Facility](#_Toc144361771)](#_Toc144362940)        | [[660](#_Toc144361771)](#_Toc144362940)                             | [[string](#_Toc144361771)](#_Toc144362940)        |
|                                            | [[9](#_Toc144361771)](#_Toc144362940)   | [[Message Type](#_Toc144361771)](#_Toc144362940)            | [[MFN](#_Toc144361771)](#_Toc144362940)                             | [[ID](#_Toc144361771)](#_Toc144362940)            |
|                                            |                                         |                                                             |                                                                     |                                                   |
| [[MFI](#_Toc144361771)](#_Toc144362940)    | [[1](#_Toc144361771)](#_Toc144362940)   | [[Master File ID](#_Toc144361771)](#_Toc144362940)          | [[123.3^Procedures^99DD](#_Toc144361771)](#_Toc144362940)           | [[coded element](#_Toc144361771)](#_Toc144362940) |
|                                            | [[3](#_Toc144361771)](#_Toc144362940)   | [[File-Level Event Code](#_Toc144361771)](#_Toc144362940)   | [[REP](#_Toc144361771)](#_Toc144362940)                             | [[table 178](#_Toc144361771)](#_Toc144362940)     |
|                                            | [[6](#_Toc144361771)](#_Toc144362940)   | [[Response Level Code](#_Toc144361771)](#_Toc144362940)     | [[NE](#_Toc144361771)](#_Toc144362940)                              | [[table 179](#_Toc144361771)](#_Toc144362940)     |
|                                            |                                         |                                                             |                                                                     |                                                   |
| [[{ MFE](#_Toc144361771)](#_Toc144362940)  | [[1](#_Toc144361771)](#_Toc144362940)   | [[Record-Level Event Code](#_Toc144361771)](#_Toc144362940) | [[MAD](#_Toc144361771)](#_Toc144362940)                             | [[table 180](#_Toc144361771)](#_Toc144362940)     |
|                                            | [[4](#_Toc144361771)](#_Toc144362940)   | [[Primary Key](#_Toc144361771)](#_Toc144362940)             | [[^^^1225^Electrocardiogram^99PRC](#_Toc144361771)](#_Toc144362940) | [[coded element](#_Toc144361771)](#_Toc144362940) |
|                                            |                                         |                                                             |                                                                     |                                                   |
| [[{ ZSY}](#_Toc144361771)](#_Toc144362940) | [[1](#_Toc144361771)](#_Toc144362940)   | [[Set ID](#_Toc144361771)](#_Toc144362940)                  | [[1](#_Toc144361771)](#_Toc144362940)                               | [[numeric](#_Toc144361771)](#_Toc144362940)       |
| [[}](#_Toc144361771)](#_Toc144362940)      | [[2](#_Toc144361771)](#_Toc144362940)   | [[Synonym](#_Toc144361771)](#_Toc144362940)                 | [[EKG](#_Toc144361771)](#_Toc144362940)                             | [[string](#_Toc144361771)](#_Toc144362940)        |

[[Note the following:](#_Toc144361771)](#_Toc144362940)

- 
- 
- 
- 
- 

[[There are no Consult ordering parameters identified at this time.](#_Toc144361881)](#_Toc144362940)

![](consult-request-tracking-technical-manual-gmrc-3-0-189/089.png)[[![](consult-request-tracking-technical-manual-gmrc-3-0-189/090.png)](#_Toc144361882)](#_Toc144362940)

[[<span id="_Toc169170103" class="anchor"></span>Figure 14‑22: Procedure Calls Example (continued)](#_Toc144361882)](#_Toc144362940)

[[![](consult-request-tracking-technical-manual-gmrc-3-0-189/091.png)](#_Toc144361883)](#_Toc144362940)

[[  
](#_Toc144361883)](#_Toc144362940)

[[<span id="_Toc169170104" class="anchor"></span>Figure 14‑23: Procedure Calls Example (continued)](#_Toc144361883)](#_Toc144362940)

[[![](consult-request-tracking-technical-manual-gmrc-3-0-189/092.png)](#_Toc144361884)](#_Toc144362940)

[[A new feature, Auto-forwarding, has been added with patch GMRC\*3.0\*139. When the Decision Support Tool (DST) determines that a Consult should be forwarded to a different location, the DST data returned will contain the text “DAF-DST Auto-forwarding:”. When the routine ^GMRCDST detects this text, it will examine the text after the colon. If it detects “YES”, then the code will mark this Consult as being forwarded. The routine will then look for the text “AFD-DST Forward to:” text and forward this Consult Order to the requested REQUEST SERVICE entry (#123.5), using the \$\$FR^GMRCGUIA utility.](#_Toc144361884)](#_Toc144362940)

[[If the REQUEST SERVICE entry does not exist, the error message "DVE-DST Error from VistA: Auto-forward target not found" will be placed in the original Consult entry. If DST does not send the “AFD-DST Forward to:” text, the error message will appear as "DVE-DST ID ISSUE: No Content sent from DST". This error message will be placed in the Original Consult entry.](#_Toc144361884)](#_Toc144362940)

[[  
](#_Toc144361884)](#_Toc144362940)

[[The namespace for the Consults package is GMRC. A listing/printout of any or all of the Consults routines can be produced by using the Kernel option XUPRROU (List Routines). This option is found on the XUPROG (Programmer Options) menu, which is a sub-menu of the EVE (Systems Manager Menu) option. When prompted with “routine(s) ? \>:” type in GMRC\* to get a listing of all Consults routines.](#_Toc144361884)](#_Toc144362940)

[[The first line of each routine contains a brief description of the general function of the routine. A listing of just the first line of each Consults routine can be produced by using the Kernel option XU FIRST LINE PRINT (First Line Routine Print). This option is found on the XUPROG (Programmer Options) menu, which is a sub-menu of the EVE (Systems Manager Menu) option.](#_Toc144361884)](#_Toc144362940)

[[The globals used in the Consults package are ^GMR(123, ^GMR(123.1, ^GMR(123.3, ^GMR(123.5 and ^GMR(123.6. A listing/printout of any of these globals can be produced by using the Kernel option XUPRGL (List Global). This option is found on the XUPROG (Programmer Options) menu, which is a sub-menu of the EVE (Systems Manager Menu) option.](#_Toc144361884)](#_Toc144362940)

[[The number-space for Consults files is 123. A listing of these files can be obtained by using the VA FileMan option DILIST (List File Attributes). Depending on the FileMan template used to print the listing, this option will print out all or part of the data dictionary for the Consults files.](#_Toc144361884)](#_Toc144362940)

[[The menu and options exported by the Consults package all begin with the GMRC namespace. Individual options can be viewed by using the Kernel option XUINQUIRE (Inquire). This option is found on the menu XUMAINT (Menu management), which is a sub-menu of the EVE (Systems Manager Menu) option.](#_Toc144361884)](#_Toc144362940)

[[A diagram of the structure of the Consults menu and its options can be produced by using the Kernel option XUUSERACC (Diagram Menus). Choosing XUUSERACC permits you to further select XUUSERACC1 or XUUSERACC2 menu diagrams with entry/exit actions or abbreviated menu diagrams. This option is found on the menu XUMAINT (Menu management), which is a sub-menu of the EVE (Systems Manager Menu) option.](#_Toc144361884)](#_Toc144362940)

[[XINDEX is a routine that produces a report called the VA Cross-Referencer. This report is a technical and cross-reference listing of one routine or a group of routines. XINDEX provides a summary of errors and warnings for routines that do not comply with VA programming standards and conventions, a list of local and global variables and what routines they are referenced in, and a listing of internal and external routine calls. XINDEX is invoked from programmer mode: D ^XINDEX. When selecting routines, select GMRC\*.](#_Toc144361884)](#_Toc144362940)

[[  
](#_Toc144361884)](#_Toc144362940)

[[Refer to Table 16-1.](#_Toc144361884)](#_Toc144362940)

[[<span id="_Toc169170413" class="anchor"></span>Table 16‑1: Glossary](#_Toc144361884)](#_Toc144362940)

| [[Term](#_Toc144361772)](#_Toc144362940)                  | [[Definition](#_Toc144361772)](#_Toc144362940)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|-----------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [[Action](#_Toc144361772)](#_Toc144362940)                | [[An action in Consults can be selected throughout processing to 1) control screen movement, or 2) process existing orders.](#_Toc144361772)](#_Toc144362940)                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [[Consult](#_Toc144361772)](#_Toc144362940)               | [[Referral of a patient by the primary care physician to another hospital service/specialty, to obtain a medical opinion based on patient evaluation and completion of any procedures, modalities, or treatments the consulting specialist deems necessary to render a medical opinion. For instance, if a primary care physician orders a patient evaluation from Cardiology Service, and the cardiology specialist orders an Electrocardiogram (EKG) to complete the evaluation and provide an opinion concerning the patient’s condition, this type of order is considered a “Consult.”](#_Toc144361772)](#_Toc144362940) |
| [[Discontinued Orders](#_Toc144361772)](#_Toc144362940)   | [[Orders that are discontinued. When an order is discontinued, it must be completely re-entered to be resubmitted. However, if an order is canceled, it can be edited to correct some deficiency and resubmitted.](#_Toc144361772)](#_Toc144362940)                                                                                                                                                                                                                                                                                                                                                                          |
| [[Order](#_Toc144361772)](#_Toc144362940)                 | [[A request for a consult (service/sub-specialty evaluation) or procedure (Electrocardiogram) to be completed for a patient.](#_Toc144361772)](#_Toc144362940)                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [[Order Cancellation](#_Toc144361772)](#_Toc144362940)    | [[The cancellation of a consult or procedure request which allows the requesting provider to edit a portion of the original request and re-submit the request to the consulting service.](#_Toc144361772)](#_Toc144362940)                                                                                                                                                                                                                                                                                                                                                                                                   |
| [[Order Discontinuation](#_Toc144361772)](#_Toc144362940) | [[A request to stop (discontinue) performance of a consult/procedure request.](#_Toc144361772)](#_Toc144362940)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [[HCPS](#_Toc144361772)](#_Toc144362940)                  | [[The Healthcare Claims Processing System is a centralized, automated system that will support the management of purchased care referrals/authorizations.](#_Toc144361772)](#_Toc144362940)                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [[IFC](#_Toc144361772)](#_Toc144362940)                   | [[Inter-Facility Consults permits the transmitting of consults and related information between Department of Veterans Affairs facilities. Consult requests are made to remote facilities because the needed service is not locally available or for patient convenience. Although the Consult Package is utilized in the hospital settings, Consult requests between facilities have been done manually in the past.](#_Toc144361772)](#_Toc144362940)                                                                                                                                                                       |
| [[MPI](#_Toc144361772)](#_Toc144362940)                   | [[Master Patient Index. An index of VA patients that is global in nature, showing patients that have been seen by more than one VA facility and giving information about which facilities are involved.](#_Toc144361772)](#_Toc144362940)                                                                                                                                                                                                                                                                                                                                                                                    |
| [[MVI](#_Toc144361772)](#_Toc144362940)                   | [[Master Veteran Index, see MPI](#_Toc144361772)](#_Toc144362940)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [[NVC](#_Toc144361772)](#_Toc144362940)                   | [[Non VA Care. Care provided to eligible Veterans when VA facilities are not feasibly available.](#_Toc144361772)](#_Toc144362940)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [[Procedure Request](#_Toc144361772)](#_Toc144362940)     | [[Any procedure (EKG, Stress Test, etc.) which may be ordered from another service/specialty without requiring formal consultation first.](#_Toc144361772)](#_Toc144362940)                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [[Result](#_Toc144361772)](#_Toc144362940)                | [[A consequence of an order. Refers to evaluation or status results. In regard to Consult/Request Tracking, results refer to a TIU document or Medicine procedure result attached to the consult or procedure request.](#_Toc144361772)](#_Toc144362940)                                                                                                                                                                                                                                                                                                                                                                     |
| [[Requestor](#_Toc144361772)](#_Toc144362940)             | [[This is the health care provider (e. g., the physician/clinician) who requests the order to be done.](#_Toc144361772)](#_Toc144362940)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [[Screen Context](#_Toc144361772)](#_Toc144362940)        | [[This term refers to the particular selection of orders displayed on the screen (e. g., Medicine consults for the patient Ralph Jones).](#_Toc144361772)](#_Toc144362940)                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [[Service](#_Toc144361772)](#_Toc144362940)               | [[A clinical or administrative specialty (or department) within a Medical Center.](#_Toc144361772)](#_Toc144362940)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [[Status](#_Toc144361772)](#_Toc144362940)                | [[A result that indicates the processing state of an order; for example, a Cardiology Consult order may be “discontinued (dc)” or “completed (c)”.](#_Toc144361772)](#_Toc144362940)                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [[Status Symbols](#_Toc144361772)](#_Toc144362940)        | [[Codes used in order entry and Consults displays to designate the status of the order.](#_Toc144361772)](#_Toc144362940)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

- 
- 
- 

[[A service is only selectable for update/tracking if it is defined as part of the ALL SERVICES hierarchy.Disabled services can be left in the ALL SERVICES hierarchy so their order results can be returned but are not selectable in the ordering process.Tracking services must be in the ALL SERVICES hierarchy in order to be receive forwarded consults. The tracking service can only be selectable in the order forwarding process if the user is an update user for the tracking service or its parent service.](#_Toc144363038)](#_Toc144362940)

1.  1.  
    2.  1.  
    3.  
    4.  
2.  1.  
    2.  
    3.  
    4.  

[[Plan the Consult Service Hierarchy.Identify services to receive consults or to be Inter-Facility Services.Determine if the service should be selectable in the ordering process from CPRS.For some consults, the order may need to be sent to a Service control point for Forwarding by the control point to a service which has been identified as a “Tracking Only” service. (Tracking Only services are not selectable during the initial CPRS order process.) Where a service control point is preferred, the tracking services should be sub-specialties under the control point service within the ALL SERVICES hierarchy.Determine if there should be a service that would be used as a “Grouper Only” (e.g., Inpatient Services, Outpatient Services, and Outside Services might be good Services to define as groupers).When a Grouper Only service is selected in the CPRS order process, the service hierarchy defined under the grouper service will be displayed to select from. The Grouper Only cannot be selected to receive an order. The ALL SERVICES service is a Grouper Only provided to build the Consult Service hierarchy upon.For each Service, Identify the Service.Select a unique name to identify the service while ordering. If the service is to be on Inter-Facility Consults (IFC) service, we suggest you include the site name in the service (Example: Eye Clinic—Boise).Optionally, select an abbreviated print name to be used when displaying notifications. This should be a short name that is easily recognized by users as belonging to the service.Optionally, select one or more synonyms that can be used when entering the service name into the computer.Identify the service printer which will be used to automatically print Consult Form SF 513 when a consult order is received from CPRS.](#_Toc144363038)](#_Toc144362940)

> [[Note: Effective with Consult/Request Tracking V. 3.](#_Toc144363038)[0, All Consult Form SF 513 prints are done from consult routines. OE/RR print formats are no longer used for consult prints.](#_Toc144362940)](#_Toc144362940)

3.  1.  
    2.  
4.  1.  
    2.  
5.  1.  
    2.  
    3.  
    4.  
    5.  
6.  1.  
    2.  
    3.  
    4.  
    5.  1.  
        2.  
        3.  
        4.  
        5.  
        6.  
7.  1.  
    2.  
    3.  
    4.  
    5.  
    6.  
    7.  
    8.  
    9.  
8.  

> [[Plan Actions to take for a Discontinued ConsultDecide if the service should be notified when a consult is discontinued.Decide if the SF 513 should be reprinted to the receiving service when a consult is discontinued.Determine Provisional Diagnosis requirements for the Service.Decide if consults going to this service should be required to have a provisional diagnosis. The provisional diagnosis can be required, set as optional, or suppressed.Decide if provisional diagnosis going to this service should be taken from the Clinical Lexicon, or if free text is allowed.Plan Prerequisites and Boilerplate.Decide if consults going to this service should have a prerequisite. A prerequisite is a text message that reminds the referring physician what needs to be done before a consult can be sent to this service. The prerequisite message gives the referring physician a chance to back out of the consult dialog.Decide if consults going to this service should provide a default reason for request when an order is placed. This is a piece of boilerplate text, including TIU objects, that is consistent for each consult received.If this service is to be an IFC service, then enter the IFC Remote Site name and IFC Remote Service name.If this service is to be an to receive IFC requests from other sites, then enter the IFC Sending Facility name(s).Decide if editing of the default reason for request should be restricted. Editing can be unrestricted, restricted, or allowed only before release to the service.Plan Notification Recipients.Identify individuals at the receiving service who should be notified when a consult is being sent to the receiving service.Identify service teams of clinicians or service users which should receive notifications. Team definitions may be used in addition to or in lieu of naming individuals to receive notifications.Identify hospital locations that are assumed to be part of this service. Any consult activity on patients in that location triggers a notification. Specify one individual to notify and/or a team to notify.Decide if parent services of this service should be notified of activities occurring on consults for this service.Decide if notifications should be deleted on an individual basis, or if all notifications should be deleted when one individual reviews it. The default is Individual Recipient, so if All Recipients is desired, use the Set Deletion Parameters for Notifications option of the Notification Mgmt Menu to change this value for each of the five consult notifications. They are:#23 CONSULT/REQUEST RESOLUTION#27 NEW SERVICE CONSULT/REQUEST#30 CONSULT/REQUEST CANCEL/HOLD#63 CONSULT/REQUEST UPDATED#89 PROSTHETICS CONSULTPlan Service Users.Decide if you are going to allow unrestricted access to this service. If so, you may skip to step 13.Identify individuals at the receiving service who will NOT receive notifications about new consults but should be able to perform update capabilities for this service.Identify teams at the receiving service who will NOT receive notifications about new consults but should be able to perform update capabilities for this service.Identify user classes who will NOT receive notifications about new consults but should be able to perform update capabilities for this service.Identify administrative update users. Such a user can perform administrative completions on consults at this service. These users can, optionally, be included as notifications recipients for this service.Identify administrative update teams for this service. The members of these teams can, optionally, be included as notifications recipients for this service.Decide if update users of the parent services should be allowed to update consults for this service.Identify a special updates individual (someone who can perform group updates) for this service. This individual should already be a service user.Identify sub-services of this service.Implementation and Maintenance (Abbreviated Guidelines)Participants: IRMS/ADPAC](#_Toc144362940)](#_Toc144362940)

1.  
2.  

> [[You may set up a team for each consult service. The team members being the identified clinical users. Use the Team Mgmt Menu option, ORLP TEAM MENU.Turn on the NEW SERVICE CONSULT/REQUEST notification for each of the individuals who were identified to receive notifications. Use the Enable/Disable Notifications option of the NOTIFICATION MGMT MENU, ORB NOT MGR MENU.Note: Unless Consult notifications are set to mandatory, individual users may use the Enable/Disable My Notifications option of the Notifications Management Menu to individually disable the notifications they do not want to receive.](#_Toc144362940)](#_Toc144362940)

3.  
4.  
5.  
6.  
7.  
8.  

> [[Turn on the CONSULT/REQUEST RESOLUTION notification for each ordering provider identified to receive this notification, or train them to do it themselves. Use the Enable/Disable Notifications option of the NOTIFICATION MGMT MENU, ORB NOT MGR MENU.Turn on the CONSULT/REQUEST CANCEL/HOLD notification for each ordering provider identified to receive this notification, or train them to do it themselves. Use the Enable/Disable Notifications option of the NOTIFICATION MGMT MENU, ORB NOT MGR MENU.Turn on the CONSULT/REQUEST UPDATED notification for each ordering provider identified to receive this notification, or train them to do it themselves. Use the Enable/Disable Notifications option of the NOTIFICATION MGMT MENU, ORB NOT MGR MENU.Turn on the PROSTHETICS CONSULT UPDATED notification for each ordering provider identified to receive this notification, or train them to do it themselves. PROSTHETICS CONSULT UPDATED should be enabled for identified personnel requiring updates to prosthetics consults. Use the Enable/Disable Notifications option of the NOTIFICATION MGMT MENU, ORB NOT MGR MENU.Define the Service hierarchy in the Request Services File (#123.5) with the associated users and service printer. Use the “Set up Consult Services” option, GMRC SETUP REQUEST SERVICES.Note: You must NOT use VA FileMan to modify services in the hierarchy. The Consult/Request Tracking interface to CPRS depends on the services being defined using the GMRC SETUP REQUEST SERVICES option.](#_Toc144362940)](#_Toc144362940)

9.  
10. 
9.  
1.  
2.  
3.  

> [[Assign the Setup Service Users GMRC SETUP SERVICE USERS option to the users permitted to manage service users.Assign the following two options to Service update users’ primary or secondary menu option: Consult Tracking \[GMRC SERVICE TRACKING\] and Service Consults Pending Resolution \[GMRC RPT PENDING CONSULTS\].SetupPlan your hospital’s TIU hierarchy. See the Text Integration Utility (TIU) Implementation Guide for details on this step.If you have not already done so, install TIU\*1\*4.Run the TIU DEFINE CONSULTS option.Note: If you do not run the TIU DEFINE CONSULTS option, no status update takes place when the TIU note is entered.](#_Toc144362940)](#_Toc144362940)

4.  
5.  

> [[Enter the rest of your planned TIU document hierarchy using the Manager Document Definition Menu.Define consult document parameters (as recommended on page 70 of this manual) using the Document Parameter Edit option.Note: We particularly recommend entering Yes to ALLOW \>1 RECORDS PER VISIT.](#_Toc144362940)](#_Toc144362940)

6.  

[[Check the value for parameter GMRC CONSULT LIST DAYS. The parameter controls how many days are searched when looking for consult to associate with a progress note. The default is 365 days.](#_Toc144362940)](#_Toc144362940)

[[  
](#_Toc144363039)](#_Toc144362940)

> [[Page 1 of 3](#_Toc144363039)](#_Toc144362940)

[[  
](#_Toc144363039)](#_Toc144362940)

[[\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_](#_Toc144363039)](#_Toc144362940)

[[Update Teams without Notifications:](#_Toc144363039)](#_Toc144362940)

[[\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  
](#_Toc144363039)](#_Toc144362940)

[[Update User Class without Notifications:](#_Toc144363039)](#_Toc144362940)

[[\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_](#_Toc144363039)](#_Toc144362940)

> [[Page 2 of 3](#_Toc144363039)](#_Toc144362940)

[[  
Consult Services Worksheet](#_Toc144363039)](#_Toc144362940)

[[\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_  
\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_](#_Toc144363039)](#_Toc144362940)

[[You can use the Consult Service User Management option, in conjunction with availability to various menus and options, to control access to Consults functionality. The menus that can be provided are:](#_Toc144363042)](#_Toc144362940)

- 
- 

| [[Option](#_Toc144361773)](#_Toc144362940)                              | [[Services](#_Toc144361773)](#_Toc144362940)                                                                        |
|-------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| [[Consult Service Tracking](#_Toc144361773)](#_Toc144362940)            | [[Tracking and/or update functionality depending upon your individual privileges.](#_Toc144361773)](#_Toc144362940) |
| [[Pharmacy TPN Consults](#_Toc144361773)](#_Toc144362940)               | [[Tracking, and update functionality.](#_Toc144361773)](#_Toc144362940)                                             |
| [[Completion Time Statistics](#_Toc144361773)](#_Toc144362940)          | [[Reporting.](#_Toc144361773)](#_Toc144362940)                                                                      |
| [[Service Consults Pending Resolution](#_Toc144361773)](#_Toc144362940) | [[Reporting.](#_Toc144361773)](#_Toc144362940)                                                                      |

[[With the GMRC Service User Management option you can set users up to be update users for one or more services at your hospital. In addition, you can grant the ability to receive consult notifications according to criteria outlined in Table 20-2.](#_Toc144361773)](#_Toc144362940)

[[<span id="_Toc169170415" class="anchor"></span>Table 20‑2: Consult Notifications Criteria](#_Toc144361773)](#_Toc144362940)

| [[Category](#_Toc144361774)](#_Toc144362940)                                           | [[Notifications Received](#_Toc144361774)](#_Toc144362940)                                                                                                       |
|----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [[UPDATE USERS W/O NOTIFICATIONS](#_Toc144361774)](#_Toc144362940)                     | [[Unless otherwise set up, will not receive notifications.](#_Toc144361774)](#_Toc144362940)                                                                     |
| [[SERVICE INDIVIDUAL TO NOTIFY](#_Toc144361774)](#_Toc144362940)                       | [[Receive consult notifications for your service.](#_Toc144361774)](#_Toc144362940)                                                                              |
| [[SERVICE TEAM TO NOTIFY](#_Toc144361774)](#_Toc144362940)                             | [[Receive consult notifications for your service. These teams send notifications regardless of the patients contained on them.](#_Toc144361774)](#_Toc144362940) |
| [[NOTIFICATION BY PT LOCATION - INDIVIDUAL TO NOTIFY](#_Toc144361774)](#_Toc144362940) | [[Receive all consult notifications for your service for patients in a specified ward.](#_Toc144361774)](#_Toc144362940)                                         |
| [[NOTIFICATION BY PT LOCATION - TEAM TO NOTIFY](#_Toc144361774)](#_Toc144362940)       | [[Receive consult notifications for patients in a specified ward.](#_Toc144361774)](#_Toc144362940)                                                              |
| [[NOTIFICATION BY PT LOCATION - TEAM TO NOTIFY](#_Toc144361774)](#_Toc144362940)       | [[Receive consult notifications for patients in a specified ward.](#_Toc144361774)](#_Toc144362940)                                                              |

| [[Privilege](#_Toc144361774)](#_Toc144362940)               | [[Granted](#_Toc144361774)](#_Toc144362940)                                                            |
|-------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| [[Originate a consult](#_Toc144361774)](#_Toc144362940)     | [[Anyone with access to CPRS](#_Toc144361774)](#_Toc144362940)                                         |
| [[Sign a consult](#_Toc144361774)](#_Toc144362940)          | [[Anyone who can sign an order](#_Toc144361774)](#_Toc144362940)                                       |
| [[Change a consult status](#_Toc144361774)](#_Toc144362940) | [[Anyone with update privileges](#_Toc144361774)](#_Toc144362940)                                      |
| [[View or print a consult](#_Toc144361774)](#_Toc144362940) | [[Anyone with the Consult Service Tracking option or access to CPRS.](#_Toc144361774)](#_Toc144362940) |

| [[Option Name](#_Toc144363043)](#_Toc144362940)               | [[File](#_Toc144363043)](#_Toc144362940) |
|---------------------------------------------------------------|------------------------------------------|
| [[GMRC MGR](#_Toc144363043)](#_Toc144362940)                  | [[19](#_Toc144363043)](#_Toc144362940)   |
| [[GMRC GENERAL SERVICE USER](#_Toc144363043)](#_Toc144362940) | [[19](#_Toc144363043)](#_Toc144362940)   |
| [[GMRC PHARMACY USER](#_Toc144363043)](#_Toc144362940)        | [[19](#_Toc144363043)](#_Toc144362940)   |
| [[GMRC SERVICE TRACKING](#_Toc144363043)](#_Toc144362940)     | [[19](#_Toc144363043)](#_Toc144362940)   |
| [[GMRC TPN CONSULTS](#_Toc144363043)](#_Toc144362940)         | [[19](#_Toc144363043)](#_Toc144362940)   |
| [[GMRC RPT PENDING CONSULTS](#_Toc144363043)](#_Toc144362940) | [[19](#_Toc144363043)](#_Toc144362940)   |
| [[GMRC REVIEW SCREEN](#_Toc144363043)](#_Toc144362940)        | [[101](#_Toc144363043)](#_Toc144362940)  |

[[  
](#_Toc144363043)](#_Toc144362940)

[[This option should be given to IRMS/ADPAC personnel. It is composed of all options distributed with the Consults package.](#_Toc144363043)](#_Toc144362940)

[[This menu provides access to the most commonly used Consults options that a general user, other than Medicine, would be interested in. This option should be added to their primary or secondary menu options.](#_Toc144363043)](#_Toc144362940)

[[This menu provides access to the most commonly used Consults options that a user of the Pharmacy TPN option would be interested in. This option should be added to their primary or secondary menu options.](#_Toc144363043)](#_Toc144362940)

[[The Consult Service Tracking (GMRC SERVICE TRACKING) option may be given to “review only” UANDU service “update” users. This option should be added to their primary or secondary menu options.](#_Toc144363043)](#_Toc144362940)

[[You may want to add the GMRC SERVICE TRACKING option to the OR MAIN MENU options in the Option file (#19) as well, since users of these OR options are likely interested in reviewing consult/request activities services may have taken.](#_Toc144363043)](#_Toc144362940)

[[Pharmacy personnel who need to be able to update File 123, REQUEST/CONSULTATION file, with service activity tracking updates should have the GMRC PHARMACY TPN CONSULTS option added to their primary or secondary menu options.](#_Toc144363043)](#_Toc144362940)

[[Refer to Table 20-5, which provides a list of recommended VA FileMan access codes associated with each file contained in the Consults package.](#_Toc144363044)](#_Toc144362940)

[[<span id="_Toc169170418" class="anchor"></span>Table 20‑5: Recommended FileMan Access Codes](#_Toc144363044)](#_Toc144362940)

| [[File Number](#_Toc144361775)](#_Toc144362940) | [[File Name](#_Toc144361775)](#_Toc144362940)            | [[DD Access](#_Toc144361775)](#_Toc144362940) | [[RD Access](#_Toc144361775)](#_Toc144362940) | [[WR Access](#_Toc144361775)](#_Toc144362940) | [[DEL Access](#_Toc144361775)](#_Toc144362940) | [[LAYGO Access](#_Toc144361775)](#_Toc144362940) |
|-------------------------------------------------|----------------------------------------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|------------------------------------------------|--------------------------------------------------|
| [[(#123)](#_Toc144361775)](#_Toc144362940)      | [[Request/Consultation](#_Toc144361775)](#_Toc144362940) |                                               |                                               |                                               |                                                |                                                  |
| [[(#123.1)](#_Toc144361775)](#_Toc144362940)    | [[Request Action Types](#_Toc144361775)](#_Toc144362940) |                                               |                                               |                                               |                                                |                                                  |
| [[(#123.3)](#_Toc144361775)](#_Toc144362940)    | [[GMRC Procedures](#_Toc144361775)](#_Toc144362940)      |                                               |                                               |                                               |                                                |                                                  |
| [[(#123.5)](#_Toc144361775)](#_Toc144362940)    | [[Request Services](#_Toc144361775)](#_Toc144362940)     |                                               |                                               |                                               |                                                |                                                  |

[[The Consults Package is distributed for all Services at a facility to track consult/request activity. Security at the Service level is set up by IRMS/ADPAC personnel in the Request Services file (#123.5). Specific fields which provide security restrictions include GMRCACTM PHARMACY PKG MENU, described below.](#_Toc144363045)](#_Toc144362940)

[[This is the PROTOCOL ACTION MENU exported for use by Pharmacy Service personnel to process Pharmacy TPN Consults.](#_Toc144363045)](#_Toc144362940)

[[Refer to Table 20-6.](#_Toc144363046)](#_Toc144362940)

[[<span id="_Toc169170419" class="anchor"></span>Table 20‑6: Routine Descriptions](#_Toc144363046)](#_Toc144362940)

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 74%" />
</colgroup>
<thead>
<tr class="header">
<th><a href="#_Toc144362940"><span>Routine</span></a></th>
<th><a href="#_Toc144362940"><span>Description</span></a></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRC101</span></a></td>
<td><a href="#_Toc144362940"><span>Create Protocol entries for OE/RR ADD orders screens</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRC101C</span></a></td>
<td><a href="#_Toc144362940"><span>Create Protocol entries for OE/RR ADD orders screens (Continued)</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRC101H</span></a></td>
<td><a href="#_Toc144362940"><span>Set up HL-7 message to update OERR orderable items file with new consult type.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRC15EN</span></a></td>
<td><a href="#_Toc144362940"><span>Environment check GMRC*3*15</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRC513U</span></a></td>
<td><a href="#_Toc144362940"><span>Obsolete utility deleted with GMRC*3*4.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRC7L</span></a></td>
<td><a href="#_Toc144362940"><span>List Template Exporter.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRC75P</span></a></td>
<td><a href="#_Toc144362940"><span>Add the ‘HCPS, APPLICATION PROXY’ user the NEW PERSON (#200) file.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCA1</span></a></td>
<td><a href="#_Toc144362940"><span>Actions taken from Review Screens.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCA2</span></a></td>
<td><a href="#_Toc144362940"><span>Select prompt for processing actions.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCAAC</span></a></td>
<td><a href="#_Toc144362940"><span>Administrative Complete action consult logic.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCACMT</span></a></td>
<td><a href="#_Toc144362940"><span>Comment Action and alerting.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCACTM</span></a></td>
<td><a href="#_Toc144362940"><span>Set GMRCACTM with action menu based on Service.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCADC</span></a></td>
<td><a href="#_Toc144362940"><span>Discontinue Action taken from List Manager.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCAFRD</span></a></td>
<td><a href="#_Toc144362940"><span>Forward Req (FR) Action from Review Screen.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCALOR</span></a></td>
<td><a href="#_Toc144362940"><span>Process a consult from an alert notification.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCALRT</span></a></td>
<td><a href="#_Toc144362940"><span>List Manager alert action interface.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCAR</span></a></td>
<td><a href="#_Toc144362940"><span>Associate Results (AR) Action taken from Review Screen.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCART</span></a></td>
<td><a href="#_Toc144362940"><span>Result display logic.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCASF</span></a></td>
<td><a href="#_Toc144362940"><span>Significant Findings Action.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCAST</span></a></td>
<td><a href="#_Toc144362940"><span>Select OE/RR Status (ST) Action.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCASV</span></a></td>
<td><a href="#_Toc144362940"><span>Build ^TMP("GMRCS" of Svc(s)/Specialties.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCASV1</span></a></td>
<td><a href="#_Toc144362940"><span>Hierarchy Mgmt cont'd.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCAU</span></a></td>
<td><a href="#_Toc144362940"><span>Action Utilities.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCCA</span></a></td>
<td><a href="#_Toc144362940"><span>Report Prompting for Configuration Tool</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCCB</span></a></td>
<td><a href="#_Toc144362940"><span>Data Gathering</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCCC</span></a></td>
<td><a href="#_Toc144362940"><span>Output Data</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCCD</span></a></td>
<td><a href="#_Toc144362940"><span>Interactive Consult Update</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCCX</span></a></td>
<td><a href="#_Toc144362940"><span>Configuration File Utilities</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCCY</span></a></td>
<td><a href="#_Toc144362940"><span>Consult Closure Tool: Date Range Selector</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCCLR</span></a></td>
<td><a href="#_Toc144362940"><span>Kill-off all variables used for consults tracking.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCCPRS</span></a></td>
<td><a href="#_Toc144362940"><span>Routine To Give Actions For Consults From The OE/RR Menu's.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCDDX</span></a></td>
<td><a href="#_Toc144362940"><span>AC cross-reference logic for 123.5, field .01.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCDST</span></a></td>
<td><a href="#_Toc144362940"><span>Retrieve decision from DST server</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCDIS</span></a></td>
<td><a href="#_Toc144362940"><span>LM routine to disassociate med results</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCDPCK</span></a></td>
<td><a href="#_Toc144362940"><span>Check for a duplicate Consult/Request that has a status of active, pending or scheduled.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCDRFR</span></a></td>
<td><a href="#_Toc144362940"><span>Default reason for request utils.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCEDIT</span></a></td>
<td><a href="#_Toc144362940"><span>Edit cancelled consult-main driver.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCEDT1</span></a></td>
<td><a href="#_Toc144362940"><span>Edit a consult and re-send as new.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCEDT2</span></a></td>
<td><a href="#_Toc144362940"><span>Resubmit a cancelled consult.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCEDT3</span></a></td>
<td><a href="#_Toc144362940"><span>For a Cancelled Consult - File edited data for tracking consult.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCEDT4</span></a></td>
<td><a href="#_Toc144362940"><span>Utilities for editing fields.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCFP</span></a></td>
<td><a href="#_Toc144362940"><span>GMRC FEE PARAM List Utilities</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRC FPA</span></a></td>
<td><a href="#_Toc144362940"><span>GMRC FEE PARAM List Utilities</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCFX23</span></a></td>
<td><a href="#_Toc144362940"><span>Consult postinit file maintenance.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCGUIA</span></a></td>
<td><a href="#_Toc144362940"><span>File Consult actions from GUI.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCGUIB</span></a></td>
<td><a href="#_Toc144362940"><span>GUI actions for consults.3</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCGUIC</span></a></td>
<td><a href="#_Toc144362940"><span>GUI actions for editing consults.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCGUIU</span></a></td>
<td><a href="#_Toc144362940"><span>Kill off variables from GUI routines.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCHK</span></a></td>
<td><a href="#_Toc144362940"><span>GMRC check for programmer access.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCHL7</span></a></td>
<td><a href="#_Toc144362940"><span>HL-7 formatting routine for consult information to be passed to OER.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCHL72</span></a></td>
<td><a href="#_Toc144362940"><span>HL-7 formats OBX and NTE segments.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCHL7A</span></a></td>
<td><a href="#_Toc144362940"><span>Receive HL-7 Message form OERR and break it into its components and store it in File 123.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCHL7B</span></a></td>
<td><a href="#_Toc144362940"><span>Process order parameters from ^GMRCHL7A and place data into ^GMR(123 global.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCHL7H</span></a></td>
<td><a href="#_Toc144362940"><span>Receive consult event messages. Called by GMRCACMT and GMRCGUIB.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCHL7I</span></a></td>
<td><a href="#_Toc144362940"><span>Processes incoming messages from HCPS.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCHL7P</span></a></td>
<td><a href="#_Toc144362940"><span>Generate HL7 v2.5 REF messages. Called by GMRCH7H.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCHL7U</span></a></td>
<td><a href="#_Toc144362940"><span>Utilities associated with HL7 messages.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCHLP</span></a></td>
<td><a href="#_Toc144362940"><span>List Manager help logic.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCIAC1</span></a></td>
<td><a href="#_Toc144362940"><span>File IFC activities cont'd.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCIAC2</span></a></td>
<td><a href="#_Toc144362940"><span>File IFC activities cont'd.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCIACT</span></a></td>
<td><a href="#_Toc144362940"><span>Process actions on IFC.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCIBKG</span></a></td>
<td><a href="#_Toc144362940"><span>IFC background error processor.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCIBKM</span></a></td>
<td><a href="#_Toc144362940"><span>Monitor IFC background params.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCIERR</span></a></td>
<td><a href="#_Toc144362940"><span>Process IFC message error alert.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCIEV1</span></a></td>
<td><a href="#_Toc144362940"><span>IFC events cont'd .</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCIEVT</span></a></td>
<td><a href="#_Toc144362940"><span>Process events and build HL7 message.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCILKP</span></a></td>
<td><a href="#_Toc144362940"><span>Look up IFC by remote consult number.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCIMSG</span></a></td>
<td><a href="#_Toc144362940"><span>IFC message handling routine.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCINC</span></a></td>
<td><a href="#_Toc144362940"><span>List incomplete IFC transactions.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCIR</span></a></td>
<td><a href="#_Toc144362940"><span>IFC request data &amp; statistics.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCISEG</span></a></td>
<td><a href="#_Toc144362940"><span>Create IFC HL7 segments.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCISG1</span></a></td>
<td><a href="#_Toc144362940"><span>Build IFC HL7 segments cont'd.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCITR</span></a></td>
<td><a href="#_Toc144362940"><span>IFC transactions.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCITST</span></a></td>
<td><a href="#_Toc144362940"><span>Test IFC setup.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCIUTL</span></a></td>
<td><a href="#_Toc144362940"><span>Utilities for inter-facility consults.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCMCP</span></a></td>
<td><a href="#_Toc144362940"><span>List Manager Format Routine To Collect Medicine Package Consults and format them for display by List Manager.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCMED</span></a></td>
<td><a href="#_Toc144362940"><span>Medicine interface routines.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCMED1</span></a></td>
<td><a href="#_Toc144362940"><span>Extract medicine results for consult tracking.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCMENU</span></a></td>
<td><a href="#_Toc144362940"><span>Select List Manager menu for user characteristics.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCMER</span></a></td>
<td><a href="#_Toc144362940"><span>Print Medicine Results in List Manager Format.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCMP</span></a></td>
<td><a href="#_Toc144362940"><span>List Manager routine: Medical Service and sub-specialty consults.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCMSS</span></a></td>
<td><a href="#_Toc144362940"><span>Setup Request Services.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCMU</span></a></td>
<td><a href="#_Toc144362940"><span>Add protocols to GMRC protocol menus.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCNOTF</span></a></td>
<td><a href="#_Toc144362940"><span>Notification recipient utilities.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCP</span></a></td>
<td><a href="#_Toc144362940"><span>Message audit and status process.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCP5</span></a></td>
<td><a href="#_Toc144362940"><span>Print Consult form 513 (main entry).</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCP513</span></a></td>
<td><a href="#_Toc144362940"><span>Print Consult form 513.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCP5A</span></a></td>
<td><a href="#_Toc144362940"><span>Print Consult form 513 (Gather Data - TIU Results).</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCP5B</span></a></td>
<td><a href="#_Toc144362940"><span>Print Consult form 513 (Gather Data - Footers, Provisional Diagnosis and Reason For Request).</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCP5C</span></a></td>
<td><a href="#_Toc144362940"><span>Print Consult form 513 (Assemble Segments And Print).</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCP5D</span></a></td>
<td><a href="#_Toc144362940"><span>Print Consult form 513 (Gather Data - Addendums, Headers, Service reports and Comments).</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCPC</span></a></td>
<td><a href="#_Toc144362940"><span>List Manager Routine: Collect and display consults by service and status.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCPC1</span></a></td>
<td><a href="#_Toc144362940"><span>List Manager Routine: Collect and display consults by service and status.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCPH</span></a></td>
<td><a href="#_Toc144362940"><span>Process XQORM helps.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCPOR</span></a></td>
<td><a href="#_Toc144362940"><span>Get DOC,LOC,TS in interactive defaults.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCPOS</span></a></td>
<td><a href="#_Toc144362940"><span>Consult postinit file maintenance.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCPOS1</span></a></td>
<td><a href="#_Toc144362940"><span>Post init to move Services from file 123.5 to the orderable items file, 101.43, and orderables in file 101 to file 101.43.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCPOS2</span></a></td>
<td><a href="#_Toc144362940"><span>Consult postinit file maintenance.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCPOST</span></a></td>
<td><a href="#_Toc144362940"><span>Post init driver routine.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCPP</span></a></td>
<td><a href="#_Toc144362940"><span>Print GMRC consult/request tracking protocols - List Manager routine.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCPR</span></a></td>
<td><a href="#_Toc144362940"><span>GMRC List Manager Routine - Get information for abbreviated print of GMRC protocols and format for List Manager.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCPR0</span></a></td>
<td><a href="#_Toc144362940"><span>Data Entry Promptint actions.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCPREF</span></a></td>
<td><a href="#_Toc144362940"><span>Setup package/procedure protocols.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCPROT</span></a></td>
<td><a href="#_Toc144362940"><span>Consult postinit file maintenance.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCPRP</span></a></td>
<td><a href="#_Toc144362940"><span>Set protocol information into ^TMP global for print and display by List Manager.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCPRPS</span></a></td>
<td><a href="#_Toc144362940"><span>List Manager GMRC Routine -- List GMRC (Consults/Request) Protocols in abbreviated form.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCPS</span></a></td>
<td><a href="#_Toc144362940"><span>Select Service/specialty to send Consult to.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCPSL1</span></a></td>
<td><a href="#_Toc144362940"><span>Main entry point for reports search by provider, location, or procedure.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCPSL2</span></a></td>
<td><a href="#_Toc144362940"><span>Build ^TMP(“GMRCRPT) for GMRCPSL1.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCPSL3</span></a></td>
<td><a href="#_Toc144362940"><span>Generate reports using ^TMP(“GMRCRPT”).</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCPSL4</span></a></td>
<td><a href="#_Toc144362940"><span>Generate reports using ^TMP(“GMRCRPT”).</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCPSL1</span></a></td>
<td><a href="#_Toc144362940"><span>Special Consult reports.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCPSL2</span></a></td>
<td><a href="#_Toc144362940"><span>Special Consult reports.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCPSL3</span></a></td>
<td><a href="#_Toc144362940"><span>Special Consult reports.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCPSEL</span></a></td>
<td><a href="#_Toc144362940"><span>Select Range Of Items From List.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCPURG</span></a></td>
<td><a href="#_Toc144362940"><span>Purge orders from the Order File 100.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCPX</span></a></td>
<td><a href="#_Toc144362940"><span>Select a new pharmacy patient for list manager consult tracking display.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCPZ</span></a></td>
<td><a href="#_Toc144362940"><span>GMRC List Manager Routine -- Main menu actions for Pharmacy consults request tracking.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCQC</span></a></td>
<td><a href="#_Toc144362940"><span>GMRC List Manager routine to print Consults pending resolution for QC purposes.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCQCST</span></a></td>
<td><a href="#_Toc144362940"><span>Gather all consults for QC that do not have status of discontinued, complete, or expired.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCR</span></a></td>
<td><a href="#_Toc144362940"><span>Driver for reviewing patient consult/requests - Used by Medicine Package to link Consults to Medicine results.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCR0</span></a></td>
<td><a href="#_Toc144362940"><span>Add original consult via backdoor service.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCR06</span></a></td>
<td><a href="#_Toc144362940"><span>Complete a consult/request.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCRA</span></a></td>
<td><a href="#_Toc144362940"><span>Build ^TMP("GMRCR",$J, array of consults.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCREXT</span></a></td>
<td><a href="#_Toc144362940"><span>Clean-up all variables and ^TMP globals upon exit.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCRFIX</span></a></td>
<td><a href="#_Toc144362940"><span>Consult postinit save GMRCR protocol file links.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCRPOS</span></a></td>
<td><a href="#_Toc144362940"><span>Consult postinit save GMRCR protocol file links.2</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCS</span></a></td>
<td><a href="#_Toc144362940"><span>Review consults by Patient and Service.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCSL</span></a></td>
<td><a href="#_Toc144362940"><span>Active Consults by Service.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCSLDT</span></a></td>
<td><a href="#_Toc144362940"><span>Get a consults detailed tracking history formatted for List Manager.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCSLM</span></a></td>
<td><a href="#_Toc144362940"><span>List Mgr routine for consult tracking list.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCSLM1</span></a></td>
<td><a href="#_Toc144362940"><span>Gather data and format ^TMP global for consult tracking Silent call for use by List Manager and GUI.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCSLM2</span></a></td>
<td><a href="#_Toc144362940"><span>List Manager routine - Detailed consult display and printing.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCSLM3</span></a></td>
<td><a href="#_Toc144362940"><span>Extract medicine results for consult tracking.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCSLM4</span></a></td>
<td><a href="#_Toc144362940"><span>List Manager routine - Activity Log Detailed Display.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCSLMA</span></a></td>
<td><a href="#_Toc144362940"><span>List Manager protocol entry, exit actions.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCSLMU</span></a></td>
<td><a href="#_Toc144362940"><span>Utilities for displaying consults in List manager.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCSLMV</span></a></td>
<td><a href="#_Toc144362940"><span>Set Video attributes for list manager screens.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCSPD</span></a></td>
<td><a href="#_Toc144362940"><span>Change Date Range in CSLT Tracking Module.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCSRVS</span></a></td>
<td><a href="#_Toc144362940"><span>Add/Edit services in File 123.5.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCSSP</span></a></td>
<td><a href="#_Toc144362940"><span>List Manager Format Routine To Collect Pharmacy TPN Consults that are Not Completed Or Have Been Discontinued.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCST</span></a></td>
<td><a href="#_Toc144362940"><span>Statistics on how long to complete consult/requests for a service.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCST0</span></a></td>
<td><a href="#_Toc144362940"><span>Statistics on how long to complete consult/requests for a service.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCST00</span></a></td>
<td><a href="#_Toc144362940"><span>Statistics on how long to complete consult/requests for a service.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCSTAT</span></a></td>
<td><a href="#_Toc144362940"><span>List Manager Ancillary routine - Restrict display of consults to a given status or statuses on List Manager Screen.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCSTL1</span></a></td>
<td><a href="#_Toc144362940"><span>List Manager Format Routine - Get Active Consults by service - pending, active, scheduled, incomplete, etc.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCSTL2</span></a></td>
<td><a href="#_Toc144362940"><span>List Manager Format Routine - Get Active Consults by service - pending, active, scheduled, incomplete, etc.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCSTLM</span></a></td>
<td><a href="#_Toc144362940"><span>List Manager Format Routine - Get Active Consults by service - pending, active, scheduled, incomplete, etc.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCSTS</span></a></td>
<td><a href="#_Toc144362940"><span>Group update status of consult and order.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCSTS1</span></a></td>
<td><a href="#_Toc144362940"><span>Group update of consults cont'd.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCSTS2</span></a></td>
<td><a href="#_Toc144362940"><span>Change status based on result activity.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCSTSI</span></a></td>
<td><a href="#_Toc144362940"><span>Special processing to change status of selected consult and order</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCSTSU</span></a></td>
<td><a href="#_Toc144362940"><span>Change status based on current order status.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCSTSZ</span></a></td>
<td><a href="#_Toc144362940"><span>Loop "AE" and get entries, dump in ^TMP.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCSTU</span></a></td>
<td><a href="#_Toc144362940"><span>Statistic Utilities for Consult/Request Package.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCSTU1</span></a></td>
<td><a href="#_Toc144362940"><span>Statistic Utilities for Consult/Request Package.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCSUBS</span></a></td>
<td><a href="#_Toc144362940"><span>Routine to check if a Service has more than one patient service.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCSVCU</span></a></td>
<td><a href="#_Toc144362940"><span>Utility to put services from file 123.5 into file 101.43 when service exists in 123.5 but not.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCT</span></a></td>
<td><a href="#_Toc144362940"><span>Get DUZ's of users for notification to service.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCTIU</span></a></td>
<td><a href="#_Toc144362940"><span>TIU utilities for exchanging info with Consults.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCTIU1</span></a></td>
<td><a href="#_Toc144362940"><span>More CT/TIU interface modules.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCTIU2</span></a></td>
<td><a href="#_Toc144362940"><span>Enter TIU Browse with DFN and TIUDA.7</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCTIU3</span></a></td>
<td><a href="#_Toc144362940"><span>Extract medicine results for consults tracking.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCTIUA</span></a></td>
<td><a href="#_Toc144362940"><span>Add the TIU note to the results multiple.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCTIUE</span></a></td>
<td><a href="#_Toc144362940"><span>Complete/Update TIU notes.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCTIUL</span></a></td>
<td><a href="#_Toc144362940"><span>Get list of existing results for consults.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCTIUP</span></a></td>
<td><a href="#_Toc144362940"><span>TIU utilities for exchanging info with Consults.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCTU</span></a></td>
<td><a href="#_Toc144362940"><span>Consults - Terminated users/remove pointers.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCTU1</span></a></td>
<td><a href="#_Toc144362940"><span>Get DD Info.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCU</span></a></td>
<td><a href="#_Toc144362940"><span>Consult/Request Utilities.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCUTIL</span></a></td>
<td><a href="#_Toc144362940"><span>Utilities for formatting word processing fields and setting into ^TMP("GMRCR" globals for use by List Manager routines.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCUTL1</span></a></td>
<td><a href="#_Toc144362940"><span>General Utilities.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCUTL2</span></a></td>
<td><a href="#_Toc144362940"><span>Secondary Printer for printing SF 513</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCXQ</span></a></td>
<td><a href="#_Toc144362940"><span>Routine to allow follow-up on legacy alerts.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCYP15</span></a></td>
<td><a href="#_Toc144362940"><span>Convert procedures from 101 to 123.3</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCYP16</span></a></td>
<td><a href="#_Toc144362940"><span>PRE/POST INSTALL FOR GMRC*3*16.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCYP18</span></a></td>
<td><p><a href="#_Toc144362940"><span>Post Install for patch 18</span></a></p>
<p><a href="#_Toc144362940"><span>.</span></a></p></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCYP23</span></a></td>
<td><a href="#_Toc144362940"><span>Post Install for patch 23.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCYP7</span></a></td>
<td><a href="#_Toc144362940"><span>Consult clean-up unreleased at test sites.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCYP8</span></a></td>
<td><a href="#_Toc144362940"><span>Post Install for GMRC*3*8.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCCCRA</span></a></td>
<td><a href="#_Toc144362940"><span>Generates the appropriate HL7 messages when a community care consult is entered into the system. ( Modified by patches 99, 106 and 123)</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>POST^GMRCP99</span></a></td>
<td><a href="#_Toc144362940"><span>Used during the installation process to set up the appropriate HL7 application protocols and logical links. (Patch 99)</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCGUIB</span></a></td>
<td><a href="#_Toc144362940"><span>This existing routine is modified at the line tag CMT. A line of code was added to verify that a consult was created for community care; if so, it will trigger a new HL7 message to HSRM that includes the comment. (Patch 99)</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCACMT</span></a></td>
<td><a href="#_Toc144362940"><span>This existing routine is modified at the line tag COMMENT. A line of code was added to verify that a consult was created for community care; if so, it will trigger a new HL7 message to HSRM that will include the comment. (Patch 99)</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>GMRCCCR1</span></a></td>
<td><a href="#_Toc144362940"><span>This is a subroutine from GMRCCCRA created in Patch 106 and updated for patch 123. It also contains subroutines used by the GMRCCCRI routine.</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>GMRCCCRI</span></a></td>
<td><a href="#_Toc144362940"><span>This routine is used by VistA to parse and process the consult update received from HSRM. This routine is new in patch 123.</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>LINK^GMRC123P</span></a></td>
<td><a href="#_Toc144362940"><span>This is a pre-install routine used by patch 123. It checks to see if the CCRA-NAK logical link exists in the system. If not, it asks for the Health Connect Server IP Address and Port number, then creates the logical link in the VistA system. This link is required to receive consult updates from HSRM to VistA.</span></a></td>
</tr>
</tbody>
</table>

[[Refer to Table 20-7.](#_Toc144363047) [For systems that can use routine mapping, this is a list of routines in the Consults package that should be mapped.](#_Toc144362988)](#_Toc144362940)

[[<span id="_Toc169170420" class="anchor"></span>Table 20‑7: Routine Mapping](#_Toc144362988)](#_Toc144362940)

| [[Routine Prefix](#_Toc144363047)](#_Toc144362940) | [[Routine Usage](#_Toc144363047)](#_Toc144362940)                                   |
|----------------------------------------------------|-------------------------------------------------------------------------------------|
| [[GMRCA\*](#_Toc144363047)](#_Toc144362940)        | [[Action routines](#_Toc144363047)](#_Toc144362940)                                 |
| [[GMRCP\*](#_Toc144363047)](#_Toc144362940)        | [[CPRS interface routines](#_Toc144363047)](#_Toc144362940)                         |
| [[GMRCR\*](#_Toc144363047)](#_Toc144362940)        | [[Consults review/tracking routines](#_Toc144363047)](#_Toc144362940)               |
| [[GMRCS](#_Toc144363047)](#_Toc144362940)          | [[Service entry point to review/tracking routines](#_Toc144363047)](#_Toc144362940) |
| [[GMRCU\*](#_Toc144363047)](#_Toc144362940)        | [[Utility routines](#_Toc144363047)](#_Toc144362940)                                |
| [[GMRCXQ](#_Toc144363047)](#_Toc144362940)         | [[View Alerts follow-up](#_Toc144363047)](#_Toc144362940)                           |
| [[GMRCD\*](#_Toc144363047)](#_Toc144362940)        | [[Decision Support Tool Utilities](#_Toc144363047)](#_Toc144362940)                 |

- 
- 

[[An asterisk (\*) denotes a wild card specification. Any routines beginning with the characters before the asterisks are included in the set.The other routines do not need to be mapped due to their smaller frequency of usage.](#_Toc144363047)](#_Toc144362940)

[[  
](#_Toc144363049)](#_Toc144362940)

[[Refer to Table 22-1.](#_Toc144363051)](#_Toc144362940)

[[<span id="_Toc169170421" class="anchor"></span>Table 22‑1: Facility Error Notifications](#_Toc144363051)](#_Toc144362940)

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 39%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr class="header">
<th><a href="#_Toc144362940"><span>Error Number</span></a></th>
<th><a href="#_Toc144362940"><span>Description</span></a></th>
<th><a href="#_Toc144362940"><span>Notification Group</span></a></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><a href="#_Toc144362940"><span>101</span></a></td>
<td><a href="#_Toc144362940"><span>Unknown Consult or Procedure request number</span></a></td>
<td><a href="#_Toc144362940"><span>GMRC CRNR IFC ERRORS</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>301</span></a></td>
<td><a href="#_Toc144362940"><span>Sending facility not registered at consulting facility for the requested Service</span></a></td>
<td><a href="#_Toc144362940"><span>GMRC CRNR IFC ERRORS,<br />
GMRC CRNR IFC CLIN ERRORS<br />
GMRC TIER II CRNR IFC ERRORS,</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>401</span></a></td>
<td><a href="#_Toc144362940"><span>Sending facility not registered at consulting facility for the requested Procedure</span></a></td>
<td><a href="#_Toc144362940"><span>GMRC CRNR IFC ERRORS,<br />
GMRC CRNR IFC CLIN ERRORS,<br />
GMRC TIER II CRNR IFC ERRORS</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>501</span></a></td>
<td><a href="#_Toc144362940"><span>Error in the Procedure name (Procedure name not found at consulting facility)</span></a></td>
<td><a href="#_Toc144362940"><span>GMRC CRNR IFC ERRORS, GMRC CRNR IFC CLIN ERRORS, GMRC TIER II CRNR IFC ERRORS</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>601</span></a></td>
<td><a href="#_Toc144362940"><span>Multiple services attached to a Procedure</span></a></td>
<td><p><a href="#_Toc144362940"><span>GMRC CRNR IFC ERRORS,<br />
GMRC CRNR IFC CLIN ERRORS,</span></a></p>
<p><a href="#_Toc144362940"><span>GMRC TIER II CRNR IFC ERRORS</span></a></p></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>701</span></a></td>
<td><a href="#_Toc144362940"><span>Error in service name (Service name not found at consulting facility)</span></a></td>
<td><a href="#_Toc144362940"><span>GMRC CRNR IFC ERRORS,<br />
GMRC CRNR IFC CLIN ERRORS,<br />
GMRC TIER II CRNR IFC ERRORS</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>702</span></a></td>
<td><a href="#_Toc144362940"><span>Service is disabled at Consulting Site</span></a></td>
<td><a href="#_Toc144362940"><span>GMRC CRNR IFC ERRORS,<br />
GMRC CRNR IFC CLIN ERRORS,<br />
GMRC TIER II CRNR IFC ERRORS</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>703</span></a></td>
<td><a href="#_Toc144362940"><span>Procedure is Inactivated at Consulting Site</span></a></td>
<td><a href="#_Toc144362940"><span>GMRC CRNR IFC ERRORS,<br />
GMRC CRNR IFC CLIN ERRORS,<br />
GMRC TIER II CRNR IFC ERRORS</span></a></td>
</tr>
<tr class="odd">
<td><a href="#_Toc144362940"><span>801</span></a></td>
<td><a href="#_Toc144362940"><span>Consult records at the two facilities may be out of synch with regards to status</span></a></td>
<td><a href="#_Toc144362940"><span>GMRC CRNR IFC ERRORS,<br />
GMRC CRNR IFC TECH ERRORS,<br />
GMRC TIER II CRNR IFC ERRORS,</span></a></td>
</tr>
<tr class="even">
<td><a href="#_Toc144362940"><span>802</span></a></td>
<td><a href="#_Toc144362940"><span>The activity or the consult request in question has been transmitted to the remote site multiple times and is already on file.</span></a></td>
<td><a href="#_Toc144362940"><span>GMRC CRNR IFC ERRORS,<br />
GMRC TIER II CRNR IFC ERRORS</span></a></td>
</tr>
</tbody>
</table>