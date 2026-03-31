---
title: Appendix - IEMM Error Table
doc_type: APX
doc_label: Appendix
doc_layer: plain
doc_subject: IEMM Error Table
app_code: ACR
app_name: Ambulatory Care Reporting
section: CLI
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 0
description: "<table> <colgroup> <col style=\\"width: 4%\\" /> <col style=\\"width: 5%\\" /> <col style=\\"width: 25%\\" /> <col style=\\"width: 16%\\" /> <col style=\\"width: 15%\\" /> <col style=\\"width: 16%\\" /> <col style=\\"width: 15%\\" /> </colgroup> <tbody> <tr class=\\"odd\\"> <td colspan=\\"2\\">Error</td> <td></td> <td></td> <td></td> "
audience: 
keywords: 
  - class
  - patient
  - colspan
  - through
  - invalid
  - protocol
  - style
  - width
  - edit
  - load
page_count: 0
word_count: 4679
section_count: 0
table_count: 12
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Ambulatory_Care_Reporting/acr_p_um_appx.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Ambulatory_Care_Reporting/acr_p_um_appx.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=116"
---

<table>
<colgroup>
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 25%" />
<col style="width: 16%" />
<col style="width: 15%" />
<col style="width: 16%" />
<col style="width: 15%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2">Error</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>NPCD</td>
<td>VISTA</td>
<td>Error Description</td>
<td colspan="2">Correction Description</td>
<td>Correction Logic</td>
<td>Validation Logic</td>
</tr>
<tr class="odd">
<td>100</td>
<td>1000</td>
<td>Event type in EVN Segment is invalid.</td>
<td colspan="2">There was a problem with the HL7 EVN Segment. This entry will be reflagged for transmission.</td>
<td>Entry will be reflagged</td>
<td>The segment must be EVN and equal to A08 or A23.</td>
</tr>
<tr class="even">
<td>105</td>
<td>1050</td>
<td>Event date is missing, invalid, after processing date, or after closeout.</td>
<td colspan="2">There was a problem with the HL7 EVN Segment date. This entry will be reflagged for transmission.</td>
<td>Entry will be reflagged</td>
<td>Ensure that the date is a valid date after 10/9/96.</td>
</tr>
<tr class="odd">
<td>106</td>
<td></td>
<td>Event time is invalid.</td>
<td colspan="2">There was a problem with the HL7 EVN Segment time. This entry will be reflagged for transmission.</td>
<td>Entry will be reflagged</td>
<td>This is also performed as part of 105/1050.</td>
</tr>
<tr class="even">
<td>200</td>
<td>2000</td>
<td>Patient name missing or invalid.</td>
<td colspan="2">Correct patient name through Load/Edit Patient Data protocol, Screen 1, Group 1.</td>
<td>Patient Load Edit</td>
<td><p>Name must:</p>
<p>-Not be all numbers</p>
<p>-Exist</p>
<p>-Not be blank or null</p>
<p>-Not have any control characters</p></td>
</tr>
<tr class="odd">
<td>203</td>
<td>2030</td>
<td>Patient ID (internal) is missing or not numeric.</td>
<td colspan="2">Reflag this entry for retransmission. If the error still occurs, you may need to delete and re-enter the check out.</td>
<td>Entry will be reflagged</td>
<td><p>ID must:</p>
<p>-Exist</p>
<p>-Not be null or zero</p>
<p>-Be numeric</p></td>
</tr>
<tr class="even">
<td>205</td>
<td>2050</td>
<td>Date of birth is missing, or invalid date, or after the date of encounter.</td>
<td colspan="2">Correct date of birth (DOB) through Load/Edit Patient Data protocol, Screen 1, Group 1.</td>
<td>Patient Load Edit</td>
<td>Must be a valid date before the encounter date and time.</td>
</tr>
<tr class="odd">
<td>210</td>
<td>2100</td>
<td>Sex code is missing or an invalid code.</td>
<td colspan="2">Correct the patient's sex code through the Patient Demographics protocol.</td>
<td>Patient Demographics</td>
<td>The code must be F, M, U, or O.</td>
</tr>
<tr class="even">
<td>215</td>
<td>2150</td>
<td>Race code missing or invalid.</td>
<td colspan="2">Correct the patient's race code through the Patient Demographics protocol of IEMM.</td>
<td>Patient Demographics (IEMM only)</td>
<td>Must be a valid code from the RACE file or not defined.</td>
</tr>
<tr class="odd">
<td>220</td>
<td>2200</td>
<td>Address line 1 is invalid.</td>
<td colspan="2">Correct the address - line 1 through the Patient Demographics protocol.</td>
<td>Patient Demographics</td>
<td>Cannot be all numeric, may be blank.</td>
</tr>
<tr class="even">
<td>221</td>
<td>2210</td>
<td>Address line 2 is invalid.</td>
<td colspan="2">Correct the address - line 2 through the Patient Demographics protocol.</td>
<td>Patient Demographics</td>
<td>Cannot be all numeric, may be blank.</td>
</tr>
<tr class="odd">
<td>222</td>
<td>2220</td>
<td>City is missing or invalid.</td>
<td colspan="2">Correct the city name through the Patient Demographics protocol.</td>
<td>Patient Demographics</td>
<td><p>Cannot be blank.</p>
<p>Cannot be all numeric.</p></td>
</tr>
<tr class="even">
<td>223</td>
<td>2230</td>
<td>State code is missing or invalid.</td>
<td colspan="2">Correct the state through the Patient Demographics protocol.</td>
<td>Patient Demographics</td>
<td><p>Cannot be blank.</p>
<p>Must be a valid entry in the STATE file.</p></td>
</tr>
<tr class="odd">
<td>224</td>
<td>2240</td>
<td>Zip code is missing or invalid.</td>
<td colspan="2">Correct the zip code though the Patient Demographics protocol.</td>
<td>Patient Demographics</td>
<td><p>Cannot be all zeros.</p>
<p>Must be 5 numbers <strong>or</strong> “5 numbers-4 numbers”.</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 25%" />
<col style="width: 16%" />
<col style="width: 15%" />
<col style="width: 16%" />
<col style="width: 15%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2">Error</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>NPCD</td>
<td>VISTA</td>
<td>Error Description</td>
<td colspan="2">Correction Description</td>
<td>Correction Logic</td>
<td>Validation Logic</td>
</tr>
<tr class="odd">
<td>225</td>
<td>2250</td>
<td>County code is invalid.</td>
<td colspan="2">Correct the county code through the Patient Demographics protocol.</td>
<td>Patient Demographics</td>
<td><p>Must not be blank.</p>
<p>County must exist for the given state.</p></td>
</tr>
<tr class="even">
<td>226</td>
<td>2260</td>
<td>Inactive state/county code.</td>
<td colspan="2">Correct the state/county codes through the Patient Demographics protocol.</td>
<td>Patient Demographics</td>
<td>This information is checked as part of state and county checks. No additional validation logic was entered.</td>
</tr>
<tr class="odd">
<td>230</td>
<td>2300</td>
<td>Marital status is invalid.</td>
<td colspan="2">Correct the patient's marital status through the Patient Demographics protocol.</td>
<td>Patient Demographics</td>
<td>Code must be A, D, M, S, W, or U.</td>
</tr>
<tr class="even">
<td>233</td>
<td>2330</td>
<td>Religion code is invalid.</td>
<td colspan="2">Correct the patient's religion code through the Patient Demographics protocol.</td>
<td>Patient Demographics</td>
<td><p>Must not be blank.</p>
<p>Must exist in the RELIGION file.</p></td>
</tr>
<tr class="odd">
<td>235</td>
<td></td>
<td>Pseudo SSN is not P or blank.</td>
<td colspan="2">Correct the SSN through the Load/Edit Patient Data protocol, Screen 1, Group 1.</td>
<td>Patient Load Edit</td>
<td>This is performed as part of 236/2360.</td>
</tr>
<tr class="even">
<td>236</td>
<td>2360</td>
<td>SSN is missing or invalid.</td>
<td colspan="2">Correct the SSN through the Load/Edit Patient Data protocol, Screen 1, Group 1.</td>
<td>Patient Load Edit</td>
<td><p>Must contain 9 numerics.</p>
<p>The Pseudo indicator must be P.</p></td>
</tr>
<tr class="odd">
<td>237</td>
<td>2370</td>
<td>Date of death is before the encounter date.</td>
<td colspan="2">If the date of death is in error, correct through the Death Entry option (security key required). If the encounter date is in error, the encounter will need to be deleted and remade.</td>
<td>Display Message – “Date of Death must be corrected through Death Entry Option.”</td>
<td>Must be a valid date after the encounter date.</td>
</tr>
<tr class="even">
<td>238</td>
<td><span dir="rtl">2380</span></td>
<td>Ethnicity code missing or invalid.</td>
<td colspan="2">Correct the patient's ethnicity code through the Patient Demographics protocol of IEMM.</td>
<td>Patient Demographics</td>
<td>Must be a valid entry in the ETHNICITY file (10.2).</td>
</tr>
<tr class="odd">
<td>240</td>
<td>2400</td>
<td>Conf. Address - Line 1 contains all numbers</td>
<td colspan="2">Correct the Confidential Address - Line 1 through the Patient Demographics protocol.</td>
<td>Patient Demographics</td>
<td>Cannot be all numeric, may be blank.</td>
</tr>
<tr class="even">
<td>241</td>
<td>2410</td>
<td>Conf. Address - Line 2 contains all numbers.</td>
<td colspan="2">Correct the Confidential Address - Line 2 through the Patient Demographics protocol.</td>
<td>Patient Demographics</td>
<td>Cannot be all numeric, may be blank.</td>
</tr>
<tr class="odd">
<td>242</td>
<td>2420</td>
<td>Conf. Address City is missing or invalid.</td>
<td colspan="2">Correct the Confidential City name through the Patient Demographics protocol.</td>
<td>Patient Demographics</td>
<td>Cannot be all blank. Cannot be all numeric.</td>
</tr>
<tr class="even">
<td>243</td>
<td>2430</td>
<td>Conf. Address State code is missing or invalid.</td>
<td colspan="2">Correct the Confidential State through the Patient Demographics protocol.</td>
<td>Patient Demographics</td>
<td>Cannot be blank. Must be a valid entry in the STATE file.</td>
</tr>
</tbody>
</table>

|       |       |                                                                                 |                                                                                                                                                                                              |     |                                                                                                                                                                   |                                                                                                             |
|-------|-------|---------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------|
| Error |       |                                                                                 |                                                                                                                                                                                              |     |                                                                                                                                                                   |                                                                                                             |
| NPCD  | VISTA | Error Description                                                               | Correction Description                                                                                                                                                                       |     | Correction Logic                                                                                                                                                  | Validation Logic                                                                                            |
| 244   | 2440  | Conf. Address zip code is missing or invalid.                                   | Correct the Confidential Zip Code through the Patient Demographics protocol.                                                                                                                 |     | Patient Demographics                                                                                                                                              | Cannot be all zeroes. Must be 5 numbers or "5 numbers-4 numbers"                                        |
| 245   | 2450  | Conf. Address County code is invalid.                                           | Correct the Confidential County Code through the Patient Demographics protocol.                                                                                                              |     | Patient Demographics                                                                                                                                              | Must not be blank. County must exist for the given state.                                                   |
| 246   |       | Conf. Address Inactive State/County Code                                        | Correct the Confidential State/County codes through the Patient Demographics protocol.                                                                                                       |     | Patient Demographics                                                                                                                                              | This information is checked as part of state and county checks. No additional validation logic was entered. |
| 247   | 2470  | Conf. Address Category is missing or invalid.                                   | Correct the Confidential Address Category through the Patient Demographics protocol.                                                                                                         |     | Patient Demographics                                                                                                                                              | Must be 1 numeric character. Cannot be zero or blank.                                                       |
| 248   | 2480  | Conf. Address Start Date is missing or the Start/End Dates are invalid.         | Correct the Confidential Address Start and Stop dates through the Patient Demographics protocol.                                                                                             |     | Patient Demographics                                                                                                                                              | Must be a valid date.                                                                                       |
| 300   | 3000  | Date of death is invalid.                                                       | If the date of death is in error, correct through the Death Entry option (security key required).                                                                                            |     | Display Message – “Date of Death must be corrected through Death Entry Option.”                                                                                   | Must be a valid date.                                                                                       |
| 303   |       | For DSS Identifier 108, date of death cannot be more than 14 days before admit. | Please note this error and report it to your supervisor for review. This error cannot be “corrected” through IEMM.                                                                           |     | Display Message – “Contact your MAS ADPAC for assistance.”                                                                                                        | No current check for this.                                                                                  |
|       | 3030  | The encounter date is greater than 14 days after the date of death.             | If Date of Death is invalid, correct through the Death Entry Option (Security Key required). If this LAB encounter is 14 after the date of death, it can not be counted for workload credit. |     | Display Message - "Correct Date of Death through the Death Entry option, or if this LAB encounter is 14 days after the Date of Death no workload credit allowed." |                                                                                                             |
| 305   |       | This person was previously reported as dead by a VAMC.                          | This patient has been reported dead by another facility. The reporting facility will be determined from the NPCD and contacted for additional information.                                   |     | Display Message – “This patient has been reported dead by another facility. Contact the NPCD for additional Information.”                                         | No current check for this.                                                                                  |
| 310   | 3100  | Homeless indicator is invalid.                                                  | The homeless indicator is set through the Social Work Information Management System (SWIMS). Contact the appropriate personnel to correct this indicator.                                    |     | Display Message – “Contact Social Work. This indicator is set through SWIMS.”                                                                                     | Must be a zero or one.                                                                                      |

<table>
<colgroup>
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 25%" />
<col style="width: 16%" />
<col style="width: 15%" />
<col style="width: 16%" />
<col style="width: 15%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2">Error</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>NPCD</td>
<td>VISTA</td>
<td>Error Description</td>
<td colspan="2">Correction Description</td>
<td>Correction Logic</td>
<td>Validation Logic</td>
</tr>
<tr class="odd">
<td>315</td>
<td>3150</td>
<td>POW status is invalid.</td>
<td colspan="2">Correct POW status through the Load/Edit Patient Data protocol, Screen 6, Group 2.</td>
<td>Patient Load Edit</td>
<td>Must be N, U, Y or blank.</td>
</tr>
<tr class="even">
<td>320</td>
<td>3200</td>
<td>Type of insurance code is invalid.</td>
<td colspan="2">Contact MCCR to correct this problem.</td>
<td>Display Message – “Contact MCCR to correct this error.”</td>
<td><p>Can be blank.</p>
<p>If a code, it must be a number 0-12.</p></td>
</tr>
<tr class="odd">
<td>322</td>
<td>3220</td>
<td>Type of insurance is inactive.</td>
<td colspan="2">Contact MCCR to correct this problem.</td>
<td>Display Message - “Contact MCCR to correct this error.”</td>
<td>Insurance type in VISTA does not have an active/inactive flag. No validation logic was needed.</td>
</tr>
<tr class="even">
<td>325</td>
<td></td>
<td>Prisoner of War Location is invalid.</td>
<td colspan="2">Review current entry through the Load/Edit Patient Data protocol, Screen 6, Group 2.</td>
<td>Patient Load Edit</td>
<td>Must be a valid location contained in the POW Period file (#22).</td>
</tr>
<tr class="odd">
<td></td>
<td>3250</td>
<td>Prisoner of War Location is invalid or inconsistent with POW status.</td>
<td colspan="2">Review current entry through the Load/Edit Patient Data protocol, Screen 6, Group 2.</td>
<td>Patient Load Edit</td>
<td>Must be a valid location contained in the POW Period file (#22).</td>
</tr>
<tr class="even">
<td>326</td>
<td></td>
<td>Prisoner of War Location is inactive.</td>
<td colspan="2">Review current entry through the Load/Edit Patient Data protocol, Screen 6, Group 2.</td>
<td>Patient Load Edit</td>
<td>Must be a valid location contained in the POW Period file (#22).</td>
</tr>
<tr class="odd">
<td>328</td>
<td></td>
<td>Prisoner of War Location inconsistent with POW status.</td>
<td colspan="2">Review current entries through the Load/Edit Patient Data protocol, Screen 6, Group 2.</td>
<td>Patient Load Edit</td>
<td>POW Status must equal Yes.</td>
</tr>
<tr class="even">
<td>340</td>
<td>3400</td>
<td>Emergency Response Indicator to identify patients impacted by the COVID-19 Pandemic is invalid.</td>
<td colspan="2">Review current entries through the Load/Edit Patient Data protocol, Screen 2, Group 5.</td>
<td>Patient Load Edit</td>
<td>Emergency Response Indicator must equal “P”.</td>
</tr>
<tr class="odd">
<td>400</td>
<td>4000</td>
<td>Patient class is missing or invalid.</td>
<td colspan="2">This value is currently set as a default by the software. Reflag this entry for transmission.</td>
<td>Entry will be reflagged</td>
<td>Must be O for outpatient.</td>
</tr>
<tr class="even">
<td>405</td>
<td>4050</td>
<td>Purpose of visit or appointment type is missing or invalid.</td>
<td colspan="2">This field is a combination of the purpose of visit and the appointment type; therefore, correction is a two step process. The purpose of visit is set by the appointment management software and cannot be manually changed. If this field is in error, the appointment will need to be deleted and remade. The appointment type can be corrected through the Encounter Information protocol.</td>
<td>Edit Encounter Option</td>
<td><p>Must be a purpose of visit of C&amp;P, 10-10, Scheduled or Unscheduled.</p>
<p>A valid appointment type is also checked for at this point.</p></td>
</tr>
<tr class="odd">
<td>406</td>
<td>4060</td>
<td>Inactive purpose of visit or appointment type.</td>
<td colspan="2">This field is a combination of the purpose of visit and the appointment type; therefore, correction is a two step process. The purpose of visit is set by the appointment management software and cannot be manually changed. If this field is in error, the appointment will need to be deleted and remade. The appointment type can be corrected through the Encounter Information protocol.</td>
<td>Edit Encounter Option</td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 25%" />
<col style="width: 16%" />
<col style="width: 15%" />
<col style="width: 16%" />
<col style="width: 15%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2">Error</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>NPCD</td>
<td>VISTA</td>
<td>Error Description</td>
<td colspan="2">Correction Description</td>
<td>Correction Logic</td>
<td>Validation Logic</td>
</tr>
<tr class="odd">
<td>407</td>
<td>4070</td>
<td>Location of visit is missing or invalid.</td>
<td colspan="2">This entry is a function of the clinic set-up parameter, CLINIC MEETS AT THIS FACILITY. This parameter must be answered.</td>
<td>Display Message – “There may be a problem with the Clinic Set-up. Contact your MAS ADPAC.”</td>
<td>Must be a one for this facility or a six for other facility.</td>
</tr>
<tr class="even">
<td>410</td>
<td>4100</td>
<td>Unique visit ID in PCE is missing or invalid.</td>
<td colspan="2">Patch SD*5.3*103 exported a routine call to relink the outpatient encounter to the visit entry. Contact your MAS ADPAC about running this routine.</td>
<td>Display Message – “Contact your MAS ADPAC”.</td>
<td>Must be defined, and a number greater than zero.</td>
</tr>
<tr class="odd">
<td>415</td>
<td>4150</td>
<td>Facility station number is missing or invalid.</td>
<td colspan="2">This error cannot be corrected through IEMM. It needs to be corrected in the STATION NUMBER (TIME SENSITIVE) file.</td>
<td>Display Message – “Contact your MAS ADPAC”.</td>
<td>Must be a valid station number.</td>
</tr>
<tr class="even">
<td>416</td>
<td>4160</td>
<td>This indicates that the facility number is no longer active.</td>
<td colspan="2">This error cannot be corrected through IEMM. It needs to be corrected in the STATION NUMBER (TIME SENSITIVE) file.</td>
<td>Display Message – “Use View Expanded for more details”.</td>
<td>Check to ensure that the facility is active at the time of the encounter.</td>
</tr>
<tr class="odd">
<td>420</td>
<td></td>
<td>Date of encounter is invalid, after date of transmission, or after closeout.</td>
<td colspan="2">If the encounter date is invalid, or before the date of transmission, the appointment will need to be canceled and remade through the Appointment Manager.</td>
<td>Display Message – “Use Appointment Management to delete this checkout and reenter.”</td>
<td>Same check performed as 4200.</td>
</tr>
<tr class="even">
<td></td>
<td>4200</td>
<td>Encounter date/time is missing or invalid.</td>
<td colspan="2">If the encounter is after the database closeout, it cannot be sent to Austin. If the encounter date is invalid, or before the date of transmission, the appointment will need to be canceled and remade through the Appointment Manager.</td>
<td>Display Message – “Use Appointment Management to delete this checkout and reenter or contact your ADPAC.”</td>
<td><p>Must be a valid date.</p>
<p>Also checked to see if this encounter is still ok to transmit workload and database close out.</p></td>
</tr>
<tr class="odd">
<td>421</td>
<td></td>
<td>Time of encounter is invalid.</td>
<td colspan="2">To correct the time of encounter, the appointment will need to be canceled and remade through the Appointment Manager.</td>
<td>Display Message – “Use Appointment Management to delete this checkout and reenter.”</td>
<td>Same check performed as 4200.</td>
</tr>
<tr class="even">
<td>500</td>
<td>5000</td>
<td>Diagnosis code (ICD) is missing or invalid.</td>
<td colspan="2">Correct diagnosis code through the Check Out protocol.</td>
<td>Checkout Interview</td>
<td>Must be a valid diagnostic code in the ICD DIAGNOSIS file.</td>
</tr>
<tr class="odd">
<td>502</td>
<td>5020</td>
<td>Inactive diagnosis code.</td>
<td colspan="2">Correct the diagnosis code through the Check Out protocol.</td>
<td>Checkout Interview</td>
<td>This information is already checked as part of the 5000 error code. At this point no additional validation has been entered.</td>
</tr>
<tr class="even">
<td>503</td>
<td>5030</td>
<td>Diagnosis coding method is missing or invalid.</td>
<td colspan="2">Currently, this value is a default in the software. If this value is incorrect, an error occurred during the build of the HL7 segment. Reflag for transmission</td>
<td>Entry will be reflagged</td>
<td>Must be I9 or I10.</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 25%" />
<col style="width: 16%" />
<col style="width: 15%" />
<col style="width: 16%" />
<col style="width: 15%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2">Error</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>NPCD</td>
<td>VISTA</td>
<td>Error Description</td>
<td colspan="2">Correction Description</td>
<td>Correction Logic</td>
<td>Validation Logic</td>
</tr>
<tr class="odd">
<td>510</td>
<td>5100</td>
<td>Diagnosis priority is invalid.</td>
<td colspan="2">Correct diagnosis code through the Check Out protocol. It may be necessary to compare what is in Scheduling using the Expand Encounter protocol to what is in PCE using either Check Out or any of the PCE menu options.</td>
<td>Checkout Interview</td>
<td>Must be a one for primary diagnosis or blank if not. Cannot have more than one diagnosis marked as primary.</td>
</tr>
<tr class="even">
<td>515</td>
<td>5150</td>
<td>Sequential number (Set ID) in DG1 Segment is invalid.</td>
<td colspan="2">There was a problem with the HL7 DG1 Segment. This entry should be reflagged for transmission.</td>
<td>Entry will be reflagged</td>
<td></td>
</tr>
<tr class="odd">
<td>600</td>
<td>6000</td>
<td>Procedure coding method is missing or invalid.</td>
<td colspan="2">Currently, this value is a default in the software. If this value is incorrect, an error occurred during the build of the HL7 segment. Reflag for transmission.</td>
<td>Entry will be reflagged</td>
<td>Must be a valid ICPT code.</td>
</tr>
<tr class="even">
<td>605</td>
<td>6050</td>
<td>CPT procedure code is missing or invalid.</td>
<td colspan="2"><p>Correct procedure coding through the Check Out</p>
<p>protocol.</p></td>
<td>Checkout Interview</td>
<td></td>
</tr>
<tr class="odd">
<td>607</td>
<td></td>
<td>Inactive procedure code.</td>
<td colspan="2">Correct procedure coding through the Check Out protocol.</td>
<td>Checkout Interview</td>
<td></td>
</tr>
<tr class="even">
<td>610</td>
<td></td>
<td>Not used at this time.</td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>612</td>
<td></td>
<td>Not used at this time.</td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>620</td>
<td>6200</td>
<td>Provider/practitioner type code is missing or invalid.</td>
<td colspan="2">This problem can be caused by 1) no person class has been designated for the provider or 2) the person class is inactive for the provider. This needs to be referred to the person that is responsible for designating person class for providers.</td>
<td>Display Message – “Contact your MAS ADPAC.”</td>
<td>There must be a valid person class for the provider.</td>
</tr>
<tr class="odd">
<td>622</td>
<td></td>
<td>Inactive procedure practitioner code.</td>
<td colspan="2">The person class is inactive for the provider. This needs to be referred to the person that is responsible for designating person class for providers.</td>
<td>Display Message - “Contact the person responsible for a provider’s person class.”</td>
<td></td>
</tr>
<tr class="even">
<td>625</td>
<td>6250</td>
<td>Sequential number (Set ID) in PR1 Segment is invalid.</td>
<td colspan="2">There was a problem with the HL7 PR1 Segment. This entry should be reflagged for transmission.</td>
<td>Entry will be reflagged</td>
<td></td>
</tr>
<tr class="odd">
<td>630</td>
<td>6300</td>
<td>CPT modifier invalid.</td>
<td colspan="2">Correct modifier through the Check Out protocol.</td>
<td>Checkout Interview</td>
<td>Must be a valid CPT Modifier in the CPT Modifier file.</td>
</tr>
<tr class="even">
<td>635</td>
<td></td>
<td>CPT procedure and modifier combination invalid.</td>
<td colspan="2">Correct procedure/modifier combination through the Check Out protocol.</td>
<td>Checkout Interview</td>
<td>Must be a valid ICPT code that is identified in the allowable ICPT range in the CPT Modifier file.</td>
</tr>
<tr class="odd">
<td>637</td>
<td>6370</td>
<td>CPT modifier coding method is missing or invalid.</td>
<td colspan="2">This value is calculated by the ACRP software. If it is incorrect, an error occurred during the build of the HL7 segment. Reflag for transmission.</td>
<td>Entry will be reflagged.</td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 25%" />
<col style="width: 16%" />
<col style="width: 15%" />
<col style="width: 16%" />
<col style="width: 15%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2">Error</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>NPCD</td>
<td>VISTA</td>
<td>Error Description</td>
<td colspan="2">Correction Description</td>
<td>Correction Logic</td>
<td>Validation Logic</td>
</tr>
<tr class="odd">
<td>700</td>
<td>7000</td>
<td>Encounter eligibility code missing or invalid.</td>
<td colspan="2">Correct the encounter eligibility code through the Encounter Information protocol.</td>
<td>Patient Load Edit</td>
<td>Must be a valid eligibility code.</td>
</tr>
<tr class="even">
<td>702</td>
<td>7020</td>
<td>Encounter eligibility code inconsistent with veteran status.</td>
<td colspan="2">If the veteran status is incorrect, change the status through the Load/Edit Patient Data protocol, Screen 7, Group 1. If the encounter eligibility is incorrect, correct through the Encounter Information protocol.</td>
<td>Patient Load Edit</td>
<td><p>If veteran status is YES, than eligibility must be</p>
<p>1-5, 15-18.</p>
<p>If veteran status is NO, than eligibility must be</p>
<p>6-10, 12-14 or 19.</p></td>
</tr>
<tr class="odd">
<td>703</td>
<td>7030</td>
<td>Encounter eligibility code inactive.</td>
<td colspan="2">Correction is made through the Load/Edit Patient Data protocol. An active eligibility code needs to be designated. In addition, the eligibility code will have to be updated using the Encounter information protocol.</td>
<td>Display Message – “Use View Expanded for more details.”</td>
<td>Eligibility code must be active.</td>
</tr>
<tr class="even">
<td>704</td>
<td>7040</td>
<td>MST Status Invalid</td>
<td colspan="2">Valid MST Statuses are Y,N,U,D and a blank.</td>
<td>Patient Load Edit</td>
<td>Veteran status must be YES.</td>
</tr>
<tr class="odd">
<td>705</td>
<td>7050</td>
<td>Veteran status is missing or invalid.</td>
<td colspan="2">Correct veteran status through Load/Edit Patient Data protocol, Screen 7, Group 1.</td>
<td>Patient Load Edit</td>
<td>Veteran status must be filled in.</td>
</tr>
<tr class="even">
<td>706</td>
<td>7060</td>
<td>MST status date invalid or inconsistent with MST status.</td>
<td colspan="2">Date in incorrect format or a date appears with an MST status of a blank.</td>
<td>Patient Load Edit</td>
<td>MST Status must equal YES and must be a valid date.</td>
</tr>
<tr class="odd">
<td>710</td>
<td>7100</td>
<td>Veteran status inconsistent with POW status.</td>
<td colspan="2">Review current entries through the Load/Edit Patient Data protocol, Screens 6 and 7.</td>
<td>Patient Load Edit</td>
<td>If veteran status is YES, POW can be YES, NO, UNKNOWN, or blank.</td>
</tr>
<tr class="even">
<td>712</td>
<td>7120</td>
<td>Agent Orange exposure claimed by incompatible patient.</td>
<td colspan="2">Exposure to Agent Orange can only be claimed by veteran patients that have a period of service of Vietnam era. Review patient information through Load/Edit Patient Data protocol, Screen 6, Group 5 and Screen 7, Group 3.</td>
<td>Patient Load Edit</td>
<td>Patients can only claim exposure to Agent Orange if they’re a veteran and have a period of service of Vietnam era.</td>
</tr>
<tr class="odd">
<td>713</td>
<td>7130</td>
<td>Agent Orange Exposure Location invalid/missing.</td>
<td colspan="2">Agent Orange Exposure Location must have a valid value if the patient claims exposure to Agent Orange. If the patient does not claim exposure, location should not have a value. Review patient information through Load/Edit Patient Data protocol, Screen 6, Group 5.</td>
<td>Patient Load Edit</td>
<td>Agent Orange Exposure Location must have a value of V, K or "". If patient claims exposure to Agent Orange, Agent Orange Exposure Location must have a value of V or K.</td>
</tr>
<tr class="even">
<td>715</td>
<td>7150</td>
<td>Radiation Exposure Method is invalid or inactive.</td>
<td colspan="2">Review current entry through the Load/Edit Patient Data protocol, Screen 6, Group 6.</td>
<td>Patient Load Edit</td>
<td>Must be a code of N, T or B.</td>
</tr>
</tbody>
</table>

|       |       |                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                          |     |                   |                                                                                            |
|-------|-------|-----------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-------------------|--------------------------------------------------------------------------------------------|
| Error |       |                                                                 |                                                                                                                                                                                                                                                                                                                                                                                                          |     |                   |                                                                                            |
| NPCD  | VISTA | Error Description                                               | Correction Description                                                                                                                                                                                                                                                                                                                                                                                   |     | Correction Logic  | Validation Logic                                                                           |
| 717   |       | Radiation Exposure Method inconsistent with radiation exposure. | Review current entries through the Load/Edit Patient Data protocol, Screen 6, Group 6.                                                                                                                                                                                                                                                                                                                   |     | Patient Load Edit | Radiation exposure field must be YES in the patient file.                                  |
| 719   |       | Radiation Exposure Method is inactive.                          | Review current entry through the Load/Edit Patient Data protocol, Screen 6, Group 6.                                                                                                                                                                                                                                                                                                                     |     | Patient Load Edit | Must be a code of N, T or B.                                                               |
| 721   | 7210  | Radiation Exposure Indicated is missing or invalid.             | Review current entry through the Load/Edit Patient Data protocol, Screen 6, Group 6.                                                                                                                                                                                                                                                                                                                     |     | Patient Load Edit | Radiation exposure indicated field must equal Y or N.                                      |
| 733   | 7330  | Combat Veteran is missing or invalid.                           | Review combat and military service data through the Load/Edit Patient Data protocol, Screen 6.                                                                                                                                                                                                                                                                                                           |     | Patient Load Edit | Combat Veteran Indicated must equal Y or N.                                                |
| 734   | 7340  | Combat Veteran end date is invalid.                             | Review combat and military service data through the Load/Edit Patient Data protocol, Screen 6.                                                                                                                                                                                                                                                                                                           |     | Patient Load Edit | Must be a valid Date.                                                                      |
| 735   |       | Combat Veteran end date missing.                                | Review combat and military service data through the Load/Edit Patient Data protocol, Screen 6.                                                                                                                                                                                                                                                                                                           |     | Patient Load Edit | Must be a valid Date.                                                                      |
| 805   | 8050  | Number of dependents is missing.                                | Correct dependent information through Load/Edit Patient Data protocol, Screen 8.                                                                                                                                                                                                                                                                                                                         |     | Patient Load Edit | Must be a number between 0 and 99.                                                         |
| 807   | 8070  | Number of dependents inconsistent with Means Test indicator.    | Compare the dependent information in the Load/Edit Patient Data protocol, Screen 8, with the information in the View a Past Means Test option, Screen 1, and correct as necessary.                                                                                                                                                                                                                       |     | Patient Load Edit | If number of dependents is XX (not applicable), the Means Test status must be AS, N, or X. |
| 810   | 8100  | Invalid Means Test indicator.                                   | 1\) Check if a Means Test is required. A Means Test can be completed (if required) through the Load/Edit Patient Data protocol after the consistency checker has run. 2) Check if a valid Means Test existed ON OR BEFORE THE DATE OF ENCOUNTER. 3) Check if a Means Test is required and not done/completed. 4) Check the eligibility of the encounter. 5) Check the appointment type of the encounter. |     | Patient Load Edit | Must be a valid Means Test status - AS, AN, N, X, or C.                                    |

<table>
<colgroup>
<col style="width: 4%" />
<col style="width: 5%" />
<col style="width: 25%" />
<col style="width: 16%" />
<col style="width: 15%" />
<col style="width: 16%" />
<col style="width: 15%" />
</colgroup>
<tbody>
<tr class="odd">
<td colspan="2">Error</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>NPCD</td>
<td>VISTA</td>
<td>Error Description</td>
<td colspan="2">Correction Description</td>
<td>Correction Logic</td>
<td>Validation Logic</td>
</tr>
<tr class="odd">
<td>812</td>
<td>8120</td>
<td>Means Test indicator inactive.</td>
<td colspan="2">1) Check if a Means Test is required. A Means Test can be completed (if required) through the Load/Edit Patient Data protocol after the consistency checker has run. 2) Check if a valid Means Test existed ON OR BEFORE THE DATE OF ENCOUNTER. 3) Check if a Means Test is required and not done/completed. 4) Check the eligibility of the encounter. 5) Check the appointment type of the encounter.</td>
<td>Patient Load Edit</td>
<td></td>
</tr>
<tr class="even">
<td>815</td>
<td>8150</td>
<td>Patient income is invalid.</td>
<td colspan="2">Correct patient income through Load/Edit Patient Data protocol, Screen 8.</td>
<td>Patient Load Edit</td>
<td>Must be a valid amount, zero or greater.</td>
</tr>
<tr class="odd">
<td>900</td>
<td></td>
<td>Outpatient classification type is missing or invalid.</td>
<td colspan="2">Review classification questions through Load/Edit Patient Data protocol, Screen 6, Groups 5, 6, and 12, and Screen 7, Group 1.</td>
<td>Patient Load Edit</td>
<td>Must be a valid classification question from the OUTPATIENT CLASSIFICATION TYPE file.</td>
</tr>
<tr class="even">
<td></td>
<td>9000</td>
<td>Classification type questions are invalid.</td>
<td colspan="2">Review classification questions through Load/Edit Patient Data protocol, Screen 6, Groups 5, 6, and 12, and Screen 7, Group 1.</td>
<td>Checkout Interview</td>
<td>Same check as above.</td>
</tr>
<tr class="odd">
<td>901</td>
<td>9010</td>
<td>No longer used.</td>
<td colspan="2"></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>902</td>
<td>9020</td>
<td>Veteran status inconsistent with classification type question.</td>
<td colspan="2">Review patient information through Load/Edit Patient Data protocol, Screen 6, Groups 5, 6, and 12, and Screen 7, Group 1. Correct inconsistencies as needed.</td>
<td>Patient Load Edit</td>
<td><p>If veteran status is YES, than the values for the classification questions must be 1, 0, or not filled in. If veteran status is NO, than there should be no answers for any classification questions except possibly environmental contamination. If environmental contamination is answered, then period of service must be one of the following:</p>
<p>-Army active duty</p>
<p>-Navy/Marines active duty</p>
<p>-Air Force active duty</p>
<p>-Coast Guard active duty</p></td>
</tr>
</tbody>
</table>

|       |       |                                                          |                                                                                                                                                                                                                                                     |     |                          |                                                                     |
|-------|-------|----------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|--------------------------|---------------------------------------------------------------------|
| Error |       |                                                          |                                                                                                                                                                                                                                                     |     |                          |                                                                     |
| NPCD  | VISTA | Error Description                                        | Correction Description                                                                                                                                                                                                                              |     | Correction Logic         | Validation Logic                                                    |
| 903   | 9030  | MST status inconsistent with classification type.        | Encounter is flagged as related to MST, but MST has not been claimed. Please correct either the encounter information or the Military Sexual Trauma status.                                                                                         |     | Checkout Interview       |                                                                     |
| 904   | 9040  | Combat Vet status inconsistent with classification type. | Encounter has been marked as being related to combat but patient is not a combat veteran (or was no longer considered a combat veteran at the time of the encounter). Review patient information through Load/Edit Patient Data protocol, Screen 6. |     | Patient Load Edit        |                                                                     |
| 905   | 9050  | Answers to classification type questions missing.        | Correct classification questions through Load/Edit Patient Data protocol, Screens 6 and 7.                                                                                                                                                          |     | Patient Load Edit        | Answers to classification questions must be 1, 0, or not filled in. |
| 906   |       | Inactive outpatient classification type.                 | Correct classification question through Load/Edit Patient Data protocol, Screens 6 and 7.                                                                                                                                                           |     | Patient Load Edit        |                                                                     |
| 915   | 9150  | Sequential number (Set ID) in ZCL is invalid.            | There was a problem with the HL7 ZCL Segment. This entry will be reflagged for transmission.                                                                                                                                                        |     | Entry will be reflagged  |                                                                     |
| 999   |       | Reason unknown.                                          | Rejected by NPCD without a valid reason, use the 'Retransmit Selected Error Code' \[SCDX AMBCAR RETRANS ERROR\] option to resend.                                                                                                                   |     | Entry will be reflagged. |                                                                     |
| 002   |       | BHS Segment missing.                                     | There was a problem with the HL7 BHS Segment. This entry will be reflagged for transmission.                                                                                                                                                        |     | Entry will be reflagged  |                                                                     |
| 003   |       | MSH Segment missing. Invalid control ID.                 | There was a problem with the HL7 MSH Segment. This entry will be reflagged for transmission.                                                                                                                                                        |     | Entry will be reflagged  |                                                                     |
| 004   |       | Invalid batch sending facility.                          | This entry will be reflagged for transmission.                                                                                                                                                                                                      |     | Entry will be reflagged  |                                                                     |
| 005   | 0005  | EVN Segment missing in HL7 transmission message.         | There was a problem with the HL7 EVN Segment. This entry will be reflagged for transmission.                                                                                                                                                        |     | Entry will be reflagged  |                                                                     |
| 006   | 0006  | PID Segment missing in HL7 transmission message.         | There was a problem with the HL7 PID Segment. This entry will be reflagged for transmission.                                                                                                                                                        |     | Entry will be reflagged  |                                                                     |
| 007   | 0007  | ZPD Segment missing in HL7 transmission message.         | There was a problem with the HL7 ZPD Segment. This entry will be reflagged for transmission.                                                                                                                                                        |     | Entry will be reflagged  |                                                                     |
| 008   | 0008  | PV1 Segment missing in HL7 transmission message.         | There was a problem with the HL7 PV1 Segment. This entry will be reflagged for transmission.                                                                                                                                                        |     | Entry will be reflagged  |                                                                     |
| 009   | 0009  | PR1 Segment missing in HL7 transmission message.         | There was a problem with the HL7 PR1 Segment. This entry will be reflagged for transmission.                                                                                                                                                        |     | Entry will be reflagged  |                                                                     |
| 010   | 0010  | ZEL Segment missing in HL7 transmission message.         | There was a problem with the HL7 ZEL Segment. This entry will be reflagged for transmission.                                                                                                                                                        |     | Entry will be reflagged  |                                                                     |

|       |       |                                                       |                                                                                                                              |     |                                                                                     |                                                                     |
|-------|-------|-------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------|-----|-------------------------------------------------------------------------------------|---------------------------------------------------------------------|
| Error |       |                                                       |                                                                                                                              |     |                                                                                     |                                                                     |
| NPCD  | VISTA | Error Description                                     | Correction Description                                                                                                       |     | Correction Logic                                                                    | Validation Logic                                                    |
| 011   | 0011  | ZIR Segment missing in HL7 transmission message.      | There was a problem with the HL7 ZIR Segment. This entry will be reflagged for transmission.                                 |     | Entry will be reflagged                                                             |                                                                     |
| 012   | 0012  | ZCL Segment missing in HL7 transmission message.      | There was a problem with the HL7 ZCL Segment. This entry will be reflagged for transmission.                                 |     | Entry will be reflagged                                                             |                                                                     |
| 013   | 0013  | ZSC Segment missing in HL7 transmission message.      | There was a problem with the HL7 ZSC Segment. This entry will be reflagged for transmission.                                 |     | Entry will be reflagged                                                             |                                                                     |
| 014   | 0014  | ZSP Segment missing in HL7 transmission message.      | There was a problem with the HL7 ZSP Segment. This entry will be reflagged for transmission.                                 |     | Entry will be reflagged                                                             |                                                                     |
| 020   |       | EVN Segment missing in delete message.                | There was a problem with the HL7 EVN Segment. This entry will be reflagged for transmission.                                 |     | Entry will be reflagged                                                             |                                                                     |
| 021   |       | PID Segment missing in delete message.                | There was a problem with the HL7 PID Segment. This entry will be reflagged for transmission.                                 |     | Entry will be reflagged                                                             |                                                                     |
| 022   |       | ZPD Segment missing in delete message.                | There was a problem with the HL7 ZPD Segment. This entry will be reflagged for transmission.                                 |     | Entry will be reflagged                                                             |                                                                     |
| 023   |       | PV1 Segment missing in delete message.                | There was a problem with the HL7 PV1 Segment. This entry will be reflagged for transmission.                                 |     | Entry will be reflagged                                                             |                                                                     |
| 030   |       | BTS Segment missing.                                  | There was a problem with the HL7 BTS Segment. This entry will be reflagged for transmission.                                 |     | Entry will be reflagged                                                             |                                                                     |
| 035   | 0035  | Invalid HL7 segment name.                             | This entry will be reflagged for transmission.                                                                               |     | Entry will be reflagged                                                             |                                                                     |
| 036   | 0036  | DG1 Segment missing in HL7 transmission message.      | There was a problem with the HL7 DG1 Segment. This entry will be reflagged for transmission.                                 |     | Entry will be reflagged                                                             |                                                                     |
| 037   | 0370  | ROL segment missing.                                  | There was a problem with the HL7 ROL Segment. This entry will be reflagged for transmission.                                 |     | Entry will be reflagged.                                                            |                                                                     |
| A00   | A000  | Invalid DSS identifier/stop code.                     | The stop code must be a valid entry in the CLINIC STOP file. Use the Encounter protocol to assign an active/valid stop code. |     | Display Message – “The Clinic set-up needs to be reviewed. Contact your MAS ADPAC.” | Must be a valid stop code from the CLINIC STOP file.                |
| A02   | A020  | Inactive DSS identifier/stop code.                    | Correct the clinic stop code through the Encounter Information option.                                                       |     | Edit Encounter Option                                                               | Check to ensure the clinic was active on the date of the encounter. |
| A05   | A050  | Sequential number (Set ID) in ZSC Segment is invalid. | There was a problem with the HL7 ZSC Segment. This entry will be reflagged for transmission.                                 |     | Entry will be reflagged                                                             |                                                                     |
| B00   | B000  | Missing or invalid service connected.                 | Correct service connected question through Load/Edit Patient Data protocol, Screen 7, Group 1.                               |     | Patient Load Edit                                                                   | Must be filled in with service connected YES or NO.                 |

|       |       |                                                             |                                                                                                                                                                                                                     |     |                                             |                                                                                                                                                 |
|-------|-------|-------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|---------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| Error |       |                                                             |                                                                                                                                                                                                                     |     |                                             |                                                                                                                                                 |
| NPCD  | VISTA | Error Description                                           | Correction Description                                                                                                                                                                                              |     | Correction Logic                            | Validation Logic                                                                                                                                |
| B05   | B050  | Invalid service-connected percentage.                       | Correct service-connected percentage through Load/Edit Patient Data protocol, Screen 7, Group 1.                                                                                                                    |     | Patient Load Edit                           | Must be a valid service-connected percentage number.                                                                                            |
| B10   | B100  | Missing or invalid period of service.                       | Correct period of service through Load/Edit Patient Data protocol, Screen 7, Group 3.                                                                                                                               |     | Patient Load Edit                           | Period of service must be answered with a valid entry.                                                                                          |
| B12   | B120  | Period of service is inactive.                              | Correct period of service through Load/Edit Patient Data protocol, Screen 7, Group 3.                                                                                                                               |     | Patient Load Edit                           | Period of service must be active.                                                                                                               |
| B15   | B150  | Invalid Vietnam service indicated.                          | Correct Vietnam service indicator through Load/Edit Patient Data protocol, Screen 6, Group 4.                                                                                                                       |     | Patient Load Edit                           | Vietnam service indicator must be YES, NO, UNKNOWN, or not filled in.                                                                           |
| B17   | B170  | Vietnam service indicated inconsistent with veteran status. | Review Vietnam service indicator and veteran status through Load/Edit Patient Data protocol, Screen 6, Group 4 and Screen 7, Group 1.                                                                               |     | Patient Load Edit                           | If Vietnam service indicator is YES, NO, or UNKNOWN, veteran status must be YES. If Vietnam indicator not filled in, veteran status must be NO. |
| C00   |       | Batch message count does not match number received.         | There was a problem with the HL7 transmission. This entry will be reflagged for transmission.                                                                                                                       |     | Entry will be reflagged                     |                                                                                                                                                 |
| D00   | D000  | Provider Type Code is missing or invalid.                   | This problem can be caused by no person class being designated for the provider or the person class being inactive. This needs to be referred to the person responsible for designating Person Class for providers. |     | Display Message - "Contact your MAS ADPAC." | There must be a valid person class for the provider.                                                                                            |
| D05   | D050  | Primary Provider Designation is missing or invalid.         | Using the Check Out protocol, ensure that one, and only one, provider has been denoted as the primary provider for the encounter.                                                                                   |     | Checkout Interview                          | Must be a valid provider(s) and one, and only one, must be marked as primary.                                                                   |
| D07   | D070  | Provider ID is missing or invalid (invalid DUZ).            | Using the Check Out protocol, ensure that one, and only one, provider has been denoted as the primary provider for the encounter.                                                                                   |     | Checkout Interview                          | Same as above.                                                                                                                                  |
| D09   |       | Provider ID is missing or invalid (invalid facility).       | This error can not be corrected through IEMM. It needs to be corrected in the STATION NUMBER (TIME SENSITIVE) file. Contact your MAS ADPAC.                                                                         |     | Display Message - "Contact your MAS ADPAC." |                                                                                                                                                 |
| D11   |       | Provider ID is missing or invalid (inactive facility).      | This error can not be corrected through IEMM. It needs to be corrected in the STATION NUMBER (TIME SENSITIVE) file. Contact your MAS ADPAC.                                                                         |     | Display Message - "Contact your MAS ADPAC." |                                                                                                                                                 |

|       |       |                                                |                                                                                                                                                                                                 |     |                                                                         |                                                  |
|-------|-------|------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----|-------------------------------------------------------------------------|--------------------------------------------------|
| Error |       |                                                |                                                                                                                                                                                                 |     |                                                                         |                                                  |
| NPCD  | VISTA | Error Description                              | Correction Description                                                                                                                                                                          |     | Correction Logic                                                        | Validation Logic                                 |
| D13   | D130  | Provider name missing or invalid.              | Provider names can not be numeric. Request that Human Resources correct the provider's name.                                                                                                    |     | Display Message - "Contact Human Resources."                            | Name cannot be numeric.                          |
| D14   | D140  | Provider SSN missing or invalid.               | All encounter providers must have an SSN listed in the New Person file (#200). Their SSN can not contain 5 or more leading zeros. Request that Human Resources obtain/store the provider's SSN. |     | Display Message - "Contact Human Resources."                            | SSN cannot contain five leading zeroes.          |
| D15   | D150  | Role Instance ID is missing or invalid.        | There was a problem with the HL7 ROL Segment. This entry will be reflagged for transmission.                                                                                                    |     | Entry will be reflagged.                                                |                                                  |
|       | Z000  | Invalid appointment type (Computer Generated). | Correct through the Edit Computer Generated Appointment Type option on the Computer Generated Menu.                                                                                             |     | Display Message – “Correct through the Computer Generated Menu option.” | Cannot be a computer generated appointment type. |