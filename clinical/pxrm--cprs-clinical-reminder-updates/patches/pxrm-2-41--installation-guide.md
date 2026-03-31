---
title: PXRM*2*41 Teledermatology Imager Note and Reader Note Install Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: Teledermatology Imager Note and Reader Note Install Guide
app_code: PXRM
app_name: "CPRS: Clinical Reminders"
section: CLI
app_status: active
pkg_ns: PXRM
patch_ver: 2
patch_id: PXRM*2*41
group_key: "PXRM:PXRM:2"
file_numbers: []
security_keys: []
menu_options: 0
description: > ![](pxrm-2-41-teledermatology-imager-note-and-reader-note-install-guide/001.png)
audience: 
keywords: 
  - lesion
  - problem
  - reader
  - table
  - contents
  - reminder
  - other
  - teledermatology
  - dialog
  - health
page_count: 0
word_count: 10979
section_count: 2
table_count: 2
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: December 2015
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_0_41_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Clinical_Reminders/pxrm_2_0_41_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=60"
---

> ![](pxrm-2-41-teledermatology-imager-note-and-reader-note-install-guide/001.png)

> Teledermatology Imager Note and Teledermatology Reader Note Reminder Dialog Templates

> PXRM\*2.0\*41

> INSTALLATION and SETUP GUIDE

> December 2015

### Product Development Department of Veterans Affairs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Contents


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

    - [Product Development Department of Veterans Affairs](#product-development-department-of-veterans-affairs)
- [Contents](#contents)
    - [Description:](#description)
    - [There is a shortage of dermatologists in the VA creating an access to care problem. Long wait times to see a dermatologist can result. In addition, dermatology services are typically based at medical center facilities that may require patients to travel long distances or times to receive care by a dermatologist.](#there-is-a-shortage-of-dermatologists-in-the-va-creating-an-access-to-care-problem-long-wait-times-to-see-a-dermatologist-can-result-in-addition-dermatology-services-are-typically-based-at-medical-center-facilities-that-may-require-patients-to-travel-long-distances-or-times-to-receive-care-by-a-dermatologist)
    - [To address these challenges, the VA has initiated a TeleDermatology Program. Store-and- forward TeleDermatology is a telehealth strategy in which a trained imager at a referring site takes digital images of the patient’s skin, uploads them through a computer into VistA Imaging along with additional patient information on a consult form completed by the ordering provider. These are then interpreted by a consulting dermatologist in a timeframe that is understood by both parties. The consulting Teledermatologist reviews the images and answers the consult, alerting the referring provider of a diagnosis and recommendation via CPRS.](#to-address-these-challenges-the-va-has-initiated-a-teledermatology-program-store-and-forward-teledermatology-is-a-telehealth-strategy-in-which-a-trained-imager-at-a-referring-site-takes-digital-images-of-the-patients-skin-uploads-them-through-a-computer-into-vista-imaging-along-with-additional-patient-information-on-a-consult-form-completed-by-the-ordering-provider-these-are-then-interpreted-by-a-consulting-dermatologist-in-a-timeframe-that-is-understood-by-both-parties-the-consulting-teledermatologist-reviews-the-images-and-answers-the-consult-alerting-the-referring-provider-of-a-diagnosis-and-recommendation-via-cprs)
    - [This patch installs the following Teledermatology reminder dialogs during installation:](#this-patch-installs-the-following-teledermatology-reminder-dialogs-during-installation)
    - [Dialogs](#dialogs)
    - [VA-TELEDERMATOLOGY IMAGER NOTE VA-TELEDERMATOLOGY READER NOTE](#va-teledermatology-imager-note-va-teledermatology-reader-note)
    - [The reminder dialog templates are one part of the teledermatology process. For information on the complete process please refer to the teledermatology implementation and user manuals found on the teledermatology website. <u>Teledermatology Document Library</u>](#the-reminder-dialog-templates-are-one-part-of-the-teledermatology-process-for-information-on-the-complete-process-please-refer-to-the-teledermatology-implementation-and-user-manuals-found-on-the-teledermatology-website-uteledermatology-document-libraryu)
    - [See <u>Appendix B</u> for a list of Dialog findings that are included in the two reminder dialog templates listed above.](#see-uappendix-bu-for-a-list-of-dialog-findings-that-are-included-in-the-two-reminder-dialog-templates-listed-above)
  - [Related Documentation](#related-documentation)
- [Installation](#installation)
    - [Installing in a non-production environment will give you time to get familiar with new functionality and complete the setup for reminders and dialogs prior to installing the software in production.](#installing-in-a-non-production-environment-will-give-you-time-to-get-familiar-with-new-functionality-and-complete-the-setup-for-reminders-and-dialogs-prior-to-installing-the-software-in-production)
    - [In programmer mode type, D ^XUP, select the Kernel Installation & Distribution System menu (XPD MAIN), then the Installation option, and then the option LOAD a Distribution. Enter your directory name. KID at the Host File prompt.](#in-programmer-mode-type-d-xup-select-the-kernel-installation-distribution-system-menu-xpd-main-then-the-installation-option-and-then-the-option-load-a-distribution-enter-your-directory-name-kid-at-the-host-file-prompt)
    - [From the Installation menu, you may elect to use the following options:](#from-the-installation-menu-you-may-elect-to-use-the-following-options)
    - [This option will create a backup message of any routines exported with the patch. It will NOT back up any other changes such as DDs or templates.](#this-option-will-create-a-backup-message-of-any-routines-exported-with-the-patch-it-will-not-back-up-any-other-changes-such-as-dds-or-templates)
    - [This option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.).](#this-option-will-allow-you-to-view-all-changes-that-will-be-made-when-the-patch-is-installed-it-compares-all-components-of-the-patch-routines-dds-templates-etc)
    - [From the Installation menu on the Kernel Installation and Distribution System (KIDS) menu, run the option Install Package(s). Select the build PXRM and proceed with the install. If you have problems with the installation, log a Remedy ticket and/or call the National Help Desk to report the problem.](#from-the-installation-menu-on-the-kernel-installation-and-distribution-system-kids-menu-run-the-option-install-packages-select-the-build-pxrm-and-proceed-with-the-install-if-you-have-problems-with-the-installation-log-a-remedy-ticket-andor-call-the-national-help-desk-to-report-the-problem)
    - [=\> TELEDERM TEMPLATES ;Created on Sep 15, 2015@08:30:40](#telederm-templates-created-on-sep-15-2015083040)
    - [Answer "NO" to the following prompt:](#answer-no-to-the-following-prompt)
    - [See <u>Appendix A</u>](#see-uappendix-au)
    - [Use the KIDS Install File Print option to print out the results of the installation process. You can select the multi-package build or any of the individual builds included in the multi-package build.](#use-the-kids-install-file-print-option-to-print-out-the-results-of-the-installation-process-you-can-select-the-multi-package-build-or-any-of-the-individual-builds-included-in-the-multi-package-build)
    - [Use the KIDS Build File Print option to print out the build components.](#use-the-kids-build-file-print-option-to-print-out-the-build-components)
    - [After successful installation, the following init routines may be deleted:](#after-successful-installation-the-following-init-routines-may-be-deleted)
- [Post-Install Set-up Instructions](#post-install-set-up-instructions)
    - [Before linking the dialog to a title or using it in Shared templates you must first add it into the TIU Template Reminder Dialog Parameter list.](#before-linking-the-dialog-to-a-title-or-using-it-in-shared-templates-you-must-first-add-it-into-the-tiu-template-reminder-dialog-parameter-list)
- [Appendix A: Installation Example](#appendix-a-installation-example)
- [Appendix B: Findings in the reminder dialog templates](#appendix-b-findings-in-the-reminder-dialog-templates)
    - [The OIT Master Glossary is available at <u>http://vaww.oed.wss.va.gov/process/Library/masterglossary/masterglossary.htm</u>](#the-oit-master-glossary-is-available-at-uhttpvawwoedwssvagovprocesslibrarymasterglossarymasterglossaryhtmu)
    - [CAC – Clinical Applications Coordinator](#cac-clinical-applications-coordinator)
    - [CDC – Centers for Disease Control and Prevention](#cdc-centers-for-disease-control-and-prevention)
    - [CPRS – Computerized Patient Record System, previous version dating back to 1997 was CPRS List Manager (VistA terminal emulation only) and no longer supported but is still accessible in VISTA. CPRS GUI is the Windows version (since 1998), and is now called just CPRS - <u>CPRS page on VDL web site</u>](#cprs-computerized-patient-record-system-previous-version-dating-back-to-1997-was-cprs-list-manager-vista-terminal-emulation-only-and-no-longer-supported-but-is-still-accessible-in-vista-cprs-gui-is-the-windows-version-since-1998-and-is-now-called-just-cprs-ucprs-page-on-vdl-web-siteu)
    - [CWAD – Special note titles that display in the POSTINGS window in the CPRS header. Each letter stands for a category: C = Crisis Notes; W = Clinical Warnings; A = Allergies/Adverse Drug Reactions (ADR); D = Advance Directives](#cwad-special-note-titles-that-display-in-the-postings-window-in-the-cprs-header-each-letter-stands-for-a-category-c-crisis-notes-w-clinical-warnings-a-allergiesadverse-drug-reactions-adr-d-advance-directives)
    - [Data Object – also called a ‘Patient Data Object’ or just as ‘object’. These are either created by programmer (OI&T staff), or a CAC/HIS can create (TIU-HS object).](#data-object-also-called-a-patient-data-object-or-just-as-object-these-are-either-created-by-programmer-oit-staff-or-a-cachis-can-create-tiu-hs-object)
    - [Dialog- A window in CPRS that opens in the format of a form to aid the user in creating text in a note and entering information into the record with a point and click interface.](#dialog-a-window-in-cprs-that-opens-in-the-format-of-a-form-to-aid-the-user-in-creating-text-in-a-note-and-entering-information-into-the-record-with-a-point-and-click-interface)
    - [Elements- A component in VistA that is configured to display content for the user when a dialog is opened.](#elements-a-component-in-vista-that-is-configured-to-display-content-for-the-user-when-a-dialog-is-opened)
    - [EVD – Ebola Virus Disease](#evd-ebola-virus-disease)
    - [FAQ – Frequently Asked Questions](#faq-frequently-asked-questions)
    - [FORUM – the VA’s WAN (Wide Area Network), for mail, patch trackers, E3R repository](#forum-the-vas-wan-wide-area-network-for-mail-patch-trackers-e3r-repository)
    - [GUI – Graphical User Interface, referring to a Windows application](#gui-graphical-user-interface-referring-to-a-windows-application)
    - [GUI Dialog Template/GUI Dialog - a CPRS template (plain text), TXML format, icons ![](pxrm-2-41-teledermatology-imager-note-and-reader-note-install-guide/005.png) ![](pxrm-2-41-teledermatology-imager-note-and-reader-note-install-guide/006.png) Health Factor- Informational data marker entered into the record to document patient information that is not readily identifiable with other information data entries in the system.](#gui-dialog-templategui-dialog-a-cprs-template-plain-text-txml-format-icons-pxrm-2-41-teledermatology-imager-note-and-reader-note-install-guide005png-pxrm-2-41-teledermatology-imager-note-and-reader-note-install-guide006png-health-factor-informational-data-marker-entered-into-the-record-to-document-patient-information-that-is-not-readily-identifiable-with-other-information-data-entries-in-the-system)
    - [Health Factors are used in TIU-Health Summary objects, in Health Summary types, and for data capture (for VA Fileman queries/reports, VISN data warehouse data pulls, etc.)](#health-factors-are-used-in-tiu-health-summary-objects-in-health-summary-types-and-for-data-capture-for-va-fileman-queriesreports-visn-data-warehouse-data-pulls-etc)
    - [HIS – Health Informatics Specialist, another title for Clinical Applications Coordinator (CAC) with same responsibilities as a CAC.](#his-health-informatics-specialist-another-title-for-clinical-applications-coordinator-cac-with-same-responsibilities-as-a-cac)
    - [Health Summary (HS) – a clinical module (package) in VistA; GMTS is the package’s name spacing - <u>Health Summary page on VDL web site</u>](#health-summary-hs-a-clinical-module-package-in-vista-gmts-is-the-packages-name-spacing-uhealth-summary-page-on-vdl-web-siteu)
    - [Health Summary Type – a configuration of health summary components used as the basis of a report viewed in VISTA or the CPRS GUI, or used in a TIU-Health Summary object](#health-summary-type-a-configuration-of-health-summary-components-used-as-the-basis-of-a-report-viewed-in-vista-or-the-cprs-gui-or-used-in-a-tiu-health-summary-object)
    - [Health Summary Object – the display settings of a Health Summary Type which is part of a TIU-Health Summary Object configuration.](#health-summary-object-the-display-settings-of-a-health-summary-type-which-is-part-of-a-tiu-health-summary-object-configuration)
    - [Health Summary Component – an item that is used to create a health summary type (i.e., report). Health Summary components can be viewed via \[GMTS HS ADHOC\], or "List Health Summary Components \[GMTS COMP LIST\]", or "List Health Summary Component Descriptions \[GMTS COMP DESC LIST\]".](#health-summary-component-an-item-that-is-used-to-create-a-health-summary-type-ie-report-health-summary-components-can-be-viewed-via-gmts-hs-adhoc-or-list-health-summary-components-gmts-comp-list-or-list-health-summary-component-descriptions-gmts-comp-desc-list)
    - [Host file – the file that is created in the reminder exchange option using .prd (Packed Reminder Definition format](#host-file-the-file-that-is-created-in-the-reminder-exchange-option-using-prd-packed-reminder-definition-format)
    - [KIDS- Kernel Installation Distribution System](#kids-kernel-installation-distribution-system)
    - [Mapping - Linking of data markers such as Health Factors or other data entry items to reminder components such as reminder elements.](#mapping-linking-of-data-markers-such-as-health-factors-or-other-data-entry-items-to-reminder-components-such-as-reminder-elements)
    - [Name spacing – the prefixing, i.e., the initial 3-4 leading characters of a module or items in VistA](#name-spacing-the-prefixing-ie-the-initial-3-4-leading-characters-of-a-module-or-items-in-vista)
    - [National Class - The highest collection of edit permissions which can be assigned to an item (versus VISN or LOCAL)](#national-class-the-highest-collection-of-edit-permissions-which-can-be-assigned-to-an-item-versus-visn-or-local)
    - [NCRC – National Clinical Reminder Committee](#ncrc-national-clinical-reminder-committee)
    - [OPH – Office of Public Health](#oph-office-of-public-health)
    - [OIA – Office of Information and Analytics](#oia-office-of-information-and-analytics)
    - [OPC – Office of Primary Care](#opc-office-of-primary-care)
    - [Packing List – the list of included items of a reminder exchange export when viewed from the ‘IFE’ action in the reminder exchange VISTA option](#packing-list-the-list-of-included-items-of-a-reminder-exchange-export-when-viewed-from-the-ife-action-in-the-reminder-exchange-vista-option)
    - [PCE – Patient Care Encounter (link to VDL web page)](#pce-patient-care-encounter-link-to-vdl-web-page)
    - [PRD - .pdf file = Packed Reminder Definition (the alternate format for sending/receiving reminder exchange exports).](#prd-pdf-file-packed-reminder-definition-the-alternate-format-for-sendingreceiving-reminder-exchange-exports)
    - [PXRM – namespace for the clinical reminders module - <u>clinical reminders page on VDL web</u> <u>site</u>](#pxrm-namespace-for-the-clinical-reminders-module-uclinical-reminders-page-on-vdl-webu-usiteu)
    - [Reminder Taxonomy- Collection of specific codes associated with specific clinical conditions](#reminder-taxonomy-collection-of-specific-codes-associated-with-specific-clinical-conditions)
    - [Reminder Dialog ![](pxrm-2-41-teledermatology-imager-note-and-reader-note-install-guide/007.png) - a template created in \[PXRM DIALOG/COMPONENT EDIT\]; can be used without reminder logic (reminder definition)](#reminder-dialog-pxrm-2-41-teledermatology-imager-note-and-reader-note-install-guide007png-a-template-created-in-pxrm-dialogcomponent-edit-can-be-used-without-reminder-logic-reminder-definition)
    - [Reminder Dialog Template ![](pxrm-2-41-teledermatology-imager-note-and-reader-note-install-guide/008.png) - a template created in \[PXRM DIALOG/COMPONENT EDIT\] and used in CPRS without linked reminder logic (reminder definition), either as a stand-alone template or the template is linked to a note title. Sometimes also referred to as a ‘reminder template’.](#reminder-dialog-template-pxrm-2-41-teledermatology-imager-note-and-reader-note-install-guide008png-a-template-created-in-pxrm-dialogcomponent-edit-and-used-in-cprs-without-linked-reminder-logic-reminder-definition-either-as-a-stand-alone-template-or-the-template-is-linked-to-a-note-title-sometimes-also-referred-to-as-a-reminder-template)
    - [Reminder Definition – used to create reminder logic for a clinical reminder or data object or reminder order check in PXRM REMINDER MANAGEMENT\]](#reminder-definition-used-to-create-reminder-logic-for-a-clinical-reminder-or-data-object-or-reminder-order-check-in-pxrm-reminder-management)
    - [Reminder Exchange – the VISTA option \[PXRM REMINDER EXCHANGE\] used to create a reminder exchange message or .prd host file](#reminder-exchange-the-vista-option-pxrm-reminder-exchange-used-to-create-a-reminder-exchange-message-or-prd-host-file)
    - [Reminder Exchange Export – either a reminder exchange message or a .prd file moved out of the Reminder Exchange option in VISTA](#reminder-exchange-export-either-a-reminder-exchange-message-or-a-prd-file-moved-out-of-the-reminder-exchange-option-in-vista)
    - [Shared Templates- ![](pxrm-2-41-teledermatology-imager-note-and-reader-note-install-guide/009.png)Templates within the shared templates tree of CPRS, which the users can access and use while documenting in the chart](#shared-templates-pxrm-2-41-teledermatology-imager-note-and-reader-note-install-guide009pngtemplates-within-the-shared-templates-tree-of-cprs-which-the-users-can-access-and-use-while-documenting-in-the-chart)
    - [SHOP-ALL – a destination through the VA’s FORUM to access and download reminder exchange messages that have been posted and stored (uses Mailman; must have FORUM access)](#shop-all-a-destination-through-the-vas-forum-to-access-and-download-reminder-exchange-messages-that-have-been-posted-and-stored-uses-mailman-must-have-forum-access)
    - [TIU -Text Integrated Utility, the notes repository (clinical package) in VISTA - <u>TIU page on</u> <u>VDL web site</u>](#tiu-text-integrated-utility-the-notes-repository-clinical-package-in-vista-utiu-page-onu-uvdl-web-siteu)
    - [TIU Document Definition – it can be a CLASS, DOCUMENT CLASS, TITLE or OBJECT (file \#8925.1). The reminder exchange packing list shows the TIU object labeled as “TIU DOCUMENT DEFINITION”.](#tiu-document-definition-it-can-be-a-class-document-class-title-or-object-file-89251-the-reminder-exchange-packing-list-shows-the-tiu-object-labeled-as-tiu-document-definition)
    - [TIU Object – a data object /patient data object (but too general a term to know if this is programmer-created or CAC/HIS-created). See DATA OBJECT above.](#tiu-object-a-data-object-patient-data-object-but-too-general-a-term-to-know-if-this-is-programmer-created-or-cachis-created-see-data-object-above)
    - [TXML - the file format of ‘plain text’ CPRS templates, aka “GUI dialogs” or “GUI Dialog Templates”. Uses the CPRS GUI Template Editor to create and edit](#txml-the-file-format-of-plain-text-cprs-templates-aka-gui-dialogs-or-gui-dialog-templates-uses-the-cprs-gui-template-editor-to-create-and-edit)
    - [User Acceptance Testing - (UAT) critical software testing where end-users test the software in real- world scenarios before it is nationally released](#user-acceptance-testing-uat-critical-software-testing-where-end-users-test-the-software-in-real-world-scenarios-before-it-is-nationally-released)
    - [URL – Uniform Resource Locator, i.e., a specific web address (Internet or Intranet)](#url-uniform-resource-locator-ie-a-specific-web-address-internet-or-intranet)
    - [Usability Testing- evaluating the software by testing with a representation of users that follow specific tasks (test scripts), identify problems, suggest improvements and determine the user’s satisfaction with the product.](#usability-testing-evaluating-the-software-by-testing-with-a-representation-of-users-that-follow-specific-tasks-test-scripts-identify-problems-suggest-improvements-and-determine-the-users-satisfaction-with-the-product)
    - [VDL –The Internet page for all VISTA manuals and documentation <u>VistA Documentation Library</u>](#vdl-the-internet-page-for-all-vista-manuals-and-documentation-uvista-documentation-libraryu)
    - [VMP- VistA Maintenance Project](#vmp-vista-maintenance-project)
    - [<u>\[return to table of contents\]</u>](#ureturn-to-table-of-contentsu)
1.  [Retrieve the host file from one of the following locations (with the ASCII file type) 5](#_bookmark6)
2.  [Install the patch first in a training or test account 5](#_bookmark7)
3.  [Load the distribution. 5](#_bookmark8)
4.  [Backup a Transport Global 5](#_bookmark9)
[a. Compare Transport Global to Current System 6](#_bookmark10)
5.  [Install the build. 6](#_bookmark11)
6.  [Install File Print 6](#_bookmark12)
7.  [Build File Print 6](#_bookmark13)
8.  [Post-installation routines 6](#_bookmark14)
> Introduction

### Description:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### There is a shortage of dermatologists in the VA creating an access to care problem. Long wait times to see a dermatologist can result. In addition, dermatology services are typically based at medical center facilities that may require patients to travel long distances or times to receive care by a dermatologist.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### To address these challenges, the VA has initiated a TeleDermatology Program. Store-and- forward TeleDermatology is a telehealth strategy in which a trained imager at a referring site takes digital images of the patient’s skin, uploads them through a computer into VistA Imaging along with additional patient information on a consult form completed by the ordering provider. These are then interpreted by a consulting dermatologist in a timeframe that is understood by both parties. The consulting Teledermatologist reviews the images and answers the consult, alerting the referring provider of a diagnosis and recommendation via CPRS.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### This patch installs the following Teledermatology reminder dialogs during installation:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Dialogs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### VA-TELEDERMATOLOGY IMAGER NOTE VA-TELEDERMATOLOGY READER NOTE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### The reminder dialog templates are one part of the teledermatology process. For information on the complete process please refer to the teledermatology implementation and user manuals found on the teledermatology website. [<u>Teledermatology Document Library</u>](http://vaww.infoshare.va.gov/sites/telehealth/docs/Forms/tdrm.aspx)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### See [<u>Appendix B</u>](#appendix-b-findings-in-the-reminder-dialog-templates) for a list of Dialog findings that are included in the two reminder dialog templates listed above.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Pre-Installation
> <span id="_bookmark2" class="anchor"></span>*Required Software for PXRM\*2\
| Package/Patch  | Namespace | Version | Comments |
|--------------------|---------------|-------------|--------------|
| Clinical Reminders | PXRM          | 2.0         |              |
|                    |               |             |              |

## Related Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Documentation</strong></th>
<th><strong>Documentation File name</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Telederm Imager/Reader Notes Install Guide</td>
<td>PXRM_2_0_41_IG.PDF</td>
</tr>
<tr class="even">
<td>Teledermatology CAC Implementation Guide</td>
<td><p><a href="http://vaww.infoshare.va.gov/sites/telehealth/docs/Fo">http://vaww.infoshare.va.gov/sites/telehealth/docs/Fo</a></p>
<p>rms/tdrm.aspx</p></td>
</tr>
<tr class="odd">
<td>Teledermatology User Guide</td>
<td><p><a href="http://vaww.infoshare.va.gov/sites/telehealth/docs/Fo">http://vaww.infoshare.va.gov/sites/telehealth/docs/Fo</a></p>
<p>rms/tdrm.aspx</p></td>
</tr>
</tbody>
</table>
> <span id="_bookmark4" class="anchor"></span>Web Sites
<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 36%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Site</strong></th>
<th><strong>URL</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Teledermatology site</td>
<td><p><a href="http://vaww.telehealth.va.gov/clinic/spc/tderm/index.asp"><u>http://vaww.telehealth.va.gov/clinic</u></a></p>
<p><a href="http://vaww.telehealth.va.gov/clinic/spc/tderm/index.asp"><u>/spc/tderm/index.asp</u></a></p></td>
<td><p>Contains manuals, information on</p>
<p>entire teledermatology process</p></td>
</tr>
<tr class="even">
<td>National Clinical Reminders site</td>
<td><a href="http://vista.med.va.gov/reminders"><u>http://vista.med.va.gov/reminders</u></a></td>
<td>Contains manuals, PowerPoint presentations, and other information about Clinical Reminders</td>
</tr>
<tr class="odd">
<td>National Clinical Reminders Committee</td>
<td><a href="http://vaww.portal.va.gov/sites/ncrcpublic/default.aspx"><u>http://vaww.portal.va.gov/sites/ncrc</u></a> <a href="http://vaww.portal.va.gov/sites/ncrcpublic/default.aspx"><u>public/default.aspx</u></a></td>
<td><p>This committee directs the development of new and revised</p>
<p>national reminders</p></td>
</tr>
<tr class="even">
<td>VistA Document Library</td>
<td><a href="http://www.va.gov/vdl/"><u>http://www.va.gov/vdl/</u></a></td>
<td><p>Contains manuals for all on the various nationally released software applications created and/or used by the</p>
<p>VA in its mission to provide the best service to our nation's veterans</p></td>
</tr>
</tbody>
</table>

# Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### This patch can be installed with users on the system, but it should be done during non-peak hours. Estimated Installation Time: 10-15 minutes

1.  <span id="_bookmark6" class="anchor"></span>Retrieve the host file from one of the following locations (with the ASCII file type):

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 31%" />
<col style="width: 51%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Albany</p>
</blockquote></th>
<th><mark>REDACTED</mark></th>
<th><mark>REDACTED</mark></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Hines</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Salt Lake City</p>
</blockquote></td>
<td><mark>REDACTED</mark></td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>

2.  <span id="_bookmark7" class="anchor"></span>Install the patch first in a training or test account.

### Installing in a non-production environment will give you time to get familiar with new functionality and complete the setup for reminders and dialogs prior to installing the software in production.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

3.  <span id="_bookmark8" class="anchor"></span>Load the distribution.

### In programmer mode type, D ^XUP, select the Kernel Installation & Distribution System menu (XPD MAIN), then the Installation option, and then the option LOAD a Distribution. Enter your directory name. KID at the Host File prompt.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Example

### From the Installation menu, you may elect to use the following options:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

4.  <span id="_bookmark9" class="anchor"></span>Backup a Transport Global

### This option will create a backup message of any routines exported with the patch. It will NOT back up any other changes such as DDs or templates.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  <span id="_bookmark10" class="anchor"></span>Compare Transport Global to Current System

### This option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.).

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

5.  <span id="_bookmark11" class="anchor"></span>Install the build.

### From the Installation menu on the Kernel Installation and Distribution System (KIDS) menu, run the option Install Package(s). Select the build PXRM and proceed with the install. If you have problems with the installation, log a Remedy ticket and/or call the National Help Desk to report the problem.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Select Installation \<TEST ACCOUNT\> Option: Install Package(s)

> Select INSTALL NAME: PXRM\*2.0\*41 9/15/15@11:17:25

### =\> TELEDERM TEMPLATES ;Created on Sep 15, 2015@08:30:40

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Answer "NO" to the following prompt:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Want KIDS to INHIBIT LOGONs during install? NO// NO Installation Example

### See [<u>Appendix A</u>](#appendix-a-installation-example)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

6.  <span id="_bookmark12" class="anchor"></span>Install File Print

### Use the KIDS Install File Print option to print out the results of the installation process. You can select the multi-package build or any of the individual builds included in the multi-package build.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

7.  <span id="_bookmark13" class="anchor"></span>Build File Print

### Use the KIDS Build File Print option to print out the build components.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

8.  <span id="_bookmark14" class="anchor"></span>Post-installation routines

### After successful installation, the following init routines may be deleted:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> PXRMP41E PXRMP41I

# Post-Install Set-up Instructions 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Enable the reminder dialogs (If necessary).

#### Note: The dialogs may not be disabled following installation. If not disabled, skip the steps below.

- Select Reminder Managers Menu Option: DM Reminder Dialog Management
- Select Reminder Dialog Management Option: DI Reminder Dialogs
- Select Item: Next Screen// CV Change View
- Select one of the following:
  4.  Reminder Dialogs
  5.  Dialog Elements
  6.  Forced Values
  7.  Dialog Groups

P Additional Prompts

R Reminders

RG Result Group (Mental Health) RE Result Element (Mental Health)

- TYPE OF VIEW: R// D Reminder Dialogs
- Search for the VA-TELEDERMATOLOGY IMAGER NOTE in the reminder dialog list
- After selecting the Dialog, check the header that starts with “REMINDER DIALOG NAME:”. If it shows “Disabled”, then proceed as below. If it does NOT show “Disabled”, skip the steps below.
- Select Item: Next Screen// E Edit/Delete Dialog
- NAME: VA-TELEDERMATOLOGY IMAGER NOTE Replace \<Enter\>
- DISABLE: DISABLE AND SEND MESSAGE// @

> SURE YOU WANT TO DELETE? Y (Yes)

- CLASS: NATIONAL// \<enter\>
- SPONSOR: Office of Telehealth Services Store and Forward Telehealth // \<enter\>
- REVIEW DATE: \<enter\>
- SOURCE REMINDER: \<enter\>
- Select SEQUENCE: 10// ^
  - Search for the VA-TELEDERMATOLOGY READER NOTE in the reminder dialog list
- Select Item: Next Screen// E Edit/Delete Dialog
- NAME: VA-TELEDERMATOLOGY READER NOTE Replace \<Enter\>
- DISABLE: DISABLE AND SEND MESSAGE// @

> SURE YOU WANT TO DELETE? Y (Yes)

- CLASS: NATIONAL// \<enter\>
- SPONSOR: Office of Telehealth Services Store and Forward Telehealth // \<enter\>
- REVIEW DATE: \<enter\>
- SOURCE REMINDER: \<enter\>
- Select SEQUENCE: 10// ^

#### Disable any VISN or Local Teledermatology Imager and/or Reader reminder dialog templates

If your site is currently using the V\*-Teledermatology Imager Note and/or the V\*-Teledermatology Reader Note reminder dialog templates OR currently using local reminder dialog templates for Teledermatology Imager and/or Reader notes they should be disabled.

- Select Reminder Managers Menu Option: DM Reminder Dialog Management
- Select Reminder Dialog Management Option: DI Reminder Dialogs
- Select Item: Next Screen// CV Change View
- Select one of the following:
4.  Reminder Dialogs
5.  Dialog Elements
6.  Forced Values
7.  Dialog Groups

P Additional Prompts

R Reminders

RG Result Group (Mental Health) RE Result Element (Mental Health)

- TYPE OF VIEW: R// D Reminder Dialogs
- Search for any local or V\* Teledermatology in the reminder dialog list
- Select Item: Next Screen// E Edit/Delete Dialog
- At the DISABLE prompt select Disable and Do Not Send Message
- CLASS: NATIONAL// \<enter\>
- SPONSOR: Office of Telehealth Services Store and Forward Telehealth // \<enter\>
- REVIEW DATE: \<enter\>
- SOURCE REMINDER: \<enter\>
- Select SEQUENCE: 10// ^
- Repeat the above step for any other local and/or V\* Teledermatology reminder dialogs.

#### Add reminder dialog templates in the TIU Template parameter

### Before linking the dialog to a title or using it in Shared templates you must first add it into the TIU Template Reminder Dialog Parameter list.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- General parameter tools \<enter\>

List Values for a Selected Parameter List Values for a Selected Entity List Values for a Selected Package List Values for a Selected Template Edit Parameter Values

Edit Parameter Values with Template Edit Parameter Definition Keyword

- Select General Parameter Tools Option: EDIT Parameter Values
- Select PARAMETER DEFINITION NAME: TIU TEMPLATE REMINDER DIALOGS

1 User USR \[choose from NEW PERSON\]

3.  Service SRV \[choose from SERVICE/SECTION\]
4.  Division DIV \[choose from INSTITUTION\]
5.  System SYS \[TEST.V02.MED.VA.GOV\]
- Enter selection: 5 System
- Select Display Sequence: ENTER A UNIQUE NUMBER (you may ? question mark this option to obtain the list of templates associated with this parameter)
- Are you adding (the new display sequence number) as a new Display Sequence? Yes// \<enter\> to confirm
- Clinical Reminder Dialog: VA-TELEDERMATOLOGY IMAGER NOTE \<enter\>
- Select Display Sequence: ENTER THE NEXT UNIQUE NUMBER
- Are you adding (the new display sequence number) as a new Display Sequence? Yes// \<enter\> to confirm
- Clinical Reminder Dialog: VA-TELEDERMATOLOGY READER NOTE \<enter\>

#### Placing the Reminder Dialog in CPRS

Link the dialogs from the CPRS TEMPLATE EDITOR.

- Open CPRS, select any patient and then the Notes tab
- Open My Templates.
- Create a new template and give it an appropriate name (right side under Personal Templates)
- In the Template Type box select Reminder Dialog.
- Select the drop down arrow in the Reminder Dialog window and locate and select the VA- TELEDERMATOLOGY IMAGER NOTE
- Create another new template and give it an appropriate name (right side under Personal Templates)
- In the Template Type box select Reminder Dialog.
- Select the drop down arrow in the Reminder Dialog window and locate and select the VA- TELEDERMATOLOGY READER NOTE
  - Select the APPLY button.

![](pxrm-2-41-teledermatology-imager-note-and-reader-note-install-guide/002.png)

#### Creating a “Teledermatology ” folder in Shared Templates

It is recommended to create a folder for this template under Shared templates called “Teledermatology”.

- Access CPRS, select any patient and select the Notes tab.
- Select Options, Edit Share templates
- Select and open Shared Templates (left side of the screen)
- On the right side of the template editor screen Select the New Template button and name New template Ebola Templates
- Select the drop down arrow under the Template type box and select Folder
- ![](pxrm-2-41-teledermatology-imager-note-and-reader-note-install-guide/003.png)Select Apply to save this folder

#### Placing the templates in the Teledermatology Templates folder

Once you have created the template into My Templates and created a Teledermatology Share Template folder you can copy the template from My Templates to the Teledermatology Template folder, making it viewable and available to all CPRS users.

- Access CPRS, select any patient and select the Notes tab.
- Select Options, Edit Share templates
- Select and open Shared Templates (left side of the screen)
- Select the Teledermatology Templates folder
- On the right side of the template editor screen select the VA-Teledermatology Imager Note template
- Select the bold Copy button between the two panes
- On the right side of the template editor screen select the VA-Teledermatology Reader Note template
- Select the bold Copy button between the two panes
- ![](pxrm-2-41-teledermatology-imager-note-and-reader-note-install-guide/004.png)Select Apply to save the template into the folder

#### Teledermatology process

Review the complete teledermatology process and make any necessary updates at your site as described on the National teledermatology web site - [<u>http://vaww.telehealth.va.gov/clinic/spc/tderm/index.asp</u>](http://vaww.telehealth.va.gov/clinic/spc/tderm/index.asp)

# Appendix A: Installation Example 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Select Installation \<TEST ACCOUNT\> Option: Load a Distribution

> Enter a Host File: \<your directory\>PXRM_2_0_41.KID

KIDS Distribution saved on Sep 15, 2015@08:30:40 Comment: TELEDERM TEMPLATES

This Distribution contains Transport Globals for the following Package(s): Build PXRM\*2.0\*41 has been loaded before, here is when:

PXRM\*2.0\*41 Install Completed

was loaded on Sep 15, 2015@09:40:15 OK to continue with Load? NO// YES

Distribution OK!

Want to Continue with Load? YES// Loading Distribution...

PXRM\*2.0\*41

Use INSTALL NAME: PXRM\*2.0\*41 to install this Distribution.

> Select Installation Option: Install Package(s)

> Select INSTALL NAME: PXRM\*2.0\*41 9/15/15@11:17:25

=\> TELEDERM TEMPLATES ;Created on Sep 15, 2015@08:30:40

This Distribution was loaded on Sep 15, 2015@11:17:25 with header of TELEDERM TEMPLATES ;Created on Sep 15, 2015@08:30:40

It consisted of the following Install(s): PXRM\*2.0\*41

Checking Install for Package PXRM\*2.0\*41 Install Questions for PXRM\*2.0\*41 Incoming Files:

811.8 REMINDER EXCHANGE (including data) Note: You already have the 'REMINDER EXCHANGE' File. I will OVERWRITE your data with mine.

Want KIDS to INHIBIT LOGONs during the install? NO//

Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt. Enter a '^' to abort the install.

DEVICE: HOME// SSH Virtual Terminal

Install Started for PXRM\*2.0\*41 :

> Sep 15, 2015@11:17:35

Build Distribution Date: Sep 15, 2015 Installing Routines:

> Sep 15, 2015@11:17:35

Running Pre-Install Routine: PRE^PXRMP41I Installing Data Dictionaries:

> Sep 15, 2015@11:17:35

Installing Data:

> Sep 15, 2015@11:17:36

Running Post-Install Routine: POST^PXRMP41I

There are 1 Reminder Exchange entries to be installed. Updating Routine file...

Updating KIDS files...

PXRM\*2.0\*41 Installed.

> Sep 15, 2015@11:17:36

Not a production UCI

PXRM\*2.0\*41

Install Completed

# Appendix B: Findings in the reminder dialog templates 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> *List of Health Factor Categories and Health Factors*

> Teledermatology Reader

#### Categories

- VA-TDR CATEGORY-EXAM F/U
- VA-TDR CATEGORY-EXAM RECOMMENDATIONS
- VA-TDR CATEGORY-IMAGE QUALITY
- VA-TDR CATEGORY-PROBLEM A
- VA-TDR CATEGORY-PROBLEM B
- VA-TDR CATEGORY-PROBLEM C
- VA-TDR CATEGORY-PROBLEM D
- VA-TDR CATEGORY-PROBLEM E
- VA-TDR CATEGORY-PROBLEM F
- VA-TDR CATEGORY-PROBLEM G
- VA-TDR CATEGORY-PROBLEM H
- VA-TDR CATEGORY-PROBLEM I
- VA-TDR CATEGORY-PROBLEM J
  - Health Factors
- VA-TDR DX LESION A-BCC
- VA-TDR DX LESION A-DYSPLASTIC NEVUS
- VA-TDR DX LESION A-MELANOMA
- VA-TDR DX LESION A-NEOPLASM UNC BEHAV
- VA-TDR DX LESION A-NEVUS
- VA-TDR DX LESION A-NON MALIG TUMOR
- VA-TDR DX LESION A-OTHER MALIGNANT
- VA-TDR DX LESION A-SCC
- VA-TDR DX LESION A-SEB KERATOSIS
- VA-TDR DX LESION B-ACTINIC KERATOSIS
- VA-TDR DX LESION B-BCC
- VA-TDR DX LESION B-DYSPLASTIC NEVUS
- VA-TDR DX LESION B-MELANOMA
- VA-TDR DX LESION B-NEOPLASM UNC BEHAV
- VA-TDR DX LESION B-NON MALIG TUMOR
- VA-TDR DX LESION B-OTHER MALIGNANT
- VA-TDR DX LESION B-SCC
- VA-TDR DX LESION B-SEB KERATOSIS
- VA-TDR DX LESION C-ACTINIC KERATOSIS
- VA-TDR DX LESION C-BCC
- VA-TDR DX LESION C-DYSPLASTIC NEVUS
- VA-TDR DX LESION C-MELANOMA
- VA-TDR DX LESION C-NEOPLASM UNC BEHAV
- VA-TDR DX LESION C-NEVUS
- VA-TDR DX LESION C-NON MALIG TUMOR
- VA-TDR DX LESION C-OTHER MALIGNANT
- VA-TDR DX LESION C-SCC
- VA-TDR DX LESION C-SEB KERATOSIS
- VA-TDR DX LESION D-ACTINIC KERATOSIS
- VA-TDR DX LESION D-BCC
- VA-TDR DX LESION D-DYSPLASTIC NEVUS
- VA-TDR DX LESION D-MELANOMA
- VA-TDR DX LESION D-NEOPLASM UNC BEHAV
- VA-TDR DX LESION D-NEVUS
- VA-TDR DX LESION D-NON MALIG TUMOR
- VA-TDR DX LESION D-OTHER MALIGNANT
- VA-TDR DX LESION D-SCC
- VA-TDR DX LESION D-SEB KERATOSIS
- VA-TDR DX LESION E-ACTINIC KERATOSIS
- VA-TDR DX LESION E-BCC
- VA-TDR DX LESION E-DYSPLASTIC NEVUS
- VA-TDR DX LESION E-MELANOMA
- VA-TDR DX LESION E-NEOPLASM UNC BEHAV
- VA-TDR DX LESION E-NEVUS
- VA-TDR DX LESION E-NON MALIG TUMOR
- VA-TDR DX LESION E-OTHER MALIGNANT
- VA-TDR DX LESION E-SCC
- VA-TDR DX LESION E-SEB KERATOSIS
- VA-TDR DX LESION F-ACTINIC KERATOSIS
- VA-TDR DX LESION F-BCC
- VA-TDR DX LESION F-DYSPLASTIC NEVUS
- VA-TDR DX LESION F-MELANOMA
- VA-TDR DX LESION F-NEOPLASM UNC BEHAV
- VA-TDR DX LESION F-NEVUS
- VA-TDR DX LESION F-NON MALIG TUMOR
- VA-TDR DX LESION F-OTHER MALIGNANT
- VA-TDR DX LESION F-SCC
- VA-TDR DX LESION F-SEB KERATOSIS
- VA-TDR DX LESION G-ACTINIC KERATOSIS
- VA-TDR DX LESION G-BCC
- VA-TDR DX LESION G-DYSPLASTIC NEVUS
- VA-TDR DX LESION G-MELANOMA
- VA-TDR DX LESION G-NEOPLASM UNC BEHAV
- VA-TDR DX LESION G-NEVUS
- VA-TDR DX LESION G-NON MALIG TUMOR
- VA-TDR DX LESION G-OTHER MALIGNANT
- VA-TDR DX LESION G-SCC
- VA-TDR DX LESION G-SEB KERATOSIS
- VA-TDR DX LESION H-ACTINIC KERATOSIS
- VA-TDR DX LESION H-BCC
- VA-TDR DX LESION H-DYSPLASTIC NEVUS
- VA-TDR DX LESION H-MELANOMA
- VA-TDR DX LESION H-NEOPLASM UNC BEHAV
- VA-TDR DX LESION H-NEVUS
- VA-TDR DX LESION H-NON MALIG TUMOR
- VA-TDR DX LESION H-OTHER MALIGNANT
- VA-TDR DX LESION H-SCC
- VA-TDR DX LESION H-SEB KERATOSIS
- VA-TDR DX LESION I-ACTINIC KERATOSIS
- VA-TDR DX LESION I-BCC
- VA-TDR DX LESION I-DYSPLASTIC NEVUS
- VA-TDR DX LESION I-MELANOMA
- VA-TDR DX LESION I-NEOPLASM UNC BEHAV
- VA-TDR DX LESION I-NEVUS
- VA-TDR DX LESION I-NON MALIG TUMOR
- VA-TDR DX LESION I-OTHER MALIGNANT
- VA-TDR DX LESION I-SCC
- VA-TDR DX LESION I-SEB KERATOSIS
- VA-TDR DX LESION J-ACTINIC KERATOSIS
- VA-TDR DX LESION J-BCC
- VA-TDR DX LESION J-DYSPLASTIC NEVUS
- VA-TDR DX LESION J-MELANOMA
- VA-TDR DX LESION J-NEOPLASM UNC BEHAV
- VA-TDR DX LESION J-NEVUS
- VA-TDR DX LESION J-NON MALIG TUMOR
- VA-TDR DX LESION J-OTHER MALIGNANT
- VA-TDR DX LESION J-SCC
- VA-TDR DX LESION J-SEB KERATOSIS
- VA-TDR DX OTHER A
- VA-TDR DX OTHER B
- VA-TDR DX OTHER C
- VA-TDR DX OTHER D
- VA-TDR DX OTHER E
- VA-TDR DX OTHER F
- VA-TDR DX OTHER G
- VA-TDR DX OTHER H
- VA-TDR DX OTHER I
- VA-TDR DX OTHER J
- VA-TDR DX RASH A
- VA-TDR DX RASH B
- VA-TDR DX RASH C
- VA-TDR DX RASH D
- VA-TDR DX RASH E
- VA-TDR DX RASH F
- VA-TDR DX RASH G
- VA-TDR DX RASH H
- VA-TDR DX RASH I
- VA-TDR DX RASH J
- VA-TDR IMAGE QUALITY HIGH
- VA-TDR IMAGE QUALITY IMPROVEMENT
- VA-TDR IMAGE QUALITY INADEQUATE
- VA-TDR READER TX BIOPSY PROBLEM A
- VA-TDR READER TX BIOPSY PROBLEM B
- VA-TDR READER TX BIOPSY PROBLEM C
- VA-TDR READER TX BIOPSY PROBLEM D
- VA-TDR READER TX BIOPSY PROBLEM E
- VA-TDR READER TX BIOPSY PROBLEM F
- VA-TDR READER TX BIOPSY PROBLEM G
- VA-TDR READER TX BIOPSY PROBLEM H
- VA-TDR READER TX BIOPSY PROBLEM I
- VA-TDR READER TX BIOPSY PROBLEM J
- VA-TDR READER TX CRYOTHERAPY PROB A
- VA-TDR READER TX CRYOTHERAPY PROB B
- VA-TDR READER TX CRYOTHERAPY PROB C
- VA-TDR READER TX CRYOTHERAPY PROB D
- VA-TDR READER TX CRYOTHERAPY PROB E
- VA-TDR READER TX CRYOTHERAPY PROB F
- VA-TDR READER TX CRYOTHERAPY PROB G
- VA-TDR READER TX CRYOTHERAPY PROB H
- VA-TDR READER TX CRYOTHERAPY PROB I
- VA-TDR READER TX CRYOTHERAPY PROB J
- VA-TDR READER TX CULTURES PROBLEM A
- VA-TDR READER TX CULTURES PROBLEM B
- VA-TDR READER TX CULTURES PROBLEM C
- VA-TDR READER TX CULTURES PROBLEM D
- VA-TDR READER TX CULTURES PROBLEM E
- VA-TDR READER TX CULTURES PROBLEM F
- VA-TDR READER TX CULTURES PROBLEM G
- VA-TDR READER TX CULTURES PROBLEM H
- VA-TDR READER TX CULTURES PROBLEM I
- VA-TDR READER TX CULTURES PROBLEM J
- VA-TDR READER TX MEDS ADD PROBLEM A
- VA-TDR READER TX MEDS ADD PROBLEM B
- VA-TDR READER TX MEDS ADD PROBLEM C
- VA-TDR READER TX MEDS ADD PROBLEM D
- VA-TDR READER TX MEDS ADD PROBLEM E
- VA-TDR READER TX MEDS ADD PROBLEM F
- VA-TDR READER TX MEDS ADD PROBLEM G
- VA-TDR READER TX MEDS ADD PROBLEM H
- VA-TDR READER TX MEDS ADD PROBLEM I
- VA-TDR READER TX MEDS ADD PROBLEM J
- VA-TDR READER TX MEDS PROB A
- VA-TDR READER TX MEDS PROB B
- VA-TDR READER TX MEDS PROB C
- VA-TDR READER TX MEDS PROB D
- VA-TDR READER TX MEDS PROB E
- VA-TDR READER TX MEDS PROB F
- VA-TDR READER TX MEDS PROB G
- VA-TDR READER TX MEDS PROB H
- VA-TDR READER TX MEDS PROB I
- VA-TDR READER TX MEDS PROB J
- VA-TDR READER TX OTHER PROBLEM A
- VA-TDR READER TX OTHER PROBLEM B
- VA-TDR READER TX OTHER PROBLEM C
- VA-TDR READER TX OTHER PROBLEM D
- VA-TDR READER TX OTHER PROBLEM E
- VA-TDR READER TX OTHER PROBLEM F
- VA-TDR READER TX OTHER PROBLEM G
- VA-TDR READER TX OTHER PROBLEM H
- VA-TDR READER TX OTHER PROBLEM I
- VA-TDR READER TX OTHER PROBLEM J
- VA-TDR READER TX RECOMMEND NONE
- VA-TDR READER TX SKIN CARE PROBLEM A
- VA-TDR READER TX SKIN CARE PROBLEM B
- VA-TDR READER TX SKIN CARE PROBLEM C
- VA-TDR READER TX SKIN CARE PROBLEM D
- VA-TDR READER TX SKIN CARE PROBLEM E
- VA-TDR READER TX SKIN CARE PROBLEM F
- VA-TDR READER TX SKIN CARE PROBLEM G
- VA-TDR READER TX SKIN CARE PROBLEM H
- VA-TDR READER TX SKIN CARE PROBLEM I
- VA-TDR READER TX SKIN CARE PROBLEM J
- VA-TDR READER UNABLE TO ASSESS PROB A
- VA-TDR READER UNABLE TO ASSESS PROB B
- VA-TDR READER UNABLE TO ASSESS PROB C
- VA-TDR READER UNABLE TO ASSESS PROB D
- VA-TDR READER UNABLE TO ASSESS PROB E
- VA-TDR READER UNABLE TO ASSESS PROB F
- VA-TDR READER UNABLE TO ASSESS PROB G
- VA-TDR READER UNABLE TO ASSESS PROB H
- VA-TDR READER UNABLE TO ASSESS PROB I
- VA-TDR READER UNABLE TO ASSESS PROB J
- VA-TDR RECONSULT TELEDERM 1 MO
- VA-TDR RECONSULT TELEDERM 1 WK
- VA-TDR RECONSULT TELEDERM 12 MO
- VA-TDR RECONSULT TELEDERM 3 MO
- VA-TDR RECONSULT TELEDERM 6 MO
- VA-TDR REFER DERM 1 MO
- VA-TDR REFER DERM 1 WK
- VA-TDR REFER DERM 12 MO
- VA-TDR REFER DERM 3 MO
- VA-TDR REFER DERM 6 MO
- VA-TDR RETURN F/U NOT REQ
- VA-TDR RETURN PCC F/U 1 MO
- VA-TDR RETURN PCC F/U 1 WK
- VA-TDR RETURN PCC F/U 3 MO
- VA-TDR RETURN PCC F/U 6 MO
- VA-TDR RETURN PCC F/U TYPE

> Teledermatology Imager

#### Categories

- VA-TDI CATEGORY-CONSULT NOT POSSIBLE
- VA-TDI CATEGORY-EDUCATION
- VA-TDI CATEGORY-EXAM F/U
- VA-TDI CATEGORY-EXAM RECOMMENDATIONS
- VA-TDI CATEGORY-HISTORY INFO
- VA-TDI CATEGORY-IMAGE QUALITY
- VA-TDI CATEGORY-LESION A
- VA-TDI CATEGORY-LESION B
- VA-TDI CATEGORY-LESION C
- VA-TDI CATEGORY-LESION D
- VA-TDI CATEGORY-LESION E
- VA-TDI CATEGORY-LESION F
- VA-TDI CATEGORY-LESION G
- VA-TDI CATEGORY-LESION H
- VA-TDI CATEGORY-LESION I
- VA-TDI CATEGORY-LESION J
- VA-TDI CATEGORY-OTHER SKIN COND
- VA-TDI CATEGORY-PROBLEM A
- VA-TDI CATEGORY-PROBLEM B
- VA-TDI CATEGORY-PROBLEM C
- VA-TDI CATEGORY-PROBLEM D
- VA-TDI CATEGORY-PROBLEM E
- VA-TDI CATEGORY-PROBLEM F
- VA-TDI CATEGORY-PROBLEM G
- VA-TDI CATEGORY-PROBLEM H
- VA-TDI CATEGORY-PROBLEM I
- VA-TDI CATEGORY-PROBLEM J
- VA-TDI CATEGORY-RASH
- VA-TDI CATEGORY-SKIN SCORE

#### Health Factors

- VA-TDI CONSENT NO
- VA-TDI CONSENT YES
- VA-TDI CONSULT NOT POSSIBLE CHOICE 1
- VA-TDI CONSULT NOT POSSIBLE CHOICE 2
- VA-TDI CONSULT NOT POSSIBLE CHOICE 3
- VA-TDI CONSULT REASON 2ND OPINION
- VA-TDI CONSULT REASON DX
- VA-TDI CONSULT REASON OTHER
- VA-TDI CONSULT REASON TX/MANAGE
- VA-TDI CONSULT SKIN BOTHERS TODAY
- VA-TDI CONSULT TRAVEL 0-50 MILE
- VA-TDI CONSULT TRAVEL 051-100 MILE
- VA-TDI CONSULT TRAVEL 101-200 MILE
- VA-TDI CONSULT TRAVEL 201-300 MILE
- VA-TDI CONSULT TRAVEL 300 PLUS MILES
- VA-TDI DERM VISIT NEW CONDITION
- VA-TDI DERM VISIT PRIOR DERM VISIT
- VA-TDI DERM VISIT PRIOR TDI CONSULT
- VA-TDI DX LESION A-ACTINIC KERATOSIS
- VA-TDI EDUCATION DONE
- VA-TDI HX IMAGER COMMENT
- VA-TDI HX IMMUNOSUPPRESSION
- VA-TDI HX NEW MED YES
- VA-TDI HX PROBLEM A BX YES
- VA-TDI HX PROBLEM A CHANGE
- VA-TDI HX PROBLEM A DURATION
- VA-TDI HX PROBLEM A SX
- VA-TDI HX PROBLEM A TX YES
- VA-TDI HX PROBLEM B BX YES
- VA-TDI HX PROBLEM B CHANGE
- VA-TDI HX PROBLEM B DURATION
- VA-TDI HX PROBLEM B SX
- VA-TDI HX PROBLEM B TX YES
- VA-TDI HX PROBLEM C BX YES
- VA-TDI HX PROBLEM C CHANGE
- VA-TDI HX PROBLEM C DURATION
- VA-TDI HX PROBLEM C SX
- VA-TDI HX PROBLEM C TX YES
- VA-TDI HX PROBLEM D BX YES
- VA-TDI HX PROBLEM D CHANGE
- VA-TDI HX PROBLEM D DURATION
- VA-TDI HX PROBLEM D SX
- VA-TDI HX PROBLEM D TX YES
- VA-TDI HX PROBLEM E BX YES
- VA-TDI HX PROBLEM E CHANGE
- VA-TDI HX PROBLEM E DURATION
- VA-TDI HX PROBLEM E SX
- VA-TDI HX PROBLEM E TX YES
- VA-TDI HX PROBLEM F BX YES
- VA-TDI HX PROBLEM F CHANGE
- VA-TDI HX PROBLEM F DURATION
- VA-TDI HX PROBLEM F SX
- VA-TDI HX PROBLEM F TX
- VA-TDI HX PROBLEM G BX YES
- VA-TDI HX PROBLEM G CHANGE
- VA-TDI HX PROBLEM G DURATION
- VA-TDI HX PROBLEM G SX
- VA-TDI HX PROBLEM G TX YES
- VA-TDI HX PROBLEM H BX YES
- VA-TDI HX PROBLEM H CHANGE
- VA-TDI HX PROBLEM H DURATION
- VA-TDI HX PROBLEM H SX
- VA-TDI HX PROBLEM H TX YES
- VA-TDI HX PROBLEM I BX YES
- VA-TDI HX PROBLEM I CHANGE
- VA-TDI HX PROBLEM I DURATION
- VA-TDI HX PROBLEM I SX
- VA-TDI HX PROBLEM I TX YES
- VA-TDI HX PROBLEM J BX YES
- VA-TDI HX PROBLEM J CHANGE
- VA-TDI HX PROBLEM J DURATION
- VA-TDI HX PROBLEM J SX
- VA-TDI HX PROBLEM J TX YES
- VA-TDI HX PROBLEM-MELANOMA FAMILY YES
- VA-TDI HX SKIN CA-BCC YES
- VA-TDI HX SKIN CA-MELANOMA YES
- VA-TDI HX SKIN CA-OTHER/UNKNOWN YES
- VA-TDI HX SKIN CA-SCC YES
- VA-TDI IMAGE QUALITY HIGH
- VA-TDI IMAGE QUALITY IMPROVEMENT
- VA-TDI IMAGE QUALITY INADEQUATE
- VA-TDI LESION A DX-ACTINIC KERATOSIS
- VA-TDI LESION A DX-BCC
- VA-TDI LESION A DX-DYSPLASTIC NEVUS
- VA-TDI LESION A DX-MELANOMA
- VA-TDI LESION A DX-NEOPLASM UNC BEHAVIOR
- VA-TDI LESION A DX-NEVUS
- VA-TDI LESION A DX-NON MALIGNANT TUMOR
- VA-TDI LESION A DX-OTHER MALIGNANT
- VA-TDI LESION A DX-SCC
- VA-TDI LESION A DX-SEB KERATOSIS
- VA-TDI LESION B DX-ACTINIC KERATOSIS
- VA-TDI LESION B DX-BCC
- VA-TDI LESION B DX-DYSPLASTIC NEVUS
- VA-TDI LESION B DX-MELANOMA
- VA-TDI LESION B DX-NEOPLASM UNC BEHAVIOR
- VA-TDI LESION B DX-NEVUS
- VA-TDI LESION B DX-NON MALIGNANT TUMOR
- VA-TDI LESION B DX-OTHER MALIGNANT
- VA-TDI LESION B DX-SCC
- VA-TDI LESION B DX-SEB KERATOSIS
- VA-TDI LESION C DX-ACTINIC KERATOSIS
- VA-TDI LESION C DX-BCC
- VA-TDI LESION C DX-DYSPLASTIC NEVUS
- VA-TDI LESION C DX-MELANOMA
- VA-TDI LESION C DX-NEOPLASM UNC BEHAVIOR
- VA-TDI LESION C DX-NEVUS
- VA-TDI LESION C DX-NON MALIGNANT TUMOR
- VA-TDI LESION C DX-SCC
- VA-TDI LESION C DX-SEB KERATOSIS
- VA-TDI LESION D DX-ACTINIC KERATOSIS
- VA-TDI LESION D DX-BCC
- VA-TDI LESION D DX-DYSPLASTIC NEVUS
- VA-TDI LESION D DX-MELANOMA
- VA-TDI LESION D DX-NEOPLASM UNC BEHAVIOR
- VA-TDI LESION D DX-NEVUS
- VA-TDI LESION D DX-NON MALIGNANT TUMOR
- VA-TDI LESION D DX-OTHER MALIGNANT
- VA-TDI LESION D DX-SCC
- VA-TDI LESION D DX-SEB KERATOSIS
- VA-TDI LESION E DX-ACTINIC KERATOSIS
- VA-TDI LESION E DX-BCC
- VA-TDI LESION E DX-DYSPLASTIC NEVUS
- VA-TDI LESION E DX-MELANOMA
- VA-TDI LESION E DX-NEOPLASM UNC BEHAVIOR
- VA-TDI LESION E DX-NEVUS
- VA-TDI LESION E DX-NON MALIGNANT TUMOR
- VA-TDI LESION E DX-OTHER MALIGNANT
- VA-TDI LESION E DX-SCC
- VA-TDI LESION E DX-SEB KERATOSIS
- VA-TDI LESION F DX-ACTINIC KERATOSIS
- VA-TDI LESION F DX-BCC
- VA-TDI LESION F DX-DYSPLASTIC NEVUS
- VA-TDI LESION F DX-MELANOMA
- VA-TDI LESION F DX-NEOPLASM UNC BEHAVIOR
- VA-TDI LESION F DX-NEVUS
- VA-TDI LESION F DX-NON MALIGNANT TUMOR
- VA-TDI LESION F DX-OTHER MALIGNANT
- VA-TDI LESION F DX-SCC
- VA-TDI LESION F DX-SEB KERATOSIS
- VA-TDI LESION G DX-ACTINIC KERATOSIS
- VA-TDI LESION G DX-BCC
- VA-TDI LESION G DX-DYSPLASTIC NEVUS
- VA-TDI LESION G DX-MELANOMA
- VA-TDI LESION G DX-NEOPLASM UNC BEHAVIOR
- VA-TDI LESION G DX-NEVUS
- VA-TDI LESION G DX-NON MALIGNANT TUMOR
- VA-TDI LESION G DX-OTHER MALIGNANT
- VA-TDI LESION G DX-SCC
- VA-TDI LESION G DX-SEB KERATOSIS
- VA-TDI LESION H DX-ACTINIC KERATOSIS
- VA-TDI LESION H DX-BCC
- VA-TDI LESION H DX-DYSPLASTIC NEVUS
- VA-TDI LESION H DX-MELANOMA
- VA-TDI LESION H DX-NEOPLASM UNC BEHAVIOR
- VA-TDI LESION H DX-NEVUS
- VA-TDI LESION H DX-NON MALIGNANT TUMOR
- VA-TDI LESION H DX-OTHER MALIGNANT
- VA-TDI LESION H DX-SCC
- VA-TDI LESION H DX-SEB KERATOSIS
- VA-TDI LESION I DX-ACTINIC KERATOSIS
- VA-TDI LESION I DX-BCC
- VA-TDI LESION I DX-DYSPLASTIC NEVUS
- VA-TDI LESION I DX-MELANOMA
- VA-TDI LESION I DX-NEOPLASM UNC BEHAVIOR
- VA-TDI LESION I DX-NEVUS
- VA-TDI LESION I DX-NON MALIGNANT TUMOR
- VA-TDI LESION I DX-OTHER MALIGNANT
- VA-TDI LESION I DX-SCC
- VA-TDI LESION I DX-SEB KERATOSIS
- VA-TDI LESION J DX-ACTINIC KERATOSIS
- VA-TDI LESION J DX-BCC
- VA-TDI LESION J DX-DYSPLASTIC NEVUS
- VA-TDI LESION J DX-MELANOMA
- VA-TDI LESION J DX-NEOPLASM UNC BEHAVIOR
- VA-TDI LESION J DX-NEVUS
- VA-TDI LESION J DX-NON MALIGNANT TUMOR
- VA-TDI LESION J DX-OTHER MALIGNANT
- VA-TDI LESION J DX-SCC
- VA-TDI LESION J DX-SEB KERATOSIS
- VA-TDI OTHER DX
- VA-TDI PCP HX PRIOR SKIN DISORDERS
- VA-TDI PCP SIG MED HX
- VA-TDI PROBLEM A LOCATION GENERALIZED
- VA-TDI PROBLEM A LOCATION HEAD/NECK
- VA-TDI PROBLEM A LOCATION LOWER EXTREM
- VA-TDI PROBLEM A LOCATION OTHER
- VA-TDI PROBLEM A LOCATION TRUNK
- VA-TDI PROBLEM A LOCATION UPPER EXTREM
- VA-TDI PROBLEM B LOCATION GENERALIZED
- VA-TDI PROBLEM B LOCATION HEAD/NECK
- VA-TDI PROBLEM B LOCATION LOWER EXTREM
- VA-TDI PROBLEM B LOCATION OTHER
- VA-TDI PROBLEM B LOCATION TRUNK
- VA-TDI PROBLEM B LOCATION UPPER EXTREM
- VA-TDI PROBLEM C LOCATION GENERALIZED
- VA-TDI PROBLEM C LOCATION HEAD/NECK
- VA-TDI PROBLEM C LOCATION LOWER EXTREM
- VA-TDI PROBLEM C LOCATION OTHER
- VA-TDI PROBLEM C LOCATION TRUNK
- VA-TDI PROBLEM C LOCATION UPPER EXTREM
- VA-TDI PROBLEM D LOCATION GENERALIZED
- VA-TDI PROBLEM D LOCATION HEAD/NECK
- VA-TDI PROBLEM D LOCATION LOWER EXTREM
- VA-TDI PROBLEM D LOCATION OTHER
- VA-TDI PROBLEM D LOCATION TRUNK
- VA-TDI PROBLEM D LOCATION UPPER EXTREM
- VA-TDI PROBLEM E LOCATION GENERALIZED
- VA-TDI PROBLEM E LOCATION HEAD/NECK
- VA-TDI PROBLEM E LOCATION LOWER EXTREM
- VA-TDI PROBLEM E LOCATION OTHER
- VA-TDI PROBLEM E LOCATION TRUNK
- VA-TDI PROBLEM E LOCATION UPPER EXTREM
- VA-TDI PROBLEM F LOCATION GENERALIZED
- VA-TDI PROBLEM F LOCATION HEAD/NECK
- VA-TDI PROBLEM F LOCATION LOWER EXTREM
- VA-TDI PROBLEM F LOCATION OTHER
- VA-TDI PROBLEM F LOCATION TRUNK
- VA-TDI PROBLEM F LOCATION UPPER EXTREM
- VA-TDI PROBLEM G LOCATION GENERALIZED
- VA-TDI PROBLEM G LOCATION HEAD/NECK
- VA-TDI PROBLEM G LOCATION LOWER EXTREM
- VA-TDI PROBLEM G LOCATION OTHER
- VA-TDI PROBLEM G LOCATION TRUNK
- VA-TDI PROBLEM G LOCATION UPPER EXTREM
- VA-TDI PROBLEM H LOCATION GENERALIZED
- VA-TDI PROBLEM H LOCATION HEAD/NECK
- VA-TDI PROBLEM H LOCATION LOWER EXTREM
- VA-TDI PROBLEM H LOCATION OTHER
- VA-TDI PROBLEM H LOCATION TRUNK
- VA-TDI PROBLEM H LOCATION UPPER EXTREM
- VA-TDI PROBLEM I LOCATION GENERALIZED
- VA-TDI PROBLEM I LOCATION HEAD/NECK
- VA-TDI PROBLEM I LOCATION LOWER EXTREM
- VA-TDI PROBLEM I LOCATION OTHER
- VA-TDI PROBLEM I LOCATION TRUNK
- VA-TDI PROBLEM I LOCATION UPPER EXTREM
- VA-TDI PROBLEM J LOCATION GENERALIZED
- VA-TDI PROBLEM J LOCATION HEAD/NECK
- VA-TDI PROBLEM J LOCATION LOWER EXTREM
- VA-TDI PROBLEM J LOCATION OTHER
- VA-TDI PROBLEM J LOCATION TRUNK
- VA-TDI PROBLEM J LOCATION UPPER EXTREM
- VA-TDI RASH DX-DRUG
- VA-TDI RASH DX-ECZEMA
- VA-TDI RASH DX-INFECTION
- VA-TDI RASH DX-MALIGNANCY
- VA-TDI RASH DX-OTHER
- VA-TDI RASH DX-PSORIASIS
- VA-TDI RASH DX-SEBORRHEIC DERMATITIS
- VA-TDI READER FOLLOW UP NOT REQ
- VA-TDI READER TX BIOPSY LESION A
- VA-TDI READER TX BIOPSY LESION B
- VA-TDI READER TX BIOPSY LESION C
- VA-TDI READER TX BIOPSY LESION D
- VA-TDI READER TX BIOPSY LESION E
- VA-TDI READER TX BIOPSY LESION F
- VA-TDI READER TX BIOPSY LESION G
- VA-TDI READER TX BIOPSY LESION H
- VA-TDI READER TX BIOPSY LESION I
- VA-TDI READER TX BIOPSY LESION J
- VA-TDI READER TX BIOPSY OTHER
- VA-TDI READER TX BIOPSY RASH
- VA-TDI READER TX CULTURES LESION A
- VA-TDI READER TX CULTURES LESION B
- VA-TDI READER TX CULTURES LESION C
- VA-TDI READER TX CULTURES LESION D
- VA-TDI READER TX CULTURES LESION E
- VA-TDI READER TX CULTURES LESION F
- VA-TDI READER TX CULTURES LESION G
- VA-TDI READER TX CULTURES LESION H
- VA-TDI READER TX CULTURES LESION I
- VA-TDI READER TX CULTURES LESION J
- VA-TDI READER TX CULTURES OTHER
- VA-TDI READER TX CULTURES RASH
- VA-TDI READER TX MEDS ADD LESION A
- VA-TDI READER TX MEDS ADD LESION B
- VA-TDI READER TX MEDS ADD LESION C
- VA-TDI READER TX MEDS ADD LESION D
- VA-TDI READER TX MEDS ADD LESION E
- VA-TDI READER TX MEDS ADD LESION F
- VA-TDI READER TX MEDS ADD LESION G
- VA-TDI READER TX MEDS ADD LESION H
- VA-TDI READER TX MEDS ADD LESION I
- VA-TDI READER TX MEDS ADD LESION J
- VA-TDI READER TX MEDS ADD OTHER
- VA-TDI READER TX MEDS ADD RASH
- VA-TDI READER TX MEDS LESION A
- VA-TDI READER TX MEDS LESION B
- VA-TDI READER TX MEDS LESION C
- VA-TDI READER TX MEDS LESION D
- VA-TDI READER TX MEDS LESION E
- VA-TDI READER TX MEDS LESION F
- VA-TDI READER TX MEDS LESION G
- VA-TDI READER TX MEDS LESION H
- VA-TDI READER TX MEDS LESION I
- VA-TDI READER TX MEDS LESION J
- VA-TDI READER TX MEDS OTHER
- VA-TDI READER TX MEDS RASH
- VA-TDI READER TX OTHER LESION A
- VA-TDI READER TX OTHER LESION B
- VA-TDI READER TX OTHER LESION C
- VA-TDI READER TX OTHER LESION D
- VA-TDI READER TX OTHER LESION E
- VA-TDI READER TX OTHER LESION F
- VA-TDI READER TX OTHER LESION G
- VA-TDI READER TX OTHER LESION H
- VA-TDI READER TX OTHER LESION I
- VA-TDI READER TX OTHER LESION J
- VA-TDI READER TX OTHER OTHER COND
- VA-TDI READER TX OTHER RASH
- VA-TDI READER TX RECOMMEND NONE
- VA-TDI READER TX SKIN CARE LESION A
- VA-TDI READER TX SKIN CARE LESION B
- VA-TDI READER TX SKIN CARE LESION C
- VA-TDI READER TX SKIN CARE LESION D
- VA-TDI READER TX SKIN CARE LESION E
- VA-TDI READER TX SKIN CARE LESION F
- VA-TDI READER TX SKIN CARE LESION G
- VA-TDI READER TX SKIN CARE LESION H
- VA-TDI READER TX SKIN CARE LESION I
- VA-TDI READER TX SKIN CARE LESION J
- VA-TDI READER TX SKIN CARE OTHER
- VA-TDI READER TX SKIN CARE RASH
- VA-TDI READER UNABLE TO ASSESS
- VA-TDI RECONSULT TELEDERM 1 MO
- VA-TDI RECONSULT TELEDERM 1 WK
- VA-TDI RECONSULT TELEDERM 12 MO
- VA-TDI RECONSULT TELEDERM 3 MO
- VA-TDI RECONSULT TELEDERM 6 MO
- VA-TDI REFER DERM 1 MO
- VA-TDI REFER DERM 1 WK
- VA-TDI REFER DERM 12 MO
- VA-TDI REFER DERM 3 MO
- VA-TDI REFER DERM 6 MO
- VA-TDI REFER DERMATOLOGY
- VA-TDI RETURN PCC F/U 1 MO
- VA-TDI RETURN PCC F/U 1 WK
- VA-TDI RETURN PCC F/U 3 MO
- VA-TDI RETURN PCC F/U 6 MO
- VA-TDI RETURN PCC F/U OTHER
- VA-TDI SKIN CONDITION SCORES

> <span id="_bookmark18" class="anchor"></span><u>Acronyms</u>

### The OIT Master Glossary is available at [<u>http://vaww.oed.wss.va.gov/process/Library/master_glossary/masterglossary.htm</u>](http://vaww.oed.wss.va.gov/process/Library/master_glossary/masterglossary.htm)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### CAC – Clinical Applications Coordinator

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### CDC – Centers for Disease Control and Prevention

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### CPRS – Computerized Patient Record System, previous version dating back to 1997 was CPRS List Manager (VistA terminal emulation only) and no longer supported but is still accessible in VISTA. CPRS GUI is the Windows version (since 1998), and is now called just CPRS - [<u>CPRS page on VDL web site</u>](http://www.va.gov/vdl/application.asp?appid=61)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### CWAD – Special note titles that display in the POSTINGS window in the CPRS header. Each letter stands for a category: C = Crisis Notes; W = Clinical Warnings; A = Allergies/Adverse Drug Reactions (ADR); D = Advance Directives

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Data Object – also called a ‘Patient Data Object’ or just as ‘object’. These are either created by programmer (OI&T staff), or a CAC/HIS can create (TIU-HS object).

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Dialog- A window in CPRS that opens in the format of a form to aid the user in creating text in a note and entering information into the record with a point and click interface.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Elements- A component in VistA that is configured to display content for the user when a dialog is opened.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### EVD – Ebola Virus Disease

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### FAQ – Frequently Asked Questions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### FORUM – the VA’s WAN (Wide Area Network), for mail, patch trackers, E3R repository

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### GUI – Graphical User Interface, referring to a Windows application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### GUI Dialog Template/GUI Dialog - a CPRS template (plain text), TXML format, icons ![](pxrm-2-41-teledermatology-imager-note-and-reader-note-install-guide/005.png) ![](pxrm-2-41-teledermatology-imager-note-and-reader-note-install-guide/006.png) Health Factor- Informational data marker entered into the record to document patient information that is not readily identifiable with other information data entries in the system.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Health Factors are used in TIU-Health Summary objects, in Health Summary types, and for data capture (for VA Fileman queries/reports, VISN data warehouse data pulls, etc.)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### HIS – Health Informatics Specialist, another title for Clinical Applications Coordinator (CAC) with same responsibilities as a CAC.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Health Summary (HS) – a clinical module (package) in VistA; GMTS is the package’s name spacing - [<u>Health Summary page on VDL web site</u>](http://www.va.gov/vdl/application.asp?appid=63)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Health Summary Types/Objects - A collection of data that displays to the user specific to the patient’s chart they are viewing.

### Health Summary Type – a configuration of health summary components used as the basis of a report viewed in VISTA or the CPRS GUI, or used in a TIU-Health Summary object

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Health Summary Object – the display settings of a Health Summary Type which is part of a TIU-Health Summary Object configuration.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Health Summary Component – an item that is used to create a health summary type (i.e., report). Health Summary components can be viewed via \[GMTS HS ADHOC\], or "List Health Summary Components \[GMTS COMP LIST\]", or "List Health Summary Component Descriptions \[GMTS COMP DESC LIST\]".

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Host file – the file that is created in the reminder exchange option using .prd (Packed Reminder Definition format

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### KIDS- Kernel Installation Distribution System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Mapping - Linking of data markers such as Health Factors or other data entry items to reminder components such as reminder elements.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Name spacing – the prefixing, i.e., the initial 3-4 leading characters of a module or items in VistA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### National Class - The highest collection of edit permissions which can be assigned to an item (versus VISN or LOCAL)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### NCRC – National Clinical Reminder Committee

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### OPH – Office of Public Health

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### OIA – Office of Information and Analytics

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### OPC – Office of Primary Care

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Packing List – the list of included items of a reminder exchange export when viewed from the ‘IFE’ action in the reminder exchange VISTA option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### PCE – Patient Care Encounter (link to VDL web page)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### PRD - .pdf file = Packed Reminder Definition (the alternate format for sending/receiving reminder exchange exports).

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### PXRM – namespace for the clinical reminders module - [<u>clinical reminders page on VDL web</u>](http://www.va.gov/vdl/application.asp?appid=60) [<u>site</u>](http://www.va.gov/vdl/application.asp?appid=60)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Reminder Taxonomy- Collection of specific codes associated with specific clinical conditions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Template- Commonly referred to as a dialog. See dialog for definition

### Reminder Dialog ![](pxrm-2-41-teledermatology-imager-note-and-reader-note-install-guide/007.png) - a template created in \[PXRM DIALOG/COMPONENT EDIT\]; can be used without reminder logic (reminder definition)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Reminder Dialog Template ![](pxrm-2-41-teledermatology-imager-note-and-reader-note-install-guide/008.png) - a template created in \[PXRM DIALOG/COMPONENT EDIT\] and used in CPRS without linked reminder logic (reminder definition), either as a stand-alone template or the template is linked to a note title. Sometimes also referred to as a ‘reminder template’.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Reminder Definition – used to create reminder logic for a clinical reminder or data object or reminder order check in PXRM REMINDER MANAGEMENT\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Reminder Exchange – the VISTA option \[PXRM REMINDER EXCHANGE\] used to create a reminder exchange message or .prd host file

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Reminder Exchange Export – either a reminder exchange message or a .prd file moved out of the Reminder Exchange option in VISTA

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Shared Templates- ![](pxrm-2-41-teledermatology-imager-note-and-reader-note-install-guide/009.png)Templates within the shared templates tree of CPRS, which the users can access and use while documenting in the chart

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### SHOP-ALL – a destination through the VA’s FORUM to access and download reminder exchange messages that have been posted and stored (uses Mailman; must have FORUM access)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### TIU -Text Integrated Utility, the notes repository (clinical package) in VISTA - [<u>TIU page on</u>](http://www.va.gov/vdl/application.asp?appid=65) [<u>VDL web site</u>](http://www.va.gov/vdl/application.asp?appid=65)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### TIU Document Definition – it can be a CLASS, DOCUMENT CLASS, TITLE or OBJECT (file \#8925.1). The reminder exchange packing list shows the TIU object labeled as “TIU DOCUMENT DEFINITION”.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> TIU-Health Summary Object (also known as a TIU-HS OBJECT) – [<u>TIU page on VDL web</u>](http://www.va.gov/vdl/application.asp?appid=65) [<u>site</u>](http://www.va.gov/vdl/application.asp?appid=65)

### TIU Object – a data object /patient data object (but too general a term to know if this is programmer-created or CAC/HIS-created). See DATA OBJECT above.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> TIU Template – a TXML template (see TXML or GUI Dialog).

### TXML - the file format of ‘plain text’ CPRS templates, aka “GUI dialogs” or “GUI Dialog Templates”. Uses the CPRS GUI Template Editor to create and edit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> TIU TEMPLATE FIELD file - file \#8927 in VISTA, where TIU template fields are stored

> TIU TEMPLATE file – file \#8927 in VISTA, where TXML templates are stored

### User Acceptance Testing - (UAT) critical software testing where end-users test the software in real- world scenarios before it is nationally released

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### URL – Uniform Resource Locator, i.e., a specific web address (Internet or Intranet)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Usability Testing- evaluating the software by testing with a representation of users that follow specific tasks (test scripts), identify problems, suggest improvements and determine the user’s satisfaction with the product.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### VDL –The Internet page for all VISTA manuals and documentation [<u>VistA Documentation Library</u>](http://www.va.gov/vdl/)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### VMP- VistA Maintenance Project

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### <u>\[return to table of contents\]</u>
<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)