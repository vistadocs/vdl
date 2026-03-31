---
title: PIMS Version 5.3 ADT Technical Manual
doc_type: TM
doc_label: Technical Manual
doc_layer: anchor
doc_subject: 
app_code: ADT
app_name: Admission Discharge Transfer
section: CLI
app_status: archive
pkg_ns: ADT
patch_ver: 5.3
patch_id: ADT*5.3
group_key: "ADT:ADT:5.3"
file_numbers: 
  - 33
  - 47
  - 409
security_keys: []
menu_options: 7
description: This section defines the HL7 message transactions that are necessary to support the outpatient database interface for the Austin Information Technology Center (AITC), (formerly the Austin Automation Center \[AAC\]).
audience: 
keywords: 
  - strong
  - table
  - class
  - patient
  - contents
  - patch
  - span
  - routines
  - even
  - date
page_count: 0
word_count: 66011
section_count: 106
table_count: 87
figure_count: 0
appendix_count: 3
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Admis_Disch_Transfer_(ADT)_Archive/adt_pims_tm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Admis_Disch_Transfer_(ADT)_Archive/adt_pims_tm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=327"
---

Patient Information Management System (PIMS) Software Version 5.3Patient Registration and Admission, Discharge, Transfer (ADT)Technical Manual

![](pims-version-5-3-adt-technical-manual/001.png)

April 2025Department of Veterans Affairs (VA)Office of Information and Technology (OIT)Enterprise Program Management Office (EPMO)

<span id="_Toc193957680" class="anchor"></span>Revision History

<table>
<caption><p><span id="_Ref53997970" class="anchor"></span>Table 1: Reference Materials Table</p></caption>
<colgroup>
<col style="width: 13%" />
<col style="width: 12%" />
<col style="width: 46%" />
<col style="width: 27%" />
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
<td>4/2025</td>
<td>0.83</td>
<td>DG*5.3*1127 – Added modified routines to Patch DG*5.3*1127 Routines</td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="even">
<td>11/2024</td>
<td>0.82</td>
<td><p>Removed Appointment Scheduling information from this manual and applied updated template.</p>
<p>Appointment Scheduling information is now avalable in a separate document: SD_PIMS_TM</p></td>
<td>GovernmentCIO<br />
Booz Allen Hamilton</td>
</tr>
<tr class="odd">
<td>11/2024</td>
<td>0.81</td>
<td>DG*5.3*1096 – Added new routine to Patch DG*5.3*1096 Routines</td>
<td>IAM</td>
</tr>
<tr class="even">
<td>11/2024</td>
<td>0.80</td>
<td>DG*5.3*1091 – Added modified routines to Patch DG*5.3*1091 Routines</td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="odd">
<td>10/2024</td>
<td>0.79</td>
<td><p>DG*5.3*1104 – Added new and modified routines Patch DG*5.3*1104 Routines</p>
<ul>
<li><p>Updated 4.1 with ^DGCOMP global</p></li>
<li><p>Updated 4.2 with the new File #33.3</p></li>
</ul></td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="even">
<td>10/2024</td>
<td>0.78</td>
<td><p>DG*5.3*1121 – Added new and modified routines Patch DG*5.3*1121 Routines</p>
<p>Added VASV(16) for PERSIAN GULF INDICATOR and VASV(17) for PERSIAN GULF INDICATOR LAST CHANGE DATE in SVC^VADPT Section</p></td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="odd">
<td>6/2024</td>
<td>0.77</td>
<td><p>DG*5.3*1118 – Added new and modified routines Patch DG*5.3*1118 Routines</p>
<p>Updated VASV(15) for TOXIC EXPOSURE RISK ACTIVITY in SVC^VADPT Section</p></td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="even">
<td>6/2024</td>
<td>0.76</td>
<td><p>DG*5.3*1120 – Added VAS Alerts Section</p>
<p>Add modified routines to Patch DG*5.3*1120 Routines</p></td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="odd">
<td>4/2024</td>
<td>0.75</td>
<td>DG*5.3*1111 – Added new and modified routines Patch DG*5.3*1111</td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="even">
<td>4/2024</td>
<td>0.74</td>
<td>DG*5.3*1107 – Added new and modified routines Patch DG*5.3*1107 Routines</td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="odd">
<td>1/2024</td>
<td>0.73</td>
<td>DG*5.3*1109 – Added new and modified routines</td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="even">
<td>12/2023</td>
<td>0.72</td>
<td>DG*5.3*1095 – Added new and modified routines Patch DG*5.3*1095 Description and Routines</td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="odd">
<td>12/2023</td>
<td>0.71</td>
<td>DG*5.3*1103 – Added new and modified routines Patch DG*5.3*1103 Routines; Updated the following sections to include TERA: SVC^VADPT, Alpha Subscripts, ZEL—VA-Specific Patient Eligibility Segment, and Table SD008—Outpatient Classification Type.</td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="even">
<td>10/2023</td>
<td>0.70</td>
<td>DG*5.3*1098 – Added new and modified routines Patch DG*5.3*1098 Routines; Added new value 29 for WORLD WAR II to Table VA04—Eligibility</td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="odd">
<td>7/2023</td>
<td>0.69</td>
<td>DG*5.3*1093 – Added new and modified routines Patch DG*5.3*1093 Routines; Updated Table VA08—Religion and Table 0006—Religion with new value for entry 28 and additional entries 84 – 89</td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="even">
<td>4/2023</td>
<td>0.68</td>
<td>DG*5.3*1090 – Added new and modified routines Patch DG*5.3*1090 Routines</td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="odd">
<td>2/2023</td>
<td>0.67</td>
<td>DG*5.3*964 - Added new and modified routines to Patch DG*5.3*964 Routines, new Namespace Conventions to Section 1.1, new files to File List in Section 4.2, and VistA Audit Solution (VAS) has been added</td>
<td>GovernmentCIO/Booz Allen Hamilton</td>
</tr>
<tr class="even">
<td>12/2022</td>
<td>0.66</td>
<td><p>DG*5.3*1082 – Patch DG*5.3*1082 Routines: Updates DATA GROUP [3] – POS, Eligibility Code(s), modifies three VHAPs; adds entries in MAS ELIGIBILITY CODE (#8.1) and ELIGIBILITY CODE (#8) files; modifies the PRESUMPTIVE PSYCHOSIS CATEGORY (#.5601) field in the PATIENT (#2) and CATEGORY CHANGES (#33.12) file and subfile; adds a new PRESUMPTIVE PSYCHOSIS HISTORY (#33.2) file; modifies ELIGIBILITY STATUS DATA, SCREEN &lt;7&gt; screen DATA GROUP [3]; modifies template DG LOAD EDIT SCREEN 7 (#420) in the INPUT TEMPLATE (#.402); post install routine will send HL7/Z07 message to VES; Patch IVM*2.0*208: HL7 ORU/ORF-Z11 PROCESSING.</p>
<p>Added Value 28 PRESUMPTIVE PSYCHOSIS HISTORY to Table VA04—Eligibility</p></td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="odd">
<td>09/2022</td>
<td>0.65</td>
<td><p>DG*5.3*1081 – Added Patch DG*5.3*1081 Routines: Updates Data Group 1 on INELIGIBLE/MISSING DATA SCREEN &lt;10&gt;; modifies VHAPs and adds CLINICAL EVALUATION entry in HEALTH BENEFITS PLAN file; adds CLINICAL EVALUATION code to VistA MAS ELIGIBILITY CODE and ELIGIBILITY CODE files; updates INEL REASON UNSPECIFIED entry in INCONSISTENT DATA ELEMENTS file; sets to UNEDITABLE and updates LONG DESCRIPTION of 6 fields in PATIENT file; updates LONG DESCRIPTION field for 3 entries in the HEALTH BENEFIT PLAN file; exports modified routines DGRP10, DGRPV, DGRPC, DG531081P and DGLOCK1.</p>
<p>Added note to Section ELIG^VADPT to indicate values that will be obsolete after patch DG*5.3*1081 is installed.</p>
<p>Updated Table VA04 – Eligibility to include new value 27 CLINICAL EVALUATION.</p></td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="even">
<td>08/2022</td>
<td>0.64</td>
<td><p>DG*5.3*1064 – Added Patch DG*5.3*1064 Routines: Added Group 6 with prompts; modified ICR #10061 and #7109 for VADPT to include new entries in DEM and DEMUPD components; added six fields to the PATIENT (#2) file; updated VistA to receive patient Indian attestation information from ES in the ZPD segment of the HL7 ORU/ORF~Z11 message; exported modified routines DGENELA2, DGENPTA1, DGENUPLA, DGMTSC4, DGMTSC4V, DGMTSCC, DGMTSCR, DGRP2, DGRPD, DGRPDB, DGRPE, DGRPH, DGRPV, VADPT0, VADPT1 and VAFHLZPD.</p>
<p>Updated Callable Entry Points in VADPT with guidance for format of data in return array, updated DEM^VADPT and DEMUPD^VADPT with new entries for INDIAN SELF IDENTIFICATION, INDIAN START DATE, INDIAN ATTESTATION DATE and INDIAN END DATE and added VADEM(15) and VADMO(15), which are set to null to avoid issues with groups that are only looking for root nodes.</p></td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="odd">
<td>07/2022</td>
<td>0.63</td>
<td><p>DG*5.3*1075 – Added Patch DG*5.3*1075 Routines:</p>
<ul>
<li><p>Added Pre/Post install routine DG531075P</p></li>
<li><p>Modified routines DGLOCK1, DGREG.INT, DGRP3.INT, DGRP6EF.INT, DGRP7.INT, DGRP7CP.INT, DGRPCE.INT, DGRPCE1.INT</p></li>
</ul>
<p>Updated Table VA04—Eligibility to include COMPACT ACT ELIGIBLE, SPECIAL TX AUTHORITY CARE and HUD-VASH</p>
<p>Corrected Table VA0022—Radiation Exposure Method to include H/N AND ATMOSPHERIC TESTING, UNDERGROUND NUCLEAR TESTING, EXPOSURE AT NUCLEAR FACILITY, and OTHER</p></td>
<td>Booz Allen Hamilton</td>
</tr>
<tr class="even">
<td>06/2022</td>
<td>0.62</td>
<td>DG*5.3*1071 – added modified routines to Patch DG*5.3*1071 Routines and DEM^VADPT and DEMUPD^VADPT updated #14 Sexual Orientation with Status, Date Created, Date Last Updated and Note.</td>
<td>VA MPI Team</td>
</tr>
<tr class="odd">
<td>02/2022</td>
<td>0.61</td>
<td><p>DG*5.3*1067 – Added Patch DG*5.3*1067 Routines:</p>
<ul>
<li><p>Added new PATIENT CONTACT RELATION file (12.11); added five new fields to the PATIENT file (#2) that contain pointers to the new PATIENT CONTACT RELATION file (#12.11); exported modified routines: DG531067P, DGDDC, DGDDDTTM, DGREG, DGRP3, DGRPD1, DGRPE, DGRRPSKN, VADPT1, and VAFHLZCT.</p></li>
<li><p>Patch IVM*2.0*204, included in the Host File for this build, contains a pre-install routine, PRE^IVM20204P, which deletes entries from the IVM DEMOGRAPHIC UPLOAD FIELDS file (#301.92) for the Next of Kin processing.</p></li>
</ul>
<p>Updated Table File List to include PATIENT CONTACT RELATION file (#12.11).</p>
<p>Updated Modified ICR #10061 in the OAD^VADPT tag for the addition of RELATIONSHIP TYPE fields in the output array and new node in the array for the relocation of the RELATIONSHIP TO PATIENT fields.</p></td>
<td>Liberty ITS</td>
</tr>
<tr class="even">
<td>11/2021</td>
<td>0.60</td>
<td>DG*5.3*1059 – added modified routines to Patch DG*5.3*1059 Section and section Files: SEXUAL ORIENTIATION TYPES file #47.77, PRONOUN TYPES file #47.78, DEM^VADPT and DEMUPD^VADPT updates #13 was missing from documentation, #14 added with patch for Sexual Orientation, Sexual Orientation Description, Pronoun, Pronoun Description, Self-Identified Gender</td>
<td>VA MPI Team</td>
</tr>
<tr class="odd">
<td>11/2021</td>
<td>0.59</td>
<td>DG*5.3*1065 – Added modified routine DGUAMWS to Patch DG*5.3*1065 Routines.</td>
<td>Liberty ITS</td>
</tr>
<tr class="even">
<td>10/2021</td>
<td>0.58</td>
<td><p>DG*5.3*1061 Updates:</p>
<p>Added Patch DG*5.3*1061 Routines: Modified ICR #10061 for VADPT with new component “CAI” for downstream applications to retrieve the COMPACT Act Indicator. Modified routines DGENELA, DGLOCK1, DGRP7, DGRPD, and VADPT. Also added DG531061P, which added entries into ELIGIBILITY CODE file (#8).</p>
<p>Added CAI^VADPT, new callable entry point in VADPT for COMPACT Act eligibility determination.</p></td>
<td>Liberty ITS</td>
</tr>
<tr class="odd">
<td>09/2021</td>
<td>0.57</td>
<td><p>DG*5.3*1056 Updates:</p>
<p>Changed “patient’s permanent address” to “patient’s mailing address” and changed “permanent mailing address” to “mailing address” where this address is referenced.</p>
<p>Added Patch DG*5.3*1056 Routines.</p></td>
<td>Liberty ITS</td>
</tr>
<tr class="even">
<td>09/2021</td>
<td>0.56</td>
<td>DG*5.3*1045 – Added modified routines DGENUPL7, DGEN, DGENA1A, DGENA6, DGREG, DCRPC, and DGENA2 to Patch DG*5.3*1045 Routines</td>
<td>Liberty ITS</td>
</tr>
<tr class="odd">
<td>08/2021</td>
<td>0.55</td>
<td>DG*5.3*1047 – Added new and modified routines to Patch DG*5.3*1047 Routines</td>
<td>Liberty ITS</td>
</tr>
<tr class="even">
<td>06/2021</td>
<td>0.54</td>
<td><p>DG*5.3*1044 Updates:</p>
<p>Changed “AIR FORCE – ACTIVE DUTY” to “USAF, USSF – ACTIVE DUTY” in Table VA11—Period of Service</p>
<p>Added Patch DG*5.3*1044 Routines: Modified routines DGRPMS, DGRPE, DGRP61 and added post-install routine DG531044P to re-compile templates.</p></td>
<td>Liberty ITS</td>
</tr>
<tr class="odd">
<td>06/2021</td>
<td>0.53</td>
<td><p>DG*5.3*1027 Updates:</p>
<p>Added new and modified routines to Patch DG*5.3*1027 Routines</p>
<p>Modified “ENROLLMENT APPLICATION DATE” to “APPLICATION DATE” in Table 45</p></td>
<td>Liberty ITS</td>
</tr>
<tr class="even">
<td>06/2021</td>
<td>0.52</td>
<td>DG*5.3*1035 – Added new and modified routines to Patch DG*5.3*1035 Routines</td>
<td>Liberty ITS</td>
</tr>
<tr class="odd">
<td>04/2021</td>
<td>0.51</td>
<td>DG*5.3*1034 – Added new and modified routines to Patch DG*5.3*1034 Routines</td>
<td>Liberty ITS</td>
</tr>
<tr class="even">
<td>04/2021</td>
<td>0.50</td>
<td><p>DG*5.3*1018 Updates:</p>
<ul>
<li><p>Added BLUE WATER NAVY to Table VA0046 – Agent Orange Exposure Location.</p></li>
</ul>
<p>Added missing updates related to patch DG*5.3*993:</p>
<ul>
<li><p>Added PATIENT REGISTRATION ONLY REASON to File List</p></li>
</ul>
<p>Added Table VA0047 – PATIENT REGISTRATION ONLY REASON</p></td>
<td>Liberty ITS</td>
</tr>
<tr class="odd">
<td>03/2021</td>
<td>0.49</td>
<td>DG*5.3*1029 – Added new and modified routines to<br />
Patch DG*5.3*1029 Routines</td>
<td>Liberty ITS</td>
</tr>
<tr class="even">
<td>02/2021</td>
<td>0.48</td>
<td><p>Added missing patch entries:</p>
<p>DG*5.3*1025 – Added new and modified routines to Patch DG*5.3*1025 Routines</p>
<p>DG*5.3*1016 – Added new and modified routines to Patch DG*5.3*1016 Routines</p>
<p>DG*5.3*977 – Added new and modified routines to Patch DG*5.3*977 Routines</p>
<p>DG*5.3*952 – Added new and modified routines to Patch DG*5.3*952 Routines</p></td>
<td>Liberty ITS</td>
</tr>
<tr class="odd">
<td>02/2021</td>
<td>0.47</td>
<td><p>DG*5.3*1046 Updates:</p>
<p>Merged duplicate copies of this manual into a single file to serve as a baseline for updates to the document moving forward.</p></td>
<td>Liberty ITS</td>
</tr>
<tr class="even">
<td>12/2020</td>
<td>0.46</td>
<td><p>DG*5.3*1014 Updates:</p>
<ul>
<li><p>Added new routines VAFHLZCE, DGRP1152A, DGRP1152U; DGADDVAL, DGADDLST, and DGUAMWS and modified routines IVMPTRN8, DGENUPL1, DGENUPLB, DGENUPL7, DGRPH, DGDEP, DGDEPE, DGR111, DGR113, DGR1131, DGR114, DGRP1, DGRP11B, DGRP2, DGRP6, DGRP61, DGRP62, DGRPCF, DGRPU, DPTLK, DGRP6EF, DGRP6CL, DGREGAED, DGREGRED, and DGREDTED to Patch DG*5.3*1014 Routines.</p></li>
</ul>
<p>Added HWSC Configuration.</p></td>
<td>Liberty ITS</td>
</tr>
<tr class="odd">
<td>12/2020</td>
<td>0.45</td>
<td><p>Updates: Merged missing content from the PIMS Technical Manual (i.e., PIMS_Technical_Manual.docx/.pdf) into this manual (i.e., adt_pims_tm.docx/.pdf) so there will only be one PIMS Technical Manual going forward:</p>
<ul>
<li><p>Changed references from VistA Scheduling Enhancement (VSE) to VistA Scheduling Graphical User Interface (VS GUI) throughout.</p></li>
<li><p>Added (missing) File #409.88 entry to Tables.</p></li>
</ul></td>
<td>VDIF Development Team</td>
</tr>
<tr class="even">
<td>12/2020</td>
<td>0.44</td>
<td><p>Updates:</p>
<ul>
<li><p>Merged two divergent versions of this same document back into a single document to keep all edits/changes in sync.</p></li>
<li><p>Updated entire document to follow current documentation standards and style guidelines.</p></li>
<li><p>Updated all styles and formatting throughout.</p></li>
<li><p>Corrected document to be Section 508 conformant.</p></li>
<li><p>Updated organizational references and acronyms.</p></li>
<li><p>Renamed this document to match current naming conventions: adt_pims_tm.docx/.pdf. This is the <em>unredacted</em> version of this document that can be uploaded to internal Anonymous directories, other VA internal repositories, and Intranet sites only accessible behind the VA firewall.</p></li>
</ul>
<p>Created a mirror document named adt_pims_tm_r.docx/.pdf. In accordance with the current VA Software Document Library (VDL) redaction requirements, all personal identifiable information (PII) and sensitive information (e.g., DFN, IPs, ports, names, Intranet links, etc.) have been replaced with a “REDACTED” placeholder.</p></td>
<td>VDIF Development Team</td>
</tr>
<tr class="odd">
<td>12/2020</td>
<td>0.43</td>
<td><p>DG*5.3*1020 Updates:</p>
<p>Table 2: Updated name of background job from "DG PTF ICD CODE NOTIFIER" to "DG EVENT NOTIFIER."</p></td>
<td>VDIF Development Team</td>
</tr>
<tr class="even">
<td>09/2020</td>
<td>0.42</td>
<td>Updates for numerous VistA patches and releases, as requested by HSP.</td>
<td>AbleVets<br />
GovernmentCIP<br />
Liberty ITS</td>
</tr>
<tr class="odd">
<td>09/2020</td>
<td>0.41</td>
<td>Approved by HSP for VS GUI R1.7.1. Added updates made in August 2020 (0.45 below) to the correct document version.</td>
<td>Liberty ITS</td>
</tr>
<tr class="even">
<td>09/2020</td>
<td>0.40</td>
<td><p>DG*5.3*1015 Updates:</p>
<p>Added modified routines DGENA2, DGENACL2, and DGENDD</p></td>
<td>Liberty ITS</td>
</tr>
<tr class="odd">
<td>08/2020</td>
<td>0.39</td>
<td><p>DG*5.3*993 Updates: Added new and modified routines.</p>
<p>Modified ZEN: VA-Specific Enrollment Segment Table to include SEQ 11 – 19.</p></td>
<td>Liberty ITS</td>
</tr>
<tr class="even">
<td>08/2020</td>
<td>0.38</td>
<td><p>DG*5.3*997 Updates:</p>
<p>Added new routines DGRP11A and DGRP11B, and modified routines DGRPE, DGRPH, DGRPP, DGRPP1, DGRPU, DGRPV, VAFHLFNC, and VAFHLZCT.</p></td>
<td>Liberty ITS</td>
</tr>
<tr class="odd">
<td>08/2020</td>
<td>0.37</td>
<td>Updates for numerous VS GUI releases with their associated VistA patches, as requested by HSP.</td>
<td>AbleVets</td>
</tr>
<tr class="even">
<td>06/2020</td>
<td>0.36</td>
<td><p>DG*5.3*932 Updates:</p>
<p>Table 2: Added DG PTF ICD CODE NOTIFIER to the list of background jobs.</p></td>
<td>CPRS VA TW</td>
</tr>
<tr class="odd">
<td>05/2020</td>
<td>0.35</td>
<td><p>DG*5.3*996 Updates:</p>
<ul>
<li><p>Added modified routine VADPT to “New and Modified Routines.”</p></li>
<li><p>Added PREFERRED NAME field to “Supported References” Table.</p></li>
<li><p>Removed VADM(14) The PREFERRED NAME of the patient (e.g., "PREFERRED NAME") from “DEM^VADPT”.</p></li>
<li><p>Added “DEMUPD^VADPT.”</p></li>
</ul>
<p>Added DEMUPD^VADPT call to “Alpha Subscripts” Table.</p></td>
<td>Liberty ITS</td>
</tr>
<tr class="even">
<td>01/2020</td>
<td>0.34</td>
<td><p>DG*5.3*952 Updates:</p>
<ul>
<li><p>Changes for Emergent OTHER THAN HONORABLE eligibility patients.</p></li>
<li><p>Added EXPANDED MH CARE NON-ENROLLEE code to the Table.</p></li>
</ul>
<p>Added new alpha subscript VAEL(“OTH”) to the Table.</p></td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>01/2020</td>
<td>0.33</td>
<td><p>DG*5.3*985 Updates:</p>
<p>Added modified routines DGR111, DGRP1, DGRPD1, DGRPE, DGRPH, and DGRPV to “New and Modified Routines.”</p></td>
<td>VA OIT</td>
</tr>
<tr class="even">
<td>12/2019</td>
<td>0.32</td>
<td><p>DG*5.3*972 Updates:</p>
<p>Added modified routine DGRPDB to “New and Modified Routines.”</p></td>
<td>VA OIT</td>
</tr>
<tr class="odd">
<td>10/2019</td>
<td>0.31</td>
<td><p>DG*5.3*982 Updates:</p>
<p>Added modified routines DGENACL2 and DGENA2 to “New and Modified Routines.”</p></td>
<td>VA OIT</td>
</tr>
<tr class="even">
<td>06/2019</td>
<td>0.30</td>
<td>Reviewed proppsed changes.</td>
<td>VA OIT</td>
</tr>
<tr class="odd">
<td>05/2019</td>
<td>0.29</td>
<td><p>DG*5.3*941 Updates:</p>
<ul>
<li><p>Reintroduced updates dated 12/2018 that were inadvertently removed from manual.</p></li>
</ul>
<p>Updated VADPT routine to include Residential Address: VAPA(30) – VAPA(39) added to ADD^VADPT and “Alpha Subscripts” Table.</p></td>
<td>VA OIT</td>
</tr>
<tr class="even">
<td>03/2019</td>
<td>0.28</td>
<td><p>DG*5.3*951 Updates:</p>
<ul>
<li><p>Added “Patch DG*5.3*951 Routines.”</p></li>
<li><p>Added PRF HL7 REQUEST LOG (#26.22) file.</p></li>
<li><p>Added “HL7 Interface Specification for Patient Record Flags (PRF).”</p></li>
</ul></td>
<td>VA OIT</td>
</tr>
<tr class="odd">
<td>10/2018</td>
<td>0.27</td>
<td><p>DG*5.3*958 Updates:</p>
<p>Added modified routine.</p></td>
<td>VA OIT</td>
</tr>
<tr class="even">
<td>09/2018</td>
<td>0.26</td>
<td><p>DG*5.3*960 Updates:</p>
<p>Added “Patch DG*5.3*960 Routines.”</p></td>
<td>VA OIT</td>
</tr>
<tr class="odd">
<td>02/2018</td>
<td>0.25</td>
<td><p>DG*5.3*933 Updates:</p>
<ul>
<li><p>Demographics Native Domain Standardization.</p></li>
</ul>
<p>Added “Appendix A.”</p></td>
<td>CTT DM NDS Team</td>
</tr>
<tr class="even">
<td>11/2017</td>
<td>0.24</td>
<td><p>DG*5.3*935 Updates:</p>
<p>Added check in MSDS^VADPT4 to prevent returning a Military Service Episode (MSE) with a Future Discharge Date (FDD) to any downstream applications (p 92).</p></td>
<td>VA OIT</td>
</tr>
<tr class="odd">
<td>03/2017</td>
<td>0.23</td>
<td><p>DG*5.3*903 - Increase Engagement in My HealtheVet (IEMHV) Updates:</p>
<ul>
<li><p>Added Section 3.5.10.</p></li>
<li><p>Updated Section 4.1 with ^DGMHV global.</p></li>
</ul>
<p>Updated Section 4.2 with new files 390.01, 390.02, 390.03, and 390.4.</p></td>
<td>VA OIT</td>
</tr>
<tr class="even">
<td>09/2015</td>
<td>0.22</td>
<td><p>DG*5.3*884 - ICD-10 PTF Modifications Updates:</p>
<ul>
<li><p>Updated title page, footers, and made various formatting changes.</p></li>
<li><p>Corrected headings in Section 2.</p></li>
</ul>
<p>Added new Input templates to Section 3.3.1.</p></td>
<td>VA OIT PD, ICD-10 PTF Modifications Team</td>
</tr>
<tr class="odd">
<td>11/2013</td>
<td>0.21</td>
<td><p>DG*5.3*869 Updates:</p>
<ul>
<li><p>Added Missing Patient, Patient Record Flag (PRF) - Patch Updates section and Patch DG*5.3*869 Routines</p></li>
<li><p>Added Patch DG*5.3*869 Features page 22. Added List of Tables.</p></li>
</ul></td>
<td>VA OIT</td>
</tr>
<tr class="even">
<td>05/2012</td>
<td>0.20</td>
<td>Updated API List.</td>
<td>VA OIT</td>
</tr>
<tr class="odd">
<td>05/2012</td>
<td>0.19</td>
<td><p>Phase I - Patches included in the High Risk Mental Health (HRMH) Project:</p>
<ul>
<li><p>Patch DG*5.3*836 - HRMH-VISTA CHANGES FOR NATIONAL REMINDER &amp; FLAG. This is a Registration patch containing Patient Record Flag APIs.</p></li>
<li><p>DGPFAPIH and DGPFAPIU are new routines.</p></li>
<li><p>Glossary of Terms added.</p></li>
</ul></td>
<td>VA OIT</td>
</tr>
<tr class="even">
<td>01/2011</td>
<td>0.18</td>
<td><p>DG*5.3*754 – ESR 3.1 Updates:</p>
<p>Removed the Confidential Address Phone Number from the HL7 PID Segment Tables.</p></td>
<td>VA OIT</td>
</tr>
<tr class="odd">
<td>05/2010</td>
<td>0.17</td>
<td><p>DG*5.3*754 – ESR 3.1 Updates:</p>
<ul>
<li><p>Updated “Alpha Subscripts” section.</p></li>
<li><p>Added ADD^VADPT (29) &amp; “CPN”.</p></li>
<li><p>Added OPD^VADPT (8) &amp; “WP”.</p></li>
</ul></td>
<td>VA OIT</td>
</tr>
<tr class="even">
<td>11/2009</td>
<td>0.16</td>
<td><p>DG*5.3*754 – ESR 3.1 Updates:</p>
<ul>
<li><p>Updated “VADPT Variables” section.</p></li>
<li><p>Added ADD^VADPT (Conf. Phone Number, OPD^VADPT (Patient’s Phone Number (Work).</p></li>
<li><p>Added SEQ 13 to the PID - Patient Identification Segment.</p></li>
</ul></td>
<td>VA OIT</td>
</tr>
<tr class="odd">
<td>03/2009</td>
<td>0.15</td>
<td><p>DG*5.3*688 Updates:</p>
<ul>
<li><p>Enrollment VistA Changes Release 2 (EVC R2).</p></li>
<li><p>Added additional Value of “O” for “Other” to Table VA0046—Agent Orange Exposure Location.</p></li>
<li><p>Removed Unknown value.</p></li>
<li><p>Changed Environmental Contaminants to SW Asia Conditions.</p></li>
<li><p>Added entries to Part 5 of the “Callable Entry Points in VADPT” section.</p></li>
<li><p>SVC^VADPT modified to add VASV (14) and VASV (14,1) to the VASV array for project SHAD.</p></li>
<li><p>Added alpha subscripts to “ADD^VADPT” section.</p></li>
<li><p>Added alpha subscripts to SVC^VADPT to reflect the alpha translation.</p></li>
<li><p>Replaced HL7 Control Segment - 2.3.6 PID-Patient Identification Segment table - with referral to MPI site on VDL.</p></li>
</ul></td>
<td>VA OIT</td>
</tr>
<tr class="even">
<td>01/2009</td>
<td>0.14</td>
<td><p>Name Change Update:</p>
<p>Austin Automation Center (AAC) to Austin Information Technology Center (AITC).</p></td>
<td>VA OIT</td>
</tr>
<tr class="odd">
<td>07/2008</td>
<td>0.13</td>
<td><p>DG*5.3*763 – Hold Debt to DMC:</p>
<ul>
<li><p>Added ENROLLMENT RATED DISABILITY UPLOAD AUDIT file to the “Files” section (File List) and “Security” section (VA FileMan Access Codes).</p></li>
<li><p>Added DGEN RD UPLOAD AUDIT PURGE background job option.</p></li>
</ul></td>
<td>VA OIT</td>
</tr>
<tr class="even">
<td>07/2008</td>
<td>0.12</td>
<td><p>DG*5.3*779 Updates:</p>
<p>Added DGEN NEACL MGT RPT1BK background job option.</p></td>
<td>VA OIT</td>
</tr>
<tr class="odd">
<td>06/2008</td>
<td>0.11</td>
<td><p>DG*5.3*782 Updates:</p>
<p>Updated RELIGION file.</p></td>
<td>VA OIT</td>
</tr>
<tr class="even">
<td>06/2008</td>
<td>0.10</td>
<td><p>DG*5.3*644 Updates:</p>
<p>Home Telehealth enhancements.</p></td>
<td>VA OIT</td>
</tr>
<tr class="odd">
<td>06/2007</td>
<td>0.9</td>
<td><p>DG*5.3*707 Updates:</p>
<p>Added “HL7 Generic PID,EVN,PV1 Segment Builder established by MPI” to the “HL7 Interface Specifications” section.</p></td>
<td>VA OIT</td>
</tr>
<tr class="even">
<td>11/2006</td>
<td>0.8</td>
<td><p>DG*5.3*650 Updates:</p>
<p>Added two new Files - #26.19 and #26.21.</p></td>
<td>VA OIT</td>
</tr>
<tr class="odd">
<td>10/2006</td>
<td>0.7</td>
<td><p>DG*5.3*689 OEF/OIF Enhancements:</p>
<p>Updated “SVC^VADPT Variable Segment” section.</p></td>
<td>VA OIT</td>
</tr>
<tr class="even">
<td>04/2006</td>
<td>0.6</td>
<td><p>DG*5.3*692 Enhancement:</p>
<p>Updated HL7 Interface Spec for Transmission of Ambulatory Care Data.</p></td>
<td>VA OIT</td>
</tr>
<tr class="odd">
<td>03/2006</td>
<td>0.5</td>
<td><p>DG*5.3*687 Maintenance:</p>
<p>Removed PTF Archive/Purge function.</p></td>
<td>VA OIT</td>
</tr>
<tr class="even">
<td>08/2005</td>
<td>0.4</td>
<td><p>DG*5.3*624 - (10-10EZ 3.0) Updates:</p>
<p>Deleted DGRPT 10-10T REGISTRATION input template in the “Compiled Template Routines” section.</p></td>
<td>VA OIT</td>
</tr>
<tr class="odd">
<td>08/2005</td>
<td>0.3</td>
<td><p>DG*5.3*666 Enhancement:</p>
<p>Added Background Job Option.</p></td>
<td>VA OIT</td>
</tr>
<tr class="even">
<td>11/2004</td>
<td>0.2</td>
<td>Manual updated to comply with SOP 192-352 Displaying Sensitive Data.</td>
<td>VA OIT</td>
</tr>
<tr class="odd">
<td>11/2004</td>
<td>0.1</td>
<td><p>DG*5.3*415 Updates:</p>
<p>Race and Ethnicity Addition to VADPT variable section (patch released in 2003, change omitted in error).</p></td>
<td>VA OIT</td>
</tr>
</tbody>
</table>

<span id="_Ref53997970" class="anchor"></span>Table 1: Reference Materials Table

Table of Contents

<span id="_Toc193957681" class="anchor"></span>List of Figures

<span id="_Toc193957682" class="anchor"></span>List of Tables

<span id="_Toc193957683" class="anchor"></span>Orientation

On-line Help System

When the format of a response is specific, there usually is a HELP message provided for that prompt. HELP messages provide lists of acceptable responses or format requirements which provide instruction on how to respond.

A HELP message can be requested by typing a "?" or "??". The HELP message appears under the prompt, then the prompt is repeated. For example, at the following prompt:

<span id="_Toc193957999" class="anchor"></span>Figure 1: Sample HELP Text

Sort by TREATING SPECIALTY:

enter "?" and the HELP message would appear.

Sort by TREATING SPECIALTY?

CHOOSE FROM:

SURGERY

CARDIOLOGY

12 PSYCHIATRY

Sort by TREATING SPECIALTY:

For some prompts, the system lists the possible answers from which to choose. Any time choices appear with numbers, the system usually accepts the number or the name.

A HELP message may not be available for every prompt. If a "?" or "??" is entered at a prompt that does not have a HELP message, the system repeats the prompt.

Acronyms

VA Acronym Lookup website (VA Intranet site)

Reference Materials

The manuals listed in the table below are available from the [VA Software Document Library (VDL)](http://www.va.gov/vdl):

<table>
<caption><p><span id="_Ref53992632" class="anchor"></span>Table 2: Background Job Options</p></caption>
<colgroup>
<col style="width: 34%" />
<col style="width: 32%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th>Documentation Name</th>
<th>File Name</th>
<th>Location</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>High Risk Mental Health Patient Project Installation and Setup Guide</td>
<td>PXRM_2_24_IG.PDF</td>
<td><p>VDL</p>
<p>Anonymous Directories</p></td>
</tr>
<tr class="even">
<td>PIMS ADT Technical Manual</td>
<td>ADT_PIMS_TM.PDF</td>
<td><p>VDL</p>
<p>Anonymous Directories</p></td>
</tr>
<tr class="odd">
<td>PIMS Appointment Scheduling Technical Manual</td>
<td>SD_PIMS_TM.PDF</td>
<td><p>VDL</p>
<p>Anonymous Directories</p></td>
</tr>
<tr class="even">
<td>PIMS Scheduling User Manual - Outputs Menu</td>
<td>PIMsSchOutput.PDF</td>
<td><p>VDL</p>
<p>Anonymous Directories</p></td>
</tr>
<tr class="odd">
<td>PIMS Scheduling User Manual - Menus, Intro &amp; Orientation, etc.</td>
<td>PIMsSchIntro.PDF</td>
<td><p>VDL</p>
<p>Anonymous Directories</p></td>
</tr>
<tr class="even">
<td>Patient Record Flag User Guide</td>
<td>PatRecFlagUG.PDF</td>
<td><p>VDL</p>
<p>Anonymous Directories</p></td>
</tr>
<tr class="odd">
<td>Scheduling and Registration Installation and Setup Guide</td>
<td>SDDG_Install_Review.PDF</td>
<td><p>VDL</p>
<p>Anonymous Directories</p></td>
</tr>
<tr class="even">
<td>High Risk Mental Health Patient Project Installation and Setup Guide</td>
<td><p>PXRM_2_18_IG.PDF</p>
<p>PXRM_2_18_IG.doc</p></td>
<td><p>VDL</p>
<p>Clinical Reminders website</p>
<p>Anonymous Directories</p></td>
</tr>
<tr class="odd">
<td>Scheduling Patch 578 Installation and Setup Guide</td>
<td>SD_5_3_578_IG.PDF</td>
<td>Anonymous Directories</td>
</tr>
<tr class="even">
<td>Registration Patch 836 Installation and Setup Guide</td>
<td>DG_5_3_836_IG.PDF</td>
<td>Anonymous Directories</td>
</tr>
</tbody>
</table>

<span id="_Ref53992632" class="anchor"></span>Table 2: Background Job Options

# Introduction and Software Purpose


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction and Software Purpose](#introduction-and-software-purpose)
  - [Namespace Conventions](#namespace-conventions)
  - [SACC Exemptions/Non-Standard Code](#sacc-exemptionsnon-standard-code)
  - [Primary Care Management Module (PCMM) Overview](#primary-care-management-module-pcmm-overview)
- [Implementation and Maintenance](#implementation-and-maintenance)
  - [Eligibility ID/Maintenance Menu](#eligibility-idmaintenance-menu)
  - [Station Number (Time Sensitive) Enter/Edit (D ^VASITE0)](#station-number-time-sensitive-enteredit-d-vasite0)
  - [Patient Record Flag (PRF) NATIONAL FLAG (#26.15) File](#patient-record-flag-prf-national-flag-2615-file)
  - [Patch DG\5.3\869—Missing Patient, Patient Record Flag Features](#patch-dg53869missing-patient-patient-record-flag-features)
- [Routines](#routines)
  - [Routines To Map](#routines-to-map)
  - [Callable Routines](#callable-routines)
  - [Compiled Template Routines](#compiled-template-routines)
    - [Input Templates](#input-templates)
    - [Print Templates](#print-templates)
    - [Compiled Cross-Reference Routines](#compiled-cross-reference-routines)
  - [Routine List](#routine-list)
  - [New and Modified Routines](#new-and-modified-routines)
    - [Patch DG\5.3\951 Routines](#patch-dg53951-routines)
    - [Patch DG\5.3\958 Routines](#patch-dg53958-routines)
    - [Patch DG\5.3\960 Routines](#patch-dg53960-routines)
    - [Patch DG\5.3\869 Routines](#patch-dg53869-routines)
    - [Patch DG\5.3\849 Routines](#patch-dg53849-routines)
    - [Patch DG\5.3\836 Routines](#patch-dg53836-routines)
    - [Patch DG\5.3\903 Routines](#patch-dg53903-routines)
    - [Patch DG\5.3\982 Routines](#patch-dg53982-routines)
    - [Patch DG\5.3\972 Routine](#patch-dg53972-routine)
    - [Patch DG\5.3\985 Routines](#patch-dg53985-routines)
    - [Patch DG\5.3\996 Routines](#patch-dg53996-routines)
    - [Patch DG\5.3\997 Routines](#patch-dg53997-routines)
    - [Patch DG\5.3\993 Routines](#patch-dg53993-routines)
    - [Patch DG\5.3\1015 Routines](#patch-dg531015-routines)
    - [Patch DG\5.3\1014 Routines](#patch-dg531014-routines)
    - [Patch DG\5.3\952 Routines](#patch-dg53952-routines)
    - [Patch DG\5.3\977 Routines](#patch-dg53977-routines)
    - [Patch DG\5.3\1016 Routines](#patch-dg531016-routines)
    - [Patch DG\5.3\1025 Routines](#patch-dg531025-routines)
    - [Patch DG\5.3\1029 Routines](#patch-dg531029-routines)
    - [Patch DG\5.3\1034 Routines](#patch-dg531034-routines)
    - [Patch DG\5.3\1035 Routines](#patch-dg531035-routines)
    - [Patch DG\5.3\1027 Routines](#patch-dg531027-routines)
    - [Patch DG\5.3\1044 Routines](#patch-dg531044-routines)
    - [Patch DG\5.3\1047 Routines](#patch-dg531047-routines)
    - [Patch DG\5.3\1045 Routines](#patch-dg531045-routines)
    - [Patch DG\5.3\1056 Routines](#patch-dg531056-routines)
    - [Patch DG\5.3\1061 Routines](#patch-dg531061-routines)
    - [Patch DG\5.3\1065 Routines](#patch-dg531065-routines)
    - [Patch DG\5.3\1059 Routines](#patch-dg531059-routines)
    - [Patch DG\5.3\1067 Routines](#patch-dg531067-routines)
    - [Patch DG\5.3\1071 Routines](#patch-dg531071-routines)
    - [Patch DG\5.3\1075 Routines](#patch-dg531075-routines)
    - [Patch DG\5.3\1064 Routines](#patch-dg531064-routines)
    - [Patch DG\5.3\1081 Routines](#patch-dg531081-routines)
    - [Patch DG\5.3\1082 Routines](#patch-dg531082-routines)
    - [Patch DG\5.3\964 Routines](#patch-dg53964-routines)
    - [Patch DG\5.3\1090 Routines](#patch-dg531090-routines)
    - [Patch DG\5.3\1093 Routines](#patch-dg531093-routines)
    - [Patch DG\5.3\1098 Routines](#patch-dg531098-routines)
    - [Patch DG\5.3\1103 Routines](#patch-dg531103-routines)
    - [Patch DG\5.3\1095 Description and Routines](#patch-dg531095-description-and-routines)
    - [Patch DG\5.3\1109 Routines](#patch-dg531109-routines)
    - [Patch DG\5.3\1107 Routines](#patch-dg531107-routines)
    - [Patch DG\5.3\1111 Routines](#patch-dg531111-routines)
    - [Patch DG\5.3\1120 Routines](#patch-dg531120-routines)
    - [Patch DG\5.3\1118 Routines](#patch-dg531118-routines)
    - [Patch DG\5.3\1121 Routines](#patch-dg531121-routines)
    - [Patch DG\5.3\1104 Description and Routines](#patch-dg531104-description-and-routines)
    - [Patch DG\5.3\1091 Description and Routines](#patch-dg531091-description-and-routines)
    - [Patch DG\5.3\1096 Description and Routines](#patch-dg531096-description-and-routines)
    - [Patch DG\5.3\1127 Routines](#patch-dg531127-routines)
- [Files](#files)
  - [Globals and Files](#globals-and-files)
  - [File List](#file-list)
- [Files and Templates in the PIMS Package](#files-and-templates-in-the-pims-package)
  - [File Flow (Relationships between files)](#file-flow-relationships-between-files)
  - [Templates](#templates)
  - [VA FileMan Functions](#va-fileman-functions)
- [Exported Options](#exported-options)
  - [Menu Diagrams](#menu-diagrams)
  - [Exported Protocols](#exported-protocols)
  - [Exported Options](#exported-options-1)
  - [Exported Remote Procedures](#exported-remote-procedures)
  - [Exported HL7 Applications for Ambulatory Care Reporting](#exported-hl7-applications-for-ambulatory-care-reporting)
  - [Exported HL7 Applications for Inpatient Reporting to National Patient Care Database](#exported-hl7-applications-for-inpatient-reporting-to-national-patient-care-database)
  - [Exported HL7 Applications for Home Telehealth Care Database](#exported-hl7-applications-for-home-telehealth-care-database)
    - [Exported DG Option](#exported-dg-option)
- [Archiving and Purging](#archiving-and-purging)
  - [Archiving](#archiving)
  - [Purging](#purging)
  - [ADT Module](#adt-module)
  - [ACRP Database Conversion Option](#acrp-database-conversion-option)
  - [HL7 Purger](#hl7-purger)
- [External/Internal Relations](#externalinternal-relations)
  - [External Relations](#external-relations)
- [DBIA Agreements](#dbia-agreements)
  - [DBIA Agreements—Custodial Package](#dbia-agreementscustodial-package)
  - [DBIA Agreements—Subscriber Package](#dbia-agreementssubscriber-package)
  - [Internal Relations](#internal-relations)
  - [Package-Wide Variables](#package-wide-variables)
  - [VADPT Variables](#vadpt-variables)
    - [Scheduling Variables](#scheduling-variables)
    - [Patient Record Flag Variables](#patient-record-flag-variables)
  - [VAUTOMA](#vautoma)
  - [VAFMON](#vafmon)
  - [AIT](#ait)
- [How To Generate Online Documentation](#how-to-generate-online-documentation)
  - [XINDEX](#xindex)
  - [Inquire to Option File](#inquire-to-option-file)
  - [Print Options File](#print-options-file)
  - [List File Attributes](#list-file-attributes)
  - [Security](#security)
    - [General Security](#general-security)
    - [Security Keys](#security-keys)
    - [Legal Requirements](#legal-requirements)
  - [VA FileMan Access Codes](#va-fileman-access-codes)
- [VADPT Variables](#vadpt-variables-1)
  - [Supported References](#supported-references)
  - [Callable Entry Points in VADPT](#callable-entry-points-in-vadpt)
    - [DEM^VADPT](#demvadpt)
    - [DEMUPD^VADPT](#demupdvadpt)
    - [ELIG^VADPT](#eligvadpt)
    - [MB^VADPT](#mbvadpt)
    - [SVC^VADPT](#svcvadpt)
    - [ADD^VADPT](#addvadpt)
    - [OAD^VADPT](#oadvadpt)
    - [INP^VADPT](#inpvadpt)
    - [IN5^VADPT](#in5vadpt)
    - [OPD^VADPT](#opdvadpt)
    - [REG^VADPT](#regvadpt)
    - [SDE^VADPT](#sdevadpt)
    - [SDA^VADPT](#sdavadpt)
    - [PID^VADPT](#pidvadpt)
    - [PID^VADPT6](#pidvadpt6)
    - [ADM^VADPT2](#admvadpt2)
    - [KVAR^VADPT](#kvarvadpt)
    - [KVA^VADPT](#kvavadpt)
    - [Combinations](#combinations)
    - [CAI^VADPT](#caivadpt)
  - [Alpha Subscripts](#alpha-subscripts)
- [Data Fields](#data-fields)
  - [Available Data Fields](#available-data-fields)
  - [Configuring Bar Code Label Printers for Print Patient Label Option](#configuring-bar-code-label-printers-for-print-patient-label-option)
    - [Hardware Setup](#hardware-setup)
    - [Software Setup](#software-setup)
  - [Control Code Overview](#control-code-overview)
    - [Patient Label Print Routine Control Code Use](#patient-label-print-routine-control-code-use)
    - [Label Printer Setup Examples](#label-printer-setup-examples)
    - [Zebra Label Printer](#zebra-label-printer)
  - [Intermec Label Printer](#intermec-label-printer)
    - [Example 1—Control Codes Setup for Horizontal Labels](#example-1control-codes-setup-for-horizontal-labels)
    - [Example 2—Control Codes Setup for Vertical Labels](#example-2control-codes-setup-for-vertical-labels)
- [HL7 Interface Specification for Transmission of Ambulatory Care Data](#hl7-interface-specification-for-transmission-of-ambulatory-care-data)
  - [Assumptions](#assumptions)
    - [Message Content](#message-content)
    - [Data Capture and Transmission](#data-capture-and-transmission)
    - [Background Messages](#background-messages)
    - [Batch Messages and Acknowledgements](#batch-messages-and-acknowledgements)
    - [VA MailMan Lower Level Protocol](#va-mailman-lower-level-protocol)
  - [HL7 Control Segments](#hl7-control-segments)
  - [Message Definitions](#message-definitions)
  - [Segment Table Definitions](#segment-table-definitions)
  - [Message Control Segments](#message-control-segments)
    - [MSH—Message Header Segments](#mshmessage-header-segments)
    - [BHS—Batch Header Segment](#bhsbatch-header-segment)
    - [BTS—Batch Trailer Segment](#btsbatch-trailer-segment)
    - [MSA—Message Acknowledgment Segment](#msamessage-acknowledgment-segment)
    - [EVN—Event Type Segment](#evnevent-type-segment)
  - [PID—Patient Identification Segment](#pidpatient-identification-segment)
    - [PD1—Patient Additional Demographic Segment](#pd1patient-additional-demographic-segment)
    - [PV1—Patient Visit Segment](#pv1patient-visit-segment)
    - [PV2—Patient Visit - Additional Information Segment](#pv2patient-visit-additional-information-segment)
    - [DG1—Diagnosis Information Segment](#dg1diagnosis-information-segment)
    - [PR1—Procedure Information Segment](#pr1procedure-information-segment)
    - [ROL—Role Segment](#rolrole-segment)
    - [ZPD—VA-Specific Patient Information Segment](#zpdva-specific-patient-information-segment)
    - [ZEL—VA-Specific Patient Eligibility Segment](#zelva-specific-patient-eligibility-segment)
    - [VA-Specific Income Segment](#va-specific-income-segment)
    - [ZCL—VA-Specific Outpatient Classification Segment](#zclva-specific-outpatient-classification-segment)
    - [ZSC—VA-Specific Stop Code Segment](#zscva-specific-stop-code-segment)
    - [ZSP—VA-Specific Service Period Segment](#zspva-specific-service-period-segment)
    - [ZEN—VA-Specific Enrollment Segment](#zenva-specific-enrollment-segment)
  - [Purpose](#purpose)
  - [Trigger Events and Message Definitions](#trigger-events-and-message-definitions)
    - [Update Patient Information (A08)](#update-patient-information-a08)
    - [Delete a Patient Record (A23)](#delete-a-patient-record-a23)
  - [Supported and User-Defined HL7 Tables](#supported-and-user-defined-hl7-tables)
    - [Table 0001—Sex](#table-0001sex)
    - [Table 0002—Marital Status](#table-0002marital-status)
    - [Table 0003—Event Type Code](#table-0003event-type-code)
    - [Table 0008—Acknowledgment Code](#table-0008acknowledgment-code)
    - [Table 0023—Admit Source (User Defined)](#table-0023admit-source-user-defined)
    - [Table 0051—Diagnosis Code (User Defined)](#table-0051diagnosis-code-user-defined)
    - [Table 0069—Hospital Service (User Defined)](#table-0069hospital-service-user-defined)
    - [Table 0076—Message Type](#table-0076message-type)
    - [Table 0088—Procedure Code (User Defined)](#table-0088procedure-code-user-defined)
    - [Table 0115—Servicing Facility (User Defined)](#table-0115servicing-facility-user-defined)
    - [Table 0133—Procedure Practitioner Type (User Defined)](#table-0133procedure-practitioner-type-user-defined)
    - [Table 0136—Yes/No Indicator](#table-0136yesno-indicator)
    - [Table SD001—Service Indicator (Stop Code)](#table-sd001service-indicator-stop-code)
    - [Table SD008—Outpatient Classification Type](#table-sd008outpatient-classification-type)
    - [Table SD009—Purpose of Visit](#table-sd009purpose-of-visit)
    - [Table VA01—Yes/No](#table-va01yesno)
    - [Table VA02—Current Means Test Status](#table-va02current-means-test-status)
    - [Table VA04—Eligibility](#table-va04eligibility)
    - [Table VA05—Disability Retirement from Military](#table-va05disability-retirement-from-military)
    - [Table VA06—Eligibility Status](#table-va06eligibility-status)
    - [Table VA07—Race](#table-va07race)
    - [Table VA08—Religion](#table-va08religion)
    - [Table VA10—Means Test Indicator](#table-va10means-test-indicator)
    - [Table VA11—Period of Service](#table-va11period-of-service)
    - [Table VA12—Type of Insurance](#table-va12type-of-insurance)
    - [Table VA0015—Enrollment Status](#table-va0015enrollment-status)
    - [Table VA0016—Reason Canceled/Declined](#table-va0016reason-canceleddeclined)
    - [Table VA0021—Enrollment Priority](#table-va0021enrollment-priority)
    - [Table VA0022—Radiation Exposure Method](#table-va0022radiation-exposure-method)
    - [Table VA0023—Prisoner of War Location](#table-va0023prisoner-of-war-location)
    - [Table VA0024—Source of Enrollment](#table-va0024source-of-enrollment)
    - [Table VA0046—Agent Orange Exposure Location](#table-va0046agent-orange-exposure-location)
    - [Table VA0047 — PATIENT REGISTRATION ONLY REASON](#table-va0047-patient-registration-only-reason)
    - [Table NPCD 001—National Patient Care Database Error Codes](#table-npcd-001national-patient-care-database-error-codes)
  - [HL7 Interface Specification for the Transmission of PCMM Primary Care Data](#hl7-interface-specification-for-the-transmission-of-pcmm-primary-care-data)
  - [Assumptions](#assumptions-1)
  - [Message Definitions](#message-definitions-1)
  - [Segment Table Definitions](#segment-table-definitions-1)
  - [Message Control Segments](#message-control-segments-1)
- [HL7 Message Transactions](#hl7-message-transactions)
- [Supported and User-Defined HL7 Tables](#supported-and-user-defined-hl7-tables-1)
  - [Table 0001—Sex](#table-0001sex-1)
  - [Table 0002—Marital Status](#table-0002marital-status-1)
  - [Table 0003—Event Type Code](#table-0003event-type-code-1)
  - [Table 0005—Race](#table-0005race)
  - [Table 0006—Religion](#table-0006religion)
  - [Table 0076—Message Type](#table-0076message-type-1)
- [HL7 Interface Specification for VIC Card VistA to NCMD](#hl7-interface-specification-for-vic-card-vista-to-ncmd)
  - [Assumptions](#assumptions-2)
  - [Message Content](#message-content-1)
  - [Data Capture and Transmission](#data-capture-and-transmission-1)
  - [VA TCP/IP Lower Level Protocol](#va-tcpip-lower-level-protocol)
    - [Message Definitions](#message-definitions-2)
    - [Segment Table Definitions](#segment-table-definitions-2)
    - [Message Control Segments](#message-control-segments-2)
    - [MSH—Message Header Segment](#mshmessage-header-segment)
    - [MSA—Message Acknowledgement Segment](#msamessage-acknowledgement-segment)
    - [PID—Patient Identification Segment](#pidpatient-identification-segment-1)
    - [ORC—Common Order Segment](#orccommon-order-segment)
    - [RQD—Requisition Detail Segment](#rqdrequisition-detail-segment)
    - [NTE—Notes and Comments Segment](#ntenotes-and-comments-segment)
  - [Trigger Events and Message Definitions](#trigger-events-and-message-definitions-1)
  - [ORM—General Order Message (Event O01)](#ormgeneral-order-message-event-o01)
    - [Sample Message](#sample-message)
  - [ORR—General Order Response Message Response to Any ORM (Event O02)](#orrgeneral-order-response-message-response-to-any-orm-event-o02)
    - [Sample Messages](#sample-messages)
  - [Supported and User Defined HL7 Tables](#supported-and-user-defined-hl7-tables-2)
    - [Table 0003—Event Type Code](#table-0003event-type-code-2)
    - [Table 0008—Acknowledgment Code](#table-0008acknowledgment-code-1)
    - [Table 0076—Message Type](#table-0076message-type-2)
    - [Table 0119—Order Control Codes](#table-0119order-control-codes)
- [HL7 Generic PID, EVN, PV1 Segment Builder Established by MPI](#hl7-generic-pid-evn-pv1-segment-builder-established-by-mpi)
  - [Integration Agreement (IA) \#3630](#integration-agreement-ia-3630)
    - [Custodial Package](#custodial-package)
  - [API: BLDEVN^VAFCQRY](#api-bldevnvafcqry)
  - [API: BLDPD1^VAFCQRY](#api-bldpd1vafcqry)
  - [API: BLDPID^VAFCQRY](#api-bldpidvafcqry)
- [HL7 Interface Specification for Home Telehealth (HTH)](#hl7-interface-specification-for-home-telehealth-hth)
  - [Assumptions](#assumptions-3)
  - [Message Content](#message-content-2)
  - [Data Capture and Transmission](#data-capture-and-transmission-2)
- [VA TCP/IP Lower Level Protocol](#va-tcpip-lower-level-protocol-1)
  - [HL7 CONTROL SEGMENTS](#hl7-control-segments-1)
  - [Message Definitions](#message-definitions-3)
  - [Segment Table Definitions](#segment-table-definitions-3)
  - [Message Control Segments](#message-control-segments-3)
    - [MSH—Message Header Segment](#mshmessage-header-segment-1)
    - [EVN—Event Type Segment](#evnevent-type-segment-1)
    - [PID—Patient Identification Segment](#pidpatient-identification-segment-2)
    - [PD1—Patient Additional Demographic Segment](#pd1patient-additional-demographic-segment-1)
    - [PV1—Patient Visit Segment](#pv1patient-visit-segment-1)
    - [MSA—Message Acknowledgement Segment](#msamessage-acknowledgement-segment-1)
- [HL7 Interface Specification for Patient Record Flags (PRF)](#hl7-interface-specification-for-patient-record-flags-prf)
- [HL7 Interface Specification for Community Care Referrals and Authorization (CCRA) Scheduling Actions](#hl7-interface-specification-for-community-care-referrals-and-authorization-ccra-scheduling-actions)
  - [Assumptions](#assumptions-4)
  - [Message Content](#message-content-3)
  - [HL7 Protocols](#hl7-protocols)
  - [HL7 Application Parameters](#hl7-application-parameters)
  - [HL7 Messaging Segments](#hl7-messaging-segments)
    - [SCH—Schedule Activity Information Segment](#schschedule-activity-information-segment)
    - [PID—Patient Information Segment](#pidpatient-information-segment)
    - [PV1—Patient Visit Segment](#pv1patient-visit-segment-2)
    - [RGS—Resource Group Segment](#rgsresource-group-segment)
    - [AIS—Appointment Information Segment](#aisappointment-information-segment)
    - [AIG—Appointment Insurance Segment](#aigappointment-insurance-segment)
    - [AIL—Appointment Location Segment](#ailappointment-location-segment)
    - [AIP—Appointment Provider Segment](#aipappointment-provider-segment)
- [Appendix A—Demographics Domain Native Domain Standardization (NDS)](#appendix-ademographics-domain-native-domain-standardization-nds)
  - [Introduction](#introduction)
  - [New Functionality](#new-functionality)
  - [Options and Build Components](#options-and-build-components)
  - [Modified and New Routines](#modified-and-new-routines)
    - [Routine Information](#routine-information)
- [VistA Audit Solution (VAS)](#vista-audit-solution-vas)
  - [VAS Web Service Components](#vas-web-service-components)
  - [VAS Options](#vas-options)
  - [VAS Parameters](#vas-parameters)
  - [VAS Routines](#vas-routines)
  - [VAS Data Dictionaries](#vas-data-dictionaries)
  - [VAS Alerts](#vas-alerts)
- [Glossary](#glossary)
- [Military Time Conversion Table](#military-time-conversion-table)
- [Alphabetical Index of PIMS Terms](#alphabetical-index-of-pims-terms)
The VistA PIMS package provides a comprehensive range of software supporting the administrative functions of patient registration, admission, discharge, transfer, and appointment scheduling. This document addresses registration and ADT; appointment scheduling is addressed in a separate document. Its functions apply throughout a patient's inpatient and/or outpatient stay from registration, eligibility and Means Testing through discharge with on-line transmission of PTF (Patient Treatment File) data to the CDW (Corporate Data Warehouse). The ADT module aids in recovery of cost of care by supplying comprehensive PTF/RUG-II options and Means Test options.
The ADT module of PIMS is fully integrated with the VA FileMan, thus allowing ad hoc reports to be extracted by non-programmer personnel. ADT is integrated with V. 3.5 of the Fee Basis software allowing Fee personnel to register patients through a select Fee option.
Related manuals include the PIMS User Manual, the PIMS Release Notes, which describe version specific changes to the PIMS package, and PIMS Installation Guide.
Several features have been designed into the PIMS package to maximize efficiency and maintain control over user access of specified sensitive patient records. The Consistency Checker reduces entry of inaccurate information by warning the user about incompatible or missing data. The Patient Sensitivity function allows a level of security to be assigned to certain records within a database in order to maintain control over unauthorized access. The Patient Lookup screens user access of these sensitive records, as well as providing for more efficient and faster retrieval of patient entries.
Tracking and calculation of data is performed transparently by the system to provide a variety of reports which assist in day-to-day operations as well as provide management with the necessary information to analyze workload and promote quality of care. Highlights include the following:
- Automation of the Daily Gains and Losses Sheet and Bed Status Report
- Inpatient Listings
- Seriously Ill Listings
- Bed Availability Reports
- AMIS Reporting
- Disposition Reporting
- Generic code sheets for reporting AMIS segments
- Automation of Appointment Status Update
Notifications for PIMS can be displayed for admissions, death discharges, deaths, and unscheduled (1010) visits. The notifications (ADMISSION, DECEASED, and UNSCHEDULED (1010) VISIT) is displayed for patients who are defined as members of a list in the OE/RR LIST (#100.21) file. The recipients of the notifications would need to be defined as users in the same OE/RR LIST entry. The notifications appear as "alerts" when the user is prompted to select an option from a menu.
1.  REF: For more information concerning OR notifications, see the [CPRS documentation on the VA Software Document Library (VDL)](https://www.va.gov/vdl/application.asp?appid=61).

## Namespace Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The namespaces assigned to the PIMS package are DG, DPT, SD, SC, and VA.

<table>
<caption><p><span id="_Toc193958030" class="anchor"></span>Table 3: Patient Record Flag files</p></caption>
<colgroup>
<col style="width: 38%" />
<col style="width: 17%" />
<col style="width: 17%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th><br />
Option Name</th>
<th>Suggested Run Frequency</th>
<th>Device Required</th>
<th>Remarks</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>DG G&amp;L RECALCULATION AUTO</td>
<td>Nightly</td>
<td>NO</td>
<td><em>Recommended</em> to run <strong>@ 9PM</strong>.</td>
</tr>
<tr class="even">
<td>DG PRE-REGISTER NIGHT JOB</td>
<td>Nightly</td>
<td>NO</td>
<td>Run during off hours. Set to <strong>NULL</strong> device for MSM sites.</td>
</tr>
<tr class="odd">
<td>DG PTF BACKGROUND JOB</td>
<td>Nightly</td>
<td>NO</td>
<td>Run during off hours.</td>
</tr>
<tr class="even">
<td>DG EVENT NOTIFIER</td>
<td>15 minutes</td>
<td>NO</td>
<td>-</td>
</tr>
<tr class="odd">
<td>DG RUG BACKGROUND JOB</td>
<td>Daily</td>
<td>YES</td>
<td>-</td>
</tr>
<tr class="even">
<td>DG RUG SEMI ANNUAL - TASKED</td>
<td>*</td>
<td>YES</td>
<td>*Queued in advance to run on 10/1 and 4/1.</td>
</tr>
<tr class="odd">
<td>DG SENSITIVE RCDS RPT-TASK</td>
<td>Nightly</td>
<td>NO</td>
<td>Run after midnight.</td>
</tr>
<tr class="even">
<td>DGEN NEACL MGT RPT1BK</td>
<td>Daily</td>
<td>YES</td>
<td>-</td>
</tr>
<tr class="odd">
<td>DGEN RD UPLOAD AUDIT PURGE</td>
<td>Daily or Weekly</td>
<td>NO</td>
<td>Purges entries from the ENROLLMENT RATED DISABILITY, UPLOAD AUDIT (#390) file after <strong>365</strong> days.</td>
</tr>
<tr class="even">
<td>DGPF BACKGROUND PROCESSING</td>
<td>Daily</td>
<td>NO</td>
<td>Run during off hours.</td>
</tr>
<tr class="odd">
<td>DGQE BACKGROUND PROCESSING</td>
<td>Nightly</td>
<td>NO</td>
<td>Run during off hours.</td>
</tr>
<tr class="even">
<td><p>SCDX AMBCAR NIGHTLY XMIT</p>
<ol start="2">
<li><p>This option has been placed out of order with patch SD*5.3*640, since ACRP transmission has been discontinued.</p></li>
</ol></td>
<td>Nightly</td>
<td>NO</td>
<td>Collects workload information and sends it to NPCDB in Austin via HL7 messages.</td>
</tr>
<tr class="odd">
<td>SCENI IEMM SUMMARY BULLETIN</td>
<td>Nightly</td>
<td>NO</td>
<td>Run after nightly transmission to Austin.</td>
</tr>
<tr class="even">
<td><p>SCRPW APM TASK JOB</p>
<ol start="3">
<li><p>This option has been placed out of order with patch SD*5.3*640 since APM transmission has been discontinued.</p></li>
</ol></td>
<td>Monthly</td>
<td>NO</td>
<td>Runs on the 15th of the current month after hours. Generates info rolled up to AITC (formerly AAC) Additional Performance Monitors (TIU).</td>
</tr>
<tr class="odd">
<td>VAFC BATCH UPDATE</td>
<td>30 minutes</td>
<td>NO</td>
<td>Transmits changes to key patient demographical data.</td>
</tr>
<tr class="even">
<td>VAFH PIVOT PURGE</td>
<td>Weekly</td>
<td>NO</td>
<td>Purges entries greater than <strong>1.5 years</strong> old from ADT/HL7 PIVOT (#391.71) file.</td>
</tr>
<tr class="odd">
<td>DG VAS EXPORT</td>
<td>300 seconds</td>
<td>No</td>
<td>Looks at the ^DGAUDIT global for entries if there are entries it processes the entries to the VAS REST API via the DG VAS WEB SERVICE.</td>
</tr>
</tbody>
</table>

<span id="_Toc193958030" class="anchor"></span>Table 3: Patient Record Flag files

## SACC Exemptions/*Non*-Standard Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are the steps you may take to obtain the Standards and Conventions Committee (SACC) exemptions for the PIMS package.

1.  FORUM.
2.  DBA Menu.
3.  SACC Exemptions Menu.
4.  Display Exemptions for a Package Option.
5.  Select SACC Exemptions package: ADT SD.

## Primary Care Management Module (PCMM) Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Primary Care Management Module (PCMM) was developed to assist VA facilities in implementing primary care. It supports both primary care teams and *non*-primary care teams. PCMM’s functionality is divided into eight areas:

- Setup & Define Team
- Assign Staff to Positions in Teams
- Assign Patient to Team
- Assign Patient to Practitioner via Team Position and Enroll in a Clinic
- Reports/Outputs/Mail Messages
- Tools to Ease Startup Process of Primary Care
- Other Changes to Scheduling Package
- Application Program Interface (API) calls.

PCMM uses a Graphical User Interface (GUI) to control the startup, setup, and assignment functions. To use the functionality in the PCMM, a site needs a Microsoft Windows workstation which has a connection to VistA (either LAN or serial connection) for each location where a patient or staff member is assigned to a team. A typical site wants one workstation for each team, one for the PIMS ADPAC, plus one for the manager in charge of primary care. Existing Scheduling functionality continues to be useable from “roll-and-scroll” terminals.

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section of the PIMS Technical Manual provides information to assist technical support staff with the implementation and maintenance of the software. This section should include information regarding the entry of required site-specific data, including where applicable.

The PIMS package can be tailored specifically to meet the needs of the various sites. Instructions are found in the User Manual under the ADT Module, Supervisor ADT and the Scheduling Module, Supervisor. A variety of options are included in these sections allowing each site to define its own configuration. The ADT portion of the PIMS package functions around the parameters defined through the MAS Parameter Entry/Edit option while the Scheduling portion parameters are defined through the Scheduling Parameters option.

A great many other options are included in these Supervisor sections, which assist in site configuration and maintenance functions. Among them are options that do the following:

- Allow for specification of mail groups to receive certain bulletins.
- Definition of devices.
- Designation of transmission routers.
- Entry/Edit of Means Test data.
- Ward setup.
- Clinic setup.

All configurations can be modified at any time as the site's needs change.

The USE USR CLASS FUNCTIONALITY? (#801) field can be used to turn on/off the user class functionality provided by the Authorizations/ Subscriptions software. This functionality allows certain staff members/users (especially clinicians) to be classified in a very specific manner (e.g., cardiologist), and yet the software can determine that the staff member is a member of a more general class (e.g., provider).

If a site has A/S installed prior to the PCMM installation, PCMM defaults to use the user class functionality:

- Sites that have *not* populated the USR CLASS MEMBERSHIP (#8930.3) file for their potential team members should have this parameter set to NO.
- Sites that have fully populated the USR CLASS MEMBERSHIP (#8930.3) file should set this parameter to YES, because the assignment of staff members to teams is less error-prone and faster than the unscreened selection from the NEW PERSON (#200) file.

The CHECK PC TEAM AT DISCHARGE? (#802) field can be used to turn off the PCMM functionality, which, upon inpatient discharge, checks the patient's primary care assignments:

- If the patient has current primary care data, it is displayed.
- If the patient does *not* have a current primary care team assignment, the user is prompted to assign the patient to a primary care team.

The ENABLE AUTOLINK FUNCTIONALITY? (#803) field should be turned off until OE/RR is installed. Although there is no harm in allowing users to add/edit auto link data, this is not usable until OE/RR is installed. The auto link functionality was added for use by OE/RR teams.

## Eligibility ID/Maintenance Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Eligibility/ID Maintenance Menu provides the options needed to accommodate VA/DOD sharing agreement requirements with regard to Patient Identification Number. For most medical centers, the PT ID is the social security number of the patient and the SHORT ID is the last four digits of the patient's social security number. For those sites with DOD sharing agreements using VA/DOD software developed by the Dallas Office of Information Field Office (OIFO), the PT ID is determined by the ID number given that patient by the military.

For most sites, each eligibility simply needs to be associated with the VA STANDARD format. This association was first accomplished during the post-init of MAS V. 5.0.

Other than The Primary Eligibility ID Reset (All Patients) option, the remaining six options would only be used by DOD sites using VA/DOD software developed by the Dallas OIFO. They should *not* be run without Central Office and/or DOD approval/direction.

4.  If you feel your site needs to use these options, contact your local OIFO for guidance.

The following is a brief description of each option and its use:

- PRIMARY ELIGIBILITY ID RESET (ALL PATIENTS)—This option sets / resets the IDs associated with each patient's primary eligibility code. This utility is called when first installing the new eligibility data structure. It runs automatically as part of the PIMS clean-up routine process.

The option can be executed multiple times with no harmful effects. It should be run during non-peak hours, preferably over a weekend. A MailMan message is sent to the user when the job is completed showing the start and completion date/time.

- ELIGIBILITY CODE ENTER/EDIT—This option allows the user to enter/edit eligibility codes used by the site. It should be run for all ELIGIBILITY file entries to associate each entry with an MAS Eligibility code and an Identification Format.

> <span id="_Toc193958000" class="anchor"></span>Figure 2: ELIGIBILITY CODE ENTER/EDIT Option—System Dialogue and User Responses (boldface)

Select ELIGIBILITY CODE NAME: MARINE CORPS

ARE YOU ADDING 'MARINE CORPS' AS A NEW ELIGIBILITY CODE (THE 5TH)? YES

ELIGIBILITY CODE MAS ELIGIBILITY CODE: OTHER FEDERAL AGENCY 4

NAME: MARINE CORPS// \<Enter\>

ABBREVIATION: MC

PRINT NAME: MARINE CORPS

INACTIVE: \<Enter\>

MAS ELIGIBILITY CODE: OTHER FEDERAL AGENCY// \<Enter\>

ID FORMAT: DOD

AGENCY: ARMY Select SYNONYM: \<Enter\>

- ID FORMAT ENTER/EDIT—This option allows the user to enter/edit identification (ID) formats with description.
- RESET ALL IDS FOR A PATIENT—This option is used to reset the corresponding IDs for all eligibilities for a single patient. The patient's eligibilities is listed as the ID is reset. This utility would be used if, for some reason, a patient's ID got corrupted.
- RESET ALL IDS FOR ALL PATIENTS—This option resets all IDs corresponding to each of the patient's eligibilities. The option should be executed during non-peak hours. When the job is completed, a MailMan message is generated to the user showing the start and completion date/time.
- SPECIFIC ELIGIBILITY ID RESET (ALL PATIENTS)—After prompting for an eligibility code and queue-to-run time, this option updates the IDs for all patients having the selected eligibility. This utility would allow a site to update their database with the new value if the ID FORMAT field in the ELIGIBILITY CODE file changed.

The option should be run during off hours. When the job is completed, a MailMan message is generated to the user showing the start and completion date/time.

- SPECIFIC ID FORMAT RESET—This option prompts for an ID format; then, all patients that have eligibility codes associated with that ID format have their IDs reset. The utility allows sites to update their database if the DEFAULT LONG ID VALUE CODE field in the IDENTIFICATION FORMAT file was modified. This option should be executed during off hours. When the job is completed, a MailMan message is sent to the user showing the start and completion date/time.

## Station Number (Time Sensitive) Enter/Edit (D ^VASITE0)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The STATION NUMBER (TIME SENSITIVE) (#389.9) file is used to hold the time sensitive station number data. This file was initially populated by the post-init routine for MAS V. 5.2. One entry was created for each medical center division with an effective date of Jan 1, 1980. It is *not* necessary to modify this data unless the station number for a division changes or a new division is added.

Entering a new medical center division name through the Supervisor ADT Menu of the ADT module of PIMS automatically creates a new entry in this file. New divisions *cannot* be added through this routine entry point.

The Station Number (Time Sensitive) Enter/Edit routine entry point is used to change an existing station number or enter a new station number for a new division. If you are changing a station number for a division, you should enter a new effective date and the new station number for that division.

Once a new division has been added, you should select the new division and enter the effective date and new station number. The IS PRIMARY DIVISION field should be set to YES for the division where the station number has no suffix. Only one division can be primary at any given time.

## Patient Record Flag (PRF) NATIONAL FLAG (#26.15) File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The new national flag data entry (MISSING PATIENT) is placed in the PRF NATIONAL FLAG (#26.15) file by the DG\*5.3\*869 DG NEW CAT 1 FLAG patch.

The new national flag data entry (HIGH RISK FOR SUICIDE) is placed in the PRF NATIONAL FLAG (#26.15) file by the DG\*5.3\*849 DGPF NEW CAT1 FLAG AND CONVERSION patch:

| File Number | File Name         | New Data Entry                                                            |
|-------------|-------------------|---------------------------------------------------------------------------|
| 26.15       | PRF NATIONAL FLAG | HIGH RISK FOR SUICIDE                                                     |
| 26.15       | PRF NATIONAL FLAG | URGENT ADDRESS AS FEMALE (see [note](#note_urgent_address_as_female_prf)) |
| 26.15       | PRF NATIONAL FLAG | MISSING PATIENT                                                           |
| 26.15       | PRF NATIONAL FLAG | BEHAVIORAL                                                                |

<span id="_Toc193958031" class="anchor"></span>Table 4: Callable Routines

5.  <span id="note_urgent_address_as_female_prf" class="anchor"></span>The URGENT ADDRESS AS FEMALE PRF updates are *not* included in the PIMS Manual updates.  
      
    REF: For information on this patch update, see the *VDL – ADT - USH LEGAL SOLUTION – CATEGORY I Patient Record Flag (PRF) Installation Guide*.

## Patch DG\*5.3\*869—Missing Patient, Patient Record Flag Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch DG\*5.3\*869 features:

- Creates National Category I MISSING PATIENT, Patient Record Flag.
- Creates DGPF MISSING PT FLAG REVIEW mail group.
- Updates File \#.84 (Field \#4), Dialog Number 261132-Patient has local ICN, to change the message that is displayed when there is an attempt by a user to assign any National, CAT I PRF to the record of a patient that does not have a National ICN. This component updates the Text (field \#4) to not reference any specific National, Category I PRF (i.e., BEHAVIORAL) to be assigned.
- Updates the following reports to reflect the new Missing Patient, Patient Record Flag (\*REF: See the Record Flag Reports Menu section for more details on each report):
- Assignment Action Not Linked Report
- Flag Assignment Report
- Patient Assignments Report
- Assignments Due For Review Report
- Assignments Approved by Report

# Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides a list of routines or instruct the user how/where to find this information online:

## Routines To Map

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Routine mapping is not required with VMS/Cache systems.

## Callable Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Callable Routine          | Description                                                            |
|---------------------------|------------------------------------------------------------------------|
| \$\$GETACT^DGPFAPI    | Obtain active Patient Record Flag assignments.                         |
| \$\$INSTPCTM^SCAPMC   | Institution & team for pt's pc team.                                   |
| \$\$PRCL^SCAPMC       | Practitioners for a Clinic.                                            |
| \$\$PRPT^SCAPMC       | Practitioners for a Patient.                                           |
| \$\$PRTM^SCAPMC       | Practitioners for a Team.                                              |
| \$\$PTTM^SCAPMC       | Patients for a Team.                                                   |
| \$\$SITE^VASITE       | Obtain Station Number Information.                                     |
| \$\$TMPT^SCAPMC       | Teams for a Patient.                                                   |
| DGINPW                | Obtain Inpatient Status.                                               |
| DGPMLOS               | Obtain Length of Stay by Admission.                                    |
| \$\$GETALL^SCAPMCA    | Return assignment information.                                         |
| \$\$OUTPTAP^SDUTL3    | Return associate pc provider information.                              |
| \$\$OUTPTRP^SDUTL3    | Return primary care provider information.                              |
| \$\$DATA2PTF^DGAPI    | Send data to PTF.                                                      |
| CPTINFO^DGAPI         | Get CPTs from PTF.                                                     |
| PTFINFOR^DGAPI        | Delete CPTs from PTF.                                                  |
| \$\$DELCPT^DGAPI      | Get Prof Serv Dates from PTF.                                          |
| \$\$DELPOV^DGAPI      | Delete POVs from PTF.                                                  |
| ICDINFO^DGAPI         | Get ICDs from PTF.                                                     |
| \$\$COMMANUM^VAFCADT2 | Build a list of numbers separated by comma.                            |
| VACPT                 | Display CPT Copyright Information.                                     |
| VADATE                | Generic Date Routine.                                                  |
| VADPT                 | Obtain Patient Information.                                            |
| VALM                  | List Manager.                                                          |
| BLDPID^VAFCQRY        | Builds the PID HL7 segment.                                        |
| \$\$EVN^VAFHLEVN      | Builds the EVN HL7 segment.                                        |
| \$\$EN^VAFHLPD1       | Builds the PD1 HL7 segment.                                        |
| \$\$SITE^VASITE       | Returns the institution and station numbers.                           |
| VAFMON                | Obtain Income or Dependent Information.                                |
| VATRAN                | Establish VA Data Transmission System (VADATS) Transmission Variables. |
| VATREDIT              | Enter/Edit TRANSMISSION ROUTERS file.                                  |
| VAUQWK                | Quick Lookup for Patient Data.                                         |
| VAUTOMA               | Generic One, Many, All Routine.                                        |

<span id="_Toc193958032" class="anchor"></span>Table 5: Input Templates

6.  REF: For entry points, see the “[Callable Routines, Entry Points, and Application Programming Interfaces](\l)” section.

## Compiled Template Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is *recommended* you recompile the following templates at 4000 bytes.

### Input Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| File \# | Template Name                  | Routines      |
|---------|--------------------------------|---------------|
| 2       | DG CONSISTENCY CHECKER         | DGRPXC\*  |
|         | DG LOAD EDIT SCREEN 7          | DGRPXX7\* |
|         | DGRP COLLATERAL REGISTER       | DGRPXCR\* |
| 40.8    | DGTS                           | DGXTS     |
| 45      | DG PTF CREATE PTF ENTRY        | DGPTXC\*  |
|         | DG PTF POST CREATE             | DGPTXCA\* |
|         | DG 101                         | DGPTX1\*  |
|         | DG 401                         | DGPTX4\*  |
|         | DG401-10P                      | DGX4\*    |
|         | DG 501                         | DGPTX5\*  |
|         | DG501-10D                      | DGX5\*    |
|         | DG 501F                        | DGX5F\*   |
|         | DG501F-10D                     | DGX5FD\*  |
|         | DG601-10P                      | DGX6\*    |
|         | DG 701                         | DGPTX7\*  |
|         | DG701-10D                      | DGX7\*    |
| 45.5    | DG PTF ADD MESSAGE             | DGPTXMS\* |
| 46.1    | DG801                          | DGPTX8\*  |
| 405     | DGPM ADMIT                     | DGPMX1\*  |
|         | DGPM TRANSFER                  | DGPMX2\*  |
|         | DGPM DISCHARGE                 | DGPMX3\*  |
|         | DGPM CHECK-IN LODGER           | DGPMX4\*  |
|         | DGPM LODGER CHECK-OUT          | DGPMX5\*  |
|         | DGPM SPECIALTY TRANSFER        | DGPMX6\*  |
|         | DGPM ASIH ADMIT                | DGPMXA\*  |
| 408.21  | DGMT ENTER/EDIT ANNUAL INCOME  | DGMTXI    |
|         | DGMT ENTER/EDIT EXPENSES       | DGMTXE    |
|         | DGRP ENTER/EDIT ANNUAL INCOME  | DGRPXIS   |
|         | DGRP ENTER/EDIT MON BENEFITS   | DGRPXMB   |
| 408.22  | DGMT ENTER/EDIT DEPENDENTS     | DGMTXD    |
|         | DGMT ENTER/EDIT MARITAL STATUS | DGMTXM    |
| 408.31  | DGMT ENTER/EDIT COMPLETION     | DGMTXC    |

<span id="_Toc193958033" class="anchor"></span>Table 6: Print Templates

### Print Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| File \# | Template Name        | Routines      |
|---------|----------------------|---------------|
| 45      | DG PTF PT BRIEF LIST | DGPTXB\*  |
| 45.86   | DGPT QUICK PROFILE   | DGPTXCP\* |

<span id="_Toc193958034" class="anchor"></span>Table 7: Compiled Cross-Reference Routines

### Compiled Cross-Reference Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| File \# | Template Name            | Routines      |
|---------|--------------------------|---------------|
| 45      | PTF                      | DGPTXX\*  |
| 405     | PATIENT MOVEMENT         | DGPMXX\*  |
| 408.21  | INDIVIDUAL ANNUAL INCOME | DGMTXX1\* |
| 408.22  | INCOME RELATION          | DGMTXX2\* |
| 408.31  | ANNUAL MEANS TEST        | DGMTXX3\* |

<span id="_Ref54081432" class="anchor"></span>Table 8: Patch DG\*5.3\*951 Routines

## Routine List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are the steps you can take to obtain a listing of the routines contained in the PIMS package.

1.  Programmer Options Menu.
6.  Routine Tools Menu.
7.  First Line Routine Print Option.
8.  Routine Selector:
- DG\* (ADT)

## New and Modified Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Patch DG\*5.3\*951 Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The table below lists the new and modified routines exported by patch DG\*5.3\*951, SHRPE ENHANCEMENTS FOR PATIENT RECORD FLAGS.

7.  Not all routines can or should be used. Please refer to the outstanding Integration Agreement before attempting to use these routines.

| New DG Routines | Modified DG Routines |
|-----------------|----------------------|
| DGPFDBRS    | DGPFAA           |
| DGPFHLF     | DGPFAA1          |
| DGPFHLT     | DGPFAA2          |
| DGPFHLT1    | DGPFAA3          |
| DGPFHLT2    | DGPFAAH          |
| DGPFHLT3    | DGPFAAH1         |
| DGPFHLT4    | DGPFAPI1         |
| DGPFHLTM    | DGPFHLQ          |
| DGPFLMA5    | DGPFHLQ4         |
| DGPFRDB     | DGPFHLR          |
| DGPFRDB1    | DGPFHLU          |
| DGPFTR      | DGPFHLU1         |
| DGPFTR1     | DGPFHLU2         |
| DGPFUT6     | DGPFHLU3         |
| DGPFUT61    | DGPFHLU4         |
| DGPFUT62    | DGPFHLUT         |
| DGPFUT64    | DGPFLMA2         |
| DGPFLMA3    | DGPFLMA4         |
| DGPFLMU1    | DGPFUT           |
| DGPFUT3     | DGPFUT4          |

<span id="_Toc528240330" class="anchor"></span>Table 9: Patch DG\*5.3\*958 Routines

### Patch DG\*5.3\*958 Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DGOREL1 routine was modified by patch DG\*5.3\*958. This patch changed the Religion List for Inpatients \[DG RELIGION LIST\] option in the Inpatient/Lodger Report Menu \[DG INPATIENT REPORTS\] to display only the last four digits of a patient’s Social Security Number (SSN). Previously, the full SSN had displayed in this report.

| New DG Routines                            | Modified DG Routines |
|--------------------------------------------|----------------------|
| There are no new routines with this patch. | DGOREL1          |

<span id="_Ref54604762" class="anchor"></span>Table 10: Patch DG\*5.3\*960 Routines

### Patch DG\*5.3\*960 Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The new and modified routines in the table below were exported by patch DG\*5.3\*960 – PATIENT RECORD FLAG REPORTS.

8.  Not all routines can or should be used. Please refer to the outstanding Integration Agreement before attempting to use these routines.

| New DG Routines | Modified DG Routines |
|-----------------|----------------------|
| DGPFAAH2    | DGPFLMT          |
| DGPFUT63    | DGPFLMT1         |
| DGPFUT7     | DGPFRAL          |
|                 | DGPFRAL1         |
|                 | DGPFRFA          |
|                 | DGPFRFA1         |

<span id="_Ref54605118" class="anchor"></span>Table 11: Patch DG\*5.3\*869 Routines

### Patch DG\*5.3\*869 Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The table below lists the new and modified routines that were exported with patch DG\*5.3\*869, DGPF NEW PATIENT RECORD FLAG – MISSING PATIENT.

9.  Not all routines can or should be used. Please refer to the outstanding Integration Agreement before attempting to use these routines.

| New DG Routines | Modified DG Routines                            |
|-----------------|-------------------------------------------------|
| DG53869P    | There are no modified routines with this patch. |

<span id="_Ref54605329" class="anchor"></span>Table 12: Patch DG\*5.3\*849 Routines

### Patch DG\*5.3\*849 Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The table below lists the DG routines that were exported with patch DG\*5.3\*849, DGPF NEW CAT1 FLAG AND CONVERSION.

10. Not all routines can or should be used. Please refer to the outstanding Integration Agreement before attempting to use these routines.

| New DG Routines | Modified DG Routines                          |
|-----------------|-----------------------------------------------|
| DG53849P    | There are no modified routines in this patch. |
| DGPFCNR     |                                               |
| DGPFCNV     |                                               |

<span id="_Toc193958040" class="anchor"></span>Table 13: Patch DG\*5.3\*1120 Routines

### Patch DG\*5.3\*836 Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch DG\*5.3\*836, Registration Patient Record Flag patch, provides new interfaces used by the Scheduling and Reminder patches to determine the High Risk for Suicide flag status on a specified date:

- GETINF^DGPFAPIH—DGPFAPIH is both a routine and API integration agreement. The DGPFAPIH routine implements the two application programming interface call points for retrieving Patient Record Flag information:
- One call point is for a specific patient and record.
- The second call point is for a list of patients with a specific, active, Patient Record Flag.

This API obtains the Patient Record Flag assignment information and status for the specified patient, patient record flag and date range. The return data is provided in an array using the target root specified by the user or in the default array variable DGPFAPI1. The DATE/TIME (#.02) field of the PRF ASSIGNMENT HISTORY (#26.14) file entry determines whether the entry falls within the specified date range. If no date range is specified, all entries are returned.

- GETLST^DGPFAPIH—This API retrieves a list of patients active at some point within a specified date range for a specified Patient Record Flag. The date range is required for this API; though, the same date can be entered to specify a single date. The return data is provided in an array using the target root specified by the user or in the default array variable DGPFAPI2. The DATE/TIME (#.02) field of the PRF ASSIGNMENT HISTORY (#26.14) file entry determines whether the entry falls within the specified date range.
- BLDMAIN^DGPFAPIH—This API builds the main return array for the specified patient. The array contains the PRF assignment data retrieved from the appropriate Local or National assignment file.
- BLDHIST^DGPFAPIH—This API collects and builds the return array containing the PRF assignment history data.
- ACTIVE^DGPFAPIU—The DGPFAPIU routine provides support utilities and functions for the new Application Programming Interface calls.

This procedure checks if the Patient Record Flag was active at any point during the specified date range. The procedure accepts a date range parameter which specifies whether “A”ll dates or only a “S”pecified date range is to be checked.

The PRF ASSIGNMENT HISTORY (#26.14) file was *not* designed for this type of date interaction so the algorithm in this procedure has to make a number of assumptions when interpreting the dates and PRF actions. While there can only be one “New Assignment” entry, it is possible to have multiple “Continue.” “Inactivate,” and “Reactivate” action entries. In addition, the “Entered In Error” action can pose additional issues with determining a status during a specific date range.

- CHKDATE^DGPFAPIU—Checks for valid start and end dates. Sets up the DGRANGE parameter with the validated dates and sets DGRANGE top element to “A” for all dates, or “S” for a specific range of dates.
- CHKDFN^DGPFAPIU—This function checks for a valid patient by checking the DFN in the PATIENT (#2) file. If a valid patient is found, the patient name is returned; otherwise, the error text from the DIQ call is returned.
- ASGNDATE^DGPFAPIU—Gets the initial Assignment Date/Time of the Patient Record Flag by looking for the “NEW ASSIGNMENT” action in the PRF ASSIGNMENT HISTORY (#26.14) file.
- GETFLAG^DGPFAPIU—This function gets the variable pointer value for the Patient Record Flag passed in. The PRF is passed in as a text value:
- If the optional flag category is passed in, only that category is checked for the PRF.
- If no category is passed in, then first the National category is checked.

### Patch DG\*5.3\*903 Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch DG\*5.3\*903 addresses NSR \# 20150314 - Increase Engagement in My HealtheVet (IEMHV). The Preregister a Patient \[DGPRE PRE-REGISTER OPTION\] option, in the VistA Registration V. 5.3 package, was enhanced to display a message alerting the registration clerk to engage with the selected patient regarding the patient’s registration status for My HealtheVet. The clerk should document that status, any registration assistance rendered, or the Veteran’s desire to be excluded from My HealtheVet registration. Recent assistance with the patient's My HealtheVet registration is displayed within the alert/reminder.

There is no interface with My HealtheVet. This is only a mechanism to engage directly with the patient to encourage him/her to register for My HealtheVet.

The MAS PARAMETERS (#43) file and the MAS Parameter Entry/Edit \[DG PARAMETER ENTRY\] option were enhanced to allow for this new functionality to be disabled/enabled. This functionality is turned off automatically during the post install for this patch.

The following new routines are being added to support Patch DG\*5.3\*903:

- DG903PST—Post install routine which does the following:
- Adds entry 315 in INCONSISTENT DATA ELEMENTS (#38.6) file.
- Disables Increase Veteran Engagement in My HealtheVet Prompts in the MAS PARAMETERS (#43) file.
- DGMHV:
- EN API—Entry Point for Alert, Socialization, and My HealtheVet Engagement field editing screen. This functionality is only executed if the ENABLE MY HEALTHEVET PROMPTS? (#1100.07) field in the MAS PARAMETERS (#43) file is set to YES (internal value 1).
- MAIN API—Main Entry Point for My HealtheVet socialization text/action.
- SOCIAL API—My HealtheVet Engagement talking point/socialization text action. Display My HealtheVet socialization canned text, prompt for patient response, display and prompt for clerk action.
- DGMHVAC:
- EN API—Entry point for My HealtheVet Engagement screen.
- MAIN API—Main Driver for My HealtheVet Engagement screen.
- ENROLLQ API—Prompt for "My HealtheVet Registered".
- AUTHENQ API—Prompt for "My HealtheVet Authenticated".
- OPTINQ API—Prompt for "Opted in for My HealtheVet Secure Messaging".
- ENROLL API—My HealtheVet Register processing.
- AUTHENT API—Authenticated My HealtheVet account status processing.
- SECMSG API—Secure Messaging processing.
- MHVOK API—Check patient's MHV registration information to determine if the alert should be activated or deactivated.
- DGMVUTL—Contains numerous APIs used by the other listed routines.

The following existing routines are being updated to support Patch DG\*5.3\*903:

- DGPAR - PREREG subroutine—Updated to display value of the ENABLE MY HEALTHEVET PROMPTS?” (#1100.07) field in the MAS PARAMETERS (#43) file.
- DGPAR1—Updated to allow the edit of the ENABLE MY HEALTHEVET PROMPTS? (#1100.07) field in the MAS PARAMETERS (#43) file.
- DGPREP1 - DIREDT API—Updated to include the new “Increase Engagement in My HealtheVet” prompts to display and prompt for updates from the clerk.
- DGRPC - EN API—Updated to include the new 315 Consistency Check for “Increase Engagement in My HealtheVet”
- DGRPC3—Added 315 subroutine to include the new 315 Consistency Check Editing functionality.
- DGRPCE1—Updated to include 315 Consistency Check Editing functionality when necessary “Increase Engagement in My HealtheVet” data fields have *not* been updated.

### Patch DG\*5.3\*982 Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch DG\*5.3\*982 includes modifications and updates to VistA Registration, Eligibility & Enrollment (REE)-related to keeping patients on the New Enrollee Appointment Request (NEAR) Call List option \[DGEN NEACL MGT RPT1\] for appointments, unless the patient has a Primary Care Appointment. It also includes adding a display message to the Management Edit option \[DGEN NEACL REQUEST MGT EDIT\] in the New Enrollee Appointment Request (NEAR) Management Menu \[DGEN NEACL REQUEST MGT MENU\].

The following modified routines are exported by patch DG\*5.3\*982:

- DGENACL2
- DGENA2

### Patch DG\*5.3\*972 Routine

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch DG\*5.3\*972 addresses NSR \#20120809 regarding Public Law 112-154. Users shall be able to view a patient’s current Camp Lejeune eligibility from the Eligibility Inquiry for Patient Billing option on the Admissions/Discharges/Transfers (ADT) Manager menu and/or the Registration sub-menu.

The following modified routine is exported by patch DG\*5.3\*972:

- DGRPDB

### Patch DG\*5.3\*985 Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch DG\*5.3\*985 includes modifications and updates to VistA REE related to adding the PREFERRED NAME (#.2405) field to the PATIENT DEMOGRAPHIC DATA SCREEN \<1\> screen.

The following modified routines are exported by patch DG\*5.3\*985:

- DGR111
- DGRP1
- DGRPD1
- DGRPE
- DGRPH
- DGRPV

### Patch DG\*5.3\*996 Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch DG\*5.3\*996 includes modifications and updates to VistA REE related to adding the PREFERRED NAME to a demographic API. A new demographics API, DEMUPD VADPT, is included in Integration Control Registration (ICR) 7109. A new tag, DEMUPD, which adds the patient’s PREFERRED NAME to the patient's basic demographic information and stores this data in the VADEMO array, has been added to the VADPT routine. ICR 7109 is in addition to, and does not replace, ICR 10061.

### Patch DG\*5.3\*997 Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch DG\*5.3\*997 includes new routines: DGRP11A and DGRP11B, and modifications to routines: DGRPE, DGRPH, DGRPP, DGRPP1, DGRPU, and DGRPV to accommodate the newly added Caregiver data screens. This includes creating and modifying routines for the newly created \<11.5\> and \<11.5.1\> screens, plus the need to accommodate the new screen ^jump flow controls, and lastly to adjust the text in the HELP and INVALID ENTRY…VALID SCREEN \#s message in response to the end of page prompts.

This patch also includes modifications to routines VAFHLFNC and VAFHLZCT to send foreign address fields in the ZCT segment when sending the Z07 message.

### Patch DG\*5.3\*993 Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch DG\*5.3\*997 contains modifications to VistA REE to separate patient registration from enrollment of Veterans for VHA healthcare. The questions beginning with the “DO YOU WANT TO ENROLL?” prompt have been moved from the end of the patient registration screens to the beginning of registration after a new patient has been added to the PATIENT (#2) file. The answer to the “DO YOU WANT TO ENROLL?” prompt is kept in the DGENRYN variable that is now used in several routines downstream from DGREG.

- DGREG—This routine is called when the DG REGISTER PATIENT option is selected. It now asks the “DO YOU WANT TO ENROLL?” questions.
- DPTLK—This is the patient lookup program. It has been changed to disallow the creation of a new patient for the following:
- The use of double-quotes (“).
- The use of DG LOAD PATIENT DATA.
- The use of DG ADMIT PATIENT.
- EN1^DGEN—This existing API has been changed to use the DGENRYN variable to determine whether the patient should be enrolled.
- ENRPAT^DGEN—This API now passes the DGENRYN variable to ENROLL^DGEN.
- ENROLL^DGEN—Is now passed the DGENRYN variable, and passes it on to CREATE^DGENA6.
- CREATE^DGENA6—Is now passed the DGENRYN variable, and passes it on to PRIORITY^DGENELA4. Also, the variable is stored in the PT APPLIED FOR ENROLLMENT (#.14) field, which is a new field that this patch introduced in the PATIENT ENROLLMENT (#27.11) file.
- PRIORITY^DGENELA4—Is now passed the DGENRYN variable, and passes it on to PRI^DGENELA4.
- PRI^DGENELA4—Is now passed the DGENRYN variable, and uses it to return a priority group of NULL if the patient is *not* being enrolled.
- AUTOUPD^DGENA2—This API is called from cross-references in many fields in the PATIENT (#2) file. This patch changes the API to retrieve the new PT APPLIED FOR ENROLLMENT field, and passes it to CREATE^DGENA6 as specified above.
- EDIT^DGENA1A—This API updates the new enrollment record. It has been changed to add the new PT APPLIED FOR ENROLLMENT (#.14) field.
- EN^DG993BO—This routine will be used if there is a need to back out the patch.
- DGENUPL2—This routine is modified to include ZEN segment Fields 16 to 19 in the DGENR array.
- DGENUPL8—This routine is modified to include “REGISTRATION ONLY” status in current and previous enrollments.
- VAFHLZEN—Creation of ZEN segment is enhanced to populate new sequence numbers 16, 17, 18 and 19 with values of:
- PT APPPLIED FOR ENROLLMENT?
- REGISTRATION ONLY REASON
- REGISTRATION ONLY DATE
- SOURCE OF REGISTRATION

The fields listed are located in the PATIENT ENROLLMENT (#27.11) file.

- DGENA1—This routine is modified to retrieve Fields 16 to 19 from ZEN segment and store them in the PATIENT (#2) file.
- DGENA—This routine is modified to enhance the DGENR array to include:
- PT APPLIED FOR ENROLLMENT?
- REGISTRATION ONLY REASON
- REGISTRATION ONLY DATE
- SOURCE OF REGISTRATION

The fields listed are located in the PATIENT ENROLLMENT (#27.11) file.

### Patch DG\*5.3\*1015 Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch DG\*5.3\*1015 includes modifications to DGENA2 and DGENACL2 to reverse the Primary Care Appointment change to the NEAR Call List \[DGEN NEACL MGT RPT1\] option and NEAR Tracking Report \[DGEN NEACL MGT RPT2\] option introduced in DG\*5.3\*982. The requirement to only remove and update a patient on these reports if the patient has a Primary Care Appointment has been removed.

In addition, DGENDD was modified to fix a defect in the VERIFY FIELDS option of the UTILITY FUNCTIONS in VA FileMan.

### Patch DG\*5.3\*1014 Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch includes new routine VAFHLZCE to build the VA-Specific Community Care Eligibility Segment (ZCE) with five fields. Data is retrieved from the PATIENT (#2) file, subfile (#2.191). Modified routine IVMPTRN8 to include ZCE segments returned from VAFHLZCE in the ORU/ORF-Z07 HL7 message; modified routine DGENUPL1 to take ZCE segment(s) in ORU/ORF-Z11 and initiate validations; modified routine DGENUPLB to parse and validate four fields in the ZCE segments and store the fields in an array for storing in the PATIENT (#2) file; and modified routine DGENUPL7 to store the validated four fields retrieved from the ZCE segments in the PATIENT (#2) file, sub-file (#2.191).

This patch also added new routine DGRP1152A for functionality to add, edit, and remove Community Care Programs, and new routine DGRP1152U for help text. This patch modified routine DGRPH to add functionality for Collateral Programs.

This patch also modified routines to add standardized patient data to screen banners and to add the PREFERRED NAME (#.2405) field from the PATIENT (#2) file to the NAME (#.01) field prompt of the PATIENT (#2) file: DGDEP, DGDEPE, DGR111, DGR113, DGR1131, DGR114, DGRP1, DGRP11B, DGRP2, DGRP6, DGRP61, DGRP62, DGRPCF, DGRPU, DPTLK, DGRP6EF and DGRP6CL.

Routines DGREGAED, DGREGRED, DGREDTED were modified to call the Universal Address Module (UAM) Address Validation code. The UAM Address Validation code is contained in 3 new routines: DGADDVAL, DGADDLST, and DGUAMWS.

DGUAMWS invokes the UAM Address Validation web service and returns any address candidates in an array. DGADDLST uses the list template DGEN ADDR VALID to display the address candidates to the user for selection. DGADDVAL is the driver routine that calls DGUAMWS and, if any results are returned, calls DGADDLST for display and selection of the validated address.

> **NOTE:** When running the ^XINDEX routine, sites will encounter an XINDEX error after the installation of this patch. Routine DGUAMWS uses HealtheVet Web Services Client (HWSC). It calls a Cache Class to parse the eXtensible Markup Language (XML) document returned by the web service call. A Standards and Exemptions (SAC) Exemption (ID 20200806-01) was approved on 08/06/2020.

The errors reported by XINDEX are:

DGUAMWS \* \* 198 Lines, 11474 Bytes, Checksum: B105727101

S DGHTTPREQ.SSLCheckServerIdentity = 0

EN+24 S - Vendor specific code is restricted.

EN+24 F - Unrecognized argument in SET command.

EN+24 F - UNDEFINED COMMAND (rest of line not checked).

D DGHTTPREQ.EntityBody.Write(DGJSON) ; places the entire json

string into EntityBody

EN+28 S - Vendor specific code is restricted.

F DGHEADER="Accept","ContentType" D

DGHTTPREQ.SetHeader(DGHEADER,"application/json")

EN+29 S - Vendor specific code is restricted.

D DGHTTPREQ.SetHeader("ContentType","application/json")

EN+30 S - Vendor specific code is restricted.

S DGHTTPRESP=DGHTTPREQ.HttpResponse

EN+35 S - Vendor specific code is restricted.

S DGDATA=DGHTTPRESP.Data.ReadLine() ; reads json string

response from the data stream.

EN+36 S - Vendor specific code is restricted.

Q DGSTAT\_"^"\_\$\$RSPMSG(DGHTTPRESP.StatusCode,.DGRESPMSG)

EN+44 S - Vendor specific code is restricted.

N DGERRCODE S DGERRCODE=DGRESPERR.code

ERRRSPMSG+4 S - Vendor specific code is restricted.

#### HWSC Configuration

The UAM Address Validation web server DG UAM AV SERVER and two services, DG UAM AV VALIDATE and DG UAM AV CANDIDATE, are configured by a post-install routine. This routine creates entries in the HWSC configuration files to define these.

Example:

<u>Web Server Manager Aug 13, 2020@08:31:46 Page: 1 of 1</u>

Web Server Manager Aug 13, 2020@08:31:46 Page: 1 of 1

HWSC Web Server Manager

Version: 1.0 Build: 9

ID Web Server Name IP Address or Domain Name:Port

1 \*DG UAM AV SERVER REDACTED:443 (SSL)

2 \*DST GET ID SERVER REDACTED:443 (SSL)

3 \*PCMMR REDACTED:80

4 \*PCMMR TEST REDACTED:10100

5 PSO WEB SERVER :80

6 \*VIAA VISTA TRIGGER SERVER :REDACTED (SSL)

Legend: \*Enabled

AS Add Server TS (Test Server)

ES Edit Server WS Web Service Manager

DS Delete Server CK Check Web Service Availability

EP Expand Entry LK Lookup Key Manager

Select Action:Quit// WS Web Service Manager

Web Service Manager Aug 14, 2020@07:19:44 Page: 1 of 1

HWSC Web Service Manager

Version: 1.0 Build: 9

ID Web Service Name Type URL Context Root

1 CDS WEB SERVICE REST cds-wsclient/cds-service

2 DG UAM AV CANDIDATE REST services/address_validation/v2/cand...

3 DG UAM AV VALIDATE REST services/address_validation/v1/vali...

4 DST GET ID SERVICE REST vs/v2/consultFactor

5 PCMM-R GET PC INFO REST REST pcmmr_web/ws/patientSummary

6 PSO ERX WEB SERVICE REST /INB-ERX/

7 VIAA VISTA TRIGGER SERVIC REST esb/assettrax/services/vistatrigger

Enter ?? for more actions

AS Add Service

ES Edit Service

DS Delete Service

EP Expand Entry

Select Action:Quit//

Select OPTION NAME:

If the following errors are seen in the error log when using the UAM Service, the server settings should be reverified. Please refer to the DG_53_P1014.KID Deployment, Installation, Back-out, and Rollback Guide for detailed instructions on verifying that the post-install routine set up the server and associated services correctly.

WRONG PORT NUMBER OR ENDPOINT (IP)

Process ID:  1302  (1302)               AUG 26, 2020 08:43:45

UCI/VOL: \[DEVVOO:DEVR0TSVR\]            

\$ZA:   0                                \$ZB: \013

Current \$IO: /dev/pts/22                Current \$ZIO: REDACTED^17^44^/dev/

pts/22

\$ZE= \<ENDOFFILE\>

Last Global Ref: ^%qCacheMsg("%ObjectErrors","en",6059)

S @%ZTERRT@("LINE")=\$STACK(%2,"MCODE")

WRONG SSL CONFIGURATION OR SERVER NOT SET UP

Process ID:  1302  (1302)               AUG 26, 2020 08:51:10

UCI/VOL: \[DEVVOO:DEVR0TSVR\]            

\$ZA:   0                                \$ZB: \013

Current \$IO: /dev/pts/22                Current \$ZIO: REDACTED^17^44^/dev/

pts/22

\$ZE= \<WRITE\>zSend+186^%Net.HttpRequest.1

Last Global Ref: ^%qCacheMsg("%ObjectErrors","en",6085)

SERVICES NOT SET UP CORRECTLY

Process ID: 23364 (23364) AUG 26, 2020 15:07:17

UCI/VOL: \[DEVVOO:DEVR0TSVR\]

\$ZA: 0 \$ZB: \013

Current \$IO: /dev/pts/12 Current \$ZIO: REDACTED^28^99^/dev/

pts/12

\$ZE= \<ECODETRAP\>zforceError+3^xobw.error.DialogError.1

Last Global Ref: ^XOB(18.02,"B","MPI_PSIM_EXECUTE",0)

set \$ECODE=",UXOBW," }

### Patch DG\*5.3\*952 Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch implements VistA modifications to assist the Department of Veterans Affairs (VA) in addressing the high rate of suicides among the nation's Veterans; specifically, former service members that have an administrative discharge of Other Than Honorable (OTH) needing emergent mental healthcare services. The patch implements the special eligibility for the population that falls into the OTH-EMERGENT (OTH-90) category.

The following modified routines are exported by patch DG\*5.3\*952:

- DGENA
- DGENA1A
- DGENELA
- DGENELA1
- DGENELA4
- DGENU
- DGENUPL
- DGENUPL1
- DGENUPL4
- DGENUPL5
- DGENUPL7
- DGENUPL8
- DGENUPLA
- DGENUPLB
- DGRP7
- DGRPC
- DGRPC3
- DGRPCE
- DGRPCE1
- DGRPE1
- VADPT0
- VADPT4
- VAFHLZE1

The following new routines are exported by DG\*5.3\*952:

- DGOTHBTN
- DGOTHD
- DGOTHD1
- DGOTHD2
- DGOTHEL
- DGOTHINQ
- DGOTHMG1
- DGOTHMG2
- DGOTHMGT
- DGOTHRP1
- DGOTHRP2
- DGOTHRP3
- DGOTHRP4
- DGOTHRP5
- DGOTHRP6
- DGOTHRPT
- DGOTHUT1
- VAFHLZTE

### Patch DG\*5.3\*977 Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The patch implements the special eligibility for the population that falls into OTH-EXTENDED category and also implements a new PRESUMPTIVE PSYCHOSIS indicator prompt and database field to capture patients seen under the Presumptive Psychosis authority.

The following modified routines are exported by patch DG\*5.3\*977:

- DGENUPL7
- DGENUPLB
- DGOTHBTN
- DGOTHD
- DGOTHD1
- DGOTHEL
- DGOTHMG2
- DGOTHRP1
- DGOTHRP2
- DGOTHRP3
- DGOTHRP5
- DGOTHRP6
- DGOTHRPT
- DGRP7
- VAFHLZTE

The following new routines are exported by DG\*5.3\*977:

- DGOTHMST
- DGPPRP1
- DGPPRP2
- DGPPRP3
- DGPPRP4
- DGPPRP5
- DGPPSYCH

### Patch DG\*5.3\*1016 Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The patch:

\- Provides changes for 'Reevaluate Eligibility' Mailman messages that are sent for patients registered as 'OTH' patients.

\- Provides a fix to ensure that the Patient Inquiry (OTH) \[DG OTH PATIENT INQUIRY\] option displays an ACTIVE OTH status if the patient transitions from OTH Emergent to OTH Extended and displays the correct current Primary Eligibility.

The following modified routines are exported by patch DG\*5.3\*1016:

- DGOTHD1
- DGOTHINQ
- DGOTHMST
- DGRP7

### Patch DG\*5.3\*1025 Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch introduces reports to identify Former Service Members whose Primary Eligibility changed from EXPANDED MH CARE NON-ENROLLEE to a new Primary Eligibility with a verified eligibility status. These patients are no longer treated under the Other Than Honorable (OTH) authority (VHA Directive 1601A.02).

The following new routines are exported by DG\*5.3\*1025:

- DGOTHFS2
- DGOTHFSM

### Patch DG\*5.3\*1029 Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch implements the code to provide data to the CPRS application in order to:

· Identify patients eligible for Presumptive Psychosis (PP) benefits and display details about their status.

· Identify patients with inactive PRF records and list the history of the PRF changes.

The following new routines are exported by DG\*5.3\*1029:

- DGOTHBT2
- DGPPAPI

### Patch DG\*5.3\*1034 Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch includes modifications and updates to Former OTH Patient Eligibility Change Report and Former OTH Patient Detail Reports to include patient’s Episodes of Care (Outpatient, Inpatient, and Prescriptions).

Additionally, this patch introduces a new report that would help identify veterans that registered for Presumptive Psychosis benefits.

The following modified routines are exported by DG\*5.3\*1034:

- DGOTHFS2
- DGOTHFSM

The following new routines are exported by DG\*5.3\*1034:

- DGFSMOUT
- DGOTHFS3
- DGOTHFS4
- DGPPRRP1
- DGPPRRPT

### Patch DG\*5.3\*1035 Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch includes modifications and updates to the Former OTH Patient Eligibility Change Report, Former OTH Patient Detail Reports, Presumptive Psychosis Reconciliation Report to include prescription Partial Fill.

Additionally, this patch introduces a new report that generates a report of an individual patient treated under Presumptive Psychosis authority within the user specified date range. This would help identify veterans that registered for Presumptive Psychosis benefits.

This patch also adds any localized messaging text to the OTH button in CPRS if it is populated for the patient.

The following modified routines are exported by DG\*5.3\*1035:

- DGFSMOUT
- DGOTHBT2
- DGOTHBTN
- DGOTHFS2
- DGOTHFS3
- DGOTHFS4
- DGOTHFSM
- DGPPRRP1
- DGPPRRPT

The following new routines are exported by DG\*5.3\*1035:

- DGPPDRP1
- DGPPDRPT
- DGPPDRX
- DGPPOHUT

### Patch DG\*5.3\*1027 Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch modifies routines DGREG and DGCOL to no longer the display the list of reasons, from the PATIENT REGISTRATION ONLY REASON (#408.43) file, before the SELF-REPORTED REGISTRATION ONLY REASON prompt in the DG REGISTER PATIENT and DG COLLATERAL PATIENT options.

This patch also modifies routine DGEN1 to disable the Enroll Patient (EP) Action protocol DGEN PATIENT ENROLLMENT option. A message is displayed instructing the user to use the Enrollment System to complete the patient’s enrollment.

In addition, the following modified routines are exported by patch DG\*5.3\*1027:

- DGCOL
- DGDIS
- DGEN
- DGEN1
- DGENA1
- DGENA1A
- DGENA3
- DGENUPL2
- DGENUPL7
- DGREG
- DGRPC
- DGRPCF
- DGRPP

The following new routines are exported by patch DG\*5.3\*1027:

- DG531027P
- DGREGEEWS

### Patch DG\*5.3\*1044 Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch DG\*5.3\*1044 adds new branch of service, SPACE FORCE, to the BRANCH OF SERVICE file (#23) and changes the name of the entry AIR FORCE--ACTIVE DUTY in the PERIOD OF SERVICE file (#21) to USAF, USSF – ACTIVE DUTY.

This patch modifies routines CMP^DGRP61, CMP^DGRPE, and VALCOM^DGRPMS to allow all service components to display at the SERVICE COMPONENT: prompt when the Military Service Episode has a BRANCH OF SERVICE of SPACE FORCE.

In addition, the post-install routine, DG531044P, is created to re-compile templates associated with the modification to the NUMBER field (#.001) of the BRANCH OF SERVICE file (#23). This field has been modified to accept an additional entry.

### Patch DG\*5.3\*1047 Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch includes modifications and updates to the billing of Former Other Than Honorable (OTH) Patient Eligibility Change Report to include the Military Sexual Trauma (MST) column and Presumptive Psychosis Detail Report to update the header of the released prescription section.

This patch introduces the new report Potential Presumptive Psychosis Patient Report \[DG POTEN PRESUMPT PSYCHOSIS\] to identify patients who have been registered in VistA using the Presumptive Psychosis (PP) 'workaround' process since 38 United States Code (USC) 1702 was passed on 3/14/2013. The report is to be used by Registration/Enrollment users to identify PP patients without PP category and select the PP category for them.

Additionally, this patch implements two modifications to support benefits provided by the Deborah Sampson Act for all Former Service Members (FSM) including those eligible for OTH benefits. Per the Deborah Sampson Act, FSMs who experienced MST are eligible for the full range of MST-related care, both mental health and other medical care.

The following modified routines are exported by DG\*5.3\*1047:

- DGOTHBT2
- DGOTHBTN
- DGOTHFS4
- DGOTHFSM
- DGPPDRX

The following new routines are exported by DG\*5.3\*1047:

- DGPOTEN

### Patch DG\*5.3\*1045 Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch DG\*5.3\*1045 modifies the routine DGENUPL7 to not trigger an ORU-Z07 HL7 message when the ENROLLMENT STATUS (#.04) field in the PATIENT ENROLLMENT (#27.11) file is NOT ELIGIBLE;INELIGIBLE DATE and the SOURCE OF ENROLLMENT (#.03) field in the PATIENT ENROLLMENT (#27.11) file is VAMC.

Routine DGEN is modified to retrieve the Ineligible Reason and set the Enrollment Status to 20 (NOT ELIGIBLE;INELIGIBLE DATE) if the Ineligible Date and Ineligible Reason are populated in the patient record. DGENA1A is modified to set the Enrollment Status to 20 for Registration Only Patients when the Ineligible Date is blank. DGENA6 is modified to set the Enrollment Status to “Registration Only” when the Ineligible Date is blank. DGREG is modified with logic to correctly create a patient enrollment record for Ineligible Date.

The consistency checker routine DGRPC is modified to set the Appointment Request fields to null if there is no Ineligible Date.

Routine DGENA2 is modified to retain the existing value for the PT APPLIED FOR ENROLLMENT? (#.14) field in the PATIENT ENROLLMENT (#27.11) file when a new enrollment record is created.

### Patch DG\*5.3\*1056 Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch DG\*5.3\*1056 removes the word “permanent” from the following fields of the PATIENT file (#2): COUNTRY field (# .1173), TEMPORARY PHONE NUMBER field (# .1219), and CONFIDENTIAL ADDR COUNTRY field (# .14116).

DG\*5.3\*1056 updates the DG ADDRESS UPDATE entry in the OPTION file (#19) to replace “(P) permanent address” with “(M) mailing address”.

DG\*5.3\*1056 removes the word “permanent” from displays and prompts in the following routines: DGADDUT2, DGADDUTL, DGFFPLM1, DGREGCP1, DGRP1, DGRPCADD, DGRPD, DGRPE, DGRPH, DGRSTBAD.

### Patch DG\*5.3\*1061 Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch DG\*5.3\*1061 modifies ICR \#10061 for VADPT to include a new component “CAI” for downstream applications to retrieve the COMPACT Act Indicator. The indicator, returned in array VA(“CAI”), is “1” (COMPACT Act Eligible) if the patient is enrolled or if the patient record contains the COMPACT ACT ELIGIBLE eligibility.

The patch also adds 'SPECIAL TX AUTHORITY CARE' and 'COMPACT ACT ELIGIBLE' to the MAS ELIGIBILITY CODE file (#8.1).

The following modified routines are exported by patch DG\*5.3\*1061:

- DGENELA
- DGLOCK1
- DGRP7
- DGRPD
- VADPT

In addition, the post-install routine, DG531061P, is created to add 'SPECIAL TX AUTHORITY CARE' and 'COMPACT ACT ELIGIBLE' to the ELIGIBILITY CODE file (#8).

### Patch DG\*5.3\*1065 Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch DG\*5.3\*1065 modifies routine DGUAMWS, which invokes the UAM Address Validation Service, to retrieve the API Key from the DG UAM API KEY parameter instance in the PARAMETERS file (#8989.5) and place the key in the message header.

### Patch DG\*5.3\*1059 Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VA MPI team in support of Identity Management released patch DG\*5.3\*1059 with the following enhancements:

1.  Two new files in support of the new fields in the PATIENT file (#2). These two files came with data entries:

> .SEXUAL ORIENTATION TYPES (#47.77)

> .PRONOUN TYPES (#47.78)

2.  Five new fields being added to the PATIENT file (#2):

> SEXUAL ORIENTATION (#.025) - Multiple / AVAFC202501 (Pointer to NEW File \#47.77)

> SEXUAL ORIENTATION DESCRIPTION (#.0251) - Free Text / AVAFC0251

> PRONOUN (#.2406) - Multiple / AVAFC2240601 (Pointer to NEW File \#47.78)

> PRONOUN DESCRIPTION (#.24061) - Free Text / AVAFC24061

> INDIVIDUAL TAX ID (#991.11) - NUMBER (900000000 - 999999999) / AVAFC99111

3.  Adding new 'AVAFC' X-REF to now allow MVI to monitor theses existing fields for changes:

> .RESIDENTIAL ADDRESS \[LINE 1\] (#.1151) - AVAFC1151

> .RESIDENTIAL ADDRESS \[LINE 2\] (#.1152) - AVAFC1152

> .RESIDENTIAL ADDRESS \[LINE 3\] (#.1153) - AVAFC1153

> .RESIDENTIAL CITY (#.1154) - AVAFC1154

> .RESIDENTIAL STATE (#.1155) - AVAFC1155

> .RESIDENTIAL ZIP+4 (#.1156) - AVAFC1156

> .RESIDENTIAL PROVINCE (#.11571) - AVAFC11571

> .RESIDENTIAL POSTAL CODE (#.11572) - AVAFC11572

> .RESIDENTIAL COUNTRY (#.11573) - AVAFC11573

4.  Modification of the DEMUPD^VADPT and DEM^VADPT to include the new fields related to sexual orientation and gender identity (SOGI).
5.  Modification of the Patient Inquiry \[DG PATIENT INQUIRY\] option to always display gender and label residential and correspondence address fields correctly.
6.  Modification of the Remote Procedure calls \[VAFC REMOTE PDAT\] and \[VAFC REMOTE AUDIT\]to ensure that lines exceeding 255 characters are not being truncated,
7.  Enhancement to the HL7 version 2.4 PID and OBX segment builders to handle the new fields added in this patient, as well as both residential and correspondence address fields

> Routines modified in DG\*5.3\*1059:

> DGRPD

> VADPT0

> VADPT1

> VAFCHFS

> VAFCPDAT

> VAFCPTED

> VAFCQRY

> VAFCQRY1

> VAFCSB

> VAFCTR

### Patch DG\*5.3\*1067 Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch DG\*5.3\*1067 modifies ICR \#10061 for the Callable Entry Point OAD^VADPT. The new RELATIONSHIP TYPE is added to the output array in the tenth node (e.g., VAOA(10)="HUSBAND"), replacing the RELATIONSHIP TO PATIENT. The RELATIONSHIP TO PATIENT is moved to the new 12<sup>th</sup> node of the output array (e.g., VAOA(12)="Ex-husband").

DG\*5.3\*1067 adds five new fields to the PATIENT file (#2). These fields will contain pointers to the new PATIENT CONTACT RELATION file (#12.11):

- K-RELATIONSHIP TYPE (#.224)
- K2-RELATIONSHIP TYPE (#.2104)
- E-RELATIONSHIP TYPE (#.3309)
- E2-RELATIONSHIP TYPE (#.331015)
- D-RELATIONSHIP TYPE (#.34015)

Patch DG\*5.3\*1067 includes updates adding the new Relation Type and Relation Note prompts to the EMERGENCY CONTACT DATA, SCREEN \<3\> screen.

The following modified routines are exported by patch DG\*5.3\*1067:

- DG531067P – Post install routine for VHAP renames, modify Parameter Definitions
- DGDDC – Insure new Next of Kin fields are cleaned up when the contact is deleted
- DGDDDTTM – Trigger Date/Time Cross References
- DGREG – Logic added to handle new Registration Only Reasons
- DGRP3 – Emergency Contact Data, Screen 3 modifications
- DGRPD1 – Update to the Patient Inquiry option
- DGRPE – Updated to handle Emergency Contact Data, Screen 3 processing
- DGRRPSKN – Modifications for the Remote Procedure Call (RPC) Patient Services Contact Information
- VADPT1 – Additional fields added to VADPT API
- VAFHLZCT – Add Relationship Types to the ZCT segment

### Patch DG\*5.3\*1071 Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VA MPI team in support of Identity Management released patch DG\*5.3\*1071 with the following enhancements:

1.  Four new fields with cross-references (X-REF) being added to the SEXUAL ORIENTATION (#2.025) multiple in the PATIENT file (#2):

. STATUS (#.02) - SET OF CODES / AUDITED / AVAFC202502

Sorting X-REF: AHIST

. DATE CREATED (#.03) - DATE / AVAFC202503

Lookup/Sorting X-REFs: G202501 / G202503

Sorting X-REF: AHIST

. DATE LAST UPDATED (#.04) - DATE / AUDITED / AVAFC202504

Lookup/Sorting X-REFs: G202502 / G202504

Sorting X-REF: AHIST

. NOTE (#.05) - POINTER / AUDITED

(\*Pointer to the TIU DOCUMENT (#8925) file)

Sorting X-REF: AHIST

. TYPE OF UPDATE (#.06) - SET OF CODES

Sorting X-REF: AHIST

2.  Modification of the DEMUPD^VADPT and DEM^VADPT to include the new additional Sexual Orientation fields.
3.  Modification of the Patient Inquiry \[DG PATIENT INQUIRY\] and \[RG EXCEPTION TF INQUIRY\] options to display the additional Sexual Orientation fields.
4.  Enhancement to the HL7 version 2.4 OBX segment builders to handle the new additional Sexual Orientation fields added for a patient.
5.  New Application Programming Interface (API) was created to allow adding/updating/validation of the Sexual Orientation fields in the multiple for the patient’s record. \[Private ICR \#7323 created in FORUM\]
6.  Modification of the \[RG EXCEPTION TF INQUIRY\] option to display the Work and Cell phone numbers for the patient if applicable.
7.  Modification of the \[RG EXCEPTION TF INQUIRY\] option to display the Correspondence and Foreign residential address information correctly/completely.

Routines added in DG\*5.3\*1071:

- DG1071P
- VAFCPAI

Routines modified in DG\*5.3\*1071:

> DGRPD

> VADPT1

> VAFCPDAT

> VAFCPDAT

> VAFCPTED

> VAFCSB

> VAFCTR

### Patch DG\*5.3\*1075 Routines 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Added Pre/Post install routine DG531075P: A new parameter DG PATCH DG\*5.3\*1075 ACTIVE is added to the PARAMETER DEFINITION (#8989.51) file. A timestamp value of August 3rd, 2022, 17:00 is stored in this parameter indicating when the new Housing and Urban

Development – Veterans Affairs Supportive Housing (HUD-VASH) eligibility code will be active. This routine also modifies the Server Host (endpoint) and Port Number for the DG EE SUMMARY SERVER web server.

The following routines are exported by patch DG\*5.3\*1075:

- DGLOCK1 – Block entry in PRIMARY ELIGIBILITY CODE prompt

> Prevents the entry of HUD-VASH eligibility code in the PRIMARY ELIGIBILITY CODE prompt on the ELIGIBILITY STATUS DATA, SCREEN \<7\>.

- DGREG.INT – Fix line 1 for SAC compliance

> Added spacing after initials on Routine Name line of routine.

- DGRP3.INT – SAC compliance

> Correct second line of routine for SAC compliance, remove extraneous slashes.

- DGRP6EF.INT – Changes for Environmental Factors screens

> Updates A/O Exposure processing on the ENVIRONMENTAL FACTORS screen.

- DGRP7.INT – Change displayed output

> The “Aid & Attendance”, “Housebound”, and the “VA Pension” prompts, on the ENVIRONMENTAL FACTORS screen for example, now display NO instead of UNANSWERED for non-Veterans.

- DGRP7CP.INT – Change displayed answers for non-Veterans

> The “Aid & Attendance”, “Housebound”, and the “VA Pension” prompts now display NO instead of UNANSWERED or NULL for non-Veterans.

- DGRPCE.INT – Add default responses

> The RECEIVING A&A BENEFITS? field (#.36205), RECEIVING HOUSEBOUND BENEFITS? field (#36215), RECEIVING A VA PENSION? field (#.36235), of the PATIENT file (#2), prompt’s defaults are set to NO only for non-Veterans.

- DGRPCE1.INT – Limit additional prompts based on response

> If “RADIATION EXPOSURE INDICATED?” field (#.32103) is not YES no additional prompts will display. In addition, “RADIATION EXPOSURE METHOD” field (#.3212) is changed to a required field.

### Patch DG\*5.3\*1064 Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch DG\*5.3\*1064 adds Group 6 to the PATIENT DATA, SCREEN \<2\>. Group 6 consists of the following prompts: “Indian:”, “Start Date:”, “Attestation Date:” and “End Date:”.

It modifies ICR \#10061 and \#7109 for VADPT to include new entries in the “DEM” and “DEMUPD” component arrays. Node 15, subnodes 1-4, will contain Indian Attestion responses from PATIENT DATA, SCREEN \<2\>, Group 6.

Six additional fields are added to the PATIENT (#2) file:

- INDIAN SELF IDENTIFICATION (#.571)
- INDIAN START DATE (#.572)
- INDIAN ATTESTATION DATE (#.573)
- INDIAN END DATE (#.574)
- INDIAN SELF IDENT CHANGE DT/TM (#.575)
- INDIAN SELF IDENT CHANGE USER (#.576)

This patch updates VistA to receive patient Indian attestation information from ES in the ZPD segment of the HL7 ORU/ORF-Z11 message.

The following modified routines are exported by patch DG\*5.3\*1064:

- DGENELA2
- DGENPTA1
- DGENUPLA
- DGMTSC4
- DGMTSC4V
- DGMTSCC
- DGMTSCR
- DGRP2
- DGRPD
- DGRPDB
- DGRPE
- DGRPH
- DGRPV
- VADPT0
- VADPT1
- VAFHLZPD

### Patch DG\*5.3\*1081 Routines 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch DG\*5.3\*1081 changes DATA GROUP 1 on the INELIGIBLE/MISSING DAT SCREEN \<10\> to UNEDITABLE. The TWX prompts, “TWX Source:”, “TWX City:”, and “TWX State:” are removed.

It modifies the VHA Profile (VHAP) LONG DESCRIPTION of VETERAN RESTRICTED MED BENEFITS, NON VETERAN OTHER RESTRICTED MED BENEFITS and INELIGIBLE entries in HEALTH BENEFITS PLAN file (#25.11).

Adds a new entry, CLINICAL EVALUATION, to the VistA MAS ELIGIBILITY CODE file (#8.1) and ELIGIBILITY CODE (#8).

Sets the field USE FOR Z07 CHECK: to NO for the INEL REASON UNSPECIFIED entry in the INCONSISTENT DATA ELEMENTS file (#38.6).

Six fields in the PATIENT file (#2) are made UNEDITABLE and their LONG DESCRIPTION fields are updated to indicate this change:

- INELIGIBLE DATE (#2,.152)
- INELIGIBLE TWX SOURCE (#2,.1651)
- INELIGIBLE TWX CITY field (#2.1653)
- INELIGIBLE TWX STATE (#2.1654)
- INELIGIBLE VARO DECISION (#2.1656)
- INELIGIBLE REASON field (#2.307)

Updates the LONG DESCRIPTION field in three entries in the HEALTH BENEFIT PLAN (#25.11) file:

- VETERAN RESTRICTED MED BENEFITS (#222)
- NON VETERAN OTHER RESTRICTED MED BENEFITS (#223)
- INELIGIBLE (#290)

The following modified routines are exported by patch DG\*5.3\*1081:

- DGRP10
- DGRPV
- DGRPC
- DG531081P
- DGLOCK1

### Patch DG\*5.3\*1082 Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch DG\*5.3\*1082 changes DATA GROUP 3 on the ELIGIBILITY STATUS DATA, SCREEN \<7\>. The PRESUMPTIVE PSYCHOSIS prompts are no longer displayed. The Presumptive Psychosis: label will display when populated and will not be editable in VistA.

In the HEALTH BENEFIT PLAN (#25.11) file, DG\*5.3\*1082 modifies the VHA Profile (VHAP) LONG DESCRIPTION of RESTRICTED EXAMINATION ONLY (#224), VETERAN RESTRICTED MED BENEFITS (#222), and NON VETERAN OTHER RESTRICTED MED BENEFITS (#223) entries and the LONG DESCRIPTION (#.04), SHORT DESCRIPTON (#.03) and the COVERAGE CODE (#.05) fields of the PRESUMPTIVE (38 USC 1702-38 CFR 17.109) (#135), and the CLINICAL EVALUATION (#308) entries.

DG\*5.3\*1082 modifies the DG LOAD EDIT SCREEN 7 entry in the INPUT TEMPLATE (#.402) file to remove the PRESUMPTIVE PSYSCHOSIS? and PRESUMPTIVE PSYSCHOSIS CATEGORY: prompts from the ELIGIBILITY STATUS DATA, SCREEN \<7\> screen in DATA GROUP \[3\].

DG\*5.3\*1082 adds the new PRESUMPTIVE PSYCHOSIS ELIGIBLE eligibility code to the MAS ELIGIBILITY CODE (#8.1) file.

DG\*5.3\*1082 adds the new PRESUMPTIVE PSYCHOSIS ELIGIBLE eligibility code to the ELIGIBILITY CODE (#8) file.

A post install routine, DG531082P, will send an HL7/Z07 message to VES for each VistA patient with a non-null value in PRESUMPTIVE PSYCHOSIS CATEGORY field (Field \#.5601) of the PATIENT file (File \#2).

The following modified/created routines are exported by patch DG\*5.3\*1082:

- DGLOCK1 – Prevents PRESUMPTIVE PSYCHOSIS ELIGIBLE eligibility as a primary eligibility code
- DGPPSYCH – Comments out obsolete YN API tag code and adds new PT API tag code to update PATIENT (#2) file field PRESUMPTIVE PSYCHOSIS CATEGORY (#.5601) and PRESUMPTIVE PSYCHOSIS CATEGORY (#33.1) file
- DG531082P– Post install routine for VHAP updates and send HL7/Z07 messages for current presumptive psychosis patients
- DGENUPL7 – File the Health Factor Segment (ZHF) data
- DGENUPL1 – Parses the HL7 ZHF segments
- DGENUPLB – Process ZHF segment
- VAFHLZHF – Create generic HL7 Enrollment (ZHF) segment
- DGRP7 – Removes the check for Veterans to have the Presumptive Psychosis field displayed

Patch IVM\*2.0\*208, included in the DG\*5.3\*1082 Host File, creates the new optional ZHF segment of the Health Level 7 (HL7) ORF/ORU-Z07 message to send Presumptive Psychosis data. It includes routine IVMPTRN8. This routine creates the optional ZHF segment.

### Patch DG\*5.3\*964 Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch DG\*5.3\*964 includes new routines DGAUDIT, DGAUDIT1, DGAUDIT2, DGAUDI,3 and DGAUDITP.A

Routines DGAUDIT and DGAUDIT1 process entries in the DG VAS QUEUE file (#46.3), using the DG VAS WEB SERVICE entry in the WEB SERVICE file (#18.02) to send the records to the VAS REST API defined by the DG VAS WEB SERVER entry in the WEB SERVER file (#18.12).

Routines DGSEC and DGSEC4 were modified to invoke VistA Audit Solution (VAS) subroutines that add an entry in the DG VAS QUEUE file (#46.3).

This patch implements the VistA Audit Solution (VAS) product that is designed to capture create, read, update, and delete (CRUD) operations on Personally Identifiable Information (PII) and Protected Health Information (PHI). VAS utilizes an external database storage system in the Veterans Affairs Enterprise Cloud (VAEC) Amazon Web Services (AWS) Cloud.

Modified Routine:

- DGSEC
- DGSEC4-

New Routines:

- DGAUDIT
- DGAUDIT1
- DGAUDIT2
- DGAUDIT3
- DGAUDITP

Options:

- Display VAS Parameters \[DG VAS DISPLAY\]
- Export new AUDIT records to external archive \[DG VAS EXPORT\]
- VistA Audit Solution (VAS) options \[DG VAS MENU\]
- Modify VAS Parameters \[DG VAS MODIFY\]

### Patch DG\*5.3\*1090 Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch DG\*5.3\*1090 changes DATA GROUP 3, Exposure Factors, on the MILITARY SERVICE DATA, SCREEN \<6\>. On the ENVIRONMENTAL FACTORS sub-screen the A/O Exp. and ION Rad. have been made uneditable.

Patch DG\*5.3\*1090 adds the following additional values to the AGENT ORANGE EXPOSURE LOCATION field (#.3213) list of SET values in the PATIENT file (#2): T:THAILAND(U.S. OR ROYAL THAI MIL BASE), L:LAOS, C:CAMBODIA(MIMOT OR KREK,KAMPONG CHAM), G:GUAM, AMERICAN SAMOA, OR TERRITORIAL WATERS, J:JOHNSTON ATOLL

Patch DG\*5.3\*1090 adds the following additional values to the AGENT ORANGE EXPOSURE LOCATION field (#50.22) list of SET values in the PATIENT ENROLLMENT file (#27.11): T:THAILAND(U.S. OR ROYAL THAI MIL BASE), L:LAOS, C:CAMBODIA(MIMOT OR KREK,KAMPONG CHAM), G:GUAM, AMERICAN SAMOA, OR TERRITORIAL WATERS, J:JOHNSTON ATOLL

Patch DG\*5.3\*1090 adds to the list of SET values for the RADIATION EXPOSURE METHOD field (Field \#.3212) of the PATIENT file (#2) the following: 8: ENEWETAK, 9: EXPOS IN PALOMARES B52, 10: THULE AFB B52.

Patch DG\*5.3\*1090 replaces the DESCRIPTION for the RADIATION EXPOSURE METHOD field (#.3212) of the PATIENT file (#2) with the following text:

This field represents the method by which the exposure to ionizing radiation occurred.

2\) Hiroshima/Nagasaki - if the Veteran was exposed to ionizing

radiation as a POW or while serving in Hiroshima and/or Nagasaki,

Japan from August 6, 1945 through July 1, 1946.

3\) Atmos Nuclr Testing - if exposure occurred at an atmospheric

nuclear device test site (e.g. the Pacific Islands, NM or NV).

4\) H/N and Atmos Testing - if exposure occurred as a POW in

Hiroshima or Nagasaki AND at an atmospheric nuclear device test

site.

5\) Undergrd Nuclr Testing - if exposure occurred while at Longshot,

Milrow, or Cannikin underground nuclear tests at Amchitka Island,

AK prior to January 1, 1974.

6\) Expos at Nuclr Facility - if exposure occurred while at

Department of Energy plants at Paducah, KY, Portsmouth, OH or the

K25 area at Oak Ridge, TN for at least 250 days before February 1,

1992\.

7\) Other - a method that does not fit any of the other categories.

8\) Enewetak - if exposure occurred during cleanup of Enewetak

Atoll, from January 1, 1977, through December 31, 1980.

9\) Expos in Palomares B52 - if exposure occurred during cleanup of

the Air Force B-52 bomber carrying nuclear weapons off the coast of

Palomares, Spain, from January 17, 1966, through March 31, 1967.

10\) Thule AFB B52 - if exposure occurred during the response to the

fire onboard an Air Force B-52 bomber carrying nuclear weapons

near Thule Air Force Base in Greenland from January 21, 1968, to

September 25, 1968.

Only Veterans exposed by methods \#2, 3, 4, 8, 9, or 10 are eligible

for copayment exemption or enrollment in priority 6 based on their

Ionizing Radiation exposure.

Only Veterans Health Administration Enrollment System users may

enter/edit this field.

Patch DG\*5.3\*1090 adds to the list of SET values for the RADIATION EXPOSURE METHOD field (#76) in the PATIENT ENROLLMENT file (#27.11): 8: ENEWETAK, 9: EXPOS IN PALOMARES B52, 10: THULE AFB B52.

Patch DG\*5.3\*1090 uses the following abbreviations for the new AGENT ORANGE EXPOSURE LOCATION displays on the ENVIRONMENTAL FACTORS sub-screen, of DATA GROUP \[3\] of the MILITARY SERVICE DATA, SCREEN \<6\>: THAILAND(U.S. OR ROYAL THAI MIL BASE):(THLD), LAOS:(LAOS), CAMBODIA(MIMOT OR KREK,KAMPONG CHAM):(CAMB), GUAM, AMERICAN SAMOA, OR TERRITORIAL WATERS:(GUAM), JOHNSTON ATOLL:(JHST)

Patch DG\*5.3\*1090 displays the entire text of the AGENT ORANGE EXPOSURE LOCATION field on the Patient Enrollment and Patient Enrollment History screens.

Patch DG\*5.3\*1090 modifies the CHECK/DON'T CHECK field (#5) and USE FOR Z07 CHECK field (#6) in the INCONSISTENT DATA ELEMENTS file (#38.6) for entries 25 AO CLAIMED W/OUT VIETNAM POS and 507 RAD EXPOSURE METHOD INVALID.

The following modified/created routines are exported by patch DG\*5.3\*1090:

- DGCV – PACT Act - additional check added for special enrollment period
- DGCVRPT – Changed dates to from 11/11/1998 to 09/30/2013 used in calculating the CV End date
- DGENEGT1 – Additional AGENT ORANGE EXPOSURE LOCATION names added - T=THAILAND(U.S. OR ROYAL THAI MIL BASE), L=LAOS, C=CAMBODIA(MIMOT OR KREK,KAMPONG CHAM), G=GUAM, AMERICAN SAMOA, OR TERRITORIAL WATERS and J=JOHNSTON ATOLL
- DGENELA4 – add additional values for RADIATION EXPOSURE METHOD field (#27.11,76) for PRIORITY 6; 8 for ENEWETAK, 9 for EXPOS IN PALOMARES B52, 10 for THULE AFB B52. Add additional values for AGENT ORANGE EXPOSURE LOCATION: - T=THAILAND(U.S. OR ROYAL THAI MIL BASE), L=LAOS, C=CAMBODIA(MIMOT OR KREK,KAMPONG CHAM), G=GUAM, AMERICAN SAMOA, OR TERRITORIAL WATERS and J=JOHNSTON ATOLL.
- DGENL1 – Remove A/O Exp Loc: label and shift AGENT ORANGE EXPOSURE LOCATION 17 to the left
- DGENUPLA – Add additional Radiation Exposure codes
- DGRP6EF.INT – Changes for ENVIRONMENTAL FACTORS screen, making A/O Exp. and ION Rad. un-editable.
- VADPT4 – Modify the RADIATION EXPOSURE METHOD (#2,.3212) to get updated field definitions
- VAFHLZE1 – Modify to accommodate two-digit Radiation Exposure Methods

### Patch DG\*5.3\*1093 Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch DG\*5.3\*1093 adds five new entries to the RELIGION file (#13):

- AFRICAN AMERICAN EPISCOPAL (code 84)
- BUDDHISM, OTHER (code 85)
- EVANGELICAL (code 86)
- HOLINESS CHURCHES (code 87)
- CATHOLIC (NON-ROMAN CATHOLIC) (code 88)

Patch DG\*5.3\*1093 changes the NAME field (#.01) of the existing entry with a CODE field (#3) of 28 in the RELIGION file (#13). It is changed from UNITARIAN-UNIVERSALISM to UNITARIAN-UNIVERSALIST. A separate entry was created for UNITARIAN-UNIVERSALISM (code 89) to use to capture the UNITARIAN-UNIVERSALISM (code 28) which was replaced by UNITARIAN-UNIVERSALIST (Code 28).

Patch DG\*5.3\*1093 modifies the file description of the RELIGION file (#13). The "currently contains 84 entries" phrase is changed to "currently contains 90 entries". Also, the typo "affects" is changed to "effects":

> DESCRIPTION: The RELIGION file currently contains 90 entries.

> These entries are determined by VACO MAS. This file should not be

> added to nor should entries in it be altered or deleted by the

> facility. Entry, edit or deletion of these entries could have

> severe negative effects on the performance of the MAS module.

In the DG\*5.3\*1093 patch, the INDIAN SELF IDENTIFICATION field (#.571) and the INDIAN ATTESTATION DATE field (#.573) of the PATIENT file (#2) have the triggers removed which queued an ORU-Z07 HL7 message to be sent to VES.

Patch DG\*5.3\*1093 sets the Write Authority flag in the INDIAN SELF IDENTIFICATION (#.571) and the INDIAN ATTESTATION DATE (#.573) fields of the PATIENT file (#2).

Patch DG\*5.3\*1093 removes all Indian Attestation data from patients’ records in the PATIENT file (#2).

Patch DG\*5.3\*1093 modifies the PATIENT DATA, SCREEN \<2\> screen to prevent the entry of data in group 6, the Indian Attestation data. Also, the \<6\> Indian Attestation group is made read-only.

Patch DG\*5.3\*1093 modifies the HL7 ORU/ORF Z07 message. The Indian Attestation–related fields in the ZPD segment will contain NULL values.

The following modified routines are exported by patch DG\*5.3\*1093:

- DG531093P
- DGENPTA1
- DGRP2
- DGRPE1
- DGRPV
- VAFHLZPD

### Patch DG\*5.3\*1098 Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch DG\*5.3\*1098 sets the INACTIVE field to YES of the WORLD WAR I eligibility code entries in the MAS ELIGIBILITY CODE (#8.1) and ELIGIBILITY CODE (#8) files.

Patch DG\*5.3\*1098 modifies the field value for the LONG DESCRIPTION field (#.04) in the HEALTH BENEFIT PLAN file (#25.11) for VHAP plan code VETERAN FULL MED BENEFITS TX GMT AND RX COPAY REQ 6 (#240) and VETERAN FULL MED BENEFITS TX AND RX COPAY REQ 6 (#281).

Patch DG\*5.3\*1098 adds the WORLD WAR II eligibility code to the MAS ELIGIBILITY CODE (#8.1) file.

Patch DG\*5.3\*1098 prevents users from adding the new WORLD WAR II eligibility code in DATA GROUP \[3\] in the PRIMARY ELIGIBILITY CODE prompt on the ELIGIBILITY STATUS DATA, SCREEN \<7\>.

Patch DG\*5.3\*1098 allows user to add the new WORLD WAR II eligibility code in DATA GROUP \[3\] in the PATIENT ELIGIBILITIES prompt on the ELIGIBILITY STATUS DATA, SCREEN \<7\> for patients matching the following criteria:

- Patient is a Veteran
- Patient has a Military Service Episode that includes any period from December 07, 1941 through December 31, 1946
- Patient's birthdate is prior to January 01, 1933

Patch DG\*5.3\*1098 adds the new entry "UNCHARACTERIZED" to the TYPE OF DISCHARGE file (#25).

Patch DG\*5.3\*1098 modifies existing entries in the INCONSISTENT DATA ELEMENTS file (#38.6). The DATE OF DEATH IN THE FUTURE (#16), THE DATE OF DEATH IS BEFORE THE DATE OF BIRTH (#308) and CLAIM FOLDER NUMBER INVALID (#406) the USE FOR Z07 CHECK field (#6) is changed from YES to NO.

Patch DG\*5.3\*1098 modifies the input template \[DG LOAD EDIT SCREEN 7\] of the ELIGIGILITY DATA, SCREEN \<7\>, Group \[1\] to no longer display the labels "Claim Number:" and "Folder Loc.:" when the CLAIM NUMBER field (#.313) and the CLAIM FOLDER LOCATION field (#.314) from the PATIENT file (#2) are both null.

Patch DG\*5.3\*1098 modifies the Enrollment Priority algorithm so that the system shall assign Priority Group 6 to a Veteran with the World War II Eligibility Code, unless the Veteran otherwise qualifies for Priority Group 1, 2, 3, 4, or 5.

> **NOTE:** For additional information on the Enrollment Priority Algorithm, please see the 'PIMS Version 5.3 ADT Module User Manual' located on the Veteran Affairs (VA) Software Document Library.

The following modified routines are exported by patch DG\*5.3\*1098:

- DG531098P
- DGLOCK1
- DGENELA4
- DGRP7
- DGRPC
- DGRPC3

### Patch DG\*5.3\*1103 Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch DG\*5.3\*1103 adds a new field to the PATIENT file (File \#2) to indicate whether the patient claims exposure to Toxic Exposure Risk Activity (TERA), field named TOXIC EXPOSURE RISK ACTIVITY (#.32116).

Patch DG\*5.3\*1103 adds TERA: as a new Group \<6\> on the ENVIRONMENTAL FACTORS sub-screen displayed when the Environment Factors group \[3\] on the MILITARY SERVICE DATA, SCREEN \<6\> is selected.

Patch DG\*5.3\*1103 adds the TOXIC EXPOSURE RISK ACTIVITY field to the SVC Component of the VADPT routine, service information for a patient, supported by ICR 10061.

Patch DG\*5.3\*1103 adds TERA to the list of Alpha Subscripts returned in the VASV array when VAHOW is set to 1.

Patch DG\*5.3\*1103 modifies the Enrollment Priority algorithm to assign Priority Group 6 to a patient with the TOXIC EXPOSURE RISK ACTIVITY field (#2,.32116) equal to 1, YES, when recalculating Priority Group values unless the Veteran qualifies for a higher Priority Group.

Patch DG\*5.3\*1103 updates the SVC^VADPT service information entry point, adds the new TOXIC EXPOSURE RISK ACTIVITY (#.32116) field to the 15<sup>th</sup> node of the VASV array.

Patch DG\*5.3\*1103 receives the TERA data from VES and stores the received TERA data.

The following modified routines are exported by patch DG\*5.3\*1103:

- VADPT
- VADPT0
- VADPT4
- DGRP6EF
- DGENUPL
- DGENUPLA
- DGENPTA1
- DGENELA4

### Patch DG\*5.3\*1095 Description and Routines 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DG\*5.3\*1095 includes updates that will display administrative eligibility for Comprehensive Prevention, Access to Care, and Treatment (COMPACT) Act as well as a break fix for a hanging comma in Admission, Discharge, Transfer/Registration (ADT REG).

The menu options DG REGISTER PATIENT, DG LOAD PATIENT DATA, FBCH ENTER REQUEST and DG PATIENT INQUIRY show ELIGIBLE, NOT ELIGIBLE, or UNDETERMINED as administrative eligibility statuses. In addition, the PTF Screen 101 will also display these 3 stat

The following modified routines are exported by patch DG\*5.3\*1095:

- DG531095P
- DGPTF1
- DGREGEEWS
- DGRPD

### Patch DG\*5.3\*1109 Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch DG\*5.3\*1109 modifies thirteen VHA Profiles (VHAP) of the HEALTH BENEFIT PLAN file (#25.11).

Patch DG\*5.3\*1109 modifies twenty-six entries in the INCONSISTENT DATA ELEMENTS file (#38.6).

Patch DG\*5.3\*1109 adds a new entry, SERVICE ACT, in the MAS ELIGIBILITY CODEfile (#8.1).

Patch DG\*5.3\*1109 adds a new entry, SERVICE ACT, in the ELIGIBILITY CODE file (#8).

Patch DG\*5.3\*1109 modifies the Enrollment Priority algorithm to assign an eligible Combat Veteran, outside the 10 year (or 5 year for those Veterans with a Service Separation Date prior to October 01, 2013) eligibility period, Priority Group 8c, regardless of Financial criteria, unless the Veteran qualifies for a better Priority Group.

Patch DG\*5.3\*1109 modifies routine DGENA5 to avoid UNDEFINED errors during creation of the ZCD segment of the Health Level 7 (HL7) ORU/ORF~Z07 message.

- DG531109P
- DGENELA4
- DGLOCK1
- DGRPC3
- DGENA5

### Patch DG\*5.3\*1107 Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DG NAME COMPONENT UPDATE stand-alone option.

This option was created for patch DG\*5\*3\*1107 and is used to restore missing Name Component (Field \#1.01) of the Patient (File \#2) and the Name Component (File \#20). This is necessary when a patient name is not updating on Toolkit ADR Compare and is not showing on the EDAT for the MVI. The person assigned the DG NAME COMPONENT UPDATE option will also need to be assigned the DGPNC security key.

The findings of the DG Name Component Update process will be stored in a temp global for 180 ^XTMP(“RESULTS”) and ^XTMP(“CONFIRM”)

The option runs the DGRNCVNC routine. This routine checks the Patient (File \#2) Field \#1.01) for missing entries. If the patient’s record is part of a Duplicate Record Merge, it skips the record and when a valid record is found, it is placed in a temporary file for processing. The results are sent in a mailman message to the person who runs the option for review. If no records were found, the first message will reflect this result. If records were found and the user decides these are valid records needing updated, they need to run the option again and choose to update the missing name components. A list of the records updated with the resulting pointers to the Name Component (File \#20) are placed in another mailman message for validation. The results can be validated by a programmer using global lister, or by a user with FileMan access.

During installation DGRNCVNCP routine runs and removes itself after installation. This routine will only display if there are findings. It will let the user know to check their mailman messages if any findings are present.

*Note:* If there are issues during the execution of the option, Service Now tickets can be forwarded to the HIG team: SPM.Health.HI.HIG for troubleshooting and later escalation if necessary to Tier3 HDSO Dev team.

### Patch DG\*5.3\*1111 Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch DG\*5.3\*1111 modifies the Register a Patient \[DG REGISTER A PATIENT\] option to:

- No longer prompt for the PREFIX (#20,4) field of the NAME COMPONENTS (#20) file during the Enterprise Search prompt Sequence.
- No longer prompt for the DEGREE (#20,6) field of the NAME COMPONENTS (#20) file during the Enterprise Search prompt Sequence.
- No longer display the "Select Admitting Area:" prompt.
- No longer display the "Is the patient currently being followed in a clinic for the same condition?" prompt.
- No longer display the "Is the patient to be examined in the medical center today?" prompt.
- No longer display the TYPE OF BENEFIT APPLIED FOR (#2.101,2) field prompt of the DISPOSITION LOG-IN DATE/TIME (#2.101) file.
- No longer display the TYPE OF CARE APPLIED FOR (#2.101,2.1) field prompt of the DISPOSITION LOG-IN DATE/TIME (#2.101) file.
- No longer display the NEED RELATED TO AN ACCIDENT (#2.101,23) field prompt of the DISPOSITION LOG-IN DATE/TIME (#2.101) file.
- No longer display the NEED RELATED TO OCCUPATION (#2.101,20) field prompt of the DISPOSITION LOG-IN DATE/TIME (#2.101) file.

Patch DG\*5.3\*1111 modifies the PATIENT DEMOGRAPHIC DATA, SCREEN \<1\> to:

- No longer prompt for the PREFIX (#20,4) and the DEGREE (#20,6) fields of the NAME COMPONENTS (#20) file in the ‘Name, SSN, DOB, Birth Sex’ DATA GROUP \[1\].
- To only display the Pager \#: label if the PAGER NUMBER (#.135) field of the PATIENT (#2) file is not NULL in DATA GROUP \[4\].
- Not to display UNANSWERED in the Pager \#: label if the value of the PAGER NUMBER (#.135) field of the PATIENT (#2) file is NULL in DATA GROUP \[4\].

Patch DG\*5.3\*1111 modifies PATIENT DATA, SCREEN \<2\> screen DATA GROUP \[1\] to no longer prompt for the FATHER'S NAME (#2,.2401) field and the MOTHER'S NAME (#2,.2402) field of the PATIENT (#2) file.

The following modified routines are exported by patch DG\*5.3\*1111:

- DGENA2
- DGENA3
- DGENA6
- DGENDD
- DGENEGT1
- DGENUPL4
- DGENUPL7
- DGENUPL8
- DGREG
- DGREG0
- DGRP1
- DGRPC
- DGRPC3
- DGRPE
- DGRPE1
- DPTLK7
- DPTNAME

### Patch DG\*5.3\*1120 Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch DG\*5.3\*1120 contains enhancements to the VistA Audit Solution (VAS) DG VAS EXPORT.

Routine DGAUDIT3 was modified to send an alert in the form of a MailMan message to members of the DG VAS MONITOR mail group when changes to the VAS STATUS (#.03) field in the DG VAS CONFIG (#46.5) file occur.

Routine DGAUDIT3 was also modified to no longer set the DATE VAS STARTED (#.04) field in the DG VAS EXPORT (#46.4) file to the current date/time every time a change to the VAS STATUS (#.03) field in the DG VAS CONFIG (#46.5) file occurs. This field will now only be set once, the first time the switch is set to either “Generate and send data” or “Generate data, don't send”.

Routine DGAUDIT1 was modified to change existing VAS alert wording. All VAS alerts include a message informing the recipient of the number of entries in the VAS queue, and the maximum number of entries permitted in the queue. Previously released patch DG\*5.3\*1108 changed VAS Export logic to no longer delete the oldest entries from the DG VAS EXPORT (#46.3) file when the number of entries exceeded the limit defined by the DG VAS MAX QUEUE ENTRIES parameter. However, that patch did not change the wording in the alert message indicating that entries would be deleted from the queue. The wording has been changed from “The maximum number of entries before automatic deletion is \###” to “The maximum number of entries in the queue is \###”.

| New DG Routines | Modified DG Routines |
|-----------------|----------------------|
|                 | DGAUDIT1         |
|                 | DGAUDIT3         |

<span id="_Ref58832903" class="anchor"></span>Table 14: File List

### Patch DG\*5.3\*1118 Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch DG\*5.3\*1118 modifies two entries in the PERIOD OF SERVICE file (#21).

Patch DG\*5.3\*1118 modifies seven entries in the INCONSISTENT DATA ELEMENTS file (#38.6).

Patch DG\*5.3\*1118 adds text to the HELP PROMPT, DESCRIPTION and TECHNICAL DESCRIPTION fields of the TOXIC EXPOSURE RISK ACTIVITY field (#.32116) in the PATIENT file (#2).

Patch DG\*5.3\*1118 updates the ENVIRONMENTAL FACTORS screen of the Environment Factors DATA GROUP 3 on the MILITARY SERVICE DATA, SCREEN \<6\>. The TERA prompt will display UNKNOWN if the TOXIC EXPOSURE RISK ACTIVITY field (#.32116) of the PATIENT file (#2) is NULL. The default value for a patient is "UNKNOWN" if no value was entered.

The following modified routines are exported by patch DG\*5.3\*1118:

- DG531118P
- DGRP6EF
- VADPT4

### Patch DG\*5.3\*1121 Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch DG\*5.3\*1121 modifies the APPLICANT/SPOUSE EMPLOYMENT DATA, SCREEN \<4\> to make the Applicant Employer, Address and Spouses Employer, Address data groups not editable.

Patch DG\*5.3\*1121 modifies the APPLICANT/SPOUSE EMPLOYMENT DATA, SCREEN \<4\> to make the Spouses Employer, Address Data Groups not editable.

Patch DG\*5.3\*1121 installs Data Dictionary TELEPHONE COUNTRY CODE (#12.12) file.

Patch DG\*5.3\*1121 installs TEMPORARY COUNTRY CODE field (#.12116), COUNTRY CODE \[RESIDENCE\] field (#.1327), COUNTRY CODE \[CELLULAR\] field (#.1328), COUNTRY CODE \[WORK\] field (#.1329), and CONFIDENTIAL COUNTRY CODE field (#.13201) to the PATIENT (#2) file.

Patch DG\*5.3\*1121 installs TEMPORARY EXTENSION field (#.12117), EXTENSION \[RESIDENCE\] field (#.13211), EXTENSION \[CELLULAR\] field (#.13212), EXTENSION \[WORK\] field (#.13213) and CONFIDENTIAL EXTENSION field (#.13214) to the PATIENT file (#2).

Patch DG\*5.3\*1121 installs PERSIAN GULF INDICATOR field (#.32117) and LAST CHANGE DATE (#.32118) of the PERSIAN GULF INDICATOR to the PATIENT file (#2).

The following modified routines are exported by patch DG\*5.3\*1121:

- DGENPTA1
- DGENUPL
- DGENUPLA
- DGRP4
- DGRP6EF
- DGRPV
- VADPT
- VADPT0
- VADPT4
- VAFCQRY3
- VAFHLZTA

### Patch DG\*5.3\*1104 Description and Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch adds functionality to enable communicating with the COMPACT ACT EPISODE OF CARE file (#818) created in PX\*1.0\*240. This COMPACT Act Acute Suicidal Crisis episodes functionality includes the following (note: complete functionality features can be reviewed in the Enhancement Tracking System Ticket(s) & Overview section):

- Capture and store Inpatient start and follow-up documentation from new Admission and Transfer workflow prompts
- Automatically close an existing Episode of Care (EOC) from the new Admission workflow prompt
- Capture and store Inpatient end documentation from the CPRS COMPACT ACT 201 ENCOUNTER template
- Display Start date, Remaining days, and End date from menu options: Patient Inquiry (DG PATIENT INQUIRY), Register a Patient (DG REGISTER PATIENT), Load Patient Data (DG LOAD PATIENT DATA), and Enter a Request/Notification (FBCH ENTER REQUEST) from the Notification/Request Menu (FBCH NOTIFICATION MENU) of the Civil Hospital Main Menu (FBCH MAIN MENU)
- Display Start date, Remaining days, and End date from the Patient Treatment File (PTF) 501 screen
- Capture whether admission or treatment is intended for an Acute Suicidal Crisis from prompts in the Admission and Transfer workflows
- Store Admitted for Acute Suicidal Crisis values in the PTF (#45) file, (70;33) position
- Store Treatment for Acute Suicidal Crisis values in the PTF 501 (#45.02) sub-file, (0;33) position
- Display whether or not the Inpatient visit is related to an Acute Suicidal Crisis on the PTF 101 screen
- Upon discharge from Inpatient stay and readmission within same day, COMPACT Act Inpatient Benefit Start Date is maintained from initial admission
- Upon discharge from Inpatient stay and no readmission within same day, automatically begin COMPACT Act Outpatient Benefit
- When an admission, discharge, or transfer movement is deleted from Admit a Patient (DG ADMIT PATIENT) or Extended Bed Control (DG BED CONTROL EXTENDED), update the COMPACT ACT EPISODE OF CARE file (#818) accordingly
- When a transfer occurs for a patient who has an open Outpatient EOC with a prior date, close the Outpatient EOC and start the Inpatient EOC
- When a transfer occurs for a patient who has an open Outpatient EOC with the current date, change the current Outpatient EOC to an Inpatient EOC
- Edit the Start and End dates and Source of Crisis End from the Supervisor ADT Menu using the COMPACT Act EOC Edit Menu option
- Change the value to "NO" from the Admitted for Acute Suicidal Crisis prompt, allowing retraction of EOC values if saved for the wrong patient or if the wrong codes were used and were discovered before discharge
- Use the COMPACT Act EOC Inpatient Retraction menu option from the Supervisor ADT Menu, allowing retraction of the EOC, if saved for the wrong patient or if the wrong codes were used. If an error is discovered after discharge, this menu is the only method to retract the EOC.
- Display whether the patient is in an open EOC from Eligibility Inquiry for Patient Billing
- Display the Administrative Eligibility status from the Patient Enrollment screen 2
- Updates the method (modified from Release 1) by which COMPACT Act Administrative Eligibility statuses are accessed
- Captures and stores requests and responses to the Enrollment and Eligibility webservice for COMPACT Act Administrative Eligibility status from the DGREGEEWS routine in the COMPACT ACT TRANSACTION LOG file (#33.3)
- Allows a Monitor Report to be run from a command line, D QUERY^DGCOMPACT, that displays records to the screen from the COMPACT ACT TRANSACTION LOG FILE (#33.3) by calling routine

Additional changes included in this patch unrelated to the COMPACT Act functionality include:

- Added enhancement in DG REG for Sexual Orientation Description field to display "Sexual Orientation Free Text:"

The following modified routines are exported by patch DG\*5.3\*1104:

> DGCOMPACT

> DGCOMPACTELIG

> DGENL1

> DGP1104

> DGPMV3

> DGPMV36

> DGPTF1

> DGPTFM4

> DGPTTS

> DGRPD

> DGRPDB

The patch creates a new file – COMPACT ACT TRANSACTION LOG file (#33.3)

The patch updates the following existing file: PTF (#45)

The patch updates the following existing Menus:

> DG SUPERVISOR MENU

> COMPACT ACT EOC EDIT --- New option

> COMPACT ACT EOC INPATIENT RETRACTION – New option

The patch updates the following input templates:

> DGPM ADMIT

> DGPM DISCHARGE

### Patch DG\*5.3\*1091 Description and Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IFC ORDER/ADDENDUM UPDATES 1.0 multi-build was made up of four (4) patches: 1) DG\*5.3\*1096, 2) EHM\*1\*10, 3) GMRC\*3\*189 and 4) DG\*5.3\*1091. EHM\*1\*10 created an HL7 Message repository to store HL7 messages exchanged between non-converted VistA sites and Cerner so that extended research could be done without fear of the messages being routinely purged. EHM\*1\*10 also created APIs that can be called to add messages to the repository. ICR \#7424 supports these APIs.

In DG\*5.3\*1091, code was added to DGPFHLR and DGPFHLS to recognize incoming PRF messages from Cerner and outgoing PRF messages to Cerner and store them in the repository.

### Patch DG\*5.3\*1096 Description and Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IFC PROXY ADD/ORDER RESUBMISSION 1.0 multi-build was made up of four (4) patches: 1) DG\*5.3\*1096, 2) EHM\*1\*10, 3) GMRC\*3\*189 and 4) DG\*5.3\*1091.

DG\*5.3\*1096 creates a new routine DGPROSAD, that allows the CONSULT/REQUEST TRACKING package the ability to create a new PATIENT (File \#2) record when they receive an Interfacility Consult (IFC) in VistA from CERNER and the patient is NOT known at the VistA site. ICR \#7421 supports the use of the interface.

This patch also adds the following RPC: MPI IFC VISTA ADD PATIENT.

### Patch DG\*5.3\*1127 Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch installs the following changes:

- Modifies the EMPLOYEE ONLY (#283) and the EMPLOYEE VETERAN (#297) entries of the HEALTH BENEFIT PLAN file (#25.11).
- Adds the new entry VFMP MEDS BY MAIL ELIGIBILITY (#310) to the HEALTH BENEFIT PLAN file (#25.11).
- Adds three new address override indicator fields, RESIDENTIAL ADDR OVERRIDE IND (#.11591), MAILING ADDR OVERRIDE IND (#.1119) and CONFIDENTIAL ADDR OVERRIDE IND (#.141201) fields to the PATIENT file (#2).
- Collects and stores the validation key returned from UAM in the new fields RESIDENTIAL ADDR OVERRIDE IND (#.11591), MAILING ADDR OVERRIDE IND (#.1119) and CONFIDENTIAL ADDR OVERRIDE IND (#.141201) of the PATIENT file (#2).
- Modifies sixteen entries in the INCONSISTENT DATA ELEMENTS file (#38.6)
- Modifies the HELP-PROMPT for PHONE NUMBER \[WORK\] field (#.132) from the PATIENT file (#2).

The following modified routines are exported by patch DG\*5.3\*1127:

- DGADDLST
- DGCLEAR
- DGREGAED
- DGREGCOP
- DGREGRED
- DGREGTED
- DGRPC
- DGRPC3
- DGUAMWS

# Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides a list of the software files. For each file, include the following:

- File number.
- File name.
- List of any special templates (print, sort, input, edit) that come with the file.
- Brief description of the data or instruct the user how/where to find this information online.
- Indicate what data comes with the files and whether that data overwrites existing data.
- Optionally, include information about file pointer relationships.

## Globals and Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The main globals used in the PIMS package are: ^DG, ^DPT, ^DGPM, ^SC, and ^SCE.

The main files are:

- PATIENT (#2)
- PATIENT MOVEMENT (#405)
- MAS MOVEMENT TYPE (#405.2)
- PTF (#45)
- CENSUS (#41.9)
- WARD LOCATION (#42)
- HOSPITAL LOCATION (#44)

The PIMS Package also uses globals:

- ^DGSL
- ^DGIN
- ^DGS
- ^DGAM
- ^DGCPT
- ^DGICD9
- ^DGWAIT
- ^DGPR
- ^DGMT
- ^DGPT
- ^DGM
- ^DGMHV
- ^DGNT
- ^DGP
- ^DGPF
- ^DGQE
- ^ICPT
- ^VA
- ^VAS
- ^VAT
- ^DIC
- ^SCPT
- ^SCTM
- ^DGCOMP

Journaling of the following globals is mandatory:

- ^DPT
- ^DGEN
- ^DGPT
- ^DGPM
- ^SC
- ^SCE
- ^SCTM

Journaling of the following globals is optional:

- ^DGS
- ^DG

Journaling of the following global is *recommended*: ^DGPF.

## File List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| File Number | File Name                                   | Global         |
|-------------|---------------------------------------------|----------------|
| 2           | PATIENT                                     | ^DPT(          |
| 5           | STATE                                       | ^DIC(5,        |
| 8           | ELIGIBILITY CODE                            | ^DIC(8,        |
| 8.1\*\*     | MAS ELIGIBILITY CODE                        | ^DIC(8.1,      |
| 8.2\*       | IDENTIFICATION FORMAT                       | ^DIC(8.2,      |
| 10\*        | RACE                                        | ^DIC(10,       |
| 11\*\*      | MARITAL STATUS                              | ^DIC(11,       |
| 12.11       | PATIENT CONTACT RELATION                    | ^DG(12.11,     |
| 13\*        | RELIGION                                    | ^DIC(13,       |
| 21\*\*      | PERIOD OF SERVICE                           | ^DIC(21,       |
| 22\*\*      | POW PERIOD                                  | ^DIC(22,       |
| 23\*        | BRANCH OF SERVICE                           | ^DIC(23,       |
| 25\*        | TYPE OF DISCHARGE                           | ^DIC(25,       |
| 25.11       | HEALTH BENEFIT PLAN                         | ^DGHBP(25.11,  |
| 26.11       | PRF LOCAL FLAG                              | ^DGPF(26.11,   |
| 26.12       | PRF LOCAL FLAG HISTORY                      | ^DGPF(26.12,   |
| 26.13       | PRF ASSIGNMENT                              | ^DGPF(26.13,   |
| 26.14       | PRF ASSIGNMENT HISTORY                      | ^DGPF(26.14,   |
| 26.15       | PRF NATIONAL FLAG                           | ^DGPF(26.15,   |
| 26.16       | PRF TYPE                                    | ^DGPF(26.16,   |
| 26.17       | PRF HL7 TRANSMISSION LOG                    | ^DGPF(26.17,   |
| 26.18       | PRF PARAMETERS                              | ^DGPF(26.18,   |
| 26.19       | PRF HL7 QUERY LOG                           | ^DGPF(26.19,   |
| 26.21       | PRF HL7 EVENT                               | ^DGPF(26.21,   |
| 26.22       | PRF HL7 REQUEST LOG                         | ^DGPF(26.22,   |
| 27.11       | PATIENT ENROLLMENT                          | ^DGEN(27.11,   |
| 27.12       | ENROLLMENT QUERY                            | ^DGEN(27.12,   |
| 27.14       | ENROLLMENT / ELIGIBILITY UPLOAD AUDIT       | ^DGENA(27.14,  |
| 27.15       | ENROLLMENT STATUS                           | ^DGEN(27.15,   |
| 27.16       | ENROLLMENT GROUP THRESHOLD                  | ^DGEN(27.16,   |
| 27.17\*     | CATASTROPHIC DISABILITY REASONS             | ^DGEN(27.17,   |
| 28.11       | NOSE AND THROAT RADIUM HISTORY              | ^DGNT(28.11,   |
| 29.11       | MST HISTORY                                 | ^DGMS(29.11,   |
| 30\*\*      | DISPOSITION LATE REASON                     | ^DIC(30,       |
| 33.3        | COMPACT ACT TRANSACTION LOG                 | ^DGCOMP(33.3,  |
| 35\*        | OTHER FEDERAL AGENCY                        | ^DIC(35,       |
| 35.1        | SHARING AGREEMENT CATEGORY                  | ^DG(35.1,      |
| 35.2        | SHARING AGREEMENT SUB-CATEGORY              | ^DG(35.2)      |
| 37\*\*      | DISPOSITION                                 | ^DIC(37,       |
| 38.1        | DG SECURITY LOG                             | ^DGSL(38.1,    |
| 38.5        | INCONSISTENT DATA                           | ^DGIN(38.5,    |
| 38.6\*\*    | INCONSISTENT DATA ELEMENTS                  | ^DGIN(38.6,    |
| 39.1\*      | EMBOSSED CARD TYPE                          | ^DIC(39.1,     |
| 39.2\*      | EMBOSSING DATA                              | ^DIC(39.2,     |
| 39.3        | EMBOSSER EQUIPMENT FILE                     | ^DIC(39.3,     |
| 39.4        | ADT / HL7 TRANSMISSION                      | ^DIC(39.4,     |
| 39.6        | VIC REQUEST                                 | ^DGQE(39.6,    |
| 39.7        | VIC HL7 TRANSMISSION LOG                    | ^DGQE(39.7,    |
| 40.7\*      | CLINIC STOP                                 | ^DIC(40.7,     |
| 40.8        | MEDICAL CENTER DIVISION                     | ^DG(40.8,      |
| 40.9\*\*    | LOCATION TYPE                               | ^DIC(40.9      |
| 41.1        | SCHEDULED ADMISSION                         | ^DGS(41.1,     |
| 41.41       | PRE-REGISTRATION AUDIT                      | ^DGS(41.41,    |
| 41.42       | PRE-REGISTRATION CALL LIST                  | ^DGS(41.42,    |
| 41.43       | PRE-REGISTRATION CALL LOG                   | ^DGS(41.43,    |
| 41.9        | CENSUS                                      | ^DG(41.9,      |
| 42          | WARD LOCATION                               | ^DIC(42,       |
| 42.4\*      | SPECIALTY                                   | ^DIC(42.4,     |
| 42.5        | WAIT LIST                                   | ^DGWAIT(       |
| 42.55\*\*   | PRIORITY GROUPING                           | ^DIC(42.55,    |
| 42.6        | AMIS 334-341                                | ^DGAM(334,     |
| 42.7        | AMIS 345&346                                | ^DGAM(345,     |
| 43          | MAS PARAMETERS                              | ^DG(43,        |
| 43.1        | MAS EVENT RATES                             | ^DG(43.1,      |
| 43.11\*\*   | MAS AWARD                                   | ^DG(43.11,     |
| 43.4\*\*    | VA ADMITTING REGULATION                     | ^DIC(43.4,     |
| 43.5        | G&L CORRECTIONS                             | ^DGS(43.5,     |
| 43.61       | G&L TYPE OF CHANGE                          | ^DG(43.61,     |
| 43.7\*\*    | ADT TEMPLATE                                | ^DG(43.7,      |
| 44          | HOSPITAL LOCATION                           | ^SC(           |
| 45          | PTF                                         | ^DGPT(         |
| 45.1\*\*    | SOURCE OF ADMISSION                         | ^DIC(45.1,     |
| 45.2        | PTF TRANSFERRING FACILITY                   | ^DGTF(         |
| 45.3\*      | SURGICAL SPECIALTY                          | ^DIC(45.3,     |
| 45.4\*      | PTF DIALYSIS TYPE                           | ^DG(45.4,      |
| 45.5        | PTF MESSAGE                                 | ^DGM(          |
| 45.6\*      | PLACE OF DISPOSITION                        | ^DIC(45.6,     |
| 45.61\*     | PTF ABUSED SUBSTANCE                        | ^DIC(45.61,    |
| 45.64\*     | PTF AUSTIN ERROR CODES                      | ^DGP(45.64,    |
| 45.68       | FACILITY SUFFIX                             | ^DIC(45.68,    |
| 45.7        | FACILITY TREATING SPECIALTY                 | ^DIC(45.7,     |
| 45.81\*     | STATION TYPE                                | ^DIC(45.81,    |
| 45.82\*     | CATEGORY OF BENEFICIARY                     | ^DIC(45.82,    |
| 45.83       | PTF RELEASE                                 | ^DGP(45.83,    |
| 45.84       | PTF CLOSE OUT                               | ^DGP(45.84,    |
| 45.85       | CENSUS WORKFILE                             | ^DG(45.85,     |
| 45.86\*     | PTF CENSUS DATE                             | ^DG(45.86,     |
| 45.87       | PTF TRANSACTION REQUEST LOG                 | ^DGP(45.87,    |
| 45.88\*     | PTF EXPANDED CODE CATEGORY                  | ^DIC(45.88,    |
| 45.89\*     | PTF EXPANDED CODE                           | ^DIC(45.89,    |
| 45.9        | PAF                                         | ^DG(45.9,      |
| 45.91       | RUG-II                                      | ^DG(45.91,     |
| 46          | INPATIENT CPT CODE                          | ^DGCPT(46      |
| 46.1        | INPATIENT POV                               | ^DGICT9(46.1,  |
| 46.3        | DG VAS QUEUE                                | ^DGAUDIT(      |
| 46.4        | DG VAS EXPORT                               | ^DGAUDIT1(     |
| 46.5        | DG VAS CONFIG                               | ^DGAUDIT2(     |
| 47\*\*      | MAS FORMS AND SCREENS                       | ^DIC(47,       |
| 47.77       | SEXUAL ORIENTATION TYPES                    | ^DG(47.77      |
| 47.78       | PRONOUN TYPES                               | ^DG(47.78      |
| 48\*\*      | MAS RELEASE NOTES                           | ^DG(48,        |
| 48.5\*\*    | MAS MODULE                                  | ^DG(48.5,      |
| 389.9       | STATION NUMBER (TIME SENSITIVE)             | ^VA(389.9,     |
| 390         | ENROLLMENT RATED DISABILITY UPLOAD AUDIT    | ^DGRDUA(390,   |
| 390.01      | MHV SOCIALIZATION                           | ^DGMHV(390.01, |
| 390.02      | MHV SOCIALIZATION ACTIONS                   | ^DGMHV(390.02, |
| 390.03      | MHV DECLINED REASONS                        | ^DGMHV(390.03, |
| 390.04      | MHV ACTION SELECTION                        | ^DGMHV(390.04, |
| 391\*\*     | TYPE OF PATIENT                             | ^DG(391,       |
| 391.1       | AMIS SEGMENT                                | ^DG(391.1,     |
| 391.31      | HOME TELEHEALTH PATIENT                     | ^DGHT(391.31,  |
| 403.35      | SCHEDULING USER PREFERENCE                  | ^SCRS(403.35,  |
| 403.43\*    | SCHEDULING EVENT                            | ^SD(403.43,    |
| 403.44\*    | SCHEDULING REASON                           | ^SD(403.44,    |
| 403.46\*    | STANDARD POSITION                           | ^SD(403.46,    |
| 403.47\*    | TEAM PURPOSE                                | ^SD(403.47,    |
| 404.41      | OUTPATIENT PROFILE                          | ^SCPT(404.41,  |
| 404.42      | PATIENT TEAM ASSIGNMENT                     | ^SCPT(404.42,  |
| 404.43      | PATIENT TEAM POSITION ASSIGNMENT            | ^SCPT(404.43,  |
| 404.44      | PCMM PARAMETER                              | ^SCTM(404.44,  |
| 404.45      | PCMM SERVER PATCH                           | ^SCTM(404.45,  |
| 404.46      | PCMM CLIENT PATCH                           | ^SCTM(404.46,  |
| 404.471     | PCMM HL7 TRANSMISSION LOG                   | ^SCPT(404.471, |
| 404.472     | PCMM HL7 ERROR LOG                          | ^SCPT(404.472, |
| 404.48      | PCMM HL7 EVENT                              | ^SCPT(404.48,  |
| 404.49      | PCMM HL7 ID                                 | ^SCPT(404.49,  |
| 404.51      | TEAM                                        | ^SCTM(404.51,  |
| 404.52      | POSITION ASSIGNMENT HISTORY                 | ^SCTM(404.52,  |
| 404.53      | PRECEPTOR ASSIGNMENT HISTORY                | ^SCTM(404.53,  |
| 404.56      | TEAM AUTOLINK                               | ^SCTM(404.56,  |
| 404.57      | TEAM POSITION                               | ^SCTM(404.57,  |
| 404.58      | TEAM HISTORY                                | ^SCTM(404.58,  |
| 404.59      | TEAM POSITION HISTORY                       | ^SCTM(404.59,  |
| 404.61      | MH PCMM STOP CODES                          | ^SCTM(404.61,  |
| 405         | PATIENT MOVEMENT                            | ^DGPM(         |
| 405.1       | FACILITY MOVEMENT TYPE                      | ^DG(405.1,     |
| 405.2\*\*   | MAS MOVEMENT TYPE                           | ^DG(405.2,     |
| 405.3\*\*   | MAS MOVEMENT TRANSACTION TYPE               | ^DG(405.3,     |
| 405.4       | ROOM-BED                                    | ^DG(405.4,     |
| 405.5\*\*   | MAS OUT-OF-SERVICE                          | ^DG(405.5,     |
| 405.6       | ROOM-BED DESCRIPTION                        | ^DG(405.6,     |
| 406.41\*\*  | LODGING REASON                              | ^DG(406.41,    |
| 407.7\*\*   | TRANSMISSION ROUTERS                        | ^VAT(407.7,    |
| 408         | DISCRETIONARY WORKLOAD                      | ^VAT(408,      |
| 408.43      | PATIENT REGISTRATION ONLY REASON            | ^DG(408.43,    |
| 408.11\*    | RELATIONSHIP                                | ^DG(408.11,    |
| 408.12      | PATIENT RELATION                            | ^DGPR(408.12,  |
| 408.13      | INCOME PERSON                               | ^DGPR(408.13,  |
| 408.21      | INDIVIDUAL ANNUAL INCOME                    | ^DGMT(408.21,  |
| 408.22      | INCOME RELATION                             | ^DGMT(408.22,  |
| 408.31      | ANNUAL MEANS TEST                           | ^DGMT(408.31,  |
| 408.32\*\*  | MEANS TEST STATUS                           | ^DG(408.32,    |
| 408.33\*\*  | TYPE OF TEST                                | ^DG(408.33,    |
| 408.34\*\*  | SOURCE OF INCOME TEST                       | ^DG(408.34,    |
| 408.41      | MEANS TEST CHANGES                          | ^DG(408.41,    |
| 408.42\*\*  | MEANS TEST CHANGES TYPE                     | ^DG(408.42,    |
| 409.68      | OUTPATIENT ENCOUNTER                        | ^SCE(          |
| 409.73      | TRANSMITTED OUTPATIENT ENCOUNTER            | ^SD(409.73,    |
| 409.74      | DELETED OUTPATIENT ENCOUNTER                | ^SD(409.74,    |
| 409.75      | TRANSMITTED OUTPATIENT ENCOUNTER ERROR      | ^SD(409.75,    |
| 409.76\*\*  | TRANSMITTED OUTPATIENT ENCOUNTER ERROR CODE | ^SD(409.76,    |
| 409.77      | ACRP TRANSMISSION HISTORY                   | ^SD(409.77,    |
| 409.91      | ACRP REPORT TEMPLATE                        | ^SDD(409.91,   |
| 409.92      | ACRP REPORT TEMPLATE PARAMETER              | ^SD(409.92,    |
| 409.95      | PRINT MANAGER CLINIC SETUP                  | ^SD(409.95,    |
| 409.96      | PRINT MANAGER DIVISION SETUP                | ^SD(409.96,    |

<span id="_Ref54082206" class="anchor"></span>Table 15: VA FileMan Functions

\*File comes with data.

\*\* File comes with data that overwrites existing data, if specified.

# Files and Templates in the PIMS Package

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are the steps you may take to obtain information concerning the files and templates contained in the PIMS package.

## File Flow (Relationships between files)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  VA FileMan Menu.
9.  Data Dictionary Utilities Menu.
10. List File Attributes Option.
11. Enter File \#number or range of File numbers.
12. Select Listing Format: Standard.
13. You see what files point to the selected file. To see what files to which the selected file points, look for fields that say: “POINTER TO”.

## Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  VA FileMan Menu.
14. Print File Entries Option.
15. Output from what File:
- Print Template
- Sort Template
- Input Template
- List Template
16. Sort by: Name.

    Start with name:
- DG to DGZ, VA to VAZ, (ADT)
17. Within name, sort by: \<Enter\>.
18. First print field: Name

## VA FileMan Functions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Included with the ACRP Reports Menu is the VA FileMan function, SCRPWDATA. This function can be used from within the OUTPATIENT ENCOUNTER file to provide any of the data elements in the VA FileMan Functions table as data within VA FileMan output. It may be used to sort or print data.

This function has one argument, which is the name (or acronym) of the data element you want to return. For example, if you want to sort or print a patient's current GAF score, the function could be used as follows.

<span id="_Toc193958001" class="anchor"></span>Figure 3: Printing SCRPWDATA Function Data

THEN PRINT FIELD: SCRPWDATA("GAF SCORE (CURRENT)");"CURRENT GAF SCORE";L8

(OR)

THEN PRINT FIELD: SCRPWDATA("DXGC");"CURRENT GAF SCORE";L8

VA FileMan function data elements that have multiple values (e.g., procedure codes, diagnoses, etc.) are returned as a single semicolon delimited string, which can be as long as 245 characters. Some data of these elements can be omitted due to truncation to stay within this limit.

The table below lists VA FileMan function data elements and their associated acronyms that can be specified as arguments to the SCRPWDATA function.

| Data Element                              | Acronym |
|-------------------------------------------|---------|
| Category: Ambulatory Procedure        |         |
| EVALUATION & MANAGEMENT CODES             | APEM    |
| AMBULATORY PROCEDURE (NO E&M CODES)       | APAP    |
| ALL AMBULATORY PROCEDURE CODES            | APAC    |
| Category: Clinic                      |         |
| CLINIC NAME                               | CLCN    |
| CLINIC GROUP                              | CLCG    |
| CLINIC SERVICE                            | CLCS    |
| Category: Diagnosis                   |         |
| PRIMARY DIAGNOSIS                         | DXPD    |
| SECONDARY DIAGNOSIS                       | DXSD    |
| ALL DIAGNOSES                             | DXAD    |
| GAF SCORE (HISTORICAL)                    | DXGH    |
| GAF SCORE (CURRENT)                       | DXGC    |
| Category: Enrollment (Current)        |         |
| ENROLLMENT DATE (CURRENT)                 | ECED    |
| SOURCE OF ENROLLMENT (CURRENT)            | ECSE    |
| ENROLLMENT STATUS (CURRENT)               | ECES    |
| ENROLLMENT FACILITY RECEIVED (CURRENT)    | ECFR    |
| ENROLLMENT PRIORITY (CURRENT)             | ECEP    |
| ENROLLMENT EFFECTIVE DATE (CURRENT)       | ECEF    |
| Category: Enrollment (Historical)     |         |
| ENROLLMENT DATE (HISTORICAL)              | EHED    |
| SOURCE OF ENROLLMENT (HISTORICAL)         | EHSE    |
| ENROLLMENT STATUS (HISTORICAL)            | EHES    |
| ENROLLMENT FACILITY RECEIVED (HISTORICAL) | EHFR    |
| ENROLLMENT PRIORITY (HISTORICAL)          | EHEP    |
| ENROLLMENT EFFECTIVE DATE (HISTORICAL)    | EHEF    |
| Category: Outpatient Encounter        |         |
| PATIENT                                   | OEPA    |
| ORIGINATING PROCESS TYPE                  | OEOP    |
| APPT. TYPE                                | OEAT    |
| STATUS                                    | OEST    |
| ELIG. OF ENCOUNTER                        | PEPW    |
| MEANS TEST (HISTORICAL)                   | PEMH    |
| MEANS TEST (CURRENT)                      | PEMC    |
| SC PERCENTAGE                             | PESP    |
| AGENT ORANGE EXPOSURE                     | PEAO    |
| IONIZING RADIATION EXPOSURE               | PEIR    |
| SW ASIA CONDITIONS EXPOSURE               | PEEC    |
| Category: Primary Care                |         |
| PC PROVIDER (HISTORICAL)                  | PCPH    |
| PC TEAM (HISTORICAL)                      | PCTH    |
| PC PROVIDER (CURRENT)                     | PCPC    |
| PC TEAM (CURRENT)                         | PCTC    |
| Category: Provider                    |         |
| PRIMARY PROVIDER                          | PRPP    |
| SECONDARY PROVIDER                        | PRSP    |
| ALL PROVIDERS                             | PRAP    |
| PRIMARY PROVIDER PERSON CLASS             | PRPC    |
| SECONDARY PROVIDER PERSON CLASS           | PRSC    |
| ALL PROVIDERS PERSON CLASS                | PRAC    |
| Category: Stop Code                   |         |
| PRIMARY STOP CODE                         | SCPC    |
| SECONDARY STOP CODE                       | SCSC    |
| BOTH STOP CODES                           | SCBC    |
| CREDIT PAIR                               | SCCP    |
| Category: V File Element              |         |
| EXAMINATION                               | VFEX    |
| HEALTH FACTOR                             | VFHF    |
| IMMUNIZATION                              | VFIM    |
| PATIENT EDUCATION                         | VFPE    |
| TREATMENTS                                | VFTR    |
| SKIN TEST                                 | VFST    |

<span id="_Toc193958043" class="anchor"></span>Table 16: New DG Option

# Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section provides a list of the options exported with the software, indicating distribution of menus to users. Any restrictions on menu distribution are noted. When the option’s availability is based on the level of system access requiring permissions the name of the type of access (e.g., security keys and/or roles) and authorization is included.

The following are the steps you may take to obtain information about menus, exported protocols, exported options, exported remote procedures, and exported HL7 applications concerning the PIMS package.

## Menu Diagrams

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Programmers Options.
- Menu Management Menu.
- Display Menus and Options Menu.
- Diagram Menus.
- Select User or Option Name:
- O.DG Manager Menu (ADT).
- O.SDMGR (Scheduling).

## Exported Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- VA FileMan Menu.
- Print File Entries Option.
- Output from what File: PROTOCOL.
- Sort by: Name.
- Start with name:
- DG to DGZ, VA to VAZ (ADT).
- Within name, sort by: \<Enter\>.
- First print field: Name.

## Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- VA FileMan Menu.
- Print File Entries Option.
- Output from what File: OPTION.
- Sort by: Name.
- Start with name:
- DG to DGZ, VA to VAZ (ADT).
- Within name, sort by: \<Enter\>.
- First print field: Name.

## Exported Remote Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- VA FileMan Menu.
- Print File Entries Option.
- Output from what File: REMOTE PROCEDURE
- Sort by: Name.
- Start with name:
- DG to DGZ, VA to VAZ (ADT).
- Within name, sort by: \<Enter\>.
- First print field: Name.

## Exported HL7 Applications for Ambulatory Care Reporting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- HL7 Main Menu.
- V1.6 Options Menu.
- Interface Workload Option.
- Look for AMBCARE-DHCP and NPCD-AAC\*.

\*AAC stands for Austin Automation Center. The name of that facility has been changed to Austin Information Technology Center.

## Exported HL7 Applications for Inpatient Reporting to National Patient Care Database

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- HL7 Main Menu.
- V1.6 Options Menu.
- Interface Workload Option.
- Look for VAFC PIMS and NPTF.

## Exported HL7 Applications for Home Telehealth Care Database

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DG HOME TELEHEALTH

### Exported DG Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The new Convert Local HRMH PRF to National Action \[DGPF LOCAL TO NATIONAL CONVERT\] option is exported by the DG\*5.3\*849, DGPF NEW CAT1 FLAG AND CONVERSION patch:

| New Dg Option                                                                           | Menu Assignment   |
|-----------------------------------------------------------------------------------------|-------------------|
| Convert Local HRMH PRF to National Action \[DGPF LOCAL TO NATIONAL CONVERT\] option | Standalone Option |

<span id="_Toc193958044" class="anchor"></span>Table 17: ADT and Scheduling Module Options

# Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the archiving capabilities of the software and any necessary instructions or guidelines:

## Archiving

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

With the release of PIMS V. 5.3, a new archive / purge option has been created for PTF-related records.

11. For details, see the Release Notes.

## Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PIMS package allows for purging of data associated with log of user access to sensitive records, consistency checker, scheduled admissions, local breakeven data for DRGs, special transaction requests, and scheduling data. Following is a list of the purge options and where the documentation may be found in the user manual.

## ADT Module

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Option Name                                       | Menu Name                 |
|---------------------------------------------------|---------------------------|
| ADT Module                                    |                           |
| Purge Breakeven Data for a Fiscal Year            | PTF                       |
| Purge Special Transaction Request Log             | PTF                       |
| Purge Non-Sensitive Patients from Security Log    | Security Officer          |
| Purge Record of User Access from Security Log     | Security Officer          |
| Purge Inconsistent Data Elements                  | Supervisor ADT            |
| Purge Scheduled Admissions                        | Supervisor ADT            |
| Scheduling Module                             |                           |
| Purge Ambulatory Care Reporting files             | Ambulatory Care Reporting |
| Purge Appointment Status Update Log File          | Supervisor                |
| Purge rejections that are past database close-out | Ambulatory Care Reporting |
| Purge Scheduling Data                             | Supervisor                |

<span id="_Ref54092191" class="anchor"></span>Table 18: Minimum Version Baseline

## ACRP Database Conversion Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of the database conversion is to convert old Scheduling encounter information into the Visit Tracking / Patient Care Encounter (PCE) database. Once you have converted all the data, you may wish to delete the old Scheduling files. A list of the files that can be deleted is displayed when selecting the Delete Old Files action in this option. It is *recommended* you back up these files before deletion.

## HL7 Purger

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is *recommended* that the Purge Message Text File Entries \[HL PURGE TRANSMISSIONS\] option be scheduled to run every day or every other day.

# External/Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section explains any special relationships and agreements between the routines and/or files/fields in this software and dependencies. List any routines essential to the software functions, for example:

- Provide information on whether an outpatient facility could function without programs relating to inpatient activity and avoid system failure.
- Specify the version of VA FileMan, Kernel, and other software required to run this software.
- Include a list of Integration Agreements (IA) with instructions for obtaining detailed information for each, or instruct the user how/where to find this information online.

## External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following minimum package versions are required:

- VA FileMan 21.0 (and higher)
- Kernel 8.0
- Kernel Toolkit 7.3
- VA MailMan 7.1 (and higher)
- CPRS V. 28 (and higher)
- PXRM 2.0.18
- PCE 1.0
- IB 2.0
- IFCAP V. 3.0
- DRG Grouper V. 13.0
- HL7 V. 1.6
- Generic Code Sheet V. 1.5

Sites should verify that all patches to these packages have been installed.

12. For Scheduling Reports to run correctly, patch DG\*5.3\*836 and DG\*5.3\*849 need to be installed and reminder location list VA-MH NO SHOW APPT CLINICS LL in File \#810.9 *must* be current.

If your site is running any of the packages listed in the table below, you *must* be running the listed version or higher.

| Package                    | Minimum Version |
|----------------------------|-----------------|
| AMIE                       | None            |
| CPRS (OR V. 3.0\*280)      | 1.0             |
| Dental                     | 1.2             |
| Dietetics                  | 4.33            |
| Inpatient Meds             | None            |
| IVM                        | 2.0             |
| Laboratory                 | 5.2             |
| Mental Health              | 5.0             |
| Nursing                    | 2.2             |
| Occurrence Screening       | 2.0             |
| Outpatient Pharmacy        | 7.0             |
| Patient Funds              | 3.0             |
| Radiology/Nuclear Medicine | 4.5             |
| Record Tracking            | 2.0             |
| Social Work                | 3.0             |
| Utilization Review         | 1.06            |

<span id="_Ref54092463" class="anchor"></span>Table 19: Ambulatory Care Reporting Project Elements

13. If you are *not* running one of the packages in the table above, you do *not* need to install it.

You *must* have all current patches for the following applications installed prior to the installation of PCMM (SD\*5.3\*41, DG\*5.3\*84):

- Kernel V. 8.0
- Kernel Toolkit V. 7.3
- VA FileMan V. 21.0 (or higher)
- RPC Broker V. 1.0 (or higher)
- PIMS V. 5.3

You *must* have KIDS Patch 44 (XU\*8.0\*44) installed prior to loading the VIC software.

CPRS uses the PCMM files and GUI interface.

The table below lists all elements that are checked for installation of Ambulatory Care Reporting Project.

| Element Checked                                                        | Check Performed           | Required For Install |
|------------------------------------------------------------------------|---------------------------|----------------------|
| PCE V. 1.0                                                             | Installed                 | Yes                  |
| HL7 V. 1.6                                                             | Installed                 | Yes                  |
| XU\*8.0\*27                                                            | Installed                 | Yes                  |
| HL\*1.6\*8                                                             | Installed                 | Yes                  |
| IB\*2.0\*60                                                            | Installed                 | Yes                  |
| REDACTED in DOMAIN (#4.2) file                                         | Entry exists              | Yes                  |
| SD\*5.3\*41                                                            | Installed                 | No                   |
| RA\*4.5\*4                                                             | Installed                 | No                   |
| LR\*5.2\*127                                                           | Installed                 | No                   |
| SOW\*3\*42                                                             | Installed                 | No                   |
| OPC GENERATION MAIL GROUP (#216) field in the MAS PARAMETER (#43) file | Contains valid Mail Group | No                   |

<span id="_Toc193958047" class="anchor"></span>Table 20: DGPFAPIH APIs

14. This domain was distributed by patch XM\*DBA\*99.  
    Not installing this patch results in the loss of workload credit.  
    Not installing this patch results in the loss of workload credit.

# DBIA Agreements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following steps are used to obtain the database integration agreements for the PIMS package.

## DBIA Agreements—Custodial Package

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  FORUM.
19. DBA Menu.
20. Integration Agreements Menu.
21. Custodial Package Menu.
22. Active by Custodial Package Option.
23. Select Package Name: Registration or Scheduling.

## DBIA Agreements—Subscriber Package

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  FORUM.
24. DBA Menu.
25. Integration Agreements Menu.
26. Subscriber Package Menu.
27. Print Active by Subscriber Package Option.
28. Start with subscriber package:
- DG to DGZ, VA to VAZ (ADT)

## Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Any PIMS option in File \#19 that is a menu option should be able to run independently provided the user has the appropriate keys and VA FileMan access.

In order to use the PCMM client software, the user *must* be assigned the SC PCMM GUI WORKSTATION option as either a primary or secondary menu option; unless the user has been assigned the XUPROGMODE security key.

This key, usually given to IRM staff, allows use of the client software without the SC PCMM GUI WORKSTATION option being assigned.

## Package-Wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no package-wide variables associated with the PIMS package.

## VADPT Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Scheduling Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

SDUTL3 contains utilities used to display and retrieve data from the CURRENT PC TEAM and CURRENT PC PRACTITIONER fields in the PATIENT (#2) file.

Documentation can also be found in the routine.

<span id="_Toc193958002" class="anchor"></span>Figure 4: \$\$OUTPTPR^SDUTL3—Routine Documentation

\$\$OUTPTPR^SDUTL3(PARM 1) - displays data from CURRENT PC

PRACTITIONER field

Input PARM 1 The internal entry of the PATIENT file.

Output CURRENT PC PRACTIONER in Internal^External format.

If look-up is unsuccessful, 0 will be returned.

<span id="_Toc193958003" class="anchor"></span>Figure 5: \$\$OUTPTTM^SDUTL3—Routine Documentation

\$\$OUTPTTM^SDUTL3(PARM 1) - displays data from CURRENT PC TEAM field.

Input PARM 1 The internal entry of the PATIENT file.

Output CURRENT PC TEAM in Internal^External format. If

look-up is unsuccessful, 0 will be returned.

<span id="_Toc193958004" class="anchor"></span>Figure 6: \$\$OUTPTAP^SDUTL3—Routine Documentation

\$\$OUTPTAP^SDUTL3(PARM 1, PARM 2)

Input PARM 1 The internal entry of the PATIENT file.

Input PARM 2 The relevant data.

Output Pointer to File 200^external value of the name.

\$\$GETALL^SCAPMCA(PARM 1, PARM 2, PARM 3)

This tag returns all information on a patient’s assignment. Please review the documentation in the SCAPMCA routine.

<span id="_Toc193958005" class="anchor"></span>Figure 7: INPTPR^SDUTL3—Routine Documentation

INPTPR^SDUTL3(PARM 1, PARM 2) - stores data in CURRENT PC

PRACTITIONER field.

Input PARM 1 The internal entry of the PATIENT file.

PARM 2 Pointer to the NEW PERSON file indicating the

practitioner associated with the patient's care.

Output SDOKS 1 if data is stored successfully; 0 otherwise

<span id="_Toc193958006" class="anchor"></span>Figure 8: INPTTM^SDUTL3—Routine Documentation

INPTTM^SDUTL3(PARM 1, PARM 2) - stores data in CURRENT PC TEAM field.

Input PARM 1 The internal entry of the PATIENT file.

PARM 2 Pointer to the TEAM file indicating the team associated

with the patient's care.

Output SDOKS 1 if data is stored successfully; 0 otherwise

### Patient Record Flag Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Integration Agreement Applicable

<span id="_Toc193958007" class="anchor"></span>Figure 9: How to Access Integration Agreements

      4903     NAME: PATIENT RECORD FLAG DATA RETRIEVAL

  CUSTODIAL PACKAGE: REGISTRATION                              

SUBSCRIBING PACKAGE: SCHEDULING                                

                        Scheduling requires Patient Record Flag information

                        as part of a new missed appointment report supporting

                        the High Risk Mental Health Initiative.  This report

                        needs to be able to determine which patients  missing

                        a recent appointment have a specified Patient Record

                        Flag assigned. 

                     CLINICAL REMINDERS                        

                        Retrieval of High Risk Mental Health Patient Flag

                        information. 

                     HEALTH SUMMARY                            

                        ADDED 7/19/2011

              USAGE: Controlled Subscri  ENTERED: JAN  6,2011

             STATUS: Active              EXPIRES:

           DURATION: Till Otherwise Agr  VERSION:

        DESCRIPTION:                        TYPE: Routine

   These API's provide a means to retrieve detailed Patient Record Flag

   information by patient and patient record flag, and, to retrieve a list of

   patients with a specific assigned patient record flag during a specified

   date range. 

     ROUTINE: DGPFAPIH

   COMPONENT:  GETINF

               This function will return detailed information from the

               Patient Record Flag files for the specified patient and PRF

               flag.  A date range for active PR Flags is optional.  Data

               array output example:

               DGARR("ASSIGNDT") - Date of initial assignment.

                      i.e. 3110131.093248^Jan 31, 2011@09:32:48)

               DGARR("CATEGORY") - National or Local flag category.

                      i.e. II (LOCAL)^II (LOCAL) DGARR("FLAG") - Variable

               pointer to Local/National flag files and flag name.

                      i.e. 1;DGPF(26.11,^HIGH RISK FOR SUICIDE

               DGARR("FLAGTYPE") - Type of flag usage. 

                      i.e. 1^BEHAVIORAL DGARR("HIST",n,"ACTION") - Type of

               action for history entry

                      i.e. 1^NEW ASSIGNMENT DGARR("HIST",n,"APPRVBY") -

               Person approving the flag assignment

                      i.e. 112345^PERSON,STEVE DGARR("HIST",1,"COMMENT",1,0)
               - Comment for record assignment action

                      i.e "New record flag assignment."

               DGARR("HIST",n,"DATETIME") - Date/Time of Action

                      i.e. 3110131.093248^JAN 31, 2011@09:32:48

               DGARR("HIST",n,"TIULINK") - Pointer to the TIU Document file

               (#8925)

                      i.e. "^" DGARR("NARR",n,0) - Describes the purpose and

               instructions for the application of the flag.

                      i.e. "TEST ENTRY" DGARR("ORIGSITE") - Site that

               initially assigned this flag (Relevant to National flags only)

                      i.e. 500^REDACTED DGARR("OWNER") - Site which

               currently "Owns" this flag (Relevant to National flags only)

                       i.e. 500^REDACTED DGARR("REVIEWDT") - Date for

               next review of record flag assignment

                      i.e. 3110501^MAY 01, 2011 DGARR("TIUTITLE") - Pointer

               to the TIU Document Definition file (#8925.1)

                      i.e. 1309^PATIENT RECORD FLAG CATEGORY II - RESEARCH

               STUDY

   VARIABLES:  Input     DGDFN

                           This is the DFN (IEN) for the patient in the

                           PATIENT File (#2).  This is a required variable. 

   VARIABLES:  Input     DGPRF

                           Variable pointer to either the PRF LOCAL FLAG File

                           (#26.11) or to the PRF NATIONAL FLAG file

                           (#26.15).  This is a required variable. 

                            

                           For National Flags:  IEN;DGPF(26.15,

                              For Local Flags:  IEN;DGPF(26.11,

   VARIABLES:  Input     DGSTART

                           Start date for when to begin search for active PRF

                           flags.  This date must be in FM format, i.e.
                           3110106.  This variable is optional, if null,

                           searches will begin with the earliest assigned

                           entry in the PRF ASSIGNMENT HISTORY file (#26.14)

   VARIABLES:  Input     DGEND

                           End date for the search for active PRF entries.

                           This date must be in FM format, i.e. 3110107.

                           This variable is optional, if null or not passed

                           in, all entries to the end of the PRF ASSIGNMENT

                           HISTORY file (#26.14) will be searched. 

   VARIABLES:  Both      DGARR

                           This variable contains the array name for the

                           return data.  This is optional.  If an array name

                           is not specified, the return data is returned in

                           local array "DGPFAPI1". 

   VARIABLES:  Output    DGRSLT

                           Return value from the API call.  Returns "1" if

                           the API was successful in returning PRF data,

                           returns "0" if the API was unsuccessful in

                           returning PRF data. 

   COMPONENT:  GETLST

               This function call returns a list of patients with a specified

               Patient Record Flag assigned for a specified date range. 

                

                 DGARR(DFN,n) - Patient Name^VPID^Date of initial

               assignment^National or Local flag category^flag name

                

               Example:

                  DGARR(9999955648,0)="EASPATIENT,ONE

               A^5000000295V790537^3100201.103713^II (LOCAL)^HIGH RISK FOR

               SUICIDE"

   VARIABLES:  Input     DGPRF

                           Variable pointer to either the PRF LOCAL FLAG File

                           (#26.11) or the PRF NATIONAL FLAG File (#26.15).

                           This variable is required. 

                            

                              National:  IEN;DGPF(26.15,

                                 Local:  IEN;DGPF(26.11,

   VARIABLES:  Input     DGSTART

                           This is the start date to begin searching for

                           patients with the assigned Patient Record Flag.

                           This date must be in FM format, i.e. 3100110. This

                           variable is optional. 

   VARIABLES:  Input     DGEND

                           This is end date for the search range for patients

                           with the assigned Patient Record Flag.  This date

                           must be in FM format, i.e. 3100112. This variable

                           is optional. 

   VARIABLES:  Both      DGARR

                           This variable contains the array name where the

                           returned patient information will be placed.  This

                           is optional, if an array name is not specified,

                           the data will be returned in a TMP Global,

                           ^TMP("PRFLST")

   VARIABLES:  Output    DGRSLT

                           This variable returns a count of the patients

                           placed in the return list. 

           KEYWORDS: PATIENT RECORD FLAGS

                      \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

<span id="_Toc193958008" class="anchor"></span>Figure 10: Inquire to an Integration Control Registration

Select INTEGRATION CONTROL REGISTRATIONS Option: INQ \<Enter\> Inquire to an Integration Control Registration

Select INTEGRATION REFERENCES: DGPFAPIU \<Enter\> 5491     REGISTRATION     Controlled Subscription     PATIENT RECORD FLAG VARIABLE POINTER     DGPFAPIU

DEVICE: ;;999 \<Enter\> SSH VIRTUAL TERMINAL

INTEGRATION REFERENCE INQUIRY \#5491            MAY  3,2012  10:27    PAGE 1

-----------------------------------------------------------------------------

      5491     NAME: PATIENT RECORD FLAG VARIABLE POINTER

  CUSTODIAL PACKAGE: REGISTRATION                               

SUBSCRIBING PACKAGE: SCHEDULING                                

                     CLINICAL REMINDERS                        

                     HEALTH SUMMARY                            

                        ADDED 7/19/2011

              USAGE: Controlled Subscri  ENTERED: JAN 31,2011

             STATUS: Active              EXPIRES:

           DURATION: Till Otherwise Agr  VERSION:

        DESCRIPTION:                        TYPE: Routine

   Builds and returns a variable pointer to the Patient Record Flag National

   or Local files based on the textual flag name. 

     ROUTINE: DGPFAPIU

   COMPONENT:  GETFLAG

               Get the variable pointer value for the flag text passed in.

   VARIABLES:  Input     DGPRF

                           Name of the Patient Record Flag in the PRF

                           NATIONAL FLAG file, \#26.15, or in the PRF LOCAL

                           FLAG file, \#26.11.  The value passed in must match

                           the NAME field, \#.01, and is a free text value. 

   VARIABLES:  Input     DGCAT

                           Optional File category value.  This value is either

                           "N" to lookup the pointer value in the National

                           file, or "L" to lookup the pointer value in the

                           PRF Local file.  If null, both the National and

                           Local files will be checked for the pointer value. 

   VARIABLES:  Output    DGRSLT

                           Returns one of the following values:

                              IEN;DGPF(National or Local File number,  i.e.

                           1;DGPF(26.11,

                            

                           Will return "-1;NOT FOUND"  If no flag is found

                           matching the test

                                       "-1;NOT ACTIVE" If the flag is not

                           currently active. 

           KEYWORDS:

#### DGPFAPIH

<table>
<caption><p><span id="_Toc193958048" class="anchor"></span>Table 21: DGPFAPIU API</p></caption>
<colgroup>
<col style="width: 36%" />
<col style="width: 63%" />
</colgroup>
<thead>
<tr class="header">
<th>API</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>GETINF^DGPFAPIH</strong></p>
<p>(Increment 1)</p>
<p><strong>DGPFAPIH</strong> is both a routine and an API/Integration agreement (#4903)</p></td>
<td><p><strong>DGPFAPIH</strong>: This routine implements the two Application Programming Interface (API) call points for retrieving Patient Record Flag (PRF) information. One call point is for a specific patient and record and the second call point is for a list of patients with a specific, active, Patient Record Flag.</p>
<p>This API obtains the Patient Record Flag assignment information and status for the specified patient, patient record flag and date range. The return data is provided in an array using the <strong>target_root</strong> specified by the user or in the default array variable <strong>DGPFAPI1</strong>. The DATE/TIME (#.02) field of the PRF ASSIGNMENT HISTORY (#26.14) file entry determines whether the entry falls within the specified date range. If no date range is specified, all entries are returned.</p></td>
</tr>
<tr class="even">
<td><p><strong>GETLST^DGPFAPIH</strong></p>
<p>(Increment 1)</p></td>
<td>This API retrieves a list of patients active at some point within a specified date range for a specified Patient Record Flag. The date range is required for this API; though, the same date can be entered to specify a single date. The return data is provided in an array using the <strong>target_root</strong> specified by the user or in the default array variable <strong>DGPFAPI2</strong>. The DATE/TIME (#.02) field of the PRF ASSIGNMENT HISTORY (#26.14) file entry determines whether the entry falls within the specified date range.</td>
</tr>
</tbody>
</table>

<span id="_Toc193958048" class="anchor"></span>Table 21: DGPFAPIU API

#### DGPFAPIU

<table>
<caption><p><span id="_Ref54095096" class="anchor"></span>Table 22: VA FileMan Access Codes</p></caption>
<colgroup>
<col style="width: 36%" />
<col style="width: 63%" />
</colgroup>
<thead>
<tr class="header">
<th>API</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>DGPFAPIU</strong></p>
<p>(Increment 1)</p></td>
<td><p>This routine provides support utilities and functions for the new Application Programming Interface calls.</p>
<p>This procedure checks if the Patient Record Flag was active at any point during the specified date range. The procedure accepts a date range parameter, which specifies whether “<strong>A</strong>”ll dates or only a “<strong>S</strong>”pecified date range is to be checked.</p>
<p>The PRF ASSIGNMENT HISTORY (#26.14) file was <em>not</em> designed for this type of date interaction, so the algorithm in this procedure has to make a number of assumptions when interpreting the dates and PRF actions. While there can only be one “<strong>New Assignment</strong>” entry, it is possible to have multiple “<strong>Continue</strong>”, “<strong>Inactivate</strong>”, and “<strong>Reactivate</strong>” action entries. In addition, the <strong>Entered In Error</strong> action can pose additional issues with determining a status during a specific date range.</p>
<p><strong>REF:</strong> See Appendix B for examples of date range and PRF History status entries.</p></td>
</tr>
<tr class="even">
<td>GETFLAG^DGPFAPIU (Increment 1)</td>
<td>This function gets the variable pointer value for the Patient Record Flag passed in. The PRF is passed in as a text value. If the optional flag category is passed in, only that category is checked for the PRF. If no category is passed in, then first the National category is checked in the integration Agreement # 5491.</td>
</tr>
</tbody>
</table>

<span id="_Ref54095096" class="anchor"></span>Table 22: VA FileMan Access Codes

## VAUTOMA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VAUTOMA is a routine that does a one/many/all prompt; returning the chosen values in a subscripted variable specified by the calling programmer.

Input Variables

- VAUTSTR—String that describes what is to be entered.
- VAUTNI—Defines if array is sorted alphabetically or numerically.
- VAUTVB—Name of the subscripted variable to be returned.
- VAUTNALL—Define this variable if you do not want the user to be given the ALL option.

Other variables as required by a call to ^DIC (see *VA FileMan Developer’s Guide*).

Output Variables

As defined in VAUTVB.

## VAFMON

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VAFMON is a routine that returns income or dependent information on a patient.

\$\$INCOME^VAFMON(PARM 1,PARM 2)

- PARM 1—The internal entry of the PATIENT (#2) file.
- PARM 2—The date for which the income is calculated.

\$\$DEP^VAFMON(PARM 1,PARM 2)

- PARM 1—The internal entry of the PATIENT (#2) file.
- PARM 2—The date for which the income is calculated.

## AIT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See the Ambulatory Care Reporting Project Interface Toolkit (AIT). The AIT is a set of programmer tools that provide access to outpatient encounter data.

# How To Generate Online Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes some of the various methods by which users may secure PIMS technical documentation.

Online technical documentation pertaining to the PIMS software, in addition to that which is located in the help prompts and on the help screens which are found throughout the PIMS package, can be generated by using several Kernel and VA FileMan options.

These include but are not limited to:

- XINDEX
- Menu Management: Inquire Option File
- Print Option File
- VA FileMan: List File Attributes

Entering question marks at the "Select ... Option:" prompt can also provide users with valuable technical information. For example:

- A single question mark (?) lists all options that can be accessed from the current option.
- Entering two question marks (??) lists all options accessible from the current one, showing the formal name and lock for each.
- Three question marks (???) displays a brief description for each option in a menu.
- An option name preceded by a question mark (?OPTION) shows extended help, if available, for that option.
15. REF: For a more exhaustive option listing and further information about other utilities that supply online technical information, consult the VistA *Kernel 8.0 and Kernel Toolkit 7.3 Systems Management Guide*.

## XINDEX

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The XINDEX option analyzes the structure of a routine(s) to determine in part if the routine(s) adheres to VistA Programming Standards. The XINDEX output can include the following components:

- Compiled list of errors and warnings
- Routine listing
- Local variables
- Global variables
- Naked globals
- Label references
- External references

By running XINDEX for a specified set of routines, the user is afforded the opportunity to discover any deviations from VistA Programming Standards that exist in the selected routine(s) and to see how routines interact with one another, that is, which routines call or are called by other routines.

To run XINDEX for the PIMS package, specify the following namespaces at the "routine(s) ?\>" prompt: DG\*, DPT\*, SD\*, VA\*, SC\*.

PIMS initialization routines that reside in the UCI in which XINDEX is being run, compiled template routines, and local routines found within the PIMS namespaces should be omitted at the "routine(s) ?\>" prompt.

To omit routines from selection, preface the namespace with a minus sign (-).

## Inquire to Option File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Inquire to Option File menu manager option provides the following information about a specified option(s):

- Option name
- Menu text
- Option description
- Type of option
- Lock (if any)

In addition, all items on the menu are listed for each menu option.

- DPT—Patient File Look-up, Patient Sensitivity
- SD and SC—Scheduling
- VA—Generic utility processing

## Print Options File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Print Options File utility generates a listing of options from the OPTION (#19) file. The user can choose to print all of the entries in this file or may elect to specify a single option or range of options.

To obtain a list of PIMS options, the following option namespaces should be specified:

- DG to DGZ
- SD to SDZ

## List File Attributes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This VA FileMan List File Attributes option allows the user to generate documentation pertaining to files and file structure. Use of this option via the "Standard" format yields the following data dictionary information for a specified file(s):

- File name and description
- Identifiers
- Cross-references
- Files pointed to by the file specified
- Files that point to the file specified
- Input templates
- Print templates
- Sort templates.

In addition, the following applicable data is supplied for each field in the file:

- Field name
- Number
- Title
- Global location
- Description
- Help prompt
- Cross-reference(s)
- Input transform
- Date last edited
- Notes

Using the "Global Map" format of this option generates an output that lists the following:

- All cross-references for the file selected
- Global location of each field in the file
- Input templates
- Print templates
- Sort templates

## Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### General Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Routines that generate statistics for AMIS or NPCDB workload should NOT be locally modified.

### Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are the steps to obtain information about the security keys contained in the PIMS package.

1.  VA FileMan Menu.
29. Print File Entries Option.
30. Output from what File: SECURITY KEY.
31. Sort by: Name.
32. Start with name:
- DG to DGZ, VA to VAZ (ADT)
33. Within name, sort by: \<Enter\>.
34. First print field: Name.
35. Then print field: Description.

### Legal Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PIMS software package makes use of Current Procedural Terminology (CPT) codes that is an American Medical Association (AMA) copyrighted product. Its use is governed by the terms of the agreement between the Department of Veterans Affairs and the AMA. The CPT copyright notice is displayed for various PIMS users and should not be turned off.

## VA FileMan Access Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The table below lists the *recommended* VA FileMan Access Codes associated with each file contained in the PIMS package. This list can be used to assist in assigning users appropriate VA FileMan Access Codes.

<table>
<caption><p><span id="_Ref54095301" class="anchor"></span>Table 23: Supported References</p></caption>
<colgroup>
<col style="width: 13%" />
<col style="width: 24%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
</colgroup>
<thead>
<tr class="header">
<th><p>File</p>
<p>Number</p></th>
<th><p>File</p>
<p>Name</p></th>
<th><p>DD</p>
<p>Access</p></th>
<th><p>RD</p>
<p>Access</p></th>
<th><p>WR</p>
<p>Access</p></th>
<th><p>DEL</p>
<p>Access</p></th>
<th><p>LAYGO</p>
<p>Access</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>2</td>
<td>PATIENT</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>D</strong></td>
<td><strong>@</strong></td>
<td><strong>D</strong></td>
</tr>
<tr class="even">
<td>5</td>
<td>STATE</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>8</td>
<td>ELIGIBILITY CODE</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>8.1</td>
<td>MAS ELIGIBILITY CODE</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>8.2</td>
<td>IDENTIFICATION FORMAT</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>10</td>
<td>RACE</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>11</td>
<td>MARITAL STATUS</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>13</td>
<td>RELIGION</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>21</td>
<td>PERIOD OF SERVICE</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>22</td>
<td>POW PERIOD</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>23</td>
<td>BRANCH OF SERVICE</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>25</td>
<td>TYPE OF DISCHARGE</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>25.11</td>
<td>HEALTH BENEFIT PLAN</td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>26.11</td>
<td>PRF LOCAL FLAG</td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>26.12</td>
<td>PRF LOCAL FLAG HISTORY</td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>26.13</td>
<td>PRF ASSIGNMENT</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>26.14</td>
<td>PRF ASSIGNMENT HISTORY</td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>26.15</td>
<td>PRF NATIONAL FLAG</td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>26.16</td>
<td>PRF TYPE</td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>26.17</td>
<td>PRF HL7 TRANSMISSION LOG</td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>26.18</td>
<td>PRF PARAMETERS</td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>26.19</td>
<td>PRF HL7 QUERY LOG</td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>26.21</td>
<td>PRF HL7 EVENT</td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>26.22</td>
<td>PRF HL7 REQUEST LOG FILE</td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>27.11</td>
<td>PATIENT ENROLLMENT</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>27.12</td>
<td>ENROLLMENT QUERY LOG</td>
<td><strong>@</strong></td>
<td></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>27.14</td>
<td><p>ENROLLMENT/ELIGIBILITY</p>
<p>UPLOAD AUDIT</p></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>27.15</td>
<td>ENROLLMENT STATUS</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>27.16</td>
<td>ENROLLMENT GROUP THRESHOLD</td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>27.17</td>
<td>CATASTROPHIC DISABILITY REASONS</td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>28.11</td>
<td>NOSE AND THROAT RADIUM HISTORY</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>29.11</td>
<td>MST HISTORY</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>30</td>
<td>DISPOSITION LATE REASON</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>35</td>
<td>OTHER FEDERAL AGENCY</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>35.1</td>
<td>SHARING AGREEMENT CATEGORY</td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>35.2</td>
<td>SHARING AGREEMENT SUB-CATEGORY</td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>37</td>
<td>DISPOSITION</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>38.1</td>
<td>DG SECURITY LOG</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>D</strong></td>
<td><strong>@</strong></td>
<td><strong>D</strong></td>
</tr>
<tr class="odd">
<td>38.5</td>
<td>INCONSISTENT DATA</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>38.6</td>
<td>INCONSISTENT DATA ELEMENTS</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>39.1</td>
<td>EMBOSSED CARD TYPE</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>39.2</td>
<td>EMBOSSING DATA</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>39.3</td>
<td>EMBOSSER EQUIPMENT FILE</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>39.4</td>
<td>ADT/HL7 TRANSMISSION</td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>39.6</td>
<td>VIC REQUEST</td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>39.7</td>
<td>VIC HL7 TRANSMISSION LOG</td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>40.7</td>
<td>CLINIC STOP</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>40.8</td>
<td>MEDICAL CENTER DIVISION</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>40.9</td>
<td>LOCATION TYPE</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>41.1</td>
<td>SCHEDULED ADMISSION</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>D</strong></td>
<td><strong>D</strong></td>
<td><strong>D</strong></td>
</tr>
<tr class="odd">
<td>41.41</td>
<td>PRE-REGISTRATION AUDIT</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>D</strong></td>
<td><strong>D</strong></td>
<td><strong>D</strong></td>
</tr>
<tr class="even">
<td>41.42</td>
<td>PRE-REGISTRATION CALL LIST</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>D</strong></td>
<td><strong>D</strong></td>
<td><strong>D</strong></td>
</tr>
<tr class="odd">
<td>41.43</td>
<td>PRE-REGISTRATION CALL LOG</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>D</strong></td>
<td><strong>D</strong></td>
<td><strong>D</strong></td>
</tr>
<tr class="even">
<td>41.9</td>
<td>CENSUS</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>42</td>
<td>WARD LOCATION</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>D</strong></td>
<td><strong>@</strong></td>
<td><strong>D</strong></td>
</tr>
<tr class="even">
<td>42.4</td>
<td>SPECIALTY</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>42.5</td>
<td>WAIT LIST</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>D</strong></td>
<td><strong>D</strong></td>
<td><strong>D</strong></td>
</tr>
<tr class="even">
<td>42.55</td>
<td>PRIORITY GROUPING</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>42.6</td>
<td>AMIS 334-341</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>D</strong></td>
<td><strong>D</strong></td>
<td><strong>D</strong></td>
</tr>
<tr class="even">
<td>42.7</td>
<td>AMIS 345&amp;346</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>D</strong></td>
<td><strong>D</strong></td>
<td><strong>D</strong></td>
</tr>
<tr class="odd">
<td>43</td>
<td>MAS PARAMETERS</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>D</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>43.1</td>
<td>MAS EVENT RATES</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>D</strong></td>
<td><strong>D</strong></td>
<td><strong>D</strong></td>
</tr>
<tr class="odd">
<td>43.11</td>
<td>MAS AWARD</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>D</strong></td>
<td><strong>D</strong></td>
<td><strong>D</strong></td>
</tr>
<tr class="even">
<td>43.4</td>
<td>VA ADMITTING REGULATION</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>43.5</td>
<td>G&amp;L CORRECTIONS</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>D</strong></td>
<td><strong>D</strong></td>
<td><strong>D</strong></td>
</tr>
<tr class="even">
<td>43.61</td>
<td>G&amp;L TYPE OF CHANGE</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>43.7</td>
<td>ADT TEMPLATE</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>44</td>
<td>HOSPITAL LOCATION</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>D</strong></td>
<td><strong>@</strong></td>
<td><strong>D</strong></td>
</tr>
<tr class="odd">
<td>45</td>
<td>PTF</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>D</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>45.1</td>
<td>SOURCE OF ADMISSION</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>45.2</td>
<td>PTF TRANSFERRING FACILITY</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>D</strong></td>
<td><strong>@</strong></td>
<td><strong>D</strong></td>
</tr>
<tr class="even">
<td>45.3</td>
<td>SURGICAL SPECIALTY</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>45.4</td>
<td>PTF DIALYSIS TYPE</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>45.5</td>
<td>PTF MESSAGE</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>45.6</td>
<td>PLACE OF DISPOSITION</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>45.61</td>
<td>PTF ABUSED SUBSTANCE</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>45.64</td>
<td>PTF AUSTIN ERROR CODES</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>45.68</td>
<td>FACILITY SUFFIX</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>45.7</td>
<td>FACILITY TREATING SPECIALTY</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>D</strong></td>
<td><strong>@</strong></td>
<td><strong>D</strong></td>
</tr>
<tr class="even">
<td>45.81</td>
<td>STATION TYPE</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>45.82</td>
<td>CATEGORY OF BENEFICIARY</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>45.83</td>
<td>PTF RELEASE</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>45.84</td>
<td>PTF CLOSE OUT</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>45.85</td>
<td>CENSUS WORKFILE</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>D</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>45.86</td>
<td>PTF CENSUS DATE</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>45.87</td>
<td>PTF TRANSACTION REQUEST LOG</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>45.88</td>
<td>PTF EXPANDED CODE CATEGORY</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>45.89</td>
<td>PTF EXPANDED CODE</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>45.9</td>
<td>PAF</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>D</strong></td>
<td><strong>D</strong></td>
<td><strong>D</strong></td>
</tr>
<tr class="even">
<td>45.91</td>
<td>RUG-II</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>46</td>
<td>INPATIENT CPT</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>D</strong></td>
<td><strong>#</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>46.1</td>
<td>INPATIENT POV</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>D</strong></td>
<td><strong>#</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>47</td>
<td>MAS FORMS AND SCREENS</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>D</strong></td>
<td><strong>#</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>48</td>
<td>MAS RELEASE NOTES</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>D</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>48.5</td>
<td>MAS MODULE</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>389.9</td>
<td>STATION NUMBER (TIME SENSITIVE)</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>390</td>
<td>ENROLLMENT RATED DISABILITY UPLOAD AUDIT</td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>391</td>
<td>TYPE OF PATIENT</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>391.1</td>
<td>AMIS SEGMENT</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>391.31</td>
<td>HOME TELEHEALTH PATIENT</td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>403.46</td>
<td>STANDARD POSITION</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>403.47</td>
<td>TEAM PURPOSE</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>404.41</td>
<td>OUTPATIENT PROFILE</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>404.42</td>
<td>PATIENT TEAM ASSIGNMENT</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>404.43</td>
<td>PATIENT TEAM POSITION ASSIGNMENT</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>404.44</td>
<td>PCMM PARAMETER</td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>404.45</td>
<td>PCMM SERVER PATCH</td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>404.46</td>
<td>PCMM CLIENT PATCH</td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>404.471</td>
<td>PCMM HL7 TRANSMISSION LOG</td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>404.472</td>
<td>PCMM HL7 ERROR LOG</td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>404.48</td>
<td>PCMM HL7 EVENT</td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>404.49</td>
<td>PCMM HL7 ID</td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>404.51</td>
<td>TEAM</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>404.52</td>
<td>POSITION ASSIGNMENT HISTORY</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>404.53</td>
<td>PRECEPTOR ASSIGNMENT HISTORY</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>404.56</td>
<td>TEAM AUTOLINK</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>404.57</td>
<td>TEAM POSITION</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>404.58</td>
<td>TEAM HISTORY</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>404.59</td>
<td>TEAM POSITION HISTORY</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>404.61</td>
<td>MH PCMM STOP CODES</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>405</td>
<td>PATIENT MOVEMENT</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>405.1</td>
<td>FACILITY MOVEMENT TYPE</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>D</strong></td>
<td><strong>@</strong></td>
<td><strong>D</strong></td>
</tr>
<tr class="odd">
<td>405.2</td>
<td>MAS MOVEMENT TYPE</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>405.3</td>
<td>MAS MOVEMENT TRANSACTION TYPE</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>405.4</td>
<td>ROOM-BED</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>D</strong></td>
<td><strong>@</strong></td>
<td><strong>D</strong></td>
</tr>
<tr class="even">
<td>405.5</td>
<td>MAS OUT-OF-SERVICE</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>405.6</td>
<td>ROOM-BED DESCRIPTION</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>D</strong></td>
<td><strong>@</strong></td>
<td><strong>D</strong></td>
</tr>
<tr class="even">
<td>406.41</td>
<td>LODGING REASON</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>D</strong></td>
<td><strong>@</strong></td>
<td><strong>D</strong></td>
</tr>
<tr class="odd">
<td>407.7</td>
<td>TRANSMISSION ROUTERS</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>408</td>
<td>DISCRETIONARY WORKLOAD</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>408.11</td>
<td>RELATIONSHIP</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>408.12</td>
<td>PATIENT RELATION</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>408.13</td>
<td>INCOME PERSON</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>408.21</td>
<td>INDIVIDUAL ANNUAL INCOME</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>408.22</td>
<td>INCOME RELATION</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>408.31</td>
<td>ANNUAL MEANS TEST</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>408.32</td>
<td>MEANS TEST STATUS</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>408.33</td>
<td>TYPE OF TEST</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>408.34</td>
<td>SOURCE OF INCOME TEST</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>408.41</td>
<td>MEANS TEST CHANGES</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>408.42</td>
<td>MEANS TEST CHANGES TYPE</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>409.41</td>
<td>OUTPATIENT CLASSIFICATION TYPE</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>409.42</td>
<td>OUTPATIENT CLASSIFICATION</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>D</strong></td>
<td><strong>D</strong></td>
<td><strong>D</strong></td>
</tr>
<tr class="even">
<td>409.45</td>
<td>OUTPATIENT CLASSIFICATION STOP CODE EXCEPTION</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>409.64</td>
<td>QUERY OBJECT</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>409.67</td>
<td>CLINIC GROUP</td>
<td><strong>@</strong></td>
<td></td>
<td><strong>D</strong></td>
<td><strong>@</strong></td>
<td><strong>D</strong></td>
</tr>
<tr class="odd">
<td>409.68</td>
<td>OUTPATIENT ENCOUNTER</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>409.73</td>
<td>TRANSMITTED OUTPATIENT ENCOUNTER</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>409.74</td>
<td>DELETED OUTPATIENT ENCOUNTER</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>409.75</td>
<td>TRANSMITTED OUTPATIENT ENCOUNTER ERROR</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>409.76</td>
<td>TRANSMITTED OUTPATIENT ENCOUNTER ERROR CODE</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>409.77</td>
<td>ACRP TRANSMISSION HISTORY</td>
<td><strong>@</strong></td>
<td><strong>d</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="odd">
<td>409.91</td>
<td>ACRP REPORT TEMPLATE</td>
<td><strong>@</strong></td>
<td></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
<tr class="even">
<td>409.92</td>
<td>ACRP REPORT TEMPLATE PARAMETER</td>
<td><strong>@</strong></td>
<td></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
<td><strong>@</strong></td>
</tr>
</tbody>
</table>

<span id="_Ref54095301" class="anchor"></span>Table 23: Supported References

# VADPT Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VADPT is a utility routine designed to provide a central point where a programmer can obtain information concerning a patient's record. Supported entry points are provided, which return demographics, inpatient status, eligibility information, etc.

Access to patient information is not limited to using the supported entry points in VADPT. Integration agreements can be established through the DBA between PIMS and other packages to reference information. Additionally, several data elements are supported without an integration agreement.

## Supported References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The table below lists references to patient information (PATIENT \[#2\] file) that are supported without an integration agreement. All nationally distributed cross-references on these fields are also supported.

| Field Name                | Field \#  | Global Location | Type of Access |
|---------------------------|-----------|-----------------|----------------|
| NAME                      | (#.01)    | 0;1             | Read           |
| PREFERRED NAME            | (#.2405)  | .24;5           | Read           |
| SEX                       | (#.02)    | 0;2             | Read           |
| DATE OF BIRTH             | (#.03)    | 0;3             | Read           |
| AGE                       | (#.033)   | N/A             | Read           |
| MARITAL STATUS            | (#.05)    | 0;5             | Read           |
| RACE                      | (#.06)    | 0;6             | Read           |
| OCCUPATION                | (#.07)    | 0;7             | Read           |
| RELIGIOUS PREFERENCE      | (#.08)    | 0;8             | Read           |
| DUPLICATE STATUS          | (#.081)   | 0;18            |                |
| PATIENT MERGED TO         | (#.082)   | 0;19            |                |
| CHECK FOR DUPLICATE       | (#.083)   | 0;20            |                |
| SOCIAL SECURITY NUMBER    | (#.09)    | 0;9             | Read           |
| REMARKS                   | (#.091)   | 0;10            | Read           |
| PLACE OF BIRTH \[CITY\]   | (#.092)   | 0;11            | Read           |
| PLACE OF BIRTH \[STATE\]  | (#.093)   | 0;12            | Read           |
| WHO ENTERED PATIENT       | (#.096)   | 0;15            | Read           |
| DATE ENTERED INTO FILE    | (#.097)   | 0;16            | Read           |
| WARD LOCATION             | (#.1)     | .1;1            | Read           |
| ROOM-BED                  | (#.101)   | .101;1          | Read           |
| CURRENT MOVEMENT          | (#.102)   | .102;1          | Read           |
| TREATING SPECIALTY        | (#.103)   | .103;1          | Read           |
| PROVIDER                  | (#.104)   | .104;1          | Read           |
| ATTENDING PHYSICIAN       | (#.1041)  | .1041;1         | Read           |
| CURRENT ADMISSION         | (#.105)   | .105;1          | Read           |
| LAST DMMS EPISODE NUMBER  | (#.106)   | .106;1          | Read           |
| LODGER WARD LOCATION      | (#.107)   | .107;1          | Read           |
| CURRENT ROOM              | (#.108)   | .108;1          | Read           |
| CONFIDENTIAL PHONE NUMBER | (#.1315)  | .1315           | Read           |
| CURRENT MEANS TEST STATUS | (#.14)    | 0;14            | Read           |
| DATE OF DEATH             | (#.351)   | .35;1           | Read           |
| DEATH ENTERED BY          | (#.352)   | .35;2           | Read           |
| PRIMARY LONG ID           | (#.363)   | .36;3           |                |
| PRIMARY SHORT ID          | (#.364)   | .36;4           |                |
| CURRENT PC PRACTITIONER   | (#404.01) | PC;1            | Read           |
| CURRENT PC TEAM           | (#404.02) | PC;2            | Read           |
| LAST MEANS TEST           | (#999.2)  | N/A             | Read           |

<span id="_Ref58328533" class="anchor"></span>Table 24: Call Combinations

## Callable Entry Points in VADPT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The format of the data in the return array should be as follows.

- The root node must always be defined.
- Unless returning multiple value data, fields should be set in the root node in a caret-delimited string.
- Lower level subscripts may contain additional data fields as needed.
- If returning data in a multiple, the root node of the multiple should contain the number of subentries being returned.

Singular data values:

- VADM(s1) = field1^field2^field3...
- VADM(s1,s2) = field1^field2^field3...

Data in a multiple:

- VADM(s1,s2) = number of subentries
- VADM(s1,s2,1.n) = The nth repetition of the entry

Example:

- VADM(99)=field1^field2^field3...
- VADM(99,1)=3
- VADM(99,1,1)=field1^field2
- VADM(99,1,2)=field1^field2^field3
- VADM(99,1,3)=field1
- VADM(99,2)=field1

### DEM^VADPT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Description

This entry point returns demographic information for a patient.

Input

- DFN—This required variable is the internal entry number in the PATIENT (#2) file.
- VAPTYP—This optional variable can be set to the internal number of a patient eligibility. The variable can be used to indicate the patient's type such as VA, Department of Defense (DOD), or Indian Health Service (IHS) through the eligibility. If this variable is *not* defined or the eligibility does *not* exist, the VA patient IDs are returned.
- VAHOW—This optional variable can be set to a requested format for the output array. If this variable is *not* defined or does not contain one of the following values, the output array is returned with numeric subscripts:
- 1—Return the output array with alpha subscripts; see “CAI^VADPT” section \[e.g., VADM(1) would be VADM("NM")\].
- 2—Return the output in the ^UTILITY global with numeric subscripts \[e.g., ^UTILITY("VADM",\$J,1)\].
- 12—Return the output in the ^UTILITY global with alpha subscripts \[e.g., ^UTILITY("VADM",\$J,"NM")\].
- VAROOT—This optional variable can be set to a local variable or global name in which to return the output (e.g., VAROOT="DGDEM").

OUTPUT

- VADM(1)—The NAME of the patient (e.g., ADTPATIENT,ONE).
- VADM(2)—The SOCIAL SECURITY NUMBER of the patient in internal^external format (e.g., 000456789^000-45-6789).
- VADM(3)—The DATE OF BIRTH of the patient in internal^external format (e.g., 2551025^OCT 25,1955).
- VADM(4)—The AGE of the patient as of today, unless a date of death exists, in which case the age returned is as of that date (e.g., 36).
- VADM(5)—The SEX of the patient in internal^external format (e.g., M^MALE).
- VADM(6)—The DATE OF DEATH of the patient, should one exist, in internal^external format (e.g., 2881101.08^NOV 1,1988@08:00).
- VADM(7)—Any REMARKS concerning this patient which may be on file (e.g., Need to obtain dependent info).
- VADM(8)—The RACE of the patient in internal^external format (e.g., 1^WHITE,NON-HISPANIC).
16. This has been left for historical purposes only as the RACE field has been replaced by the RACE INFORMATION multiple.
- VADM(9)—The RELIGION of the patient in internal^external format (e.g., 99^CATHOLIC).
- VADM(10)—The MARITAL STATUS of the patient in internal^external format (e.g., 1^MARRIED).
- VADM(11)—Number of entries found in the ETHNICITY INFORMATION multiple (e.g., 1).
- VADM(11,1..n)—The *n<sup>th</sup>* repetition of ETHNICITY INFORMATION for the patient in internal^external format (e.g., 1^HISPANIC OR LATINO).
- VADM(11,1..n,1)—METHOD OF COLLECTION for the Nth repetition of ETHNICITY INFORMATION for the patient in internal^external format \[e.g., 2^PROXY)\].
- VADM(12)—Number of entries found in the RACE INFORMATION multiple (e.g., 1).
- VADM(12,1..n)—The *n<sup>th</sup>* repetition of RACE INFORMATION for the patient in internal^external format (e.g., 11^WHITE).
- VADM(12,1..n,1)—METHOD OF COLLECTION for the *nth* repetition of RACE INFORMATION for the patient in internal^external format \[e.g., 2^PROXY)\].
- VADM(13) – The current active entry from the LANGUAGE DATE/TIME (#.207) multiple in fileman format ^ human readable format \[e.g. 3210924.1426^SEP 24,2021@14:26\]
- VADM(13,1) - Current value for PREFERRED LANGUAGE for the patient in internal^external format \[e.g. 1^ENGLISH\]
- VADM(14) – set to null to avoid issues with groups that are only looking for root nodes
- VADM(14,1) – The number of entries found in the SEXUAL ORIENTATION multiple (e.g., 2).
- VADM(14,1,1..n) – The *n*<sup>th</sup> repetition of SEXUAL ORIENTATION for the patient in external^internal format (e.g., "Bisexual^BIS").
- VADM(14,1,1..n,1) – The current STATUS of the Sexual Orientation for the patient in external^internal format (e.g., "Active^A").
- VADM(14,1,1..n,2) – The DATE CREATED value of the Sexual Orientation for the patient in external^internal format (e.g., "JAN 24, 2022^3220124").
- VADM(14,1,1..n,3) – The DATE LAST UPDATED value of the Sexual Orientation for the patient in external^internal format (e.g., "JAN 24, 2022^3220124").
- VADM(14,1,1..n,4) – The Internal Entry Number (IEN) of the NOTE \[DOCUMENT TYPE in TUI DOCUMENT File (#8925)\] value of the Sexual Orientation for the patient in external^internal format (e.g., "CLINICAL WARNING^20").
- VADM(14,2) – The SEXUAL ORIENTATION DESCRIPTION for the patient free text format (e.g., "I have many sexual orientations").
- VADM(14,3) – The number of entries found in the PRONOUN multiple (e.g., 2).
- VADM(14,3,1..n) – The *n*<sup>th</sup> repetition of PRONOUN for the patient in external^internal format (e.g., "Ze/Zir/Zirs^ZIR").
- VADM(14,4) – The PRONOUN DESCRIPTION for the patient free text format (e.g., "I have many pronouns I would like used").
- VADM(14,5) – The SELF IDENTIFIED GENDER for the patient in internal^external format (e.g., Other^O")
- VADM(15) – Set to null to avoid issues with groups that are only looking for root nodes
- VADM(15,1) – The response to INDIAN SELF IDENTIFICATION (#.571) is NULL, “Y” or “N”.
- VADM(15,2) – The INDIAN START DATE (#.572) in internal format or NULL.
- VADM(15,3) – The INDIAN ATTESTATION DATE (#.573) in internal format or NULL.
- VADM(15,4) – The INDIAN END DATE (#.574) in internal format or NULL.
- VA("PID")—The PRIMARY LONG ID for a patient. The format of this variable depends on the type of patient if VAPTYP is set (e.g., 000-45-6789).
- VA("BID")—The PRIMARY SHORT ID for a patient. The format of this variable depends on the type of patient if VAPTYP is set (e.g., 6789).
- VAERR—The error flag has one of the following values:
- 0—No errors encountered.
- 1—Error encountered: DFN or ^DPT(DFN,0) is *not* defined.

### DEMUPD^VADPT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Description

This entry point returns demographic information for a patient.

Input

- DFN—This required variable is the internal entry number in the PATIENT (#2) file.
- VAPTYP—This optional variable can be set to the internal number of a patient eligibility. The variable can be used to indicate the patient's type such as VA, DOD, or IHS through the eligibility. If this variable is *not* defined or the eligibility does *not* exist, the VA patient IDs are returned.
- VAHOW—This optional variable can be set to a requested format for the output array. If this variable is *not* defined or does *not* contain one of the following values, the output array is returned with numeric subscripts:
- 1—Return the output array with alpha subscripts; see “CAI^VADPT” section \[e.g., VADEMO(1) would be VADEMO("NM")\].
- 2—Return the output in the ^UTILITY global with numeric subscripts \[e.g., ^UTILITY("VADEMO",\$J,1)\].
- 12—Return the output in the ^UTILITY global with alpha subscripts \[e.g., ^UTILITY("VADEMO",\$J,"NM",1)\] stores the PREFERRED NAME.
- VAROOT—This optional variable can be set to a local variable or global name in which to return the output (e.g., VAROOT="DGDEM").

Output

- VADEMO(1)—The NAME of the patient (e.g., ADTPATIENT,ONE).
- VADEMO(1,1)—The PREFERRED NAME of the patient (e.g., "NICKNAME JONES").
- VADEMO(2)—The SOCIAL SECURITY NUMBER of the patient in internal^external format (e.g., \#########^###-##-####).
- VADEMO(3)—The DATE OF BIRTH of the patient in internal^external format (e.g., 2551025^OCT 25,1955).
- VADEMO(4)—The AGE of the patient as of today, unless a date of death exists, in which case the age returned is as of that date (e.g., 36).
- VADEMO(5)—The SEX of the patient in internal^external format (e.g., M^MALE).
- VADEMO(6)—The DATE OF DEATH of the patient, should one exist, in internal^external format (e.g., 2881101.08^NOV 1,1988@08:00).
- VADEMO(7)—Any REMARKS concerning this patient which may be on file (e.g., Need to obtain dependent information).
- VADEMO(8)—The RACE of the patient in internal^external format (e.g., 1^WHITE,NON-HISPANIC).
17. This has been left for historical purposes only as the RACE field has been replaced by the RACE INFORMATION multiple.
- VADEMO(9)—The RELIGION of the patient in internal^external format (e.g., 99^CATHOLIC).
- VADEMO(10)—The MARITAL STATUS of the patient in internal^external format (e.g., 1^MARRIED).
- VADEMO(11)—Number of entries found in the ETHNICITY INFORMATION multiple (e.g., 1).
- VADEMO(11,1..n)—The *n*<sup>th</sup> repetition of ETHNICITY INFORMATION for the patient in internal^external format (e.g., 1^HISPANIC OR LATINO).
- VADEMO(11,1..n,1)—METHOD OF COLLECTION for the Nth repetition of ETHNICITY INFORMATION for the patient in internal^external format \[e.g., 2^PROXY)\].
- VADEMO(12)—Number of entries found in the RACE INFORMATION multiple (e.g., 1).
- VADEMO(12,1..n)—The *n*<sup>th</sup> repetition of RACE INFORMATION for the patient in internal^external format (e.g., 11^WHITE).
- VADEMO(12,1..n,1)—METHOD OF COLLECTION for the *n*<sup>th</sup> repetition of RACE INFORMATION for the patient in internal^external format \[e.g., 2^PROXY)\].
- VADEMO(12)—Number of entries found in the RACE INFORMATION multiple (e.g., 1).
- VADEMO(12,1..n)—The *n*<sup>th</sup> repetition of RACE INFORMATION for the patient in internal^external format (e.g., 11^WHITE).
- VADEMO(12,1..n,1)—METHOD OF COLLECTION for the *n*<sup>th</sup> repetition of RACE INFORMATION for the patient in internal^external format \[e.g., 2^PROXY)\].
- VADEMO(13) - The current active entry from the LANGUAGE DATE/TIME (#.207) multiple in fileman format ^ human readable format \[e.g. 3210924.1426^SEP 24,2021@14:26\]
- VADEMO(13,1) - Current value for PREFERRED LANGUAGE for the patient in internal^external format \[e.g. 1^ENGLISH\]
- VADEMO(14,1) – The number of entries found in the SEXUAL ORIENTATION multiple (e.g., 2).
- VADEMO(14,1,1..n) – The *n*<sup>th</sup> repetition of SEXUAL ORIENTATION for the patient in external^internal format (e.g., "Bisexual^BIS").
- VADEMO (14,1,1..n,1) – The current STATUS of the Sexual Orientation for the patient in external^internal format (e.g., "Active^A").
- VADEMO (14,1,1..n,2) – The DATE CREATED value of the Sexual Orientation for the patient in external^internal format (e.g., "JAN 24, 2022^3220124").
- VADEMO (14,1,1..n,3) – The DATE LAST UPDATED value of the Sexual Orientation for the patient in external^internal format (e.g., "JAN 24, 2022^3220124").
- VADEMO (14,1,1..n,4) – The Internal Entry Number (IEN) of the NOTE \[DOCUMENT TYPE in TUI DOCUMENT File (#8925)\] value of the Sexual Orientation for the patient in external^internal format (e.g., "CLINICAL WARNING^20").
- VADEMO(14,2) – The SEXUAL ORIENTATION DESCRIPTION for the patient free text format (e.g., "I have many sexual orientations").
- VADEMO(14,3) – The number of entries found in the PRONOUN multiple (e.g., 2).
- VADEMO(14,3,1..n) – The *n*<sup>th</sup> repetition of PRONOUN for the patient in external^internal format (e.g., "Ze/Zir/Zirs^ZIR").
- VADEMO(14,4) – The PRONOUN DESCRIPTION for the patient free text format (e.g., "I have many pronouns I would like used").
- VADEMO(14,5) – The SELF IDENTIFIED GENDER for the patient in internal^external format (e.g., Other^O")
- VADEMO(15) – Set to null to avoid issues with groups that are only looking for root nodes
- VADEMO(15,1) – The response to INDIAN SELF IDENTIFICATION (#.571) is NULL, “Y” or “N”.
- VADEMO(15,2) – The INDIAN START DATE (#.572) in internal format or NULL.
- VADEMO(15,3) – The INDIAN ATTESTATION DATE (#.573) in internal format or NULL.
- VADEMO(15,4) – The INDIAN END DATE (#.574) in internal format or NULL.
- VAERR—The error flag has one of the following values:
- 0—No errors encountered.
- 1—Error encountered: DFN or ^DPT(DFN,0) is *not* defined.

### ELIG^VADPT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Description

This entry point returns eligibility information for a patient.

Input

- DFN—This required variable is the internal entry number in the PATIENT (#2) file.
- VAHOW—This optional variable can be set to a requested format for the output array. If this variable is *not* defined or does *not* contain one of the following values, the output array is returned with numeric subscripts:
- 1—Return the output array with alpha subscripts; see “CAI^VADPT” section \[e.g., VAEL(1) would be VAEL("EL")\].
- 2—Return the output in the ^UTILITY global with numeric subscripts \[e.g., ^UTILITY("VAEL",\$J,1)\].
- 12—Return the output in the ^UTILITY global with alpha subscripts \[e.g., ^UTILITY("VAEL",\$J,"EL")\].
- VAROOT—This optional variable can be set to a local variable or global name in which to return the output (e.g., VAROOT="DGELG").

Output

- VAEL(1)—The PRIMARY ELIGIBILITY CODE of the patient in internal^external format (e.g., 1^SERVICE CONNECTED 50-100%).
- VAEL(1,#)—An array of other PATIENT ELIGIBILITIES to which the patient is entitled to care, in internal^external format. The \# sign represents the internal entry number of the eligibility in the ELIGIBILITY CODE file (e.g., 13^PRISONER OF WAR).
- VAEL(2)—The PERIOD OF SERVICE of the patient in internal^external format (e.g., 19^WORLD WAR I).
- VAEL(3)—If the SERVICE CONNECTED? field is YES, a "1" is returned in the first piece; otherwise, a "0" is returned. If service connected, the SERVICE CONNECTED PERCENTAGE field is returned in the second piece (e.g., 1^70).
- VAEL(4)—If the VETERAN (Y/N)? field is YES, a "1" is returned; otherwise, a "0" is returned (e.g., 1).
- VAEL(5)—If an INELIGIBLE DATE exists, a "0" is returned indicating the patient is ineligible; otherwise, a "1" is returned (e.g., 0).
- VAEL(5,1)—If ineligible, the INELIGIBLE DATE of the patient in internal^external format (e.g., 2880101^JAN 1,1988).
- VAEL(5,2)—If ineligible, the INELIGIBLE TWX SOURCE in internal^external format (e.g., 2^REGIONAL OFFICE). *Note: Obsolete after patch DG\*5.3\*1081 is installed.*
- VAEL(5,3)—If ineligible, the INELIGIBLE TWX CITY (e.g., ANYSITE1). *Note: Obsolete after patch DG\*5.3\*1081 is installed.*
- VAEL(5,4)—If ineligible, the INELIGIBLE TWX STATE from which the ineligible notification was received in internal^external format (e.g., 36^NEW YORK). *Note: Obsolete after patch DG\*5.3\*1081 is installed.*
- VAEL(5,5)—If ineligible, the INELIGIBLE VARO DECISION (e.g., UNABLE TO VERIFY). *Note: Obsolete after patch DG\*5.3\*1081 is installed.*
- VAEL(5,6)—If ineligible, the INELIGIBLE REASON (e.g., NO DD214).
- VAEL(6)—The TYPE of patient in internal^external format (e.g., 1^SC VETERAN).
- VAEL(7)—The CLAIM NUMBER of the patient (e.g., 123456789).
- VAEL(8)—The current ELIGIBILITY STATUS of the patient in internal^external format (e.g., V^VERIFIED).
- VAEL(9)—The CURRENT MEANS TEST STATUS of the patient CODE^NAME (e.g., A^MEANS TEST EXEMPT).
- VAEL(10)—The CURRENT EXPANDED MH CARE TYPE of the patient CODE^NAME (e.g., OTH-90^EMERGENT MH OTH).
- VAERR—The error flag has one of the following values:
- 0—No errors encountered.
- 1—Error encountered: DFN or ^DPT(DFN,0) is *not* defined.

### MB^VADPT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Description

This entry point returns monetary benefit information for a patient.

Input

- DFN—This required variable is the internal entry number in the PATIENT (#2) file.
- VAHOW—This optional variable can be set to a requested format for the output array. If this variable is not defined or does not contain one of the following values, the output array is returned with numeric subscripts:
- 1—Return the output array with alpha subscripts; see “CAI^VADPT” section \[e.g., VAMB(1) would be VAMB("AA")\].
- 2—Return the output in the ^UTILITY global with numeric subscripts \[e.g., ^UTILITY("VAMB",\$J,1)\].
- 12—Return the output in the ^UTILITY global with alpha subscripts \[e.g., ^UTILITY("VAMB",\$J,"AA")\].
- VAROOT—This optional variable can be set to a local variable or global name in which to return the output (e.g., VAROOT="DGMB").

Output

- VAMB(1)—If the RECEIVING A&A BENEFITS? field is YES, a "1" is returned in the first piece; otherwise, a "0" is returned. If receiving A&A benefits, the TOTAL ANNUAL VA CHECK AMOUNT is returned in the second piece (e.g., 1^1000).
- VAMB(2)—If the RECEIVING HOUSEBOUND BENEFITS? field is YES, a "1" is returned in the first piece; otherwise, a "0" is returned. If receiving housebound benefits, the TOTAL ANNUAL VA CHECK AMOUNT is returned in the second piece (e.g., 1^0).
- VAMB(3)—If the RECEIVING SOCIAL SECURITY field is YES, a "1" is returned in the first piece; otherwise, a "0" is returned. If receiving social security, the AMOUNT OF SOCIAL SECURITY is returned in the second piece (e.g., 0).
- VAMB(4)—If the RECEIVING A VA PENSION? field is YES, a "1" is returned in the first piece; otherwise, a "0" is returned. If receiving a VA pension, the TOTAL ANNUAL VA CHECK AMOUNT is returned in the second piece (e.g., 1^563.23).
- VAMB(5)—If the RECEIVING MILITARY RETIREMENT? field is YES, a "1" is returned in the first piece; otherwise, a "0" is returned. If receiving military retirement, the AMOUNT OF MILITARY RETIRE-MENT is returned in the second piece (e.g., 0).
- VAMB(6)—The RECEIVING SUP. SECURITY (SSI) field is being eliminated. Since v5.2, a "0" is returned for this variable.
- VAMB(7)—If the RECEIVING VA DISABILITY? field is YES, a "1" is returned in the first piece; otherwise, a "0" is returned. If receiving VA disability, the TOTAL ANNUAL VA CHECK AMOUNT is returned in the second piece (e.g., 0).
- VAMB(8)—If the TYPE OF OTHER RETIRE-MENT field is filled in, a "1" is returned in the first piece; otherwise, a "0" is returned. If receiving other retirement, the AMOUNT OF OTHER RETIREMENT is returned in the second piece (e.g., 1^2500.12).
- VAMB(9)—If the GI INSURANCE POLICY? field is YES, a "1" is returned in the first piece; otherwise, a "0" is returned. If receiving GI insurance, the AMOUNT OF GI INSURANCE is returned in the second piece (e.g., 1^100000).
- VAERR—The error flag has one of the following values:
- 0—No errors encountered.
- 1—error encountered: DFN or ^DPT(DFN,0) is *not* defined.

### SVC^VADPT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Description

This entry point returns service information for a patient.

The VADPT API was updated to exclude any Future Discharge Date (FDD) record. The line tags for this API are:

- SVC^VADPT
- 7^VADPT
- 8^VADPT

The ICR for VADPT is 10061. More details can be found in FORUM, in the documentation of ICR 10061.

Input

- DFN—This required variable is the internal entry number in the PATIENT (#2) file.
- VAHOW—This optional variable can be set to a requested format for the output array. If this variable is *not* defined or does *not* contain one of the following values, the output array is returned with numeric subscripts:
- 1—Return the output array with alpha subscripts; see “CAI^VADPT” section \[e.g., VASV(1) would be VASV("VN")\].
- 2—Return the output in the ^UTILITY global with numeric subscripts \[e.g., ^UTILITY("VASV",\$J,1)\].
- 12—Return the output in the ^UTILITY global with alpha subscripts \[e.g., ^UTILITY("VASV",\$J,"VN")\].
- VAROOT—This optional variable can be set to a local variable or global name in which to return the output (e.g., VAROOT="DGSVC").

Output

- VASV(1)—If the VIETNAM SERVICE INDICATED field is YES, a "1" is returned; otherwise, a "0" is returned (e.g., 0).
- VASV(1,1)—If Vietnam Service, the VIETNAM FROM DATE in internal^external format (e.g., 2680110^JAN 10,1968).
- VASV(1,2)—If Vietnam Service, the VIETNAM TO DATE in internal^external format (e.g., 2690315^MAR 15,1969).
- VASV(2)—If the AGENT ORANGE EXPOS. INDICATED field is YES, a "1" is returned; otherwise, a "0" is returned (e.g., 0).
- VASV(2,1)—If Agent Orange exposure, the AGENT ORANGE REGISTRATION DATE in internal^external format (e.g., 2870513^MAY 13,1987).
- VASV(2,2)—If Agent Orange exposure, the AGENT ORANGE EXAMINATION DATE in internal^external format (e.g., 2871101^NOV 1,1987).
- VASV(2,3)—If Agent Orange exposure, AGENT ORANGE REPORTED TO C.O. date in internal^external format (e.g., 2871225^DEC 25,1987).
- VASV(2,4)—If Agent Orange exposure, AGENT ORANGE REGISTRATION \# (e.g., 123456).
- VASV(2,5)—If Agent Orange exposure, the AGENT ORANGE EXPOSURE LOCATION in internal^external format (e.g., V^VIETNAM).
- VASV(3)—If the RADIATION EXPOSURE INDICATED field is YES, a "1" is returned; otherwise, a "0" is returned (e.g., 0).
- VASV(3,1)—If Radiation Exposure, RADIATION REGISTRATION DATE in internal^external format (e.g., 2800202^FEB 02,1980).
- VASV(3,2)—If Radiation Exposure, RADIATION EXPOSURE METHOD in internal^external format (e.g., T^NUCLEAR TESTING).
- VASV(4)—If the POW STATUS INDICATED field is YES, a "1" is returned; otherwise, a "0" is returned (e.g., 0).
- VASV(4,1)—If POW status, POW FROM DATE in internal^external format (e.g., 2450319^MAR 19,1945).
- VASV(4,2)—If POW status, POW TO DATE in internal^external format (e.g., 2470101^JAN 1,1947).
- VASV(4,3)—If POW status, POW CONFINEMENT LOCATION in internal^external format (e.g., 2^WORLD WAR II - EUROPE).
- VASV(5)—If the COMBAT SERVICE INDICATED field is YES, a "1" is returned; otherwise, a "0" is returned (e.g., 0).
- VASV(5,1)—If combat service, COMBAT FROM DATE in internal^external format (e.g., 2430101^JAN 1,1943).
- VASV(5,2)—If combat service, COMBAT TO DATE in internal^external format (e.g., 2470101^JAN 1,1947).
- VASV(5,3)—If combat service, COMBAT SERVICE LOCATION in internal^external format (e.g., 2^WORLD WAR II - EUROPE).
- VASV(6)—If a SERVICE BRANCH \[LAST\] field is indicated, a "1" is returned in the first piece; otherwise, a "0" is returned (e.g., 0).
- VASV(6,1)—If service branch, BRANCH OF SERVICE field in internal^external format (e.g., 3^AIR FORCE).
- VASV(6,2)—If service branch, SERVICE NUMBER field in internal^external format (e.g., 123456789).
- VASV(6,3)—If service branch, SERVICE DISCHARGE TYPE in internal^external format (e.g., 1^HONORABLE).
- VASV(6,4)—If service branch, SERVICE ENTRY DATE in internal^external format (e.g., 2440609^JUN 9,1944).
- VASV(6,5)—If service branch, SERVICE SEPARATION DATE in internal^external format (e.g., 2480101^JAN 1,1948).
- VASV(6,6)—If service branch, SERVICE COMPONENT in internal code^external format (e.g., R^REGULAR).
- VASV(7)—If a SERVICE SECOND EPISODE field is indicated, a "1" is returned; otherwise, a "0" is returned (e.g., 0).
- VASV(7,1)—If second episode, BRANCH OF SERVICE field in internal^external format (e.g., 3^AIR FORCE).
- VASV(7,2)—If second episode, SERVICE NUMBER field in internal^external format (e.g., 123456789).
- VASV(7,3)—If second episode, SERVICE DISCHARGE TYPE in internal^external format (e.g., 1^HONORABLE).
- VASV(7,4)—If second episode, SERVICE ENTRY DATE in internal^external format (e.g., 2440609^JUN 9,1944).
- VASV(7,5)—If second episode, SERVICE SEPARATION DATE in internal^external format (e.g., 2480101^JAN 1,1948).
- VASV(7,6)—If second episode, SERVICE COMPONENT in internal^external format (e.g., R^REGULAR).
- VASV(8)—If a SERVICE THIRD EPISODE field is indicated, a "1" is returned; otherwise, a "0" is returned (e.g., 0).
- VASV(8,1)—If third episode, BRANCH OF SERVICE field in internal^external format (e.g., 3^AIR FORCE).
- VASV(8,2)—If third episode, SERVICE NUMBER field in internal^external format (e.g., 123456789).
- VASV(8,3)—If third episode, SERVICE DIS-CHARGE TYPE in internal^external format (e.g., 1^HONORABLE).
- VASV(8,4)—If third episode, SERVICE ENTRY DATE in internal^external format (e.g., 2440609^JUN 9,1944).
- VASV(8,5)—If third episode, SERVICE SEPARATION DATE in internal^external format (e.g., 2480101^JAN 1,1948).
- VASV(8,6)—If third episode, SERVICE COMPONENT in internal code^external format.(e.g., R^REGULAR).
- VASV(9)—If the CURRENT PH INDICATOR field is YES, a “1” is returned; otherwise, a “0” is returned (e.g., 0).
- VASV(9,1)—If the CURRENT PH INDICATOR field is YES, CURRENT PURPLE HEART STATUS in internal^external format.(e.g., 2^IN PROCESS).
- VASV(9,2)—If the CURRENT PH INDICATOR field is NO, CURRENT PURPLE HEART REMARKS in internal^external format (e.g., 5^VAMC).
- VASV(10)—Is either 1 or 0, 1 if there is a value for Combat Vet End Date, 0 if not.
- VASV(10,1)—Internal Combat Vet End Date ^external Combat Vet End Date (e.g., 3060101^JAN 1, 2006).
- VASV(11)—The number of OIF conflict entries found for the Veteran in the SERVICE \[OEF OR OIF\] (#2.3215) SUB-FILE \[n = 1—Total number of OIF conflict entries\].
- VASV(11,n,1)—SERVICE LOCATION (#2.3215; .01) internal code=1^external (e.g., 1^OIF). Where “*n*” is the number used to provide a unique number for each OIF or a conflict being returned.
- VASV(11,n,2)—OEF/OIF FROM DATE (#2.3215; .02) internal format ^external format (e.g., 3060101^JAN 1, 2006). Where “*n*” is the number used to provide a unique number for each OIF conflict being returned.
- VASV(11,n,3)—OEF/OIF TO DATE (#2.3215; .03) internal format ^external format (e.g., 3060101^MAR 1, 2006). Where “*n*” is the number used to provide a unique number for each OIF conflict being returned.
- VASV(12)—The number of OEF conflict entries found for the Veteran in the SERVICE \[OEF OR OIF\] \#2.3215 SUB-FILE. \[n = 1—VASV(12)\].
- VASV(12,n,1)—SERVICE LOCATION (#2.3215; .01) internal code = 2 ^external (e.g., 2^OEF). Where “*n*” is the number used to provide a unique number for each OEF conflict being returned.
- VASV(12,n,2)—OEF/OIF FROM DATE (#2.3215; .02) internal format ^external format (e.g., 3060101^JAN 1, 2006). Where “*n*” is the number used to provide a unique number for each OEF conflict being returned.
- VASV(12,n,3)—OEF/OIF TO DATE (#2.3215; .03) internal format ^external format (e.g., 3060101^MAR 1, 2006). Where “*n*” is the number used to provide a unique number for each OEF conflict being returned.
- VASV(13)—The number of UNKNOWN OEF/OIF conflict entries found for the Veteran in the SEVICE \[OEF OR OIF\] \#2.3215 SUB-FILE. \[n = 1—VASV(13)\].
- VASV(13,n,1)—SERVICE LOCATION (#2.3215; .01) internal CODE = 3^external format (e.g., 3^UNKNOWN OEF/OIF). Where “*n*” is the number used to provide a unique number for each UNKNOWN OEF/OIF conflict being returned.
- VASV(13,n,2)—OEF/OIF FROM DATE (#2.3215; .02) internal format ^external format (e.g., 3060101^JAN 1, 2006). Where “*n*” is the number used to provide a unique number for each UNKNOWN OEF/OIF conflict being returned.
- VASV(13,n,3)—OEF/OIF TO DATE (#2.3215; .03) internal format ^external format (e.g., 3060101^MAR 1, 2006). Where “*n*” is the number used to provide a unique number for each UNKNOWN OEF/OIF conflict being returned.
- VASV(14)—If the PROJ 112/ SHAD field is populated, a "1" is returned; otherwise, a "0" is returned (e.g., 0).
- VASV(14,1)—If the PROJ 112/SHAD field is populated, PROJ 112/SHAD in internal^external format (e.g., 1^YES).
- VASV(15)—If TOXIC EXPOSURE RISK ACTIVITY (#.32116) field of the PATIENT file \#2) is populated, TOXIC EXPOSURE RISK ACTIVITY is stored in internal^external format (e.g., 1^YES, 0^NO). If TOXIC EXPOSURE RISK ACTIVITY (#.32116) field of the PATIENT file \#2) is NULL, the word UNKNOWN is stored in the second piece (e.g., ^UNKNOWN).
- VASV(16)— If the PERSIAN GULF INDICATOR field is populated, the stored value will be rturned in internal^external format (e.g., 1^YES is returned for YES; a 0^NO is returned for NO; otherwise ^UNKNOWN is returned for UNKNOWN).
- VASV(17) — The date and time of the last change made to the PERSIAN GULF INDICATOR is stored internally in FileMan date-time format and will be returned in internal^external format (e.g: 3240716.083303^JUN 29,2023@12:52:41).
- VAERR—The error flag has one of the following values:
- 0—No errors encountered.
- 1—Error encountered: DFN or ^DPT(DFN,0) is *not* defined.

### ADD^VADPT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Description

This entry point returns address data for a patient. If a temporary address is in effect, the data returned is that pertaining to that temporary address; otherwise, the patient mailing address information is returned.

Input

- DFN—This required variable is the internal entry number in the PATIENT (#2) file.
- VAHOW—This optional variable can be set to a requested format for the output array. If this variable is not defined or does not contain one of the following values, the output array is returned with numeric subscripts:
- 1—Return the output array with alpha subscripts; see “CAI^VADPT” section \[e.g., VAPA(1) would be VAPA("L1")\].
- 2—Return the output in the ^UTILITY global with numeric subscripts \[e.g., ^UTILITY(“VAPA”, \$J,1)\].
- 12—Return the output in the ^UTILITY global with alpha subscripts \[e.g., ^UTILITY("VAPA",\$J,"L1")\].
- VAROOT—This optional variable can be set to a local variable or global name in which to return the output (e.g., VAROOT="DGADD").
- VAPA("P")—This optional variable can be set to force the return of the patient's mailing address. The mailing address array is returned regardless of whether or not a temporary address is in effect \[e.g., VAPA("P")=""\].
- VAPA("CD")—This is an optional input parameter set to an effective date in VA File Manager format to manipulate the active/inactive status returned in the VAPA(12) node. The indicator reflects the active status as of the date specified or the current date if VAPA("CD") is undefined.
- VATEST("ADD",9)—This optional variable can be defined to a beginning date in VA FileMan format. If the entire range specified is not within the effective time window of the temporary address start and stop dates, the patient's regular address is returned \[e.g., VATEST("ADD",9)=2920101\].
- VATEST("ADD",10)—This optional variable can be defined to a ending date in VA FileMan format. If the entire range specified is not within the effective time window of the temporary address start and stop dates, the patient's regular address is returned \[e.g., VATEST("ADD",10)=2920301\].

Output

- VAPA(1)—The first line of the STREET ADDRESS (e.g., 123 South Main Street).
- VAPA(2)—The second line of the STREET ADDRESS (e.g., Apartment \#1245).
- VAPA(3)—The third line of the STREET ADDRESS (e.g., P.O. Box 1234).
- VAPA(4)—The CITY corresponding to the street address previously indicated (e.g., ANYSITE1).
- VAPA(5)—The STATE corresponding to the city previously indicated in internal^external format (e.g., 6^CALIFORNIA).
- VAPA(6)—The ZIP CODE of the city previously indicated (e.g., 12345).
- VAPA(7)—The COUNTY in which the patient is residing in internal^external format (e.g., 1^ALAMEDA).
- VAPA(8)—The PHONE NUMBER of the location in which the patient is currently residing \[e.g., (123) 456-7890\].
- VAPA(9)—If the address information provided pertains to a temporary address, the TEMPORARY ADDRESS START DATE in internal^external format (e.g., 2880515^MAY 15,1988).
- VAPA(10)—If the address information provided pertains to a temporary address, the TEMPORARY ADDRESS END DATE in internal^external format (e.g., 2880515^MAY 15,1988).
- VAPA(11)—The ZIP+4 (5 or 9-digit zip code) of the city previously indicated in internal^external format (e.g., 123454444^12345-4444).
- VAPA(12)—Confidential Address Active indicator:
- O—Inactive
- 1—Active).
- VAPA(13)—The first line of the Confidential Street Address.
- VAPA(14)—The second line of the Confidential Street Address.
- VAPA(15)—The third line of the Confidential Street Address.
- VAPA(16)—The city for the Confidential Address.
- VAPA(17)—The state for the Confidential Address in internal^external format (e.g., 36^NEW YORK).
- VAPA(18)—The 5-digit or 9-digit Zip Code for the Confidential Address in internal^external format (e.g., 12208^12208 or 122081234^12208-1234).
- VAPA(19)—The county for the Confidential Address in internal^external format (e.g., 1^ANYSITE1).
- VAPA(20)—The start date for the Confidential Address in internal^external format (e.g., 3030324^MAR 24,2003).
- VAPA(21)—The end date for the Confidential Address in internal^external format (e.g., 3030624^JUN 24,2003).
- VAPA(22,N)—The Confidential Address Categories in internal^external format^status (n=internal value) \[e.g., VAPA(22,4)=4^MEDICAL RECORDS^Y\].
- VAPA(23)—The Mailing or Temporary Province (if temp address is current and active, it’s temp).
- VAPA(24)—The Mailing or Temporary Postal Code (if temp address is current and active, it's temp).
- VAPA(25)—The Mailing or Temporary Country (if temp address is current and active, it's temp).
- VAPA(26)—The Confidential Province.
- VAPA(27)—The Confidential Postal Code.
- VAPA(28)—The Confidential Country.
- VAPA(29)—The Confidential Phone Number.
- VAPA(30)—Residential Address Line 1.
- VAPA(31)—Residential Address Line 2.
- VAPA(32)—Residential Address Line 3.
- VAPA(33)—Residential Address City.
- VAPA(34)—Residential Address State (e.g., 6^CALIFORNIA).
- VAPA(35)—Residential Address ZIP.
- VAPA(36)—Residential Address County (e.g., 6^WORCHESTER).
- VAPA(37)—Residential Address Country (e.g., 6^UNITED STATES).
- VAPA(38)—Residential Address Province.
- VAPA(39)—Residential Address Postal Code.
- VAERR—The error flag has one of the following values:
- 0—No errors encountered.
- 1—Error encountered: DFN or ^DPT(DFN,0) is *not* defined.

### OAD^VADPT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Description

This entry point returns other specific address information.

Input

- DFN—This required variable is the internal entry number in the PATIENT (#2) file.
- VAHOW—This optional variable can be set to a requested format for the output array. If this variable is *not* defined or does *not* contain one of the following values, the output array is returned with numeric subscripts:
- 1—Return the output array with alpha subscripts; see “CAI^VADPT” section \[e.g., VAOA(1) would be VAOA("L1")\].
- 2—Return the output in the ^UTILITY global with numeric subscripts \[e.g., ^UTILITY("VAOA",\$J,1)\].
- 12—Return the output in the ^UTILITY global with alpha subscripts \[e.g., ^UTILITY("VAOA,\$J,"L1"\].
- VAROOT—This optional variable can be set to a local variable or global name in which to return the output (e.g., VAROOT="DGOA").
- VAOA("A")—This optional variable may be passed to indicate which specific address the programmer wants returned. If it is *not* defined, the PRIMARY NEXT-OF-KIN is returned; otherwise, the following are returned based on information desired:
- VAOA("A")=1—Primary emergency contact.
- VAOA("A")=2—Designee for personal effects.
- VAOA("A")=3—Secondary next-of-kin.
- VAOA("A")=4—Secondary emergency contact.
- VAOA("A")=5—Patient employer.
- VAOA("A")=6—Spouse's employer.

Output

- VAOA(1)—The first line of the STREET ADDRESS (e.g., 123 South First Street).
- VAOA(2)—The second line of the STREET ADDRESS (e.g., Apartment 9D).
- VAOA(3)—The third line of the STREET ADDRESS (e.g., P.O. Box 1234).
- VAOA(4)—The CITY in which the contact/employer resides (e.g., NEWINGTON).
- VAOA(5)—The STATE in which the contact/employer resides in internal^external format (e.g., 6^CALIFORNIA).
- VAOA(6)—The ZIP CODE of the location in which the contact/employer resides (e.g., 12345).
- VAOA(7)—The COUNTY in which the contact/employer resides in internal^external format (e.g., 1^ALAMEDA).
- VAOA(8)—The PHONE NUMBER of the contact/employer \[e.g., (000) 555-1234\].
- VAOA(9)—The NAME of the contact or, in case of employment, the employer to whom this address information applies (e.g., SMITH,ROBERT P).
- VAOA(10)— The RELATIONSHIP TYPE of the emergency contact to the patient. One of the following responses:
1.  BROTHER
2.  CHILD-IN-LAW
3.  DAUGHTER
4.  EXTENDED FAMILY MEMBER
5.  FATHER
6.  GRANDCHILD
7.  HUSBAND
8.  MOTHER
9.  NIECE/NEPHEW
10. SISTER
11. SON
12. STEPCHILD
13. UNRELATED FRIEND/OTHER
14. WARD
15. WIFE

> Note: For employer data this node is NULL

- VAOA(11)—The ZIP+4 (5 or 9 digit zip code) of the location in which the contact/employer resides in internal^external format \[e.g., 123454444^12345-4444\].
- VAOA(12)—The RELATIONSHIP TO PATIENT field of the contact (if applicable) (e.g., FATHER-Deaf-text only). NOTE: This node is not created for employer data.
- VAERR—The error flag has one of the following values:
- 0—No errors encountered.
- 1—Error encountered: DFN or ^DPT(DFN,0) is *not* defined.

### INP^VADPT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Description

This entry point returns data related to an inpatient episode.

Input

- DFN—This required variable is the internal entry number in the PATIENT (#2) file.
- VAHOW—This optional variable can be set to a requested format for the output array. If this variable is *not* defined or does *not* contain one of the following values, the output array is returned with numeric subscripts:
- 1—Return the output array with alpha subscripts; see “CAI^VADPT” section \[e.g., VAIN(1) would be VAIN("AN")\].
- 2—Return the output in the ^UTILITY global with numeric subscripts \[e.g., ^UTILITY("VAIN",\$J,1)\].
- 12—Return the output in the ^UTILITY global with alpha subscripts \[e.g., ^UTILITY("VAIN,\$J,"AN"\].
- VAROOT—This optional variable can be set to a local variable or global name in which to return the output (e.g., VAROOT="DGIN").
- VAINDT—This optional variable may be set to a past date/time for which the programmer wishes to know the patient's inpatient status. This *must* be passed as an internal VA FileMan date/time format. If time is *not* passed, it assumes anytime during that day. If this variable is *not* defined, it assumes now as the date/time (e.g., 2880101.08).

Output

- VAIN(1)—The INTERNAL NUMBER \[IFN\] of the admission if one was found for the date/time requested. If no inpatient episode was found for the date/time passed, then all variables in the VAIN array are returned as NULL (e.g., 123044).
- VAIN(2)—The PRIMARY CARE PHYSICIAN \[PROVIDER\] assigned to the patient at the date/time requested in internal^external format (e.g., 3^ADTPROVIDER,ONE L).
- VAIN(3)—The TREATING SPECIALTY assigned to the patient at the date/time requested in internal^external format (e.g., 19^GERIATRICS).
- VAIN(4)—The WARD LOCATION to which the patient was assigned at the date/time requested in internal^external format (e.g., 27^IBSICU).
- VAIN(5)—The ROOM-BED to which the patient was assigned at the date/time requested in external format (e.g., 123-B).
- VAIN(6)—This returns a "1" in the first piece if the patient is in a bed status; otherwise, a "0" is returned. A *non*-bed status is made based on the last transfer type to a *non*-bed status, (i.e., authorized absence, unauthorized absence, etc.). The second piece contains the name of the last transfer type should one exist (e.g., 1^FROM AUTHORIZED ABSENCE).
- VAIN(7)—The ADMISSION DATE/TIME for the patient in internal^external format (e.g., 2870213.0915^FEB 13,1987@09:15).
- VAIN(8)—The ADMISSION TYPE for the patient in internal^external format (e.g., 3^DIRECT).
- VAIN(9)—The ADMITTING DIAGNOSIS for the patient (e.g., PSYCHOSIS).
- VAIN(10)—The internal entry number of the PTF record corresponding to this admission (e.g., 2032).
- VAIN(11)—The ATTENDING PHYSICIAN in internal^external format (e.g., 25^ADTPROVIDER,ONE).
- VAERR—The error flag has one of the following values:
- 0—No errors encountered.
- 1—Error encountered: DFN or ^DPT(DFN,0) is *not* defined.

### IN5^VADPT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Description

This entry point returns data related to an inpatient episode.

Input

- DFN—This required variable is the internal entry number in the PATIENT (#2) file.
- VAHOW—This optional variable can be set to a requested format for the output array. If this variable is *not* defined or does *not* contain one of the following values, the output array is returned with numeric subscripts:
- 1—Return the output array with alpha subscripts; see “CAI^VADPT” section \[e.g., VAIP(1) would be VAIP("MN")\].
- 2—Return the output in the ^UTILITY global with numeric subscripts \[e.g., ^UTILITY("VAIP",\$J,1)\].
- 12—Return the output in the ^UTILITY global with alpha subscripts \[e.g., ^UTILITY("VAIP,\$J,"MN"\].
- VAROOT—This optional variable can be set to a local variable or global name in which to return the output (e.g., VAROOT="DGI5").
- VAIP("D")—This optional variable can be defined as follows:
- VAIP("D") = VA FileMan date in internal format. If the patient was an inpatient at the date/time passed, movement data pertaining to that date/time is returned.
- VAIP("D") = "LAST" Movement data pertaining to the last movement on file, regardless if patient is a current inpatient.
- VAIP("D") = Valid date without time returns movement data if patient was an inpatient at any time during the day on the date that was passed.
- VAIP("D")—If *not* passed, returns movement data if the patient was in inpatient based on "NOW".
- VAIP("L")—This optional variable, when passed, will include lodgers movements in the data \[e.g., VAIP("L")=""\].
- VAIP("V")—Can be defined as the variable used instead of VAIP \[e.g., VAIP("V")="SD"\].
- VAIP("E")—This optional variable is defined as the internal file number of a specific movement. If this is defined, VAIP("D") is ignored \[e.g., VAIP("E")=123445\].
- VAIP("M")—This optional variable can be passed as a "1" or a "0" (or NULL):
- VAIP("M")=0—The array returned is based on the *admission* movement associated with the movement date/time passed.
- VAIP("M")=1—The array returned is based on the *last* movement associated with the date/time passed.

Output

- VAIP(1)—The INTERNAL FILE NUMBER \[IFN\] of the movement found for the specified date/time (e.g., 231009).
- VAIP(2)—The TRANSACTION TYPE of the movement in internal^external format; where:
- 1 = Admission
- 2 = Transfer
- 3 = Discharge
- 4 = Check-in lodger
- 5 = Check-out lodger
- 6 = Specialty transfer

(e.g., 3^DISCHARGE)

- VAIP(3)—The MOVEMENT DATE/TIME in internal^external date format (e.g., 2880305.09^MAR 5,1988@09:00).
- VAIP(4)—The TYPE OF MOVEMENT in internal^external format (e.g., 4^INTERWARD TRANSFER).
- VAIP(5)—The WARD LOCATION to which patient was assigned with that movement in internal^external format (e.g., 32^1B-SURG).
- VAIP(6)—The ROOM-BED to which the patient was assigned with that movement in internal^external format (e.g., 88^201-01).
- VAIP(7)—The PRIMARY CARE PHYSICIAN assigned to the patient in internal^external format (e.g., 3^ADTPROVIDER,TEN).
- VAIP(8)—The TREATING SPECIALTY assigned with that movement in internal^external format (e.g., 98^OPTOMETRY).
- VAIP(9)—The DIAGNOSIS assigned with that movement (e.g., UPPER GI BLEEDING).
- VAIP(10)—This returns a "1" in the first piece if the patient is in a bed status; otherwise, a "0" is returned. A *non*-bed status is made based on the last transfer type, if one exists, and a transfer to a *non*-bed status (i.e., authorized absence, unauthorized absence, etc.). The second piece contains the name of the last transfer type should one exist (e.g., 1^FROM AUTHORIZED ABSENCE).
- VAIP(11)—If patient is in an absence status on the movement date/time, this returns the EXPECTED RETURN DATE from absence in internal^external format (e.g., 2880911^SEP 11,1988).
- VAIP(12)—The internal entry number of the PTF record corresponding to this admission (e.g., 2032).
- VAIP(13)—The INTERNAL FILE NUMBER of the admission associated with this movement (e.g., 200312).
- VAIP(13,1)—The MOVEMENT DATE/TIME in internal^external format (e.g., 2881116.08^NOV 16,1988@08:00).
- VAIP(13,2)—The TRANSACTION TYPE in internal^external format (e.g., 1^ADMISSION).
- VAIP(13,3)—The MOVEMENT TYPE in internal^external format (e.g., 15^DIRECT).
- VAIP(13,4)—The WARD LOCATION associated with this patient with this movement in internal^external format (e.g., 5^7BSCI).
- VAIP(13,5)—The PRIMARY CARE PHYSICIAN assigned to the patient for this movement in internal^external format (e.g., 16^ADTPROVIDER, ONE C).
- VAIP(13,6)—The TREATING SPECIALTY for the patient for this movement in internal^external format (e.g., 3^NEUROLOGY).
- VAIP(14)—The INTERNAL FILE NUMBER of the last movement associated with this movement (e.g., 187612).
- VAIP(14,1)—The MOVEMENT DATE/TIME in internal^external format (e.g., 2881116.08^NOV 16,1988@08:00).
- VAIP(14,2)—The TRANSACTION TYPE in internal^external format (e.g., 2^TRANSFER).
- VAIP(14,3)—The MOVEMENT TYPE in internal^external format (e.g., 4^INTERWARD TRANSFER).
- VAIP(14,4)—The WARD LOCATION associated with this patient with this movement in internal^external format (e.g., 5^7BSCI).
- VAIP(14,5)—The PRIMARY CARE PHYSICIAN assigned to the patient for this movement in internal^external format (e.g., 16^ADTPROVIDER, ONE C).
- VAIP(14,6)—The TREATING SPECIALTY for the patient for this movement in internal^external format (e.g., 3^NEUROLOGY).
- VAIP(15)—The INTERNAL FILE NUMBER of the movement which occurred immediately prior to this one, if one exists (e.g., 153201).
- VAIP(15,1)—The MOVEMENT DATE/TIME in internal^external format (e.g., 2881116.08^NOV 16,1988@08:00).
- VAIP(15,2)—The TRANSACTION TYPE in internal^external format (e.g., 2^TRANSFER).
- VAIP(15,3)—The MOVEMENT TYPE in internal^external format (e.g., 4^INTERWARD TRANSFER).
- VAIP(15,4)—The WARD LOCATION associated with this patient with this movement in internal^external format (e.g., 5^7BSCI).
- VAIP(15,5)—The PRIMARY CARE PHYSICIAN assigned to the patient for this movement in internal^external format (e.g., 16^ADTPROVIDER,TWO).
- VAIP(15,6)—The TREATING SPECIALTY for the patient for this movement in internal^external format (e.g., 3^NEUROLOGY).
- VAIP(16)—The INTERNAL FILE NUMBER of the movement which occurred immediately following this one, if one exists (e.g., 146609).
- VAIP(16,1)—The MOVEMENT DATE/TIME in internal^external format (e.g., 2881116.08^NOV 16,1988@08:00).
- VAIP(16,2)—The TRANSACTION TYPE in internal^external format (e.g., 2^TRANSFER).
- VAIP(16,3)—The MOVEMENT TYPE in internal^external format (e.g., 4^INTERWARD TRANSFER).
- VAIP(16,4)—The WARD LOCATION associated with this patient with this movement in internal^external format (e.g., 5^7BSCI).
- VAIP(16,5)—The PRIMARY CARE PHYSICIAN assigned to the patient for this movement in internal^external format (e.g., 16^ADTPROVIDER,THREE).
- VAIP(16,6)—The TREATING SPECIALTY for the patient for this movement in internal^external format (e.g., 3^NEUROLOGY).
- VAIP(17)—The INTERNAL FILE NUMBER of the discharge associated with this movement (e.g., 1902212).
- VAIP(17,1)—The MOVEMENT DATE/TIME in internal^external format (e.g., 2881116.08^NOV 16,1988@08:00).
- VAIP(17,2)—The TRANSACTION TYPE in internal^external format (e.g., 3^DISCHARGE).
- VAIP(17,3)—The MOVEMENT TYPE in internal^external format (e.g., 16^REGULAR).
- VAIP(17,4)—The WARD LOCATION associated with this patient for this movement in internal^external format (e.g., 5^7BSCI).
- VAIP(17,5)—The PRIMARY CARE PHYSICIAN assigned to the patient for this movement in internal^external format (e.g., 16^ADTPROVIDER,ONE).
- VAIP(17,6)—The TREATING SPECIALTY for the patient for this movement in internal^external format (e.g., 3^NEUROLOGY).
- VAIP(18)—The ATTENDING PHYSICIAN assigned to the patient for this movement in internal^external format (e.g., 25^ADTPROVIDER,TEN).
- VAIP(19,1)—It contains whether or not the patient chose to be excluded from the facility directory for the admission related to this movement in internal^external format (e.g., 1^YES).
- VAIP(19,2)—Date/time answer to facility directory question was answered in internal^external format (e.g., 3030426.08^APR26,2003@08:00).
- VAIP(19,3)—User entering answer to facility directory question in internal^external format (e.g., 1934^ADTEMPLOYEE,ONE).
- VAERR—The error flag has one of the following values:
- 0—No errors encountered.
- 1—Error encountered: DFN or ^DPT(DFN,0) is *not* defined.

### OPD^VADPT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Description

Returns other pertinent patient data which is commonly used but not contained in any other calls to VADPT.

Input

- DFN—This required variable is the internal entry number in the PATIENT (#2) file.
- VAHOW—This optional variable can be set to a requested format for the output array. If this variable is *not* defined or does *not* contain one of the following values, the output array is returned with numeric subscripts:
- 1—Return the output array with alpha subscripts; see “CAI^VADPT” section \[e.g., VAPD(1) would be VAPD("BC")\].
- 2—Return the output in the ^UTILITY global with numeric subscripts \[e.g., ^UTILITY("VAPD",\$J,1)\].
- 12—Return the output in the ^UTILITY global with alpha subscripts \[e.g., ^UTILITY("VAPD",\$J,"BC"\].
- VAROOT—This optional variable can be set to a local variable or global name in which to return the output (e.g., VAROOT="DGPD").

Output

- VAPD(1)—The PLACE OF BIRTH \[CITY\] (e.g., SAN FRANCISCO).
- VAPD(2)—The PLACE OF BIRTH \[STATE\] in internal^external format (e.g., 6^CALIFORNIA).
- VAPD(3)—The FATHER'S NAME (e.g., ADTFATHER,ONE).
- VAPD(4)—The MOTHER'S NAME (e.g., MARY).
- VAPD(5)—The MOTHER'S MAIDEN NAME (e.g., ADTMOTHER,ONE).
- VAPD(6)—The patient's OCCUPATION.(e.g., CARPENTER)
- VAPD(7)—The patient's EMPLOYMENT STATUS in internal^external format (e.g., 4^SELF EMPLOYED).
- VAPD(8)—The patient's Phone Number (work).
- VAERR—The error flag has one of the following values:
- 0—No errors encountered.
- 1—Error encountered - DFN or ^DPT(DFN,0) is *not* defined.

### REG^VADPT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Description

Returns REGISTRATION/DISPOSITION data.

Input

- DFN—This required variable is the internal entry number in the PATIENT (#2) file.
- VAROOT—This optional variable can be set to a local variable or global name in which to return the output (e.g., VAROOT="DGADD").
- VARP("F")—Can be defined as the "from" date for which registrations are desired. This *must* be passed as a valid VA FileMan date (e.g., VARP("F")=2930101).
- VARP("T")—Can be defined as the "to" date for which registrations are desired. This *must* be passed as a valid VA FileMan date. If neither VARP("F") nor VARP("T") are defined, all registrations are returned (e.g., VARP("T")=2930530).
- VARP("C")—Can be defined as the number of registrations you want returned in the array (e.g., VARP("C")=5 returns the five most recent).

Output

- ^UTILITY("VARP",\$J,#,"I")—Internal format.
- ^UTILITY("VARP",\$J,#,"E")—External format:
- Piece 1—Registration Date/Time
- Piece 2—Status
- Piece 3—Type of Benefit applied for
- Piece 4—Facility Applying to
- Piece 5—Who Registered
- Piece 6—Log out (disposition) date/time
- Piece 7—Disposition Type
- Piece 8—Who Dispositioned

VAERR—The error flag has one of the following values:

- 0—No errors encountered.
- 1—Error encountered: DFN or ^DPT(DFN,0) is *not* defined.

### SDE^VADPT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Description

Returns ACTIVE clinic enrollments for a patient.

Input

DFN—This required variable is the internal entry number in the PATIENT (#2) file.

Output

- ^UTILITY("VAEN",\$J,#,"I")—Internal format.
- ^UTILITY("VAEN",\$J,#,"E")—External format:
- Piece 1—Clinic Enrolled in
- Piece 2—Enrollment Date
- Piece 3—OPT or AC

VAERR—The error flag has one of the following values:

- 0—No errors encountered.
- 1—Error encountered: DFN or ^DPT(DFN,0) is *not* defined.

### SDA^VADPT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Description

Returns APPOINTMENT DATE/TIME data for a patient.

Input

- DFN—This required variable is the internal entry number in the PATIENT (#2) file.
- VASD("T")—Can be defined as the "to" date for which registrations are desired. This *must* be passed as a valid VA FileMan date. If neither VASD("F") nor VASD("T") are defined, all future appointments are returned.
- VASD("F")—Can be defined as the "from" date for which appointments are desired. This *must* be passed as a valid VA FileMan date. If *not* defined, it is assumed only future appointments should be returned.
- VASD("W")—Can be passed as the specific STATUS desired in the following format. If *not* passed, only those appointments that are still scheduled (or kept in the event of a past date) for both inpatients and outpatients are returned.

If VASD("W") Contains a value these appointments are returned:

1.  Active/Kept
2.  Inpatient appts. only
3.  No-shows
4.  No-shows, auto-rebook
5.  Cancelled by Clinic
6.  Cancelled by Clinic, auto rebook
7.  Cancelled by Patient
8.  Cancelled by Patient, auto rebook
9.  No action taken
- VASD("C", Clinic IFN)—Can be set up to contain only those internal file entries from the HOSPITAL LOCATION file for clinics that you would like to see appointments for this particular patient.

You can define this array with just one clinic or with many. If you do *not* define this variable, it is assumed that you want appointments for this patient in all clinics returned.

Output

- ^UTILITY("VASD",\$J,#,"I")—Internal format.
- ^UTILITY("VASD",\$J,#,"E")—External format:
- Piece 1—Date/Time of Appointment
- Piece 2—Clinic
- Piece 3—Status
- Piece 4—Appointment Type
- VAERR—The error flag has one of the following values:
- 0—No errors encountered.
- 1—Error encountered - DFN or ^DPT(DFN,0) is *not* defined.

### PID^VADPT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Description

This call is used to obtain the patient identifier in long and brief format.

Input

- DFN—This required variable is the internal entry number in the PATIENT (#2) file.
- VAPTYP—This optional variable can be set to the internal number of a patient eligibility. The variable can be used to indicate the patient's type, such as VA, DOD, or IHS, through the eligibility. If this variable is *not* defined or the eligibility does *not* exist, the VA patient IDs are returned.

Output

- VA("PID")—The long patient identifier (e.g., 000-22-3333P).
- VA("BID")—The short patient identifier (e.g., 3333P).
- VAERR—The error flag has one of the following values:
- 0—No errors encountered.
- 1—Error encountered: DFN or ^DPT(DFN,0) is *not* defined.

### PID^VADPT6

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This call returns the same variables as the [PID^VADPT](#pidvadpt) call, but eliminates the unnecessary processing time required calling [PID^VADPT](#pidvadpt).

### ADM^VADPT2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Description

This returns the internal file number of the admission movement. If VAINDT is *not* defined, this uses "NOW" for the date/time.

Input

- DFN—This required variable is the internal entry number in the PATIENT (#2) file.
- VAINDT—This optional variable can be set to a past date/time for which the programmer wants to know the patient's inpatient status. This *must* be passed as an internal VA FileMan date/time format (e.g., 2880101.08).

Output

- VADMVT—Returns the internal file number of the admission movement.
- VAERR—The error flag has one of the following values:
- 0—No errors encountered.
- 1—Error encountered: DFN or ^DPT(DFN,0) is *not* defined.

### KVAR^VADPT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This call is used to remove all variables defined by the VADPT routine. The programmer should elect to use this call to remove the arrays that were returned by VADPT.

### KVA^VADPT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This call is used as the [KVAR^VADPT](#kvarvadpt) call and also kills the VA("BID") and VA("PID") variables.

### Combinations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following calls can be made to return a combination of arrays with a single call.

DFN is a required variable that is the internal entry number in the PATIENT (#2) file. See specific call in the Call Combinations table for other variable input.

| Output: | Demographic | Eligibility | Inpatient | Inpatient | Address | Service | Monetary | Registration   | Enrollment     | Appointment    |
|---------|-------------|-------------|-----------|-----------|---------|---------|----------|----------------|----------------|----------------|
| CALL    | VADM        | VAEL        | VAIN      | VAIP      | VAPA    | VASV    | VAMB     | UTILITY("VARP" | UTILITY("VAEN" | UTILITY("VASD" |
| OERR    | X           |             | X         |           |         |         |          |                |                |                |
| 1       | X           |             | X         |           |         |         |          |                |                |                |
| 2       | X           | X           |           |           |         |         |          |                |                |                |
| 3       |             | X           | X         |           |         |         |          |                |                |                |
| 4       | X           |             |           |           | X       |         |          |                |                |                |
| 5       |             |             | X         |           | X       |         |          |                |                |                |
| 6       | X           | X           |           |           | X       |         |          |                |                |                |
| 7       |             | X           |           |           |         | X       |          |                |                |                |
| 8       |             | X           |           |           |         | X       | X        |                |                |                |
| 9       | X           |             |           |           |         |         |          | X              | X              | X              |
| 10      |             |             |           |           |         |         |          |                | X              | X              |
| 51      | X           |             |           | X         |         |         |          |                |                |                |
| 52      |             | X           |           | X         |         |         |          |                |                |                |
| 53      |             |             |           | X         | X       |         |          |                |                |                |
| ALL     | X           | X           | X         |           | X       | X       | X        | X              | X              | X              |
| A5      | X           | X           |           | X         | X       | X       | X        | X              | X              | X              |

<span id="_Ref58422357" class="anchor"></span>Table 25: Alpha Subscripts

### CAI^VADPT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Description

Returns the Comprehensive Prevention, Access to Care, and Treatment (COMPACT) indicator for enrolled Veterans and non-enrolled Veterans.

Input

- DFN—This required variable is the internal entry number in the PATIENT (#2) file.

Output

- VACOM("CAI")—Returns the Veteran’s COMPACT eligibility status
- 0—Veteran is not COMPACT eligible
- 1—Veteran is COMPACT eligible

## Alpha Subscripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Call             | Variable    | Alpha Translation |
|------------------|-------------|-------------------|
| DEM^VADPT    | VADM(1)     | VADM("NM")        |
|                  | VADM(2)     | VADM("SS")        |
|                  | VADM(3)     | VADM("DB")        |
|                  | VADM(4)     | VADM("AG")        |
|                  | VADM(5)     | VADM("SX")        |
|                  | VADM(6)     | VADM("EX")        |
|                  | VADM(7)     | VADM("RE")        |
|                  | VADM(8)     | VADM("RA")        |
|                  | VADM(9)     | VADM("RP")        |
|                  | VADM(10)    | VADM("MS")        |
| DEMUPD^VADPT | VADEMO(1)   | VADEMO("NM")      |
|                  | VADEMO(1,1) | VADEMO(“NM”,1)    |
|                  | VADEMO(2)   | VADEMO("SS")      |
|                  | VADEMO(3)   | VADEMO("DB")      |
|                  | VADEMO(4)   | VADEMO("AG")      |
|                  | VADEMO(5)   | VADEMO("SX")      |
|                  | VADEMO(6)   | VADEMO("EX")      |
|                  | VADEMO(7)   | VADEMO("RE")      |
|                  | VADEMO(8)   | VADEMO("RA")      |
|                  | VADEMO(9)   | VADEMO("RP")      |
|                  | VADEMO(10)  | VADEMO("MS")      |
|                  | VADEMO(11)  | VADEMO(“ET”)      |
|                  | VADEMO(12)  | VADEMO(“RC”)      |
|                  | VADEMO(13)  | VADEMO("PL")      |
| ELIG^VADPT   | VAEL(1)     | VAEL("EL")        |
|                  | VAEL(1,#)   | VAEL("EL",#)      |
|                  | VAEL(2)     | VAEL("PS")        |
|                  | VAEL(3)     | VAEL("SC")        |
|                  | VAEL(4)     | VAEL("VT")        |
|                  | VAEL(5)     | VAEL("IN")        |
|                  | VAEL(5,#)   | VAEL("IN",#)      |
|                  | VAEL(6)     | VAEL("TY")        |
|                  | VAEL(7)     | VAEL("CN")        |
|                  | VAEL(8)     | VAEL("ES")        |
|                  | VAEL(9)     | VAEL("MT")        |
|                  | VAEL(10)    | VAEL(“OTH”)       |
| MB^VADPT     | VAMB(1)     | VAMB("AA")        |
|                  | VAMB(2)     | VAMB("HB")        |
|                  | VAMB(3)     | VAMB("SS")        |
|                  | VAMB(4)     | VAMB("PE")        |
|                  | VAMB(5)     | VAMB("MR")        |
|                  | VAMB(6)     | VAMB("SI")        |
|                  | VAMB(7)     | VAMB("DI")        |
|                  | VAMB(8)     | VAMB("OR")        |
|                  | VAMB(9)     | VAMB("GI")        |
| SVC^VADPT    | VASV(1)     | VASV("VN")        |
|                  | VASV(1,#)   | VASV("VN",#)      |
|                  | VASV(2)     | VASV("AO")        |
|                  | VASV(2,#)   | VASV("AO",#)      |
|                  | VASV(3)     | VASV("IR")        |
|                  | VASV(3,#)   | VASV("IR",#)      |
|                  | VASV(4)     | VASV("PW")        |
|                  | VASV(4,#)   | VASV("PW",#)      |
|                  | VASV(5)     | VASV("CS")        |
|                  | VASV(5,#)   | VASV("CS",#)      |
|                  | VASV(6)     | VASV("S1")        |
|                  | VASV(6,#)   | VASV("S1",#)      |
|                  | VASV(7)     | VASV("S2")        |
|                  | VASV(7,#)   | VASV("S2",#)      |
|                  | VASV(8)     | VASV("S3")        |
|                  | VASV(8,#)   | VASV("S3",#)      |
|                  | VASV(9)     | VASV(“PH”)        |
|                  | VASV(9,#)   | VASV(“PH”,#)      |
|                  | VASV(10)    | VASV(“CV”)        |
|                  | VASV(10,#)  | VASV(“CV”,#)      |
|                  | VASV(11)    | VASV(“OIF”)       |
|                  | VASV(11,#)  | VASV(“OIF”,#)     |
|                  | VASV(12)    | VASV(“OEF”)       |
|                  | VASV(12,#)  | VASV(“OEF”,#)     |
|                  | VASV(13)    | VASV(“UNK”)       |
|                  | VASV(13,#)  | VASV(“UNK”,#)     |
|                  | VASV(14)    | VASV(“SHD”)       |
|                  | VASV(14,#)  | VASV(“SHD”,#)     |
|                  | VASV(15)    | VASV(“TERA”)      |
| ADD^VADPT    | VAPA(1)     | VAPA("L1")        |
|                  | VAPA(2)     | VAPA("L2")        |
|                  | VAPA(3)     | VAPA("L3")        |
|                  | VAPA(4)     | VAPA("CI")        |
|                  | VAPA(5)     | VAPA("ST")        |
|                  | VAPA(6)     | VAPA("ZP")        |
|                  | VAPA(7)     | VAPA("CO")        |
|                  | VAPA(8)     | VAPA("PN")        |
|                  | VAPA(9)     | VAPA("TS")        |
|                  | VAPA(10)    | VAPA("TE")        |
|                  | VAPA(11)    | VAPA("Z4")        |
|                  | VAPA(12)    | VAPA(“CCA”)       |
|                  | VAPA(13)    | VAPA(“CL1”)       |
|                  | VAPA(14)    | VAPA(“CL2”)       |
|                  | VAPA(15)    | VAPA(“CL3”)       |
|                  | VAPA(16)    | VAPA(“CCI”)       |
|                  | VAPA(17)    | VAPA(“CST”)       |
|                  | VAPA(18)    | VAPA(“CZP”)       |
|                  | VAPA(19)    | VAPA(“CCO”)       |
|                  | VAPA(20)    | VAPA(“CCS”)       |
|                  | VAPA(21)    | VAPA(“CCE”)       |
|                  | VAPA(22)    | VAPA(“CTY”)       |
|                  | VAPA(23)    | VAPA(“PR”)        |
|                  | VAPA(24)    | VAPA(“PC”)        |
|                  | VAPA(25)    | VAPA(“CT”)        |
|                  | VAPA(26)    | VAPA(“CPR”)       |
|                  | VAPA(27)    | VAPA(“CPC”)       |
|                  | VAPA(28)    | VAPA(“CCT”)       |
|                  | VAPA(29)    | VAPA(“CPN”)       |
|                  | VAPA(30)    | VAPA(“RL1”)       |
|                  | VAPA(31)    | VAPA(“RL2”)       |
|                  | VAPA(32)    | VAPA(“RL3”)       |
|                  | VAPA(33)    | VAPA(“RCI”)       |
|                  | VAPA(34)    | VAPA(“RST”)       |
|                  | VAPA(35)    | VAPA(“RZP”)       |
|                  | VAPA(36)    | VAPA(“RCO”)       |
|                  | VAPA(37)    | VAPA(“RCT”)       |
|                  | VAPA(38)    | VAPA(“RPR”)       |
|                  | VAPA(39)    | VAPA(“RPC”)       |
| OAD^VADPT    | VAOA(1)     | VAOA("L1")        |
|                  | VAOA(2)     | VAOA("L2")        |
|                  | VAOA(3)     | VAOA("L3")        |
|                  | VAOA(4)     | VAOA("CI")        |
|                  | VAOA(5)     | VAOA("ST")        |
|                  | VAOA(6)     | VAOA("ZP")        |
|                  | VAOA(7)     | VAOA("CO")        |
|                  | VAOA(8)     | VAOA("PN")        |
|                  | VAOA(9)     | VAOA("NM")        |
|                  | VAOA(10)    | VAOA("RE")        |
|                  | VAOA(11)    | VAOA("Z4")        |
| INP^VADPT    | VAIN(1)     | VAIN("AN")        |
|                  | VAIN(2)     | VAIN("DR")        |
|                  | VAIN(3)     | VAIN("TS")        |
|                  | VAIN(4)     | VAIN("WL")        |
|                  | VAIN(5)     | VAIN("RB")        |
|                  | VAIN(6)     | VAIN("BS")        |
|                  | VAIN(7)     | VAIN("AD")        |
|                  | VAIN(8)     | VAIN("AT")        |
|                  | VAIN(9)     | VAIN("AF")        |
|                  | VAIN(10)    | VAIN("PT")        |
|                  | VAIN(11)    | VAIN("AP")        |
| IN5^VADPT    | VAIP(1)     | VAIP("MN")        |
|                  | VAIP(2)     | VAIP("TT")        |
|                  | VAIP(3)     | VAIP("MD")        |
|                  | VAIP(4)     | VAIP("MT")        |
|                  | VAIP(5)     | VAIP("WL")        |
|                  | VAIP(6)     | VAIP("RB")        |
|                  | VAIP(7)     | VAIP("DR")        |
|                  | VAIP(8)     | VAIP("TS")        |
|                  | VAIP(9)     | VAIP("MF")        |
|                  | VAIP(10)    | VAIP("BS")        |
|                  | VAIP(11)    | VAIP("RD")        |
|                  | VAIP(12)    | VAIP("PT")        |
|                  | VAIP(13)    | VAIP("AN")        |
|                  | VAIP(13,#)  | VAIP("AN",#)      |
|                  | VAIP(14)    | VAIP("LN")        |
|                  | VAIP(14,#)  | VAIP("LN",#)      |
|                  | VAIP(15)    | VAIP("PN")        |
|                  | VAIP(15,#)  | VAIP("PT",#)      |
|                  | VAIP(16)    | VAIP("NN")        |
|                  | VAIP(16,#)  | VAIP("NN",#)      |
|                  | VAIP(17)    | VAIP("DN")        |
|                  | VAIP(17,#)  | VAIP("DN",#")     |
|                  | VAIP(18)    | VAIP("AP")        |
| OPD^VADPT    | VAPD(1)     | VAPD("BC")        |
|                  | VAPD(2)     | VAPD("BS")        |
|                  | VAPD(3)     | VAPD("FN")        |
|                  | VAPD(4)     | VAPD("MN")        |
|                  | VAPD(5)     | VAPD("MM")        |
|                  | VAPD(6)     | VAPD("OC")        |
|                  | VAPD(7)     | VAPD("ES")        |
|                  | VAPD(8)     | VAPD("WP")        |

<span id="_Toc193958053" class="anchor"></span>Table 26: Available Data Fields

# Data Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Available Data Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Ref54772172" class="anchor"></span>Table 27: Patient Label Print Routine Control Codes</p></caption>
<colgroup>
<col style="width: 4%" />
<col style="width: 17%" />
<col style="width: 13%" />
<col style="width: 21%" />
<col style="width: 21%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th>ID</th>
<th>Field Name</th>
<th>Data Type</th>
<th>Format or Valid Values</th>
<th>Description</th>
<th>Examples of Returned Data</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>APPOINTMENT DATE/TIME</td>
<td>DATE/TIME</td>
<td>YYYMMDD@HHMM</td>
<td>The scheduled Appointment date/time.</td>
<td><p>3021215@113</p>
<p>3021201@0815</p></td>
</tr>
<tr class="even">
<td>2</td>
<td>CLINIC ID and NAME</td>
<td>POINTER and TEXT</td>
<td>ID^name</td>
<td>Clinic ID and name.</td>
<td><p>150^CARDIOLOGY</p>
<p>32^TOM’S CLINIC</p></td>
</tr>
<tr class="odd">
<td>3</td>
<td>APPOINTMENT STATUS</td>
<td>ALPHA</td>
<td><ul>
<li><p><strong>N—</strong>No-Show</p></li>
<li><p><strong>C—</strong>Cancelled</p></li>
<li><p><strong>R—</strong>Scheduled / Kept</p></li>
<li><p><strong>NT—</strong>No Action Taken</p></li>
</ul></td>
<td><p>The status of the appointment:</p>
<ul>
<li><p><strong>N</strong> for no-show appointment.</p></li>
<li><p><strong>C</strong> for cancelled appointment (cancelled for ANY reason).</p></li>
<li><p><strong>NT</strong> for no action taken.</p></li>
<li><p><strong>R</strong> for a future appointment or a past kept appointment.</p></li>
</ul></td>
<td><ul>
<li><p><strong>N</strong></p></li>
<li><p><strong>C</strong></p></li>
<li><p><strong>R</strong></p></li>
<li><p><strong>NT</strong></p></li>
</ul></td>
</tr>
<tr class="even">
<td>4</td>
<td>PATIENT ID and NAME</td>
<td>POINTER and TEXT</td>
<td>ID^name</td>
<td>Patient ID and name.</td>
<td><p>34877^DGPATIENT,ONE</p>
<p>455^DGPATIENT,TWO</p></td>
</tr>
<tr class="odd">
<td>5</td>
<td>LENGTH OF APPOINTMENT</td>
<td>NUMERIC</td>
<td>NNN</td>
<td>The scheduled length of appointment, in minutes.</td>
<td><p>20</p>
<p>60</p></td>
</tr>
<tr class="even">
<td>6</td>
<td>COMMENTS</td>
<td>TEXT</td>
<td>free text</td>
<td>Any comments associated with the appointment.</td>
<td>PATIENT NEEDS WHEELCHAIR</td>
</tr>
<tr class="odd">
<td>7</td>
<td>OVERBOOK</td>
<td>TEXT</td>
<td>Y or N</td>
<td>“<strong>Y</strong>” if appointment is an overbook else “<strong>N</strong>”.</td>
<td><p>Y</p>
<p>N</p></td>
</tr>
<tr class="even">
<td>8</td>
<td>ELIGIBILITY OF VISIT ID and NAME</td>
<td>POINTER and TEXT</td>
<td>ID^name</td>
<td>Eligibility code and name associated with the appointment.</td>
<td><p>2^AID &amp; ATTENDANCE</p>
<p>7^ALLIED VETERAN</p>
<p>13^COLLATERAL OF VET.</p></td>
</tr>
<tr class="odd">
<td>9</td>
<td>CHECK-IN DATE/TIME</td>
<td>DATE/TIME</td>
<td>YYYMMDD@HHMM</td>
<td>Date/Time the patient checked in for the appointment.</td>
<td>3021215@113</td>
</tr>
<tr class="even">
<td>10</td>
<td>APPOINTMENT TYPE ID and NAME</td>
<td>POINTER and TEXT</td>
<td>ID^name</td>
<td>Type of appointment ID and name.</td>
<td><p>1^COMPENSATION &amp; PENSION</p>
<p>3^ORGAN DONORS</p>
<p>7^COLLATERAL OF VET.</p></td>
</tr>
<tr class="odd">
<td>11</td>
<td>CHECK-OUT DATE/TIME</td>
<td>DATE/TIME</td>
<td>YYYMMDD@HHMM</td>
<td>Date/Time the patient checked out of the appointment.</td>
<td>3021215@113</td>
</tr>
<tr class="even">
<td>12</td>
<td>PATIENT STATUS</td>
<td>TEXT</td>
<td><p>I</p>
<p>O</p>
<p><strong>NULL</strong></p></td>
<td>For future, scheduled appointments, the current status of the patient. For past, kept appointments, the status at the time of the appointment. For cancelled and no-show appointments, this is <strong>NULL</strong>.</td>
<td><p>I</p>
<p>O</p>
<p>“”</p></td>
</tr>
</tbody>
</table>

<span id="_Ref54772172" class="anchor"></span>Table 27: Patient Label Print Routine Control Codes

## Configuring Bar Code Label Printers for Print Patient Label Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Veteran Identification Card (VIC) provided by the VIC Replacement project does *not* support embossing of protected health information. Instead, the Print Patient Label \[DG PRINT PATIENT LABEL\] option allows labels to be printed with the patient’s protected health information.

The labels contain the following:

- Patient’s name
- Social security number
- Date of birth
- (Optional fourth line) Contains the patient’s inpatient location (ward and room#)

<span id="_Ref54771807" class="anchor"></span>Figure 11: Sample Label

![](pims-version-5-3-adt-technical-manual/002.png)

The labels can be affixed to medical record forms in lieu of using the current embossed cards to imprint this information.

Example Label

The Print Patient Label \[DG PRINT PATIENT LABEL\] option was exported with the Veteran ID Card (VIC) Replacement patch (DG\*5.3\*571). This option was placed on the ADT Outputs Menu \[DG OUTPUTS MENU\] option.

This option supports plain text printing to dot matrix and laser printers by prompting the user for the number of lines that the label stock can contain. In addition, bar code label printers, such as Zebra and Intermec, are supported on systems that have installed the Kernel Support for Bar Code Printers patch (XU\*8.0\*205).

### Hardware Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The printer *must* be physically connected to the network and then defined in the DEVICE (#3.5) and TERMINAL TYPE (#3.2) files.

### Software Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Bar code label printers, such as the Zebra and Intermec printers, require control codes to be defined in the CONTROL CODES (#3.2055) subfile of the TERMINAL TYPE (#3.2) file.

The patient label print routine (DGPLBL) checks for the existence of the control codes before attempting to execute. Presently, the patient label print routine (DGPLBL) uses eight control codes. DBIA \#3435 allows direct M read access to the CONTROL CODES (#3.2055) subfile of the TERMINAL TYPE (#3.2) file.

It is *not* required that all control codes be defined; just build the necessary control codes for the selected printer.

## Control Code Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The table below lists the control codes that are currently used by the patient label print routine (DGPLBL). In order for the routine to work correctly, these control codes *must* be entered through VA FileMan in the CONTROL CODES (#3.2055) subfile in the TERMINAL TYPE (#3.2) file using the names listed in the table below.

| Code | Description           |
|------|-----------------------|
| FI   | Format Initialization |
| FE   | Format End            |
| SL   | Start of Label        |
| EL   | End of Label          |
| ST   | Start of Text         |
| ET   | End of Text           |
| STF  | Start of Text Field   |
| ETF  | End of Text Field     |

<span id="_Ref54266837" class="anchor"></span>Table 28: MSH—Message Header Segments

### Patient Label Print Routine Control Code Use

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following pseudo-code listing shows the flow and the points at which each of the control codes are used. It is *not* required that all control codes be defined; just build the necessary control codes for the selected printer:

1.  Label print routine invoked.
36. Control codes loaded into local array DGIOCC. Variable DGIOCC is defined to indicate whether or not control codes exist.
37. Format Initialization.
38. For each label printed:
- Start of Label
- Start of Text\*
- Start of Text Field\*
- Text Information\*
- End of Text Field\*
- End of Text\*
- End of Label.
39. Format End.

\*Indicates items that may be executed repeatedly.

### Label Printer Setup Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are examples of the control codes setup in the CONTROL CODES (#3.2055) subfile in the TERMINAL TYPE (#3.2) file for the Zebra and Intermec label printers.

These printers were used during the development process, and the examples are provided to guide the user in the control code setup. The examples provided are based on a 1½ by 3½ inch label.

### Zebra Label Printer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Example 1—Control Codes Setup for Horizontal Labels

<span id="_Toc193958010" class="anchor"></span>Figure 12: Zebra Label Printer Example—Control Codes Setup for Horizontal Labels

NUMBER: 1

ABBREVIATION: FI

FULL NAME: FORMAT INITIALIZATION

CONTROL CODE: W "^XA",!,"^LH0,0^FS",!

NUMBER: 2

ABBREVIATION: SL

FULL NAME: START LABEL

CONTROL CODE: W "^XA",! S DGY=30,DGX=10

NUMBER: 3

ABBREVIATION: ST

FULL NAME: START TEXT

CONTROL CODE: W "^FO",DGX,",",DGY,"^A0N,30,30" S DGY=DGY+40

NUMBER: 4

ABBREVIATION: STF

FULL NAME: START TEXT FIELD

CONTROL CODE: W "^FD"

NUMBER: 5

ABBREVIATION: ETF

FULL NAME: END TEXT FIELD

CONTROL CODE: W "^FS",!

NUMBER: 6

ABBREVIATION: EL

FULL NAME: END LABEL

CONTROL CODE: W "^XZ",!

#### Example 2—Control Codes Setup for Vertical Labels

<span id="_Toc193958011" class="anchor"></span>Figure 13: Zebra Label Printer Example—Control Codes Setup for Vertical Labels

NUMBER: 1

ABBREVIATION: FI

FULL NAME: FORMAT INITIALIZATION

CONTROL CODE: W "^XA",!,"^LH0,0^FS",!

NUMBER: 2

ABBREVIATION: SL

FULL NAME: START LABEL

CONTROL CODE: W "^XA",! S DGY=50,DGX=190

NUMBER: 3

ABBREVIATION: ST

FULL NAME: START TEXT

CONTROL CODE: W "^FO",DGX,",",DGY,"^A0R,30,20" S DGX=DGX-40

NUMBER: 4

ABBREVIATION: STF

FULL NAME: START TEXT FIELD

CONTROL CODE: W "^FD"

NUMBER: 5

ABBREVIATION: ETF

FULL NAME: END TEXT FIELD

CONTROL CODE: W "^FS",!

NUMBER: 6

ABBREVIATION: EL

FULL NAME: END LABEL

CONTROL CODE: W "^XZ",!

## Intermec Label Printer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Intermec label printers require that a label format be sent to the printer prior to sending any data to print. The label format is defined in an M routine, which is then defined in the OPEN EXECUTE (#6) field in the TERMINAL TYPE (#3.2) file.

Two sample formats are provided with patch DG\*5.3\*571 in routine DGPLBL1:

- HINTERM^DGPLBL1 entry point creates a horizontal format label.
- VINTERM^DGPLBL1 entry point creates a vertical format label.

The following setup examples show the OPEN EXECUTE (#6) and CONTROL CODES (#55) field values that were used in the development process and are provided to guide the user in this setup.

The examples are based on a 1½ by 3½ inch label.

### Example 1—Control Codes Setup for Horizontal Labels

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc193958012" class="anchor"></span>Figure 14: Control Codes Setup for Horizontal Labels

OPEN EXECUTE: D HINTERM^DGPLBL1

NUMBER: 1

ABBREVIATION: FI

FULL NAME: FORMAT INITIALIZATION

CONTROL CODE: W "\<STX\>R;\<ETX\>",!

NUMBER: 2

ABBREVIATION: SL

FULL NAME: START LABEL

CONTROL CODE: W "\<STX\>\<ESC\>E2\<ETX\>",!,"\<STX\>\<CAN\>\<ETX\>",!

NUMBER: 3

ABBREVIATION: ST

FULL NAME: START TEXT

CONTROL CODE: W "\<STX\>”

NUMBER: 4

ABBREVIATION: ET

FULL NAME: END TEXT

CONTROL CODE: W "\<CR\>\<ETX\>",!

NUMBER: 5

ABBREVIATION: EL

FULL NAME: END LABEL

CONTROL CODE: W "\<STX\>\<ETB\>\<ETX\>",!

### Example 2—Control Codes Setup for Vertical Labels

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc193958013" class="anchor"></span>Figure 15: Control Codes Setup for Vertical Labels

OPEN EXECUTE: D VINTERM^DGPLBL1

NUMBER: 1

ABBREVIATION: FI

FULL NAME: FORMAT INITIALIZATION

CONTROL CODE: W "\<STX\>R;\<ETX\>",!

NUMBER: 2

ABBREVIATION: SL

FULL NAME: START LABEL

CONTROL CODE: W "\<STX\>\<ESC\>E2\<ETX\>",!,"\<STX\>\<CAN\>\<ETX\>",!

NUMBER: 3

ABBREVIATION: ST

FULL NAME: START TEXT

CONTROL CODE: W "\<STX\>”

NUMBER: 4

ABBREVIATION: ET

FULL NAME: END TEXT

CONTROL CODE: W "\<CR\>\<ETX\>",!

NUMBER: 5

ABBREVIATION: EL

FULL NAME: END LABEL

CONTROL CODE: W "\<STX\>\<ETB\>\<ETX\>",!

# HL7 Interface Specification for Transmission of Ambulatory Care Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

18. Starting December 1, 2018, the Ambulatory Care nightly job and Performance Monitor data extract daily transmissions, and monthly APM Performance Monitor Task generated from each VistA site are no longer needed to be sent to the AITC; the National Patient Care Database (NPCDB) is being shut down in Austin and the Corporate Data Warehouse (CDW) is replacing the database as the authoritative source. The VistA extracts done to populate the CDW replaces the need for the HL7 transmission.
- Place the following options “out of order”:
- Ambulatory Care Nightly Transmission to NPCDB \[SCDX AMBCAR NIGHTLY XMIT\].
- Retransmit Ambulatory Care Data by Date Range \[SCDX AMBCAR RETRANS BY DATE\].
- Retransmit Selected Error Code \[SCDX AMBCAR RETRANS ERROR\].
- Selective Retransmission of NPCDB Rejections \[SCDX AMBCAR RETRANS SEL REJ\].
- Schedule APM Performance Monitor Task \[SCRPW APM TASK JOB\].
- Performance Monitor Retransmit Report (AAC) \[SCRPW PM RETRANSMIT REPORT\].
- Nightly job for PM data extract \[SDOQM PM NIGHTLY JOB\].

This interface specification specifies the information needed for Ambulatory Care data reporting. This data exchange is triggered by specific outpatient events that relate to workload credit in VistA. The basic communication protocol is addressed, as well as the information that is made available and how it is obtained.

This application uses an abstract message approach and encoding rules specified by HL7. HL7 is used for communicating data associated with various events that occur in health care environments. For example, when a check-out occurs in VistA, the event triggers an update patient information message. This message is an unsolicited transaction to all external systems interfacing with VistA.

The formats of these messages conform to the Version 2.3 HL7 Interface Standards where applicable. HL7 custom message formats ("Z" segments) are used only when necessary.

## Assumptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Assumptions have been made at the beginning of this project in order to help define the scope and meet the initial needs in interfacing with the Austin Information Technology Center (AITC; formerly known as the Austin Automation Center \[AAC\]).

### Message Content

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The data sent in the HL7 messages is limited to the information that can be processed by the AITC, with the exception of the PID and ZPD segments, which are populated using the nationally supported VistA call. The data sent is also limited to what is available in VistA.

In order to capture the most information, specific outpatient events generate messages to the AITC systems. This is *not* intended to cover all possible outpatient events, only those events that may result in the capture of workload information and data needed to update the National Patient Care Database (NPCDB).

The mode for capturing data for outpatient events was chosen to capture as much of the data as possible.

19. REF: For further information on the mode for capturing the outpatient events, see “[Data Capture and Transmission](#data-capture-and-transmission).”

### Data Capture and Transmission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When AICS, PIMS, and PCE options or calls are used to update specific outpatient encounter data in VistA, these events and changes are captured. Any changes made to the VistA database in *non*-standard ways, such as a direct global set by an application or by M code, are *not* captured.

### Background Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A nightly background job sends HL7 messages for each outpatient encounter event for the day.

### Batch Messages and Acknowledgements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Batch messages are used to transmit the outpatient encounter events.

Each batch message sent is acknowledged at the application level. The batch acknowledgment contains acknowledgment messages only for those messages containing errors.

Using this mode, it is possible that an empty batch acknowledgment is sent. This happens only when all messages in the batch being acknowledged were accepted.

### VA MailMan Lower Level Protocol

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HL7 V. 1.6 of the VA MailMan lower level protocol (LLP) is used. This version of the VA MailMan LLP differs from HL7 V. 1.5 in that a blank line is placed between each segment in the message \[denoting a carriage return\].

## HL7 Control Segments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section defines the HL7 control segments supported by VistA. The messages are presented separately and defined by category. Segments are also described. The messages are presented in the following categories:

- Message Control.
- Unsolicited Transactions from VistA (Section 3).

## Message Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the VistA perspective, all incoming or outgoing messages are handled or generated based on an event.

In this section, and the following sections, these elements are defined for each message:

- Trigger events.
- Message event code.
- List of segments used in the message.
- List of fields for each segment in the message.

Each message is composed of segments, which:

- Contain logical groupings of data.
- Can be optional or repeatable:
- A \[ \] indicates the segment is optional.
- The { } indicates the segment is repeatable.

For each message category there is a list of HL7 standard segments or "Z" segments used for the message.

## Segment Table Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For each segment, the data elements are described in table format. The table includes the following:

- Sequence number (SEQ)
- Maximum length (LEN)
- Data type (DT)
- Required or optional (R/O)
- Repeatable (RP/#),
- Table number (TBL \#)
- Element name
- VistA description

Each segment is described in the following sections.

## Message Control Segments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the message control segments that are contained in message types described in this document. These are generic descriptions.

Any time any of the segments described in this section are included in a message in this document, the VistA descriptions and mappings are as specified here, unless otherwise specified in that section.

### MSH—Message Header Segments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Ref58233474" class="anchor"></span>Table 29: BHS—Batch Header Segment</p></caption>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 24%" />
<col style="width: 31%" />
</colgroup>
<thead>
<tr class="header">
<th>SEQ</th>
<th>LEN</th>
<th>DT</th>
<th>R/O</th>
<th>RP/#</th>
<th>TBL#</th>
<th>Element Name</th>
<th>VistA Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>1</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Field Separator</td>
<td><em>Recommended</em> value is <strong>^</strong> (caret).</td>
</tr>
<tr class="even">
<td>2</td>
<td>4</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Encoding Characters</td>
<td><p><em>Recommended</em> delimiter values:</p>
<ul>
<li><p>Component = <strong>~</strong> (tilde)</p></li>
<li><p>Repeat = <strong>|</strong> (bar)</p></li>
<li><p>Escape = <strong>\</strong> (back slash)</p></li>
<li><p>Subcomponent = <strong>&amp;</strong> (ampersand)</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>3</td>
<td>15</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Sending Application</td>
<td><p>When originating from facility:<br />
<strong>AMBCARE-DH441</strong></p>
<p>When originating from NPCDB: <strong>NPCD-AAC*</strong></p></td>
</tr>
<tr class="even">
<td>4</td>
<td>20</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Sending Facility</td>
<td><p>When originating from facility: Station's facility number.</p>
<p>When originating from NPCDB: 200.</p></td>
</tr>
<tr class="odd">
<td>5</td>
<td>30</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Receiving Application</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>6</td>
<td>30</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Receiving Facility</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>7</td>
<td>26</td>
<td>TS</td>
<td></td>
<td></td>
<td></td>
<td>Date/Time Of Message</td>
<td>Date and time message was created.</td>
</tr>
<tr class="even">
<td>8</td>
<td>40</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Security</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>9</td>
<td>7</td>
<td>CM</td>
<td>R</td>
<td></td>
<td><p>0076</p>
<p>0003</p></td>
<td>Message Type</td>
<td><p>Two Components:</p>
<ul>
<li><p>Component 1: See <a href="#_Ref58237660">Table 0076—Message Type</a>.</p></li>
<li><p>Component 2: See <a href="#_Ref58237406">Table 0003—Event Type Code</a>.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>10</td>
<td>20</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Message Control ID</td>
<td>Automatically generated by VistA HL7 package.</td>
</tr>
<tr class="odd">
<td>11</td>
<td>1</td>
<td>ID</td>
<td>R</td>
<td></td>
<td>0103</td>
<td>Processing ID</td>
<td><strong>P</strong> (production).</td>
</tr>
<tr class="even">
<td>12</td>
<td>8</td>
<td>ID</td>
<td>R</td>
<td></td>
<td>0104</td>
<td>Version ID</td>
<td>2.3 (Version 2.3).</td>
</tr>
<tr class="odd">
<td>13</td>
<td>15</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Sequence Number</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>14</td>
<td>180</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Continuation Pointer</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>15</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td>0155</td>
<td>Accept Acknowledgment Type</td>
<td><strong>NE</strong> (never acknowledge).</td>
</tr>
<tr class="even">
<td>16</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td>0155</td>
<td>Application Acknowledgment Type</td>
<td><strong>AL</strong> (always acknowledge).</td>
</tr>
<tr class="odd">
<td>17</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td>Country Code</td>
<td>Not used.</td>
</tr>
</tbody>
</table>

<span id="_Ref58233474" class="anchor"></span>Table 29: BHS—Batch Header Segment

20.  NOTE: \*AAC stands for Austin Automation Center. The name of that facility has been changed to Austin Information Technology Center (AITC).

### BHS—Batch Header Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Ref58233590" class="anchor"></span>Table 30: BTS—Batch Trailer Segment</p></caption>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 23%" />
<col style="width: 30%" />
</colgroup>
<thead>
<tr class="header">
<th>SEQ</th>
<th>LEN</th>
<th>DT</th>
<th>R/O</th>
<th>RP/#</th>
<th>TBL#</th>
<th>Element Name</th>
<th>VistA Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>1</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Batch Field Separator</td>
<td><em>Recommended</em> value is <strong>^</strong> (caret).</td>
</tr>
<tr class="even">
<td>2</td>
<td>4</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Batch Encoding Characters</td>
<td><p><em>Recommended</em> delimiter values:</p>
<ul>
<li><p>Component = <strong>~</strong> (tilde)</p></li>
<li><p>Repeat = <strong>|</strong> (bar)</p></li>
<li><p>Escape = <strong>\</strong> (back slash)</p></li>
<li><p>Subcomponent = <strong>&amp;</strong> (ampersand)</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>3</td>
<td>15</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Batch Sending Application</td>
<td><p>When originating from facility: <strong>AMBCARE-DH142</strong></p>
<p>When originating from NPCDB: <strong>NPCD-AAC*</strong></p></td>
</tr>
<tr class="even">
<td>4</td>
<td>20</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Batch Sending Facility</td>
<td><p>When originating from facility: Station's facility number</p>
<p>When originating from NPCDB: <strong>200</strong></p></td>
</tr>
<tr class="odd">
<td>5</td>
<td>15</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Batch Receiving Application</td>
<td><p>When originating from facility: <strong>NPCD-AAC</strong></p>
<p>When originating from NPCDB: <strong>AMBCARE-DH142</strong></p></td>
</tr>
<tr class="even">
<td>6</td>
<td>20</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Batch Receiving Facility</td>
<td><p>When originating from facility: <strong>200</strong></p>
<p>When originating from NPCDB: Station’s facility number</p></td>
</tr>
<tr class="odd">
<td>7</td>
<td>26</td>
<td>TS</td>
<td></td>
<td></td>
<td></td>
<td>Batch Creation Date/Time</td>
<td>Date and time batch message was created.</td>
</tr>
<tr class="even">
<td>8</td>
<td>40</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Batch Security</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td></td>
<td><em>20</em></td>
<td><em>ST</em></td>
<td></td>
<td></td>
<td></td>
<td><em>Batch Name/ID/Type</em></td>
<td><p>Four Components0F</p>
<ul>
<li><p>Component 1: Not used.</p></li>
<li><p>Component 2: <strong>P</strong>.</p></li>
<li><p>Component 3: <strong>ADT|Z00</strong>.</p></li>
<li><p>Component 4: <strong>2.3</strong>.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>10</td>
<td>80</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Batch Comment</td>
<td><p>Two Components1F<a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a>:</p>
<ul>
<li><p>Component 1: See <a href="#_Ref58237468">Table 0008—Acknowledgment Code</a>.</p></li>
<li><p>Component 2: Text Message.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>11</td>
<td>20</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Batch Control ID</td>
<td>Automatically generated by VistA HL7 Package.</td>
</tr>
<tr class="even">
<td>12</td>
<td>20</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Reference Batch Control ID</td>
<td>Batch Control ID of batch message being acknowledged.</td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>The VistA HL7 package has placed special meaning on this field. Note that this field is only used with batch acknowledgments.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

<span id="_Ref58233590" class="anchor"></span>Table 30: BTS—Batch Trailer Segment

21. \*AAC stands for Austin Automation Center. The name of that facility has been changed to Austin Information Technology Center (AITC).

### BTS—Batch Trailer Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| SEQ | LEN | DT  | R/O | RP/# | TBL# | Element Name        | VistA Description                |
|-----|-----|-----|-----|------|------|---------------------|----------------------------------|
| 1   | 10  | ST  |     |      | 0093 | Batch Message Count | Number of messages within batch. |
| 2   | 80  | ST  |     |      | 0094 | Batch Comment       | Not used.                        |
| 3   | 100 | CM  |     | Y    | 0095 | Batch Totals        | Not used.                        |

<span id="_Ref58233647" class="anchor"></span>Table 31: MSA—Message Acknowledgement Segment

### MSA—Message Acknowledgment Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| SEQ | LEN | DT  | R/O | RP/# | TBL#     | Element Name                | VistA Description                                                           |
|-----|-----|-----|-----|------|----------|-----------------------------|-----------------------------------------------------------------------------|
| 1   | 2   | ID  | R   |      | 0008     | Acknowledgment Code         | REF: See [Table 0008—Acknowledgment Code](#_Ref58237468).               |
| 2   | 20  | ST  | R   |      |          | Message Control ID          | Message Control ID of message being acknowledged.                           |
| 3   | 80  | ST  |     |      | NPCD 001 | Text Message                | Repetitive list of error codes denoting why the message was rejected2F[^1]. |
| 4   | 15  | NM  |     |      |          | Expected Sequence Number    | Not used.                                                                   |
| 5   | 1   | ID  |     |      | 0102     | Delayed Acknowledgment Type | Not used.                                                                   |
| 6   | 100 | CE  |     |      |          | Error Condition             | Not used.                                                                   |

<span id="_Ref58233685" class="anchor"></span>Table 32: EVN—Event Type Segment

### EVN—Event Type Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| SEQ |     |     | LEN | DT  | R/O | RP/# | TBL# | Element Name            | VistA Description                                         |
|-----|-----|-----|-----|-----|-----|------|------|-------------------------|-----------------------------------------------------------|
| 1   |     |     | 3   | ID  | R   |      | 0003 | Event Type Code         | REF: See [Table 0003—Event Type Code](#_Ref58237406). |
| 2   |     |     | 26  | TS  | R   |      |      | Date/Time of Event      | Date/Time Event Occurred.                                 |
| 3   |     |     | 26  | TS  |     |      |      | Date/Time Planned Event | Not used.                                                 |
| 4   |     |     | 3   | ID  |     |      | 0062 | Event Reason Code       | Not used.                                                 |
| 5   |     |     | 60  | CN  |     |      | 0188 | Operator ID             | Not used.                                                 |

<span id="_Ref58233812" class="anchor"></span>Table 33: PD1—Patient Additional Demographic Segment

## PID—Patient Identification Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For information on the Patient Identification (PID) segment, see Section 3.15, “PID-Patient Identification Segment” in the *MPI/PD HL7 Interface Specification* manual found on the VA Software Documentation Library (VDL).

### PD1—Patient Additional Demographic Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Ref58233913" class="anchor"></span>Table 34: PV1—Patient Visit Segment</p></caption>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 25%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th>SEQ</th>
<th>LEN</th>
<th>DT</th>
<th>R/O</th>
<th>RP/#</th>
<th>TBL#</th>
<th>Element Name</th>
<th>VistA Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>2</td>
<td>IS</td>
<td>O</td>
<td>Y</td>
<td>0223</td>
<td>LIVING DEPENDENCY</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>2</td>
<td>2</td>
<td>IS</td>
<td>O</td>
<td></td>
<td>0220</td>
<td>LIVING ARRANGEMENT</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>90</td>
<td>XON</td>
<td>O</td>
<td>Y</td>
<td></td>
<td>PATIENT PRIMARY FACILITY3F<a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a></td>
<td><p>Eight Components:</p>
<ul>
<li><p>Facility Name.</p></li>
<li><p>Not used.</p></li>
<li><p>Facility Number.</p></li>
<li><p>Not used.</p></li>
<li><p>Not used.</p></li>
<li><p>Not used.</p></li>
<li><p>Not used.</p></li>
<li><p>Not used.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>4</td>
<td>90</td>
<td>XCN</td>
<td>O</td>
<td>Y</td>
<td></td>
<td>PATIENT PRIMARY CARE PROVIDER NAME &amp; ID NO.</td>
<td><p>14 Components:</p>
<p>2 Sub-Components:</p>
<ul>
<li><p>Pointer to Entry In NEW PERSON (#200) file.</p></li>
<li><p>Facility Number.</p></li>
<li><p>Not used.</p></li>
<li><p>Not used.</p></li>
<li><p>Not used.</p></li>
<li><p>Not used.</p></li>
<li><p>Not used.</p></li>
<li><p>Not used.</p></li>
<li><p>This is always <strong>VA200</strong> (NEW PERSON file).</p></li>
<li><p>Not used.</p></li>
<li><p>Not used.</p></li>
<li><p>Not used.</p></li>
<li><p>Not used.</p></li>
<li><p>Not used.</p></li>
<li><p>Not used.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>5</td>
<td>2</td>
<td>IS</td>
<td>O</td>
<td></td>
<td>0231</td>
<td>STUDENT INDICATOR</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>6</td>
<td>2</td>
<td>IS</td>
<td>O</td>
<td></td>
<td>0295</td>
<td>HANDICAP</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>7</td>
<td>2</td>
<td>IS</td>
<td>O</td>
<td></td>
<td>0315</td>
<td>LIVING WILL</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>8</td>
<td>2</td>
<td>IS</td>
<td>O</td>
<td></td>
<td>0316</td>
<td>ORGAN DONOR</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>9</td>
<td>2</td>
<td>ID</td>
<td>O</td>
<td></td>
<td>0136</td>
<td>SEPARATE BILL</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>10</td>
<td>2</td>
<td>CX</td>
<td>O</td>
<td>Y</td>
<td></td>
<td>DUPLICATE PATIENT</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>11</td>
<td>1</td>
<td>CE</td>
<td>O</td>
<td></td>
<td>0125</td>
<td>PUBLICITY INDICATOR</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>12</td>
<td>1</td>
<td>ID</td>
<td>O</td>
<td></td>
<td>01293</td>
<td>PROTECTION INDICATOR</td>
<td>Not used.</td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>This element is only available from CIRN enabled facilities.<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

<span id="_Ref58233913" class="anchor"></span>Table 34: PV1—Patient Visit Segment

### PV1—Patient Visit Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| SEQ | LEN     | DT  | R/O | RP/# | TBL# | Element Name              | VistA Description                                                     |
|-----|---------|-----|-----|------|------|---------------------------|-----------------------------------------------------------------------|
| 1   | 4       | SI  |     |      |      | Set ID - Patient Visit    | Sequential Number.                                                    |
| 2   | 1       | ID  | R   |      | 0004 | Patient Class             | This is always O (outpatient).                                    |
| 3   | 12      | CM  |     |      |      | Assigned Patient Location | Not used.                                                             |
| 4   | 4       | ID  |     |      | 0007 | Admission Type            | REF: See [Table SD009—Purpose of Visit](#_Ref58238120).           |
| 5   | 20      | ST  |     |      |      | Preadmit Number           | Not used.                                                             |
| 6   | 12      | CM  |     |      |      | Prior Patient Location    | Not used.                                                             |
| 7   | 60      | CN  |     |      | 0010 | Attending Doctor          | Not used.                                                             |
| 8   | 60      | CN  |     |      | 0010 | Referring Doctor          | Not used.                                                             |
| 9   | 60      | CN  |     | Y    | 0010 | Consulting Doctor         | Not used.                                                             |
| 10  | 3       | ID  |     |      | 0069 | Hospital Service          | Not used.                                                             |
| 11  | 12      | CM  |     |      |      | Temporary Location        | Not used.                                                             |
| 12  | 2       | ID  |     |      | 0087 | Preadmit Test Indicator   | Not used.                                                             |
| 13  | 2       | ID  |     |      | 0092 | Readmission Indicator     | Not used.                                                             |
| 14  | 3       | ID  |     |      | 0023 | Admit Source              | REF: See [Table 0023—Admit Source (User Defined)](#_Ref58237220). |
| 15  | 2       | ID  |     | Y    | 0009 | Ambulatory Status         | Not used.                                                             |
| 16  | 2       | ID  |     |      | 0099 | VIP Indicator             | Not used.                                                             |
| 17  | 60      | CN  |     |      | 0010 | Admitting Doctor          | Not used.                                                             |
| 18  | 2       | ID  |     |      | 0018 | Patient Type              | Not used.                                                             |
| 19  | 15      | NM  |     |      |      | Visit Number              | Pointer to entry in OUTPATIENT ENCOUNTER (#409.68) file.              |
| 20  | 50      | CM  |     | Y    | 0064 | Financial Class           | Not used.                                                             |
| 21  | 2       | ID  |     |      | 0032 | Charge Price Indicator    | Not used.                                                             |
| 22  | 2       | ID  |     |      | 0045 | Courtesy Code             | Not used.                                                             |
| 23  | 2       | ID  |     |      | 0046 | Credit Rating             | Not used.                                                             |
| 24  | 2       | ID  |     | Y    | 0044 | Contract Code             | Not used.                                                             |
| 25  | 8       | DT  |     | Y    |      | Contract Effective Date   | Not used.                                                             |
| 26  | 12      | NM  |     | Y    |      | Contract Amount           | Not used.                                                             |
| 27  | 3       | NM  |     | Y    |      | Contract Period           | Not used.                                                             |
| 28  | 2       | ID  |     |      | 0073 | Interest Code             | Not used.                                                             |
| 29  | 1       | ID  |     |      | 0110 | Transfer to Bad Debt Code | Not used.                                                             |
| 30  | 8       | DT  |     |      |      | Transfer to Bad Debt Date | Not used.                                                             |
| 31  | 10      | ID  |     |      | 0021 | Bad Debt Agency Code      | Not used.                                                             |
| 32  | 12      | NM  |     |      |      | Bad Debt Transfer Amount  | Not used.                                                             |
| 33  | 12      | NM  |     |      |      | Bad Debt Recovery Amount  | Not used.                                                             |
| 34  | 1       | ID  |     |      | 0111 | Delete Account Indicator  | Not used.                                                             |
| 35  | 8       | DT  |     |      |      | Delete Account Date       | Not used.                                                             |
| 36  | 3       | ID  |     |      | 0112 | Discharge Disposition     | Not used.                                                             |
| 37  | 25      | CM  |     |      | 0113 | Discharged to Location    | Not used.                                                             |
| 38  | 2       | ID  |     |      | 0114 | Diet Type                 | Not used.                                                             |
| 39  | 74F[^2] | ID  |     |      | 0115 | Servicing Facility        | Facility number and suffix.                                           |
| 40  | 1       | ID  |     |      | 0116 | Bed Status                | Not used.                                                             |
| 41  | 2       | ID  |     |      | 0117 | Account Status            | Not used.                                                             |
| 42  | 12      | CM  |     |      |      | Pending Location          | Not used.                                                             |
| 43  | 12      | CM  |     |      |      | Prior Temporary Location  | Not used.                                                             |
| 44  | 26      | TS  |     |      |      | Admit Date/Time           | Date/time of encounter.                                               |
| 45  | 26      | TS  |     |      |      | Discharge Date/Time       | Not used.                                                             |
| 46  | 12      | NM  |     |      |      | Current Patient Balance   | Not used.                                                             |
| 47  | 12      | NM  |     |      |      | Total Charges             | Not used.                                                             |
| 48  | 12      | NM  |     |      |      | Total Adjustments         | Not used.                                                             |
| 49  | 12      | NM  |     |      |      | Total Payments            | Not used.                                                             |
| 50  | 20      | CM  |     |      |      | Alternate Visit ID        | Unique Identifier (PCE).                                              |

<span id="_Ref58233962" class="anchor"></span>Table 35: PV2—Patient Visit - Additional Information Segment

### PV2—Patient Visit - Additional Information Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Ref58234023" class="anchor"></span>Table 36: DG1—Diagnosis Information Segment</p></caption>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 9%" />
<col style="width: 29%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th>SEQ</th>
<th>LEN</th>
<th>DT</th>
<th>OPT</th>
<th>RP/#</th>
<th>TBL#</th>
<th>ITEM#</th>
<th>Element Name</th>
<th><p>VistA</p>
<p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>80</td>
<td>PL</td>
<td>C</td>
<td></td>
<td></td>
<td>00181</td>
<td>Prior Pending Location</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>2</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td></td>
<td>0129</td>
<td>00182</td>
<td>Accommodation Code</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td></td>
<td></td>
<td>00183</td>
<td>Admit Reason</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>4</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td></td>
<td></td>
<td>00184</td>
<td>Transfer Reason</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>5</td>
<td>25</td>
<td>ST</td>
<td>O</td>
<td>Y</td>
<td></td>
<td>00185</td>
<td>Patient Valuables</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>6</td>
<td>25</td>
<td>ST</td>
<td>O</td>
<td></td>
<td></td>
<td>00186</td>
<td>Patient Valuables Location</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>7</td>
<td>2</td>
<td>IS</td>
<td>O</td>
<td>Y</td>
<td>0130</td>
<td>00187</td>
<td>Visit User Code</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>8</td>
<td>26</td>
<td>TS</td>
<td>O</td>
<td></td>
<td></td>
<td>00188</td>
<td>Expected Admit Date/Time</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>9</td>
<td>26</td>
<td>TS</td>
<td>O</td>
<td></td>
<td></td>
<td>00189</td>
<td>Expected Discharge Date/Time</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>10</td>
<td>3</td>
<td>NM</td>
<td>O</td>
<td></td>
<td></td>
<td>00711</td>
<td>Estimated Length of Inpatient Stay</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>11</td>
<td>3</td>
<td>NM</td>
<td>O</td>
<td></td>
<td></td>
<td>00712</td>
<td>Actual Length of Inpatient Stay</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>12</td>
<td>50</td>
<td>ST</td>
<td>O</td>
<td></td>
<td></td>
<td>00713</td>
<td>Visit Description</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>13</td>
<td>250</td>
<td>XCN</td>
<td>O</td>
<td>Y</td>
<td></td>
<td>00714</td>
<td>Referral Source Code</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>14</td>
<td>8</td>
<td>DT</td>
<td>O</td>
<td></td>
<td></td>
<td>00715</td>
<td>Previous Service Date</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>15</td>
<td>1</td>
<td>ID</td>
<td>O</td>
<td></td>
<td>0136</td>
<td>00716</td>
<td>Employment Illness Related Indicator</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>16</td>
<td>1</td>
<td>IS</td>
<td>O</td>
<td></td>
<td>0213</td>
<td>00717</td>
<td>Purge Status Code</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>17</td>
<td>8</td>
<td>DT</td>
<td>O</td>
<td></td>
<td></td>
<td>00718</td>
<td>Purge Status Date</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>18</td>
<td>2</td>
<td>IS</td>
<td>O</td>
<td></td>
<td>0214</td>
<td>00719</td>
<td>Special Program Code</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>19</td>
<td>1</td>
<td>ID</td>
<td>O</td>
<td></td>
<td>0136</td>
<td>00720</td>
<td>Retention Indicator</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>20</td>
<td>1</td>
<td>NM</td>
<td>O</td>
<td></td>
<td></td>
<td>00721</td>
<td>Expected Number of Insurance Plans</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>21</td>
<td>1</td>
<td>IS</td>
<td>O</td>
<td></td>
<td>0215</td>
<td>00722</td>
<td>Visit Publicity Code</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>22</td>
<td>1</td>
<td>ID</td>
<td>O</td>
<td>Y</td>
<td>0136</td>
<td>00723</td>
<td>Visit Protection Indicator</td>
<td>Visit Protection Indicator.</td>
</tr>
<tr class="odd">
<td>23</td>
<td>250</td>
<td>XON</td>
<td>O</td>
<td></td>
<td></td>
<td>00724</td>
<td>Clinic Organization Name</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>24</td>
<td>2</td>
<td>IS</td>
<td>O</td>
<td></td>
<td>0216</td>
<td>00725</td>
<td>Patient Status Code</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>25</td>
<td>1</td>
<td>IS</td>
<td>O</td>
<td></td>
<td>0217</td>
<td>00726</td>
<td>Visit Priority Code</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>26</td>
<td>8</td>
<td>DT</td>
<td>O</td>
<td></td>
<td></td>
<td>00727</td>
<td>Previous Treatment Date</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>27</td>
<td>2</td>
<td>IS</td>
<td>O</td>
<td></td>
<td>0112</td>
<td>00728</td>
<td>Expected Discharge Disposition</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>28</td>
<td>8</td>
<td>DT</td>
<td>O</td>
<td></td>
<td></td>
<td>00729</td>
<td>Signature on File Date</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>29</td>
<td>8</td>
<td>DT</td>
<td>O</td>
<td></td>
<td></td>
<td>00730</td>
<td>First Similar Illness Date</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>30</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td></td>
<td>0218</td>
<td>00731</td>
<td>Patient Charge Adjustment Code</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>31</td>
<td>2</td>
<td>IS</td>
<td>O</td>
<td></td>
<td>0219</td>
<td>00732</td>
<td>Recurring Service Code</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>32</td>
<td>1</td>
<td>ID</td>
<td>O</td>
<td></td>
<td>0136</td>
<td>00733</td>
<td>Billing Media Code</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>33</td>
<td>26</td>
<td>TS</td>
<td>O</td>
<td></td>
<td></td>
<td>00734</td>
<td>Expected Surgery Date and Time</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>34</td>
<td>1</td>
<td>ID</td>
<td>O</td>
<td></td>
<td>0136</td>
<td>00735</td>
<td>Military Partnership Code</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>35</td>
<td>1</td>
<td>ID</td>
<td>O</td>
<td></td>
<td>0136</td>
<td>00736</td>
<td>Military Non-Availability Code</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>36</td>
<td>1</td>
<td>ID</td>
<td>O</td>
<td></td>
<td>0136</td>
<td>00737</td>
<td>Newborn Baby Indicator</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>37</td>
<td>1</td>
<td>ID</td>
<td>O</td>
<td></td>
<td>0136</td>
<td>00738</td>
<td>Baby Detained Indicator</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>38</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td></td>
<td>0430</td>
<td>01543</td>
<td>Mode of Arrival Code</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>39</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td>Y</td>
<td>0431</td>
<td>01544</td>
<td>Recreational Drug Use Code</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>40</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td></td>
<td>0432</td>
<td>01545</td>
<td>Admission Level of Care Code</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>41</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td>Y</td>
<td>0433</td>
<td>01546</td>
<td>Precaution Code</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>42</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td></td>
<td>0434</td>
<td>01547</td>
<td>Patient Condition Code</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>43</td>
<td>2</td>
<td>IS</td>
<td>O</td>
<td></td>
<td>0315</td>
<td>00759</td>
<td>Living Will Code</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>44</td>
<td>2</td>
<td>IS</td>
<td>O</td>
<td></td>
<td>0316</td>
<td>00760</td>
<td>Organ Donor Code</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>45</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td>Y</td>
<td>0435</td>
<td>01548</td>
<td>Advance Directive Code</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>46</td>
<td>8</td>
<td>DT</td>
<td>O</td>
<td></td>
<td></td>
<td>01549</td>
<td>Patient Status Effective Date</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>47</td>
<td>26</td>
<td>TS</td>
<td>C</td>
<td></td>
<td></td>
<td>01550</td>
<td>Expected LOA Return Date/Time</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>48</td>
<td>26</td>
<td>TS</td>
<td>O</td>
<td></td>
<td></td>
<td>01841</td>
<td>Expected Pre-admission Testing Date/Time</td>
<td>Not used.</td>
</tr>
</tbody>
</table>

<span id="_Ref58234023" class="anchor"></span>Table 36: DG1—Diagnosis Information Segment

### DG1—Diagnosis Information Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Ref58234114" class="anchor"></span>Table 37: PR1—Procedure Information Segment</p></caption>
<colgroup>
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 20%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th>SEQ</th>
<th>LEN</th>
<th>DT</th>
<th>R/O</th>
<th>RP/#</th>
<th>TBL#</th>
<th>Element Name</th>
<th>VistA Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>4</td>
<td>SI</td>
<td>R</td>
<td></td>
<td></td>
<td>Set ID ‑ Diagnosis</td>
<td>Sequential Number.</td>
</tr>
<tr class="even">
<td>2</td>
<td>2</td>
<td>ID</td>
<td>R</td>
<td></td>
<td>0053</td>
<td>Diagnosis Coding Method</td>
<td><p>I9 = ICD-9-CM</p>
<p>I10 = ICD-10-CM</p></td>
</tr>
<tr class="odd">
<td>3</td>
<td>8</td>
<td>ID</td>
<td></td>
<td></td>
<td>0051</td>
<td>Diagnosis Code</td>
<td><p>Diagnosis code from OUTPATIENT DIAGNOSIS (#409.43) and ICD DIAGNOSIS (#80) files.</p>
<p><strong>REF:</strong> See <a href="#_Ref58237521">Table 0051—Diagnosis Code (User Defined)</a> for sample listing of possible values.</p></td>
</tr>
<tr class="even">
<td>4</td>
<td>40</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Diagnosis Description</td>
<td><p>Corresponding diagnosis description from ICD DIAGNOSIS (#80) file.</p>
<p><strong>REF:</strong> See <a href="#_Ref58237521">Table 0051—Diagnosis Code (User Defined)</a> for sample listing of possible values.</p></td>
</tr>
<tr class="odd">
<td>5</td>
<td>26</td>
<td>TS</td>
<td></td>
<td></td>
<td></td>
<td>Diagnosis Date/Time</td>
<td>Date/time of encounter.</td>
</tr>
<tr class="even">
<td>6</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td>0052</td>
<td>Diagnosis Type</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>7</td>
<td>60</td>
<td>CE</td>
<td></td>
<td></td>
<td>0118</td>
<td>Major Diagnostic Category</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>8</td>
<td>4</td>
<td>ID</td>
<td></td>
<td></td>
<td>0055</td>
<td>Diagnostic Related Group</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>9</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td>DRG Approval Indicator</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>10</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td>0056</td>
<td>DRG Grouper Review Code</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>11</td>
<td>60</td>
<td>CE</td>
<td></td>
<td></td>
<td>0083</td>
<td>Outlier Type</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>12</td>
<td>3</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Outlier Days</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>13</td>
<td>12</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Outlier Cost</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>14</td>
<td>4</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Grouper Version And Type</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>15</td>
<td>2</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Diagnosis Priority</td>
<td>Contains <strong>1</strong> if this is the primary diagnosis for the episode.</td>
</tr>
<tr class="even">
<td>16</td>
<td>60</td>
<td>CN</td>
<td></td>
<td></td>
<td></td>
<td>Diagnosing Clinician</td>
<td>Not used.</td>
</tr>
</tbody>
</table>

<span id="_Ref58234114" class="anchor"></span>Table 37: PR1—Procedure Information Segment

### PR1—Procedure Information Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Ref58234153" class="anchor"></span>Table 38: ROL—Role Segment</p></caption>
<colgroup>
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 20%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th>SEQ</th>
<th>LEN</th>
<th>DT</th>
<th>R/O</th>
<th>RP/#</th>
<th>TBL#</th>
<th>Element Name</th>
<th>VistA Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>4</td>
<td>SI</td>
<td>R</td>
<td></td>
<td></td>
<td>Set ID - Procedure</td>
<td>Sequential Number.</td>
</tr>
<tr class="even">
<td>2</td>
<td>2</td>
<td>ID</td>
<td>R</td>
<td></td>
<td>0089</td>
<td>Procedure Coding Method</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>80</td>
<td>CE</td>
<td>R</td>
<td></td>
<td>0088</td>
<td>Procedure Code</td>
<td><p>Three Components:</p>
<ul>
<li><p>1. Procedure Code.</p></li>
<li><p>2. Corresponding procedure description from CPT (#81) file.</p></li>
<li><p>3. Coding Method (this is always <strong>C4</strong>).</p></li>
</ul>
<p><strong>REF:</strong> See <a href="#_Ref58237746">Table 0088—Procedure Code (User Defined)</a> for sample listing of possible procedure codes and descriptions.</p></td>
</tr>
<tr class="even">
<td>4</td>
<td>40</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Procedure Description</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>5</td>
<td>26</td>
<td>TS</td>
<td></td>
<td></td>
<td></td>
<td>Procedure Date/Time</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>6</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td>0090</td>
<td>Procedure Type</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>7</td>
<td>4</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Procedure Minutes</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>8</td>
<td>60</td>
<td>CN</td>
<td></td>
<td></td>
<td></td>
<td>Anesthesiologist</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>9</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td>0019</td>
<td>Anesthesia Code</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>10</td>
<td>4</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Anesthesia Minutes</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>11</td>
<td>60</td>
<td>CN</td>
<td></td>
<td></td>
<td></td>
<td>Surgeon</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>12</td>
<td>60</td>
<td>CM</td>
<td></td>
<td>Y</td>
<td></td>
<td>Procedure Practitioner</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>13</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td>0059</td>
<td>Consent Code</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>14</td>
<td>2</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Procedure Priority</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>15</td>
<td>80</td>
<td>CD</td>
<td></td>
<td></td>
<td></td>
<td>Associated Diagnosis Code</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>16</td>
<td>80</td>
<td>CE</td>
<td></td>
<td>Y</td>
<td>0340</td>
<td>Procedure Code Modifier</td>
<td><p>Three Components:</p>
<ul>
<li><p>1. Modifier Code.</p></li>
<li><p>2. Corresponding modifier description from CPT MODIFIER (#81.3) file.</p></li>
<li><p>3. Coding Method:</p></li>
</ul>
<ul>
<li><p><strong>C</strong>—CPT</p></li>
<li><p><strong>H</strong>—HCPCS</p></li>
</ul>
<p><strong>REF:</strong> See Table 0340 for sample listing of possible modifier codes and descriptions.</p></td>
</tr>
</tbody>
</table>

<span id="_Ref58234153" class="anchor"></span>Table 38: ROL—Role Segment

### ROL—Role Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Ref58234199" class="anchor"></span>Table 39: ZPD—VA-Specific Patient Information Segment</p></caption>
<colgroup>
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 17%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr class="header">
<th>SEQ</th>
<th>LEN</th>
<th>DT</th>
<th>R/O</th>
<th>RP/#</th>
<th>TBL#</th>
<th>Element Name</th>
<th>VistA Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>60</td>
<td>EI</td>
<td>R</td>
<td></td>
<td></td>
<td>Role Instance ID</td>
<td><p>Four Components:</p>
<ul>
<li><p>Entity Identifier5F<a href="#fn1" class="footnote-ref" id="fnref1" role="doc-noteref"><sup>1</sup></a> 6F<a href="#fn2" class="footnote-ref" id="fnref2" role="doc-noteref"><sup>2</sup></a>.</p></li>
<li><p>Not used.</p></li>
<li><p>Not used.</p></li>
<li><p>Not used.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>2</td>
<td>2</td>
<td>ID</td>
<td>R</td>
<td></td>
<td>0287</td>
<td>Action Code</td>
<td>This is always be <strong>CO</strong> (correct).</td>
</tr>
<tr class="odd">
<td>3</td>
<td>80</td>
<td>CE</td>
<td>R</td>
<td></td>
<td></td>
<td>Role</td>
<td><p>Six Components:</p>
<ul>
<li><p>Provider Type Code.</p></li>
<li><p>Not used.</p></li>
<li><p>This is always <strong>VA8932.1</strong> (PERSON CLASS file).</p></li>
<li><p>Primary Encounter Provider Designation.</p></li>
<li><p>Not used.</p></li>
<li><p>This is always <strong>VA01</strong>.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>4</td>
<td>80</td>
<td>XCN</td>
<td>R</td>
<td>Y/2</td>
<td></td>
<td>Role Person</td>
<td><p>14 Components:</p>
<p><strong>Repetition 1:</strong></p>
<p>2 Sub-Components:</p>
<ul>
<li><p>Pointer to entry in NEW PERSON (#200) file.</p></li>
<li><p>Facility Number.</p></li>
<li><p>Not used.</p></li>
<li><p>Not used.</p></li>
<li><p>Not used.</p></li>
<li><p>Not used.</p></li>
<li><p>Not used.</p></li>
<li><p>Not used.</p></li>
<li><p>This is always <strong>VA200</strong> (NEW PERSON file).</p></li>
<li><p>Not used.</p></li>
<li><p>Not used.</p></li>
<li><p>Not used.</p></li>
<li><p>Not used.</p></li>
<li><p>Not used.</p></li>
<li><p>Not used.</p></li>
</ul>
<p><strong>Repetition 2:</strong></p>
<ul>
<li><p>SSN.</p></li>
<li><p>Not used.</p></li>
<li><p>Not used.</p></li>
<li><p>Not used.</p></li>
<li><p>Not used.</p></li>
<li><p>Not used.</p></li>
<li><p>Not used.</p></li>
<li><p>This is always <strong>SSA</strong> (Social Security Administration).</p></li>
<li><p>Not used.</p></li>
<li><p>Not used.</p></li>
<li><p>Not used.</p></li>
<li><p>Not used.</p></li>
<li><p>Not used.</p></li>
<li><p>Not used.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>5</td>
<td>26</td>
<td>TS</td>
<td>O</td>
<td></td>
<td></td>
<td>Role Begin Date/Time</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>6</td>
<td>26</td>
<td>TS</td>
<td>O</td>
<td></td>
<td></td>
<td>Role End Date/Time</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>7</td>
<td>80</td>
<td>CE</td>
<td>O</td>
<td></td>
<td></td>
<td>Role Duration</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>8</td>
<td>80</td>
<td>CE</td>
<td>O</td>
<td></td>
<td></td>
<td>Role Action Reason</td>
<td>Not used.</td>
</tr>
</tbody>
</table>
<aside id="footnotes" class="footnotes footnotes-end-of-document" role="doc-endnotes">
<hr />
<ol>
<li id="fn1"><p>This element is <strong>1-15</strong> characters/digits followed by a hyphen (<strong>-</strong>) followed by <strong>3</strong> characters/digits followed by a hyphen (<strong>-</strong>) followed by <strong>1-15</strong> digits followed by an asterisk (<strong>*</strong>) followed by <strong>1-4</strong> digits. (Ex: 123AZ-ALB-1934*1).<a href="#fnref1" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
<li id="fn2"><p>The trailing set of digits (i.e., everything to the right of the asterisk) are an appended Set ID and should be treated as such.<a href="#fnref2" class="footnote-back" role="doc-backlink">↩︎</a></p></li>
</ol>
</aside>

<span id="_Ref58234199" class="anchor"></span>Table 39: ZPD—VA-Specific Patient Information Segment

### ZPD—VA-Specific Patient Information Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| SEQ | LEN | DT  | R/O | RP/# | TBL#   | VistA Element Name                    |
|-----|-----|-----|-----|------|--------|---------------------------------------|
| 1   | 4   | SI  | R   |      |        | SET ID - PATIENT ID                   |
| 2   | 60  | ST  |     |      |        | REMARKS                               |
| 3   | 20  | ST  |     |      |        | PLACE OF BIRTH CITY                   |
| 4   | 2   | ST  |     |      |        | PLACE OF BIRTH STATE                  |
| 5   | 2   | ID  |     |      | VA02   | CURRENT MEANS TEST STATUS             |
| 6   | 35  | ST  |     |      |        | FATHER'S NAME                         |
| 7   | 35  | ST  |     |      |        | MOTHER'S NAME                         |
| 8   | 1   | ID  |     |      | VA01   | RATED INCOMPETENT                     |
| 9   | 19  | TS  |     |      |        | DATE OF DEATH                         |
| 10  | 48  | PN  |     |      |        | COLLATERAL SPONSOR                    |
| 11  | 1   | ID  |     |      | VA01   | ACTIVE HEALTH INSURANCE?              |
| 12  | 1   | ID  |     |      | VA01   | COVERED BY MEDICAID?                  |
| 13  | 19  | TS  |     |      |        | DATE MEDICAID LAST ASKED              |
| 14  | 1   | ID  |     |      | VA07   | RACE7F[^3]                            |
| 15  | 3   | ID  |     |      | VA08   | RELIGION8F[^4]                        |
| 16  | 1   | ID  |     |      | VA01   | HOMELESS INDICATOR                    |
| 17  | 1   | ID  |     |      |        | POW STATUS INDICATED?                 |
| 18  | 2   | ID  |     |      | VA12   | TYPE OF INSURANCE                     |
| 19  | 1   | ID  |     |      | VA14   | MEDICATION COPAYMENT EXEMPTION STATUS |
| 20  | 1   | ID  |     |      | VA0023 | PRISONER OF WAR LOCATION CODE         |
| 21  | 30  | ST  |     |      |        | PRIMARY CARE TEAM                     |

<span id="_Ref58234243" class="anchor"></span>Table 40: ZEL—VA-Specific Patient Eligibility Segment

### ZEL—VA-Specific Patient Eligibility Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| SEQ | LEN | DT  | R/O | RP/# | TBL#   | VistA Element Name                             |
|-----|-----|-----|-----|------|--------|------------------------------------------------|
| 1   | 4   | SI  | R   |      |        | SET ID                                         |
| 2   | 2   | ID  |     |      | VA04   | ELIGIBILITY CODE                               |
| 3   | 16  | CK  |     |      |        | LONG ID                                        |
| 4   | 12  | ST  |     |      |        | SHORT ID                                       |
| 5   | 1   | ID  |     |      | VA05   | DISABILITY RETIREMENT FROM MIL.                |
| 6   | 8   | NM  |     |      |        | CLAIM FOLDER NUMBER                            |
| 7   | 40  | ST  |     |      |        | CLAIM FOLDER LOCATION                          |
| 8   | 1   | ID  |     |      | VA01   | VETERAN?                                       |
| 9   | 30  | ST  |     |      |        | TYPE OF PATIENT                                |
| 10  | 1   | ID  |     |      | VA06   | ELIGIBILITY STATUS                             |
| 11  | 8   | DT  |     |      |        | ELIGIBILITY STATUS DATE                        |
| 12  | 8   | DT  |     |      |        | ELIGIBILITY INTERIM RESPONSE                   |
| 13  | 50  | ST  |     |      |        | ELIGIBILITY VERIFICATION METHOD                |
| 14  | 1   | ID  |     |      | VA01   | RECEIVING A&A BENEFITS?                        |
| 15  | 1   | ID  |     |      | VA01   | RECEIVING HOUSEBOUND BENEFITS?                 |
| 16  | 1   | ID  |     |      | VA01   | RECEIVING A VA PENSION?                        |
| 17  | 1   | ID  |     |      | VA01   | RECEIVING A VA DISABILITY?                     |
| 18  | 1   | ID  |     |      | VA01   | EXPOSED TO AGENT ORANGE                        |
| 19  | 1   | ID  |     |      | VA01   | RADIATION EXPOSURE INDICATED?                  |
| 20  | 1   | ID  |     |      | VA01   | SW ASIA CONDITIONS?                            |
| 21  | 5   | NM  |     |      |        | TOTAL ANNUAL VA CHECK AMOUNT                   |
| 22  | 1   | ID  |     |      | VA0022 | RADIATION EXPOSURE METHOD CODE                 |
| 23  | 1   | ID  |     |      | VA0036 | MILITARY SEXUAL TRAUMA STATUS                  |
| 24  | 8   | DT  |     |      |        | DATE MILITARY SEXUAL TRAUMA STATUS CHANGED     |
| 25  | 7   | ID  |     |      | VA0115 | SITE DETERMINING MST STATUS                    |
| 26  | 8   | DT  |     |      |        | AGENT ORANGE REGISTRATION DATE                 |
| 27  | 8   | DT  |     |      |        | AGENT ORANGE EXAM DATE                         |
| 28  | 6   | NM  |     |      |        | AGENT ORANGE REGISTRATION \#                   |
| 29  | 1   | ID  |     |      | VA0046 | AGENT ORANGE EXPOSURE LOCATION                 |
| 30  | 8   | DT  |     |      |        | RADIATION REGISTRATION DATE                    |
| 31  | 8   | DT  |     |      |        | SW ASIA COND EXAM DATE                         |
| 32  | 8   | DT  |     |      |        | SW ASIA COND REGISTRATION DATE                 |
| 33  | 8   | DT  |     |      |        | MONETARY BEN. VERIFY DATE                      |
| 34  | 8   | DT  |     |      |        | USER ENROLLEE VALID THROUGH                    |
| 35  |     |     |     |      |        | USER ENROLLEE SITE                             |
| 36  |     |     |     |      |        | ELIGIBILITY VERIFICATION SOURCE AND SITE       |
| 37  | 1   | ID  |     |      | VA01   | COMBAT VETERAN                                 |
| 38  | 8   | DT  |     |      |        | COMBAT VETERAN STATUS END DATE                 |
| 39  | 1   | ID  |     |      | VA01   | DISCHARGE DUE TO DISABILITY?                   |
| 40  | 1   | ID  |     |      | VA01   | PROJECT 112/SHAD?                              |
| 48  | 1   | ID  |     |      | VA01   | TOXIC EXPOSURE RISK ACTIVITY (TERA) INDICATOR? |

<span id="_Ref58234292" class="anchor"></span>Table 41: VA-Specific Income Segment

### VA-Specific Income Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| SEQ | LEN | DT  | R/O | RP/# | TBL# | VistA Element Name           |
|-----|-----|-----|-----|------|------|------------------------------|
| 1   | 4   | SI  | R   |      |      | SET ID                       |
| 2   | 1   | ID  |     |      | VA01 | MARRIED LAST CALENDAR YEAR   |
| 3   | 1   | ID  |     |      | VA01 | LIVED WITH PATIENT           |
| 4   | 8   | NM  |     |      |      | AMOUNT CONTRIBUTED TO SPOUSE |
| 5   | 1   | ID  |     |      | VA01 | DEPENDENT CHILDREN           |
| 6   | 1   | ID  |     |      | VA01 | INCAPABLE OF SELF-SUPPORT    |
| 7   | 1   | ID  |     |      | VA01 | CONTRIBUTED TO SUPPORT       |
| 8   | 1   | ID  |     |      | VA01 | CHILD HAD INCOME             |
| 9   | 1   | ID  |     |      | VA01 | INCOME AVAILABLE TO YOU      |
| 10  | 2   | NM  |     |      |      | NUMBER OF DEPENDENT CHILDREN |
| 11  | 2   | ST  |     |      |      | NUMBER OF DEPENDENTS         |
| 12  | 10  | NM  |     |      |      | PATIENT INCOME               |
| 13  | 2   | ID  |     |      | VA10 | MEANS TEST INDICATOR         |

<span id="_Ref58234381" class="anchor"></span>Table 42: ZCL—VA-Specific Outpatient Classification Segment

### ZCL—VA-Specific Outpatient Classification Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| SEQ | LEN | DT  | R/O | RP/# | TBL#  | VistA Element Name             |
|-----|-----|-----|-----|------|-------|--------------------------------|
| 1   | 4   | SI  | R   |      |       | SET ID                         |
| 2   | 2   | ID  | R   |      | SD008 | Outpatient Classification Type |
| 3   | 50  | ST  |     |      |       | Value                          |

<span id="_Ref58234423" class="anchor"></span>Table 43: ZSC—VA-Specific Stop Code Segment

### ZSC—VA-Specific Stop Code Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| SEQ | LEN | DT  | R/O | RP/# | TBL#  | VistA Element Name                |
|-----|-----|-----|-----|------|-------|-----------------------------------|
| 1   | 4   | SI  | R   |      |       | Sequential number                 |
| 2   | 4   | ID  | R   |      | SD001 | Stop Code                         |
| 3   | 30  | ST  |     |      | SD001 | Name                              |
| 4   | 1   | NM  |     |      |       | Cost Distribution Center          |
| 5   | 1   | ID  |     |      |       | Current Exempt. Fr Classification |

<span id="_Ref58234463" class="anchor"></span>Table 44: ZSP—VA-Specific Service Period Segment

### ZSP—VA-Specific Service Period Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| SEQ | LEN | DT  | R/O | RP/# | TBL# | VistA Element Name           |
|-----|-----|-----|-----|------|------|------------------------------|
| 1   | 4   | SI  | R   |      |      | SET ID                       |
| 2   | 1   | ID  | R   |      | VA01 | Service Connected?           |
| 3   | 3   | NM  |     |      |      | Service Connected Percentage |
| 4   | 2   | ID  |     |      | VA11 | Period of Service            |
| 5   | 1   | ST  |     |      |      | VIETNAM SERVICE INDICATED?   |
| 6   | 1   | ID  |     |      | VA01 | P&T                          |
| 7   | 1   | ID  |     |      | VA01 | UNEMPLOYABLE                 |
| 8   | 19  | TS  |     |      |      | SC AWARD DATE                |

<span id="_Ref58235298" class="anchor"></span>Table 45: ZEN—VA-Specific Enrollment Segment

### ZEN—VA-Specific Enrollment Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Toc193958073" class="anchor"></span>Table 46: A08 Codes and Descriptions</p></caption>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 12%" />
<col style="width: 48%" />
</colgroup>
<thead>
<tr class="header">
<th>SEQ</th>
<th>LEN</th>
<th>DT</th>
<th>R/O</th>
<th>RP/#</th>
<th>TBL#</th>
<th>VistA Element Name</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>4</td>
<td>SI</td>
<td>R</td>
<td></td>
<td></td>
<td>SET ID</td>
</tr>
<tr class="even">
<td>2</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>ENROLLMENT DATE</td>
</tr>
<tr class="odd">
<td>3</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td>VA0024</td>
<td>SOURCE OF ENROLLMENT</td>
</tr>
<tr class="even">
<td>4</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td>VA0015</td>
<td>ENROLLMENT STATUS</td>
</tr>
<tr class="odd">
<td>5</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td>VA0016</td>
<td>REASON CANCELED/DECLINED</td>
</tr>
<tr class="even">
<td>6</td>
<td>60</td>
<td>TX</td>
<td></td>
<td></td>
<td></td>
<td>CANCELED/DECLINED REMARKS</td>
</tr>
<tr class="odd">
<td>7</td>
<td>7</td>
<td>ID</td>
<td></td>
<td></td>
<td>VA0115</td>
<td>FACILITY RECEIVED</td>
</tr>
<tr class="even">
<td>8</td>
<td>7</td>
<td>ID</td>
<td></td>
<td></td>
<td>VA0115</td>
<td>PRIMARY FACILITY</td>
</tr>
<tr class="odd">
<td>9</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td>VA0021</td>
<td>ENROLLMENT PRIORITY</td>
</tr>
<tr class="even">
<td>10</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>EFFECTIVE DATE</td>
</tr>
<tr class="odd">
<td>11</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>APPLICATION DATE</td>
</tr>
<tr class="even">
<td>12</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>ENROLLMENT END DATE</td>
</tr>
<tr class="odd">
<td>13</td>
<td>1</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA035</td>
<td>ENROLLMENT SUB-GROUP</td>
</tr>
<tr class="even">
<td>14</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td><p>SOURCE DESIGNATION</p>
<p>V=VISTA, E = ESR, PA = PCP Active, PI = PCP Inactive</p></td>
</tr>
<tr class="odd">
<td>15</td>
<td>1</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA117</td>
<td>REASON FOR CLOSED APPLICATION</td>
</tr>
<tr class="even">
<td>16</td>
<td>1</td>
<td>IS</td>
<td></td>
<td></td>
<td>VA001</td>
<td><p>PT APPLIED FOR ENROLLMENT?</p>
<p>0 – No</p>
<p>1 - Yes</p></td>
</tr>
<tr class="odd">
<td>17</td>
<td>1</td>
<td>IS</td>
<td></td>
<td></td>
<td></td>
<td><p>REGISTRATION ONLY REASON</p>
<p>‘1’ - C&amp;P DISABILITY BENEFITS EXAM</p>
<p>‘2’ - ACTIVE DUTY</p>
<p>‘3’ - SERVICE CONNECTED ONLY</p>
<p>‘4’ - EXPOSURE REGISTRY EXAM</p>
<p>‘5’ - RESEARCH</p>
<p>‘6’ - HUMANITARIAN/EMERGENCY</p>
<p>‘7’ - EMPLOYEE</p>
<p>‘8’ - BENEFICIARY</p>
<p>‘9’ - OTHER THAN HONORABLE (OTH)</p>
<p>‘10’ - MARRIAGE/FAMILY COUNSELING</p>
<p>‘11’ - COLLATERAL (OTHER)</p>
<p>‘12’ - ART/IVF</p>
<p>‘13’ - NEWBORN</p>
<p>‘14’ - LEGISLATIVE MANDATE</p>
<p>‘15’ - OTHER</p>
<p>‘16’ - NORTH CHICAGO ACTIVE DUTY</p>
<p>‘17’ - UNANSWERED</p>
<p>‘18’ - CAREGIVER</p>
<p>‘19’ - VHA TRANSPLANT PROGRAM</p></td>
</tr>
<tr class="even">
<td>18</td>
<td>8</td>
<td>DT</td>
<td></td>
<td></td>
<td></td>
<td>REGISTRATION ONLY DATE</td>
</tr>
<tr class="odd">
<td>19</td>
<td>8</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td><p>SOURCE OF REGISTRATION</p>
<p>Valid values:</p>
<p>‘1’ - ‘VAMC’</p>
<p>‘2’ - ‘HEC</p>
<p>‘3’ - ‘HCA’</p>
<p>‘4’ – CARMA</p>
<p>‘5’ - OTHER</p></td>
</tr>
</tbody>
</table>

<span id="_Toc193958073" class="anchor"></span>Table 46: A08 Codes and Descriptions

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section defines the HL7 message transactions that are necessary to support the outpatient database interface for the Austin Information Technology Center (AITC), (formerly the Austin Automation Center \[AAC\]).

These messages uses the generic HL7 format, so that they can be expanded later to support new interfaces at other facilities.

## Trigger Events and Message Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each triggering event is listed below, along with the applicable form of the message to be exchanged. The notation used to describe the sequence, optionally, and repetition of segments is described in the HL7 Final Standard Manual, Chapter 2, Section 2.4.8, Chapter Formats for Defining Abstract Messages, and in summary form, in Section [2.1](#eligibility-idmaintenance-menu).

### Update Patient Information (A08)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Outpatient Event Driver is triggered under the following circumstances:

- When an outpatient appointment is checked out.
- When a checked out outpatient appointment is edited.
- When stop codes for an outpatient appointment are added or edited.
- When a check out creates an occasion of service.

Taking advantage of the outpatient event driver, this triggers an A08 message to be sent. The receiving system replaces any data that exists with the “new” data that is transmitted with this message.

| Code          | Description                                 |
|---------------|---------------------------------------------|
| ADT           | ADT Message                             |
| MSH           | Message Header                              |
| EVN           | Event Type                                  |
| PID           | Patient Identification                      |
| PD1           | Patient Additional Demographic              |
| PV1           | Patient Visit                               |
| PV2           | Patient Visit Additional Information        |
| \[ { DG1 } \] | Diagnosis Information                       |
| { PR1 }       | Procedure Information                       |
| {ROL}         | Role                                        |
| ZPD           | VA-Specific Patient Information             |
| ZEL           | VA-Specific Patient Eligibility Information |
| ZIR           | VA-Specific Income                          |
| {ZCL}         | VA-Specific Outpatient Classification       |
| {ZSC}         | VA-Specific Stop Code                       |
| ZSP           | VA-Specific Service Period                  |
| ZEN           | VA-Specific Enrollment                      |
| ACK           | General Acknowledgment Message              |
| MSH           | Message Header                              |
| MSA           | Message Acknowledgment                      |

<span id="_Toc193958074" class="anchor"></span>Table 47: A23 Codes and Descriptions

### Delete a Patient Record (A23)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a check out is deleted, this message instructs the receiver to delete the information for this patient’s visit.

| Code | Description                     |
|------|---------------------------------|
| ADT  | ADT Message                 |
| MSH  | Message Header                  |
| EVN  | Event Type                      |
| PID  | Patient Identification          |
| PD1  | Patient Additional Demographic  |
| PV1  | Patient Visit                   |
| ZPD  | VA-Specific Patient Information |
| ACK  | General Acknowledgment Message  |
| MSH  | Message Header                  |
| MSA  | Message Acknowledgment          |

<span id="_Ref58237283" class="anchor"></span>Table 48: Table 0001—Sex

## Supported and User-Defined HL7 Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Table 0001—Sex

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Value | Description |
|-------|-------------|
| F     | FEMALE      |
| M     | MALE        |
| O     | OTHER       |
| U     | UNKNOWN     |

<span id="_Ref58237358" class="anchor"></span>Table 49: Table 0002—Marital Status

### Table 0002—Marital Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Value | Description |
|-------|-------------|
| A     | SEPARATED   |
| D     | DIVORCED    |
| M     | MARRIED     |
| S     | SINGLE      |
| W     | WIDOWED     |

<span id="_Ref58237406" class="anchor"></span>Table 50: Table 0003—Event Type Code

### Table 0003—Event Type Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Value | Description                |
|-------|----------------------------|
| A08   | UPDATE PATIENT INFORMATION |
| A23   | DELETE PATIENT RECORD      |

<span id="_Ref58237468" class="anchor"></span>Table 51: Table 0008—Acknowledgment Code

### Table 0008—Acknowledgment Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Value | Description                          |
|-------|--------------------------------------|
| AA    | APPLICATION ACKNOWLEDGMENT: ACCEPT   |
| AE    | APPLICATION ACKNOWLEDGMENT: ERROR    |
| AR    | APPLICATION ACKNOWLEDGMENT: REJECT   |
| CA    | ACCEPT ACKNOWLEDGMENT: COMMIT ACCEPT |
| CE    | ACCEPT ACKNOWLEDGMENT: COMMIT ERROR  |
| CR    | ACCEPT ACKNOWLEDGMENT: COMMIT REJECT |

<span id="_Ref58237220" class="anchor"></span>Table 52: Table 0023—Admit Source (User Defined)

### Table 0023—Admit Source (User Defined)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Used for Location of Visit.

| Value | Description    |
|-------|----------------|
| 1     | THIS FACILITY  |
| 6     | OTHER FACILITY |

<span id="_Ref58237521" class="anchor"></span>Table 53: Table 0051—Diagnosis Code (User Defined)

### Table 0051—Diagnosis Code (User Defined)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use ICD DIAGNOSIS (#80) file, CODE NUMBER (#.01) for value and DIAGNOSIS (#3) for Description.

| Value | Description              |
|-------|--------------------------|
| 253.2 | PANHYPOPITUITARISM       |
| 253.3 | PITUITARY DWARFISM       |
| 253.4 | ANTER PITUITARY DIS NEC  |
| 253.5 | DIABETES INSIPIDUS       |
| 253.6 | NEUROHYPOPHYSIS DIS NEC  |
| 253.7 | IATROGENIC PITUITARY DIS |
| 253.8 | DISEASES OF THYMUS NEC   |
| 253.9 | PITUITARY DISORDER NOS   |
| 254.1 | ABSCESS OF THYMUS        |
| 254.8 | DISEASES OF THYMUS NEC   |
| 254.9 | DISEASE OF THYMUS NOS    |
| 255.1 | HYPERALDOSTERONISM       |
| 255.2 | ADRENOGENITAL DISORDERS  |

<span id="_Ref58237565" class="anchor"></span>Table 54: Table 0069—Hospital Service (User Defined)

### Table 0069—Hospital Service (User Defined)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use SPECIALTY (#42.4) file, PTF Code (#.001).

| Value | Description            |
|-------|------------------------|
| 2     | CARDIOLOGY             |
| 6     | DERMATOLOGY            |
| 7     | ENDOCRINOLOGY          |
| 8     | GEM ACUTE MEDICINE     |
| 12    | CORONARY CARE UNIT     |
| 12    | EMERGENCY MEDICINE     |
| 15    | GENERAL MEDICINE       |
| 21    | BLIND REHAB            |
| 31    | GEM INTERMEDIATE CARE  |
| 55    | EVAL/BRF TRMT PTSD     |
| 72    | ALCOHOL                |
| 85    | DOM                    |
| 88    | DOMICILIARY PTSD       |
| 91    | GASTROENTEROLOGY       |
| 92    | GEN INTERMEDIATE PSYCH |

<span id="_Ref58237660" class="anchor"></span>Table 55: Table 0076—Message Type

### Table 0076—Message Type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Value   | Description            |
|---------|------------------------|
| ADT | ADT MESSAGE            |
| ACK | GENERAL ACKNOWLEDGMENT |

<span id="_Ref58237746" class="anchor"></span>Table 56: Table 0088—Procedure Code (User Defined)

### Table 0088—Procedure Code (User Defined)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Value | Description                                    |
|-------|------------------------------------------------|
| 10141 | INCISION AND DRAINAGE OF HEMATOMA; COMPLICATED |

<span id="_Ref58237823" class="anchor"></span>Table 57: Table 0115—Servicing Facility (User Defined)

### Table 0115—Servicing Facility (User Defined)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Value   | Description                |
|---------|----------------------------|
| 512 9AC | Perry Point (Nursing Home) |

<span id="_Ref58237888" class="anchor"></span>Table 58: Table 0133—Procedure Practitioner Type (User Defined)

### Table 0133—Procedure Practitioner Type (User Defined)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Value   | Occupation                              | Specialty              | Subspecialty            |
|---------|-----------------------------------------|------------------------|-------------------------|
| V110000 | Physicians (M.D.) and Osteopaths (D.O.) |                        |                         |
| V110100 | Physicians (M.D.) and Osteopaths (D.O.) | Addiction Medicine     |                         |
| V110300 | Physicians (M.D.) and Osteopaths (D.O.) | Allergy and Immunology |                         |
| V110301 | Physicians (M.D.) and Osteopaths (D.O.) | Allergy and Immunology | Clinical and Laboratory |
| V110200 | Physicians (M.D.) and Osteopaths (D.O.) | Allergy                |                         |
| V110400 | Physicians (M.D.) and Osteopaths (D.O.) | Anesthesiology         |                         |
| V110401 | Physicians (M.D.) and Osteopaths (D.O.) | Anesthesiology         | Critical Care           |
| V110402 | Physicians (M.D.) and Osteopaths (D.O.) | Anesthesiology         | Pain Management         |

<span id="_Ref58237945" class="anchor"></span>Table 59: Table 0136—Yes/No Indicator

### Table 0136—Yes/No Indicator

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Value | Description |
|-------|-------------|
| Y | YES         |
| N | NO          |

<span id="_Ref58238002" class="anchor"></span>Table 60: Table SD001—Service Indicator (Stop Code)

### Table SD001—Service Indicator (Stop Code)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Value | Description                    |
|-------|--------------------------------|
| 104   | PULMONARY FUNCTION             |
| 105   | X-RAY                          |
| 106   | EEG                            |
| 107   | EKG                            |
| 108   | LABORATORY                     |
| 109   | NUCLEAR MEDICINE               |
| 110   | CARDIOVASCULAR NUCLEAR MED     |
| 111   | ONCOLOGICAL NUCLEAR MED        |
| 112   | INFECTIOUS DISEASE NUCLEAR MED |
| 113   | RADIONUCLIDE TREATMENT         |
| 114   | SING PHOTON EMISS TOMOGRAPHY   |
| 115   | ULTRASOUND                     |
| 117   | NURSING                        |
| 118   | HOME TREATMENT SERVICES        |
| 119   | COMM NURSING HOME FOLLOW-UP    |

<span id="_Ref58238052" class="anchor"></span>Table 61: Table SD008—Outpatient Classification Type

### Table SD008—Outpatient Classification Type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Value | Description                                   |
|-------|-----------------------------------------------|
| 1     | AGENT ORANGE                                  |
| 2     | IONIZING RADIATION                            |
| 3     | SERVICE CONNECTED                             |
| 4     | SW ASIA CONDITIONS                            |
| 5     | MILITARY SEXUAL TRAUMA                        |
| 6     | HEAD AND/OR NECK CANCER                       |
| 7     | COMBAT VETERAN                                |
| 8     | PROJECT 112/SHAD                              |
| 9     | TOXIC EXPOSURE RISK ACTIVITY (TERA) INDICATOR |

<span id="_Ref58238120" class="anchor"></span>Table 62: Table SD009—Purpose of Visit

### Table SD009—Purpose of Visit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Value denotes a combination of Purpose of Visit & Appointment Type.

| Value | Purpose Of Visit | Appointment Type       |
|-------|------------------|------------------------|
| 0101  | C&P              | COMPENSATION & PENSION |
| 0102  | C&P              | CLASS II DENTAL        |
| 0103  | C&P              | ORGAN DONORS           |
| 0104  | C&P              | EMPLOYEE               |
| 0105  | C&P              | PRIMA FACIA            |
| 0106  | C&P              | RESEARCH               |
| 0107  | C&P              | COLLATERAL OF VET.     |
| 0108  | C&P              | SHARING AGREEMENT      |
| 0109  | C&P              | REGULAR                |
| 0111  | C&P              | SERVICE CONNECTED      |
| 0201  | 10-10            | COMPENSATION & PENSION |
| 0202  | 10-10            | CLASS II DENTAL        |
| 0203  | 10-10            | ORGAN DONORS           |
| 0204  | 10-10            | EMPLOYEE               |
| 0205  | 10-10            | PRIMA FACIA            |
| 0206  | 10-10            | RESEARCH               |
| 0207  | 10-10            | COLLATERAL OF VET.     |
| 0208  | 10-10            | SHARING AGREEMENT      |
| 0209  | 10-10            | REGULAR                |
| 0211  | 10-10            | SERVICE CONNECTED      |
| 0301  | SCHEDULED VISIT  | COMPENSATION & PENSION |
| 0302  | SCHEDULED VISIT  | CLASS II DENTAL        |
| 0303  | SCHEDULED VISIT  | ORGAN DONORS           |
| 0304  | SCHEDULED VISIT  | EMPLOYEE               |
| 0305  | SCHEDULED VISIT  | PRIMA FACIA            |
| 0306  | SCHEDULED VISIT  | RESEARCH               |
| 0307  | SCHEDULED VISIT  | COLLATERAL OF VET.     |
| 0308  | SCHEDULED VISIT  | SHARING AGREEMENT      |
| 0309  | SCHEDULED VISIT  | REGULAR                |
| 0311  | SCHEDULED VISIT  | SERVICE CONNECTED      |
| 0401  | UNSCHED. VISIT   | COMPENSATION & PENSION |
| 0402  | UNSCHED. VISIT   | CLASS II DENTAL        |
| 0403  | UNSCHED. VISIT   | ORGAN DONORS           |
| 0404  | UNSCHED. VISIT   | EMPLOYEE               |
| 0405  | UNSCHED. VISIT   | PRIMA FACIA            |
| 0406  | UNSCHED. VISIT   | RESEARCH               |
| 0407  | UNSCHED. VISIT   | COLLATERAL OF VET.     |
| 0408  | UNSCHED. VISIT   | SHARING AGREEMENT      |
| 0409  | UNSCHED. VISIT   | REGULAR                |
| 0411  | UNSCHED. VISIT   | SERVICE CONNECTED      |

<span id="_Ref58238196" class="anchor"></span>Table 63: Table VA01—Yes/No

### Table VA01—Yes/No

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Value | Description |
|-------|-------------|
| 0     | NO          |
| 1     | YES         |
| N     | NO          |
| Y     | YES         |
| U     | UNKNOWN     |

<span id="_Ref58238248" class="anchor"></span>Table 64: Table VA02—Current Means Test Status

### Table VA02—Current Means Test Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

TYPE OF CARE (#.03) field in the MEANS TEST STATUS (#408.32) file.

| Value | Description    |
|-------|----------------|
| D     | DISCRETIONARY  |
| M     | MANDATORY      |
| N     | NOT APPLICABLE |

<span id="_Ref58238341" class="anchor"></span>Table 65: Table VA04—Eligibility

### Table VA04—Eligibility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

NAME (#.01) field in the MAS ELIGIBILITY CODE (#8.1) file.

| Value | Description                    |
|-------|--------------------------------|
| 1     | SERVICE CONNECTED 50% to 100%  |
| 2     | AID & ATTENDANCE               |
| 3     | SC LESS THAN 50%               |
| 4     | NSC - VA PENSION               |
| 5     | NSC                            |
| 6     | OTHER FEDERAL AGENCY           |
| 7     | ALLIED VETERAN                 |
| 8     | HUMANITARIAN EMERGENCY         |
| 9     | SHARING AGREEMENT              |
| 10    | REIMBURSABLE INSURANCE         |
| 12    | CHAMPVA                        |
| 13    | COLLATERAL OF VET.             |
| 14    | EMPLOYEE                       |
| 15    | HOUSEBOUND                     |
| 16    | MEXICAN BORDER WAR             |
| 17    | WORLD WAR I                    |
| 18    | PRISONER OF WAR                |
| 19    | TRICARE/CHAMPUS                |
| 21    | CATASTROPHIC DISABILITY        |
| 22    | PURPLE HEART RECIPIENT         |
| 23    | EXPANDED MH CARE NON-ENROLLEE  |
| 24    | COMPACT ACT ELIGIBLE           |
| 25    | SPECIAL TX AUTHORITY CARE      |
| 26    | HUD-VASH                       |
| 27    | CLINICAL EVALUATION            |
| 28    | PRESUMPTIVE PSYCHOSIS ELIGIBLE |
| 29    | 29 WORLD WAR II                |

<span id="_Ref58238415" class="anchor"></span>Table 66: Table VA05—Disability Retirement from Military

### Table VA05—Disability Retirement from Military

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DISABILITY RET. FROM MILITARY? (#.362) field in the PATIENT (#2) file.

| Value | Description                                                   |
|-------|---------------------------------------------------------------|
| 0     | NO                                                            |
| 1     | YES, RECEIVING MILITARY RETIREMENT                            |
| 2     | YES, RECEIVING MILITARY RETIREMENT IN LIEU OF VA COMPENSATION |
| 3     | UNKNOWN                                                       |

<span id="_Ref58238468" class="anchor"></span>Table 67: Table VA06—Eligibility Status

### Table VA06—Eligibility Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ELIGIBILITY STATUS (#.3611) field in the PATIENT (#2) file.

| Value | Description             |
|-------|-------------------------|
| P     | PENDING VERIFICATION    |
| R     | PENDING RE-VERIFICATION |
| V     | VERIFIED                |

<span id="_Ref58238511" class="anchor"></span>Table 68: Table VA07—Race

### Table VA07—Race

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ABBREVIATION (#2) field in the RACE (#10) file.

| Value | Description                      |
|-------|----------------------------------|
| 1     | HISPANIC, WHITE                  |
| 2     | HISPANIC, BLACK                  |
| 3     | AMERICAN INDIAN OR ALASKA NATIVE |
| 4     | BLACK, NOT OF HISPANIC ORIGIN    |
| 5     | ASIAN OR PACIFIC ISLANDER        |
| 6     | WHITE, NOT OF HISPANIC ORIGIN    |
| 7     | UNKNOWN                          |

<span id="_Ref58238574" class="anchor"></span>Table 69: Table VA08—Religion

### Table VA08—Religion

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CODE (#3) field in the RELIGION (#13) file.

| Value | Description                   |
|-------|-------------------------------|
| 0     | ROMAN CATHOLIC CHURCH         |
| 1     | JUDAISM                       |
| 2     | EASTERN ORTHODOX              |
| 3     | BAPTIST                       |
| 4     | METHODIST                     |
| 5     | LUTHERAN                      |
| 6     | PRESBYTERIAN                  |
| 7     | UNITED CHURCH OF CHRIST       |
| 8     | EPISCOPALIAN                  |
| 9     | ADVENTIST                     |
| 10    | ASSEMBLY OF GOD               |
| 11    | BRETHREN                      |
| 12    | CHRISTIAN SCIENTIST           |
| 13    | CHURCH OF CHRIST              |
| 14    | CHURCH OF GOD                 |
| 15    | DISCIPLES OF CHRIST           |
| 16    | EVANGELICAL COVENANT          |
| 17    | FRIENDS                       |
| 18    | JEHOVAH'S WITNESSES           |
| 19    | LATTER DAY SAINTS             |
| 20    | ISLAM                         |
| 21    | NAZARENE                      |
| 22    | OTHER                         |
| 23    | PENTECOSTAL                   |
| 24    | PROTESTANT                    |
| 25    | PROTESTANT, NO DENOMINATION   |
| 26    | REFORMED                      |
| 27    | SALVATION ARMY                |
| 28    | UNITARIAN-UNIVERSALIST        |
| 29    | UNKNOWN/NO PREFERENCE         |
| 30    | NATIVE AMERICAN               |
| 31    | ZEN BUDDHISM                  |
| 32    | AFRICAN RELIGIONS             |
| 33    | AFRO-CARIBBEAN RELIGIONS      |
| 34    | AGNOSTICISM                   |
| 35    | ANGLICAN                      |
| 36    | ANIMISM                       |
| 37    | ATHEISM                       |
| 38    | BABI & BAHA’I FAITHS          |
| 39    | BON                           |
| 40    | CAO DAI                       |
| 41    | CELTICISM                     |
| 42    | CHRISTIAN (NON-SPECIFIC)      |
| 43    | CONFUCIANISM                  |
| 44    | CONGREGATIONAL                |
| 45    | CYBERCULTURE RELIGIONS        |
| 46    | DIVINATION                    |
| 47    | FOURTH WAY                    |
| 48    | FREE DAISM                    |
| 49    | FULL GOSPEL                   |
| 50    | GNOSIS                        |
| 51    | HINDUISM                      |
| 52    | HUMANISM                      |
| 53    | INDEPENDENT                   |
| 54    | JAINISM                       |
| 55    | MAHAYANA                      |
| 56    | MEDITATION                    |
| 57    | MESSIANIC JUDAISM             |
| 58    | MITRAISM                      |
| 59    | NEW AGE                       |
| 60    | NON-ROMAN CATHOLIC            |
| 61    | OCCULT                        |
| 62    | ORTHODOX                      |
| 63    | PAGANISM                      |
| 64    | PROCESS, THE                  |
| 65    | REFORMED/PRESBYTERIAN         |
| 66    | SATANISM                      |
| 67    | SCIENTOLOGY                   |
| 68    | SHAMANISM                     |
| 69    | SHIITE (ISLAM)                |
| 70    | SHINTO                        |
| 71    | SIKISM                        |
| 72    | SPIRITUALISM                  |
| 73    | SUNNI (ISLAM)                 |
| 74    | TAOISM                        |
| 75    | THERAVADA                     |
| 76    | UNIVERSAL LIFE CHURCH         |
| 77    | VAJRAYANA (TIBETAN)           |
| 78    | VEDA                          |
| 79    | VOODOO                        |
| 80    | WICCA                         |
| 81    | YAOHUSHUA                     |
| 82    | ZOROASTRIANISM                |
| 83    | ASKED BUT DECLINED TO ANSWER  |
| 84    | AFRICAN AMERICAN EPISCOPAL    |
| 85    | BUDDHISM, OTHER               |
| 86    | EVANGELICAL                   |
| 87    | HOLINESS CHURCHES             |
| 88    | CATHOLIC (NON-ROMAN CATHOLIC) |
| 89    | UNITARIAN-UNIVERSALISM        |

<span id="_Ref58238800" class="anchor"></span>Table 70: Table VA10—Means Test Indicator

### Table VA10—Means Test Indicator

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Ref58238866" class="anchor"></span>Table 71: Table VA11—Period of Service</p></caption>
<colgroup>
<col style="width: 10%" />
<col style="width: 89%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>AS</strong></td>
<td><p>This Means Test category includes all compensable service-connected (<strong>0-100%</strong>) Veterans and special category Veterans. Special category Veterans include:</p>
<ul>
<li><p>Mexican Border War and World War I Veterans</p></li>
<li><p>Former Prisoners of War</p></li>
<li><p>Patients receiving care for conditions potentially related to exposure to any of the following:</p></li>
</ul>
<ul>
<li><p>Agent Orange (Herbicides)</p></li>
<li><p>Ionizing Radiation</p></li>
<li><p>SW Asia Conditions</p></li>
</ul>
<p>This category also includes <strong>0%</strong> <em>non</em>-compensable service-connected Veterans when they are treated for a service-connected condition.</p></td>
</tr>
<tr class="even">
<td><strong>AN</strong></td>
<td><p>This Means Test category includes NSC Veterans who are required to complete VA Form 10-10F (Financial Worksheet) and those NSC Veterans in receipt of any of the following:</p>
<ul>
<li><p>VA pension</p></li>
<li><p>Aid and attendance</p></li>
<li><p>Housebound allowance</p></li>
<li><p>Entitled to State Medicaid</p></li>
</ul>
<p>This category may also include <strong>0%</strong> <em>non</em>-compensable service-connected Veterans when they are <em>not</em> treated for a service-connected condition and are placed in this category based on completion of a Means Test.</p></td>
</tr>
<tr class="odd">
<td><strong>C</strong></td>
<td>This Means Test category includes those Veterans who, based on income and/or net worth, are required to reimburse VA for care rendered. This category also includes those pending adjudication. This category may also include <strong>0%</strong> <em>non</em>-compensable service-connected Veterans when they are <em>not</em> treated for a service-connected condition and are placed in this category based on completion of a Means Test.</td>
</tr>
<tr class="even">
<td><strong>G</strong></td>
<td>This Means Test category includes Veterans whose income is less than or equal to the MT threshold and whose estate value is greater than or equal to the net worth threshold, or such Veterans whose income is greater than the MT threshold, but less than or equal to the GMT threshold, and whose estate value is less than the net worth threshold.</td>
</tr>
<tr class="odd">
<td><strong>N</strong></td>
<td>This Means Test category includes only <em>non</em>-Veterans receiving treatment at VA facilities.</td>
</tr>
<tr class="even">
<td><strong>X</strong></td>
<td>This Means Test category includes treatment of patients who are not required to complete the Means Test for the care being provided. If the Veteran was admitted prior to <strong>July 1, 1986</strong> with no change in the level of care being received, (i.e., if the patient was in the Nursing Home Care Unit (NHCU) on <strong>June 30, 1986</strong> and has remained in the NHCU since that date with no transfer to the hospital for treatment), the "<strong>X</strong>" Means Test indicator is accepted. This category also includes patients admitted to the domiciliary, patients seen for completion of a compensation and pension examination, and Class II dental treatment.</td>
</tr>
<tr class="odd">
<td><strong>U</strong></td>
<td>This Means Test category includes only those patients who require a Means Test, and the Means Test has <em>not</em> been done/completed. The National Patient Care Database does <em>not</em> accept the transaction unless the Means Test has been completed.</td>
</tr>
</tbody>
</table>

<span id="_Ref58238866" class="anchor"></span>Table 71: Table VA11—Period of Service

### Table VA11—Period of Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Value | Description                |
|-------|----------------------------|
| 0     | KOREAN                     |
| 1     | WORLD WAR I                |
| 2     | WORLD WAR II               |
| 3     | SPANISH AMERICAN           |
| 4     | PRE-KOREAN                 |
| 5     | POST-KOREAN                |
| 6     | OPERATION DESERT SHIELD    |
| 7     | VIETNAM ERA                |
| 8     | POST-VIETNAM               |
| 9     | OTHER OR NONE              |
| A     | ARMY - ACTIVE DUTY         |
| B     | NAVY, MARINE - ACTIVE DUTY |
| C     | USAF, USSF - ACTIVE DUTY   |
| D     | COAST GUARD - ACTIVE DUTY  |
| E     | RETIRED, UNIFORMED FORCES  |
| F     | MEDICAL REMEDIAL ENLIST    |
| G     | MERCHANT SEAMEN - USPHS    |
| H     | OTHER USPHS BENEFICIARIES  |
| I     | OBSERVATION/EXAMINATION    |
| J     | OFFICE OF WORKERS COMP     |
| K     | JOB CORPS/PEACE CORPS      |
| L     | RAILROAD RETIREMENT        |
| M     | BENEFICIARIES-FOREIGN GOV  |
| N     | HUMANITARIAN (NON-VET)     |
| O     | CHAMPUS RESTORE            |
| P     | OTHER REIMBURS. (NON-VET)  |
| Q     | OTHER FEDERAL - DEPENDENT  |
| R     | DONORS (NON-VET)           |
| S     | SPECIAL STUDIES (NON-VET)  |
| T     | OTHER NON-VETERANS         |
| U     | CHAMPVA - SPOUSE, CHILD    |
| V     | CHAMPUS                    |
| W     | CZECHOSLOVAKIA/POLAND SVC  |
| X     | PERSIAN GULF WAR           |
| Y     | CAV/NPS                    |
| Z     | MERCHANT MARINE            |

<span id="_Ref58238923" class="anchor"></span>Table 72: Table VA12—Type of Insurance

### Table VA12—Type of Insurance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Value | Description           |
|-------|-----------------------|
| 0     | NO INSURANCE          |
| 1     | MAJOR MEDICAL         |
| 2     | DENTAL                |
| 3     | HMO                   |
| 4     | PPO                   |
| 5     | MEDICARE              |
| 6     | MEDICAID              |
| 7     | CHAMPUS               |
| 8     | WORKMAN COMP          |
| 9     | INDEMNITY             |
| 10    | PRESCRIPTION          |
| 11    | MEDICARE SUPPLEMENTAL |
| 12    | ALL OTHER             |

<span id="_Ref58238970" class="anchor"></span>Table 73: Table VA0015—Enrollment Status

### Table VA0015—Enrollment Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Value | Description       |
|-------|-------------------|
| 1     | UNVERIFIED        |
| 2     | VERIFIED          |
| 3     | INACTIVE          |
| 4     | REJECTED          |
| 5     | SUSPENDED         |
| 6     | TERMINATED        |
| 7     | CANCELED/DECLINED |
| 8     | EXPIRED           |
| 9     | PENDING           |

<span id="_Ref58239033" class="anchor"></span>Table 74: Table VA0016—Reason Canceled/Declined

### Table VA0016—Reason Canceled/Declined

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Value | Description            |
|-------|------------------------|
| 1     | DISSATISFIED WITH CARE |
| 2     | GEOGRAPHIC ACCESS      |
| 3     | OTHER INSURANCE        |
| 4     | OTHER                  |

<span id="_Ref58239100" class="anchor"></span>Table 75: Table VA0021—Enrollment Priority

### Table VA0021—Enrollment Priority

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Value | Description |
|-------|-------------|
| 1     | PRIORITY 1  |
| 2     | PRIORITY 2  |
| 3     | PRIORITY 3  |
| 4     | PRIORITY 4  |
| 5     | PRIORITY 5  |
| 6     | PRIORITY 6  |
| 7     | PRIORITY 7  |
| 8     | PRIORITY 8  |

<span id="_Ref58239147" class="anchor"></span>Table 76: Table VA0022—Radiation Exposure Method

### Table VA0022—Radiation Exposure Method

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Value | Description                  |
|-------|------------------------------|
| 2     | NAGASAKI - HIROSHIMA         |
| 3     | NUCLEAR TESTING              |
| 4     | H/N AND ATMOSPHERIC TESTING  |
| 5     | UNDERGROUND NUCLEAR TESTING  |
| 6     | EXPOSURE AT NUCLEAR FACILITY |
| 7     | OTHER                        |

<span id="_Ref58239205" class="anchor"></span>Table 77: Table VA0023—Prisoner of War Location

### Table VA0023—Prisoner of War Location

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Value | Description                 |
|-------|-----------------------------|
| 4     | WORLD WAR I                 |
| 5     | WORLD WAR II - EUROPE       |
| 6     | WORLD WAR II - PACIFIC      |
| 7     | KOREAN                      |
| 8     | VIETNAM                     |
| 9     | OTHER                       |
| A     | PERSIAN GULF WAR            |
| B     | YUGOSLAVIA AS A COMBAT ZONE |

<span id="_Ref58239249" class="anchor"></span>Table 78: Table VA0024—Source of Enrollment

### Table VA0024—Source of Enrollment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Value | Description |
|-------|-------------|
| 1     | VAMC        |
| 2     | HEC         |
| 3     | OTHER VAMC  |

<span id="_Ref58239294" class="anchor"></span>Table 79: Table VA0046—Agent Orange Exposure Location

### Table VA0046—Agent Orange Exposure Location

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Value | Description     |
|-------|-----------------|
| B     | BLUE WATER NAVY |
| K     | KOREAN DMZ      |
| V     | VIETNAM         |
| O     | OTHER           |

<span id="_Ref66971208" class="anchor"></span>Table 80: Table VA0047— PATIENT REGISTRATION ONLY REASON Values<span id="_Toc51598972" class="anchor"></span>

### Table VA0047 — PATIENT REGISTRATION ONLY REASON 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Value | Description                  |
|-------|------------------------------|
| 2     | ACTIVE DUTY                  |
| 12    | ART/IVF                      |
| 8     | BENEFICIARY                  |
| 1     | C&P DISABILITY BENEFITS EXAM |
| 18    | CAREGIVER                    |
| 11    | COLLATERAL (OTHER)           |
| 7     | EMPLOYEE                     |
| 4     | EXPOSURE REGISTRY EXAM       |
| 6     | HUMANITARIAN/EMERGENCY       |
| 14    | LEGISLATIVE MANDATE          |
| 10    | MARRIAGE/FAMILY COUNSELING   |
| 13    | NEWBORN                      |
| 16    | NORTH CHICAGO ACTIVE DUTY    |
| 15    | OTHER                        |
| 9     | OTHER THAN HONORABLE (OTH)   |
| 5     | RESEARCH                     |
| 3     | SERVICE CONNECTED ONLY       |
| 17    | UNANSWERED                   |
| 19    | VHA TRANSPLANT PROGRAM       |

Table 81: Table NPCD 001—National Patient Care Database Error Codes

### Table NPCD 001—National Patient Care Database Error Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Value | Description        |
|-------|--------------------|
| 100   | EVENT TYPE SEGMENT |
| 200   | PATIENT NAME       |
| 205   | DATE OF BIRTH      |
| 210   | SEX                |
| 215   | RACE               |

<span id="_Ref58239440" class="anchor"></span>Table 82: Table 0001—Sex

## HL7 Interface Specification for the Transmission of PCMM Primary Care Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PCMM no longer transfers data using HL7 transmissions. This was replaced by Corporate Data Warehouse (CDW)/VHA Support Service Center (VSSC) in 2009.

## Assumptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PCMM no longer transfers data using HL7 transmissions. This was replaced by Corporate Data Warehouse (CDW)/VHA Support Service Center (VSSC) in 2009.

## Message Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PCMM no longer transfers data using HL7 transmissions. This was replaced by Corporate Data Warehouse (CDW)/VHA Support Service Center (VSSC) in 2009.

## Segment Table Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PCMM no longer transfers data using HL7 transmissions. This was replaced by Corporate Data Warehouse (CDW)/VHA Support Service Center (VSSC) in 2009.

## Message Control Segments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PCMM no longer transfers data using HL7 transmissions. This was replaced by Corporate Data Warehouse (CDW)/VHA Support Service Center (VSSC) in 2009.

# HL7 Message Transactions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PCMM no longer transfers data using HL7 transmissions. This was replaced by Corporate Data Warehouse (CDW)/VHA Support Service Center (VSSC) in 2009.

VistA Scheduling uses HL7 to send updated Return To Clinic (RTC) appointments from VistA Scheduling to Computerized Patient Record System (CPRS).

# Supported and User-Defined HL7 Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table 0001—Sex

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Value | Description |
|-------|-------------|
| F     | FEMALE      |
| M     | MALE        |
| O     | OTHER       |
| U     | UNKNOWN     |

<span id="_Ref58239494" class="anchor"></span>Table 83: Table 0002—Marital Status

## Table 0002—Marital Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Value | Description |
|-------|-------------|
| A     | SEPARATED   |
| D     | DIVORCED    |
| M     | MARRIED     |
| S     | SINGLE      |
| W     | WIDOWED     |

<span id="_Ref58239533" class="anchor"></span>Table 84: Table 0003—Event Type Code

## Table 0003—Event Type Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Value | Description                |
|-------|----------------------------|
| A08   | UPDATE PATIENT INFORMATION |

<span id="_Ref58239573" class="anchor"></span>Table 85: Table 0005—Race

## Table 0005—Race

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Value | Description                      |
|-------|----------------------------------|
| 1     | HISPANIC, WHITE                  |
| 2     | HISPANIC, BLACK                  |
| 3     | AMERICAN INDIAN OR ALASKA NATIVE |
| 4     | BLACK, NOT OF HISPANIC ORIGIN    |
| 5     | ASIAN OR PACIFIC ISLANDER        |
| 6     | WHITE, NOT OF HISPANIC ORIGIN    |
| 7     | UNKNOWN                          |

<span id="_Ref58239613" class="anchor"></span>Table 86: Table 0006—Religion

## Table 0006—Religion

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Value | Description                   |
|-------|-------------------------------|
| 0     | ROMAN CATHOLIC CHURCH         |
| 1     | JUDAISM                       |
| 2     | EASTERN ORTHODOX              |
| 3     | BAPTIST                       |
| 4     | METHODIST                     |
| 5     | LUTHERAN                      |
| 6     | PRESBYTERIAN                  |
| 7     | UNITED CHURCH OF CHRIST       |
| 8     | EPISCOPALIAN                  |
| 9     | ADVENTIST                     |
| 10    | ASSEMBLY OF GOD               |
| 11    | BRETHREN                      |
| 12    | CHRISTIAN SCIENTIST           |
| 13    | CHURCH OF CHRIST              |
| 14    | CHURCH OF GOD                 |
| 15    | DISCIPLES OF CHRIST           |
| 16    | EVANGELICAL COVENANT          |
| 17    | FRIENDS                       |
| 18    | JEHOVAH'S WITNESSES           |
| 19    | LATTER DAY SAINTS             |
| 20    | ISLAM                         |
| 21    | NAZARENE                      |
| 22    | OTHER                         |
| 23    | PENTECOSTAL                   |
| 24    | PROTESTANT                    |
| 25    | PROTESTANT, NO DENOMINATION   |
| 26    | REFORMED                      |
| 27    | SALVATION ARMY                |
| 28    | UNITARIAN-UNIVERSALIST        |
| 29    | UNKNOWN/NO PREFERENCE         |
| 30    | NATIVE AMERICAN               |
| 31    | ZEN BUDDHISM                  |
| 32    | AFRICAN RELIGIONS             |
| 33    | AFRO-CARIBBEAN RELIGIONS      |
| 34    | AGNOSTICISM                   |
| 35    | ANGLICAN                      |
| 36    | ANIMISM                       |
| 37    | ATHEISM                       |
| 38    | BABI & BAHA’I FAITHS          |
| 39    | BON                           |
| 40    | CAO DAI                       |
| 41    | CELTICISM                     |
| 42    | CHRISTIAN (NON-SPECIFIC)      |
| 43    | CONFUCIANISM                  |
| 44    | CONGREGATIONAL                |
| 45    | CYBERCULTURE RELIGIONS        |
| 46    | DIVINATION                    |
| 47    | FOURTH WAY                    |
| 48    | FREE DAISM                    |
| 49    | FULL GOSPEL                   |
| 50    | GNOSIS                        |
| 51    | HINDUISM                      |
| 52    | HUMANISM                      |
| 53    | INDEPENDENT                   |
| 54    | JAINISM                       |
| 55    | MAHAYANA                      |
| 56    | MEDITATION                    |
| 57    | MESSIANIC JUDAISM             |
| 58    | MITRAISM                      |
| 59    | NEW AGE                       |
| 60    | NON-ROMAN CATHOLIC            |
| 61    | OCCULT                        |
| 62    | ORTHODOX                      |
| 63    | PAGANISM                      |
| 64    | PROCESS, THE                  |
| 65    | REFORMED/PRESBYTERIAN         |
| 66    | SATANISM                      |
| 67    | SCIENTOLOGY                   |
| 68    | SHAMANISM                     |
| 69    | SHIITE (ISLAM)                |
| 70    | SHINTO                        |
| 71    | SIKISM                        |
| 72    | SPIRITUALISM                  |
| 73    | SUNNI (ISLAM)                 |
| 74    | TAOISM                        |
| 75    | THERAVADA                     |
| 76    | UNIVERSAL LIFE CHURCH         |
| 77    | VAJRAYANA (TIBETAN)           |
| 78    | VEDA                          |
| 79    | VOODOO                        |
| 80    | WICCA                         |
| 81    | YAOHUSHUA                     |
| 82    | ZOROASTRIANISM                |
| 83    | ASKED BUT DECLINED TO ANSWER  |
| 84    | AFRICAN AMERICAN EPISCOPAL    |
| 85    | BUDDHISM, OTHER               |
| 86    | EVANGELICAL                   |
| 87    | HOLINESS CHURCHES             |
| 88    | CATHOLIC (NON-ROMAN CATHOLIC) |
| 89    | UNITARIAN-UNIVERSALISM        |

<span id="_Ref58239714" class="anchor"></span>Table 87: Table 0076—Message Type

## Table 0076—Message Type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Value | Description |
|-------|-------------|
| ADT   | ADT MESSAGE |

<span id="_Ref58240754" class="anchor"></span>Table 88: MSH—Message Header Segment

# HL7 Interface Specification for VIC Card VistA to NCMD

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a Veteran’s ID Card (VIC) Image Capture workstation retrieves demographic data from VistA, a record is created in a VistA file to indicate that a VIC request is pending under the following exception conditions.

- The patient does *not* have a National Integrated Control Number (ICN).
- The eligibility/enrollment information needed to determine the patient’s eligibility for a VIC is incomplete.
- The current status of the Veteran’s claim for Purple Heart eligibility is either pending or in-process.

A Health Level 7 (HL7) message is used to notify the National Card Management Directory (NCMD) when these exceptions have been resolved.

This specifies the information needed to either release the previous hold or cancel a pending VIC order request and communicate the order action to the NCMD.

The data exchange is triggered when the daily VistA re-evaluation of the pending VIC order request finds that a National ICN exists and the VIC eligibility can be determined.

The basic communication protocol is addressed, as well as the information that is made available and how it is obtained.

This application uses the abstract message approach and encoding rules specified by HL7. HL7 is used for communicating data associated with various events that occur in health care environments.

The formats of these messages conform to the Version 2.4 HL7 Interface Standards where applicable.

## Assumptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The transmission of VIC requests from VistA to the NCMD assumes the following.

- All VistA sites have installed VistA HL7 software and it is operational.
- The Veteran’s demographics and digital photograph have been previously loaded into the NCMD.

## Message Content

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The data sent in the HL7 messages is limited to the information that is required to uniquely identify the patient and request the VIC card. The data transmitted is limited to available VistA data.

## Data Capture and Transmission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following event trigger generates a General Order Message (ORM~O01).

VistA re-evaluates a pending VIC card request and the associated patient has a nationally assigned ICN and the necessary eligibility/enrollment information needed to determine the patient’s VIC eligibility.

22. Any modification made to the VistA database in *non*-standard ways, such as a direct global set by an application or by M code, is *not* captured.

## VA TCP/IP Lower Level Protocol

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HL7 V. 1.6 TCP/IP lower level protocol (LLP) is used, which implements the HL7 Minimal Lower Layer Protocol (MLLP) referenced in section C.4 of Appendix C of the Health Level 7 Implementation Guide (v2.3).

HL7 CONTROL SEGMENTS: This section defines the HL7 control segments supported by VistA. The messages are presented separately and defined by category. Segments are also described. The messages are presented in the Message Control category.

### Message Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the VistA perspective, all incoming or outgoing messages are handled or generated based on an event.

In this section and the following sections, the following elements are defined for each message.

- Trigger events.
- Message event code.
- List of segments used in the message.
- List of fields for each segment in the message.

Each message is composed of segments, which:

- Contain logical groupings of data.
- May be optional or repeatable:
- A \[ \] indicates the segment is optional
- The { } indicates the segment is repeatable.

For each message category, there is a list of HL7 standard segments used for the message.

### Segment Table Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For each segment, the data elements are described in table format. The table includes the following:

- Sequence number (SEQ)
- Maximum length (LEN)
- Data type (DT)
- Required or optional (R/O)
- Repeatable (RP/#)
- Table number (TBL#)
- Element name
- VistA description

Each segment is described in the following sections.

### Message Control Segments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the message control segments that are contained in message types described in this document. These are generic descriptions. Any time any of the segments described in this section are included in a message in this document, the VistA descriptions and mappings are as specified here, unless otherwise specified in that section.

### MSH—Message Header Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Ref58240755" class="anchor"></span>Table 89: MSA—Message Acknowledgement Segment</p></caption>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 24%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th>SEQ</th>
<th>LEN</th>
<th>DT</th>
<th>R/O</th>
<th>RP/#</th>
<th>TBL#</th>
<th>Element Name</th>
<th>VistA Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>1</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Field Separator</td>
<td><em>Recommended</em> value is ^ (caret)</td>
</tr>
<tr class="even">
<td>2</td>
<td>4</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Encoding Characters</td>
<td><p><em>Recommended</em> delimiter values:</p>
<ul>
<li><p>Component = <strong>~</strong> (tilde)</p></li>
<li><p>Repeat = <strong>|</strong> (bar)</p></li>
<li><p>Escape = <strong>\</strong> (back slash)</p></li>
<li><p>Sub-component = <strong>&amp;</strong> (ampersand)</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>3</td>
<td>15</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Sending Application</td>
<td>Name field of HL7 Application Parameter file.</td>
</tr>
<tr class="even">
<td>4</td>
<td>20</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Sending Facility</td>
<td>Sending station's facility number from Institution field of HL7 Communication Parameters file.</td>
</tr>
<tr class="odd">
<td>5</td>
<td>30</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Receiving Application</td>
<td>Name field of HL7 Application Parameter file.</td>
</tr>
<tr class="even">
<td>6</td>
<td>30</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Receiving Facility</td>
<td>Receiving station’s facility number from Institution field of HL Logical Link file.</td>
</tr>
<tr class="odd">
<td>7</td>
<td>26</td>
<td>TS</td>
<td></td>
<td></td>
<td></td>
<td>Date/Time Of Message</td>
<td>Date and time message was created.</td>
</tr>
<tr class="even">
<td>8</td>
<td>40</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Security</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>9</td>
<td>7</td>
<td>CM</td>
<td>R</td>
<td></td>
<td><p>0076</p>
<p>0003</p></td>
<td>Message Type</td>
<td><p>2 Components:</p>
<ul>
<li><p>See <a href="#_Ref58237660">Table 0076—Message Type</a>.</p></li>
<li><p>See <a href="#_Ref58237406">Table 0003—Event Type Code</a>.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>10</td>
<td>20</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Message Control ID</td>
<td>Automatically generated by VistA HL7 Package.</td>
</tr>
<tr class="odd">
<td>11</td>
<td>1</td>
<td>ID</td>
<td>R</td>
<td></td>
<td>0103</td>
<td>Processing ID</td>
<td><strong>P</strong> (production).</td>
</tr>
<tr class="even">
<td>12</td>
<td>8</td>
<td>ID</td>
<td>R</td>
<td></td>
<td>0104</td>
<td>Version ID</td>
<td>Version ID field of event protocol in Protocol file.</td>
</tr>
<tr class="odd">
<td>13</td>
<td>15</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Sequence Number</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>14</td>
<td>180</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Continuation Pointer</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>15</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td>0155</td>
<td>Accept Acknowledgment Type</td>
<td><strong>NE</strong> (never acknowledge).</td>
</tr>
<tr class="even">
<td>16</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td>0155</td>
<td>Application Acknowledgment Type</td>
<td><strong>AL</strong> (always acknowledge).</td>
</tr>
<tr class="odd">
<td>17</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td>Country Code</td>
<td><strong>USA</strong>.</td>
</tr>
<tr class="even">
<td>18</td>
<td>6</td>
<td>ID</td>
<td></td>
<td>Y/3</td>
<td>0211</td>
<td>Character Set</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>19</td>
<td>60</td>
<td>CE</td>
<td></td>
<td></td>
<td></td>
<td>Principal Language of Message</td>
<td>Not used.</td>
</tr>
</tbody>
</table>

<span id="_Ref58240755" class="anchor"></span>Table 89: MSA—Message Acknowledgement Segment

### MSA—Message Acknowledgement Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| 2.3.1 | LEN | DT  | R/O | RP/# | TBL# | Element Name                | VistA Description                                                 |
|-------|-----|-----|-----|------|------|-----------------------------|-------------------------------------------------------------------|
| 1     | 2   | ID  | R   |      | 0008 | Acknowledgment Code         | REF: See HL7 [Table 0008—Acknowledgment Code](#_Ref58237468). |
| 2     | 20  | ST  | R   |      |      | Message Control ID          | Message Control ID of the message being acknowledged.             |
| 3     | 80  | ST  | O   |      |      | Text Message                | Free text error message.                                          |
| 4     | 15  | NM  | O   |      |      | Expected Sequence Number    | Not used.                                                         |
| 5     | 1   | ID  | B   |      | 0102 | Delayed Acknowledgment Type | Not used.                                                         |
| 6     | 100 | CE  | O   |      |      | Error Condition             | Not used.                                                         |

<span id="_Ref58240756" class="anchor"></span>Table 90: PID—Patient Identification Segment

### PID—Patient Identification Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Ref58240757" class="anchor"></span>Table 91: ORC—Common Order Segment</p></caption>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 25%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th>SEQ</th>
<th>LEN</th>
<th>DT</th>
<th>R/O</th>
<th>RP/#</th>
<th>TBL#</th>
<th>Element Name</th>
<th>VistA Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>4</td>
<td>SI</td>
<td></td>
<td></td>
<td></td>
<td>Set ID - Patient ID</td>
<td>Always set to “<strong>1</strong>”.</td>
</tr>
<tr class="even">
<td>2</td>
<td>20</td>
<td>CK</td>
<td></td>
<td></td>
<td></td>
<td>Patient ID (External ID)</td>
<td>Social Security Number field in the PATIENT (#2) file.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>20</td>
<td>CM</td>
<td>R</td>
<td>Y</td>
<td></td>
<td>Patient ID (Internal ID)</td>
<td><p>Integrated Control Number (ICN) field in the PATIENT (#2) file.</p>
<ul>
<li><p>Component 1: ICN w/checksum</p></li>
<li><p>Component 2: <strong>NULL</strong></p></li>
<li><p>Component 3: <strong>NULL</strong></p></li>
<li><p>Component 4: Assigning authority (subcomponent 1: “<strong>USVHA</strong>”, subcomponent 3: “<strong>L</strong>”</p></li>
<li><p>Component 5: Type “<strong>NI</strong>”</p></li>
</ul></td>
</tr>
<tr class="even">
<td>4</td>
<td>12</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Alternate Patient ID</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>5</td>
<td>48</td>
<td>PN</td>
<td>R</td>
<td></td>
<td></td>
<td>Patient Name</td>
<td>Name.</td>
</tr>
<tr class="even">
<td>6</td>
<td>30</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Mother's Maiden Name</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>7</td>
<td>26</td>
<td>TS</td>
<td></td>
<td></td>
<td></td>
<td>Date of Birth</td>
<td>Date of birth.</td>
</tr>
<tr class="even">
<td>8</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td>0001</td>
<td>Sex</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>9</td>
<td>48</td>
<td>PN</td>
<td></td>
<td>Y</td>
<td></td>
<td>Patient Alias</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>10</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td>0005</td>
<td>Race</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>11</td>
<td>106</td>
<td>AD</td>
<td></td>
<td>Y</td>
<td></td>
<td>Patient Address</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>12</td>
<td>4</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td>County Code</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>13</td>
<td>40</td>
<td>TN</td>
<td></td>
<td>Y</td>
<td></td>
<td>Phone Number – Home</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>14</td>
<td>40</td>
<td>TN</td>
<td></td>
<td>Y</td>
<td></td>
<td>Phone Number – Business</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>15</td>
<td>25</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Language – Patient</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>16</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td>0002</td>
<td>Marital Status</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>17</td>
<td>3</td>
<td>ID</td>
<td></td>
<td></td>
<td>0006</td>
<td>Religion</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>18</td>
<td>20</td>
<td>CK</td>
<td></td>
<td></td>
<td></td>
<td>Patient Account Number</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>19</td>
<td>16</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>SSN Number – Patient</td>
<td>Social security number and pseudo indicator.</td>
</tr>
<tr class="even">
<td>20</td>
<td>25</td>
<td>CM</td>
<td></td>
<td></td>
<td></td>
<td>Driver's Lic Num – Patient</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>21</td>
<td>20</td>
<td>CK</td>
<td></td>
<td></td>
<td></td>
<td>Mother's Identifier</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>22</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td>0189</td>
<td>Ethnic Group</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>23</td>
<td>25</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Birth Place</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>24</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td>Multiple Birth Indicator</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>25</td>
<td>2</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Birth Order</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>26</td>
<td>3</td>
<td>ID</td>
<td></td>
<td>Y</td>
<td>0171</td>
<td>Citizenship</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>27</td>
<td>60</td>
<td>CE</td>
<td></td>
<td></td>
<td>0172</td>
<td>Veterans Military Status</td>
<td>Not used.</td>
</tr>
</tbody>
</table>

<span id="_Ref58240757" class="anchor"></span>Table 91: ORC—Common Order Segment

### ORC—Common Order Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| SEQ | LEN | DT  | R/O | RP/# | TBL# | Element Name              | VistA Description                                             |
|-----|-----|-----|-----|------|------|---------------------------|---------------------------------------------------------------|
| 1   | 2   | ID  | R   |      | 0119 | Order Control             | REF: See [Table 0119—Order Control Codes](#_Ref58241178). |
| 2   | 22  | EI  | C   |      |      | Placer Order Number       | Not used.                                                     |
| 3   | 22  | EI  | C   |      |      | Filler Order Number       | Not used.                                                     |
| 4   | 22  | EI  |     |      |      | Placer Group Number       | Not used.                                                     |
| 5   | 2   | ID  |     |      | 0038 | Order Status              | Not used.                                                     |
| 6   | 1   | ID  |     |      | 0121 | Response Flag             | Not used.                                                     |
| 7   | 200 | TQ  |     |      |      | Quantity/timing           | Not used.                                                     |
| 8   | 200 | CM  |     |      |      | Parent                    | Not used.                                                     |
| 9   | 26  | TS  |     |      |      | Date/Time of Transaction  | Not used.                                                     |
| 10  | 120 | XCN |     |      |      | Entered By                | Not used.                                                     |
| 11  | 120 | XCN |     |      |      | Verified By               | Not used.                                                     |
| 12  | 120 | XCN |     |      |      | Ordering Provider         | Not used.                                                     |
| 13  | 80  | PL  |     |      |      | Enterer’s Location        | Not used.                                                     |
| 14  | 40  | XTN |     | Y/2  |      | Call Back Phone Number    | Not used.                                                     |
| 15  | 26  | TS  |     |      |      | Order Effective Date/Time | Not used.                                                     |
| 16  | 200 | CE  |     |      |      | Order Control Code Reason | Not used.                                                     |
| 17  | 60  | CE  |     |      |      | Entering Organization     | Not used.                                                     |
| 18  | 60  | CE  |     |      |      | Entering Device           | Not used.                                                     |
| 19  | 120 | XCN |     |      |      | Action By                 | Not used.                                                     |

<span id="_Ref58240758" class="anchor"></span>Table 92: RQD—Requisition Detail Segment

### RQD—Requisition Detail Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| SEQ | LEN | DT  | R/O | RP/# | TBL# | Element Name                | VistA Description                                          |
|-----|-----|-----|-----|------|------|-----------------------------|------------------------------------------------------------|
| 1   | 4   | SI  |     |      |      | Requisition Line Number     | Always set to “1”.                                     |
| 2   | 60  | CE  | C   |      |      | Item Code – Internal        | Not used.                                                  |
| 3   | 60  | CE  | C   |      |      | Item Code – External        | NCMD Card ID (#.01) field in the VIC REQUEST (#39.6) file. |
| 4   | 60  | CE  | C   |      |      | Hospital Item Code          | Not used.                                                  |
| 5   | 6   | NM  |     |      |      | Requisition Quantity        | Not used.                                                  |
| 6   | 60  | CE  |     |      |      | Requisition Unit of Measure | Not used.                                                  |
| 7   | 30  | IS  |     |      | 0319 | Dept. Cost Center           | Not used.                                                  |
| 8   | 30  | IS  |     |      | 0320 | Item Natural Account Code   | Not used.                                                  |
| 9   | 60  | CE  |     |      |      | Deliver to ID               | Not used.                                                  |
| 10  | 8   | DT  |     |      |      | Date Needed                 | Not used.                                                  |

<span id="_Ref58240759" class="anchor"></span>Table 93: NTE—Notes and Comments Segment

### NTE—Notes and Comments Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Toc193958121" class="anchor"></span>Table 94: Table 0003—Event Type Code</p></caption>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 25%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th>SEQ</th>
<th>LEN</th>
<th>DT</th>
<th>R/O</th>
<th>RP/#</th>
<th>TBL#</th>
<th>ELEMENT NAME</th>
<th>VistA DESCRIPTION</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>4</td>
<td>SI</td>
<td>O</td>
<td></td>
<td></td>
<td>Set ID</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>2</td>
<td>8</td>
<td>ID</td>
<td>O</td>
<td></td>
<td>105</td>
<td>Source of Comment</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>65536</td>
<td>FT</td>
<td>O</td>
<td>Y</td>
<td></td>
<td>Comment</td>
<td><p><strong>1<sup>st</sup> repetition:</strong> String “<strong>POW:</strong>” followed by single character Prisoner of War indicator calculated from the PATIENT ELIGIBILITIES (#361) field of the PATIENT (#2) file and the current enrollment status derived from the supported call $$STATUS^DGENA.</p>
<p>Example: <strong>POW:Y</strong></p>
<p><strong>2<sup>nd</sup> repetition:</strong> String “<strong>PH:</strong>” followed by single character Purple Heart indicator calculated from CURRENT PH INDICATOR (#.531) and CURRENT PURPLE HEART STATUS (#.532) fields of the PATIENT (#2) file.</p>
<p>Example: <strong>PH:N</strong></p></td>
</tr>
<tr class="even">
<td>4</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td></td>
<td>364</td>
<td>Comment Type</td>
<td>Not used.</td>
</tr>
</tbody>
</table>

<span id="_Toc193958121" class="anchor"></span>Table 94: Table 0003—Event Type Code

## Trigger Events and Message Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each triggering event is listed below along with the applicable form of the message to be exchanged. The notation used to describe the sequence, option, and repetition of segments is described in the HL7 V. 2.4 Standard Specification Manual, Chapter 2, and in summary form, in Section [2.1](#eligibility-idmaintenance-menu) of this document.

## ORM—General Order Message (Event O01)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ORM~O01 message to be sent to the NCMD:

- ORM—Order Message
- MSH—Message Header
- PID—Patient Identification
- ORC—Common Order
- RQD—Requisition Detail
- NTE—Notes and Comments

### Sample Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc193958014" class="anchor"></span>Figure 16: Sample ORM~O01 Message Sent to NCMD

MSH^~\|\\^VIC NCMD SEND^500~REDACTED~DNS^VIC NCMD RECV^NCMD^20031008144616-0400^^ORM~O01^50018835^P^2.4^^^NE^AL^USA

PID^1^222-33-4444\~~^1001178082V735077\~\~~USVHA&&L~NI^^ADTPATIENT~ONE^^

19500404^^^^^^^^^^^^222334444

ORC^RL

RQD^1^^22233444-ADTPATIENT-1

NTE^^^POW:N\|PH:Y

## ORR—General Order Response Message Response to Any ORM (Event O02)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Upon receipt of a VIC Card request order message, the NCMD responds with an ORR~O02 message:

- ORR—Order Response Message
- MSH—Message Header
- MSA—Message Acknowledgment

### Sample Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

General Order Response (ORR~O02) message when the General Order Message (ORM~O01) is successful.

<span id="_Toc193958015" class="anchor"></span>Figure 17: General Order Response (ORR~O02) Message—Success: General Order Message (ORM~O01)

MSH^~\|\\^VIC NCMD RECV^NCMD^VIC NCMD SEND^500~REDACTED~DNS^20031008144616-0400^^ORR~O02^782218835^P^2.4^^^NE^AL^USA

MSA^AA^50018835

General Order Response (ORR~O02) message when the General Order Message (ORM~O01) fails.

<span id="_Toc193958016" class="anchor"></span>Figure 18: General Order Response (ORR~O02) Message—Failure: General Order Message (ORM~O01)

MSH^~\|\\^VIC NCMD RECV^NCMD^VIC NCMD SEND^500~REDACTED~DNS^20031008144616-0400^^ORR~O02^782218835^P^2.4^^^NE^AL^USA

MSA^AE^50018835^CardID not on file

## Supported and User Defined HL7 Tables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Table 0003—Event Type Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Value   | Description          |
|---------|----------------------|
| O01 | ORM – Order Message  |
| O02 | ORR – Order Response |

<span id="_Toc193958122" class="anchor"></span>Table 95: Table 0008—Acknowledgment Code

### Table 0008—Acknowledgment Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Toc193958123" class="anchor"></span>Table 96: Table 0076—Message Type</p></caption>
<colgroup>
<col style="width: 23%" />
<col style="width: 76%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>AA</strong></td>
<td><ul>
<li><p>Original mode: Application Accept</p></li>
<li><p>Enhanced mode: Application acknowledgment: Accept</p></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>AE</strong></td>
<td><ul>
<li><p>Original mode: Application Error</p></li>
<li><p>Enhanced mode: Application acknowledgment: Error</p></li>
</ul></td>
</tr>
<tr class="odd">
<td><strong>AR</strong></td>
<td><ul>
<li><p>Original mode: Application Reject</p></li>
<li><p>Enhanced mode: Application acknowledgment: Reject</p></li>
</ul></td>
</tr>
<tr class="even">
<td><strong>CA</strong></td>
<td>Enhanced mode: Accept acknowledgment: Commit Accept</td>
</tr>
<tr class="odd">
<td><strong>CE</strong></td>
<td>Enhanced mode: Accept acknowledgment: Commit Error</td>
</tr>
<tr class="even">
<td><strong>CR</strong></td>
<td>Enhanced mode: Accept acknowledgment: Commit Reject</td>
</tr>
</tbody>
</table>

<span id="_Toc193958123" class="anchor"></span>Table 96: Table 0076—Message Type

### Table 0076—Message Type

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Value   | Description                  |
|---------|------------------------------|
| ORM | Order Message                |
| ORR | Order Acknowledgment Message |

<span id="_Ref58241178" class="anchor"></span>Table 97: Table 0119—Order Control Codes

### Table 0119—Order Control Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Value  | Description           |
|--------|-----------------------|
| RL | Release Previous Hold |
| CA | Cancel Order Request  |

<span id="_Ref58244295" class="anchor"></span>Table 98: MSH—Message Header Segment

# HL7 Generic PID, EVN, PV1 Segment Builder Established by MPI

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes functionality that can be used by other applications to dynamically build fully populated PID, EVN, and PV1 segments for use in communicating to and from VistA and/or HealtheVet (HeV) VistA.

This document specifies the information needed by applications to use the generic HL7 v2.4 segment builders. In order for applications to use this functionality, they *must* first subscribe to the Integration Agreement \#3630 described below.

23. REF: For more information about the specific data elements included in these segments, see the [MPI HL7 v2.4 Interface Specification on the VDL](https://www.va.gov/vdl/application.asp?appid=16).

## Integration Agreement (IA) \#3630

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This Integration Agreement consists of three Health Level 7 (HL7), Version 2.4 segment builders in the form of the following APIs:

- BLDEVN^VAFCQRY
- BLDPD1^VAFCQRY
- BLDPID^VAFCQRY

These generic segment builders can be used to build Version 2.4 HL7 PID, EVN, and PD1 segments.

### Custodial Package

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

REGISTRATION has the following Subscribing Packages:

- MASTER PATIENT INDEX VISTA
- CLINICAL INFO RESOURCE NETWORK
- OUTPATIENT PHARMACY
- CLINICAL PROCEDURES
- PHARMACY BENEFITS MANAGEMENT
- RADIOLOGY/NUCLEAR MEDICINE
- GEN. MED. REC. - VITALS
- ADVERSE REACTION TRACKING
- LAB SERVICE
- CLINICAL CASE REGISTRIES

## API: BLDEVN^VAFCQRY

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Description

The entry point builds the EVN segment via Version 2.4 including the treating facility last treatment date and event reason.

Format

BLDEVN^VAFCQRY

Input Variables

- DFN: Internal Entry Number of the patient in the PATIENT (#2) file.
- SEQ: Variable consisting of sequence numbers delimited by commas that are used to build the message.
- EVN: (Passed by reference). This is the array location to place EVN segment result. The array can have existing values when passed.
- HL: Array that contains the necessary HL variables (init^hlsub).
- EVR: Event reason that triggered this message.
- ERR: Array used to return an error.

## API: BLDPD1^VAFCQRY

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Description

This entry point builds the Version 2.4 PD1 segment.

Format

BLDPD1^VAFCQRY

Input Variables

- DFN: Internal Entry Number of the patient in the PATIENT (#2) file.
- SEQ: Variable consisting of sequence numbers delimited by commas that is used to build the message.
- PD1: (Passed by reference). Array location to place PD1 segment result. The array can have existing values when passed.
- HL: Array that contains the necessary HL variables (init^hlsub).
- ERR: Array used to return an error.

## API: BLDPID^VAFCQRY

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Description

This entry point builds the Version 2.4 PID segment.

Format

BLDPID^VAFCQRY

Input Variables

- DFN: Internal Entry Number of the patient in the PATIENT (#2) file.
- CNT: The value to be place in PID seq#1 (SET ID).
- SEQ: Variable consisting of sequence numbers delimited by commas that is used to build the message.

"ALL" can be passed to get all available fields in the PID segment that are available. This is the default.

- PID: (Passed by reference). The array location to place PID segment result, the array can have existing values when passed.
- HL: Array that contains the necessary HL variables (init^hlsub).
- ERR: Array used to return an error.

# HL7 Interface Specification for Home Telehealth (HTH)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Home Telehealth (HTH) application is in support of the Care Coordination Program that involves the use of Home Telehealth technologies. Home Telehealth helps the Veterans Health Administration (VHA) by 836 creating a framework for optimizing the overall development and implementation of Telemedicine in VHA.

This document specifies the information needed for activation and inactivation of Home Telehealth patients with their perspective HTH vendors.

This application uses the abstract message approach and encoding rules specified by HL7. HL7 is used for communicating data associated with various events which occur in health care environments.

The formats of these messages conform to the Version 2.4 HL7 Interface Standards.

## Assumptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The transmission of HTH registration/inactivation requests from VistA to the HTH vendors assumes the following.

- All VistA sites have installed VistA HL7 software and it is operational.
- The associated VistA Consult Patch GMRC\*3\*42 has been installed and HTH consults activated.

## Message Content

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The data sent in the HL7 messages is limited to the information that is required to uniquely identify the patient and requested by the HTH vendors. The data transmitted is recorded and available in VistA.

## Data Capture and Transmission

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following event trigger generates a Register a Patient (Event A04):

- Provider evaluates patient and refers patient for HTH care by submitting a consult request. A pending consult request goes to the HTH Care Coordinator and verifies eligibility. A registration request is submitted to HTH vendor by using the Patient Sign-Up/Activation \[DGHT PATIENT SIGNUP\] menu option.
- The protocol DG HOME TELEHEALTH ADT-A04 CLIENT in PROTOCOL (#101) file is used for the Patient Sign-Up/Activation process.
- The entry DG HOME TELEHEALTH in the HL7 APPLICATION PARAMETER (#771) file is used for processing outgoing HL7 messages from the Home Telehealth vendors.
- The entry HTAPPL in the HL7 APPLICATION PARAMETER (#771) file is used for processing incoming HL7 messages from the Home Telehealth vendors.

The following entries in the HL LOGICAL LINK (#870) file facilitate the transmission of Home Telehealth patient data to Home Telehealth vendor server system via the Austin Interface:

- DG HT AMD
- DG HT ATI
- DG HT HH
- DG HT VIT
- DG HT VN
- DG HTH

The mail group DGHTERR generates mail messages for any transmission rejects received from the vendor server.

The following event trigger generates an Inactivation of a Patient (Event A03):

- HTH Care Coordinator determines patient care is now complete. An inactivation request is submitted to HTH vendor Patient Inactivation \[DGHT PATIENT INACTIVATION\] menu option.
- The protocol DG HOME TELEHEALTH ADT-A03 CLIENT in the PROTOCOL (#101) file is used for the Patient Inactivation process.
- The entry DG HOME TELEHEALTH in the HL7 APPLICATION PARAMETER (#771) file is used for processing outgoing HL7 messages from the Home Telehealth vendors.
- The entry HTAPPL in the HL7 APPLICATION PARAMETER (#771) file is used for processing incoming HL7 messages from the Home Telehealth vendors.

The following entries in the HL LOGICAL LINK (#870) file facilitate the transmission of Home Telehealth patient data to Home Telehealth vendor server system via the Austin Interface:

- DG HT AMD
- DG HT ATI
- DG HT HH
- DG HT VIT
- DG HT VN
- DG HTH

The DGHTERR mail group generates mail messages for any transmission rejects received from the vendor server.

24. Any modification made to the VistA database in *non*-standard ways, such as a direct global set by an application or by M code, is *not* processed appropriately.

# VA TCP/IP Lower Level Protocol

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HL7 V. 1.6 TCP/IP lower level protocol (LLP) is used, which implements the HL7 Minimal Lower Layer Protocol (MLLP) referenced in section C.4 of Appendix C of the Health Level 7 Implementation Guide (v2.4).

## HL7 CONTROL SEGMENTS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section defines the HL7 control segments supported by VistA. The messages are presented separately and defined by category. Segments are also described. The messages are presented in the Message Control category.

## Message Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the VistA perspective, all incoming or outgoing messages are handled or generated based on an event.

In this section and the following sections, the following elements are defined for each message:

- Trigger events
- Message event code
- List of segments used in the message
- List of fields for each segment in the message

Each message is composed of segments, which:

- Contain logical groupings of data.
- May be optional or repeatable:
- A \[ \] indicates the segment is optional.
- The { } indicates the segment is repeatable.

For each message category, there is a list of HL7 standard segments used for the message.

## Segment Table Definitions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For each segment, the data elements are described in table format. The table includes the following:

- Sequence number (SEQ)
- Maximum length (LEN)
- Data type (DT)
- Required or optional (R/O)
- Repeatable (RP/#),
- Table number (TBL#)
- Element name
- VistA description

Each segment is described in the following sections.

## Message Control Segments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes the message control segments that are contained in message types described in this document. These are generic descriptions. Any time any of the segments described in this section are included in a message in this document, the VistA descriptions and mappings are as specified here unless otherwise specified in that section.

### MSH—Message Header Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Ref58244372" class="anchor"></span>Table 99: EVN—Event Type Segment</p></caption>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 24%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th>SEQ</th>
<th>LEN</th>
<th>DT</th>
<th>R/O</th>
<th>RP/#</th>
<th>TBL#</th>
<th>Element Name</th>
<th>VistA Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>1</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Field Separator</td>
<td><em>Recommended</em> value is <strong>^</strong> (caret).</td>
</tr>
<tr class="even">
<td>2</td>
<td>4</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Encoding Characters</td>
<td><p><em>Recommended</em> delimiter values:</p>
<ul>
<li><p>Component = <strong>~</strong> (tilde)</p></li>
<li><p>Repeat = <strong>|</strong> (bar)</p></li>
<li><p>Escape = <strong>\</strong> (back slash)</p></li>
<li><p>Sub-component = <strong>&amp;</strong> (ampersand)</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>3</td>
<td>15</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Sending Application</td>
<td>Name field of HL7 Application Parameter file.</td>
</tr>
<tr class="even">
<td>4</td>
<td>20</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Sending Facility</td>
<td>Sending station's facility number from Institution field of HL7 Communication Parameters file.</td>
</tr>
<tr class="odd">
<td>5</td>
<td>30</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Receiving Application</td>
<td>Name field of HL7 Application Parameter file.</td>
</tr>
<tr class="even">
<td>6</td>
<td>30</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Receiving Facility</td>
<td>Receiving station’s facility number from Institution field of HL Logical Link file.</td>
</tr>
<tr class="odd">
<td>7</td>
<td>26</td>
<td>TS</td>
<td></td>
<td></td>
<td></td>
<td>Date/Time Of Message</td>
<td>Date and time message was created.</td>
</tr>
<tr class="even">
<td>8</td>
<td>40</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Security</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>9</td>
<td>7</td>
<td>CM</td>
<td>R</td>
<td></td>
<td><p>0076</p>
<p>0003</p></td>
<td>Message Type</td>
<td><p>2 Components:</p>
<ul>
<li><p>See <a href="#_Ref58237660">Table 0076—Message Type</a>.</p></li>
<li><p>See <a href="#_Ref58237406">Table 0003—Event Type Code</a>.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>10</td>
<td>20</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Message Control ID</td>
<td>Automatically generated by VistA HL7 Package.</td>
</tr>
<tr class="odd">
<td>11</td>
<td>1</td>
<td>ID</td>
<td>R</td>
<td></td>
<td>0103</td>
<td>Processing ID</td>
<td><strong>P</strong> (production).</td>
</tr>
<tr class="even">
<td>12</td>
<td>8</td>
<td>ID</td>
<td>R</td>
<td></td>
<td>0104</td>
<td>Version ID</td>
<td>Version ID field of event protocol in Protocol file.</td>
</tr>
<tr class="odd">
<td>13</td>
<td>15</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Sequence Number</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>14</td>
<td>180</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Continuation Pointer</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>15</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td>0155</td>
<td>Accept Acknowledgment Type</td>
<td><strong>NE</strong> (never acknowledge).</td>
</tr>
<tr class="even">
<td>16</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td>0155</td>
<td>Application Acknowledgment Type</td>
<td><strong>AL</strong> (always acknowledge).</td>
</tr>
<tr class="odd">
<td>17</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td>Country Code</td>
<td><strong>USA</strong>.</td>
</tr>
<tr class="even">
<td>18</td>
<td>6</td>
<td>ID</td>
<td></td>
<td>Y/3</td>
<td>0211</td>
<td>Character Set</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>19</td>
<td>60</td>
<td>CE</td>
<td></td>
<td></td>
<td></td>
<td>Principal Language of Message</td>
<td>Not used.</td>
</tr>
</tbody>
</table>

<span id="_Ref58244372" class="anchor"></span>Table 99: EVN—Event Type Segment

### EVN—Event Type Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Ref58244447" class="anchor"></span>Table 100: PID—Patient Identification Segment</p></caption>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 24%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th>SEQ</th>
<th>LEN</th>
<th>DT</th>
<th>R/O</th>
<th>RP/#</th>
<th>TBL#</th>
<th>Element Name</th>
<th>VistA Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>1</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Field Separator</td>
<td><em>Recommended</em> value is <strong>^</strong> (caret).</td>
</tr>
<tr class="even">
<td>2</td>
<td>4</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Encoding Characters</td>
<td><p><em>Recommended</em> delimiter values:</p>
<ul>
<li><p>Component = <strong>~</strong> (tilde)</p></li>
<li><p>Repeat = <strong>|</strong> (bar)</p></li>
<li><p>Escape = <strong>\</strong> (back slash)</p></li>
<li><p>Sub-component = <strong>&amp;</strong> (ampersand)</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>3</td>
<td>15</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Sending Application</td>
<td>Name field of HL7 Application Parameter file.</td>
</tr>
<tr class="even">
<td>4</td>
<td>20</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Sending Facility</td>
<td>Sending station's facility number from Institution field of HL7 Communication Parameters file.</td>
</tr>
<tr class="odd">
<td>5</td>
<td>30</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Receiving Application</td>
<td>Name field of HL7 Application Parameter file.</td>
</tr>
<tr class="even">
<td>6</td>
<td>30</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Receiving Facility</td>
<td>Receiving station’s facility number from Institution field of HL Logical Link file.</td>
</tr>
<tr class="odd">
<td>7</td>
<td>26</td>
<td>TS</td>
<td></td>
<td></td>
<td></td>
<td>Date/Time Of Message</td>
<td>Date and time message was created.</td>
</tr>
<tr class="even">
<td>8</td>
<td>40</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Security</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>9</td>
<td>7</td>
<td>CM</td>
<td>R</td>
<td></td>
<td><p>0076</p>
<p>0003</p></td>
<td>Message Type</td>
<td><p>Two Components:</p>
<ul>
<li><p>See <a href="#_Ref58237660">Table 0076—Message Type</a>.</p></li>
<li><p>See <a href="#_Ref58237406">Table 0003—Event Type Code</a>.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>10</td>
<td>20</td>
<td>ST</td>
<td>R</td>
<td></td>
<td></td>
<td>Message Control ID</td>
<td>Automatically generated by VistA HL7 Package.</td>
</tr>
<tr class="odd">
<td>11</td>
<td>1</td>
<td>ID</td>
<td>R</td>
<td></td>
<td>0103</td>
<td>Processing ID</td>
<td><strong>P</strong> (production).</td>
</tr>
<tr class="even">
<td>12</td>
<td>8</td>
<td>ID</td>
<td>R</td>
<td></td>
<td>0104</td>
<td>Version ID</td>
<td>Version ID field of event protocol in Protocol file.</td>
</tr>
<tr class="odd">
<td>13</td>
<td>15</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Sequence Number</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>14</td>
<td>180</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Continuation Pointer</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>15</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td>0155</td>
<td>Accept Acknowledgment Type</td>
<td><strong>NE</strong> (never acknowledge).</td>
</tr>
<tr class="even">
<td>16</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td>0155</td>
<td>Application Acknowledgment Type</td>
<td><strong>AL</strong> (always acknowledge).</td>
</tr>
<tr class="odd">
<td>17</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td>Country Code</td>
<td><strong>USA</strong>.</td>
</tr>
<tr class="even">
<td>18</td>
<td>6</td>
<td>ID</td>
<td></td>
<td>Y/3</td>
<td>0211</td>
<td>Character Set</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>19</td>
<td>60</td>
<td>CE</td>
<td></td>
<td></td>
<td></td>
<td>Principal Language of Message</td>
<td>Not used.</td>
</tr>
</tbody>
</table>

<span id="_Ref58244447" class="anchor"></span>Table 100: PID—Patient Identification Segment

### PID—Patient Identification Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Ref58244535" class="anchor"></span>Table 101: PDI—Patient Additional Demographic Segment</p></caption>
<colgroup>
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 24%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th>SEQ</th>
<th>LEN</th>
<th>DT</th>
<th>R/O</th>
<th>RP/#</th>
<th>TBL#</th>
<th>Element Name</th>
<th>VistA Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>4</td>
<td>SI</td>
<td></td>
<td></td>
<td></td>
<td>Set ID - Patient ID</td>
<td>Always set to “<strong>1</strong>”.</td>
</tr>
<tr class="even">
<td>2</td>
<td>20</td>
<td>CK</td>
<td></td>
<td></td>
<td></td>
<td>Patient ID (External ID)</td>
<td>Social Security Number field of PATIENT (#2) file.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>20</td>
<td>CM</td>
<td>R</td>
<td>Y</td>
<td></td>
<td>Patient ID (Internal ID)</td>
<td><p>Integrated Control Number (ICN) field in the PATIENT (#2) file:</p>
<ul>
<li><p>Component 1: ICN w/checksum</p></li>
<li><p>Component 2: DFN</p></li>
<li><p>Component 3: <strong>NULL</strong></p></li>
<li><p>Component 4: Assigning authority (subcomponent 1: ‘USVHA’, subcomponent 3: “<strong>L</strong>”.</p></li>
<li><p>Component 5: Type “<strong>NI</strong>”.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>4</td>
<td>12</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Alternate Patient ID</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>5</td>
<td>48</td>
<td>PN</td>
<td>R</td>
<td></td>
<td></td>
<td>Patient Name</td>
<td>Name.</td>
</tr>
<tr class="even">
<td>6</td>
<td>30</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Mother's Maiden Name</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>7</td>
<td>26</td>
<td>TS</td>
<td></td>
<td></td>
<td></td>
<td>Date of Birth</td>
<td>Date of birth.</td>
</tr>
<tr class="even">
<td>8</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td>0001</td>
<td>Sex</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>9</td>
<td>48</td>
<td>PN</td>
<td></td>
<td>Y</td>
<td></td>
<td>Patient Alias</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>10</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td>0005</td>
<td>Race</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>11</td>
<td>106</td>
<td>AD</td>
<td></td>
<td>Y</td>
<td></td>
<td>Patient Address</td>
<td>Home Address.</td>
</tr>
<tr class="even">
<td>12</td>
<td>4</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td>County Code</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>13</td>
<td>40</td>
<td>TN</td>
<td></td>
<td>Y</td>
<td></td>
<td>Phone Number – Home</td>
<td>Home Phone Validated.</td>
</tr>
<tr class="even">
<td>14</td>
<td>40</td>
<td>TN</td>
<td></td>
<td>Y</td>
<td></td>
<td>Phone Number – Business</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>15</td>
<td>25</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Language – Patient</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>16</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td>0002</td>
<td>Marital Status</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>17</td>
<td>3</td>
<td>ID</td>
<td></td>
<td></td>
<td>0006</td>
<td>Religion</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>18</td>
<td>20</td>
<td>CK</td>
<td></td>
<td></td>
<td></td>
<td>Patient Account Number</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>19</td>
<td>16</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>SSN Number – Patient</td>
<td>Social security number and pseudo indicator.</td>
</tr>
<tr class="even">
<td>20</td>
<td>25</td>
<td>CM</td>
<td></td>
<td></td>
<td></td>
<td>Driver's Lic Num – Patient</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>21</td>
<td>20</td>
<td>CK</td>
<td></td>
<td></td>
<td></td>
<td>Mother's Identifier</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>22</td>
<td>1</td>
<td>ID</td>
<td></td>
<td></td>
<td>0189</td>
<td>Ethnic Group</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>23</td>
<td>25</td>
<td>ST</td>
<td></td>
<td></td>
<td></td>
<td>Birth Place</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>24</td>
<td>2</td>
<td>ID</td>
<td></td>
<td></td>
<td></td>
<td>Multiple Birth Indicator</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>25</td>
<td>2</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>Birth Order</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>26</td>
<td>3</td>
<td>ID</td>
<td></td>
<td>Y</td>
<td>0171</td>
<td>Citizenship</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>27</td>
<td>60</td>
<td>CE</td>
<td></td>
<td></td>
<td>0172</td>
<td>Veterans Military Status</td>
<td>Not used.</td>
</tr>
</tbody>
</table>

<span id="_Ref58244535" class="anchor"></span>Table 101: PDI—Patient Additional Demographic Segment

### PD1—Patient Additional Demographic Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| SEQ | LEN | DT  | OPT | RP/# | TBL# | ITEM# | Element Name                                |
|-----|-----|-----|-----|------|------|-------|---------------------------------------------|
| 1   | 2   | IS  | O   | Y    | 0223 | 00755 | Living Dependency                           |
| 2   | 2   | IS  | O   |      | 0220 | 00742 | Living Arrangement                          |
| 3   | 250 | XON | O   | Y    |      | 00756 | Patient Primary Facility                    |
| 4   | 250 | XCN | B   | Y    |      | 00757 | Patient Primary Care Provider Name & ID No. |
| 5   | 2   | IS  | O   |      | 0231 | 00745 | Student Indicator                           |
| 6   | 2   | IS  | O   |      | 0295 | 00753 | Handicap                                    |
| 7   | 2   | IS  | O   |      | 0315 | 00759 | Living Will Code                            |
| 8   | 2   | IS  | O   |      | 0316 | 00760 | Organ Donor Code                            |
| 9   | 1   | ID  | O   |      | 0136 | 00761 | Separate Bill                               |
| 10  | 250 | CX  | O   | Y    |      | 00762 | Duplicate Patient                           |
| 11  | 250 | CE  | O   |      | 0215 | 00743 | Publicity Code                              |
| 12  | 1   | ID  | O   |      | 0136 | 00744 | Protection Indicator                        |
| 13  | 8   | DT  | O   |      |      | 01566 | Protection Indicator Effective Date         |
| 14  | 250 | XON | O   | Y    |      | 01567 | Place of Worship                            |
| 15  | 250 | CE  | O   | Y    | 0435 | 01568 | Advance Directive Code                      |
| 16  | 1   | IS  | O   |      | 0441 | 01569 | Immunization Registry Status                |
| 17  | 8   | DT  | O   |      |      | 01570 | Immunization Registry Status Effective Date |
| 18  | 8   | DT  | O   |      |      | 01571 | Publicity Code Effective Date               |
| 19  | 5   | IS  | O   |      | 0140 | 01572 | Military Branch                             |
| 20  | 2   | IS  | O   |      | 0141 | 00486 | Military Rank/Grade                         |
| 21  | 3   | IS  | O   |      | 0142 | 01573 | Military Status                             |

<span id="_Ref58244584" class="anchor"></span>Table 102: PVI—Patient Visit Segment

### PV1—Patient Visit Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| SEQ | LEN | DT  | OPT | RP/# | TBL#                                                                                                                                                                                                                                                                                                                                               | ITEM# | Element Name              |
|-----|-----|-----|-----|------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------|---------------------------|
| 1   | 4   | SI  | O   |      |                                                                                                                                                                                                                                                                                                                                                    | 00131 | Set ID - PV1              |
| 2   | 1   | IS  | R   |      | 0004                                                                                                                                                                                                                                                                                                                                               | 00132 | Patient Class             |
| 3   | 80  | PL  | O   |      |                                                                                                                                                                                                                                                                                                                                                    | 00133 | Assigned Patient Location |
| 4   | 2   | IS  | O   |      | 0007                                                                                                                                                                                                                                                                                                                                               | 00134 | Admission Type            |
| 5   | 250 | CX  | O   |      |                                                                                                                                                                                                                                                                                                                                                    | 00135 | Preadmit Number           |
| 6   | 80  | PL  | O   |      |                                                                                                                                                                                                                                                                                                                                                    | 00136 | Prior Patient Location    |
| 7   | 250 | XCN | O   | Y    | 0010                                                                                                                                                                                                                                                                                                                                               | 00137 | Attending Doctor          |
| 8   | 250 | XCN | O   | Y    | 0010                                                                                                                                                                                                                                                                                                                                               | 00138 | Referring Doctor          |
| 9   | 250 | XCN | B   | Y    | 0010                                                                                                                                                                                                                                                                                                                                               | 00139 | Consulting Doctor         |
| 10  | 3   | IS  | O   |      | 0069                                                                                                                                                                                                                                                                                                                                               | 00140 | Hospital Service          |
| 11  | 80  | PL  | O   |      |                                                                                                                                                                                                                                                                                                                                                    | 00141 | Temporary Location        |
| 12  | 2   | IS  | O   |      | 0087                                                                                                                                                                                                                                                                                                                                               | 00142 | Preadmit Test Indicator   |
| 13  | 2   | IS  | O   |      | 0092                                                                                                                                                                                                                                                                                                                                               | 00143 | Re-admission Indicator    |
| 14  | 6   | IS  | O   |      | 0023                                                                                                                                                                                                                                                                                                                                               | 00144 | Admit Source              |
| 15  | 2   | IS  | O   | Y    | [0009](https://vaww.oed.portal.va.gov/pm/hppmd/ETS/Lists/Service%20Request/AppData/Local/Microsoft/vhaisbadamsr/AppData/Local/Microsoft/Windows/Temporary%20Internet%20Files/AppData/Local/Microsoft/Windows/vhaisbadamsr/AppData/Local/Microsoft/Users/vhaisbadamsr/AppData/Local/Microsoft/Users/vhaispsteelr/Local%20Settings/Temporary%20Inte) | 00145 | Ambulatory Status         |
| 16  | 2   | IS  | O   |      | 0099                                                                                                                                                                                                                                                                                                                                               | 00146 | VIP Indicator             |
| 17  | 250 | XCN | O   | Y    | 0010                                                                                                                                                                                                                                                                                                                                               | 00147 | Admitting Doctor          |
| 18  | 2   | IS  | O   |      | 0018                                                                                                                                                                                                                                                                                                                                               | 00148 | Patient Type              |
| 19  | 250 | CX  | O   |      |                                                                                                                                                                                                                                                                                                                                                    | 00149 | Visit Number              |
| 20  | 50  | FC  | O   | Y    | 0064                                                                                                                                                                                                                                                                                                                                               | 00150 | Financial Class           |
| 21  | 2   | IS  | O   |      | 0032                                                                                                                                                                                                                                                                                                                                               | 00151 | Charge Price Indicator    |
| 22  | 2   | IS  | O   |      | 0045                                                                                                                                                                                                                                                                                                                                               | 00152 | Courtesy Code             |
| 23  | 2   | IS  | O   |      | 0046                                                                                                                                                                                                                                                                                                                                               | 00153 | Credit Rating             |
| 24  | 2   | IS  | O   | Y    | 0044                                                                                                                                                                                                                                                                                                                                               | 00154 | Contract Code             |
| 25  | 8   | DT  | O   | Y    |                                                                                                                                                                                                                                                                                                                                                    | 00155 | Contract Effective Date   |
| 26  | 12  | NM  | O   | Y    |                                                                                                                                                                                                                                                                                                                                                    | 00156 | Contract Amount           |
| 27  | 3   | NM  | O   | Y    |                                                                                                                                                                                                                                                                                                                                                    | 00157 | Contract Period           |
| 28  | 2   | IS  | O   |      | 0073                                                                                                                                                                                                                                                                                                                                               | 00158 | Interest Code             |
| 29  | 4   | IS  | O   |      | 0110                                                                                                                                                                                                                                                                                                                                               | 00159 | Transfer to Bad Debt Code |
| 30  | 8   | DT  | O   |      |                                                                                                                                                                                                                                                                                                                                                    | 00160 | Transfer to Bad Debt Date |
| 31  | 10  | IS  | O   |      | 0021                                                                                                                                                                                                                                                                                                                                               | 00161 | Bad Debt Agency Code      |
| 32  | 12  | NM  | O   |      |                                                                                                                                                                                                                                                                                                                                                    | 00162 | Bad Debt Transfer Amount  |
| 33  | 12  | NM  | O   |      |                                                                                                                                                                                                                                                                                                                                                    | 00163 | Bad Debt Recovery Amount  |
| 34  | 1   | IS  | O   |      | 0111                                                                                                                                                                                                                                                                                                                                               | 00164 | Delete Account Indicator  |
| 35  | 8   | DT  | O   |      |                                                                                                                                                                                                                                                                                                                                                    | 00165 | Delete Account Date       |
| 36  | 3   | IS  | O   |      | 0112                                                                                                                                                                                                                                                                                                                                               | 00166 | Discharge Disposition     |
| 37  | 47  | DLD | O   |      | 0113                                                                                                                                                                                                                                                                                                                                               | 00167 | Discharged to Location    |
| 38  | 250 | CE  | O   |      | 0114                                                                                                                                                                                                                                                                                                                                               | 00168 | Diet Type                 |
| 39  | 2   | IS  | O   |      | 0115                                                                                                                                                                                                                                                                                                                                               | 00169 | Servicing Facility        |
| 40  | 1   | IS  | B   |      | 0116                                                                                                                                                                                                                                                                                                                                               | 00170 | Bed Status                |
| 41  | 2   | IS  | O   |      | 0117                                                                                                                                                                                                                                                                                                                                               | 00171 | Account Status            |
| 42  | 80  | PL  | O   |      |                                                                                                                                                                                                                                                                                                                                                    | 00172 | Pending Location          |
| 43  | 80  | PL  | O   |      |                                                                                                                                                                                                                                                                                                                                                    | 00173 | Prior Temporary Location  |
| 44  | 26  | TS  | O   |      |                                                                                                                                                                                                                                                                                                                                                    | 00174 | Admit Date/Time           |
| 45  | 26  | TS  | O   | Y    |                                                                                                                                                                                                                                                                                                                                                    | 00175 | Discharge Date/Time       |
| 46  | 12  | NM  | O   |      |                                                                                                                                                                                                                                                                                                                                                    | 00176 | Current Patient Balance   |
| 47  | 12  | NM  | O   |      |                                                                                                                                                                                                                                                                                                                                                    | 00177 | Total Charges             |
| 48  | 12  | NM  | O   |      |                                                                                                                                                                                                                                                                                                                                                    | 00178 | Total Adjustments         |
| 49  | 12  | NM  | O   |      |                                                                                                                                                                                                                                                                                                                                                    | 00179 | Total Payments            |
| 50  | 250 | CX  | O   |      | 0203                                                                                                                                                                                                                                                                                                                                               | 00180 | Alternate Visit ID        |
| 51  | 1   | IS  | O   |      | 0326                                                                                                                                                                                                                                                                                                                                               | 01226 | Visit Indicator           |
| 52  | 250 | XCN | B   | Y    | 0010                                                                                                                                                                                                                                                                                                                                               | 01274 | Other Healthcare Provider |

<span id="_Ref58244631" class="anchor"></span>Table 103: MSA—Message Acknowledgement Segment

### MSA—Message Acknowledgement Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| SEQ | LEN | DT  | R/O | RP/# | TBL# | Element Name                | VistA Description                                                 |
|-----|-----|-----|-----|------|------|-----------------------------|-------------------------------------------------------------------|
| 1   | 2   | ID  | R   |      | 0008 | Acknowledgment Code         | REF: See HL7 [Table 0008—Acknowledgment Code](#_Ref58237468). |
| 2   | 20  | ST  | R   |      |      | Message Control ID          | Message Control ID of the message being acknowledged.             |
| 3   | 80  | ST  | O   |      |      | Text Message                | Free text error message.                                          |
| 4   | 15  | NM  | O   |      |      | Expected Sequence Number    | Not used.                                                         |
| 5   | 1   | ID  | B   |      | 0102 | Delayed Acknowledgment Type | Not used.                                                         |
| 6   | 100 | CE  | O   |      |      | Error Condition             | Not used.                                                         |

<span id="_Ref58244790" class="anchor"></span>Table 104: SCH—Schedule Activity Information Segment

# HL7 Interface Specification for Patient Record Flags (PRF)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For HL7 interface specification for Patient Record Flags (PRF) functionality, see the Patient Record Flags HL7 Interface Specification document in the VA Software Document Library Patient Record Flags folder.

# HL7 Interface Specification for Community Care Referrals and Authorization (CCRA) Scheduling Actions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Community Care Referrals and Authorization (CCRA) appointment actions updates VistA to schedule, cancel, or update appointments in support of the HealthShare Referral Manager (HSRM) application. When an appointment is made or canceled, or if an appointment is updated as a No Show for a community care referral in HSRM, HSRM sends an HL7 message to VistA to update the VistA files with the appointment information. This information is then viewable in VistA Scheduling Options, CPRS, VS GUI, and other applications.

The formats of the HL7 messages conform to HL7 Version 2.5, Schedule Information Unsolicited (SIU) message type, the message structure is as follows:

- S12—Schedule an appointment.
- S15—Cancel and appointment.
- S26—Update the appointment as a NO SHOW by the patient.

## Assumptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The transmission of HSRM HL7 appointment messages assumes the following:

- VistA sites have patches GRMC\*3.0\*99 and GMRC\*3.0\*106 installed.
- All VistA systems have installed patch SD\*5.3\*707. This patch receives the HL7 messages from HSRM and processes the date.

## Message Content

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The scheduling messages contain only the data necessary to perform the scheduling action.

## HL7 Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- CCRA HSRM SIU-S12 CLIENT—This is the subscriber protocol that processes the make appointment message.
- CCRA HSRM SIU-S12 SERVER—This the event driver protocol that is triggered when a make appointment message is received.
- CCRA HSRM SIU-S15 CLIENT—This is the subscriber protocol that processes the cancel appointment message.
- CCRA HSRM SIU-S15 SERVER—This is the event driver protocol that is triggered when a cancel appointment message is received.
- CCRA HSRM SIU-S26 CLIENT—This is the subscriber protocol that processes the appointment update for a NO SHOW appointment action.
- CCRA HSRM SIU-S26 SERVER—This is the event driver protocol that is triggered when a NO SHOW update message is received.

## HL7 Application Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- SD-CCRA-HSRM—Defines the sending application parameters.
- SD-CCRA-VISTA—Defines the receiving application parameters.

## HL7 Messaging Segments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### SCH—Schedule Activity Information Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The SCH segment contains general information about the scheduled appointment.

<table>
<caption><p><span id="_Ref58244861" class="anchor"></span>Table 105: PID—Patient Information Segment</p></caption>
<colgroup>
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 9%" />
<col style="width: 23%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th>SEQ</th>
<th>LEN</th>
<th>DT</th>
<th>R/O/C</th>
<th>RP/#</th>
<th>TBL#</th>
<th>ITEM#</th>
<th>Element Name</th>
<th>VistA Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>75</td>
<td>EI</td>
<td>R</td>
<td></td>
<td></td>
<td>860</td>
<td>Placer Appointment ID</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>2</td>
<td>75</td>
<td>EI</td>
<td>C</td>
<td></td>
<td></td>
<td>861</td>
<td>Filler Appointment ID</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>3</td>
<td>5</td>
<td>NM</td>
<td>C</td>
<td></td>
<td></td>
<td>862</td>
<td>Occurrence Number</td>
<td>VistA consult ID.</td>
</tr>
<tr class="even">
<td>4</td>
<td>22</td>
<td>EI</td>
<td>O</td>
<td></td>
<td></td>
<td>218</td>
<td>Placer Group Number</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>5</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td></td>
<td></td>
<td>864</td>
<td>Schedule ID</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>6</td>
<td>250</td>
<td>CE</td>
<td>R</td>
<td></td>
<td></td>
<td>883</td>
<td>Event Reason</td>
<td>Scheduled or Canceled.</td>
</tr>
<tr class="odd">
<td>7</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td></td>
<td></td>
<td>866</td>
<td>Appointment Reason</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>8</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td></td>
<td></td>
<td>867</td>
<td>Appointment Type</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>9</td>
<td>20</td>
<td>NM</td>
<td></td>
<td></td>
<td></td>
<td>868</td>
<td>Appointment Duration</td>
<td>Appointment length.</td>
</tr>
<tr class="even">
<td>10</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td></td>
<td></td>
<td>869</td>
<td>Appointment Duration Units</td>
<td>Minutes or hours.</td>
</tr>
<tr class="odd">
<td>11</td>
<td>200</td>
<td>TQ</td>
<td>R</td>
<td>Y</td>
<td></td>
<td>884</td>
<td>Appointment Timing Quantity</td>
<td><p>^^^Appointment Start Date Time^Appointment.</p>
<p>End Date Time.</p></td>
</tr>
<tr class="even">
<td>12</td>
<td>250</td>
<td>XCN</td>
<td>O</td>
<td>Y</td>
<td></td>
<td>874</td>
<td>Placer Contact Person</td>
<td><p>^Provider Last.</p>
<p>Name^Provider First Name.</p></td>
</tr>
<tr class="odd">
<td>13</td>
<td>250</td>
<td>XTN</td>
<td>O</td>
<td></td>
<td></td>
<td>875</td>
<td>Placer Contact Phone Number</td>
<td>^^^Scheduler's VA exchange email.</td>
</tr>
<tr class="even">
<td>14</td>
<td>250</td>
<td>XAD</td>
<td>O</td>
<td>Y</td>
<td></td>
<td>876</td>
<td>Placer Contact Address</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>15</td>
<td>80</td>
<td>PL</td>
<td>O</td>
<td></td>
<td></td>
<td>877</td>
<td>Placer Contact Location</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>16</td>
<td>250</td>
<td>XCN</td>
<td>R</td>
<td>Y</td>
<td></td>
<td>885</td>
<td>Filler Contact Person</td>
<td>DUZ^name of person that scheduled the appointment.</td>
</tr>
<tr class="odd">
<td>17</td>
<td>250</td>
<td>XTN</td>
<td>O</td>
<td></td>
<td></td>
<td>886</td>
<td>Filler Contact Phone Number</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>18</td>
<td>250</td>
<td>XAD</td>
<td>O</td>
<td></td>
<td></td>
<td>887</td>
<td>Filler Contact Address</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>19</td>
<td>80</td>
<td>PL</td>
<td>O</td>
<td></td>
<td></td>
<td>888</td>
<td>Filler Contact Location</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>20</td>
<td>250</td>
<td>XCN</td>
<td>R</td>
<td>Y</td>
<td></td>
<td>878</td>
<td>Entered by Person</td>
<td>Free text scheduler name.</td>
</tr>
<tr class="odd">
<td>21</td>
<td>250</td>
<td>XTN</td>
<td>O</td>
<td>Y</td>
<td></td>
<td>879</td>
<td>Entered by Phone Number</td>
<td>Not Used.</td>
</tr>
<tr class="even">
<td>22</td>
<td>80</td>
<td>PL</td>
<td>O</td>
<td></td>
<td></td>
<td>880</td>
<td>Entered by Location</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>23</td>
<td>75</td>
<td>EI</td>
<td>O</td>
<td></td>
<td></td>
<td>881</td>
<td>Parent Placer Appointment ID</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>24</td>
<td>75</td>
<td>EI</td>
<td>O</td>
<td></td>
<td></td>
<td>882</td>
<td>Parent Filler Appointment ID</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>25</td>
<td>250</td>
<td>CE</td>
<td>R</td>
<td></td>
<td></td>
<td>889</td>
<td>Filler Status Code</td>
<td>Scheduled or Canceled.</td>
</tr>
<tr class="even">
<td>26</td>
<td>22</td>
<td>EI</td>
<td>C</td>
<td>Y</td>
<td></td>
<td>216</td>
<td>PLACER ORDER NUMBER</td>
<td>Not Used.</td>
</tr>
<tr class="odd">
<td>27</td>
<td>22</td>
<td>EI</td>
<td>C</td>
<td>Y</td>
<td></td>
<td>217</td>
<td>FILLER ORDER NUMBER</td>
<td>Not Used.</td>
</tr>
</tbody>
</table>

<span id="_Ref58244861" class="anchor"></span>Table 105: PID—Patient Information Segment

### PID—Patient Information Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PID segment has patient identification information.

| SEQ | LEN | DT  | OPT | RP/# | TBL# | ITEM# | Element Name                      | VistA Description                       |
|-----|-----|-----|-----|------|------|-------|-----------------------------------|-----------------------------------------|
| 1   | 4   | SI  | O   |      |      | 104   | Set ID - PID                      | Not used.                               |
| 2   | 20  | CX  | B   |      |      | 105   | Patient ID                        | Not used.                               |
| 3   | 250 | CX  | R   | Y    |      | 106   | Patient Identifier List           | Patient ICN^^^USAVHA^NI~DFN.            |
| 4   | 20  | CX  | B   | Y    |      | 107   | Alternate Patient ID - PID        | Not used.                               |
| 5   | 250 | XPN | R   | Y    |      | 108   | Patient Name                      | Last Name^First Name^MI^^^^^L.          |
| 6   | 250 | XPN | O   | Y    |      | 109   | Mother’s Maiden Name              | Not used.                               |
| 7   | 26  | TS  | O   |      |      | 110   | Date/Time of Birth                | Patient Date of Birth.                  |
| 8   | 1   | IS  | O   |      | 1    | 111   | Administrative Sex                | Patient’s Gender.                       |
| 9   | 250 | XPN | B   | Y    |      | 112   | Patient Alias                     | Not used.                               |
| 10  | 250 | CE  | O   | Y    | 5    | 113   | Race                              | Not used.                               |
| 11  | 250 | XAD | O   | Y    |      | 114   | Patient Address                   | Not used.                               |
| 12  | 4   | IS  | B   |      | 289  | 115   | County Code                       | Not used.                               |
| 13  | 250 | XTN | O   | Y    |      | 116   | Phone Number - Home               | Not used.                               |
| 14  | 250 | XTN | O   | Y    |      | 117   | Phone Number - Business           | Not used.                               |
| 15  | 250 | CE  | O   |      | 296  | 118   | Primary Language                  | Not used.                               |
| 16  | 250 | CE  | O   |      | 2    | 119   | Marital Status                    | Not used.                               |
| 17  | 250 | CE  | O   |      | 6    | 120   | Religion                          | Not used.                               |
| 18  | 250 | CX  | O   |      |      | 121   | Patient Account Number            | Consult ID related to this appointment. |
| 19  | 16  | ST  | B   |      |      | 122   | SSN Number - Patient              | Not used.                               |
| 20  | 25  | DLN | O   |      |      | 123   | Driver's License Number - Patient | Not used.                               |
| 21  | 250 | CX  | O   | Y    |      | 124   | Mother's Identifier               | Not used.                               |
| 22  | 250 | CE  | O   | Y    | 189  | 125   | Ethnic Group                      | Not used.                               |
| 23  | 250 | ST  | O   |      |      | 126   | Birth Place                       | Not used.                               |
| 24  | 1   | ID  | O   |      | 136  | 127   | Multiple Birth Indicator          | Not used.                               |
| 25  | 2   | NM  | O   |      |      | 128   | Birth Order                       | Not used.                               |
| 26  | 250 | CE  | O   | Y    | 171  | 129   | Citizenship                       | Not used.                               |
| 27  | 250 | CE  | O   |      | 172  | 130   | Veterans Military Status          | Not used.                               |
| 28  | 250 | CE  | B   |      | 212  | 739   | Nationality                       | Not used.                               |
| 29  | 26  | TS  | O   |      |      | 740   | Patient Death Date and Time       | Not used.                               |
| 30  | 1   | ID  | O   |      | 136  | 741   | Patient Death Indicator           | Not used.                               |
| 31  | 1   | ID  | O   |      | 136  | 1535  | Identity Unknown Indicator        | Not used.                               |
| 32  | 20  | IS  | O   | Y    | 445  | 1536  | Identity Reliability Code         | Not used.                               |
| 33  | 26  | TS  | O   |      |      | 1537  | Last Update Date/Time             | Not used.                               |
| 34  | 40  | HD  | O   |      |      | 1538  | Last Update Facility              | Not used.                               |
| 35  | 250 | CE  | C   |      | 446  | 1539  | Species Code                      | Not used.                               |
| 36  | 250 | CE  | C   |      | 447  | 1540  | Breed Code                        | Not used.                               |
| 37  | 80  | ST  | O   |      |      | 1541  | Strain                            | Not used.                               |
| 38  | 250 | CE  | O   | 2    | 429  | 1542  | Production Class Code             | Not used.                               |

<span id="_Ref58244915" class="anchor"></span>Table 106: PV1—Patient Visit Segment

### PV1—Patient Visit Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The PV1 segment has the patient visit information.

| SEQ | LEN | DT  | OPT | RP/# | TBL# | ITEM# | Element Name              | VistA Description      |
|-----|-----|-----|-----|------|------|-------|---------------------------|------------------------|
| 1   | 4   | SI  | O   |      |      | 131   | Set ID - PV1              | Not used.              |
| 2   | 1   | IS  | R   |      | 4    | 132   | Patient Class             | Not used.              |
| 3   | 80  | PL  | O   |      |      | 133   | Assigned Patient Location | Not used.              |
| 4   | 2   | IS  | O   |      | 7    | 134   | Admission Type            | Not used.              |
| 5   | 250 | CX  | O   |      |      | 135   | Preadmit Number           | Not used.              |
| 6   | 80  | PL  | O   |      |      | 136   | Prior Patient Location    | Not used.              |
| 7   | 250 | XCN | O   | Y    | 10   | 137   | Attending Doctor          | Not used.              |
| 8   | 250 | XCN | O   | Y    | 10   | 138   | Referring Doctor          | Not used.              |
| 9   | 250 | XCN | B   | Y    | 10   | 139   | Consulting Doctor         | Not used.              |
| 10  | 3   | IS  | O   |      | 69   | 140   | Hospital Service          | Not used.              |
| 11  | 80  | PL  | O   |      |      | 141   | Temporary Location        | Not used.              |
| 12  | 2   | IS  | O   |      | 87   | 142   | Preadmit Test Indicator   | Not used.              |
| 13  | 2   | IS  | O   |      | 92   | 143   | Re-admission Indicator    | Not used.              |
| 14  | 6   | IS  | O   |      | 23   | 144   | Admit Source              | Not used.              |
| 15  | 2   | IS  | O   | Y    | 9    | 145   | Ambulatory Status         | Not used.              |
| 16  | 2   | IS  | O   |      | 99   | 146   | VIP Indicator             | Not used.              |
| 17  | 250 | XCN | O   | Y    | 10   | 147   | Admitting Doctor          | Not used.              |
| 18  | 2   | IS  | O   |      | 18   | 148   | Patient Type              | Not used.              |
| 19  | 250 | CX  | O   |      |      | 149   | Visit Number              | VistA Consult Id.      |
| 20  | 50  | FC  | O   | Y    | 64   | 150   | Financial Class           | Not used.              |
| 21  | 2   | IS  | O   |      | 32   | 151   | Charge Price Indicator    | Not used.              |
| 22  | 2   | IS  | O   |      | 45   | 152   | Courtesy Code             | Not used.              |
| 23  | 2   | IS  | O   |      | 46   | 153   | Credit Rating             | Not used.              |
| 24  | 2   | IS  | O   | Y    | 44   | 154   | Contract Code             | Not used.              |
| 25  | 8   | DT  | O   | Y    |      | 155   | Contract Effective Date   | Not used.              |
| 26  | 12  | NM  | O   | Y    |      | 156   | Contract Amount           | Not used.              |
| 27  | 3   | NM  | O   | Y    |      | 157   | Contract Period           | Not used.              |
| 28  | 2   | IS  | O   |      | 73   | 158   | Interest Code             | Not used.              |
| 29  | 1   | IS  | O   |      | 110  | 159   | Transfer to Bad Debt Code | Not used.              |
| 30  | 8   | DT  | O   |      |      | 160   | Transfer to Bad Debt Date | Not used.              |
| 31  | 10  | IS  | O   |      | 21   | 161   | Bad Debt Agency Code      | Not used.              |
| 32  | 12  | NM  | O   |      |      | 162   | Bad Debt Transfer Amount  | Not used.              |
| 33  | 12  | NM  | O   |      |      | 163   | Bad Debt Recovery Amount  | Not used.              |
| 34  | 1   | IS  | O   |      | 111  | 164   | Delete Account Indicator  | Not used.              |
| 35  | 8   | DT  | O   |      |      | 165   | Delete Account Date       | Not used.              |
| 36  | 3   | IS  | O   |      | 112  | 166   | Discharge Disposition     | Not used.              |
| 37  | 25  | CM  | O   |      | 113  | 167   | Discharged to Location    | Not used.              |
| 38  | 250 | CE  | O   |      | 114  | 168   | Diet Type                 | Not used.              |
| 39  | 2   | IS  | O   |      | 115  | 169   | Servicing Facility        | Not used.              |
| 40  | 1   | IS  | B   |      | 116  | 170   | Bed Status                | Not used.              |
| 41  | 2   | IS  | O   |      | 117  | 171   | Account Status            | Not used.              |
| 42  | 80  | PL  | O   |      |      | 172   | Pending Location          | Not used.              |
| 43  | 80  | PL  | O   |      |      | 173   | Prior Temporary Location  | Not used.              |
| 44  | 26  | TS  | O   |      |      | 174   | Admit Date/Time           | Appointment Date/Time. |
| 45  | 26  | TS  | O   | Y    |      | 175   | Discharge Date/Time       | Not used.              |
| 46  | 12  | NM  | O   |      |      | 176   | Current Patient Balance   | Not used.              |
| 47  | 12  | NM  | O   |      |      | 177   | Total Charges             | Not used.              |
| 48  | 12  | NM  | O   |      |      | 178   | Total Adjustments         | Not used.              |
| 49  | 12  | NM  | O   |      |      | 179   | Total Payments            | Not used.              |
| 50  | 250 | CX  | O   |      | 203  | 180   | Alternate Visit ID        | Not used.              |
| 51  | 1   | IS  | O   |      | 326  | 1226  | Visit Indicator           | Not used.              |
| 52  | 250 | XCN | B   | Y    | 10   | 1274  | Other Healthcare Provider | Not used.              |

<span id="_Ref58244961" class="anchor"></span>Table 107: RGS—Resource Group Segment

### RGS—Resource Group Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RGS segment is the appointment grouper segment.

<table>
<caption><p><span id="_Ref58245007" class="anchor"></span>Table 108: AIS—Appointment Information Segment</p></caption>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 5%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 20%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th>SEQ</th>
<th>LEN</th>
<th>DT</th>
<th>OPT</th>
<th>RP/#</th>
<th>TBL#</th>
<th>ITEM#</th>
<th>Element Name</th>
<th>VistA Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>4</td>
<td>SI</td>
<td>R</td>
<td></td>
<td></td>
<td>1203</td>
<td>Set ID - RGS</td>
<td><strong>1</strong></td>
</tr>
<tr class="even">
<td>2</td>
<td>3</td>
<td>ID</td>
<td>C</td>
<td></td>
<td>206</td>
<td>763</td>
<td>Segment Action Code</td>
<td><ul>
<li><p><strong>A</strong>—Add/Insert</p></li>
<li><p><strong>D</strong>—Delete</p></li>
<li><p><strong>U</strong>—Update</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>3</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td></td>
<td></td>
<td>1204</td>
<td>Resource Group ID</td>
<td>Not used.</td>
</tr>
</tbody>
</table>

<span id="_Ref58245007" class="anchor"></span>Table 108: AIS—Appointment Information Segment

### AIS—Appointment Information Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The AIS segment contains information about the appointment.

<table>
<caption><p><span id="_Ref58245067" class="anchor"></span>Table 109: AIG—Appointment Insurance Segment</p></caption>
<colgroup>
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 5%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 9%" />
<col style="width: 21%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th>SEQ</th>
<th>LEN</th>
<th>DT</th>
<th>OPT</th>
<th>RP/#</th>
<th>TBL#</th>
<th>ITEM#</th>
<th>Element Name</th>
<th>VistA Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>4</td>
<td>SI</td>
<td>R</td>
<td></td>
<td></td>
<td>890</td>
<td>Set ID - AIS</td>
<td>Segment Sequence Number.</td>
</tr>
<tr class="even">
<td>2</td>
<td>3</td>
<td>ID</td>
<td>C</td>
<td></td>
<td>206</td>
<td>763</td>
<td>Segment Action Code</td>
<td><ul>
<li><p><strong>A</strong>—Add/Insert</p></li>
<li><p><strong>D</strong>—Delete</p></li>
<li><p><strong>U</strong>—Update</p></li>
</ul>
<p>Make appointment is <strong>A</strong>.</p>
<p>Cancel appointment is <strong>D</strong>.</p></td>
</tr>
<tr class="odd">
<td>3</td>
<td>250</td>
<td>CE</td>
<td>R</td>
<td></td>
<td></td>
<td>238</td>
<td>Universal Service Identifier</td>
<td>ICD Code^Provisional Diagnosis.</td>
</tr>
<tr class="even">
<td>4</td>
<td>26</td>
<td>TS</td>
<td>C</td>
<td></td>
<td></td>
<td>1202</td>
<td>Start Date/Time</td>
<td>Appointment start date time in UTC.</td>
</tr>
<tr class="odd">
<td>5</td>
<td>20</td>
<td>NM</td>
<td>C</td>
<td></td>
<td></td>
<td>891</td>
<td>Start Date/Time Offset</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>6</td>
<td>250</td>
<td>CE</td>
<td>C</td>
<td></td>
<td></td>
<td>892</td>
<td>Start Date/Time Offset Units</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>7</td>
<td>20</td>
<td>NM</td>
<td>O</td>
<td></td>
<td></td>
<td>893</td>
<td>Duration</td>
<td>Length of appointment.</td>
</tr>
<tr class="even">
<td>8</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td></td>
<td></td>
<td>894</td>
<td>Duration Units</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>9</td>
<td>10</td>
<td>IS</td>
<td>C</td>
<td></td>
<td>279</td>
<td>895</td>
<td>Allow Substitution Code</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>10</td>
<td>250</td>
<td>CE</td>
<td>C</td>
<td></td>
<td>278</td>
<td>889</td>
<td>Filler Status Code</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>11</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td>Y</td>
<td>411</td>
<td>1474</td>
<td>Placer Supplemental Service Information</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>12</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td>Y</td>
<td>411</td>
<td>1475</td>
<td>Filler Supplemental Service Information</td>
<td>Not used.</td>
</tr>
</tbody>
</table>

<span id="_Ref58245067" class="anchor"></span>Table 109: AIG—Appointment Insurance Segment

### AIG—Appointment Insurance Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table style="width:100%;">
<caption><p><span id="_Ref58245102" class="anchor"></span>Table 110: AIL—Appointment Location Segment</p></caption>
<colgroup>
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 5%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 9%" />
<col style="width: 19%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th>SEQ</th>
<th>LEN</th>
<th>DT</th>
<th>OPT</th>
<th>RP/#</th>
<th>TBL#</th>
<th>ITEM#</th>
<th>Element Name</th>
<th>VistA Data Element</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>4</td>
<td>SI</td>
<td>R</td>
<td></td>
<td></td>
<td>896</td>
<td>Set ID - AIG</td>
<td>Segment Sequence Number.</td>
</tr>
<tr class="even">
<td>2</td>
<td>3</td>
<td>ID</td>
<td>C</td>
<td></td>
<td>206</td>
<td>763</td>
<td>Segment Action Code</td>
<td><ul>
<li><p><strong>A</strong>—Add</p></li>
<li><p><strong>D</strong>—Delete</p></li>
<li><p><strong>U</strong>—Update</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>3</td>
<td>250</td>
<td>CE</td>
<td>C</td>
<td></td>
<td></td>
<td>897</td>
<td>Resource ID</td>
<td>Provider Name.</td>
</tr>
<tr class="even">
<td>4</td>
<td>250</td>
<td>CE</td>
<td>R</td>
<td></td>
<td></td>
<td>898</td>
<td>Resource Type</td>
<td>Provider.</td>
</tr>
<tr class="odd">
<td>5</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td>Y</td>
<td></td>
<td>899</td>
<td>Resource Group</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>6</td>
<td>5</td>
<td>NM</td>
<td>O</td>
<td></td>
<td></td>
<td>900</td>
<td>Resource Quantity</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>7</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td></td>
<td></td>
<td>901</td>
<td>Resource Quantity Units</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>8</td>
<td>26</td>
<td>TS</td>
<td>C</td>
<td></td>
<td></td>
<td>1202</td>
<td>Start Date/Time</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>9</td>
<td>20</td>
<td>NM</td>
<td>C</td>
<td></td>
<td></td>
<td>891</td>
<td>Start Date/Time Offset</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>10</td>
<td>250</td>
<td>CE</td>
<td>C</td>
<td></td>
<td></td>
<td>892</td>
<td>Start Date/Time Offset Units</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>11</td>
<td>20</td>
<td>NM</td>
<td>O</td>
<td></td>
<td></td>
<td>893</td>
<td>Duration</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>12</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td></td>
<td></td>
<td>894</td>
<td>Duration Units</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>13</td>
<td>10</td>
<td>IS</td>
<td>C</td>
<td></td>
<td>279</td>
<td>895</td>
<td>Allow Substitution Code</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>14</td>
<td>250</td>
<td>CE</td>
<td>C</td>
<td></td>
<td>278</td>
<td>889</td>
<td>Filler Status Code</td>
<td>Not used.</td>
</tr>
</tbody>
</table>

<span id="_Ref58245102" class="anchor"></span>Table 110: AIL—Appointment Location Segment

### AIL—Appointment Location Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<caption><p><span id="_Ref58245143" class="anchor"></span>Table 111: AIP—Appointment Provider Segment</p></caption>
<colgroup>
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 10%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 9%" />
<col style="width: 16%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th>SEQ</th>
<th>LEN</th>
<th>DT</th>
<th>OPT</th>
<th>RP/#</th>
<th>TBL#</th>
<th>ITEM#</th>
<th>Element Name</th>
<th>VistA Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>4</td>
<td>SI</td>
<td>R</td>
<td></td>
<td></td>
<td>902</td>
<td>Set ID - AIL</td>
<td>Segment Sequence Number.</td>
</tr>
<tr class="even">
<td>2</td>
<td>3</td>
<td>ID</td>
<td>C</td>
<td></td>
<td>206</td>
<td>763</td>
<td>Segment Action Code</td>
<td><ul>
<li><p><strong>A</strong>—Add</p></li>
<li><p><strong>D</strong>—Cancel</p></li>
<li><p><strong>U</strong>—Update</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>3</td>
<td>80</td>
<td>PL</td>
<td>C</td>
<td></td>
<td></td>
<td>903</td>
<td>Location Resource ID</td>
<td>Consult Title.</td>
</tr>
<tr class="even">
<td>4</td>
<td>250</td>
<td>CE</td>
<td>R</td>
<td></td>
<td></td>
<td>904</td>
<td>Location Type- AIL</td>
<td>Consult Title.</td>
</tr>
<tr class="odd">
<td>5</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td></td>
<td></td>
<td>905</td>
<td>Location Group</td>
<td>Not Used.</td>
</tr>
<tr class="even">
<td>6</td>
<td>26</td>
<td>TS</td>
<td>C</td>
<td></td>
<td></td>
<td>1202</td>
<td>Start Date/Time</td>
<td>Not Used.</td>
</tr>
<tr class="odd">
<td>7</td>
<td>20</td>
<td>NM</td>
<td>C</td>
<td></td>
<td></td>
<td>891</td>
<td>Start Date/Time Offset</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>8</td>
<td>250</td>
<td>CE</td>
<td>C</td>
<td></td>
<td></td>
<td>892</td>
<td>Start Date/Time Offset Units</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>9</td>
<td>20</td>
<td>NM</td>
<td>O</td>
<td></td>
<td></td>
<td>893</td>
<td>Duration</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>10</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td></td>
<td></td>
<td>894</td>
<td>Duration Units</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>11</td>
<td>10</td>
<td>IS</td>
<td>C</td>
<td></td>
<td>279</td>
<td>895</td>
<td>Allow Substitution Code</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>12</td>
<td>250</td>
<td>CE</td>
<td>C</td>
<td></td>
<td>278</td>
<td>889</td>
<td>Filler Status Code</td>
<td>Not used.</td>
</tr>
</tbody>
</table>

<span id="_Ref58245143" class="anchor"></span>Table 111: AIP—Appointment Provider Segment

### AIP—Appointment Provider Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table style="width:100%;">
<caption><p><span id="_Toc193958139" class="anchor"></span>Table 112: Glossary</p></caption>
<colgroup>
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 25%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th>SEQ</th>
<th>LEN</th>
<th>DT</th>
<th>OPT</th>
<th>RP/#</th>
<th>TBL#</th>
<th>ITEM#</th>
<th>Element Name</th>
<th>VistA Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td>4</td>
<td>SI</td>
<td>R</td>
<td></td>
<td></td>
<td>906</td>
<td>Set ID - AIP</td>
<td>Segment Sequence Number.</td>
</tr>
<tr class="even">
<td>2</td>
<td>3</td>
<td>ID</td>
<td>C</td>
<td></td>
<td>206</td>
<td>763</td>
<td>Segment Action code</td>
<td><ul>
<li><p><strong>A</strong>—Add</p></li>
<li><p><strong>D</strong>—Delete</p></li>
<li><p><strong>U</strong>—Update</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>3</td>
<td>250</td>
<td>XCN</td>
<td>C</td>
<td>Y</td>
<td></td>
<td>913</td>
<td>Personnel Resource ID</td>
<td><p>Provider DUZ^^Provider Last.</p>
<p>Name^Provider First Name.</p></td>
</tr>
<tr class="even">
<td>4</td>
<td>250</td>
<td>CE</td>
<td>R</td>
<td></td>
<td></td>
<td>907</td>
<td>Resource Role</td>
<td>Will be Provider.</td>
</tr>
<tr class="odd">
<td>5</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td></td>
<td></td>
<td>899</td>
<td>Resource Group</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>6</td>
<td>26</td>
<td>TS</td>
<td>C</td>
<td></td>
<td></td>
<td>1202</td>
<td>Start Date/Time</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>7</td>
<td>20</td>
<td>NM</td>
<td>C</td>
<td></td>
<td></td>
<td>891</td>
<td>Start Date/Time Offset</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>8</td>
<td>250</td>
<td>CE</td>
<td>C</td>
<td></td>
<td></td>
<td>892</td>
<td>Start Date/Time Offset Units</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>9</td>
<td>20</td>
<td>NM</td>
<td>O</td>
<td></td>
<td></td>
<td>893</td>
<td>Duration</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>10</td>
<td>250</td>
<td>CE</td>
<td>O</td>
<td></td>
<td></td>
<td>894</td>
<td>Duration Units</td>
<td>Not used.</td>
</tr>
<tr class="odd">
<td>11</td>
<td>10</td>
<td>IS</td>
<td>C</td>
<td></td>
<td>279</td>
<td>895</td>
<td>Allow Substitution Code</td>
<td>Not used.</td>
</tr>
<tr class="even">
<td>12</td>
<td>250</td>
<td>CE</td>
<td>C</td>
<td></td>
<td>278</td>
<td>889</td>
<td>Filler Status Code</td>
<td>Not used.</td>
</tr>
</tbody>
</table>

<span id="_Toc193958139" class="anchor"></span>Table 112: Glossary

# Appendix A—Demographics Domain Native Domain Standardization (NDS)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This appendix provides a brief description of the new features and functions of the Demographics Domain Native Domain Standardization project. This project consists of multiple patches, which *must* be installed for the functionality to perform.

The Collaborative Terminology Tooling and Data Management (CTT & DM) Native Domain Standardization (NDS) Demographics Domain project supports the effort to standardize the following VistA Files in a native format within the existing Veterans Health Information Systems Technology Architecture (VistA):

- RACE (#10)
- MARITAL STATUS (#11)
- RELIGION (#13)

Demographics data is generated in the PATIENT (#2) file in VistA, which is part of the Registration package. This file includes:

- 469 fields
- 88 forward pointers
- 357 backward pointers
- 28 sub-files
- 8 computed fields

Standardization of the VistA RACE (#10), MARITAL STATUS (#11), and RELIGION (#13) files facilitate the broad exchange of health information, which ultimately contributes to the following:

- Improved patient safety
- Healthcare quality
- Efficiency

Mapping tables serve as an interim solution to achieving VA’s ultimate goal of providing VA and its partner institutions with applications that can be used natively without the need for mapping tables. The use of a standard terminology also facilitates the ability to provide more automated decision support for patient care. Because the Demographics Domain contributes a substantial amount of valuable clinical data, the importance of having this data in a standard, structured, easily mineable format is imperative.

This product *shall* run on standard hardware platforms used by the Department of Veterans Affairs (VA) Healthcare facilities.

## New Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The added functional components are:

- The system includes one new field that incorporates code data from their respective Standards Development Organizations (SDO) to the following files:
- RACE (#10)
- MARITAL STATUS (#11)
- RELIGION (#13)

These new fields are set as a Multiple in order to accommodate the potential need to store multiple codes to define a given term.

- The system includes three new files that incorporate code data from the respective Standards Development Organizations (SDO) for the following files:
- Race—RACE MASTER (#10.99)
- Marital Status—MASTER MARITAL STATUS (#11.99)
- Religion—MASTER RELIGION (#13.99)
- The system includes new VistA menu options to provide a method of interactively associating local race, marital status, and religion file entries to the corresponding master file if they have *not* already been associated via the Master File Server (MFS).
- The system includes new VistA reports to list the local race, marital status, and religion files’ associations to the corresponding master file.
- The entirety of the work within the scope of this effort has no impact on Graphic User Interfaces (GUI) within the VA network, and does *not* impact the workflow of clinicians.

Refer to the following CTT &DM NDS documents for additional information:

- Collaborative Terminology Tooling & Data Management Demographics Compendium V5.0, November 2016.
- Collaborative Terminology Development Tooling Business Requirements Document (BRD).
- DoD/VA Interagency Program Office (IPO), Healthcare Information Interoperability Technical Package (I2TP), Version 6.0, DRAFT, August 2016.

## Options and Build Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch implements demographics domain changes required by the Collaborative Terminology Tooling & Data Management (CTT & DM) Native Domain Standardization (NDS) project. This patch adds the following new “Master” files containing standard sets of concepts from the Health Level Seven (HL7) Standards Development Organization (SDO):

- RACE MASTER (#10.99)
- MASTER MARITAL STATUS (#11.99)
- MASTER RELIGION (#13.99)

New fields have also been added to the RACE (#10), MARITAL STATUS (#11), and RELIGION (#13) files pointing to the corresponding master file for the purpose of interoperability, by allowing each VA concept (Race, Marital Status, Religion) to be associated with a standard, interoperable, concept.

The RACE MASTER (#10.99), MASTER MARITAL STATUS (#11.99), and MASTER RELIGION (#13.99) files have been “locked down” to prevent local changes to the contents of the file; as each of these files contain entries representing the sets of concept names and codes from the respective Standards Development Organizations, and a VA Unique Identifier (VUID) identifying the standard SDO concept across the VHA enterprise.

The Master File Association \[DGMF AMAIN\] and Master File Reports \[DGMF RMAIN\] VistA menu options are accessible via the following menu path:

<span id="_Toc193958017" class="anchor"></span>Figure 19: Accessing the Master File Association \[DGMF AMAIN\] and Master File Reports \[DGMF RMAIN\] Options

Supervisor ADT Menu \[DG SUPERVISOR MENU\]  
ADT System Definition Menu \[DG SYSTEM DEFINITION MENU\]  
Master Demographics Files \[DGMF MENU\]  
Master File Association Enter/Edit \[DGMF AMAIN\]

Master File Reports \[DGMF RMAIN\]

<span id="_Toc193958018" class="anchor"></span>Figure 20: Build Components

Patch Components:

-----------------

Files & Fields Associated:

File Name (Number) Field Name (Number) New/Modified/Deleted

------------------ -------------- ----- --------------------

RACE (#10) RACE MASTER (#90) New

RACE MASTER (#10.99) REPLACED BY VHA STANDARD New

TERM (#99.97)

RACE MASTER (#10.99) MASTER ENTRY FOR VUID (#99.98) New

RACE MASTER (#10.99) VUID (#99.99) New

RACE MASTER (#10.99) EFFECTIVE DATE/TIME (#99.991) New

EFFECTIVE DATE/TIME EFFECTIVE DATE/TIME (#.01) New

(sub-file \#10.9901)

EFFECTIVE DATE/TIME STATUS (.02) New

(sub-file \#10.9901)

MARITAL STATUS (#11) MASTER MARITAL STATUS (#90) New

MASTER MARITAL STATUS REPLACED BY VHA STANDARD New

(#11.99) TERM (#99.97)

MASTER MARITAL STATUS MASTER ENTRY FOR VUID (#99.98) New

(#11.99)

MASTER MARITAL STATUS VUID (#99.99) New

(#11.99)

MASTER MARITAL STATUS EFFECTIVE DATE/TIME (#99.991) New

(#11.99)

EFFECTIVE DATE/TIME EFFECTIVE DATE/TIME (#.01) New

(sub-file \#11.9901)

EFFECTIVE DATE/TIME STATUS (.02) New

(sub-file \#11.9901)

RELIGION (#13) MASTER RELIGION (#13.99) New

MASTER RELIGION REPLACED BY VHA STANDARD New

(#13.99) TERM (#99.97)

MASTER RELIGION MASTER ENTRY FOR VUID (#99.98) New

(#13.99)

MASTER RELIGION VUID (#99.99) New

(#13.99)

RELIGION (#13) EFFECTIVE DATE/TIME (#99.991) New

(#13.99)

EFFECTIVE DATE/TIME EFFECTIVE DATE/TIME (#.01) New

(sub-file \#13.9901)

EFFECTIVE DATE/TIME STATUS (.01) New

(sub-file \#13.9901)

## Modified and New Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Routine Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The second line of each of these routines now looks like:

<span id="_Toc193958019" class="anchor"></span>Figure 21: Routine Second Line

;;5.3;Registration;\*\*\[Patch List\]\*\*;Aug 13, 1993;Build 33

The checksums in [Figure 36](#_Ref54600511) are new checksums, and can be checked with CHECK1^XTSUMBLD:

<span id="_Ref54600511" class="anchor"></span>Figure 22: Checksums

Routine Name: DG933PO

    Before:       n/a   After: B27885525  \*\*933\*\*

Routine Name: DGMFA10

    Before:       n/a   After: B14104060  \*\*933\*\*

Routine Name: DGMFA11

    Before:       n/a   After: B14590448  \*\*933\*\*

Routine Name: DGMFA13

   Before:       n/a   After: B13906961  \*\*933\*\*

Routine Name: DGMFASS

    Before:       n/a   After:  B3776607  \*\*933\*\*

Routine Name: DGMFR10

    Before:       n/a   After: B72687376  \*\*933\*\*

Routine Name: DGMFR11

    Before:       n/a   After: B68721321  \*\*933\*\*

Routine Name: DGMFR13

    Before:       n/a   After: B62970443  \*\*933\*\*

Routine Name: DGMFRPT

    Before:       n/a   After:  B3969553  \*\*933\*\*

Routine Name: DGNDSU

    Before:       n/a   After: B33380048  \*\*933\*\*

Routine Name: DGZRT

    Before:       n/a   After: B36061811  \*\*933\*\*

# VistA Audit Solution (VAS)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch DG\*5.3\*964 supports the Veterans Health Information Systems and Technology Architecture (VistA) Audit Solution (VAS). The goal of VAS is to improve VistA's security posture to provide better IT services for Veterans and to ensure the security of Veteran's data. As part of the solution, VAS utilizes an external database storage system in the Veterans Affairs Enterprise Cloud (VAEC) Amazon Web Services (AWS) Cloud.

The VAS software improves VistA's ability to respond to Freedom of Information Act (FOIA) inquiries regarding system user's interaction with Veterans’ data, ensuring that access to Veterans’ data can be adequately accounted for in the response to the FOIA inquiry. The VAS solution leverages existing VistA FileMan audit functionality as well as the standard patient lookup to capture auditable events and place them in an outbound queue in JSON (JavaScript Object Notation) format. These audit records are Patient related records for which an inquiry, update, create, or delete action occurred. Once the information is sent to the external archive the temporary stored record is deleted.

The audit records are transmitted by new web service DG VAS WEB SERVICE to the VAS Representational state transfer (REST) Application Programmer Interface (API), which are eventually stored in the VAS external archive. The VAS web server is defined by the DG VAS WEB SERVER entry in the WEB SERVER file (#18.12), which is configured with the domain name and port appropriate for the local facility.

By default after installation, the VAS export process is set to "Don't generate or send data". When set to this value, no audit data is queued or sent to the VAS REST API. This status may be viewed and modified using the VistA Audit Solution (VAS) options Menu \[DG VAS MENU\].

## VAS Web Service Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VAS web server REDACTED uses the “encrypt_only_tlsv12” SSL configuration. This configuration was released with HealtheVet Web Services Client (HWSC) patch XOBW\*1.0\*6, meaning XOBW\*1.0\*6 is required by VAS.

<span id="_Toc92448087" class="anchor"></span>Figure 23: VAS Web Server

REDACTED

<span id="_Toc92448088" class="anchor"></span>Figure 24: VAS Web Service

REDACTED

## VAS Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Options are provided to display and modify settings related to the VAS export process. The options are located in the DG VAS MENU under the DG SECURITY OFFICER MENU.

The DG VAS DISPLAY option displays export status, the VAS server and port, and other parameters related to the export process. The option also displays details related to the DG VAS EXPORT scheduled option.

The DG VAS MODIFY option allows users holding the DG SECURITY OFFICER key to modify all the parameters except the server and port, which are associated with the REDACTED and must be modified using the Web Server Manager \[REDACTED\] option.

<span id="_Toc193958023" class="anchor"></span>Figure 25: VAS Options

<table>
<caption><p><span id="_Ref58337765" class="anchor"></span>Table 113: Military Time Conversion Table</p></caption>
<colgroup>
<col style="width: 43%" />
<col style="width: 56%" />
</colgroup>
<thead>
<tr class="header">
<th>Option</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>DG VAS MENU</td>
<td>This menu contains options that display and modify settings related to the VistA Audit Solution (VAS). Only holders of the DG SECURITY OFFICER key have access to this menu.</td>
</tr>
<tr class="even">
<td>DG VAS DISPLAY</td>
<td>This option displays settings related to the VistA Audit Solution (VAS) export process.</td>
</tr>
<tr class="odd">
<td>DG VAS MODIFY</td>
<td>This option provides users with the ability to edit settings related to the VistA Audit Solution (VAS) export process.</td>
</tr>
<tr class="even">
<td>DG VAS EXPORT</td>
<td><p>This option is intended to be initiated by TaskMan to send records from the DG VAS QUEUE file to the VistA Audit Solution (VAS) external archive.</p>
<p>The option should be configured to run at Startup, and should be scheduled to run periodically. The process is not designed to run more than one</p>
<p>instance simultaneously; If the option is already running (based on a lock on the ^DGAUDIT(0) global node), then it simply quits.</p></td>
</tr>
<tr class="odd">
<td>DG AUDIT TASKMAN</td>
<td>This option provides an 'on demand' start of the the VistA Audit Solution (VAS) export process. The VAS export process is intended to run at regularly scheduled intervals by via the DG VAS EXPORT scheduled option.</td>
</tr>
</tbody>
</table>

<span id="_Ref58337765" class="anchor"></span>Table 113: Military Time Conversion Table

## VAS Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Parameters are provided to maintain and tune the VAS export process. The parameters may be viewed via the DG VAS DISPLAY option and edited via the DG VAS MODIFY option.

<span id="_Toc193958024" class="anchor"></span>Figure 26: VAS Parameters

| Parameter Name                 | Description                                                                                                                                                                  |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DG VAS BATCH SIZE              | This is the maximum number of audit records that will be sent in a single batch to the Vista Audit Solution.                                                                 |
| DG VAS DAYS TO KEEP EXCEPTIONS | The number of days to keep VAS export exceptions before purging.                                                                                                             |
| DG VAS DEBUGGING FLAG          | When set to 1 (on), this flag sends diagnostic data via email to the VAS MONITOR GROUP, and then resets to 0 (off).                                                          |
| DG VAS MAX QUEUE ENTRIES       | The maximum number of entries that may be stored in the VAS queue (DG VAS QUEUE file \#46.3).                                                                                |
| DG VAS MAX WRITE ATTEMPTS      | The number of consecutive unsuccessful attempts to write to the VAS REST API via POST command before an error is logged and a mail message is sent to the VAS MONITOR GROUP. |
| REDACTED                       | The email group to which VAS export issues and notifications are sent                                                                                                        |

## VAS Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Routines used by the VAS export are listed in the table below.

<span id="_Toc193958025" class="anchor"></span>Figure 27: VAS Routines

| Parameter Name | Description                                                                                                                                                                                                                                                                                                                                                                 |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DGAUDIT        | Main VAS export driver. Defined in the ROUTINE field of the DG VAS EXPORT option.                                                                                                                                                                                                                                                                                           |
| DGAUDIT1       | VAS export processing routine invoked from DGAUDIT.                                                                                                                                                                                                                                                                                                                         |
| DGAUDIT2       | Invoked from DGSEC to capture patient inquiry events and store audit records in JSON format into the DG VAS QUEUE file (#46.3).                                                                                                                                                                                                                                             |
| DGUADIT3       | Invoked by the DG VAS DISPLAY option to display VAS export settings, and by the DG VAS MODIFY option to edit VAS export settings.                                                                                                                                                                                                                                           |
| DGAUDITP       | Post installation routine for VAS patch DG\*5.3\*964. This registers the DG VAS WEB SERVICE in the WEB SERVICE file (#18.02), sets initial values for the VAS parameters, adds the server DNS to the DG VAS WEB SERVER entry in the WEB SERVER file (#18.12) based on the facility station number, and adds the DG VAS EXPORT option to the OPTION SCHEDULING file (#19.2). |
| DGSEC          | “MAS Patient Look-up Security Check” routine, invoked for all VistA patient lookups, invokes VAS routine DGAUDIT2 to log patient lookup audit events.                                                                                                                                                                                                                       |
| DGSEC4         | “Utilities for record access & sensitive record processing” routine, used to log sensitive patient lookups.                                                                                                                                                                                                                                                                 |

## VAS Data Dictionaries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Data Dictionaries used by the VAS export process are listed in the table below.

<span id="_Toc193958026" class="anchor"></span>Figure 28: VAS Data Dictionaries

| DD Name       | DD Number | Global    | Description                                                                                                                                         |
|---------------|-----------|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| DG VAS QUEUE  | 46.3      | ^DGAUDIT  | This file holds the inquire and update audit transactions queued to be sent to the Vista Audit Solutions (VAS) external archive.                    |
| DG VAS EXPORT | 46.4      | ^DGAUDIT1 | This file contains the most recent record from the AUDIT file (#1.1) that was queued to be sent to the VistA Audit Solution (VAS) external archive. |
| DG VAS CONFIG | 46.5      | ^DGAUDIT2 | This file contains settings for the VistA Audit Solution (VAS) process that sends audit transactions to the VAS external archive.                   |

## VAS Alerts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MailMan alerts sent by the VAS export process are listed in the table below.

<span id="_Toc193958027" class="anchor"></span>Figure 29: VAS Alerts

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th>Alert Subject</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>VAS SWITCH ALERT###*</p>
<ul>
<li><p>*### is the station number.</p></li>
</ul></td>
<td><p>This alert is sent to members of the mail group defined in the DG VAS MONITOR GROUP parameter (the default is the DG VAS MONITOR mail group). The alert notifies the recipient when the VAS Export send status switch is changed from any value to any value using the Modify VAS Parameters [DG VAS MODIFY] option in the VistA Audit Solution (VAS) options menu [DG VAS MENU].</p>
<p>The possible values of the VAS send status switch are:</p>
<p>0 Don't generate or send data</p>
<p>1 Generate and send data</p>
<p>2 Generate data, don't send</p>
<p>The alert contains the Date/Time the send status switch was changed, the facility at which the change occurred, the new and old switch values, the number of entries in the VAS Queue, the maximum number of entries allowed in the VAS Queue, and the Internal Entry Number (IEN or DUZ) of the user who modified the switch value.</p>
<p>Example, VAS SWITCH ALERT</p>
<p>The VistA Audit Solution (VAS) send status switch was changed at Station 000 (ANYTOWN) on May 06, 2024 at 11:33:51</p>
<p>New Value: 'Generate and send data'</p>
<p>Old Value: 'Don't generate or send data'</p>
<p>The ^DGAUDIT global contains 3 entries.</p>
<p>The maximum number of entries in the queue is 60001.</p>
<p>[10000000009]</p></td>
</tr>
<tr class="even">
<td><p>VAS AUDIT ERROR MESSAGE FROM STATION ###</p>
<p>*### is the station number</p></td>
<td><p>This general alert is sent when the VAS Export is unable to send records to the VAS cloud database. The alert contains the Date/Time the failure occurred, the VA facility at which the failure occurred, the alert details, the number of entries in the VAS Queue, and the maximum number of entries allowed in the VAS Queue.</p>
<p>Examples, VAS AUDIT ERROR MESSAGE</p>
<p><strong>Database Error</strong></p>
<p>Date/Time: May 01, 2024@12:49:07</p>
<p>Error from DG VAS WEB SERVER: ###.###.### on port ###</p>
<p>Result of POST command:</p>
<p>HTTP/1.1 500 Internal Server Error</p>
<p>{"message":"Error sending records to redis"}</p>
<p>The ^DGAUDIT global contains 1085 entries.</p>
<p>The maximum number of entries in the queue is 60000.</p>
<p><strong>Unable to Connect</strong></p>
<p>Result of POST command:</p>
<p>ERROR #6059: Unable to open TCP/IP socket to server</p>
<p><strong>Missing or invalid JSON format</strong></p>
<p>An audit record with missing or invalid JSON data was purged from the VAS queue. See ^XTMP("DGAUDIT_EXCEPTION"</p>
<p>for more information. Header information:</p>
<p>Request Type: INQUIRY</p>
<p>File Name: PATIENT</p>
<p>File Number: 2</p>
<p>Menu Option Used: MAG WINDOWS</p>
<p><strong>Connection Timeout</strong></p>
<p>Result of POST command:</p>
<p>ERROR #5922: Timed out waiting for response</p>
<p><strong>Invalid Response</strong></p>
<p>Result of POST command:</p>
<p>ERROR #6097: Error '&lt;READ&gt;zRead+28^%Net.HttpRequest.1' while using TCP /IP device '9999'</p></td>
</tr>
</tbody>
</table>

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Also, please refer to the following sites:
- OIT Master Glossary website (VA Intranet)
- VA Acronym Lookup website (VA Intranet)
<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 79%" />
</colgroup>
<thead>
<tr class="header">
<th>Term</th>
<th>Definition</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ADD-ONS</td>
<td>Patients who have been scheduled for a visit after routing slips for a particular date have been printed.</td>
</tr>
<tr class="even">
<td>ALOS</td>
<td>Average Length of Stay.</td>
</tr>
<tr class="odd">
<td>AMIS</td>
<td>Automated Management Information System.</td>
</tr>
<tr class="even">
<td>ANCILLARY</td>
<td>A test added to an existing appointment (i.e., lab, x-ray, EKG) test.</td>
</tr>
<tr class="odd">
<td>API</td>
<td>Application Program Interface.</td>
</tr>
<tr class="even">
<td>BILLINGS</td>
<td>Bills sent to Veteran.</td>
</tr>
<tr class="odd">
<td>BRD</td>
<td>Business Requirements Document.</td>
</tr>
<tr class="even">
<td>CLINIC PULL LIST</td>
<td>A list of patients whose radiology/MAS records should be pulled from the file room for use in conjunction with scheduled clinic visits.</td>
</tr>
<tr class="odd">
<td>COLLATERAL</td>
<td>A visit by a <em>non</em>-Veteran patient whose appointment is related to or visit associated with a service-connected patient's treatment.</td>
</tr>
<tr class="even">
<td>Computerized Patient Record System (CPRS)</td>
<td>An integrated, comprehensive suite of clinical applications in VistA that work together to create a longitudinal view of the Veteran’s Electronic Medical Record (EMR). CPRS capabilities include a Real Time Order Checking System, a Notification System to alert clinicians of clinically significant events, Consult/Request tracking and a Clinical Reminder System. CPRS provides access to most components of the patient chart.</td>
</tr>
<tr class="odd">
<td>CPRS</td>
<td>Computerized Patient Record System.</td>
</tr>
<tr class="even">
<td>CPT</td>
<td>Current Procedural Terminology.</td>
</tr>
<tr class="odd">
<td>CR</td>
<td>Clinical Reminders.</td>
</tr>
<tr class="even">
<td>DBIA</td>
<td>Database Integration Agreement.</td>
</tr>
<tr class="odd">
<td>DRG</td>
<td>Diagnostic Related Group.</td>
</tr>
<tr class="even">
<td>GMTS</td>
<td>Health Summary namespace.</td>
</tr>
<tr class="odd">
<td>GUI</td>
<td>Graphic User Interface.</td>
</tr>
<tr class="even">
<td>HL7</td>
<td>Health Level Seven.</td>
</tr>
<tr class="odd">
<td>ICR</td>
<td>Integration Control Reference.</td>
</tr>
<tr class="even">
<td>IRT</td>
<td>Incomplete Records Tracking.</td>
</tr>
<tr class="odd">
<td>IVMH</td>
<td>Improve Veteran Mental Health.</td>
</tr>
<tr class="even">
<td>MEANS TEST</td>
<td>A financial report upon which certain patients' eligibility for care is based.</td>
</tr>
<tr class="odd">
<td>Mental Health Treatment Coordinator (MHTC)</td>
<td><p>The liaison between the patient and the mental health system at a VA site. There is only one Mental Health treatment coordinator per patient, and they are the key coordinator for behavioral health services care.</p>
<p>For more information about the MH treatment coordinator’s responsibilities, see the VHA Handbook 1160.1, “Uniform Mental Health Services in VA Medical Centers for Clinics,” page 3-4.</p>
<p><strong>NOTE:</strong> In the handbook, the MHTC is called the Principal Mental Health Provider.</p></td>
</tr>
<tr class="even">
<td>MH</td>
<td>Mental Health.</td>
</tr>
<tr class="odd">
<td>MHA3</td>
<td>Mental Health Assistant 3 package.</td>
</tr>
<tr class="even">
<td>MHTC</td>
<td>Mental Health Treatment Coordinator.</td>
</tr>
<tr class="odd">
<td>NO SHOW</td>
<td>A person who did not report for a scheduled clinic visit without prior notification to the medical center.</td>
</tr>
<tr class="even">
<td>NON-COUNT</td>
<td>A clinic whose visits do not affect AMIS statistics.</td>
</tr>
<tr class="odd">
<td>NSR</td>
<td>New Service Request.</td>
</tr>
<tr class="even">
<td>OE/RR</td>
<td>Order Entry/Results Reporting.</td>
</tr>
<tr class="odd">
<td>OPC</td>
<td>Outpatient Clinic.</td>
</tr>
<tr class="even">
<td>OR</td>
<td>CPRS Order Entry/Results Reporting namespace.</td>
</tr>
<tr class="odd">
<td>PAF</td>
<td>Patient Assessment File; where PAI information is stored until transmission to Austin.</td>
</tr>
<tr class="even">
<td>PAI</td>
<td>Patient Assessment Instrument.</td>
</tr>
<tr class="odd">
<td>PCE</td>
<td>Patient Care Encounter.</td>
</tr>
<tr class="even">
<td>PCMM</td>
<td>Primary Care Management Module.</td>
</tr>
<tr class="odd">
<td>PRF</td>
<td>Patient Record Flag.</td>
</tr>
<tr class="even">
<td>Principal Mental Health Provider (PMHP)</td>
<td>See MH Treatment Coordinator (MHTC).</td>
</tr>
<tr class="odd">
<td>PTF</td>
<td>Patient Treatment File.</td>
</tr>
<tr class="even">
<td>PULL LIST</td>
<td>A list of patients whose radiology/PIMS records should be "pulled" from the file room for scheduled clinic visits.</td>
</tr>
<tr class="odd">
<td>PX</td>
<td>Patient Care Encounter namespace.</td>
</tr>
<tr class="even">
<td>PXRM</td>
<td>Clinical Reminders package namespace.</td>
</tr>
<tr class="odd">
<td>RAM</td>
<td>Resource Allocation Methodology.</td>
</tr>
<tr class="even">
<td>Reminder Definitions</td>
<td>These are pre-defined sets of findings that are used to identify patient cohorts and reminder resolutions. The reminder is used for patient care and/or report extracts.</td>
</tr>
<tr class="odd">
<td>Reminder Dialogs</td>
<td>These are pre-defined sets of text and findings that provide information to the CPRS GUI for collecting and updating appropriate findings while building a progress note.</td>
</tr>
<tr class="even">
<td>Reminder Terms</td>
<td>Terms are used to map local findings to national findings, providing a method to standardize the findings for national use. These are also used for local grouping of findings for easier reference in reminders and are defined in the Reminder Terms file.</td>
</tr>
<tr class="odd">
<td>ROUTING SLIP</td>
<td>When printed for a specified date, it shows the current appointment time, clinic, location, and stop code. It also shows future appointments.</td>
</tr>
<tr class="even">
<td>RPC</td>
<td>Remote Procedure Calls.</td>
</tr>
<tr class="odd">
<td>RSD</td>
<td>Requirements Specification Document.</td>
</tr>
<tr class="even">
<td>RUG</td>
<td>Resource Utilization Group.</td>
</tr>
<tr class="odd">
<td>SBR</td>
<td>Suicide Behavior Report.</td>
</tr>
<tr class="even">
<td>SHARING AGREEMENT</td>
<td>Agreement or contract under which patients from other government agencies or private facilities are treated.</td>
</tr>
<tr class="odd">
<td>SME</td>
<td>Subject Matter Expert.</td>
</tr>
<tr class="even">
<td>SPECIAL SURVEY</td>
<td>An ongoing survey of care given to patients alleging Agent Orange or Ionizing Radiation exposure. Each visit by such patients <em>must</em> receive "special survey dispositioning" which records whether treatment provided was related to their exposure. This data is used for Congressional reporting purposes.</td>
</tr>
<tr class="odd">
<td>STOP CODE</td>
<td><p>A three-digit number corresponding to an additional stop/service a patient received in conjunction with a clinic visit.</p>
<p>Stop code entries are used so that medical facilities may receive credit for the services rendered during a patient visit.</p></td>
</tr>
<tr class="even">
<td>THIRD PARTY</td>
<td>Billings where a party other than the patient is billed.</td>
</tr>
<tr class="odd">
<td>TIU</td>
<td>Text Integration Utility namespace.</td>
</tr>
<tr class="even">
<td>TIU</td>
<td>Text Integration Utility.</td>
</tr>
<tr class="odd">
<td>TSR</td>
<td>Treating Specialty Report.</td>
</tr>
<tr class="even">
<td>VHA</td>
<td>Veterans Health Administration.</td>
</tr>
<tr class="odd">
<td>VistA</td>
<td>Veterans Information System and Technology Architecture.</td>
</tr>
</tbody>
</table>

# Military Time Conversion Table

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Standard       | Military   |
|----------------|------------|
| 12:00 MIDNIGHT | 2400 HOURS |
| 11:00 PM       | 2300 HOURS |
| 10:00 PM       | 2200 HOURS |
| 9:00 PM        | 2100 HOURS |
| 8:00 PM        | 2000 HOURS |
| 7:00 PM        | 1900 HOURS |
| 6:00 PM        | 1800 HOURS |
| 5:00 PM        | 1700 HOURS |
| 4:00 PM        | 1600 HOURS |
| 3:00 PM        | 1500 HOURS |
| 2:00 PM        | 1400 HOURS |
| 1:00 PM        | 1300 HOURS |
| 12:00 NOON     | 1200 HOURS |
| 11:00 AM       | 1100 HOURS |
| 10:00 AM       | 1000 HOURS |
| 9:00 AM        | 0900 HOURS |
| 8:00 AM        | 0800 HOURS |
| 7:00 AM        | 0700 HOURS |
| 6:00 AM        | 0600 HOURS |
| 5:00 AM        | 0500 HOURS |
| 4:00 AM        | 0400 HOURS |
| 3:00 AM        | 0300 HOURS |
| 2:00 AM        | 0200 HOURS |
| 1:00 AM        | 0100 HOURS |

# Alphabetical Index of PIMS Terms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- ACRP Ad Hoc Report
- ACRP Database Conversion
- Add / Edit a Holiday
- Add / Edit Stop Codes
- Alpha List of Incomplete Encounters
- Append Ancillary Test to Appt.
- Appointment Check-in / Check-out
- Appointment List
- Appointment Management
- Appointment Management Report
- Appointment Status Update
- Appointment Waiting Time Report
- Batch Update Comp Gen Appt Type for C&Ps
- Call List
- Cancel Appointment
- Cancel Clinic Availability
- Cancelled Clinic Report
- Change Patterns to 30-60
- Chart Request
- Check Transmitted Outpatient Encounter Files
- Check-in / Unsched. Visit
- Clinic Appointment Availability Report
- Clinic Assignment Listing
- Clinic Edit Log Report
- Clinic Group Maintenance for Reports
- Clinic List (Day of Week)
- Clinic Next Available Appt. Monitoring Report
- Clinic Profile
- Clinic Utilization Statistical Summary
- Computer Generated Appointment Type Listing
- Convert Patient File Fields to PCMM
- Correct Incomplete Encounters
- Current MAS Release Notes
- Data Transmission Report
- Delete an Ad Hoc Report Template
- Delete Ancillary Test for Appt.
- Discharge from Clinic
- Display Ad Hoc Report Template Parameters
- Display Appointments
- Display Clinic Availability Report
- Edit Appointment Type for Add / Edit Encounters
- Edit Clinic Enrollment Data
- Edit Clinic Stop Code Name- Local Entries Only
- Edit Computer Generated Appointment Type
- Edit Outpatient Encounter
- Enc. by DSS ID / DSS ID by Freq. (OP0, OP1, OP2)
- Enc. by IP DSS ID / DSS ID by Freq. (IP0, IP1, IP2)
- Encounter ‘Action Required’ Report
- Encounter Activity Report
- Encounters Transmitted with MT Status of U
- Enrollment Review Date Entry
- Enrollments \> X Days
- Enter / Edit Letters
- Error Listing
- File Room List
- Find Next Available Appointment
- Future Appointments for Inpatients
- High Risk MH No-Show Adhoc Report
- High Risk MH No-Show Nightly Report
- Inactivate a Clinic
- Incomplete Encounter Error Report
- Incomplete Encounters by Error Code
- Inpatient Appointment List
- Look Up on Clerk Who Made Appointment
- Make Appointment
- Make Consult Appointment
- Management Edit
- Management Report for Ambulatory Procedures
- Means Test / Eligibility / Enrollment Report
- Means Test IP Visits & Unique (IP3, IP4, IP5)
- Means Test Visits & Uniques (OP3, OP4, OP5)
- Most Frequent 20 IP Practitioner Types (IP8)
- Most Frequent 20 Practitioner Types (OP8)
- Most Frequent 50 CPT Codes (OP6)
- Most Frequent 50 ICD-9-CM Codes (OP7)
- Most Frequent 50 IP CPT Codes (IP6)
- Most Frequent 50 IP ICD-9-CM Codes (IP7)
- Multiple Appointment Booking
- Multiple Clinic Display / Book
- Non-Conforming Clinics Stop Code Report
- No-Show Report
- No-Shows
- Outpatient Diagnosis / Procedure Code Search
- Outpatient Diagnosis / Procedure Frequency Report
- Outpatient Encounter Workload Statistics
- Patient Activity by Appointment Frequency
- Patient Appointment Statistics
- Patient Encounter List
- Patient Profile MAS
- Performance Monitor Detailed Report
- Performance Monitor Retransmit Report (AAC)
- Performance Monitor Summary Report
- Print Appointment Status Update (Date Range)
- Print from Ad Hoc Template
- Print Scheduling Letters
- Provider / Diagnosis Report
- Purge Ambulatory Care Reporting files
- Purge Appointment Status Update Log File
- Purge rejections that are past database close-out
- Purge Scheduling Data
- Radiology Pull List
- Reactivate a Clinic
- Remap Clinic
- Restore Clinic Availability
- Retransmit Ambulatory Care Data by Date Range
- Retransmit Selected Error Code
- Retroactive Visits List
- Review of Scheduling / PCE / Problem List Data
- Routing Slips
- SC Veterans Awaiting Appointments
- Selective Retransmission of NPCDB Rejections
- Set up a Clinic
- Sharing Agreement Category Update
- Stop Code Listing (Computer Generated)
- Summary Report - IEMM
- Team / Position Assignment / Re-Assignment
- Tracking Report
- Transmission History for Patient
- Transmission History Report - Full
- Trend of Facility Uniques by 12 Month Date Ranges
- Veterans Without Activity Since a Specified Date
- View Appointment Status Update Date (Single Date)
- Visit Rpt by Transmitted OPT Encounter
- Visits and Unique IP SSNs by County (IP9)
- Visits and Unique SSNs by County (OP9)
- Workd Report

Template Revision History

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 11%" />
<col style="width: 45%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Version</th>
<th>Description</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>July 2024</td>
<td>1.3</td>
<td>Updated to OIT Brand and OIT Production Documentation Standards.</td>
<td>OIT Documentation Standards Committee</td>
</tr>
<tr class="even">
<td>March 2024</td>
<td>1.2</td>
<td><p>Updates:</p>
<ul>
<li><p>Updated organization references.</p></li>
<li><p>Updated Styles and formatting.</p></li>
<li><p>Updated instructional text throughout.</p></li>
</ul></td>
<td>OIT Documentation Standards Committee</td>
</tr>
<tr class="odd">
<td>July 2016</td>
<td>1.1</td>
<td>Updated instructional text to simplify content.</td>
<td>OIT Documentation Standards Committee</td>
</tr>
<tr class="even">
<td>June 2016</td>
<td>1.0</td>
<td>Initial version.</td>
<td>OIT Documentation Standards Committee</td>
</tr>
</tbody>
</table>

[^1]: Special meaning placed on this field to support multiple rejection reasons by the National Patient Care Database (NPCDB).

[^2]: According to the HL7 standard, the maximum length of this element is 2.

[^3]: This element is also found in the Patient Identification (PID) segment.

[^4]: This element is also found in the Patient Identification (PID) segment.