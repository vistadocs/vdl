---
title: National Drug File Version 4 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: anchor
doc_subject: 
app_code: PSN
app_name: "Pharmacy: National Drug File (NDF)"
section: CLI
app_status: active
pkg_ns: PSN
patch_ver: 4
patch_id: PSN*4
group_key: "PSN:PSN:4"
file_numbers: []
security_keys: []
menu_options: 0
description: - [# Enhancements](#enhancements) - [Redesigned National Drug File V. 4.0 Menu](#redesigned-national-drug-file-v-40-menu) > The National Drug File (NDF) V. 4.0 software module provides standardization of the local drug files in all Department of Veterans Affairs Medical Centers (VAMCs). Standardizat
audience: 
keywords: 
  - drug
  - national
  - report
  - product
  - table
  - contents
  - formulary
  - names
  - comes
  - enhancements
page_count: 0
word_count: 338
section_count: 2
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: October 1998
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-National_Drug_File_(NDF)/ndf_4_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-National_Drug_File_(NDF)/ndf_4_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=89"
---

![](national-drug-file-version-4-release-notes/001.png)

NATIONAL DRUG FILE(NDF)Release Notes

October 1998

V*IST*A Technical Services

# # Enhancements


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [# Enhancements](#enhancements)
  - [Redesigned National Drug File V. 4.0 Menu](#redesigned-national-drug-file-v-40-menu)
> The National Drug File (NDF) V. 4.0 software module provides standardization of the local drug files in all Department of Veterans Affairs Medical Centers (VAMCs). Standardization includes the adoption of new drug nomenclature and drug classification, and links the local drug file entries to data in the National Drug files.
> For drugs approved by the Food and Drug Administration (FDA), VAMCs have access to information concerning dosage form, strength and unit; package size and type; manufacturer’s trade name; and National Drug Code (NDC). The NDF software lays the foundation for sharing prescription information among VAMCs.
> With this version of NDF, a new design of the National Drug files will lay the foundation for timely data releases by Pharmacy Benefits Management (PBM) personnel to field facilities using the NDF Management System. As new drug products are released, this information can be quickly sent to facilities. Pharmacy end users will be able to match (classify) a greater percentage of their local drug files for new products. Update/delivery of data will be controlled by PBM personnel. Frequent updating of NDF will be possible with minimal time for installation and downtime.
> In addition to the redesign of NATIONAL DRUG file (#50.6), Version 4.0 will provide the following enhancements:
- Addition of new fields to NDF, such as National Formulary and restriction indicators.
- Lay foundation for interfaces to other Commercial Off The Shelf (COTS) software to update NDF fields for new/revised drug information.
- Update current NDF with new/revised product information.
- Creation of an Application Programmer’s Interface (API) to accommodate all existing VISTA software Database Integration Agreements (DBIAs) with NDF.
- A clean-up of associated files, such as DRUG MANUFACTURER (#55.95), DRUG UNITS (#50.607), etc.
- Incorporation of approved enhancement requests by Pharmacy/Information Resources Management (IRM) end users.
File Changes
> The NATIONAL DRUG file (#50.6) has been redesigned from a file seven multiples deep to a new file structure of four separate files. The new files are the VA PRODUCT file (#50.68), the NDC/UPN file (#50.67), the VA DISPENSE UNIT file (#50.64), and File \#50.6, which is now the VA GENERIC file.

## Redesigned National Drug File V. 4.0 Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The National Drug File menu has been redesigned and synonyms have been added.

> REMA Rematch/Match Single Drugs \[PSNDRUG\]

> VER Verify Matches \[PSNVFY\]

> SVER Verify Single Match \[PSNVER\]

> MERG Merge National Drug File Data Into Local File \[PSNMRG\]

> AUTO Automatic Match of Unmatched Drugs \[PSNAUTO\]

> CLAS Allow Unmatched Drugs to be Classed \[PSNSTCL\]

> \[Locked: PSNMGR\]

> RPRT National Drug File Reports \[PSNSUBM\]

> LDF Local Drug File Report \[PSNLDG\]

> VAGN Report of VA Generic Names from National Drug \[PSNVAGN\]

> ATMP Report of Attempted Match Drugs \[PSNEXC\]

> PROD A Product Names Matched Report \[PSNPFN\]

> NOCL Local Drugs with No VA Drug Class Report \[PSNOCLS\]

> CLVA VA Drug Classification \[PSNCLS\]

> DFL NDF Info from Your Local Drug File \[PSNRPT\]

> SUPL Supply (XA000) VA Class Report \[PSNSUPLY\]

> MANC Manually Classed Drugs Report \[PSNMCLS\]

> NMAT Local Drugs with NO Match to NDF Report \[PSNONDF\]

> \*LOCF Local Formulary Report \[PSNFRMLY\] \[Locked: PSNMGR\]

> NATF National Formulary Report \[PSNNFL\]

> DDIN Drug-Drug Interaction Report \[PSNTER\]

> CMOP VA Products Marked for CMOP Transmission \[PSNCMOP\]

> PNCL VA Product Names By Class Report \[PSNCLPR\]

> INQ Inquiry Options \[PSNQUER\]

> LINQ Inquire to Local Drug File \[PSNVIEW\]

> \*\*PNIN Inquire to VA Product Info For Local Drug \[PSNLOOK\]

> NDCU NDC/UPN Inquiry \[PSNUPN\]

> PMIS Print a PMI Sheet \[PSNPMIS\]

> \* Formerly *Formulary Report*

> \*\* Formerly *Lookup National Drug Info in Local File.*Changes and Enhancements

> Several option names have been changed to better reflect the performance of the option. Five new options have been added to allow the user access to more reports and added inquiry information.

> *Option Name Changes*

> The *Lookup National Drug Info In Local File* option has been renamed *Inquire to VA Product Info For Local Drug* \[PSNLOOK\] and can be found under the *Inquiry Options* \[PSNQUER\] menu.

> The *Formulary Report* option has been renamed *Local Formulary Report* \[PSNFRMLY\].

*New Options*

> Five new options have been added to assist the user. Four of these options can be found on the National Drug File Reports option menu. The fifth option is located on the *Inquiry Options* menu. They are the following:

- <u>National Formulary Report</u> \[PSNNFL\] – This option allows you to generate a report of National Formulary names marked as National Formulary. This information comes from the VA PRODUCTS file (#50.68).
- <u>Drug-Drug Interaction Report</u> \[PSNTER\] – This option allows you to generate a report of all drug-drug interactions, both critical and significant, contained in the DRUG INTERACTION file (#56).
- <u>VA Products Marked for CMOP Transmission</u> \[PSNCMOP\] – This option allows you to generate a report of all VA Product Names marked for Consolidated Mail Outpatient Pharmacy (CMOP) transmission. You can sort by VA Product Name or by the VA Identifier. This information comes from the VA PRODUCT file (#50.68).
- <u>VA Product Names By Class Report</u> \[PSNCLPR\] – This option generates a report of all VA Product Names sorted by VA Drug Class. You can sort by Primary, Secondary, or Both classes. The information for this report comes from the VA PRODUCT file (#50.68).
- <u>NDC/UPN Inquiry</u> \[PSNUPN\] – With this option you can enter an NDC or UPN to get the corresponding information displayed to the screen. This data comes from the NDC/UPN file (#50.67).

> *Deleted Option*

> The *Match Local Drug File with National File* \[PSNBLD\] option has been deleted.