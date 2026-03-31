---
title: Fee Basis Version 3.5 Installation Guide (1995)
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: (1995)
app_code: FB
app_name: Fee Basis
section: FIN
app_status: active
pkg_ns: FB
patch_ver: 3.5
patch_id: FB*3.5
group_key: "FB:FB:3.5"
file_numbers: []
security_keys: []
menu_options: 3
description: - [Department of Veterans Affairs Decentralized Hospital Computer Program](#department-of-veterans-affairs-decentralized-hospital-computer-program) - [Information Systems Center Albany, New York](#information-systems-center-albany-new-york) - [PACKAGE INTEGRATION](#package-integration) - [The follow
audience: 
keywords: 
  - blockquote
  - filed
  - fbini
  - table
  - contents
  - fbaa
  - basis
  - class
  - attachment
  - fbch
page_count: 0
word_count: 7272
section_count: 1
table_count: 3
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Fee_Basis/fb3_5ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Fee_Basis/fb3_5ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=40"
---

# Department of Veterans Affairs Decentralized Hospital Computer Program


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Department of Veterans Affairs Decentralized Hospital Computer Program](#department-of-veterans-affairs-decentralized-hospital-computer-program)
- [Information Systems Center Albany, New York](#information-systems-center-albany-new-york)
- [PACKAGE INTEGRATION](#package-integration)
- [The following are the minimum package requirements for the installation of Fee Basis Version 3.5.](#the-following-are-the-minimum-package-requirements-for-the-installation-of-fee-basis-version-35)
- [Kernel V. 7.1](#kernel-v-71)
- [Fee Basis V. 3.0 (if previously running Fee Basis) Registration V. 5.3](#fee-basis-v-30-if-previously-running-fee-basis-registration-v-53)
- [INSTALLATION STEPS](#installation-steps)
- [Get Fee Basis users off system(s). 2. Backup system(s).](#get-fee-basis-users-off-systems-2-backup-systems)
- [Disable journalling the FB\ globals, if applicable.](#disable-journalling-the-fb-globals-if-applicable)
- [(Use 24k partition for MSM)](#use-24k-partition-for-msm)
- [DUZ, DUZ(0)="@", DT, DTIME.](#duz-duz0-dt-dtime)
- [Use the appropriate vendor-supplied utility to load all Fee Basis routines. 7. D ^FBINIT (See Attachment B for sample init.)](#use-the-appropriate-vendor-supplied-utility-to-load-all-fee-basis-routines-7-d-fbinit-see-attachment-b-for-sample-init)
- [INSTALLATION STEPS](#installation-steps-1)
- [Move routines to all systems.](#move-routines-to-all-systems)
- [Rebuild map set, if applicable. The following routines are recommended for Fee Basis mapping.](#rebuild-map-set-if-applicable-the-following-routines-are-recommended-for-fee-basis-mapping)
- [FBAAMP2 (recommended as FBAAMP\)](#fbaamp2-recommended-as-fbaamp)
- [It is recommended that sites journal ^FB\. Enable journalling, if applicable.](#it-is-recommended-that-sites-journal-fb-enable-journalling-if-applicable)
- [The following chart for package initialization time provides average times based on installation at ten test sites.](#the-following-chart-for-package-initialization-time-provides-average-times-based-on-installation-at-ten-test-sites)
- [POST-INSTALLATION CONSIDERATIONS](#post-installation-considerations)
- [<u>Elimination of Denials Files</u>](#uelimination-of-denials-filesu)
- [The post-init will be called automatically at the end of the FBINIT process. If necessary, you can run it by invoking ^FBPST35A. If the routine has previously run to completion, it will simply exit processing.](#the-post-init-will-be-called-automatically-at-the-end-of-the-fbinit-process-if-necessary-you-can-run-it-by-invoking-fbpst35a-if-the-routine-has-previously-run-to-completion-it-will-simply-exit-processing)
- [<u>Removal of Fields Starred for Deletion</u>](#uremoval-of-fields-starred-for-deletionu)
- [As part of the post-initialization process, the following fields, previously starred for deletion, will be removed from the system:](#as-part-of-the-post-initialization-process-the-following-fields-previously-starred-for-deletion-will-be-removed-from-the-system)
- [POST-INSTALLATION CONSIDERATIONS](#post-installation-considerations-1)
- [<u>Security Keys</u>](#usecurity-keysu)
- [There are three security keys used by the FEE BASIS package. The FBAA ESTABLISH VENDOR key is required to add/edit vendors to Fee Basis and the FBAASUPERVISOR key is required to perform the supervisory functions, such as release a batch and queue data for transmission to Austin. The XUSPF200 key is used when adding a person to the NEW PERSON file (#200). Its holders are not required to enter a Social Security Number (SSN) upon input of the person.](#there-are-three-security-keys-used-by-the-fee-basis-package-the-fbaa-establish-vendor-key-is-required-to-addedit-vendors-to-fee-basis-and-the-fbaasupervisor-key-is-required-to-perform-the-supervisory-functions-such-as-release-a-batch-and-queue-data-for-transmission-to-austin-the-xuspf200-key-is-used-when-adding-a-person-to-the-new-person-file-200-its-holders-are-not-required-to-enter-a-social-security-number-ssn-upon-input-of-the-person)
- [<u>Printer Requirements</u>](#uprinter-requirementsu)
- [All printers used to print the VA authorization forms (VA Form 10-7079 and VA Form 10-7078) must be set to a pitch no larger than 16 and at 8 lines to the inch. All reports/listings have been designed for 8 1/2 x 11 paper.](#all-printers-used-to-print-the-va-authorization-forms-va-form-10-7079-and-va-form-10-7078-must-be-set-to-a-pitch-no-larger-than-16-and-at-8-lines-to-the-inch-all-reportslistings-have-been-designed-for-8-12-x-11-paper)
- [<u>Mail Groups</u>](#umail-groupsu)
- [Five mail groups are used with the Fee Basis package. Each group must have at least one member prior to transmitting any data to Austin. Austin sends confirmation messages, along with daily reports, to the mail groups listed below.](#five-mail-groups-are-used-with-the-fee-basis-package-each-group-must-have-at-least-one-member-prior-to-transmitting-any-data-to-austin-austin-sends-confirmation-messages-along-with-daily-reports-to-the-mail-groups-listed-below)
- [POST-INSTALLATION CONSIDERATIONS](#post-installation-considerations-2)
- [<u>Domains</u>](#udomainsu)
- [With Version 3.5, Fee Basis continues to use the TRANSMISSION ROUTERS file (#407.7). FEE and NVP are the two entries which must exist in this file. Below are examples of the two entries in the file with appropriate domains.](#with-version-35-fee-basis-continues-to-use-the-transmission-routers-file-4077-fee-and-nvp-are-the-two-entries-which-must-exist-in-this-file-below-are-examples-of-the-two-entries-in-the-file-with-appropriate-domains)
- [<u>H. VA FileMan DD Checker Utility</u>](#uh-va-fileman-dd-checker-utilityu)
- [POST-INSTALLATION CONSIDERATIONS](#post-installation-considerations-3)
- [<u>I. FEE BASIS VENDOR CORRECTION file (#161.25) Cleanup</u>](#ui-fee-basis-vendor-correction-file-16125-cleanupu)
- [As part of the post-initialization process, the vendors residing in your FEE BASIS VENDOR CORRECTION file will be reviewed for accuracy. All vendors found with invalid vendor identification numbers will be removed from the file and placed in delete status in the FEE BASIS VENDOR file (#161.2). If any vendors are found, a mail message will be generated listing the vendor name and ID for each invalid entry. This mail message will be forwarded to the G.FEE mail group. Refer to Attachment E for a sample mail message.](#as-part-of-the-post-initialization-process-the-vendors-residing-in-your-fee-basis-vendor-correction-file-will-be-reviewed-for-accuracy-all-vendors-found-with-invalid-vendor-identification-numbers-will-be-removed-from-the-file-and-placed-in-delete-status-in-the-fee-basis-vendor-file-1612-if-any-vendors-are-found-a-mail-message-will-be-generated-listing-the-vendor-name-and-id-for-each-invalid-entry-this-mail-message-will-be-forwarded-to-the-gfee-mail-group-refer-to-attachment-e-for-a-sample-mail-message)
- [RESOURCE REQUIREMENTS](#resource-requirements)
- [Formula for TUs: (# of FEE patients/160,000) + .04 = TUs needed Storage requirements:](#formula-for-tus-of-fee-patients160000-04-tus-needed-storage-requirements)
- [Equipment requirements: No increase from Fee Basis Version 3.0.](#equipment-requirements-no-increase-from-fee-basis-version-30)
- [ATTACHMENT B. FBINIT](#attachment-b-fbinit)
- [ATTACHMENT B. FBINIT](#attachment-b-fbinit-1)
- [ATTACHMENT B. FBINIT](#attachment-b-fbinit-2)
- [ATTACHMENT B. FBINIT](#attachment-b-fbinit-3)
- [ATTACHMENT B. FBINIT](#attachment-b-fbinit-4)
- [ATTACHMENT B. FBINIT](#attachment-b-fbinit-5)
- [ATTACHMENT B. FBINIT](#attachment-b-fbinit-6)
- [ATTACHMENT B. FBINIT](#attachment-b-fbinit-7)
- [ATTACHMENT B. FBINIT](#attachment-b-fbinit-8)
- [ATTACHMENT B. FBINIT](#attachment-b-fbinit-9)
- [ATTACHMENT C. PAID SERVER](#attachment-c-paid-server)
- [The following is a sample PAID Server mail message.](#the-following-is-a-sample-paid-server-mail-message)
- [ATTACHMENT D. FBPST35C POST-INIT MESSAGE](#attachment-d-fbpst35c-post-init-message)
- [ATTACHMENT E. FEE BASIS VENDOR CORRECTIONS CLEANUP](#attachment-e-fee-basis-vendor-corrections-cleanup)
FEE BASIS INSTALLATION GUIDE
> Version 3.5 January 1995

# Information Systems Center Albany, New York

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

[Section 1. Installation](#package-integration) 1

[Package Integration](#package-integration) 1

[Installation Steps](#package-integration) 1

[Post-Installation Considerations](#post-installation-considerations) 3

1.  [Elimination of Denials Files](#post-installation-considerations) 3
2.  [Removal of Fields Starred for Deletion](#post-installation-considerations) 3
3.  [Security Keys](#post-installation-considerations-1) 4
4.  [Printer Requirements](#post-installation-considerations-1) 4
5.  [Mail Groups](#post-installation-considerations-1) 4
6.  [Domains](#post-installation-considerations-2) 5
7.  [Server Option](#post-installation-considerations-2) 5
8.  [VA FileMan DD Checker Utility](#post-installation-considerations-2) 5
9.  [Fee Basis Vendor Correction file (#161.25) Cleanup](#post-installation-considerations-3) 6

[Resource Requirements](#post-installation-considerations-3) 6

[Section 2. Attachments](#_bookmark5) 7

[Attachment A. Routines](#_bookmark5) 7

[Attachment B. FBINIT](#attachment-b.-fbinit) 9

[Attachment C. PAID Server](#attachment-c.-paid-server) 19

[Attachment D. FBPST35C Post-Init Message](#attachment-d.-fbpst35c-post-init-message) 20

[Attachment E. Fee Basis Vendor Corrections Cleanup](#attachment-e.-fee-basis-vendor-corrections-cleanup) 21

# PACKAGE INTEGRATION

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# The following are the minimum package requirements for the installation of Fee Basis Version 3.5.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> VA File Manager V. 20.0 NEW PERSON file (#200)

# Kernel V. 7.1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Kernel Toolkit V. 7.2 IFCAP V. 4.0

# Fee Basis V. 3.0 (if previously running Fee Basis) Registration V. 5.3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Integrated Billing V. 2.0 CPT V. 5.0

# INSTALLATION STEPS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <u>Step</u> <u>Description</u>

# Get Fee Basis users off system(s). 2. Backup system(s).

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

3.  Disable routine mapping (DSM), if operating system supports mapping.

# Disable journalling the FB\* globals, if applicable.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

4.  Sign into UCI where package is to be loaded. (Use 16k partition for DSM)

# (Use 24k partition for MSM)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Assure that the following vari ables are defined:

# DUZ, DUZ(0)="@", DT, DTIME.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

5.  Delete all FB\* routines from your routine directory.

# Use the appropriate vendor-supplied utility to load all Fee Basis routines. 7. D ^FBINIT (See Attachment B for sample init.)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

8.  Delete FBIN\* and FBONI\* routines from the routine directory.

# INSTALLATION STEPS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <u>Step</u> <u>Description</u>

# Move routines to all systems.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

9.  Recompile templates FB VENDOR UPDATE and FBAA AUTHORIZATION on all CPUs using the same routine size. Use the appropriate sequential medium to move routines across systems (i.e., tape), then call line tag RCOMP^FBAAUTL3.

# Rebuild map set, if applicable. The following routines are recommended for Fee Basis mapping.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 20%" />
<col style="width: 20%" />
<col style="width: 19%" />
<col style="width: 20%" />
</colgroup>
<thead>
<tr class="header">
<th>FBAAAUT</th>
<th>FBAACO*</th>
<th>FBAACCB*</th>
<th>FBAACIE</th>
<th><blockquote>
<p>FBAADEM*</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>FBAAEP*</td>
<td>FBAAMP</td>
<td>FBAAOB</td>
<td>FBAAPI</td>
<td><blockquote>
<p>FBAAPIE*</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBAASCB*</td>
<td>FBAAUTL*</td>
<td>FBAAVD*</td>
<td>FBCH78*</td>
<td><blockquote>
<p>FBCHREQ*</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>FBCHSCB</td>
<td>FBMRA*</td>
<td>FBNHEA*</td>
<td>FBNHED*</td>
<td><blockquote>
<p>FBNHEP*</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBNHPC</td>
<td>FBNHRAT</td>
<td>FBNHRC</td>
<td>FBUC*</td>
<td></td>
</tr>
</tbody>
</table>

> The following routine, which was previously recommended for mapping, is obsolete with Fee Basis V. 3.5.

# FBAAMP2 (recommended as FBAAMP\*)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> For a complete list of obsolete routines, please see the Release Notes.

# It is recommended that sites journal ^FB\*. Enable journalling, if applicable.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

10. Bring system(s) back on line.

# The following chart for package initialization time provides average times based on installation at ten test sites.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 40%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p><u>MSM</u></p>
</blockquote></th>
<th><blockquote>
<p><u>VAX</u></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>PRE-INIT</td>
<td><blockquote>
<p>3 sec</p>
</blockquote></td>
<td><blockquote>
<p>2 sec</p>
</blockquote></td>
</tr>
<tr class="even">
<td>FBINIT</td>
<td><blockquote>
<p>16 min</p>
</blockquote></td>
<td><blockquote>
<p>5 min</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>POST-INIT</td>
<td><blockquote>
<p>15 min</p>
</blockquote></td>
<td><blockquote>
<p>8 min</p>
</blockquote></td>
</tr>
</tbody>
</table>

# POST-INSTALLATION CONSIDERATIONS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# <u>Elimination of Denials Files</u>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> As part of the post-initialization process, the FEE BASIS MEDICAL DENIALS file (#163) and the FEE BASIS PHARMACY DENIALS file (#163.1) will be removed from the system. The post-init will allow the user to determine if s/he wishes to save any medical denials and merge them into the FEE BASIS PAYMENT file (#162). The software will merge data (if selected), then remove both denials files from the system.

# The post-init will be called automatically at the end of the FBINIT process. If necessary, you can run it by invoking ^FBPST35A. If the routine has previously run to completion, it will simply exit processing.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# <u>Removal of Fields Starred for Deletion</u>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# As part of the post-initialization process, the following fields, previously starred for deletion, will be removed from the system:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| <u>File#</u> | <u>File Name</u>          | <u>Field#</u> | <u>Field Name</u>              |
|--------------|---------------------------|---------------|--------------------------------|
| 161          | FEE BASIS PATIENT         | 102           | \*AUSTIN DELETED               |
|              |                           | 103           | \*DATE OF AUSTIN DELETE        |
|              |                           | 104           | \*DATE TRANSMITTED TO AUSTIN   |
| 161.01       | FEE BASIS PATIENT         | 4             | \*CNH LEVEL OF CARE            |
| 161.2        | FEE BASIS VENDOR          | 16            | \*NUMBER OF SKILLED BEDS       |
|              |                           | 17            | \*NUMBER OF INTERMEDIATE BEDS  |
|              |                           | 21            | \*LEVELS OF CARE PROVIDED      |
| 161.4        | FEE BASIS SITE PARAMETERS | 36            | \*LAST UC UPDATED              |
|              |                           | 37            | \*DATE UC CONVERSION COMPLETED |

> The post-init allows you to choose to task the job in the background. If the job is tasked, a mail message will be sent to the user performing the installation of Fee Basis V. 3.5 upon successful completion of the FBPST35C post-init process. In the event that the job is tasked, but a mail message is not received, you can run the FBPST35C post-init again (D ^FBPST35C). If you choose not to task the job in the background, the post-init will complete in real time, and NO mail message will be sent. Refer to Attachment D for a sample mail message.

# POST-INSTALLATION CONSIDERATIONS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# <u>Security Keys</u>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# There are three security keys used by the FEE BASIS package. The FBAA ESTABLISH VENDOR key is required to add/edit vendors to Fee Basis and the FBAASUPERVISOR key is required to perform the supervisory functions, such as release a batch and queue data for transmission to Austin. The XUSPF200 key is used when adding a person to the NEW PERSON file (#200). Its holders are not required to enter a Social Security Number (SSN) upon input of the person.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# <u>Printer Requirements</u>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# All printers used to print the VA authorization forms (VA Form 10-7079 and VA Form 10-7078) must be set to a pitch no larger than 16 and at 8 lines to the inch. All reports/listings have been designed for 8 1/2 x 11 paper.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# <u>Mail Groups</u>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Five mail groups are used with the Fee Basis package. Each group must have at least one member prior to transmitting any data to Austin. Austin sends confirmation messages, along with daily reports, to the mail groups listed below.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> FEE Used to receive confirmation and server messages. FEE AUSTIN MESSAGES Used to receive daily reports.

> NVP Used to receive confirmation messages from the Non-VA Pricer system for Civil Hospital program.

> NVP AUSTIN MESSAGES Used to receive daily reports from the Non-VA P ricer system for Civil Hospital program.

> FIS AUSTIN MESSAGES Used to receive Fee Basis daily reports for Fiscal Service.

# POST-INSTALLATION CONSIDERATIONS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# <u>Domains</u>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# With Version 3.5, Fee Basis continues to use the TRANSMISSION ROUTERS file (#407.7). FEE and NVP are the two entries which must exist in this file. Below are examples of the two entries in the file with appropriate domains.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 59%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>NAME: FEE</p>
</blockquote></th>
<th><blockquote>
<p>LINES/MSG FIXED LENGTH RECORD: 150</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>RECEIVING USER: XXX</td>
<td><blockquote>
<p>DOMAIN MAIL ROUTER: Q-FEE.VA.GOV</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>TRANSMIT: YES</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>NAME: NVP</p>
</blockquote></td>
<td><blockquote>
<p>LINES/MSG FIXED LENGTH RECORD: 150</p>
</blockquote></td>
</tr>
<tr class="even">
<td>RECEIVING USER: XXX</td>
<td><blockquote>
<p>DOMAIN MAIL ROUTER: Q-NVP.VA.GOV</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>TRANSMIT: YES</p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><u>G. Server Option</u></td>
<td></td>
</tr>
</tbody>
</table>

> With Version 3.5, Fee Basis uses the FBAA PAID SERVER option to accept and process check confirmation messages from Austin. Medical Centers must insure that the FEE mail group is populated with at least one DHCP user in order to receive the server mail messages that will be transmitted upon completion of the Server job. (Refer to Attachment C for a sample Paid Server message.)

# <u>H. VA FileMan DD Checker Utility</u>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> After installing Version 3.5, you should use the Check/Fix DD Structure option in the Data Dictionary Utilities submenu of VA FileMan Version 20.0 to correct possible inconsistencies in the data dictionaries. Please refer to Pages 35–36 in the VA FileMan V. 20.0 User Manual for instructions detailing the use of this option.

> We recommend that you follow the example shown on Page 36. You should start with File \#161 and go to File \#163.99. This process does not change any file structures, nor does it affect any data.

# POST-INSTALLATION CONSIDERATIONS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# <u>I. FEE BASIS VENDOR CORRECTION file (#161.25) Cleanup</u> 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# As part of the post-initialization process, the vendors residing in your FEE BASIS VENDOR CORRECTION file will be reviewed for accuracy. All vendors found with invalid vendor identification numbers will be removed from the file and placed in delete status in the FEE BASIS VENDOR file (#161.2). If any vendors are found, a mail message will be generated listing the vendor name and ID for each invalid entry. This mail message will be forwarded to the G.FEE mail group. Refer to Attachment E for a sample mail message.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# RESOURCE REQUIREMENTS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Formula for TUs: (# of FEE patients/160,000) + .04 = TUs needed Storage requirements:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Initial: .004 Mbytes/FEE patient

> Additional: (# of inpatient invoices X 335)/1,000,000

> (# of inpatient authorizations X 700)/1,000,000 (# of unauthorized claims X 630)/1,000,000

# Equipment requirements: No increase from Fee Basis Version 3.0.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 14%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="7"><span id="_bookmark5" class="anchor"></span>Section 2 - Attachments</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="7">ATTACHMENT A. ROUTINES</td>
</tr>
<tr class="even">
<td>FBAA79</td>
<td>FBAA79A</td>
<td>FBAAAUT</td>
<td><blockquote>
<p>FBAAAV</p>
</blockquote></td>
<td><blockquote>
<p>FBAABDL</p>
</blockquote></td>
<td><blockquote>
<p>FBAABET</p>
</blockquote></td>
<td>FBAABPG</td>
</tr>
<tr class="odd">
<td>FBAABS</td>
<td>FBAABT</td>
<td>FBAACCB</td>
<td><blockquote>
<p>FBAACCB0</p>
</blockquote></td>
<td><blockquote>
<p>FBAACCB1</p>
</blockquote></td>
<td><blockquote>
<p>FBAACCB2</p>
</blockquote></td>
<td>FBAACH</td>
</tr>
<tr class="even">
<td>FBAACIE</td>
<td>FBAACLU</td>
<td>FBAACO</td>
<td><blockquote>
<p>FBAACO0</p>
</blockquote></td>
<td><blockquote>
<p>FBAACO1</p>
</blockquote></td>
<td><blockquote>
<p>FBAACO2</p>
</blockquote></td>
<td>FBAACO3</td>
</tr>
<tr class="odd">
<td>FBAACO4</td>
<td>FBAACO5</td>
<td>FBAACP</td>
<td><blockquote>
<p>FBAACP1</p>
</blockquote></td>
<td><blockquote>
<p>FBAACR</p>
</blockquote></td>
<td><blockquote>
<p>FBAADCB</p>
</blockquote></td>
<td>FBAADD</td>
</tr>
<tr class="even">
<td>FBAADEM</td>
<td>FBAADEM1</td>
<td>FBAADOB</td>
<td><blockquote>
<p>FBAADV</p>
</blockquote></td>
<td><blockquote>
<p>FBAAEAR</p>
</blockquote></td>
<td><blockquote>
<p>FBAAELT</p>
</blockquote></td>
<td>FBAAEPI</td>
</tr>
<tr class="odd">
<td>FBAAESP</td>
<td>FBAAETA</td>
<td>FBAALB</td>
<td><blockquote>
<p>FBAALPI</p>
</blockquote></td>
<td><blockquote>
<p>FBAALU</p>
</blockquote></td>
<td><blockquote>
<p>FBAAMP</p>
</blockquote></td>
<td>FBAAMP1</td>
</tr>
<tr class="even">
<td>FBAAMPG1</td>
<td>FBAAMPRG</td>
<td>FBAAOB</td>
<td><blockquote>
<p>FBAAODP</p>
</blockquote></td>
<td><blockquote>
<p>FBAAODP0</p>
</blockquote></td>
<td><blockquote>
<p>FBAAPAA</p>
</blockquote></td>
<td>FBAAPAY</td>
</tr>
<tr class="odd">
<td>FBAAPCC</td>
<td>FBAAPDM</td>
<td>FBAAPET</td>
<td><blockquote>
<p>FBAAPH</p>
</blockquote></td>
<td><blockquote>
<p>FBAAPHV</p>
</blockquote></td>
<td><blockquote>
<p>FBAAPI</p>
</blockquote></td>
<td>FBAAPIE</td>
</tr>
<tr class="even">
<td>FBAAPIE1</td>
<td>FBAAPII</td>
<td>FBAAPIN</td>
<td><blockquote>
<p>FBAAPIN1</p>
</blockquote></td>
<td><blockquote>
<p>FBAAPIP</p>
</blockquote></td>
<td><blockquote>
<p>FBAAPIS</p>
</blockquote></td>
<td>FBAAPLU</td>
</tr>
<tr class="odd">
<td>FBAAPM</td>
<td>FBAAPOC</td>
<td>FBAAPP</td>
<td><blockquote>
<p>FBAAPP0</p>
</blockquote></td>
<td><blockquote>
<p>FBAAPPH</p>
</blockquote></td>
<td><blockquote>
<p>FBAAPRC</p>
</blockquote></td>
<td>FBAAPRGS</td>
</tr>
<tr class="even">
<td>FBAAPV</td>
<td>FBAARB</td>
<td>FBAARD</td>
<td><blockquote>
<p>FBAARD0</p>
</blockquote></td>
<td><blockquote>
<p>FBAARD1</p>
</blockquote></td>
<td><blockquote>
<p>FBAARD2</p>
</blockquote></td>
<td>FBAARD3</td>
</tr>
<tr class="odd">
<td>FBAARJP</td>
<td>FBAARMRA</td>
<td>FBAAROC</td>
<td><blockquote>
<p>FBAARP</p>
</blockquote></td>
<td><blockquote>
<p>FBAARR</p>
</blockquote></td>
<td><blockquote>
<p>FBAARR0</p>
</blockquote></td>
<td>FBAARR1</td>
</tr>
<tr class="even">
<td>FBAARR2</td>
<td>FBAARV</td>
<td>FBAAS79</td>
<td><blockquote>
<p>FBAASAP</p>
</blockquote></td>
<td><blockquote>
<p>FBAASCB</p>
</blockquote></td>
<td><blockquote>
<p>FBAASCB0</p>
</blockquote></td>
<td>FBAASL</td>
</tr>
<tr class="odd">
<td>FBAASL1</td>
<td>FBAASL1B</td>
<td>FBAASLP</td>
<td><blockquote>
<p>FBAASOUT</p>
</blockquote></td>
<td><blockquote>
<p>FBAASTA</p>
</blockquote></td>
<td><blockquote>
<p>FBAATIC</p>
</blockquote></td>
<td>FBAAUTL</td>
</tr>
<tr class="even">
<td>FBAAUTL1</td>
<td>FBAAUTL2</td>
<td>FBAAUTL3</td>
<td><blockquote>
<p>FBAAUTL4</p>
</blockquote></td>
<td><blockquote>
<p>FBAAUTL5</p>
</blockquote></td>
<td><blockquote>
<p>FBAAV0</p>
</blockquote></td>
<td>FBAAV01</td>
</tr>
<tr class="odd">
<td>FBAAV1</td>
<td>FBAAV2</td>
<td>FBAAV3</td>
<td><blockquote>
<p>FBAAV4</p>
</blockquote></td>
<td><blockquote>
<p>FBAAV5</p>
</blockquote></td>
<td><blockquote>
<p>FBAAV6</p>
</blockquote></td>
<td>FBAAVD</td>
</tr>
<tr class="even">
<td>FBAAVD1</td>
<td>FBAAVD2</td>
<td>FBAAVLU</td>
<td><blockquote>
<p>FBAAVP</p>
</blockquote></td>
<td><blockquote>
<p>FBAAVP0</p>
</blockquote></td>
<td><blockquote>
<p>FBAAVR</p>
</blockquote></td>
<td>FBAAVR0</td>
</tr>
<tr class="odd">
<td>FBAAVR1</td>
<td>FBAAVR2</td>
<td>FBAAVS</td>
<td><blockquote>
<p>FBAUTHP</p>
</blockquote></td>
<td><blockquote>
<p>FBCH78</p>
</blockquote></td>
<td><blockquote>
<p>FBCH780</p>
</blockquote></td>
<td>FBCH78A</td>
</tr>
<tr class="even">
<td>FBCHACT</td>
<td>FBCHACT0</td>
<td>FBCHACT1</td>
<td><blockquote>
<p>FBCHC78</p>
</blockquote></td>
<td><blockquote>
<p>FBCHCD</p>
</blockquote></td>
<td><blockquote>
<p>FBCHCO</p>
</blockquote></td>
<td>FBCHCR</td>
</tr>
<tr class="odd">
<td>FBCHCR1</td>
<td>FBCHDEL</td>
<td>FBCHDI</td>
<td><blockquote>
<p>FBCHDI2</p>
</blockquote></td>
<td><blockquote>
<p>FBCHDIN</p>
</blockquote></td>
<td><blockquote>
<p>FBCHDUC</p>
</blockquote></td>
<td>FBCHEAP</td>
</tr>
<tr class="even">
<td>FBCHEP</td>
<td>FBCHEP1</td>
<td>FBCHEUC</td>
<td><blockquote>
<p>FBCHEUC1</p>
</blockquote></td>
<td><blockquote>
<p>FBCHEUC2</p>
</blockquote></td>
<td><blockquote>
<p>FBCHP78</p>
</blockquote></td>
<td>FBCHPET</td>
</tr>
<tr class="odd">
<td>FBCHPH</td>
<td>FBCHPH0</td>
<td>FBCHPRC</td>
<td><blockquote>
<p>FBCHPRC1</p>
</blockquote></td>
<td><blockquote>
<p>FBCHPSA</p>
</blockquote></td>
<td><blockquote>
<p>FBCHPSA0</p>
</blockquote></td>
<td>FBCHPSA1</td>
</tr>
<tr class="even">
<td>FBCHREQ</td>
<td>FBCHREQ1</td>
<td>FBCHREQ2</td>
<td><blockquote>
<p>FBCHRJP</p>
</blockquote></td>
<td><blockquote>
<p>FBCHROC</p>
</blockquote></td>
<td><blockquote>
<p>FBCHRR</p>
</blockquote></td>
<td>FBCHSCB</td>
</tr>
<tr class="odd">
<td>FBCHSL1</td>
<td>FBCHSLP</td>
<td>FBCHSTA</td>
<td><blockquote>
<p>FBCHSTAT</p>
</blockquote></td>
<td><blockquote>
<p>FBCHVH</p>
</blockquote></td>
<td><blockquote>
<p>FBCHVP</p>
</blockquote></td>
<td>FBCKDIS</td>
</tr>
<tr class="even">
<td>FBCKDIS1</td>
<td>FBCNHCEN</td>
<td>FBDOC</td>
<td><blockquote>
<p>FBINI001</p>
</blockquote></td>
<td><blockquote>
<p>FBINI002</p>
</blockquote></td>
<td><blockquote>
<p>FBINI003</p>
</blockquote></td>
<td>FBINI004</td>
</tr>
<tr class="odd">
<td>FBINI005</td>
<td>FBINI006</td>
<td>FBINI007</td>
<td><blockquote>
<p>FBINI008</p>
</blockquote></td>
<td><blockquote>
<p>FBINI009</p>
</blockquote></td>
<td><blockquote>
<p>FBINI00A</p>
</blockquote></td>
<td>FBINI00B</td>
</tr>
<tr class="even">
<td>FBINI00C</td>
<td>FBINI00D</td>
<td>FBINI00E</td>
<td><blockquote>
<p>FBINI00F</p>
</blockquote></td>
<td><blockquote>
<p>FBINI00G</p>
</blockquote></td>
<td><blockquote>
<p>FBINI00H</p>
</blockquote></td>
<td>FBINI00I</td>
</tr>
<tr class="odd">
<td>FBINI00J</td>
<td>FBINI00K</td>
<td>FBINI00L</td>
<td><blockquote>
<p>FBINI00M</p>
</blockquote></td>
<td><blockquote>
<p>FBINI00N</p>
</blockquote></td>
<td><blockquote>
<p>FBINI00O</p>
</blockquote></td>
<td>FBINI00P</td>
</tr>
<tr class="even">
<td>FBINI00Q</td>
<td>FBINI00R</td>
<td>FBINI00S</td>
<td><blockquote>
<p>FBINI00T</p>
</blockquote></td>
<td><blockquote>
<p>FBINI00U</p>
</blockquote></td>
<td><blockquote>
<p>FBINI00V</p>
</blockquote></td>
<td>FBINI00W</td>
</tr>
<tr class="odd">
<td>FBINI00X</td>
<td>FBINI00Y</td>
<td>FBINI00Z</td>
<td><blockquote>
<p>FBINI010</p>
</blockquote></td>
<td><blockquote>
<p>FBINI011</p>
</blockquote></td>
<td><blockquote>
<p>FBINI012</p>
</blockquote></td>
<td>FBINI013</td>
</tr>
<tr class="even">
<td>FBINI014</td>
<td>FBINI015</td>
<td>FBINI016</td>
<td><blockquote>
<p>FBINI017</p>
</blockquote></td>
<td><blockquote>
<p>FBINI018</p>
</blockquote></td>
<td><blockquote>
<p>FBINI019</p>
</blockquote></td>
<td>FBINI01A</td>
</tr>
<tr class="odd">
<td>FBINI01B</td>
<td>FBINI01C</td>
<td>FBINI01D</td>
<td><blockquote>
<p>FBINI01E</p>
</blockquote></td>
<td><blockquote>
<p>FBINI01F</p>
</blockquote></td>
<td><blockquote>
<p>FBINI01G</p>
</blockquote></td>
<td>FBINI01H</td>
</tr>
<tr class="even">
<td>FBINI01I</td>
<td>FBINI01J</td>
<td>FBINI01K</td>
<td><blockquote>
<p>FBINI01L</p>
</blockquote></td>
<td><blockquote>
<p>FBINI01M</p>
</blockquote></td>
<td><blockquote>
<p>FBINI01N</p>
</blockquote></td>
<td>FBINI01O</td>
</tr>
<tr class="odd">
<td>FBINI01P</td>
<td>FBINI01Q</td>
<td>FBINI01R</td>
<td><blockquote>
<p>FBINI01S</p>
</blockquote></td>
<td><blockquote>
<p>FBINI01T</p>
</blockquote></td>
<td><blockquote>
<p>FBINI01U</p>
</blockquote></td>
<td>FBINI01V</td>
</tr>
<tr class="even">
<td>FBINI01W</td>
<td>FBINI01X</td>
<td>FBINI01Y</td>
<td><blockquote>
<p>FBINI01Z</p>
</blockquote></td>
<td><blockquote>
<p>FBINI020</p>
</blockquote></td>
<td><blockquote>
<p>FBINI021</p>
</blockquote></td>
<td>FBINI022</td>
</tr>
<tr class="odd">
<td>FBINI023</td>
<td>FBINI024</td>
<td>FBINI025</td>
<td><blockquote>
<p>FBINI026</p>
</blockquote></td>
<td><blockquote>
<p>FBINI027</p>
</blockquote></td>
<td><blockquote>
<p>FBINI028</p>
</blockquote></td>
<td>FBINI029</td>
</tr>
<tr class="even">
<td>FBINI02A</td>
<td>FBINI02B</td>
<td>FBINI02C</td>
<td><blockquote>
<p>FBINI02D</p>
</blockquote></td>
<td><blockquote>
<p>FBINI02E</p>
</blockquote></td>
<td><blockquote>
<p>FBINI02F</p>
</blockquote></td>
<td>FBINI02G</td>
</tr>
<tr class="odd">
<td>FBINI02H</td>
<td>FBINI02I</td>
<td>FBINI02J</td>
<td><blockquote>
<p>FBINI02K</p>
</blockquote></td>
<td><blockquote>
<p>FBINI02L</p>
</blockquote></td>
<td><blockquote>
<p>FBINI02M</p>
</blockquote></td>
<td>FBINI02N</td>
</tr>
<tr class="even">
<td>FBINI02O</td>
<td>FBINI02P</td>
<td>FBINI02Q</td>
<td><blockquote>
<p>FBINI02R</p>
</blockquote></td>
<td><blockquote>
<p>FBINI02S</p>
</blockquote></td>
<td><blockquote>
<p>FBINI02T</p>
</blockquote></td>
<td>FBINI02U</td>
</tr>
<tr class="odd">
<td>FBINI02V</td>
<td>FBINI02W</td>
<td>FBINI02X</td>
<td><blockquote>
<p>FBINI02Y</p>
</blockquote></td>
<td><blockquote>
<p>FBINI02Z</p>
</blockquote></td>
<td><blockquote>
<p>FBINI030</p>
</blockquote></td>
<td>FBINI031</td>
</tr>
<tr class="even">
<td>FBINI032</td>
<td>FBINI033</td>
<td>FBINI034</td>
<td><blockquote>
<p>FBINI035</p>
</blockquote></td>
<td><blockquote>
<p>FBINI036</p>
</blockquote></td>
<td><blockquote>
<p>FBINI037</p>
</blockquote></td>
<td>FBINI038</td>
</tr>
<tr class="odd">
<td>FBINI039</td>
<td>FBINI03A</td>
<td>FBINI03B</td>
<td><blockquote>
<p>FBINI03C</p>
</blockquote></td>
<td><blockquote>
<p>FBINI03D</p>
</blockquote></td>
<td><blockquote>
<p>FBINI03E</p>
</blockquote></td>
<td>FBINI03F</td>
</tr>
<tr class="even">
<td>FBINI03G</td>
<td>FBINI03H</td>
<td>FBINI03I</td>
<td><blockquote>
<p>FBINI03J</p>
</blockquote></td>
<td><blockquote>
<p>FBINI03K</p>
</blockquote></td>
<td><blockquote>
<p>FBINI03L</p>
</blockquote></td>
<td>FBINI03M</td>
</tr>
<tr class="odd">
<td>FBINI03N</td>
<td>FBINI03O</td>
<td>FBINI03P</td>
<td><blockquote>
<p>FBINI03Q</p>
</blockquote></td>
<td><blockquote>
<p>FBINI03R</p>
</blockquote></td>
<td><blockquote>
<p>FBINI03S</p>
</blockquote></td>
<td>FBINI03T</td>
</tr>
<tr class="even">
<td>FBINI03U</td>
<td>FBINI03V</td>
<td>FBINI03W</td>
<td><blockquote>
<p>FBINI03X</p>
</blockquote></td>
<td><blockquote>
<p>FBINI03Y</p>
</blockquote></td>
<td><blockquote>
<p>FBINI03Z</p>
</blockquote></td>
<td>FBINI040</td>
</tr>
<tr class="odd">
<td>FBINI041</td>
<td>FBINI042</td>
<td>FBINI043</td>
<td><blockquote>
<p>FBINI044</p>
</blockquote></td>
<td><blockquote>
<p>FBINI045</p>
</blockquote></td>
<td><blockquote>
<p>FBINI046</p>
</blockquote></td>
<td>FBINI047</td>
</tr>
<tr class="even">
<td>FBINI048</td>
<td>FBINI049</td>
<td>FBINI04A</td>
<td><blockquote>
<p>FBINI04B</p>
</blockquote></td>
<td><blockquote>
<p>FBINI04C</p>
</blockquote></td>
<td><blockquote>
<p>FBINI04D</p>
</blockquote></td>
<td>FBINI04E</td>
</tr>
<tr class="odd">
<td>FBINI04F</td>
<td>FBINI04G</td>
<td>FBINI04H</td>
<td><blockquote>
<p>FBINI04I</p>
</blockquote></td>
<td><blockquote>
<p>FBINI04J</p>
</blockquote></td>
<td><blockquote>
<p>FBINI04K</p>
</blockquote></td>
<td>FBINI04L</td>
</tr>
<tr class="even">
<td>FBINI04M</td>
<td>FBINI04N</td>
<td>FBINI04O</td>
<td><blockquote>
<p>FBINI04P</p>
</blockquote></td>
<td><blockquote>
<p>FBINI04Q</p>
</blockquote></td>
<td><blockquote>
<p>FBINI04R</p>
</blockquote></td>
<td>FBINIS</td>
</tr>
<tr class="odd">
<td>FBINIT</td>
<td>FBINIT1</td>
<td>FBINIT2</td>
<td><blockquote>
<p>FBINIT3</p>
</blockquote></td>
<td><blockquote>
<p>FBINIT4</p>
</blockquote></td>
<td>FBINIT5</td>
<td>FBMRASV1</td>
</tr>
<tr class="even">
<td>FBMRASV2</td>
<td>FBMRASVR</td>
<td>FBNHACT</td>
<td><blockquote>
<p>FBNHAMI1</p>
</blockquote></td>
<td><blockquote>
<p>FBNHAMI2</p>
</blockquote></td>
<td>FBNHAMIE</td>
<td>FBNHAMIS</td>
</tr>
</tbody>
</table>

| Section 2. Attachments |          |          |          |          |          |          |
|------------------------|----------|----------|----------|----------|----------|----------|
| ATTACHMENT A. ROUTINES |          |          |          |          |          |          |
| FBNHDEC                | FBNHDIEP | FBNHDLAD | FBNHDLDI | FBNHDLTR | FBNHEA   | FBNHEAU1 |
| FBNHEAU2               | FBNHEAUT | FBNHED   | FBNHEDA1 | FBNHEDAD | FBNHEDAT | FBNHEDDI |
| FBNHEDPA               | FBNHEDTR | FBNHEP   | FBNHEP1  | FBNHEP2  | FBNHET   | FBNHEXP  |
| FBNHPAMS               | FBNHPC   | FBNHPC1  | FBNHPLT  | FBNHRAT  | FBNHRAT1 | FBNHRC   |
| FBNHRCS                | FBNHRCS1 | FBNHRCS2 | FBNHRCS3 | FBNHRCS4 | FBNHRDEL | FBNHROS  |
| FBNTEG                 | FBNTEG0  | FBONI001 | FBONIT   | FBONIT1  | FBONIT2  | FBONIT3  |
| FBP35D                 | FBPAID   | FBPAID1  | FBPAID2  | FBPAY    | FBPAY2   | FBPAY21  |
| FBPAY3                 | FBPAY67  | FBPAY671 | FBPCR    | FBPCR2   | FBPCR3   | FBPCR67  |
| FBPCR671               | FBPHON   | FBPHON1  | FBPHON2  | FBPRE35  | FBPRICE  | FBPRICE1 |
| FBPST35                | FBPST35A | FBPST35B | FBPST35C | FBUCDD   | FBUCDD1  | FBUCDIS  |
| FBUCDUP                | FBUCED   | FBUCED0  | FBUCED1  | FBUCEN   | FBUCEN1  | FBUCEVT  |
| FBUCEX                 | FBUCLET  | FBUCLET0 | FBUCLET1 | FBUCLINK | FBUCLNK1 | FBUCOUT  |
| FBUCOUT1               | FBUCPAY  | FBUCPEND | FBUCSTAT | FBUCUPD  | FBUCUPD1 | FBUCUTL  |
| FBUCUTL1               | FBUCUTL2 | FBUCUTL3 | FBUCUTL4 | FBUCUTL5 | FBUCUTL6 | FBUCUTL7 |
| FBUCUTL8               | FBUINS   | FBVDISP  |          |          |          |          |
| 458 routines           |          |          |          |          |          |          |

# ATTACHMENT B. FBINIT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \>D ^FBINIT

This version (#3.5) of 'FBINIT' was created on 30-JAN-1995

> (at ALBANY ISC VAX DEVELOPMENT, by VA FileMan V.20.0)

I HAVE TO RUN AN ENVIRONMENT CHECK ROUTINE. I AM GOING TO SET UP THE FOLLOWING FILES:

161. FEE BASIS PATIENT

> **NOTE:** You already have the 'FEE BASIS PATIENT' File.

> 161.2 FEE BASIS VENDOR

> **NOTE:** You already have the 'FEE BASIS VENDOR' File.

21. FEE BASIS CNH CONTRACT

> **NOTE:** You already have the 'FEE BASIS CNH CONTRACT' File.

22. FEE BASIS CNH RATE

> **NOTE:** You already have the 'FEE BASIS CNH RATE' File.

23. FEE BASIS CNH AUTHORIZATION RATE

> **NOTE:** You already have the 'FEE BASIS CNH AUTHORIZATION RATE' File.

25. FEE BASIS VENDOR CORRECTION

> **NOTE:** You already have the 'FEE BASIS VENDOR CORRECTION' File.

26. FEE BASIS PATIENT MRA

> **NOTE:** You already have the 'FEE BASIS PATIENT MRA' File.

27. FEE BASIS SUSPENSION (including data) Note: You already have the 'FEE BASIS SUSPENSION' File. I will OVERWRITE your data with mine.
3.  FEE BASIS LETTER (including data) Note: You already have the 'FEE BASIS LETTER' File. I will MERGE your data with mine.
4.  FEE BASIS SITE PARAMETERS

> **NOTE:** You already have the 'FEE BASIS SITE PARAMETERS' File.

5.  FEE CH REPORT OF CONTACT

> **NOTE:** You already have the 'FEE CH REPORT OF CONTACT' File.

6.  FEE BASIS SPECIALTY CODE (including data) Note: You already have the 'FEE BASIS SPECIALTY CODE' File. I will OVERWRITE your data with mine.
7.  FEE BASIS BATCH

> **NOTE:** You already have the 'FEE BASIS BATCH' File.

8.  FEE BASIS PROGRAM (including data) Note: You already have the 'FEE BASIS PROGRAM' File. I will OVERWRITE your data with mine.

# ATTACHMENT B. FBINIT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

81. FEE BASIS PARTICIPATION CODE (including data) Note: You already have the 'FEE BASIS PARTICIPATION CODE' File. I will OVERWRITE your data with mine.
82. FEE BASIS PURPOSE OF VISIT

> **NOTE:** You already have the 'FEE BASIS PURPOSE OF VISIT' File.

83. FEE BASIS ID CARD AUDIT

> **NOTE:** You already have the 'FEE BASIS ID CARD AUDIT' File.

162. FEE BASIS PAYMENT

> **NOTE:** You already have the 'FEE BASIS PAYMENT' File.

1.  FEE BASIS PHARMACY INVOICE

> **NOTE:** You already have the 'FEE BASIS PHARMACY INVOICE' File.

2.  FEE NOTIFICATION/REQUEST

> **NOTE:** You already have the 'FEE NOTIFICATION/REQUEST' File.

3.  FEE CNH ACTIVITY

> **NOTE:** You already have the 'FEE CNH ACTIVITY' File.

> 162.4 VA FORM 10-7078

> **NOTE:** You already have the 'VA FORM 10-7078' File.

5.  FEE BASIS INVOICE

> **NOTE:** You already have the 'FEE BASIS INVOICE' File.

6.  FEE BASIS DISPOSITION CODE (including data) Note: You already have the 'FEE BASIS DISPOSITION CODE' File. I will OVERWRITE your data with mine.
7.  FEE BASIS UNAUTHORIZED CLAIMS

> **NOTE:** You already have the 'FEE BASIS UNAUTHORIZED CLAIMS' File.

8.  FEE BASIS UNAUTHORIZED CLAIMS PENDING INFO

> **NOTE:** You already have the 'FEE BASIS UNAUTHORIZED CLAIMS PENDING INFO' File.

91. FEE BASIS UNAUTHORIZED CLAIMS DISPOSITIONS (including data) Note: You already have the 'FEE BASIS UNAUTHORIZED CLAIMS DISPOSITIONS' File. I will OVERWRITE your data with mine.
92. FEE BASIS UNAUTHORIZED CLAIMS STATUS (including data) Note: You already have the 'FEE BASIS UNAUTHORIZED CLAIMS STATUS' File. I will OVERWRITE your data with mine.
93. FEE BASIS UNAUTHORIZED REQUESTED INFORMATION

> **NOTE:** You already have the 'FEE BASIS UNAUTHORIZED REQUESTED INFORMATION'

File.

94. FEE BASIS UNAUTHORIZED DISAPPROVAL REASONS (including data) Note: You already have the 'FEE BASIS UNAUTHORIZED DISAPPROVAL REASONS' File. I will OVERWRITE your data with mine.
95. FEE BASIS CHECK CANCELLATION REASON (including data) I will OVERWRITE your data with mine.

# ATTACHMENT B. FBINIT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

163.85 FEE BASIS VA TYPE OF SERVICE (including data) Note: You already have the 'FEE BASIS VA TYPE OF SERVICE' File. I will OVERWRITE your data with mine.

> 163.99 FEE BASIS FEE SCHEDULE

> **NOTE:** You already have the 'FEE BASIS FEE SCHEDULE' File.

SHALL I WRITE OVER FILE SECURITY CODES? NO// \<RET\> (NO)

> **NOTE:** This package also contains BULLETINS

> SHALL I WRITE OVER EXISTING BULLETINS OF THE SAME NAME? YES// \<RET\>

> (YES)

> **NOTE:** This package also contains SORT TEMPLATES

> SHALL I WRITE OVER EXISTING SORT TEMPLATES OF THE SAME NAME? YES// \<RET\>

> (YES)

> **NOTE:** This package also contains INPUT TEMPLATES

> SHALL I WRITE OVER EXISTING INPUT TEMPLATES OF THE SAME NAME? YES// \<RET\>

> (YES)

> **NOTE:** This package also contains PRINT TEMPLATES

> SHALL I WRITE OVER EXISTING PRINT TEMPLATES OF THE SAME NAME? YES// \<RET\>

> (YES)

> **NOTE:** This package also contains SECURITY KEYS

> SHALL I WRITE OVER EXISTING SECURITY KEYS OF THE SAME NAME? YES// \<RET\>

> (YES)

> **NOTE:** This package also contains OPTIONS

> SHALL I WRITE OVER EXISTING OPTIONS OF THE SAME NAME? YES// \<RET\>

> (YES)

ARE YOU SURE EVERYTHING'S OK? NO// Y (YES)

...SORRY, JUST A MOMENT PLEASE..............................................

............................................................................

............................................................................

..................................................................

'FB INSURANCE CHANGE' BULLETIN FILED -- Remember to add mail groups for new bulletins.

'FBAA BATCH PURGE' BULLETIN FILED -- Remember to add mail groups for new bulletins.

'FBAA PURGE' BULLETIN FILED -- Remember to add mail groups for new bulletins. 'FBAA PURGE TRANSMITTED MRA'S' BULLETIN FILED -- Remember to add mail groups for new bulletins............................................................

.............................................................................

.............................................................................

...........

'FB CHECK DISPLAY' Option Filed 'FB MRA MAIN MENU' Option Filed 'FB PAY VENDOR' Option Filed 'FB PAY VETERAN' Option Filed 'FB PCR' Option Filed

'FB PHONE MENU' Option Filed

'FB VENDOR/VETERAN PAYMENTS' Option Filed 'FBAA ACTIVE BATCH LISTING' Option Filed 'FBAA AUTHORIZATION DISPLAY' Option Filed

'FBAA BATCH DELETE' Option Filed 'FBAA BATCH EDIT' Option Filed 'FBAA BATCH MENU' Option Filed 'FBAA BATCH RANGE' Option Filed

'FBAA BATCH STATUS' Option Filed

# ATTACHMENT B. FBINIT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

'FBAA C&P ENTER PAYMENT' Option Filed 'FBAA CALCULATE SCHEDULE' Option Filed 'FBAA CANCEL MEDICAL VOID' Option Filed 'FBAA CANCEL PHARMACY VOID' Option Filed

'FBAA CLERK LOOK-UP' Option Filed 'FBAA CLOSE BATCH' Option Filed

'FBAA CLOSE OUT INVOICE' Option Filed

'FBAA COMPLETE PHARMACY INVOICE' Option Filed

'FBAA COST REPORT' Option Filed 'FBAA DELETE PAYMENT' Option Filed

'FBAA DISPLAY ID CARD HISTORY' Option Filed 'FBAA DISPLAY OPEN BATCHES' Option Filed 'FBAA EDIT INVOICE STATUS' Option Filed

'FBAA EDIT PAYMENT' Option Filed

'FBAA EDIT PHARMACY INVOICE' Option Filed

'FBAA EDIT SCHEDULE' Option Filed

'FBAA ENTER AUTHORIZATION' Option Filed

'FBAA ENTER PAYMENT' Option Filed

'FBAA ENTER PHARMACY INVOICE' Option Filed 'FBAA ENTER SITE PARAMETERS' Option Filed 'FBAA ENTER/EDIT LETTERS' Option Filed

'FBAA FEE SCHEDULE' Option Filed 'FBAA FINALIZE BATCH' Option Filed 'FBAA FMS UPDATE' Option Filed

'FBAA ID CARDS CURRENT LIST' Option Filed 'FBAA INVOICE DISPLAY' Option Filed

'FBAA LIST BATCH' Option Filed

'FBAA LIST CLOSED BATCHES' Option Filed 'FBAA LIST PENDING RX' Option Filed 'FBAA MAIN MENU' Option Filed

'FBAA MEDICAL MAIN MENU' Option Filed 'FBAA MEDICAL REIMBURSEMENT' Option Filed 'FBAA MEDICAL VOID PAYMENT' Option Filed 'FBAA MRA DELETE VENDOR' Option Filed

'FBAA MRA PURGE' Option Filed 'FBAA MRA PURGE AUTO' Option Filed 'FBAA MRA SERVER' Option Filed

'FBAA MRA VENDOR REINSTATE' Option Filed 'FBAA MRA VETERAN ADD TYPE' Option Filed 'FBAA MRA VETERAN CHANGE TYPE' Option Filed 'FBAA MRA VETERAN DELETE TYPE' Option Filed 'FBAA MRA VETERAN REINSTATE' Option Filed 'FBAA MRA'S AWAITING APPROVAL' Option Filed 'FBAA MULTIPLE PAYMENT ENTRY' Option Filed 'FBAA OBSOLETE ID CARDS' Option Filed

'FBAA OPEN BATCH' Option Filed

'FBAA OPEN PHARMACY BATCH' Option Filed

'FBAA OUTPUTS MENU' Option Filed 'FBAA PAID SERVER' Option Filed 'FBAA PATIENT INQUIRY' Option Filed

'FBAA PAYMENT HISTORY DISPLAY' Option Filed

'FBAA PAYMENT MENU' Option Filed

'FBAA PENDING MAS COMPLETION' Option Filed 'FBAA PHARMACY BATCH OPTIONS' Option Filed 'FBAA PHARMACY HISTORY' Option Filed

'FBAA PHARMACY INVOICE DISPLAY' Option Filed

# ATTACHMENT B. FBINIT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

'FBAA PHARMACY INVOICE STATUS' Option Filed 'FBAA PHARMACY LOOKUP' Option Filed

'FBAA PHARMACY MAIN MENU' Option Filed 'FBAA PHARMACY REVIEW' Option Filed

'FBAA PHARMACY VOID PAYMENT' Option Filed 'FBAA PRINT 7079 GROUP' Option Filed 'FBAA PRINT 7079 SINGLE' Option Filed

'FBAA PRINT REPORT OF CONTACT' Option Filed 'FBAA PRINT SCHEDULE' Option Filed

'FBAA QUEUE DATA FOR TRANS.' Option Filed 'FBAA REGISTRATION MAIN MENU' Option Filed 'FBAA REIMBURSEMENT PHARMACY' Option Filed 'FBAA REINITIATE REJECTS' Option Filed

'FBAA REJECT PRINT' Option Filed 'FBAA REOPEN BATCH' Option Filed 'FBAA REPORT OF CONTACT' Option Filed

'FBAA REQUEUE MRA' Option Filed

'FBAA SUPERVISOR OPTIONS' Option Filed 'FBAA SUPERVISOR RELEASE' Option Filed 'FBAA SUSPENSION LETTER INDIV' Option Filed 'FBAA SUSPENSION LETTER PRINT' Option Filed 'FBAA TERMINATE ID CARD' Option Filed

'FBAA TRAVEL ENTRY' Option Filed

'FBAA VENDOR DEMOGRAPHICS' Option Filed

'FBAA VENDOR LOOKUP' Option Filed

'FBAA VENDOR MRA MAIN MENU' Option Filed 'FBAA VENDOR OPTIONS' Option Filed

'FBAA VENDOR PAYMENT DISPLAY' Option Filed 'FBAA VETERAN MRA MAIN MENU' Option Filed 'FBAA VOID PAYMENT MENU' Option Filed 'FBAA VOUCHER DELETE REJECT' Option Filed

'FBCH 7078 SETUP' Option Filed

'FBCH ANCILLARY PAYMENT' Option Filed

'FBCH ANCILLARY REIMBURSEMENT' Option Filed

'FBCH BATCH OPTIONS' Option Filed 'FBCH CANCEL 7078' Option Filed 'FBCH CENSUS REPORT' Option Filed 'FBCH COMPLETE 7078' Option Filed 'FBCH COMPLETE PAYMENT' Option Filed

'FBCH COST REPORT' Option Filed 'FBCH DELETE INVOICE' Option Filed 'FBCH DELETE REQUEST' Option Filed 'FBCH DELETE VOID' Option Filed 'FBCH DISPLAY 7078' Option Filed 'FBCH DISPLAY REQUEST' Option Filed 'FBCH DISPOSITION MENU' Option Filed

'FBCH EDIT 7078' Option Filed

'FBCH EDIT ANCILLARY PAYMENT' Option Filed

'FBCH EDIT PAYMENT' Option Filed

'FBCH EDIT REPORT OF CONTACT' Option Filed

'FBCH EDIT REQUEST' Option Filed 'FBCH ENTER PAYMENT' Option Filed 'FBCH ENTER REQUEST' Option Filed 'FBCH GENERIC PRICER' Option Filed 'FBCH HOSPITAL ACTIVITY' Option Filed 'FBCH INVOICE DISPLAY' Option Filed

# ATTACHMENT B. FBINIT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

'FBCH LEGAL ENTITLEMENT' Option Filed

'FBCH MAIN MENU' Option Filed

'FBCH MEDICAL ENTITLEMENT' Option Filed 'FBCH MULTIPLE PAYMENTS' Option Filed 'FBCH NOTIFICATION MENU' Option Filed 'FBCH OPEN ANCILLARY BATCH' Option Filed

'FBCH OPEN BATCH' Option Filed 'FBCH OUTPUT MENU' Option Filed 'FBCH PAYMENT MENU' Option Filed 'FBCH PENDING REQUEST' Option Filed 'FBCH PRICER REJECTS' Option Filed 'FBCH PRICER RELEASE' Option Filed 'FBCH PRINT 7078' Option Filed

'FBCH PRINT CANCELLED 7078' Option Filed 'FBCH PRINT REPORT OF CONTACT' Option Filed 'FBCH PRINT REQUEST AUDIT' Option Filed

'FBCH PSA OUTPUT' Option Filed

'FBCH REIMBURSEMENT INVOICE' Option Filed 'FBCH REINITIATE PRICER REJECTS' Option Filed 'FBCH REOPEN REQUEST' Option Filed

'FBCH REQUEST STATS' Option Filed 'FBCH UC COST REPORT' Option Filed

'FBCH UPDATE REPORT OF CONTACT' Option Filed

'FBCH VOID PAYMENT' Option Filed 'FBCNH ACTIVITY REPORT' Option Filed

'FBCNH ADMISSIONS \> 90 DAYS' Option Filed

'FBCNH ADMIT' Option Filed 'FBCNH AMIE' Option Filed 'FBCNH AMIS' Option Filed

'FBCNH AUTHORIZATION MAIN MENU' Option Filed 'FBCNH BATCH MAIN MENU' Option Filed

'FBCNH CANCEL 7078' Option Filed 'FBCNH CENSUS REPORT' Option Filed 'FBCNH COST REPORT' Option Filed 'FBCNH DELETE ADMISSION' Option Filed 'FBCNH DELETE DISCHARGE' Option Filed

'FBCNH DELETE MOVEMENT MENU' Option Filed

'FBCNH DELETE RATE' Option Filed 'FBCNH DELETE TRANSFER' Option Filed

'FBCNH DELETE VOID' Option Filed 'FBCNH DISCHARGE' Option Filed 'FBCNH DISPLAY 7078' Option Filed

'FBCNH DISPLAY EPISODE OF CARE' Option Filed 'FBCNH EDIT ADMISSION' Option Filed

'FBCNH EDIT AUTHORIZATION' Option Filed 'FBCNH EDIT DISCHARGE' Option Filed 'FBCNH EDIT MOVEMENT' Option Filed 'FBCNH EDIT PAYMENT' Option Filed 'FBCNH EDIT TRANSFER' Option Filed

'FBCNH ENTER AUTHORIZATION' Option Filed 'FBCNH ENTER PAYMENT' Option Filed 'FBCNH ENTER VETERAN RATES' Option Filed 'FBCNH ESTIMATE FUNDS' Option Filed 'FBCNH EXPIRATION REPORT' Option Filed

'FBCNH FUND CONTROL MAIN MENU' Option Filed 'FBCNH LIST PAYMENT & TOTALS' Option Filed

# ATTACHMENT B. FBINIT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

'FBCNH MAIN MENU' Option Filed

'FBCNH MOVEMENT MAIN MENU' Option Filed

'FBCNH OPEN BATCH' Option Filed

'FBCNH OUTPUTS MAIN MENU' Option Filed 'FBCNH PAYMENT MAIN MENU' Option Filed 'FBCNH POST COMMITMENTS' Option Filed

'FBCNH PRINT ROSTER' Option Filed 'FBCNH RATE CHANGE' Option Filed

'FBCNH RCS 10-0168 REPORT' Option Filed

'FBCNH TRANSFER' Option Filed

'FBCNH UPDATE VENDOR CONTRACT' Option Filed 'FBCNH VENDOR ENTER/EDIT' Option Filed

'FBCNH VOID PAYMENT' Option Filed 'FBUC ABANDONED' Option Filed 'FBUC ADD NEW PERSON' Option Filed

'FBUC ALL CLAIMS OUTPUT' Option Filed

'FBUC APPEAL EDIT' Option Filed 'FBUC ASSOCIATE' Option Filed

'FBUC BATCH PRINT LETTERS' Option Filed

'FBUC COVA APPEAL' Option Filed

'FBUC DELETE UNAUTHORIZED CLAIM' Option Filed

'FBUC DISASSOCIATE' Option Filed

'FBUC DISPLAY UNAUTHORIZED' Option Filed 'FBUC DISPOSITION UNAUTH CLAIM' Option Filed

'FBUC ENTER' Option Filed 'FBUC ENTER/EDIT' Option Filed

'FBUC EXPIRE OUTPUT' Option Filed 'FBUC INITIATE APPEAL' Option Filed

'FBUC LETTERS' Option Filed 'FBUC MAIN' Option Filed

'FBUC MODIFY UNAUTHORIZED CLAIM' Option Filed

'FBUC OUTPUTS' Option Filed 'FBUC PAYMENTS' Option Filed

'FBUC QUEUE BATCH PRINT' Option Filed 'FBUC RECEIVE INFORMATION' Option Filed

'FBUC REOPEN' Option Filed

'FBUC REPRINT LETTER(S)' Option Filed 'FBUC REQUEST INFO FILE' Option Filed 'FBUC REQUEST INFORMATION' Option Filed 'FBUC RETURN ADDRESS DIS/ED' Option Filed

'FBUC STATS OUTPUT' Option Filed 'FBUC STATUS OUTPUT' Option Filed

'FBUC UPDATE DATE LETTER SENT' Option Filed

'FBUC UTILITIES' Option Filed................................................

Compiling FB VENDOR UPDATE input template of File 161.2...

'FBCTV' ROUTINE FILED......

'FBCTV1' ROUTINE FILED......

'FBCTV2' ROUTINE FILED.....

'FBCTV3' ROUTINE FILED.. 'FBCTV4' ROUTINE FILED

# ATTACHMENT B. FBINIT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Compiling FBAA AUTHORIZATION input template of File 161.. 'FBCTAU' ROUTINE FILED...

'FBCTAU2' ROUTINE FILED.. 'FBCTAU1' ROUTINE FILED......

'FBCTAU3' ROUTINE FILED.......

'FBCTAU4' ROUTINE FILED...

'FBCTAU5' ROUTINE FILED. 'FBCTAU6' ROUTINE FILED

NO SECURITY-CODE PROTECTION HAS BEEN MADE

Starting Post Init FBPST35 1/30/95@15:12:42 Completed FBPST35 1/30/95@15:12:44

Beginning FBPST35A....

> CONVERSION OF DENIALS FILES

Now I will move any Medical Denial information you wish to keep into the Fee Basis Payment File (#162). I will then remove the Fee Basis Medical Denials file (#163) and the Fee Basis Pharmacy Denials file (#163.1).

Do you want to keep any Medical Denials that are presently stored in the Fee Basis Medical Denials file (#163)? No// YES

You may elect to merge all of your Fee Basis Medical Denials. If you choose not to retain all denials, you will be prompted to select a STARTING DATE to retain denials. Denials from the starting date to the present date will be merged into file \#162.

Do you wish to retain all Medical Denials? No// \<RET\>

Select date to retain denials: T-365

> Beginning merge...

> Deleting the Fee Basis Medical Denials file (#163)...

> Deleting the Fee Basis Pharmacy Denials file (#163.1)...

> Cleaning up DD nodes...

Completed FBPST35A 1/30/95@15:14:07 Beginning FBPST35B ....

> CONVERSION OF FEE BASIS FEE SCHEDULE FILE (#163.99)

Completed FBPST35B 1/30/95@15:14:16 Beginning FBPST35C

> REMOVAL OF FIELDS PREVIOUSLY STARRED FOR DELETION.

# ATTACHMENT B. FBINIT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

I will now remove the following fields that have been starred for deletion:

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 37%" />
<col style="width: 6%" />
<col style="width: 44%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th><blockquote>
<p>File</p>
</blockquote></th>
<th colspan="2">Field</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td><blockquote>
<p>----</p>
</blockquote></td>
<td>-----</td>
<td></td>
</tr>
<tr class="even">
<td>161</td>
<td>Fee Basis Patient</td>
<td>102</td>
<td>*AUSTIN DELETED</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>103</td>
<td>*DATE OF AUSTIN DELETE</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>104</td>
<td>*DATE TRANSMITTED TO AUSTIN</td>
</tr>
<tr class="odd">
<td>161.01</td>
<td>Fee Basis Patient</td>
<td><blockquote>
<p>4</p>
</blockquote></td>
<td>*CNH LEVEL OF CARE</td>
</tr>
<tr class="even">
<td>161.2</td>
<td>Fee Basis Vendor</td>
<td>16</td>
<td>*NUMBER OF SKILLED BEDS</td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td>17</td>
<td>*NUMBER OF INTERMEDIATE BEDS</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>21</td>
<td>*LEVELS OF CARE PROVIDED</td>
</tr>
<tr class="odd">
<td>161.4</td>
<td>Fee Basis Site Parameters</td>
<td>36</td>
<td>*LAST UC UPDATED</td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td>37</td>
<td>*DATE UC CONVERSION COMPLETED</td>
</tr>
</tbody>
</table>

Do you want me to task this job in the background for you? Yes// NO

| If you respond YES…                                                                                                      | If you respond NO…                                                                                                      |
|--------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|
| Routine FBPST35 to remove obsolete fields has been tasked.                                                               | Deleting any data remaining in the obsolete fields.                                                                     |
|                                                                                                                          | Deleting Field \# 4 from File \# 161.01.                                                                                |
| Please refer to Attachment D for a sample mail message that will be sent ONLY if you choose to task post- init FBPST35C. | Deleting Field \# 102 from File \# 161. Deleting Field \# 103 from File \# 161. Deleting Field \# 104 from File \# 161. |
|                                                                                                                          | Deleting Field \# 16 from File \# 161.2.                                                                                |
|                                                                                                                          | Deleting Field \# 17 from File \# 161.2.                                                                                |
|                                                                                                                          | Deleting Field \# 21 from File \# 161.2.                                                                                |
|                                                                                                                          | Deleting Field \# 36 from File \# 161.4.                                                                                |
|                                                                                                                          | Deleting Field \# 37 from File \# 161.4.                                                                                |
|                                                                                                                          | Completed FBPST35C                                                                                                      |

This version of 'FBONIT' was created on 30-JAN-1995

> (at ALBANY ISC VAX DEVELOPMENT, by OE/RR V.2.5)

> PROTOCOL INSTALLATION

...OK, this may take a while, hold on please...............

'FB BATCH STATUS' Protocol Filed 'FB CHANGE VENDOR' Protocol Filed 'FB CHANGE VETERAN' Protocol Filed 'FB CPT DESCRIPTION' Protocol Filed

'FB DISPLAY AUTHORIZATION' Protocol Filed

'FB DISPLAY CHECK' Protocol Filed 'FB DISPLAY VENDOR' Protocol Filed 'FB EXPAND VIEW' Protocol Filed

# ATTACHMENT B. FBINIT

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

'FB INVOICE DISPLAY' Protocol Filed 'FB LIST BATCH' Protocol Filed

'FB PHONE MENU' Protocol Filed

> FB LIST BATCH added as item to FB PHONE MENU.

> FB INVOICE DISPLAY added as item to FB PHONE MENU. FB BATCH STATUS added as item to FB PHONE MENU.

> FB DISPLAY VENDOR added as item to FB PHONE MENU.

> FB DISPLAY AUTHORIZATION added as item to FB PHONE MENU.

> FB EXPAND VIEW added as item to FB PHONE MENU.

> FB CHANGE VETERAN added as item to FB PHONE MENU. FB CHANGE VENDOR added as item to FB PHONE MENU. FB DISPLAY CHECK added as item to FB PHONE MENU. FB CPT DESCRIPTION added as item to FB PHONE MENU.

OK, Protocol Installation is Complete.

'FBPHONE MENU' List Template...Filed.

# \>

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# ATTACHMENT C. PAID SERVER

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# The following is a sample PAID Server mail message.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Subj: Server Request Notice \[#183837\] 27 May 94 11:15 20 Lines From: POSTMASTER Page 1

> May 26, 1994 2:50 PM

A request for execution of a server option has been received. Sender: <POSTMASTER@FOC-AUSTIN.VA.GOV>

Option name: FBAA PAID SERVER Subject: FPA/ \#941461343846831

Message \#: 183818

Comments: No errors detected by the Menu System.

> This is the server bulletin XQSERVER

> The 'AMOUNT PAID' has been altered on the Fee Payment Voucher Document in FMS for the following payments:

Check Number: 102 to SEAL POINT MEDICAL CNH for ABBOTT,JOHN A. - 8543

> From Date: 9/1/93 To Date: 9/5/93 Invoice Number: 1481

\>\>\> For detailed payment information use the appropriate payment output. \<\<\< Select MESSAGE Action: IGNORE (in IN basket)//

# ATTACHMENT D. FBPST35C POST-INIT MESSAGE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following message will be sent ONLY if you choose to task post-init FBPST35C.

Subj: FEE BASIS POST-INIT COMPLETE \[#118575\] 15 Aug 94 14:21 1 Line

From: POSTMASTER in 'IN' basket. Page 1 \*\*NEW\*\*

Post initialization routine FBPST35C has run to completion. Select MESSAGE Action: IGNORE (in IN basket)//

# ATTACHMENT E. FEE BASIS VENDOR CORRECTIONS CLEANUP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following message will be sent ONLY if you have invalid vendor IDs in the FEE BASIS VENDOR CORRECTION file (#161.25).

Subj: FEE BASIS VENDOR CORRECTIONS CLEANUP \[#188399\] 20 Sep 94 14:21 4 Lines

From: POSTMASTER in 'IN' basket. Page 1 \*\*NEW\*\*

The following vendors with invalid IDs have been placed in delete status: FULLER CLINIC 000000000

> GOODEN NURSING HOME INC 111

Select MESSAGE Action: IGNORE (in IN basket)//