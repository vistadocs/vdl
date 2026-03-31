---
title: PSO*7*161 Laser Printed Prescription Labels Phase II Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: Laser Printed Prescription Labels Phase II
app_code: PSO
app_name: "Pharmacy: Outpatient Pharmacy"
section: CLI
app_status: archive
pkg_ns: PSO
patch_ver: 7
patch_id: PSO*7*161
group_key: "PSO:PSO:7"
file_numbers: []
security_keys: []
menu_options: 0
description: "Laser Printed Prescriptions Labels Phase II functionality affects Pharmacy Data Management in the following ways:"
audience: 
keywords: 
  - warning
  - label
  - labels
  - pharmacy
  - print
  - table
  - laser
  - contents
  - prescription
  - patient
page_count: 0
word_count: 3680
section_count: 11
table_count: 3
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 2005
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy_Archive/pso_7_p161_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy_Archive/pso_7_p161_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=394"
---

> ![](pso-7-161-laser-printed-prescription-labels-phase-ii-release-notes/001.png)

Laser printed prescriptions labelsPhase ii

####### RELEASE NOTES 

March 2005

PSS\*1\*87

PSO\*7\*161

V*IST*A Health Systems Design & Development

Table of Contents

*(This page included for two-sided copying.)*

# # Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Introduction](#introduction)
- [Pharmacy Data Management](#pharmacy-data-management)
  - [Overview](#overview)
  - [Features, Functions and Enhancements](#features-functions-and-enhancements)
  - [Files and Fields](#files-and-fields)
  - [Other Functionality](#other-functionality)
- [Outpatient Pharmacy](#outpatient-pharmacy)
  - [Overview](#overview-1)
  - [Features, Functions, and Enhancements](#features-functions-and-enhancements-1)
  - [Files and Fields](#files-and-fields-1)
  - [Other Functionality](#other-functionality-1)
- [Special Considerations](#special-considerations)
  - [Communications Interfaces](#communications-interfaces)
  - [New Utility Routine](#new-utility-routine)
The purpose of these Release Notes is to briefly describe the features and functions of the Laser Printed Prescriptions Labels Phase II software. Pharmacy Data Management and Outpatient Pharmacy information is included in this manual. This document is intended for the Information Resources Management Service (IRMS) staff and the Pharmacy Automated Data Processing Application Coordinator (ADPAC).
The Pharmacy Benefits Management Strategic Healthcare Group (PBM-SHG) requested enhancements to the Outpatient Pharmacy Veterans Health Information Systems and Technology Architecture (V*IST*A) application. Compliance issues of the patient counseling guidelines set by the Joint Commission for the Accreditation of Healthcare Organizations (JCAHO), and Omnibus Budget Reconciliation Act (OBRA) 1990 requirements are included in these enhancements.
Pharmacy staff members and an industrial engineer in Veterans Integrated Service Network (VISN) 8 have provided Pharmacy Benefit Management (PBM) with a laser label prototype design based on prior work that Tampa Department of Veterans Affairs Medical Center (VAMC) personnel performed. This group has worked with national staff and the development team within Provider Systems - Pharmacy (a.k.a. Clinical Ancillary Systems Service) to establish the standard format for the 8.5 by 14-inch laser prescription label with Patient Medication Information (PMI) Sheet.
The Laser Printed Prescriptions Labels project includes two phases of enhancements. Phase I included the upgrade of the print format to an 8.5 by 14-inch laser prescription label, patient’s prescription label information with an expiration date and a PMI sheet all printed on the larger laser label. That phase was completed in May 2003.
Phase II is the focus of these release notes. This phase includes the individual installation of the Pharmacy Data Management, Consolidated Mail Outpatient Pharmacy (CMOP) and Outpatient Pharmacy patches. Following the installation of these patches, the site’s pharmacy system will reference a new commercial data source for printing the prescription warning labels. This will provide patients with the option of receiving the PMI sheets and warning labels in their language preference (English or Spanish). Another enhancement is the addition of an option to manually print the Multi-Rx refill request form on laser label stock.
The Laser Printed Prescriptions Labels project worked together with the ePharmacy project team and incorporated some of the ePharmacy requirements. Adding the 3<sup>rd</sup> Party Rx information and the National Drug Code (NDC) to the Patient Fill section of the labels when the information is available assists in meeting end-user requirements for operational support of electronic claims processing. A Signature Log is also incorporated to support adjudicating payer contractual requirements.
For any sites utilizing Automated Dispensing Machines, the laser labels print stream is modified within the Outpatient Pharmacy patch. Each site must determine if their machines rely on the data print stream being sent to the laser labels port. If so, the site has two options available before implementing these patches.
1.  The site can implement the Outpatient Automation Interface (OPAI), which was available as patch PSO\*7\*156 and released in October 2004.
2.  The site can contact their dispensing machine vendor to make adjustments based on the new data print stream.
The first option is the preferred solution since it is expected OPAI will be mandated and any future changes to the label format would not affect the dispensing equipment interface.
Laser Printed Prescriptions Labels Phase II software is not part of a master build. This phase includes patches PSS\*1\*87, PSX\*2\*54, PSO\*7\*161 and PSO\*7\*200, which are installed separately. The software listed in the table below must be installed before one can load all the patches that make the Laser Printed Prescriptions Labels Phase II project functional.
![](pso-7-161-laser-printed-prescription-labels-phase-ii-release-notes/002.png)Note: The CMOP patch, PSX\*2\*54, will be released at a later date, when the CMOPs are ready to receive the format changes.
![](pso-7-161-laser-printed-prescription-labels-phase-ii-release-notes/003.png)Note: The Outpatient Pharmacy patch, PSO\*7\*200, will be released at a later date, when changes are made to the Outpatient Automation Interface processing to pass the new warning label text in English or Spanish.
| Package                                  | Minimum Version Needed |
|----------------------------------------------|----------------------------|
| VA FileMan                                   | 22.0                       |
| Kernel                                       | 8.0                        |
| MailMan                                      | 8.0                        |
| Outpatient Pharmacy                          | 7.0                        |
| Pharmacy Data Management                     | 1.0                        |
| National Drug File (NDF)                     | 4.0                        |
| Consolidated Mail Outpatient Pharmacy (CMOP) | 2.0                        |
| Health Level 7 (HL7)                         | 1.6                        |

# Pharmacy Data Management 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section lists new and changed features, functions, and enhancements of the Laser Printed Prescriptions Labels Phase II software for the Pharmacy Data Management package.

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Laser Printed Prescriptions Labels Phase II functionality affects Pharmacy Data Management in the following ways:

- It adds a new Warning Label Builder program to allow the user to view/modify the list of warning labels for a drug.
- The PSSCOMMON Input Template for the *Drug Enter/Edit* \[PSS DRUG ENTER/EDIT\] option is modified to allow the user to view/modify the new warning labels that will print for a drug.
- The *Lookup into Dispense Drug File* \[PSS LOOK\] option will display the new warning label information for a drug.

## Features, Functions and Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains information about new and enhanced Pharmacy Data Management menu options for the Laser Printed Prescriptions Labels Phase II software.

#### New Menu Options

############################### 

The following menu options have been added to support the Laser Printed Prescriptions Labels Phase II project:

- *Warning Builder* \[PSS WARNING BUILDER\] option allows the user to print a copy of the old and new warning file entries. This option also allows the user to choose various ways to select drugs to review those warnings, which will print when the flag is turned “on” for the new warning label source. It allows the user to override the default warning labels and create a custom warning list for the selected drug. This is accomplished by specifying a list of warning numbers from the old RX CONSULT file (#54) and/or the new commercial data source warning file.
- *Warning Mapping* \[PSS WARNING MAPPING\] option can be used to match an entry from the old RX CONSULT file (#54) to the WARNING LABEL-ENGLISH file (#50.625) to aid in using the Warning Builder (to identify local warnings that do not have an equivalent entry in the new commercial data source). The user can also enter a Spanish translation for an RX CONSULT file (#54) entry, if desired, but whenever possible, the new commercial data source’s warnings should be used.

#### #### #### Enhanced Option Functionality

############################### 

The following menu options have been modified to support Laser Printed Prescriptions Labels Phase II:

- *Pharmacy Data Management* \[PSS MGR\] option is modified to include the new Warning *Builder* \[PSS WARNING BUILDER\] option and the *Warning Mapping* \[PSS WARNING MAPPING\] option.
- *Pharmacy System Parameters Edit* \[PSS SYS EDIT\] option allows the user to choose (edit) the WARNING LABEL SOURCE field (#16) in the PHARMACY SYSTEM file (#59.7) to turn on the new data source for warnings.

## Files and Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains information about new Pharmacy Data Management fields for the Laser Printed Prescriptions Labels Phase II software.

#### #### New Fields

############################### 

############################### WARNING LABEL SOURCE field (#16)

############################### 

This field in the PHARMACY SYSTEM file (#59.7) identifies whether the warning labels will be used from the RX CONSULT file (#54) only or the new commercial data source files, the WARNING LABEL-ENGLISH file (#50.625) or the WARNING LABEL-SPANISH file (#50.626). A “null” value will indicate the warning labels are coming from the old RX CONSULT file (#54) and an “N” for “New” value indicates the new data source warning labels are enabled. This field is editable through the *Pharmacy System Parameters Edit* \[PSS SYS EDIT\] option.

############################### 

############################### NEW WARNING LABEL LIST field (#8.1)

############################### 

This field in the DRUG file (#50) can contain a customized list of warning numbers for the drug when the default warnings are not sufficient. The warnings in this field can be from the WARNING LABEL-ENGLISH file (#50.625) or WARNING LABEL-SPANISH file (#50.626) and/or the old RX CONSULT file (#54). The new data source’s warnings are denoted with a suffix of “N”. An example of the drug warnings would be 1N, 8N, 23, 5N, 12N where the warnings 1, 8, 5, and 12 are from the new data source and 23 is from the RX CONSULT file (#54).

GENDER SPECIFIC LBLS ON ALL RX field (#8.2)

This field in the DRUG file (#50) identifies whether the warning should print if it applies only to a particular gender or if it will print for both genders. A “null” or “Y” value will indicate a warning will print for all patients. An “N” value will allow the warning to print for this drug when the patient is that specific gender. The commercial data source will indicate whether the warning applies to a particular gender or to both.

WARNING MAPPING field (#2)

This field in the RX CONSULT file (#54) contains the warning label number from the new national warning label provider that corresponds to the current RX CONSULT file (#54) entry. A “zero” (0) value indicates the site is not mapping the current file entry to a new warning label and a “null” entry indicates that a new warning label is not available for this current file entry. The first twenty (1-20) entries in the RX CONSULT file (#54) will be populated during the post-installation of the PSS\*1\*87 patch. The following table indicates the populated values.

|                 |                             |
|-----------------|-----------------------------|
| RX CONSULT File | Warning Mapping Field Value |
| 1               | 1                           |
| 2               | 2                           |
| 3               | 3                           |
| 4               | 4                           |
| 5               | 5                           |
| 6               | 6                           |
| 7               | NULL (No mapping available) |
| 8               | 8                           |
| 9               | 9                           |
| 10              | 10                          |
| 11              | 11                          |
| 12              | 19                          |
| 13              | 20                          |
| 14              | NULL (No mapping available) |
| 15              | 30                          |
| 16              | NULL (No mapping available) |
| 17              | NULL (No mapping available) |
| 18              | NULL (No mapping available) |
| 19              | NULL (No mapping available) |
| 20              | NULL (No mapping available) |

############################### 

SPANISH TRANSLATION field (#3)

This field in the RX CONSULT file (#54) contains the Spanish translation for the warning label. (No other languages are available at this time.) Of the original 20 warning labels, only warning label \#20 will be populated with the translation. Warning label 20 is the “NO TRANSFER” warning: “CAUTION: Federal law prohibits the transfer of this drug to any person other than the patient for whom it was prescribed. The Spanish Translation: PRECAUCION: La ley federal prohibe la transferencia de este medicamento a otro paciente para el que no fue recetado.”

## Other Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DRUG file (#50) INPUT template \[PSSCOMMON\] is modified to allow the user to view the new warning labels for a drug and edit the NEW WARNING LABEL LIST field (#8.1) of the DRUG file (#50) if desired. The GENDER SPECIFIC LBLS ON ALL RX field (#8.2) is available for editing if this drug has any gender specific warnings.

A new Application Program Interface (API), between the Pharmacy Data Management package and the Outpatient Pharmacy package, is responsible for deciding which warnings will print for the specified drug.

Another API is responsible for returning the warning label text in the appropriate language to be printed on the labels.

The height of the individual lines of white spaces between the sections of the PMI sheet is reduced, resulting in extra lines of the PMI to print on that page.

# Outpatient Pharmacy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section lists new and changed features, functions, and enhancements of the Laser Printed Prescriptions Labels Phase II software for the Outpatient Pharmacy package.

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Laser Printed Prescriptions Labels Phase II functionality affects Outpatient Pharmacy in the following ways:

- The ability to reference a new commercial data source for printing prescription warning labels.
- The patient’s PMI language preference setting (English or Spanish) determines the language of the warning labels and PMI sheets.
- Multi-Rx forms no longer print during any label reprint. A new option is available to manually reprint the Multi-Rx forms.
- Several changes (detailed in the following sections) are made to the label format and content.

## Features, Functions, and Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains information about new and enhanced Outpatient Pharmacy menu options and actions for the Laser Printed Prescriptions Labels Phase II software. No menu options, reports, or actions have been deleted.

#### New Menu Options

The following new report menu options have been added to support Laser Printed Prescriptions Labels Phase II:

############################### 

*Manual Print of Multi-Rx Forms* \[PSO LM MULTI-RX PRINT\] option appears under the *Rx (Prescriptions)* \[PSO RX\] option and allows the user to reprint the Multi-Rx Refill Request form on laser label stock without having to reprint the entire prescription labels. The user will receive a system confirmation that this form has been queued to print.

*Signature Log Reprint* \[PSO SIGLOG REPRINT\] option appears under the *Rx (Prescriptions)* \[PSO RX\] option and allows the user to reprint the Signature Log for a particular prescription. This option was requested in conjunction with the ePharmacy requirements.

#### #### #### Enhanced Option Functionality

############################### 

The following menu option has been modified to support Laser Printed Prescriptions Labels Phase II:

- *Rx (Prescriptions)* \[PSO RX\] option is modified to include the new manual print of the Multi-Rx form.

#### #### #### New Action

The following new hidden action has been added to the *Patient Prescription Processing* \[PSO LM BACKDOOR ORDERS\] option to support Laser Printed Prescriptions Labels Phase II:

############################### 

- The hidden action, Multi-Rx Request Print \[MR\], will print the *Manual Print of Multi-Rx Forms* \[PSO LM MULTI-RX PRINT\] option for the current patient selected on the *Patient Prescription Processing* \[PSO LM BACKDOOR ORDERS\] option. This new action, MR, exists under the hidden *Other OP Actions* \[OTH\] option. The user will receive a system confirmation that this form has been queued to print.

## Files and Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section contains information about a new Outpatient Pharmacy field for the Laser Printed Prescriptions Labels Phase II software.

#### New Field

############################### 

############################### MAILING COMMENTS field (#.081)

############################### 

This field in the OUTPATIENT SITE file (#59) is available for a site to enter any information that will show on the Mail Address label. For example, this free text entry might be “Forwarding service requested” or “Address service requested”. The comments will show after the MAIL field (#.03) in PHARMACY PATIENT file (#55) on the label.

## Other Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The OUTPATIENT SITE file (#59) INPUT template \[PSO SITE\] is modified to allow the user to enter information into the new mailing comments line of the mailing label section of the prescription document.

Several changes that are not addressed in the above sections are listed below. These changes are grouped according to the sections of the prescription label document.

#### Prescription Label Section Changes

- When the length of the SIG (SIG field (#10) of the PRESCRIPTION file (#52)) requires the use of two or more labels, the first four lines of the label will not print on the second and subsequent labels. These lines include the Department of Veterans Affairs Medical Center (VAMC) name and address lines, the prescription number along with the refill information and the last line is the patient’s name and last portion of the social security number.
- The number of lines of the SIG that print on each label is increased to reduce the number of labels needed for the prescription. This also allows the overlapping of the multiple labels to eliminate the need for cutting the labels to make them fit.
- The SIG is bottom-justified within lines 5 to 8, above the “Discard after” date line on the last continued label.
- The text “May refill nX by MMM DD, YYYY” or “NO REFEFILLS LEFT” or “NO REFILL” is added between the “Discard after” date line and the “Qty:” line.
- “Mfr\_\_\_\_” is added to the “Discard after” date line beside the discard date. This line along with the quantity, physician, and drug name appear only on the last continued label.
- “Discard after” text prints for all drugs except those marked as supply items.
- On the first bottle label, the phrase “(continued on next label)” is eliminated, however the Rx number and “(label continued)” do remain on the subsequent continuation labels.

#### Warning Label Section Changes

- Warnings print in English or Spanish depending on the patient’s PMI preference.
- When there are fewer than five warning labels, the warning labels are bottom-justified.

#### Warning Label Section Changes (continued)

- When the DEA SPECIAL HDLG field (#3) in the DRUG file (#50) begins with 1,2,3,4,or 5, the NO TRANSFER warning label from the RX CONSULT file (#54) (entry number 20) prints in the appropriate language.
- The new data source contains several lengthy warnings (especially Spanish translations). A fourth line of text is allowed, if needed, for the smallest font.
- The top warning label sometimes printed on or over the perforated line. For some fonts, the white space between the lines of this warning is reduced so the warning will fit on the label.

#### Mail Address Section Changes

- The current date is printing in the upper right corner. It is right-justified and is retrieved from the LABEL DATE/TIME field (#32,.01) in the PRESCRIPTION file (#52). This date prints to the right on the same line as “Attn: (119)”
- The patient name prints first name first instead of last name, first name.
- When the routing is “Window”, the word “Window” is bolded. “Mail” is also bolded in this section.

#### Pharmacy Fill Card Section Changes

- The seconds is removed from the label date/time.
- The drug warnings are listed and separated by commas. If an entry in the list does not have an “N” (for “New”), then that warning number is from the RX CONSULT file (#54). Otherwise the warning is from the new commercial data source residing in the WARNING LABEL-ENGLISH file (#50.625) or the WARNING LABEL-SPANISH file (#50.626).
- The patient status and location (clinic) is added beneath the drug warnings.
- The patient’s name and last portion of the social security number is bolded.
- When the bottle cap is “non-safety”, the words “NON-SAFETY” are bolded.
- The number of lines of the SIG that print on each pharmacy fill card label is increased to reduce the number of labels needed for the prescription.

#### Patient Fill Section Changes

- The barcode prints every time even when there are no refills.
- The site telephone number prints when the “PHONE IN OR MAIL THIS REFILL REQUEST” prints.
- The text “n refills left until MMM DD, YYYY” is changed to “May refill nX by MMM DD, YYYY”.
- The text “3<sup>rd</sup> Party Rx” and the NDC number are added when this information is available. This enhancement is in request to the ePharmacy requirements.

#### #### Prescription Document PMI Section Changes

- The PMI section prints in the patient’s language preference.
- The white spaces between the sections of this document are reduced to allow more lines to print on the page.
- When there are more than five warning labels for the prescription, the additional warnings print at the top of the PMI section.

#### Trailing Document Changes

- The patient’s phone number, followed by an underline, prints on the Address Change form.
- The name and last portion of the social security number is bolded and the font is enlarged in the Allergies/ADR section.
- In the Allergies/ADR section, when the TYPE field (#2) of the HOSPITAL LOCATION file (#44) equals “W” (Ward) for any prescription for this patient, then the word “INPATIENT” prints on the line following the patient name.
- When no information is available or exists in the Allergies/ADR section, then “No Assessment Made” prints under the Verified Allergies heading. When the assessment is No Known Allergies (NKA), the Verified Allergies heading prints with the “NKA” indicator. All other subheadings/lines are removed for both of these examples due to no data being available.

#### Trailing Document Changes (continued)

- When the Suspended Prescription section contains no suspended prescriptions, then the heading does not print.
- The second and third lines of text from the Suspended Prescription section is modified to contain “The following prescription(s) have been requested and will be mailed to you on or after the date indicated”.
- In the Refill Narrative and Copay Narrative sections, the first seven lines print when there are more than seven lines from the original text. However, it could appear that more than seven lines are printing when the text wraps for a particular line.
- When the Refill Narrative and Copay Narrative sections contain no narratives, then the headings do not print.
- When the Multi-Rx Refill section is blank, indicating the patient does not have any refillable prescriptions, the SITE NUMBER field (#.06) of the OUTPATIENT SITE file (#59) prints on the bottom of the section and is right-justified.
- A signature log prints in the bottle label section of the trailing documents. The patient will sign for the medications received on this log. This option is in request to the ePharmacy requirements.

# Special Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Communications Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A specialized label printer (ScripTalk®) generates prescription labels with speech synthesized patient information. Currently, the software prints up to three warning label numbers from the RX CONSULT file (#54). Provider Systems will work with the ScripTalk® vendor to ensure continued function of spoken warning labels by the label readers if and when the ScripTalk® printers are capable of receiving the new warning text instead of warning numbers.

Outpatient Pharmacy patch PSO\*7\*200 is under development to be able to send the new warning labels in the patient’s language preference to the Outpatient Automation Interface. Provider Systems will keep vendors informed of any changes made to the interface routines.

## New Utility Routine

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Routine PSOLLU4 is included in the Outpatient Pharmacy patch PSO\*7\*161. This routine will change some of the control codes in the TERMINAL TYPE file (#3.2). The user will run this utility in programmer mode, after the patch is installed. The PATIENT FILL INITIALIZATION, PHARMACY FILL DOCUMENT WARNING, MAILING LABEL INITIALIZATION, and RETURN MAIL INITIALIZATION settings will have slight adjustments.

![](pso-7-161-laser-printed-prescription-labels-phase-ii-release-notes/004.png)Note: The user running this utility must have their FileMan access set to “@” to have permission to execute this routine.

*  
(This page included for two-sided copying.)*