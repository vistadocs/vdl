---
title: Automatic Replenishment/Ward Stock Version 2.3 Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: 
app_code: AR/WS
app_name: "Pharmacy: Automatic Replenish / Ward Stock"
section: CLI
app_status: active
pkg_ns: AR/WS
patch_ver: 2.3
patch_id: AR/WS*2.3
group_key: "AR/WS:AR/WS:2.3"
file_numbers: []
security_keys: []
menu_options: 0
description: "The AR/WS module relies on, at least, the following external packages to run effectively:"
audience: 
keywords: 
  - psgw
  - filed
  - print
  - shall
  - write
  - over
  - existing
  - stock
  - inventory
  - amis
page_count: 0
word_count: 1355
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
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Auto_Repl_Ward_Stock_(ARWS)/wsinstall.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Auto_Repl_Ward_Stock_(ARWS)/wsinstall.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=83"
---

Installation

This guide explains how to install Version 2.3 of the Automatic Replenishment/

Ward Stock (AR/WS) module of the Inpatient Pharmacy package.

The AR/WS module relies on, at least, the following external packages to run effectively:

> <u>Package</u> <u>Minimum Version Needed</u>

> Kernel 7.0

> VA FileMan 19.0

> MailMan 7.0

> MAS 5.2

> Outpatient Pharmacy 5.6

> AR/WS 2.04\*\*Note: Version 2.3 may be installed in an account that did not previously have any versions of AR/WS loaded. If, however, there are previous versions that are before V. 2.04, it will be necessary to load V. 2.04 first.

> \(1\) Load the AR/WS routines, PSGW\* into a test account. To run this module, the NEW PERSON file (#200), WARD LOCATION (#42), HOSPITAL LOCATION (#44), SPECIALTY (#42.4), DRUG (#50), and ORDER UNIT (#51.5) files are needed. The system does not need to be taken down, but the AR/WS menus *must* be disabled during installation.

Initializing AR/WS Version 2.3

> Version 2.3 Automatic Replenishment/Ward Stock inits were created with VA FileMan Version 19.0. The inits do not contain any data, as the data is created by each individual VAMC.

> With respect to the options, templates, and security keys, the inits send those which are specifically needed by the module. Answer “YES” to allow these entries to overwrite the existing entries.

> A pre-init routine (^PSGWPRE1) is called at the beginning of the init process. If a version of AR/WS prior to V. 2.04 is currently operational then this installation will be aborted and a message will be printed stating that it will be necessary to obtain a copy of the tape and installation notes for V. 2.04 and install it before installing V. 2.3. If this is the first version of AR/WS to be loaded, then nothing will happen during the pre-init and the normal init process will continue. If, however, AR/WS V. 2.04 is currently operational the RETURN REASON subfield in the PHARMACY AOU STOCK file (#58.1) will be deleted. This field will be restored by the inits as a multiple field.

> One routine is called near the end of the init process. First, the ^PSGWPOST routine will transfer the old RETURN REASON data to the new location created by the data dictionary change. Second, it will re-index the IU cross-reference in the DRUG file (#50). This cross-reference is used by the nightly job PSGW UPDATE AMIS STATS to identify non-pharmacy items in AOUs. Lastly, the sort keys assigned to AOUs in the AOU INVENTORY GROUP file (#58.2) will be re-initialized. This is done because some sites have rearranged their inventory groups so many times that the sort keys have become too large for the input transform on the field to accept.

> Now you are ready to continue the installation of this package. In programmer mode, please be sure that the variable DUZ is set to a valid user number and that DUZ(0) is set to “@”.

> \(2\) Install the AR/WS module by entering the command D ^PSGWINIT while logged on in the test account in programmer mode. The init process should take approximately 45-60 minutes to run.

> \(3\) Enter AR/WS users into the system. All pharmacy personnel may be assigned *PSGWMGR* as the primary menu option. If Pharmacy wishes to give the *Auto Replenishment/Ward Stock Nurses’ Menu* to Nursing, then nursing personnel may be assigned the *PSGW RN* menu option. Read “On-Demand Requests” in the AR/WS User Manual before assigning this menu, as some coordination between services is required.

> Some stations design their own menus for individual users. If this is the case, then the top level AR/WS menu (and only the top level menu) should contain the following enter and exit code in the OPTION file to ensure that users are prompted only *once* for an Inpatient Site:

> EXIT ACTION : K PSGWSITE

> ACTION : I '\$D(PSGWSITE) D ^PSGWSET

> This enter and exit code must be present because the PSGWSITE variable is set as users enter the package. If the Kernel’s ^OPTION NAME feature is used to jump directly into lower levels of the AR/WS package, then the “Inpatient Site Name” prompt *must* be answered in order to define the PSGWSITE variable. All options are able to be independently implemented, however, if the instructions above are not followed, users will be repeatedly asked to select an Inpatient Site if there are two or more sites that are flagged for AR/WS use.

> \(4\) Key allocation. There are four keys associated with AR/WS:

> • The PSGWMGR key must be given to the Inpatient Pharmacy Package Coordinator and other users who are allowed to edit AR/WS files and run the AMIS report.

> • The PSGW PURGE key should be given only to the Inpatient Pharmacy Package Coordinator or his/her designee. This lock controls the deletion of data from the AR/WS files and should be assigned with discretion!

> • The PSGW PARAM key should be given only to the Inpatient Pharmacy Package Coordinator. This lock controls when the collection of AMIS data begins.

> • The PSGW TRAN key should be given only to the Inpatient Pharmacy Package Coordinator or his/her designee. This key controls access to the *Transfer AOU StockEntries* option. Using the transfer option, users may copy the stock entries from one Area of Use into other Areas of Use.

At this point, proceed as follows:

> • AR/WS V. 2.04 is currently operational - skip to step 11.

> • AR/WS is being loaded for the first time - go on to step 5 then continue thru step 11.

> • If any version prior to V. 2.04 is currently operational, it will be necessary to obtain a tape and copy of the installation notes for V. 2.04 and load it before proceeding with the installation of V. 2.3.

> \(5\) It is necessary at this point for the Inpatient Pharmacy Package Coordinator to edit the Site Parameters. On the *Supervisor’s Menu*, go to the *Set Up AR/WS (Build Files)* option. For all Inpatient Site names in the file, answer the question “IS SITE SELECTABLE FOR AR/WS?”. Edit only this parameter at this time. *Do not* set the “BEGIN COLLECTING AMIS DATA NOW?” site parameter to “YES” until the *Prepare AMIS Data* options are completed, reviewed, and correct.

> On the *Supervisor’s Menu*, use the *Set Up AR/WS (Build Files)* options to enter data into the AR/WS files:

> a\) *Enter/Edit Inventory Types*

> b\) *Item Location Codes - Enter/Edit*

> c\) *Create the Area of Use*

> d\) *Stock Items - Enter/Edit*

> e\) *Expiration Date - Enter/Edit*

> f\) *Add/Delete Ward (for Item)*

> g\) *Transfer AOU Stock Entries*

> h\) *AOU Inventory Group - Enter/Edit*

> i\) *Site Parameters* \*\*Note:*Do not* turn on the “BEGIN COLLECTING AMIS DATA NOW?” site parameter until the *Prepare AMIS Data* options are completed, reviewed, and correct. (See step 7 which follows.)

> \(6\) On the *Supervisor’s Menu*, use all of the *Prepare AMIS Data* options to prepare the data base for the collection of AMIS data.

> a\) *Print AMIS Worksheet*

> b\) *Enter AMIS Data for All Drugs/All AOUs*

> c\) *Data for AMIS Stats - Print*

> d\) *AMIS Data Enter/Edit (Single Drug)*

> e\) *Identify AOU Returns & AMIS Count*

> f\) *Identify AOU INPATIENT SITE*

> g\) *Show AOU Status for AMIS*

> \(7\) Carefully examine the reports produced by the *Data for AMIS Stats - Print* option and the *Show AOU Status for AMIS* option. When you are sure that the data is accurate, return to the *Site Parameters* option on the *Set Up AR/WS (Build Files)* menu. Set the “BEGIN COLLECTING AMIS DATA NOW?” site parameter to “YES”. This must be done for every Inpatient Site Name which has the “IS SITE SELECTABLE FOR AR/WS?” parameter answered “YES”. Once this flag is set to “YES”, you should under *no circumstances* flip the setting back and forth. The setting of this parameter directly affects the accuracy of the AMIS report. You are now accumulating AMIS data as regular inventories are done.

> \(8\) Before purging the system of any old data, you may wish to print reports for the previous quarter, month, year, etc. Many reports will allow you to get printouts on existing data. Use the *Auto Replenishment Reports* options on the *Production Menu* and the *Management Reports* options on the *Supervisor’s Menu* for this purpose.

> \(9\) After paper copies are made of all desired reports, you may wish to delete some data from the files. It is a site specific decision as to how much old data should be retained. Use the *Obsolete Data Purge* options on the *Supervisor’s Menu* for this purpose.

\(10\) There are two background TaskMan jobs that should be scheduled to run nightly. Please bring this to the attention of your IRM service or ADP department.

> • The *PSGW PURGE INVENTORY* option deletes inventory sheets that are over 100 days old, so that you may no longer edit this data. This option *does not* delete data from the INVENTORY file.

> • The *PSGW UPDATE AMIS STATS* option moves data accumulated from daily inventory activity into the AR/WS STATS file (#58.5). Unless this data is transferred into the STATS file, the AMIS report will not be accurate.

> Using the TaskMan Manager’s *Schedule/Unschedule Options* option, select each of these two options. At the “QUEUED TO RUN AT WHAT TIME:” prompt, enter “T@” followed by the time you want the job to begin. The time should be one that does not conflict with system backup. At the “RESCHEDULING FREQUENCY:” prompt, enter “1D”. The “DEVICE” prompt should remain blank as these are both background jobs.

\(11\) There are two Data Dictionary nodes which may be left from previous versions of AR/WS. These nodes are the following:

1\. ^DD(58.15,0,"NM","RETURNED ITEMS")=""

2\. ^DD(58.26,0,"NM","WARD(FOR ITEM)")=""

> To remove these nodes, please run the *CHECK/FIX DD STRUCTURE* option under the *DATA DICTIONARY UTILITIES* option of VA FileMan V. 19.0. Start and end with PHARMACY AOU STOCK file (#58.1) and answer “YES” to the prompt “Remove erroneous nodes?”.

The INIT process follows:

\><u>D ^PSGWINIT</u>

This version (#2.3T3) of 'PSGWINIT' was created on 17-AUG-1993

(at BIRMINGHAM ISC - 10, by VA FileMan V.19.0)

I HAVE TO RUN AN ENVIRONMENT CHECK ROUTINE.

Beginning pre-init...

Initialization process started AUG 18,1993@10:44:43.

Deleting RETURN REASON subfield in Pharmacy AOU Stock file (#58.1)...

(This field will be restored by inits as a multiple field)

Pre-initialization is now complete!

I AM GOING TO SET UP THE FOLLOWING FILES:

50 DRUG (Partial Definition)

> **NOTE:** You already have the 'DRUG' File.

Shall I write over the existing Data Definition? YES// <u>\<RET\></u>

58.1 PHARMACY AOU STOCK

> **NOTE:** You already have the 'PHARMACY AOU STOCK' File.

Shall I write over the existing Data Definition? YES// <u>\<RET\></u>

58.16 AOU INVENTORY TYPE

> **NOTE:** You already have the 'AOU INVENTORY TYPE' File.

Shall I write over the existing Data Definition? YES// <u>\<RET\></u>

58.17 AOU ITEM LOCATION

> **NOTE:** You already have the 'AOU ITEM LOCATION' File.

Shall I write over the existing Data Definition? YES// <u>\<RET\></u>

58.19 PHARMACY AOU INVENTORY

> **NOTE:** You already have the 'PHARMACY AOU INVENTORY' File.

Shall I write over the existing Data Definition? YES// <u>\<RET\></u>

58.2 AOU INVENTORY GROUP

> **NOTE:** You already have the 'AOU INVENTORY GROUP' File.

Shall I write over the existing Data Definition? YES// <u>\<RET\></u>

58.3 PHARMACY BACKORDER

> **NOTE:** You already have the 'PHARMACY BACKORDER' File.

Shall I write over the existing Data Definition? YES// <u>\<RET\></u>

58.5 AR/WS STATS FILE

> **NOTE:** You already have the 'AR/WS STATS FILE' File.

Shall I write over the existing Data Definition? YES// <u>\<RET\></u>

59.4 INPATIENT SITE (Partial Definition)

> **NOTE:** You already have the 'INPATIENT SITE' File.

Shall I write over the existing Data Definition? YES// <u>\<RET\></u>

59.7 PHARMACY SYSTEM

> **NOTE:** You already have the 'PHARMACY SYSTEM' File.

Shall I write over the existing Data Definition? YES// <u>\<RET\></u>

SHALL I WRITE OVER FILE SECURITY CODES? NO// <u>\<RET\></u> (NO)

> **NOTE:** This package also contains SORT TEMPLATES

SHALL I WRITE OVER EXISTING SORT TEMPLATES OF THE SAME NAME? YES// <u>\<RET\></u> (YES)

> **NOTE:** This package also contains INPUT TEMPLATES

SHALL I WRITE OVER EXISTING INPUT TEMPLATES OF THE SAME NAME? YES//<u>\<RET\></u> (YES)

> **NOTE:** This package also contains PRINT TEMPLATES

SHALL I WRITE OVER EXISTING PRINT TEMPLATES OF THE SAME NAME? YES// <u>\<RET\></u> (YES)

> **NOTE:** This package also contains FUNCTIONS

SHALL I WRITE OVER EXISTING FUNCTIONS OF THE SAME NAME? YES// <u>\<RET\></u> (YES)

> **NOTE:** This package also contains SECURITY KEYS

SHALL I WRITE OVER EXISTING SECURITY KEYS OF THE SAME NAME? YES// <u>\<RET\></u> (YES)

> **NOTE:** This package also contains OPTIONS

SHALL I WRITE OVER EXISTING OPTIONS OF THE SAME NAME? YES// <u>\<RET\></u> (YES)

ARE YOU SURE EVERYTHING'S OK? NO// <u>Y</u> (YES)

...HMMM, JUST A MOMENT PLEASE...................................................

...............................................................................................................

'PSGW ADD/DEL WARD' Option Filed

'PSGW AMIS' Option Filed

'PSGW AOU INACTIVATION' Option Filed

'PSGW AOU INV GROUP EDIT' Option Filed

'PSGW AOU INV GROUP PRINT' Option Filed

'PSGW AOU INV GROUP SORT' Option Filed

'PSGW AOU INVENTORY INPUT' Option Filed

'PSGW AOU RET/AMIS CT PRINT' Option Filed

'PSGW AOU RETURNS & AMIS COUNT' Option Filed

'PSGW AREA OF USE EDIT' Option Filed

'PSGW BACKORDER' Option Filed

'PSGW BACKORDER (ALL) PRINT' Option Filed

'PSGW BACKORDER AOU PRINT' Option Filed

'PSGW BACKORDER EDIT' Option Filed

'PSGW BACKORDER IN' Option Filed

'PSGW BACKORDER ITEM PRINT' Option Filed

'PSGW BACKORDER ITEMS PRINT' Option Filed

'PSGW CLEAR AMIS EXCEPTIONS' Option Filed

'PSGW COST PER AOU' Option Filed

'PSGW CRASH CART LOCATION EDIT' Option Filed

'PSGW CRASH CART LOCATION PRINT' Option Filed

'PSGW CRASH CART MENU' Option Filed

'PSGW DELETE INVENTORY' Option Filed

'PSGW DUPLICATE REPORT' Option Filed

'PSGW EDIT AOU STOCK' Option Filed

'PSGW EDIT INVENTORY USER' Option Filed

'PSGW ENTER AMIS DATA/ALL DRUGS' Option Filed

'PSGW ENTER/EDIT AMIS DATA' Option Filed

'PSGW EXP REPORT' Option Filed

'PSGW EXPIRATION ENTER/EDIT' Option Filed

'PSGW HIGH COST' Option Filed

'PSGW HIGH VOLUME' Option Filed

'PSGW INACTIVATE AOU STOCK ITEM' Option Filed

'PSGW INPUT AOU INP SITE' Option Filed

'PSGW INV TYPE' Option Filed

'PSGW INV TYPE EDIT' Option Filed

'PSGW INVENTORY DISPENSE' Option Filed

'PSGW INVENTORY PICK LIST' Option Filed

'PSGW INVENTORY SHEET' Option Filed

'PSGW INVENTORY SINGLE' Option Filed

'PSGW ITEM INQUIRY' Option Filed

'PSGW ITEM LOC EDIT' Option Filed

'PSGW ITEM LOC PRINT' Option Filed

'PSGW LOOKUP ITEM' Option Filed

'PSGW MGT REPORTS' Option Filed

'PSGW ON-DEMAND' Option Filed

'PSGW ON-DEMAND DELETE' Option Filed

'PSGW ON-DEMAND EDIT' Option Filed

'PSGW ON-DEMAND NURSING EDIT' Option Filed

'PSGW ON-DEMAND PRINT' Option Filed

'PSGW PREPARE AMIS DATA' Option Filed

'PSGW PRINT AMIS REPORT' Option Filed

'PSGW PRINT AMIS WORKSHEET' Option Filed

'PSGW PRINT AOU STOCK' Option Filed

'PSGW PRINT DATA FOR AMIS STATS' Option Filed

'PSGW PRINT SETUP LISTS' Option Filed

'PSGW PURGE' Option Filed

'PSGW PURGE AMIS' Option Filed

'PSGW PURGE FILES' Option Filed

'PSGW PURGE INVENTORY' Option Filed

'PSGW RE-INDEX AMIS' Option Filed

'PSGW RECALCULATE AMIS' Option Filed

'PSGW REPORTS' Option Filed

'PSGW RETURN ITEMS' Option Filed

'PSGW RETURNS BREAKDOWN' Option Filed

'PSGW RN' Option Filed

'PSGW SETUP' Option Filed

'PSGW SHOW AREA OF USE' Option Filed

'PSGW SINGLE ITEM COST' Option Filed

'PSGW SITE' Option Filed

'PSGW STANDARD COST REPORT' Option Filed

'PSGW STOCK ITEM DATA' Option Filed

'PSGW STOCK PERCENTAGE' Option Filed

'PSGW TRANSFER ENTRIES' Option Filed

'PSGW UPDATE AMIS STATS' Option Filed

'PSGW USAGE REPORT' Option Filed

'PSGW WARD CONVERSION' Option Filed

'PSGW WARD INV PRINT' Option Filed

'PSGW WARD STOCK' Option Filed

'PSGW WARD STOCK MAINT' Option Filed

'PSGW ZERO USAGE' Option Filed

'PSGWMGR' Option Filed.................

NO SECURITY-CODE PROTECTION HAS BEEN MADE

Beginning post-init...

Post-init conversion of RETURN REASON subfield has already been done!

Now re-indexing the "IU" cross-reference in the Drug file (#50)........

Now re-initializing sort keys for AOUs in AOU Inventory Group file (#58.2)...

*\[At this point, the post-init checks for Duplicate Entries in the ITEM subfile (#58.11) of the PHARMACY AOU STOCK file (#58.1). If duplicate entries are found, the message following this installation example is sent to the installer and the PSGWMGR key holders.\]*

Now checking for duplicate entries in the ITEM subfile of the Pharmacy

AOU Stock file.

Duplicate entries exist.

A MailMan message is being sent to you regarding the problem.

Now reindexing the "WS" cross-reference on the AREA OF USE (AOU) field of the

AREA OF USE (AOU) subfile of the AOU INVENTORY GROUP file.

Post-init completed AUG 18,1993@10:46:35.

AR/WS Version 2.3 has been successfully installed!

Initialization process took 20 minutes.

MailMan 7.0 service for INSTALLER,JOHN Q. at ISC-BIRM.VA.GOV

You last used MailMan: 18 AUG 93 09:32

You have 1 new message.

Select MailMan Option: <u>NEW</u> MAIL AND RESPONSES

Subj: Duplicate entries in ITEM subfile. \[#564\] 18 AUG 93 11:04:43 20 Lines

From: INPATIENT PHARMACY AR/WS in 'IN' basket. Page 1 \*\*NEW\*\*

------------------------------------------------------------------------------

Duplicate entries exist in the ITEM subfile (#58.11) of the PHARMACY AOU

STOCK file (#58.1). Please execute the following procedures to clean the

subfile:

1\. Run the option Duplicate Entry Report to obtain a listing of the

duplicates with their inventory, on-demand, and return data.

2\. With the information provided on the report, choose the duplicate

that needs to be removed.

3\. Enter a phrase such as "DO NOT USE" in the LOCATION field of the

inactivated item. The option Stock Items - Enter/Edit will

allow one to edit the LOCATION field.

4\. Inactivate the chosen item in the option Inactivate AOU Stock Item.

The Purge Dispensing Data option will purge the item from the subfile 100 days from the date of the item’s last activity.

Select MESSAGE Action: IGNORE (in IN basket)// <u>\<RET\></u>

After the initialization process is complete, you may wish to delete the init routines. If you choose to delete the init routines (PSGWI\*), you may also delete routines PSGWPOST, PSGWPST1, and PSGWPRE\* as they are used only by the init process.

At this time, you may wish to print a %INDEX for a hard copy of the routines, variables, etc. In programmer mode, D ^%INDEX for the PSGW\* routines.

Data Dictionary

The Data Dictionaries (DDs) are considered part of the on-line documentation for this software application. Use VA FileMan option \#8 (DATA DICTIONARY UTILITIES) to print the DDs. The following are the files for which you should print DDs:

> \#50 DRUG

> \#58.1 PHARMACY AOU STOCK

> \#58.16 AOU INVENTORY TYPE

> \#58.17 AOU ITEM LOCATION

> \#58.19 PHARMACY AOU INVENTORY

> \#58.2 AOU INVENTORY GROUP

> \#58.3 PHARMACY BACKORDER

> \#58.5 AR/WS STATS FILE

> \#59.4 INPATIENT SITE

> \#59.7 PHARMACY SYSTEM