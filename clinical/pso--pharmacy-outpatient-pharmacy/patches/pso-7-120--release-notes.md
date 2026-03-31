---
title: PSO*7*120 Laser Printed Rx Labels with PMI Sheets Phase I Release Note
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: Laser Printed Rx Labels with PMI Sheets Phase I Release Note
app_code: PSO
app_name: "Pharmacy: Outpatient Pharmacy"
section: CLI
app_status: archive
pkg_ns: PSO
patch_ver: 7
patch_id: PSO*7*120
group_key: "PSO:PSO:7"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - label
  - prescription
  - table
  - contents
  - laser
  - phase
  - labels
  - print
  - printer
  - features
page_count: 0
word_count: 972
section_count: 5
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: April 2003
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy_Archive/pso_7_0_p120_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy_Archive/pso_7_0_p120_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=394"
---

> ![](pso-7-120-laser-printed-rx-labels-with-pmi-sheets-phase-i-release-note/001.png)

Laser Printed Prescription Labels with PMI Sheets

#### Phase I

####### RELEASE NOTES

PSO\*7\*120

April 2003

V*IST*A System Design & Development

Table of Contents

*\<Page left blank for two-sided printing\>*

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Enhancements](#enhancements)
    - [Phase I](#phase-i)
    - [Phase II](#phase-ii)
  - [VA Laser Prescription Document](#va-laser-prescription-document)
  - [Laser Printer Requirements](#laser-printer-requirements)
- [New or Revised Features and Functions](#new-or-revised-features-and-functions)
  - [Modifications to Existing Features](#modifications-to-existing-features)
The Laser Labels project is an enhancement to the Outpatient Pharmacy (OP) V. 7.0 software package. The Laser Labels project introduces the use of laser-printed prescription labels in all VA facilities, and provides a Patient Medication Information (PMI) sheet with each prescription.
> Reminder: The existing dot-matrix label print functionality will continue to function after installation of this enhancement.
> Note: The following patches *must be installed* before installation of PSO\*7\*120:
- PSO\*7\*34

#### PSO\*7\*40

- PSO\*7\*92
- PSN\*4\*68

## Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

System Design & Development (SD&D) Provider Systems will deliver project enhancements in two phases as described below.

### Phase I

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This patch delivers the first phase of functionality. This enhancement will enable OP V. 7.0 to create 8.5 x 14-inch laser prescription documents. These documents include the patient’s prescription label information with an expiration date, prescription trailing documents, and a PMI sheet on national laser label format.

Currently, the OP V. 7.0 application prints patient prescription labels; however, the format does not print the labels with PMI sheets. Instead, a pharmacist must request the sheets during the processing of the patient’s prescription or use a separate menu option to print the sheets. Printing the label and PMI sheets on the same form will reduce prescription processing time.

### Phase II

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Phase II will be part of a future release and will reference a new data source for printing prescription warning labels. Phase II will also allow printing of patient instructions and warning labels in English or Spanish.

## VA Laser Prescription Document

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A workgroup of representatives from many VA pharmacies determined the laser label format. Because the format is new to users, the following three documents on the project website illustrate the new format:

- PSO_7_120_PrescriptionDocumentDescriptions.doc
- Label Measured Drawing.pdf
- SAMPLE LABELS FOR SRS.doc

The project website is located at:

<span class="mark">REDACTED</span>

## Laser Printer Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

##################### 

The enhancement software requires the use of one or more specially configured printers. The printer must print to a legal length form and must have barcode print capability. The printer must also support Hewlett Packard’s Printer Control Language (PCL) version 5 or greater.

If this equipment is not already available at your site, a variety of printers are available on the PCHS-2 contract, although most barcode chips are not a part of that contract. (Barcode chips cost from \$350 to \$500.)

> Warning: Due to the thickness of the adhesive-backed portion of the new label form, only 300 labels will fit in a printer tray designed to hold 500 pages of 20 lb. bond paper.

> Note: No special hardware, operating systems, nor programming languages are required for laser label printing.

Suggestions for printers are listed in RECOMMENDED PRINTERS.doc at the following link:

<span class="mark">REDACTED</span>

# New or Revised Features and Functions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The new or revised features and functions of the Laser Labels project for Outpatient Pharmacy V. 7.0 are included in this section.

##################### 2.1. Accessing the Laser Label Format

To access the new laser label format, the user must make the appropriate entries in the CONTROL CODES multiple (#55) of the TERMINAL TYPE file (#3.2).

> Note: Installation of PSO\*7\*120 has *no major effect* on the existing label functionality, and will not change the printed format of the label until you perform further steps, as described in the *Outpatient Pharmacy V. 7.0 Technical Manual.*

An example of a CONTROL CODE is as follows:

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<tbody>
<tr class="odd">
<td><blockquote>
<p>NUMBER: 11 CTRL CODE ABBREVIATION: MLI</p>
<p>FULL NAME: MAILING LABEL INITIALIZATION</p>
<p>CONTROL CODE: S PSOFONT="F10",PSOX=1700,PSOY=175,PSOYI=50</p>
</blockquote></td>
</tr>
</tbody>
</table>

In this control code, the setup is done that defines the font, starting page position, and line size for the Mailing Label Section of the label.

> Note: The detailed description of these control codes is found in the *Outpatient Pharmacy V. 7.0 Technical Manual.*

## Modifications to Existing Features

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Phase I affects some OUTPATIENT SITE file (#59) fields and other OP prescription label print features.

#### When a user selects a device defined for Laser Label output, the “OK to assume label alignment is correct? YES//” prompt is not asked.

#### ### Affected Options

The following options are affected by the “OK to assume label alignment is correct” YES//” prompt:

- *Rx (Prescriptions)* \[PSO RX\] option
- *Outpatient Pharmacy Manager* \[PSO MANAGER\] option
- *Patient Prescription Processing* \[PSO LM BACKDOOR ORDERS\] option
- *Complete Orders from OERR* \[PSO LMOE FINISH\] option
- *Pharmacist Menu* \[PSO USER1\] option
- *Pharmacy Technician's Menu* \[PSO USER2\] option
- *Suspense Functions* \[PSO PND\] option
- *Print from Suspense File* \[PSO PNDLBL\] option
- *Reprint Batches from Suspense* \[PSO PNDRPT\] option
- *Pull Early from Suspense* \[PSO PNDRX\] option
- *Reprint an Outpatient Rx Label* \[PSO RXRPT\] option
- *Label/Profile Monitor Reprint* \[PSO B\] option
- *Barcode Batch Prescription Entry* \[PSO BATCH BARCODE\] option
- *Change Label Printer* \[PSO CHANGE PRINTER\] option

The system reference to the PRESCRIPTION file (#52) COPIES field (#10.6) is changed. For a new prescription, when COPIES is set to 1, the full prescription content prints. If COPIES is greater than 1, the full prescription content prints one time. On the additional copies, only the adhesive prescription label portion prints. The adhesive portion includes the bottle label, warning label, and patient address label.

#### The prompt “Print ‘LEFT’ side of label only? N//” is changed to “Print adhesive portion of label only? N//.”

When “Print adhesive portion of label only? N//” prompt is answered NO, the full prescription content prints. When answered YES, only the adhesive portion of the label prints.

The BARCODES ON REQUEST FORMS field (#.119) of the OUTPATIENT SITE file (#59) is not used in this enhancement. Regardless of the value of this field, barcodes will print on the request form.

The NEW LABEL STOCK field (#4) of the OUTPATIENT SITE file (#59) is not used in this enhancement. The device setup controls the branch to the new functionality.