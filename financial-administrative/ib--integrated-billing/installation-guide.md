---
title: Integrated Billing Version 2 Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: 
app_code: IB
app_name: Integrated Billing
section: FIN
app_status: active
pkg_ns: IB
patch_ver: 2
patch_id: IB*2
group_key: "IB:IB:2"
file_numbers: 
  - 350
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - filed
  - ibini
  - protocol
  - blockquote
  - table
  - contents
  - routine
  - ibdf
  - installation
  - billing
page_count: 0
word_count: 16387
section_count: 6
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 1994
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Integrated_Billing_(IB)/ib20ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Integrated_Billing_(IB)/ib20ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=45"
---

### Department of Veterans Affairs Decentralized Hospital Computer Program

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

INTEGRATED BILLING INSTALLATION GUIDE

> Version 2.0 March 1994

### Information Systems Center Albany, New York

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

    - [Department of Veterans Affairs Decentralized Hospital Computer Program](#department-of-veterans-affairs-decentralized-hospital-computer-program)
    - [Information Systems Center Albany, New York](#information-systems-center-albany-new-york)
- [Introduction](#introduction)
    - [This package includes one new global, IBT, that may need to be placed and translated prior to starting the install process. The IBT global is used for the Claims Tracking module, and its growth is dependent upon which options within Claims Tracking are activated. Our initial estimate is that 5 megabytes will be required per year, if Claims Tracking is fully activated. Please see the Technical Manual for additional resource requirements for the Claims Tracking module.](#this-package-includes-one-new-global-ibt-that-may-need-to-be-placed-and-translated-prior-to-starting-the-install-process-the-ibt-global-is-used-for-the-claims-tracking-module-and-its-growth-is-dependent-upon-which-options-within-claims-tracking-are-activated-our-initial-estimate-is-that-5-megabytes-will-be-required-per-year-if-claims-tracking-is-fully-activated-please-see-the-technical-manual-for-additional-resource-requirements-for-the-claims-tracking-module)
    - [Three jobs will be queued at the conclusion of the installation. These jobs will be queued to run 15 minutes after the installation is completed. When each of these queued jobs is completed, a MailMan message will be sent to the user who started the installation. Note: Users may be allowed back into the system while these jobs are running.](#three-jobs-will-be-queued-at-the-conclusion-of-the-installation-these-jobs-will-be-queued-to-run-15-minutes-after-the-installation-is-completed-when-each-of-these-queued-jobs-is-completed-a-mailman-message-will-be-sent-to-the-user-who-started-the-installation-note-users-may-be-allowed-back-into-the-system-while-these-jobs-are-running)
    - [The three queued jobs are as follows.](#the-three-queued-jobs-are-as-follows)
    - [All current inpatients with insurance are loaded into the Claims Tracking module.](#all-current-inpatients-with-insurance-are-loaded-into-the-claims-tracking-module)
    - [Insurance policy information from the PATIENT file (#2) is moved into the new GROUP INSURANCE PLAN file (#355.3).](#insurance-policy-information-from-the-patient-file-2-is-moved-into-the-new-group-insurance-plan-file-3553)
    - [Note: This conversion will populate the "1" and "2" nodes of the INSURANCE TYPE subfile (#.3121) of the PATIENT file (#2) (the nodes](#note-this-conversion-will-populate-the-1-and-2-nodes-of-the-insurance-type-subfile-3121-of-the-patient-file-2-the-nodes)
    - [^DPT(DFN,.312,ien,1) and ^DPT(DFN,.312,ien,2) ). If you have any local modifications which store data on these nodes, you must first delete this data before installing Integrated Billing v2.0. Existence of any data on the "1" or "2" nodes will cause this conversion to fail.](#dptdfn312ien1-and-dptdfn312ien2-if-you-have-any-local-modifications-which-store-data-on-these-nodes-you-must-first-delete-this-data-before-installing-integrated-billing-v20-existence-of-any-data-on-the-1-or-2-nodes-will-cause-this-conversion-to-fail)
    - [Diagnoses for all entries in the BILL/CLAIMS file (#399) are moved into the new IB BILL/CLAIMS DIAGNOSIS file (#362.3).](#diagnoses-for-all-entries-in-the-billclaims-file-399-are-moved-into-the-new-ib-billclaims-diagnosis-file-3623)
    - [You will be required to answer one question in the pre-init before committing to the installation of Integrated Billing v2.0. You will be asked if you would like to turn on automatic billing for inpatient billing. The purpose for deciding to run the inpatient biller at the time of installation is to properly set up the Third Party Auto Biller to run for the current inpatients who are loaded into the Claims Tracking module in the job that is queued from the post-init.](#you-will-be-required-to-answer-one-question-in-the-pre-init-before-committing-to-the-installation-of-integrated-billing-v20-you-will-be-asked-if-you-would-like-to-turn-on-automatic-billing-for-inpatient-billing-the-purpose-for-deciding-to-run-the-inpatient-biller-at-the-time-of-installation-is-to-properly-set-up-the-third-party-auto-biller-to-run-for-the-current-inpatients-who-are-loaded-into-the-claims-tracking-module-in-the-job-that-is-queued-from-the-post-init)
    - [If automatic billing for inpatients is selected, the following parameters will be established during the post-init.](#if-automatic-billing-for-inpatients-is-selected-the-following-parameters-will-be-established-during-the-post-init)
    - [Auto Biller Frequency: 7 days](#auto-biller-frequency-7-days)
    - [The Auto Biller will not run until 7 days after the installation.](#the-auto-biller-will-not-run-until-7-days-after-the-installation)
    - [Automate Billing: Yes](#automate-billing-yes)
    - [The Earliest Auto Bill Date will be set during the conversion for current inpatients who are loaded into the Claims Tracking module.](#the-earliest-auto-bill-date-will-be-set-during-the-conversion-for-current-inpatients-who-are-loaded-into-the-claims-tracking-module)
    - [Billing Cycle: This will be left blank. The billing cycle will be one month.](#billing-cycle-this-will-be-left-blank-the-billing-cycle-will-be-one-month)
    - [Days Delay: 2 days](#days-delay-2-days)
    - [This is the number of days after the billing cycle is completed that the bill will be created.](#this-is-the-number-of-days-after-the-billing-cycle-is-completed-that-the-bill-will-be-created)
    - [Please note that there is a 15-minute window (from the time the init is completed to the time that the Claims Tracking job begins) to change these parameters. Also, these parameters may be altered at any time using the option IB AUTO BILLER PARAMS.](#please-note-that-there-is-a-15-minute-window-from-the-time-the-init-is-completed-to-the-time-that-the-claims-tracking-job-begins-to-change-these-parameters-also-these-parameters-may-be-altered-at-any-time-using-the-option-ib-auto-biller-params)
- [Package Integration](#package-integration)
    - [This package contains two inits.](#this-package-contains-two-inits)
    - [The init IBINIT was created with Kernel v7.1 and VA FileMan v20.0. It contains all the necessary options, protocols, functions, mail groups, templates, files, fields, and data needed to install and run Integrated Billing v2.0.](#the-init-ibinit-was-created-with-kernel-v71-and-va-fileman-v200-it-contains-all-the-necessary-options-protocols-functions-mail-groups-templates-files-fields-and-data-needed-to-install-and-run-integrated-billing-v20)
    - [The init IBDEINIT contains sample encounter forms which you may install at your facility. This init must be installed using the Encounter Form Import/ Export Utility. Instructions for installing this init may be found in the Encounter Form Utilities Module of the User Manual, Import/Export Utility option.](#the-init-ibdeinit-contains-sample-encounter-forms-which-you-may-install-at-your-facility-this-init-must-be-installed-using-the-encounter-form-import-export-utility-instructions-for-installing-this-init-may-be-found-in-the-encounter-form-utilities-module-of-the-user-manual-importexport-utility-option)
    - [IB requires the following packages be installed. Accounts Receivable v3.7](#ib-requires-the-following-packages-be-installed-accounts-receivable-v37)
    - [IFCAP v4.0 OERR v1.96](#ifcap-v40-oerr-v196)
    - [Outpatient Pharmacy v5.6](#outpatient-pharmacy-v56)
    - [Kernel v7.1 and VA FileMan v20.0](#kernel-v71-and-va-fileman-v200)
    - [This package was created with Kernel v7.1 and VA FileMan v20.0. The IBNTEG routine was created using Kernel Tool Kit v7.2 XTSUMBLD utility.](#this-package-was-created-with-kernel-v71-and-va-fileman-v200-the-ibnteg-routine-was-created-using-kernel-tool-kit-v72-xtsumbld-utility)
    - [PIMS v5.3](#pims-v53)
    - [The Scheduling patch SD\5.3\13 also has to be installed. The Registration informational patch DG\5.3\26 describes all changes to PIMS which are needed to run Integrated Billing v2.0. The IBINIT post-init conditionally installs the PIMS routines which are part of this patch.](#the-scheduling-patch-sd5313-also-has-to-be-installed-the-registration-informational-patch-dg5326-describes-all-changes-to-pims-which-are-needed-to-run-integrated-billing-v20-the-ibinit-post-init-conditionally-installs-the-pims-routines-which-are-part-of-this-patch)
- [Pre-Installation Checklist](#pre-installation-checklist)
    - [Have you loaded this package into your test account?](#have-you-loaded-this-package-into-your-test-account)
    - [This package checks to be sure that PIMS v5.3 and Accounts Receivable v3.7 is installed. Please be sure that you have these packages installed.](#this-package-checks-to-be-sure-that-pims-v53-and-accounts-receivable-v37-is-installed-please-be-sure-that-you-have-these-packages-installed)
    - [Have you installed patch SD\5.3\13?](#have-you-installed-patch-sd5313)
    - [Did you place the new global IBT?](#did-you-place-the-new-global-ibt)
    - [Are protections and translation set up correctly for this new global?](#are-protections-and-translation-set-up-correctly-for-this-new-global)
    - [Do you have any tasked jobs or other systems processes that need to be s hut down or rescheduled?](#do-you-have-any-tasked-jobs-or-other-systems-processes-that-need-to-be-s-hut-down-or-rescheduled)
    - [Have you scheduled down-time with the users? You should schedule approximately 2-4 hours of down time to install this package. Note that you may bring users back on-line after the installation has completed and the queued jobs are running.](#have-you-scheduled-down-time-with-the-users-you-should-schedule-approximately-2-4-hours-of-down-time-to-install-this-package-note-that-you-may-bring-users-back-on-line-after-the-installation-has-completed-and-the-queued-jobs-are-running)
    - [Have you scheduled an unattended backup prior to beginning the installation?](#have-you-scheduled-an-unattended-backup-prior-to-beginning-the-installation)
    - [Did you review global journaling and your routine map sets prior to starting the installation?](#did-you-review-global-journaling-and-your-routine-map-sets-prior-to-starting-the-installation)
    - [Have you read the complete installation instructions?](#have-you-read-the-complete-installation-instructions)
    - [Have you coordinated the installation with the respective services in your facility? These services may include MAS, MCCR, Fiscal, Utilization Review, Fee Basis, and Quality Management.](#have-you-coordinated-the-installation-with-the-respective-services-in-your-facility-these-services-may-include-mas-mccr-fiscal-utilization-review-fee-basis-and-quality-management)
    - [Have you reviewed which users are going to get the new Claims Tracking, Encounter Form Utilities, and Insurance Data Capture menus and options, including any local menus?](#have-you-reviewed-which-users-are-going-to-get-the-new-claims-tracking-encounter-form-utilities-and-insurance-data-capture-menus-and-options-including-any-local-menus)
    - [Have you made sure that you have no data stored on the "1" or "2" nodes of the INSURANCE TYPE (#.3121) subfile of the PATIENT (#2) file (the nodes](#have-you-made-sure-that-you-have-no-data-stored-on-the-1-or-2-nodes-of-the-insurance-type-3121-subfile-of-the-patient-2-file-the-nodes)
    - [^DPT(DFN,.312,ien,1) and ^DPT(DFN,.312,ien,2) )?](#dptdfn312ien1-and-dptdfn312ien2)
- [Installation Instructions](#installation-instructions)
  - [Step Description](#step-description)
    - [Get users off system(s).](#get-users-off-systems)
    - [Backup system(s).](#backup-systems)
    - [Disable Routine Mapping (DSM) on all systems.](#disable-routine-mapping-dsm-on-all-systems)
    - [Disable journaling. The globals IB, IBE, IBA, IBT, DPT, and DGCR will be very active during the installation and subsequent conversions.](#disable-journaling-the-globals-ib-ibe-iba-ibt-dpt-and-dgcr-will-be-very-active-during-the-installation-and-subsequent-conversions)
    - [Sign into the UCI where the package is to be loaded.](#sign-into-the-uci-where-the-package-is-to-be-loaded)
    - [Note: It is suggested that MSM sites run the install on the Print Server. (Use 16K partition for DSM. Use 40K partition for MSM.)](#note-it-is-suggested-that-msm-sites-run-the-install-on-the-print-server-use-16k-partition-for-dsm-use-40k-partition-for-msm)
    - [You should install patch SD\5.3\13 if you have not already done so.](#you-should-install-patch-sd5313-if-you-have-not-already-done-so)
    - [The tape contains routines in the DGCR and IB namespaces. Mount the tape and load the routines. See the Routine List section for a list of the distributed routines.](#the-tape-contains-routines-in-the-dgcr-and-ib-namespaces-mount-the-tape-and-load-the-routines-see-the-routine-list-section-for-a-list-of-the-distributed-routines)
    - [Verify that DUZ, DT, DTIME, and U are defined and that DUZ(0)="@". The DUZ variable must be defined as an active user and the DUZ(0) variable must equal "@" in order to initialize.](#verify-that-duz-dt-dtime-and-u-are-defined-and-that-duz0-the-duz-variable-must-be-defined-as-an-active-user-and-the-duz0-variable-must-equal-in-order-to-initialize)
    - [This package will create the new global IBT. This global should grow steadily, depending upon which options within the Claims Tracking module have been activated. When the conversions routines are run, there will be considerable growth of the global IBA.](#this-package-will-create-the-new-global-ibt-this-global-should-grow-steadily-depending-upon-which-options-within-the-claims-tracking-module-have-been-activated-when-the-conversions-routines-are-run-there-will-be-considerable-growth-of-the-global-iba)
    - [D ^IBINIT to begin the installation. Follow the sample installation in this guide.](#d-ibinit-to-begin-the-installation-follow-the-sample-installation-in-this-guide)
    - [The pre-initialization routine will check the current environment. You must also indicate whether you wish to have the post-init routine set the inpatient Auto Biller parameters.](#the-pre-initialization-routine-will-check-the-current-environment-you-must-also-indicate-whether-you-wish-to-have-the-post-init-routine-set-the-inpatient-auto-biller-parameters)
    - [When the package files are displayed, answer "NO" to all "add data" questions, as shown in the sample installation. Answer "YES" to the "Shall I write over File Security Code?" question, as shown in the sample installation.](#when-the-package-files-are-displayed-answer-no-to-all-add-data-questions-as-shown-in-the-sample-installation-answer-yes-to-the-shall-i-write-over-file-security-code-question-as-shown-in-the-sample-installation)
  - [Step Description](#step-description-1)
    - [The initialization routine will accomplish the following.](#the-initialization-routine-will-accomplish-the-following)
    - [Delete the IB ERROR file (#350.8), which will be recreated during the init.](#delete-the-ib-error-file-3508-which-will-be-recreated-during-the-init)
    - [Delete various obsolete input templates, print templates, cross- references, list templates, and protocols.](#delete-various-obsolete-input-templates-print-templates-cross-references-list-templates-and-protocols)
    - [The post-initialization routine will accomplish the following.](#the-post-initialization-routine-will-accomplish-the-following)
    - [Populate the new IB ACTION STATUS file (#350.21).](#populate-the-new-ib-action-status-file-35021)
    - [Update the print routine for the HCFA 1500 entry in the BILL FORM TYPE file (#353) and add a new entry to this file.](#update-the-print-routine-for-the-hcfa-1500-entry-in-the-bill-form-type-file-353-and-add-a-new-entry-to-this-file)
    - [Update the inpatient Auto Biller parameters, if specified in the pre- initialization process.](#update-the-inpatient-auto-biller-parameters-if-specified-in-the-pre-initialization-process)
    - [Flag all new telephone stop codes which were added with the Scheduling patch SD\5.3\13.](#flag-all-new-telephone-stop-codes-which-were-added-with-the-scheduling-patch-sd5313)
    - [Review all charges "on hold" in the INTEGRATED BILLING ACTIO N file (#350) and change the status of the charge if the charge has been cancelled.](#review-all-charges-on-hold-in-the-integrated-billing-actio-n-file-350-and-change-the-status-of-the-charge-if-the-charge-has-been-cancelled)
    - [Install all required protocols and list templates.](#install-all-required-protocols-and-list-templates)
    - [Add an entry in the PACKAGE file (#9.4) for the Encounter Form Import/Export Utility (namespace IBDE).](#add-an-entry-in-the-package-file-94-for-the-encounter-form-importexport-utility-namespace-ibde)
    - [Add new entries to the following files.](#add-new-entries-to-the-following-files)
    - [MCCR UTILITY (#399.1)](#mccr-utility-3991)
    - [REVENUE CODE (#399.2)](#revenue-code-3992)
    - [RATE TYPE (#399.3)](#rate-type-3993)
    - [IB CHARGE REMOVE REASONS (#350.3)](#ib-charge-remove-reasons-3503)
    - [Remove the option IB UB-82 TEST PATTERN PRINT from the menu IB OUTPUT PATIENT REPORT MENU.](#remove-the-option-ib-ub-82-test-pattern-print-from-the-menu-ib-output-patient-report-menu)
    - [Remove the option IB NEW FEATURES 1.5 from all menus.](#remove-the-option-ib-new-features-15-from-all-menus)
  - [Step Description](#step-description-2)
    - [Install the following PIMS and Fee Basis routines in your system. Make sure these routines are moved to all systems, if necessary.](#install-the-following-pims-and-fee-basis-routines-in-your-system-make-sure-these-routines-are-moved-to-all-systems-if-necessary)
    - [Queue three conversion jobs to run, starting 15 minutes from the present time.](#queue-three-conversion-jobs-to-run-starting-15-minutes-from-the-present-time)
    - [Recompile all templates and cross-references. Type D ALL^IBEFUTL1 to recompile all input, print, and cross-reference routines on all CPUs. The following is a list of the templates that should be compiled.](#recompile-all-templates-and-cross-references-type-d-allibefutl1-to-recompile-all-input-print-and-cross-reference-routines-on-all-cpus-the-following-is-a-list-of-the-templates-that-should-be-compiled)
    - [Note: If you move compiled routines, you may move IBX\ for all Integrated Billing compiled routines.](#note-if-you-move-compiled-routines-you-may-move-ibx-for-all-integrated-billing-compiled-routines)
    - [\>\>\> Remember to recompile the following templates on all CPUs.](#remember-to-recompile-the-following-templates-on-all-cpus)
  - [Step Description](#step-description-3)
    - [\>\>\> Remember to recompile the following cross references for the following files on all CPUs.](#remember-to-recompile-the-following-cross-references-for-the-following-files-on-all-cpus)
    - [Move routines to all systems. It is recommended that the globals DGCR, IB, IBA, IBE, and IBT be journaled.](#move-routines-to-all-systems-it-is-recommended-that-the-globals-dgcr-ib-iba-ibe-and-ibt-be-journaled)
    - [Rebuild routine map sets.](#rebuild-routine-map-sets)
    - [It is strongly recommended that the following routines be added to the routine map set on the volume set that they will be primarily running on.](#it-is-strongly-recommended-that-the-following-routines-be-added-to-the-routine-map-set-on-the-volume-set-that-they-will-be-primarily-running-on)
    - [IBA\ IBC\ IBEF\ IBR\ IBT\ IBX\](#iba-ibc-ibef-ibr-ibt-ibx)
    - [You may wish to bring users on-line at this point.](#you-may-wish-to-bring-users-on-line-at-this-point)
    - [You may now delete obsolete routines from your system.](#you-may-now-delete-obsolete-routines-from-your-system)
    - [The IB routines IBACKIN, IBEP, IBEHCFA, IBEHCF1, IBOHCTP,](#the-ib-routines-ibackin-ibep-ibehcfa-ibehcf1-ibohctp)
    - [IBOHCP, IB15\, and IBY\ are obsolete and may be deleted from your system.](#ibohcp-ib15-and-iby-are-obsolete-and-may-be-deleted-from-your-system)
    - [The only active DGCR routines with Integrated Billing v2.0 are DGCRNS, DGCRAMS, and DGCRP3. All other DGCR routines are obsolete and may be deleted from your system.](#the-only-active-dgcr-routines-with-integrated-billing-v20-are-dgcrns-dgcrams-and-dgcrp3-all-other-dgcr-routines-are-obsolete-and-may-be-deleted-from-your-system)
    - [You may now use the Encounter Form Import/Export Utility to import the sample encounter forms exported with this package. It is not necessary to perform this step at this point, but it must be performed before you begin active design and development of forms for your facility. Instructions for importing the forms may be found in the Encounter Form Utilities Module of the User Manual, Import/Export Utility option. Once you have imported these sample forms, you may delete the IBDEI\ routines from your system. This will delete the initialization routines for the Encounter Form Import/Export Utility package (namespace IBDE).](#you-may-now-use-the-encounter-form-importexport-utility-to-import-the-sample-encounter-forms-exported-with-this-package-it-is-not-necessary-to-perform-this-step-at-this-point-but-it-must-be-performed-before-you-begin-active-design-and-development-of-forms-for-your-facility-instructions-for-importing-the-forms-may-be-found-in-the-encounter-form-utilities-module-of-the-user-manual-importexport-utility-option-once-you-have-imported-these-sample-forms-you-may-delete-the-ibdei-routines-from-your-system-this-will-delete-the-initialization-routines-for-the-encounter-form-importexport-utility-package-namespace-ibde)
  - [Step Description](#step-description-4)
    - [You will be notified by a MailMan message when each of the queued conversion jobs have completed. Once the final conversion has completed, you may delete the IBI\, IBONI\, and IB20\ routines from your system. This will delete the initialization, pre-init, and post-init routines from your system.](#you-will-be-notified-by-a-mailman-message-when-each-of-the-queued-conversion-jobs-have-completed-once-the-final-conversion-has-completed-you-may-delete-the-ibi-iboni-and-ib20-routines-from-your-system-this-will-delete-the-initialization-pre-init-and-post-init-routines-from-your-system)
    - [Run the Build Primary Menu Trees option on the Menu Management menu on all systems. Though this step is optional, it may greatly improve performance during the first few days of operation.](#run-the-build-primary-menu-trees-option-on-the-menu-management-menu-on-all-systems-though-this-step-is-optional-it-may-greatly-improve-performance-during-the-first-few-days-of-operation)
    - [Review the entry in the IB SITE PARAMETERS file (#350.9) and ensure that all parameters are set correctly.](#review-the-entry-in-the-ib-site-parameters-file-3509-and-ensure-that-all-parameters-are-set-correctly)
    - [Ensure that the option IB MT NIGHT COMP is tasked to run early each morning (after the G&L has been completed, but before normal working hours). This job now includes updates performed by the Claims Tracking and Automated Biller modules. Be sure that this option is not tasked twice to run on your system! This will have adverse effects on the Means Test Billing module.](#ensure-that-the-option-ib-mt-night-comp-is-tasked-to-run-early-each-morning-after-the-gl-has-been-completed-but-before-normal-working-hours-this-job-now-includes-updates-performed-by-the-claims-tracking-and-automated-biller-modules-be-sure-that-this-option-is-not-tasked-twice-to-run-on-your-system-this-will-have-adverse-effects-on-the-means-test-billing-module)
- [Routine List](#routine-list)
- [Sample Installation](#sample-installation)
- [Resource Requirements](#resource-requirements)
    - [The installation of Integrated Billing v2.0 may require approximately 5-15 megabytes of additional disk capacity. This includes up to 2.5 megabytes in the global DPT, up to 2.5 megabytes in the global DGCR, up to 5 megabytes in the global IBA, and up to 5 megabytes in the new global IBT. 4 megabytes of disk capacity will be needed to load all of the routines exported with this package.](#the-installation-of-integrated-billing-v20-may-require-approximately-5-15-megabytes-of-additional-disk-capacity-this-includes-up-to-25-megabytes-in-the-global-dpt-up-to-25-megabytes-in-the-global-dgcr-up-to-5-megabytes-in-the-global-iba-and-up-to-5-megabytes-in-the-new-global-ibt-4-megabytes-of-disk-capacity-will-be-needed-to-load-all-of-the-routines-exported-with-this-package)
    - [The Encounter Form Utilities require a small amount of additional capacity to edit and store the format of the encounter forms. Please note that the standard partition size has been increased to 40K. You will need to increase your partition size to the new standard in order to run the utilities. The printing of encounter forms will require at least one dedicated printer that most sites have already received. The printing will require additional CPU capacity; however, this job may be scheduled during non-peak workload hours.](#the-encounter-form-utilities-require-a-small-amount-of-additional-capacity-to-edit-and-store-the-format-of-the-encounter-forms-please-note-that-the-standard-partition-size-has-been-increased-to-40k-you-will-need-to-increase-your-partition-size-to-the-new-standard-in-order-to-run-the-utilities-the-printing-of-encounter-forms-will-require-at-least-one-dedicated-printer-that-most-sites-have-already-received-the-printing-will-require-additional-cpu-capacity-however-this-job-may-be-scheduled-during-non-peak-workload-hours)
    - [The Insurance Data Capture module has been highly used during testing. This module will increase disk utilization in the DPT global by approximately 1K per every 10 insurance policies and in the IBA global by 1K per every three insurance policies.](#the-insurance-data-capture-module-has-been-highly-used-during-testing-this-module-will-increase-disk-utilization-in-the-dpt-global-by-approximately-1k-per-every-10-insurance-policies-and-in-the-iba-global-by-1k-per-every-three-insurance-policies)
    - [Based on the experience of our test sites, the Claims Tracking module will use approximately 5K of disk space for every pre-admission entry (one for every insurance case plus 5 per week for UR). In addition, approximately 1K of disk space for every 3 outpatient visits or prescription refills will be used.](#based-on-the-experience-of-our-test-sites-the-claims-tracking-module-will-use-approximately-5k-of-disk-space-for-every-pre-admission-entry-one-for-every-insurance-case-plus-5-per-week-for-ur-in-addition-approximately-1k-of-disk-space-for-every-3-outpatient-visits-or-prescription-refills-will-be-used)

### This package includes one new global, IBT, that may need to be placed and translated prior to starting the install process. The IBT global is used for the Claims Tracking module, and its growth is dependent upon which options within Claims Tracking are activated. Our initial estimate is that 5 megabytes will be required per year, if Claims Tracking is fully activated. Please see the Technical Manual for additional resource requirements for the Claims Tracking module.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Three jobs will be queued at the conclusion of the installation. These jobs will be queued to run 15 minutes after the installation is completed. When each of these queued jobs is completed, a MailMan message will be sent to the user who started the installation. Note: Users may be allowed back into the system while these jobs are running.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### The three queued jobs are as follows.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### All current inpatients with insurance are loaded into the Claims Tracking module.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Insurance policy information from the PATIENT file (#2) is moved into the new GROUP INSURANCE PLAN file (#355.3).

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Note: This conversion will populate the "1" and "2" nodes of the INSURANCE TYPE subfile (#.3121) of the PATIENT file (#2) (the nodes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### ^DPT(DFN,.312,ien,1) and ^DPT(DFN,.312,ien,2) ). If you have any local modifications which store data on these nodes, you must first delete this data before installing Integrated Billing v2.0. Existence of any data on the "1" or "2" nodes will cause this conversion to fail.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Diagnoses for all entries in the BILL/CLAIMS file (#399) are moved into the new IB BILL/CLAIMS DIAGNOSIS file (#362.3).

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### You will be required to answer one question in the pre-init before committing to the installation of Integrated Billing v2.0. You will be asked if you would like to turn on automatic billing for inpatient billing. The purpose for deciding to run the inpatient biller at the time of installation is to properly set up the Third Party Auto Biller to run for the current inpatients who are loaded into the Claims Tracking module in the job that is queued from the post-init.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Introduction

### If automatic billing for inpatients is selected, the following parameters will be established during the post-init.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Auto Biller Frequency: 7 days

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### The Auto Biller will not run until 7 days after the installation.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Automate Billing: Yes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### The Earliest Auto Bill Date will be set during the conversion for current inpatients who are loaded into the Claims Tracking module.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Billing Cycle: This will be left blank. The billing cycle will be one month.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Days Delay: 2 days

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### This is the number of days after the billing cycle is completed that the bill will be created.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Please note that there is a 15-minute window (from the time the init is completed to the time that the Claims Tracking job begins) to change these parameters. Also, these parameters may be altered at any time using the option IB AUTO BILLER PARAMS.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Package Integration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### This package contains two inits.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### The init IBINIT was created with Kernel v7.1 and VA FileMan v20.0. It contains all the necessary options, protocols, functions, mail groups, templates, files, fields, and data needed to install and run Integrated Billing v2.0.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### The init IBDEINIT contains sample encounter forms which you may install at your facility. This init must be installed using the Encounter Form Import/ Export Utility. Instructions for installing this init may be found in the Encounter Form Utilities Module of the User Manual, Import/Export Utility option.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### IB requires the following packages be installed. Accounts Receivable v3.7

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### IFCAP v4.0 OERR v1.96

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Outpatient Pharmacy v5.6

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Kernel v7.1 and VA FileMan v20.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### This package was created with Kernel v7.1 and VA FileMan v20.0. The IBNTEG routine was created using Kernel Tool Kit v7.2 XTSUMBLD utility.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### PIMS v5.3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### The Scheduling patch SD\*5.3\*13 also has to be installed. The Registration informational patch DG\*5.3\*26 describes all changes to PIMS which are needed to run Integrated Billing v2.0. The IBINIT post-init conditionally installs the PIMS routines which are part of this patch.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Package Integration

# Pre-Installation Checklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Have you loaded this package into your test account?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### This package checks to be sure that PIMS v5.3 and Accounts Receivable v3.7 is installed. Please be sure that you have these packages installed.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Have you installed patch SD\*5.3\*13?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Did you place the new global IBT?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Are protections and translation set up correctly for this new global?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Do you have any tasked jobs or other systems processes that need to be s hut down or rescheduled?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Have you scheduled down-time with the users? You should schedule approximately 2-4 hours of down time to install this package. Note that you may bring users back on-line after the installation has completed and the queued jobs are running.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Have you scheduled an unattended backup prior to beginning the installation?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Did you review global journaling and your routine map sets prior to starting the installation?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Have you read the complete installation instructions?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Have you coordinated the installation with the respective services in your facility? These services may include MAS, MCCR, Fiscal, Utilization Review, Fee Basis, and Quality Management.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Have you reviewed which users are going to get the new Claims Tracking, Encounter Form Utilities, and Insurance Data Capture menus and options, including any local menus?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Have you made sure that you have no data stored on the "1" or "2" nodes of the INSURANCE TYPE (#.3121) subfile of the PATIENT (#2) file (the nodes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### ^DPT(DFN,.312,ien,1) and ^DPT(DFN,.312,ien,2) )?

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Pre-Installation Checklist

# Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Step Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Get users off system(s).

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Backup system(s).

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Disable Routine Mapping (DSM) on all systems.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Disable journaling. The globals IB, IBE, IBA, IBT, DPT, and DGCR will be very active during the installation and subsequent conversions.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Sign into the UCI where the package is to be loaded.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Note: It is suggested that MSM sites run the install on the Print Server. (Use 16K partition for DSM. Use 40K partition for MSM.)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### You should install patch SD\*5.3\*13 if you have not already done so.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### The tape contains routines in the DGCR and IB namespaces. Mount the tape and load the routines. See the Routine List section for a list of the distributed routines.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Verify that DUZ, DT, DTIME, and U are defined and that DUZ(0)="@". The DUZ variable must be defined as an active user and the DUZ(0) variable must equal "@" in order to initialize.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### This package will create the new global IBT. This global should grow steadily, depending upon which options within the Claims Tracking module have been activated. When the conversions routines are run, there will be considerable growth of the global IBA.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### D ^IBINIT to begin the installation. Follow the sample installation in this guide.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### The pre-initialization routine will check the current environment. You must also indicate whether you wish to have the post-init routine set the inpatient Auto Biller parameters.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### When the package files are displayed, answer "NO" to all "add data" questions, as shown in the sample installation. Answer "YES" to the "Shall I write over File Security Code?" question, as shown in the sample installation.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation Instructions

## Step Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### The initialization routine will accomplish the following.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Delete the IB ERROR file (#350.8), which will be recreated during the init.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Delete various obsolete input templates, print templates, cross- references, list templates, and protocols.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### The post-initialization routine will accomplish the following.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Populate the new IB ACTION STATUS file (#350.21).

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Update the print routine for the HCFA 1500 entry in the BILL FORM TYPE file (#353) and add a new entry to this file.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Update the inpatient Auto Biller parameters, if specified in the pre- initialization process.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Flag all new telephone stop codes which were added with the Scheduling patch SD\*5.3\*13.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Review all charges "on hold" in the INTEGRATED BILLING ACTIO N file (#350) and change the status of the charge if the charge has been cancelled.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Install all required protocols and list templates.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Add an entry in the PACKAGE file (#9.4) for the Encounter Form Import/Export Utility (namespace IBDE).

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Add new entries to the following files.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### MCCR UTILITY (#399.1)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### REVENUE CODE (#399.2)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### RATE TYPE (#399.3)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### IB CHARGE REMOVE REASONS (#350.3)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Remove the option IB UB-82 TEST PATTERN PRINT from the menu IB OUTPUT PATIENT REPORT MENU.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Remove the option IB NEW FEATURES 1.5 from all menus.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation Instructions

## Step Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Install the following PIMS and Fee Basis routines in your system. Make sure these routines are moved to all systems, if necessary.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> DG3PR0 DG3PR1

> DG3PR2 DGBLRV

> DGPMVBUR DGPTF

> DGPTTS DGPTTS1

> DGPTTS3 DGRPDB

> DGPTUTL FBUINS

### Queue three conversion jobs to run, starting 15 minutes from the present time.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Recompile all templates and cross-references. Type D ALL^IBEFUTL1 to recompile all input, print, and cross-reference routines on all CPUs. The following is a list of the templates that should be compiled.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Note: If you move compiled routines, you may move IBX\* for all Integrated Billing compiled routines.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \>\>\> Remember to recompile the following templates on all CPUs.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 44%" />
<col style="width: 19%" />
<col style="width: 16%" />
<col style="width: 19%" />
</colgroup>
<thead>
<tr class="header">
<th>TEMPLATE</th>
<th><blockquote>
<p>ROUTINE</p>
</blockquote></th>
<th><blockquote>
<p>TYPE</p>
</blockquote></th>
<th><blockquote>
<p>ROUTINE</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>IB CURRENT STATUS</td>
<td><blockquote>
<p>IBXEXS</p>
</blockquote></td>
<td><blockquote>
<p>INPUT</p>
</blockquote></td>
<td><blockquote>
<p>DIEZ</p>
</blockquote></td>
</tr>
<tr class="even">
<td>IB EDIT MCCR PARM</td>
<td><blockquote>
<p>IBXPAR</p>
</blockquote></td>
<td><blockquote>
<p>INPUT</p>
</blockquote></td>
<td><blockquote>
<p>DIEZ</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>IB INACTIVATE EXEMPTION</td>
<td><blockquote>
<p>IBXEXI</p>
</blockquote></td>
<td><blockquote>
<p>INPUT</p>
</blockquote></td>
<td><blockquote>
<p>DIEZ</p>
</blockquote></td>
</tr>
<tr class="even">
<td>IB NEW EXEMPTION</td>
<td><blockquote>
<p>IBXEX</p>
</blockquote></td>
<td><blockquote>
<p>INPUT</p>
</blockquote></td>
<td><blockquote>
<p>DIEZ</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>IB SCREEN1</td>
<td><blockquote>
<p>IBXSC1</p>
</blockquote></td>
<td><blockquote>
<p>INPUT</p>
</blockquote></td>
<td><blockquote>
<p>DIEZ</p>
</blockquote></td>
</tr>
<tr class="even">
<td>IB SCREEN2</td>
<td><blockquote>
<p>IBXSC2</p>
</blockquote></td>
<td><blockquote>
<p>INPUT</p>
</blockquote></td>
<td><blockquote>
<p>DIEZ</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>IB SCREEN3</td>
<td><blockquote>
<p>IBXSC3</p>
</blockquote></td>
<td><blockquote>
<p>INPUT</p>
</blockquote></td>
<td><blockquote>
<p>DIEZ</p>
</blockquote></td>
</tr>
<tr class="even">
<td>IB SCREEN4</td>
<td><blockquote>
<p>IBXSC4</p>
</blockquote></td>
<td><blockquote>
<p>INPUT</p>
</blockquote></td>
<td><blockquote>
<p>DIEZ</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>IB SCREEN5</td>
<td><blockquote>
<p>IBXSC5</p>
</blockquote></td>
<td><blockquote>
<p>INPUT</p>
</blockquote></td>
<td><blockquote>
<p>DIEZ</p>
</blockquote></td>
</tr>
<tr class="even">
<td>IB SCREEN6</td>
<td><blockquote>
<p>IBXSC6</p>
</blockquote></td>
<td><blockquote>
<p>INPUT</p>
</blockquote></td>
<td><blockquote>
<p>DIEZ</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>IB SCREEN7</td>
<td><blockquote>
<p>IBXSC7</p>
</blockquote></td>
<td><blockquote>
<p>INPUT</p>
</blockquote></td>
<td><blockquote>
<p>DIEZ</p>
</blockquote></td>
</tr>
<tr class="even">
<td>IB SCREEN8</td>
<td><blockquote>
<p>IBXSC8</p>
</blockquote></td>
<td><blockquote>
<p>INPUT</p>
</blockquote></td>
<td><blockquote>
<p>DIEZ</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>IB SCREEN82</td>
<td><blockquote>
<p>IBXSC82</p>
</blockquote></td>
<td><blockquote>
<p>INPUT</p>
</blockquote></td>
<td><blockquote>
<p>DIEZ</p>
</blockquote></td>
</tr>
<tr class="even">
<td>IB SCREEN8H</td>
<td><blockquote>
<p>IBXSC8H</p>
</blockquote></td>
<td><blockquote>
<p>INPUT</p>
</blockquote></td>
<td><blockquote>
<p>DIEZ</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>IB STATUS</td>
<td><blockquote>
<p>IBXST</p>
</blockquote></td>
<td><blockquote>
<p>INPUT</p>
</blockquote></td>
<td><blockquote>
<p>DIEZ</p>
</blockquote></td>
</tr>
<tr class="even">
<td>IBDF EDIT DATA FIELD</td>
<td><blockquote>
<p>IBXF15</p>
</blockquote></td>
<td><blockquote>
<p>INPUT</p>
</blockquote></td>
<td><blockquote>
<p>DIEZ</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>IB BILLING CLOCK HEADER</td>
<td><blockquote>
<p>IBXBCR2</p>
</blockquote></td>
<td><blockquote>
<p>PRINT</p>
</blockquote></td>
<td><blockquote>
<p>DIPZ</p>
</blockquote></td>
</tr>
<tr class="even">
<td>IB BILLING CLOCK INQ</td>
<td><blockquote>
<p>IBXBCR</p>
</blockquote></td>
<td><blockquote>
<p>PRINT</p>
</blockquote></td>
<td><blockquote>
<p>DIPZ</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>IB CPT CP DISPLAY</td>
<td><blockquote>
<p>IBXCPTC</p>
</blockquote></td>
<td><blockquote>
<p>PRINT</p>
</blockquote></td>
<td><blockquote>
<p>DIPZ</p>
</blockquote></td>
</tr>
<tr class="even">
<td>IB CPT PG DISPLAY</td>
<td><blockquote>
<p>IBXCPTG</p>
</blockquote></td>
<td><blockquote>
<p>PRINT</p>
</blockquote></td>
<td><blockquote>
<p>DIPZ</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>IB CPT RG DISPLAY</td>
<td><blockquote>
<p>IBXCPTR</p>
</blockquote></td>
<td><blockquote>
<p>PRINT</p>
</blockquote></td>
<td><blockquote>
<p>DIPZ</p>
</blockquote></td>
</tr>
<tr class="even">
<td>IB DIVISION DISPLAY</td>
<td><blockquote>
<p>IBXDIVD</p>
</blockquote></td>
<td><blockquote>
<p>PRINT</p>
</blockquote></td>
<td><blockquote>
<p>DIPZ</p>
</blockquote></td>
</tr>
</tbody>
</table>

Installation Instructions

## Step Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### \>\>\> Remember to recompile the following cross references for the following files on all CPUs.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 49%" />
<col style="width: 17%" />
<col style="width: 15%" />
<col style="width: 17%" />
</colgroup>
<thead>
<tr class="header">
<th>FILE</th>
<th><blockquote>
<p>ROUTINE</p>
</blockquote></th>
<th><blockquote>
<p>TYPE</p>
</blockquote></th>
<th><blockquote>
<p>ROUTINE</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>INTEGRATED BILLING ACTION (#350)</td>
<td><blockquote>
<p>IBXA</p>
</blockquote></td>
<td><blockquote>
<p>X-REF</p>
</blockquote></td>
<td><blockquote>
<p>DIKZ</p>
</blockquote></td>
</tr>
<tr class="even">
<td>ENCOUNTER FORM (#357)</td>
<td><blockquote>
<p>IBXF0</p>
</blockquote></td>
<td><blockquote>
<p>X-REF</p>
</blockquote></td>
<td><blockquote>
<p>DIKZ</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>ENCOUNTER FORM BLOCK (#357.1)</td>
<td><blockquote>
<p>IBXF1</p>
</blockquote></td>
<td><blockquote>
<p>X-REF</p>
</blockquote></td>
<td><blockquote>
<p>DIKZ</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SELECTION LIST (#357.2)</td>
<td><blockquote>
<p>IBXF2</p>
</blockquote></td>
<td><blockquote>
<p>X-REF</p>
</blockquote></td>
<td><blockquote>
<p>DIKZ</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>SELECTION (#357.3)</td>
<td><blockquote>
<p>IBXF3</p>
</blockquote></td>
<td><blockquote>
<p>X-REF</p>
</blockquote></td>
<td><blockquote>
<p>DIKZ</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SELECTION GROUP (#357.4)</td>
<td><blockquote>
<p>IBXF4</p>
</blockquote></td>
<td><blockquote>
<p>X-REF</p>
</blockquote></td>
<td><blockquote>
<p>DIKZ</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>DATA FIELD (#357.5)</td>
<td><blockquote>
<p>IBXF5</p>
</blockquote></td>
<td><blockquote>
<p>X-REF</p>
</blockquote></td>
<td><blockquote>
<p>DIKZ</p>
</blockquote></td>
</tr>
<tr class="even">
<td>BILL/CLAIMS (#399)</td>
<td><blockquote>
<p>IBXX</p>
</blockquote></td>
<td><blockquote>
<p>X-REF</p>
</blockquote></td>
<td><blockquote>
<p>DIKZ</p>
</blockquote></td>
</tr>
</tbody>
</table>

### Move routines to all systems. It is recommended that the globals DGCR, IB, IBA, IBE, and IBT be journaled.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Rebuild routine map sets.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### It is strongly recommended that the following routines be added to the routine map set on the volume set that they will be primarily running on.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### IBA\* IBC\* IBEF\* IBR\* IBT\* IBX\*

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### You may wish to bring users on-line at this point.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### You may now delete obsolete routines from your system.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### The IB routines IBACKIN, IBEP, IBEHCFA, IBEHCF1, IBOHCTP,

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### IBOHCP, IB15\*, and IBY\* are obsolete and may be deleted from your system.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### The only active DGCR routines with Integrated Billing v2.0 are DGCRNS, DGCRAMS, and DGCRP3. All other DGCR routines are obsolete and may be deleted from your system.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### You may now use the Encounter Form Import/Export Utility to import the sample encounter forms exported with this package. It is not necessary to perform this step at this point, but it must be performed before you begin active design and development of forms for your facility. Instructions for importing the forms may be found in the Encounter Form Utilities Module of the User Manual, Import/Export Utility option. Once you have imported these sample forms, you may delete the IBDEI\* routines from your system. This will delete the initialization routines for the Encounter Form Import/Export Utility package (namespace IBDE).

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation Instructions

## Step Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### You will be notified by a MailMan message when each of the queued conversion jobs have completed. Once the final conversion has completed, you may delete the IBI\*, IBONI\*, and IB20\* routines from your system. This will delete the initialization, pre-init, and post-init routines from your system.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Run the Build Primary Menu Trees option on the Menu Management menu on all systems. Though this step is optional, it may greatly improve performance during the first few days of operation.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Review the entry in the IB SITE PARAMETERS file (#350.9) and ensure that all parameters are set correctly.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Ensure that the option IB MT NIGHT COMP is tasked to run early each morning (after the G&L has been completed, but before normal working hours). This job now includes updates performed by the Claims Tracking and Automated Biller modules. Be sure that this option is not tasked twice to run on your system! This will have adverse effects on the Means Test Billing module.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation Instructions

# Routine List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DGCRAMS DGCRNS DGCRP3 IB20IN IB20PRE IB20PT IB20PT1 IB20PT2 IB20PT3 IB20PT31 IB20PT32 IB20PT4 IB20PT41 IB20PT42 IB20PT43 IB20PT44 IB20PT45 IB20PT46 IB20PT47 IB20PT48 IB20PT5 IB20PT51 IB20PT6 IB20PT61 IB20PT62 IB20PT7 IB20PT71 IB20PT8 IB20PT81 IB20PT82 IB20PT83 IB20PT84 IB20PT85 IB20PT86 IB20PT87 IB20PT88 IB20PT89 IB20PT8A IB20PT8B IB20PT8C IBACVA IBACVA1 IBACVA2 IBAERR IBAERR1 IBAERR2 IBAERR3 IBAFIL IBAMTBU IBAMTBU1 IBAMTBU2 IBAMTC IBAMTC1 IBAMTC2 IBAMTC3 IBAMTD IBAMTD1 IBAMTD2 IBAMTED IBAMTED1 IBAMTEDU IBAMTEL IBAMTI IBAMTI1 IBAMTI2 IBAMTS IBAMTS1 IBAMTS2 IBAPDX IBAPDX0 IBAPDX1 IBAREP IBARX IBARX1 IBARXDOC IBARXEB IBARXEC IBARXEC0 IBARXEC1 IBARXEC2 IBARXEC3 IBARXEC4 IBARXEC5 IBARXECA IBARXEI IBARXEP IBARXEPE IBARXEPL

| IBARXEPV IBARXET |         | IBARXEU          | IBARXEU0 IBARXEU1 IBARXEU3 IBARXEU4 IBARXEU5 |         |                            |                  |         |
|------------------|---------|------------------|----------------------------------------------|---------|----------------------------|------------------|---------|
| IBARXEVT IBARXEX |         | IBARXEX1 IBAUTL  |                                              | IBAUTL1 | IBAUTL2                    | IBAUTL3          | IBAUTL4 |
| IBAUTL5          | IBAUTL6 | IBAUTL7          | IBCA                                         | IBCA0   | IBCA1                      | IBCA2            | IBCA3   |
| IBCAMS           | IBCB    | IBCB1            | IBCB2                                        | IBCBB   | IBCBB1                     | IBCBB2           | IBCBR   |
| IBCBULL          | IBCC    | IBCCC            | IBCCC1                                       | IBCCC2  | IBCCC3                     | IBCCPT           | IBCD    |
| IBCD1            | IBCD2   | IBCD3            | IBCD4                                        | IBCD5   | IBCDC                      | IBCDE            | IBCF    |
| IBCF1            | IBCF10  | IBCF11           | IBCF12                                       | IBCF13  | IBCF14                     | IBCF1TP          | IBCF2   |
| IBCF21           | IBCF22  | IBCF23           | IBCF2P                                       | IBCF2TP | IBCF3                      | IBCF31           | IBCF32  |
| IBCF33           | IBCF331 | IBCF34           | IBCF3P                                       | IBCF3TP | IBCF4                      | IBCFP            | IBCMENU |
| IBCNADD          | IBCNQ   | IBCNQ1           | IBCNS                                        | IBCNS1  | IBCNS2                     | IBCNSA           | IBCNSA0 |
| IBCNSA1          | IBCNSA2 | IBCNSBL          | IBCNSBL1 IBCNSC                              |         | IBCNSC0                    | IBCNSC01 IBCNSC1 |         |
| IBCNSC2          | IBCNSC3 | IBCNSD           | IBCNSD1                                      | IBCNSEH | IBCNSEVT IBCNSM            |                  | IBCNSM1 |
| IBCNSM2          | IBCNSM3 | IBCNSM31 IBCNSM4 |                                              | IBCNSM5 | IBCNSM6                    | IBCNSM7          | IBCNSM8 |
| IBCNSM9          | IBCNSOK | IBCNSOK1 IBCNSP  |                                              | IBCNSP0 | IBCNSP01 IBCNSP02 IBCNSP1  |                  |         |
| IBCNSP2          | IBCNSP3 | IBCNSU           | IBCNSU1                                      | IBCNSV  | IBCOC                      | IBCOC1           | IBCONS1 |
| IBCONS2          | IBCONS3 | IBCONSC          | IBCOPV                                       | IBCOPV1 | IBCOPV2                    | IBCORC           | IBCORC1 |
| IBCORC2          | IBCRTN  | IBCSC1           | IBCSC2                                       | IBCSC3  | IBCSC4                     | IBCSC4A          | IBCSC4B |
| IBCSC4C          | IBCSC4D | IBCSC4E          | IBCSC5                                       | IBCSC5A | IBCSC5B                    | IBCSC5C          | IBCSC6  |
| IBCSC61          | IBCSC7  | IBCSC8           | IBCSC82                                      | IBCSC8H | IBCSCE                     | IBCSCE1          | IBCSCH  |
| IBCSCH1          | IBCSCP  | IBCSCU           | IBCU                                         | IBCU1   | IBCU2                      | IBCU3            | IBCU4   |
| IBCU41           | IBCU5   | IBCU6            | IBCU61                                       | IBCU62  | IBCU63                     | IBCU64           | IBCU7   |
| IBCU71           | IBCU8   | IBCU81           | IBCU82                                       | IBCVA   | IBCVA0                     | IBCVA1           | IBDE    |
| IBDE1            | IBDE1A  | IBDE1B           | IBDE2                                        | IBDE3   | IBDEHELP IBDEI001 IBDEI002 |                  |         |

IBDEI003 IBDEI004 IBDEI005 IBDEI006 IBDEI007 IBDEI008 IBDEI009 IBDEI00A IBDEI00B IBDEI00C IBDEI00D IBDEI00E IBDEI00F IBDEI00G IBDEI00H IBDEI00I IBDEI00J IBDEI00K IBDEI00L IBDEI00M IBDEI00N IBDEI00O IBDEI00P IBDEI00Q IBDEI00R IBDEI00S IBDEI00T IBDEI00U IBDEI00V IBDEI00W IBDEI00X IBDEI00Y IBDEI00Z IBDEI010 IBDEI011 IBDEI012 IBDEI013 IBDEI014 IBDEI015 IBDEI016 IBDEI017 IBDEI018 IBDEI019 IBDEI01A IBDEI01B IBDEI01C IBDEI01D IBDEI01E IBDEI01F IBDEI01G IBDEI01H IBDEI01I IBDEI01J IBDEI01K IBDEI01L IBDEI01M IBDEI01N IBDEI01O IBDEI01P IBDEI01Q IBDEI01R IBDEI01S IBDEI01T IBDEI01U IBDEI01V IBDEI01W IBDEI01X IBDEI01Y IBDEINI1 IBDEINI2 IBDEINI3 IBDEINI4 IBDEINI5 IBDEINIS IBDEINIT IBDF10 IBDF10A IBDF10B IBDF11 IBDF11A IBDF12 IBDF13 IBDF14 IBDF15 IBDF16 IBDF17 IBDF18 IBDF19 IBDF1A IBDF1B IBDF1B1 IBDF1B1A IBDF1B1B IBDF1B2 IBDF1B3 IBDF1B5 IBDF1BA IBDF1C IBDF2A IBDF2B IBDF2B1 IBDF2D IBDF2D1 IBDF2E IBDF2F IBDF3 IBDF4 IBDF4A IBDF5 IBDF5A IBDF5B IBDF5C IBDF6 IBDF6A IBDF6C IBDF7 IBDF8 IBDF9 IBDF9A IBDF9A1 IBDF9B IBDF9B1 IBDF9C IBDF9D IBDF9E IBDFN IBDFN1 IBDFN2 IBDFN3 IBDFN4 IBDFN5 IBDFN6 IBDFU IBDFU1 IBDFU10 IBDFU1A IBDFU1B IBDFU2 IBDFU2A IBDFU2B IBDFU2C IBDFU3 IBDFU4 IBDFU5 IBDFU5A IBDFU6 IBDFU7 IBDFU8 IBDFU9 IBDFUA IBEBR IBEBRH IBECEA IBECEA0 IBECEA1 IBECEA2 IBECEA21 IBECEA22 IBECEA3 IBECEA31

Routine List

IBECEA32 IBECEA33 IBECEA4 IBECEA5 IBECEA51 IBECEAU IBECEAU1 IBECEAU2 IBECEAU3 IBECEAU4 IBECK IBECPF IBECPTE IBECPTT IBECPTZ IBEF IBEFCOP IBEFUNC IBEFUNC1 IBEFUNC2 IBEFUTL IBEFUTL1 IBEMTBC IBEMTF IBEMTF1 IBEMTF2 IBEMTO IBEMTO1 IBEPAR IBEPAR1 IBERS IBERS1 IBERS2 IBERS3 IBERSE IBERSI IBERSP IBERSP1 IBESTAT IBETIME IBINI001 IBINI002 IBINI003 IBINI004 IBINI005 IBINI006 IBINI007 IBINI008 IBINI009 IBINI00A IBINI00B IBINI00C IBINI00D IBINI00E IBINI00F IBINI00G IBINI00H IBINI00I IBINI00J IBINI00K IBINI00L IBINI00M IBINI00N IBINI00O IBINI00P IBINI00Q IBINI00R IBINI00S IBINI00T IBINI00U IBINI00V IBINI00W IBINI00X IBINI00Y IBINI00Z IBINI010 IBINI011 IBINI012 IBINI013 IBINI014 IBINI015 IBINI016 IBINI017 IBINI018 IBINI019 IBINI01A IBINI01B IBINI01C IBINI01D IBINI01E IBINI01F IBINI01G IBINI01H IBINI01I IBINI01J IBINI01K IBINI01L IBINI01M IBINI01N IBINI01O IBINI01P IBINI01Q IBINI01R IBINI01S IBINI01T IBINI01U IBINI01V IBINI01W IBINI01X IBINI01Y IBINI01Z IBINI020 IBINI021 IBINI022 IBINI023 IBINI024 IBINI025 IBINI026 IBINI027 IBINI028 IBINI029 IBINI02A IBINI02B IBINI02C IBINI02D IBINI02E IBINI02F IBINI02G IBINI02H IBINI02I IBINI02J IBINI02K IBINI02L IBINI02M IBINI02N IBINI02O IBINI02P IBINI02Q IBINI02R IBINI02S IBINI02T IBINI02U IBINI02V IBINI02W IBINI02X IBINI02Y IBINI02Z IBINI030 IBINI031 IBINI032 IBINI033 IBINI034 IBINI035 IBINI036 IBINI037 IBINI038 IBINI039 IBINI03A IBINI03B IBINI03C IBINI03D IBINI03E IBINI03F IBINI03G IBINI03H IBINI03I IBINI03J IBINI03K IBINI03L IBINI03M IBINI03N IBINI03O IBINI03P IBINI03Q IBINI03R IBINI03S IBINI03T IBINI03U IBINI03V IBINI03W IBINI03X IBINI03Y IBINI03Z IBINI040 IBINI041 IBINI042 IBINI043 IBINI044 IBINI045 IBINI046 IBINI047 IBINI048 IBINI049 IBINI04A IBINI04B IBINI04C IBINI04D IBINI04E IBINI04F IBINI04G IBINI04H IBINI04I IBINI04J IBINI04K IBINI04L IBINI04M IBINI04N IBINI04O IBINI04P IBINI04Q IBINI04R IBINI04S IBINI04T IBINI04U IBINI04V IBINI04W IBINI04X IBINI04Y IBINI04Z IBINI050 IBINI051 IBINI052 IBINI053 IBINI054 IBINI055 IBINI056 IBINI057 IBINI058 IBINI059 IBINI05A IBINI05B IBINI05C IBINI05D IBINI05E IBINI05F IBINI05G IBINI05H IBINI05I IBINI05J IBINI05K IBINI05L IBINI05M IBINI05N IBINI05O IBINI05P IBINI05Q IBINI05R IBINI05S IBINI05T IBINI05U IBINI05V IBINI05W IBINI05X IBINI05Y IBINI05Z IBINI060 IBINI061 IBINI062 IBINI063 IBINI064 IBINI065 IBINI066 IBINI067 IBINI068 IBINI069 IBINI06A IBINI06B IBINI06C IBINI06D IBINI06E IBINI06F IBINI06G IBINI06H IBINI06I IBINI06J IBINI06K IBINI06L IBINI06M IBINI06N IBINI06O IBINI06P IBINI06Q IBINI06R IBINI06S IBINI06T IBINI06U IBINI06V IBINI06W IBINI06X IBINI06Y IBINI06Z IBINI070 IBINI071 IBINI072 IBINI073 IBINI074 IBINI075 IBINI076 IBINI077 IBINI078 IBINI079 IBINI07A IBINI07B IBINI07C IBINI07D IBINI07E IBINI07F IBINI07G IBINI07H IBINI07I IBINI07J IBINI07K IBINI07L IBINI07M IBINI07N IBINI07O IBINI07P IBINI07Q IBINI07R IBINI07S IBINI07T IBINI07U IBINI07V IBINI07W IBINI07X IBINI07Y IBINI07Z IBINI080 IBINI081 IBINI082 IBINI083 IBINI084 IBINI085 IBINI086 IBINI087 IBINI088 IBINI089 IBINI08A IBINI08B IBINI08C IBINI08D IBINI08E IBINI08F IBINI08G IBINI08H IBINI08I IBINI08J IBINI08K IBINI08L IBINI08M IBINI08N IBINI08O IBINI08P IBINI08Q IBINI08R IBINI08S IBINI08T IBINI08U IBINI08V IBINI08W IBINI08X IBINI08Y IBINI08Z IBINI090 IBINI091 IBINI092 IBINI093 IBINI094 IBINI095 IBINI096 IBINI097 IBINI098 IBINI099 IBINI09A IBINI09B IBINI09C IBINI09D IBINI09E IBINI09F IBINI09G IBINI09H IBINI09I IBINI09J IBINI09K IBINI09L IBINI09M IBINI09N IBINI09O IBINI09P IBINI09Q IBINI09R IBINI09S IBINI09T IBINI09U IBINI09V IBINI09W IBINI09X IBINI09Y IBINI09Z IBINI0A0 IBINI0A1 IBINI0A2 IBINI0A3 IBINI0A4 IBINI0A5 IBINI0A6 IBINI0A7 IBINI0A8 IBINI0A9 IBINI0AA IBINI0AB IBINI0AC IBINI0AD IBINI0AE IBINI0AF IBINI0AG IBINI0AH IBINI0AI IBINI0AJ IBINI0AK IBINI0AL IBINI0AM IBINI0AN IBINI0AO IBINI0AP IBINI0AQ IBINI0AR IBINI0AS IBINI0AT IBINI0AU IBINI0AV IBINI0AW IBINI0AX IBINI0AY IBINI0AZ IBINI0B0 IBINI0B1 IBINI0B2 IBINI0B3 IBINI0B4 IBINI0B5 IBINI0B6 IBINI0B7 IBINI0B8 IBINI0B9 IBINI0BA IBINI0BB IBINI0BC IBINI0BD IBINI0BE IBINI0BF IBINI0BG IBINI0BH IBINI0BI IBINI0BJ IBINI0BK IBINI0BL IBINI0BM IBINI0BN IBINI0BO IBINI0BP IBINI0BQ IBINI0BR IBINI0BS IBINI0BT IBINI0BU IBINI0BV IBINI0BW IBINI0BX IBINI0BY IBINI0BZ IBINI0C0

Routine List

IBINI0C1 IBINI0C2 IBINI0C3 IBINI0C4 IBINI0C5 IBINI0C6 IBINI0C7 IBINI0C8 IBINI0C9 IBINI0CA IBINI0CB IBINI0CC IBINI0CD IBINI0CE IBINI0CF IBINI0CG IBINI0CH IBINI0CI IBINI0CJ IBINI0CK IBINI0CL IBINI0CM IBINI0CN IBINI0CO IBINI0CP IBINI0CQ IBINI0CR IBINI0CS IBINI0CT IBINI0CU IBINI0CV IBINI0CW IBINI0CX IBINI0CY IBINI0CZ IBINI0D0 IBINI0D1 IBINI0D2 IBINI0D3 IBINI0D4 IBINI0D5 IBINI0D6 IBINI0D7 IBINI0D8 IBINI0D9 IBINI0DA IBINI0DB IBINI0DC IBINI0DD IBINI0DE IBINI0DF IBINI0DG IBINI0DH IBINI0DI IBINI0DJ IBINI0DK IBINI0DL IBINI0DM IBINI0DN IBINI0DO IBINI0DP IBINI0DQ IBINI0DR IBINI0DS IBINI0DT IBINI0DU IBINI0DV IBINI0DW IBINI0DX IBINI0DY IBINI0DZ IBINI0E0 IBINI0E1 IBINI0E2 IBINI0E3 IBINI0E4 IBINI0E5 IBINI0E6 IBINI0E7 IBINI0E8 IBINI0E9 IBINI0EA IBINI0EB IBINI0EC IBINIS IBINIT IBINIT1 IBINIT2 IBINIT3 IBINIT4 IBINIT5 IBINIT6 IBNTEG IBNTEG0 IBNTEG01 IBNTEG02 IBOA31 IBOA32 IBOAMS IBOBCC IBOBCC1 IBOBCR6 IBOBCRT IBOBL IBOCHK IBOCNC IBOCNC1 IBOCNC2 IBOCOSI IBOCPD IBOCPDS IBODISP IBODIV IBOEMP IBOEMP1 IBOEMP2 IBOHLD1 IBOHLD2 IBOLK IBOLK1 IBOMBL IBOMTC IBOMTC1 IBOMTE IBOMTE1 IBOMTE2 IBOMTP IBOMTP1 IBONI001 IBONI002 IBONI003 IBONI004 IBONI005 IBONI006 IBONI007 IBONI008 IBONI009 IBONI010 IBONI011 IBONI012 IBONI013 IBONI014 IBONI015 IBONI016 IBONI017 IBONI018 IBONI019 IBONI020 IBONI021 IBONI022 IBONI023 IBONI024 IBONI025 IBONI026 IBONI027 IBONI028 IBONI029 IBONI030 IBONI031 IBONI032 IBONI033 IBONI034 IBONI035 IBONI036 IBONI037 IBONI038 IBONI039 IBONI040

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 11%" />
<col style="width: 12%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="3">IBONI041 IBONI042 IBONIT</th>
<th>IBONIT1</th>
<th>IBONIT2</th>
<th>IBONIT3</th>
<th>IBORAT</th>
<th>IBORAT1A</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="5">IBORAT1B IBORAT1C IBORAT2A IBORAT2B IBORAT2C</td>
<td>IBORT</td>
<td>IBORT1</td>
<td>IBOST</td>
</tr>
<tr class="even">
<td>IBOSTUS</td>
<td colspan="2">IBOSTUS1 IBOTR</td>
<td>IBOTR1</td>
<td>IBOTR2</td>
<td>IBOTR3</td>
<td>IBOTR4</td>
<td>IBOUNP1</td>
</tr>
<tr class="odd">
<td>IBOUNP2</td>
<td>IBOUNP3</td>
<td>IBOUNP4</td>
<td>IBOUNP5</td>
<td>IBOUNP6</td>
<td>IBOUTL</td>
<td>IBOVOP</td>
<td>IBOVOP1</td>
</tr>
<tr class="even">
<td>IBOVOP2</td>
<td>IBP</td>
<td>IBPA</td>
<td>IBPEX</td>
<td>IBPF</td>
<td>IBPF1</td>
<td>IBPFU</td>
<td>IBPO</td>
</tr>
<tr class="odd">
<td>IBPP</td>
<td>IBPU</td>
<td>IBPU1</td>
<td>IBPU2</td>
<td>IBPUBUL</td>
<td>IBPUDEL</td>
<td>IBR</td>
<td>IBRBUL</td>
</tr>
<tr class="even">
<td>IBRCON1</td>
<td>IBRCON2</td>
<td>IBRCON3</td>
<td>IBRFN</td>
<td>IBRFN1</td>
<td>IBRFN2</td>
<td>IBRREL</td>
<td>IBRUTL</td>
</tr>
<tr class="odd">
<td>IBTOAT</td>
<td>IBTOAT1</td>
<td>IBTOAT2</td>
<td>IBTOBI</td>
<td>IBTOBI1</td>
<td>IBTOBI2</td>
<td>IBTOBI3</td>
<td>IBTOBI4</td>
</tr>
<tr class="even">
<td>IBTODD</td>
<td>IBTODD1</td>
<td>IBTOLR</td>
<td>IBTONB</td>
<td>IBTOPW</td>
<td>IBTOSA</td>
<td>IBTOSUM</td>
<td>IBTOSUM1</td>
</tr>
<tr class="odd">
<td colspan="2">IBTOSUM2 IBTOTR</td>
<td>IBTOUA</td>
<td>IBTOUR</td>
<td>IBTOUR1</td>
<td>IBTOUR2</td>
<td>IBTOUR3</td>
<td>IBTOUR4</td>
</tr>
<tr class="even">
<td>IBTOUR5</td>
<td>IBTOVS</td>
<td>IBTRC</td>
<td>IBTRC1</td>
<td>IBTRC2</td>
<td>IBTRC3</td>
<td>IBTRC4</td>
<td>IBTRCD</td>
</tr>
<tr class="odd">
<td>IBTRCD0</td>
<td>IBTRCD1</td>
<td>IBTRD</td>
<td>IBTRD1</td>
<td>IBTRDD</td>
<td>IBTRDD1</td>
<td>IBTRE</td>
<td>IBTRE0</td>
</tr>
<tr class="even">
<td>IBTRE1</td>
<td>IBTRE2</td>
<td>IBTRE20</td>
<td>IBTRE3</td>
<td>IBTRE4</td>
<td>IBTRE5</td>
<td>IBTRE6</td>
<td>IBTRED</td>
</tr>
<tr class="odd">
<td>IBTRED0</td>
<td colspan="2">IBTRED01 IBTRED1</td>
<td>IBTRED2</td>
<td>IBTRKR</td>
<td>IBTRKR1</td>
<td>IBTRKR2</td>
<td>IBTRKR3</td>
</tr>
<tr class="even">
<td colspan="2">IBTRKR31 IBTRKR4</td>
<td colspan="2">IBTRKR41 IBTRKR5</td>
<td>IBTRP</td>
<td>IBTRPR</td>
<td>IBTRPR0</td>
<td>IBTRPR01</td>
</tr>
<tr class="odd">
<td>IBTRPR1</td>
<td>IBTRPR2</td>
<td>IBTRV</td>
<td>IBTRV1</td>
<td>IBTRV2</td>
<td>IBTRV3</td>
<td>IBTRV31</td>
<td>IBTRVD</td>
</tr>
<tr class="even">
<td>IBTRVD0</td>
<td>IBTRVD1</td>
<td>IBTUTL</td>
<td>IBTUTL1</td>
<td>IBTUTL2</td>
<td>IBTUTL3</td>
<td>IBTUTL4</td>
<td></td>
</tr>
<tr class="odd">
<td colspan="3"><blockquote>
<p>1207 routines</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

Routine List

# Sample Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\>D ^IBINIT

This version (#2.0) of 'IBINIT' was created on 21-MAR-1994

(at ALBANY ISC VAX DEVELOPMENT, by VA FileMan V.20.0) I HAVE TO RUN AN ENVIRONMENT CHECK ROUTINE.

Initialization Started: MAR 21, 1994@12:38:03

The auto biller parameters can be set automatically during the post-init by answering the following question affirmatively. If the auto biller parameters are set-up by the post-init then the Earliest Auto Bill

Date of the current inpatient admissions will be set as they are loaded into the Claims Tracking module by one of the queued conversion routines. The result will be that the auto biller will be able to process these inpatient admissions and possibly create bills for them when it runs. If these parameters are not set and the auto biller will be running at your site for inpatient admissions then the Earliest Auto Bill Date of each current inpatient admission will

have to be set manually after the conversion is done. The parameters will be set up with the following values:

> Auto Biller Frequency: 7 days - the auto biller will not run

> until 7 days after this install Automate Billing: 1 Yes - the Earliest Auto bill date will

> be set during the conversion Billing Cycle: left blank, billing cycle will be one month Days Delay: 2 days - number of days after the billing

> cycle is completed that the bill will be created

If these settings for the parameters are not what your site requires then you may change them after the installation is complete but before the conversions begin to run - there is a 15 minute window.

These parameters can also be changed at any time after the

installation and conversion are complete (option IB AUTO BILLER PARAMS).

Enter Yes or No: YES

I AM GOING TO SET UP THE FOLLOWING FILES:

2 PATIENT (Partial Definition) Note: You already have the 'PATIENT' File.

> 36 INSURANCE COMPANY

> **NOTE:** You already have the 'INSURANCE COMPANY' File.

350. INTEGRATED BILLING ACTION

> **NOTE:** You already have the 'INTEGRATED BILLING ACTION' File.

1.  IB ACTION TYPE (including data) Note: You already have the 'IB ACTION TYPE' File. Want my data merged with yours? NO

Sample Installation

2.  IB ACTION CHARGE (including data) Note: You already have the 'IB ACTION CHARGE' File. Want my data merged with yours? NO

> 350.21 IB ACTION STATUS

3.  IB CHARGE REMOVE REASONS (including data) Note: You already have the 'IB CHARGE REMOVE REASONS' File. Want my data merged with yours? NO
4.  BILLABLE AMBULATORY SURGICAL CODE

> **NOTE:** You already have the 'BILLABLE AMBULATORY SURGICAL CODE' File.

> 350.41 UPDATE BILLABLE AMBULATORY SURGICAL CODE

> **NOTE:** You already have the 'UPDATE BILLABLE AMBULATORY SURGICAL CODE' File.

5.  BASC LOCALITY MODIFIER

> **NOTE:** You already have the 'BASC LOCALITY MODIFIER' File.

6.  IB ARCHIVE/PURGE LOG

> **NOTE:** You already have the 'IB ARCHIVE/PURGE LOG' File.

7.  AMBULATORY CHECK-OFF SHEET

> **NOTE:** You already have the 'AMBULATORY CHECK-OFF SHEET' File.

> 350.71 AMBULATORY SURG. CHECK-OFF SHEET PRINT FIELDS

> **NOTE:** You already have the 'AMBULATORY SURG. CHECK-OFF SHEET PRINT FIELDS'

File.

8.  IB ERROR (including data) Note: You already have the 'IB ERROR' File. I will OVERWRITE your data with mine.
9.  IB SITE PARAMETERS

> **NOTE:** You already have the 'IB SITE PARAMETERS' File.

351. CATEGORY C BILLING CLOCK

> **NOTE:** You already have the 'CATEGORY C BILLING CLOCK' File.

1.  IB CONTINUOUS PATIENT

> **NOTE:** You already have the 'IB CONTINUOUS PATIENT' File.

2.  SPECIAL INPATIENT BILLING CASES

352.1 BILLABLE APPOINTMENT TYPE (including data) Note: You already have the 'BILLABLE APPOINTMENT TYPE' File. Want my data merged with yours? NO

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 38%" />
<col style="width: 41%" />
</colgroup>
<thead>
<tr class="header">
<th>352.2</th>
<th colspan="2"><blockquote>
<p>NON-BILLABLE DISPOSITIONS</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>352.3</td>
<td colspan="2"><blockquote>
<p>NON-BILLABLE CLINIC STOP CODES</p>
</blockquote></td>
</tr>
<tr class="even">
<td>352.4</td>
<td colspan="2"><blockquote>
<p>NON-BILLABLE CLINICS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>353</td>
<td><blockquote>
<p>BILL FORM TYPE</p>
</blockquote></td>
<td>(including data)</td>
</tr>
</tbody>
</table>

> **NOTE:** You already have the 'BILL FORM TYPE' File. Want my data merged with yours? NO

Sample Installation

1.  PLACE OF SERVICE (including data) Note: You already have the 'PLACE OF SERVICE' File. Want my data to overwrite yours? NO
2.  TYPE OF SERVICE (including data) Note: You already have the 'TYPE OF SERVICE' File. Want my data to overwrite yours? NO
354. BILLING PATIENT

> **NOTE:** You already have the 'BILLING PATIENT' File.

1.  BILLING EXEMPTIONS

> **NOTE:** You already have the 'BILLING EXEMPTIONS' File.

2.  EXEMPTION REASON (including data) Note: You already have the 'EXEMPTION REASON' File. Want my data merged with yours? NO
3.  BILLING THRESHOLDS (including data) Note: You already have the 'BILLING THRESHOLDS' File. Want my data merged with yours? NO
4.  BILLING ALERTS

> **NOTE:** You already have the 'BILLING ALERTS' File.

5.  BILLING ALERT DEFINITION (including data) Note: You already have the 'BILLING ALERT DEFINITION' File. Want my data merged with yours? NO
6.  IB FORM LETTER (including data) Note: You already have the 'IB FORM LETTER' File. Want my data merged with yours? NO
1.  TYPE OF PLAN (including data) I will OVERWRITE your data with mine.
2.  TYPE OF INSURANCE COVERAGE (including data) I will OVERWRITE your data with mine.

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 41%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr class="header">
<th>355.3</th>
<th colspan="2"><blockquote>
<p>GROUP INSURANCE PLAN</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>355.4</td>
<td colspan="2"><blockquote>
<p>ANNUAL BENEFITS</p>
</blockquote></td>
</tr>
<tr class="even">
<td>355.5</td>
<td colspan="2"><blockquote>
<p>INSURANCE CLAIMS YEAR TO DATE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>355.6</td>
<td><blockquote>
<p>INSURANCE RIDERS</p>
</blockquote></td>
<td>(including data)</td>
</tr>
</tbody>
</table>

I will MERGE your data with mine.

> 355.7 PERSONAL POLICY

356. CLAIMS TRACKING
     1.  HOSPITAL REVIEW

356.11 CLAIMS TRACKING REVIEW TYPE (including data) I will MERGE your data with mine.

> 356.2 INSURANCE REVIEW

Sample Installation

356.21 CLAIMS TRACKING DENIAL REASONS (including data) I will MERGE your data with mine.

356.3 CLAIMS TRACKING SI/IS CATEGORIES (including data) I will MERGE your data with mine.

> 356.399 CLAIMS TRACKING/BILL

4.  CLAIMS TRACKING NON-ACUTE CLASSIFICATIONS (including data) I will MERGE your data with mine.
5.  CLAIMS TRACKING ALOS (including data) I will MERGE your data with mine.
6.  CLAIMS TRACKING TYPE (including data) I will MERGE your data with mine.
7.  CLAIMS TRACKING ACTION (including data) I will MERGE your data with mine.
8.  CLAIMS TRACKING NON-BILLABLE REASONS (including data) I will MERGE your data with mine.

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 41%" />
<col style="width: 38%" />
</colgroup>
<thead>
<tr class="header">
<th>356.9</th>
<th colspan="2"><blockquote>
<p>INPATIENT DIAGNOSIS</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>356.91</td>
<td colspan="2"><blockquote>
<p>INPATIENT PROCEDURE</p>
</blockquote></td>
</tr>
<tr class="even">
<td>356.93</td>
<td colspan="2"><blockquote>
<p>INPATIENT INTERIM DRG</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>356.94</td>
<td colspan="2"><blockquote>
<p>INPATIENT PROVIDERS</p>
</blockquote></td>
</tr>
<tr class="even">
<td>357</td>
<td colspan="2"><blockquote>
<p>ENCOUNTER FORM</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>357.1</td>
<td colspan="2"><blockquote>
<p>ENCOUNTER FORM BLOCK</p>
</blockquote></td>
</tr>
<tr class="even">
<td>357.2</td>
<td colspan="2"><blockquote>
<p>SELECTION LIST</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>357.3</td>
<td colspan="2"><blockquote>
<p>SELECTION</p>
</blockquote></td>
</tr>
<tr class="even">
<td>357.4</td>
<td colspan="2"><blockquote>
<p>SELECTION GROUP</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>357.5</td>
<td colspan="2"><blockquote>
<p>DATA FIELD</p>
</blockquote></td>
</tr>
<tr class="even">
<td>357.6</td>
<td><blockquote>
<p>PACKAGE INTERFACE</p>
</blockquote></td>
<td>(including data)</td>
</tr>
</tbody>
</table>

I will OVERWRITE your data with mine.

7.  FORM LINE
8.  TEXT AREA
91. MARKING AREA TYPE (including data) I will MERGE your data with mine.
92. PRINT CONDITIONS (including data) I will MERGE your data with mine.
358. IMP/EXP ENCOUNTER FORM
     1.  IMP/EXP ENCOUNTER FORM BLOCK

Sample Installation

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 79%" />
</colgroup>
<thead>
<tr class="header">
<th>358.2</th>
<th><blockquote>
<p>IMP/EXP SELECTION LIST</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>358.3</td>
<td><blockquote>
<p>IMP/EXP SELECTION</p>
</blockquote></td>
</tr>
<tr class="even">
<td>358.4</td>
<td><blockquote>
<p>IMP/EXP SELECTION GROUP</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>358.5</td>
<td><blockquote>
<p>IMP/EXP DATA FIELD</p>
</blockquote></td>
</tr>
<tr class="even">
<td>358.6</td>
<td><blockquote>
<p>IMP/EXP PACKAGE INTERFACE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>358.7</td>
<td><blockquote>
<p>IMP/EXP FORM LINE</p>
</blockquote></td>
</tr>
<tr class="even">
<td>358.8</td>
<td><blockquote>
<p>IMP/EXP TEXT AREA</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>358.91</td>
<td><blockquote>
<p>IMP/EXP MARKING AREA</p>
</blockquote></td>
</tr>
<tr class="even">
<td>362.1</td>
<td><blockquote>
<p>IB AUTOMATED BILLING COMMENTS</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>362.3</td>
<td><blockquote>
<p>IB BILL/CLAIMS DIAGNOSIS</p>
</blockquote></td>
</tr>
<tr class="even">
<td>362.4</td>
<td><blockquote>
<p>IB BILL/CLAIMS PRESCRIPTION REFILL</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>362.5</td>
<td><blockquote>
<p>IB BILL/CLAIMS PROSTHETICS</p>
</blockquote></td>
</tr>
<tr class="even">
<td>399</td>
<td><blockquote>
<p>BILL/CLAIMS</p>
</blockquote></td>
</tr>
</tbody>
</table>

> **NOTE:** You already have the 'BILL/CLAIMS' File.

1.  MCCR UTILITY (including data) Note: You already have the 'MCCR UTILITY' File. Want my data merged with yours? NO
2.  REVENUE CODE (including data) Note: You already have the 'REVENUE CODE' File. Want my data merged with yours? NO
3.  RATE TYPE (including data) Note: You already have the 'RATE TYPE' File. Want my data merged with yours? NO
4.  MCCR INCONSISTENT DATA ELEMENTS (including data) Note: You already have the 'MCCR INCONSISTENT DATA ELEMENTS' File. Want my data merged with yours? NO
5.  BILLING RATES (including data) Note: You already have the 'BILLING RATES' File. Want my data merged with yours? NO
95. PRINT MANAGER CLINIC SETUP
96. PRINT MANAGER DIVISION SETUP

SHALL I WRITE OVER FILE SECURITY CODES? NO// Y (YES)

> **NOTE:** This package also contains SORT TEMPLATES

> SHALL I WRITE OVER EXISTING SORT TEMPLATES OF THE SAME NAME? YES// (YES)

> **NOTE:** This package also contains INPUT TEMPLATES

> SHALL I WRITE OVER EXISTING INPUT TEMPLATES OF THE SAME NAME? YES// (YES)

> **NOTE:** This package also contains PRINT TEMPLATES

> SHALL I WRITE OVER EXISTING PRINT TEMPLATES OF THE SAME NAME? YES// (YES)

Sample Installation

> **NOTE:** This package also contains FUNCTIONS

> SHALL I WRITE OVER EXISTING FUNCTIONS OF THE SAME NAME? YES// (YES)

> **NOTE:** This package also contains SECURITY KEYS

> SHALL I WRITE OVER EXISTING SECURITY KEYS OF THE SAME NAME? YES// (YES)

> **NOTE:** This package also contains OPTIONS

SHALL I WRITE OVER EXISTING OPTIONS OF THE SAME NAME? YES// (YES) ARE YOU SURE EVERYTHING'S OK? NO// Y (YES)

\>\>\> Removing IB SCREEN7H input template...

\>\>\> Removing 'AVC' cross-reference on REVENUE CODE field... ..

\>\>\> Removing 'AVP' cross-reference on PROCEDURES field.....

\>\>\> Deleting Obsolete List Template 'IB BILLABLE EVENT'...

\>\>\> Deleting Obsolete Print Template 'IB BILLING CYCLE PRINT'...

\>\>\> Deleting obsolete protocols...

> deleting protocol 'IBACM ENTRY SELECT'. done.

> deleting protocol 'IBACM MENU'. done.

> deleting protocol 'IBACM BLANK 1'. done.

> deleting protocol 'IBACM BLANK 10'. done.

> deleting protocol 'IBACM BLANK 11'. done.

> deleting protocol 'IBACM BLANK 12'. done.

> deleting protocol 'IBACM BLANK 2'. done.

> deleting protocol 'IBACM BLANK 3'. done.

> deleting protocol 'IBACM BLANK 4'. done.

> deleting protocol 'IBACM BLANK 5'. done.

> deleting protocol 'IBACM BLANK 6'. done.

> deleting protocol 'IBACM BLANK 7'. done.

> deleting protocol 'IBACM BLANK 8'. done.

> deleting protocol 'IBACM BLANK 9'. done.

\>\>\> Changing the option 'IB UB-82 MENU' to 'IB THIRD PARTY BILLING MENU'...

\>\>\> Deleting IB ERROR file (350.8) with data.

> It will be restored.

\>\>\> Deleting protocol 'IBACM1 MENU'...

> It will be restored.

...SORRY, LET ME THINK ABOUT THAT A MOMENT....................................

..............................................................................

..............................................................................

..............................................................................

..............................................................................

..............................................................................

..............................................................................

..............................................................................

..............................................................................

.......................

Sample Installation

Compiling Cross-Reference routine.............

...SORRY, THIS MAY TAKE A FEW MOMENTS...

IBXA1 routine filed IBXA2 routine filed

IBXA routine filed..................

Compiling Cross-Reference routine.............

...EXCUSE ME, LET ME PUT YOU ON 'HOLD' FOR A SECOND...

IBXF01 routine filed IBXF02 routine filed IBXF0 routine filed

Compiling Cross-Reference routine.............

...SORRY, I'M WORKING AS FAST AS I CAN...

IBXF11 routine filed IBXF12 routine filed IBXF13 routine filed IBXF14 routine filed IBXF15 routine filed IBXF16 routine filed IBXF1 routine filed

Compiling Cross-Reference routine.............

...EXCUSE ME, JUST A MOMENT PLEASE...

IBXF21 routine filed IBXF22 routine filed IBXF23 routine filed IBXF24 routine filed IBXF25 routine filed IBXF26 routine filed IBXF2 routine filed

Compiling Cross-Reference routine.............

...HMMM, I'M WORKING AS FAST AS I CAN...

IBXF31 routine filed IBXF32 routine filed IBXF33 routine filed IBXF34 routine filed IBXF3 routine filed

Compiling Cross-Reference routine.............

...HMMM, JUST A MOMENT PLEASE...

IBXF41 routine filed IBXF42 routine filed IBXF4 routine filed

Sample Installation

Compiling Cross-Reference routine.............

...EXCUSE ME, LET ME PUT YOU ON 'HOLD' FOR A SECOND...

IBXF51 routine filed IBXF52 routine filed IBXF53 routine filed IBXF54 routine filed IBXF5 routine filed...

Compiling Cross-Reference routine.............

...EXCUSE ME, HOLD ON...

IBXX1 routine filed IBXX2 routine filed IBXX3 routine filed IBXX4 routine filed IBXX5 routine filed IBXX6 routine filed IBXX7 routine filed IBXX8 routine filed IBXX9 routine filed IBXX10 routine filed IBXX11 routine filed IBXX12 routine filed IBXX13 routine filed IBXX14 routine filed IBXX15 routine filed IBXX16 routine filed IBXX17 routine filed IBXX18 routine filed IBXX19 routine filed IBXX20 routine filed

IBXX routine filed............................................................

..............................................................................

.......................................... 'IB ACTIVATE REVENUE CODES' Option Filed 'IB AUTHORIZE BILL GENERATION' Option Filed 'IB AUTO BILLER PARAMS' Option Filed

'IB BACKGRND VET DISCHS W/INS' Option Filed 'IB BACKGRND VETS INPT W/INS' Option Filed 'IB BACKGRND VETS OPT W/INS' Option Filed 'IB BASC INACTIVE CODES' Option Filed

'IB BASC LOCALITY MODIFIER' Option Filed 'IB BASC PRINT A GROUP' Option Filed

'IB BASC PRINT GROUP ENTRY' Option Filed 'IB BASC RATE GROUP ENTRY' Option Filed

'IB BASC TRANSFER' Option Filed

'IB BASC TRANSFER ERRORS' Option Filed

'IB BASC UPDATE MENU' Option Filed 'IB BATCH PRINT BILLS' Option Filed 'IB BILL STATUS REPORT' Option Filed 'IB BILLING CLERK MENU' Option Filed 'IB BILLING RATES FILE' Option Filed

'IB BILLING SUPERVISOR MENU' Option Filed 'IB BILLING TOTALS REPORT' Option Filed

'IB CANCEL BILL' Option Filed

'IB CANCEL/EDIT/ADD CHARGES' Option Filed

Sample Installation

'IB CLEAN AUTO BILLER LIST' Option Filed

'IB COPY AND CANCEL' Option Filed 'IB EDIT BILLING INFO' Option Filed 'IB EDIT RETURNED BILL' Option Filed

'IB EDIT SITE PARAMETERS' Option Filed

'IB FAST ENTER BILLING RATES' Option Filed 'IB FILER CLEAR PARAMETERS' Option Filed

'IB FILER START' Option Filed 'IB FILER STOP' Option Filed

'IB FLAG CONTINUOUS PATIENTS' Option Filed 'IB HCFA-1500 TEST PATTERN' Option Filed 'IB INPATIENT VET REPORT' Option Filed

'IB LIST ALL BILLS FOR PAT.' Option Filed 'IB LIST BILLS FOR EPISODE' Option Filed 'IB LIST OF BILLING RATES' Option Filed

'IB MANAGER MENU' Option Filed

'IB MCCR PARAMETER EDIT' Option Filed

'IB MEANS TEST MENU' Option Filed 'IB MT BILLING REPORT' Option Filed 'IB MT CLOCK INQUIRY' Option Filed

'IB MT CLOCK MAINTENANCE' Option Filed 'IB MT DISP SPECIAL CASES' Option Filed

'IB MT ESTIMATOR' Option Filed

'IB MT FLAG OPT PARAMS' Option Filed

'IB MT LIST FLAGGED PARAMS' Option Filed

'IB MT LIST HELD (RATE) CHARGES' Option Filed 'IB MT LIST SPECIAL CASES' Option Filed

'IB MT NIGHT COMP' Option Filed 'IB MT ON HOLD MENU' Option Filed

'IB MT PASS CONV CHARGES' Option Filed

'IB MT PROFILE' Option Filed

'IB MT REL HELD (RATE) CHARGES' Option Filed 'IB MT RELEASE CHARGES' Option Filed

'IB OUTPATIENT VET REPORT' Option Filed 'IB OUTPT VISIT DATE INQUIRY' Option Filed 'IB OUTPUT AUTO BILLER' Option Filed

'IB OUTPUT BASC FORMS FOR APPT' Option Filed

'IB OUTPUT CLK PROD' Option Filed

'IB OUTPUT CONTINUOUS PATIENTS' Option Filed 'IB OUTPUT EMPLOYER REPORT' Option Filed

'IB OUTPUT EVENTS REPORT' Option Filed

'IB OUTPUT FULL INQ BY BILL NO' Option Filed 'IB OUTPUT HELD CHARGES' Option Filed

'IB OUTPUT IB INQ' Option Filed

'IB OUTPUT INPTS WITHOUT INS' Option Filed 'IB OUTPUT INQ BY PATIENT' Option Filed 'IB OUTPUT LIST ACTIONS' Option Filed

'IB OUTPUT MANAGEMENT REPORTS' Option Filed

'IB OUTPUT MENU' Option Filed

'IB OUTPUT MOST COMMON OPT CPT' Option Filed 'IB OUTPUT OPTS WITHOUT INS' Option Filed 'IB OUTPUT PATIENT REPORT MENU' Option Filed 'IB OUTPUT RANK CARRIERS' Option Filed

'IB OUTPUT STATISTICAL REPORT' Option Filed 'IB OUTPUT TREND REPORT' Option Filed

'IB OUTPUT UNBILLED BASC' Option Filed 'IB OUTPUT VERIFY RX LINKS' Option Filed 'IB OUTPUT VETS BY DISCH' Option Filed 'IB PATIENT BILLING INQUIRY' Option Filed

Sample Installation

'IB PRINT BILL' Option Filed

'IB PRINT BILL ADDENDUM' Option Filed 'IB PURGE BILLING DATA' Option Filed

'IB PURGE DELETE TEMPLATE ENTRY' Option Filed 'IB PURGE LIST LOG ENTRIES' Option Filed

'IB PURGE LIST TEMPLATE ENTRIES' Option Filed 'IB PURGE LOG INQUIRY' Option Filed

'IB PURGE MENU' Option Filed

'IB PURGE/ARCHIVE BILLING DATA' Option Filed 'IB PURGE/BASC TRANSFER CLEANUP' Option Filed 'IB PURGE/FIND BILLING DATA' Option Filed

'IB RATE TYPE' Option Filed 'IB REPOST' Option Filed

'IB RETURN BILL' Option Filed

'IB RETURN BILL LIST' Option Filed 'IB RETURN BILL MENU' Option Filed 'IB REV CODE TOTALS' Option Filed 'IB RX ADD THRESHOLDS' Option Filed 'IB RX EDIT LETTER' Option Filed 'IB RX EXEMPTION MENU' Option Filed 'IB RX HARDSHIP' Option Filed

'IB RX INQUIRE' Option Filed

'IB RX PRINT EX LETERS' Option Filed 'IB RX PRINT PAT. EXEMP.' Option Filed

'IB RX PRINT RETRO CHARGES' Option Filed 'IB RX PRINT THRESHOLDS' Option Filed 'IB RX PRINT VERIFY EXEMP' Option Filed 'IB SITE DEVICE SETUP' Option Filed

'IB SITE MGR MENU' Option Filed

'IB SITE STATUS DISPLAY' Option Filed 'IB SYSTEM DEFINITION MENU' Option Filed

'IB THIRD PARTY BILLING MENU' Option Filed 'IB THIRD PARTY OUTPUT MENU' Option Filed 'IB UB-82 TEST PATTERN PRINT' Option Filed 'IB UB-92 TEST PATTERN PRINT' Option Filed 'IBCN INSURANCE CO EDIT' Option Filed 'IBCN INSURANCE MGMT MENU' Option Filed

'IBCN LIST INACTIVE INS W/PAT' Option Filed 'IBCN LIST NEW NOT VER' Option Filed

'IBCN PATIENT INSURANCE' Option Filed 'IBCN VIEW INSURANCE CO' Option Filed 'IBCN VIEW INSURANCE DATA' Option Filed 'IBCN VIEW PATIENT INSURANCE' Option Filed

'IBDF CLINIC SETUP/EDIT FORMS' Option Filed 'IBDF COPY CPTS TO FORM' Option Filed

'IBDF DEFINE AVAILABLE REPORT' Option Filed 'IBDF DEFINE AVLABLE HLTH SMRY' Option Filed 'IBDF EDIT CLINIC REPORTS' Option Filed 'IBDF EDIT DIVISION REPORTS' Option Filed 'IBDF EDIT ENCOUNTER FORMS' Option Filed 'IBDF EDIT MARKING AREA' Option Filed

'IBDF EDIT PACKAGE INTERFACE' Option Filed

'IBDF EDIT TOOL KIT' Option Filed

'IBDF EDIT TOOL KIT BLOCKS' Option Filed 'IBDF EDIT TOOL KIT FORMS' Option Filed 'IBDF ENCOUNTER FORM' Option Filed

'IBDF IMPORT/EXPORT UTILITY' Option Filed

'IBDF IRM OPTIONS' Option Filed

'IBDF LIST CLINICS USING FORMS' Option Filed 'IBDF MISCELLANEOUS CLEANUP' Option Filed

Sample Installation

'IBDF PRINT BLNK ENCOUNTER FORM' Option Filed 'IBDF PRINT ENCOUNTER FORMS' Option Filed

'IBDF PRINT MANAGER' Option Filed 'IBDF PRINT OPTIONS' Option Filed

'IBDF PRNT FORM W/DATA NO APPT.' Option Filed 'IBDF REPORT CLINIC SETUPS' Option Filed

'IBT EDIT APPEALS/DENIALS' Option Filed 'IBT EDIT BI TRACKING ENTRY' Option Filed 'IBT EDIT COMMUNICATIONS' Option Filed 'IBT EDIT HR REVIEWS TO DO' Option Filed 'IBT EDIT HR TRACKING ENTRY' Option Filed 'IBT EDIT IR REVIEWS TO DO' Option Filed 'IBT EDIT IR TRACKING ENTRY' Option Filed

'IBT EDIT REASON NOT BILLABLE' Option Filed

'IBT EDIT REVIEWS' Option Filed

'IBT EDIT REVIEWS TO DO' Option Filed 'IBT EDIT TRACKING ENTRY' Option Filed

'IBT EDIT TRACKING PARAMETERS' Option Filed

'IBT MANAGER MENU' Option Filed

'IBT OUTPUT BILLING SHEET' Option Filed 'IBT OUTPUT CLAIM INQUIRY' Option Filed

'IBT OUTPUT DENIED DAYS REPORT' Option Filed 'IBT OUTPUT LIST VISITS' Option Filed

'IBT OUTPUT MCCR/UR SUMMARY' Option Filed

'IBT OUTPUT MENU' Option Filed

'IBT OUTPUT ONE ADMISSION SHEET' Option Filed 'IBT OUTPUT PENDING ITEMS' Option Filed

'IBT OUTPUT REVIEW WORKSHEET' Option Filed 'IBT OUTPUT SCHED ADM W/INS' Option Filed 'IBT OUTPUT UNSCHE ADM W/INS' Option Filed 'IBT OUTPUT UR ACTIVITY REPORT' Option Filed 'IBT SUP MANUALLY QUE ENCTRS' Option Filed 'IBT SUP MANUALLY QUE RX FILLS' Option Filed 'IBT SUPERVISORS MENU' Option Filed

'IBT USER COMBINED MCCR/UR MENU' Option Filed

'IBT USER MENU (BI)' Option Filed 'IBT USER MENU (HR)' Option Filed

'IBT USER MENU (IR)' Option Filed.............................................

..............................................................................

.....

Compiling IB CURRENT STATUS input template of File 354...

'IBXEXS' ROUTINE FILED

Compiling IB EDIT MCCR PARM input template of File 350.9.............

'IBXPAR' ROUTINE FILED...............

'IBXPAR1' ROUTINE FILED.........

'IBXPAR2' ROUTINE FILED

Compiling IB INACTIVATE EXEMPTION input template of File 354.1.. 'IBXEXI' ROUTINE FILED

Compiling IB NEW EXEMPTION input template of File 354.1...

'IBXEX' ROUTINE FILED.......

'IBXEX1' ROUTINE FILED

Sample Installation

Compiling IB SCREEN1 input template of File 399.. 'IBXSC1' ROUTINE FILED.....

'IBXSC11' ROUTINE FILED...

'IBXSC13' ROUTINE FILED.....

'IBXSC14' ROUTINE FILED.....

'IBXSC15' ROUTINE FILED......

'IBXSC16' ROUTINE FILED.. 'IBXSC12' ROUTINE FILED

Compiling IB SCREEN2 input template of File 399 'IBXSC2' ROUTINE FILED.....

'IBXSC21' ROUTINE FILED........

'IBXSC22' ROUTINE FILED.....

'IBXSC23' ROUTINE FILED

Compiling IB SCREEN3 input template of File 399...

'IBXSC3' ROUTINE FILED...

'IBXSC31' ROUTINE FILED..........

'IBXSC32' ROUTINE FILED

Compiling IB SCREEN4 input template of File 399.....

'IBXSC4' ROUTINE FILED...

'IBXSC42' ROUTINE FILED....

'IBXSC41' ROUTINE FILED. 'IBXSC43' ROUTINE FILED.. 'IBXSC44' ROUTINE FILED

Compiling IB SCREEN5 input template of File 399...

'IBXSC5' ROUTINE FILED...

'IBXSC53' ROUTINE FILED. 'IBXSC51' ROUTINE FILED....

'IBXSC52' ROUTINE FILED. 'IBXSC54' ROUTINE FILED.. 'IBXSC55' ROUTINE FILED

Compiling IB SCREEN6 input template of File 399........

'IBXSC6' ROUTINE FILED.....

'IBXSC61' ROUTINE FILED.. 'IBXSC63' ROUTINE FILED......

'IBXSC62' ROUTINE FILED. 'IBXSC64' ROUTINE FILED

Compiling IB SCREEN7 input template of File 399.......

'IBXSC7' ROUTINE FILED.....

'IBXSC72' ROUTINE FILED.. 'IBXSC74' ROUTINE FILED. 'IBXSC71' ROUTINE FILED......

'IBXSC73' ROUTINE FILED. 'IBXSC75' ROUTINE FILED

Compiling IB SCREEN8 input template of File 399........

'IBXSC8' ROUTINE FILED

Sample Installation

Compiling IB SCREEN82 input template of File 399...........

'IBXSC82' ROUTINE FILED...

'IBXSC821' ROUTINE FILED

Compiling IB SCREEN8H input template of File 399....

'IBXSC8H' ROUTINE FILED

Compiling IB STATUS input template of File 399...

'IBXST' ROUTINE FILED. 'IBXST2' ROUTINE FILED. 'IBXST1' ROUTINE FILED

Compiling IBDF EDIT DATA FIELD input template of File 357.5.......

'IBXFI5' ROUTINE FILED......

'IBXFI51' ROUTINE FILED......

'IBXFI52' ROUTINE FILED...

'IBXFI53' ROUTINE FILED

Compiling IB BILLING CLOCK HEADER print template of File 351........

'IBXBCR2' ROUTINE FILED...

Compiling IB BILLING CLOCK INQ print template of File 351.....................

.......

'IBXBCR' ROUTINE FILED..........

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 30%" />
<col style="width: 11%" />
<col style="width: 3%" />
<col style="width: 6%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th>Compiling 'IBXCPTC'</th>
<th>IB CPT CP DISPLAY print ROUTINE FILED......</th>
<th>template</th>
<th>of</th>
<th>File</th>
<th>350.71....................</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p>Compiling</p>
<p>.. 'IBXCPTG'</p></td>
<td>IB CPT PG DISPLAY print ROUTINE FILED......</td>
<td>template</td>
<td>of</td>
<td>File</td>
<td>350.7......................</td>
</tr>
<tr class="even">
<td><p>Compiling</p>
<p>......</p>
<p>'IBXCPTR'</p></td>
<td>IB CPT RG DISPLAY print ROUTINE FILED.........</td>
<td>template</td>
<td>of</td>
<td>File</td>
<td>409.71.....................</td>
</tr>
</tbody>
</table>

Compiling IB DIVISION DISPLAY print template of File 40.8......................

'IBXDIVD' ROUTINE FILED.....

NOTE THAT FILE SECURITY-CODE PROTECTION HAS BEEN MADE

\>\>\> Cleaning up dangling nodes in the IB ACTION CHARGE (#350.2) file...

\>\>\> Initializing the DEFAULT FORM TYPE, if necessary...

\>\>\> Populating the IB ACTION (#350.21) file...

\>\>\> Updating the BASC start date to 10/1/99...

Sample Installation

\>\>\> Updating the Eligibility logic for SC veterans for Pharmacy copay...

\>\>\> Updating the cancellation reason MT CHARGE EDITED in file \#350.3 ...

\>\>\> Updating the central collection mailgroup to REDACTED...

\>\>\> Updating the Form Types in \#353...

\>\>\> Initializing the AUTO BILLER PARAMETERS ...

\>\>\> Adding UB-92 form type to the Form Type (#353) file.

\>\>\> Adding Addendum form type to the Form Type (#353) file.

\>\>\> Flagging Telephone stop codes as non-billable for Means Test Billing...

> Flagged stop code 'TELEPHONE TRIAGE' as non-billable... Flagged stop code 'TELEPHONE/MEDICINE' as non-billable... Flagged stop code 'TELEPHONE/SURGERY' as non-billable...

> Flagged stop code 'TELEPHONE/SPECIAL PSYCHIATRY' as non-billable... Flagged stop code 'TELEPHONE/GENERAL PSYCHIATRY' as non-billable... Flagged stop code 'TELEPHONE/PTSD' as non-billable...

> Flagged stop code 'TELEPHONE/ALCOHOL DEPENDENCE' as non-billable... Flagged stop code 'TELEPHONE/DRUG DEPENDENCE' as non-billable...

> Flagged stop code 'TELEPHONE/SUBSTANCE ABUSE' as non-billable... Flagged stop code 'TELEPHONE/ANCILLARY' as non-billable...

> Flagged stop code 'TELEPHONE/REHAB AND SUPPORT' as non-billable... Flagged stop code 'TELEPHONE/DIAGNOSTIC' as non-billable...

> Flagged stop code 'TELEPHONE/PROSTHETICS/ORTHOTIC' as non-billable... Flagged stop code 'TELEPHONE/DENTAL' as non-billable...

> Flagged stop code 'TELEPHONE/DIALYSIS' as non-billable...

\>\>\> Examining all charges 'on hold' in File \#350...

> \>\> 1 held charge was updated to cancelled.

> \>\> 66 held charges were re-indexed.

\>\>\> Adding new IB Action Types into file \#350.1...

> \>\> 'CHAMPVA SUBSISTENCE LIMIT' has been filed...

> \>\> 'DG CHAMPVA PER DIEM NEW' has been filed...

> \>\> 'DG CHAMPVA PER DIEM CANCEL' has been filed...

> \>\> 'DG CHAMPVA PER DIEM UPDATE' has been filed...

\>\>\> Adding new IB Action Charges into file \#350.2...

> \>\> 'CHAMPVA SUBSISTENCE LIMIT' has been filed...

> \>\> 'CHAMPVA PER DIEM' has been filed...

> \>\> 'CHAMPVA PER DIEM' has been filed...

\>\>\> Updating pointers to file \#49 from file \#350.1... ....

\>\>\> Updating pointers to file \#350.1 from file \#350.2 ... ...

\>\>\> Updating pointers to file \#350.1 from file \#350.1... ....

This version of 'IBONIT' was created on 21-MAR-1994

> (at ALBANY ISC VAX DEVELOPMENT, by OE/RR V.2.5)

Sample Installation

> PROTOCOL INSTALLATION

...OK, this may take a while, hold on please..................................

...........................

> Located in the IB (INTEGRATED BILLING) namespace.. You may see this dis­ Located in the IB (INTEGRATED BILLING) namespace.. played numerous times Located in the IB (INTEGRATED BILLING) namespace.. depending on the ver-

> 'IB CATEGORY C BILLING' Protocol Filed sion of Order Entry you

> 'IB EXEMPTION EVENTS' Protocol Filed are running.

'IB MEANS TEST EVENT' Protocol Filed 'IBACM ADD CHARGE' Protocol Filed

IBACM ADD CHARGE added as item to IBACM1 MENU. 'IBACM ADD CHARGE ONE' Protocol Filed

'IBACM CANCEL CHARGE' Protocol Filed

IBACM CANCEL CHARGE added as item to IBACM1 MENU. 'IBACM CANCEL CHARGE ONE' Protocol Filed

'IBACM OP LINK' Protocol Filed 'IBACM PASS CHARGE' Protocol Filed

IBACM PASS CHARGE added as item to IBACM1 MENU. 'IBACM PATIENT CHANGE' Protocol Filed

IBACM PATIENT CHANGE added as item to IBACM1 MENU. 'IBACM UPDATE CHARGE' Protocol Filed

IBACM UPDATE CHARGE added as item to IBACM1 MENU. 'IBACM UPDATE CHARGE ONE' Protocol Filed

'IBACM UPDATE EVENT' Protocol Filed 'IBACM1 DATE CHANGE' Protocol Filed

IBACM1 DATE CHANGE added as item to IBACM1 MENU. 'IBACM1 MENU' Protocol Filed

IBACM UPDATE EVENT added as item to IBACM1 MENU. 'IBACME CHANGE STATUS' Protocol Filed

'IBACME EVENT MENU' Protocol Filed

> IBACME CHANGE STATUS added as item to IBACME EVENT MENU.

IBACME LAST CALC added as item to IBACME EVENT MENU. 'IBACME LAST CALC' Protocol Filed

'IBCN INSURANCE BULLETIN' Protocol Filed 'IBCN NEW INSURANCE EVENTS' Protocol Filed

> IBCN INSURANCE BULLETIN added as item to IBCN NEW INSURANCE EVENTS.

'IBCNMS VIEW ALL DATA' Protocol Filed 'IBCNS EXIT' Protocol Filed

'IBCNS QUIT' Protocol Filed

'IBCNSA AN BEN ADD COM' Protocol Filed 'IBCNSA AN BEN CH YR' Protocol Filed 'IBCNSA AN BEN ED ALL' Protocol Filed 'IBCNSA AN BEN HOME HEA' Protocol Filed 'IBCNSA AN BEN HOSPC' Protocol Filed 'IBCNSA AN BEN INPT' Protocol Filed 'IBCNSA AN BEN IV MGMT' Protocol Filed 'IBCNSA AN BEN MEN H' Protocol Filed 'IBCNSA AN BEN OPT' Protocol Filed 'IBCNSA AN BEN POL INF' Protocol Filed 'IBCNSA AN BEN REHAB' Protocol Filed 'IBCNSA AN BEN USER INF' Protocol Filed 'IBCNSA ANNUAL BENEFITS' Protocol Filed

> IBCNSA AN BEN POL INF added as item to IBCNSA ANNUAL BENEFITS. IBCNSA AN BEN OPT added as item to IBCNSA ANNUAL BENEFITS. IBCNSA AN BEN INPT added as item to IBCNSA ANNUAL BENEFITS. IBCNSA AN BEN MEN H added as item to IBCNSA ANNUAL BENEFITS. IBCNSA AN BEN HOME HEA added as item to IBCNSA ANNUAL BENEFITS. IBCNSA AN BEN HOSPC added as item to IBCNSA ANNUAL BENEFITS.

Sample Installation

> IBCNSA AN BEN ED ALL added as item to IBCNSA ANNUAL BENEFITS. IBCNSA AN BEN CH YR added as item to IBCNSA ANNUAL BENEFITS.

> IBCNS EXIT added as item to IBCNSA ANNUAL BENEFITS.

> IBCNSA AN BEN REHAB added as item to IBCNSA ANNUAL BENEFITS. IBCNSA AN BEN IV MGMT added as item to IBCNSA ANNUAL BENEFITS.

'IBCNSC INS CO (IN)ACTIVATE COMPANY' Protocol Filed 'IBCNSC INS CO APPEALS OFFICE' Protocol Filed 'IBCNSC INS CO BILLING PARAMETERS' Protocol Filed 'IBCNSC INS CO CHANGE COMPANY' Protocol Filed

'IBCNSC INS CO EDIT ALL' Protocol Filed 'IBCNSC INS CO INPT CLAIMS' Protocol Filed 'IBCNSC INS CO INQUIRY OFFICE' Protocol Filed

'IBCNSC INS CO MAIN MAILING ADDRESS' Protocol Filed

'IBCNSC INS CO OPT CLAIMS' Protocol Filed 'IBCNSC INS CO REMARKS' Protocol Filed 'IBCNSC INS CO RX CLAIMS' Protocol Filed 'IBCNSC INS CO SYNONYMS' Protocol Filed 'IBCNSC INS CO TELEPHONE' Protocol Filed 'IBCNSC INSURANCE CO' Protocol Filed

> IBCNSC INS CO EDIT ALL added as item to IBCNSC INSURANCE CO. IBCNSC INS CO APPEALS OFFICE added as item to IBCNSC INSURANCE CO. IBCNSC INS CO INQUIRY OFFICE added as item to IBCNSC INSURANCE CO.

> IBCNSC INS CO MAIN MAILING ADDRESS added as item to IBCNSC INSURANCE CO. IBCNSC INS CO BILLING PARAMETERS added as item to IBCNSC INSURANCE CO. IBCNSC INS CO CHANGE COMPANY added as item to IBCNSC INSURANCE CO. IBCNSC INS CO REMARKS added as item to IBCNSC INSURANCE CO.

> IBCNSC INS CO SYNONYMS added as item to IBCNSC INSURANCE CO.

> IBCNSC INS CO (IN)ACTIVATE COMPANY added as item to IBCNSC INSURANCE CO. IBCNSC INS CO INPT CLAIMS added as item to IBCNSC INSURANCE CO.

> IBCNSC INS CO OPT CLAIMS added as item to IBCNSC INSURANCE CO. IBCNSC INS CO RX CLAIMS added as item to IBCNSC INSURANCE CO.

IBCNS QUIT added as item to IBCNSC INSURANCE CO. 'IBCNSD B USED ADD COM' Protocol Filed

'IBCNSD B USED CH YR' Protocol Filed 'IBCNSD B USED ED AL' Protocol Filed 'IBCNSD B USED INPT DED' Protocol Filed

> IBCNSD B USED ADD COM added as item to IBCNSD B USED INPT DED.

'IBCNSD B USED OPT DED' Protocol Filed 'IBCNSD B USED POL INF' Protocol Filed 'IBCNSD BENEFITS USED BY DATE' Protocol Filed

> IBCNSD B USED POL INF added as item to IBCNSD BENEFITS USED BY DATE. IBCNSD B USED OPT DED added as item to IBCNSD BENEFITS USED BY DATE. IBCNSD B USED INPT DED added as item to IBCNSD BENEFITS USED BY DATE. IBCNSD B USED ADD COM added as item to IBCNSD BENEFITS USED BY DATE. IBCNSD B USED CH YR added as item to IBCNSD BENEFITS USED BY DATE. IBCNSD B USED ED AL added as item to IBCNSD BENEFITS USED BY DATE. IBCNS EXIT added as item to IBCNSD BENEFITS USED BY DATE.

'IBCNSM INSURANCE MANAGEMENT' Protocol Filed

> IBCNSM CHANGE PATIENT added as item to IBCNSM INSURANCE MANAGEMENT. IBCNSM VIEW PAT POLICY added as item to IBCNSM INSURANCE MANAGEMENT. IBCNSM BENEFITS USED added as item to IBCNSM INSURANCE MANAGEMENT. IBCNSM ADD POLICY added as item to IBCNSM INSURANCE MANAGEMENT.

> IBCNSM UPDATE ANNUAL BENEFITS added as item to IBCNSM INSURANCE MANAGEMENT. IBCNSM UPDATE INS CO. added as item to IBCNSM INSURANCE MANAGEMENT.

> IBCNSM PRINT WORKSHEET added as item to IBCNSM INSURANCE MANAGEMENT. IBCNSM PRINT PATIENT INS added as item to IBCNSM INSURANCE MANAGEMENT. IBCNSM VERIFY INS added as item to IBCNSM INSURANCE MANAGEMENT.

> IBCNSM DELETE POLICY added as item to IBCNSM INSURANCE MANAGEMENT. IBCNSM EDIT ALL added as item to IBCNSM INSURANCE MANAGEMENT.

Sample Installation

> IBCNSM PERSONAL RIDERS added as item to IBCNSM INSURANCE MANAGEMENT.

'IBCNSM ADD POLICY' Protocol Filed 'IBCNSM BENEFITS USED' Protocol Filed 'IBCNSM CHANGE PATIENT' Protocol Filed 'IBCNSM DELETE POLICY' Protocol Filed 'IBCNSM EDIT ALL' Protocol Filed

'IBCNSM PATIENT INSURANCE' Protocol Filed

> IBCNSM CHANGE PATIENT added as item to IBCNSM PATIENT INSURANCE. IBCNSM VIEW PAT POLICY added as item to IBCNSM PATIENT INSURANCE. IBCNSM BENEFITS USED added as item to IBCNSM PATIENT INSURANCE. IBCNSM ADD POLICY added as item to IBCNSM PATIENT INSURANCE.

> IBCNSM UPDATE ANNUAL BENEFITS added as item to IBCNSM PATIENT INSURANCE. IBCNSM PRINT WORKSHEET added as item to IBCNSM PATIENT INSURANCE.

> IBCNSM PRINT PATIENT INS added as item to IBCNSM PATIENT INSURANCE. IBCNSM DELETE POLICY added as item to IBCNSM PATIENT INSURANCE. IBCNSM EDIT ALL added as item to IBCNSM PATIENT INSURANCE.

> IBCNSM VERIFY INS added as item to IBCNSM PATIENT INSURANCE. IBCNSM PERSONAL RIDERS added as item to IBCNSM PATIENT INSURANCE. IBCNS QUIT added as item to IBCNSM PATIENT INSURANCE.

'IBCNSM PERSONAL RIDERS' Protocol Filed 'IBCNSM PRINT PATIENT INS' Protocol Filed 'IBCNSM PRINT WORKSHEET' Protocol Filed 'IBCNSM UPDATE ANNUAL BENEFITS' Protocol Filed 'IBCNSM UPDATE INS BENEFITS' Protocol Filed

'IBCNSM UPDATE INS CO.' Protocol Filed 'IBCNSM UPDATE POLICY' Protocol Filed 'IBCNSM VERIFY INS' Protocol Filed 'IBCNSM VIEW BENEFITS' Protocol Filed 'IBCNSM VIEW INS CO' Protocol Filed 'IBCNSM VIEW NAT INS CO' Protocol Filed 'IBCNSM VIEW PAT POLICY' Protocol Filed 'IBCNSP ADD COMMENT' Protocol Filed 'IBCNSP ANNUAL BENEFITS' Protocol Filed 'IBCNSP BENEFITS USED' Protocol Filed 'IBCNSP EDIT ALL' Protocol Filed

'IBCNSP EDIT EFFECTIVE DATES' Protocol Filed

'IBCNSP EDIT POLICY INFO' Protocol Filed

'IBCNSP EMPLOYER INFO FOR CLAIMS' Protocol Filed 'IBCNSP INSURANCE CONTACT INF' Protocol Filed

'IBCNSP PERSONAL RIDERS' Protocol Filed 'IBCNSP POLICY MENU' Protocol Filed

> IBCNSP EDIT POLICY INFO added as item to IBCNSP POLICY MENU. IBCNSP EDIT EFFECTIVE DATES added as item to IBCNSP POLICY MENU. IBCNSP VERIFY COVERAGE added as item to IBCNSP POLICY MENU. IBCNSP SUBSCRIBER UPDATE added as item to IBCNSP POLICY MENU.

> IBCNSP EMPLOYER INFO FOR CLAIMS added as item to IBCNSP POLICY MENU. IBCNSP ADD COMMENT added as item to IBCNSP POLICY MENU.

> IBCNSP UR INFO added as item to IBCNSP POLICY MENU.

> IBCNSP ANNUAL BENEFITS added as item to IBCNSP POLICY MENU. IBCNSP BENEFITS USED added as item to IBCNSP POLICY MENU.

> IBCNSP EDIT ALL added as item to IBCNSP POLICY MENU. IBCNS EXIT added as item to IBCNSP POLICY MENU.

IBCNSP INSURANCE CONTACT INF added as item to IBCNSP POLICY MENU. 'IBCNSP SUBSCRIBER UPDATE' Protocol Filed

'IBCNSP UR INFO' Protocol Filed

'IBCNSP VERIFY COVERAGE' Protocol Filed 'IBCNSV ANNUAL BENEFITS' Protocol Filed

> IBCNSA AN BEN CH YR added as item to IBCNSV ANNUAL BENEFITS.

> IBCNS EXIT added as item to IBCNSV ANNUAL BENEFITS.

Sample Installation

'IBCNSV BENEFITS USED BY DATE' Protocol Filed

> IBCNSD B USED CH YR added as item to IBCNSV BENEFITS USED BY DATE. IBCNS EXIT added as item to IBCNSV BENEFITS USED BY DATE.

'IBCNSV INSURANCE CO' Protocol Filed

> IBCNSC INS CO CHANGE COMPANY added as item to IBCNSV INSURANCE CO.

IBCNS QUIT added as item to IBCNSV INSURANCE CO. 'IBCNSV PATIENT INSURANCE' Protocol Filed

> IBCNSM CHANGE PATIENT added as item to IBCNSV PATIENT INSURANCE. IBCNSV VIEW AN BEN added as item to IBCNSV PATIENT INSURANCE. IBCNSV VIEW EXP POL added as item to IBCNSV PATIENT INSURANCE. IBCNSV VIEW BEN USED added as item to IBCNSV PATIENT INSURANCE. IBCNS QUIT added as item to IBCNSV PATIENT INSURANCE.

'IBCNSV POLICY MENU' Protocol Filed

IBCNS EXIT added as item to IBCNSV POLICY MENU. 'IBCNSV VIEW AN BEN' Protocol Filed

'IBCNSV VIEW BEN USED' Protocol Filed 'IBCNSV VIEW EXP POL' Protocol Filed

'IBDE ADD BLOCK TO IMP/EXP WS' Protocol Filed 'IBDE ADD FORM TO IMP/EXP WS' Protocol Filed

'IBDE DELETE FORM FROM IMP/EXP FILES' Protocol Filed

'IBDE DELETE IMP/EXP FILES' Protocol Filed

'IBDE DELTE TK BLOCK FROM IMP/EXP FILES' Protocol Filed

'IBDE DISPLAY TK BLOCKS' Protocol Filed

'IBDE EDIT BLOCK'S IMP/EXP NOTES' Protocol Filed 'IBDE EDIT FORM'S IMP/EXP NOTES' Protocol Filed

'IBDE EXECUTE DIFROM' Protocol Filed 'IBDE EXECUTE INITS' Protocol Filed 'IBDE IMP/EXP HELP' Protocol Filed

'IBDE IMP/EXP MENU FOR BLOCKS' Protocol Filed

> IBDE DELETE IMP/EXP FILES added as item to IBDE IMP/EXP MENU FOR BLOCKS. IBDE IMP/EXP HELP added as item to IBDE IMP/EXP MENU FOR BLOCKS.

> IBDE EXECUTE DIFROM added as item to IBDE IMP/EXP MENU FOR BLOCKS. IBDE EXECUTE INITS added as item to IBDE IMP/EXP MENU FOR BLOCKS.

> IBDE DELTE TK BLOCK FROM IMP/EXP FILES added as item to IBDE IMP/EXP MENU FOR BLOCKS.

> IBDE ADD BLOCK TO IMP/EXP WS added as item to IBDE IMP/EXP MENU FOR BLOCKS. IBDE EDIT BLOCK'S IMP/EXP NOTES added as item to IBDE IMP/EXP MENU FOR BLOCKS.

> IBDE VIEW BLOCK'S IMP/EXP NOTES added as item to IBDE IMP/EXP MENU FOR BLOCKS.

> IBDE IMPORT TK BLOCK added as item to IBDE IMP/EXP MENU FOR BLOCKS.

IBDF QUIT added as item to IBDE IMP/EXP MENU FOR BLOCKS. 'IBDE IMP/EXP MENU FOR FORMS' Protocol Filed

> IBDE ADD FORM TO IMP/EXP WS added as item to IBDE IMP/EXP MENU FOR FORMS. IBDE DELETE FORM FROM IMP/EXP FILES added as item to IBDE IMP/EXP MENU FOR FORMS.

> IBDE DELETE IMP/EXP FILES added as item to IBDE IMP/EXP MENU FOR FORMS.

> IBDE EDIT FORM'S IMP/EXP NOTES added as item to IBDE IMP/EXP MENU FOR FORMS. IBDE VIEW FORM'S IMP/EXP NOTES added as item to IBDE IMP/EXP MENU FOR FORMS. IBDE IMPORT FORM added as item to IBDE IMP/EXP MENU FOR FORMS.

> IBDE IMP/EXP HELP added as item to IBDE IMP/EXP MENU FOR FORMS. IBDE EXECUTE DIFROM added as item to IBDE IMP/EXP MENU FOR FORMS. IBDE EXECUTE INITS added as item to IBDE IMP/EXP MENU FOR FORMS.

> IBDE DISPLAY TK BLOCKS added as item to IBDE IMP/EXP MENU FOR FORMS.

'IBDE IMPORT FORM' Protocol Filed 'IBDE IMPORT TK BLOCK' Protocol Filed

'IBDE VIEW BLOCK'S IMP/EXP NOTES' Protocol Filed 'IBDE VIEW FORM'S IMP/EXP NOTES' Protocol Filed

'IBDF ADD BLANK GROUP' Protocol Filed

Sample Installation

'IBDF ADD BLANK SELECTION' Protocol Filed 'IBDF ADD GROUP' Protocol Filed

'IBDF ADD SELECTION' Protocol Filed

'IBDF ADD TO CLINIC SETUP' Protocol Filed 'IBDF CHANGE BLOCK TK ORDER' Protocol Filed

'IBDF CHANGE CLINIC' Protocol Filed

'IBDF CLINIC'S FORMS MENU' Protocol Filed

> IBDF EDIT FORM added as item to IBDF CLINIC'S FORMS MENU.

> IBDF CREATE BLANK FORM added as item to IBDF CLINIC'S FORMS MENU. IBDF COPY FORM added as item to IBDF CLINIC'S FORMS MENU.

> IBDF ADD TO CLINIC SETUP added as item to IBDF CLINIC'S FORMS MENU.

> IBDF DELETE FROM CLINIC SETUP added as item to IBDF CLINIC'S FORMS MENU. IBDF PRINT SAMPLE FORM added as item to IBDF CLINIC'S FORMS MENU.

> IBDF DELETE FORM added as item to IBDF CLINIC'S FORMS MENU. IBDF CHANGE CLINIC added as item to IBDF CLINIC'S FORMS MENU.

> IBDF EDIT FORM NAME/DESCR/SIZE added as item to IBDF CLINIC'S FORMS MENU.

> IBDF QUIT added as item to IBDF CLINIC'S FORMS MENU.

> IBDF COMPILE FORM added as item to IBDF CLINIC'S FORMS MENU.

'IBDF COMPILE FORM' Protocol Filed

'IBDF COPY BLOCK INTO TOOL KIT' Protocol Filed

'IBDF COPY FORM' Protocol Filed

'IBDF COPY FORM BLOCK' Protocol Filed 'IBDF CREATE BLANK FORM' Protocol Filed 'IBDF CREATE EMPTY BLOCK' Protocol Filed 'IBDF DATA FIELD' Protocol Filed

'IBDF DELETE A BLOCK' Protocol Filed 'IBDF DELETE FORM' Protocol Filed

'IBDF DELETE FROM CLINIC SETUP' Protocol Filed

'IBDF DELETE GROUP' Protocol Filed 'IBDF DELETE SELECTION' Protocol Filed

'IBDF DELETE TOOL KIT BLOCK' Protocol Filed

'IBDF DELETE TOOL KIT FORM' Protocol Filed

'IBDF DISPLAY FORM BLOCK FOR EDIT' Protocol Filed 'IBDF DISPLAY GRP'S SLCTNS FOR EDIT' Protocol Filed

'IBDF DISPLAY TOOL KIT BLOCKS FOR ADDING' Protocol Filed

'IBDF EDIT FORM' Protocol Filed

'IBDF EDIT FORM BLOCK MENU' Protocol Filed

> IBDF SELECTION LIST added as item to IBDF EDIT FORM BLOCK MENU.

> IBDF RESIZE BLOCK (WHILE EDITING BLOCK) added as item to IBDF EDIT FORM BLOCK MENU.

> IBDF EDIT NAME,HEADER,OUTLINE added as item to IBDF EDIT FORM BLOCK MENU. IBDF DATA FIELD added as item to IBDF EDIT FORM BLOCK MENU.

> IBDF STRAIGHT LINE added as item to IBDF EDIT FORM BLOCK MENU.

> IBDF EXIT added as item to IBDF EDIT FORM BLOCK MENU.

> IBDF TEXT AREA added as item to IBDF EDIT FORM BLOCK MENU.

> IBDF SHIFT BLOCK CONTENTS added as item to IBDF EDIT FORM BLOCK MENU.

> IBDF SAVE/DISCARD BLOCK CHANGES added as item to IBDF EDIT FORM BLOCK MENU.

'IBDF EDIT FORM NAME/DESCR/SIZE' Protocol Filed 'IBDF EDIT GROUP HDR/ORDER' Protocol Filed

'IBDF EDIT GROUP'S SELECTIONS MENU' Protocol Filed

> IBDF ADD SELECTION added as item to IBDF EDIT GROUP'S SELECTIONS MENU. IBDF EDIT SELECTION added as item to IBDF EDIT GROUP'S SELECTIONS MENU. IBDF DELETE SELECTION added as item to IBDF EDIT GROUP'S SELECTIONS MENU. IBDF EXIT added as item to IBDF EDIT GROUP'S SELECTIONS MENU.

> IBDF ADD BLANK SELECTION added as item to IBDF EDIT GROUP'S SELECTIONS MENU. IBDF FORMAT GROUP'S SELECTIONS added as item to IBDF EDIT GROUP'S SELECTIONS MENU.

'IBDF EDIT HEADER BLOCK' Protocol Filed

'IBDF EDIT NAME,HEADER,OUTLINE' Protocol Filed

Sample Installation

'IBDF EDIT SELECTION' Protocol Filed

'IBDF EDIT SELECTION LIST MENU' Protocol Filed

> IBDF ADD GROUP added as item to IBDF EDIT SELECTION LIST MENU. IBDF DELETE GROUP added as item to IBDF EDIT SELECTION LIST MENU.

> IBDF EDIT GROUP HDR/ORDER added as item to IBDF EDIT SELECTION LIST MENU. IBDF DISPLAY GRP'S SLCTNS FOR EDIT added as item to IBDF EDIT SELECTION LIST MENU.

> IBDF EXIT added as item to IBDF EDIT SELECTION LIST MENU.

> IBDF ADD BLANK GROUP added as item to IBDF EDIT SELECTION LIST MENU.

> IBDF FORMAT ALL SELECTIONS added as item to IBDF EDIT SELECTION LIST MENU.

'IBDF EDIT TOOL KIT BLOCK' Protocol Filed

'IBDF EDIT TOOL KIT BLOCKS MENU' Protocol Filed

> IBDF EDIT TOOL KIT BLOCK added as item to IBDF EDIT TOOL KIT BLOCKS MENU. IBDF NEW TOOL KIT BLOCK added as item to IBDF EDIT TOOL KIT BLOCKS MENU. IBDF DELETE TOOL KIT BLOCK added as item to IBDF EDIT TOOL KIT BLOCKS MENU. IBDF COPY BLOCK INTO TOOL KIT added as item to IBDF EDIT TOOL KIT BLOCKS MENU.

> IBDF CHANGE BLOCK TK ORDER added as item to IBDF EDIT TOOL KIT BLOCKS MENU.

'IBDF EXIT' Protocol Filed

'IBDF FORMAT ALL SELECTIONS' Protocol Filed 'IBDF FORMAT GROUP'S SELECTIONS' Protocol Filed

'IBDF MENU FOR ADDING TOOL KIT BLOCK' Protocol Filed

> IBDF SELECT TOOL KIT BLOCK added as item to IBDF MENU FOR ADDING TOOL KIT BLOCK.

> IBDF VIEW TOOL KIT BLOCK added as item to IBDF MENU FOR ADDING TOOL KIT BLOCK.

IBDF EXIT added as item to IBDF MENU FOR ADDING TOOL KIT BLOCK. 'IBDF MENU FOR EDITING DISPLAYED FORM' Protocol Filed

> IBDF DISPLAY TOOL KIT BLOCKS FOR ADDING added as item to IBDF MENU FOR EDITING DISPLAYED FORM.

> IBDF MOVE BLOCK added as item to IBDF MENU FOR EDITING DISPLAYED FORM. IBDF RESIZE BLOCK (WHILE EDITING FORM) added as item to IBDF MENU FOR EDITING DISPLAYED FORM.

> IBDF DISPLAY FORM BLOCK FOR EDIT added as item to IBDF MENU FOR EDITING DISPLAYED FORM.

> IBDF DELETE A BLOCK added as item to IBDF MENU FOR EDITING DISPLAYED FORM. IBDF EXIT added as item to IBDF MENU FOR EDITING DISPLAYED FORM.

> IBDF EDIT HEADER BLOCK added as item to IBDF MENU FOR EDITING DISPLAYED FORM.

> IBDF CREATE EMPTY BLOCK added as item to IBDF MENU FOR EDITING DISPLAYED FORM.

> IBDF REDRAW FORM added as item to IBDF MENU FOR EDITING DISPLAYED FORM. IBDF COPY FORM BLOCK added as item to IBDF MENU FOR EDITING DISPLAYED FORM. IBDF SHIFT BLOCKS added as item to IBDF MENU FOR EDITING DISPLAYED FORM. IBDF VIEW FORM W/WO DATA added as item to IBDF MENU FOR EDITING DISPLAYED FORM.

'IBDF MOVE BLOCK' Protocol Filed

'IBDF NEW TOOL KIT BLOCK' Protocol Filed

'IBDF PRINT MANAGER CLINIC SETUP' Protocol Filed

IBDF PRINT MANAGER CLINIC SETUP added as item to SD PARM PARAMETERS MENU. 'IBDF PRINT MANAGER DIVISION SETUP' Protocol Filed

> IBDF PRINT MANAGER DIVISION SETUP added as item to SD PARM PARAMETERS MENU.

'IBDF PRINT SAMPLE FORM' Protocol Filed 'IBDF QUIT' Protocol Filed

'IBDF REDRAW FORM' Protocol Filed

'IBDF RESIZE BLOCK (WHILE EDITING BLOCK)' Protocol Filed 'IBDF RESIZE BLOCK (WHILE EDITING FORM)' Protocol Filed 'IBDF SAVE/DISCARD BLOCK CHANGES' Protocol Filed

'IBDF SELECT TOOL KIT BLOCK' Protocol Filed

Sample Installation

'IBDF SELECTION LIST' Protocol Filed

'IBDF SHIFT BLOCK CONTENTS' Protocol Filed

'IBDF SHIFT BLOCKS' Protocol Filed 'IBDF STRAIGHT LINE' Protocol Filed 'IBDF TEXT AREA' Protocol Filed

'IBDF TOOL KIT FORMS MENU' Protocol Filed

> IBDF EDIT FORM added as item to IBDF TOOL KIT FORMS MENU.

> IBDF CREATE BLANK FORM added as item to IBDF TOOL KIT FORMS MENU. IBDF COPY FORM added as item to IBDF TOOL KIT FORMS MENU.

> IBDF PRINT SAMPLE FORM added as item to IBDF TOOL KIT FORMS MENU.

> IBDF EDIT FORM NAME/DESCR/SIZE added as item to IBDF TOOL KIT FORMS MENU. IBDF DELETE TOOL KIT FORM added as item to IBDF TOOL KIT FORMS MENU.

'IBDF VIEW FORM W/WO DATA' Protocol Filed 'IBDF VIEW TOOL KIT BLOCK' Protocol Filed 'IBTRC MENU' Protocol Filed

> IBTRC ADD INS. ACTION added as item to IBTRC MENU. IBTRC DELETE INS. ACTION added as item to IBTRC MENU.

> IBTRC QUICK EDIT added as item to IBTRC MENU. IBTRC VIEW/EDIT added as item to IBTRC MENU. IBTRC APPEAL/DENIALS added as item to IBTRC MENU. IBTRC ADD COMMENT added as item to IBTRC MENU.

> IBTRC SHOW SC CONDITIONS added as item to IBTRC MENU.

> IBCNS EXIT added as item to IBTRC MENU.

> IBTRC DIAGNOSIS UPDATE added as item to IBTRC MENU. IBTRC PROCEDURE UPDATE added as item to IBTRC MENU. IBTRC PROVIDER UPDATE added as item to IBTRC MENU. IBTRC STATUS CHANGE added as item to IBTRC MENU.

> IBTRC PRINT REV WORKSHEET added as item to IBTRC MENU.

IBTRC CHANGE PATIENT added as item to IBTRC MENU. 'IBTRC ADD COMMENT' Protocol Filed

'IBTRC ADD INS. ACTION' Protocol Filed 'IBTRC APPEAL/DENIALS' Protocol Filed 'IBTRC CHANGE PATIENT' Protocol Filed 'IBTRC DELETE INS. ACTION' Protocol Filed 'IBTRC DIAGNOSIS UPDATE' Protocol Filed 'IBTRC PRINT REV WORKSHEET' Protocol Filed

'IBTRC PROCEDURE UPDATE' Protocol Filed 'IBTRC PROVIDER UPDATE' Protocol Filed 'IBTRC QUICK EDIT' Protocol Filed

'IBTRC SHOW SC CONDITIONS' Protocol Filed 'IBTRC STATUS CHANGE' Protocol Filed 'IBTRC VIEW/EDIT' Protocol Filed

'IBTRCD MENU' Protocol Filed

> IBTRCD APPEAL INFO added as item to IBTRCD MENU. IBTRCD CONTACT INFO added as item to IBTRCD MENU. IBTRCD INSURANCE INFO added as item to IBTRCD MENU. IBTRCD ACTION INFO added as item to IBTRCD MENU. IBTRCD COMMENT INFO added as item to IBTRCD MENU. IBTRCD EDIT PT. INS. added as item to IBTRCD MENU. IBCNS EXIT added as item to IBTRCD MENU.

> IBTRCD DIAGNOSIS UPDATE added as item to IBTRCD MENU. IBTRCD PROCEDURE UPDATE added as item to IBTRCD MENU. IBTRCD PROVIDER UPDATE added as item to IBTRCD MENU.

> IBTRCD STATUS CHANGE added as item to IBTRCD MENU. IBTRC PRINT REV WORKSHEET added as item to IBTRCD MENU.

'IBTRCD ACTION INFO' Protocol Filed 'IBTRCD APPEAL INFO' Protocol Filed 'IBTRCD COMMENT INFO' Protocol Filed 'IBTRCD CONTACT INFO' Protocol Filed

Sample Installation

'IBTRCD DIAGNOSIS UPDATE' Protocol Filed 'IBTRCD EDIT PT. INS.' Protocol Filed 'IBTRCD INSURANCE INFO' Protocol Filed 'IBTRCD PROCEDURE UPDATE' Protocol Filed 'IBTRCD PROVIDER UPDATE' Protocol Filed 'IBTRCD STATUS CHANGE' Protocol Filed 'IBTRD MENU' Protocol Filed

> IBTRD VIEW EDIT DENIAL added as item to IBTRD MENU. IBTRD QUICK EDIT added as item to IBTRD MENU.

> IBTRD ADD APPEAL added as item to IBTRD MENU.

> IBTRD DELETE APPEAL/DENIAL added as item to IBTRD MENU.

> IBTRD PATIENT INS. EDIT added as item to IBTRD MENU. IBTRD VIEW INS. CO added as item to IBTRD MENU.

> IBTRD SHOW SC CONDITIONS added as item to IBTRD MENU.

IBCNS EXIT added as item to IBTRD MENU. 'IBTRD ADD APPEAL' Protocol Filed

'IBTRD DELETE APPEAL/DENIAL' Protocol Filed 'IBTRD PATIENT INS. EDIT' Protocol Filed 'IBTRD QUICK EDIT' Protocol Filed

'IBTRD SHOW SC CONDITIONS' Protocol Filed 'IBTRD VIEW EDIT DENIAL' Protocol Filed 'IBTRD VIEW INS. CO' Protocol Filed 'IBTRDD MENU' Protocol Filed

> IBTRDD ACTION INFO added as item to IBTRDD MENU. IBTRDD APPEAL INFO added as item to IBTRDD MENU. IBTRDD COMMENT INFO added as item to IBTRDD MENU. IBTRDD CONTACT INFO added as item to IBTRDD MENU. IBTRDD EDIT PT. INS. added as item to IBTRDD MENU. IBTRDD INSURANCE INFO added as item to IBTRDD MENU. IBCNS EXIT added as item to IBTRDD MENU.

'IBTRDD ACTION INFO' Protocol Filed 'IBTRDD APPEAL INFO' Protocol Filed 'IBTRDD COMMENT INFO' Protocol Filed 'IBTRDD CONTACT INFO' Protocol Filed 'IBTRDD EDIT PT. INS.' Protocol Filed 'IBTRDD INSURANCE INFO' Protocol Filed 'IBTRE BI MENU' Protocol Filed

> IBTRE CHANGE PATIENT added as item to IBTRE BI MENU. IBTRE VIEW/EDIT TRACKING added as item to IBTRE BI MENU.

> IBTRE CHANGE DATE added as item to IBTRE BI MENU.

> IBTRE SHOW SC CONDITIONS added as item to IBTRE BI MENU.

> IBCNS EXIT added as item to IBTRE BI MENU.

IBTRE BILLING INFO added as item to IBTRE BI MENU. 'IBTRE HR MENU' Protocol Filed

> IBTRE CHANGE PATIENT added as item to IBTRE HR MENU. IBTRE ADD TRACKING added as item to IBTRE HR MENU. IBTRE DELETE TRACKING added as item to IBTRE HR MENU.

> IBTRE QUICK EDIT added as item to IBTRE HR MENU.

> IBTRE VIEW/EDIT TRACKING added as item to IBTRE HR MENU.

> IBTRE EDIT REVIEWS added as item to IBTRE HR MENU. IBTRE CHANGE DATE added as item to IBTRE HR MENU. IBTRE ASSIGN CASE added as item to IBTRE HR MENU.

> IBTRE SHOW SC CONDITIONS added as item to IBTRE HR MENU. IBTRE DIAGNOSIS UPDATE added as item to IBTRE HR MENU.

> IBCNS EXIT added as item to IBTRE HR MENU.

> IBTRE PROCEDURE UPDATE added as item to IBTRE HR MENU. IBTRE PROVIDER UPDATE added as item to IBTRE HR MENU.

'IBTRE IR MENU' Protocol Filed

> IBTRE CHANGE PATIENT added as item to IBTRE IR MENU.

Sample Installation

> IBTRE ADD TRACKING added as item to IBTRE IR MENU. IBTRE DELETE TRACKING added as item to IBTRE IR MENU.

> IBTRE QUICK EDIT added as item to IBTRE IR MENU.

> IBTRE VIEW/EDIT TRACKING added as item to IBTRE IR MENU. IBTRE COMMUNICATIONS EDIT added as item to IBTRE IR MENU.

> IBTRE DENIALS/APPEALS added as item to IBTRE IR MENU. IBTRE CHANGE DATE added as item to IBTRE IR MENU. IBTRE ASSIGN CASE added as item to IBTRE IR MENU.

> IBTRE SHOW SC CONDITIONS added as item to IBTRE IR MENU. IBTRE DIAGNOSIS UPDATE added as item to IBTRE IR MENU.

> IBCNS EXIT added as item to IBTRE IR MENU.

> IBTRE PROCEDURE UPDATE added as item to IBTRE IR MENU. IBTRE PROVIDER UPDATE added as item to IBTRE IR MENU.

IBTRE BILLING INFO added as item to IBTRE IR MENU. 'IBTRE MENU' Protocol Filed

> IBTRE CHANGE PATIENT added as item to IBTRE MENU. IBTRE ADD TRACKING added as item to IBTRE MENU. IBTRE DELETE TRACKING added as item to IBTRE MENU. IBTRE QUICK EDIT added as item to IBTRE MENU.

> IBTRE VIEW/EDIT TRACKING added as item to IBTRE MENU. IBTRE EDIT REVIEWS added as item to IBTRE MENU.

> IBTRE COMMUNICATIONS EDIT added as item to IBTRE MENU.

> IBTRE DENIALS/APPEALS added as item to IBTRE MENU. IBTRE CHANGE DATE added as item to IBTRE MENU. IBTRE ASSIGN CASE added as item to IBTRE MENU.

> IBTRE SHOW SC CONDITIONS added as item to IBTRE MENU.

> IBTRE DIAGNOSIS UPDATE added as item to IBTRE MENU. IBCNS EXIT added as item to IBTRE MENU.

> IBTRE PROCEDURE UPDATE added as item to IBTRE MENU. IBTRE PROVIDER UPDATE added as item to IBTRE MENU. IBTRE BILLING INFO added as item to IBTRE MENU.

'IBTRE ADD TRACKING' Protocol Filed 'IBTRE ASSIGN CASE' Protocol Filed 'IBTRE BILLING INFO' Protocol Filed 'IBTRE CHANGE DATE' Protocol Filed 'IBTRE CHANGE PATIENT' Protocol Filed

'IBTRE COMMUNICATIONS EDIT' Protocol Filed

'IBTRE DELETE TRACKING' Protocol Filed 'IBTRE DENIALS/APPEALS' Protocol Filed 'IBTRE DIAGNOSIS UPDATE' Protocol Filed 'IBTRE EDIT REVIEWS' Protocol Filed 'IBTRE PROCEDURE UPDATE' Protocol Filed 'IBTRE PROVIDER UPDATE' Protocol Filed 'IBTRE QUICK EDIT' Protocol Filed

'IBTRE SHOW SC CONDITIONS' Protocol Filed 'IBTRE VIEW/EDIT TRACKING' Protocol Filed 'IBTRED BI MENU' Protocol Filed

> IBTRED BILLING INFO added as item to IBTRED BI MENU. IBTRED UR INFO added as item to IBTRED BI MENU. IBTRED PRECERT INFO added as item to IBTRED BI MENU. IBCNS EXIT added as item to IBTRED BI MENU.

'IBTRED HR MENU' Protocol Filed

> IBTRED UR INFO added as item to IBTRED HR MENU. IBTRED EDIT REVIEWS added as item to IBTRED HR MENU.

> IBTRED DIAGNOSIS UPDATE added as item to IBTRED HR MENU.

> IBCNS EXIT added as item to IBTRED HR MENU.

> IBTRED PROCEDURE UPDATE added as item to IBTRED HR MENU. IBTRED PROVIDER UPDATE added as item to IBTRED HR MENU.

'IBTRED IR MENU' Protocol Filed

Sample Installation

> IBTRED BILLING INFO added as item to IBTRED IR MENU. IBTRED UR INFO added as item to IBTRED IR MENU. IBTRED PRECERT INFO added as item to IBTRED IR MENU.

> IBTRED COMMUNICATIONS EDIT added as item to IBTRED IR MENU. IBTRED DIAGNOSIS UPDATE added as item to IBTRED IR MENU.

> IBCNS EXIT added as item to IBTRED IR MENU.

> IBTRED PROCEDURE UPDATE added as item to IBTRED IR MENU. IBTRED PROVIDER UPDATE added as item to IBTRED IR MENU.

'IBTRED MENU' Protocol Filed

> IBTRED BILLING INFO added as item to IBTRED MENU. IBTRED UR INFO added as item to IBTRED MENU. IBTRED PRECERT INFO added as item to IBTRED MENU. IBTRED EDIT REVIEWS added as item to IBTRED MENU.

> IBTRED COMMUNICATIONS EDIT added as item to IBTRED MENU. IBTRED DIAGNOSIS UPDATE added as item to IBTRED MENU.

> IBCNS EXIT added as item to IBTRED MENU.

> IBTRED PROCEDURE UPDATE added as item to IBTRED MENU. IBTRED PROVIDER UPDATE added as item to IBTRED MENU.

'IBTRED BILLING INFO' Protocol Filed 'IBTRED COMMUNICATIONS EDIT' Protocol Filed

'IBTRED DIAGNOSIS UPDATE' Protocol Filed 'IBTRED EDIT REVIEWS' Protocol Filed 'IBTRED PRECERT INFO' Protocol Filed 'IBTRED PROCEDURE UPDATE' Protocol Filed 'IBTRED PROVIDER UPDATE' Protocol Filed 'IBTRED UR INFO' Protocol Filed

'IBTRPR HR MENU' Protocol Filed

> IBTRPR CHANGE DATE added as item to IBTRPR HR MENU. IBTRPR QUICK EDIT added as item to IBTRPR HR MENU. IBTRPR VIEW EDIT added as item to IBTRPR HR MENU. IBTRPR UR REVIEW added as item to IBTRPR HR MENU. IBTRPR STATUS CHANGE added as item to IBTRPR HR MENU. IBTRPR CLAIMS TRACKING added as item to IBTRPR HR MENU.

> IBTRPR REMOVE FROM LIST added as item to IBTRPR HR MENU. IBTRPR SHOW SC CONDITIONS added as item to IBTRPR HR MENU. IBTRPR PRINT WORKSHEET added as item to IBTRPR HR MENU. IBTRPR DIAGNOSIS UPDATE added as item to IBTRPR HR MENU. IBTRPR PROCEDURE UPDATE added as item to IBTRPR HR MENU. IBTRPR PROVIDER UPDATE added as item to IBTRPR HR MENU.

'IBTRPR IR MENU' Protocol Filed

> IBTRPR CHANGE DATE added as item to IBTRPR IR MENU. IBTRPR QUICK EDIT added as item to IBTRPR IR MENU. IBTRPR VIEW EDIT added as item to IBTRPR IR MENU.

> IBTRPR INSURANCE ACTIONS added as item to IBTRPR IR MENU. IBTRPR STATUS CHANGE added as item to IBTRPR IR MENU. IBTRPR CLAIMS TRACKING added as item to IBTRPR IR MENU. IBTRPR REMOVE FROM LIST added as item to IBTRPR IR MENU. IBTRPR SHOW SC CONDITIONS added as item to IBTRPR IR MENU. IBTRPR PRINT WORKSHEET added as item to IBTRPR IR MENU. IBTRPR DIAGNOSIS UPDATE added as item to IBTRPR IR MENU. IBTRPR PROCEDURE UPDATE added as item to IBTRPR IR MENU. IBTRPR PROVIDER UPDATE added as item to IBTRPR IR MENU.

'IBTRPR MENU' Protocol Filed

> IBTRPR CHANGE DATE added as item to IBTRPR MENU. IBTRPR QUICK EDIT added as item to IBTRPR MENU. IBTRPR VIEW EDIT added as item to IBTRPR MENU.

> IBTRPR INSURANCE ACTIONS added as item to IBTRPR MENU.

> IBTRPR UR REVIEW added as item to IBTRPR MENU. IBTRPR STATUS CHANGE added as item to IBTRPR MENU.

Sample Installation

> IBTRPR CLAIMS TRACKING added as item to IBTRPR MENU. IBTRPR REMOVE FROM LIST added as item to IBTRPR MENU. IBTRPR SHOW SC CONDITIONS added as item to IBTRPR MENU. IBTRPR PRINT WORKSHEET added as item to IBTRPR MENU. IBTRPR DIAGNOSIS UPDATE added as item to IBTRPR MENU. IBTRPR PROCEDURE UPDATE added as item to IBTRPR MENU. IBTRPR PROVIDER UPDATE added as item to IBTRPR MENU.

'IBTRPR CHANGE DATE' Protocol Filed 'IBTRPR CLAIMS TRACKING' Protocol Filed 'IBTRPR DIAGNOSIS UPDATE' Protocol Filed 'IBTRPR INSURANCE ACTIONS' Protocol Filed

'IBTRPR PRINT WORKSHEET' Protocol Filed 'IBTRPR PROCEDURE UPDATE' Protocol Filed 'IBTRPR PROVIDER UPDATE' Protocol Filed 'IBTRPR QUICK EDIT' Protocol Filed 'IBTRPR REMOVE FROM LIST' Protocol Filed

'IBTRPR SHOW SC CONDITIONS' Protocol Filed

'IBTRPR STATUS CHANGE' Protocol Filed 'IBTRPR UR REVIEW' Protocol Filed 'IBTRPR VIEW EDIT' Protocol Filed 'IBTRV MENU' Protocol Filed

> IBTRV QUICK EDIT added as item to IBTRV MENU. IBTRV DELETE REVIEW added as item to IBTRV MENU. IBTRV EXPAND REVIEW added as item to IBTRV MENU. IBTRV COMPLETE REV added as item to IBTRV MENU. IBTRV DIAGNOSIS added as item to IBTRV MENU. IBCNS EXIT added as item to IBTRV MENU.

> IBTRV PROCEDURE UPDATE added as item to IBTRV MENU. IBTRV PROVIDER UPDATE added as item to IBTRV MENU. IBTRV ADD NEXT REVIEW added as item to IBTRV MENU. IBTRV CHANGE PATIENT added as item to IBTRV MENU.

'IBTRV ADD NEXT REVIEW' Protocol Filed 'IBTRV CHANGE PATIENT' Protocol Filed 'IBTRV COMMUNICATIONS EDIT' Protocol Filed

'IBTRV COMPLETE REV' Protocol Filed 'IBTRV CONT STAY' Protocol Filed 'IBTRV DELETE REVIEW' Protocol Filed 'IBTRV DIAGNOSIS' Protocol Filed

'IBTRV DISCHARGE REVIEW' Protocol Filed 'IBTRV EXPAND REVIEW' Protocol Filed 'IBTRV NEXT REVIEW' Protocol Filed 'IBTRV PRE-CERT' Protocol Filed

'IBTRV PROCEDURE UPDATE' Protocol Filed 'IBTRV PROVIDER UPDATE' Protocol Filed 'IBTRV QUICK EDIT' Protocol Filed

'IBTRV URGENT ADM REVIEW' Protocol Filed 'IBTRVD MENU' Protocol Filed

> IBTRVD STATUS CHANGE added as item to IBTRVD MENU. IBTRVD ADD COMMENTS added as item to IBTRVD MENU. IBTRVD REVIEW INFO added as item to IBTRVD MENU. IBTRVD SPEC UNIT added as item to IBTRVD MENU.

> IBTRVD DIAGNOSIS UPDATE added as item to IBTRVD MENU. IBTRVD REVIEW CRITERIA added as item to IBTRVD MENU.

> IBCNS EXIT added as item to IBTRVD MENU.

> IBTRVD PROCEDURE UPDATE added as item to IBTRVD MENU. IBTRVD PROVIDER UPDATE added as item to IBTRVD MENU.

'IBTRVD ADD COMMENTS' Protocol Filed 'IBTRVD COMMUNICATIONS EDIT' Protocol Filed

'IBTRVD DIAGNOSIS UPDATE' Protocol Filed

Sample Installation

'IBTRVD INSURANCE ACTION' Protocol Filed 'IBTRVD PROCEDURE UPDATE' Protocol Filed 'IBTRVD PROVIDER UPDATE' Protocol Filed 'IBTRVD REVIEW CRITERIA' Protocol Filed 'IBTRVD REVIEW INFO' Protocol Filed 'IBTRVD SPEC UNIT' Protocol Filed 'IBTRVD STATUS CHANGE' Protocol Filed 'SD PARM PARAMETERS MENU' Protocol Filed OK, Protocol Installation is Complete.

\>\>\> Installing List Templates...

'IB CHARGES' List Template...Filed. 'IB EVENTS' List Template...Filed.

'IBCNS ANNUAL BENEFITS' List Template...Filed. 'IBCNS BENEFITS USED BY DATE' List Template...Filed. 'IBCNS EXPANDED POLICY' List Template...Filed. 'IBCNS INSURANCE COMPANY' List Template...Filed. 'IBCNS INSURANCE MANAGEMENT' List Template...Filed.

'IBCNS PATIENT INSURANCE' List Template...Filed. 'IBCNS VIEW AN BEN' List Template...Filed. 'IBCNS VIEW BEN USED' List Template...Filed. 'IBCNS VIEW EXP POL' List Template...Filed. 'IBCNS VIEW INS CO' List Template...Filed. 'IBCNS VIEW PAT INS' List Template...Filed. 'IBDE IMP/EXP FORMS' List Template...Filed. 'IBDE IMP/EXP TK BLOCKS' List Template...Filed. 'IBDE TEXT DISPLAY' List Template...Filed.

'IBDF CLINIC FORM LIST' List Template...Filed. 'IBDF DISPLAY FORM FOR EDIT' List Template...Filed.

'IBDF DISPLAY GROUPS FOR EDIT' List Template...Filed. 'IBDF EDIT GROUP'S SELECTIONS' List Template...Filed.

'IBDF EDIT TOOL KIT BLOCKS' List Template...Filed. 'IBDF FORM BLOCK EDIT' List Template...Filed. 'IBDF TOOL KIT BLOCK LIST' List Template...Filed. 'IBDF TOOL KIT FORMS' List Template...Filed.

'IBDF VIEW TOOL KIT BLOCK' List Template...Filed. 'IBT APPEAL/DENIAL EDITOR' List Template...Filed. 'IBT APPEAL/DENIAL INS EDITOR' List Template...Filed. 'IBT CLAIMS TRACKING EDITOR' List Template...Filed. 'IBT COMMUNICATIONS EDITOR' List Template...Filed. 'IBT EDIT PENDING REVIEW' List Template...Filed.

'IBT EXPAND/EDIT COMMUNICATIONS' List Template...Filed.

'IBT EXPAND/EDIT DENIALS' List Template...Filed. 'IBT EXPAND/EDIT REVIEW' List Template...Filed. 'IBT EXPAND/EDIT TRACKING' List Template...Filed. 'IBT REVIEW EDITOR' List Template...Filed.

\>\>\> Creating a PACKAGE (#9.4) file entry for the Encounter Form Import/Export Utility... done.

\>\>\> Creating an entry in the ENCOUNTER FORM file (#357) required by the Encounter Form Utilities... done

\>\>\> Creating an entry in the ENCOUNTER FORM file (#357) required by the Encounter Form Utilities... done

\>\>\> Adding new discharge status for bills...

Sample Installation

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 11%" />
<col style="width: 81%" />
</colgroup>
<thead>
<tr class="header">
<th><p>&gt;&gt;&gt;</p>
<p>&gt;&gt;&gt;</p>
<p>&gt;&gt;&gt;</p></th>
<th><p>Adding Adding</p>
<p>Adding</p></th>
<th><p>new entries to the Rate Type File - CHAMPVA ... new revenue codes...</p>
<p>Occurrence Span Codes...</p></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>&gt;&gt;&gt;</td>
<td>Adding</td>
<td>Value Codes...</td>
</tr>
<tr class="even">
<td>&gt;&gt;&gt;</td>
<td>Adding</td>
<td>new cancellation reasons into file #350.3...</td>
</tr>
</tbody>
</table>

> \>\> 'MT CATEGORY CHANGED FROM C' has been filed...

> \>\> 'COMP & PENSION VISIT RECORDED' has been filed...

> \>\> 'CHAMPVA ADMISSION DELETED' has been filed...

> \>\> 'RECD INPATIENT CARE' has been filed...

> \>\> 'CHECK OUT DELETED' has been filed...

> \>\> 'CLASSIFICATION CHANGED' has been filed...

> \>\> 'RESEARCH VISIT/ADMISSION' has been filed...

> \>\> 'SERVICE CONNECTED VISIT/ADM' has been filed...

> \>\> 'HARDSHIP GRANTED' has been filed...

> \>\> 'ADJUDICATED AS CATEGORY A' has been filed...

> \>\> 'TREATED AT OTHER FACILITY' has been filed...

> \>\> 'AGENT ORANGE RELATED VISIT' has been filed...

> \>\> 'IONIZING RAD RELATED VISIT' has been filed...

> \>\> 'ENV CONTAMINANT RELATED VISIT' has been filed...

> \>\> 'CLASS II DENTAL VISIT' has been filed...

\>\>\> Loading routines of other packages, if appropriate...

> \>\> Installing DGBLRV routine from IB20PT81 routine... DGBLRV filed.

> \>\> Installing DGPTF routine from IB20PT82 routine... DGPTF filed.

> \>\> Installing DGPTTS routine from IB20PT83 routine... DGPTTS filed.

> \>\> Installing DGPTTS1 routine from IB20PT84 routine... DGPTTS1 filed.

> \>\> Installing DGPTTS3 routine from IB20PT85 routine... DGPTTS3 filed.

> \>\> Installing DGPTUTL routine from IB20PT86 routine... DGPTUTL filed.

> \>\> Installing DGRPDB routine from IB20PT87 routine... DGRPDB filed.

> \>\> Installing DG3PR0 routine from IB20PT88 routine... DG3PR0 filed.

> \>\> Installing DG3PR1 routine from IB20PT89 routine... DG3PR1 filed.

> \>\> Installing DG3PR2 routine from IB20PT8A routine... DG3PR2 filed.

> \>\> Installing DGPMVBUR routine from IB20PT8B routine... DGPMVBUR filed.

> \>\> Installing FBUINS routine from IB20PT8C routine... FBUINS filed.

\<\<\< Mail Group 'IB NEW INSURANCE' added... Remember to add Members to this group

\<\<\< Updating new site parameters automatically!

\<\<\< Deleting Obsolete field \*INSURANCE ADDRESS from Patient File Data Dictionary

\<\<\< Deleting Obsolete \*ADDRESS data from Insurance Company Entries I'll write a dot for each 100 entries....

\<\<\< Deleting Obsolete subfile \*ADDRESS from Insurance Company File Data Dictionary

\<\<\< Patient file insurance conversion

> Cross-reference patient file by Insurance company and Update Health Insurance Policy Pointers

Sample Installation

> Patient file update queued as task 563

\<\<\< Bill/Claims file Conversion.

> Cross-reference Bill/Claims file by Primary Insurer Bill/Claims file update queued as task 564

\<\<\< Load current inpatients into Claims Tracking Claims Tracking update queued as task 565

\>\>\> Initialization Complete at MAR 21, 1994@12:50:06

> Elapse time for initialization was: 0 Hours, 12 Minutes, 3 Seconds

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* The installation of Integrated Billing Version 2.0 has completed.

Please remember to re-compile all templates, by typing D ALL^IBEFUTL1 in programmer mode, on all of your systems.

Please be sure that the Means Test nightly billing compilation (option IB MT NIGHT COMP) is scheduled to run. If it is not, it should be scheduled to run early each morning (after the G&L Recalculation).

Be sure that it is not scheduled twice!!

The Integrated Billing DGCR\* routines have been converted to the IB\* namespace. The following DGCR\* routines are still required on your system:

> DGCRNS DGCRAMS DGCRP3

These routines were exported with this version.

The following DGCR\* routines are now obsolete and may be deleted from your system:

DGCRA DGCRA0 DGCRA1 DGCRA2 DGCRA3 DGCRA31 DGCRA32 DGCRAMS1 DGCRAMS2 DGCRB DGCRB1 DGCRB2 DGCRBB DGCRBB1 DGCRBB2 DGCRBR DGCRBULL DGCRC DGCRCC DGCRCC1 DGCRCC2 DGCRCPT DGCRMENU DGCRNQ DGCRNQ1 DGCROBL DGCROMBL DGCRONS1 DGCRONS2 DGCRONSC DGCROPV DGCROPV1 DGCROPV2 DGCRORT DGCRORT1 DGCROST DGCROST1 DGCROTR DGCROTR1 DGCROTR2 DGCROTR3 DGCROTR4 DGCRP DGCRP0 DGCRP1 DGCRP2 DGCRP4 DGCRPAR DGCRPAR1 DGCRSC1 DGCRSC2 DGCRSC3 DGCRSC4 DGCRSC4A DGCRSC4B DGCRSC4C DGCRSC5 DGCRSC6 DGCRSC61 DGCRSC7 DGCRSC8 DGCRSC8H DGCRSCE DGCRSCE1 DGCRSCH DGCRSCH1 DGCRSCP DGCRSCU DGCRSCV DGCRST DGCRST1 DGCRST2 DGCRST3 DGCRST4 DGCRST5 DGCRTN DGCRTP DGCRU DGCRU1 DGCRU2 DGCRU3 DGCRU4 DGCRU5 DGCRU6 DGCRU61 DGCRU62 DGCRU63 DGCRU7 DGCRU71 DGCRVA DGCRVA0 DGCRVA1 DGCRXX DGCRXX1 DGCRXX10 DGCRXX11 DGCRXX12 DGCRXX13 DGCRXX14 DGCRXX15 DGCRXX16 DGCRXX17 DGCRXX18 DGCRXX19 DGCRXX2 DGCRXX3 DGCRXX4 DGCRXX5 DGCRXX6 DGCRXX7 DGCRXX8 DGCRXX9

Sample Installation

The following IB\* routines are now obsolete and may be deleted from your system:

IBACKIN IBEP IBEHCFA IBEHCF1 IBOHCTP IBOHCP

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\>

Sample Installation

# Resource Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### The installation of Integrated Billing v2.0 may require approximately 5-15 megabytes of additional disk capacity. This includes up to 2.5 megabytes in the global DPT, up to 2.5 megabytes in the global DGCR, up to 5 megabytes in the global IBA, and up to 5 megabytes in the new global IBT. 4 megabytes of disk capacity will be needed to load all of the routines exported with this package.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### The Encounter Form Utilities require a small amount of additional capacity to edit and store the format of the encounter forms. Please note that the standard partition size has been increased to 40K. You will need to increase your partition size to the new standard in order to run the utilities. The printing of encounter forms will require at least one dedicated printer that most sites have already received. The printing will require additional CPU capacity; however, this job may be scheduled during non-peak workload hours.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### The Insurance Data Capture module has been highly used during testing. This module will increase disk utilization in the DPT global by approximately 1K per every 10 insurance policies and in the IBA global by 1K per every three insurance policies.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Based on the experience of our test sites, the Claims Tracking module will use approximately 5K of disk space for every pre-admission entry (one for every insurance case plus 5 per week for UR). In addition, approximately 1K of disk space for every 3 outpatient visits or prescription refills will be used.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Resource Requirements