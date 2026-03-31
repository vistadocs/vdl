---
title: NPM Release Notes Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: plain
doc_subject: NPM Release Notes
app_code: NPM
app_name: National Patch Module
section: INF
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 0
description: Patch ModuleRelease Notes&Installation GuideDecentralized Hospital Computer ProgramREDACTED Information Systems CenterTroy, New YorkDecember 1992PATCH MODULE RELEASE NOTES & INSTALLATION GUIDETABLEO FCONTENTS===================================================================
audience: 
keywords: 
  - patch
  - package
  - test
  - message
  - domain
  - patches
  - completed
  - personnel
  - date
  - unverified
page_count: 0
word_count: 2234
section_count: 0
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/National_Patch_Module_(NPM)/pmrnig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/National_Patch_Module_(NPM)/pmrnig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=20"
---

Patch ModuleRelease Notes&Installation GuideDecentralized Hospital Computer ProgramREDACTED Information Systems CenterTroy, New YorkDecember 1992PATCH MODULE RELEASE NOTES & INSTALLATION GUIDETABLEO FCONTENTS===================================================================

Enhancements and Changes (for Developers) 1

Enhancements and Changes (for Verifiers) 2

Enhancements and Changes (for IRM/Support Personnel) 3

Menu Diagram 4

Post Installation Setup Required for each Package (on FORUM) 7

Local ISC Development System Setup and Procedures 8

Procedure to Send a PackMan Message for Input to the Patch Module 9

Option Documentation 10

> Add a Patch 10

> Add Package to Patch Module 15

> Edit a Patch 17

> Summary Report of All Patches for a Package 21

> Verified Patch Summary Report by Date 22

> Verify a Patch (and or edit internal comments) 23

ENHANCEMENTS & CHANGES (for Developers)

Patch priority limited to either EMERGENCY or MANDATORY.

Patch category expanded to include enhancement, patch for a patch.

Network mail input of routines and/or text description for a patch.

A new DHCP message file \#11005.1 to hold routines and message data.

A new option, Create a PackMan Message, from the local FORUM directory.

Patch numbers are always incremented when adding a patch.

A flag when entering a routine name to warn that the routine has previous patches.

A new multiple field to list associated patches, when appropriate.

A flag to force sequential verification/release of associated patches.

A flag to hold verification/release until a certain date.

A field to enter routine checksum values.

A new option, Forward a Completed/Unverified Patch Message.

Network mail distribution of completed/unverified patch messages to verifiers.

The completed/unverified patch bulletin will show network recipients of the patch message, the FORUM patch message number, and the category - patch for a patch.

ENHANCEMENTS & CHANGES (for Verifiers)

A new option, Forward a Completed/Unverified Patch Message.

Network mail distribution of completed/unverified patch messages to verifiers.

The completed/unverified patch bulletin will show network recipients of the patch message, the FORUM patch message number, and the category - patch for a patch.

A new option, Completed Patch Summary for Assigned Packages. This report will include routines, associated patches, and hold date.

A flag to warn the routines in a patch have previous patches.

A flag to prevent verification/release by date.

A flag to force sequential verification/release of associated patches.

A sequential release number will be generated on verification and included in the patch message for patch management. The SEQ \# will appear in the verified patch message subject next to the patch designation.

> **NOTE:** The post-init of the package installation will generate SEQ \#s by date for all verified patches for the last two versions of each package in the system. SEQ \#s will also be generated for a package database version.

ENHANCEMENTS & CHANGES (for IRM/Support Personnel)

Network mail distribution of verified patch messages to G.SUPPORT@ISCS defined in the A1AE package of the Patch Module.

The verified patch bulletin will show network recipients of the patch message, the FORUM patch message number, and category - patch for a patch.

A sequential release number will be generated on verification and included in the patch message for patch management. The SEQ \# will appear in the verified patch message subject next to the patch designation.

> **NOTE:** The post-init of the package installation will generate SEQ \#s by date for all verified patches for the last two versions of each package in the system. SEQ \#s will also be generated for a package database version.

A new option, Forward a Verified Patch Message.

The option, Summary Report of All Patches for a Package, will include routines, associated patches, and hold date.

The option, Verified Patch Summary Report by Date, will include associated patch(s) and hold date.

MENU DIAGRAM

Patch User Menu (A1AE USER)

\|

\|--------------------------------------------------------- All Verified

Patches for a

Package

\[A1AE PRTPHA\]

---------------------------------------------------------- Detailed Report

of Verified

Patches by Date

\[A1AE PRTCOMDETDT\]

----- Developer's Menu \[AIAE ----------------------------- Add a Patch \[A1AE

DEVELOPER\] PHADD\]

\*\*LOCKED: A1AE DEVELOPER\*\*

\|

\|---------------------------------------------- Completed/Unveri-

\| fied Patch Report

\| \[A1AE PRTCOMPH\]

\|

\|---------------------------------------------- Copy a patch into a

\| new patch \[A1AE

\| COPY PATCH\]

\|

\|-----------------(NEW)------------------------ Create a packman

\| message \[A1AE

\| DEV CREATE\]

\|

\|---------------------------------------------- Delete an Unveri-

\| fied Patch

\| \[A1AE PHDEL\]

\|

\|---------------------------------------------- Display a Completed

\| /Unverified Patch

\| \[A1AE DISCOMPH\]

\|

\|---------------------------------------------- Edit a Patch

\| \[A1AE PHEDIT\]

\|

\|---------------------------------------------- Extended Display of

\| a Patch \[A1AE

\| PHEXTEND\]

\|

\|-----------------(NEW)------------------------ Forward a Completed

\| /Unverified Patch

\| Message \[A1AE

\| DEV FORWARD\]

MENU DIAGRAM

\|

\|----------- Package Management \[A1AE --------- Enter/Edit

\| PKGMGT\] Authorized Users

\| \| \[A1AE PKGEDIT\]

\| \|

\| \|----------------------------- Key Allocation for

\| \| Patch Functions

\| \| \[A1AE XUSEC\]

\| \| \*\*LOCKED: A1AE

\| \| XUSEC\*\*

\| \|

\| \|----------------------------- List of Package

\| Users \[A1AE

\| PKGLIST\]

\|

\|

\|---------------------------------------------- Under Development

Patch Report

\[A1AE PRTUDVPH\]

--------------------------------------------------------- Display a Patch

\[A1AE PRTPHD\]

--------------------------------------------------------- Display Number of

New Patches \[A1AE

PRTNEWPHNUM\]

----------------------------(NEW)------------------------ Forward a

Verified Patch

message \[A1AE

FORWARD\]

--------------------------------------------------------- New Patch Report

\[A1AE PRTNEWPH\]

----- Patch Module -------------------------------------- Add Package to

Management \[A1AE MGR\] Patch Module

\*\*LOCKED: A1AE MGR\*\* \[A1AE MGRADD\]

\|

\|---------------------------------------------- Key Allocation for

Patch Functions

\[A1AE XUSEC\]

\*\*LOCKED: A1AE

XUSEC\*\*

--------------------------------------------------------- Patch Options

Documentation

\[A1AE PATCHDOC\]

--------------------------------------------------------- Select Packages

for Notification

\[A1AE PKGSEL\]

MENU DIAGRAM

--------------------------------------------------------- Set All patches for

selected Packages

as Printed \[A1AE

PKGPRT\]

----------------------------(CHANGED)-------------------- Summary Report

of All Patches

for a Package

\[A1AE PRTPHS\]

----------------------------(CHANGED)-------------------- Verified Patch

Summary Report

by Date \[A1AE

PRTCOMSUMDT\]

----- Verifier Menu --------(NEW)------------------------ Completed Patch

\[A1AE VERIFIER\] Summary for

\*\*LOCKED: A1AE Assigned Packages

PHVER\*\* \[A1AE PRTCOMPHVER\]

\|

\|---------------------------------------------- Completed/Unveri-

\| fied Patch Report

\[A1AE PRTCOMPH\]

\|

\|---------------------------------------------- Display a Completed

\| /Unverified Patch

\| \[A1AE DISCOMPH\]

\|

\|---------------------------------------------- Forward a Completed

\| /Unverified Patch

\| Message \[A1AE

\| DEV FORWARD\]

\|

\|---------------------------------------------- Verify a Patch

\| (and/or edit

\| internal comments)

\| \[A1AE PHVER\]

\| \*\*LOCKED: A1AE

PHVER\*\*POST INSTALLATION SETUP REQUIRED FOR EACH PACKAGE (ON FORUM)

1\. Enable patch description copy question if you want it.

2\. Add domains for each package verifier.

3\. OPTIONAL - Setup test users if the Patch Module is to be used for a test site package.

> **NOTE:** A test site package does not require verification of patches.

Select Developers Menu Option: Package Management Option

select Package Management Option: Enter/Edit Authorized users

Select the Package: RT

USER SELECTION PERMITTED: no change

\* PERMIT DEVELOPER TO COMPLETE: no change

FOR TEST SITE ONLY?: no change

\(1\) Ask Patch Description Copy: NO// Say YES if you want the option to copy

the patch description from the input

PackMan text when editing a patch.

-----------------------------------------------------------------------------

Select SUPPORT PERSONNEL: HARVEY,JULIE//

SUPPORT PERSONNEL: HARVEY,JULIE//

VERIFY PERSONNEL: VERIFIER//

\(2\) VERIFIER'S DOMAIN: VER.ISC-REDACTED.VA.GOV// For each verifier, add a sub-

domain where completed/

unverified patch messages are

sent.

OPTIONAL

Select the Package: DVBZ

'This package is considered a TEST SITE PACKAGE in the Patch Module'

-----------------------------------------------------------------------------

\* PERMIT DEVELOPER TO COMPLETE: no change

FOR TEST SITE ONLY: YES// no change

ASK PATCH DESCRIPTION COPY: no change

-----------------------------------------------------------------------------

Select SELECTED USERS FOR PACKAGE: JONES,JOHN

SELECTED USERS FOR PACKAGE: JONES,JOHN

\(3\) TEST SITE DOMAIN: REDACTED.VA.GOV For each TEST SITE USER for the

package, enter the domain where a

message containing the completed/

unverified test version patch

should be sent.

LOCAL ISC DEVELOPMENT SYSTEM SETUP AND PROCEDURES

1\. In the Development System sub-domain, add a DOMAIN file entry "Q-Patch.va.gov" with

relay domain to the parent domain "ISC-XXXX".

2\. In the parent ISC-XXXX domain, add a DOMAIN file entry "Q-Patch.va.gov" with relay

domain FORUM.

domain: COR.ISC-REDACTED.VA.GOV

=====================

OUTPUT FROM WHAT FILE: DOMAIN//

Select DOMAIN NAME: Q-PATCH.VA.GOV

NAME: Q-PATCH.VA.GOV RELAY DOMAIN: ISC-REDACTED.VA.GOV

domain: ISC-REDACTED.VA.GOV

=================

Select DOMAIN NAME: Q-PATCH.VA.GOV

NAME: Q-PATCH.VA.GOV RELAY DOMAIN: FORUM

PROCEDURE TO SEND A PACKMAN MESSAGE FOR INPUT TO THE PATCH MODULE

1\. Create the PackMan message.

Subject : Namespace\*version\[\*patch number and text\]

Recipient: XXX@Q-PATCH.VA.GOV

or

Recipient: yourname@Q-PATCH.VA.GOV

2\. Include all routines to be included in the patch under development. The version line of the

routine(s) will be updated to the correct patch number by the patch system; however, any previous patches should be included in the input.

3\. Optional text can be included in the text portion of the message if you want to prepare patch text description locally and then just copy it at FORUM.

4\. THE SUBJECT NAMESPACE CONVENTION is critical. You will only be able to see and use messages with subject: "namespace\*version" when editing a patch. The Q-Patch will act as a package, version specific shared mail-box for the package developers in the patch system.

ADD A PATCH

This function permits authorized developers to add a new patch to a specific version of a package. Patches are unique by their designation and have the following format: package namespace\*

version number\*system assigned patch number. When the patch is added, the system assigns it a patch status of "'under development". A developer other than the one entering the patch must review the patch and change the status to "completed/unverified" using the Edit a Patch option.

> Select PACKAGE: RT RECORD TRACKING RT

> Select VERSION: 1// \<RET\> Date Verified: 04-14-92

> ARE YOU ADDING 'RT\*2\*3' AS A NEW DHCP PATCHES (THE 3RD)? yes

> DHCP PATCHES PATCH SUBJECT: wrap

> Patch Added: RT\*2\*3

> PATCH SUBJECT: wrap// \<RET\>

> PRIORITY: m MANDATORY

> HOLDING DATE: \<RET\>

> Select CATEGORY OF PATCH: r (ROUTINE)

> Select CATEGORY OF PATCH: \<RET\>

> The PATCH SUBJECT field has two cross-references that can be used for look-up; a regular cross-reference and key word in context cross reference. If you do not want this patch verified/installed until a certain date, enter that date at the HOLDING DATE prompt. The priorities are "E"mergency (must be installed within one working day of receipt) or "M"andatory (must be installed within five days of receipt). CATEGORY OF PATCH is a multiple field.

ADD A PATCH

> Do you want to copy lines from a message into the Patch

> Description? No// yes

> \(1\) RT\*2\*1 JONES,JENNY APR 14,1992

> \(2\) RT\*2\*TESTMESSAGE JONES,JENNY MAY 8, 1992

> Select Message to copy: 2// \<RET\>

> Copy from line: 1

> Copy through line: 1// 3

> 1\>If a user enters an '^' at the select patient prompt, an error

> 2\>\<UNDEF\> will occur. This patch will disable the use of '^' at

> 3\>this prompt.

> Do you want to copy this line? NO// yes

> PATCH DESCRIPTION:

> 1\>\$TXT Created by JONES,JENNY at ISC-REDACTED.VA.GOV on FRIDAY,

> 05/08/92 AT 13:47

> EDIT Option: \<RET\>

> The first prompt in the above screen will only appear if the ASK PATCH DESCRIPTION COPY parameter is set to YES for the selected package (through the Add Package to Patch Module option). The system will check messages in the queue with subject starting with "package namespace\*version" and will copy the selected lines of the text portion of the selected PackMan message. The option provides the ability to add/edit the patch description.

ADD A PATCH

> Select ROUTINE NAME: RTQ2

> editing DESCRIPTION OF ROUTINE CHANGES

> Copy routine lines from the routine directory into the description?

> No// \<RET\>

> Copy routine lines from a PackMan message into the description?

> No// yes

> Copy from line: XQ

> Copy through line: XQ// \<RET\>

> 1\> XQ K RTBLD,RTTYR,RTBKGRD,RTPAR,RTSD,RT,RTSEL,A,Z,L,L1,I,RTINST,

> RTDIV,RTPULL,RTPN,RTTY,RTTYP,RTAPL,RTQ,RTY,RTS,RTQDT,RTB,RTPLTY,

> RTE D CLOSE^RTUTL Q

> Do you want to copy this line? No// yes

> ..

> DESCRIPTION OF ROUTINE CHANGES:

> 1\> XQ K RTBLD,RTTYR,RTBKGRD,RTPAR,RTSD,RT,RTSEL,A,Z,L,L1,I,RTINST,

> RTDIV,RTPULL,RTPN,RTTY,RTTYP,RTAPL,RTQ,RTY,RTS,RTQDT,RTB,RTPLTY,

> RTE D CLOSE^RTUTL Q

> EDIT Option:

> ROUTINE CHECKSUM:

> 1\>5463243

> 2\>\<RET\>

> EDIT Option: \<RET\>

> Select ROUTINE NAME: \<RET\>

> If a programming change has been made to a routine, enter the name of the routine. Each routine in the patch must be entered as a separate entry in the routine multiple. THIS IS MANDATORY. If the routine can be found in the routine directory on FORUM, you will be prompted to copy routine lines into the routine description. Enter the line tag or line tag plus offset. You will usually copy the modified line out of the PackMan message into the routine description. At the ROUTINE CHECKSUM prompt, you should enter the value obtained from running CHECK^XTSUMBLD.

ADD A PATCH

> editing MESSAGE TEXT

> Do you want to copy 'RT\*2\*TESTMESSAGE' into the Message Text?

> No// yes

> Using message 'RT\*1' Checking the input .. Deleting old text ..

> Adding \<\<= NOT VERIFIED \> to the first line

> line (6) ;;v 1.0;Record Tracking;\*\*3\*\*;6/22/92

> MESSAGE TEXT:...

> 29\> G ^RTSM

> 30\> ;

> 31\>7 ;;Management Reports Menu

> 32\> G ^RTRPT

> 33\> ;

> 34\>8 ;;MAS Specific Setup Menu

> 35\> G ^RTMAS

> 36\> ;

> 37\>\$END ROU RT

> EDIT Option: \<RET\>

> You may choose to copy the routine portion of the PackMan message into your patch. If a PackMan message was selected previously, that message subject will be displayed in the first prompt shown on this screen; otherwise, you may select the PackMan message here. "NOT VERIFIED" is added to the first line of the routines and is subsequently removed when the patch is verified. When the routines are copied into the message text, the patch number is added to the version line of the routines. For routine patches, the input PackMan message must contain all the routines in the patch, and they must be copied into the message text. The message text becomes the installable PackMan routines portion of the released patch message.

ADD A PATCH

> editing comments only seen by verifiers/developers

> INTERNAL COMMENTS:

> 1\> Test verify

> 2\> \<RET\>

> EDIT Option: \<RET\>

> Select PATCH RELEASE CHECK: RT\*2\*1 WRAPAROUND UNDER DEVE PKE

> ARE YOU ADDING 'RT\*1\*1' AS A NEW PATCH RELEASE CHECK (THE 1ST FOR

> THIS DHCP PATCHES? y (YES)

> PATCH RELEASE CHECK REQUIRED FOR VERIFICATION: YES

> REQUIRED FOR VERIFICATION: YES// \<RET\>

> STATUS OF PATCH: UNDER DEVELOPMENT// \<RET\>

> The new INTERNAL COMMENTS field has been established as a means for the developer and verifier to exchange comments between themselves. If another patch must be verified/installed with this patch, enter that patch at the Select PATCH RELEASE CHECK prompt. If you use the routine name for lookup make sure the correct patch is selected as routines may appear in more than one patch. This is a multiple field and patches entered may be from the same package or different packages. Enter YES at the PATCH RELEASE CHECK REQUIRED FOR VERIFICATION prompt if the patch you entered in the PATCH RELEASE CHECK field must be verified/installed prior to verification/installation of the patch you are adding. Enter NO to allow concurrent verification/installation of the patches.

ADD PACKAGE TO PATCH MODULE

This option allows users to add packages to the DHCP PATCH/PROBLEM PACKAGE file (#11007). Only holders of security key A1AE MGR may access this option. The following is an explanation of most of the fields and how they should be answered when initially adding a package. An example of what may appear on the screen when utilizing the option appears on the next page.

DHCP PATCH/PROBLEM PACKAGE USER SELECTION PERMITTED

Set this parameter to NO.

USER SELECTION PERMITTED: NO//

Accept the default at this parameter until the package is added; then go back and enter YES. This will cause a mail bulletin to be sent on FORUM to three large mail groups informing them the package is now available in the Patch Module. Make sure the SHORT DESCRIPTION field in the PACKAGE file (#9.4) is filled in as text for the bulletin.

\*PERMIT DEVELOPER TO COMPLETE: YES//

Accept the default of YES at this prompt.

FOR TEST SITE ONLY: NO//

Enter NO if patches for this package are for all sites. Enter YES if they are for test sites only.

ASK PATCH DESCRIPTION COPY

If set to YES, user will be asked "Do you want to copy lines from a message into the Patch Description?" when adding or editing a patch.

Select SUPPORT PERSONNEL

Enter the verifiers assigned to this package. This is a multiple field.

VERIFY PERSONNEL

This field should always be set to V (Verifier) as the support personnel entered at the previous prompt should always be verifiers.

ADD PACKAGE TO PATCH MODULEVERIFIER'S DOMAIN

This field identifies the verifier's network mail domain for sending patch messages to the verifier.

The entry must contain a valid domain and have the format: \[subdomain.\]DOMAIN.

Select DEVELOPMENT PERSONNEL

Enter assigned developers for the selected package. This is a multiple field.

Development personnel may enter/edit authorized users in the DHCP AUTHORIZED USER file for those packages for which they are assigned developers.

Select PACKAGE: A1BN INCOME DATA COLLECTION

ARE YOU ADDING 'AIBN INCOME DATE COLLECTION' AS A NEW DHCP PATCH/PROBLEM

PACKAGE (THE 9TH)? YES

DHCP PATCH/PROBLEM PACKAGE USER SELECTION PERMITTED: NO

------------------------------------------------------------------------

USER SELECTION PERMITTED: NO// \<RET\>

\*PERMIT DEVELOPER TO COMPLETE: YES// \<RET\>

FOR TEST SITE ONLY?: NO// \<RET\>

ASK PATCH DESCRIPTION COPY: YES

------------------------------------------------------------------------

Select SUPPORT PERSONNEL: CHANDLER,DUSTY

VERIFY PERSONNEL: V VERIFIER

VERIFIER'S DOMAIN: VER.ISC-REDACTED

Select SUPPORT PERSONNEL: \<RET\>

------------------------------------------------------------------------

Select DEVELOPMENT PERSONNEL: HARRISON,PAUL

Select DEVELOPMENT PERSONNEL: BATES,NORMA

Select DEVELOPMENT PERSONNEL: \<RET\>

------------------------------------------------------------------------

EDIT A PATCH

This function permits authorized developers of a package to edit a patch. The option is also used by a developer other than the one who entered the patch to review the patch and change the status to "completed/unverified". When looking up a patch, the values for the following fields can be entered as the look-up value: patch designation, package, patch subject, routine name. There is also a key word in context cross-reference on the SUBJECT field that can be used. Which fields may be edited are dependent on the value of the STATUS field.

> Select PATCH: RT

> 1 RT\*2\*1 TEST WRAP COMPLETED/PKE

> 2 RT\*2\*2 TEST VERIFY UNDER DEVE PKE

> CHOOSE 1-2: 2

> Editing Patch: RT\*2\*2

> PATCH SUBJECT: TEST VERIFY// \<RET\>

> PRIORITY: MANDATORY// \<RET\>

> HOLDING DATE: \<RET\>

> Select CATEGORY OF PATCH: ROUTINE// \<RET\>

> The priorities are "E"mergency (must be installed within one working day of receipt) or "M"andatory (must be installed within five days of receipt). CATEGORY OF PATCH is a multiple field. If you do not want this patch verified/installed until a certain date, enter that date at the HOLDING DATE prompt. The holding date can be changed to a future date but not a past date. For patches with a "completed" status, you may change the patch subject and holding date without having the patch status revert to "under development".

> Do you want to copy lines from a message into the Patch

> Description? No// \<RET\>

> PATCH DESCRIPTION:

> 1\>\$TXT Created by JONES,JENNY at ISC-REDACTED.VA.GOV on FRIDAY,

> 05/08/92 AT 13:47

> EDIT Option: \<RET\>

> The first prompt in the above screen will only appear if the ASK PATCH DESCRIPTION COPY parameter is set to YES for the selected package (through the Add Package to Patch Module option). The system will check messages in the queue with subject starting with "package namespace\*version" and will copy the selected lines of the text portion of the selected PackMan message. The option provides the ability to add/edit the patch description.

EDIT A PATCH

> Select ROUTINE NAME: RT// \<RET\>

> ROUTINE NAME: RT// \<RET\>

> editing DESCRIPTION OF ROUTINE CHANGES

> Copy routine lines from the routine directory into the description?

> No// \<RET\>

> Copy routine lines from a PackMan message into the description?

> No// \<RET\>

> DESCRIPTION OF ROUTINE CHANGES:

> 1\>new line looks like:

> 2\> XQ K RTBLD,RTTYR,RTBKGRD,RTPAR,RTSD,RT,RTSEL,A,Z,L,L1,I,RTINST,

> EDIT Option: \<RET\>

> ROUTINE CHECKSUM:

> 1\>5463243

> EDIT Option: \<RET\>

> Select ROUTINE NAME: \<RET\>

> If a programming change has been made to a routine, enter the name of the routine. Each routine in the patch must be entered as a separate entry in the routine multiple. THIS IS MANDATORY. If the routine can be found in the routine directory on FORUM, you will be prompted to copy routine lines into the routine description. Enter the line tag or line tag plus offset. You may also copy the modified line out of the PackMan message into the routine description. At the ROUTINE CHECKSUM prompt, you should enter the value obtained from running CHECK^XTSUMBLD.

EDIT A PATCH

> editing MESSAGE TEXT

> Do you want to copy a PackMan message into the Message Text? No//

> \<RET\>

> MESSAGE TEXT:...

> 29\> G ^RTSM

> 30\> ;

> 31\>7 ;;Management Reports Menu

> 32\> G ^RTRPT

> 33\> ;

> 34\>8 ;;MAS Specific Setup Menu

> 35\> G ^RTMAS

> 36\> ;

> 37\>\$END ROU RT

> EDIT Option: \<RET\>

> You may choose to copy the routine portion of the PackMan message into your patch. If a PackMan message was selected previously, that message subject will be displayed in the first prompt shown on this screen; otherwise, you may select the PackMan message here. If you choose to copy, "NOT VERIFIED" is added to the first line of the routines and is subsequently removed when the patch is verified. When the routines are copied into the message text, the patch number is added to the version line of the routines. The message text should not have to be edited. Any edits must be done very carefully or the resulting PackMan routine may not install correctly.

EDIT A PATCH

> editing comments only seen by verifiers/developers...

> INTERNAL COMMENTS:

> 1\> Test verify

> EDIT Option: \<RET\>

> Select PATCH RELEASE CHECK: RT\*2\*1// \<RET\>

> PATCH RELEASE CHECK: RT\*2\*1// \<RET\>

> REQUIRED FOR VERIFICATION: NO// \<RET\>

> Select PATCH RELEASE CHECK: \<RET\>

> STATUS OF PATCH: UNDER DEVELOPMENT// c COMPLETED/UNVERIFIED

> Are you sure you want to change status to 'Complete/not verified'?

> No// yes

> ...status changed to 'Completed/not verified'

> . .... .

> NOTE: A message has been sent to the verifiers of this package.

> Note: A bulletin has been sent to the verifiers of this package

> informing them of this 'Completed/not verified' patch.

> The new INTERNAL COMMENTS field has been established as a means for the developer and verifier to exchange comments between themselves. If another patch must be verified/installed with this patch, enter that patch at the Select PATCH RELEASE CHECK prompt. If you use the routine name for lookup make sure the correct patch is selected as routines may appear in more than one patch. This is a multiple field and patches entered may be from the same package or different packages. Enter YES at the REQUIRED FOR VERIFICATION prompt if the patch entered in the PATCH RELEASE CHECK field must be verified/installed prior to verification/installation of the patch you are editing. Enter NO to allow concurrent verification/installation of the patches.

> When the patch status is changed to "completed/unverified", a patch message is sent to the verifiers of the package at the network address defined in the package VERIFIER'S DOMAIN field. A bulletin is also sent to the package verifiers at FORUM.

SUMMARY REPORT OF ALL PATCHES FOR A PACKAGE

> Select PACKAGE: RT RECORD TRACKING RT

> Select VERSION: 1// \<RET\> Date Verified: 03-25-89

> Sort by reverse SEQ \# ? No// \<RET\>

Patch Summary Report NOV 10,1992 15:20 PAGE 1

Designation

SEQ Subject Status Routine

--------------------------------------------------------------------

RT\*1\*1 1 TEST 10 V 05/20/90

RT\*1\*2 2 Disable LAYGO for Sc V 05/07/90 RTQ2

RT\*1\*5 3 TEST COPY V 09/22/92 RT

RTQ

Hold date 10/19/92

Associated patches: (v)A1AE\*1\*6 install with patch \`RT\*1\*17'

(c)DVB\*11\*3 install with patch \`RT\*1\*17'

(v)RA\*1.1 \<\<= must be installed BEFORE \`RT\*1\*17'

-----------------------------------------------------------------------------RT\*1\*4 4 TEST 11 V 05/21/90 RT

-----------------------------------------------------------------------------RT\*1\*3 5 TEST 14 RTTEST V 05/22/90 RTSM6

-----------------------------------------------------------------------------RT\*1\*6 6 TEST 12 V 05/21/90 RT

-----------------------------------------------------------------------------RT\*1\*7 7 TEST BULLETIN V 10/26/92 RT

RTQ2

Hold date 10/26/92

----------------------------------------------------------------------------

RT\*1\*10 TEST DESCRIPTION INP U 06/13/91

-----------------------------------------------------------------------------RT\*1\*11 TEST DES COPY U 06/13/91 RT

RTQ

------------------------------------------------------------------------------RT\*1\*12 TEST DES1 C 09/15/92

-----------------------------------------------------------------------------RT\*DBA\*13 TST SUMMARY C 09/14/92

-----------------------------------------------------------------------------RT\*1\*14 TEST COPY/PATCH CHEC C 10/19/92 RT

RTQ

RTQ2

Hold date 10/19/92

Associated patches: (v)A1AE\*1\*6 install with patch \`RT\*1\*34'

(c)DVB\*11\*3 \<\<= must be installed BEFORE \`RT\*1\*34'

-----------------------------------------------------------------------------

VERIFIED PATCH SUMMARY REPORT BY DATE

> Do you want to Print Patches for a Specific Package? No// Y

> Select PACKAGE: RT RECORD TRACKING RT

> \*\*\*\* Date Range of Verified Patches \*\*\*\*

> Beginning DATE: T-999 (FEB 15, 1990)

> Ending DATE: T (NOV 10, 1992)

> DEVICE: HOME// \<RET\> Decnet RIGHT MARGIN: 80// \<RET\>

Patch SEQ \# Patch Subject Date Priority

Designation Verified

-----------------------------------------------------------------------------

RT\*1.26\*17 14 TEST COPY SEP 22, 1992 MANDATORY

Hold date: OCT 19, 1992

Associated patches: (v)A1AE\*1\*6 install with patch

(u)RA\*2.08\*5 \<\<= must be installed BEFORE

RT\*1\*4 13 TEST DEMO COPY SEP 16, 1992 EMERGENCY

RT\*1\*18 12 TEST : SEP 15, 1992 EMERGENCY

RT\*1\*3 11 DEMO PATCH JUN 12, 1991 MANDATORY

Associated patches: (v)RT\*1.25\*3 \<\<= must be installed BEFORE

RT\*1\*19 9 TST MAR 19, 1991 MANDATORY

RT\*1\*20 8 TEST20 NEW MAIL,PRINT MAR 19, 1991 MANDATORY

RT\*1\*14 7 TEST 14 RTTEST MAY 22, 1990 MANDATORY

RT\*1\*11 6 TEST 11 MAY 21, 1990 MANDATORY

RT\*1\*12 5 TEST 12 MAY 21, 1990 MANDATORY

RT\*1\*13 4 TEST 13 MAY 21, 1990 MANDATORY

RT\*1\*10 3 TEST 10 MAY 20, 1990 MANDATORY

RT\*1\*8 2 TEST 8 MAY 17, 1990 MANDATORY

RT\*1\*2 1 Disable LAYGO for Schedu MAY 7, 1990 MANDATORY

VERIFY A PATCH (and or edit internal comments)

The Verify a Patch option can be used by authorized verifiers of a package to change the status of a patch from "completed/unverified" to "verified". Once the status has been changed, a patch message is sent to G.SUPPORT at the ISCs for distribution, a bulletin is sent to user(s) who have requested notification of patches for the package, and the patch becomes available to all patch users. The option can also be used to add/edit the INTERNAL COMMENTS field. Only holders of the A1AE PHVER security key may access this option.

> Select PATCH: RT\*1\*3 TEST WRAP COMPLETED/ PKE

> Do not release/verify until: NOV 6, 1992

> Internal Comments to developers/verifiers for: RT\*1\*3

> INTERNAL COMMENTS:

> 1\>TEST INTERNAL WRAP

> EDIT Option: \<RET\>

> Continue and Display Patch? No// YES

> 'RTQ2' routine has previous Patches: (c)RT\*1\*1

> DEVICE: HOME// \<RET\> LAT

> The "Do not release/verify" message appears if there is a holding date for the selected patch.

> If the routine(s) associated with this patch has had previous version-specific patches, they will be displayed. The letter in the parentheses indicates the status of that patch (i.e., (c) above).

VERIFY A PATCH (and or edit internal comments)

> DHCP Completed/not verified Patch Display Page: 1

> =====================================================================

> Run Date: OCT 26, 1992 Designation: RT\*1\*3

> Package : RT - RECORD TRACKING Priority : MANDATORY

> Version : 1 Status : COMPLETED/UNVERIFIED

> ======================================================================

> Associated patches: (c)RT\*1\*4 install with patch \`RT\*1\*2'

> (c)RA\*1.08\*5 \<\<= must be installed BEFORE \`RT\*1\*2'

> Subject: TEST WRAP

> Category: ROUTINE

> Description:

> ===========

> Any associated patches are listed, indicating that concurrent or sequential release/verification is required.

> DHCP Completed/not verified Patch Display Page: 2

> =====================================================================

> Run Date: OCT 26, 1992 Designation: RT\*1\*3

> Package : RT - RECORD TRACKING Priority : MANDATORY

> Version : 2 Status : COMPLETED/UNVERIFIED

> =====================================================================

> Routine Information:

> ====================

> old line looks like:

> Routine Name: RTQ2

> Description of Changes:

> Routine Checksum: 4599234

VERIFY A PATCH (and or edit internal comments)

> User Information: Hold Date : OCT 22,1992

> Entered By : EKLUND,PETER Date Entered : APR 14,1992

> Completed By: URBANSKI,JOSEPH L. Date Completed: SEP 16,1992

> Verified By : Date Verified :

> =====================================================================

> Verifying Patch: RT\*1\*3

> STATUS OF PATCH: COMPLETED/UNVERIFIED// VERIFIED

> Are you sure you want to change status to 'Verified'? No// YES

> ...status changed to 'Verified'

> Removing \<\<= NOT VERIFIED \> from the first line

> . ... .

> NOTE: A message has been sent to the Network Mail groups for

> distribution.

> NOTE: A bulletin has been sent to the select users of this package

> informing them of this 'Verified' patch.