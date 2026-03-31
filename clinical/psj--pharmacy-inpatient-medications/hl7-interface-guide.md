---
title: VistA to MOCHA Version 2 Interface Document
doc_type: INT
doc_label: Interface Specification
doc_layer: anchor
doc_subject: Interface Document
app_code: PSJ
app_name: "Pharmacy: Inpatient Medications"
section: CLI
app_status: active
pkg_ns: PSJ
patch_ver: 2
patch_id: PSJ*2
group_key: "PSJ:PSJ:2"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - colspan
  - base
  - drug
  - dose
  - profile
  - order
  - phenytoin
  - prospective
  - drugdrug
  - message
page_count: 0
word_count: 8092
section_count: 4
table_count: 4
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: June 2018
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Inpatient_Med/pss_1_vista_to_mocha_id.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Inpatient_Med/pss_1_vista_to_mocha_id.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=88"
---

![](vista-to-mocha-version-2-interface-document/001.png)

VistA to MOCHA  
Interface Document

June 2018

Product Development

######### Revision History

Each time this manual is updated, the Title Page lists the new revised date and this page describes the changes. If the Revised Pages column lists “All,” replace the existing manual with the reissued manual. If the Revised Pages column lists individual entries (e.g., 25, 32), either update the existing manual with the Change Pages Document or print the entire new manual.

<table>
<caption><p>Table 1: Monograph Table</p></caption>
<colgroup>
<col style="width: 11%" />
<col style="width: 13%" />
<col style="width: 17%" />
<col style="width: 57%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Revised Pages</th>
<th>Patch Numbers</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>06/2018</td>
<td><a href="#Page_14">14-18</a>, <a href="#Page_23">23-24</a></td>
<td><p>OR*3*481</p>
<p>PSO*7*518</p>
<p>PSJ*5*358</p>
<p>PSS*1*224</p></td>
<td><p>Updated “recommended frequency” examples</p>
<p>Added missing closed quotes around “Check” in examples</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>02/2018</td>
<td><p>2, 3-24,</p>
<p>24</p></td>
<td><p>OR*3*382</p>
<p>OR*3*469</p>
<p>PSJ*5*256</p>
<p>PSJ*5*347</p>
<p>PSO*7*402</p>
<p>PSO*7*500</p>
<p>PSS*1*178</p>
<p>PSS*1*206</p></td>
<td><p>Updated Section 3, Dosing</p>
<p>Updated Section 4, Drug-Drug Interaction/Duplicate Therapy for PDRG input value</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>03/2014</td>
<td>All Pages</td>
<td>PSS*1*136, PSS*1*160, PSS*1*173</td>
<td><p>New document.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
</tbody>
</table>

Table 1: Monograph Table

*(This page included for two-sided copying.)*Preface

This document describes the specifics of how the interface works and what is required to use the interface. It is intended for technical personnel.

*(This page included for two-sided copying.)*Table of Contents

*  
(This page included for two-sided copying.)*

# Overview


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Overview](#overview)
- [Ping](#ping)
- [Dosing](#dosing)
  - [How the Dose Call Works](#how-the-dose-call-works)
- [Drug-Drug Interaction/Duplicate Therapy](#drug-drug-interactionduplicate-therapy)
  - [Drug-Drug Interaction Output](#drug-drug-interaction-output)
  - [Duplicate Therapy Output](#duplicate-therapy-output)
- [Drug-Drug Interaction/Duplicate Therapy Exception Handling](#drug-drug-interactionduplicate-therapy-exception-handling)
This document provides technical details for the order check interfaces from Veterans Health Information Systems and Technology Architecture (VistA) to Medication Order Check Healthcare Application (MOCHA).
MOCHA provides three order checks for Outpatient Pharmacy, Inpatient Medications, and Computerized Patient Record System (CPRS). These three checks are Drug-Drug Interactions, Duplicate Therapy Order Checks, and Dosing Order Checks. VistA submits a list of profile and prospective drugs for a patient and receives alerts from the MedKnowledge Framework. Profile drugs are drugs already on the patient profile(s) and prospective drugs are the drugs the patient is being prescribed or to be administered. There is also a Ping check available that simply tests the interface for connectivity.
The Drug-Drug Interactions review a set of drugs to see whether any of the drugs cause unwanted or unexpected chemical or biological reactions when administered together that will affect the efficacy of one of the drugs or the health of the patient. Drug interaction information is based on published professional literature. Each check begins with a First Databank (FDB) drug concept, in this case Routed Drug (Drug Name + Route; i.e., Coumadin Oral), and, using the ingredients in that drug, returns other reacting drugs that the patient is on.
The Duplicate Therapy Order Checks review a set of drugs to see whether any of the drugs unnecessarily overlap in their use or effect with other drugs in the set. The FDB MedKnowledge Framework assigns each drug to one or more therapeutic groups that indicate the drug’s use and purpose. If any of the drugs in the set are found to overlap therapeutic groups, a duplicate therapy warning is raised. The duplication allowance for a therapeutic group acts as an additional filter in determining if the warning will be raised. If the duplication of the therapeutic group exceeds the duplication allowance of a therapeutic group, a warning will be raised.
The Dosing Order Checks review a drug’s dosing regimen against the patient's age, weight, and body surface area to determine if the dosing regimen is appropriate for the patient. Age is always required, but weight and body surface area are only sometimes required depending on the drug being prescribed or administered. For the purpose of the interface, it is recommended to always send in this data whenever possible because which drugs require weight and body surface area is not known when the call to the interface is being made.
The calling applications provide input ^TMP globals with all the necessary information. There are various entry points for the calling applications and the particular checks being requested. Once all the ^TMP globals are properly set, the interface is called via the IN^PSSHRQ2(BASE) M line tag. The BASE parameter is the second subscript of the ^TMP global. Upon return, the interface will populate an output ^TMP global containing the results of the order checks or Ping using the same BASE subscript.
Prior to calling the interface, the VistA Pharmacy System performs numerous data validation checks. If the data is invalid for a particular prospective or profile drug, it may be removed from the input list and an exception global is created describing the issue.
When calling the interface for order checks, the Ping must always be done in a separate call, the Dosing Order Checks must always be done in a separate call, and the Drug-Drug Interaction and Duplicate Therapy Order Checks must be done together in a separate call.
| Note:                                                                                                      | In all of the examples below, the subscript \$J is equal to the unique session Job number of the signed-in user. The second subscript of each Input and Output global example is the literal value that the calling application passes into the interface. |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vista-to-mocha-version-2-interface-document/002.png) |                                                                                                                                                                                                                                                            |

# Ping

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Ping simply tests the connectivity of the interface (optional). The Ping is normally performed by the calling application just prior to making one of the order check calls. If a Ping call is made and the results are unsuccessful, normally the subsequent order check call will not be performed and a message displayed to the user informing the user that order checks cannot occur at this time.

The only input global required for the Ping is as follows:

^TMP(\$J,BASE,”IN”,”PING”) = ””

One of two output globals can be returned. If the Ping is successful, the following global is returned. The critical global node below is the ‘0’ node, which is the first node. In this case, it is equal to 0 indicating the Ping was successful. The nodes below the 0 node contain various data elements about the FDB MedKnowledge Framework database being accessed.

^TMP(\$J,BASE,”OUT”,0) = 0

^TMP(\$J, BASE,"OUT","customBuildVersion")=1

^TMP(\$J, BASE,"OUT","customDbVersion")=3.3

^TMP(\$J, BASE,"OUT","customIssueDate")=20171002

^TMP(\$J, BASE,"OUT","difBuildVersion")=4

^TMP(\$J, BASE,"OUT","difDbVersion")=3.3

^TMP(\$J, BASE,"OUT","difIssueDate")=20180112

If the Ping is unsuccessful, the following global is returned. The important piece of data is piece 1 (using the ‘^’ as the delimiter) of the 0 node. The ‘-1’ indicates an unsuccessful Ping attempt. The text in the second piece can vary, depending upon the problem.

^TMP(\$J,BASE,"OUT",0)="-1^Vendor Database cannot be reached."

# Dosing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Mocha returns various messages to the calling applications, including a Maximum Single Dose Order Check warning, a Maximum Daily Dose Order Check warning, a Recommended Frequency message, General Dosing Guidelines, and various Error/Exception messages.

## How the Dose Call Works

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Data is first passed by parameters into the DOSE^PSSDSAPD M line tag. It is called by Outpatient Pharmacy, Inpatient Medications, and CPRS. If the CPRS order is an IV Order, it is routed through the Inpatient Medications Package first so necessary adjustments can be made to the data. Then DOSE^PSSDSAPD is called by Inpatient Medications for that IV Order from CPRS. DOSE^PSSDSAPD evaluates the data passed in and then builds the ^TMP global that is then passed into the IN^PSSHRQ2 line tag. Then, upon return to DOSE^PSSDSAPD, the PSSDSAPD routine will create a new, easy to display ^TMP global that includes only the information that the calling application needs to display to the user.

| Note:                                                                                                      | The manipulation of the data done by the DOSE^PSSDSAPD code prior to the IN^PSSHRQ2 call can cause some confusion. For example, for complex orders, new input nodes can be created that “total” the previous Dosages of the order in order to perform a Daily Dose check. Also, invalid data can be created and sent to the interface for the sole purpose of receiving general dosing guidelines for the drug(s) being prescribed or administered. The PSS routines maintain records of all globals sent into the interface, then use that information upon return from the interface to create the displayable ^TMP globals for the calling application. |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vista-to-mocha-version-2-interface-document/003.png) |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

From any Dialogue other than the IV Dialogue in CPRS if there already is a DRUG file (#50) entry as part of the order, the call to \$\$EXMT^PSSDSAPI can be made first to see if the DOSE^PSSDSAPD call needs to be made. The \$\$EXMT^PSSDSAPI call returns a value indicating whether or not the drug is exempt from Dose checks.

Details of the \$\$EXMT^PSSDSAPI(X) call:

> <u>\$\$EXMT^PSSDSAPI(X)</u> (Returns Dose Exemption Status of Drug)

> Input X = Dispense Drug Internal Entry Number (IEN) DRUG file (#50)

> Output 1 = Exempt from Dosage Checks

> 0 = Not exempt from Dosage Checks

> Reasons for exemptions:

> If drug is a Supply item

> If the Dosage Form is exempt and the VA PRODUCT file (#50.68) entry does not override the Dosage Form exemption (e.g., Creams, Topicals)

> If the Dosage Form is not exempt but the VA PRODUCT file (#50.68) entry overrides the non-exempt Dosage Form (e.g., PLACEBO TAB)

Details of the DOSE^PSSDSAPD call:

> <u>DOSE^PSSDSAPD(X1,X2,X3,X4) (Dose call API)</u>

> Parameters:

> X1 = Literal values for up to 3 return ^TMP Globals:

> Example:

> X1(1)=”PSOBASE1” (Required)

> This is the raw data output used to create displayable output for the calling applications.

> X1(2)=”PSOBASE2” (Optional)

> This is primarily used by CPRS

> X1(3)=”PSOBASE3” (Optional)

> This is primarily used by Pharmacy

> X2 = Patient Internal Entry Number (Required)

> X3 = Array \#1 (Array for order data to be processed by API – see details below)

> X4 = Array \#2 (Array for order data taken “as is” – see details below)

> Notes concerning the X3 and X4 input arrays:

- The \# is a counter (1,2,3, etc.) For a simple order (one dosing sequence), using 1 is recommended. For a complex order, increment the counter for each Dosing sequence, then all Dosing sequences should be passed in together.
- For some of the X3 and X4 values, there is no \# (counter) since there could only be one value for the entire order, even for a complex order.

The X3 Array Input details:

The X3 array will be used to derive some of the input data that will be set into the ^TMP global when the corresponding data field within the X4 array is not defined (see X4 explanation below). Note that not all data elements have corresponding values in the X3 and X4 arrays.

> X3(#,”DRG_AMT”) and X3(#,”DRG_UNIT”) – (Optional) array nodes that contain the Numeric Dose Amount and Dose Unit text for Possible Dosages. The software will only use these array values if both are defined. The DRG_UNIT value represents the VistA Unit, which will be translated into the FDB Unit prior to call the interface.

> Example:

> X3(#,”DRG_AMT”) = 325

> X3(#,”DRG_UNIT”) = ”MILLIGRAMS”

> X3(#,”DOSE”) = Dosage Ordered (Optional). This value represents a selected Local Possible Dosage. The data element is only passed in from CPRS, and is contained in piece 5 using the “&” as the delimiter.

> Example:

> X3(#,”DOSE”) = ”&&&&1 TABLESPOONFUL&25&&”

> X3(#,”DO”) = Dosage Ordered (Optional). This would be a Free Text Dosage entered during the order entry process. This would be passed in if Possible Dosage Data is not passed in X4(#,”DOSE_AMT”) and X4(#,”DOSE_UNIT”), or X3(#,”DRG_AMT”) and X3(#,”DRG_UNIT”).

> Example:

> X3(#,”DO”) = ”ONE TO TWO TABLETS”

> X3(#,”MR_IEN”) = MEDICATION ROUTE file (#51.2) IEN (Optional). This must be passed in if X4(#,”ROUTE”) is not passed in.

> Example:

> X3(#,”MR_IEN”) = 12

> X3(#,”SCHEDULE”) = Free Text Schedule (Optional), normally passed in when X4(#,”FREQ”) is not passed in.

> Example:

> X3(#,”SCHEDULE”) = “Q12H”

> X3(#,”DRATE”) = Duration (Optional), with five possible duration values. If only a number is passed in, ‘Days’ will be assumed.

> \#M = \# number of Minutes

> \#H = \# number of Hours

> \#D = \# number of Days

> \#W = \# number of Weeks

> \#L = \# number of Months

> Example:

> X3(#,”DRATE”) = “2D” (representing 2 Days)

> X3(#,”CONJ”) = Conjunction, three possible values: (Required for complex orders when there is a subsequent Dosing Sequence)

> T = Then

> A = And

> E = Except

> Example:

> X3(#,”CONJ”) = “A”

> X3(#,”EFD”) = Expected First Dose, in FileMan Date/time format, for complex Inpatient orders only.

> Example:

> X3(#,”EFD”) = “3180122.145533”

> X3(”CONTEXT”) = (optional) indicates the type of order. If nothing is passed in, the software will assume CPRS-UD (CPRS unit Dose) if called from CPRS, else will assume OP-UD (Outpatient Unit Dose) if called from Pharmacy. Possible values are as follows: (Note that there is no counter subscript.)

> CPRS-UD = CPRS Unit Dose

> OP-UD = Outpatient Unit Dose

> IP-UD = Inpatient Unit Dose

> IP-IV = Inpatient IV

> CPRS-IV-I = CPRS IV Intermittent

> CPRS-IV-C = CPRS IV Continuous

> IP-IV-I = Inpatient IV Intermittent

> IP-IV-I = Inpatient IV Continuous

> Example:

> X3(”CONTEXT”) = “CPRS-UD”

The X4 array Input details:

> X4(#,”RX_NUM”) = Pharmacy Order Number (Required). A multi-piece data element using the ‘;’ as a separator.

> Example:

> X4(#,”RX_NUM”) = “O;1;PROSPECTIVE;1”

> Piece 1 = Order Type (For the Dose call use “O” for Outpatient, “I” for Inpatient.)

> Piece 2 = Order Number (irrelevant for Dose Call, but should be the same throughout a complex order)

> Piece 3 = Drug Type (Use PROSPECTIVE for the Dose Call)

> Piece 4 = Counter (1 for a simple order, must increment for a complex order)

> X4(#,”DRUG_IEN”) = DRUG file (#50) IEN. (Optional)

> Example:

> X4(#,”DRUG_IEN”) = 1636

> X4(#,”DRUG_NM”) = Name of Drug to be used in all return messages. (Required)

> Example:

> X4(#,”DRUG_NM”) = “SIMVASTATIN 40MG TAB”

> X4(#,”DOSE_AMT”) and X4(#,”DOSE_UNIT”) = (Optional) These data elements represent Possible Dosage data. To be used, both of these must be passed in. They represent a numeric Dosage and an FDB Dose Unit.

> Example:

> X4(#,”DOSE_AMT”) = 325

> X4(#,”DOSE_UNIT”) =”MILLIGRAMS”

> X4(“OI”) = PHARMACY ORDERABLE ITEM file (#50.7) IEN. (Optional). If X4(#,”DRUG_IEN”) is passed in, then this will be ignored. If you do not pass in X4(#,”DRUG_IEN”), then this is required. Note that there is no counter subscript.

> Example:

> X4(”OI”) = 123

> X4(“PACKAGE”) = (Optional) One of three values, “O” for Outpatient, “X” for Non-VA Meds, or “I” for Inpatient. Dosing checks are currently not being performed on Non-VA Meds. Note that there is no counter subscript.

> Example:

> X4(”PACKAGE”) = “O”

> X4(“OI_USAGE”)= Orderable Item Usage. (Optional)

> This will only be used if X4(#,”DRUG_IEN”) is not passed in, and X4(“PACKAGE”) is passed in as “I”. Note that there is no counter subscript. The 4 possible values are:

- “B” for Base only
- “A” for Additive only
- “AB” for Base and Additive
- Null if not marked for Base or Additive

> Example:

> X4(”OI_USAGE”) = “A”

> X4(#, “ADJ_MSG”)= Adjusted Dose message (Optional). This is passed in only by Inpatient Medications to be used as a message that gets displayed along with a Single Dose warning (if applicable). The message alerts the user that an adjusted Dose had to be sent to the interface because the frequency had to be rounded to a whole number, which then required the Dose to be adjusted accordingly.

> Example:

> X4(#,”ADJ_MSG”) = PLEASE NOTE: The single dose of the IV Additive has been adjusted to reflect the amount of drug infused over the nearest whole number of hours (1005 ML over 15 hours).

> X4(#,”ROUTE”) = FDB Med Route. (Optional). This must be passed in if X3(#,”MR_IEN”) is not passed in.

> Example:

> X4(#,”ROUTE”)=”ORAL”

> X4(#,”FREQ”) = Frequency. (Optional). Normally passed in when X3(#,”SCHEDULE”) is not passed in.

> Example:

> X4(#,”FREQ”)=4

> X4(#,”DOSE_RATE”) = DOSE RATE (Optional), if not defined, the API will default to DAY.

> Example:

> X4(#,”DOSE_RATE”)=”DAY”

> X4(#,”DOSE_TYPE”) = Dose Type (Optional), the API will default to MAINTENANCE if not passed in. FDB has more than 2 values, but the only 2 possible values we pass in are:

> MAINTENANCE

> SINGLE DOSE

> Example:

> X4(#,”DOSE_TYPE”)=”MAINTENANCE”

> X4(#,”DURATION”) = Duration (Optional)

> Example:

> X4(#,”DURATION””)=1

> X4(#,”DURATION_RT”) = Duration Rate (Optional)

> Example:

> X4(#,”DURATION_RT”)=”DAY”

X4(#,”ENH”) – (Optional) Flag from CPRS indicating that the Enhanced Order Checks were done on this order. It is used to suppress a Dosing exception message if the Dosing exception was already shown as part of the Enhanced Order Checks exception for a drug level type of error. ‘1’ is passed in if enhanced order checks were done.‘0’, null, or an undefined “ENH” node indicates enhanced order checks were not done.

> Example:

> X4(#,”ENH”)=1

> X4(#,”HT_ERROR”) – (Optional) Only passed in as null from the Inpatient Medications Package, indicating to display a missing Body Surface Area (BSA) error along with the Free Text Infusion Rate error (if applicable).

> Example:

> X4(#,”HT_ERROR”)=””

> X4(#,”WT_ERROR”) – (Optional) Only passed in as null from the Inpatient Medications Package indicating to display a missing weight error along with the Free Text Infusion Rate error (if applicable).

> Example:

> X4(#,”WT_ERROR”)=””

> X4(#,”OI_ERROR”, drug name) – (Optional) Indicates an error as designated by the code in piece 1. Piece 2 is equal to the Pharmacy Order Number. Only codes 1 and 4 are passed in by the calling applications.

> Piece 1 codes are as follows:

> 1 – No Dispense Drug Found

> 2 – Free Text Dosage could not be evaluated

> 3 – Free Text Infusion Rate could not be evaluated

> 4 – No Active IV Additive/Solution marked for IV Fluid Order Entry could be found

> Example:

> X4(#,”OI_ERROR”,”SIMVASTATIN 40MG”)=1^“O;1;PROSPECTIVE;1”

> X4(#,”FRQ_ERROR”) – (Optional) This indicates that a Frequency was unable to be derived.

> Example:

> X4(#,”FRQ_ERROR”)=””

> X4(#,”INF_ERROR”) – (Optional) Only passed in from the Inpatient Medication Package indicating to display a Free Text Infusion Rate error.

> Example:

> X4(#,”INF_ERROR”)=””

All of the preceding data is then formatted into a ^TMP global in the DOSE^PSSDSAPD code to be passed into the IN^PSSHRQ2 interface driver routine. This is an example of the Input TMP global:

^TMP(\$J,BASE,”IN”,”DOSE”)=”” (Indicates to interface to perform Dose Call)

^TMP(\$J,BASE,”IN”,”DOSE”,”AGE”)=1088 (Age in Days)

^TMP(\$J,BASE,”IN”,”DOSE”,”BSA”)=2.237778390112771458 (Body Surface Area)

^TMP(\$J,BASE,”IN”,”DOSE”,”O;1;PROSPECTIVE;1”)=”006561^4005197^3776^WARFARIN 2MG TABS^15^MILLIGRAMS^DAY^1^1^DAY^ORAL^SINGLE DOSE^^0”

Data Node.Piece 1 – GCNSEQNO

Piece 2 – VUID (VHA Unique Identifier)

Piece 3 – DRUG file (#50) IEN

Piece 4 – Drug Name

Piece 5 – Dose Amount

Piece 6 – Dose Unit

Piece 7 – Dose Rate

Piece 8 – Frequency

Piece 9 – Duration

Piece 10 – Duration Rate

Piece 11 – Medication Route

Piece 12 – Dose Type

Piece 13 – Not used

Piece 14 – Dose Form Flag (Set from the DOSE FORM INDICATOR field (#3) of the DOSE UNITS file (#51.24).)

^TMP(\$J,BASE,”IN”,”DOSE”,”WT”)=95 (Weight)

^TMP(\$J,BASE,”IN”,”IEN”)=428 (PATIENT file (#2) IEN)

^TMP(\$J,BASE,”IN”,”PROSPECTIVE”,”O;1;PROSPECTIVE;1”)=”006561^4005197^3776^WARFARIN 2MG TABS” (Corresponding node to data node above)

OUTPUT DETAILS:

This is an example of the raw data output. (X1(1) of parameter 1 of DOSE^PSSDSAPD)

^TMP(\$J,BASE,”OUT”,0)=1

^TMP(\$J,BASE,”OUT”,”DOSE”,”O;1;PROSPECTIVE;1”,”WARFARIN 2MG TABS”,”CHEMO”)=”false”

^TMP(\$J,BASE,”OUT”,”DOSE”,”O;1;PROSPECTIVE;1”,”WARFARIN 2MG TABS”,”DAILY”,”MESSAGE”,3776)=”Total dose amount of 15 MILLIGRAMS/DAY exceeds the maximum daily dose amount of 10 MILLIGRAMS/DAY.”

^TMP(\$J,BASE,”OUT”,”DOSE”,”O;1;PROSPECTIVE;1”,”WARFARIN 2MG TABS”,”DAILY”,”STATUS”,3776)=”ExceedsMax”

^TMP(\$J,BASE,”OUT”,”DOSE”,”O;1;PROSPECTIVE;1”,”WARFARIN 2MG TABS”,”DAILY”,”STATUSCODE”,3776)=2

^TMP(\$J,BASE,”OUT”,”DOSE”,”O;1;PROSPECTIVE;1”,”WARFARIN 2MG TABS”,”DAILYMAX”,”MESSAGE”,3776)=”Total dose amount of 15 MILLIGRAMS/DAY exceeds the maximum daily dose amount of 10 MILLIGRAMS/DAY.”

^TMP(\$J,BASE,”OUT”,”DOSE”,”O;1;PROSPECTIVE;1”,”WARFARIN 2MG TABS”,”DAILYMAX”,”STATUS”,3776)=”ExceedsMax”

^TMP(\$J,BASE,”OUT”,”DOSE”,”O;1;PROSPECTIVE;1”,”WARFARIN 2MG TABS”,”DAILYMAX”,”STATUSCODE”,3776)=2

^TMP(\$J,BASE,”OUT”,”DOSE”,”O;1;PROSPECTIVE;1”,”WARFARIN 2MG TABS”,”GENERAL”,”DOSEFORMHIGH”,3776)=”0.17”

^TMP(\$J,BASE,”OUT”,”DOSE”,”O;1;PROSPECTIVE;1”,”WARFARIN 2MG TABS”,”GENERAL”,”DOSEFORMHIGHUNIT”,3776)=”EA/KG/DAY”

^TMP(\$J,BASE,”OUT”,”DOSE”,”O;1;PROSPECTIVE;1”,”WARFARIN 2MG TABS”,”GENERAL”,”DOSEFORMLOW”,3776)=”0.01”

^TMP(\$J,BASE,”OUT”,”DOSE”,”O;1;PROSPECTIVE;1”,”WARFARIN 2MG TABS”,”GENERAL”,”DOSEFORMLOWUNIT”,3776)=”EA/KG/DAY”

^TMP(\$J,BASE,”OUT”,”DOSE”,”O;1;PROSPECTIVE;1”,”WARFARIN 2MG TABS”,”GENERAL”,”DOSEHIGH”,3776)=”0.34”

^TMP(\$J,BASE,”OUT”,”DOSE”,”O;1;PROSPECTIVE;1”,”WARFARIN 2MG TABS”,”GENERAL”,”DOSEHIGHUNIT”,3776)=”MG/KG/DAY”

^TMP(\$J,BASE,”OUT”,”DOSE”,”O;1;PROSPECTIVE;1”,”WARFARIN 2MG TABS”,”GENERAL”,”DOSELOW”,3776)=”0.02”

^TMP(\$J,BASE,”OUT”,”DOSE”,”O;1;PROSPECTIVE;1”,”WARFARIN 2MG TABS”,”GENERAL”,”DOSELOWUNIT”,3776)=”MG/KG/DAY”

^TMP(\$J,BASE,”OUT”,”DOSE”,”O;1;PROSPECTIVE;1”,”WARFARIN 2MG TABS”,”GENERAL”,”DOSEROUTEDESCRIPTION”,3776)=”ORAL”

^TMP(\$J,BASE,”OUT”,”DOSE”,”O;1;PROSPECTIVE;1”,”WARFARIN 2MG TABS”,”GENERAL”,”MAXLIFETIMEDOSE”,3776)=0

^TMP(\$J,BASE,”OUT”,”DOSE”,”O;1;PROSPECTIVE;1”,”WARFARIN 2MG TABS”,”GENERAL”,”MESSAGE”,3776)=”General dosing range for WARFARIN 2MG TABS (ORAL): 0.02 MG/KG/DAY to 0.34 MG/KG/DAY”

^TMP(\$J,BASE,”OUT”,”DOSE”,”O;1;PROSPECTIVE;1”,”WARFARIN 2MG TABS”,”RANGE”,”HIGH”,3776)=”0.34 MG/KG/DAY”

^TMP(\$J,BASE,”OUT”,”DOSE”,”O;1;PROSPECTIVE;1”,”WARFARIN 2MG TABS”,”RANGE”,”LOW”,3776)=”0.02 MG/KG/DAY”

^TMP(\$J,BASE,”OUT”,”DOSE”,”O;1;PROSPECTIVE;1”,”WARFARIN 2MG TABS”,”RANGE”,”STATUS”,3776)=”Passed”

^TMP(\$J,BASE,”OUT”,”DOSE”,”O;1;PROSPECTIVE;1”,”WARFARIN 2MG TABS”,”RANGE”,”STATUSCODE”,3776)=1

^TMP(\$J,BASE,”OUT”,”DOSE”,”O;1;PROSPECTIVE;1”,”WARFARIN 2MG TABS”,”SINGLE”,”MAX”,3776)=”0.34 MG/KG”

^TMP(\$J,BASE,”OUT”,”DOSE”,”O;1;PROSPECTIVE;1”,”WARFARIN 2MG TABS”,”SINGLE”,”STATUS”,3776)=”Passed”

^TMP(\$J,BASE,”OUT”,”DOSE”,”O;1;PROSPECTIVE;1”,”WARFARIN 2MG TABS”,”SINGLE”,”STATUSCODE”,3776)=1

Pharmacy Data Management (PDM) uses the above raw data output, and depending on parameter 1 of the input of the DOSE^PSSDSAPD call, 1 and/or 2 new output globals are created. These globals were created so that the calling applications do not have to determine what errors, message, exceptions, etc. to display. The PDM package does all of that screening and whatever is returned to the calling applications in these two globals should be displayed. Output Global 2 is used by CPRS and Output Global 3 is used by Inpatient Medications and Outpatient Pharmacy.

As stated in the previous paragraph, the parameter 1 input of the DOSE^PSSDSAPD call is used to indicate which globals to return:

X(1) = Literal for Global 1 (Raw data global detailed above)

X(2) = Literal for Global 2 (Details below)

X(3) = Literal for Global 3 (Details below)

Some general notes pertaining to Outputs 2 and 3:

It is possible there may be additional values added for the Type subscript in the Valid Dose Messages, so it is recommended to loop on that subscript instead of hard-coding these 3 entries. It is also recommended to loop on all non-literal subscripts because of the various possible returns, especially for complex orders.

When DRUG_IEN is a subscript, it will be the value of X4(#,”DRUG_IEN”) if that value is passed in, else will be the value of X4 (“OI”).

For the RX_NUM subscript, it is possible that the API had to create a new Dosing Sequence, and if so, the RX_NUM would not be one that was sent into the API. For example, a complex Outpatient Order and the first two conjunctions are “A” for AND, and these three RX_NUM’s are passed in:

> “O;12345;PROSPECTIVE;1”

> “O;12345;PROSPECTIVE;2”

> “O;12345;PROSPECTIVE;3”

If the data for the first two Dosing Sequences meet certain business rules, the API may have to create a 2<sup>nd</sup> Dosing sequence for

> “O;12345;PROSPECTIVE;3”

> And it would be:

> “O;12345;PROSPECTIVE;3;1”

You see that a fifth piece (1) had to be added. The reason is for “O;12345;PROSPECTIVE;3” that data had to be passed in for the Maximum Single Dose Order Check. Due to the way the FDB API’s are structured, another Dosing Sequence has to be sent into the interface adding the Dosages from the first three to do the Max Daily Dose Order Check. The output is screened so only the Maximum Single Dose Order Check data is displayed for “O;12345;PROSPECTIVE;3” and only Max Daily Dose Order Check data is displayed for “O;12345;PROSPECTIVE;3;1”.

Following are further output details of X(1), X(2), and X(3) of parameter 1 of the DOSE^PSSDSAPD call.

X(1) Output: (With BASE equal to X(1) of parameter 1 of the DOSE^PSSDSAPD call)

> Top level ‘0’ node:

> As part of the raw data captured above, the top level ‘0’ node is returned as follows:

Piece 1 of this node will be set to -1 if there is a fatal error of some kind and the Vendor database cannot be reached, and piece 2 will be set to the reason. Else it will be set to 0 or 1.

> Example:

> ^TMP(\$J,BASE,”OUT”,0)=1

X(2) Output: (With BASE equal to X(2) of parameter 1 of the DOSE^PSSDSAPD call)

System level error message:

Piece 1 of this node will be set to -1 if there is a fatal error of some kind and the Vendor database cannot be reached, and piece 2 will be set to the reason. Else it will be set to 0 or 1.

> Example:

> ^TMP(\$J,BASE,”OUT”,0)=”-1^Vendor Database cannot be reached.”

<span id="Page_14" class="anchor"></span>High Single Dose message:

> ^TMP(\$J,BASE,”OUT”,”CHECK”,X1,RX_NUM,X2,”ATYPE”)=”DOSE^SINGLE”

> ^TMP(\$J,BASE,”OUT”,”CHECK”,X1,RX_NUM,X2,”MSG”,1)=warning text

> where X1 = piece 4 “;” of RX_NUM

> where RX_NUM = Order Number

> where X2 = return counter

> Example:

> ^TMP(\$J,BASE,"OUT","CHECK",1,"O;1;PROSPECTIVE;1",1,"ATYPE")="DOSE^SINGLE"

> ^TMP(\$J,BASE,"OUT","CHECK",1,"O;1;PROSPECTIVE;1",1,"MSG",1)="BACLOFEN 10MG TABS: Single dose amount of 1,000 MILLIGRAMS exceeds the maximum single dose amount of 20 MILLIGRAMS.”

High Single Dose message with Per Orifice note (the Per Orifice note will precede any High Single Dose, High Daily Dose, or General Dosing Guidelines message for any drugs administered via the eye, ear or nose):

> ^TMP(\$J,BASE,”OUT”,”CHECK”,X1,RX_NUM,X2,”ATYPE”)=”DOSE^SINGLE”

> ^TMP(\$J,BASE,”OUT”,”CHECK”,X1,RX_NUM,X2,”MSG”,1)=warning text

> where X1 = piece 4 “;” of RX_NUM

> where RX_NUM = Order Number

> where X2 = return counter

> Example:

> ^TMP(\$J,BASE,"OUT","CHECK",1,"O;1;PROSPECTIVE;1",2,"ATYPE")="DOSE^SINGLE"

> ^TMP(\$J,BASE,"OUT","CHECK",1,"O;1;PROSPECTIVE;1",2,"MSG",1)= "Dosing Information provided is PER NOSTRIL:"

> ^TMP(\$J,BASE,"OUT","CHECK",1,"O;1;PROSPECTIVE;1",2,"MSG",2)= "CROMOLYN 40MG/ML (4%) NASAL SPRAY 26ML: Single dose form amount of 2 SPRAY(S) exceeds the maximum single dose form amount of 1 SPRAY(S)."

High Daily Dose message:

> ^TMP(\$J,BASE,”OUT”,”CHECK”,X1,RX_NUM,X2,”ATYPE”)=”DOSE^DAILY”

> ^TMP(\$J,BASE,”OUT”,”CHECK”,X1,RX_NUM,X2,”MSG”,1)=warning text

> where X1 = piece 4 “;” of RX_NUM

> where RX_NUM = Order Number

> where X2 = return counter

> Example:

> ^TMP(\$J,BASE,"OUT","CHECK",1,"O;1;PROSPECTIVE;1",2,"ATYPE")="DOSE^DAILY"

> ^TMP(\$J,BASE,"OUT","CHECK",1,"O;1;PROSPECTIVE;1",2,"MSG",1)="BACLOFEN10MG TABS: Total dose amount of 2,000 MILLIGRAMS/DAY exceeds the maximum daily dose amount of 80 MILLIGRAMS/DAY."

High Single Dose message and High Daily Dose messages with adjusted dose example. For continuous IV orders with a drug (as an IV Additive or within a PreMix Solution) that is not administered via a ‘CONTINUOUS’ FDB route and the frequency of the order is less than one (i.e. IV bag infuses longer than the order duration) or the frequency requires rounding for a 24 hour period (i.e. IV bag infuses longer than 24 hours), they may require single dose adjustments. If the single dose adjustment is made, a corresponding adjustment will also result with the daily dose. This information is summarized in parenthesis in both Warning messages.

^TMP(\$J,BASE,”OUT”,”CHECK”,X1,RX_NUM,X2,”ATYPE”)=”DOSE^SINGLE”

^TMP(\$J,BASE,”OUT”,”CHECK”,X1,RX_NUM,X2,”MSG”,1)=warning text

> where X1 = piece 4 “;” of RX_NUM

> where RX_NUM = Order Number

> where X2 = return counter

^TMP(\$J,BASE,”OUT”,”CHECK”,X1,RX_NUM,X2,”ATYPE”)=”DOSE^DAILY”

^TMP(\$J,BASE,”OUT”,”CHECK”,X1,RX_NUM,X2,”MSG”,1)=warning text

> where X1 = piece 4 “;” of RX_NUM

> where RX_NUM = Order Number

> where X2 = return counter

> Example:

> ^TMP(\$J,BASE,"OUT","CHECK",1,"I;;PROSPECTIVE;1",1,"ATYPE")="DOSE^SINGLE"

> ^TMP(\$J,BASE,"OUT","CHECK",1,"I;;PROSPECTIVE;1",1,"MSG",1)= "FOLIC ACID INJ,SOLN 1000 MG: Single dose amount of 670 MILLIGRAMS exceeds the maximum single dose amount of 1 MILLIGRAMS. (670 ML over 10 hours)"

> ^TMP(\$J,BASE,"OUT","CHECK",1,"I;;PROSPECTIVE;1",2,"ATYPE")="DOSE^DAILY"

> ^TMP(\$J,BASE,"OUT","CHECK",1,"I;;PROSPECTIVE;1",2,"MSG",1)=" "FOLIC ACID INJ,SOLN 1000 MG: Total dose amount of 670 MILLIGRAMS/DAY exceeds the maximum daily dose amount of 1 MILLIGRAMS/DAY. (670 ML over 10 hours)"

General Dosing Guidelines message:

^TMP(\$J,BASE,”OUT”,”CHECK”,X1,RX_NUM,X2,”ATYPE”)=”DOSE^GENERAL”

^TMP(\$J,BASE,”OUT”,”CHECK”,X1,RX_NUM,X2,”MSG”,1)=guidelines text

> where X1 = piece 4 “;” of RX_NUM

> where RX_NUM = Order Number

> where X2 = return counter

> Example:

> ^TMP(\$J,BASE,"OUT","CHECK",1,"O;1;PROSPECTIVE;1",3,"ATYPE")="DOSE^GENERAL"

> ^TMP(\$J,BASE,"OUT","CHECK",1,"O;1;PROSPECTIVE;1",3,"MSG",1)="General dosing range for BACLOFEN 10MG TABS (ORAL): 10 milligram per day to 80 milligram per day. Maximum daily dose is 80 milligram per day."

Exception message:

^TMP(\$J,BASE,”OUT”,”CHECK”,X1,RX_NUM,X2,”ATYPE”)=”DOSE^EXCEPTION”

^TMP(\$J,BASE,”OUT”,”CHECK”,X1,RX_NUM,X2,”MSG”,1)=exception text

> where X1 = piece 4 “;” of RX_NUM

> where RX_NUM = Order Number

> where X2 = return counter

> Example:

> ^TMP(\$J,BASE,"OUT","CHECK",1,"O;1;PROSPECTIVE;1",1,"ATYPE")="DOSE^EXCEPTION"

> ^TMP(\$J,BASE,"OUT","CHECK",1,"O;1;PROSPECTIVE;1",3,"MSG",1)=" Max Daily Dose Check could not be done for Drug: BACLOFEN 10MG TABS, please complete a manual check for appropriate Dosing."

Exception message with a Height/Weight required message (If a Dose check cannot be done because that drug requires a Weight and/or Body Surface Area and the patient does not have a Weight and/or Height documented, that information will be returned):

^TMP(\$J,BASE,”OUT”,”CHECK”,X1,RX_NUM,X2,”ATYPE”)=”DOSE^EXCEPTION”

^TMP(\$J,BASE,”OUT”,”CHECK”,X1,RX_NUM,X2,”MSG”,1)=exception text

> where X1 = piece 4 “;” of RX_NUM

> where RX_NUM = Order Number

> where X2 = return counter

> Example:

> ^TMP(\$J,BASE,"OUT","CHECK",1,"O;1;PROSPECTIVE;1",1,"ATYPE")="DOSE^EXCEPTION"

> ^TMP(\$J,BASE,"OUT","CHECK",1,"O;1;PROSPECTIVE;1",1,"MSG",1)= "Dosing Checks could not be done for Drug: LOMUSTINE 100MG CAP. Reason(s): No weight and/or height documented for patient."

Exception message with warning (This is actually a warning ‘error’ from the Vendor):

^TMP(\$J,BASE,”OUT”,”CHECK”,X1,RX_NUM,X2,”ATYPE”)=”DOSE^EXCEPTION”

^TMP(\$J,BASE,”OUT”,”CHECK”,X1,RX_NUM,X2,”MSG”,1)=exception/warning text

> where X1 = piece 4 “;” of RX_NUM

> where RX_NUM = Order Number

> where X2 = return counter

> Example:

> ^TMP(\$J,BASE,"OUT","CHECK",1,"O;1;PROSPECTIVE;1",1,"ATYPE")="DOSE^EXCEPTION"

> ^TMP(\$J,BASE,"OUT","CHECK",1,"O;1;PROSPECTIVE;1",1,"MSG",1)= "Dosing Order Check Warning for NITROGLYCERIN PATCHES 10MG/24HR: Dosing is not established for a patient of this age."

Informational message:

^TMP(\$J,BASE,”OUT”,”CHECK”,X1,RX_NUM,X2,”ATYPE”)=”DOSE^INFORMATIONAL”

^TMP(\$J,BASE,”OUT”,”CHECK”,X1,RX_NUM,X2,”MSG”,1)=informational text

> where X1 = piece 4 “;” of RX_NUM

> where RX_NUM = Order Number

> where X2 = return counter

> Example:

> ^TMP(\$J,BASE,"OUT","CHECK",1,"O;1;PROSPECTIVE;1",1,"ATYPE")="DOSE^INFORMATIONAL"

> ^TMP(\$J,BASE,"OUT","CHECK",1,"O;1;PROSPECTIVE;1",1,"MSG",1)= "Recommended frequency of SIMVASTATIN 10MG TAB is 1 time(s) per day."

Complex order (IV) example message. In this example multiple drug entries are passed into FDB. The output contains High Single Dose messages, High Daily Dose messages, Exception messages, and General Dosing Guidelines messages. All of the ^TMP output globals have been documented in the above examples, so only the output example will be documented here.

> Example:

> ^TMP(\$J,BASE,"OUT","CHECK",1,"I;;PROSPECTIVE;1",1,"ATYPE")="DOSE^SINGLE"

> ^TMP(\$J,BASE,"OUT","CHECK",1,"I;;PROSPECTIVE;1",1,"MSG",1)="POTASSIUM CHLORIDE

> INJ,SOLN 60 MEQ: Single dose amount of 60 MILLIEQUIVALENTS exceeds the maximum single dose amount of 40 MILLIEQUIVALENTS."

> ^TMP(\$J,BASE,"OUT","CHECK",1,"I;;PROSPECTIVE;1",2,"ATYPE")="DOSE^DAILY"

> ^TMP(\$J,BASE,"OUT","CHECK",1,"I;;PROSPECTIVE;1",2,"MSG",1)="POTASSIUM CHLORIDE

> INJ,SOLN 60 MEQ: Total dose amount of 1,440 MILLIEQUIVALENTS/DAY exceeds the maximum daily dose amount of 100 MILLIEQUIVALENTS/DAY."

> ^TMP(\$J,BASE,"OUT","CHECK",2,"I;;PROSPECTIVE;2",1,"ATYPE")="DOSE^EXCEPTION"

> ^TMP(\$J,BASE,"OUT","CHECK",2,"I;;PROSPECTIVE;2",1,"MSG",1)="Dosing Checks could not be done for Drug: MAGNESIUM SULFATE INJ,SOLN 16 MEQ, please complete a manual check for appropriate Dosing. "

> ^TMP(\$J,BASE,"OUT","CHECK",2,"I;;PROSPECTIVE;2",2,"ATYPE")="DOSE^EXCEPTION"

> ^TMP(\$J,BASE,"OUT","CHECK",2,"I;;PROSPECTIVE;2",2,"MSG",1)="Dosing Checks could

> not be done for Drug: MAGNESIUM SULFATE INJ,SOLN 16 MEQ, please complete a manual check for appropriate Dosing. "

> ^TMP(\$J,BASE,"OUT","CHECK",2,"I;;PROSPECTIVE;2",3,"ATYPE")="DOSE^GENERAL"

> ^TMP(\$J,BASE,"OUT","CHECK",2,"I;;PROSPECTIVE;2",3,"MSG",1)="General dosing range for MAGNESIUM SULFATE INJ,SOLN 16 MEQ (INTRAVENOUS): 0.5 gram per day to 250 milligram per kilogram per day. Maximum daily dose is 12 gram per day."

> ^TMP(\$J,BASE,"OUT","CHECK",3,"I;;PROSPECTIVE;3",1,"ATYPE")="DOSE^EXCEPTION"

> ^TMP(\$J,BASE,"OUT","CHECK",3,"I;;PROSPECTIVE;3",1,"MSG",1)="Dosing Checks could not be done for Drug: CALCIUM GLUCONATE INJ,SOLN 20 MEQ, please complete a manual check for appropriate Dosing. "

> ^TMP(\$J,BASE,"OUT","CHECK",3,"I;;PROSPECTIVE;3",2,"ATYPE")="DOSE^EXCEPTION"

> ^TMP(\$J,BASE,"OUT","CHECK",3,"I;;PROSPECTIVE;3",2,"MSG",1)="Dosing Checks could not be done for Drug: CALCIUM GLUCONATE INJ,SOLN 20 MEQ, please complete a manual check for appropriate Dosing. "

> ^TMP(\$J,BASE,"OUT","CHECK",3,"I;;PROSPECTIVE;3",3,"ATYPE")="DOSE^GENERAL"

> ^TMP(\$J,BASE,"OUT","CHECK",3,"I;;PROSPECTIVE;3",3,"MSG",1)="General dosing range for CALCIUM GLUCONATE INJ,SOLN 20 MEQ (INTRAVENOUS): 1.9 milligram per kilogram per day to 6000 milligram per day. Maximum daily dose is 8000 milligram per day.”

> ^TMP(\$J,BASE,"OUT","CHECK",5,"I;;PROSPECTIVE;5",1,"ATYPE")="DOSE^DAILY"

> ^TMP(\$J,BASE,"OUT","CHECK",5,"I;;PROSPECTIVE;5",1,"MSG",1)="RANITIDINE INJ 50 MG: Total dose amount of 1,200 MILLIGRAMS/DAY exceeds the maximum daily dose amount of 400 MILLIGRAMS/DAY."

X(3) Output:

System-level error message:

Piece 1 of this node will be set to -1 if there is a fatal error of some kind and the Vendor database cannot be reached, and piece 2 will be set to the reason. Else it will be set to 0 or 1.

> Example:

> ^TMP(\$J,BASE,”OUT”,0)=1

High Single Dose message:

^TMP(\$J,BASE,"OUT",X1,RX_NUM,”MESSAGE",”1_SINGLE”,drug_ien)=warning text

> where X1 = piece 4 “;” of RX_NUM

> where RX_NUM = Order Number

> where drug_ien = Drug (#50) File internal entry number

> Example:

> ^TMP(\$J,BASE,"OUT",1,"O;1;PROSPECTIVE;1","MESSAGE","1_SINGLE",155)="WARF ARIN 10MG TAB: Single dose amount of 20 MILLIGRAMS exceeds the maximum single dose amount of 7.5 MILLIGRAMS."

High Daily Dose message:

^TMP(\$J,BASE,"OUT",X1,RX_NUM,”MESSAGE",”2_RANGE”,drug_ien)=warning text

> where X1 = piece 4 “;” of RX_NUM

> where RX_NUM = Order Number

> where drug_ien = Drug (#50) File internal entry number

> Example:

> ^TMP(\$J,BASE,"OUT",1,"O;1;PROSPECTIVE;1","MESSAGE","2_RANGE",155)="WARF ARIN 10MG TAB: Total dose amount of 40 MILLIGRAMS/DAY exceeds the maximum daily dose amount of 7.5 MILLIGRAMS/DAY."

Informational message:

^TMP(\$J,BASE,"OUT",X1,RX_NUM,”MESSAGE",”4_TRAIL”)=informational text

> where X1 = piece 4 “;” of RX_NUM

> where RX_NUM = Order Number

> Example:

> ^TMP(\$J,BASE,"OUT",1,"O;1;PROSPECTIVE;1","MESSAGE","4_TRAIL")="Recommended frequency of BACLOFEN 10MG TABS is 2 to 4 times per day."

High Single Dose and High Daily Dose messages with Per Orifice note (the Per Orifice note will precede any High Single Dose, High Daily Dose, or General Dosing Guidelines message for any drugs administered via the eye, ear or nose):

^TMP(\$J,BASE,"OUT",X1,RX_NUM,”MESSAGE",”.1_INTRO”,drug_ien)=introductory text

^TMP(\$J,BASE,"OUT",X1,RX_NUM,”MESSAGE",”1_SINGLE”,drug_ien)=warning text

^TMP(\$J,BASE,"OUT",X1,RX_NUM,”MESSAGE",”2_RANGE”,drug_ien)=warning text

> where X1 = piece 4 “;” of RX_NUM

> where RX_NUM = Order Number

> where drug_ien = Drug (#50) File internal entry number

> Example:

> ^TMP(\$J,BASE"OUT",1,"O;1;PROSPECTIVE;1","MESSAGE",".1_INTRO")="Dosing Information provided is PER NOSTRIL:"

> ^TMP(\$J,BASE"OUT",1,"O;1;PROSPECTIVE;1","MESSAGE","1_SINGLE",173)="CROMOLYN 40MG/ML (4%) NASAL SPRAY 26ML: Single dose form amount of 4 SPRAY(S) exceeds the maximum single dose form amount of 1 SPRAY(S)."

> ^TMP(\$J,BASE"OUT",1,"O;1;PROSPECTIVE;1","MESSAGE","2_RANGE",173)="CROMOLYN 40MG/ML (4%) NASAL SPRAY 26ML: Total dose form amount of 8 SPRAY(S)/DAY exceeds the maximum daily dose form amount of 6 SPRAY(S)/DAY."

High Single Dose message and High Daily Dose messages with adjusted dose example. For continuous IV orders with a drug (as an IV Additive or within a PreMix Solution) that is not administered via a ‘CONTINUOUS’ FDB route and the frequency of the order is less than one (i.e. IV bag infuses longer than the order duration) or the frequency requires rounding for a 24 hour period (i.e. IV bag infuses longer than 24 hours), they may require single dose adjustments. If the single dose adjustment is made, a corresponding adjustment will also result with the daily dose.

^TMP(\$J,BASE,"OUT",X1,RX_NUM,”MESSAGE",”.5_SINGLE”,drug_ien)=adjusted dose text

^TMP(\$J,BASE,"OUT",X1,RX_NUM,”MESSAGE",”1_SINGLE”,drug_ien)=warning text

^TMP(\$J,BASE,"OUT",X1,RX_NUM,”MESSAGE",”2_RANGE”,drug_ien)=warning text

> where X1 = piece 4 “;” of RX_NUM

> where RX_NUM = Order Number

> where drug_ien = Drug (#50) File internal entry number

> Example:

> ^TMP(\$J,BASE,"OUT",1,"I;6V;PROSPECTIVE;1","MESSAGE",".5_SINGLE",1343)="PLEASE NOTE: The single dose of the IV Additive has been adjusted to reflect the amount of drug infused over the nearest whole number of hours (1005 ML over 15 hours)."

> ^TMP(\$J,BASE,"OUT",1,"I;6V;PROSPECTIVE;1","MESSAGE","1_SINGLE",1343)="FOLIC ACID 1000 MG: Single dose amount of 1,005 MILLIGRAMS exceeds the maximum single dose amount of 1 MILLIGRAMS."

^TMP(\$J,BASE,"OUT",1,"I;6V;PROSPECTIVE;1","MESSAGE","2_RANGE",1343)="FOLIC ACID 1000 MG: Total dose amount of 1,005 MILLIGRAMS/DAY exceeds the maximum daily dose amount of 1 MILLIGRAMS/DAY."

High Single Dose message and High Daily Dose messages are exactly the same. When this occurs the warning message is only returned one time.

^TMP(\$J,BASE,"OUT",X1,RX_NUM,”MESSAGE",”1_SINGLE_RANGE”,drug_ien)=warning text

> where X1 = piece 4 “;” of RX_NUM

> where RX_NUM = Order Number

> where drug_ien = Drug (#50) File internal entry number

> Example:

> ^TMP(\$J,BASE,"OUT",1,"I;6V;PROSPECTIVE;1","MESSAGE","1_SINGLE_RANGE",1343)= "CEFAZOLIN 10000 GM: The dose rate of 1,250 GRAMS/HOUR exceeds the maximum dose rate of 0.66667 GRAMS/HOUR."

Exception message and General Dosing Guidelines messages.

^TMP(\$J,BASE,"OUT",X1,RX_NUM,”EXCEPTIONS”X2)=exception information

> where X1 = piece 4 “;” of RX_NUM

> where RX_NUM = Order Number

> where X2 = counter

^TMP(\$J,BASE,"OUT",X1,RX_NUM,”MESSAGE",”3_GENERAL”,drug_ien,X2)=guidelines text

> where X1 = piece 4 “;” of RX_NUM

> where RX_NUM = Order Number

> where drug_ien = Drug (#50) File internal entry number

> where X2 = counter

> Example:

> ^TMP(\$J,BASE,"OUT",1,"O;1;PROSPECTIVE;1","EXCEPTIONS",1)="Max Daily Dose Check could not be performed for Drug: WARFARIN 2MG TABS"

> ^TMP(\$J,BASE,"OUT",1,"O;1;PROSPECTIVE;1","EXCEPTIONS",2)=" Reason(s): Invalid or Undefined Frequency"

> ^TMP(\$J,BASE,"OUT",1,"O;1;PROSPECTIVE;1","MESSAGE","3_GENERAL",3776,1)="General dosing range for WARFARIN 2MG TABS (ORAL): 0.409 milligram per day to 7.5 milligram per day. Maximum daily dose is 7.5 milligram per day."

Error messages for Single and Daily Dose checks.

> ^TMP(\$J,BASE,"OUT",X1,RX_NUM,”ERROR”,X2,”MSG”)=error introduction

> ^TMP(\$J,BASE,"OUT",X1,RX_NUM,”ERROR”,X2,”TEXT”)=error text

> where X1 = piece 4 “;” of RX_NUM

> where RX_NUM = Order Number

> where X2 = counter

> Example:

> ^TMP(\$J,BASE,"OUT",1,"O;1;PROSPECTIVE;1","ERROR",1,"MSG")="Maximum Single Dose Check could not be performed for Drug: WARFARIN 2MG TABS:"

> ^TMP(\$J,BASE,"OUT",1,"O;1;PROSPECTIVE;1","ERROR",1,"TEXT")="Reason(s) for BUCCAL route: No dosing information specific to maximum single dose is available from the database."

> ^TMP(\$J,BASE,"OUT",1,"O;1;PROSPECTIVE;1","ERROR",2,"MSG")="Max Daily Dose Check could not be performed for Drug: WARFARIN 2MG TABS:"

> ^TMP(\$J,BASE,"OUT",1,"O;1;PROSPECTIVE;1","ERROR",2,"TEXT")="Reason(s) for BUCCAL route: Unavailable"

Warning Message.

> ^TMP(\$J,BASE,"OUT",X1,RX_NUM,”ERROR”,X2,”MSG”)=warning introduction

> ^TMP(\$J,BASE,"OUT",X1,RX_NUM,”ERROR”,X2,”TEXT”)=warning text

> where X1 = piece 4 “;” of RX_NUM

> where RX_NUM = Order Number

> where X2 = counter

> Example:

> ^TMP(\$J,BASE,"OUT",1,"O;1;PROSPECTIVE;1","ERROR",1,"MSG")="Dosing Order Check Warning for CLOPIDOGREL 300MG TAB:"

> ^TMP(\$J,BASE,"OUT",1,"O;1;PROSPECTIVE;1","ERROR",1,"TEXT")="Dosing is not established for a patient of this age."

<span id="Page_23" class="anchor"></span>Error message for Single and Daily Dose checks, General Dosing guidelines, and recommended frequency message.

> ^TMP(\$J,BASE,"OUT",X1,RX_NUM,”ERROR”,X2,”MSG”)=error introduction

> ^TMP(\$J,BASE,"OUT",X1,RX_NUM,”ERROR”,X2,”TEXT”)=error text

> ^TMP(\$J,BASE,"OUT",X1,RX_NUM,”MESSAGE",”3_GENERAL”,drug_ien,X2)=guidelines text

> where X1 = piece 4 “;” of RX_NUM

> where RX_NUM = Order Number

> where drug_ien = Drug (#50) File internal entry number

> where X2 = counter

> ^TMP(\$J,BASE,"OUT",X1,RX_NUM,”MESSAGE”,”4_TRAIL”)= Recommended frequency text

> where X1 = piece 4 “;” of RX_NUM

> where RX_NUM = Order Number

> Example:

> ^TMP(\$J,BASE,"OUT",1,"O;1;PROSPECTIVE;1","ERROR",1,"MSG")="Dosing Checks could not be performed for Drug: LOMUSTINE 10MG CAP"

> ^TMP(\$J,BASE,"OUT",1,"O;1;PROSPECTIVE;1","ERROR",1,"TEXT")="Reason(s): Body surface area required."

> ^TMP(\$J,BASE,"OUT",1,"O;1;PROSPECTIVE;1","MESSAGE","3_GENERAL",1613,1)="General dosing range for LOMUSTINE 10MG CAP (ORAL): 117 milligram per meter squared per day to 143 milligram per meter squared per day. Maximum daily dose is 143 milligram per meter squared per day."

> ^TMP(\$J,BASE,"OUT",1,"O;1;PROSPECTIVE;1","MESSAGE","4_TRAIL")= "Recommended frequency of LOMUSTINE 10MG CAP is 1 time(s) per day."

> **NOTE:** the Recommended Frequency message will always be the last message to display in Pharmacy.

High Single Dose messages in a complex order:

> ^TMP(\$J,BASE,"OUT",X1,RX_NUM,”MESSAGE",”1_SINGLE”,drug_ien)=warning text

> where X1 = piece 4 “;” of RX_NUM

> where RX_NUM = Order Number

> where drug_ien = Drug (#50) File internal entry number

> Example:

> ^TMP(\$J,BASE,"OUT",1,"O;1;PROSPECTIVE;1","MESSAGE","1_SINGLE",155)="WARFARIN 10MG TAB: Single dose amount of 20 MILLIGRAMS exceeds the maximum single dose amount of 7.5 MILLIGRAMS."

> ^TMP(\$J,BASE,"OUT",2,"O;1;PROSPECTIVE;2","MESSAGE","1_SINGLE",155)="WARFARIN 10MG TAB: Single dose amount of 10 MILLIGRAMS exceeds the maximum single dose amount of 7.5 MILLIGRAMS."

> **NOTE:** As of Mocha 2.1b, only the Single Dose checks are performed on complex orders, however, in the background, massaging of the data is performed to do the Daily Dose check, the data is just not displayed to the user. For example, when the ‘AND’ conjunction is used, a new Pharmacy Order number is created with an additional fifth piece, "O;1;PROSPECTIVE;2;1", for the sole purpose of adding the dosages from the previous dosing sequences together to send in this new Dosing sequence to receive daily dose check information.

# Drug-Drug Interaction/Duplicate Therapy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As stated earlier, the Drug-Drug Interaction and Duplicate Therapy Order Checks must be together in a call to the interface with no other order checks or pings as part of the call.

For Drug-Drug Interaction and Duplicate Therapy Order Checks, the software will check prospective against profile drugs and prospective against prospective drugs.

The software’s default behavior for Drug-Drug Interaction and Duplicate Therapy Order Checks is to check prospective medications against profile medications and prospective medications against each other. An unsupported feature allows the software to check ALL medications against each other—prospective against profile, prospective against prospective and profile against profile. This is accomplished by setting a PROFILEVPROFILE node as shown below:

^TMP(\$J,BASE, “IN”,”PROFILEVPROFILE”) =””

These nodes indicate that the Drug-Drug Interaction and Duplicate Therapy Order Checks are the checks to be performed:

^TMP(\$J,BASE,”IN”,”DRUGDRUG”) = ””

^TMP(\$J,BASE,”IN”,”THERAPY”) = ””

For CPRS, Drug-Drug Interaction and Duplicate Therapy Order Checks are performed when CPRS calls this line tag:

> CPRS^PSODDPR4(PSODFN,LIST,.PDRG,PTY)

Where:

> PSODFN = PATIENT’S IEN

> LIST = GLOBAL BASE SUBSCRIPT

> PDRG = DRUG ARRAY where ‘n’ is a counter:

> PDRG(n) = DRUG File (#50) internal entry number^DRUG File (#50) .01 field^null or DRUG File (#50) .01 field^CPRS order number

> PTY = PACKAGE (O or I);ORDER NUMBER (Optional)

| Note:                                                                                                      | The PDRG array is for newly ordered medications to be checked against the patient’s existing medication profile. |
|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| ![](vista-to-mocha-version-2-interface-document/004.png) |                                                                                                                  |

Example of an Input ^TMP global for Drug-Drug Interaction and Duplicate Therapy Order Checks:

^TMP(\$J,BASE,"IN","DRUGDRUG")=""

^TMP(\$J,BASE,"IN","IEN")=181

^TMP(\$J,BASE,"IN","PROFILE","O;402236;PROFILE;2")="000378^4001737^37

81^CAPTOPRIL 100MG TABS^11460^O"

^TMP(\$J,BASE,"IN","PROFILE","O;402237;PROFILE;3")="^0^2977^CAPTOPRIL

25MG TABS^11461^O"

^TMP(\$J,BASE,"IN","PROFILE","O;402262;PROFILE;6")="040238^4013279^79

01^SIMVASTATIN 80MG TAB^11543^O"

^TMP(\$J,BASE,"IN","PROFILE","O;402263;PROFILE;8")="016995^4005766^79

03^ASPIRIN 81MG TAB^11554^O"

^TMP(\$J,BASE,"IN","PROFILE","O;402264;PROFILE;5")="016579^4010153^79

02^SIMVASTATIN 40MG TAB^11556^O"

^TMP(\$J,BASE,"IN","PROFILE","O;402369;PROFILE;12")="002819^4008952^8

33^SIMETHICONE 40MG TAB^11831^O"

^TMP(\$J,BASE,"IN","PROFILE","O;402465;PROFILE;11")="008779^4003800^1

613^LOMUSTINE 10MG CAP^12037^O"

^TMP(\$J,BASE,"IN","PROFILE","O;402561;PROFILE;4")="000300^4003452^16

93^MINOXIDIL 2.5MG S.T.^12254^O"

^TMP(\$J,BASE,"IN","PROFILE","O;402563;PROFILE;9")="002947^4008446^83

4^BISACODYL 5MG TAB^12256^O"

^TMP(\$J,BASE,"IN","PROFILE","O;403274;PROFILE;10")="011663^4006820^1

847^CIMETIDINE 150MG/ML 8ML INJ^13552^O"

^TMP(\$J,BASE,"IN","PROFILE","O;403275;PROFILE;14")="000123^4003366^1

940^AMINOPHYLLIN 200MG TAB ^13553^O"

^TMP(\$J,BASE,"IN","PROSPECTIVE","Z;1;PROSPECTIVE;1")="6559^4029330^7

906^WARFARIN 10MG TAB"

^TMP(\$J,BASE,"IN","THERAPY")=""

The following breaks down the above ^TMP global into more detail:

The first and last nodes indicate to perform Drug-Drug Interaction and Duplicate Therapy Order Checks:

^TMP(\$J,BASE,"IN","DRUGDRUG")=""

^TMP(\$J,BASE,"IN","THERAPY")=""

This node represents the IEN of the patient from the PATIENT file (#2):

^TMP(\$J,BASE,"IN","IEN")=181

This node represents the drugs that are being ordered (prospective drugs). In this case, there is only one prospective drug:

^TMP(\$J,BASE,"IN","PROSPECTIVE","Z;1;PROSPECTIVE;1")="6559^4029330^7

906^WARFARIN 10MG TAB"

The Z;1;PROSPECTIVE;1" subscript represents the Pharmacy Order Number,

Pharmacy Order Number is formatted as:

> Order Type (INPATIENT\| OUTPATIENT\|NON VA\| PENDING \| REMOTE)

> ; Order Number

> ; Drug Type (PROFILE \| PROSPECTIVE \| REMOTE)

> ; COUNTER

Examples of Order Type for Pharmacy Order Number can be Z=Outpatient Prospective Drug, I=Inpatient, O=Outpatient, R=RDI.

Examples of Order Number for Pharmacy Order Number can be the order number for outpatient and inpatient drugs, the ‘D0’ value from the ^XTMP array of the RDI call for remote orders, or some other unique value.

Examples of drug type flag values include prospective, profile, and remote.

A counter will be appended to the fourth piece of each Pharmacy Order Number that identifies a profile or prospective drug as unique.

The combination of the four pieces of the Pharmacy Order Number must be unique.

Drug Name will be used to populate the optional Descriptive Name value in FDB. The text of DRUG NAME will replace the FDB drug name in all return values that use a drug name.

The Drug IEN value for Outpatient and Inpatient orders is the IEN from DRUG file (#50). The Drug IEN value for remote orders is the VUID of the drug. The VUID is attained by using the pointer in DRUG file (#50), PSNDF VA PRODUCT NAME ENTRY field (#22), which points to file VA PRODUCT file (#50.68).

The value of the Prospective node -"6559^4029330^7906^WARFARIN 10MG TAB" is as follows:

Piece 1 – The GCNSEQNO field (#11) of the VA PRODUCT file (#50.68)

Piece 2 - The VUID field (#99.99) of the VA PRODUCT file (#50.68)

Piece 3 – The IEN from the DRUG file (#50)

Piece 4 - Drug Name. It will be used to populate the Descriptive Name value in FDB. The text of DRUG NAME will replace the FDB drug name in all return values that use a drug name.

The Profile nodes represent the drugs that are currently on the Profile. The various profiles and drugs from those profiles will differ depending on the package where the order is being placed.

> Example:

^TMP(\$J,BASE,"IN","PROFILE","O;402262;PROFILE;6")="040238^4013279^79

01^SIMVASTATIN 80MG TAB^11543^O"

The value of the Profile node - ="040238^4013279^7901^SIMVASTATIN 80MG TAB^11543^O" is as follows:

Piece 1 – The GCNSEQNO field (#11) of the VA PRODUCT file (#50.68)

Piece 2 – The VUID field (#99.99) of the VA PRODUCT file (#50.68)

Piece 3 – The IEN from the DRUG file (#50) (For Remote orders the software will populate this with a 0)

Piece 4 – Drug Name. It will be used to populate the Descriptive Name value in FDB. The text of DRUG NAME will replace the FDB drug name in all return values that use a drug name

Piece 5 – IEN from the ORDER file (#100)

Piece 6 – Package

## Drug-Drug Interaction Output

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Drug-Drug Interaction Order Checks will be returned in the “DRUGDRUG” node of the output global.

The result of a Drug-Drug Interaction Order Check is always returned in a single set of warning for a pair of drugs.

Drug-Drug Interaction Order Checks with an FDB severity of “Contraindicated Drug Combination” will be displayed as "Critical". Drug-Drug Interaction Order Checks with an FDB severity of "Severe Interaction" will be displayed as "Significant".

A critical Drug-Drug Interaction Order Checks will be marked with a ‘C’ in the Severity subscript. A significant Drug-Drug Interaction Order Checks will be marked with an ‘S’ in the Severity subscript.

Individual Drug-Drug Interaction Order Checks with severities other than critical or significant will not be included in the output global.

It is possible that two drugs can return more than one drug-drug interaction. This can happen with combination drugs containing two or more active ingredients.

Monographs will appear in the following order in the output global. A single empty node will exist between each monograph element.

<table>
<colgroup>
<col style="width: 52%" />
<col style="width: 47%" />
</colgroup>
<thead>
<tr class="header">
<th>Professional Monograph</th>
<th>Consumer Monograph*</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Disclaimer</p>
<p>monograph title</p>
<p>severity level</p>
<p>mechanism of action</p>
<p>clinical effects</p>
<p>predisposing factors</p>
<p>patient management</p>
<p>discussion</p>
<p>references</p>
<p>FDB copyright</p></td>
<td><p>Disclaimer</p>
<p>monograph title</p>
<p>medical warning</p>
<p>how occurs</p>
<p>what might happen</p>
<p>what to do</p>
<p>references</p>
<p>FDB copyright</p></td>
</tr>
</tbody>
</table>

> \*The consumer monograph has not yet been implemented in MOCHA.

Here is an example of an Output ^TMP global for a Drug-Drug Interaction warning. Please see the details section directly after this global output for some specifics of the global:

^TMP(\$J,BASE,"OUT",0)=1

^TMP(\$J,BASE,"OUT","DRUGDRUG","C","PHENYTOIN 30MG CAP ","O;403360;PROFILE;1",1)="Z;1;PROSPECTIVE;1^1847^1655^CIMETIDINE 150MG/ML 8ML INJ^13775^O"

^TMP(\$J,BASE,"OUT","DRUGDRUG","C","PHENYTOIN 30MG CAP ","O;403360; PROFILE;1",1,"CLIN")="CLINICAL EFFECTS: Concurrent use of cimetidine or ranitidine may result in elevated levels of and toxicity from the hydantoin. Neutropenia and thrombocytopenia have been reported with concurrent cimetidine and phenytoin."

^TMP(\$J,BASE,"OUT","DRUGDRUG","C","PHENYTOIN 30MG CAP ","O;403360;PROFILE;1",1,"INT")="HYDANTOINS/CIMETIDINE; RANITIDINE"

^TMP(\$J,BASE,"OUT","DRUGDRUG","C","PHENYTOIN 30MG CAP ","O;403360; PROFILE;1",1,"PMON")=9

^TMP(\$J,BASE,"OUT","DRUGDRUG","C","PHENYTOIN 30MG CAP ","O;403360; PROFILE;1",1,"PMON",1,0)="This information is generalized and not intended as specific medical advice. Consult your healthcare professional before taking or discontinuing any drug or commencing any course of treatment."

^TMP(\$J,BASE,"OUT","DRUGDRUG","C","PHENYTOIN 30MG CAP ","O;403360; PROFILE;1",1,"PMON",2,0)=""

^TMP(\$J,BASE,"OUT","DRUGDRUG","C","PHENYTOIN 30MG CAP ","O;403360; PROFILE;1",1,"PMON",3,0)="MONOGRAPH TITLE: Hydantoins/Cimetidine; Ranitidine"

^TMP(\$J,BASE,"OUT","DRUGDRUG","C","PHENYTOIN 30MG CAP ","O;403360;PROFILE;1",1,"PMON",4,0)=""

^TMP(\$J,BASE,"OUT","DRUGDRUG","C","PHENYTOIN 30MG CAP ","O;403360; PROFILE;1",1,"PMON",5,0)="SEVERITY LEVEL: 3-Moderate Interaction: Assess the risk to the patient and take action as needed."

^TMP(\$J,BASE,"OUT","DRUGDRUG","C","PHENYTOIN 30MG CAP ","O;403360; PROFILE;1",1,"PMON",6,0)=""

^TMP(\$J,BASE,"OUT","DRUGDRUG","C","PHENYTOIN 30MG CAP ","O;403360; PROFILE;1",1,"PMON",7,0)="MECHANISM OF ACTION: The predominant mechanism appears to be inhibition of hepatic microsomal enzymes resulting in impaired hydantoin metabolism. metabolism."

^TMP(\$J,BASE,"OUT","DRUGDRUG","C","PHENYTOIN 30MG CAP ","O;403360; PROFILE;1",1,"PMON",8,0)=""

^TMP(\$J,BASE,"OUT","DRUGDRUG","C","PHENYTOIN 30MG CAP ","O;403360; PROFILE;1",1,"PMON",9,0)="CLINICAL EFFECTS: Concurrent use of cimetidine or ranitidine may result in elevated levels of and toxicity from the hydantoin. Neutropenia and thrombocytopenia have been reported with concurrent cimetidine and phenytoin.”

^TMP(\$J,BASE,"OUT","DRUGDRUG","C","PHENYTOIN 30MG CAP ","O;403360; PROFILE;1",1,"PMON",10,0)=""

^TMP(\$J,BASE,"OUT","DRUGDRUG","C","PHENYTOIN 30MG CAP ","O;403360; PROFILE;1",1,"PMON",11,0)="PREDISPOSING FACTORS: None determined."

^TMP(\$J,BASE,"OUT","DRUGDRUG","C","PHENYTOIN 30MG CAP ","O;403360; PROFILE;1",1,"PMON",12,0)=""

^TMP(\$J,BASE,"OUT","DRUGDRUG","C","PHENYTOIN 30MG CAP ","O;403360; PROFILE;1",1,"PMON",13,0)="PATIENT MANAGEMENT: Patient receiving concurrent therapy should be monitored for increased hydantoin levels and effects. A dosage adjustment may be required after initiating or discontinuing cimetidine or ranitidine. Substituting famotidine or nizatidine may be considered in patients experiencing adverse effects from the combination or to avoid the interaction."

^TMP(\$J,BASE,"OUT","DRUGDRUG","C","PHENYTOIN 30MG CAP ","O;403360; PROFILE;1",1,"PMON",14,0)=""

^TMP(\$J,BASE,"OUT","DRUGDRUG","C","PHENYTOIN 30MG CAP ","O;403360;

PROFILE;1",1,"PMON",15,0)="DISCUSSION: There are several case reports and studies documenting increases in phenytoin levels (50% or greater) during concurrent use of cimetidine (400 mg/day to 2400 mg/day).(1-11) Phenytoin toxicity occurred in some patients. The interaction often occurred in two to ten days after concurrent therapy was initiated. Neutropenia and thrombocytopenia have also been reported during concurrent phenytoin and cimetidine.(12-15)There are three case reports of elevated phenytoin levels during concurrent ranitidine therapy.(16-18) However, in a study, no alterations in phenytoin levels were seen,(19) suggesting the interaction may not occur in all patients. Studies have shown that famotidine(1) and nizatidine(20) do not interact with phenytoin."

^TMP(\$J,BASE,"OUT","DRUGDRUG","C","PHENYTOIN 30MG CAP ","O;403360; PROFILE;1",1,"PMON",16,0)=""

^TMP(\$J,BASE,"OUT","DRUGDRUG","C","PHENYTOIN 30MG CAP ","O;403360; PROFILE;1",1,"PMON",17,0)="REFERENCES:"

^TMP(\$J,BASE,"OUT","DRUGDRUG","C","PHENYTOIN 30MG CAP ","O;403360; PROFILE;1",1,"PMON",18,0)="1.Sambol NC, Upton RA, Chremos AN, Lin ET, Williams RL. A comparison of the influence of famotidine and cimetidine on phenytoin elimination and hepatic blood flow. Br J Clin Pharmacol 1989 Jan;27(1):83-7."

^TMP(\$J,BASE,"OUT","DRUGDRUG","C","PHENYTOIN 30MG CAP ","O;403360; PROFILE;1",1,"PMON",19,0)="2.Levine M, Jones MW, Sheppard I. Differential effect of cimetidine on serum concentrations of carbamazepine and phenytoin. Neurology 1985 Apr; 35(4):562-5."

^TMP(\$J,BASE,"OUT","DRUGDRUG","C","PHENYTOIN 30MG CAP ","O;403360; PROFILE;1",1,"PMON",20,0)="3.Phillips P, Hansky J. Phenytoin toxicity secondary to cimetidine administration. Med J Aust 1984 Oct 27;141(9):602."

^TMP(\$J,BASE,"OUT","DRUGDRUG","C","PHENYTOIN 30MG CAP ","O;403360; PROFILE;1",1,"PMON",21,0)="4.Iteogu MO, Murphy JE, Shleifer N, Davis R. Effect of cimetidine on single-dose phenytoin kinetics. Clin Pharm 1983 Jul-Aug;2(4):302,304."

^TMP(\$J,BASE,"OUT","DRUGDRUG","C","PHENYTOIN 30MG CAP ","O;403360; PROFILE;1",1,"PMON",22,0)="5.Salem RB, Breland BD, Mishra SK, Jordan JE. Effect of cimetidine on phenytoin serum levels. Epilepsia 1983 Jun;24(3):284-8."

^TMP(\$J,BASE,"OUT","DRUGDRUG","C","PHENYTOIN 30MG CAP ","O;403360; PROFILE;1",1,"PMON",23,0)="6.Bartle WR, Walker SE, Shapero T. Dose-dependent effect of cimetidine on phenytoin kinetics. Clin Pharmacol Ther 1983 May;33(5):649-55."

^TMP(\$J,BASE,"OUT","DRUGDRUG","C","PHENYTOIN 30MG CAP ","O;403360; PROFILE;1",1,"PMON",24,0)="7.Algozzine GJ, Stewart RB, Springer PK. Decreased clearance of phenytoin with cimetidine. Ann Intern Med 1981 Aug;95(2):244-5."

^TMP(\$J,BASE,"OUT","DRUGDRUG","C","PHENYTOIN 30MG CAP ","O;403360; PROFILE;1",1,"PMON",25,0)="8.Hetzel DJ, Bochner F, Hallpike JF, Shearman DJ, Hann CS. Cimetidine interaction with phenytoin. Br Med J (Clin Res Ed) 1981 May 9; 282(6275):1512."

^TMP(\$J,BASE,"OUT","DRUGDRUG","C","PHENYTOIN 30MG CAP ","O;403360; PROFILE;1",1,"PMON",26,0)="9.Neuvonen PJ, Tokola RA, Kaste M. Cimetidine-phenytoin interaction: effect on serum phenytoin concentration and antipyrine test. Eur J Clin Pharmacol 1981;21(3):215-20."

^TMP(\$J,BASE,"OUT","DRUGDRUG","C","PHENYTOIN 30MG CAP ","O;403360; PROFILE;1",1,"PMON",27,0)="10.Frigo GM, Lecchini S, Caravaggi M, Gatti G, Tonini M, D'Angelo L, Perucca E, Crema A. Reduction of phenytoin clearance caused by cimetidine. Eur J Clin Pharmacol 1983;25(1):135-7."

^TMP(\$J,BASE,"OUT","DRUGDRUG","C","PHENYTOIN 30MG CAP ","O;403360; PROFILE;1",1,"PMON",28,0)="11.Griffin JW Jr, May JR, DiPiro JT. Drug interactions: theory versus practice. Am J Med 1984 Nov 19;77(5B):85-9."

^TMP(\$J,BASE,"OUT","DRUGDRUG","C","PHENYTOIN 30MG CAP ","O;403360; PROFILE;1",1,"PMON",29,0)="12.Sazie E, Jaffe JP. Severe granulocytopenia with cimetidine and phenytoin. Ann Intern Med 1980 Jul;93(1):151-2."

^TMP(\$J,BASE,"OUT","DRUGDRUG","C","PHENYTOIN 30MG CAP ","O;403360; PROFILE;1",1,"PMON",30,0)="13.Arbiser JL, Goldstein AM, Gordon D. Thrombocytopenia following administration of phenytoin, dexamethasone and cimetidine: a case report and a potential mechanism. J Intern Med 1993 Jul;234(1):91-4."

^TMP(\$J,BASE,"OUT","DRUGDRUG","C","PHENYTOIN 30MG CAP ","O;403360; PROFILE;1",1,"PMON",31,0)="14.Yue CP, Mann KS, Chan KH. Severe thrombocytopenia due to combined cimetidine and phenytoin therapy. Neurosurgery 1987 Jun;20(6):963-5."

^TMP(\$J,BASE,"OUT","DRUGDRUG","C","PHENYTOIN 30MG CAP ","O;403360; PROFILE;1",1,"PMON",32,0)="15.Wong YY, Lichtor T, Brown FD. Severe thrombocytopenia associated with phenytoin and cimetidine therapy. Surg Neurol 1985 Feb;23(2):169-72."

^TMP(\$J,BASE,"OUT","DRUGDRUG","C","PHENYTOIN 30MG CAP ","O;403360; PROFILE;1",1,"PMON",33,0)="16.Tse CS, Akinwande KI, Biallowons K. Phenytoin concentration elevation subsequent to ranitidine administration. Ann Pharmacother 1993 Dec; 27(12):1448-51."

^TMP(\$J,BASE,"OUT","DRUGDRUG","C","PHENYTOIN 30MG CAP ","O;403360; PROFILE;1",1,"PMON",34,0)="17.Tse CS, Iagmin P. Phenytoin and ranitidine interaction. Ann Intern Med 1994 May 15;120(10):892-3."

^TMP(\$J,BASE,"OUT","DRUGDRUG","C","PHENYTOIN 30MG CAP ","O;403360; PROFILE;1",1,"PMON",35,0)="18.Bramhall D, Levine M. Possible interaction of ranitidine with phenytoin. Drug Intell Clin Pharm 1988 Dec;22(12):979-80."

^TMP(\$J,BASE,"OUT","DRUGDRUG","C","PHENYTOIN 30MG CAP ","O;403360 PROFILE;1",1,"PMON",36,0)="19.Watts RW, Hetzel DJ, Bochner F, Hallpike JF, Hann CS, Shearman DJ. Lack of interaction between ranitidine and phenytoin. Br J Clin Pharmacol 1983 Apr;15(4):499-500."

^TMP(\$J,BASE,"OUT","DRUGDRUG","C","PHENYTOIN 30MG CAP ","O;403360; PROFILE;1",1,"PMON",37,0)="20.Bachmann KA, Sullivan TJ, Jauregui L, Reese JH, Miller K, Levine L. Absence of an inhibitory effect of omeprazole and nizatidine on phenytoin disposition, a marker of CYP2C activity. Br J Clin Pharmacol 1993 Oct; 36(4):380-2."

^TMP(\$J,BASE,"OUT","DRUGDRUG","C","PHENYTOIN 30MG CAP ","O;403360; PROFILE;1",1,"PMON",38,0)=""

^TMP(\$J,BASE,"OUT","DRUGDRUG","C","PHENYTOIN 30MG CAP ","O;403360; PROFILE;1",1,"PMON",39,0)="Copyright 2013 First Databank, Inc."

^TMP(\$J,BASE,"OUT","DRUGDRUG","C","PHENYTOIN 30MG CAP ","O;403360; PROFILE;1",1,"SEV")="Critical"

^TMP(\$J,BASE,"OUT","DRUGDRUG","C","PHENYTOIN 30MG CAP ","O;403360; PROFILE;1",1,"SHORT")="PHENYTOIN 30MG CAP and CIMETIDINE 150MG/ML 8ML INJ may interact based on the potential interaction between HYDANTOINS and CIMETIDINE; RANITIDINE."

Details of the Drug-Drug Interaction output global:

> Top level 0 node:

> Piece 1 of this node will be set to -1 if there is a fatal error of some kind, and the Vendor database cannot be reached. Else it will be set to 0 or 1.

> Example:

> ^TMP(\$J,BASE,"OUT",0)=1

Drug-Drug Interaction Output Global:

<table style="width:100%;">
<colgroup>
<col style="width: 0%" />
<col style="width: 7%" />
<col style="width: 0%" />
<col style="width: 8%" />
<col style="width: 0%" />
<col style="width: 8%" />
<col style="width: 0%" />
<col style="width: 8%" />
<col style="width: 0%" />
<col style="width: 11%" />
<col style="width: 0%" />
<col style="width: 11%" />
<col style="width: 0%" />
<col style="width: 4%" />
<col style="width: 0%" />
<col style="width: 11%" />
<col style="width: 0%" />
<col style="width: 5%" />
<col style="width: 0%" />
<col style="width: 3%" />
<col style="width: 0%" />
<col style="width: 15%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><strong>ROOT</strong></th>
<th colspan="2"><strong>NAME<br />
SPACE</strong></th>
<th colspan="2"><strong>SUB<br />
SCRIPT</strong></th>
<th colspan="2"><strong>Severity</strong></th>
<th colspan="2"><strong>DRUG NAME</strong></th>
<th colspan="2"><strong>PHARMACY ORDER NUMBER</strong></th>
<th colspan="2"><strong>CNT</strong></th>
<th colspan="2"><strong>SUB<br />
SCRIPT</strong></th>
<th colspan="2"><strong>CNT</strong></th>
<th colspan="2"></th>
<th colspan="2"><strong>VALUE</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><p>^TMP</p>
<p>($JOB,</p>
<p>BASE</p></td>
<td colspan="2">“OUT”</td>
<td colspan="2">“DRUGDRUG”</td>
<td colspan="2">“C”</td>
<td colspan="2">“ASPIRIN"</td>
<td colspan="2">“I;A1234;PROFILE;COUNTER)”</td>
<td colspan="2">1)</td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2">=</td>
<td colspan="2">2nd Drug PhyOrderNumber ^ 2nd Drug IEN ^1st Drug IEN^2nd Drug Name^CPRS OrderNbr ^Package</td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2">“SEV”)</td>
<td colspan="2"></td>
<td colspan="2">=</td>
<td colspan="2">SEVERITY</td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2">“SHORT”)</td>
<td colspan="2"></td>
<td colspan="2">=</td>
<td colspan="2">SHORT TEXT</td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2">“INT”)</td>
<td colspan="2"></td>
<td colspan="2">=</td>
<td colspan="2">INTERACTION</td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2">“PMON”)</td>
<td colspan="2"></td>
<td colspan="2">=</td>
<td colspan="2">No. of sections in professional monograph.</td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2">1,0)</td>
<td colspan="2">=</td>
<td colspan="2">DISCLAIMER</td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2">3,0)</td>
<td colspan="2">=</td>
<td colspan="2">MONOGRAPH TITLE <em>(Note: for formatting purposes a singled empty line will be added after each piece of the monograph)</em></td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2">5,0)</td>
<td colspan="2">=</td>
<td colspan="2">SEVERITY LEVEL</td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2">7,0)</td>
<td colspan="2">=</td>
<td colspan="2">MECHANISM OF ACTION</td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2">9,0)</td>
<td colspan="2">=</td>
<td colspan="2">CLINICAL EFFECTS</td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2">11,0)</td>
<td colspan="2">=</td>
<td colspan="2">PREDISPOSING FACTORS</td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2">13,0)</td>
<td colspan="2">=</td>
<td colspan="2">PATIENT MANAGEMENT</td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2">15,0)</td>
<td colspan="2">=</td>
<td colspan="2">DISCUSSION</td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2">17:17+n,0)</td>
<td colspan="2">=</td>
<td colspan="2">REFERENCES</td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2">17+n+1.0)</td>
<td colspan="2">=</td>
<td colspan="2">COPYRIGHT</td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2">“CLIN”)</td>
<td colspan="2"></td>
<td colspan="2">=</td>
<td colspan="2">CLINICAL EFFECTS</td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2">1,0)</td>
<td colspan="2">=</td>
<td colspan="2">DISCLAIMER</td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2">3,0)</td>
<td colspan="2">=</td>
<td colspan="2">MONOGRAPH TITLE</td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2">5,0)</td>
<td colspan="2">=</td>
<td colspan="2">MEDICAL WARNING</td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2">7,0)</td>
<td colspan="2">=</td>
<td colspan="2">HOW OCCURS</td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2">9,0)</td>
<td colspan="2">=</td>
<td colspan="2">WHAT MIGHT HAPPEN</td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2">11,0)</td>
<td colspan="2">=</td>
<td colspan="2">COPYRIGHT</td>
</tr>
<tr class="odd">
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2">11,0)</td>
<td colspan="2">=</td>
<td colspan="2">WHAT TO DO</td>
</tr>
<tr class="even">
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2"></td>
<td colspan="2">13,0)</td>
<td colspan="2">=</td>
<td colspan="2">COPYRIGHT</td>
</tr>
</tbody>
</table>

## Duplicate Therapy Output

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Duplicate Therapy Order Check results are returned in a ^TMP global, grouped according to drugs involved in the result. The drugs are identified by a combination of IEN and order number. The “Class”, “Short”, and “Allow” nodes will be grouped together using a counter.

Here is an example of an Output ^TMP global for a Duplicate Therapy Order Check warning. Please see the details section directly after this global output for some specifics of the global:

> ^TMP(\$J,BASE,"OUT",0)=1

> ^TMP(\$J,BASE,"OUT","THERAPY",1,1,"ALLOW")=0

> ^TMP(\$J,BASE,"OUT","THERAPY",1,1,"CLASS")="HMGCo-A Reductase Inhibitors"

> ^TMP(\$J,BASE,"OUT","THERAPY",1,1,"SHORT")="Use of SIMVASTATIN 40MG TAB and ATORVASTATIN CA 10MG TAB may represent a duplication in therapy based on their association to the therapeutic drug class HMGCo-A Reductase Inhibitors."

> ^TMP(\$J,BASE,"OUT","THERAPY",1,"DRUGS",1)="Z;1;PROSPECTIVE;1^7902^SIMVASTATIN 40MG TAB^^"

> ^TMP(\$J,BASE,"OUT","THERAPY",1,"DRUGS",2)="O;403361;PROFILE;1^218^ATORVASTATIN CA 10MG TAB^12183^O"

Duplicate Therapy Output Global:

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 9%" />
<col style="width: 11%" />
<col style="width: 5%" />
<col style="width: 9%" />
<col style="width: 9%" />
<col style="width: 4%" />
<col style="width: 34%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>ROOT</strong></th>
<th><strong>NAME<br />
SPACE</strong></th>
<th><strong>SUB<br />
SCRIPT</strong></th>
<th><strong>Cnt</strong></th>
<th><strong>SUB<br />
SCRIPT</strong></th>
<th><strong>SUB<br />
SCRIPT</strong></th>
<th></th>
<th><strong>VALUE</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>^TMP($JOB,BASE,</td>
<td>OUT</td>
<td>THERAPY</td>
<td>1</td>
<td>DRUGS</td>
<td>1</td>
<td>=</td>
<td>PharmacyOrderNumber ^ Drug IEN ^ Drug Name ^ CPRS Order Number ^ Package</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td>1</td>
<td>DRUGS</td>
<td>2</td>
<td>=</td>
<td>PharmacyOrderNumber ^ Drug IEN ^ Drug Name ^ CPRS Order Number ^ Package</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td>1</td>
<td>DRUGS</td>
<td>(N+1)</td>
<td>=</td>
<td>PharmacyOrderNumber ^ Drug IEN ^ Drug Name ^ CPRS Order Number ^ Package</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td>1</td>
<td>1</td>
<td>ALLOW</td>
<td>=</td>
<td>DUPLICATE ALLOWANCE</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td>1</td>
<td>1</td>
<td>CLASS</td>
<td>=</td>
<td>CLASS</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td>1</td>
<td>1</td>
<td>SHORT</td>
<td>=</td>
<td>SHORT TEXT</td>
</tr>
</tbody>
</table>

# Drug-Drug Interaction/Duplicate Therapy Exception Handling

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Exceptions originate from three sources: VistA application, VistA Interface, or the FDB server. Regardless of the error’s origin, the VistA interface code creates and formats the exception message for the calling application to display.

Prior to calling FDB for Drug-Drug Interaction and Duplicate Therapy Order Checks, the application code may come across invalid drug data that will prevent the medication from being included in any drug checks. To provide a common interface, the application can pass error codes and information to the interface to generate standard warning messages. These error codes, error messages, and error reasons are shown below. As of the release of MOCHA v2.0, only two error codes were being used, error codes 1 and 4.

- Error code 1 is used when there is no Active Dispense Drug found for the order.
- Error code 4 is used when no Active IV Additive/Solution marked for IV Fluid order entry could be found.

For these two input errors, the input global will have the following format:

^TMP\$J,”BASE”,”IN”,”EXCEPTIONS”,”OI”,DRUG NAME)=Error code^Pharmacy Order Number

> Example:

^TMP(\$J,BASE,"IN","EXCEPTIONS","OI","HYDROXYCHLOROQUINE TAB")="1^P;599;PROFILE;15"

| Note:                                                                                                      | In the above example, the drug name is actually the Name and Dosage Form from the PHARMACY ORDERABLE ITEM file (#50.7) since that is what is normally used as a drug name when there is no entry from the DRUG file (#50) available. |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](vista-to-mocha-version-2-interface-document/005.png) |                                                                                                                                                                                                                                      |

The resulting exception message that is returned to the calling application looks like this:

^TMP(\$J,BASE,"OUT","EXCEPTIONS","P;599;PROFILE;15",1)="^^^^^^Enhanced Order Checks cannot be performed for Orderable Item: HYDROXYCHLOROQUINE TAB^^^ No Dispense Drug found."

In the above example, the fifth subscript is the Pharmacy Order Number and the sixth subscript is a counter. Piece 7 is the Error Message and piece 10 is the reason text.

The subscripts of all exceptions messages for Drug-Drug Interaction and Duplicate Therapy Order Checks are formatted in VistA this same way, regardless of the exception origin. The data pieces are also consistent, though for certain exceptions some may have more data than others. In the above example, only data pieces 7 and 10 were populated. In this example for a drug that is not matched to National Drug File, you can see that more data is populated:

^TMP(\$J,BASE,"OUT","EXCEPTIONS","O;402237;PROFILE;3",1)="^0^2977^CAPTOPRIL 25MG TABS^11461^O^Enhanced Order Checks cannot be performed for Local Drug: CAPTOPRIL 25MG TABS^^DOSE,CDEV^Drug not matched to NDF"

The data pieces are as follows:

> Piece 1 – GCNSEQNO

> Piece 2 – VUID

> Piece 3 – DRUG file (#50) IEN

> Piece 4 – Drug Name

> Piece 5 – CPRS Order Number

> Piece 6 – Package

> Piece 7 – Error Message

> Piece 8 – Reason Code

> Piece 9 – Source

> Piece 10 – Reason Text

Pieces 7 and 10 are the key elements of data to display to the user. Piece 7 will always be populated, as in the above example, but piece 10 may or may not be populated.

An example when piece 10 would not be populated is when the DRUG file (#50) entry is matched to National Drug File, and a GCNSEQNO field (#11) is populated in the matched VA PRODUCT file (#50.68) entry, but that particular GCNSEQNO field (#11) cannot be checked in FDB. In that case, the following global is returned to the calling application, and in this case, piece 7 should be displayed to the user and note that piece 10 is null:

^TMP(\$J,BASE,"OUT","EXCEPTIONS","O;403362;PROFILE;2",1)="999999^4004156^1491^GRISEOFULVIN 500MG S.T.^13778^O^Order Checks could not be done for Drug: GRISEOFULVIN 500MG S.T., please complete a manual check for Drug Interactions and Duplicate Therapy.^^PEPS^"