---
title: Laboratory Version 5.2 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: anchor
doc_subject: null
app_code: LR
app_name: Laboratory
section: CLI
app_status: active
pkg_ns: LR
patch_ver: 5.2
patch_id: LR*5.2
group_key: LR:LR:5.2
file_numbers:
- '2'
- '3'
- '4'
- '6'
- '7'
- '9'
- '10'
- '11'
- '16'
- '17'
- '60'
- '61.2'
- '62'
- '62.06'
- '62.07'
- '62.3'
- '62.4'
- '62.5'
- '62.6'
- '63'
- '63.08'
- '64'
- '64.03'
- '64.05'
- '64.1'
- '64.1999'
- '64.2'
- '64.21'
- '64.22'
- '64.3'
- '64.5'
- '65'
- '65.4'
- '65.5'
- '65.9'
- '65.9999'
- '66'
- '66.2'
- '66.5'
- '66.9'
- '67'
- '67.1'
- '67.4'
- '67.9'
- '67.9999'
- '68'
- '68.2'
- '68.45'
- '69.2'
- '69.9'
- '81'
- '90'
- '95'
- '107'
- '200'
- '501'
- '505'
- '613'
security_keys:
- DIUSER
- LRSUPER
- PROVIDER
menu_options: 1
description: '- Data Dictionary Changes - LABORATORY TEST file (#60) - ETIOLOGY FIELD file (#61.2) - COLLECTION SAMPLE file (#62) - EXECUTE CODE file (#62.07) - [AUTO...'
audience: System administrators, end users reviewing changes
keywords: []
page_count: 0
word_count: 24464
section_count: 91
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: false
is_stub: false
pub_date: October 1994
revision_count: 0
revision_newest: ''
revision_oldest: ''
docx_url: https://www.va.gov/vdl/documents/Clinical/Laboratory/lab52rn.docx
pdf_url: https://www.va.gov/vdl/documents/Clinical/Laboratory/lab52rn.pdf
app_url: https://www.va.gov/vdl/application.asp?appid=71
audit_applied: '2026-05-31'
master_source: Laboratory Version 5.2 Release Notes
master_pub_date: October 1994
consolidated_from: 4 versions
prior_versions:
- LA*5.2*68 Laboratory Release Notes
- LR*5.2*395 Laboratory Release Notes
- LR*5.2*465 Laboratory Release Notes
consolidated_title: laboratory release notes
---

Decentralized Hospital Computer Program

LABORATORYRELEASE NOTES

October 1994

Information Systems Center

Dallas, Texas
# Data Dictionary Changes


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Data Dictionary Changes](#data-dictionary-changes)
  - [LABORATORY TEST file (#60)](#laboratory-test-file-60)
  - [ETIOLOGY FIELD file (#61.2)](#etiology-field-file-612)
  - [COLLECTION SAMPLE file (#62)](#collection-sample-file-62)
  - [EXECUTE CODE file (#62.07)](#execute-code-file-6207)
  - [AUTO INSTRUMENT file (#62.4)](#auto-instrument-file-624)
  - [LAB DATA file (#63)](#lab-data-file-63)
  - [WKLD CODE file (#64)](#wkld-code-file-64)
  - [WKLD LOG FILE file (#64.03)](#wkld-log-file-file-6403)
  - [## ## NON WKLD PROCEDURES file (#64.05)](#non-wkld-procedures-file-6405)
  - [WKLD DATA file (#64.1)](#wkld-data-file-641)
  - [ARCHIVED WKLD DATA file (#64.19999)](#archived-wkld-data-file-6419999)
  - [WKLD SUFFIX CODES file (#64.2)](#wkld-suffix-codes-file-642)
  - [WKLD CODE LAB SECT file (#64.21)](#wkld-code-lab-sect-file-6421)
  - [WKLD ITEM FOR COUNT file (#64.22)](#wkld-item-for-count-file-6422)
  - [WKLD INSTRUMENT MANUFACTURER file (#64.3)](#wkld-instrument-manufacturer-file-643)
  - [## LAB REPORTS file (#64.5)](#lab-reports-file-645)
  - [BLOOD INVENTORY file (#65)](#blood-inventory-file-65)
  - [BLOOD BANK UTILITY file (#65.4)](#blood-bank-utility-file-654)
  - [BLOOD DONOR file (#65.5)](#blood-donor-file-655)
  - [## LAB LETTER file (#65.9)](#lab-letter-file-659)
  - [ARCHIVED BLOOD INVENTORY file (#65.9999)](#archived-blood-inventory-file-659999)
  - [BLOOD PRODUCT file (#66)](#blood-product-file-66)
  - [BLOOD BANK VALIDATION file (#66.2)](#blood-bank-validation-file-662)
  - [OPERATION (MSBOS) file (#66.5)](#operation-msbos-file-665)
  - [## BLOOD COMPONENT REQUEST file (#66.9)](#blood-component-request-file-669)
  - [REFERRAL PATIENT file (#67)](#referral-patient-file-67)
  - [NON PATIENT WORKLOAD file (#67.4)](#non-patient-workload-file-674)
  - [LAB MONTHLY WORKLOADS file (#67.9)](#lab-monthly-workloads-file-679)
  - [ARCHIVED LAB MONTHLY WORKLOADS file (#67.99999)](#archived-lab-monthly-workloads-file-6799999)
  - [ACCESSION file (#68)](#accession-file-68)
  - [LOAD/WORK LIST file (#68.2)](#loadwork-list-file-682)
  - [GROUP USER MANUAL file (#68.45)](#group-user-manual-file-6845)
  - [LAB SECTION PRINT file (#69.2)](#lab-section-print-file-692)
  - [LABORATORY SITE file (#69.9)](#laboratory-site-file-699)
  - [## LAB JOURNAL (File 95)](#lab-journal-file-95)
  - [## Donor menu \[LRBLD\] changes](#donor-menu-lrbld-changes)
  - [### Donor Options](#donor-options)
  - [Inventory menu \[LRBLI\] changes](#inventory-menu-lrbli-changes)
    - [Disposition - not transfused \[LRBLIDN\]](#disposition-not-transfused-lrblidn)
    - [Disposition-relocation \[LRBLIDR\]](#disposition-relocation-lrblidr)
    - [Shipping invoices for blood components \[LRBLISH\]](#shipping-invoices-for-blood-components-lrblish)
    - [Inventory ABO/Rh testing worksheet \[LRBLIW\]](#inventory-aborh-testing-worksheet-lrbliw)
    - [### Enter crossmatch results \[LRBLPX\]](#enter-crossmatch-results-lrblpx)
  - [Blood bank patient \[LRBLP\] Changes](#blood-bank-patient-lrblp-changes)
    - [Specimen log-in \[LRBLPLOGIN\]](#specimen-log-in-lrblplogin)
  - [Inquiry menu \[LRBLQ\] Changes](#inquiry-menu-lrblq-changes)
    - [Inquiry Options](#inquiry-options)
    - [Single donor demographic information \[LRBLQSDD\]](#single-donor-demographic-information-lrblqsdd)
  - [### Patient Medication List \[LRBLPH\]](#patient-medication-list-lrblph)
  - [### Patient blood bank record \[LRBLQDR\]](#patient-blood-bank-record-lrblqdr)
    - [### #### Old Version Problem (E3R 89-38, 91-118)](#old-version-problem-e3r-89-38-91-118)
    - [Single donor information \[LRBLQSD\]](#single-donor-information-lrblqsd)
    - [### ### Validation documentation \[LRBLVALI\]](#validation-documentation-lrblvali)
  - [Report menu \[LRBLR\] changes](#report-menu-lrblr-changes)
    - [Print single BB patient report \[LRBLP PRINT SINGLE\]](#print-single-bb-patient-report-lrblp-print-single)
    - [Blood bank consultation reports \[LRBLCN\]](#blood-bank-consultation-reports-lrblcn)
    - [Units available (indate/no disposition) \[LRBLRUA\]](#units-available-indateno-disposition-lrblrua)
    - [Transfusion reaction count \[LRBLTA\]](#transfusion-reaction-count-lrblta)
    - [Phenotyped units available \[LRBLIPH\]](#phenotyped-units-available-lrbliph)
    - [### ### Crossmatch/Transfusions by Specialty/Physician \[LRBLAA\]](#crossmatchtransfusions-by-specialtyphysician-lrblaa)
    - [Autologous Disposition report \[LRBLJB\]](#autologous-disposition-report-lrbljb)
    - [### Transfused RBC for treating specialty \[LRBLJUT\]](#transfused-rbc-for-treating-specialty-lrbljut)
    - [### Transfusion by treating specialty/physician \[LRBLITS\]](#transfusion-by-treating-specialtyphysician-lrblits)
    - [Blood bank administrative data \[LRBLA\]](#blood-bank-administrative-data-lrbla)
    - [Print blood bank validation \[LRBVALP\]](#print-blood-bank-validation-lrbvalp)
  - [Supervisor menu \[LRBLS\] changes](#supervisor-menu-lrbls-changes)
    - [Edit Donor History Questions \[LRBLSEH\]](#edit-donor-history-questions-lrblseh)
    - [Edit unit disposition fields \[LRBLSED\]](#edit-unit-disposition-fields-lrblsed)
    - [Edit pooled blood product \[LRBLJM\]](#edit-pooled-blood-product-lrbljm)
    - [Edit blood bank utility file \[LRBLSEU\]](#edit-blood-bank-utility-file-lrblseu)
    - [Blood component request edit \[LRBLSRQ\]](#blood-component-request-edit-lrblsrq)
  - [#### New Version](#new-version)
  - [This new option allows the editing of requests for blood components.](#this-new-option-allows-the-editing-of-requests-for-blood-components)
    - [Blood Bank validation documentation \[LRBLVAL\]](#blood-bank-validation-documentation-lrblval)
  - [#### New Version](#new-version-1)
    - [Unknown unit transfusion reaction \[LRBLPTXR\]](#unknown-unit-transfusion-reaction-lrblptxr)
    - [Blood bank inventory integrity report \[LRBLII\]](#blood-bank-inventory-integrity-report-lrblii)
    - [Remove units with final disposition \[LRBLSER\]](#remove-units-with-final-disposition-lrblser)
    - [Blood bank workload \[LRBLSW\]](#blood-bank-workload-lrblsw)
    - [### Display workload for an accession \[LRUWL\]](#display-workload-for-an-accession-lruwl)
  - [General Functionality Changes](#general-functionality-changes)
    - [Transfusion Reaction Records Changes](#transfusion-reaction-records-changes)
    - [OPERATION (MSBOS) file (#66.5)](#operation-msbos-file-665-1)
    - [BLOOD COMPONENT REQUEST file (#66.9)](#blood-component-request-file-669-1)
    - [Data compilation for Workload](#data-compilation-for-workload)
  - [## Data entry, anat path menu \[LRAPD\] changes](#data-entry-anat-path-menu-lrapd-changes)
    - [### Provisional anatomic diagnosis, \[LRAPAUPAD\]](#provisional-anatomic-diagnosis-lrapaupad)
    - [#### New Version](#new-version-2)
    - [FS/Gross/Micro/Dx \[LRAPDGM\]](#fsgrossmicrodx-lrapdgm)
    - [### ### Supplementary Report, Anat Path \[LRAPDSR\]](#supplementary-report-anat-path-lrapdsr)
  - [Edit/modify data, anat path menu \[LRAPE\] changes](#editmodify-data-anat-path-menu-lrape-changes)
    - [Edit log-in & clinical hx, anat path \[LRAPED\]](#edit-log-in-clinical-hx-anat-path-lraped)
    - [Modify anat path gross/micro/dx/frozen section \[LRAPM\]](#modify-anat-path-grossmicrodxfrozen-section-lrapm)
    - [Edit anat path comments \[LRAPEDC\]](#edit-anat-path-comments-lrapedc)
  - [Inquiries, anat path menu \[LRAPI\] changes](#inquiries-anat-path-menu-lrapi-changes)
    - [Search options, anat path \[LRAPSEARCH\]](#search-options-anat-path-lrapsearch)
  - [Log-in menu, anat path menu \[LRAPL\] changes](#log-in-menu-anat-path-menu-lrapl-changes)
  - [### Log-in, anat path \[LRAPLG\]](#log-in-anat-path-lraplg)
    - [Print log book \[LRAPBK\]](#print-log-book-lrapbk)
  - [#### Old Version Problem (E3R 92-06, 92-37)](#old-version-problem-e3r-92-06-92-37)
  - [Print, anat path menu \[LRAPP\] changes](#print-anat-path-menu-lrapp-changes)
    - [Print single report only \[LRAP PRINT SINGLE\]](#print-single-report-only-lrap-print-single)
  - [If an autopsy is logged into the REFERRAL PATIENT file (#67), you cannot get a printed report using the print options like Print Single Report \[LRAP\]. The patient name prompt only appears in upper case letters so you can't access the REF: file.](#if-an-autopsy-is-logged-into-the-referral-patient-file-67-you-cannot-get-a-printed-report-using-the-print-options-like-print-single-report-lrap-the-patient-name-prompt-only-appears-in-upper-case-letters-so-you-cant-access-the-ref-file)
    - [Alphabetical autopsy list \[LRAPAUA\]](#alphabetical-autopsy-list-lrapaua)
    - [Path cases by resident, tech, senior or clinician \[LRAPAUL\]](#path-cases-by-resident-tech-senior-or-clinician-lrapaul)
    - [% Pos, Atyp, Dysp, Neg, Susp, Unsat cytopath \[LRAPCYPCT\]](#pos-atyp-dysp-neg-susp-unsat-cytopath-lrapcypct)
    - [Accession list with stains \[LRAPSA\]](#accession-list-with-stains-lrapsa)
    - [Autopsy Slide Labels \[LRAUMLK\]](#autopsy-slide-labels-lraumlk)
    - [Anatomic Path slide Labels \[LRAPLM\]](#anatomic-path-slide-labels-lraplm)
    - [### Cum path data summaries \[LRAPT\]](#cum-path-data-summaries-lrapt)
  - [## Supervisor, anat path menu \[LRAPSUPER\] changes](#supervisor-anat-path-menu-lrapsuper-changes)
    - [Delete anat path descriptions by date \[LRAPDAR\]](#delete-anat-path-descriptions-by-date-lrapdar)
    - [Edit pathology parameters \[LRAPHDR\];](#edit-pathology-parameters-lraphdr)
    - [Print path modifications \[LRAPMOD\]](#print-path-modifications-lrapmod)
    - [Frozen section, surgical path correlation \[LRAPQAFS\]](#frozen-section-surgical-path-correlation-lrapqafs)
  - [### Malignancy review \[LRAPQAMR\]](#malignancy-review-lrapqamr)
    - [QA outcome review cases \[LRAPQOR\]](#qa-outcome-review-cases-lrapqor)
    - [10% Random case review, surg path \[LRAPQAR\]](#10-random-case-review-surg-path-lrapqar)
    - [### #### Old Version Problem (E3R 92-31)](#old-version-problem-e3r-92-31)
    - [AFIP registries \[LRAPAFIP\]](#afip-registries-lrapafip)
    - [Persian Gulf Veterans \[LRAPPG\]](#persian-gulf-veterans-lrappg)
    - [Anatomic pathology turnaround time \[LRAPTT\]](#anatomic-pathology-turnaround-time-lraptt)
    - [### Move anatomic path accession \[LRAPMV\]](#move-anatomic-path-accession-lrapmv)
    - [Edit Referral patient file \[LRUV\]](#edit-referral-patient-file-lruv)
  - [Clinician options, anat path menu \[LRAPMD\] changes](#clinician-options-anat-path-menu-lrapmd-changes)
    - [Edit/print/display preselected lab tests \[LRUMD\]](#editprintdisplay-preselected-lab-tests-lrumd)
    - [Autopsy protocol/supplementary report \[LRAPAUPT\]](#autopsy-protocolsupplementary-report-lrapaupt)
    - [Print surgical pathology report for a patient \[LRAPSPSGL\]](#print-surgical-pathology-report-for-a-patient-lrapspsgl)
  - [Workload, anat path menu \[LRAPW\] changes](#workload-anat-path-menu-lrapw-changes)
    - [Cytopathology screening workload \[LRAPWR\]](#cytopathology-screening-workload-lrapwr)
    - [Display workload for an accession \[LRUWL\]](#display-workload-for-an-accession-lruwl-1)
    - [EM scanning and photo workload \[LRAPWE\]](#em-scanning-and-photo-workload-lrapwe)
    - [Surg path gross assistance workload \[LRAPWRSP\]](#surg-path-gross-assistance-workload-lrapwrsp)
  - [General Functionality Changes](#general-functionality-changes-1)
    - [Pathology Report Heading](#pathology-report-heading)
    - [Autopsy Assistant field](#autopsy-assistant-field)
    - [SNOMED Code Field Definition](#snomed-code-field-definition)
    - [Extended Syntax](#extended-syntax)
    - [Anatomic Pathologist's Name](#anatomic-pathologists-name)
  - [## Phlebotomy menu \[LR GET\] changes](#phlebotomy-menu-lr-get-changes)
    - [Lab order by collection type \[LRRP5\]](#lab-order-by-collection-type-lrrp5)
    - [Print Future Collection Labels \[LRUFCL\]](#print-future-collection-labels-lrufcl)
    - [Print Single Future Collection Labels \[LRUFCLS\]](#print-single-future-collection-labels-lrufcls)
    - [Order/Test Status \[LROS\]](#ordertest-status-lros)
  - [Accessioning menu \[LR IN\] changes](#accessioning-menu-lr-in-changes)
    - [Accessioning tests ordered by ward order entry \[LROE\]](#accessioning-tests-ordered-by-ward-order-entry-lroe)
  - [## Version 5.2 will not do this.](#version-52-will-not-do-this)
    - [Fast Lab Test Order (SEND PATIENT) \[LROW SEND PAT\]](#fast-lab-test-order-send-patient-lrow-send-pat)
  - [#### Old Version Problem (E3R 90-54)](#old-version-problem-e3r-90-54)
  - [## Version 5.2 will not allow the entry of past dates for orders.](#version-52-will-not-allow-the-entry-of-past-dates-for-orders)
    - [Fast Lab Test Order (SEND PATIENT) \[LROW SEND PAT\]](#fast-lab-test-order-send-patient-lrow-send-pat-1)
    - [Fast Lab Test Order (IMMEDIATE COLLECT) \[LROW IMMED COLLECT\]](#fast-lab-test-order-immediate-collect-lrow-immed-collect)
    - [Manual Enter Clinic Stop Codes \[LRSTOPC\]](#manual-enter-clinic-stop-codes-lrstopc)
    - [Multipurpose accessioning \[LRQUICK\]](#multipurpose-accessioning-lrquick)
    - [Reprint order accession label(s) \[LRLABXOL\]](#reprint-order-accession-labels-lrlabxol)
  - [Process data in lab menu \[LR DO!\] changes](#process-data-in-lab-menu-lr-do-changes)
    - [All Enter/Verify options](#all-enterverify-options)
    - [Enter/verify/modify data (manual) \[LRENTER\]](#enterverifymodify-data-manual-lrenter)
    - [Misc. processing \[LR PROCESS, MISC\]](#misc-processing-lr-process-misc)
    - [WKLD log file download \[LRCAPDL\]](#wkld-log-file-download-lrcapdl)
    - [Rollover Accession (Manual) \[LR ROLLOVER\]](#rollover-accession-manual-lr-rollover)
    - [Std/QC/Reps Manual Workload count \[LR WKLD STD/QC/REPS\]](#stdqcreps-manual-workload-count-lr-wkld-stdqcreps)
  - [Quality control menu \[LRQCM\] changes](#quality-control-menu-lrqcm-changes)
    - [Add/Edit QC Name and/or Edit Test Names \[LRQCADDNAME\]](#addedit-qc-name-andor-edit-test-names-lrqcaddname)
    - [Quality control display (Levy-Jennings) \[LRQC\]](#quality-control-display-levy-jennings-lrqc)
  - [Results menu \[LR OUT\] changes](#results-menu-lr-out-changes)
    - [Interim report \[LRRP2\]](#interim-report-lrrp2)
  - [#### Old Version Problem (NOIS GRJ-1093-50007)](#old-version-problem-nois-grj-1093-50007)
  - [## When using the interim report option, the user had to enter a date for the starting date that was closer to today than the ending date. If this occurred, the user would see a FileMan date as a default on the second try.](#when-using-the-interim-report-option-the-user-had-to-enter-a-date-for-the-starting-date-that-was-closer-to-today-than-the-ending-date-if-this-occurred-the-user-would-see-a-fileman-date-as-a-default-on-the-second-try)
    - [Interim report by Provider \[LRRD\]](#interim-report-by-provider-lrrd)
  - [## When using the interim report options that did not use the patient name as the sorting mechanisms, you were not allowed to select a range of dates.](#when-using-the-interim-report-options-that-did-not-use-the-patient-name-as-the-sorting-mechanisms-you-were-not-allowed-to-select-a-range-of-dates)
  - [#### New Version Correction/Change](#new-version-correctionchange)
  - [Ward lab menu \[LRWARDM\]](#ward-lab-menu-lrwardm)
    - [Lab test order \[LROW\]](#lab-test-order-lrow)
  - [Microbiology menu \[LRMI\] changes](#microbiology-menu-lrmi-changes)
    - [Results entry (batch) \[LRMISTUF\]](#results-entry-batch-lrmistuf)
  - [Results entry \[LRMIEDZ\]](#results-entry-lrmiedz)
    - [Old Version Problem (E3R 88-111, NOIS MAD-1092-40003)](#old-version-problem-e3r-88-111-nois-mad-1092-40003)
    - [Verification of data by supervisor \[LRMIVER\]](#verification-of-data-by-supervisor-lrmiver)
    - [Review Accession Workload \[LR WKLD AUDIT\]](#review-accession-workload-lr-wkld-audit)
    - [Microbiology Trend Report \[LRMITS\]](#microbiology-trend-report-lrmits)
    - [Workload editing for Microbiology](#workload-editing-for-microbiology)
    - [Updated Vitek/Microscan section](#updated-vitekmicroscan-section)
    - [Microbiology Report Status field](#microbiology-report-status-field)
    - [Typo in Micro report Display/Print](#typo-in-micro-report-displayprint)
    - [Microbiology Execute Codes](#microbiology-execute-codes)
    - [MIC Default Interpretation](#mic-default-interpretation)
  - [Supervisor menu \[LRSUPERVISOR\] changes](#supervisor-menu-lrsupervisor-changes)
    - [Manual Queuing of Fileroom Cum \[LRAC MANUAL FILEROOM CUM\]](#manual-queuing-of-fileroom-cum-lrac-manual-fileroom-cum)
    - [Reprint a Permanent Page from Cumulative \[LRAC 1 PAGE\]](#reprint-a-permanent-page-from-cumulative-lrac-1-page)
    - [Add a new WKLD code to file \[LRCAP CODE ADD\]](#add-a-new-wkld-code-to-file-lrcap-code-add)
    - [Convert Archived Data to Use New Person file \[LR ARCHIVE NP CONVERSION\]](#convert-archived-data-to-use-new-person-file-lr-archive-np-conversion)
  - [### Check Files for Inconsistencies \[LRCHKFILES\]](#check-files-for-inconsistencies-lrchkfiles)
    - [Download Format for Intermec Printer \[LR BARCODE FORMAT LOAD\]](#download-format-for-intermec-printer-lr-barcode-format-load)
    - [LIM workload menu \[LR LIM/WKLD MENU\]](#lim-workload-menu-lr-limwkld-menu)
    - [Detail workload report \[LRRP6\]](#detail-workload-report-lrrp6)
    - [Etiology WKLD Codes (Force) \[LRCAPF\]](#etiology-wkld-codes-force-lrcapf)
    - [File 81 conversion \[LRBLPOST\]](#file-81-conversion-lrblpost)
    - [LMIP Reports/Data Collection \[LR WKLD4\]](#lmip-reportsdata-collection-lr-wkld4)
    - [### PHASE 1: Move data from 64.1 to 67.9 \[LR WKLD LMIP 1\]](#phase-1-move-data-from-641-to-679-lr-wkld-lmip-1)
    - [PHASE 2: Collect data for transmit to NDB \[LR WKLD LMIP 2\]](#phase-2-collect-data-for-transmit-to-ndb-lr-wkld-lmip-2)
    - [PHASE 3: Print of data to be sent to NDB \[LR WKLD LMIP 3\]](#phase-3-print-of-data-to-be-sent-to-ndb-lr-wkld-lmip-3)
    - [### PHASE 4: Create E-mail message for NDB \[LR WKLD LMIP 4\]](#phase-4-create-e-mail-message-for-ndb-lr-wkld-lmip-4)
    - [PHASE 5: Purge monthly WKLD data from 67.9](#phase-5-purge-monthly-wkld-data-from-679)
    - [RCS-CDR/LMIP report \[LRCAPM5\]](#rcs-cdrlmip-report-lrcapm5)
    - [### Recompile Phase 1 LMIP data \[LR WKLD LMIP 1 REPEAT\]](#recompile-phase-1-lmip-data-lr-wkld-lmip-1-repeat)
    - [Supervisor workload menu \[LR SUPER/WKLD MENU\]](#supervisor-workload-menu-lr-superwkld-menu)
    - [Treating Specialty Workload Report \[LRCAPTS\]](#treating-specialty-workload-report-lrcapts)
    - [Workload code list \[LRCAPD\]](#workload-code-list-lrcapd)
    - [Workload cost report by major section \[LRCAPML\]](#workload-cost-report-by-major-section-lrcapml)
    - [Workload Report \[LRCAPR1\]](#workload-report-lrcapr1)
    - [Workload statistics by accession area and shift \[LRRP8\]](#workload-statistics-by-accession-area-and-shift-lrrp8)
    - [### Workload Statistics by Major Section \[LRCAPMA\]](#workload-statistics-by-major-section-lrcapma)
    - [Turn on site workload statistics \[LR WKLD STATS ON\]](#turn-on-site-workload-statistics-lr-wkld-stats-on)
    - [### ### Turn on workload stats for accession area \[LR WKLD STATS ON ACC AREA\]](#turn-on-workload-stats-for-accession-area-lr-wkld-stats-on-acc-area)
    - [### ### Re-index Antimicrobial Suscept File (62.06) \[LRMIXALL\]](#re-index-antimicrobial-suscept-file-6206-lrmixall)
    - [Watch the data in the LA global \[LA WATCH\]](#watch-the-data-in-the-la-global-la-watch)
    - [Audit of deleted/edited comments \[LRDCOM\]](#audit-of-deletededited-comments-lrdcom)
    - [Changes in verified lab data \[LRUER\]](#changes-in-verified-lab-data-lruer)
    - [### Search for Critical Value Flagged Tests \[LRSORC\]](#search-for-critical-value-flagged-tests-lrsorc)
  - [## Version 5.2 will allow you to sort by accession area, patient name or location. The collection date is also printed.](#version-52-will-allow-you-to-sort-by-accession-area-patient-name-or-location-the-collection-date-is-also-printed)
    - [Search for High/Low Values of a Test \[LRSORA\]](#search-for-highlow-values-of-a-test-lrsora)
    - [Summary List (Extended Supervisor's) \[LRLISTE\]](#summary-list-extended-supervisors-lrliste)
    - [VA FileMan \[DIUSER\]](#va-fileman-diuser)
    - [Diagram Menus \[XUUSERACC\]](#diagram-menus-xuuseracc)
  - [Technical Changes](#technical-changes)
    - [Hooks for Timing Response Log](#hooks-for-timing-response-log)
    - [Kernel Form Feed Standard](#kernel-form-feed-standard)
    - [File 69.9 - Collection List Build \$H field](#file-699-collection-list-build-h-field)
    - [Programming Change - Locks](#programming-change-locks)
    - [Container Field, LABORATORY TEST file](#container-field-laboratory-test-file)
    - [Misspelling in Routine](#misspelling-in-routine)
    - [Removal of Obsolete Field](#removal-of-obsolete-field)
  - [General Functionality Changes](#general-functionality-changes-2)
    - [Display STAT on Verify Screens](#display-stat-on-verify-screens)
    - [Bar code enhancements](#bar-code-enhancements)
  - [## ### Provider name/title/key](#provider-nametitlekey)
    - [Show Order Comments](#show-order-comments)
    - [Incomplete Test List](#incomplete-test-list)
    - [Display of Provider during Verification](#display-of-provider-during-verification)
    - [Label printing](#label-printing)
    - [### ### New Documentation Subfile](#new-documentation-subfile)
    - [Cumulative Update](#cumulative-update)
    - [Ektachem problems](#ektachem-problems)
    - [LRTASK CONJAM routine change](#lrtask-conjam-routine-change)
  - [Workload Functionality](#workload-functionality)
    - [Updating WKLD code file](#updating-wkld-code-file)
    - [Venipuncture Workload codes](#venipuncture-workload-codes)
    - [E3Rs addressed by Workload rewrite](#e3rs-addressed-by-workload-rewrite)
  - [REFERENCE SECTION](#reference-section)
  - [## ## ## ## ## List of New Options/Menus](#list-of-new-optionsmenus)
  - [List of Deleted Options](#list-of-deleted-options)
  - [List of Options with Menu Text/Name changes](#list-of-options-with-menu-textname-changes)
    - [Menu text changed.](#menu-text-changed)
    - [Name Changed](#name-changed)
    - [Name and Menu Text changed](#name-and-menu-text-changed)
  - [New Help Frames](#new-help-frames)
  - [OE/RR Routines](#oerr-routines)
  - [List of Completed E3R's by Number](#list-of-completed-e3rs-by-number)
- [Index](#index)

## LABORATORY TEST file (#60)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1. AP Multiply Factor (Field .02, Subfile 60.02)

> If procedure is counted more than once, the number of times counted is entered here. This field is only used for cytology workload and labels.

2. Sample WKLD Code (Field 500, Subfile 60.03)

> If this test has a sample type that should have a specific WKLD code associated with it, enter the WKLD code here. For example: Urine electrophoresis always has a urine protein performed, so you would enter the WKLD code for that procedure here. It will only be counted for collection sample of urine.

3. Verify WKLD Code (Field 500)

> There has been a Name Change for this subfile from AMIS/CAP Code to Verify WKLD Code. The WKLD codes for this test are entered here. The codes are captured during verification. Enter only the WKLD codes for the procedures that are done at your hospital for this test.

- Test Multiply Factor: If this WKLD code should be counted more than once, enter the number of times it should be counted to get the total correct workload. If the field is blank, then it will automatically be counted 1 time.
- Protect Suffix: If you wish to prevent the suffix from being converted to another suffix during verification, enter YES in this field. Codes that do not have a .0000 suffix need not be protected. They are not changed during verification.
4. Accession WKLD Code (Field 500.1)

> This is a new subfile. Enter the WKLD code used to identify the accession workload for this test. This field can also be used for prep procedures, for example inoculating culture plates. This WKLD code count will appear on the date the specimen was accessioned into the laboratory. The field functions in the same manner as the WKLD codes, except it doesn't require a completion date to be counted. For Cytology Screening Workload, the appropriate WKLD codes are entered here.

5. Site Notes Date (Field 505)

> This is a new subfile. The site can enter on-line documentation to tests in the file.

## ETIOLOGY FIELD file (#61.2)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. Etiology WKLD Code (Field 11)

> Enter a WKLD code into this new field which can be associated with the isolation and identification of this particular organism. The verifier will be able to select from these entries for additional workload.

## COLLECTION SAMPLE file (#62)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. Collection WKLD Code (Field 500)

> This new field is used for those unique situations when an accession WKLD code cannot be used. For example Bacterial culture test. By using this field you don't have to enter collection samples in the LABORATORY TEST file (#60).

## EXECUTE CODE file (#62.07)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. Execute WKLD Code (Field 500)

> WKLD codes associated with the execute codes are entered into this new multiple field.

2\. Site Notes Date (Field 501)

> This is a new subfile. The site can enter on-line documentation to codes in the file.

## AUTO INSTRUMENT file (#62.4)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. WKLD Method (Field .14)

> This new field will indicate what method the system should use as a default value for workload identification purposes.

2\. WKLD Code Method Name (Field .15)

> This new field is automatically filled in when a selection of WKLD code method name is made. It represents an eye readable name of the code selected.

3\. WKLD Code Suffix (Field .16)

> This new field indicates what suffix should be used as a default value for this instrument.4. Default Auto Micro Test (Field 106)

> This new field is used for the default laboratory test name that is to be used to record workload for each organism when using the automated Microbiology instrument to verify the test.

4\. Direct Device (Field 29)

> This new field is used when bypassing the LSI. It is the name of the device that is used to communicate with a direct connect instrument. This field is a free text pointer to the Device file. It stores the free text name of the device. The name is used in the ^LAPORTXX routine to set IOP before calling ^%ZIS.

5\. Site Notes Date (Field 107)

> This is a new subfile that will contain the date and text (word processing field) of any site notes.

## LAB DATA file (#63)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. Transfusion Reaction Type (Field .11, Subfile 63.017)

> A new field, Transfusion Reaction Type, was added to Transfusion Record (63,.085). This field is a pointer to BLOOD BANK UTILITY file (#65.4) and allows selection of entries from the BLOOD BANK UTILITY file (#65.4) which have a "T" entered in the .02 field, screen. This field contains data for reactions associated with a specific unit.

2\. Transfusion Reaction Date (Field .086)

> A new multiple field was added to File 63 to accommodate reactions which are not associated with specific units. This new multiple (63.0171) includes Transfusion Reaction Date (63.071,.01), Transfusion Reaction Type (63.071,.02), Person Entering Reaction (63.071,.03), and Transfusion Reaction Comment (63.071,1). When an entry is made in the .02 field, the AR cross reference is set.

3\. TC Code (Field 0.14, Subfile 63.02)

> A new field allows Electron Microscopy to have the comparable functionality to Surgical Pathology.

4\. Delayed Report Comment (Field 0.97, Subfile 63.02)

> A new subfile allows Electron Microscopy to record reasons for delayed reports.

5\. Specimen (Field .012, Subfile 63.08)

> Significant changes have been made to subfields of the Specimen multiple for Surgical Pathology to accommodate the implementation of WKLD and changes in generation of slide labels.

6\. Labels to Print (Field .07, Subfield 63.8122)

> A new field, Labels to Print, has been added to keep track of whether the slide label has printed or not.

7\. Delayed Report Comment (Field 0.97, Subfile 63.8)

> A new subfile allows Surgical Pathology to record reasons for delayed reports.

8\. Microscopic Description (Field 1.1, Subfile 63.8)

> The name of the field has been changed to eliminate the "diagnosis" portion, based on the addition of field 1.4. However, this does not automatically change the Report Header text which is stored in the LABORATORY SITE file (#69.9).

9\. Frozen Section (Field 1.3, Subfile 63.8)

> A new field, Frozen Section, has been added to allow the frozen section diagnosis to be entered, reported and stored separately from that of the permanent sections for Surgical Pathology. In order for this field to appear in the appropriate edit templates, it is necessary to indicate such in the Edit Pathology Parameters, \[LRAPHDR\] option.

10\. Surgical Path Diagnosis (Field 1.4, Subfile 63.8)

> A new word processing field has been added to allow separate entry of the 'diagnosis' from that of the microscopic description. This field <u>cannot</u> be purged, as the gross description, microscopic description and the comments fields can; thus, allowing the actual description to be retained in addition to the specimen and the SNOMED coding. This field also appears in the Cum path summary option output. In the next version, this field will also be used to automate the SNOMED coding process.

> In order to activate use of this field, it is necessary to make the necessary changes in the Edit Pathology Reports Parameters option, that is to have the Ask Diagnosis field set to "YES" and to indicate the appropriate text under Report Header 4. If this is done, the text for Report Header 3 should also be changed.

> **NOTE:** Corresponding fields have been also added for Cytology (Subfile 63.09,

field 1.4) and Electron Microscopy (Subfile 63.02, field 1.4).

11\. Specimen (Field .012, Subfield 63.09)

> Significant changes have been made to subfields of the Specimen multiple for Cytology to accommodate the implementation of WKLD and changes in generation of slide labels.

12\. TC Code (Field 0.14, Subfile 63.09)

> A new field allows Cytopathology to have the comparable functionality to Surgical Pathology.

13\. Autopsy Assistant (Field 13.8)

> This new field can contain the name of the autopsy assistant.

14\. Treating Specialty at Death (Field 14.6)

> For quality assurance review purposes, a new field Treating Specialty at Death (63,14.6) has been added to both the Log-in, Anat Path \[LRAPLG\] and the Edit Log-in & Clinical Hx, Anat Path \[LRAPED\] options. If all of the data is entered, it is possible to have data on deaths sort by Service, Treating Specialty, and Physician using the QA Outcome Review Cases \[LRAPQOR\] option in the Supervisor's, Anat Path menu.

15\. Autopsy Release Date/Time (Field 14.7)

Autopsy Released By (Field 14.8)

> Two new fields have been added, they are Autopsy Release Date/Time (63,14.7) and Autopsy Release By (63,14.8). Autopsy reports must now be verified/released in the same manner as surgical path, cytopathology, and electron microscopy in order to make them visible to the clinician.

16\. Provisional Anat Dx Date (Field 14.9)

> A new field, Provisional Anat Dx Date (14.9), has been added to accommodate issuance of an official Provisional Anatomic Diagnosis Report for Autopsies. By having a separate date field, it allows the issuance of this report to be tracked separately from that of the final report. This field is also used for the calculation of the turnaround time for PADs.

## WKLD CODE file (#64)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The name was changed from AMIS/CAP to WKLD CODE. This file contains the list of WKLD codes which are used to compile Laboratory workload statistics. This file is exported with data from the most current test listing. Periodically, this file will be updated with the newest listing plus any current test that was inadvertently over looked.

This file should not be edited directly. The Laboratory program will distribute additional entries at regular intervals.

## WKLD LOG FILE file (#64.03)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is a new file that contains an entry for each WKLD related activity. This file can be used for special costing projects to track at a specific Laboratory site.

## ## ## NON WKLD PROCEDURES file (#64.05)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is a new file that will be used by later versions. This file is not implemented with Version 5.2.

## WKLD DATA file (#64.1)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is a new file that contains the Laboratory Workload data.

## ARCHIVED WKLD DATA file (#64.19999)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is a new file that contains the Laboratory Archive Workload data.

## WKLD SUFFIX CODES file (#64.2)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is a new file that contains a listing of nationally approved Workload Suffix codes. This file should not be edited locally.

## WKLD CODE LAB SECT file (#64.21)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is a new file that contains the lab section to be used for workload recording. This is not the lab section which is used at the local site.

## WKLD ITEM FOR COUNT file (#64.22)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is a new file that contains all of the approved item descriptions used for counting Workload data. This file should not be edited locally.

## WKLD INSTRUMENT MANUFACTURER file (#64.3)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is a new file that contains an approved list of Venders/Manufacturers of Laboratory equipment or test reagents. This file should not be edited locally.

## ## LAB REPORTS file (#64.5)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. File Room Report (Field 3, Subfile 64.52)

> This field is used to designate a report to print to a file room location. It is used in conjunction with fields File Room (#4) and Separate File Room (#17). It allows the cumulative to identify those reports which should be run when a site wishes to print the file room reports and they are doing so on a schedule separate from the regular cumulative.

2\. Blood Bank Reports (Field 3.5)

> Enter "YES" if blood bank results are to be printed along with the cumulative report.

3\. Alternate File Room (Field \#1, Subfile \#64.56)

> This field is used to designate those locations which a site wishes to print to a "FILEROOM" location but which they do not wish to be a standard file room. This could be sites which have satellite clinics which have their own file rooms. The name entered here will cause this location to be sorted to a location called FILE ROOM\_ alternate file room name followed by a 1 or 2 (for example FILE ROOM OPC1) The patients will be sorted in terminal digit order similar to the regular file room. This requires that the site has FILEROOM set to "YES" to sort non inpatients to location FILEROOM.

4\. File Room Report Date (Field 16)

> This field is used if the site wishes to print the FILEROOM location on a different schedule than the regular Cumulative print. If this feature is utilized, the last date the FILEROOM location(s) were printed is stored in this field.

5\. Separate File Room (Field 17)

> This field is used to designate the FILE ROOM Cumulative to be printed on a schedule different from the regular cumulative.

## BLOOD INVENTORY file (#65)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. The \[LRBLIDTM\] template was changed to prevent inappropriate data deletion of the MODIFY TO/FROM multiple.

2\. BAG LOT \# (Field 1.1)

> If the ASK BAG LOT \# field in the BLOOD PRODUCT file 66 is set to "YES", this field is included during component modification using the Disposition-not Transfused option in the Inventory menu. It allows recording of the bag lot \# which is required when the product is transferred to another bag as part of the modification process.

3\. Date/Time Unit Assigned (Field .02, Subfile 65.01)

> This new field records the date/time that a unit is assigned to a patient, mainly for workload capture purposes.

4\. Transfusion Reaction Type (Field 6.8)

> This new field is a pointer to BLOOD BANK UTILITY file (#65.4) and allows selection of entries from the BLOOD BANK UTILITY file (#65.4) which have a "T" entered in the .02 field, Screen.

5\. From/To (Field .03, Subfile 65.091)

> This new field records whether the entry in the MODIFY TO/FROM multiple is "TO" or "FROM." Units in the existing File 65 will have this field completed during the INIT routine \[LRBLSET\].

6 WKLD Code (Field .01, Subfile 65.311)

> This new subfield points to the WKLD CODE file (#64) and provides linkage of workload activity to tests/procedures with associated WKLD codes. It is used to record workload associated with units as it is accumulated.

## BLOOD BANK UTILITY file (#65.4)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. The name of File 65.4 was changed from BLOOD DONOR UTILITY to BLOOD BANK UTILITY.

2\. A new choice was added to the set of codes for Screen (Field .02). "T" will stand for Transfusion Reaction.

## BLOOD DONOR file (#65.5)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. WKLD code (Field 1, Subfile 65.59911)

> This new subfield, located under the Workload Test/Procedure (Field 500) subfile, points to the WKLD CODE file (#64) and provides linkage of workload activity to tests/procedures with associated WKLD codes.

## ## LAB LETTER file (#65.9)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new choice (SHIPPING INVOICE) in the set allows for customized text to appear in the output on the shipping invoice generated by the Shipping Invoices for Blood Components \[LRBLISH\] option.

A new choice (INVENTORY WORKSHEET) in the set allows for customized text to appear in the output on the worksheet generated by the Inventory ABO/Rh Testing Worksheet \[LRBLIW\].

## ARCHIVED BLOOD INVENTORY file (#65.9999)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is a new file that contains the Archived Blood Inventory data.

## BLOOD PRODUCT file (#66)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. Administrative category (Field .26)

> This new field is used by several options to group entries according to the type of component. It is based on the AABB groupings on the annual questionnaire. It must be completed for all entries in File 66 that are currently being used.

2\. Pooled Product (Field .27)

> This new field is used to identify components in the file which are pooled. It is used to help troubleshoot and also to help determine what data should present in the Blood Bank Inventory Integrity Report \[LRBLII\] option.

3\. ASK BAG LOT \# (Field .28)

> This new field is used during component modification in the Inventory menu, Disposition-not Transfused, option to determine whether the bag lot number should be captured for units which require transfer of the product to another bag as part of the modification process. If set to "YES" for the product, the BAG LOT# prompt will be included in the edit template.

4\. WKLD Code (Field 500)

> This new subfield points to the WKLD CODE file (#64) and provides linkage of workload activity to tests/procedures with associated WKLD codes.

## BLOOD BANK VALIDATION file (#66.2)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This new file provides the mechanism for documenting the mandated validation of the Blood Bank software options. Data entry in the file is NOT intended to replace the mandated documentation of the validation testing, including:

> 1\. Observations from testing, for example, screen prints, logging files, printed reports, written transcriptions, data tapes, data disks, etc.

> 2\. A record/log of unusual occurrences, bugs, deviations from the BB User Manual & resolution

> 3\. Final approval by other responsible individuals, including the BB Medical Director and the LIM.

It may be used to replace the documentation of the review, the acceptability/ outcome of the review, the date/signature of approval and the date of implementation.

This file offers longitudinal tracking of validation of the software to include the release of new versions, the installation of patches and the installation of any local modifications.

The content and the formatting of the file is consistent with the worksheets provided in the Blood Bank User Manual and the Technical Manual and complies with the requirements of the American Association of Blood Bank and the Food and Drug Administration.

The two options that allow easy access to this file are Validation Documentation \[LRBLVALI\] and Print Blood Bank Validation \[LRBLVALP\]

## OPERATION (MSBOS) file (#66.5)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This new file will replace the Blood Component Request field (#66) in the CPT file (#81). Previous problems with issuing new updates to the CPT file (#81) have been encountered in that the entries in the Blood Component Request field (#66), which relate the Maximum Surgical Blood Order Schedule, are overwritten. Entries in the OPERATION (MSBOS) File (#66.5) will represent a subset of CPT file (#81) , with the .01 field being a pointer to CPT file (#81). Only those entries in the CPT file (#81) for which there is MSBOS data will be included. For Version 5.2, a conversion routine and corresponding option, File 81 Conversion \[LRBLPOST\], has been included. This option is locked with the LRLIASON key and needs to be run ONLY by those sites who have entries in the Blood Component Request field (#66) in the CPT file (#81).

## ## BLOOD COMPONENT REQUEST file (#66.9)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This renamed file will be used by the Surgery Package for entry of preoperative blood orders, that is for Surgery Package versions after 3.0. In the next release of the Laboratory package, this file will also be used for entry of blood orders other than by the Surgery package and for resolving some difficulties in component requesting and selecting units reported by those facilities which keep red cell units in stock which have different anticoagulants.

The old name of the file was Blood Component.

## REFERRAL PATIENT file (#67)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This name of this file was changed from REFERRAL to REFERRAL PATIENT file.

## NON PATIENT WORKLOAD file (#67.4)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This new file will be developed in a later version to support non-workload functions.

## LAB MONTHLY WORKLOADS file (#67.9)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This file is used to collect workload data in preparation for transmission to the National Database. This is done each month that LMIP reportable statistics are compiled into this file. This file was named WORKLOAD file.

## ARCHIVED LAB MONTHLY WORKLOADS file (#67.99999)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This new file contains archived Lab monthly workload data. Not all sites will make use of this file but if it is used, it makes historical data reports possible.

## ACCESSION file (#68)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. Lab Division (Field .19)

> This new field will be used to determine where a particular accession belongs.

2\. Technologist (Field 3, Subfile 68.04)

> This field was named Tech Initial. The DUZ of the person verifying the test will be stored here. This field previously stored the initials of the technologist verifying the test.

3\. Tally to WKLD (Field 5.1, Subfile 68.04)

> This new field will be set to 1 if WKLD workload is counted. This flag prevents the test from being counted more than once.

4\. WKLD Code (Field 6, Subfile 68.04)

> The workload tallies are stored in these fields. The data is stuffed automatically by routines at the time of verification of the test. The name of this subfile was changed from CAP code to WKLD code.

5\. Identify (Field 7, Subfile 68.04)

> The name of this field has been changed from Test Reason to Identify. This field will be deleted in future versions.

6\. WKLD Suffix (Field 8, Subfile 68.04)

> This new field contains the WKLD code suffix used to identify the method used to verify this particular test. The suffix is stuffed at the time of verification automatically.

7\. Bar Code Print (Field 5)

> Set this new field to YES if bar code labels are to be printed for this accession area. The label printer needs to be correctly defined in the DEVICE and TERMINAL TYPE files.

8\. Reserved (Field 8)

> This new field was created for a future use.

9\. Work Area (Field 9)

> If this accession area is only to be used as a work area in the load/worklist file, set to "YES". The accession area cannot be used to accession specimens to if set to "YES". This new field acts as an on/off flag.

10\. Workload On (Field 10)

> Set this new field to "YES" when ready to turn on the automatic collection of workload data.

11\. Collect STD/QC/Repeats (Field 11)

> Set this new field to "YES" if manual counts for Quality Control are needed. When set to "YES", an additional prompt will appear during verification (at the end of the session not after every entry). The counts entered will be added to all tests the user verified during that particular session. The function of entering this data can be also done by using the option Std/QC/Repeats Manual Workload Count \[LR WKLD STD/QC/REPS\].

## LOAD/WORK LIST file (#68.2)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. WKLD Method (Field .14)

> This new field is a pointer to the WKLD SUFFIX CODES file (#64.2) and will be used as a default response when setting up WKLD code during verification. The WKLD suffix is automatically appended to each WKLD code during verification and is stuffed into the ACCESSION file (#68).

2\. WKLD Code Method Name (Field .15)

> This new field should contain the subsection which should receive credit for workload any time a user selects this worklist.

3\. WKLD Code Suffix (Field .16)

> This new field indicates the standard default method used by this particular Load/Worklist.

4\. Major Accession Area (Field 1)

> This field contains the major accession area which should receive the workload credit. Anytime a user selects this worklist the entry will be used to tally workload.

5\. Lab Subsection (Field 1.5)

> This is the next level down from the Major Accession area. Any example might be, chemistry is the major accession area and Special Chemistry would be the lab subsection.

6\. Work Area (Field 1.7)

> This is the lowest level of work distribution. Generally, this would indicate the work bench where the work is to be done. An example might be Chemistry (major accession area), Special Chemistry (lab sub section), and Drug screens (work area).

7\. Additional Lab Tests (Field 52, Subfile 68.2)

> If this particular work list should have additional workload counts, enter the test in the Laboratory Test file (#60) which contains the verify WKLD codes (field 500) needed. These WKLD codes will be included with each verified accession. An example might be an instrument setup for a batch instrument.

## GROUP USER MANUAL file (#68.45)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This file was created for a future use of allowing a selection of specific data elements for inclusion in a defined group user manual. This functionality will be provided in a future release.

## LAB SECTION PRINT file (#69.2)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. Routine Procedure 1 (Field .11)

> This new field contains the number of times a procedure is routinely performed. For EM the number of thick sections made per block.

2\. Routine Procedure 2 (Field .12)

> This new field contains the number of times a procedure is routinely performed. For EM the number of grids routinely made per block.

3\. Report Header 3 (Field .13)

> A new field has been added to accommodate the header text for the Frozen Section text to appear in the Surgical Pathology Report.

4\. Report Header 4 (Field .14)

> A new field has been added to accommodate the header text for the Diagnosis text to appear in the Surgical Pathology, Cytology, and Electron Microscopy reports.

5\. New Pg. for Supplementary Rpt (Field .21)

> If a page feed is wanted before printing the supplementary report, a "YES" is entered in this new field.

6\. Slide Label (Field .3)

> This new subfile is needed so that the site can enter a 1-9 character label name for their cytology slides rather than using a default choice.

7\. Generic List (Field 6)

> This multiple field was added to accommodate generic labels for autopsy. This information can used by the Blocks, Stains, Procedures \[LRAPSPDAT\] option for the Autopsy area and by the Microscopic slide labels option.

8\. Morphology Entry (Field 12)

> A new multiple field has been added to accommodate the morphology codes to be used by the % Pos, Atyp, Dysp, Neg, Susp, Unsat cytopath \[LRAPCYPCT\] option. This will allow the sites to specify the morphology codes which they commonly use. This is particularly useful for the atypia designations.

## LABORATORY SITE file (#69.9)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. Default Institution (Field 3)

> Certain workload functions are performed in the background without a user being identified. In this circumstance, the system has no way of identifying the institution that the workload should be credited to. This new field contains the default value to be used by the system.

2\. Immed Lab Collect Div. (Field 5.1)

> This new subfile contains the new fields to define wards for Immediate or STAT draws. If defined, a printer within the laboratory will print out all immediate collect orders.

3\. Major Section (Field .1, Subfile 69.98)

This new field is a pointer to the ACCESSION file (#68).

4\. Subsection (Field .11, Subfile 69.98)

This new field is a pointer to the ACCESSION file (#68).

5\. Blood Bank Institution (Field 8.1)

> This new field must be filled in to properly collect the Blood Bank workload.

6\. Default Type for Quick Orders ( Field 5, Subfile 69.99)

> This field used to be named Default Type of Collection. The entry in this field will determine the type of collection that "Quick Orders" will have assigned to them.

7\. Ask Frozen Section (Field 11.1)

> If frozen sections are to be put in a separate field (^DD(63.08,1.3), enter "YES". A "YES" answer will cause an additional prompt to appear during Log-in and data entry which allows the entry of a frozen section diagnoses.

> A new field has been added to determine whether the Frozen Section field in File 63.08 should be included in the appropriate edit templates for data entry in Surgical Pathology.

8\. Ask Surg Path Diagnosis (Field 11.2)

> A new field has been added to determine whether the Surgical Path Diagnosis field (Field 1.4, Subfile 63.08) should be included in the appropriate edit templates for data entry in Surgical Pathology.

> NOTE: Corresponding fields have been also added for Cytology (Field 11.3) and Electron Microscopy (Field 11.4).

9\. Ask Cytopath Diagnosis (Field 11.3)

> If diagnoses are to be put in a separate field, "YES" should be entered.

10\. Ask EM Diagnosis (Field 11.4)

> If diagnosis is to be put in a separate field, "YES" should be entered.

11\. WKLD Stats On (Field 17)

> To have WKLD statistics collected at the time of accessioning and verification, set this new field to "YES". This is the primary switch to turn on workload collection. This entry turns off the entire function. There is also a secondary switch in the ACCESSION file (#68) which allows each accession to be turned on independently. Both fields must be answered "YES" to allow workload data to be accumulated for an accession area.

12\. Log Printer for Routine LC (Field 303)

> This field was renamed from Log Device for LC to Log Printer for Routine LC. This is the device you want the routine Lab Collect requests to print on.

13\. Reserved Field \#1 (Field 304)

> This field was renamed from Send Data to Foreign CPU to Reserved Field \#1. This field is now reserved for future development.

14\. Default OPT Treating Sp. (Field 607)

> This new field is an experimental field that did not get removed from the final release.

15\. LRNIGHT (Field 608)

> This new field is used to prevent two copies of the WORKLOAD data collection routine from being executed at the same time. This field contains the date/time that the WORKLOAD collection routine began processing data. This field is set to null when the process completes. This field should NOT be set through FileMan. To recover after a system failure; delete this entry to allow the workload collection routine to proceed.

16\. Phleb/Stop Code Running (Field 609)

> Do not enter a date in this new field. Doing so may stop the data collection process. The routines will fill in the field during the data collection process and delete the date when the process has gone to a normal completion. If the system goes down during the data collection process, you must delete the date from this field. When the scheduled run time occurs, the data collection will continue automatically. However if the routine errors during the collection process, this field will contain the word "ERROR" followed by the date when the error occurred. If this is the case, you may wish to contact your IRM service for assistance.

17\. Clinic Stop Code (Field 611)

> This new field is to contain the clinic stop code to be used by the laboratory for the MAS package "stop code credit". Generally, the code number is 108.

18\. Counting BB Workload (Field 612)

> This new field is filled in by the workload routine while it processes the Blood Bank workload.

19\. Urgency Alert (Field 613)

> This new field is used as a cutoff level (urgency) to control the flashing of the urgency alert display during verification. Any urgency less (lower number) than this urgency will cause the display to flash.

20\. Transmit Clinic Stop Codes (Field 614)

> This new field should be answered "YES" if you wish the Laboratory Package to automatically stuff clinic stops codes for you. The data is automatically collected but will not be transmitted unless this field is set to "YES".

21\. PCE/VSIT On (Field 615)

> This new field will be used with Visit File when it becomes available. THIS FIELD IS NOT PRESENTLY USED. This field is reserved for future development.

22\. Collect WKLD File Data (Field 616

> This new field controls whether or not data will be accumulated in the WKLD LOG file (#64.03). This WKLD LOG file can be used for special onsite local interest compilations of laboratory workload. There is an option provided to allow the printing of this file with suitable call separators for downloading to spread sheet programs on a PC based system.

## ## LAB JOURNAL (File 95)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This file has been moved into the Laboratory namespace. The name was changed to Lab Journal from Journal.

Enhancements To Blood Bank

## ## Donor menu \[LRBLD\] changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## ### Donor Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 91-37)

There was no field accessible to enter the donor's SSN unless the facility was a Department of Defense site. In order to better track donors, to minimize the chance for duplicate records and to maximize the chance for detecting potential donors with a previous donation history, the SSN was deemed necessary.

#### New Version Correction/Change

The donor SSN can be entered and accessed through all appropriate donor options.

#### Type(s) of Change

#### New Functionality

## Inventory menu \[LRBLI\] changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Disposition - not transfused \[LRBLIDN\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 92-53, 92-55, 93-25)

1\. In Version 5.1, if a unit was modified in the Disposition - Not Transfused option \[LRBLIDN\] and the unit had been restricted for a particular patient, it would not display the modified unit when you got into the Specimen Log In. This was due to the fact that the "AU" cross reference in the BLOOD INVENTORY file (#65) did not get set for the new unit.

2\. In Version 5.1, if a unit was released to inventory from the donor module before testing was completed, no warning message was displayed during future modifications or shipment.

3\. If the bar code reader is used and a component is made into components, the bar code reader is deactivated by the time you get to the next unit that you want to make into components. Fix code to allow bar code reader to be used for next component.

4\. When modifying units in inventory, the default for the expiration date was based on the entry in the DAYS LEFT field for the new component. If that field had no entry, the default became the expiration date of the original unit. No evaluation was done to determine whether the new expiration date being calculated based on the DAYS LEFT field exceeded the original expiration date.

5\. No way currently exists to track the lot numbers of bags used during component modification, for example transfer bags or bags used for freezing red cells. Since it is a FDA requirement, included in Current Good Manufacturing Practices, that this information be recorded, this must currently be recorded manually.

6\. The option would not allow the pooling of platelets with two different types of anticoagulants.

#### New Version Correction/Change

1\. The "AU" cross reference in the BLOOD INVENTORY file (#65) is set for the new unit when the unit is modified in the Disposition not transfused option and has been restricted for a particular patient. The modified unit is displayed when you use Specimen Log In.

2\. In order to add one additional measure to prevent units with positive or incompletely tested disease markers from being inadvertently shipped to another facility, a warning message has been added to both the Disposition - Not Transfused \[LRBLIDN\] and the Shipping Invoices for Blood Components \[LRBLISH\] options.

3\. The bar code reader allows you time to get to the next unit when changing a component to components.

4\. If the calculation of the new expiration date, based on the entry in the DAYS LEFT field in the BLOOD PRODUCT file (#66) for the new component, exceeds the expiration date of the original unit, a warning message

"Expiration date exceeds original unit expiration date xxx OK ? NO// "

is displayed. Since there are some circumstances, such as rejuvenated red cells or frozen red blood cells, in which this would be appropriate, it is possible to indicate such and proceed. If the new date is not appropriate, the field and default are re displayed for editing.

5\. A new field, Ask Bag Lot \# (Field 1.1) was added to the BLOOD INVENTORY file (#65) which will be included in the edit templates used during component modification for those products which require transfer of the product to a bag which was not part of the original donor bag. Whether the prompt appears is dependent on the entry in the new Ask Bag Lot# field, i.e., field .28, in the BLOOD PRODUCT file (#66).

6\. The option will now allow the pooling of platelets with different anticoagulants.

#### Type(s) of Change

1\. Patch to Version 5.1 - new to documentation

2\. New Functionality

3\. New Functionality

4\. New Functionality

5\. Data Dictionary Change

New Functionality

6\. New Functionality

### Disposition-relocation \[LRBLIDR\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3Rs 90-41,91-97)

1\. The option displays products or units in an unorganized manner. This was not a major problem when the patient has only a few units. But when there were many units or products such as for surgery/emergency cases, it was very confusing to choose the unit(s) needed. It also increased the time involved in choosing the unit(s).

2\. There was no checking done if the user indicated that the inspection was unsatisfactory. The unit was still able to be relocated.

3\. If autologous donor has been tested and has an antibody, you are still required to phenotype the unit or you cannot relocate it. It should function like the other autologous functions.

#### New Version Correction/Change

1\. The report groups the products together. The display uses a new field, Administrative Category, (based on the AABB groupings in the annual questionnaire). \* all of the RBC products that are liquid are combined. Within administrative category, it sorts by expiration date and there is a blank line in between each administrative category.

2\. You can no longer release units with an answer of "UNSATISFACTORY" to the "INSPECTION:" prompt.

3\. No checking is done of the Antigen Absent field if it is an autologous unit.

4\. As an additional measure to prevent homologous blood from being issued when there are autologous units available, a flag has been added to the Disposition - Relocation \[LRBLIDR\] option. Any autologous units in the BLOOD INVENTORY file (#65) will be displayed at the beginning of the option.

#### Type(s) of Change

1\. Data Dictionary Change

> Output Redesigned

> New Functionality

2\. New Functionality

> Patch To Version 5.1, new to documentation

3\. New Functionality

4\. New Functionality

### Shipping invoices for blood components \[LRBLISH\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 89-98)

1\. The Blood Bank package-shipping invoice needed to be redone to be more consistent with that of the Red Cross. In addition, the paragraph that stated that the VA facility tested for HIV, Hepatitis, etc. needed to be more sites configurable.

2\. In Version 5.1, if a unit was released to inventory from the donor module before testing was completed, no warning message was displayed during future modifications or shipment.

#### New Version Correction/Change

1\. The lab letter file was used to correct this problem. The site will need to enter a new letter as "SHIPPING INVOICE" in order for this to work (must match exactly). The text to appear should be entered in the Letter Text field. This should include lines to be filled in and signatures.

2\. In order to add one additional measure to prevent units with positive or incompletely tested disease markers from being inadvertently shipped to another facility, a warning message has been added to both the Disposition - Not Transfused \[LRBLIDN\] and the Shipping Invoices for Blood Components \[LRBLISH\] options.

#### Type(s) of Change

#### 1\. Data Dictionary Change

2\. New Functionality

### Inventory ABO/Rh testing worksheet \[LRBLIW\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 92-86)

The text, which appears at the bottom of the Inventory testing worksheet, should reflect the key (code or legend) to illustrate and give meaning to numbers, letters and abbreviations used to record observed results and interpretations. This text has previously not been editable by the sites unless there was a local modification to the routine.

#### New Version Correction/Change 

The Lab Letter File based on the "INVENTORY WORKSHEET" entry now controls the text, which appears at the bottom of the Inventory testing worksheet. This will allow the text to match the key used at that specific facility.

Since the name of the letter is hard coded in the routine, the name must be an exact match. Use the Edit Lab Letter File \[LRBLSLL\] option in the Supervisor's menu to create the new entry, specifying 'letter' as the screen.

#### Type(s) of Change

#### New Functionality

### ### Enter crossmatch results \[LRBLPX\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem

The Crossmatch Comment was a free text field and could not take advantage of the LAB DESCRIPTION file (#62.5).

#### New Version Correction/Change

The Crossmatch Comment field now points to the LAB DESCRIPTION file (#62.5).

#### #### Type(s) of Change

#### New Functionality

Data Dictionary change

## Blood bank patient \[LRBLP\] Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Specimen log-in \[LRBLPLOGIN\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 93-02)

While in this option, an error would occur if the patient's movement had not been completed.

#### New Version Correction/Change

#### This has been corrected.

#### Type(s) of Change

#### New Functionality

## Inquiry menu \[LRBLQ\] Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Inquiry Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 91-37)

There was no field accessible to enter the donor's SSN unless the facility was a Department of Defense site. In order to better 33track donors, to minimize the chance for duplicate records and to maximize the chance for detecting potential donors with a previous donation history, the SSN was deemed necessary.

#### New Version Correction/Change

The donor SSN can be entered and accessed through all appropriate inquiry options.

#### Type(s) of Change

#### New Functionality

### Single donor demographic information \[LRBLQSDD\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version

This is a new option to display a donor's demographic data.

#### Type(s) of Change

#### New Option

## ### Patient Medication List \[LRBLPH\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 91-96)

Although the drugs were displayed when a positive direct antiglobulin test was entered through \[LRBLPET\], there was not a way to print the information.

#### New Version Correction/Change

The ability to print the inpatient and outpatient medication has been added.

#### Type(s) of Change

#### New Option

## ### Patient blood bank record \[LRBLQDR\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### ### #### Old Version Problem (E3R 89-38, 91-118)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If the report was displayed on the CRT, you were prompted for another patient name after it finished. If the report was sent to a printer, after queuing it, the prompt returns to the Blood Bank Inquire menu. If printing a number of patients, you had to keep reselecting the option for each one. No capability existed for selecting a date range or a specific component. The output was always all inclusive.

#### New Version Correction/Change

This option now allows:

• Specification of a date range

• Inclusion of all or selected components

• Inclusion of either detailed summary or only totals

• Selection of more than 1 patient at a time

#### Type(s) of Change

#### New Functionality

New Prompt

Output Redesigned

### Single donor information \[LRBLQSD\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 90-79)

If you need to look up information on a single donor unit and you use the Single Donor Information \[LRBLQSD\] option, the option gives you ALL the information on the donor. If the donor is a regular donor, you will get pages of information. If you send it to the screen, you have a hard time finding the unit you are looking for.

#### New Version Correction/Change

Instead of being a FileMan dump, the entire output has been redesigned. There is a new prompt asking whether you want a single donation or all donations. It allows entry of either the donor name or the donor ID to get the information. If you say you want a single donation record, it displays a list of the donation dates and associated unit IDs to select from. In addition, the output is hard coded to make it a little easier to read and a little more compressed.

#### Type(s) of Change

New Functionality

New Prompt

Output Redesigned

### ### ### Validation documentation \[LRBLVALI\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version

This option allows user to view the entries for the validation documentation by option name. This information is stored in the new file, BLOOD BANK VALIDATION file (#66.2).

#### Type(s) of Change

#### New Option

## Report menu \[LRBLR\] changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Print single BB patient report \[LRBLP PRINT SINGLE\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (NOIS MIW-1291-40002)

The Blood Bank patient report options should document the physician's name on the reports.

The NOIS call reported that the Print single BB patient report \[LRBLP PRINT SINGLE\] option would give duplicate reports of changes in a patients data.

#### New Version Correction/Change

The reports now contain the physician's name.

The Print single BB patient report \[LRBLP PRINT SINGLE\] option now shows only one set of change data reports.

#### Type(s) of Change

New Functionality

Output Redesigned

### Blood bank consultation reports \[LRBLCN\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version

This new option allows the semiautomatic production of consultation reports on patients with alloantibodies or a positive direct antiglobulin test.

#### Type(s) of Change

#### New Option

### Units available (indate/no disposition) \[LRBLRUA\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 89-37)

No report existed which indicated the patient for whom the Autologous and Directed Donor Units were restricted. This information was only available when the units were crossmatched. This required keeping a separate list to answer inquiries about unit availability.

#### #### New Version Correction/Change

The information is included on the Unit Available report. The header shows \* for Autologous/Directed, then the report prints \* followed by the patient's name and if the unit is currently assigned, the specimen date appears.

#### Type(s) of Change

#### New Functionality

Output Redesigned

### Transfusion reaction count \[LRBLTA\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version

This is a new option that evaluates those transfusion reactions that are associated with units. This option provides tallies of reactions by type and component for a specified disposition date range. This option replaces the Transfusion Reaction Report \[LRBLIPTR\] option which has been deleted from the Report menu.

#### Type(s) of Change

#### New Option

### Phenotyped units available \[LRBLIPH\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 89-92)

The option was somewhat limited in that it:

1\. only permitted selection of one component at a time

2\. did not differentiate between units available and those already cross matched and assigned to another patient.

#### New Version Correction/Change

The capability to select a group of related components, such as, all liquid red blood cell products, based on the Administrative Category, has been added. The output was changed to indicate current unit status, such as, the unit was assigned to a patient.

#### Type(s) of Change

#### New Functionality

Output Redesigned

### ### ### Crossmatch/Transfusions by Specialty/Physician \[LRBLAA\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 89-69)

The option, Crossmatch: Transfusion report did not list the crossmatches by location and this functionality was needed. In addition, there was not a report, which allowed data retrieval by treating specialty/physician.

#### New Version Correction/Change

In order to meet the requirements of the Joint Commission for the Accreditation of Healthcare Organizations (JCAHO), data was needed to determine ordering patterns by treating specialty/physician. This option creates such a report and is located in the Blood Utilization & Summary Reports menu under the Reports menu.

#### Type(s) of Change

#### New Functionality

New Option

### Autologous Disposition report \[LRBLJB\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem

There was not an easy way to evaluate autologous unit usage patterns.

#### New Version Correction/Change

A new option has been added which allows review of autologous units according to type of disposition. In addition to the patient identification and the unit information, the number of days in inventory is calculated. By printing both types of reports, it is easy to evaluate the number of units available and the number of units transfused to determine the rate of over ordering. If the listing of transfused patients is also compared to the transfusion record for those patients, it is also possible to calculate the rate of under utilization, that is those patients who also required homologous (allogeneic) units.

#### Type(s) of Change

#### New Functionality

New Option

### ### Transfused RBC for treating specialty \[LRBLJUT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem

No easy way existed to evaluate unit usage patterns by treating specialty or surgical procedure. This made calculation of data for the Maximum Surgical Blood Order Schedule very difficult.

#### New Version Correction/Change

This new option has been added which allows review of all red cell components by treating specialty.

If the listing of transfused patients is also compared to the patients undergoing surgical procedures for that treating specialty for a given time period, it is possible to calculate the information needed to establish the appropriate Maximum Surgical Blood Order Schedule or to perform periodic audits for Transfusion Committee review.

#### Type(s) of Change

#### New Functionality

New Option

### ### Transfusion by treating specialty/physician \[LRBLITS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version

This option prints a report that contains both physicians names and treating specialty.

The name was changed from Transfusion Statistics by Specialty to Transfusion by Treating Specialty/Physician.

#### Type(s) of Change

#### New Functionality

Name Change

### Blood bank administrative data \[LRBLA\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version

This new option generates a report consolidating data from BLOOD INVENTORY file (#65) and BLOOD DONOR file (#65.5) into a single report. The format selected is compatible with the data requested on the American Association of Blood Banks (AABB) questionnaire. A new field, Administrative Category, (.26) has been added to the BLOOD PRODUCT file (#66).

#### Type(s) of Change

#### New Functionality

Data Dictionary change

New Option

### Print blood bank validation \[LRBVALP\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version Correction/Change

This option prints the blood bank validation records stored in the new file, BLOOD BANK VALIDATION file (#66.2). The content and the formatting of the file is consistent with the worksheets provided in the Blood Bank User Manual and the Technical Manual and complies with the requirements of the American Association of Blood Bank and the Food and Drug Administration.

#### Type(s) of Change

#### New Option

New Functionality

## Supervisor menu \[LRBLS\] changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Edit Donor History Questions \[LRBLSEH\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version Correction/Change

The field containing the donor history questions has been changed from a multiple to a word-processing field. This allows for easier editing of the donor history form.

#### Type(s) of Change

#### New Functionality

### Edit unit disposition fields \[LRBLSED\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (Issued as patch to V. 5.1)

If you deleted the disposition for a unit in Version 5.1, it deleted the modified to/from multiple node 9 of the global. If you were deleting a disposition of "TRANSFUSED" and the unit is "pooled platelets", the modified to/from multiple was deleted.

#### New Version Correction/Change

A warning message is displayed to indicate that deleting of the disposition will delete the modification information. In addition, a new option, Edit Pooled Blood Product \[LRBLJM\], was added to edit pooled products.

#### Type(s) of Change

#### Patch to Version 5.1 - new to documentation

### Edit pooled blood product \[LRBLJM\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 89-11)

In order to edit the information regarding a pooled product, it was necessary to use the Edit Unit Disposition Fields \[LRBLSED\] option. This was only possible once the pooled product had a disposition and was cumbersome to utilize. In addition, changes had to be made for both the pooled product and for the individual units which comprised the pool.

#### New Version Correction/Change

Information regarding the contents of a pooled product can be edited using this option, that is units can be added to or deleted from the pool. The appropriate data is automatically updated for all of the units using this option. This option is in the Blood Bank Inventory Edit Option menu under the Supervisors menu.

#### Type(s) of Change

#### New Functionality

New Option

### Edit blood bank utility file \[LRBLSEU\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version

This option now allows you to make use of the new choice in the set of codes for Screen (Field .02). The new choice is "T" for Transfusion Reaction.

The name of the option has been changed to reflect the name change of the file (from Edit Donor Utility File to Edit Blood Bank Utility File).

#### Type(s) of Change

#### New Functionality

Name Change

### Blood component request edit \[LRBLSRQ\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## #### New Version 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## This new option allows the editing of requests for blood components.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Type(s) of Change

#### New Option

### Blood Bank validation documentation \[LRBLVAL\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## #### New Version 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This new option allows the documentation of the validation of blood bank options

#### Type(s) of Change

#### New Option

### Unknown unit transfusion reaction \[LRBLPTXR\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version

Data entry for transfusion reactions for which there is no unit associated is done using this new option under the Blood Bank Patient Edit Options \[LRBLSP\] option in the Supervisor's menu. This allows entry of the reaction type, as defined in File 65.4, and a free text transfusion reaction comment as well as the transfusion reaction date.

#### Type(s) of Change

#### New Option

### Blood bank inventory integrity report \[LRBLII\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 92-15)

Since Version 5.1, the code was added which looked at the product names in the blood products file. If the name contained the word "pool", the program assumed that your lab would modify this product. It then checked for your modification data. If your local blood supplier supplied products already labeled "Pooled Plts" or "Pooled Cryoprecipitate", the "pool" name created problems with the integrity report, which is all of these units were identified as missing modification information. The only way around this was to locally remove the code, rename the products or wade through a thick error report.

#### New Version Correction/Change

There are 2 new fields in the BLOOD PRODUCT file (#66).

.26 Administrative Category: This field is based on the AABB groupings.

.27 Pooled Product: The logic does not look for the word "POOL" in the name field.

If .26 is either Random Platelets or Cryoprecipitate and

If .27 = "YES" and

If Supplier = "SELF" (automatically done when products are pooled using the Disposition - Not Transfused \[LRBLIDN\] option), then the integrity check will assume there should be entries in the Modified To/From field (#9) in the BLOOD INVENTORY file (#65).

#### Type(s) of Change

#### Data Dictionary Change

Change in Functionality

### Remove units with final disposition \[LRBLSER\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (NOIS CLL-0992-40001)

When a unit ID is entered with an "E" in it, the site gets an E_NUMBER error. The "E" is read by MUMPS as meaning exponential.

#### New Version Correction/Change

This no longer will happen.

#### Type(s) of Change

#### Change in Functionality

### Blood bank workload \[LRBLSW\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version

This is a new menu of workload options for Blood bank.

#### Type(s) of Change

#### New Menu

### ### Display workload for an accession \[LRUWL\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version

This is a new option to display test and WKLD codes for an accession (in a specific accession area) for a specific date.

#### Type(s) of Change

#### New Option

## General Functionality Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Transfusion Reaction Records Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version

#### Data Dictionary Changes

To identify transfusion reaction types and to maintain patient records of transfusion reactions when specific units cannot be identified with the transfusion reaction the several changes were made:

1\. The name of file 65.4 was changed from BLOOD DONOR UTILITY to BLOOD BANK UTILITY.

2\. A new choice was added to the set of codes for Screen field (#.02). "T" will stand for TRANSFUSION REACTION.

3\. A new field, Transfusion Reaction Type (Field 6.8) was added to BLOOD INVENTORY file (#65). This field is a pointer to BLOOD BANK UTILITY file (#65.4) and allows selection of entries from BLOOD BANK UTILITY file (#65.4) which have a "T" entered in the field, Screen (#.02).

4\. A new field, Transfusion Reaction Type (Field .11), was added to the LAB DATA file (#63) in the Transfusion Record field (63,.085). This field is a pointer to BLOOD BANK UTILITY file (#65.4) and allows selection of entries from BLOOD BANK UTILITY file (#65.4) which have a "T" entered in the field, Screen (#.02). This field contains data for reactions associated with a specific unit.

5\. A new multiple field, Transfusion Reaction Date (63,.086) was added to LAB DATA file (#63) to accommodate reactions which are not associated with specific units. This new multiple (63.0171) includes Transfusion Reaction Date (63.071,.01), Transfusion Reaction Type (63.071,.02), Person Entering Reaction (63.071,.03), and Transfusion Reaction Comment (63.071,1). When an entry is made in the .02 field, the AR cross reference is set.

> NOTE: These fields are included in the audit trail of changes in data.

#### Functionality Changes

The capability to track transfusion reactions has been expanded significantly. In previous versions, transfusion reactions were associated with specific units in BLOOD INVENTORY file (#65) or were noted in the free text Blood Bank Comments field. No capability existed to link specific types of transfusion reactions with either a patient or to extract data for reactions which were not necessarily linked to a specific unit.

Data entry and display of transfusion reactions is handled according to whether the reaction was "with a unit identified" or "without a unit identified". However, display of both is included in all of the same options that the Antibodies Identified and Blood Bank Comments appear (part of the LRDPA2 routine). In order to allow adequate supervisory review, it has also been included on the report generated by Patient Antibody Report (short list) \[LRBLPR\] option. For those reactions associated with a unit, the date of the reaction, the type of reaction, the unit ID and the component abbreviation are included. For those reactions which had no specific unit identified, the date and type of reaction as well as any comments entered are included.

Data entry for transfusion reactions for which there is an associated unit is done in the same manner as it was in previous version, that is either as part of the data entry in the Blood Transfusion Results \[LRBLPT\] option or Supervisory Edit option, Edit Unit Disposition Fields \[LRBLSFD\].

Data entry for transfusion reactions for which there is no unit associated is done using the Unknown Unit Transfusion Reaction \[LRBLPTXR\] option under the Blood Bank Patient Edit Options \[LRBLSP\] in the Supervisor's menu. This allows entry of the reaction type, as defined in BLOOD BANK UTILITY file (#65.4), and a free text, Transfusion Reaction Comment as well as the Transfusion Reaction Date.

In addition to the information displays previously described, a new option, Transfusion Reaction Count \[LRBLTA\] which evaluates those transfusion reactions which are associated with units. This option has been added to the Reports menu and provides tallies of reactions by type and component for a specified disposition date range. This option replaces the Transfusion Reaction Report \[LRBLIPTR\] option which has been deleted from the menu.

The report generated by Transfusion Data Report \[LRBLITR\] includes all of the transfusion reactions without a unit identified as well as those associated with a specific unit.

#### Type(s) of Change

#### New Functionality

Data Dictionary Change

### OPERATION (MSBOS) file (#66.5)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem

Previous problems with issuing new updates to the CPT file (#81) have been encountered in that the entries in the \*BLOOD COMPONENT REQUEST field (#.66), which relate to the Maximum Surgical Blood Order Schedule, are overwritten.

#### New Version Correction/Change

A new file, OPERATION (MSBOS) file (#66.5) has been created. Entries in OPERATION (MSBOS) file (#66.5) will represent a subset of the CPT file (#81), with the .01 field being a pointer to the CPT file (#81). Only those entries in the CPT file (#81) for which there is MSBOS data will be included.

For Version 5.2, a conversion routine and corresponding option, File 81 Conversion \[LRBLPOST\], has been included. This option (located on the LIM Workload menu) is locked with the LRLIASON key and needs to be run ONLY by those sites who have entries in CPT file (#81), \*BLOOD COMPONENT REQUEST field (#.66). For those sites having entries, this routine will need to be run as soon as possible after installation of Version 5.2 since the checks included in the component request entry options now point to the new file. Subsequent entry/editing will be done using the same option as in previous versions (Maximum Surgical Blood Order Edit \[LRBLSMS\]). However, this option now uses the new OPERATION (MSBOS) file (#66.5).

#### Type(s) of Change

#### Data Dictionary change

New Option

### BLOOD COMPONENT REQUEST file (#66.9)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem

Previous problems with having the Surgery package point to the BLOOD PRODUCT file (#66) have been reported. It is extremely confusing to the physician ordering components to have so many choices.

#### New Version Correction/Change

The new BLOOD COMPONENT REQUEST file (#66.9) will be used by the Surgery Package for entry of preoperative blood orders (for Surgery Package versions after 3.0.)

In the next release of the Laboratory package, this file will also be used for entry of blood orders other than by the Surgery package and for resolving some difficulties in component requesting and selecting units reported by those facilities which keep red cell units in stock which have different anticoagulants.

#### Type(s) of Change

#### Data Dictionary change

### Data compilation for Workload

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem

In order to obtain the data needed for compilation of data for AMIS and other reports, it was necessary to print many of the utilization and summary reports on a weekly or monthly basis.

#### New Version Correction/Change

In the near future, Pathology & Laboratory Medicine Service will be going to the new LMIP system of workload recording. The compilation of data for workload reports will become much easier with Version 5.2 due to the expanded workload capabilities which now include Blood Bank.

Until this replacement is completed, the collection of data for AMIS will be simplified. Instead of having to print a large number of different reports, it will be possible to obtain the majority of the data for the H28, H29, H84, and H86 segments from the new workload reports once workload is activated for Blood Bank and the data capture has been validated. These workload reports are designed for all areas within Pathology & Laboratory Medicine Service and are included in the main lab menu options. The data for the H01 segment and certain portions of the other segments not included in the regular workload reports can be obtained from the report generated by the new Blood Bank Administrative Data Report \[LRBLA\] option.

The listing in the Reports Menu Data Flow Chart in the areas designated as monthly reports and periodic reports have been amended to eliminate those reports for which data can be obtained via the mechanisms detailed above, while retaining those which are probably utilized for retaining hard copies of data or for other purposes such as Blood Transfusion Committee review.

#### Type(s) of Change

#### New Functionality

ENHANCEMENTS TO ANATOMIC PATHOLOGY

<span id="_Toc506704375" class="anchor"></span>

## ## Data entry, anat path menu \[LRAPD\] changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### ### Provisional anatomic diagnosis, \[LRAPAUPAD\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 89-87, 90-46)

Autopsy reports were available as soon as the Report Date was entered. This was not consistent with the rest of the Anatomic Pathology package.

#### New Version Correction/Change

Autopsy reports must now be verified/released in the same manner as surgical path, cytopathology, and electron microscopy in order for them to be accessible to clinicians via the Clinician menu options. Two new fields have been added, that is Autopsy Release Date/Time (63, 14.7) and Autopsy Released By (63, 14.8).

A new field, Provisional AP Diagnosis Date (63, 14.9) has been added to accommodate issuance of an official Provisional Anatomic Diagnosis Report for Autopsies. By having a separate date field, it allows the issuance of this report to be tracked separately from that of the final report. This field is also used for the calculation of the turnaround time for the Provisional Anatomic Diagnosis (PAD).

### #### New Version

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This new option has been added to accommodate issuance of an official Provisional Anatomic Diagnosis Report for Autopsies. The information can be entered into the Pathology Diagnosis field. However, the fact that it is a Provisional Gross Anatomical Pathological Diagnosis (subject to revision), MUST be included to minimize confusion. If the facility wishes to have this information accessible via the options in the Clinician menu, it is necessary to verify the report. The status can later be changed to unverified during the time the final report information is being entered.

#### Type(s) of Change

#### Data Dictionary Change

New Functionality

New Option

### FS/Gross/Micro/Dx \[LRAPDGM\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version Correction/Change

These options now allow you to manipulate the data entry/edit of the frozen section, microscopic, and gross description fields as well as entry/edit of the diagnosis field. The inclusion of the frozen section and/or diagnosis fields in the edit template is controlled by the Edit Pathology Parameters \[LRAPHDR\] option in the Supervisor's menu.

The names of the options have been changed:

from Microscopic/Gross Review

to FS/Gross/Micro/Dx,

from Gross/Review/Microscopic/SNOMED coding

to FS/Gross/Micro/Dx/SNOMED coding, and

from Gross/Review/Microscopic/ICD9CM coding

to FS/Gross/Micro/Dx/ICD9CM coding.

#### Type(s) of Change

#### New Functionality

Name Change

### ### ### Supplementary Report, Anat Path \[LRAPDSR\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 92-02)

It would be useful if the SNOMED code fields could be added to the Supplemental report option.

#### New Version Correction/Change

New prompts have been added to allow the entry of SNOMED codes.

#### Type(s) of Change

#### New Functionality

## Edit/modify data, anat path menu \[LRAPE\] changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Edit log-in & clinical hx, anat path \[LRAPED\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version Correction/Change

For autopsy quality assurance review purposes, a new field, Treating Specialty at Death (63,14.6) has been added to both the Log-in, Anat Path \[LRAPLG\] and the Edit Log-in data, Anat Path \[LRAPED\] options. If all of the data is entered, it is possible to have data on deaths sort by Service, Treating Specialty, and Physician using the QA Outcome Review Cases \[LRAPQOR\] option in the Supervisor's menu.

In order to allow the user to have more control over the length of the edit template in Edit Log-in & Clinical Hx, Anat Path \[LRAPED\] for autopsies, a new prompt has been added to allow the user to indicate whether the fields for weights and measurements should be included.

The name of the option has been changed from Edit log-in data, anat path to Edit log-in & clinical hx, anat path.

#### Type(s) of Change

#### Data Dictionary Change

New Functionality

Name Change

### Modify anat path gross/micro/dx/frozen section \[LRAPM\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (93-09)

The option only allowed you to change the word processing field, Microscopic Exam/Diagnosis. There was no mechanism to edit the gross description in a manner, which meets medical/legal requirements for documenting changes in verified data.

#### #### New Version Correction/Change 

The option has been modified to allow modification of the gross description, the microscopic description, the diagnosis or the frozen section. If the gross description is selected, the Specimen field is also included for editing. Once any of these items are modified, the report immediately changes from a "released" status and the report is flagged as a modified report. The accession must be released again, using the Verify/Release Reports, Anat Path \[LRAPR\] option, once it is modified.

The name of the option has been changed from Modify Anat Path Micro/Dx to Modify Anat Path Gross/Micro/Dx/Frozen Section.

#### Type(s) of Change

Data Dictionary

New Functionality

Name Change

### Edit anat path comments \[LRAPEDC\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

New Version

If a report is delayed, the reason(s) for delay may be entered here. They will appear on the log book report and the clinician screen display. This is accomplished by the use of new fields, Delayed Report Comment (#.97), under the Anatomic Path multiples in the LAB DATA file (#63).

The name of the option has been changed from Edit Anat Path Specimen Comments to Edit Anat Path Comments.

#### Type(s) of Change

Data Dictionary

New Functionality

Name Change

## Inquiries, anat path menu \[LRAPI\] changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Search options, anat path \[LRAPSEARCH\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 91-66)

When using the SNOMED search options, if the listing is longer than 1 page, the last line will have the first four columns of data printed, but the last 2 columns are missing. The first line of the next page will repeat this entry with all data present. The search summary at the end appears to count the incomplete entry plus the complete line as 2 entries in the total, instead of 1.

#### New Version Changes/Corrections

The form feed problem has been corrected in the new version.

#### Type(s) of Change

#### New Functionality

## Log-in menu, anat path menu \[LRAPL\] changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## ### Log-in, anat path \[LRAPLG\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### #### Old Version Problem (E3R 93-50, 91-15)

The old version only allowed four choices for Autopsy Type (Full Autopsy, Head Only, Trunk only, Other Limitation). Also, the site cannot change the requesting location if the patient is an inpatient.

#### New Version Changes/Corrections

#### The new version allows two more choices (Chest Only and Abdomen Only) for the Autopsy Type. The site can now change the requesting location during log-in whether the patient is an inpatient or an outpatient.

For autopsy quality assurance review purposes, a new field, Treating Specialty at Death (63,14.6), has been added to both the Log-in, Anat Path \[LRAPLG\] and the Edit Log-in Data, Anat Path \[LRAPED\] options. If all of the data is entered, it is possible to have data on deaths sort by Service, Treating Specialty, and Physician using the QA Outcome Review Cases \[LRAPQOR\] option in the Supervisor's menu.

If the Ask Frozen Section field is set to "YES", (done using the Edit Pathology Parameters \[LRAPHDR\] option), that field will appear in the log-in template for those cases in which the information would be entered at that point in the process.

#### Type(s) of Change

#### Data Dictionary Change

New Functionality

### Print log book \[LRAPBK\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## #### Old Version Problem (E3R 92-06, 92-37)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The user does not have the option of printing the SNOMED codes on the Log Book for autopsies. This option is available with cytologies and surgeries.

#### New Version Changes/Corrections

The user can print the SNOMED codes on the Log Book for autopsies.

#### Type(s) of Change

#### New Functionality

## Print, anat path menu \[LRAPP\] changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Print single report only \[LRAP PRINT SINGLE\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 93-06)

## If an autopsy is logged into the REFERRAL PATIENT file (#67), you cannot get a printed report using the print options like Print Single Report \[LRAP\]. The patient name prompt only appears in upper case letters so you can't access the REF: file.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version

The "Select Patient Name" prompt now allows use of the extended syntax

#### Type(s) of Change

#### New Functionality

### Alphabetical autopsy list \[LRAPAUA\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version

This new option provides a list of autopsies from one date to another and is meant to replace a site's card file of autopsies.

#### Type(s) of Change

#### New Option

New Functionality

### Path cases by resident, tech, senior or clinician \[LRAPAUL\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version

This option now allows you to obtain a list by clinician as well as by the pathologists.

The name of the option was changed from List of path cases by resident, tech or, senior to Path cases by resident, tech, senior, or clinician.

#### Type(s) of Change

#### New Functionality

Name Change

### % Pos, Atyp, Dysp, Neg, Susp, Unsat cytopath \[LRAPCYPCT\] 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 91-29, 92-32)

The morphology codes used were hard coded in the routine. Sites were not given any flexibility in the codes used.

#### New Version 

A new multiple field, Morphology Code (File 69.2, field 12), has been added to accommodate the morphology codes to be used by the % Pos, Atyp, Dysp, Neg, Susp, Unsat Cytopath \[LRAPCYPCT\] option. This will allow the sites to specify the morphology codes which they commonly use. This is particularly useful for the atypia designations.

The name of the option was changed from % Pos, Neg, Susp, & Unsat Cytopath Specimens to % Pos, Atyp, Dysp, Neg, Susp, Unsat Cytopath.

#### Type(s) of Change

Data Dictionary Change

New Functionality

Name Change

### Accession list with stains \[LRAPSA\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 93-27)

A lab user would enter block/stains in the AP module but only the numbers of slides prepared print out on the report option. The report does not print the number of control slides. The addition of the control slide information to the report should allow the user to visualize all information regarding the particular Block/stain at one time rather than having to step through the Enter/Edit option.

#### New Version

The option will print a number (such as 3/2) with 2 being the number of control slides

#### Type(s) of Change

New Functionality

### Autopsy Slide Labels \[LRAUMLK\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem

No ability existed to print autopsy labels, either with a set specimen label or with no specimen designated, but merely with an accession number and facility name.

#### New Version Correction/Change 

Choices have been provided for the generation of microscopic slide labels for autopsies.

This new option has been added which allows the user to specify a number of labels to print for a given accession number, with no specific paraffin blocks or stains associated.

#### Type(s) of Change

Data Dictionary Change

New Functionality

New Option

### Anatomic Path slide Labels \[LRAPLM\] 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 91-24)

1\. On a recut, all labels for that accession have to be reprinted just to get a few extra labels

2\. Have the ability to print control slide labels

#### New Version Correction/Change

It is now possible to reprint labels and to specify a range of numbers. The option also now works for Cytology as well as for Surgical Pathology.

The capability to create a generic list of labels to be used by Anatomic Path Slide Labels \[LRAPLM\] has been added. This is based on the new field in LAB SECTION PRINT file (#69.2), that is field 6, Generic List (Multiple-69.26), with the .01 field, Generic Label.

#### Type(s) of Change

#### New Functionality

Data Dictionary Change

### ### Cum path data summaries \[LRAPT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 91-122)

For the CUM path data summaries option, if you tried to print a second patient while the first report is printing, you would crash with an error.

#### New Version

The new version has corrected this problem.

#### Type(s) of Change

#### New Functionality

## ## Supervisor, anat path menu \[LRAPSUPER\] changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Delete anat path descriptions by date \[LRAPDAR\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 91-91)

There has been much discussion about purging the text (word processing field) of the AP module - especially the Surgical accession area. The diagnosis is considered to be, and is, more precise than the SNOMED codes which are most useful in searching. For the Cum Path summary, the codes are admittedly imprecise and thus, the need for seeing the diagnosis as given by the responsible pathologist.

#### New Version Correction/Change

The capability to exclude purging of the microscopic descriptions field and/or the frozen section field has been added. If so, the microscopic descriptions and/or the frozen section field will be saved. However, even if these fields are purged, the new Diagnosis fields for each area are not removed.

#### Type(s) of Change

#### New Functionality

New Prompt

### Edit pathology parameters \[LRAPHDR\]; 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 92-40)

1\. The QA portion of the Anatomic Pathology module did not allow entry of TC codes for other than Surgical Pathology accessions.

2\. No mechanism existed to enter and report information related to the Frozen section separately from that of the permanent sections.

3\. The final diagnosis for the cases had to be incorporated into the text of the Microscopic Description/Diagnosis as there was not a separate field for diagnosis. This was true for all of the areas.

#### New Version Correction/Change

1\. TC CODES will be available for Cytopathology and EM. This capability is activated by editing the pathology parameters to turn on "asking TC CODES."

2\. A new prompt has been added to the Edit Pathology Parameters \[LRAPHDR\] option to allow the facility to choose to utilize the new Frozen Section diagnosis field. If this field is set to "YES', changes will appear in several options to accommodate the addition of the new word processing field for the frozen section diagnosis, including data entry, reporting and purging. As part of the data entry process, additional functionality was also added to ensure that the appropriate SNOMED procedure code was being captured, that is a reminder message is now displayed if an entry is made in the Frozen Section field.

If this filed is set to "YES", the Report Header 3 (Field .13) to accommodate the header text for the Frozen Section text to appear in the Surgical Pathology Report, needs to be entered.

3\. A new prompt has been added to the Edit Pathology Parameters \[LRAPHDR\] option to allow the facility to choose to utilize the new Diagnosis fields, that is Surgical Path Diagnosis, Cytopathology Diagnosis, and EM Diagnosis. If this field is set to "YES", changes will appear in several options to accommodate the addition of the new word processing field for the diagnosis, including data entry and reporting.

These fields <u>cannot</u> be purged, as the gross description, microscopic description and the comments fields can. Thus, allowing the actual description to be retained in addition to the specimen and the SNOMED coding. This field also appears in the Cum path summary option output. In the next version, this field will also be used to automate the SNOMED coding process.

If this filed is set to "YES", the Report Header 4 (Field .14) to accommodate the header text for the Frozen Section text to appear in the Surgical Pathology Report needs to be entered.

> **NOTE:** There actually are several options affected. However, the control mechanism is in this option.

4\. The option's name was changed from Edit Pathology Report Parameters to Edit Pathology Parameters.

5\. The site can customize their cytology labels by entering in a 1- 9 character label name rather than use the first nine characters of Cell Block, Cytospin, Membrane Filter, Prepared Slides, or Smear Prep.

#### Type(s) of Change

#### New Functionality

Data Dictionary Change

Name Change

### Print path modifications \[LRAPMOD\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Old Version Problem

When this option was used, all you can see is the changed report. You do not see what was there before (the original released report).

#### New Version

This option now allows you to print a report that has all the original data as well as any modifications to that data.

The name of the option has been changed from Print Path Micro/Dx Modifications to Print Path Modifications.

#### Type(s) of Change

#### New Functionality

Name Change

### Frozen section, surgical path correlation \[LRAPQAFS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 92-31)

When the quality assurance options were used, the anatomic reports automatically printed out at the end. This generated many pages of printed reports that were not always desired.

#### New Version Correction/Changes

A new prompt was added in the Frozen section, surgical path correlation option to allow the user to indicate whether the output should include the anatomic report.

#### Type(s) of Change

#### New Functionality

New Prompt

## ### Malignancy review \[LRAPQAMR\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 92-31)

When the quality assurance options were used, the anatomic reports automatically printed out at the end. This generated many pages of printed reports that were not always desired.

#### New Version Correction/Changes

A new prompt was added in the Malignancy Review option to allow the user to indicate whether the output should include the report

#### Type(s) of Change

#### New Functionality

New Prompt

### QA outcome review cases \[LRAPQOR\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version

In order to enhance the usefulness of software in assisting with the mandated autopsy reviews for premortem/postmortem correlation, the output of the QA Outcome Review Cases \[LRAPQOR\] option has been revised. Data regarding these reviews can be entered using the existing QA code mechanism.

#### Type(s) of Change

#### New Functionality

### 10% Random case review, surg path \[LRAPQAR\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### ### #### Old Version Problem (E3R 92-31)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the quality assurance options were used, the anatomic reports automatically printed out at the end. This generated many pages of printed reports that were not always desired.

#### New Version Correction/Changes

A new prompt was added in the 10% Surgical Path Random Review option to allow the user to indicate whether the output should include the report

#### Type(s) of Change

#### New Functionality

New Prompt

### AFIP registries \[LRAPAFIP\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version

This is a new menu that contains the following options:

PO Prisoner of war veterans \[LRAPDPT\]

PG Persian gulf veterans \[LRAPPG\]

#### Type(s) of Change

#### New Menu

### Persian Gulf Veterans \[LRAPPG\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version

This is a new option that prints a list of veterans who served in the Persian Gulf and who had pathology specimens.

#### Type(s) of Change

#### New Option

New Functionality

### Anatomic pathology turnaround time \[LRAPTT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 93-34)

LRUTT calculates turnaround time in excess of 1 day incorrectly. X (number of days) is added to 1440 (minutes in a day) when it really should be multiplied by 1440.

#### New Version

The turnaround time is calculated correctly in the new version.

#### Type(s) of Change

#### New Functionality

### ### Move anatomic path accession \[LRAPMV\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version 

If it is necessary to transfer data associated with a specific surgical pathology accession from one file to another, for example, REFERRAL PATIENT file (#67) to PATIENT file (#2), OR from one patient to another within the PATIENT file (#2), this option can be used.

This new option eliminates the need to edit the global for those occurrences in which a surgical pathology accession is assigned to a patient and the error is not detected until after the report has been verified/released.

This option is locked with the LRLIAISON key because of the implications of such a data transfer.

#### Type(s) of Change

#### New Functionality

New Option

### Edit Referral patient file \[LRUV\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 93-35)

When logging in surgical or cytology specimens, if the patient must be entered into the REFERRAL PATIENT file (#67), there is no provision to enter the sex. This becomes especially important with cytology specimens. It can be done/entered via FileMan but this is awkward and not all lab personnel are given FM access.

#### New Version 

A new option in the AP supervisor menu allows the user to edit the fields in the REFERRAL PATIENT file (#67) .

#### Type(s) of Change

#### New Functionality

New Option

## Clinician options, anat path menu \[LRAPMD\] changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Edit/print/display preselected lab tests \[LRUMD\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 92-18)

The physician could not send his list of patients to print and usually did not have access to a slave printer.

#### New Version Correction/Change

You will be able to print both the patient list and the test list when using these options. If the test list is longer than one screen, only one screen at a time will display.

#### Type(s) of Change

#### New Functionality

### Autopsy protocol/supplementary report \[LRAPAUPT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 89-87, 90-46)

Autopsy reports were available as soon as the Report Date was entered. This was not consistent with the rest of the Anatomic Pathology module.

#### New Version

This new option has been added to the clinician's menu to accommodate viewing of released autopsy reports.

Examples:

1\. If the site enters a provisional gross anatomical diagnosis and releases the report, this will be accessible until the accession is "unreleased".

2\. If the site enters a provisional gross anatomical diagnosis and does not release the report, this will not be accessible until the accession is "released".

#### Type(s) of Change

New Functionality

New Option

### Print surgical pathology report for a patient \[LRAPSPSGL\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version

In order to minimize the potential complications created by allowing printing of extra hard copies of pathology reports, a comment "see hard copy of report in chart" was added to the bottom of the report above the pathologist's name. In addition, the SNOMED codes were removed from the reports generated via these options.

#### Type(s) of Change

#### New Functionality

## Workload, anat path menu \[LRAPW\] changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version

This new menu contains the options for displaying and recording the anatomic pathology workload.

#### Type(s) of Change

#### New Menu

### Cytopathology screening workload \[LRAPWR\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version

This new option records the date/time cytopathology slides are screened and captures the screening workload.

#### Type(s) of Change

#### New Option

New Functionality

### Display workload for an accession \[LRUWL\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version

This new option displays the tests and WKLD codes for an accession. This report is sorted by date and accession area.

#### Type(s) of Change

#### New Option

New Functionality

### EM scanning and photo workload \[LRAPWE\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version

This new option allows recording workload for scanning and photography of EM grids and the making of prints.

#### Type(s) of Change

#### New Option

New Functionality

### Surg path gross assistance workload \[LRAPWRSP\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version

Use this option to record workload for gross description and cutting of surgical tissue by a non-physician.

#### Type(s) of Change

#### New Option

New Functionality

## General Functionality Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Pathology Report Heading

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 93-36)

The pathology report form SF515 has the heading "Pathological Report" just before the gross description.

#### New Version Correction/Change

The report now reads "Pathology Report".

#### Type(s) of Change

#### New Functionality

### Autopsy Assistant field

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 92-77)

The field label, RESIDENT in the Autopsy Protocol, is inaccurate unless a resident assists at an autopsy. For sites with no pathology residents, this label is inaccurate. Change field label to ASSISTANT or create an additional ASSISTANT field.

#### New Version Correction/Change

A new field, Autopsy Assistant, has been created.

#### Type(s) of Change

#### New Functionality

Data Dictionary Change

### SNOMED Code Field Definition

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 92-78)

The field containing the SNOMED codes in files 61-61.5 allow free test 2-7 characters. Local codes are sometimes made which use letters at the end. The problem is that the search options do not allow for any letters to be entered except the ones used by the official codes.

#### New Version Correction/Change

The SNOMED search options now allow the user to look for any codes even if they are not one of the official codes.

#### Type(s) of Change

#### Data Dictionary Change

### Extended Syntax

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 93-06)

If an autopsy is logged into the referral file, you cannot get a printed report using the print options. The patient name prompt only appears in upper case letters so you can't access the REF: file.

#### New Version Correction/Change

The "Select Patient Name" prompt allow the use of the extended syntax.

#### Type(s) of Change

#### New Functionality

### Anatomic Pathologist's Name

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 88-127)

In the provider file, if the appropriate professional title is entered, odd printouts occur in the AP module on reports, for example LABPROVIDER, ONE.

#### New Version Correction/Change

The Laboratory package now references the NEW PERSON file (#200), Provider Class field (53.5) and uses that title at the end of the name.

#### Type(s) of Change

#### New Functionality

ENHANCEMENTS TO GENERAL LABORATORY

<span id="_Toc506704420" class="anchor"></span>

## ## Phlebotomy menu \[LR GET\] changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Lab order by collection type \[LRRP5\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version

This new option allows you to print a report for a certain date and collection type (Lab Collect, Send Patient, or Ward Collect).

#### Type(s) of Change

#### New Option

New Functionality

### Print Future Collection Labels \[LRUFCL\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 91-73, 92-08, 93-47)

The collection list cannot build until the day of collection. The list needs to be printed earlier when a computer downtime is scheduled.

#### New Version Correction/Change

This new option will print any order that has the collection type of LAB COLLECT or IMMEDIATE COLLECT. This option could be used to print a list of patient collection labels in anticipation of computer downtime.

#### Type(s) of Change

#### New Option

New Functionality

### Print Single Future Collection Labels \[LRUFCLS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version

This new option is a single order version of the Print Future Collection Labels \[LRUFCK\] option. The user must supply the order number.

#### Type(s) of Change

#### New Option

New Functionality

### Order/Test Status \[LROS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 93-07)

The Order/Test Status option would only allow you to look up orders for the last 30 days.

#### New Version Correction/Change

The option will now allow you to look at orders for the same number of days that are entered in the Grace Period for Orders field in the LABORATORY SITE file (#69.9).

#### Type(s) of Change

#### New Functionality

## Accessioning menu \[LR IN\] changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Accessioning tests ordered by ward order entry \[LROE\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 93-49)

When this option is used to enter consecutive orders on the same patient, the comment entered for the first order is repeated invisibly on the next order entered.

#### New Version Correction/Change

## ## Version 5.2 will not do this.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Type(s) of Change

#### New Functionality

### Fast Lab Test Order (SEND PATIENT) \[LROW SEND PAT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## #### Old Version Problem (E3R 90-54)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows orders to be entered with a past date.

#### New Version Correction/Change

## ## Version 5.2 will not allow the entry of past dates for orders.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Type(s) of Change

#### New Functionality

### Fast Lab Test Order (SEND PATIENT) \[LROW SEND PAT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version Correction/Change

These options have been changed so that you can order tests one year in the future.

#### Type(s) of Change

#### New Functionality

### Fast Lab Test Order (IMMEDIATE COLLECT) \[LROW IMMED COLLECT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 86-04, 87-72, 90-83, 92-03 )

There was not a functionality to order STAT, TIMED, ASAP, or IMMEDIATE COLLECT tests. The existing order entry options did not have the flexibility needed to handle "on demand" type testing.

#### New Version Correction/Change

The new option allows the wards to request immediate collection of a test specimen by the laboratory. In addition, the laboratory can set certain time frames and days of the week when this functionality will not be available.

#### Type(s) of Change

#### New Functionality

New option

### Manual Enter Clinic Stop Codes \[LRSTOPC\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 88-19)

In order to improve Outpatient Clinic Visits statistics, laboratory personnel had to manually enter Stop Codes using the Clinic Visit Stops Add/Edit option.

#### New Version Correction/Change

The new version will automatically stuff the lab clinic stop code (108) during the accessioning of outpatient orders. On capturing the stop codes, the program will enter the person's DUZ that enters the test. The tasked option, LR Nightly, will process any stop code data that was not already processed.

It is recommended that the LIM coordinates with the MAS ADPAC before turning on the Transmit Clinic Stop Code field in the LABORATORY SITE file (#69.9) so that MAS will be aware that the stop code will be passed automatically. These codes will appear in the category of Computer Generated Stop Codes (MAS option - Stop Code Listing (Computer Generated) \[SDACS CGSCLIST\]).

However, there will be rare occasions when the lab will need to enter the stop codes manually (e.g., for example, the computer has been down or certain blood bank procedures such as therapeutic phlebotomy).

#### Type(s) of Change

#### New Functionality

New Option

### Multipurpose accessioning \[LRQUICK\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 94-06)

If, during the same sign on session, you both build a load/worklist and accession a patient using the Multipurpose Accessioning option, the labels that are printed include the standards and controls for the load/worklist.

#### New Version Correction/Change

The labels that print are for the accession only.

#### Type(s) of Change

#### New Functionality

### Reprint order accession label(s) \[LRLABXOL\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 93-23)

The old version only had the ability to reprint accession labels by individual accession numbers.

#### #### New Version Correction/Change

This new option will reprint all the accession labels for an entire order.

#### Type(s) of Change

#### New Functionality

New Option

## Process data in lab menu \[LR DO!\] changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### All Enter/Verify options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version

Version 5.2 allows tracking of who verifies which test. This information is available on the Summary List (Extended Supervisor's) \[LRLISTE\] report. The prompts have been changed to reflect this new approach.

> Old Version:

> TESTS DONE BY ('E' to edit data, 'C' to edit comments) PO// \<RET\>

> Approve for release by entering your initials:

> New Version

> SELECT ('E' to Edit, 'C' for Comments, 'W' Workload ) \<RET\>

> Approve for release by entering your initials:

Whoever verifies the test is recorded and kept track of by test rather than the last person who verifies something on the accession being given credit for the whole thing. If you "Approve for release", you are accepting responsibility for that entry.

#### Type(s) of Change

#### New Functionality

### Enter/verify/modify data (manual) \[LRENTER\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 87-53, 90-65)

The EM option needs to allow for data entry and review for each test without automatic verification.

#### New Version Correction/Change

This has been completed. As part of the change, there is an additional prompt that appears when you indicate that you are finished editing.

ACCESSION: CH 0907 1 CH 0915 1

09/07 0045d 09/15 0045d

GLUCOSE 123 100 mg/dL

COMMENT:

This indicates

If you need to change something, enter your initials: \<RET\> \<- that you are finished editing.

Approve update of data by entering your initials: PO

(GLUCOSE reported incorrectly as 154)

#### Type(s) of Change

#### New Functionality

### Misc. processing \[LR PROCESS, MISC\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version

A new menu has been created to contain some of the Process menu options.

#### Type(s) of Change

#### New Functionality

New Menu

### WKLD log file download \[LRCAPDL\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version

This option can be used to download data from the WKLD LOG file (#64.03) to spread sheets. Not all sites will want to use this option but it is available so that site-specific reports can be generated.

#### Type(s) of Change

#### New Functionality

New Option

### Rollover Accession (Manual) \[LR ROLLOVER\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version

This option should be used if the task option, Rollover Accession (Manual) \[LRTASK ROLLOVER\], does not run for some reason. This option should not be the normal method for transferring incomplete accessions from the previous day to the present day's accession file.

#### Type(s) of Change

#### New Functionality

New Option

Fast bypass data entry/verify \[LRFASTS\]<span id="_Toc506704435" class="anchor"></span>

#### Old Version Problem (E3R 90-64)

Bypass normal data entry option will only allow one test to be entered at one time on a patient. The technologist should be able to enter multiple tests at a time.

#### New Version Correction/Change

The new option, Fast Bypass Data Entry/Verify, allows the user to accession several tests in different accession areas for the same patient.

#### Type(s) of Change

#### New Functionality

New Option

### Std/QC/Reps Manual Workload count \[LR WKLD STD/QC/REPS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version 

This new option allows the user to manually update the standards, QC and repeats workload counts as well as add manual workload counts.

The user will have the opportunity of adding standards, QC and repeats at the end of every verification session if the Workload On field (#10) and the Collect STD/QC/ Repeats field (#11) are set to "YES".

#### Type(s) of Change

#### New Functionality

New Option

## Quality control menu \[LRQCM\] changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Add/Edit QC Name and/or Edit Test Names \[LRQCADDNAME\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 89-34)

When using the option, Add/Edit QC Name and/or Edit Test Names \[LRQCADDNAME\], the prompt asks whether you want to see all the entries in the LAB CONTROL NAME file (#62.3). When answered "YES", not all the entries are shown. Technologists needing to do editing in the LAB CONTROL NAME file (#62.3) cannot see all of the entries with the intended menu option.

#### New Version Correction/Change

This option now allows you to see all the entries.

#### Type(s) of Change

#### New Functionality

### Quality control display (Levy-Jennings) \[LRQC\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 89-12, 89-34)

If the field, Exclude Data, is flagged "YES", no Levy-Jennings chart can be printed. After data entry is excluded, one may still want to graph from the data previously collected.

#### New Version Correction/Change

Even if data entry is excluded, you may produce a Levy-Jennings chart.

#### Type(s) of Change

#### New Functionality

## Results menu \[LR OUT\] changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Interim report \[LRRP2\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## #### Old Version Problem (NOIS GRJ-1093-50007)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## ## When using the interim report option, the user had to enter a date for the starting date that was closer to today than the ending date. If this occurred, the user would see a FileMan date as a default on the second try.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version Correction/Change

The date prompts work whichever way you enter the dates.

#### Type(s) of Change

#### New Functionality

Change in Functionality

### Interim report by Provider \[LRRD\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 90-63, 91-09, 92-70)

## ## When using the interim report options that did not use the patient name as the sorting mechanisms, you were not allowed to select a range of dates. 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Another problem was that the user had to type in an exact match for the location at the "Select PATIENT LOCATION" Prompt. The program would only accept the exact match to a location. For example, you would have to enter exactly "1E". The program would not accept a "1"

## #### New Version Correction/Change

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can now select a date range. The program now will accept a less than exact location. For example, you may enter a "1" and the program will find all matches to the entry.

#### Type(s) of Change

#### New Functionality

Change in Functionality

## Ward lab menu \[LRWARDM\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Lab test order \[LROW\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (NOIS ISH-1092-40002)

This option would display the collection order cut-off times even if you do not choose (B)LOOD for lab collection.

#### New Version Correction/Change

This option shows the collection order cut-off times only if the user chooses the lab collection prompt.

#### Type(s) of Change

#### Change in functionality

## Microbiology menu \[LRMI\] changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Results entry (batch) \[LRMISTUF\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 92-11)

The User crashes with a bad command detected in ^DIE if a semicolon is used to punctuate text stuffed in the Parasite Rpt Remark field.

#### New Version Correction/Change

This option will now accept the semicolon.

#### Type(s) of Change

#### Change in functionality

## Results entry \[LRMIEDZ\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Old Version Problem (E3R 88-111, NOIS MAD-1092-40003)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On entering a gram stain result, a date was automatically set for approval when entering the accession. Even if no data is entered, it is impossible to remove the accession once this is done.

The NOIS call reported an undefined error if you timed out at the "BACT RPT STATUS:" prompt.

#### New Version Correction/Change

Data now must be entered before the accession is "locked in" and you do not an undefined error is you time out.

#### Type(s) of Change

#### Change in functionality

### Verification of data by supervisor \[LRMIVER\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 92-96)

This option would not allow the verification of tests that were not in a yearly accession area.

#### New Version Correction/Change

This has been corrected.

#### Type(s) of Change

#### New Functionality

### Review Accession Workload \[LR WKLD AUDIT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version Correction/Change

This is one of the new options designed to work with the new workload functionality. This option allows one to review what workload has been completed for a given accession.

#### Type(s) of Change

#### New Functionality

### Microbiology Trend Report \[LRMITS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 87-67, 89-30, 90-21, 90-69)

There were numerous problems with the old Antibiotic Trend report.

#### New Version Correction/Change

The Antibiotic Trend report has been totally rewritten. Details about the new report, which is now called the Microbiology Trend Report, are located in the Planning and Implementation Guide.

#### Type(s) of Change

#### Change in Functionality

Output Redesigned

New Option

### Workload editing for Microbiology

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version

In the "CH" subscripted procedure, the assay procedure is counted only one time. If the verified result is later corrected or changed, only one credit is given. In the case of "MI" subscripted procedures, each organism isolated is counted. This difference between "CH" and "MI" subscripted test forms the basic foundation for workload accounting in microbiology. The software has been designed to allow this type of workflow to be captured each time a workload definable the technologist does entry. In order to provide for various possible combinations of procedures done in microbiology, certain editing of workload functions had to be provided. This is in contrast to "CH" subscripted, which does not allow such extensive editing.

#### Type(s) of Change

#### New Functionality

### Updated Vitek/Microscan section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version

The section on the Vitek automated Microbiology instrument is now located in the Technical Manual. This section has been edited to reflect new information concerning the interfacing of this instrument.

#### Type(s) of Change

#### New Functionality

### Microbiology Report Status field

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version

A patch to Version 5.1 corrected the problem of getting an undefined error if you used an "^" at the Report Status field in Microbiology.

#### Type(s) of Change

#### Patch to Version 5.1 - new to documentation

### Typo in Micro report Display/Print

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 91-86)

Spelling error in parasitology preliminary report. ("\* PARASITOLOGY PRELIMIARY REPORT =\>")

#### New Version Correction/Change

Spelling error is corrected. ("\* PARASITOLOGY PRELIMINARY REPORT =\>")

#### Type(s) of Change

#### Corrected spelling

### Microbiology Execute Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 90-26)

The Microbiology edit codes do not allow editing of the Collection Sample data field. Errors cannot be corrected once the entry is accepted.

#### New Version 

With Version 5.2, no data is being exported with the EXECUTE CODE file (#62.07). Any modification of the execute codes will have to be done on the local level.

### MIC Default Interpretation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 93-59)

When the site changes the MIC entries in the ANTIMICROBIAL SUSCEPTIBILITY file (#62.06), the AI cross reference gets deleted.

#### New Version Correction/Change

The AI cross-reference is no longer deleted.

#### Type(s) of Change

#### Change in functionality

## Supervisor menu \[LRSUPERVISOR\] changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Manual Queuing of Fileroom Cum \[LRAC MANUAL FILEROOM CUM\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version

If the Fileroom cumulative is not being automatically run through the LRTASK CUM FILEROOM option, this option may be used to run that cumulative.

#### Type(s) of Change

#### New Functionality

New Option

### Reprint a Permanent Page from Cumulative \[LRAC 1 PAGE\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem

Older versions of the Laboratory package did not allow you to reprint permanent Miscellaneous pages.

#### New Version Correction/Change

The option now allows you to print all permanent pages from the Cumulative.

#### Type(s) of Change

#### Change in Functionality

### Add a new WKLD code to file \[LRCAP CODE ADD\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version

This option allows the site to "create" an individualized workload code for a specific test/procedure and instrument/method by combining the workload code for the test with a suffix code for the instrument.

#### Type(s) of Change

#### New Functionality

New Option

### Convert Archived Data to Use New Person file \[LR ARCHIVE NP CONVERSION\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version

Data that has been archived before Version 5.2 will have pointers to the USER file (#3), the PROVIDER file (#6) and the PERSON file (#16). The option will allow you to convert "old data" to use the NEW PERSON file (#200) and readable by Version 5.2.

#### Type(s) of Change

#### New Functionality

New Option

## ### Check Files for Inconsistencies \[LRCHKFILES\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem

The Blood Bank files were not checked by this option.

#### New Version Correction/Change

The Blood Bank files are now checked just like the other files when this option is used.

#### Type(s) of Change

#### New Functionality

### Download Format for Intermec Printer \[LR BARCODE FORMAT LOAD\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version

This option is used to download the printer format for barcode accession labels.

#### Type(s) of Change

#### New Functionality

New Option

### LIM workload menu \[LR LIM/WKLD MENU\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version

This is a new menu containing workload specific options that are locked either by the LRSUPER or the LRLIASON keys.

#### Type(s) of Change

#### New Menu

### Detail workload report \[LRRP6\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version

Provides a detailed print of the tests/WKLD codes for a specific date range.

#### Type(s) of Change

#### New Functionality

New Option

### Etiology WKLD Codes (Force) \[LRCAPF\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version

To use the new version workload capabilities, certain files must have the correct workload codes inserted. The ETIOLOGY FIELD file (#61.2) would normally require many hours of work by the LIM to properly insert the codes. This file stuffer capability will help reduce the time needed to perform the task. This option is used to automatically add WKLD codes into the ETIOLOGY FIELD file (#61.2). A sort template must be created using standard FileMan options. This option will utilize the selected template and then add WKLD codes.

Details are available in the Planning and Implementation Guide in the Microbiology Implementation section.

#### Type(s) of Change

#### New Functionality

New Option

### File 81 conversion \[LRBLPOST\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version

This option (located on the LIM WORKLOAD menu) is locked with the LRLIASON key and needs to be run ONLY by those sites that have entries in File 81, field 66. For those sites having entries, this routine will need to be run as soon as possible after installation of Version 5.2 since the checks included in the component request entry options now point to the new file.

#### Type(s) of Change

#### New Functionality

New Option

### LMIP Reports/Data Collection \[LR WKLD4\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version

This new menu contains the LMIP report options. The entire menu is locked with the LRLIASON key.

#### Type(s) of Change

#### New Menu

### ### PHASE 1: Move data from 64.1 to 67.9 \[LR WKLD LMIP 1\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version

This option performs the first step in producing your monthly report for LMIP and management. This option extracts data from your WKLD DATA file (#64.1), condenses the data and stores it in the LAB MONTHLY WORKLOAD file (#67.9).

> **NOTE:** Non patients are those entries in the REFFERAL PATIENT file (#67) and patients (both in and out) are from the PATIENT file (#2).

#### Type(s) of Change

#### New Functionality

New Option

### PHASE 2: Collect data for transmit to NDB \[LR WKLD LMIP 2\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version

This option is the second stage of LMIP data reporting. The data is condensed even more and prepared for transmission to the National Data Base (NDB).

#### Type(s) of Change

#### New Functionality

New Option

### PHASE 3: Print of data to be sent to NDB \[LR WKLD LMIP 3\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version

This option produces a "human readable" report of the data the system has collected for the requested reporting period.

#### Type(s) of Change

#### New Functionality

New Option

### ### PHASE 4: Create E-mail message for NDB \[LR WKLD LMIP 4\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version

This option is the last phase of data collection. This option will place the formatted data into an appropriately formatted mail message.

#### Type(s) of Change

#### New Functionality

New Option

### PHASE 5: Purge monthly WKLD data from 67.9

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version

This option is used to purge LMIP data from the LAB MONTHLY WORKLOAD file (#67.9) after data has been sent to the NDB.

#### Type(s) of Change

#### New Functionality

New Option

### RCS-CDR/LMIP report \[LRCAPM5\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version

This option will provide a report based on treating specialty codes. The data is from the LAB MONTHLY WORKLOAD file (#67.9), the same as used for the LMIP reports. The LMIP choice in this report consists of two pages that closely follow the LMIP report you are presently sending in to central office.

#### Type(s) of Change

#### New Functionality

New Option

### ### Recompile Phase 1 LMIP data \[LR WKLD LMIP 1 REPEAT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version

This option allows the user to rerun Phase 1 of LMIP data collection. This option deletes the data in 67.9 and reset the pointer in 64.1 to allow the date to be recompiled again.

#### Type(s) of Change

#### New Functionality

New Option

### Supervisor workload menu \[LR SUPER/WKLD MENU\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version

New Menu contain the workload options available to the lab supervisor.

#### Type(s) of Change

#### New Menu

### Treating Specialty Workload Report \[LRCAPTS\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 88-20, 88-65, 88-66, 91-04, 91-06)

The option, CAP Statistics by Treating Area, counted each individual Hospital Location separately. This resulted in multiple outpatient clinics being listed separately since they had different names.

#### New Version Correction/Change 

This new option has changed how workload is counted.

#### Type(s) of Change

#### New Functionality

New option

### Workload code list \[LRCAPD\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version

This option will print a list of all the WKLD codes in the LABORATORY TEST file (#60).

#### Type(s) of Change

#### New Functionality

New Option

### Workload cost report by major section \[LRCAPML\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version

This report is summed by major section and lab subsection. You must have the cost entered for the specific WKLD code in WKLD CODE file (#64) in the Cost field (#7).

#### Type(s) of Change

#### New Functionality

New Option

### Workload Report \[LRCAPR1\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 93-26)

#### An option is needed that will identify STAT lab requests by location/provider for usage in QA.

#### New version

This new option allows generation of a workload report by numerous combinations of selection criteria. This report can be produced in a detailed or condensed format. You can select STAT tests only and you can select which location(s) you want.

#### Type(s) of Change

#### New Functionality

New Option

### Workload statistics by accession area and shift \[LRRP8\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 94-20)

The option, Accession and Test Counts by Shift \[LRUPACS\], automatically defines the shifts. The site needs to be able to define the time of the shifts.

#### New Version

This option provides a report that is a summary of workload statistics broken down by time ranges, accession areas and WKLD codes. The site defines the time ranges.

#### Type(s) of Change

#### New Functionality

New Option

### ### Workload Statistics by Major Section \[LRCAPMA\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version

This workload report is summed by LAB division, major section, and subsection.

#### Type(s) of Change

#### New Functionality

New Option

### Turn on site workload statistics \[LR WKLD STATS ON\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version

This new option allows the user to turn on the workload compiling features of Version 5.2. This option allows you to answer yes to the WKLD Stats On field in the Laboratory site file (#69.9). You must also turn on the switch that controls the accession area (Workload On - in ACCESSION file (#68)).

#### Type(s) of Change

#### New Functionality

New Option

### ### ### Turn on workload stats for accession area \[LR WKLD STATS ON ACC AREA\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version

This new option allows the user to turn on the workload data collection for a specific accession area by using the Workload On field in the ACCESSION file (#68). You must first have answered "YES" to the WKLD Stats On field in the LABORATORY SITE file (#69.9).

#### Type(s) of Change

#### New Functionality

New Option

### ### ### Re-index Antimicrobial Suscept File (62.06) \[LRMIXALL\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version

This option is used to re-index a single antibiotic in the ANTIMICROBIAL SUSCEPTIBILITY file (#62.06). This option differs from the FileMan re-index option in two ways.

1\. This option removes all X-ref entries.

2\. It allows the user to select a single antibiotic.

When a selection is made, X-Ref of "AI", "AJ", and "AS" cleared and redefined.

> **NOTE:** This option may be used when trouble shooting a printout of antibiotics on the Microbiology Results printout.

#### Type(s) of Change

#### New Functionality

New option

### Watch the data in the LA global \[LA WATCH\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version

You can now watch the verifiable data in the ^LAH global using this option.

#### Type(s) of Change

#### New Functionality

### Audit of deleted/edited comments \[LRDCOM\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 92-34)

The option, Audit of Deleted Comments \[LRDCOM\], lists edited comments also. The program also did not allow anyone without the LRSUPER key to delete comments.

#### New Version Correction/Change

The option was renamed and the report now is captioned to read, "DELETED/EDITED COMMENTS".

The program now allows the deletion of comments without the user having the LRSUPER key. However, all computer generated comments such as "TESTNAME incorrectly reported as VALUE" cannot be deleted unless the user has the LRSUPER key.

#### Type(s) of Change

#### Name Change

New Functionality

### Changes in verified lab data \[LRUER\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version

A new option, Changes in Verified Lab Data \[LRUER\], has been added to the Supervisor menu \[LRSUPERVISOR\] to allow tracking of changes in verified laboratory results for "CH" subscripted tests for quality assurance purposes. This option is somewhat analogous to the Audit data changes report option for Blood Bank.

There are two choices for this option. One choice, the "reported incorrectly as" comments, reports the changes made in verified data and the other, the "specimen rejected" comments, when the lab collection team rejects

#### Type(s) of Change

#### New Functionality

New Option

### ### Search for Critical Value Flagged Tests \[LRSORC\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 87-68, 87-103, 92-34)

The Search for Critical Value Flagged Tests \[LRSORC\] option will not allow you to sort by accession area and the report does not have the collection date for the specimen.

#### New Version Correction/Change

## ## Version 5.2 will allow you to sort by accession area, patient name or location. The collection date is also printed.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Type(s) of Change

#### New Functionality

### Search for High/Low Values of a Test \[LRSORA\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 88-59, 89-04, 92-48)

When the High/Low Value search is printed, the date for the specimen does not contain the year. This causes confusion if the search has dates from different years. The report does not have the collection date for the specimen.

#### New Version Correction/Change

When you print a High/Low Value search, the year appears as part of the date of the specimen. The report has also been reformatted to make it easier to read. The collection date is also printed.

#### Type(s) of Change

#### New Functionality

Output Redesigned

### Summary List (Extended Supervisor's) \[LRLISTE\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 86-12, 87-65, 87-101, 92-59)

The Summary List (Supervisor's) report showed the last person to verify a test in an accession number. Multiple people could have verified individual tests on that accession number but there was not a record of who verified what.

#### New Version Correction/Change

The new report now indicates if more than one person did the verifying.

#### Type(s) of Change

#### New option

### VA FileMan \[DIUSER\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem

Many sites did not allow their Lab Supervisors or Laboratory Information Managers (LIMs) full FileMan menu access. Every time the lab package was installed, they had to manipulate the menus to remove the VA FileMan menu and put the approved local variant on the menu.

#### New Version Correction/Change

With Version 5.2, VA FileMan will not be exported with the Laboratory package. IF you need to keep this menu, you MUST have your IRM assign it to you.

#### Type(s) of Change

#### menu change

### Diagram Menus \[XUUSERACC\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version Change

With Version 5.2, this option will not be exported with the Laboratory package. IF you need to keep this option, you MUST have your IRM assign it to you.

#### Type(s) of Change

#### menu change

## Technical Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Hooks for Timing Response Log

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version

Hooks have been added so that the "process time" for Lab processes can be monitored by the System Manager.

#### Type(s) of Change

#### New Functionality

### Kernel Form Feed Standard

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version (E3R 92-94, 93-37)

Version 5.2 of the Laboratory package conforms to the new Form Feed standard that Kernel 7.0 addressed. The reports do not start with a form feed but will end with one.

#### Type(s) of Change

#### New Functionality

New Requirement

### File 69.9 - Collection List Build \$H field

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 91-07)

The program displayed the date in the \$H format which is hard to read.

#### New Version Correction/Change

The program now displays the date in an eye readable format.

#### Type(s) of Change

#### Change in Functionality

### Programming Change - Locks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### New Version 

All locks are now incremental.

#### Type(s) of Change

#### Change in Functionality

### Container Field, LABORATORY TEST file 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Old Version (NOIS MAD-0491-40001)

The information in the COLLECTION SAMPLE FILE (#62) could be changed without causing a corresponding change in the LABORATORY TEST file (#60).

#### New Version Correction/Change

The files were changed so that the Container field, in the LABORATORY TEST file (#60), is now a computed field. The field will be automatically filled in by the system if there is a Tube Top Color (Field \#3) defined in the COLLECTION SAMPLE FILE (#62) for that collection sample.

#### Type(s) of Change

#### Change in Functionality

### Misspelling in Routine 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Old Version (NOIS TAC-0394-50019)

The word ACCESSIONS is misspelled as ACCESIONS in the routine LRAPDA.

#### New Version Correction/Change

Corrected.

#### Type(s) of Change

#### Corrected spelling

### Removal of Obsolete Field

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Old Version (NOIS ISH-121-40001)

The field, Can Be Ordered Stat, in the ACCESSION TEST GROUP file (#62.6) was only partially removed with Version 5.1. Some sites, that had entries in that field, did not have the field completely removed.

#### New Version Correction/Change

The field is removed to avoid any confusion with the urgency determinants in OE/RR Version 2.5.

#### Type(s) of Change

#### Corrected spelling

## General Functionality Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Display STAT on Verify Screens

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 87-97)

There is no indication that an order is STAT when you verify a test.

#### New Version Correction/Change

When verifying tests, a warning will be displayed is that test has a STAT urgency. The warning will display if the Urgency Alert field (#613) in the LABORATORY SITE file (#69.9) has an entry

#### Type(s) of Change

#### New Functionality

Output Redesigned

### Bar code enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 87-105)

The laboratory package did not have the capability to automatically print bar code labels with the accession number.

#### New Version Correction/Change

Bar code labels can be set up to automatically print for a particular accession area. Routines have been written for the OTC and Intermec printers.

#### Type(s) of Change

#### New Functionality

## ## ### Provider name/title/key 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 88-127, 89-88, 90-76, 90-82)

The provider name, title and abbreviation were handled differently depending on what option was being used. Some options looked at the patient file for the provider name and some to the provider file and some to the person file.

#### #### New Version correction

All information concerning the provider will be in the NEW PERSON file (#200). The security keys, the title, the abbreviation and the name of the provider will all be in this file. Options will now need to look in only one file for provider information instead of the two or three files that had to be checked previously.

#### Type(s) of Change

#### Change in Functionality

New Requirement

### Show Order Comments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (94-08)

Order comments entered by Ward Order Entry do not show up on the interim report for microbiology. These order comments contain pertinent information entered by the ward that needs to be displayed to the user.

#### New Version Correction/Change

The comments are now printed on the interim reports.

#### Type(s) of Change

#### Change in Functionality

### Incomplete Test List 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 91-02)

1\. The program would place an "input only" test on the incomplete list and you could not remove the test from the list.

2\. Completed tests occasionally show up on the incomplete test list because the results were entered under the original accession date rather than the "rollover" today's date.

#### #### New Version Correction/Change

1\. The program does not put input only tests on the incomplete list.

2\. All tests are completed when entered under either the original accession date or today's date.

#### Type(s) of Change

#### Change in Functionality

### Display of Provider during Verification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 92-95)

The ordering provider was not displayed on the screen during result verification. This would facilitate provider notification for critical values.

#### New Version Correction/Change

All the verification options except group verify or batch verify displays the provider on the screen.

#### Type(s) of Change

#### Change in functionality

### Label printing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 87-40, 87-76)

If more than six tests were on a single accession number, some of the names were not printed on the label.

#### New Version Correction/Change

The new label routine will print \*\* if there are additional tests not on the label.

#### Type(s) of Change

#### New Functionality

### ### ### New Documentation Subfile

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 93-15)

The sites did not have a place to put on-line documentation.

#### New Version Correction/Change

A new subfile, Site Notes Date, was placed in field (#505) in the LABORATORY TEST file (#60), field (#501) in the EXECUTE CODE file (#62.07), and field (#107) in the AUTO INSTRUMENT file (#62.4). It is a date/time multiple that can be used to document any changes to these files

#### Type(s) of Change

#### New Functionality

Data Dictionary change

### Cumulative Update

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 88-130, 91-82, 93-20)

1\. You cannot print the outpatient and inpatient cumulatives at different times.

2\. The locations entered in the Separate Report Location field do not print in the terminal digit order as the other cumulative do.

3\. Additional file room report locations are needed for file rooms in outpatient labs, which are in separate locations.

#### New Version Correction/Change

The new functionality for the Cumulative allows different groups of cumulative to be printed at separate times. All cumulatives designated as separate file rooms now print in the terminal digit order and additional file room report locations can be created.

A new option was created to allow the tasking of the fileroom cumulative. The option is Task Cumulative Fileroom Report \[LRTASK CUM FILEROOM\].

#### Type(s) of Change

#### New Functionality

Data Dictionary change

New Option

### Ektachem problems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 92-64, 93-30)

1\. The download will fail if the number one cup has an accession with a specimen type other than one that the Ektachem will accept.

2\. The names for samples accessioned for files other than PATIENT will not transmit when downloaded by the LADOWN routine.

#### New Version Correction/Change

1\. The routine now sets a default specimen type of serum that corrects this problem.

2\. The LADOWN routine accepts the names for samples from all the files (such as REFERRAL PATIENT (#67), RESEARCH (#67.1), etc.,).

#### Type(s) of Change

#### Coding Change

### LRTASK CONJAM routine change

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 94-05)

The controls accessioned by the nightly job can be assigned a strange LAB ARRIVAL TIME such as 09/21/93 01:81.

#### New Version Correction/Change

The tasked job now checks the system clock rather than just counting the minutes form the time the task is queued to run.

#### Type(s) of Change

#### Coding Change

## Workload Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Updating WKLD code file 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem

Due to the explosive growth of new methods and instrumentation, the College of American Pathologist could not update their workload codes (CAP codes) fast enough to keep pace with the demand from the field. Each site was able to create their own "code" but this led to confusion between sites.

#### New Version Correction/Change

To keep pace with the demand from the field, CAP codes will be replaced with WKLD codes created and controlled by the Laboratory package of the DHCP. All DHCP sites will use the same set of codes and only the Laboratory developers will be able to add new codes.

#### Type(s) of Change

#### New Functionality

### Venipuncture Workload codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Old Version Problem (E3R 88-64)

The venipuncture (travel time) procedure code associated with the LAB COLLECT accessions was not being properly counted. At the same time, the venipuncture procedure code associated with SEND PATIENT accessions was not being captured.

#### New Version Correction/Change

The venipuncture counts can be collected automatically with Version 5.2.

#### Type(s) of Change

New Functionality

### E3Rs addressed by Workload rewrite

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

87-47 Count Accession Tests option should allow you to select one particular test, one particular location or a combination of the two.

88-65 CAP Statistics by Treating Area should allow sorting for Ambulatory Care clinics.

88-67 AMIS/CAP procedure name linked to site/specimen - need to allow the DEFAULT: YES and the AMIS/CAP CODE TEST name to be linked to the SITE/SPECIMEN multiple in File 60.

88-69 AMIS/CAP procedure code suffix number: the same test may be done on different instruments but only one suffix code is allowed as a default

89-83 Workload reporting - CAP statistics are captured for all tests not just the ones that have AMIS/CAP procedures defined

89-85 CAP workload reporting - edit CAP procedure using the EW option

89-86 CAP workload counts - CAP statistics should be a part of the LOAD/WORKLIST file

90-16 Tests that are canceled are still counted for the AMIS/CAP procedure

90-92 Have the ability to request a summary or the full BB AMIS report

91-19 Allow duplicate CAP codes under same test - allow entry of duplicate CAP codes under the same test on an accession number

91-36 Blood Team AMIS counts - AMIS counts for the number of patients drawn by the lab phlebotomy team must be done manually.

91-269 AMIS/CAP portion: modified so that duplicate CAP codes may be entered

92-13 Need ability to print all counting options by location or by individual test.

92-33 Count Accession Test option should be able to sort by one location for all accession areas.

#### New Version

These E3Rs are considered completed with the new workload functionality.

#### Type(s) of Change

#### New Functionality

## REFERENCE SECTION

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## ## ## ## ## ## List of New Options/Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

LR ARCHIVE NP CONVERSION Convert archived data to use New Person file

LR BARCODE FORMAT LOAD Download Format for Intermec Printer

LR LIM/WKLD MENU LIM workload menu

LR PROCESS, MISC Misc. Processing

LR ROLLOVER Rollover Accession (Manual)

LR SUPER/WKLD MENU Supervisor workload menu

LR TASK CUM FILEROOM Task Cumulative Fileroom Report

LR WKLD LMIP 1 PHASE 1: Move data from 64.1 to 67.9

LR WKLD LMIP 1 REPEAT Recompile Phase 1 LMIP Data

LR WKLD LMIP 2 PHASE 2: Collect data for transmit to NDB

LR WKLD LMIP 3 PHASE 3: Print of data to be sent to NDB

LR WKLD LMIP 4 PHASE 4: Create E-mail message for NDB

LR WKLD LMIP 5 PHASE 5: Purge monthly WKLD data from 67.9

LR WKLD4 LMIP Reports/Data Collection

LR WKLD AUDIT Review Accession Workload

LR WKLD STD/QC/REPS Std/QC/Reps Manual Workload count

LRAC MANUAL FILEROOM CUM Manual Queuing of Fileroom Cum

LRAPAFIP AFIP registries

LRAPAUA Alphabetical autopsy list

LRAPAUPAD Provisional anatomic diagnoses

LRAPAUPT Autopsy protocol/supplementary report

LRAPMV Move anatomic path accession

LRAPPG Persian gulf veterans

LRAPW Workload, anat path

LRAPWE EM scanning and photo workload

LRAPWR Cytopathology screening workload

LRAPWRSP Surg path gross assistance workload

LRAUMLK Autopsy Slide Labels (generic)

LRBLA Blood Bank Administrative Data

LRBLAA Crossmatch/Transfusions by Specialty/Physician

LRBLCN Blood bank consultation reports

LRBLJM Edit pooled blood product

LRBLPH Patient Medication List

LRBLPOST File 81 conversion

LRBLPTXR Unknown unit transfusion reaction

LRBLQSDD Single donor demographic information

LRBLSRQ Blood component request edit

LRBLSW Blood bank workload

LRBLTA Transfusion reaction count

LRBLVAL Blood Bank validation documentation

LRBLVALI Validation documentation

LRBLVALP Print blood bank validation

LRCAP CODE ADD Add a new WKLD code to file

LRCAPAM5 RCS-CDR/LMIP REPORT

LRCAPD Workload code list

LRCAPDL WKLD log file download

LRCAPF Etiology WKLD Code Stuffer

LRCAPMA Workload Statistics by Major Section

LRCAPML Workload cost report by major section

LRCAPR1 Workload Report

LRCAPTS Treating Specialty Workload Report

LRFASTS Fast Bypass Data Entry/Verify

LRLABXOL Reprint order accession label(s)

LRLISTE Summary list (extended supervisors')

LRMITS Microbiology Trend Report

LRMIXALL Re-index Antimicrobial Suscept File (62.06)

LROW IMMED COLLECT Fast lab test order (IMMEDIATE COLLECT)

LRRP5 Lab orders by collection type

LRRP6 Detail workload report

LRRP8 Workload statistics by accession area and shift

LRSTOPC Manual Enter Clinic Stop Codes

LRTASK CUM FILEROOM TASK CUMULATIVE FILEROOM REPORT

LRUER Changes in verified lab data

LRUFCL Print Future Collection Labels

LRUFCLS Print Single Future Collection Label

LRUV Edit referral patient file

LRUWL Display workload for an accession

## List of Deleted Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The first section of LR CAP options are being deleted due to the change of workload recording functions with this version. (They are replaced with LR WKLD options that perform similar functions.)

The second listing consists of:

1\. Other LR options that are no longer needed.

2\. Options that are old ones that have not been attached to active menus for more than one version.

3\. Others are old menus that need to be cleaned out of the program.

LR CAP Lab statistics menu

LR CAP CODE BY CODE CAP code list by code

LR CAP CODE BY NAME CAP code list by name

LR CAP COMMENTS Edit Workload Comments

LR CAP MANUAL Manually compile CAP and workload counts

LR CAP REQUEST Requesting center dictionary

LR CAP MANUAL INPUT Workload Manual Input

LR CAP SECTION BY CODE Lab section list by code

LR CAP SECTION BY NAME Lab section list by name

LR CAP SERVICE Service dictionary

LR CAP STATS ON Turn on site workload statistics

LR CAP STATS ON ACC AREA Turn on workload stats for accession area

LR CAP STD/QC/REPS Std/QC/Reps Manual workload count

LR CAP SUB BY SECTION Lab subsection by Lab section

LR CAP SUBSECTION Lab subsection list

LR CAP TEST DICT Test dictionary

LR CAP2 CAP statistics reports

LR CAP3 File listings

LRCAPL CAP statistics by Treating Area

LR CAP1 Edit CAP options

LRAPRPT Pathology reports for a patient

LRAPSGL Print a pathology report for a patient

LRAU Autopsy pathology

LRAUDA Data entry, Autopsy Path

LRAUDAA Autopsy protocol & ICD9CM coding

LRAUDAB Autopsy protocol & SNOMED coding

LRAUDAC SNOMED coding, Autopsy Path

LRAUDAI ICD9CM coding, Autopsy Path

LRAUDAP Autopsy protocol

LRAUDAR Delete autopsy protocols by date

LRAUDAS Special studies, Autopsy

LRAUFAD Final Autopsy Diagnoses Date

LRAULG Log-in, Autopsy path

LRAUP Print option, Autopsy path

LRAUPRO Protocols, Autopsy

LRAURV Autopsy Data Review

LRAUS Search options, Autopsy path

LRAUSM Morphology field search, Autopsy path

LRAUSD Disease field search, Autopsy path

LRAUSF Function field search, Autopsy path

LRAUSE Etiology field search, Autopsy path

LRAUSI ICD9CM code search, Autopsy path

LRAUSP Procedure field search, Autopsy path

LRAUSTATUS Autopsy status list

LRCAPE Edit CAP defaults and param for individual tests

LRCAPE1 Edit/setup entries for CAP statistics

LRCAPE2 Edit CAP param for all tests

LRCAPED Manual edit of CAP and WORKLOAD data.

LRCAPS CAP statistics summary

LRCAPW CAP workload statistics

LRCY Cytopathology

LRCYCUM Display cytopath reports for a patient

LRCYDA Data entry, Cytopath

LRCYDAA Gross review/Microscopic/ICD9CM coding, Cytopath

LRCYDAB Gross review/Microscopic/SNOMED coding, Cytopath

LRCYDAC SNOMED coding, Cytopath

LRCYDAE Modify cytopath micro/dx description

LRCYDAG Gross description/Clinical Hx, Cytopath

LRCYDAI ICD9CM coding, Cytopath

LRCYDAM Microscopic/Gross review, Cytopath

LRCYDAP Spec Studies-EM;Immuno;Consult;Pic, Cytopath

LRCYDAR Delete Cytopath descriptions by date

LRCYDAS Supplementary report, Cytopath

LRCYLG Log-in, Cytopath

LRCYOLD Enter old cytopath records

LRCYP Print option, Cytopath

LRCYRPT Final cytopath reports

LRCYS Search options, Cytopath

LRCYSGL Print cytopathology report for a patient

LRCYWORK Cumulative reports for cytopath micro exams

LRDOWN 1 Download a load list to an Instrument.

LREM Electron microscopy

LREMCUM Display EM reports for a patient

LREMDA Data entry, EM

LREMDAA Gross review/Microscopic/ICD9CM coding, EM

LREMDAB Gross review/Microscopic/SNOMED coding, EM

LREMDAC SNOMED coding, EM

LREMDAE Modify EM micro/dx description

LREMDAG Gross description/Clinical Hx, EM

LREMDAI ICD9CM coding, EM

LREMDAM Microscopic/Gross review, EM

LREMDAP Spec studies-Immuno;Consult;Photo, EM

LREMDAR Delete EM descriptions by date

LREMDAS Supplemental report, EM

LREMLG Log-in, EM

LREMOLD Enter old EM records

LREMP Print option, EM

LREMRPT Final EM reports

LREMS Search options, EM

LREMSGL Print electron microscopy report for a patient

LREMWORK Cum report for micro exams, EM

LRLIASON Lab liaison menu

LRMITRZ Antimicrobial trends report

LRMIULDF Quick Accessioning

LRSNOMEDIT Enter/edit items in a SNOMED field

LRSP Surgical pathology

LRSPCUM Display surg path reports for a patient

LRSPDA Data entry, Surg path

LRSPDAA Gross review/Microscopic/ICD9CM coding, Surg Path

LRSPDAB Gross review/Microscopic/SNOMED Coding, Surg Path

LRSPDAC SNOMED coding, Surg Path

LRSPDAE Modify surg path micro/dx description

LRSPDAG Gross Description/Clinical Hx, Surg Path

LRSPDAI ICD9CM coding, Surg Path

LRSPDAM Microscopic/Gross Review, Surg Path

LRSPDAP Spec Studies-EM;Immuno;Consult;Pic, Surg Path

LRSPDAR Delete Surg Path Descriptions by Date

LRSPDAS Supplementary Report, Surg Path

LRSPDAT Blocks, Stains, Procedures

LRSPDES Enter/edit lab description file

LRSPLG Log-in, Surg path

LRSPOLD Enter old surg path records

LRSPP Print option, Surg path

LRSPRPT Final Surgical Path Reports

LRSPS Search options, Surg path

LRSPSD DISEASE code search, SNOMED

LRSPSE ETIOLOGY code search, SNOMED

LRSPSF FUNCTION code search, SNOMED

LRSPSGL Print surgical pathology report for a patient

LRSPSI ICD9CM code search

LRSPSM MORPHOLOGY code search, SNOMED

LRSPSP PROCEDURE code search, SNOMED

LRSPWORK Gross Reports for Surg Path Micro Exams

LRTASK PHSET2 CREATE A COLLECTION LIST

LRUAP Log book

LRUCN Blood bank consultation reports

LRUDEL Delete an accession number

LRULY Log-in

## List of Options with Menu Text/Name changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Menu text changed.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From LRACC4 Work sheet of all unverified accession for a date

To LRACC4 Work sheet of all unverified accessions for a date

From LRAPAUL List of path cases by resident, tech or , senior

To LRAPAUL Path cases by resident, tech, senior or clinician

From LRAPCYPCT % Pos, Neg, Susp, & Unsat cytopath specimens

To LRAPCYPCT % Pos, Atyp, Dysp, Neg, Susp, Unsat cytopath

From LRAPDGS Gross review/Microscopic/SNOMED

To LRAPDGS FS/Gross/Micro/Dx/SNOMED Coding

From LRAPDGM Microscopic/Gross Review

To LRAPDGM FS/Gross/Micro/Dx

From LRAPDGI Gross/Review/Microscopic/ICD9CM coding

To LRAPDGI FS/Gross/Micro/DX/ICD9CM coding

From LRAPED Edit log-in data, anat path

To LRAPED Edit log-in & clinical hx, anat path

From LRAPEDC Edit anat path specimen comments

To LRAPEDC Edit anat path comments

From LRAPHDR Edit pathology report parameters

To LRAPHDR Edit pathology parameters

From LRAPM Modify anat path micro/dx

To LRAPM Modify anat path gross/micro/dx/frozen section

From LRAPMOD Print path micro/dx modifications

To LRAPMOD Print path modifications

From LRBLITS Transfusion statistics by specialty

To LRBLITS Transfusion by treating specialty/physician

From LRBLSEU Edit donor utility file

To LRBLSEU Edit blood bank utility file

From LRDCOM Audit of deleted comments

To LRDCOM Audit of deleted/edited comments

From LRMENU Laboratory

To LRMENU Laboratory DHCP Menu

From LROPTLST Listing of Laboratory Menus/Options

To LROPTLST Listing of Laboratory Menus/Options

### Name Changed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From LR CAP Lab statistics menu

To LR WKLD Lab statistics menu

From LR CAP COMMENTS Edit Workload Comments

To LR WKLD COMMENTS Edit Workload Comments

From LR CAP REQUEST Requesting center dictionary

To LR WKLD REQUEST Requesting center dictionary

From LR CAP MANUAL INPUT Workload Manual Input

To LR WKLD MANUAL INPUT Workload Manual Input

From LR CAP SECTION BY CODE Lab section list by code

To LR WKLD SECTION BY CODE Lab section list by code

From LR CAP SECTION BY NAME Lab section list by name

To LR WKLD SECTION BY NAME Lab section list by name

From LR CAP SERVICE Service dictionary

To LR WKLD SERVICE Service dictionary

From LR CAP SUB BY SECTION Lab subsection by Lab section

To LR WKLD SUB BY SECTION Lab subsection by Lab section

From LR CAP SUBSECTION Lab subsection list

To LR WKLD SUBSECTION Lab subsection list

From LR CAP TEST DICT Test dictionary

To LR WKLD TEST DICT Test dictionary

From LR CAP3 File listings

To LR WKLD3 File listings

### Name and Menu Text changed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From LR CAP CODE BY CODE CAP code list by code

To LR WKLD CODE BY CODE WKLD code list by code

From LR CAP CODE BY NAME CAP code list by name

To LR WKLD CODE BY NAME WKLD code list by name

From LR CAP MANUAL Manually compile CAP and workload counts

To LR WKLD MANUAL Manually compile WKLD and workload counts

From LR CAP2 CAP statistics reports

To LR WKLD2 WKLD statistics reports

## New Help Frames

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These are the new Help Frames that are exported with Version 5.2. They all relate to the new Microbiology Trend Report. These are the only legitimate Help Frames for the Laboratory package. All other Help Frames are obsolete.

LRMITS AP Micro Trend Antibiotic Pattern

LRMITS CRITERIA Micro Trend Report Criteria

LRMITS DEFAULTS Micro Trend Default Reports

LRMITS DETAIL Micro Trend Detailed Reports

LRMITS GENERAL Micro Trend General Description

LRMITS LOS Micro Trend Length of Stay

LRMITS MERGE Micro Trend Merge Criteria

LRMITS OPTION Micro Trend Option

LRMITS OTYPE Micro Trend Organism Types

LRMITS PRINT Micro Trend Printing Reports

LRMITS REPORT TYPES Micro Trend Report Types

LRMITS SORG Micro Trend Specific Organisms

LRMITS TIME RANGE Micro Trend Time Range

Example:

Select Microbiology print menu Option: ?MICROBIOLOGY TREND REPORT

Micro Trend Option

Antibiotic Trends Report

This report is used by the Laboratory to look for changes or trends in

susceptibility patterns. Select a specific topic for further information.

Topics:

General Description

Default Reports

Report Types

Criteria for Reports

Time Range

Types of Organisms

Specific Organisms

Length of Stay

Antibiotic Pattern

Merge Criteria

Detailed Reports

Printing Reports

RELATED HELP FRAME KEYWORD

------------------ -------

1 Micro Trend General Description \[GENERAL DESCRIPTION\]

2 Micro Trend Default Reports \[DEFAULT REPORTS\]

3 Micro Trend Report Types \[REPORT TYPES\]

4 Micro Trend Report Criteria \[CRITERIA FOR REPORTS\]

5 Micro Trend Time Range \[TIME RANGE\]

6 Micro Trend Organism Types \[TYPES OF ORGANISMS\]

7 Micro Trend Specific Organisms \[SPECIFIC ORGANISMS\]

8 Micro Trend Length of Stay \[LENGTH OF STAY\]

9 Micro Trend Antibiotic Pattern \[ANTIBIOTIC PATTERN\]

10 Micro Trend Merge Criteria \[MERGE CRITERIA\]

11 Micro Trend Detailed Reports \[DETAILED REPORTS\]

12 Micro Trend Printing Reports \[PRINTING REPORTS\]

\* - Recently viewed help frame

Select HELP SYSTEM action or \<return\>: \<RET\>

## OE/RR Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These routines are in the LR namespaced but are actually part of the OE/RR package. As that package changes, these routines may be changed or deleted.

LRO ;SLC/DCM - Being replaced ;1/10/91 16:0 ;

LRO1 ;SLC/DCM - Being replaced ; 3/9/89 19:39 ;

LRO2 ;SLC/DCM - Being replaced ;1/10/91 16:01 ;

LRO3 ;SLC/DCM - Being replaced ; 7/3/89 15:07 ;

LRO4 ;SLC/DCM - Being replaced ;1/31/91 08:46 ;

LRO5 ;SLC/DCM - Being replaced ;1/10/91 16:01 ;

LRO6 ;SLC/DCM - Being replaced ; 2/14/89 18:07 ;

LRO7 ;SLC/DCM - Being replaced ;1/9/91 17:32 ;

LRO8 ;SLC/DCM - Being replaced ;1/10/91 16:0 ;

LRORDST1 ;SLC/CJS/RWF - Being replaced ;3/29/90 16:40 ;

LROSX0 ;SLC/DCM - Being replaced ;1/29/91 14:44

LROSX1 ;SLC/DCM - Being replaced ;7/17/90 12:17

## List of Completed E3R's by Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

E3R Page Number

86-04 88

86-12 116

87-101 116

87-103 115

87-105 121

87-40 124

87-47 128

87-53 91

87-65, 116

87-67 100

87-68 115

87-72 88

87-76 124

87-97 121

88-111 98

88-127 81, 122

88-130 125

88-19 89

88-20 110

88-59 116

88-64 127

88-65 110, 128

88-66 110

88-67 128

88-69 128

89-04 116

89-09 98

89-11 45

89-12 95

89-30 100

89-34 95

89-37 40

89-38 37

89-69 41

89-83 128

89-85 128

89-86 128

89-87 57, 75

89-88 122

89-92 41

89-98 33

90-16 128

90-21 100

90-26 102

E3R Page Number

90-27 41

90-41 32

90-46 57, 75

90-54 87

90-63 96

90-64 93

90-65 91

90-69 100

90-76 122

90-79 38

90-82 122

90-83 88

90-92 128

91-02 123

91-04 110

91-06 110

91-07 118

91-09 96

91-112 41

91-118 37

91-122 67

91-15 62

91-19 128

91-24 67

91-269 128

91-29 65

91-36 128

91-37 29, 36

91-66 61

91-73 85

91-78 41

91-82 125

91-86 102

91-91 68

91-96 37

91-97 32

92-02 58

92-03 88

92-06 63

92-08 85

92-11 98

92-13 128

92-15 47

92-18 75

E3R Page Number

92-31 70, 71, 72

92-32 65

92-33 128

92-34 114, 115

92-37 63

92-40 68

92-48 116

92-53 30

92-55 30

92-59 116

92-64 126

92-70 96

92-77 79

92-78 80

92-86 33

92-94 118

92-95 124

92-96 99

93-02 35

93-06 64, 80

93-07 86

93-09 59

93-15 125

93-20 125

93-23 90

93-25 30

93-27 66

93-35) 74

93-36 79

93-37 118

93-47 85

93-49 87

93-50 62

93-59 102

94-06 89

94-08 122

94-20 112

INDEX

<span id="_Toc506704515" class="anchor"></span>

# Index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

%
% Pos, Atyp, Dysp, Neg, Susp, Unsat cytopath \[LRAPCYPCT\] · 76
8
86-04 · 103
86-12 · 135
87-101 · 135
87-103 · 134
87-105 · 141
87-40 · 143
87-47 · 148
87-53 · 107
87-65, · 135
87-67 · 114
87-68 · 134
87-72 · 103
87-76 · 143
87-97 · 140
88-127 · 97, 141
88-130 · 145
88-19 · 104
88-20 · 128
88-59 · 135
88-64 · 147
88-65 · 128, 148
88-66 · 128
88-67 · 148
88-69 · 148
89-04 · 135
89-11 · 55
89-12 · 110
89-30 · 114
89-34 · 110
89-38 · 46
89-83 · 148
89-85 · 148
89-86 · 148
89-87 · 67, 92
89-88 · 141
89-92 · 50
89-98 · 42
9
90-16 · 148
90-21 · 114
90-26 · 117
90-41 · 41
90-46 · 67, 92
90-54 · 102
90-63 · 111
90-64 · 109
90-65 · 107
90-69 · 114
90-76 · 141
90-79 · 47
90-82 · 141
90-83 · 103
90-92 · 148
91-02 · 142
91-04 · 128
91-06 · 128
91-07 · 138
91-09 · 111
91-118 · 46
91-122 · 80
91-15 · 73
91-19 · 148
91-24 · 80
91-269 · 149
91-29 · 76
91-36 · 148
91-37 · 37, 45
91-66 · 72
91-73 · 100
91-82 · 145
91-86 · 117
91-91 · 82
91-96 · 46
91-97 · 41
92-02 · 68
92-03 · 103
92-06 · 74
92-08 · 100
92-11 · 112
92-13 · 149
92-15 · 57
92-18 · 91
92-31 · 86, 87, 88
92-32 · 76
92-33 · 149
92-34 · 133, 134
92-37 · 74
92-40 · 83
92-48 · 135
92-53 · 38
92-55 · 38
92-59 · 135
92-64 · 146
92-70 · 111
92-77 · 95
92-78 · 96
92-86 · 43
92-94 · 137
92-95 · 143
92-96 · 113
93-02 · 44
93-06 · 75, 96
93-07 · 101
93-09 · 70
93-15 · 144
93-20 · 145
93-23 · 105
93-25 · 38
93-27 · 78
93-35) · 90
93-36 · 95
93-37 · 137
93-47 · 100
93-49 · 102
93-50 · 73
93-59 · 118
94-06 · 105
94-08 · 142
94-20 · 130
A
Accession list with stains \[LRAPSA\] · 78
Accessioning tests ordered by ward order entry \[LROE\] · 102
Add a new WKLD code to file \[LRCAP CODE ADD\] · 120
Add/Edit QC Name and/or Edit Test Names \[LRQCADDNAME\] · 110
Alphabetical autopsy list \[LRAPAUA\] · 75
Anatomic pathology turnaround time \[LRAPTT\] · 89
Autologous Disposition report \[LRBLJB\] · 51
Autopsy Assistant field · 95
Autopsy Slide Labels \[LRAUMLK\] · 78
B
Bar code enhancements · 141
Blood bank inventory integrity report \[LRBLII\] · 57
Blood Bank validation documentation \[LRBLVAL\] · 56
Blood bank workload \[LRBLSW\] · 58
Blood component request edit \[LRBLSRQ\] · 56
BLOOD COMPONENT REQUEST file ( · 66.9)
C
Change in functionality · 112, 113, 118, 143
Change in Functionality · 57, 58, 111, 114, 119, 138, 139, 141, 142
Changes in verified lab data \[LRUER\] · 134
Check Files for Inconsistencies \[LRCHKFILES\] · 120
Coding Change · 146
Convert Archived Data to Use New Person file \[LR ARCHIVE NP CONVERSION\] · 120
Corrected spelling · 117, 139, 140
CPT file ( · 81)
Cum path data summaries \[LRAPT\] · 80
Cytopathology screening workload \[LRAPWR\] · 93
D
Data compilation for Workload · 63
Data Dictionary · 70, 71
Data Dictionary change · 43, 53, 61, 62, 144, 145
Data Dictionary Change · 40, 42, 57, 61, 67, 69, 73, 76, 78, 80, 84, 95, 96
Delete anat path descriptions by date \[LRAPDAR\] · 82
deletion of comments · 133
Detail workload report \[LRRP6\] · 123
Diagram Menus \[XUUSERACC\] · 136
Display STAT on Verify Screens · 140
Display workload for an accession \[LRUWL\] · 58, 93
Disposition-relocation \[LRBLIDR\] · 41
Donor Options · 37
Download Format for Intermec Printer \[LR BARCODE FORMAT LOAD\] · 122
E
Edit blood bank utility file \[LRBLSEU\] · 55
Edit Donor History Questions \[LRBLSEH\] · 54
Edit log-in & clinical hx, anat path \[LRAPED\] · 69
Edit pathology parameters \[LRAPHDR\] · 83
Edit pooled blood product \[LRBLJM\] · 55
Edit Referral patient file \[LRUV\] · 90
Edit unit disposition fields \[LRBLSED\] · 54
Edit/print/display preselected lab tests \[LRUMD\] · 91
EM scanning and photo workload \[LRAPWE\] · 94
Enter crossmatch results \[LRBLPX\] · 43
Etiology WKLD Codes (Force) \[LRCAPF\] · 123
extended syntax · 75
F
Fast bypass data entry/verify \[LRFASTS\] · 109
Fast Lab Test Order (SEND PATIENT) \[LROW SEND PAT\] · 102
File 81 conversion \[LRBLPOST\] · 124
File 81 Conversion \[LRBLPOST\] · 61
Frozen section, surgical path correlation \[LRAPQAFS\] · 86
H
Hooks for Timing Response Log · 137
I
Inquiries, anat path menu \[LRAPI\] changes · 72
Inquiry Options · 45
Inventory ABO/Rh testing worksheet \[LRBLIW\] · 43
K
Kernel Form Feed Standard · 137
L
Lab order by collection type \[LRRP5\] · 100
LIM workload menu \[LR LIM/WKLD MENU\] · 122
LMIP Reports/Data Collection \[LR WKLD4\] · 124
Log-in, anat path \[LRAPLG\] · 73
M
Malignancy review \[LRAPQAMR\] · 87
manual counts for Quality Control · 26
Manual Queuing of Fileroom Cum \[LRAC MANUAL FILEROOM CUM\] · 119
Maximum Surgical Blood Order Edit \[LRBLSMS\] · 61
menu change · 136
MIC Default Interpretation · 118
Microbiology Execute Codes · 117
Microbiology Trend Report \[LRMITS\] · 114
Misc. processing \[LR PROCESS, MISC\] · 108
Modify anat path gross/micro/dx/frozen section \[LRAPM\] · 70
Move anatomic path accession \[LRAPMV\] · 90
Multipurpose accessioning \[LRQUICK\] · 105
N
Name Change · 11, 15, 17, 21, 24, 25, 26, 30, 32, 52, 55, 68, 69, 70, 71, 76, 77, 84, 85, 133
new choice · 21
new field · 12, 13, 14, 15, 16, 20, 22, 25, 26, 27, 28, 30, 31, 32, 33, 59
new field · 16, 32
new fields · 14, 16
new file · 17, 18, 21, 23, 24
New Functionality · 37, 40, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 61, 63, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 82, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 113, 114, 115, 116, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 137, 140, 141, 143, 144, 145, 147, 149
New Menu · 58, 88, 93, 108, 122, 124, 127
new multiple field · 12
New option · 103, 128, 132, 135
New Option · 45, 46, 47, 48, 49, 50, 51, 52, 53, 55, 56, 58, 61, 67, 75, 79, 89, 90, 92, 93, 94, 100, 101, 104, 105, 108, 109, 114, 119, 120, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 134, 145
New Prompt · 46, 47, 82, 86, 87, 88
New Requirement · 137, 141
new subfield · 20, 21, 22
new subfile · 11, 12, 13, 14, 15, 30
NOIS CLL-0992-40001 · 58
NOIS GRJ-1093-50007 · 111
NOIS ISH-1092-40002 · 112
NOIS ISH-121-40001 · 140
NOIS MAD-0491-40001 · 139
NOIS MIW-1291-40002 · 48
NOIS TAC-0394-50019 · 139
O
OPERATION (MSBOS) file ( · 66.5)
Order/Test Status \[LROS\] · 101
Output Redesigned · 42, 46, 47, 48, 49, 50, 114, 135, 140
P
Patch to Version 5.1 · 40, 54, 116
Patch To Version 5.1 · 42
Path cases by resident, tech, senior or clinician \[LRAPAUL\] · 76
Pathology Report Heading · 95
Patient blood bank record \[LRBLQDR\] · 46
Patient Medication List \[LRBLPH\] · 46
Persian Gulf Veterans \[LRAPPG\] · 89
PHASE 2: Collect data for transmit to NDB \[LR WKLD LMIP 2\] · 125
PHASE 3: Print of data to be sent to NDB \[LR WKLD LMIP 3\] · 126
PHASE 4: Create E-mail message for NDB \[LR WKLD LMIP 4\] · 126
Print blood bank validation \[LRBVALP\] · 53
Print Future Collection Labels \[LRUFCL\] · 100
Print path modifications \[LRAPMOD\] · 85
Print Single Future Collection Labels \[LRUFCLS\] · 101
Print single report only \[LRAP PRINT SINGLE\] · 75
Q
QA outcome review cases \[LRAPQOR\] · 87
Quality control display (Levy-Jennings) \[LRQC\] · 110
R
RCS-CDR/LMIP report \[LRCAPM5\] · 127
Recompile Phase 1 LMIP data \[LR WKLD LMIP 1 REPEAT\] · 127
Re-index Antimicrobial Suscept File (62.06) \[LRMIXALL\] · 132
Reprint a Permanent Page from Cumulative \[LRAC 1 PAGE\] · 119
Reprint order accession label(s) \[LRLABXOL\] · 105
Results entry (batch) \[LRMISTUF\] · 112
Review Accession Workload \[LR WKLD AUDIT\] · 114
S
Search for Critical Value Flagged Tests \[LRSORC\] · 134
Search for High/Low Values of a Test \[LRSORA\] · 135
Search options, anat path \[LRAPSEARCH\] · 72
Single donor demographic information \[LRBLQSDD\] · 45
Single donor information \[LRBLQSD\] · 47
SNOMED Code Field Definition · 96
Specimen log-in \[LRBLPLOGIN\] · 44
Std/QC/Repeats Manual Workload Count \[LR WKLD STD/QC/REPS\] · 26
Summary List (Extended Supervisor's) \[LRLISTE\] · 135
Supervisor workload menu \[LR SUPER/WKLD MENU\] · 127
Surg path gross assistance workload \[LRAPWRSP\] · 94
system failure · 32
T
Task Cumulative Fileroom Report \[LRTASK CUM FILEROOM\]. · 145
Transfused RBC for treating specialty \[LRBLJUT\] · 51
Transfusion reaction count \[LRBLTA\] · 49
Transfusion Reaction Records Changes · 59
Transfusion Reaction Report · 49
Treating Specialty Workload Report \[LRCAPTS\] · 128
Turn on site workload statistics \[LR WKLD STATS ON\] · 131
Typo in Micro report Display/Print · 117
U
Units available (indate/no disposition) \[LRBLRUA\] · 48
Unknown unit transfusion reaction \[LRBLPTXR\] · 56
Updated Vitek/Microscan section · 116
V
VA FileMan \[DIUSER\] · 136
Validation documentation \[LRBLVALI\] · 47
Verification of data by supervisor \[LRMIVER\] · 113
W
Watch the data in the LA global \[LA WATCH\] · 133
WKLD log file download \[LRCAPDL\] · 108
Workload code list \[LRCAPD\] · 128
Workload editing for Microbiology · 115
Workload Report \[LRCAPR1\] · 129
Workload statistics by accession area and shift \[LRRP8\] · 130
Workload Statistics by Major Section \[LRCAPMA\] · 130
Workload, anat path menu \[LRAPW\] changes · 93


---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: LA*5.2*68 Laboratory Release Notes

## Health Data Repository

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>Patch LA*5.2*68 allows the HL7 ORU message containing patient laboratory results to be transmitted to the subscriber, LA7 LAB RESULTS TO HDR (SUB). This subscriber protocol is used to transmit laboratory results to the VA HDR.</p>
<ul>
<li><p>After you activate sending messages to the HDR, extracting existing laboratory data (HDR historical) will follow, so that there will be an overlap with no gaps of laboratory data within the HDR.</p></li>
<li><p>Once you activate sending messages to the HDR, do not inactivate, as this can cause gaps of laboratory data within the HDR.</p></li>
<li><p>If you must inactivate sending messages to the HDR, contact the HDR program office, so that the laboratory data can be tracked and recovered.</p></li>
</ul></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### ## Blood Bank Clearance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>VISTA Laboratory Package patch LA*5.2*68 contains changes to software controlled by VHA DIRECTIVE 99-053, titled VISTA BLOOD BANK SOFTWARE. Changes include:</p>
<p>New style indexes have been created for the following sub-files</p>
<p>of the LAB DATA file (#63):</p>
<p>ELECTRON MICROSCOPY (#63.02)</p>
<p>SURGICAL PATHOLOGY (#63.08)</p>
<p>CYTOPATHOLOGY (#63.09)</p>
<p>All of the above changes have been reviewed by the VISTA Blood Bank Developer and found to have no impact on the VISTA BLOOD BANK SOFTWARE control functions.</p>
<p>RISK ANALYSIS: Changes made by patch LA*5.2*68 have no effect on Blood Bank software functionality, therefore RISK is none.</p>
<p>EFFECT ON BLOOD BANK FUNCTIONAL REQUIREMENTS: <strong>P</strong>atch LA*5.2*68 does not alter or modify any software design safeguards or safety critical elements functions.</p>
<p>POTENTIAL IMPACT ON SITES: This patch contains changes to 0 routines and 1 file identified in Veterans Health Administration (VHA) Directive 99-053, group B listing. The changes have no effect on Blood Bank functionality or medical device control functions. There is no adverse potential to sites.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Enhancements/New

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  The following protocols are added to the PROTOCOL file (#101).

NAME: LA7 LAB RESULTS ACTION

ITEM TEXT: Lab process results for HL7 messaging

TYPE: action

PACKAGE: AUTOMATED LAB INSTRUMENTS

DESCRIPTION: Action protocol to setup sending lab results to HL7 message subscribers via protocol LA7 LAB RESULTS AVAILABLE (EVN) - Lab Results Available Event. This protocol should be attached to protocol LAB RESULTS =\> EXTERNAL PACKAGE \[LR7O ALL EVSEND RESULTS\] which is an extended action protocol triggered by the lab result verification process.

ENTRY ACTION: D QUEUE^LA7HDR TIMESTAMP: 59056,40855

NAME: LA7 LAB RESULTS AVAILABLE (EVN) ITEM TEXT: Lab Results Available Event

TYPE: event driver CREATOR: LDSICREATOR,ONE

DESCRIPTION: A VistA Laboratory package HL7 ORU result message is created and sent by the HL package for transmission to any subscribers of event protocol LA7 LAB RESULTS AVAILABLE (EVN).

It provides the capability for the generation of a Laboratory HL7 ORU message containing patient laboratory results to subscribers of the HL7 event protocol LA7 LAB RESULTS AVAILABLE (EVN) as these results are made available within the Laboratory package.

The following subscripts are supported by the event: CH, MI, SP, CY, and EM.

TIMESTAMP: 59725,36770 SENDING APPLICATION: LA7LAB

TRANSACTION MESSAGE TYPE: ORU EVENT TYPE: R01

MESSAGE STRUCTURE: ORU_R01 ACCEPT ACK CODE: AL

APPLICATION ACK TYPE: NE VERSION ID: 2.4

RESPONSE PROCESSING ROUTINE: D ACK^LA7VHL

> SUBSCRIBERS: LA7 LAB RESULTS TO HDR (SUB)

NAME: LA7 LAB RESULTS TO HDR (SUB) ITEM TEXT: Send Lab Results to HDR

TYPE: subscriber CREATOR: LDSICREATOR,ONE

DESCRIPTION: This protocol should be attached to the HL7 event protocol LA7 LAB RESULTS AVAILABLE (EVN). See this protocol for further information.

This subscriber protocol is used by the Laboratory package to indicate to the HL package to send laboratory results to the VA Health Data Repository (HDR).

It utilizes the "Router" Subscriber Protocol supported by the VistA HL package. The routing logic uses the value of the parameter passed into the router to determine which Laboratory package subscript should be sent to the HDR.

> Examples

> ROUTING LOGIC: D RTR^LA7HDR("CH;") will only send to HDR results

> associated with Laboratory "CH" subscript.

> ROUTING LOGIC: D RTR^LA7HDR("MI;") will only send to HDR results

> associated with Laboratory "MI" subscript.

> ROUTING LOGIC: D RTR^LA7HDR("CH;MI;SP;") will only send to HDR results

> associated with Laboratory "CH", "MI", and "SP" subscripts.

TIMESTAMP: 59056,40125 RECEIVING APPLICATION: LA7HDR

EVENT TYPE: R01 LOGICAL LINK: VDEFVIE4

RESPONSE MESSAGE TYPE: ACK SENDING FACILITY REQUIRED?: YES

RECEIVING FACILITY REQUIRED?: YES ROUTING LOGIC: D RTR^LA7HDR("CH;")

> **NOTE:** This subscriber protocol is distributed with the Routing Logic disabled. See post-installation instructions for guidance to enable the protocol.

2.  The LA7 HDR Recover option is added to the OPTION file (#19).

NAME: LA7 HDR RECOVER MENU TEXT: Recover/Transmit Lab

HDR Result Messages

TYPE: run routine CREATOR:LDSICREATOR,ONE  
PACKAGE: AUTOMATED LAB INSTRUMENTS

DESCRIPTION: Option to recover from failed Lab HDR ORU Result message generation and/or transmission failure. This option allows the user to select those VistA Laboratory accessions that need to be transmitted to the VA HDR and other subscribers of the VistA Laboratory Result Available HL7 message capability via the protocol Lab Results Available Event \[LA7 LAB RESULTS AVAILABLE (EVN)\].

If the original message generation/transmission failed due to system or communication problems then using this option will allow the generation of new HL7 messages with the results associated with the selected accessions. Accessions can be selected using the human-readable accession designation (area abbreviation modified date accession number - "CH 1225 100") or the accession's associated 10 character unique identifier (UID)

ROUTINE: RECOVER^LA7HDR

UPPERCASE MENU TEXT: RECOVER/TRANSMIT LAB HDR RESUL

This option is assigned to the Lab liaison menu option \[LRLIAISON\] and can be assigned as needed to support/monitor message transmsission to the VA HDR and other subscribers.

## Enhancements/Modifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  When the configuration LA7HDR in LA7 MESSAGE PARAMETER file (#62.48) has an active status, the LA7HDR routine queues the record for transmission to the HDR via a HL7 ORU result message, which is transmitted by the HL package to any subscribers of event protocol, LA7 LAB RESULTS AVAILABLE (EVN), as well as to the HDR subscriber, LA7 LAB RESULTS TO HDR (SUB).

    The LA7 LAB RESULTS TO HDR (SUB) subscriber protocol uses the logical link VDEFVIE4. This is a router subscriber protocol that determines which Lab HL7 ORU messages are sent to the HDR.
3.  Anatomic Pathology is not *CPRS-aware* and is unable to notify CPRS of release of anatomic pathology results. HDR is notified of availability of anatomic pathology results via three new style cross-references in LAB DATA file (#63). When this capability is enabled, these indices also trigger generation of a Lab HL7 ORU message.
1.  Subfile \#63.02 – new style indices

AC (#98) FIELD MUMPS ACTION

Short Descr: Notify HDR and others that this report is available.

Description: This MUMPS cross-reference triggers the sending of this

report to the Health Data Repository (HDR) and other

subscribers when electron microscopy results are released.

Set Logic: D APQ^LA7HDR(DA(1),"EM",DA)

Kill Logic: Q

X(1): REPORT RELEASE DATE (63.02,.11) (Subscr 1) (forwards)

1.  Subfile \#63.08 – new style indices

AD (#95) FIELD MUMPS ACTION

Short Descr: Notify HDR and others that this report is available.

Description: This MUMPS cross-reference triggers the sending of this

report to the Health Data Repository (HDR) and other

subscribers when surgical pathology results are released.

Set Logic: D APQ^LA7HDR(DA(1),"SP",DA)

Kill Logic: Q

X(1): REPORT RELEASE DATE/TIME (63.08,.11) (Subscr 1)

(forwards)

2.  Subfile \#63.09 – new style indices

AD (#96) FIELD MUMPS ACTION

Short Descr: Notify HDR and others that this report is available.

Description: This MUMPS cross-reference triggers the sending of this

report to the Health Data Repository (HDR) and other

subscribers when cytopathology results are released.

Set Logic: D APQ^LA7HDR(DA(1),"CY",DA)

Kill Logic: Q

X(1): REPORT RELEASE DATE/TIME (63.09,.11) (Subscr 1)

(forwards)

4.  The current Laboratory package does not support LOINC encoding of microbiology results. A default encoding is enabled for LOINC encode of standard microbiology tests and antibiotics. LOINC codes valid as of version 2.14.

> There is default mapping of NLT/LOINC codes to standard fields within the MICROBIOLOGY file (#5) multiple of LAB DATA file (#63) .

Test Order NLT Result NLT LOINC Code

Bacteriology report (#11) 87993.0000

Gram stain (#11.6) 87993.0000 87754.0000 664-3

Bacteriology organism (#12) 87993.0000 87570.0000 11475-1

Bacteria colony count (#12,1) 87719.0000 564-5

Parasite report (#14) 87505.0000

Parasite organism (#16) 87505.0000 87576.0000 17784-0

Mycology report (#18) 87994.0000

Fungal organism (#20) 87994.0000 87578.0000 580-1

Fungal colony count (#20,1) 87994.0000 87723.0000 19101-5

Mycobacterium report (#22) 87995.0000

Acid Fast stain (#24) 87995.0000 87756.0000 11545-1

Acid Fast stain quantity (#25) 87995.0000 87583.0000 11545-1

Mycobacterium organism (#26) 87995.0000 87589.0000 543-9

Mycobacterium colony count (#26,1) 87995.0000 87719.0000 564-5

Virology report (#33) 87996.0000

Viral agent (#36) 87996.0000 87590.0000 6584-7

> Bacteriology or mycobacterium (TB) organism's susceptibilities are based on a local site's mapping of National VA Lab Code field (#64) in ANTIMICROBIAL SUSCEPTIBILITY file (#62.06) and the related default LOINC code associated with this VA NLT code.

> Use the Map/Unmap Antimicrobial Default LOINC Code \[LR LOINC MAP ANTIMICROBIAL\] option to configure the default LOINC code for each antibiotic.

5.  The current Laboratory package does not support LOINC encoding of surgical pathology results. LOINC codes valid as of version 2.14.

> There is default mapping of NLT/LOINC codes to standard fields within the SURGICAL PATHOLOGY (#8) multiple of LAB DATA file (#63).

Test Order NLT Result NLT LOINC Code

Specimen (#.012) 88515.0000 88539.0000 22633-2

Brief clinical history (#.013) 88515.0000 88542.0000 22636-5

Preoperative diagnosis (#.014) 88515.0000 88544.0000 10219-4

Operative findings (#.015) 88515.0000 88546.0000 10215-2

Postoperative diagnosis (#.016) 88515.0000 88547.0000 10218-6

Gross description (#1) 88515.0000 88549.0000 22634-0

Microscopic description (#1.1) 88515.0000 88563.0000 22635-7

Frozen section (#1.3) 88515.0000 88569.0000 22635-7

Surgical path diagnosis (#1.4) 88515.0000 88571.0000 22637-3

Supplementary report (#1.2) 88515.0000 88589.0000 22639-9

Specimen weight (#2) 88515.0000 81233.0000 3154-2

6.  The current Laboratory package does not support LOINC encoding of cytopathology results. LOINC codes valid as of version 2.14.

> There is default mapping of NLT/LOINC codes to standard fields within the CYTOPATHOLOGY (#9) multiple of LAB DATA file (#63).

Test Order NLT Result NLT LOINC Code

Specimens (#.012) 88593.0000 88539.0000 22633-2

Brief clinical history (#.013) 88593.0000 88542.0000 22636-5

Preoperative diagnosis (#.014) 88593.0000 88544.0000 10219-4

Operative findings (#.015) 88593.0000 88542.0000 10215-2

Postoperative diagnosis (#.016) 88593.0000 88547.0000 10218-6

Gross description (#1) 88593.0000 88549.0000 22634-0

Microscopic examination (#1.1) 88593.0000 88563.0000 22635-7

Supplementary report (#1.2) 88593.0000 88589.0000 22639-9

Cytopatholgy diagnosis (#1.4) 88593.0000 88571.0000 22637-3

7.  The current Laboratory package does not support LOINC encoding of electron microscopy.

> There is default mapping of NLT/LOINC codes to standard fields within the EM (#2) multiple of LAB DATA file (#63).

Test Order NLT Result NLT LOINC Code

Specimens (#.012) 88597.0000 88057.0000 22633-2

Brief clinical history (#.013) 88597.0000 88542.0000 22636-5

Preoperative diagnosis (#.014) 88597.0000 88544.0000 10219-4

Operative findings (#.015) 88597.0000 88542.0000 10215-2

Postoperative diagnosis (#.016) 88597.0000 88547.0000 10218-6

Gross description (#1) 88597.0000 88549.0000 22634-0

Microscopic examination (#1.1) 88597.0000 88563.0000 22635-7

Supplementary report (#1.2) 88597.0000 88589.0000 22639-9

EM diagnosis (#1.4) 88597.0000 88571.0000 22637-3

8.  This patch converts several FileMan DBS calls on INSTITUTION file (#4) to use the supported APIs, \$\$NS^XUAF4 and \$\$STA^XUAF4.
9.  To integrate the VistA-Office EHR with the regular VistA system, as well as add functionality available in the Indian Health Services system, the GQPR^LA7QRY API was modified to allow for VistA-Office EHR to use data geared specifically toward clinical operations, whether in a hospital or a stand alone clinic.
- The use of an Electronic Health Record number is supported as a patient identifier that the API accepts.
- The entry point, GCPR^LA7QRY, remains unchanged. However the parameter used to pass the patient identifier contains a second piece indicating the type of identifier contained in the first piece.
- This API supports three types of patient identifiers.
1.  SS= Social Security number
2.  PI = VA MPI Integration Control Number
3.  MR= medical record number of patient in file PATIENT/IHS (#9000001)

> **NOTE:** Regular VistA users will not see this modification.

10. To support HDR-Historical, which uses the GRPR^LA7QRY API to extract historical laboratory test results, the input parameter, LA7SC to GCPR^LA7QRY, supports a second piece. When the second piece of input parameter LA7SC equals 1, the API returns results encoded using VUIDs, when available.
11. This patch corrects a defect identified during patch development with processing input parameters for the GCPR^LA7QRY API. When the input parameter LA7SC identifies specific subscripts for which to search, the API searches those subscripts for any search code, even when specific search codes are passed to the API in the LA7SC array.
12. This patch corrects a defect identified during patch development with processing input parameters for the GCPR^LA7QRY API. When the input parameters, LA7SDT and LA7EDT, identify specific results for an available date range, the API returns anatomic pathology results that were not released. This API was corrected to check the Report Release Date field (#.11) for subscripts CY, EM, and SP.
13. This patch corrects a defect identified by MyHeatheVet, related to the encoding of four fields in the OBR segment for anatomic pathology reports.
1.  OBR-32 - Principal result interpreter
3.  OBR-33 - Assistant result interpreter
4.  OBR-34 – Technician
5.  OBR-35 - Transcriptionist

> The name component of these fields was encoded with the wrong HL7 delimiter (component separator). The name component is now encoded with the subcomponent separator per the HL7 standard.

## Enhancements/Remedy Tickets 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Remedy ticket HD0000000096207 reported a problem with the error code returned by the Lab API, LA7QRY. A FileMan DBS error code was erroroneously returned to the calling application.
- Routines, LA7QRY, LA7QRY1, and LA7QRY2 were modified to use a different namespaced variable,LA7QERR, to return to the calling application any error conditions.
- Routine LA7VOBX1 was modified to use another namespaced variable, LA7DDERR, to handle FileMan DBS error conditions related to FileMan data dictionary calls.
14. Remedy tickets HD0000000141922 and HD0000000148089 reported a problem: failure to generate the MailMan bulletin,LA7 ORDER STATUS CHANGED, at the *collection* laboratory facility.  
      
    Routine LA7VMSG1 was changed to set the interface type of the flag in the Lab HL7 ORU message indicating an order status change to trigger the generation of the bulletin at the collection site.
