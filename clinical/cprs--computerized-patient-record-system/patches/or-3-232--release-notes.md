---
title: OR*3*232 Remote Data Interoperability Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: Remote Data Interoperability
app_code: CPRS
app_name: Computerized Patient Record System
section: CLI
app_status: archive
pkg_ns: OR
patch_ver: 3
patch_id: OR*3*232
group_key: "CPRS:OR:3"
file_numbers: []
security_keys: []
menu_options: 0
description: The most recent entries in this list are linked to the location in the manual they describe. Click on a link or page number to go to that section.
audience: 
keywords: 
  - order
  - mark
  - cprs
  - class
  - drug
  - checks
  - span
  - remote
  - redacted
  - patch
page_count: 0
word_count: 2246
section_count: 0
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: April 2007
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)_Archive/or_3_232rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)_Archive/or_3_232rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=338"
---

![](or-3-232-remote-data-interoperability-release-notes/001.png)

Remote Data Interoperability (OR\*3.0\*232) Release Notes

April 2007

Health Data Systems

Computerized Patient Record System Product Line

<span id="_Toc107371093" class="anchor"></span>Revision History

The most recent entries in this list are linked to the location in the manual they describe. Click on a link or page number to go to that section.

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 14%" />
<col style="width: 10%" />
<col style="width: 26%" />
<col style="width: 18%" />
<col style="width: 18%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Date</strong></td>
<td><strong>Patches</strong></td>
<td><strong>Page</strong></td>
<td><strong>Change</strong></td>
<td><strong>Project Manager</strong></td>
<td><strong>Technical Writer</strong></td>
</tr>
<tr class="even">
<td>4/4/07</td>
<td>OR*3.0*232</td>
<td>4-8</td>
<td><blockquote>
<p>Added revisions from reviewers.</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>3/29/07</td>
<td>OR*3.0*232</td>
<td>4-8</td>
<td><blockquote>
<p>Added revisions from reviewers.</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>3/15/07</td>
<td>OR*3.0*232</td>
<td></td>
<td><blockquote>
<p>Added the information about the known issues affecting RDI.</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>7/7/06</td>
<td>OR*3.0*232</td>
<td>4-6</td>
<td><blockquote>
<p>Added information regarding the OR RDI PARAMS menu and the related parameters.</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>6/9/06</td>
<td>OR*3.0*232</td>
<td>4-6</td>
<td><blockquote>
<p>Inserting references to DoD data.</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>3/8/06</td>
<td>OR*3.0*232</td>
<td>4-6</td>
<td><blockquote>
<p>Revisions from team members, removing references to DoD data and active dual consumers.</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td>1/19/06</td>
<td>OR*3.0*232</td>
<td>4-5</td>
<td><blockquote>
<p>Revisions from team members</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>9/1/05</td>
<td>OR*3.0*232</td>
<td></td>
<td><blockquote>
<p>Initial version</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

<span id="_Toc162932984" class="anchor"></span>Table of Contents

<span id="_Toc162932985" class="anchor"></span>Introduction

The Remote Data Interoperability (RDI) project provides order checking using a patient’s local clinical data and data stored in the Health Data Repository (HDR). The HDR stores data from all VA Medical Centers, and when the Clinical Health Data Repository (CHDR) project is active, any participating Department of Defense (DoD) sites that share active patients (known as Active Dual Consumers or ADC) with VA sites. When the user is placing orders, the order checks will use local data and HDR data (outpatient medication and allergy data) to determine if any orders are contraindicated based on clinical data originating at any other site.

Four packages are involved in this project and each package has a patch for RDI changes:

- Computerized Patient Record System (CPRS) patch OR\*3\*232
- Inpatient Medications patch PSJ\*5.0\*146
- Outpatient Pharmacy patch PSO\*7.0\*207
- Adverse Reaction Tracking System (ARTS) patch GMRA\*4.0\*26

This document deals mainly with the CPRS changes in patch OR\*3.0\*232. However, another patch, OR\*3.0\*238, is also required to enable RDI. The changes in patch OR\*3.0\*232 will not be apparent to users until patch OR\*3.0\*238 is installed on their systems. OR\*3.0\*238 introduces a new option that enables access to HDR data.

<span id="_Toc162932986" class="anchor"></span>OR\*3.0\*232 Required Patches

- GMRA\*4.0\*26
- HL\*1.6\*133
- OR\*3.0\*195

<span id="_Toc162932987" class="anchor"></span>OR\*3.0\*232 Related Patch

- RA\*5.0\*72

In order for patients with contrast media allergies to be registered successfully in the Radiology application, patch RA\*5.0\*72 must be installed.

<span id="_Toc162932988" class="anchor"></span>OR\*3.0\*238 Required Patch

- OR\*3.0\*232

<span id="_Toc162932989" class="anchor"></span>Changes in OR\*3.0\*232

Patch OR\*3\*232 contains the CPRS changes that enable drug-drug, drug-drug class, duplicate drug, drug-allergy, and contrast media allergy order checks using data sent from VA sites and eventually from participating DoD sites that is stored in the Health Data Repository (HDR) or Health Data Repository Interim Messaging Solution (HDR-IMS), which will be the database used until the complete HDR is ready. With regard to RDI, this document will use the term HDR for both the complete HDR and HDR-IMS. The HDR will include only standardized data domains as created by the Data Standardization initiative. At this time, the standardized domains include allergies, outpatient medications, and vital signs.

RDI uses the same order checks that CPRS users are familiar with and adds the benefit of doing those checks against remote outpatient medication and remote allergy data stored in the HDR. It then displays any order checks to CPRS users in the order check screen with which they are familiar.

<span id="_Toc162932990" class="anchor"></span>When Will RDI Be Enabled?

Whether the RDI features are enabled depends on the value of the parameter OR RDI HAVE HDR. With patch OR\*3.0\*232, the value is NO. The menu option to change this parameter will be available in patch OR\*3.0\*238. Until then, the remote order checking features of RDI will be dormant.

> **NOTE:** Sites should not enable the OR RDI HAVE HDR parameter until they receive official instructions.

<span id="_Toc162932991" class="anchor"></span>How Does RDI Work?

When an order check is needed either because a CPRS user is writing orders or because CPRS receives a request from Outpatient Pharmacy, CPRS sends a request to Clinical Data Service (CDS) for outpatient medication and allergy information.

The request includes the following data, not necessarily in this order:

- patient internal control number (ICN) or national identifier
- dates (t-30 for outpatient medications with an expired or discontinued status, plus all other statuses—all allergies are returned)
- domain (such as outpatient medications)

What Happens when Data Does Come from the HDR?

If CPRS does receive the data from CDS, CPRS stores the data for the amount of time specified in a parameter; the default is 120 minutes, but sites can change this value. CPRS does not request data from CDS again during the order session unless more than the specified time has elapsed. So if the default is 120 minutes and only 55 minutes have passed, the stored (cached) data will be used for the order checks, but if 130 minutes have elapsed since the data was stored, CPRS will request the data again.

Order checks from CPRS can happen several times during a CPRS session:

- Beginning to write/copy/change orders – When a user selects an order menu to begin writing orders, CPRS requests some order checks, such as polypharmacy, renal function, or creatinine clearance, for example.
- On order acceptance – When the user selects Accept, CPRS requests the order checks.
- Signature of orders – When a user signs the order, CPRS requests order checks.

Outpatient Pharmacy and Adverse Reaction Tracking process the information CPRS provides and sends all drug-drug, drug-drug class, duplicate drug, drug-allergy, and contrast media allergy order checks back to CPRS for display to the user. For drug-drug and drug-drug class interactions, the message CPRS displays also shows the last refill date, quantity dispensed, and the facility name where the medication was prescribed; allergy information and information about local order checks do not include the facility name, but do indicate whether the allergy is from a local or remote location. The facility information is provided as a convenience to the user.

With RDI, when a user writes an inpatient, outpatient, or Non-VA medication order, an order check against remote outpatient medications is done. The order check is done against all active outpatient medications and all outpatient medications that expired or were discontinued less than 30 days in the past. If the user records that the patient is taking a Non-VA medication, the order check will happen against remote outpatient medication data. However, neither Non-VA medications nor inpatient medications on other systems (remote Non-VA medications nor remote inpatient medications) can be used for order checking because they are not in the HDR.

What If CPRS Receives No Data from the HDR?

If CPRS does not receive a response from the HDR within the amount of time specified in the logical link ORHDR, the order checks will be done against local data only. In this case, CPRS displays a “local data only” message at the bottom of the order check screen once during the ordering session (so it will appear once for each patient if there is a problem receiving HDR data) to inform the user that order checks are using only local data. However, in the background, CPRS continues to attempt to communicate with the HDR (by pinging). When communication with the HDR is reestablished, users will begin to see remote order checks again.

> **NOTE:** A national announcement (“Automated Notification Report” or ANR) is sent out when problems with the HDR might be occurring or when scheduled maintenance will occur that would create situations when the HDR will not be available. Someone at your site should monitor ANR messages so that your site will be aware of these outages and can prepare for them or alert staff as needed.

There are several reasons why CPRS might not receive data from the HDR:

- The HDR could not be reached – The HDR is a new database that stores a great deal of data about VHA patients. Because it is new as is much of the hardware and software that supports it, the HDR may experience some problems. There are many pieces to the communication that takes place between the HDR and a local site, both software and hardware, including Clinical Data Service (CDS) and the database itself, just to name a few; failure of any piece may disrupt communication with the HDR, which might cause a site to see the “local data only” message.
- The site may experience local area network (LAN) or wide area network (WAN) connectivity problems – In addition to the HDR software and hardware, each site has a LAN and connections to the WAN that could be having problems. This might also cause a site to see the “local data only” message.
- The patient may not have a national identifier – Each patient should have a unique number (called an ICN) that identifies the patient nationally. This number is used by the Master Patient Index (MPI), Remote Data Views (RDV), VistaWeb, and other applications. If a patient does not have an ICN, CPRS displays the “local data only” message. In addition, none of the applications mentioned can get data for the patient from other sites, including from the HDR.

<span id="_Toc162932992" class="anchor"></span>RDI Known Issues

Sites should be aware of the following two RDI known issues:

- Known Issue \# 1 – No Mechanism to Report that RDI Is Turned Off: Test sites requested that RDI include a mechanism to inform the local IRM Service if the RDI parameter (OR RDI HAVE HDR) is turned off. Test sites agreed that a VistA email be triggered to a mail group if the parameter is set to OFF at any time after installation. This parameter should be checked for status on a daily basis. It was felt by everyone that daily checks should be sufficient.

Impact: Without this functionality, the risk is that RDI communication to the HDR might be turned off without the local site realizing that order checks are not being done against remote data stored in the HDR.

Workarounds: Local sites can manually check the status of the parameter OR RDI HAVE HDR to be sure it is set to Yes (turned on).

Resolution: This will be included in a subsequent release.

- Known Issue \# 2 – Medication Not Matched to National Drug File: The HDR-Hx and HDR-IMS contain prescriptions with drugs that are not matched to the National Drug File (NDF). This prescription data should be used in remote order checking for duplicate drug classes. This can be accomplished by sending VA DRUG CLASS file (#50.605) VUID to the HDR-IMS and having it returned by CDS from both the HDR-Hx and HDR-IMS.

Impact: Order checks from remote data stored in the HDR may be incomplete. The provider may assume that s/he is receiving all the order checks when in actuality they may not get all medication order checks if the drug has not been matched to the National Drug File. Some drugs are never matched to the NDF so the only way to use them in order checks is if the match is made at the drug ingredient level.

Workarounds: None recommended.

Resolution: Because the National Drug File is updated regularly, these missing order checks could be resolved whenever the NDF is updated. Some drugs may never be matched, especially drugs used in research.

<span id="_Toc162932993" class="anchor"></span>Changes in OR\*3.0\*238

Patch OR\*3.0\*238 activates the menu OR RDI PARAMS. This menu sets two parameters:

- OR RDI HAVE HDR – This parameter defines whether CPRS should query the HDR for remote allergy and Outpatient Pharmacy data. The default is NO, but this parameter is set to YES when patch OR\*3.0\*238 is installed.
- OR RDI CACHE TIME – This parameter defines how long (the number of minutes) CPRS should locally store the remote allergy and Outpatient Pharmacy data to be used for order checks. The default is 120 minutes, but can be from 0 to 9999 minutes. A setting of 0 (zero) means that data will be requested every time an order check is needed, which would increase WAN traffic significantly. If the data is older than the time set in this parameter, CPRS will request the data from the HDR again when one of the triggers described above occurs, such as an order being accepted.

> **NOTE:** To edit the values of these parameters, users must use the OR RDI PARAMS menu. Users will not be able to use the general parameter editing menu options, such as XPAR EDIT.