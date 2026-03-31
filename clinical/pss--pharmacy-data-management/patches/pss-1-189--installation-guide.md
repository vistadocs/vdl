---
title: PSS*1*189 Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: 
app_code: PSS
app_name: "Pharmacy: Data Management"
section: CLI
app_status: active
pkg_ns: PSS
patch_ver: 1
patch_id: PSS*1*189
group_key: "PSS:PSS:1"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - patch
  - install
  - table
  - contents
  - installation
  - dextrose
  - components
  - options
  - solution
  - prompted
page_count: 0
word_count: 1990
section_count: 17
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: June 2016
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Data_Mgmnt_(PDM)/pss_1_p189_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Data_Mgmnt_(PDM)/pss_1_p189_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=93"
---

---
date: "![](pss-1-189-installation-guide/001.png)"
---

PSS\*1.0\*189

INSTALLATIONGUIDE

June 2016

Table of Contents

[Department of Veterans Affairs [i](#_Toc454278438)](http://vaww.esm.infoshare.va.gov/sites/hps/PS_CA/CASDDPEA/PSUIDTS/Shared%20Documents/SQA_Test/pss_1_p189_ig.docx#_Toc454278438)

[Office of Enterprise Development [i](#_Toc454278439)](http://vaww.esm.infoshare.va.gov/sites/hps/PS_CA/CASDDPEA/PSUIDTS/Shared%20Documents/SQA_Test/pss_1_p189_ig.docx#_Toc454278439)

*(This page left blank for two-sided copying.)*

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Patch Components](#patch-components)
  - [Patch PSS\1\189 Components](#patch-pss1189-components)
  - [## <u>Associated Patch Components</u>](#uassociated-patch-componentsu)
  - [Patch IB\2\545 Components](#patch-ib2545-components)
  - [Patch PSJ\5\313 Components](#patch-psj5313-components)
  - [Patch PSN\4\429 Components](#patch-psn4429-components)
  - [Patch PSO\7\444 Components](#patch-pso7444-components)
  - [# Documentation Retrieval Instructions:](#documentation-retrieval-instructions)
- [Pre-Installation Considerations](#pre-installation-considerations)
  - [PSS\1\189](#pss1189)
  - [# Installation Procedure](#installation-procedure)
  - [Installation sequence:](#installation-sequence)
  - [Install Patch PSS\1\189](#install-patch-pss1189)
  - [Install Patch PSO\7\444](#install-patch-pso7444)
  - [Install Patch PSJ\5\313](#install-patch-psj5313)
  - [## Install Patch PSN\4\429](#install-patch-psn4429)
  - [## Install Patch IB\2\545](#install-patch-ib2545)
- [Post Installation Considerations](#post-installation-considerations)
  - [IV Solution Post-Install Automatic Clean-up (Post-install routine)](#iv-solution-post-install-automatic-clean-up-post-install-routine)
This installation guide will describe the setup steps necessary to install patch PSS\*1.0\*189.
This patch is part of the Pharmacy Safety Updates project which was established to address specific New Service Requests (NSRs) as well as some Remedy Tickets related to the VistA Pharmacy applications as approved by the Health Systems Enterprise Systems Manager (ESM).
Although the focus of this installation guide is PSS\*1.0\*189, this project is comprised of patches from five different applications, as shown below. This patch is the only one that has any pre-installation or post installation instructions which requires additional installation information beyond the patch description.
APPLICATION/VERSION PATCH
--------------------------------------------------------------------------------------------------------
PHARMACY DATA MANAGEMENT (PDM) V. 1.0 PSS\*1\*189
OUTPATIENT PHARMACY (OP) V. 7.0 PSO\*7\*444
INPATIENT MEDICATIONS (IM) V.5.0 PSJ\*5\*313
NATIONAL DRUG FILE (NDF) V. 4.0 PSN\*4\*429
INTEGRATED BILLING (IB) V. 2.0 IB\*2\*545
The following New service Requests (NSR) and Remedy Tickets are being addressed by the Pharmacy Safety Updates project which encompasses PSS\*1.0\*189:
1.  Allow Dispensing of Greater Than 90 Day Supply - The Outpatient Pharmacy and supporting VistA applications are being modified to allow dispensing of more than 90 day supply fill for outpatient prescriptions. The new limit will be 365 days and will be set for each drug individually. See below for more information on specific menu options related to this enhancement.  (NSRs 20060601/20111206)
2.  The use of a STRENGTH Property to IV ADDITIVES and Premixed  IV SOLUTIONS - Although patches PSJ\*5\*289 and PSS\*1\*174 introduced quite a few enhancements to the IV Additives and IV Solutions ordering functionality they did not go far enough in addressing all the issues originally in the NSR. This patch will extend the display and selection of the correct IV Additive strength to other components of the Inpatient Medications and Pharmacy Data Management applications. In addition, it will also impose a new rule where an Orderable Item can only have one IV Solution for a specific volume when it is marked to be used in the CPRS IV Fluid Order Entry. (NSR 20110308)
3.  Inactivate Pharmacy Standard Schedule - This enhancement is a conversion of an existing Class III software solution that permits an entry in the ADMINISTRATION SCHEDULE file (#51.1) to be marked as INACTIVE via the Standard Schedule Edit \[PSS SCHEDULE EDIT\] option. Once marked INACTIVE the schedule is automatically removed from the list of schedules to be displayed/chosen when entering an order in CPRS. (NSR 20080907)
4.  Patient Medication Profile Bad Address Indicator display - The Outpatient Pharmacy medication profile has a display problem for a prescription with the following characteristics: 2-letter status (e.g., DC), drug marked for CMOP and Bad Address Indicator. When a prescription with all these three features is displayed, the DAY SUP column value is being truncated. (Remedy 387051)

# Patch Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Patch PSS\*1\*189 Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Files & Fields Associated:

> File Name (#) Field Name (#) New/Modified/Deleted

> ------------------ ----------------------------------- --------------------

> DRUG (#50) MAXIMUM DAYS SUPPLY (#66) New

> MEDICATION INSTRUCTION (#51)

> FREQUENCY (IN MINUTES) (#31) Modified

> ADMINISTRATION SCHEDULE (#51.1)

> FREQUENCY (IN MINUTES) (#2) Modified

> INACTIVE (#12) New

> IV ADDITIVES (#52.6)

> INACTIVATION DATE (#12) Modified

> IV SOLUTIONS (#52.7)

> VOLUME (#2) Modified

> INACTIVATION DATE (#8) Modified

> USED IN IV FLUID ORDER DIALOG (#17) Modified

Templates Associated:

> Template Name Type File Name (#) New/Modified/Deleted

> ------------- ----- ------------------------- --------------------

> PSSCOMMON INPUT DRUG (#50) Modified

> PSSJ SCHEDULE EDIT INPUT ADMINISTRATION SCHEDULE (#51.1) Modified

## ## <u>Associated Patch Components</u>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Patch IB\*2\*545 Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Files & Fields Associated:

> File Name (#) Field Name (#) New/Modified/Deleted

> ------------------ -------------------------------- --------------------

> IB BILL/CLAIMS PRESCRIPTION REFILL (#362.4)

> DAYS SUPPLY (#.06) Modified

## Patch PSJ\*5\*313 Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Patch PSN\*4\*429 Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Files & Fields Associated:

> File Name (#) Field Name (#) New/Modified/Deleted

> ------------------ -------------------------------- --------------------

> VA PRODUCT(#50.68) MAXIMUM DAYS SUPPLY (#32) New

## Patch PSO\*7\*444 Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Files & Fields Associated:

> File Name (#) Field Name (#) New/Modified/Deleted

> ------------------ ----------------------------------- --------------------

> PRESCRIPTION (#52) DAYS SUPPLY (#8) Modified

> RETURN TO STOCK LOG (#52.07)

> DAYS SUPPLY (#4) Modified

> REFILL (#52.1) DAYS SUPPLY (#1.1) Modified

> PENDING OUTPATIENT ORDERS (#52.41)

> DAYS SUPPLY (#101) Modified

## # Documentation Retrieval Instructions:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

-------------------------------------

Updated documentation describing the new functionality introduced by this patch is available.

The preferred method is to retrieve the files from the ANONYMOUS.SOFTWARE directory on <span class="mark">REDACTED</span> using secure file transfer protocol. This transmits the files from the first available SFTP server. Sites may also elect to retrieve files directly from a specific server as follows:

<span class="mark">REDACTED</span>

Documentation can also be retrieved from the VA Software Documentation

Library (VDL) on the Internet at the following address:

http://www.va.gov/vdl.

| File Description                          | File Name           | FTP Mode |
|-----------------------------------------------|-------------------------|--------------|
| Pharmacy Data Management User Manual          | PSS_1_UM_R0616.PDF      | BINARY       |
| Outpatient Pharmacy Pharmacist’s User Manual  | pso_7_phar_um_r0616.PDF | BINARY       |
| Inpatient Medication Pharmacist’s User Manual | psJ_5_pHAR_um_R0616.PDF | BINARY       |
| Inpatient Medication Nurse’s User Manual      | psJ_5_nur_um_R0616.PDF  | BINARY       |
| Inpatient Medication Supervisor’s User Manual | psJ_5_SUPR_um_R0616.PDF | BINARY       |
| Release Notes                                 | PSS_1_P189_RN.PDF       | BINARY       |
| Installation Guide                            | PSS_1_P189_IG.PDF       | BINARY       |

Documentation can also be retrieved from the VA Software Documentation Library (VDL) on the Internet at the following address: <http://www4.va.gov/vdl>.

*(This page left blank for two-sided copying.)*

# Pre-Installation Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## PSS\*1\*189

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IV Solution Pre-Install Manual Clean-up (Environment Check routine).

\*\*\*Please note\*\*\*

The pre-installation environment check routine will only execute in production environments.

An environment check routine will run before the patch is installed to ensure that an orderable item does not have more than one IV Solution with the same volume when they are marked YES to be used in the CPRS IV Fluid Order Entry. If at least one orderable item entry is found, the patch installation will be aborted and a Mailman message will be sent to all users holding the following security keys: PSIVMGR, PSJI MGR, PSNMGR. The message will contain a list of all orderable items that need to be cleaned up, as seen in the sample message below:

Subj: Duplicate IV Solution Volume under same Orderable Item \[#215733\]

From: PATCH PSS\*1\*189 In 'IN' basket. Page 1

-------------------------------------------------------------------------

The list below shows IV Solutions in your database that need to be cleaned up before patch PSS\*1\*189 can be installed.

Rule: An Orderable Item can only have ONE IV solution with a specific volume when it is marked to be used in the IV Order Dialog.

Run Date/Time: Jun 12, 2015@09:49:16

ORDERABLE ITEM(IEN)

IV DISPENSE DRUG(IEN) IV DISPENSE DRUG(IEN)

IV SOLUTION(IEN/VOLUME) IV SOLUTION(IEN/VOLUME)

-------------------------------------------------------------------------------

DEXTROSE

DEXTROSE 20% IN WATER 500ML(2679) DEXTROSE 20% IN WATER 500ML(2679)

20% DEXTROSE(11/500 ML) DEXTROSE 20%(13/500 ML)

20% DEXTROSE(2/500 ML) 20% DEXTROSE(11/500 ML)

20% DEXTROSE(2/500 ML) DEXTROSE 20%(13/500 ML)

DEXTROSE 20% IN WATER 500ML(2679) DEXTROSE 20% 500ML IN 1000ML B(4490)

20% DEXTROSE(11/500 ML) DEXTROSE 20% IN WATER 500ML(18/500 ML)

DEXTROSE 20%(13/500 ML) DEXTROSE 20% IN WATER 500ML(18/500 ML)

20% DEXTROSE(2/500 ML) DEXTROSE 20% IN WATER 500ML(18/500 ML)

DEXTROSE 20% IN WATER 500ML(2679) DEXTROSE 5% 500ML INJ(626)

20% DEXTROSE(11/500 ML) DEXTROSE 5%(42/500 ML)

DEXTROSE 20%(13/500 ML) DEXTROSE 5%(42/500 ML)

20% DEXTROSE(2/500 ML) DEXTROSE 5%(42/500 ML)

## # Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Below is the step-by-step procedure for installing patches.

## Installation sequence:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch PSS\*1\*189 must be installed before PSO\*7\*444 and PSJ\*5\*313. The following is the recommended sequence for the Pharmacy Safety Updates project patches.

1.  PSS\*1\*189
2.  PSO\*7\*444
3.  PSJ\*5\*313
4.  PSN\*4\*429
5.  IB\*2\*545

## Install Patch PSS\*1\*189

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Although this installation will take no longer than 3 minutes, it is recommended that it be installed overnight to prevent any disruption of service to other users.

1.  Use the INSTALL/CHECK MESSAGE option on the PackMan menu.

(when loading the distribution, the following text will display:

“Will first run the Environment Check Routine, PSS189EN”)

2.  From the Kernel Installation & Distribution System (KIDS) menu, select the Installation menu.
3.  From this menu, you may select to use the following options

(when prompted for INSTALL NAME, enter PSS\*1.0\*189)

> a\. Backup a Transport Global - This option will create a backup message of any routines exported with the patch. It will NOT back up any other changes such as DDs or templates.

> b\. Compare Transport Global to Current System - This option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.).

> c\. Verify Checksums in Transport Global - This option will ensure the integrity of the routines that are in the transport global.

> d\. Print Transport Global - This option will allow you to view the components of the KIDS build.

4.  Use the Install Package(s) option and select the package PSS\*1.0\*189.
5.  When prompted "Want KIDS to INHIBIT LOGONs during the install? NO//"

respond NO.

6.  When prompted "Want to DISABLE Scheduled Options, Menu Options, and

Protocols? NO//" respond NO.

## Install Patch PSO\*7\*444

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Although this installation will not take much time, it is recommended that it be installed overnight to prevent any disruption of service to other users.

1\. Use the INSTALL/CHECK MESSAGE option on the PackMan menu.

2\. From the Kernel Installation & Distribution System (KIDS) menu, select the Installation menu.

3\. From this menu, you may select to use the following options

(when prompted for INSTALL NAME, enter PSO\*7.0\*444)

> a\. Backup a Transport Global - This option will create a backup message of any routines exported with the patch. It will NOT back up any other changes such as DDs or templates.

> b\. Compare Transport Global to Current System - This option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.).

> c\. Verify Checksums in Transport Global - This option will ensure the integrity of the routines that are in the transport global.

> d\. Print Transport Global - This option will allow you to view the components of the KIDS build.

4\. Use the Install Package(s) option and select the package PSO\*7.0\*444.

5\. When prompted "Want KIDS to INHIBIT LOGONs during the install? NO//"

respond NO.

6\. When prompted "Want to DISABLE Scheduled Options, Menu Options, and

Protocols? NO//" respond NO.

## Install Patch PSJ\*5\*313

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Although this installation will not take much time, it is recommended that it be installed overnight to prevent any disruption of service to other users.

1\. Use the INSTALL/CHECK MESSAGE option on the PackMan menu.

2\. From the Kernel Installation & Distribution System (KIDS) menu, select the Installation menu.

3\. From this menu, you may select to use the following options

(when prompted for INSTALL NAME, enter PSJ\*5.0\*313)

> a\. Backup a Transport Global - This option will create a backup message of any routines exported with the patch. It will NOT back up any other changes such as DDs or templates.

> b\. Compare Transport Global to Current System - This option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.).

> c\. Verify Checksums in Transport Global - This option will ensure the integrity of the routines that are in the transport global.

> d\. Print Transport Global - This option will allow you to view the components of the KIDS build.

4\. Use the Install Package(s) option and select the package PSJ\*5.0\*313.

5\. When prompted "Want KIDS to INHIBIT LOGONs during the install? NO//"

respond NO.

6\. When prompted "Want to DISABLE Scheduled Options, Menu Options, and

Protocols? NO//" respond NO.

## ## Install Patch PSN\*4\*429

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Although this installation will not take much time, it is recommended that it be installed overnight to prevent any disruption of service to other users.

1\. Use the INSTALL/CHECK MESSAGE option on the PackMan menu.

2\. From the Kernel Installation & Distribution System (KIDS) menu, select the Installation menu.

3\. From this menu, you may select to use the following options

(when prompted for INSTALL NAME, enter PSN\*4.0\*429)

> a\. Backup a Transport Global - This option will create a backup message of any routines exported with the patch. It will NOT back up any other changes such as DDs or templates.

> b\. Compare Transport Global to Current System - This option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.).

> c\. Verify Checksums in Transport Global - This option will ensure the integrity of the routines that are in the transport global.

> d\. Print Transport Global - This option will allow you to view the components of the KIDS build.

4\. Use the Install Package(s) option and select the package PSN\*4.0\*429.

5\. When prompted "Want KIDS to INHIBIT LOGONs during the install? NO//"

respond NO.

6\. When prompted "Want to DISABLE Scheduled Options, Menu Options, and

Protocols? NO//" respond NO.

## ## Install Patch IB\*2\*545

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Although this installation will not take much time, it is recommended that it be installed overnight to prevent any disruption of service to other users.

1\. Use the INSTALL/CHECK MESSAGE option on the PackMan menu.

2\. From the Kernel Installation & Distribution System (KIDS) menu, select the Installation menu.

3\. From this menu, you may select to use the following options

(when prompted for INSTALL NAME, enter IB\*2.0\*545)

> a\. Backup a Transport Global - This option will create a backup message of any routines exported with the patch. It will NOT back up any other changes such as DDs or templates.

> b\. Compare Transport Global to Current System - This option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.).

> c\. Verify Checksums in Transport Global - This option will ensure the integrity of the routines that are in the transport global.

> d\. Print Transport Global - This option will allow you to view the components of the KIDS build.

4\. Use the Install Package(s) option and select the package IB\*2.0\*545.

5\. When prompted "Want KIDS to INHIBIT LOGONs during the install? NO//"

respond NO.

6\. When prompted "Want to DISABLE Scheduled Options, Menu Options, and

Protocols? NO//" respond NO.

*(This page left blank for two-sided copying.)*

# Post Installation Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## IV Solution Post-Install Automatic Clean-up (Post-install routine)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

IV Solutions that are no longer used, meaning that either the IV Solution and/or the Dispense Drug and/or the Orderable Item are marked INACTIVE will have the field USED IN IV FLUID ORDER ENTRY set to 'NO'.

A list of such IV Solutions will be sent to all users holding the following security keys: PSIVMGR, PSJI MGR, and PSNMGR. The message will contain a list of all IV Solutions that have been automatically updated as seen in the sample message below:

Subj: Auto-update of the IV Solution file \[#216328\] 08/18/15@09:58

From: PATCH PSS\*1\*189 In 'IN' basket. Page 1 \*New\*

-------------------------------------------------------------------------

The list below shows IV Solutions in your database that had the field

USED IN IV FLUID ORDER ENTRY set to 'NO' because either the Orderable

Item, the Dispense Drug or the IV Solution itself was marked INACTIVE.

Run Date/Time: Aug 18, 2015@09:58:38

-------------------------------------------------------------------------

ORDERABLE ITEM (IEN)

IV DISPENSE DRUG (IEN)

IV SOLUTION (IEN/VOLUME)

-------------------------------------------------------------------------

CEFAZOLIN (106)

CEFAZOLIN SOD 1GM INJ (1498)

20% DEXTROSE (2/500 ML) \*\*\* INACTIVE DATE: JAN 11, 1994 \*\*\*

20% DEXTROSE (11/500 ML) \*\*\* INACTIVE DATE: JAN 11, 1994 \*\*\*