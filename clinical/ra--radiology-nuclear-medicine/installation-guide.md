---
title: Radiology Version 5 Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: 
app_code: RA
app_name: Radiology/Nuclear Medicine
section: CLI
app_status: archive
pkg_ns: RA
patch_ver: 5
patch_id: RA*5
group_key: "RA:RA:5"
file_numbers: 
  - 79
security_keys: []
menu_options: 4
description: - [Department of Veterans Affairs Veterans Health Administration Office of Chief Information Officer](#department-of-veterans-affairs-veterans-health-administration-office-of-chief-information-officer) - [Installation Information](#installation-information) - [This package was created using Kernel V
audience: 
keywords: 
  - blockquote
  - table
  - contents
  - class
  - mail
  - installation
  - strong
  - package
  - install
  - medicine
page_count: 0
word_count: 7930
section_count: 4
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: April 1998
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Radiology_Nuclear_Med_Archive/ra5_0ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Radiology_Nuclear_Med_Archive/ra5_0ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=384"
---

> ![](radiology-version-5-installation-guide/001.png)

RADIOLOGY / NUCLEAR MEDICINE INSTALLATION GUIDE

> Version 5.0

> April 1998

### Department of Veterans Affairs Veterans Health Administration Office of Chief Information Officer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Installation Information


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

    - [Department of Veterans Affairs Veterans Health Administration Office of Chief Information Officer](#department-of-veterans-affairs-veterans-health-administration-office-of-chief-information-officer)
- [Installation Information](#installation-information)
    - [This package was created using Kernel V. 8.0 and VA FileMan V. 21.0 and requires the following external software:](#this-package-was-created-using-kernel-v-80-and-va-fileman-v-210-and-requires-the-following-external-software)
    - [Minimum](#minimum)
    - [<u>Package Name</u> <u>Required Version</u>](#upackage-nameu-urequired-versionu)
    - [VA FileMan 21.0](#va-fileman-210)
    - [Kernel 8.0](#kernel-80)
    - [MailMan 7.1](#mailman-71)
    - [PIMS 5.3](#pims-53)
    - [Health Level Seven 1.6](#health-level-seven-16)
    - [Adverse Reaction Tracking 3.0](#adverse-reaction-tracking-30)
    - [OE/RR 2.5](#oerr-25)
    - [PCE 1.0](#pce-10)
  - [Pre-installation](#pre-installation)
    - [Coordinate the installation with your ADPAC. There are many enhancements to this version, some requiring up front preparation by the ADPAC before this version is installed. For example, if the nuclear medicine data collection features are going to be used, the ADPAC will have to work with the Pharmacy ADPAC to make sure all radiopharmaceuticals used at the site have been added to the Drug file \#50. (See the Radiology/Nuclear Medicine ADPAC Guide, Implementation Check List.)](#coordinate-the-installation-with-your-adpac-there-are-many-enhancements-to-this-version-some-requiring-up-front-preparation-by-the-adpac-before-this-version-is-installed-for-example-if-the-nuclear-medicine-data-collection-features-are-going-to-be-used-the-adpac-will-have-to-work-with-the-pharmacy-adpac-to-make-sure-all-radiopharmaceuticals-used-at-the-site-have-been-added-to-the-drug-file-50-see-the-radiologynuclear-medicine-adpac-guide-implementation-check-list)
    - [The package will be installed using Kernel Installation and Distribution system (KIDS).](#the-package-will-be-installed-using-kernel-installation-and-distribution-system-kids)
    - [Make certain at least patches RA\4.5\2, RA\4.5\10, and DI\21.0\41 are installed prior to installing this version of the software. (If this is a virgin installation, you may skip patches RA\4.5\2 and RA\4.5\10.)](#make-certain-at-least-patches-ra452-ra4510-and-di21041-are-installed-prior-to-installing-this-version-of-the-software-if-this-is-a-virgin-installation-you-may-skip-patches-ra452-and-ra4510)
    - [Cardiology Studies (Nuc Med) Nuclear Medicine](#cardiology-studies-nuc-med-nuclear-medicine)
    - [If they do not exist, try to determine how and why these entries were corrupted and make the necessary corrections. The environment check routine](#if-they-do-not-exist-try-to-determine-how-and-why-these-entries-were-corrupted-and-make-the-necessary-corrections-the-environment-check-routine)
    - [Schedule downtime with the package and any interface users ( e.g., any PACS/ Imaging or voice recognition system users). This installation will put RA namespaced options and protocols out of service for the duration of the installation. Please refer to the Test Site Install Times chart, page 23, for a sampling of installation and cleanup times. The cleanup runs in the background so users can go back on the system while it is running. The cleanup run time depends largely on how many entries are in File \#74.4.](#schedule-downtime-with-the-package-and-any-interface-users-eg-any-pacs-imaging-or-voice-recognition-system-users-this-installation-will-put-ra-namespaced-options-and-protocols-out-of-service-for-the-duration-of-the-installation-please-refer-to-the-test-site-install-times-chart-page-23-for-a-sampling-of-installation-and-cleanup-times-the-cleanup-runs-in-the-background-so-users-can-go-back-on-the-system-while-it-is-running-the-cleanup-run-time-depends-largely-on-how-many-entries-are-in-file-744)
    - [Six bulletins are exported with this package. These bulletins are generated when an important action happens, such as the deletion of an exam. Consult with the package ADPAC to determine how many Radiology/Nuclear Medicine package related mail groups should exist and what mail group(s) should be associated with each bulletin and who the mail group members should be. If this is not a virgin installation, you may not need to make any changes. For more information on bulletins and mail groups, see page 19 of this manual.](#six-bulletins-are-exported-with-this-package-these-bulletins-are-generated-when-an-important-action-happens-such-as-the-deletion-of-an-exam-consult-with-the-package-adpac-to-determine-how-many-radiologynuclear-medicine-package-related-mail-groups-should-exist-and-what-mail-groups-should-be-associated-with-each-bulletin-and-who-the-mail-group-members-should-be-if-this-is-not-a-virgin-installation-you-may-not-need-to-make-any-changes-for-more-information-on-bulletins-and-mail-groups-see-page-19-of-this-manual)
    - [Use the Distribution Queue Purge \[RA RPTDISTPURGE\] option to purge distribution files of printed reports in the Report Distribution Queue file \#74.3. This will help to minimize the CPU time needed to run the clean-up programs. The entries in this file are only pointers to the real report records. Sites not using distribution queues may have zero entries in this file. If there are zero entries in File \#74.3, skip to step 9.](#use-the-distribution-queue-purge-ra-rptdistpurge-option-to-purge-distribution-files-of-printed-reports-in-the-report-distribution-queue-file-743-this-will-help-to-minimize-the-cpu-time-needed-to-run-the-clean-up-programs-the-entries-in-this-file-are-only-pointers-to-the-real-report-records-sites-not-using-distribution-queues-may-have-zero-entries-in-this-file-if-there-are-zero-entries-in-file-743-skip-to-step-9)
    - [After the purge completes, determine the number of entries in the Report Distribution file \#74.4. Using the VA FileMan Inquire option, enter "74.4" at the Output From What File prompt. VA FileMan should display the number of entries in the file. Use an "^" to exit the option. If you have a large number of entries (e.g., \>10,000), you may want to use the Rebuild Distribution Queues \[RA RPTDISTREBUILD\] option and enter a date within the last 45 days. The purpose of this is to reduce the volume of data that must be processed by the clean-up programs.](#after-the-purge-completes-determine-the-number-of-entries-in-the-report-distribution-file-744-using-the-va-fileman-inquire-option-enter-744-at-the-output-from-what-file-prompt-va-fileman-should-display-the-number-of-entries-in-the-file-use-an-to-exit-the-option-if-you-have-a-large-number-of-entries-eg-10000-you-may-want-to-use-the-rebuild-distribution-queues-ra-rptdistrebuild-option-and-enter-a-date-within-the-last-45-days-the-purpose-of-this-is-to-reduce-the-volume-of-data-that-must-be-processed-by-the-clean-up-programs)
    - [Use the global placement utilities to create and place the new ^RADPTN global.](#use-the-global-placement-utilities-to-create-and-place-the-new-radptn-global)
    - [For multiple cpu's the following globals must be translated:](#for-multiple-cpus-the-following-globals-must-be-translated)
  - [Installation Instructions](#installation-instructions)
    - [This guide can be used to install the package into either a test or production account. The following table indicates which steps are appropriate for the installation. You will probably wish to install the package in your test account first.](#this-guide-can-be-used-to-install-the-package-into-either-a-test-or-production-account-the-following-table-indicates-which-steps-are-appropriate-for-the-installation-you-will-probably-wish-to-install-the-package-in-your-test-account-first)
    - [very large numbers of records in Files \#74.4, \#70, and \#74. Use the KIDS Install File Print option under the Utilities Menu to check on the progress and completion of the cleanup install. If there are errors, you should fix the data problems, then restart the cleanup install through the KIDS Restart Install of Package(s) option.](#very-large-numbers-of-records-in-files-744-70-and-74-use-the-kids-install-file-print-option-under-the-utilities-menu-to-check-on-the-progress-and-completion-of-the-cleanup-install-if-there-are-errors-you-should-fix-the-data-problems-then-restart-the-cleanup-install-through-the-kids-restart-install-of-packages-option)
    - [reports (see Implementation and Maintenance section of the technical manual for more information on how you can do this),](#reports-see-implementation-and-maintenance-section-of-the-technical-manual-for-more-information-on-how-you-can-do-this)
    - [The KIDS Distributions, ^XTMP("XQOO", "RADIOLOGY/NUCLEAR MEDICINE CLEANUP 5.0") and ^XTMP("XQOO","RADIOLOGY/NUCLEAR MEDICINE 5.0"),](#the-kids-distributions-xtmpxqoo-radiologynuclear-medicine-cleanup-50-and-xtmpxqooradiologynuclear-medicine-50)
    - [occupy approximately 2 megabytes of disk space and are deleted upon successful completion of the installation process.](#occupy-approximately-2-megabytes-of-disk-space-and-are-deleted-upon-successful-completion-of-the-installation-process)
    - [Use the KIDS Build File Print option if you wish to obtain a complete listing of package components (e.g., routines and options) sent with this Distribution file.](#use-the-kids-build-file-print-option-if-you-wish-to-obtain-a-complete-listing-of-package-components-eg-routines-and-options-sent-with-this-distribution-file)
    - [Use the KIDS Install File Print option if you wish to print out the results of the installation process. You will need to retrieve the two install results separately.](#use-the-kids-install-file-print-option-if-you-wish-to-print-out-the-results-of-the-installation-process-you-will-need-to-retrieve-the-two-install-results-separately)
    - [A summary of installation times at the test sites can be found on page 23.](#a-summary-of-installation-times-at-the-test-sites-can-be-found-on-page-23)
    - [Please refer to the Health Level Seven package documentation and the Radiology/Nuclear Medicine Technical manual to set up and maintain](#please-refer-to-the-health-level-seven-package-documentation-and-the-radiologynuclear-medicine-technical-manual-to-set-up-and-maintain)
    - [Radiology/Nuclear Medicine interfaces with non-VISTA systems (e.g., voice recognition systems and PACS systems).](#radiologynuclear-medicine-interfaces-with-non-vista-systems-eg-voice-recognition-systems-and-pacs-systems)
    - [Note: If you run an XINDEX or %INDEX, you may run into several errors caused by references to routines not in the UCI if the imaging package and/or OE/RR V. 3.0 (CPRS) are not yet installed or released. These errors are benign and do not affect the operation of the Radiology/Nuclear Medicine package. Routines involved are:](#note-if-you-run-an-xindex-or-index-you-may-run-into-several-errors-caused-by-references-to-routines-not-in-the-uci-if-the-imaging-package-andor-oerr-v-30-cprs-are-not-yet-installed-or-released-these-errors-are-benign-and-do-not-affect-the-operation-of-the-radiologynuclear-medicine-package-routines-involved-are)
    - [There will also be a false warning for RAUTL8. This occurs because XINDEX and](#there-will-also-be-a-false-warning-for-rautl8-this-occurs-because-xindex-and)
    - [%INDEX can't recognize that a second line label is still part of an extrinsic function and is not called separately from the extrinsic function.](#index-cant-recognize-that-a-second-line-label-is-still-part-of-an-extrinsic-function-and-is-not-called-separately-from-the-extrinsic-function)
- [Installation Over Version 4.5 (Example)](#installation-over-version-45-example)
    - [The following example is taken from an installation on an Open M system. Quotes enclosing messages may not appear on your system and messages may change depending on the data at your facility.](#the-following-example-is-taken-from-an-installation-on-an-open-m-system-quotes-enclosing-messages-may-not-appear-on-your-system-and-messages-may-change-depending-on-the-data-at-your-facility)
- [Mail Groups and Bulletins](#mail-groups-and-bulletins)
    - [This chapter discusses creating mail groups and associating those mail groups to the package's six bulletins. These bulletins are generated when important actions take place (e.g., the deletion of an exam) and are sent to members of a mail group who should be aware that the action took place. The names of the bulletins are:](#this-chapter-discusses-creating-mail-groups-and-associating-those-mail-groups-to-the-packages-six-bulletins-these-bulletins-are-generated-when-important-actions-take-place-eg-the-deletion-of-an-exam-and-are-sent-to-members-of-a-mail-group-who-should-be-aware-that-the-action-took-place-the-names-of-the-bulletins-are)
    - [RAD/NUC MED REQUEST CANCELLED RAD/NUC MED EXAM DELETED RAD/NUC MED REPORT DELETION RAD/NUC MED REPORT UNVERIFIED RAD/NUC MED CREDIT FAILURE RAD/NUC MED REQUEST HELD](#radnuc-med-request-cancelled-radnuc-med-exam-deleted-radnuc-med-report-deletion-radnuc-med-report-unverified-radnuc-med-credit-failure-radnuc-med-request-held)
    - [To find out what mail groups are associated with these bulletins and who belongs to those mail groups, you can do a VA FileMan sort and print. The following is an example of a sort and print that can be run before or after the installation of this new version.](#to-find-out-what-mail-groups-are-associated-with-these-bulletins-and-who-belongs-to-those-mail-groups-you-can-do-a-va-fileman-sort-and-print-the-following-is-an-example-of-a-sort-and-print-that-can-be-run-before-or-after-the-installation-of-this-new-version)
    - [Consult with the package ADPAC to determine how many mail groups to create, what mail group(s) you wish to associate with each bulletin, and who should be the coordinator for each mail group.](#consult-with-the-package-adpac-to-determine-how-many-mail-groups-to-create-what-mail-groups-you-wish-to-associate-with-each-bulletin-and-who-should-be-the-coordinator-for-each-mail-group)
    - [The following are suggestions for setting up six mail groups, one for each bulletin.](#the-following-are-suggestions-for-setting-up-six-mail-groups-one-for-each-bulletin)
    - [Bulletin Name: RAD/NUC MED REQUEST CANCELLED](#bulletin-name-radnuc-med-request-cancelled)
    - [Bulletin Name: RAD/NUC MED EXAM DELETED](#bulletin-name-radnuc-med-exam-deleted)
    - [Bulletin Name: RAD/NUC MED REPORT DELETION <u>Mail Group (#3.8) field name</u> <u>Suggested value</u>](#bulletin-name-radnuc-med-report-deletion-umail-group-38-field-nameu-usuggested-valueu)
    - [NAME RA REPORT DELETION](#name-ra-report-deletion)
    - [TYPE Public](#type-public)
    - [RESTRICTIONS Unrestricted](#restrictions-unrestricted)
    - [DESCRIPTION The members of this mail group will receive a bulletin when a Radiology/Nuclear Medicine report is deleted.](#description-the-members-of-this-mail-group-will-receive-a-bulletin-when-a-radiologynuclear-medicine-report-is-deleted)
    - [Bulletin Name: RAD/NUC MED REPORT UNVERIFIED <u>Mail Group (#3.8) field name</u> <u>Suggested value</u>](#bulletin-name-radnuc-med-report-unverified-umail-group-38-field-nameu-usuggested-valueu)
    - [NAME RA REPORT UNVERIFIED](#name-ra-report-unverified)
    - [TYPE Public](#type-public-1)
    - [RESTRICTIONS Unrestricted](#restrictions-unrestricted-1)
    - [DESCRIPTION The members of this mail group will receive a bulletin when a Radiology/Nuclear Medicine report is changed from Verified to any other status.](#description-the-members-of-this-mail-group-will-receive-a-bulletin-when-a-radiologynuclear-medicine-report-is-changed-from-verified-to-any-other-status)
    - [Bulletin Name: RAD/NUC MED REQUEST HELD](#bulletin-name-radnuc-med-request-held)
    - [Bulletin Name: RAD/NUC MED CREDIT FAILURE](#bulletin-name-radnuc-med-credit-failure)
    - [The following is an example of creating a mail group.](#the-following-is-an-example-of-creating-a-mail-group)
    - [The following is an example of associating a mail group with a bulletin.](#the-following-is-an-example-of-associating-a-mail-group-with-a-bulletin)
- [Test Site Install Times](#test-site-install-times)
  - [Install Times from Test Sites](#install-times-from-test-sites)

### This package was created using Kernel V. 8.0 and VA FileMan V. 21.0 and requires the following external software:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Minimum

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### <u>Package Name</u> <u>Required Version</u>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### VA FileMan 21.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Kernel 8.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### MailMan 7.1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### PIMS 5.3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Health Level Seven 1.6

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Adverse Reaction Tracking 3.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### OE/RR 2.5

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### PCE 1.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Pre-installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Coordinate the installation with your ADPAC. There are many enhancements to this version, some requiring up front preparation by the ADPAC before this version is installed. For example, if the nuclear medicine data collection features are going to be used, the ADPAC will have to work with the Pharmacy ADPAC to make sure all radiopharmaceuticals used at the site have been added to the Drug file \#50. (See the Radiology/Nuclear Medicine ADPAC Guide, Implementation Check List.)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### The package will be installed using Kernel Installation and Distribution system (KIDS).

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Make certain at least patches RA\*4.5\*2, RA\*4.5\*10, and DI\*21.0\*41 are installed prior to installing this version of the software. (If this is a virgin installation, you may skip patches RA\*4.5\*2 and RA\*4.5\*10.)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  If this is a virgin installation, you may skip this step. Make certain the following entries are among those in the Imaging Type file \#79.2:

### Cardiology Studies (Nuc Med) Nuclear Medicine

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### If they do not exist, try to determine how and why these entries were corrupted and make the necessary corrections. The environment check routine

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> requires the conditions in both steps 3 and 4 in order to run the installation.

### Schedule downtime with the package and any interface users ( e.g., any PACS/ Imaging or voice recognition system users). This installation will put RA namespaced options and protocols out of service for the duration of the installation. Please refer to the Test Site Install Times chart, page [23,](#test-site-install-times) for a sampling of installation and cleanup times. The cleanup runs in the background so users can go back on the system while it is running. The cleanup run time depends largely on how many entries are in File \#74.4.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Six bulletins are exported with this package. These bulletins are generated when an important action happens, such as the deletion of an exam. Consult with the package ADPAC to determine how many Radiology/Nuclear Medicine package related mail groups should exist and what mail group(s) should be associated with each bulletin and who the mail group members should be. If this is not a virgin installation, you may not need to make any changes. For more information on bulletins and mail groups, see page [19](#mail-groups-and-bulletins) of this manual.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Use the Distribution Queue Purge \[RA RPTDISTPURGE\] option to purge distribution files of printed reports in the Report Distribution Queue file \#74.3. This will help to minimize the CPU time needed to run the clean-up programs. The entries in this file are only pointers to the real report records. Sites not using distribution queues may have zero entries in this file. If there are zero entries in File \#74.3, skip to step 9.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### After the purge completes, determine the number of entries in the Report Distribution file \#74.4. Using the VA FileMan Inquire option, enter "74.4" at the Output From What File prompt. VA FileMan should display the number of entries in the file. Use an "^" to exit the option. If you have a large number of entries (e.g., \>10,000), you may want to use the Rebuild Distribution Queues \[RA RPTDISTREBUILD\] option and enter a date within the last 45 days. The purpose of this is to reduce the volume of data that must be processed by the clean-up programs.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Use the global placement utilities to create and place the new ^RADPTN global.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### For multiple cpu's the following globals must be translated:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> ^RA

> ^RABTCH

> ^RADPT

> ^RADPTN (new global)

> ^RAMIS

> ^RAO

> ^RARPT

> 2 Radiology/Nuclear Medicine V. 5.0 April 1998

## Installation Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### This guide can be used to install the package into either a test or production account. The following table indicates which steps are appropriate for the installation. You will probably wish to install the package in your test account first.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 69%" />
<col style="width: 10%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><u>Step</u></p>
</blockquote></th>
<th><blockquote>
<p><u>Description</u></p>
</blockquote></th>
<th><blockquote>
<p><u>Test</u></p>
</blockquote></th>
<th><blockquote>
<p><u>Prod</u></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1.</p>
</blockquote></td>
<td><blockquote>
<p>Make sure the Radiology/Nuclear Medicine (or Imaging Service) and voice recognition system users are off the system. Clinicians should stop ordering Rad/Nuc Med procedures during the install.</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>P</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2.</p>
</blockquote></td>
<td><blockquote>
<p>Backup the system.</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>P</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>3.</p>
</blockquote></td>
<td><blockquote>
<p>Disable Mapping for RA* routines, if applicable.</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>P</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>4.</p>
</blockquote></td>
<td><blockquote>
<p>Disable journaling, if applicable (RA* globals).</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>P</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>5.</p>
</blockquote></td>
<td><blockquote>
<p>Stop all tasked jobs in the RA* namespace. Taskman should be up and running during this install.</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>P</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>6.</p>
</blockquote></td>
<td><blockquote>
<p>Manually disable the RA SIGN-ON MSG option. This must be done prior to the install to prevent errors during sign-on for other users.</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>P</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>7.</p>
</blockquote></td>
<td><blockquote>
<p>Delete old package routines from all your systems (optional). You may wish to delete existing RA namespaced routines. Also, remember not to delete any locally created routines (e.g., RAZ*). Use the routine deletion method you are most comfortable with.</p>
<p>Example:</p>
<p><strong>D ^%RDELETE</strong></p>
<p>ROUTINE DELETE</p>
<p>routine (s) ? &gt; <strong>RA*</strong></p>
<p>routine (s) ? &gt; -<strong>RAZ*</strong> (On Open M, 'RAZ*) routine (s) ? &gt; <strong>&lt;RET&gt;</strong></p>
<p>nnn routines to DELETE, OK: NO// <strong>YES</strong> (On Open M, you get a Device: prompt)</p>
</blockquote></td>
<td>T</td>
<td><blockquote>
<p>P</p>
</blockquote></td>
</tr>
</tbody>
</table>

> April 1998 Radiology/Nuclear Medicine V. 5.0 3

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 72%" />
<col style="width: 10%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>8.</p>
</blockquote></th>
<th><blockquote>
<p>Sign into the account where the package is installed. Make certain your DUZ variable is set to a valid user number and DUZ(0) equals "@". <strong>The environment check routine requires this.</strong> Invoke the KIDS menu (XPD Installation Menu option).</p>
<p>There are two (2) builds that must be loaded. Only one build needs to be installed - it queues the cleanup.</p>
<p>First, use the Load a Distribution option to load:</p>
<p><strong>RAD5_0CLN.KID</strong></p>
<p><strong>The environment check routine requires this.</strong></p>
<p>Then use the same option to load: <strong>RAD5_0.KID</strong></p>
<p>Use the Install Package(s) option to install:</p>
<p><strong>RADIOLOGY/NUCLEAR MEDICINE 5.0</strong></p>
<p>This installation assumes TaskMan is running.</p>
<p>Note: The installation example dialogue that follows may vary depending on the system you have (Alpha or Open-M) and the additional work that must be done in the pre- and post- installation process.</p>
<p>See example of an installation over version 4.5, page <a href="#installation-over-version-4.5-example">8.</a></p>
</blockquote></th>
<th><blockquote>
<p>T</p>
</blockquote></th>
<th>P</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>9.</p>
</blockquote></td>
<td><blockquote>
<p>If you have not encountered any problems during the installation, users can be allowed back on the system when it is complete. (Check the KIDS Install File Print in the Utilities menu to verify successful completion of this Radiology/Nuclear Medicine V. 5.0 install.)</p>
</blockquote></td>
<td></td>
<td>P</td>
</tr>
<tr class="even">
<td><blockquote>
<p>10.</p>
</blockquote></td>
<td><blockquote>
<p>If your site is running the HL7 messaging interface to the VISTA Imaging package, you need to update copies of Radiology/Nuclear Medicine V. 4.5 routines that may exist on the DICOM server and/or Imaging workstations. These routines must also be updated each time they are affected by future patches.</p>
</blockquote></td>
<td></td>
<td>P</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>11.</p>
</blockquote></td>
<td><blockquote>
<p>The KIDS cleanup install, RADIOLOGY/NUCLEAR MEDICINE CLEANUP 5.0, will run in the background.</p>
<p>It should take less than 36 hours unless your site has</p>
</blockquote></td>
<td><blockquote>
<p>T</p>
</blockquote></td>
<td>P</td>
</tr>
</tbody>
</table>

> 4 Radiology/Nuclear Medicine V. 5.0 April 1998

### very large numbers of records in Files \#74.4, \#70, and \#74. Use the KIDS Install File Print option under the Utilities Menu to check on the progress and completion of the cleanup install. If there are errors, you should fix the data problems, then restart the cleanup install through the KIDS Restart Install of Package(s) option.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Post Installation:

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 69%" />
<col style="width: 10%" />
<col style="width: 10%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><u>Step</u></p>
</blockquote></th>
<th><blockquote>
<p><u>Description</u></p>
</blockquote></th>
<th><blockquote>
<p><u>Test</u></p>
</blockquote></th>
<th><blockquote>
<p><u>Prod</u></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>1.</p>
</blockquote></td>
<td><blockquote>
<p>Enable journaling, if applicable. The following globals are recommended for journaling:</p>
<p>^RA</p>
<p>^RABTCH</p>
<p>^RADPT</p>
<p>^RADPTN (new global)</p>
<p>^RAMIS</p>
<p>^RAO</p>
<p>^RARPT</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>P</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>2.</p>
</blockquote></td>
<td><blockquote>
<p>If you did not purge all RA* routines prior to the install, you will need to delete RACTTK* and RACTEX* routines.</p>
</blockquote></td>
<td>T</td>
<td><blockquote>
<p>P</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>3.</p>
</blockquote></td>
<td><blockquote>
<p>Move the Radiology/Nuclear Medicine routines (RA* minus RAI*) onto all your systems, if applicable.</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>P</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>4.</p>
</blockquote></td>
<td><blockquote>
<p>Enable routine mapping, if applicable. The following routines are recommended for mapping:</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>P</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 19%" />
<col style="width: 20%" />
<col style="width: 21%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>RABTCH*</p>
</blockquote></th>
<th><blockquote>
<p>RACNLU</p>
</blockquote></th>
<th><blockquote>
<p>RACT*</p>
</blockquote></th>
<th><blockquote>
<p>RADEM*</p>
</blockquote></th>
<th><blockquote>
<p>RADPA</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>RAEDCN*</p>
</blockquote></td>
<td><blockquote>
<p>RAEDPT</p>
</blockquote></td>
<td><blockquote>
<p>RAFLH*</p>
</blockquote></td>
<td><blockquote>
<p>RAHL*</p>
</blockquote></td>
<td><blockquote>
<p>RAJAC</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>RAORD*</p>
</blockquote></td>
<td><blockquote>
<p>RAPROD*</p>
</blockquote></td>
<td><blockquote>
<p>RAPROQ</p>
</blockquote></td>
<td><blockquote>
<p>RAPSET*</p>
</blockquote></td>
<td><blockquote>
<p>RAPTLU</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>RAREG*</p>
</blockquote></td>
<td><blockquote>
<p>RART*</p>
</blockquote></td>
<td><blockquote>
<p>RASERV</p>
</blockquote></td>
<td><blockquote>
<p>RASTED</p>
</blockquote></td>
<td><blockquote>
<p>RASTEXT*</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>RASTREQ*</p>
</blockquote></td>
<td><blockquote>
<p>RAUTL*</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 73%" />
<col style="width: 9%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>5.</p>
</blockquote></th>
<th><blockquote>
<p><strong>If this is a virgin installation of this package:</strong></p>
</blockquote>
<ul>
<li><p>Define at least one division for your site (File #79),</p></li>
<li><p>Assign the RA OVERALL menu to the ADPAC,</p></li>
<li><blockquote>
<p>Assign the three RA security keys (RA ALLOC, RA MGR, and RA VERIFY) to the ADPAC,</p>
</blockquote></li>
<li><p>Specify devices to print flash cards, jacket labels and</p></li>
</ul></th>
<th>T</th>
<th><blockquote>
<p>P</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

### reports (see Implementation and Maintenance section of the technical manual for more information on how you can do this),

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 72%" />
<col style="width: 10%" />
<col style="width: 8%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><ul>
<li><blockquote>
<p>Enter a mail group name for each one of the six bulletins (see pag<a href="#mail-groups-and-bulletins">e 19</a>) exported, and</p>
</blockquote></li>
<li><p>Add the RA OVERALL menu to XUCORE menu.</p></li>
</ul></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>6.</p>
</blockquote></td>
<td><blockquote>
<p>If your Rad/Nuc Med service wants to print cancelled requests, you will need to enter the devices on which they should print. Use the Device Specifications for Imaging Locations [RA DEVICE] option under the IRM Menu [RA SITEMANAGER].</p>
</blockquote></td>
<td><blockquote>
<p>T</p>
</blockquote></td>
<td>P</td>
</tr>
<tr class="even">
<td><blockquote>
<p>7.</p>
</blockquote></td>
<td><blockquote>
<p>If your facility is planning to use the Radiopharmaceutical dosage ticket feature, use the Device Specifications for Imaging Locations option to enter printers for each nuclear medicine imaging location where dosage tickets need to be printed.</p>
</blockquote></td>
<td></td>
<td>P</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>8.</p>
</blockquote></td>
<td><blockquote>
<p>Print the install log using the KIDS Install File Print option and review it with your ADPAC. Some adjustments may be needed if the label or report printers data could not be resolved, or if any other messages indicate a problem.</p>
</blockquote></td>
<td></td>
<td>P</td>
</tr>
<tr class="even">
<td><blockquote>
<p>9.</p>
</blockquote></td>
<td><blockquote>
<p>Further implementation can be done by the package</p>
<p>ADPAC using the Implementation Check List in the ADPAC guide.</p>
</blockquote></td>
<td><blockquote>
<p>T</p>
</blockquote></td>
<td>P</td>
</tr>
</tbody>
</table>

### The KIDS Distributions, ^XTMP("XQOO", "RADIOLOGY/NUCLEAR MEDICINE CLEANUP 5.0") and ^XTMP("XQOO","RADIOLOGY/NUCLEAR MEDICINE 5.0"),

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### occupy approximately 2 megabytes of disk space and are deleted upon successful completion of the installation process.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Use the KIDS Build File Print option if you wish to obtain a complete listing of package components (e.g., routines and options) sent with this Distribution file.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Use the KIDS Install File Print option if you wish to print out the results of the installation process. You will need to retrieve the two install results separately.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### A summary of installation times at the test sites can be found on pag[e 23.](#test-site-install-times)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Please refer to the Health Level Seven package documentation and the Radiology/Nuclear Medicine Technical manual to set up and maintain

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Radiology/Nuclear Medicine interfaces with non-V*IST*A systems (e.g., voice recognition systems and PACS systems).

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Note: If you run an XINDEX or %INDEX, you may run into several errors caused by references to routines not in the UCI if the imaging package and/or OE/RR V. 3.0 (CPRS) are not yet installed or released. These errors are benign and do not affect the operation of the Radiology/Nuclear Medicine package. Routines involved are:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> MAGRIC MAGSET3 ORMFN ORXP ORERR

### There will also be a false warning for RAUTL8. This occurs because XINDEX and

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### %INDEX can't recognize that a second line label is still part of an extrinsic function and is not called separately from the extrinsic function.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Installation Over Version 4.5 (Example)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### The following example is taken from an installation on an Open M system. Quotes enclosing messages may not appear on your system and messages may change depending on the data at your facility.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### D ^XUP

> Setting up programmer environment Terminal Type set to: C-VT320

> Select OPTION NAME: EVE Systems Manager Menu

> Core Applications ... Device Management ...

> FM VA FileMan ...

> Manage Mailman ... Menu Management ... Programmer Options ...

> Operations Management ... Spool Management ...

> System Security ... Taskman Management ... User Management ...

> Application Utilities ... Capacity Management ...

> MailMan Menu ...

> Select Systems Manager Menu Option: Programmer Options

> KIDS Kernel Installation & Distribution System ... NTEG Build an 'NTEG' routine for a package

> PG Programmer mode

> Calculate and Show Checksum Values Delete Unreferenced Options

> Error Processing ... Global Block Count List Global

> Map Pointer Relations Number base changer Routine Tools ...

> Test an option not in your menu Verifier Tools Menu ...

> Select Programmer Options Option: KIDS Kernel Installation & Distribution System

> Edits and Distribution ... Utilities ...

> Installation ...

> 8 Radiology/Nuclear Medicine V. 5.0 April 1998

> Select Kernel Installation & Distribution System Option: Installation

> Select Installation Option: Load a Distribution Enter a Host File: RAD5_0CLN.KID

> "KIDS Distribution saved on Sep 30, 1997@11:45:18" Comment: Rad/Nuc Med Cleanup 5.0

> This Distribution contains Transport Globals for the following Package(s): RADIOLOGY/NUCLEAR MEDICINE CLEANUP 5.0

> Want to Continue with Load? YES// \<RET\>

> Loading Distribution...

> Want to RUN the Environment Check Routine? YES// \<RET\>

> RADIOLOGY/NUCLEAR MEDICINE CLEANUP 5.0

> "Will first run the Environment Check Routine, RAIENV"

> This build will be queued to run from the RADIOLOGY/NUCLEAR MEDICINE

> 5.0 build. RADIOLOGY/NUCLEAR MEDICINE CLEANUP 5.0 cannot be run independently.

> Use INSTALL NAME: RADIOLOGY/NUCLEAR MEDICINE CLEANUP 5.0 to install this

> Distribution.

> Select Installation Option: Load a Distribution Enter a Host File: RAD5_0.KID

> "KIDS Distribution saved on Sep 30, 1997@11:45:18" Comment: Rad/Nuc Med 5.0

> This Distribution contains Transport Globals for the following Package(s): RADIOLOGY/NUCLEAR MEDICINE 5.0

> Want to Continue with Load? YES// \<RET\>

> Loading Distribution...

> Want to RUN the Environment Check Routine? YES// \<RET\>

> RADIOLOGY/NUCLEAR MEDICINE 5.0

> April 1998 Radiology/Nuclear Medicine V. 5.0 9

> "Will first run the Environment Check Routine, RAIENVCK"

> Use INSTALL NAME: RADIOLOGY/NUCLEAR MEDICINE 5.0 to install this

> Distribution.

1.  Load a Distribution
2.  Verify Checksums in Transport Global
3.  Print Transport Global
4.  Compare Transport Global to Current System
5.  Backup a Transport Global
6.  Install Package(s)

> Restart Install of Package(s) Unload a Distribution

> Select Installation Option: Install Package(s)

> Select INSTALL NAME: RADIOLOGY/NUCLEAR MEDICINE 5.0 Loaded from Distribution 11/5/97@16:50:55

> "This Distribution was loaded on Nov 05, 1997@16:50:55 with header of" "Rad/Nuc Med 5.0;Created on Sep 30, 1997@11:45:18"

> It consisted of the following Install(s): RADIOLOGY/NUCLEAR MEDICINE 5.0

> RADIOLOGY/NUCLEAR MEDICINE 5.0

> "Will first run the Environment Check Routine, RAIENVCK"

> Install Questions for RADIOLOGY/NUCLEAR MEDICINE 5.0 Incoming Files:

> 34 CONTRACT/SHARING AGREEMENTS

> Note: You already have the 'CONTRACT/SHARING AGREEMENTS' File.

> 70 RAD/NUC MED PATIENT

> Note: You already have the 'RAD/NUC MED PATIENT' File.

> 10 Radiology/Nuclear Medicine V. 5.0 April 1998

> 70.2 NUC MED EXAM DATA

71. RAD/NUC MED PROCEDURES (including data) Note: You already have the 'RAD/NUC MED PROCEDURES' File. Data will NOT be added.
    1.  MAJOR RAD/NUC MED AMIS CODES (including data) Note: You already have the 'MAJOR RAD/NUC MED AMIS CODES' File. Data will NOT be added.
    2.  PROCEDURE MODIFIERS (including data) Note: You already have the 'PROCEDURE MODIFIERS' File. Data will NOT be added.
    3.  RAD/NUC MED COMMON PROCEDURE

> Note: You already have the 'RAD/NUC MED COMMON PROCEDURE' File.

4.  RAD/NUC MED PROCEDURE MESSAGE

> Note: You already have the 'RAD/NUC MED PROCEDURE MESSAGE' File.

5.  IMAGING STOP CODES

> Note: You already have the 'IMAGING STOP CODES' File.

6.  ROUTE OF ADMINISTRATION (including data)

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 6%" />
<col style="width: 80%" />
</colgroup>
<thead>
<tr class="header">
<th>71.7</th>
<th></th>
<th><blockquote>
<p>SITE OF ADMINISTRATION (including data)</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>71.8</td>
<td></td>
<td><blockquote>
<p>RADIOPHARMACEUTICAL SOURCE</p>
</blockquote></td>
</tr>
<tr class="even">
<td>71.9</td>
<td></td>
<td><blockquote>
<p>RADIOPHARMACEUTICAL LOT</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><p>72</p>
<p>Note:</p></td>
<td>You</td>
<td><blockquote>
<p>EXAMINATION STATUS (including data) already have the 'EXAMINATION STATUS' File.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Data will NOT be added.

74. RAD/NUC MED REPORTS

> Note: You already have the 'RAD/NUC MED REPORTS' File.

1.  STANDARD REPORTS

> Note: You already have the 'STANDARD REPORTS' File.

2.  REPORT BATCHES

> Note: You already have the 'REPORT BATCHES' File.

> April 1998 Radiology/Nuclear Medicine V. 5.0 11

3.  REPORT DISTRIBUTION QUEUE (including data) Note: You already have the 'REPORT DISTRIBUTION QUEUE' File. I will MERGE your data with mine.
4.  REPORT DISTRIBUTION

> Note: You already have the 'REPORT DISTRIBUTION' File.

1.  RAD/NUC MED ORDERS

> Note: You already have the 'RAD/NUC MED ORDERS' File.

2.  RAD/NUC MED REASON (including data) Note: You already have the 'RAD/NUC MED REASON' File. Data will NOT be added.
1.  COMPLICATION TYPES (including data) Note: You already have the 'COMPLICATION TYPES' File. Data will NOT be added.
2.  LBL/HDR/FTR FORMATS

> \*BUT YOU ALREADY HAVE 'FLASH CARD FORMATS' AS FILE \#78.2!

> Shall I write over your FLASH CARD FORMATS File? YES// \<ret\>

3.  DIAGNOSTIC CODES (including data) Note: You already have the 'DIAGNOSTIC CODES' File. Data will NOT be added.
4.  FILM SIZES

> Note: You already have the 'FILM SIZES' File.

6.  CAMERA/EQUIP/RM

> Note: You already have the 'CAMERA/EQUIP/RM' File.

7.  LABEL PRINT FIELDS (including data) Note: You already have the 'LABEL PRINT FIELDS' File. I will OVERWRITE your data with mine.
79. RAD/NUC MED DIVISION

> Note: You already have the 'RAD/NUC MED DIVISION' File.

1.  IMAGING LOCATIONS

> Note: You already have the 'IMAGING LOCATIONS' File.

> 12 Radiology/Nuclear Medicine V. 5.0 April 1998

2.  IMAGING TYPE (including data) Note: You already have the 'IMAGING TYPE' File. I will MERGE your data with mine.

> 101 PROTOCOL (including data) Note: You already have the 'PROTOCOL' File. Data will NOT be added.

> 200 NEW PERSON (Partial Definition) Note: You already have the 'NEW PERSON' File.

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//\<ret\> Enter options you wish to mark as 'Out Of Order': RA\*

> Enter options you wish to mark as 'Out Of Order': -DI\*

> Enter options you wish to mark as 'Out Of Order': \<ret\>

> Enter protocols you wish to mark as 'Out Of Order': RA\* Enter protocols you wish to mark as 'Out Of Order': \<ret\> Delay Install (Minutes): (0-60): 0// \<ret\>

> Enter the Device you want to print the Install messages.

> You can queue the install by enter a 'Q' at the device prompt. Enter a '^' to abort the install.

> DEVICE: HOME// (Spoolfile)

> PACKAGE: RADIOLOGY/NUCLEAR MEDICINE 5.0 Nov 06, 1997 1:42 pm PAGE 1

> COMPLETED ELAPSED

> April 1998 Radiology/Nuclear Medicine V. 5.0 13

> STATUS: Install Completed DATE LOADED: NOV 05, 1997@16:50:55 INSTALLED BY: SUPPORT,IRM

> NATIONAL PACKAGE: RADIOLOGY/NUCLEAR MEDICINE

> INSTALL STARTED: NOV 05, 1997@17:21:13 17:27:15 0:06:02

> ROUTINES: 17:21:59 0:00:46 PRE-INIT CHECK POINTS:

> XPD PREINSTALL STARTED 17:22:02 0:00:03

> PREA1 17:22:10 0:00:08

> PREA2 17:22:11 0:00:01

> PREA4 17:22:11

> PREA10 17:22:12 0:00:01

> PREA11 17:22:13 0:00:01

> PREB1 17:22:13

> PREB2 17:22:13

> PREB3 17:22:14 0:00:01

> PREB4 17:22:15 0:00:01

> PREB5 17:22:16 0:00:01

> PREB7 17:22:18 0:00:02

> XPD PREINSTALL COMPLETED 17:22:19 0:00:01

> FILES:

> CONTRACT/SHARING AGREEMENTS 17:22:19

> RAD/NUC MED PATIENT 17:22:37 0:00:18

> NUC MED EXAM DATA 17:22:39 0:00:02

> RAD/NUC MED PROCEDURES 17:22:47 0:00:08

> MAJOR RAD/NUC MED AMIS CODES 17:22:48 0:00:01

> PROCEDURE MODIFIERS 17:22:50 0:00:02

> RAD/NUC MED COMMON PROCEDURE 17:22:52 0:00:02

> RAD/NUC MED PROCEDURE MESSAGE 17:22:52

> IMAGING STOP CODES 17:22:53 0:00:01

> ROUTE OF ADMINISTRATION 17:22:54 0:00:01

> SITE OF ADMINISTRATION 17:22:55 0:00:01

> RADIOPHARMACEUTICAL SOURCE 17:22:55

> RADIOPHARMACEUTICAL LOT 17:22:56 0:00:01

> EXAMINATION STATUS 17:23:02 0:00:06

> RAD/NUC MED REPORTS 17:23:10 0:00:08

> STANDARD REPORTS 17:23:11 0:00:01

> REPORT BATCHES 17:23:13 0:00:02

> REPORT DISTRIBUTION QUEUE 17:23:15 0:00:02

> REPORT DISTRIBUTION 17:23:16 0:00:01

> RAD/NUC MED ORDERS 17:23:22 0:00:06

> RAD/NUC MED REASON 17:23:23 0:00:01

> COMPLICATION TYPES 17:23:24 0:00:01

> LBL/HDR/FTR FORMATS 17:23:26 0:00:02

> DIAGNOSTIC CODES 17:23:27 0:00:01

> FILM SIZES 17:23:28 0:00:01

> CAMERA/EQUIP/RM 17:23:29 0:00:01

> LABEL PRINT FIELDS 17:23:30 0:00:01

> RAD/NUC MED DIVISION 17:23:35 0:00:05

> IMAGING LOCATIONS 17:23:38 0:00:03

> IMAGING TYPE 17:23:40 0:00:02

> NEW PERSON 17:23:58 0:00:18

> BULLETIN 17:24:10 0:00:12

> SECURITY KEY 17:24:12 0:00:02

> FUNCTION 17:24:12

> PRINT TEMPLATE 17:24:21 0:00:09

> SORT TEMPLATE 17:24:27 0:00:06

> INPUT TEMPLATE 17:24:56 0:00:29

> 14 Radiology/Nuclear Medicine V. 5.0 April 1998

<table>
<colgroup>
<col style="width: 21%" />
<col style="width: 26%" />
<col style="width: 33%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>HL7 APPLICATION PROTOCOL</p>
</blockquote></th>
<th><blockquote>
<p>PARAMETER</p>
</blockquote></th>
<th><blockquote>
<p>17:24:56</p>
<p>17:24:57</p>
</blockquote></th>
<th>0:00:01</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>OPTION</p>
</blockquote></td>
<td></td>
<td>17:26:48</td>
<td>0:01:51</td>
</tr>
<tr class="even">
<td><blockquote>
<p>POST-INIT CHECK XPD POSTINSTALL</p>
</blockquote></td>
<td><blockquote>
<p>POINTS: STARTED</p>
</blockquote></td>
<td>17:26:49</td>
<td>0:00:01</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>POST1</p>
<p>POST2</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>17:26:49</p>
<p>17:26:50</p>
</blockquote></td>
<td>0:00:01</td>
</tr>
<tr class="even">
<td><blockquote>
<p>POST3 POST31 POST311 POST4</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>17:26:53</p>
<p>17:26:54</p>
</blockquote></td>
<td><blockquote>
<p>0:00:03</p>
<p>0:00:01</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>POST7 POST8 POST9 POST10</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>17:26:54</p>
<p>17:26:54</p>
<p>17:26:54</p>
<p>17:26:55</p>
</blockquote></td>
<td>0:00:01</td>
</tr>
<tr class="even">
<td><blockquote>
<p>POSTCLN POST11 POST12</p>
<p>XPD POSTINSTALL</p>
</blockquote></td>
<td><blockquote>
<p>COMPLETED</p>
</blockquote></td>
<td><blockquote>
<p>17:26:56</p>
<p>17:26:56</p>
<p>17:26:56</p>
<p>17:26:56</p>
</blockquote></td>
<td>0:00:01</td>
</tr>
</tbody>
</table>

> INSTALL QUESTION PROMPT ANSWER

> XPF78.2#1 Shall I write over your FLASH CARD FORMATS File YES XPZ1 Want to DISABLE Scheduled Options, Menu Options, and Protocols YES MESSAGES:

> Install Started for RADIOLOGY/NUCLEAR MEDICINE 5.0 : Nov 05, 1997@17:21:13

> Installing Routines:

> Nov 05, 1997@17:21:59

> Running Pre-Install Routine: ^RAIPRE

> Deleting obsolete Stop Codes multiple from Rad/Nuc Med Procedures data dictionary. Deleting Stop Code data from the Rad/Nuc Med Procedures file. Please be patient, this may take a while.

> Deleting obsolete Principal Clinic field from Imaging Locations data dictionary. Deleting Principal Clinic data from the Imaging Locations file.

> Deleting obsolete Common Procedure Group field from Rad/Nuc Med Common Procedure data dictionary. Deleting Common Procedure Group data from the Rad/Nuc Med Common Procedure file.

> Deleting obsolete Input Devices multiple from Imaging Locations data dictionary. Deleting Imaging Devices data from the Imaging Locations file.

> Deleting obsolete Device Assignment Explanation word processing field from Imaging Type data dictionary. Deleting Device Assignment Explanation data from the Imaging type file.

> Deleting obsolete Allow 'VA' Patient Entry field from Rad/ Nuc Med Division data dictionary. Deleting Allow 'VA' Patient Entry data from the Rad/Nuc Med Division file.

> Deleting obsolete Allow 'NON-VA' Patient Entry field from Rad/Nuc Med Division data dictionary. Deleting Allow 'NON- VA' Patient Entry data from the Rad/Nuc Med Division file.

> Deleting obsolete Ask 'Requesting Physician' field from

> April 1998 Radiology/Nuclear Medicine V. 5.0 15

> Rad/Nuc Med Division data dictionary. Deleting Ask 'Requ- esting Physician' data from the Rad/Nuc Med Division file.

> Deleting obsolete LAST DFN CONVERTED (75.1) field from RAD/NUC MED DIVISION data dictionary.

> Deleting LAST DFN CONVERTED (75.1) data from the RAD/NUC MED DIVISION file. Division: VAMC, ANYWHERE,IL

> Deleting obsolete CONVERSION START TIME (75.1) field from RAD/NUC MED DIVISION data dictionary.

> Deleting CONVERSION START TIME (75.1) data from the RAD/NUC MED DIVISION file. Division: VAMC, ANYWHERE,IL

> Deleting obsolete CONVERSION STOP TIME (75.1) field from RAD/NUC MED DIVISION data dictionary.

> Deleting CONVERSION STOP TIME (75.1) data from the RAD/NUC MED DIVISION file. Division: VAMC, ANYWHERE,IL

> Deleting obsolete LAST DFN CONVERTED (70) field from RAD/NUC MED DIVISION data dictionary.

> Deleting LAST DFN CONVERTED (70) data from the

> RAD/NUC MED DIVISION file. Division: VAMC, ANYWHERE,IL

> Deleting obsolete CONVERSION START TIME (70) field from RAD/NUC MED DIVISION data dictionary.

> Deleting CONVERSION START TIME (70) data from the RAD/NUC MED DIVISION file. Division: VAMC, ANYWHERE,IL

> Deleting obsolete CONVERSION STOP TIME (70) field from RAD/NUC MED DIVISION data dictionary.

> Deleting CONVERSION STOP TIME (70) data from the RAD/NUC MED DIVISION file. Division: VAMC, ANYWHERE,IL

> Changing name of Label Print Field (file: 78.7) from: 'RADIOLOGY LOCATION' to 'IMAGING LOCATION'

> Un-compiling the \`RA STATUS CHANGE' input template on the Rad/Nuc Med Patient file. All the compiled templates associated with \`RA STATUS CHANGE' will be deleted.

> Un-compiling the \`RA EXAM EDIT' input template on the Rad/Nuc Med Patient file. All the compiled templates associated with \`RA EXAM EDIT' will be deleted.

> Installing Data Dictionaries:

> Nov 05, 1997@17:23:58

> Installing Data:

> Nov 05, 1997@17:24:07

> Installing PACKAGE COMPONENTS: Installing BULLETIN

> Installing SECURITY KEY Installing FUNCTION Installing PRINT TEMPLATE Installing SORT TEMPLATE Installing INPUT TEMPLATE

> 16 Radiology/Nuclear Medicine V. 5.0 April 1998

> Installing HL7 APPLICATION PARAMETER

> Installing PROTOCOL Installing OPTION

> Nov 05, 1997@17:26:48

> Running Post-Install Routine: ^RAIPST

> Option 'RA SIGN-ON MSG' IS NOW UNDER option 'XU USER SIGN-ON'

> Deleting obsolete \*CREDIT CLINIC STOP data dictionary and Descriptor nodes from Major Rad/Nuc Med AMIS Codes file

> Converting free-text pointer data in the REQUIRED FLASH CARD PRINTER field of the Rad/Nuc Med Procedures file to regular pointers to the Device file.

> Converting free-text pointer data for fields:

> FLASH CARD PRINTER NAME, JACKET LABEL PRINTER NAME, REPORT PRINTER NAME and REQUEST PRINTER NAME

> in the Imaging Locations file to regular pointers to the Device file.

> Converting ALLOW 'RELEASED/UNVERIFIED' data from the Rad/

> Nuc Med Division file to the new ALLOW 'RELEASED/UNVERIFIED'. field on the Imaging Locations file.

> Deleting obsolete ALLOW 'RELEASED/UNVERIFIED' field from Rad/Nuc Med Division file.

> Correcting values in the REPORT RIGHT MARGIN field of all entries in the IMAGING LOCATIONS file.

> Add Exam Statuses with an Imaging Type of 'Mammography'. Exam Statuses created: Cancelled; Waiting For Exam; Called For Exam; Examined; Transcribed and Complete.

> Updating Routine file...

> The following Routines were created during this install: RACTRG

> RACTRG1 RACTRG10 RACTRG11 RACTRG12 RACTRG13 RACTRG2 RACTRG3 RACTRG4 RACTRG5 RACTRG6 RACTRG7 RACTRG8 RACTRG9 RACTWR RACTWR1 RACTWR2 RACTWR3

> PACKAGE: RADIOLOGY/NUCLEAR MEDICINE 5.0 Nov 06, 1997 1:42 pm PAGE 2

> April 1998 Radiology/Nuclear Medicine V. 5.0 17

> COMPLETED ELAPSED

> RACTWR4 RACTWR5 RACTVR RACTVR1 RACTVR2 RACTVR3 RACTVR4 RACTOE RACTOE1 RACTOE2 RACTOE3 RACTOE4 RACTOE5 RACTOE6 RACTOE7 RACTOE8 RACTQE RACTQE1 RACTQE2 RACTQE3 RACTQE4 RACTQE5 RACTQE6

> Updating KIDS files...

> RADIOLOGY/NUCLEAR MEDICINE 5.0 Installed.

> Nov 05, 1997@17:27:15

> Install Message sent \#6331999

# Mail Groups and Bulletins

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### This chapter discusses creating mail groups and associating those mail groups to the package's six bulletins. These bulletins are generated when important actions take place (e.g., the deletion of an exam) and are sent to members of a mail group who should be aware that the action took place. The names of the bulletins are:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### RAD/NUC MED REQUEST CANCELLED RAD/NUC MED EXAM DELETED RAD/NUC MED REPORT DELETION RAD/NUC MED REPORT UNVERIFIED RAD/NUC MED CREDIT FAILURE RAD/NUC MED REQUEST HELD

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### To find out what mail groups are associated with these bulletins and who belongs to those mail groups, you can do a VA FileMan sort and print. The following is an example of a sort and print that can be run before or after the installation of this new version.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### D Q^DI

> VA FileMan 21.0

> Select OPTION: 2 PRINT FILE ENTRIES OUTPUT FROM WHAT FILE: BULLETIN// \<RET\>

> SORT BY: NAME// \<RET\>

> START WITH NAME: FIRST// RA\<RET\>

> GO TO NAME: LAST// RADZ\<RET\>

WITHIN NAME, SORT BY: \<RET\>

FIRST PRINT FIELD: .01\<RET\> NAME

> THEN PRINT FIELD: 4\<RET\> MAIL GROUP (multiple) THEN PRINT MAIL GROUP SUB-FIELD: .01\<RET\> MAIL GROUP

> THEN PRINT MAIL GROUP SUB FIELD: MAIL GROUP:MEMBER\<RET\>

> THEN PRINT MAIL GROUP SUB FIELD: \<RET\>

> THEN PRINT FIELD: \<RET\>

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Heading (S/C): BULLETIN LIST// \<RET\> START AT PAGE: 1// \<RET\>

> DEVICE: (printer name) \<RET\> RIGHT MARGIN: 80// \<RET\>

### Consult with the package ADPAC to determine how many mail groups to create, what mail group(s) you wish to associate with each bulletin, and who should be the coordinator for each mail group.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### The following are suggestions for setting up six mail groups, one for each bulletin.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Bulletin Name: RAD/NUC MED REQUEST CANCELLED

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 39%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><u>Mail Group (#3.8) field name</u></p>
</blockquote></th>
<th><blockquote>
<p><u>Suggested value</u></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>NAME</p>
</blockquote></td>
<td><blockquote>
<p>RA REQUEST CANCELLED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>TYPE</p>
</blockquote></td>
<td><blockquote>
<p>Public</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>RESTRICTIONS</p>
</blockquote></td>
<td><blockquote>
<p>Unrestricted</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DESCRIPTION</p>
</blockquote></td>
<td><blockquote>
<p>The members of this mail group will receive a bulletin when a Radiology/Nuclear Medicine</p>
<p>request is cancelled.</p>
</blockquote></td>
</tr>
</tbody>
</table>

### Bulletin Name: RAD/NUC MED EXAM DELETED

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 37%" />
<col style="width: 62%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><u>Mail Group (#3.8) field name</u></p>
</blockquote></th>
<th><blockquote>
<p><u>Suggested value</u></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>NAME</p>
</blockquote></td>
<td><blockquote>
<p>RA EXAM DELETED</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>TYPE</p>
</blockquote></td>
<td><blockquote>
<p>Public</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>RESTRICTIONS</p>
</blockquote></td>
<td><blockquote>
<p>Unrestricted</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DESCRIPTION</p>
</blockquote></td>
<td><blockquote>
<p>The members of this mail group will receive a bulletin when a Radiology/Nuclear Medicine exam</p>
<p>is deleted</p>
</blockquote></td>
</tr>
</tbody>
</table>

### Bulletin Name: RAD/NUC MED REPORT DELETION <u>Mail Group (#3.8) field name</u> <u>Suggested value</u>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### NAME RA REPORT DELETION

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### TYPE Public

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### RESTRICTIONS Unrestricted

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### DESCRIPTION The members of this mail group will receive a bulletin when a Radiology/Nuclear Medicine report is deleted.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Bulletin Name: RAD/NUC MED REPORT UNVERIFIED <u>Mail Group (#3.8) field name</u> <u>Suggested value</u>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### NAME RA REPORT UNVERIFIED

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### TYPE Public

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### RESTRICTIONS Unrestricted

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### DESCRIPTION The members of this mail group will receive a bulletin when a Radiology/Nuclear Medicine report is changed from Verified to any other status.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Bulletin Name: RAD/NUC MED REQUEST HELD

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 39%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><u>Mail Group (#3.8) field name</u></p>
</blockquote></th>
<th><blockquote>
<p><u>Suggested value</u></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>NAME</p>
</blockquote></td>
<td><blockquote>
<p>RA REQUEST HELD</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>TYPE</p>
</blockquote></td>
<td><blockquote>
<p>Public</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>RESTRICTIONS</p>
</blockquote></td>
<td><blockquote>
<p>Unrestricted</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DESCRIPTION</p>
</blockquote></td>
<td><blockquote>
<p>The members of this mail group will receive a</p>
<p>bulletin when a Radiology/Nuclear Medicine request is placed on a status of Hold.</p>
</blockquote></td>
</tr>
</tbody>
</table>

### Bulletin Name: RAD/NUC MED CREDIT FAILURE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 39%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><u>Mail Group (#3.8) field name</u></p>
</blockquote></th>
<th><blockquote>
<p><u>Suggested value</u></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>NAME</p>
</blockquote></td>
<td><blockquote>
<p>RA CREDIT FAILURE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>TYPE</p>
</blockquote></td>
<td><blockquote>
<p>Public</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>RESTRICTIONS</p>
</blockquote></td>
<td><blockquote>
<p>Unrestricted</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>DESCRIPTION</p>
</blockquote></td>
<td><blockquote>
<p>The members of this mail group will receive a bulletin when an exam has not been credited</p>
<p>properly.</p>
</blockquote></td>
</tr>
</tbody>
</table>

### The following is an example of creating a mail group.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### D Q^DI

> VA FileMan 21.0

> Select OPTION: 1 ENTER OR EDIT FILE ENTRIES INPUT TO WHAT FILE: MAIL GROUP// \<RET\>

> EDIT WHICH FIELD: ALL// \<RET\>

> Select MAIL GROUP NAME: RA CREDIT FAILURE

> Are you adding 'RA CREDIT FAILURE' as a new MAIL GROUP (the nnTH)? YES

> MAIL GROUP COORDINATOR: Mail Group Coordinator FT Select MEMBER: Mail Group Member NS

> Are you adding 'Mail Group Member' as a new MEMBER (the 1ST for this MAIL GROUP)? YES

> Select MEMBER: \<RET\>

> DESCRIPTION:

#### 1\>The members of this mail group will receive a bulletin when an

#### 2\>exam has not been credited properly.

> 3\>\<RET\>

> EDIT Option: \<RET\>

> TYPE: public

> ORGANIZER: Public Mail Group Organizer COORDINATOR: Public Mail Group Coordiaton SELECT AUTHORIZED SENDER: \<RET\>

> ALLOW SELF ENROLLMENT?: NO REFERENCE COUNT: \<RET\> LAST REFERENCED: \<RET\>

> RESTRICTIONS: 0\<RET\>UNRESTRICTED Select MEMBER GROUP NAME: \<RET\> Select REMOTE MEMBERS: \<RET\> Select DISTRIBUTION LIST: \<RET\>

> April 1998 Radiology/Nuclear Medicine V. 5.0 21

> Select MAIL GROUP NAME: \<RET\>

### The following is an example of associating a mail group with a bulletin.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### D Q^DI

> VA FileMan 21.0

> Select OPTION: 1 ENTER OR EDIT FILE ENTRIES INPUT TO WHAT FILE: BULLETIN// \<RET\>

> EDIT WHICH FIELD: ALL// 4\<RET\> (multiple) EDIT WHICH MAIL GROUP SUB-FIELD: ALL// \<RET\>

> THEN EDIT FIELD: \<RET\>

> Select BULLETIN NAME: RAD/NUC MED CREDIT FAILURE

> Select MAIL GROUP: RA CREDIT FAILURE

> Are you adding 'RA CREDIT FAILURE' as

> a new MAIL GROUP (the 1st for this BULLETIN)? YES

> Select MAIL GROUP: \<RET\>

> Select BULLETIN NAME: \<RET\>

# Test Site Install Times

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Install Times from Test Sites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 7%" />
<col style="width: 15%" />
<col style="width: 25%" />
<col style="width: 27%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><u>Type of System</u></p>
</blockquote></th>
<th><blockquote>
<p><u>File</u></p>
</blockquote></th>
<th><u>#of Entries</u></th>
<th><blockquote>
<p>Radiology/Nuclear Medicine 5.0 <u>Install Time (HH:MM)</u></p>
</blockquote></th>
<th><blockquote>
<p>Radiology/Nuclear Medicine Cleanup 5.0 <u>Install Time (HH:MM)</u></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Alpha (site 1)</p>
</blockquote></td>
<td><blockquote>
<p>70</p>
</blockquote></td>
<td>59,500</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>74</p>
</blockquote></td>
<td>369,000</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>74.4</p>
</blockquote></td>
<td>30,800</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Total</strong></td>
<td></td>
<td></td>
<td><strong>00:08</strong></td>
<td><strong>22:35</strong></td>
</tr>
<tr class="odd">
<td colspan="5"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Alpha (site 2)</p>
</blockquote></td>
<td><blockquote>
<p>70</p>
</blockquote></td>
<td>74,515</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>74</p>
</blockquote></td>
<td>546,600</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>74.4</p>
</blockquote></td>
<td>235,813</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Total</strong></td>
<td></td>
<td></td>
<td><strong>00:04</strong></td>
<td><strong>15:09</strong></td>
</tr>
<tr class="even">
<td colspan="5"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Alpha (site 3)</p>
</blockquote></td>
<td><blockquote>
<p>70</p>
</blockquote></td>
<td>39,920</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>74</p>
</blockquote></td>
<td>363,442</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>74.4</p>
</blockquote></td>
<td>252</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Total</strong></td>
<td></td>
<td></td>
<td><strong>00:03</strong></td>
<td><strong>2:04</strong></td>
</tr>
<tr class="odd">
<td colspan="5"></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Alpha (site 4)</p>
</blockquote></td>
<td><blockquote>
<p>70</p>
</blockquote></td>
<td>97,066</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>74</p>
</blockquote></td>
<td>519,576</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>74.4</p>
</blockquote></td>
<td>0</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><strong>Total</strong></td>
<td></td>
<td></td>
<td><strong>00:03</strong></td>
<td><strong>00:06</strong></td>
</tr>
<tr class="even">
<td colspan="5"></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Open M (site 1)</p>
</blockquote></td>
<td><blockquote>
<p>70</p>
</blockquote></td>
<td>20,700</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>74</p>
</blockquote></td>
<td>189,200</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>74.4</p>
</blockquote></td>
<td>4,000</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Total</strong></td>
<td></td>
<td></td>
<td><strong>00:01</strong></td>
<td><strong>00:30</strong></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Open M (site 2)</p>
</blockquote></td>
<td><blockquote>
<p>70</p>
</blockquote></td>
<td>14,890</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>74</p>
</blockquote></td>
<td>79,860</td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>74.4</p>
</blockquote></td>
<td>0</td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><strong>Total</strong></td>
<td></td>
<td></td>
<td><strong>00:01</strong></td>
<td><strong>00:24</strong></td>
</tr>
</tbody>
</table>

> 24 Radiology/Nuclear Medicine V. 5.0 April 1998