---
title: AMPL User Guide
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: AMPL
app_code: PREA
app_name: "Pharmacy: Advanced Medication Platform"
section: CLI
app_status: archive
pkg_ns: PREA
patch_ver: 1.9
patch_id: PREA*1.9
group_key: "PREA:PREA:1.9"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - figure
  - span
  - ampl
  - patient
  - guide
  - class
  - orders
  - anchor
  - table
  - below
page_count: 0
word_count: 18707
section_count: 41
table_count: 3
figure_count: 218
appendix_count: 2
has_toc: False
is_stub: False
pub_date: November 2024
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharmacy_PREA_Archive/PREA_1_9_AMPL_GUI_UG.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharmacy_PREA_Archive/PREA_1_9_AMPL_GUI_UG.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=398"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>Advanced Medication Platform (AMPL)  
  Graphical User Interface (GUI)  
  User Guide
---

![](ampl-user-guide/001.png)

November 2024

Office of Information and Technology (OIT)

Revision History

<table>
<caption><p>Table 1: Allergy Identifier</p></caption>
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
<td>11/2024</td>
<td>0.5</td>
<td><p>1.3.1<br />
Updated content for the new hover text for a Patient’s Social Security Number<br />
<br />
5.2<br />
Updated the figures in this section for the new display and hover text for a Patient’s Social Security Number</p>
<p>3.1<br />
Updated figure to show the new login screen message that reflects the current operational guidance so that the system complies with Authority to Operate (ATO) requirements and users are aware of usage restrictions</p></td>
<td>AMPL GUI TEAM</td>
</tr>
<tr class="even">
<td>08/2024</td>
<td>0.4</td>
<td>5.3<br />
Updated figure to show the addition of the Residential Address displaying in AMPL</td>
<td>AMPL GUI Team</td>
</tr>
<tr class="odd">
<td>06/2024</td>
<td>0.3</td>
<td><p>4.2</p>
<p>5</p>
<p>5.2</p>
<p>5.3</p>
<p>Updated figures in these sections for the addition of the Links button</p>
<p>5.1</p>
<p>Created new section (content and figures) for the addition of the Links button</p>
<p>4.6</p>
<p>Updated content and figures for the new Toggle button on the Patient to Process List</p>
<p>5.2</p>
<p>Updated content and figures for the addition of the Mail Restrictions field</p>
<p>6.1.1.5</p>
<p>Updated content and figures for the addition of the Drug Marked for CMOP field in Pending Orders</p>
<p>6.1.3.1</p>
<p>Updated content and figures for the addition of the Flag Icon for flagged orders</p>
<p>6.1.4.3</p>
<p>Updated content and figures for the addition of the Hazardous to Handle Icon</p>
<p>Note: The Links button was added to the header in AMPL and figures throughout the User Guide have been updated to reflect the change</p></td>
<td>AMPL GUI Team</td>
</tr>
<tr class="even">
<td>03/2024</td>
<td>0.2</td>
<td><p>6.6.2<br />
Updated the list of filters<br />
Updated the screen capture to show the changes as they appear in AMPL</p>
<p>6.1.1.5<br />
Updated the screen capture to show the changes as they appear in AMPL<br />
<br />
5.2</p>
<p>Updated to add mail restrictions and patient narrative</p>
<p>Updated figures to show the changes as they appear in AMPL<br />
<br />
6.4.1<br />
Updated figures to show the changes as they appear in AMPL<br />
<br />
6.1.1<br />
Updated to include the changed column headers<br />
Updated the figures to show the changes as they appear in AMPL<br />
<br />
6.1.4.3<br />
Updated to include the new fields<br />
Updated the figures to show the changes as they appear in AMPL</p></td>
<td>AMPL GUI Team</td>
</tr>
<tr class="odd">
<td>08/2023</td>
<td>0.1</td>
<td>Document Baseline</td>
<td>AMPL GUI Team</td>
</tr>
</tbody>
</table>

Table 1: Allergy Identifier

Table of Contents

List of Figures

Figure 1: Logical High Level AMPL GUI HealthShare Data Flow [6](#_Toc180613815)

Figure 2: AMPL GUI Login Page [7](#_Toc180613816)

Figure 3: SSOi Page for VA Users [8](#_Toc180613817)

Figure 4: Set VistA Context [8](#_Toc180613818)

Figure 5: Change Station [9](#_Toc180613819)

Figure 6: Pending Orders Manager Landing Page – Patient Table [9](#_Toc180613820)

Figure 7: Pending Orders Manager Tabs [10](#_Toc180613821)

Figure 8: VistA Patient Lookup [10](#_Toc180613822)

Figure 9: VistA Patient Lookup Info Button [10](#_Toc180613823)

Figure 10: Patient Lookup Search Criteria Help [11](#_Toc180613824)

Figure 11: VistA Logo Button [11](#_Toc180613825)

Figure 12: Current Query [11](#_Toc180613826)

Figure 13: Column Filter and Sort Icons [12](#_Toc180613827)

Figure 14: Patient Queue [12](#_Toc180613828)

Figure 15: Patient Cover Sheet with Patient Queue List [13](#_Toc180613829)

Figure 16: POM Button Toggle to Coversheet and Retained in Patient Queue [13](#_Toc180613830)

Figure 17: Outpatient Orders by Date Tab [13](#_Toc180613831)

Figure 18: Outpatient Orders by Date - Site Selection [14](#_Toc180613832)

Figure 19: Outpatient Orders by Date - Aging Summary [14](#_Toc180613833)

Figure 20: Outpatient Orders by Date – Aging Summary Quick Filter [14](#_Toc180613834)

Figure 21: Outpatient Orders by Date - Selecting an Ordering Institution [15](#_Toc180613835)

Figure 22: Outpatient Orders by Date - Site and Institution Selected [15](#_Toc180613836)

Figure 23: Outpatient Orders by Date - Patient List [15](#_Toc180613837)

Figure 24: Outpatient Orders by Date - Query Editor Filters [16](#_Toc180613838)

Figure 25: Outpatient Orders by Date - Query Editor Filter [16](#_Toc180613839)

Figure 26: Outpatient Orders by Date - Query Editor Filter Applied [16](#_Toc180613840)

Figure 27: Outpatient Orders by Date - Results of Query Filter Applied to List [17](#_Toc180613841)

Figure 28: Supply Filter - Defaults Other Fields [17](#_Toc180613842)

Figure 29: Provider Filter - Defaults [17](#_Toc180613843)

Figure 30: Date Filter - Commonly Used Date Ranges [18](#_Toc180613844)

Figure 31: Query for Date Field Quick List [18](#_Toc180613845)

Figure 32: Outpatient Orders by Location Tab [19](#_Toc180613846)

Figure 33: Outpatient Orders by Location - Site Selection [19](#_Toc180613847)

Figure 34: Outpatient Orders by Location - Selecting an Ordering Institution [19](#_Toc180613848)

Figure 35: Outpatient Orders by Location - Site and Institution Selected [20](#_Toc180613849)

Figure 36: Outpatient Orders by Location - STAT Symbol [20](#_Toc180613850)

Figure 37: Outpatient Orders by Location - Clinic Selected [20](#_Toc180613851)

Figure 38: Outpatient Orders by Location - Select Patient(s) to Process List [21](#_Toc180613852)

Figure 39: Outpatient Orders by Location - Process All Button [21](#_Toc180613853)

Figure 40: Outpatient Orders by Location - Query Editor Filters [21](#_Toc180613854)

Figure 41: Outpatient Orders by Location - Query Editor Filter Operators [22](#_Toc180613855)

Figure 42: Outpatient Orders by Location - Query Editor Filters Drug Selected [22](#_Toc180613856)

Figure 43: Outpatient Orders by Location - Query Editor Search Criteria [22](#_Toc180613857)

Figure 44: Outpatient Orders by Location - Query Editor Delete Icon [22](#_Toc180613858)

Figure 45: Outpatient Orders by Location - Patient Filter [23](#_Toc180613859)

Figure 46: Inpatient Orders Tab [23](#_Toc180613860)

Figure 47: Inpatient Orders - Division Selection [24](#_Toc180613861)

Figure 48: Inpatient Orders - Division Selected [24](#_Toc180613862)

Figure 49: Inpatient Orders - Ward Group Selected [24](#_Toc180613863)

Figure 50: Inpatient Orders - Select Patient(s) to Process List [24](#_Toc180613864)

Figure 51: Inpatient Orders - Query Editor Filters [25](#_Toc180613865)

Figure 52: Inpatient Orders - Query Editor Filter Applied [25](#_Toc180613866)

Figure 53: Inpatient Orders - Query Editor Filters Drug Value [26](#_Toc180613867)

Figure 54: Inpatient Orders - Query Editor Search Criteria [26](#_Toc180613868)

Figure 55: Inpatient Orders - Query Editor Delete Icon [26](#_Toc180613869)

Figure 56: Inpatient Orders - "Save Query” Dialog [26](#_Toc181786688)

Figure 57: Inpatient Orders – Saved User Query Dropdown Menu [27](#_Toc181786689)

Figure 58: Clinic Orders Tab [27](#_Toc180613871)

Figure 59: Clinic Orders - Select Division [27](#_Toc180613872)

Figure 60: Clinic Orders - Division Selected [28](#_Toc180613873)

Figure 61: Clinic Orders - Clinic Group Selected [28](#_Toc180613874)

Figure 62: Clinic Orders - Query Editor Filters [28](#_Toc180613875)

Figure 63: Clinic Orders - Select Patient(s) to Process List Toggle On [29](#_Toc180613876)

Figure 64: Clinic Orders - Select Patient(s) to Process List Toggle Off [29](#_Toc180613877)

Figure 65: Clinic Orders - Select Patient(s) to Process List Toggle Button Help Text [29](#_Toc180613878)

Figure 66: Patient Coversheet [30](#_Toc180613879)

Figure 67: Refresh Patient Data [30](#_Toc180613880)

Figure 68: Links Button [31](#_Toc180613881)

Figure 69: Patient Banner [31](#_Toc180613882)

Figure 70: Covid-19 Testing Status [31](#_Toc180613883)

Figure 71: Mail Restrictions [32](#_Toc180613884)

Figure 72: Patient Reload Button [32](#_Toc180613885)

Figure 73: Patient Information Banner [32](#_Toc180613886)

Figure 74: Patient Demographic - Details [33](#_Toc180613887)

Figure 75: Contact Info Tab [34](#_Toc180613888)

Figure 76: Pharmacy Info Tab [34](#_Toc180613889)

Figure 77: Eligibility Tab [35](#_Toc180613890)

Figure 78: Social, Primary Care, Clinic Info Tab [35](#_Toc180613891)

Figure 79: Military Service Tab [36](#_Toc180613892)

Figure 80: Health Plans/Insurance Tab [36](#_Toc180613893)

Figure 81: Primary Care Team Information [36](#_Toc180613894)

Figure 82: Primary Care Details - Outpatient [37](#_Toc180613895)

Figure 83: Primary Care Details - Inpatient [37](#_Toc180613896)

Figure 84: Allergies/ADRs Listed in Patient Banner [37](#_Toc180613897)

Figure 85: Allergy Banner Pop-Up Window [38](#_Toc180613898)

Figure 86: Postings Buttons - Indicating Critical Information [39](#_Toc180613899)

Figure 87: Postings Buttons - Indicating No Postings [39](#_Toc180613900)

Figure 88: CWAD - List Window [39](#_Toc180613901)

Figure 89: CWAD - Detailed Display [40](#_Toc180613902)

Figure 90: Patient Data Domain Tabs [41](#_Toc180613903)

Figure 91: Med List Tab [41](#_Toc180613904)

Figure 92: Outpatient Med List [42](#_Toc180613905)

Figure 93: Outpatient Med List - Remote Orders Button [42](#_Toc180613906)

Figure 94: Outpatient Med List - Remote Orders [43](#_Toc180613907)

Figure 95: Outpatient Med List - More Button [43](#_Toc180613908)

Figure 96: Outpatient Med List - Expanded View [43](#_Toc180613909)

Figure 97: Outpatient Med List - Help Text [44](#_Toc180613910)

Figure 98: CMOP Indicator [45](#_Toc180613911)

Figure 99: Outpatient Med List - Show Remote Orders Checkbox [46](#_Toc180613912)

Figure 100: Outpatient Med Order – Active Order Detail Screen [46](#_Toc180613913)

Figure 101: Outpatient Med Order – Pending Order Detail Screen [47](#_Toc180613914)

Figure 102: Outpatient Med Order – Additional Details [47](#_Toc180613915)

Figure 103: Outpatient Med Order – Order Check [47](#_Toc180613916)

Figure 104: Outpatient Med Order - Drug Restriction/Guideline Information [47](#_Toc180613917)

Figure 105: Outpatient Med Order - Drug Info [48](#_Toc180613918)

Figure 106: Outpatient Med Order - Provider Info [48](#_Toc180613919)

Figure 107: Outpatient Med Order - Activity Log [48](#_Toc180613920)

Figure 108: Inpatient Med List [49](#_Toc180613921)

Figure 109: Inpatient Med List - More Button [49](#_Toc180613922)

Figure 110: Inpatient Med List - Expanded View [50](#_Toc180613923)

Figure 111: Inpatient Med List - Help Text [50](#_Toc180613924)

Figure 112: Inpatient Med Order - Active Orders Detail Screen [51](#_Toc180613925)

Figure 113: Inpatient Med Order - Additional Details [51](#_Toc180613926)

Figure 114: Inpatient Med Order - Order Check [51](#_Toc180613927)

Figure 115: Inpatient Med Order - Drug Restriction/Guideline Information [52](#_Toc180613928)

Figure 116: Inpatient Med Order - Drug Info [52](#_Toc180613929)

Figure 117: Inpatient Med Order - Provider Information [52](#_Toc180613930)

Figure 118: Inpatient Med Order - PADE Inventory [53](#_Toc180613931)

Figure 119: Inpatient Med Order - Administration Hx [53](#_Toc180613932)

Figure 120: Clinic Med List [54](#_Toc180613933)

Figure 121: Clinic Med List - Remote Orders Button [54](#_Toc180613934)

Figure 122: Clinic Med List - Remote Orders [54](#_Toc180613935)

Figure 123: Clinic Med List - Expanded View [55](#_Toc180613936)

Figure 124: Clinic Med List - Help Text [55](#_Toc180613937)

Figure 125: Clinic Med Order – Active Order Detail Screen [55](#_Toc180613938)

Figure 126: Clinic Med Order - IV Med Order Details [56](#_Toc180613939)

Figure 127: Clinic Med Order - Additional Details [56](#_Toc180613940)

Figure 128: Clinic Med Order - Order Check [56](#_Toc180613941)

Figure 129: Clinic Med Order - Drug Restriction/Guideline Information [56](#_Toc180613942)

Figure 130: Clinic Med Order - Drug Info [57](#_Toc180613943)

Figure 131: Clinic Med Order - Provider Information [57](#_Toc180613944)

Figure 132: Clinic Med Order - PADE Activity [57](#_Toc180613945)

Figure 133: Clinic Med Order - Administration Hx [58](#_Toc180613946)

Figure 134: Non-VA Med List [58](#_Toc180613947)

Figure 135: Non-VA Med List - Remote Orders Button [58](#_Toc180613948)

Figure 136: Non-VA Med List - Remote Orders [59](#_Toc180613949)

Figure 137: Non-VA Med List - More Button [59](#_Toc180613950)

Figure 138: Non-VA Med List - Expanded View [59](#_Toc180613951)

Figure 139: Non-VA Med List - Help Text [59](#_Toc180613952)

Figure 140: Non-VA Med Orders - Details for Active Medication [60](#_Toc180613953)

Figure 141: Allergies and ADRs Tab [60](#_Toc180613954)

Figure 142: Allergies and ADRs - Allergy Assessment Needed [61](#_Toc180613955)

Figure 143: Allergies and ADRs Column Header Help Text [61](#_Toc180613956)

Figure 144: Allergies and ADRs - Entered in Error Records Indicator [61](#_Toc180613957)

Figure 145: Allergies and ADRs - Entered in Error Records [61](#_Toc180613958)

Figure 146: Allergies and ADRs - Query Editor [62](#_Toc180613959)

Figure 147: Allergies and ADRs - Filter for No Value [62](#_Toc180613960)

Figure 148: Allergies and ADRs - Filter Options [63](#_Toc180613961)

Figure 149: Allergies and ADRs - Sorting Options [63](#_Toc180613962)

Figure 150: Allergies and ADRs - Accordion View [63](#_Toc180613963)

Figure 151: Allergies and ADRs - Accordion View – Records Entered in Error [64](#_Toc180613964)

Figure 152: Vitals Tab [64](#_Toc180613965)

Figure 153: Vitals - Help Text [65](#_Toc180613966)

Figure 154: Vitals - Additional Vitals [65](#_Toc180613967)

Figure 155: Vitals - Display [66](#_Toc180613968)

Figure 156: Vitals - Date Range [66](#_Toc180613969)

Figure 157: Vitals – Commonly Used Date Ranges [66](#_Toc180613970)

Figure 158: Vitals - Date Range Display [67](#_Toc180613971)

Figure 159: Vitals - Expanded View [67](#_Toc180613972)

Figure 160: Vitals - Graphing [67](#_Toc180613973)

Figure 161: Vitals - Regression Lines and Labels [68](#_Toc180613974)

Figure 162: Labs Tab [68](#_Toc180613975)

Figure 163: Labs - Column Headers [68](#_Toc180613976)

Figure 164: Labs - Help Text [68](#_Toc180613977)

Figure 165: Labs - Test Record Expanded View [69](#_Toc180613978)

Figure 166: Labs - Lab Results Pending [69](#_Toc180613979)

Figure 167: Labs - No Lab Data [69](#_Toc180613980)

Figure 168: Labs - Show Query Editor Button [70](#_Toc180613981)

Figure 169: Labs - Filter and Sorting Options [70](#_Toc180613982)

Figure 170: Progress Notes Tab [71](#_Toc180613983)

Figure 171: Progress Notes - Column Headers [71](#_Toc180613984)

Figure 172: Progress Notes - Help Text [71](#_Toc180613985)

Figure 173: Progress Notes - Expanded View [72](#_Toc180613986)

Figure 174: Progress Notes - Interdisciplinary Note [72](#_Toc180613987)

Figure 175: Progress Notes - Query Editor Button [72](#_Toc180613988)

Figure 176: Progress Notes - Filter and Sorting Options [73](#_Toc180613989)

Figure 177: Consults Tab [73](#_Toc180613990)

Figure 178: Consults - Column Headers [73](#_Toc180613991)

Figure 179: Consults - Help Text [74](#_Toc180613992)

Figure 180: Consults - Expanded View [74](#_Toc180613993)

Figure 181: Consults - Filter and Sort [75](#_Toc180613994)

Figure 182: Problem List Tab [75](#_Toc180613995)

Figure 183: Problem List - Column Headers [76](#_Toc180613996)

Figure 184: Problem List - Help Text [76](#_Toc180613997)

Figure 185: Problem List - Expanded View [77](#_Toc180613998)

Figure 186: Problem List - Filter and Sort Options [77](#_Toc180613999)

Figure 187: Immunization Tab [78](#_Toc180614000)

Figure 188: Immunization - Column Headers [78](#_Toc180614001)

Figure 189: Immunization - Help Text [78](#_Toc180614002)

Figure 190: Immunization - Expanded View [79](#_Toc180614003)

Figure 191: Immunization - Filters and Sort Options [79](#_Toc180614004)

Figure 192: Appointments Tab [80](#_Toc180614005)

Figure 193: Appointments - Column Headers [80](#_Toc180614006)

Figure 194: Appointments - Help Text [80](#_Toc180614007)

Figure 195: Appointments - Print Buttons [80](#_Toc180614008)

Figure 196: Appointments - Expanded View [81](#_Toc180614009)

Figure 197: Appointments - Filter and Sort Options [82](#_Toc180614010)

Figure 198: Version and Build Information [83](#_Toc180614011)

Figure 199: Joint Legacy Viewer (JLV) Button [84](#_Toc180614012)

Figure 200: Patient Record Flag Indicator [85](#_Toc180614013)

Figure 201: Patient Record Flags [85](#_Toc180614014)

Figure 202: Patient Record Flag Window [86](#_Toc180614015)

Figure 203: Patient Record Flag Category I Flag Signed, Linked Notes [86](#_Toc180614016)

Figure 204: Patient Record Category Flag I Progress Note Window [87](#_Toc180614017)

Figure 205: Category II Flags [88](#_Toc180614018)

Figure 206: Patient Record Flag Category II Flag Signed, Linked Notes [88](#_Toc180614019)

Figure 207: Patient Record Category Flag II Progress Note Window [88](#_Toc180614020)

Figure 208: Context Status [89](#_Toc180614021)

Figure 209: Context Sharing Confirmation Window [89](#_Toc180614022)

Figure 210: CCOW Button [90](#_Toc180614023)

Figure 211: Re-establishing Context Confirmation [90](#_Toc180614024)

Figure 212: Notification of Failed Context Changes Window [90](#_Toc180614025)

Figure 213: VistA Logo Button [91](#_Toc180614026)

Figure 214: Notification of Patient Change in AMPL [91](#_Toc180614027)

Figure 215: Patient Context Change Cannot be Made in AMPL Notification Window [91](#_Toc180614028)

Figure 216: VistA Spacebar Return Function [92](#_Toc180614029)

Figure 217: Logout Button [94](#_Toc180614030)

Figure 218: Desktop Shortcut [99](#_Toc180614031)

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Document Orientation](#document-orientation)
    - [Organization of the Guide](#organization-of-the-guide)
    - [Assumptions](#assumptions)
    - [Disclaimers](#disclaimers)
    - [Documentation Conventions](#documentation-conventions)
    - [References and Resources](#references-and-resources)
  - [Getting Help](#getting-help)
    - [Hover for Help Text](#hover-for-help-text)
- [System Summary](#system-summary)
  - [System Configuration](#system-configuration)
  - [Data Flows](#data-flows)
  - [User Access Levels](#user-access-levels)
  - [Continuity of Operation](#continuity-of-operation)
- [Getting Started](#getting-started)
  - [Logging On](#logging-on)
- [Pending Orders Manager Landing Page](#pending-orders-manager-landing-page)
  - [Current Query and Query Editor](#current-query-and-query-editor)
    - [National and User Queries](#national-and-user-queries)
  - [Selecting a Patient](#selecting-a-patient)
  - [Outpatient Orders by Date](#outpatient-orders-by-date)
    - [Query Editor](#query-editor)
  - [Outpatient Orders by Location](#outpatient-orders-by-location)
  - [Inpatient Orders](#inpatient-orders)
  - [Clinic Orders](#clinic-orders)
- [Patient Coversheet](#patient-coversheet)
  - [Links](#links)
  - [Patient Banner](#patient-banner)
  - [Patient Detailed Demographics](#patient-detailed-demographics)
  - [Patient Banner Allergies/Adverse Reactions (ADRs)](#patient-banner-allergiesadverse-reactions-adrs)
  - [Crisis, Warnings, Allergies, and Directives (CWAD) Postings](#crisis-warnings-allergies-and-directives-cwad-postings)
- [Patient Domain Tabs](#patient-domain-tabs)
  - [Med List Tab](#med-list-tab)
    - [Outpatient Med List](#outpatient-med-list)
    - [Inpatient Med List](#inpatient-med-list)
    - [Clinic Med List](#clinic-med-list)
    - [Non-VA Med List](#non-va-med-list)
  - [Allergies and ADRs Tab](#allergies-and-adrs-tab)
    - [Allergy and ADRs - Query Editor](#allergy-and-adrs-query-editor)
    - [Allergies and ADRs – Accordion View](#allergies-and-adrs-accordion-view)
  - [Vitals Tab](#vitals-tab)
    - [Vitals by Date Range](#vitals-by-date-range)
    - [Vitals – Expanded View](#vitals-expanded-view)
    - [Vitals – Graphing Capabilities](#vitals-graphing-capabilities)
  - [Labs Tab](#labs-tab)
    - [Labs - Laboratory Test Record Expanded View](#labs-laboratory-test-record-expanded-view)
    - [Labs - Query Editor](#labs-query-editor)
  - [Progress Notes Tab](#progress-notes-tab)
    - [Progress Notes – Expanded View](#progress-notes-expanded-view)
    - [Progress Notes – Query Editor](#progress-notes-query-editor)
  - [Consults Tab](#consults-tab)
    - [Consults Tab – Expanded View](#consults-tab-expanded-view)
    - [Consults Tab – Query Editor](#consults-tab-query-editor)
  - [Problem List Tab](#problem-list-tab)
    - [Problem List – Expanded View](#problem-list-expanded-view)
    - [Problem List – Query Editor](#problem-list-query-editor)
  - [Immunization Tab](#immunization-tab)
    - [Immunization Tab – Expanded View](#immunization-tab-expanded-view)
    - [Immunization Tab – Query Editor](#immunization-tab-query-editor)
  - [Appointments Tab](#appointments-tab)
    - [Appointments Tab – Expanded View](#appointments-tab-expanded-view)
    - [Appointments Tab – Query Editor](#appointments-tab-query-editor)
- [Version and Build Information](#version-and-build-information)
  - [Date Formats for Entry](#date-formats-for-entry)
  - [Time Display](#time-display)
- [Joint Legacy Viewer (JLV) Button](#joint-legacy-viewer-jlv-button)
- [Patient Record Flag](#patient-record-flag)
  - [Patient Record Flag Window Display](#patient-record-flag-window-display)
  - [Patient Record Flag – Category I Flags (National)](#patient-record-flag-category-i-flags-national)
  - [Patient Record Flag – Category II Flags (Clinical)](#patient-record-flag-category-ii-flags-clinical)
- [Clinical Context Object Workgroup (CCOW)](#clinical-context-object-workgroup-ccow)
  - [Desktop Patient Context – Context Status](#desktop-patient-context-context-status)
  - [Desktop Patient Context – Suspend (Break) Context Links](#desktop-patient-context-suspend-break-context-links)
  - [Desktop Patient Context – Re-establish (Rejoin) Context Link](#desktop-patient-context-re-establish-rejoin-context-link)
  - [Desktop Patient Context – Notification of Failed Context Changes](#desktop-patient-context-notification-of-failed-context-changes)
- [VistA ‘Spacebar Return’ Functionality in AMPL GUI Application](#vista-spacebar-return-functionality-in-ampl-gui-application)
  - [VistA Logo Button](#vista-logo-button)
  - [VistA Patient Context – Change Cannot be Done in AMPL](#vista-patient-context-change-cannot-be-done-in-ampl)
  - [Vista ‘Spacebar Return’ Function](#vista-spacebar-return-function)
- [Changing User ID and Password](#changing-user-id-and-password)
- [Exit System](#exit-system)
- [Caveats and Exceptions](#caveats-and-exceptions)
- [Troubleshooting](#troubleshooting)
- [Acronyms and Abbreviations](#acronyms-and-abbreviations)
- [Appendix A: Post-implementation Access or Removal Requests](#appendix-a-post-implementation-access-or-removal-requests)
- [Appendix B: AMPL Desktop Shortcut](#appendix-b-ampl-desktop-shortcut)
Advanced Medication Platform (AMPL) Graphic User Interface (GUI) is a front-end application supporting the Department of Veterans Affairs (VA) pharmacists by fulfilling the need for medical knowledge during patient care. Access to relevant medical knowledge can lead to increased quality of care, better efficiency, and improved health outcomes. It can also decrease the potential for errors and adverse events resulting in decreased cost and increased provider and patient satisfaction. Incorporating GUI capabilities into the processing of pharmacy medication orders is a way to minimize risks and enhance health care.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

AMPL GUI is a Graphic User Interface application tailored to users of the Veterans Health Information Systems and Technology Architecture (VistA) Pharmacy packages. AMPL GUI provides pharmacists with a single point of access to patients’ medical data from all VA Medical Centers in a clearer and more user-friendly display. AMPL GUI is intended to advance VA’s ongoing efforts to employ robust electronic health records and improve the efficiency and safety of the medication order process.

AMPL GUI supports the current workflow as well as the development and incorporation of modern technology, functionality, and techniques. It will allow users to make more informed decisions using clinical knowledge and patient-specific expandable information, intelligently filtered, sorted, organized, and presented within a single application as care is being delivered.

AMPL GUI displays data from the following domains as well as the Pending Order Manager Display:

- Allergies/ADRs
- Appointments
- Consults
- Demographics
- Immunizations
- Lab
- Pharmacy
- Problem List
- Progress Notes
- Vitals

## Document Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The AMPL User Guide is formatted comparable to the *Computerized Patient Record System (CPRS) User Manual: GUI Version*.

### Organization of the Guide

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This guide is organized in the way users will initially access AMPL GUI. It is organized in a way to help the reader understand the basic layout of AMPL GUI and provide the reader with information about the specific tasks that pharmacy staff need to perform. The contents are organized as a functionality listing, starting with the features of the patient header, then going tab by tab through each set of clinical offerings.

### Assumptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The user guide is written from the perspective of VA users, assuming the following:

- User can open, navigate, and use a web browser.
- User can use web-based applications, their menu options, and navigation tools.
- User has completed any prerequisite training specific to the AMPL GUI application.
- User has been provided access to the AMPL GUI application.
- Pharmacy staff who have access to AMPL GUI will use their Personal Identity Verification (PIV) card to sign on. A URL will be given during implementation.
- The functionality of AMPL GUI will be used to support Veterans Health Administration (VHA) and/or Veterans Benefits Administration (VBA) workflows.

### Disclaimers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Software Disclaimer

This software was developed at the Department of Veterans Affairs by employees of the Federal Government in the course of their official duties. Pursuant to Title 17 Section 105 of the United States Code this software is not subject to copyright protection and is in the public domain. VA assumes no responsibility whatsoever for its use by other parties, and makes no guarantees, expressed or implied, about its quality, reliability, or any other characteristic. We appreciate acknowledgement if the software is used. This software can be redistributed and/or modified freely if any derivative works bear some notice that they are derived from it, and any modified versions bear some notice that they have been modified.

#### Documentation Disclaimer

The appearance of external hyperlink references in this guide does not constitute endorsement by the VA of this website or the information, products, or services contained therein. The VA does not exercise any editorial control over the information you may find at these locations. Such links are provided and are consistent with the stated purpose of the VA.

### Documentation Conventions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Various symbols are used throughout the documentation to alert the reader to special information. The following shows the symbols being used and the description of each:

![](ampl-user-guide/002.png) The Information symbol indicated especially important or helpful information.

In addition, the AMPL GUI application uses several symbols. The following figures list these symbols and include a brief description of how it is used:

![](ampl-user-guide/003.png)This icon designates that the column is sorted – Ascending (the number listed next to the arrow is showing the sort order for that column if more than one column is sorted).

![](ampl-user-guide/004.png)This icon designates that the column is sorted – Descending (the number listed next to the arrow is showing the sort order for that column if more than one column is sorted).

![](ampl-user-guide/005.png)This icon is used to indicate columns are hidden from view.

![](ampl-user-guide/006.png)This symbol, located next to a clinic record, indicates that there is at least one order for that clinic with a priority of STAT, ASAP, or a schedule of NOW.

![](ampl-user-guide/007.png) Patient Context Indicator – Indicates whether CCOW is synchronizing patients with other GUIs

![](ampl-user-guide/008.png) VistA button - Allows the user to choose the last patient accessed in VistA similar to ‘Spacebar Return’ functionality 

![](ampl-user-guide/009.png) Refresh icon

![](ampl-user-guide/010.png) Reset icon

![](ampl-user-guide/011.png) Filter icon

![](ampl-user-guide/012.png) Medication List tab – Indicates Remote Orders

![](ampl-user-guide/013.png) Patient Lookup icon

![](ampl-user-guide/014.png) Add icon

![](ampl-user-guide/015.png) More button – Displays Expanded view of Medication Orders

![](ampl-user-guide/016.png) Table icon

![](ampl-user-guide/017.png) The Caution/Warning symbol indicates that data within a tab may be incomplete. The information may be updated by refreshing the patient.

![](ampl-user-guide/018.png) Entered in Error NOTE: Notice the difference between these two icons, the Entered in Error icon has a pink background.

Other Important Notes:

- For all instances where time is displayed, the time will reflect the time zone of where the item was entered and not update to the user’s time zone.
- Some data fields in VistA, along with certain data changes done through FileMan will NOT trigger an update to AMPL GUI. See the list below for specific data trigger issues. More details are provided in Section 2.2 Data Flows.
  - Date of Birth
  - Temporary Mailing Information Phone Numbers
  - Emergency Contact Info Relationship
  - Emergency Contact Info Phone Numbers
  - POW War Field
  - Combat from Date
  - Combat to Date
  - Combat Location
  - Nature of Order
  - Prescription Refills without Status Change

### References and Resources

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Additional information on AMPL GUI can be found in the following documents:

- AMPL Technical Manual
- AMPL GUI Deployment, Installation, and Rollback Guide (DIBR)

## Getting Help

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A future version of this document will include online help for how-to information, AMPL GUI Resources, access to AMPL GUI training videos, and additional training materials.

Prior to contacting the Enterprise Service Desk (ESD) for support, please refer to <u>3.1</u> for detailed information about how to access AMPL GUI and to section <u>15</u> for suggested resolution steps and troubleshooting information.

If you are an authorized user that has trouble logging in to AMPL or experiencing other application issues, please contact the Enterprise Service Desk via telephone or by using the Your IT self-service portal for assistance.

If you are unable to retrieve community partner documents for a patient, please contact your local Veterans Health Information Exchange (VHIE) Coordinator.

### Hover for Help Text

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Help text is widely available throughout AMPL by hovering over text or data fields including column headers, symbols, facility numbers (hovering provides facility name), and Query Editors (date box and filter text box), Patient’s Social Security Number (hovering displays the full 9 digits).

Examples are included in sections as applicable.

# System Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

AMPL GUI is a web-based application that is intended to assist with accessing and displaying of pharmacy orders and relevant patient data in the support of processing pharmacy orders.

It consists of two primary functions, the Pending Order Manager (POM) and the Patient Coversheet. The POM is used to find and organize pharmacy orders that need actions. It supports the ability to create a queue of orders that then can be used to retrieve a patient’s record in the coversheet. The AMPL GUI patient coversheet, through a series of tabs, displays pharmacologically relevant aspects of the patient medical record. AMPL GUI is read-only for the initial release, with urgent future plans to convert to read/write functionality.

## System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The system is hosted in the Veterans Affairs Enterprise Cloud (VAEC) Amazon Web Services (AWS) cloud. It is solely accessed through a web browser. The preferred browser is Google Chrome, but most modern web browsers should be acceptable. Microsoft Explorer is not supported.

Access to the VA network and a web browser is needed to access AMPL GUI. To utilize the AMPL GUI’s Clinical Context Object Workgroup (CCOW) functionality, CCOW needs to be installed and configured on the workstation.

## Data Flows

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a patient’s record is accessed in AMPL, the pharmacist is provided a comprehensive view of local and remote clinical patient data to provide enhanced decision support by bringing together several domains of patient data including patient demographics, CWAD, allergies and adverse reactions, consultations, immunizations, vitals, progress notes, problem lists, labs, medications, and appointments. All this data is obtained from VistA through the Veterans Data Integration and Federation (VDIF) service which aggregates data from all VA Medical Centers where that patient has been seen.

Most data updates made in VistA trigger propagation of that data through several systems in VDIF to ultimately be available to AMPL. This process is designed to occur quickly such that changes in VistA are reflected in AMPL within minutes. There are times that the system has a backlog with a queue of data to be processed, which may degrade the response time for data changes to be available to AMPL.

Patient demographics by themselves do not trigger propagation of data to VDIF. If a change is made only to a patient’s demographic information in VistA, those changes will not be immediately reflected in VDIF or AMPL. See section 1.2.4 for a list. Once other changes are made for the patient that do trigger data propagation, such as addition of a medication order or allergy, status change of a medication order or allergy, or any other changes that trigger propagation to VDIF, the patient demographics changes will be propagated to AMPL at that time.

Patient data flowing from VistA is stored by VDIF. It is transmitted upon request to AMPL in either Fast Healthcare Interoperability Resources (FHIR) format, a standard mechanism for sharing health data or using custom requests.

In addition to patient data, AMPL also provides functionality to assist pharmacists with managing pending orders. The data in the Pending Orders Manager is pulled using VDIF custom service calls to the currently selected VistA site. An AMPL user can select a VistA station and see the Pending Orders for that site or search for patients and open their records from that site. Please refer to section <u>3.1</u> for details on how to change the selected station.

<span id="_Toc180613815" class="anchor"></span>Figure 1: Logical High Level AMPL GUI HealthShare Data Flow

![](ampl-user-guide/019.png)

## User Access Levels

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

AMPL GUI implements a single level of user access. Access is granted at the enterprise level via an Active Directory (AD) group. No local VistA credentials are necessary to use AMPL GUI.

## Continuity of Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

AMPL GUI is hosted on the Amazon Web Service (AWS) cloud, managed by the Veterans Affairs Enterprise Cloud (VAEC) group. This environment is highly available and is unlikely to experience an extended outage. AMPL GUI is an enhancement to existing pharmacy systems and does not replace any existing system. In the unlikely event that AMPL GUI is unavailable, traditional pharmacy systems can still be utilized.

# Getting Started

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Pharmacy staff will be granted access to AMPL GUI and will use their Personal Identity Verification (PIV) card for sign on. If you currently do not have access to AMPL GUI, please refer to <u>Appendix A: Post-implementation Access or Removal Requests</u> for access instructions.

## Logging On

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following steps will display the process of logging on to AMPL GUI using Single Sign-On Integration (SSOi) and PIV authentication, similar to other web applications.

The application can be easily accessed by creating a Desktop Shortcut. Please refer to <u>Appendix B: AMPL Desktop Shortcut</u>.

1.  Enter the AMPL URL (<https://ampl.vaec.va.gov>) into the address bar of your internet browser. The following login page will appear:

<span id="_Toc180613816" class="anchor"></span>Figure 2: AMPL GUI Login Page

![](ampl-user-guide/020.png)

2.  After clicking Login, users are redirected to the VA SSOi page (see image below)
    1.  Click the Sign in with VA Personal Identity Verification (PIV) Card graphic.
    2.  Select the appropriate certificate and click OK.
    3.  Enter your Personal Identification Number (PIN) and click OK.
    4.  If PIV card is unavailable, user can sign in with network credentials by clicking View Other Sign-in Options.

<span id="_Toc180613817" class="anchor"></span>Figure 3: SSOi Page for VA Users

![](ampl-user-guide/021.png)

3.  A pop-up window will appear and require the user to enter their 3-digit Station \#. This allows AMPL GUI to retrieve local data from the correct database. Previous station number will be retained if the computer is the same and cookies do not get cleared.

> ![](ampl-user-guide/022.png)NOTE: If the user moves to another computer, they will have to re-enter the station number. Additionally, if the browser gets cleared of cookies and site data on a computer, then they will be prompted to re-select the station number again.

<span id="_Toc180613818" class="anchor"></span>Figure 4: Set VistA Context

![](ampl-user-guide/023.png)

> ![](ampl-user-guide/024.png)NOTE: Once logged in, the selected Station may be changed at any time by clicking the dropdown next to your username in the upper right-hand corner of the screen. See figure below:

<span id="_Toc180613819" class="anchor"></span>Figure 5: Change Station

![](ampl-user-guide/025.png)

4.  Once logged in, The Pending Orders Manager (POM) landing page will display.

> On the POM you can select one or more patients from the list of pending orders as described in <u>Pending Orders Manager Landing Page</u>

<span id="_Toc180613820" class="anchor"></span>Figure 6: Pending Orders Manager Landing Page – Patient Table

> ![](ampl-user-guide/026.png)

# Pending Orders Manager Landing Page

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the Pending Orders Manager Landing Page, the tabs are organized for pharmacist’s specific role such as, Outpatient Pharmacists have the tabs Outpatient Orders by Date, or by Location. Inpatient Pharmacists have the tab Inpatient Orders and Clinical Pharmacists have the Clinic Orders tab. All are available on the POM in case user switches roles or have multiple roles. On each tab header there is a count of the number of orders currently pending at the station the user is signed into. A refresh button is available on each tab header to update the data. See figure below:

<span id="_Toc180613821" class="anchor"></span>Figure 7: Pending Orders Manager Tabs

![](ampl-user-guide/027.png)

To find a patient not included in the Pending Orders Manager lists, use the VistA Patient Lookup box in the header. Please refer to section <u>Patient Coversheet</u> for additional information. See figure below:

<span id="_Toc180613822" class="anchor"></span>Figure 8: VistA Patient Lookup

![](ampl-user-guide/028.png)

For a list of available criteria that can be used for patient lookup, click the “i” Button to display Search Criteria Help. See figures below:

<span id="_Toc180613823" class="anchor"></span>Figure 9: VistA Patient Lookup Info Button

![](ampl-user-guide/029.png)

<span id="_Toc180613824" class="anchor"></span>Figure 10: Patient Lookup Search Criteria Help

![](ampl-user-guide/030.png)

VistA logo button provides a mechanism to mimic VistA's last patient selected functionality. See <u>VistA Logo Button</u> for details.

<span id="_Toc180613825" class="anchor"></span>Figure 11: VistA Logo Button

![](ampl-user-guide/031.png)

## Current Query and Query Editor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each tab may open with a filter and sort applied, which can be seen in the Current Query display. See figure below:

<span id="_Toc180613826" class="anchor"></span>Figure 12: Current Query

![](ampl-user-guide/032.png)

To modify the Current Query, open the Query Editor by clicking on the blue arrow next to the Current Query. To filter by certain fields, select the criteria to use for further filtering by selecting from the Select Filter Field dropdown list. Once the fields are defined, click Add to have the filter added to the search criteria. Continue this process with other filters, as needed.

The sort may be added or modified by selecting fields from the sort section dropdown menu of the Query Editor. Once the fields are defined, click Add to have the filter added to the search criteria. Once completed, click on Refresh to update the display. To delete a filter, select the red “X” icon to the right of it. To clear filters added by the user and return to the tab’s default, click the Reset button.

If a column is used to sort the data, a green arrow ![](ampl-user-guide/033.png) appears next to the column header. To reverse the sort order, click on the green arrow. Repeatedly clicking the sortable column will toggle between ascending, descending then back to default. If more than 1 column is sorted, a small number by the arrow ![](ampl-user-guide/034.png) indicates the order.

See figures below:

<span id="_Toc180613827" class="anchor"></span>Figure 13: Column Filter and Sort Icons

![](ampl-user-guide/035.png)

### National and User Queries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span class="mark">The query tool allows users to create and save default selections on the POM for the Outpatient Orders by Date, Outpatient Orders by Location, Inpatient Orders and Clinic Orders Tabs.</span>

## Selecting a Patient

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once a tab is selected and the Outpatient site, Ordering Institution, Ward group, Ward or Clinic is chosen, a list of patients with related pending orders will display. One or more patients may be selected from the list for processing. If multiple patients are selected, they will be added to the patient queue and their names will display at the bottom of the screen. Several patient identifiers display in the patient queue to assist with selecting the correct patient, including last four of the Social Security Number, Date of Birth and Ward Location if the patient is admitted. If the patient is marked as a sensitive record, this information will be replaced with asterisks. Sensitive patients may not be selected or viewed at this time. See figure below:

<span id="_Toc180613828" class="anchor"></span>Figure 14: Patient Queue

![](ampl-user-guide/036.png)

If a patient is selected in the VistA Patient Lookup box, the name will be added to the Patient Queue. Each additional patient(s) selected is added to the Patient Queue. The Queue is retained if the user toggles from Pending Orders Manager and back to the Coversheet. See figures below:

<span id="_Toc180613829" class="anchor"></span>Figure 15: Patient Cover Sheet with Patient Queue List

![](ampl-user-guide/037.png)

<span id="_Toc180613830" class="anchor"></span>Figure 16: POM Button Toggle to Coversheet and Retained in Patient Queue

![](ampl-user-guide/038.png)

The Patient Queue is cleared if user returns to the Pending Orders Manager page by changing stations or logging out of AMPL and logging back in. It is not retained in future sessions.

## Outpatient Orders by Date

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Outpatient Orders by Date is the default tab on the Pending Orders Manager page. To display orders, select a specific Outpatient Site from the dropdown menu. All sites related to the login facility will display. The total number of orders will be visible in the blue bubble in the tab, as well as a Refresh button to update the list. See figure below:

<span id="_Toc180613831" class="anchor"></span>Figure 17: Outpatient Orders by Date Tab

![](ampl-user-guide/039.png)

To change the Outpatient Site or Ordering Institution, click on the dropdown menu and all sites related to the login facility will display, with checkboxes to allow for multiple selections. See figure below:

<span id="_Toc180613832" class="anchor"></span>Figure 18: Outpatient Orders by Date - Site Selection

![](ampl-user-guide/040.png)

Once an Outpatient Site is selected, a chronological list of orders, oldest to newest is displayed, as well as an Order Aging Summary. Neither will display until the Outpatient Site is selected.

> ![](ampl-user-guide/041.png)NOTE: Total number of orders and the Order Aging Summary counts will update if Ordering Institution is selected to further the orders.

<span id="_Toc180613833" class="anchor"></span>Figure 19: Outpatient Orders by Date - Aging Summary

![](ampl-user-guide/042.png)

In the figure below, T-5 Days is selected, and the patient selection list will be filtered to only patients with orders from that date range.

This quick filter feature uses the same Reset button as all other query filters. For additional details, please refer to section <u>Query Editor</u>

<span id="_Toc180613834" class="anchor"></span>Figure 20: Outpatient Orders by Date – Aging Summary Quick Filter

![](ampl-user-guide/043.png)

When an Outpatient Site is selected, the order display defaults to All Ordering Institutions or to the single Ordering Institution if the Outpatient site only has one. To further filter the orders for the site, select a specific Ordering Institution by using the dropdown menu and selecting from the list. See figure below:

<span id="_Toc180613835" class="anchor"></span>Figure 21: Outpatient Orders by Date - Selecting an Ordering Institution

![](ampl-user-guide/044.png)

Once the Ordering Institution is selected, the orders for that institution will display in chronological order, oldest to newest. The display also includes the Order Aging Summary and the total number of orders for that Ordering Institution. See figure below:

<span id="_Toc180613836" class="anchor"></span>Figure 22: Outpatient Orders by Date - Site and Institution Selected

![](ampl-user-guide/045.png)

Orders will display for the patients who meet the criteria above.

The column headers include Date/Time Entered, Patient, DOB, Pharmacy OI, Routing, Priority, Flagged, Provider and Location. The default view includes All Records, 50 Results/page.

<span id="_Toc180613837" class="anchor"></span>Figure 23: Outpatient Orders by Date - Patient List

![](ampl-user-guide/046.png)

From the list of Orders, specific orders for one or more patients may be selected by checking the order(s) and the Process Selected button. The complete list of patients may be loaded by using the Process All button.

### Query Editor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To filter this list before processing, open the Query Editor by clicking the arrow next to “Current Query” and select the criteria to use for further filtering by selecting from the Select Filter Field dropdown list. See figure below:

<span id="_Toc180613838" class="anchor"></span>Figure 24: Outpatient Orders by Date - Query Editor Filters

![](ampl-user-guide/047.png)

Continue building a filter by selecting from the dropdown list of operators “contains”, “is”, or “is not” as appropriate. For this example, Routing was selected, then the “is” operator was selected to further restrict output and “Window” was chosen as the Routing. See figure below:

<span id="_Toc180613839" class="anchor"></span>Figure 25: Outpatient Orders by Date - Query Editor Filter

![](ampl-user-guide/048.png)

Click Add to have the filter added to the search criteria. Continue this process with other filters, as needed. Once completed, click on Refresh to update the display. To delete a filter, select the red “X” icon to the right of it. To clear filters added by the user and return to the tab’s default, click the Reset button. See figure below:

<span id="_Toc180613840" class="anchor"></span>Figure 26: Outpatient Orders by Date - Query Editor Filter Applied

![](ampl-user-guide/049.png)

This filter reduced the results from 292 to 8.

<span id="_Toc180613841" class="anchor"></span>Figure 27: Outpatient Orders by Date - Results of Query Filter Applied to List

![](ampl-user-guide/050.png)

For some filters, default values are added to the operator and criteria. For example, if the Supply filter is chosen, the other fields default to “is” and “true”. See figure below:

<span id="_Toc180613842" class="anchor"></span>Figure 28: Supply Filter - Defaults Other Fields

![](ampl-user-guide/051.png)

When the Provider filter is selected, the operator defaults to “is” and a dropdown list of providers is added. See figure below:

<span id="_Toc180613843" class="anchor"></span>Figure 29: Provider Filter - Defaults

![](ampl-user-guide/052.png)

If a date filter is selected, a list of common date ranges is available by clicking the arrow to the left of the date field. See figure below:

<span id="_Toc180613844" class="anchor"></span>Figure 30: Date Filter - Commonly Used Date Ranges

![](ampl-user-guide/053.png)

Help Text is available by hovering over the date box. This is a widely available feature throughout AMPL.

<span id="_Toc180613845" class="anchor"></span>Figure 31: Query for Date Field Quick List

![](ampl-user-guide/054.png)

## Outpatient Orders by Location

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To display Outpatient Orders by Location, click on that tab from the Pending Orders Manager page, then select a specific Outpatient Site and Ordering Institution. The total number of orders will be visible in the blue bubble in the tab, as well as a Refresh button to update the list. See figure below:

<span id="_Toc180613846" class="anchor"></span>Figure 32: Outpatient Orders by Location Tab

![](ampl-user-guide/055.png)

To select or change the Outpatient Site, click the dropdown menu and all sites related to the login facility will display. See figure below:

<span id="_Toc180613847" class="anchor"></span>Figure 33: Outpatient Orders by Location - Site Selection

![](ampl-user-guide/056.png)

When an Outpatient Site is selected, the order display defaults to All Ordering Institutions. To further filter the orders for the site, select a specific Ordering Institution by using the dropdown menu and selecting from the list. See figure below:

<span id="_Toc180613848" class="anchor"></span>Figure 34: Outpatient Orders by Location - Selecting an Ordering Institution

![](ampl-user-guide/057.png)

Once the Ordering Institution is selected, a list of orders for the location will display with the total number of orders. See figure below:

<span id="_Toc180613849" class="anchor"></span>Figure 35: Outpatient Orders by Location - Site and Institution Selected

![](ampl-user-guide/058.png)

Some orders may display a STAT symbol in the last column. Hovering over the icon displays help text, “Indicates that there is at least one order for the clinic that has a priority of ‘STAT’, ‘ASAP (EMERGENCY)’ or has a schedule of ‘NOW’. See figure below:

<span id="_Toc180613850" class="anchor"></span>Figure 36: Outpatient Orders by Location - STAT Symbol

![](ampl-user-guide/059.png)

From this location list, orders may be processed for some or all locations. Selecting specific Clinic Group(s) or Clinic(s) adds the patients with orders from those clinics to the Select Patients(s) to Process list. The Select All button above the Clinic Group list adds all patients to the Patient(s) to Process list. A list of patients will display in the Select Patient(s) to Process list below the Location List. See figure below:

<span id="_Toc180613851" class="anchor"></span>Figure 37: Outpatient Orders by Location - Clinic Selected

![](ampl-user-guide/060.png)

From the Select Patient(s) to Process List, select one or more patients and click the Process Selected button located above the Select Patient list at the top right. The Process All button adds all orders to the Patient Queue list for processing. See figures below:

<span id="_Toc180613852" class="anchor"></span>Figure 38: Outpatient Orders by Location - Select Patient(s) to Process List

![](ampl-user-guide/061.png)

<span id="_Toc180613853" class="anchor"></span>Figure 39: Outpatient Orders by Location - Process All Button

![](ampl-user-guide/062.png)

On the Outpatient Orders by Location Tab, there are two places to filter the list, the Group(s) and Clinic(s) section and the Patient(s) to Process section. The process is the same to modify both queries.

To filter the Orders list before processing, open the Query Editor by clicking on the arrow next to “Current Query” and selecting additional criteria from the Select Filter Field dropdown list. See figure below:

<span id="_Toc180613854" class="anchor"></span>Figure 40: Outpatient Orders by Location - Query Editor Filters

![](ampl-user-guide/063.png)

Choosing a field allows filtering by selecting from the dropdown list of operators “contains”, “is”, or “is not” as appropriate. For this example, Drug was selected, then the “is” operator was selected to further restrict output. See figure below:

<span id="_Toc180613855" class="anchor"></span>Figure 41: Outpatient Orders by Location - Query Editor Filter Operators

![](ampl-user-guide/064.png)

Next, click on the “Select a value” dropdown and a list of the available drugs with check boxes will display. Only drugs in the orders are displayed, not the entire drug file list. See figure below:

<span id="_Toc180613856" class="anchor"></span>Figure 42: Outpatient Orders by Location - Query Editor Filters Drug Selected

![](ampl-user-guide/065.png)

Multiple drugs can be selected from the list. Once finished, click Add to have the filter added to the search criteria. See figure below:

<span id="_Toc180613857" class="anchor"></span>Figure 43: Outpatient Orders by Location - Query Editor Search Criteria

![](ampl-user-guide/066.png)

Other filters may be added as needed. When finished, click on Refresh to update the display. To delete a filter, select the red “X” icon to the right of it. To clear filters/sorts added by the user and return to the tab’s default, click the Reset button. See figure below:

<span id="_Toc180613858" class="anchor"></span>Figure 44: Outpatient Orders by Location - Query Editor Delete Icon

![](ampl-user-guide/067.png)

Queries can be set at both the Location and Patient Level.

To add a query at the patient level, select the query editor box in the Select Patient(s) to Process section. Build the filter using the process described above. In this example, the Patient List will be filtered by Priority. To filter the patient list, open the Query Editor by clicking on the arrow next to “Current Query” and selecting additional criteria from the Select Filter Field dropdown list. When the filter is completed, click Add to have the filter added to the search criteria. To apply filters in one or both sections, click the Refresh button in that section. See figure below:

<span id="_Toc180613859" class="anchor"></span>Figure 45: Outpatient Orders by Location - Patient Filter

![](ampl-user-guide/068.png)

## Inpatient Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the Inpatient Orders tab is selected from the Pending Orders Manager page, choose a Division. The total number of orders will be visible in the blue bubble in the tab, as well as a Refresh button to update the list. See figure below:

<span id="_Toc180613860" class="anchor"></span>Figure 46: Inpatient Orders Tab

![](ampl-user-guide/069.png)

To select or change the Division, click on the dropdown menu to display a list of Divisions. Once a Division is selected, the ward group(s) or wards with pending Inpatient Orders will display. An Order Aging Summary is also included. If all pending inpatient orders are less than 1 hour old, the Order Aging Summary will show 0 orders in all columns. See figures below:

<span id="_Toc180613861" class="anchor"></span>Figure 47: Inpatient Orders - Division Selection

![](ampl-user-guide/070.png)

<span id="_Toc180613862" class="anchor"></span>Figure 48: Inpatient Orders - Division Selected

![](ampl-user-guide/071.png)

From this list, the user may select a Ward Group, ward or the Select All button. This will populate a list of patients in the Select Patient(s) to Process list. See figure below:

<span id="_Toc180613863" class="anchor"></span>Figure 49: Inpatient Orders - Ward Group Selected

![](ampl-user-guide/072.png)

From the Select Patient(s) to Process list, one or more patients may be selected by checking the patient’s name(s) and the Process Selected button. The complete list of patients may be loaded by using the Process All button. See figure below:

<span id="_Toc180613864" class="anchor"></span>Figure 50: Inpatient Orders - Select Patient(s) to Process List

![](ampl-user-guide/073.png)

To further filter this list before processing, open the Query Editor by clicking on the arrow next to “Current Query”. Select the criteria for further filtering from the Select Filter Field dropdown list. See figure below:

<span id="_Toc180613865" class="anchor"></span>Figure 51: Inpatient Orders - Query Editor Filters

![](ampl-user-guide/074.png)

Continue building a filter by selecting from the dropdown list of operators “contains”, “is”, or “is not” as appropriate. For this example, Drug was selected, then the “is” operator was selected to further restrict output. See figure below:

<span id="_Toc180613866" class="anchor"></span>Figure 52: Inpatient Orders - Query Editor Filter Applied

![](ampl-user-guide/075.png)

Next, click on the “Select a value” dropdown and a list of the available drugs with check boxes will display. Only drugs in the orders are displayed, not the entire drug file list. See figure below:

<span id="_Toc180613867" class="anchor"></span>Figure 53: Inpatient Orders - Query Editor Filters Drug Value

![](ampl-user-guide/076.png)

Multiple drugs may be selected from the list. Click Add to have the filter added to the search criteria. See figure below:

<span id="_Toc180613868" class="anchor"></span>Figure 54: Inpatient Orders - Query Editor Search Criteria

![](ampl-user-guide/077.png)

Continue this process with other filters as needed. When finished, click on Refresh to update the display. To delete a filter, select the red “X” icon to the right of it. To clear filters/sorts added by the user and return to the tab’s default, click the Reset button. See figure below:

<span id="_Toc180613869" class="anchor"></span>Figure 55: Inpatient Orders - Query Editor Delete Icon

![](ampl-user-guide/078.png)

To save a filter for future use, click “Save Query” and give the query a name. Once saved, the query will be available under the “User Queries” dropdown on the right side of the Query Editor window and can be executed via the “Refresh” button.

<span id="_Toc181786688" class="anchor"></span>Figure 56: Inpatient Orders - "Save Query” Dialog

![](ampl-user-guide/079.png)

<span id="_Toc181786689" class="anchor"></span>Figure 57: Inpatient Orders – Saved User Query Dropdown Menu

![](ampl-user-guide/080.png)

The list may be filtered at the Ward Group level or the Select Patient(s) to Process level.

## Clinic Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the Clinic Orders tab is selected from the Pending Orders Manager page, choose a Division. The total number of orders will be visible in the blue bubble on the tab, as well as a Refresh button to update the list. See figure below:

<span id="_Toc180613871" class="anchor"></span>Figure 58: Clinic Orders Tab

![](ampl-user-guide/081.png)

To select or change the Division, click on the dropdown menu, it will display a list of Divisions. Once the Division is selected, the Clinic Group(s) and Clinic(s) associated with that Division will display. See figures below:

<span id="_Toc180613872" class="anchor"></span>Figure 59: Clinic Orders - Select Division

![](ampl-user-guide/082.png)

<span id="_Toc180613873" class="anchor"></span>Figure 60: Clinic Orders - Division Selected

![](ampl-user-guide/083.png)

From this list, orders can be processed by selecting a Clinic Group, Clinic or the Select All button. The Select Patient(s) to Process list will populate with patients who have pending orders from the clinic(s) selected. See figure below:

<span id="_Toc180613874" class="anchor"></span>Figure 61: Clinic Orders - Clinic Group Selected

![](ampl-user-guide/084.png)

Both the Clinic group and Select Patient(s) to Process lists may be further filtered using the Query Editor. To filter the list before processing, open the Query Editor for either the Clinic Group or Select Patient(s) to Process sections by clicking on the arrow next to “Current Query” in that section and choose the criteria to use by selecting from the Select Filter Field dropdown list. Additional filters may be added. See figure below:

<span id="_Toc180613875" class="anchor"></span>Figure 62: Clinic Orders - Query Editor Filters

![](ampl-user-guide/085.png)

From the Select Patient(s) to Process list, one or more patients may be selected by checking the box in front of patient’s name and processed by clicking the Process Selected button. The cover sheet will open for the first patient chosen and other patients selected will be added to the Patient Queue. To add all the patients to the Patient Queue, select the Process All button. On the Select Patient to Process Table, a toggle button, next to the Process All button toggles between a summary listing of all pending clinic orders for a current patient and a listing of individual clinic orders for a patient by date and by pharmacy orderable item. See figure below:

<span id="_Toc180613876" class="anchor"></span>Figure 63: Clinic Orders - Select Patient(s) to Process List Toggle On

![](ampl-user-guide/086.png)

<span id="_Toc180613877" class="anchor"></span>Figure 64: Clinic Orders - Select Patient(s) to Process List Toggle Off

![](ampl-user-guide/087.png)

<span id="_Toc180613878" class="anchor"></span>Figure 65: Clinic Orders - Select Patient(s) to Process List Toggle Button Help Text

![](ampl-user-guide/088.png)

# Patient Coversheet

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once a patient has been selected, the Patient Coversheet displays with a header, footer, patient banner, and Tabs for domains, where the patient may have data stored. See figure below:

<span id="_Toc180613879" class="anchor"></span>Figure 66: Patient Coversheet

![](ampl-user-guide/089.png)

![](ampl-user-guide/090.png)NOTE: Like VistA and CPRS, new changes made to patient data after the patient’s record is accessed in AMPL (entering a new order, discontinuing an active order) are not seen until the patient is refreshed. See figure below:

> In AMPL, the Refresh button is used.

> In CPRS, the File/Refresh Patient Information is used.

> In VistA, close the patient in a backdoor pharmacy option and open the patient again.

<span id="_Toc180613880" class="anchor"></span>Figure 67: Refresh Patient Data

![](ampl-user-guide/091.png)

## Links

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once a patient queue is populated and the first patient record is displayed, a new “Links” button is added to the blue AMPL toolbar. It contains links to outside sources of Clinical Information. See figure below:

<span id="_Toc180613881" class="anchor"></span>Figure 68: Links Button

![](ampl-user-guide/092.png)

![](ampl-user-guide/093.png) NOTE: This is an example list of links, they are subject to change.

## Patient Banner

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The patient banner with Covid-19 testing status, basic demographics, Creatinine Clearance, most recent Serum Creatinine lab result, Body Surface Area (BSA), Height, Weight, Body Mass Index (BMI) and Allergies/ADRs displays on the Coversheet. It also displays on all pages of the patient’s record.

Basic patient demographics included in the patient banner are Patient Name, Social Security Number (SSN), Date of Birth (DOB), Gender, Last Clinic, Last Discharge, RX Patient Status, PCMM info, Eligibility, Service Connection % and Disabilities, Creatinine Clearance (CrCL), Body Surface Area (BSA), Height (HT), Weight (WT), Body Mass Index (BMI), and Patient Narrative. See figure below:

<span id="_Toc180613882" class="anchor"></span>Figure 69: Patient Banner

![](ampl-user-guide/094.png)

<span id="_Toc180613883" class="anchor"></span>Figure 70: Covid-19 Testing Status

![](ampl-user-guide/095.png)

> ![](ampl-user-guide/096.png) NOTE: Only the last four of a patient’s social security number initially displays in AMPL. To see a patient’s full social security number, hover over the field.

If a patient has mail restrictions, an envelope icon will be displayed below Postings and flag boxes.

Next to the mail icon, the specifications of Local Certified Mail or Local-Regular Mail will display a white envelope, Do Not Mail will display a white envelope with a red x and the expiration date will be displayed if applicable.

<span id="_Toc180613884" class="anchor"></span>Figure 71: Mail Restrictions

![](ampl-user-guide/097.png)

> ![](ampl-user-guide/098.png) NOTE: To update a patient record, a Reload button is available. See figure below:

<span id="_Toc180613885" class="anchor"></span>Figure 72: Patient Reload Button

![](ampl-user-guide/099.png)

## Patient Detailed Demographics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In addition to the basic demographics on the Patient Coversheet, additional detailed Patient Demographic information can be accessed and viewed by selecting the More button in the patient header or on the patient picture. See figure below:

<span id="_Toc180613886" class="anchor"></span>Figure 73: Patient Information Banner

![](ampl-user-guide/100.png)

The expanded view will display tabs that contain additional information on Contact Info, Pharmacy Info, Eligibility, Social, Primary Care, Clinic Info, Military Service, and Health Plans/Insurance. See figure below:

<span id="_Toc180613887" class="anchor"></span>Figure 74: Patient Demographic - Details

![](ampl-user-guide/101.png)

The Contact Info tab includes Residential Address, Mailing Address, Temporary Mailing Address, Confidential Address, Emergency Response Information, Emergency Contact Information, Secondary Emergency Contact Information, Next of Kin Information, Secondary Next of Kin Information, Language Date/Time, and Preferred Language. See figure below:

If a patient has been seen at multiple facilities, the Emergency Response Indicator will be displayed from the last facility where the patient was treated.

<span id="_Toc180613888" class="anchor"></span>Figure 75: Contact Info Tab

![](ampl-user-guide/102.png)

The Pharmacy Info tab includes CAP, Mail, Dialysis Patient, CNH Current, Nursing Home Contract, Respite Patient Start Date, Other Language Preference, Remarks, Inpatient/Outpatient Narrative, Mail Status Expiration Date, Patient Rx Status, Community Nursing Home, Last Date of Contract, Respite Patient End Date, and PMI Language Preference. See figure below:

<span id="_Toc180613889" class="anchor"></span>Figure 76: Pharmacy Info Tab

![](ampl-user-guide/103.png)

The Eligibility tab includes Combat Vet Status, Unemployable, Permanent & Total Disabled, Current Means Test Status, Medication Copayment Exemption Status, Rx Patient Status, Primary Eligibility, SC Percent, Rated Disabilities and Environmental Factors. See figure below:

If a patient has been seen at multiple facilities, the following eligibility data will be displayed from the last facility where the patient was treated:

• Current Means Test

• Copay Income Exemption Status

• Primary Eligibility

• Service-Connected

• Service-Connected Percentage

• Environmental Factors (Agent Orange, Radiation, Persian Gulf, Head Neck Cancer (HNC), and Military Sexual Trauma (MST))

<span id="_Toc180613890" class="anchor"></span>Figure 77: Eligibility Tab

![](ampl-user-guide/104.png)

The Social, Primary Care, Clinic Info tab includes Marital Status, Race, Ethnicity, Religious Preference, Method of Collection, Inpatient Attending, Inpatient Provider, Currently enrolled in clinics, and Future Appointments. Primary Care information for patients who are currently admitted includes local Inpatient Attending and Inpatient Provider with Remote site’s PACT and Primary Care Provider with phone number. For Outpatients, it includes local and remote sites’ PACT and Primary Care Provider with phone number. See figure below:

<span id="_Toc180613891" class="anchor"></span>Figure 78: Social, Primary Care, Clinic Info Tab

![](ampl-user-guide/105.png)

The Military Service tab includes a Service Branch/Component table including the Service \#, Entered, Separated, and Discharge. Additional information displays including Conflict Locations, Environmental Factors, Prisoner of War (POW) including From/To, Combat including From/To, War, Location, Military Disability Retirement, Discharge due to Disability, Dental Injury, Teeth Extracted, Purple Heart, and Purple Heart Status. See figure below:

If a patient has been seen at multiple facilities, the following military data will be displayed from the last facility where the patient was treated:

- Military service episodes
- Military conflict locations (Vietnam, Lebanon, Grenada, Panama, Persian Gulf, Somalia, and Yugoslavia)
- Military POW information
- Military Combat information
- Military Service Environmental Factors (Agent Orange, Radiation, Persian Gulf, Head Neck Cancer (HNC), and Military Sexual Trauma (MST))
- Purple Heart information

<span id="_Toc180613892" class="anchor"></span>Figure 79: Military Service Tab

![](ampl-user-guide/106.png)

The Health Plans/Insurance tab includes Health Benefit Plans Currently Assigned to Veteran and a Health Insurance Information table including the Insurance name, Phone Number, Subscriber ID, Group, Holder, Effective date, and Expiration date. See figure below:

<span id="_Toc180613893" class="anchor"></span>Figure 80: Health Plans/Insurance Tab

![](ampl-user-guide/107.png)

For additional Primary Care information, click on the Primary Care Provider (PCP) information and a pop-up window will display. For an outpatient, local and remote PACT and Primary Care provider information displays. If patient is currently admitted, the display includes Inpatient Attending and Inpatient Provider. See figures below:

<span id="_Toc180613894" class="anchor"></span>Figure 81: Primary Care Team Information

![](ampl-user-guide/108.png)

<span id="_Toc180613895" class="anchor"></span>Figure 82: Primary Care Details - Outpatient

![](ampl-user-guide/109.png)

<span id="_Toc180613896" class="anchor"></span>Figure 83: Primary Care Details - Inpatient

![](ampl-user-guide/110.png)

If a user makes changes to only patient demographics information in VistA, those changes will not be reflected in VDIF or AMPL. Patient demographics by themselves do not trigger propagation of data to VDIF.

When other changes are made for the patient that will trigger data propagation from VistA to VDIF, patient demographics changes will also be propagated to AMPL. Examples of data that will trigger propagation are addition of a medication order or allergy or a status change of a medication order or allergy.

## Patient Banner Allergies/Adverse Reactions (ADRs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As part of the patient banner, details of an Allergy/ADR listed can be viewed by selecting the entry without having to go into the Allergy/ADR tab to find the record(s). See figure below:

<span id="_Toc180613897" class="anchor"></span>Figure 84: Allergies/ADRs Listed in Patient Banner

![](ampl-user-guide/111.png)

<span id="_Toc180613898" class="anchor"></span>Figure 85: Allergy Banner Pop-Up Window

![](ampl-user-guide/112.png)

The Allergy/ADR window information lists the GMR Allergy with identifier of the originating file, Causative Agent/Reactant, Signs & Symptoms/Date Entered, Observed/Historical, Observation/Historical Date/Severity, Mechanism, Reaction Type, Facility, Drug Classes, Ingredients, Originator/Origination Date/Time, Verification, and Comments.

The GMR Allergy identifier is determined by the file source of the allergen as shown in the table below:

| Identifier | Originating File                 | VistA File Name/Number     |
|------------|----------------------------------|----------------------------|
| N          | National Drug file, Generic name | VA GENERIC file (#50.6)    |
| N          | National Drug file, Trade name   | NDC/UPN file (#50.67)      |
| A          | VA Allergies file                | GMR ALLERGIES (#120.82)    |
| C          | VA Drug Class                    | VA DRUG CLASS (#50.605)    |
| I          | Ingredients                      | DRUG INGREDIENTS (#50.416) |

Table 2: Indicators

## Crisis, Warnings, Allergies, and Directives (CWAD) Postings

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Crisis, Warnings, Allergies, and Directives (CWAD) Postings button, contained in the header of the AMPL GUI application coversheet, will display only applicable letters from CWAD if the patient record contains any critical information. The CWAD postings are signed/completed progress notes for a patient and the posting letters are:

“C” represents Crisis Notes and is cautionary information about critical behavior or patient health (i.e., suicide attempt).

“W” represents Warning Notes and are notifications that inform about possible risks associated with the patient (i.e., violent patient)

“A” represents any Allergy/ADR that is recorded for the patient or if no allergy assessment has been performed for the patient.

“D” represents Directives (advanced directives) and recorded agreements made by the patient and/or family with clinical staff (i.e., Do Not Resuscitate \[DNR\]).

If the record does not contain any postings, the CWAD Posting button will be labeled ‘No Postings’.

If the record contains No Known Allergies (NKA), the CWAD button will say ‘No Posting’ however when you click on the CWAD button it will display ‘No Known Allergies’ on the top half of the posting window.

See figures below:

<span id="_Toc180613899" class="anchor"></span>Figure 86: Postings Buttons - Indicating Critical Information

![](ampl-user-guide/113.png)

<span id="_Toc180613900" class="anchor"></span>Figure 87: Postings Buttons - Indicating No Postings

![](ampl-user-guide/114.png)

If letters are shown, indicating postings, click on the Posting button and a list will appear in a pop-up window. See figure below:

<span id="_Toc180613901" class="anchor"></span>Figure 88: CWAD - List Window

![](ampl-user-guide/115.png)

The information under Allergies includes GMR Allergy, Severity, Signs/Symptoms, and Facility. The information under Crisis Notes, Warnings, and Directives includes Local Title, Date of Note, and Facility.

For more detail on any of the postings, click on the individual listing in the CWAD list window, and more information will display. The information displayed includes Standard Title, Report Text, Date of Note, Exp Signer, Status, Signed By, Entry Date, Exp Cosigner, Facility/Locations, Signature Date/Time, Author, Urgency, Signature Block Name and Signature Block Title. See figure below:

<span id="_Toc180613902" class="anchor"></span>Figure 89: CWAD - Detailed Display

![](ampl-user-guide/116.png)

# Patient Domain Tabs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Below the Patient header, data is organized under domain tabs. These tabs include Med List, Allergies and ADRs, Vitals, Labs, Progress Notes, Consults, Problem List, Immunizations, and Appointments.

<span id="_Toc180613903" class="anchor"></span>Figure 90: Patient Data Domain Tabs

![](ampl-user-guide/117.png)

## Med List Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Med List Tab displays med orders for Outpatient, Inpatient, Clinic, and Non-VA. There is a refresh button available to refresh the patient’s med list. See figure below:

<span id="_Toc180613904" class="anchor"></span>Figure 91: Med List Tab

![](ampl-user-guide/118.png)

### Outpatient Med List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Outpatient Med list displays Active, Expired, Discontinued, Non-verified, Hold and Pending Orders. The medications included in the discontinued and expired categories are determined by RECENTLY DC’D/EXPIRED DAYS Field (#3.2) in the OUTPATIENT SITE (#59) File.

<span id="_Toc180613905" class="anchor"></span>Figure 92: Outpatient Med List

![](ampl-user-guide/119.png)

To include Local clinic orders, click on the Local Orders (L) button.

To include Remote clinic orders, click on the Remote Orders (R) button in the Non-VA header. If Remote button is disabled, it indicates patient does not have remote orders. See figures below:

<span id="_Toc180613906" class="anchor"></span>Figure 93: Outpatient Med List - Remote Orders Button

![](ampl-user-guide/120.png)

<span id="_Toc180613907" class="anchor"></span>Figure 94: Outpatient Med List - Remote Orders

![](ampl-user-guide/121.png)

#### Outpatient Med List - Expanded View

The More button will bring up the Expanded View. See figure below:

<span id="_Toc180613908" class="anchor"></span>Figure 95: Outpatient Med List - More Button

![](ampl-user-guide/122.png)

The Expanded view displays additional details, including RX#, Generic Drug Name, Dosage, Route, Schedule/(Duration), Indication, Issue Date, Quantity, Days’ Supply, Route (M/W), Refills (total and remaining), Last Fill Date, Status and Provider. See figure below:

<span id="_Toc180613909" class="anchor"></span>Figure 96: Outpatient Med List - Expanded View

![](ampl-user-guide/123.png)

#### Outpatient Med List – Expanded View Help Text

Help text for each column of the Expanded View of Outpatient Med Orders is displayed by hovering over the column header. See figure below:

<span id="_Toc180613910" class="anchor"></span>Figure 97: Outpatient Med List - Help Text

![](ampl-user-guide/124.png)

#### Outpatient Med List - Expanded View Indicators

Outpatient med orders can display various indicators such whether a prescription is copay eligible or marked for Consolidated Mail Outpatient Pharmacies (CMOP), highly automated facilities that fill and mail prescriptions to Veterans. Indicators such as the greater sign (\>), an indicator for a CMOP drug, displays after the RX#. Other indicators include “t” for a Titration RX, \$ for copay eligible, “T” for last fill in transmitted or retransmitted CMOP state and “e” for electronic third party billable are displayed immediately after the Prescription Number. See figure below:

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 71%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Indicators</strong></th>
<th><strong>Description</strong></th>
</tr>
<tr class="odd">
<th>CMOP Indicators</th>
<th><p>There are two separate indicators when the drug in an order is marked for Consolidated Mail Outpatient Pharmacy (CMOP) processing. This indicator is displayed after the Order Status if applicable.</p>
<blockquote>
<p>&gt; Drug for the prescription is marked for CMOP</p>
<p>T Displayed when the last fill is either in a Transmitted or Retransmitted</p>
</blockquote>
<p>CMOP state. (This indicator can overwrite the “&gt;” indicator.</p></th>
</tr>
<tr class="header">
<th>Copay Indicator</th>
<th>A “$” displayed to the right of the prescription number indicates the prescription is copay eligible.</th>
</tr>
<tr class="odd">
<th>ePharmacy Indicator</th>
<th>An ‘e’ displayed to the right of the prescription number indicates that the prescription is electronic third party billable.</th>
</tr>
<tr class="header">
<th>Inbound eRX Indicator</th>
<th>An “&amp;” indicates the prescription was received from an outside provider as an Inbound ePrescription.</th>
</tr>
<tr class="odd">
<th>Return to Stock Indicator</th>
<th>An “R” displayed to the right of the Last Fill Date indicates the last fill was returned to stock.</th>
</tr>
<tr class="header">
<th>Titration Indicator</th>
<th>A ‘t’ indicates the prescription is a complex order that includes ‘then’ conjunction</th>
</tr>
<tr class="odd">
<th>Maintenance RX (Titration)</th>
<th>An “m” displayed to the right of the prescription number indicates the prescription has been converted to a maintenance RX from a Titration RX (complex order with a ‘then’ conjunction)</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

<span id="_Toc180613911" class="anchor"></span>Figure 98: CMOP Indicator

![](ampl-user-guide/125.png)

#### Outpatient Med List - Expanded View Remote Orders

A checkbox for Remote Orders is located at the upper left of the window. By checking this box, the remote orders will display at the bottom. See figure below:

<span id="_Toc180613912" class="anchor"></span>Figure 99: Outpatient Med List - Show Remote Orders Checkbox

![](ampl-user-guide/126.png)

#### Outpatient Med Order - Details 

To view details of an Outpatient Med Order, click on it in the Med List or the Expanded View. A pop-up will display with details about the order.

At the bottom of the display, buttons are available to display additional information related to the order including Order Checks, Drug Restrictions/Guidelines, Drug Info, Provider Info and Activity Log. See figures below:

<span id="_Toc180613913" class="anchor"></span>Figure 100: Outpatient Med Order – Active Order Detail Screen

![](ampl-user-guide/127.png)

<span id="_Toc180613914" class="anchor"></span>Figure 101: Outpatient Med Order – Pending Order Detail Screen

![](ampl-user-guide/128.png)

<span id="_Toc180613915" class="anchor"></span>Figure 102: Outpatient Med Order – Additional Details

![](ampl-user-guide/129.png)

Clicking on one of the buttons displays order details relevant to the button selected. See figures below for examples of each:

<span id="_Toc180613916" class="anchor"></span>Figure 103: Outpatient Med Order – Order Check

![](ampl-user-guide/130.png)

<span id="_Toc180613917" class="anchor"></span>Figure 104: Outpatient Med Order - Drug Restriction/Guideline Information

![](ampl-user-guide/131.png)

<span id="_Toc180613918" class="anchor"></span>Figure 105: Outpatient Med Order - Drug Info

![](ampl-user-guide/132.png)

<span id="_Toc180613919" class="anchor"></span>Figure 106: Outpatient Med Order - Provider Info

![](ampl-user-guide/133.png)

<span id="_Toc180613920" class="anchor"></span>Figure 107: Outpatient Med Order - Activity Log

![](ampl-user-guide/134.png)

### Inpatient Med List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Inpatient Med List displays Active, Non-Verified, Pending and Recently DC’d/Expired (Last 24 Hours) for patients currently admitted at the local facility. See figure below:

<span id="_Toc180613921" class="anchor"></span>Figure 108: Inpatient Med List

![](ampl-user-guide/135.png)

#### Inpatient Med List - Expanded View

The More button will bring up the Expanded View. See figure below:

<span id="_Toc180613922" class="anchor"></span>Figure 109: Inpatient Med List - More Button

![](ampl-user-guide/136.png)

The Expanded View includes Generic Drug Name, Dosage/Infusion Rate, Route, Schedule/Duration, Indication, IV Type, Schedule Type, Start Date/Time, Stop Date/Time, Status, Last BCMA Action, Action Status, Missing Dose Indicator, WS/PD Indicator, and Provider. See figure below:

<span id="_Toc180613923" class="anchor"></span>Figure 110: Inpatient Med List - Expanded View

![](ampl-user-guide/137.png)

#### Inpatient Med List - Expanded View Help Text

Help text for each column of the Expanded View - Inpatient Med Orders is displayed by hovering over the column header. See figure below:

<span id="_Toc180613924" class="anchor"></span>Figure 111: Inpatient Med List - Help Text

![](ampl-user-guide/138.png)

#### Inpatient Med Order - Details

To view details of an Inpatient Med Order, click on it in the Med List or the Expanded View. A pop-up will display with details about the order. See figure below:

<span id="_Toc180613925" class="anchor"></span>Figure 112: Inpatient Med Order - Active Orders Detail Screen

![](ampl-user-guide/139.png)

At the bottom of the Inpatient Med Order screen, buttons are available that will display additional information related to the order including Order Checks, Drug Restrictions/Guidelines, Drug Info, Provider Info, Pharmacy Automated Dispensing Equipment (PADE) Inventory Activity, and Admin Hx (History). See figure below:

<span id="_Toc180613926" class="anchor"></span>Figure 113: Inpatient Med Order - Additional Details

![](ampl-user-guide/140.png)

Clicking on one of the buttons displays order details relevant to the button selected. See figures below for examples of each:

<span id="_Toc180613927" class="anchor"></span>Figure 114: Inpatient Med Order - Order Check

![](ampl-user-guide/141.png)

<span id="_Toc180613928" class="anchor"></span>Figure 115: Inpatient Med Order - Drug Restriction/Guideline Information

![](ampl-user-guide/142.png)

<span id="_Toc180613929" class="anchor"></span>Figure 116: Inpatient Med Order - Drug Info

![](ampl-user-guide/143.png)

<span id="_Toc180613930" class="anchor"></span>Figure 117: Inpatient Med Order - Provider Information

![](ampl-user-guide/144.png)

If the Inpatient location has a PADE dispensing device, the PADE Inventory Activity button will display the PADE activity log of all meds dispensed in the past thirty days. It includes current and historical activity from previous admissions or visits. See figure below:

<span id="_Toc180613931" class="anchor"></span>Figure 118: Inpatient Med Order - PADE Inventory

![](ampl-user-guide/145.png)

If the Inpatient location uses BCMA, the Administration History (Admin HX) button will display administrations recorded in BCMA for the medication, most recent records first. See figure below:

<span id="_Toc180613932" class="anchor"></span>Figure 119: Inpatient Med Order - Administration Hx

![](ampl-user-guide/146.png)

### Clinic Med List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Clinic Med List displays active clinic med orders by location at the local facility. See figure below:

<span id="_Toc180613933" class="anchor"></span>Figure 120: Clinic Med List

![](ampl-user-guide/147.png)

To include Remote clinic orders, click on the Remote Orders (R) button in the Clinic header. If Remote button is disabled, it indicates patient does not have remote orders. See figures below:

<span id="_Toc180613934" class="anchor"></span>Figure 121: Clinic Med List - Remote Orders Button

![](ampl-user-guide/148.png)

<span id="_Toc180613935" class="anchor"></span>Figure 122: Clinic Med List - Remote Orders

![](ampl-user-guide/149.png)

#### Clinic Med List - Expanded View

To access an Expanded View of Clinic Med Orders for a patient, click the MORE button.

The Expanded View of Clinic Med Orders includes Generic Drug Name, Dosage/Infusion Rate, Route, Schedule/(Duration), Indication, IV Type (if applicable), Schedule Type, Start Date/Time, Stop Date/Time, Status, Last BCMA Action, Action Status, Missing Dose Indicator, PADE/Ward Stock Indicator (PD Ind), and Provider.

The column to the left of the drug name will display a flag icon if the order is flagged. See figure below:

<span id="_Toc180613936" class="anchor"></span>Figure 123: Clinic Med List - Expanded View

![](ampl-user-guide/150.png)

#### Clinic Med List - Expanded View Help Text

The column header for the Expanded View of the Clinic Med Orders records displays help text by hovering over the column header. See figure below:

<span id="_Toc180613937" class="anchor"></span>Figure 124: Clinic Med List - Help Text

![](ampl-user-guide/151.png)

#### Clinic Med Order – Details

To view additional details of a Unit Dose Clinic Med Order, click on it in the Med List or Expanded View list. A new pop-up window will display the Unit Dose Med Order details. See figure below:

<span id="_Toc180613938" class="anchor"></span>Figure 125: Clinic Med Order – Active Order Detail Screen

![](ampl-user-guide/152.png)

An IV Clinic Med will display fields specific to an IV order in the pop-up. See figure below:

<span id="_Toc180613939" class="anchor"></span>Figure 126: Clinic Med Order - IV Med Order Details

![](ampl-user-guide/153.png)

At the bottom of the Clinic Med Order screen, additional details are available including Order Checks, Drug Restrictions/Guidelines, Drug Info, Provider Info, PADE Inventory Activity, and Admin Hx. See figure below:

<span id="_Toc180613940" class="anchor"></span>Figure 127: Clinic Med Order - Additional Details

![](ampl-user-guide/154.png)

Selecting a button will display additional details in a pop-up window. See figures below for examples of each:

<span id="_Toc180613941" class="anchor"></span>Figure 128: Clinic Med Order - Order Check

![](ampl-user-guide/155.png)

<span id="_Toc180613942" class="anchor"></span>Figure 129: Clinic Med Order - Drug Restriction/Guideline Information

![](ampl-user-guide/156.png)

<span id="_Toc180613943" class="anchor"></span>Figure 130: Clinic Med Order - Drug Info

![](ampl-user-guide/157.png)

<span id="_Toc180613944" class="anchor"></span>Figure 131: Clinic Med Order - Provider Information

![](ampl-user-guide/158.png)

If the clinic has a PADE dispensing device the PADE Inventory Activity button will display the PADE activity log of all medications dispensed in the past thirty days. The PADE inventory will display current and historical activity from previous admissions or visits. See figures below:

<span id="_Toc180613945" class="anchor"></span>Figure 132: Clinic Med Order - PADE Activity

![](ampl-user-guide/159.png)

<span id="_Toc180613946" class="anchor"></span>Figure 133: Clinic Med Order - Administration Hx

![](ampl-user-guide/160.png)

### Non-VA Med List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Non-VA Med List displays active Non-VA med orders from the local station.

<span id="_Toc180613947" class="anchor"></span>Figure 134: Non-VA Med List

![](ampl-user-guide/161.png)

To include Remote clinic orders, click on the Remote Orders (R) button in the Non-VA header. If Remote button is disabled, it indicates patient does not have remote orders. See figures below:

<span id="_Toc180613948" class="anchor"></span>Figure 135: Non-VA Med List - Remote Orders Button

![](ampl-user-guide/162.png)

<span id="_Toc180613949" class="anchor"></span>Figure 136: Non-VA Med List - Remote Orders

![](ampl-user-guide/163.png)

#### Non-VA Med Orders - Expanded View

The More button will bring up the Expanded View. See figure below:

<span id="_Toc180613950" class="anchor"></span>Figure 137: Non-VA Med List - More Button

![](ampl-user-guide/164.png)

The Expanded view displays additional details, including Generic Drug Name, Dosage, Route, Schedule, Start Date, Documented Date, and Documented By. See figure below:

<span id="_Toc180613951" class="anchor"></span>Figure 138: Non-VA Med List - Expanded View

![](ampl-user-guide/165.png)

#### Non-VA Med List – Expanded View Help Text

Help text for each column of the Expanded View of Non-VA Med Orders is displayed by hovering over the column header. See figure below:

<span id="_Toc180613952" class="anchor"></span>Figure 139: Non-VA Med List - Help Text

![](ampl-user-guide/166.png)

#### Non-VA Med Orders – Details

To view details of a Non-VA Med Order, click on it in the Non-VA section or the Expanded View. A pop-up will display with details about the order. Details include CPRS Order Number, Orderable Item, Dispense Drug, Dosage, Route, Schedule, Duration, Conjunction, SIG, Comments, Statement/Explanation, Start Date, Documented Date/Time, Documented By, Clinic, Facility and Provider Order Check. If the drug is marked as “Hazardous to Handle” an Icon will appear after the drug name. See figure below:

<span id="_Toc180613953" class="anchor"></span>Figure 140: Non-VA Med Orders - Details for Active Medication

![](ampl-user-guide/167.png)

## Allergies and ADRs Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All allergy records for the selected patient in the Allergies and ADRs tab, including the total number of records in the blue circle in the tab will be displayed.

The column headers include Standard Term (GMR Allergy), Causative Agent/Reactant, Signs/Symptoms, Observed/Historical, Severity, Mechanism, Reaction Type, Origination Date/Time, and Facility. The default view is All Records sorted by Standard Term ascending. See figure below:

<span id="_Toc180613954" class="anchor"></span>Figure 141: Allergies and ADRs Tab

![](ampl-user-guide/168.png)

If the patient has no allergy assessment at the local facility, a pop-up window will display, indicating that an allergy assessment is needed. See figure below:

<span id="_Toc180613955" class="anchor"></span>Figure 142: Allergies and ADRs - Allergy Assessment Needed

![](ampl-user-guide/169.png)

![](ampl-user-guide/170.png)NOTE: If a patient has an allergy assessment at the local facility, but no assessment at a remote facility, the remote information will be included in the table, but no pop-up will display.

When hovering over the column headers, help text is shown. See figure below:

<span id="_Toc180613956" class="anchor"></span>Figure 143: Allergies and ADRs Column Header Help Text

![](ampl-user-guide/171.png)

A plus sign (+) indicator will display with the total number in the tab if a patient has Entered in Error records. See figure below:

<span id="_Toc180613957" class="anchor"></span>Figure 144: Allergies and ADRs - Entered in Error Records Indicator

![](ampl-user-guide/172.png)

To show the Entered in Error records, click on the checkbox and the following information will display. The Enter in Error records are highlighted in red and include an Entered in Error indicator. See figure below:

<span id="_Toc180613958" class="anchor"></span>Figure 145: Allergies and ADRs - Entered in Error Records

![](ampl-user-guide/173.png)

### Allergy and ADRs - Query Editor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A Query Editor is available to filter records in the Allergies and ADRs tab. To add a filter, open the Query Editor by clicking on the Query Editor button. See figure below:

<span id="_Toc180613959" class="anchor"></span>Figure 146: Allergies and ADRs - Query Editor

![](ampl-user-guide/174.png)

Filtering and sorting options are available by using the dropdown menus shown below. Both options include Standard Term, Causative Agent/Reactant, Signs/Symptom, Observed/Historical, Severity, Mechanism, Reaction Type, Origination Date/Time, Facility, and Drug Class.

Once the filter is selected a dropdown list of choices is displayed, including “No Value” to search for records where the field is blank.

<span id="_Toc180613960" class="anchor"></span>Figure 147: Allergies and ADRs - Filter for No Value

![](ampl-user-guide/175.png)

> **NOTE:** The signs/symptoms filter includes signs and symptoms for allergies entered in error.

Once a filter/sort is selected, click Add to have the filter added to the search criteria. Continue this process with other filters, as needed. Once completed, click on Refresh to update the display. To delete a filter, select the red “X” icon to the right of it. To clear filters added by the user and return to the tab’s default, click the Reset button. To close the Query Editor, click on the Hide Query Editor Button. See figures below:

<span id="_Toc180613961" class="anchor"></span>Figure 148: Allergies and ADRs - Filter Options

![](ampl-user-guide/176.png)

<span id="_Toc180613962" class="anchor"></span>Figure 149: Allergies and ADRs - Sorting Options

![](ampl-user-guide/177.png)

### Allergies and ADRs – Accordion View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Allergies and ADRs’ records are available in an accordion view. To access this information, click on the allergy record and additional details will display. See figure below:

<span id="_Toc180613963" class="anchor"></span>Figure 150: Allergies and ADRs - Accordion View

![](ampl-user-guide/178.png)

The accordion view is also available for Records Entered in Error. See figure below:

<span id="_Toc180613964" class="anchor"></span>Figure 151: Allergies and ADRs - Accordion View – Records Entered in Error

![](ampl-user-guide/179.png)

## Vitals Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Vitals Tab displays a table of the most recent values for common vitals. It includes the following column headers: Vital Name, Metric Value, US Std Value, Qualifier, Date/Time Taken, and Facility.

Default common vitals include: Temperature, Height, Weight, BMI, Blood Pressure, Pulse, Central Venous Pressure, Respirations, Pulse Oximetry, and Pain Scale. See figure below:

<span id="_Toc180613965" class="anchor"></span>Figure 152: Vitals Tab

![](ampl-user-guide/180.png)

> ![](ampl-user-guide/181.png) NOTE: The AMPL GUI application converts imperial values provided for a vital type to metric values where appropriate so that both values display.

Help text will display when hovering over the column headers. See figure below:

<span id="_Toc180613966" class="anchor"></span>Figure 153: Vitals - Help Text

![](ampl-user-guide/182.png)

To display additional Vital types to the Latest Vitals table, use the dropdown menu below the table, select the Vital type, and then click the Add button. See Figure below:

<span id="_Toc180613967" class="anchor"></span>Figure 154: Vitals - Additional Vitals

![](ampl-user-guide/183.png)

### Vitals by Date Range

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Vitals tab includes the ability to display readings for a date range. To display multiple values for a Vital, click on that Vital and results will display in an additional table to the right with a default date range of one year for Outpatient and one week for Inpatient. Additional Vitals may be added by clicking on the Vital name. They can be removed by clicking again. See figure below:

<span id="_Toc180613968" class="anchor"></span>Figure 155: Vitals - Display

![](ampl-user-guide/184.png)

To change the date range, modify the Readings from or through dates. See figure below:

<span id="_Toc180613969" class="anchor"></span>Figure 156: Vitals - Date Range

![](ampl-user-guide/185.png)

> ![](ampl-user-guide/186.png) NOTE: To obtain the acceptable Date/Time formats, enter ‘?’ in the date range box.

In addition, commonly used date ranges can be chosen using the arrow beside the date box. See figure below:

<span id="_Toc180613970" class="anchor"></span>Figure 157: Vitals – Commonly Used Date Ranges

![](ampl-user-guide/187.png)

Once a date range is chosen, the results for the selected vitals taken within the date range will display in the table. See figure below:

<span id="_Toc180613971" class="anchor"></span>Figure 158: Vitals - Date Range Display

![](ampl-user-guide/188.png)

### Vitals – Expanded View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To see additional details on a Vital, click on the Vital in the date range table on the right and a pop-up box will display. Details include Date/Time Vitals Taken, Date/Time Vitals Entered, Entered By, Hospital Location, Facility, Rate, Qualifier. See figure below:

<span id="_Toc180613972" class="anchor"></span>Figure 159: Vitals - Expanded View

![](ampl-user-guide/189.png)

### Vitals – Graphing Capabilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Vital types in the date range table may also be shown in a graph by selecting the graphing icon located in the top right corner of the Vitals screen. See figure below:

<span id="_Toc180613973" class="anchor"></span>Figure 160: Vitals - Graphing

![](ampl-user-guide/190.png)

Regression lines and labels may be added by checking the buttons below the graph. To return to the Table format, click on the Table icon in the upper right corner. See figure below:

<span id="_Toc180613974" class="anchor"></span>Figure 161: Vitals - Regression Lines and Labels

![](ampl-user-guide/191.png)

## Labs Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Labs tab displays lab data for the last year and future lab orders, sorted by Collection Date/Time descending, 100 results per page. Laboratory records from all VHA facilities are included. See figure below:

<span id="_Toc180613975" class="anchor"></span>Figure 162: Labs Tab

![](ampl-user-guide/192.png)

The column headers include Collection Date/Time, Test Name, Flag, Specimen, Provider, Ordered Date/Time, Status, Urgency, Accession \#, Available Date/Time, Hospital Location and Facility. See figure below:

<span id="_Toc180613976" class="anchor"></span>Figure 163: Labs - Column Headers

![](ampl-user-guide/193.png)

Help text will display when hovering over the column headers. See figure below:

<span id="_Toc180613977" class="anchor"></span>Figure 164: Labs - Help Text

![](ampl-user-guide/194.png)

### Labs - Laboratory Test Record Expanded View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To view results, if available, for a Lab record click on the individual record. A pop-up window displays test results in four columns: Name, Value, Flag, and Reference Range. Comments, if available, display below the results. If partial results have been reported, only those will display in the pop-up window. See figure below:

<span id="_Toc180613978" class="anchor"></span>Figure 165: Labs - Test Record Expanded View

![](ampl-user-guide/195.png)

When the results are pending, the lab test name and collection date and time will display. To close the pop-up, click on the Close button or click outside the expanded view window. See figure below:

<span id="_Toc180613979" class="anchor"></span>Figure 166: Labs - Lab Results Pending

![](ampl-user-guide/196.png)

When there are no laboratory test records to display for the selected patient, the Labs Label tab will indicate that. See figure below:

<span id="_Toc180613980" class="anchor"></span>Figure 167: Labs - No Lab Data

![](ampl-user-guide/197.png)

### Labs - Query Editor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A Query Editor is available to filter and sort records in the Labs tab. To add a filter or change the sort, open the Query Editor by clicking on the Current Query button. See figure below:

<span id="_Toc180613981" class="anchor"></span>Figure 168: Labs - Show Query Editor Button

![](ampl-user-guide/198.png)

Filtering and sorting options are available by using the dropdown menus shown below. Filter options include Collection Date/Time, Test Name, Flag, Specimen, Provider, Ordered Date/Time, Status, Urgency, Accession#, Available Date/Time, Hospital Location, Facility and Report Text. Sort fields include Collection Date/Time, Test Name, Specimen, provider, Ordered Date/Time, Status, Urgency, Accession#, Available Date/Time, Hospital Location and Facility.

Once a filter/sort is selected, click Add to have the filter added to the search criteria. Continue this process with other filters, as needed. Once completed, click on Refresh to update the display. To delete a filter, select the red “X” icon to the right of it. To clear filters added by the user and return to the tab’s default, click the Reset button. To close the Query Editor, click on the Hide Query Editor Button. See figure below:

<span id="_Toc180613982" class="anchor"></span>Figure 169: Labs - Filter and Sorting Options

![](ampl-user-guide/199.png)

## Progress Notes Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On the Progress Notes tab, all signed notes entered within the last year, sorted by Date/Time Entered descending, 100 results per page will display. See figure below:

<span id="_Toc180613983" class="anchor"></span>Figure 170: Progress Notes Tab

![](ampl-user-guide/200.png)

The column headers include Local Title, Date/Time Entered, Author, Status, Hospital Location, and Facility. See figure below:

<span id="_Toc180613984" class="anchor"></span>Figure 171: Progress Notes - Column Headers

![](ampl-user-guide/201.png)

When hovering over the column headers, help text is shown. See figure below:

<span id="_Toc180613985" class="anchor"></span>Figure 172: Progress Notes - Help Text

![](ampl-user-guide/202.png)

### Progress Notes – Expanded View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To view details for a single Progress Note, click on the individual record. A pop-up window displays. Details include Local Title, Standard Title, Report Text, Date of Note, Entry Date, Author, Expected Signer, Expected Cosigner, Urgency, Status, Facility/Location, Signed By, Signature Date/Time, Signature Block Name and Signature Block Title. If note is amended, details will include Amended By, Amendment Date/Time, Amendment Block Name and Amendment Signed. To close the pop-up, click on the Close button or click outside the expanded view window. See figure below:

<span id="_Toc180613986" class="anchor"></span>Figure 173: Progress Notes - Expanded View

![](ampl-user-guide/203.png)

> ![](ampl-user-guide/204.png) NOTE: Interdisciplinary Notes, Group Notes and Addendum can be directly viewed from the parent Progress Note, where applicable. See figure below:

<span id="_Toc180613987" class="anchor"></span>Figure 174: Progress Notes - Interdisciplinary Note

> ![](ampl-user-guide/205.png)

### Progress Notes – Query Editor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A Query Editor is available to filter and sort records in the Progress Notes tab. To add a filter or change the sort order, open the Query Editor by clicking on the Current Query button. See figure below:

<span id="_Toc180613988" class="anchor"></span>Figure 175: Progress Notes - Query Editor Button

![](ampl-user-guide/206.png)

Filtering and sorting options are available by using the dropdown menus shown below. Filter options include Local Title, Date/Time Entered, Author, Status, Hospital Location, Facility, Standard Title, Report Text, Expected Signer, Expected Cosigner and Urgency. Sort options include Local Title, Date/Time Entered, Author, Status, Hospital Location, Facility, Standard Title, Expected Signer, and Expected Cosigner.

Once a filter/sort is selected, click Add to have the filter added to the search criteria. Continue this process with other filters, as needed. Once completed, click on Refresh to update the display. To delete a filter, select the red “X” icon to the right of it. To clear filters added by the user and return to the tab’s default, click the Reset button. To close the Query Editor, click on the Hide Query Editor Button. See figure below:

<span id="_Toc180613989" class="anchor"></span>Figure 176: Progress Notes - Filter and Sorting Options

![](ampl-user-guide/207.png)

## Consults Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the Consults tab, consult records from all Veterans Health Administration (VHA) facilities will display for the selected patient. The default view includes all records sorted by Date/Time in descending order, with 100 records per page. See figure below:

<span id="_Toc180613990" class="anchor"></span>Figure 177: Consults Tab

![](ampl-user-guide/208.png)

The column headers include Date/Time, Procedure/Consult, Service, Status, and Facility. See figure below:

<span id="_Toc180613991" class="anchor"></span>Figure 178: Consults - Column Headers

![](ampl-user-guide/209.png)

Help text will display when hovering over the column headers. See figure below:

<span id="_Toc180613992" class="anchor"></span>Figure 179: Consults - Help Text

![](ampl-user-guide/210.png)

### Consults Tab – Expanded View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To view details for a single Consult record, click on the individual record. A pop-up window displays with data divided into three sections.

In the first section of the window, the information includes To Service, From Service, Requesting Provider, Service Rendered as, Place of Consultation, Patient Location, Urgency, Date/Time Requested, Status, Orderable Item, Clinically Indicated Date, Last Action, Significant Findings, Ordering Facility, and Reason for Request.

The second section includes: Consult or Procedure, Provisional Diagnosis, Attention, Provisional Diagnosis Date, Provisional Diagnosis System, and Report Text.

The last section includes Activity, Date/Time, Responsible Person, Entered By.

To close the pop-up, click on the Close button or click outside the expanded view window. See figure below:

<span id="_Toc180613993" class="anchor"></span>Figure 180: Consults - Expanded View

![](ampl-user-guide/211.png)

### Consults Tab – Query Editor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Filtering and sorting options are available by using the dropdown menus shown below. Both options include Date/Time, Procedure/Consult, Service, Status, Facility, (From) Service, Requesting Provider, Service Rendered as, Urgency, Patient Location, Reason for Request, Last Action, Provisional Diagnosis and Orderable Item.

Once a filter/sort is selected, click Add to have the filter added to the search criteria. Continue this process with other filters, as needed. Once completed, click on Refresh to update the display. To delete a filter, select the red “X” icon to the right of it. To clear filters added by the user and return to the tab’s default, click the Reset button. To close the Query Editor, click on the Hide Query Editor Button. See figure below:

<span id="_Toc180613994" class="anchor"></span>Figure 181: Consults - Filter and Sort

![](ampl-user-guide/212.png)

## Problem List Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the Problem List tab, all ‘Active’ problems display. The default view includes all ‘Active’ records sorted by Immediacy ascending, then Description ascending. See figure below:

<span id="_Toc180613995" class="anchor"></span>Figure 182: Problem List Tab

![](ampl-user-guide/213.png)

The column headers include Status, Verified, Immediacy, Description/Comments, Onset Date, Last Updated Date, and Facility. See figure below:

<span id="_Toc180613996" class="anchor"></span>Figure 183: Problem List - Column Headers

![](ampl-user-guide/214.png)

Help text will display when hovering over the column headers. See figure below:

<span id="_Toc180613997" class="anchor"></span>Figure 184: Problem List - Help Text

![](ampl-user-guide/215.png)

### Problem List – Expanded View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To view additional details on a Problem List record, click on the record.

The information includes Problem Category(ies), Diagnosis, Coding System, Code Number, Onset Date, Status/Verified/Immediacy, Service-Connected Condition, Exposure, Provider, Service, Clinic, Facility, Date Entered, Entered By, Last Updated, Comments, and Audit History.

To close the pop-up, click on the Close button or click outside the expanded view window. See figure below:

<span id="_Toc180613998" class="anchor"></span>Figure 185: Problem List - Expanded View

![](ampl-user-guide/216.png)

### Problem List – Query Editor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Filtering and sorting options are available by using the dropdown menus shown below. Filtering options include Status, Verified, Immediacy, Onset Date, Last Updated Date, Facility, Description, and Comments.

Sorting options include Status, Verified, Immediacy, Onset Date, Last Updated Date, Facility and Description.

Once a filter/sort is selected, click Add to have the filter added to the search criteria. Continue this process with other filters, as needed. Once completed, click on Refresh to update the display. To delete a filter, select the red “X” icon to the right of it. To clear filters added by the user and return to the tab’s default, click the Reset button. To close the Query Editor, click on the Hide Query Editor Button. See figure below:

<span id="_Toc180613999" class="anchor"></span>Figure 186: Problem List - Filter and Sort Options

![](ampl-user-guide/217.png)

## Immunization Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On the Immunizations tab, all Immunizations are displayed, listed by Name (of Immunization) ascending.

<span id="_Toc180614000" class="anchor"></span>Figure 187: Immunization Tab

![](ampl-user-guide/218.png)

The column headers include Name (of immunization), Administration Date/Time, Reaction and Facility.

<span id="_Toc180614001" class="anchor"></span>Figure 188: Immunization - Column Headers

![](ampl-user-guide/219.png)

Help text will display when hovering over the column headers. See figure below:

<span id="_Toc180614002" class="anchor"></span>Figure 189: Immunization - Help Text

![](ampl-user-guide/220.png)

### Immunization Tab – Expanded View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To view additional details on an immunization, click on the record and a pop-up window will display. The information includes Full Name, Vaccine Information Statement(s) Offered, VIS (Vaccine Information Statement) Name, Edition Date, Language, Date Administered, Dose/Dose Units, Series, Max \# In Series, Admin Route/Site, Reaction, Contraindicated, Manufacturer, Lot Number, Expiration Date, NDC, Location/Facility, Administered By, Ordered By, and Comments. To close the pop-up, click on the Close button or click outside the expanded view window. See figure below:

<span id="_Toc180614003" class="anchor"></span>Figure 190: Immunization - Expanded View

![](ampl-user-guide/221.png)

### Immunization Tab – Query Editor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Filtering and sorting options are available by using the dropdown menus shown below. Filtering options include Name (of immunization), Administration Date/Time, Reaction, Facility, Full Name (of immunization), Series, Contraindicated, Lot \#, NDC, Location, and Comments.

Sorting options include Name (of immunization), Administration Date/Time, Reaction, Facility, and Series.

Once a filter/sort is selected, click Add to have the filter added to the search criteria. Continue this process with other filters, as needed. Once completed, click on Refresh to update the display. To delete a filter, select the red “X” icon to the right of it. To clear filters added by the user and return to the tab’s default, click the Reset button. To close the Query Editor, click on the Hide Query Editor Button. See figure below:

<span id="_Toc180614004" class="anchor"></span>Figure 191: Immunization - Filters and Sort Options

![](ampl-user-guide/222.png)

## Appointments Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Appointments tab displays data for the last year, sorted by Date/Time descending order, 100 results per page will display. See figure below:

<span id="_Toc180614005" class="anchor"></span>Figure 192: Appointments Tab

![](ampl-user-guide/223.png)

The column headers include Date/Time, Clinic, Specialty, Provider, Status, and Facility. See figure below:

<span id="_Toc180614006" class="anchor"></span>Figure 193: Appointments - Column Headers

![](ampl-user-guide/224.png)

Help text will display when hovering over the column headers. See figure below:

<span id="_Toc180614007" class="anchor"></span>Figure 194: Appointments - Help Text

![](ampl-user-guide/225.png)

Two print buttons are in the top right corner of the Appointments tab, Print Current List or Print Upcoming Appointments. See figure below:

<span id="_Toc180614008" class="anchor"></span>Figure 195: Appointments - Print Buttons

![](ampl-user-guide/226.png)

### Appointments Tab – Expanded View

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Click on an individual appointment to see Progress Note(s) associated with the record. For past appointments, a pop-up window displays any Progress Note(s) associated with the visit. Future appointments and those without an associated Progress Note will display “No Progress Notes for this appointment”. If multiple notes are associated with the visit, including group notes, amendments, and addendums, all will be displayed. Information includes Standard Title, Report Text, Date of Note, Entry Date, Author, Exp Signer, Exp Cosigner, Urgency, Status, Facility/Location, Signed By, Signature Date/Time, Signature Block Name, and Signature Block Title. See figure below:

<span id="_Toc180614009" class="anchor"></span>Figure 196: Appointments - Expanded View

![](ampl-user-guide/227.png)

### Appointments Tab – Query Editor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Filtering and sorting options are available by using the dropdown menus shown below. Filtering options include Date/Time, Clinic, Specialty, Provider, Status and Facility.

Sorting options include Date/Time, Clinic, Specialty, Provider, Status and Facility.

Once a filter/sort is selected, click Add to have it added to the search criteria. Continue this process with other filters, as needed. Once completed, click on Refresh to update the display. To delete a filter, select the red “X” icon to the right of it. To clear filters added by the user and return to the tab’s default, click the Reset button. To close the Query Editor, click on the Hide Query Editor Button. See figure below:

<span id="_Toc180614010" class="anchor"></span>Figure 197: Appointments - Filter and Sort Options

![](ampl-user-guide/228.png)

# Version and Build Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From AMPL GUI application, version and build information is available by clicking in the user-station number box in the upper right corner of the header. See figure below:

<span id="_Toc180614011" class="anchor"></span>Figure 198: Version and Build Information

![](ampl-user-guide/229.png)

## Date Formats for Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When searching, enter dates in the customary format of *mm/dd/yyyy* format.

## Time Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The remote orders times will remain in the time zone where they were given or recorded.

# Joint Legacy Viewer (JLV) Button

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Joint Legacy Viewer (JLV) is accessible by clicking the JLV button in the upper right corner of the screen. It includes data from external partners (e.g. (Department of Defense (DOD)). See figure below:

<span id="_Toc180614012" class="anchor"></span>Figure 199: Joint Legacy Viewer (JLV) Button

![](ampl-user-guide/230.png)

# Patient Record Flag

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patient Record Flags alert VHA employees of patients whose behavior or characteristics may pose a threat to the safety of the employee, other patients, or compromise the delivery of quality health care. Patient Record Flags are divided into types: Category I (national) and Category II (local). Each type is described in sections below.

The Patient Record Flag indicator is included in the Patient Header on the coversheet. The button will display “FLAG” in red when Patient Records Flags are available. If no Patient Record Flags are available, the button will be disabled. See figure below:

<span id="_Toc180614013" class="anchor"></span>Figure 200: Patient Record Flag Indicator

![](ampl-user-guide/231.png)

## Patient Record Flag Window Display

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patient Record Flags are accessible by clicking on the Patient Record Flag button. The Patient Record Flag information includes Category I Flags, Category II Flags, Flag Name, Assignment Narrative, Flag Type, Approved By, Flag Category, Next Review Date, Assignment Status, Owner Site, Initial Assigned Date, Originating Site, and Signed, Linked Notes of Title. See figure below:

<span id="_Toc180614014" class="anchor"></span>Figure 201: Patient Record Flags

![](ampl-user-guide/232.png)

If multiple Patient Record Flags exist for a patient, details of each flag are accessible by clicking on it. See figure below:

<span id="_Toc180614015" class="anchor"></span>Figure 202: Patient Record Flag Window

![](ampl-user-guide/233.png)

## Patient Record Flag – Category I Flags (National)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Category I Patient Record Flags are established and approved at a national level and are transmitted to all facilities, ensuring that these flags are universally available.

Each flag includes a narrative that describes the reason for the flag and may include some suggested actions for users to take when they encounter the patient.

Category I Patient Record Flags will display in a pop-up when the patient’s record is opened. They may also be accessed by clicking on the Flag button in patient demographics.

The Progress Note for the Category I Patient Record Flag is also available. To access the note, click on the note link under the Signed, Linked Notes of Title section. See figure below:

<span id="_Toc180614016" class="anchor"></span>Figure 203: Patient Record Flag Category I Flag Signed, Linked Notes

![](ampl-user-guide/234.png)

Upon clicking the link for the Linked Note, a new window displays the Progress Note for the Patient Record Flag Category including the Date of Note, Entry Date, Author, Expiration Signer, Expiration Cosigner, Urgency, Status, Facility/Location, Signed By, Signature Date/Time, Signature Block Name, and Signature Block Title. See figure below:

<span id="_Toc180614017" class="anchor"></span>Figure 204: Patient Record Category Flag I Progress Note Window

![](ampl-user-guide/235.png)

## Patient Record Flag – Category II Flags (Clinical)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Category II Patient Record Flags are established and approved at a local level by individual VISNs or facilities. They are not shared between sites. When a flag is selected, details for the flag will be displayed, including Flag Name, Assignment Narrative, Flag Type, Flag Category, Assignment Status, Initial Assignment Date, Approved By, Next Review Date, Owner Site, Originating Site, and a link to the related Progress Note. The Progress Note for the Category II Patient Record Flag is also available. To access the note, click on the note link under the Signed, Linked Notes of Title section. See figure below:

<span id="_Toc180614018" class="anchor"></span>Figure 205: Category II Flags

![](ampl-user-guide/236.png)

<span id="_Toc180614019" class="anchor"></span>Figure 206: Patient Record Flag Category II Flag Signed, Linked Notes

![](ampl-user-guide/237.png)

Upon clicking on the link for the Progress Note, a new window displays the Progress Note for the Patient Record Flag Category II including the Date of Note, Entry Date, Author, Expiration Signer, Expiration Cosigner, Urgency, Status, Facility/Location, Signed By, Signature Date/Time, Signature Block Name, and Signature Block Title.

To Close the Progress Note, use the button at the bottom of the window.

<span id="_Toc180614020" class="anchor"></span>Figure 207: Patient Record Category Flag II Progress Note Window

![](ampl-user-guide/238.png)

# Clinical Context Object Workgroup (CCOW)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Clinical Context Object Workgroup (CCOW) is a Health Level Seven (HL7) International standard protocol designed to enable disparate applications to synchronize patient context in real time and at interface level.

AMPL GUI participates in patient context sharing both with the VA’s existing enterprise desktop CCOW software and with individual VistA systems.

When switching patients in AMPL GUI, participating applications such as CPRS will be notified of the change and switch to the new patient. Similarly, switching patients in a participating application will cause AMPL GUI to change to the new patient.

AMPL GUI allows sharing patient context with individual VistA systems, integrating with VistA’s ‘Last Selected Patient’ functionality.

## Desktop Patient Context – Context Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A visual indicator of current context-sharing status is displayed in the AMPL GUI header using the same iconography as CPRS.

<span id="_Toc180614021" class="anchor"></span>Figure 208: Context Status

![](ampl-user-guide/239.png)

## Desktop Patient Context – Suspend (Break) Context Links

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Clicking on the status button will turn off context sharing, prompting for confirmation beforehand. See figure below:

<span id="_Toc180614022" class="anchor"></span>Figure 209: Context Sharing Confirmation Window

![](ampl-user-guide/240.png)

Once context is broken, switching patients in AMPL will no longer change the current patient in other participating GUI applications and vice versa.

## Desktop Patient Context – Re-establish (Rejoin) Context Link

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Re-establish patient context by clicking the CCOW button in the AMPL GUI header. See figure below:

<span id="_Toc180614023" class="anchor"></span>Figure 210: CCOW Button

![](ampl-user-guide/241.png)

A prompt to confirm prior to re-establishing context will display. See figure below:

<span id="_Toc180614024" class="anchor"></span>Figure 211: Re-establishing Context Confirmation

![](ampl-user-guide/242.png)

## Desktop Patient Context – Notification of Failed Context Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If changing context or checking for context changes in AMPL GUI fails, context will be broken, and an error message will display. See figure below:

<span id="_Toc180614025" class="anchor"></span>Figure 212: Notification of Failed Context Changes Window

![](ampl-user-guide/243.png)

# VistA ‘Spacebar Return’ Functionality in AMPL GUI Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

AMPL GUI provides a mechanism to mimic VistA’s “Last Selected Patient” functionality.

## VistA Logo Button

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To switch to the patient that is currently selected in VistA, click on the VistA logo button located in the AMPL GUI header. See figure below:

<span id="_Toc180614026" class="anchor"></span>Figure 213: VistA Logo Button

![](ampl-user-guide/244.png)

After clicking on the VistA logo button, the option to choose whether a patient change should be made in AMPL is displayed in a pop-up. See figure below:

<span id="_Toc180614027" class="anchor"></span>Figure 214: Notification of Patient Change in AMPL

![](ampl-user-guide/245.png)

## VistA Patient Context – Change Cannot be Done in AMPL

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When using the VistA logo button, when a VistA context cannot be made in AMPL an error message will display. See figure below:

<span id="_Toc180614028" class="anchor"></span>Figure 215: Patient Context Change Cannot be Made in AMPL Notification Window

![](ampl-user-guide/246.png)

## Vista ‘Spacebar Return’ Function

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In VistA, using the existing ‘Spacebar Return’ function at a ‘Select Patient’ prompt will select the currently selected AMPL GUI patient. The user must be in the AMPL Patient Cover Sheet.

<span id="_Toc180614029" class="anchor"></span>Figure 216: VistA Spacebar Return Function

![](ampl-user-guide/247.png)

# Changing User ID and Password

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A PIV card is used to validate users for access.

# Exit System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To exit the system, navigate to the dropdown next to your username in the upper right-hand corner of the AMPL GUI header. click on the Logout button found under the Change Station button. See figure below:

<span id="_Toc180614030" class="anchor"></span>Figure 217: Logout Button

![](ampl-user-guide/248.png)

# Caveats and Exceptions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Caveats and Exceptions are not applicable to AMPL GUI.

# Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section includes general information regarding errors, probable causes, and resolutions.

| Symptom                                                                                                            | Cause                                                                                 | Resolution                                                                                                                                                                                                                             |
|------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| When logging into AMPL, you see a blank page.                                                                          | AMPL is designed for Chrome-based browsers.                                               | Use a Chrome-based browser.                                                                                                                                                                                                                |
| When logging into AMPL, you receive a message saying, "You do not have sufficient permissions to use the application." | Your user account has not been added to the required Active Directory Group.              | Contact support to have your windows account added to the proper security group.                                                                                                                                                           |
| While using the application, the display is poorly formatted, or user interface elements do not perform as intended.   | AMPL is designed for Chrome-based browsers with a minimum window size of 1024x768 pixels. | Use a Chrome-based browser and try increasing the size of the browser window.                                                                                                                                                              |
| While using the application you are taken back to the login page.                                                      | Your IAM user session has expired.                                                        | Log back into the application.                                                                                                                                                                                                             |
| While using the application you receive a message saying an error occurred while retrieving data.                      | A system-level error has occurred.                                                        | Contact support to report the issue.                                                                                                                                                                                                       |
| When a patient record loads user receives a Pre-Check error                                                            | Error occurred while performing the patient pre-check.                                    | Patient record will be loaded without additional user interaction                                                                                                                                                                          |
| When a patient record loads in AMPL, on rare occasions some data may be missing.                                       | Technical Issues in AMPL.                                                                 | A warning indicator icon displays on a domain TAB on the Cover Sheet if any such data is missing for the domain. The icon will remain as long as the patient’s record is open.                                                             |
| A patient record loads in AMPL missing recent updates to patient demographic data.                                     | Updates to patient demographic data in VistA do not trigger propagation to VDIF.          | When other data updates for that patient such as medication order changes are made, VistA will trigger the updates including the patient demographics changes to be propagated to VDIF. This will make the data changes available in AMPL. |

Troubleshooting IssuesThis table includes the cause of the issue, the symptom, and the resolution.

# Acronyms and Abbreviations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table lists acronyms found in this document and provides definitions.

| Acronym | Definition                                                  |
|-------------|-----------------------------------------------------------------|
| ACOE        | Agile Center of Excellence                                      |
| AD          | Active Directory                                                |
| ADRs        | Adverse Reactions                                               |
| AITC        | Austin Information Technology Center                            |
| AMPL GUI    | Advanced Medication Platform Graphic User Interface             |
| BMI         | Body Mass Index                                                 |
| BSA         | Body Surface Area                                               |
| CCOW        | Clinical Context Object Workgroup                               |
| CD          | Critical Decision (Used in the VIP Process)                     |
| CMOP        | Consolidated Mail Outpatient Pharmacies                         |
| CPRS        | Computerized Patient Record System                              |
| CrCL        | Creatine Clearance                                              |
| CREAT       | Creatine                                                        |
| CVP         | Central Venous Pressure                                         |
| CWAD        | Crisis Notes, Warning Notes, Allergies/ADRs, and Directives     |
| DNR         | Do Not Resuscitate                                              |
| DOD         | Department of Defense                                           |
| EKG         | Electrocardiogram                                               |
| eMI         | Enterprise Messaging Infrastructure                             |
| ePAS        | Electronic Permissions Access                                   |
| EUO         | End-User Operations                                             |
| FHIR        | Fast Healthcare Interoperability Resources                      |
| GMR         | General Medical Record                                          |
| HL7         | Health Level Seven                                              |
| ID          | Identification                                                  |
| IEN         | Internal Entry Number                                           |
| ITOPS       | IT Operations and Services                                      |
| JVL         | Joint Longitudinal Viewer                                       |
| mg/dL       | Milligrams per deciliter                                        |
| MHA         | Mental Health Assistant                                         |
| MPI         | Master Patient Index                                            |
| NAA         | No Allergy Assessment                                           |
| NARS        | Network Access Request                                          |
| NKA         | No Known Allergies                                              |
| OIT         | Office of Information and Technology                            |
| PADE        | Pharmacy Automated Dispensing Equipment                         |
| PBM         | Pharmacy Benefits Management                                    |
| PIV         | Personal Identity Verification                                  |
| POW         | Prisoner of War                                                 |
| Q12H        | Taking medication every 12 Hours                                |
| Q8H         | Taking medication every 8 Hours                                 |
| SSN         | Social Security Number                                          |
| SSOI        | Single Sign-On Internal                                         |
| TIU         | Text Integration Utility                                        |
| URL         | Uniform Resource Locator                                        |
| VAEC        | Veterans Affairs Enterprise Cloud                               |
| VAMC        | Veterans Affairs Medical Center                                 |
| VBA         | Veterans Benefits Administration                                |
| VHA         | Veterans Health Administration                                  |
| VIP         | Veterans-focused Integration Process                            |
| VIS         | Vaccine Information Statement                                   |
| VistA       | Veterans Health Information Systems and Technology Architecture |
| VPR         | Virtual Patient Record                                          |

# Appendix A: Post-implementation Access or Removal Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Access to AMPL GUI is granted by membership in an Active Directory (AD) group. After initial implementation, a site may request access or removal of an individual by following the process used by their site. There are several processes for requesting and removing membership to the AD group, including ePAS, Network Access Requests (NARS) or helpdesk requests. Each region may use a different process. Please check with local IT end-user operations (EUO), or IT Operations and Services (ITOPS) to find the current process for your site.

# Appendix B: AMPL Desktop Shortcut

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The AMPL application can be easily accessed by creating a Desktop Shortcut. Follow the step-by-step instructions below to create a shortcut for your desktop.

1.  Right-click on a blank area of your desktop and select “New” and then “Shortcut”.
2.  For the location, type the path to the browser you wish to use followed by the AMPL URL (<https://ampl.vaec.va.gov>). The following figure depicts Google Chrome as an example.

<span id="_Toc180614031" class="anchor"></span>Figure 218: Desktop Shortcut

![](ampl-user-guide/249.png)

3.  Type the name for the shortcut: “AMPL”.
4.  Select “Next”.
5.  Select “Finish”. The shortcut is now created and will be found on your Desktop.