---
title: DVB*4*49 Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: 
app_code: HINQ
app_name: Hospital Inquiry
section: FIN
app_status: active
pkg_ns: DVB
patch_ver: 4
patch_id: DVB*4*49
group_key: "HINQ:DVB:4"
file_numbers: []
security_keys: []
menu_options: 0
description: INSTALLATION INSTRUCTIONS=========================If installed during the normal workday, it is recommended thefollowing menu options are disabled to prevent possibleconflicts while running the KIDS Install. Other VISTA userswill not be affected.DGBT BENE TRAVEL SCREEN Claim Enter/EditDG LOAD PATIEN
audience: 
keywords: 
  - dvbhce
  - install
  - hinq
  - installation
  - options
  - wish
  - mark
  - hsusp
  - transport
  - kids
page_count: 0
word_count: 1037
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
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Hosp_Inquiry_(HINQ)/dvb_4_p49_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Hosp_Inquiry_(HINQ)/dvb_4_p49_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=41"
---

![](dvb-4-49-installation-guide/001.png)

HINQ REPLACEMENT INTERIM SOLUTION PHASE 1

INSTALLATION GUIDE

DVB_4_P49.KID

November, 2005

V*IST*A Health Systems Design & Development

INSTALLATION INSTRUCTIONS=========================If installed during the normal workday, it is recommended thefollowing menu options are disabled to prevent possibleconflicts while running the KIDS Install. Other VISTA userswill not be affected.DGBT BENE TRAVEL SCREEN Claim Enter/EditDG LOAD PATIENT DATA Load/Edit Patient DataDG REGISTER PATIENT Register a PatientDVB HREQ-GENERHREQ Generate HINQ RequestsDVB HREQ-INDIVHREQ Individual HINQ RequestDVB HREQ-STATUSBYPAT Status of HINQ by PatientDVB HSUSP-ENTERREQ Enter a Request in the HINQ Suspense FileDVB HSUSP-MAIL Create a mail messageDVB HSUSP-PRINTSUSP Print Suspense File MessagesDVB HSUSP-PROCESSFILE Process the HINQ Suspense FileInstall time - less than three minutes.1. Retrieve the KIDS host file per software retrieval directionsabove.2. Place the host file into a directory that is accessible from theaccount into which you are installing.3. START UP KIDS-------------Start up the Kernel Installation and Distribution System Menu\[XPD MAIN\]:Edits and Distribution ...Utilities ...Installation ...Select Kernel Installation & Distribution System Option: Installation1 Load a Distribution2 Verify Checksums in Transport Global3 Print Transport Global4 Compare Transport Global to Current System5 Backup a Transport Global6 Install Package(s)Restart Install of Package(s)Unload a DistributionSelect Installation Option: 1 Load a DistributionEnter a Host File: DVB_4_P49.KIDUse INSTALL NAME: DVB \*4.0\*49 to install this Distribution.4. In KIDS Menu------------Select Kernel Installation & Distribution System Option: INStallation---Load a DistributionPrint Transport GlobalCompare Transport Global to Current SystemVerify Checksums in Transport GlobalInstall Package(s)Restart Install of Package(s)Unload a DistributionBackup a Transport GlobalSelect Installation Option:5. Select Installation Option:--------------------------NOTE: The following are OPTIONAL (When prompted for the INSTALLNAME, enter DVB\*4.0\*49):a. Backup a Transport Global - This option will create a backupmessage of any routines exported with this patch. It willnot backup any other changes such as DD's or templates.b. Compare Transport Global to Current System - This optionwill allow you to view all changes that will be made whenthis patch is installed. It compares all components of thispatch (routines, DD's, templates, etc.).c. Verify Checksums in Transport Global - This option willAllow you to ensure the integrity of the routines that arein the transport global.6. Select Installation Option: Install Package(s)----------------\*\*This is the step to start the installation of this KIDS patch:a. Choose the Install Package(s) option to start the patchinstall. Enter DVB\*4.0\*49 when prompted for a build name.b. When prompted Want KIDS to Rebuild Menu Trees Upon Completionof the Install? YES// answer NOc. When prompted 'Want KIDS to INHIBIT LOGONs during theinstall? YES//' answer NO (unless otherwise indicated).d. When prompted 'Want to DISABLE Scheduled Options, MenuOptions, and Protocols? YES//' answer YES (unless otherwiseindicated).e. When prompted 'Enter options you wish to mark as 'Out OfOrder':' Enter the following options:DGBT BENE TRAVEL SCREEN Claim Enter/EditDG LOAD PATIENT DATA Load/Edit Patient DataDG REGISTER PATIENT Register a PatientDVB HREQ-GENERHREQ Generate HINQ RequestsDVB HREQ-INDIVHREQ Individual HINQ RequestDVB HREQ-STATUSBYPAT Status of HINQ by PatientDVB HSUSP-ENTERREQ Enter a Request in the HINQ Suspense FileDVB HSUSP-MAIL Create a mail messageDVB HSUSP-PRINTSUSP Print Suspense File MessagesDVB HSUSP-PROCESSFILE Process the HINQ Suspense Filef. When prompted 'Enter protocols you wish to mark as 'Out OfOrder': hit 'Enter'.g. If prompted 'Delay Install (Minutes): (0-60): 0//answer "0" (unless otherwise indicated).The following is a copy of the installation display of this hostfile.Select Installation Option: 6 Install Package(s)Select INSTALL NAME: DVB\*4.0\*49 Loaded from Distribution 8/9/05@13:34:20=\> HINQ REPLACEMENT 8/8/05 ;Created on Aug 08, 2005@15:02:17This Distribution was loaded on Aug 09, 2005@13:34:20 with header ofHINQ REPLACEMENT 8/8/05 ;Created on Aug 08, 2005@15:02:17It consisted of the following Install(s):DVB\*4.0\*49 DG\*5.3\*631 DGBT\*1.0\*11Checking Install for Package DVB\*4.0\*49Install Questions for DVB\*4.0\*49Incoming Files:395 DVB PARAMETERS (Partial Definition)Note: You already have the 'DVB PARAMETERS' File.Checking Install for Package DG\*5.3\*631Install Questions for DG\*5.3\*631Incoming Files:2 PATIENT (Partial Definition)Note: You already have the 'PATIENT' File.Checking Install for Package DGBT\*1.0\*11Install Questions for DGBT\*1.0\*11Want KIDS to INHIBIT LOGONs during the install? YES// NOWant to DISABLE Scheduled Options, Menu Options, and Protocols? YES//Enter options you wish to mark as 'Out Of Order': DG LOAD PATIENT DATA Load/Edit Patient DataEnter options you wish to mark as 'Out Of Order': DG REGISTER PATIENT Register a PatientEnter options you wish to mark as 'Out Of Order': DGBT BENE TRAVEL MENU Beneficiary Travel MenuEnter options you wish to mark as 'Out Of Order': DVB HREQ-GENERHREQ Generate HINQ RequestsEnter options you wish to mark as 'Out Of Order': DVB HREQ-INDIVHREQ Individual HINQ RequestEnter options you wish to mark as 'Out Of Order': DVB HREQ-STATUSBYPAT Status of HINQ by PatientEnter options you wish to mark as 'Out Of Order': DVB HSUSP-ENTERREQ Enter a Request in the HINQ Suspense FileEnter options you wish to mark as 'Out Of Order': DVB HSUSP-MAIL Create a mail messageEnter options you wish to mark as 'Out Of Order': DVB HSUSP-PRINTSUSP Print Suspense File MessagesEnter options you wish to mark as 'Out Of Order': DVB HSUSP-PROCESSFILE Process the HINQ Suspense FileEnter protocols you wish to mark as 'Out Of Order':Delay Install (Minutes): (0-60): 0//Enter the Device you want to print the Install messages.You can queue the install by enter a 'Q' at the device prompt.Enter a '^' to abort the install.DEVICE: HOME// NETWORKInstall Started for DVB\*4.0\*49 :Aug 09, 2005@15:44:09Build Distribution Date: Aug 08, 2005Installing Routines:Aug 09, 2005@15:44:09Installing Data Dictionaries:Aug 09, 2005@15:44:09Installing PACKAGE COMPONENTS:Installing PRINT TEMPLATEInstalling INPUT TEMPLATEAug 09, 2005@15:44:10Running Post-Install Routine: ^DVB4049PIP address successfully updated to 10.224.132.135.Previous IP address was 10.224.132.135.\>\> \*\*\* Updating ANATOMICAL-LOSS CODE file (#395.2)Updating Routine file...The following Routines were created during this install:DVBHCEDVBHCE1DVBHCE10DVBHCE11DVBHCE12DVBHCE13DVBHCE14DVBHCE15DVBHCE16DVBHCE17DVBHCE18DVBHCE19DVBHCE2DVBHCE20DVBHCE21DVBHCE22DVBHCE23DVBHCE24DVBHCE25DVBHCE26DVBHCE27DVBHCE28DVBHCE29DVBHCE3DVBHCE30DVBHCE31DVBHCE32DVBHCE33DVBHCE34DVBHCE35DVBHCE4DVBHCE5DVBHCE6DVBHCE7DVBHCE8DVBHCE9DVBHCGUpdating KIDS files...DVB\*4.0\*49 Installed.Aug 09, 2005@15:44:11Install Message sent \#1490Install Started for DG\*5.3\*631 :Aug 09, 2005@15:44:11Build Distribution Date: Aug 08, 2005Installing Routines:Aug 09, 2005@15:44:11Installing Data Dictionaries: ....Aug 09, 2005@15:44:13Updating Routine file...Updating KIDS files...DG\*5.3\*631 Installed.Aug 09, 2005@15:44:13DGBT\*1.0\*11--------------------------------------------------------------------------------Install Message sent \#1491Install Started for DGBT\*1.0\*11 :Aug 09, 2005@15:44:13Build Distribution Date: Aug 08, 2005Installing Routines:Aug 09, 2005@15:44:13Updating Routine file...Updating KIDS files...DGBT\*1.0\*11 Installed.Aug 09, 2005@15:44:13Install Message sent \#1492--------------------------------------------------------------------------------+------------------------------------------------------------+100% ¦ 25 50 75 ¦Complete +------------------------------------------------------------+Install Completed