---
consolidated_title: "controlled substances installation guide"
app_code: PSD
doc_type: IG
master_source: "Controlled Substances Version 3 Installation Guide"
master_pub_date: March 1997
consolidated_from: 2 versions
prior_versions:
  - "Controlled Substances Version 3 Installation Guide (Updated PSD*3*89)"
---

**CONTROLLED SUBSTANCES**

**INSTALLATION GUIDE**


March 1997


Software Service

**Clinical Ancillary Product Line**

**Preface**

This guide explains how to install Version 3.0 of the Controlled Substances (CS) module of the Pharmacy package.

This package was exported using the Kernel Installation and Distribution

System (KIDS) instead of the VA FileMan DIFROM utility. You will use KIDS to install the software. Please read your KIDS documentation located in Part 5 of your Kernel V. 8.0 Systems Manual and familiarize yourself with KIDS before you install this software.

If your Pharmacy Service intends to use the Health Level Seven (HL7) interface to narcotic dispensing equipment systems, it would be a good idea to familiarize yourself with the HL7 V. 1.6 User manual.

**Table of Contents**

Intranet

Package Requirements

Steps for Installation

Assigning CS Menus

Allocating Security Keys

Resource Requirements

Hardware Requirements

Disk Space

Journaling Globals and Mapping Routines

Nightly Background Job

Appendix A

Port Set up for HL7 Interface to Narcotic Dispensing Equipment

Appendix B

Starting the HL7 Interface to Narcotic Dispensing Equipment

########### 

## Intranet

We are now on the intranet, come visit us. REDACTED This address will take you to the Clinical Products page where you will find a listing of all the clinical software manuals and other software manuals. Click on the Controlled Substances (CS) link and it will take you to the CS Homepage. You can also get there by going straight to

REDACTED (don’t forget to bookmark it!)

In addition, both of these homepages have a Software Service Homepage link. Simply click on this link and then follow the links to the manuals you would like to see.

## Package Requirements

The CS module relies on, at least, the following external packages to run effectively:

Package	Minimum version needed

Kernel	8.0

VA FileMan	21.0

MailMan	7.1

Nursing	2.5

Outpatient Pharmacy	6.0

Auto Replenishment/Ward Stock	2.2

Inpatient Medications	4.0

Drug Accountability	2.0

Integrated Billing	2.0

Health Level 7 (HL7)	1.6

To run this module, the New Person (#200), Ward Location (#42), Drug (#50), PHARMACY SYSTEM (#59.7), INPATIENT SITE (#59.4), and Prescription (#52) files are needed. The system does not need to be taken down, but the CS and Drug Accountability menus must be made **unavailable** to the users. This is now handled within the KIDS install process.

Patches XU*8.0*26 and XU*8.0*44 must be installed to support the witness   	identification for Nurse dispensing functionality and the HL7 interface.

Patch PSO*6*134 should be installed to ensure compatibility between 	Outpatient Version 6.0 and Controlled Substances Version 3.0.

Please note that patch PSGW* 2.2*2 should be installed to ensure 	compatibility between AR/WS Version 2.2 and Controlled Substances Version 	3.0.

This package is required to support the Health Level 7 (HL7) Interface to 	Narcotic dispensing Equipment Systems.

## ## Steps for Installation

It is recommended that the following eight steps be performed in a test UCI prior to installing in a production environment.

(1) If your Pharmacy Service intends to use the Health Level 7 (HL7) Interface to

the Narcotic dispensing Equipment Systems (NDES), we **strongly** suggest that you read through Appendix A of this document and complete your port set up before proceeding with the installation.

(2) Set up Variables. Set up your DUZ and set DUZ(0) to "@" using the ^XUP

entry point.

&gt; **D ^XUP &lt;RET&gt;** *(To set DUZ when responding to the Access Code prompt.*

*Press return at the OPTION prompt.)*

Setting up programmer environment

Terminal Type set to: **C-VT100**

Select OPTION NAME: **KERNEL INSTALLATION &amp; DISTRIBUTION SYSTEM**

Select Kernel Installation &amp; Distribution System Option: **IN** stallation

Select Installation Option: **LOA** d a Distribution

Enter a Host File: **CSUB3\_0.KID**

KIDS Distribution saved on Aug 22, 1996@16:34:54

Comment: CONTROLLED SUBSTANCES VERSION 3.0

This Distribution contains Transport Globals for the following Package(s):

CONTROLLED SUBSTANCES 3.0

Want to Continue with Load? YES// **&lt;RET&gt;**

Loading Distribution...

Want to RUN the Environment Check Routine? YES// **&lt;RET&gt;**

Will first run the Environment Check Routine, PSDINPRE

Use CONTROLLED SUBSTANCES 3.0 to install this Distribution.

> **NOTE:** At this point, you may wish to run the *Verify Checksum in Transport Global* option. If any of the routine checksums failed, you should contact your distributing IRM Field Office and not proceed with the installation process.

Select Installation Option: **INST** all Package(s)

Select INSTALL NAME: **CONTROLLED SUBSTANCES 3.0**

This Distribution was loaded on Aug 26, 1996@16:12:07 with header of

CONTROLLED SUBSTANCES VERSION 3.0  ;Created on Aug 22, 1996@16:34:5

It consisted of the following Install(s):

CONTROLLED SUBSTANCES 3.0

Will first run the Environment Check Routine, PSDINPRE

Install Questions for CONTROLLED SUBSTANCES 3.0

50        DRUG  (Partial Definition)

> **NOTE:** You already have the 'DRUG' File.

58.2      AOU INVENTORY GROUP  (Partial Definition)

> **NOTE:** You already have the 'AOU INVENTORY GROUP' File.

58.8      DRUG ACCOUNTABILITY STATS

> **NOTE:** You already have the 'DRUG ACCOUNTABILITY STATS' File.

58.81     DRUG ACCOUNTABILITY TRANSACTION

> **NOTE:** You already have the 'DRUG ACCOUNTABILITY TRANSACTION' File.

58.82     CS ORDER STATUS  (including data)

> **NOTE:** You already have the 'CS ORDER STATUS' File.

I will MERGE your data with mine.

58.83     CS COMPLETION STATUS  (including data)

> **NOTE:** You already have the 'CS COMPLETION STATUS' File.

I will MERGE your data with mine.

58.84     DRUG ACCOUNTABILITY TRANSACTION TYPE  (including data)

> **NOTE:** You already have the 'DRUG ACCOUNTABILITY TRANSACTION TYPE' File.

I will OVERWRITE your data with mine.

58.85     CS WORKSHEET

> **NOTE:** You already have the 'CS WORKSHEET' File.

58.86     CS DESTRUCTION

> **NOTE:** You already have the 'CS DESTRUCTION' File.

58.87     CS CORRECTION LOG

> **NOTE:** You already have the 'CS CORRECTION LOG' File.

58.88     CS IRL PROGRAM  (including data)

> **NOTE:** You already have the 'CS IRL PROGRAM' File.

I will OVERWRITE your data with mine.

58.89     CS ERROR LOG

> **NOTE:** You already have the 'CS ERROR LOG' File.

59.4      INPATIENT SITE  (Partial Definition)

> **NOTE:** You already have the 'INPATIENT SITE' File.

59.7      PHARMACY SYSTEM  (Partial Definition)

> **NOTE:** You already have the 'PHARMACY SYSTEM' File.

Do you want to enter/edit your interface setup

for Narcotic Dispensing Equipment Systems? No// **?**

Interface to Narcotic Dispensing Equipment Systems

Version 3.0 of the Controlled Substances package uses the HL7 package

to provide a generic interface to Narcotic Dispensing Equipment Systems

(NDES).  HL7 or Health Level Seven is a standard protocol which specifies

the implementation of interfaces between two computer applications (sender

and receiver) from different vendors for electronic data exchange in

health care environments.  If your Pharmacy sService is using an NDES such

as Access, Meditrol, Pyxis, or Suremed you may wish to set up the

interface.  This will be accomplished by adding entries to the HL7

APPLICATION PARAMETER (#771), HL LOWER LEVEL PROTOCOL PARAMETER (#869.2),

and HL LOGICAL LINK (#870) files.  You will be asked to identify an HL7

device which must exist as entry in your DEVICE file (#3.5).

The PSDHLK routine is invoked by the Controlled Substances post-init.

The routine, PSDHL7 is also independently invokable at any time that a site

needs to set up their interface for nNarcotic dDispensing eEquipment sSystems.

If you do NOT want to perform this step at the time of the post-init,

you can simply D ^PSDHL7 when you're ready.

Select HELP SYSTEM action or &lt;return&gt;: **&lt;RET&gt;**

Do you want to enter edit your interface setup

for narcotic dispensing equipment systems? No// **Y** es  Only answer "yes" if you intend to use the HL7 interface to a narcotic dispensing equipment system.

Select one of the following:

H         Hybrid Lower Layer Protocol {Pyxis, Suremed, Meditrol}

X         X3.28 Protocol

Select a communications protocol: H// **&lt;RET&gt;** ybrid Lower Layer Protocol

HLLP DEVICE: *[Enter your Interface device from your DEVICE file here.]*

Want to DISABLE Scheduled Options and Options? YES// **&lt;RET&gt;**

Enter options you wish to mark as 'Out Of Order': **PSA***

{Because Drug Accountability shares many files with Controlled Substances, the PSA* options should also be placed Out Of Order.}

{If you have any local options that might be affected by this install, it is recommended that you mark them Out of Order.}

Enter options you wish to mark as 'Out Of Order': **??**

Out of Order Manager

You are building a list of options and/or protocols to be marked 'Out

Of Order'. You may enter them in several different ways:

You may simply enter an option or protocol name,

or  NAM* to specify all that begin with the characters 'NAM'

or  NAM1-NAM2 to specify all the options or protocols that fall

alphabetically between NAM1 and NAM2 inclusive,

or  *    to select all options or protocols,

or  -    with any of the above to remove items already selected,

or  ^    to quit and exit the program,

or  ^PR  to switch from working with options to protocols,

or  ^OP  to switch from working with protocols to options,

or  ?    to see a brief help prompt,

or  ??   to see this help screen again,

or  ???   to see the list of items chosen so far,

or  ????   to see the Option or Protocol File,

Select HELP SYSTEM action or &lt;return&gt;: **&lt;RET&gt;**

Enter options you wish to mark as 'Out Of Order': **???**

{To see a list of items chosen so far, enter ???.}

You will place Out Of Order the following options: **&lt;RET&gt;**

{What follows is a partial list, but the install automatically places all Controlled Substances options and protocols out of order.}

Set Up CS (Build Files) Menu   [PSD SETUP]   (IEN = 4306)

Enter/Edit CS Drug Location Codes   [PSD DRUG LOC EDIT]   (IEN = 4307)

Create/Edit the Narcotic Area of Use   [PSD NAOU EDIT]   (IEN = 4308)

You will place Out Of Order the following protocols: **&lt;RET&gt;**

[PSD PAT ADT]   (IEN = 937)

[PSD MM]   (IEN = 938)

Controlled Substances admit (A01) server   [PSD A01 SERVER]   (IEN = 939)

Controlled Substances admit client   [PSD A01 CLIENT]   (IEN = 940)

Controlled Substances transfer (A02) server   [PSD A02 SERVER]   (IEN = 941)

Controlled Substances transfer (A02) client   [PSD A02 CLIENT]   (IEN = 942)

Controlled Substances discharge (A03) server   [PSD A03 SERVER]   (IEN = 943)

Controlled Substances discharge (A03) client   [PSD A03 CLIENT]   (IEN = 944)

Enter options you wish to mark as 'Out Of Order': **&lt;RET&gt;**

Enter protocols you wish to mark as 'Out Of Order': **&lt;RET&gt;**

Enter protocols you wish to mark as 'Out Of Order': **&lt;RET&gt;**

Delay Install (Minutes):  (0-60): 0// **&lt;RET&gt;**

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// *[Select Print Device]*

Install Started for CONTROLLED SUBSTANCES 3.0 :

Aug 26, 1996@16:13:57

Installing Routines:

Aug 26, 1996@16:14:21

Installing Data Dictionaries:

Aug 26, 1996@16:14:41

Installing Data:

Aug 26, 1996@16:14:42

Installing PACKAGE COMPONENTS:

Installing HELP FRAME

Installing SECURITY KEY

Installing INPUT TEMPLATE

Installing HL LOWER LEVEL PROTOCOL PARAMETER

Installing HL LOGICAL LINK

Installing HL7 APPLICATION PARAMETER

Installing PROTOCOL

Located in the PSD (CONTROLLED SUBSTANCES) namespace.

Located in the PSD (CONTROLLED SUBSTANCES) namespace.

Located in the PSD (CONTROLLED SUBSTANCES) namespace.

Located in the PSD (CONTROLLED SUBSTANCES) namespace.

Located in the PSD (CONTROLLED SUBSTANCES) namespace.

Located in the PSD (CONTROLLED SUBSTANCES) namespace.

Located in the PSD (CONTROLLED SUBSTANCES) namespace.

Installing LIST TEMPLATE

Aug 26, 1996@16:15:27

Installing OPTION

Running Post-Install Routine: ^PSDIPOST

CONTROLLED SUBSTANCES VERSION 2.0 has been previously installed,

no post-init conversion required.

Finished.

{You will only see the next two updates if you answered yes to the interface setup question.}

Updating FACILITY NAME for PSD-CS entry in file #771.

Updating DEVICE for PSD-NDES HLLP entry in file #869.2.

Updating Routine file...

Updating KIDS files...

CONTROLLED SUBSTANCES 3.0 Installed.

Aug 26, 1996@16:15:50..

Install Message sent #71

Install Completed

Select Installation Option:

Use the *KIDS Build File Print* option if you wish to obtain a complete listing of the package components (e.g., routines and options) sent with this Distribution file.

Use the *KIDS Install File Print* option if you wish to print out the results of the installation process.

After you have installed the package in a test account, and pharmacy has familiarized themselves with all the options, you should repeat this procedure in a live account.

(3) **Set up hardware devices required by Version 3.0.** This is an important step. Version 2.0 of Controlled Substances printed green sheets on pre-printed forms using either an HP III or Kyocera printer. Version 3.0 prints these same forms on plain paper but **requires** updates to your TERMINAL TYPE file in order to format these forms correctly. The routine PSDTER is provided for your convenience to perform these updates. It must be run on the TERMINAL TYPE entry that is attached to the DEVICE that Pharmacy currently uses for printing green sheets or Pharmacy will be **unable** to continue to print greens sheets. This is a critical step in the dispensing of controlled substances. For an example of running the routine, please see page 26.

(4) The install process takes approximately 20 minutes to run. File security codes of the “@” have been exported. A post-init routine will only run if Controlled Substances Version 2.0 has not been installed. It will mark entries in your Drug file (#50) for CS use based on the Drug Enforcement Agency (DEA) Special Handling Data. The re-indexing of data in the APPLICATION PACKAGES’ USE field (#63) in the DRUG file (#50), DATE/TIME TURN IN DESTROY field (#37), and the RECEIPT DATE/TIME field (#21) in the DRUG ACCOUNTABILITY TRANSACTION file (#58.81), and the DATE/TIME DESTROYED field (#10) in the CS DESTRUCTION file (#58.86), also occurs during the post-init process. The security keys PSDMGR, PSD PARAM, PSD TRAN, PSD ERROR, and PSD NURSE will be created, if necessary.

(5) Assign the appropriate menus to CS users.

(6) Allocate necessary security keys to CS users.

(7) Enable nightly background job. See instructions on page .

(8) If your Pharmacy Service intends to use the Health Level 7 (HL7) Interface to

the Narcotic dispensing Equipment Systems, please read Appendix B of this document for instructions on starting the interface.

## Assigning CS Menus

The following menus are available for Pharmacy personnel:

Controlled Substances Menu...[PSD MENU]

Supervisor (CS) Menu...[PSD MGR]

**&gt;Locked with PSDMGR

Technician (CS Pharmacy) Menu...[PSD PHARM TECH]

Pharmacist Menu...[PSD TRANSACTION MENU]

Production Reports...[PSD PRODUCTION REPORTS]

Barcode Drug Labels for Vault [PSD LABEL VAULT]

All nursing personnel, using the CS software, may be assigned the *PSD NURSE MENU* as a menu option. Nursing Supervisors may want access to the *PSD NURSE SUPR MENU* . Controlled Substances inspectors may be assigned the *PSD INSPECTOR MENU* . Some stations design their own menus for individual users. If this is the case, then **only** the top level CS menus should contain the following entry and exit code in the OPTION file (#19) to ensure that users are prompted only **once** for an Inpatient Site:

ENTRY ACTION : I '$D(PSDSITE) D ^PSDSET

EXIT ACTION: K PSDSITE

This entry and exit code must be present because the PSDSITE variable is set as users enter the package. If the Kernel’s “^ OPTION NAME” feature is used to jump directly into lower levels of the CS package, then the Inpatient Site Name prompt must be answered in order to define the PSDSITE variable. All options are independently secured; however, if the instructions above are not followed, users will be repeatedly asked to select an Inpatient Site if there are two or more sites that are flagged as selectable for CS use.

## Allocating Security Keys

There are nine keys associated with CS:

**• PSD ERROR** Allocate this key to pharmacy supervisors responsible for 	maintaining the narcotic vault.

This key controls access to reports listing various errors 	and exception conditions generated when entries are filed 	from the barcode TRAKKER. Also, the holders of this key 	will receive electronic mail messages created by using the 	TRAKKER.

**• PSDMGR** Allocate this key to the Inpatient Pharmacy 	Coordinators. This key controls the editing of CS files for 	package set up and it locks the *Supervisor (CS) Menu* .

**• PSD NURSE** Allocate this key to nurses, usually LPNs, who may only 	receive and administer controlled substances drugs, but 	cannot place order requests.

**• PSD PARAM** Allocate this key to **only** the Inpatient Pharmacy 	Coordinators. This key controls the printing of the Green 	Sheets and the range of automated dispensing numbers 	for a dispensing site.

**• PSD TRAN** Allocate this key only to the Inpatient Pharmacy 	Coordinator. This key controls the access to the *Transfer Stock Entries* option. Users can copy stock 	entries from one Narcotic Area Of Use (NAOU) into 	another NAOU or from an Auto Replenishment/Ward 	Stock (AR/WS) Area Of Use (AOU) into an NAOU.

**• PSJ PHARM TECH** Allocate this key to pharmacy technicians handling 	controlled substances orders.

**• PSJ RNURSE** Allocate this key to nurses who request and receive 	controlled substances orders on the wards.

**• PSJ RPHARM** Allocate this key to pharmacists who can dispense and 	receive controlled substances drugs.

**• PSD TECH** This key will give access to the List On-Hand Amounts, 	Transfer Drugs between Dispensing Sites Report, and the 	Daily Activity Log options on the Pharmacy Technician 	Menu.

## Resource Requirements

### Hardware Requirements

The following equipment is recommended to successfully implement Version 3.0:

Intermec TRAKKER 9440 (Barcode Reader)

HP LaserJet III (or any compatible laser printer)

VT320 (bi-directional only) or any bi-directional flow CRT

The laser single sheet feed printer is required to print the pre-printed VA FORM

10-2638 and barcode ID labels. It is recommended that the printer be physically located in the narcotic vault for efficiency and security.

The laser printer must be a selectable device via the terminal server. Barcode printing is not available with a slaved printer.

The barcode TRAKKERs and CRTs are required to download/upload data necessary in maintaining a perpetual inventory within the pharmacy narcotic vault.

To support barcode label printing and downloading/uploading via the TRAKKER, certain hardware specific parameters for the TERMINAL TYPE file (#3.2) and DEVICE file (#3.5) are necessary. To assist Information Resources Management (IRM) in setting up these devices the routine PSDTER has been included in the routine set. The TERMINAL TYPE file (#3.2) information includes right margin, form feed, page length, back space, open execute, barcode on, and barcode off. The DEVICE file (#3.5) data includes margin width, form feed, page length, back space, and subtype. For the TRAKKER, open printer port and close printer port are included in the TERMINAL TYPE file (#3.2) information. See page  for examples in setting up the devices using the routine PSDTER.

**Kyocera Setup for Printing Barcodes**

**DEVICE file (#3.5):**

NAME: KYOCERA BARCODER	$I: &lt;$I value&gt;

ASK DEVICE: YES	ASK PARAMETERS: YES

SIGN-ON/SYSTEM DEVICE: NO	LOCATION OF TERMINAL: &lt;location&gt;

MARGIN WIDTH: 0 	FORM FEED: #

PAGE LENGTH: 66	BACK SPACE: $C(8)

SUBTYPE: P-KYOCERA-BARCODE	TYPE: TERMINAL

**TERMINAL TYPE file (#3.2):**

NAME: P-KYOCERA-BARCODE                 SELECTABLE AT SIGN-ON: NO

RIGHT MARGIN: 0                                     FORM FEED: #

PAGE LENGTH: 66                                    BACK SPACE: $C(8)

OPEN EXECUTE: W "!R! RES;FONT "\_$S($G(PSDCPI)=10:1,1:6)\_";EXIT;"

10 PITCH: "!R! FONT1; EXIT;"          12 PITCH: "!R! FONT6; EXIT;"

DEFAULT LINES PER INCH: "!R! SLM 2; EXIT;"

X LINES PER INCH: "!R! SLPI 4.1; EXIT;"

BAR CODE OFF: "', 60, 60, 3, 6, 6, 6, 3, 6, 6, 6;"\_$S('$D(PSDX1):"",PSDX1=PSDC

NT:"MRP 0 , 60;",1:"")\_"EXIT;"

BAR CODE ON: "!R! FONT 6; UNIT D; "\_$S('$D(PSDX1):"",PSDX1=1:"MRP 0,-60 ; ",1:"")\_$S('$D(PSDX1):"",1:"MRP "\_(PSDX1&gt;1*810+38)\_" , 0 ;")\_" BARC 19, N, '"

**HP LaserJet III Setup for Printing Barcodes**

The barcode font cartridge must be installed prior to trying to print any barcode labels. Refer to page 11 in the *Using the Hewlett-Packard Barcodes and More Font Cartridges* guide.

**DEVICE file (#3.5):**

NAME: HP III BARCODER	$I: &lt;$I value&gt;

ASK DEVICE: YES	ASK PARAMETERS: YES

SIGN-ON/SYSTEM DEVICE: NO	LOCATION OF TERMINAL: &lt;location&gt;

MARGIN WIDTH: 0	FORM FEED: #

PAGE LENGTH: 58 	BACK SPACE: $C(8)

SUBTYPE: P-HP BARCODER 	TYPE: TERMINAL

LAT SERVER NODE: &lt;node name&gt;	LAT SERVER PORT: &lt;port number&gt;

VMS DEVICE TYPE: NOT SPOOLED	LAT PORT SPEED: 96

**TERMINAL TYPE file (#3.2):**

NAME: P-HP BARCODER                     SELECTABLE AT SIGN-ON: NO

RIGHT MARGIN: 0                       FORM FEED: #

PAGE LENGTH: 58                       BACK SPACE: $C(8)

OPEN EXECUTE: W

$C(27)\_"E"\_$C(27)\_"&amp;l0O"\_$C(27)\_"(8U"\_$C(27)\_"(s0p"\_$S($G(PSDC

PI)=10:"10h14",1:"12h12")\_"v0s0b6T"

10 PITCH: $C(27)\_"(s10H"              12 PITCH: $C(27)\_"(s12H"

HIGH INTENSITY (BOLD): $C(27)\_"(s4b"

DEFAULT LINES PER INCH: $C(27)\_"&amp;l8C"

X LINES PER INCH: $C(27)\_"&amp;l12C"

BAR CODE OFF:

"*"\_$C(27)\_"&amp;l0O"\_$C(27)\_"(8U"\_$C(27)\_"(s0p"\_$S($G(PSDCPI)=10:"1

0h14",1:"12h12")\_"v0s0b6T"

BAR CODE ON: $S($D(PSDX2):$C(27)\_"*p"\_(PSDX2-1*300+200)\_"y*p"\_(PSDX1-

1*810+38)\_"X",1:"")\_$C(27)\_"(0Y"\_$C(27)\_"(s0p8.1h12v0s0b0T*"

**Preparation of Portable Barcode Reader (TRAKKER 9440)**

Controlled Substances Version 3.0 includes options for downloading Interactive Reader Language (IRL) programs to the TRAKKER. For these options to function, the TRAKKER must be connected to your **V** *IST* **A** (Veterans Health Information Systems and Technology Architecture) computer system. The TRAKKER comes with an RS-232 cable. The end of the cable that is intended to be connected to your system terminates to a DB—25 PIN connector.

The TRAKKER may be connected to your system via the auxiliary port of any CRT that supports complete bi-directional data flow and flow control (XON-XOFF) through the auxiliary port. Whatever strategy works for addressing a slaved printer to the CRT will also work for the TRAKKER.

*Preparing the TRAKKER for Operation*

The following procedure illustrates stepping through the configuration process to verify whether the TRAKKER is properly prepared to interface with **V** *IST* **A** .

**Note:** A brief example of the TRAKKER setup may be displayed by 	running routine PSDTRAK from programmer mode.

To enter the configuration mode you must do the following:

1.	Turn the TRAKKER on by pressing the [on-off] key. The unit should

perform a brief self-test and then display a Ready prompt.

2.	Hold down the [ctrl] key and press **E** . The words “CONFIGURATION

MENU:” should appear on the first line of the TRAKKER display screen. 	You are now in the configuration mode.

To prepare the TRAKKER for operation with the Veterans Health Information Systems and Technology Architecture ( **V** *IST* **A** ):

3.	Press the [enter] key until you are prompted to “Select or modify 	operating parameters?”. The word **NO** will appear on the fourth 	TRAKKER display line.

4.	Change **NO** to **YES** by pressing the [space] key.

5.	Use the [enter] key to step through the basic operating parameters. 	Unless otherwise instructed, use the [space] key to make your selections:

a.	BEEP VOLUME: Set this according to your preference. If your 	work environment is noisy, choose **HIGH** .

b.	DISPLAY MODE: This tells the TRAKKER how to display data 	that you enter. Choose **BUFFERED** .

c.	CHARACTER SET: This selects an alphabet. Choose **US-ASCII** .

d.	CPU RESP REQD MODE: Tells the TRAKKER whether to wait for 	an acknowledgment from **V** *IST* **A** after each transmission of 	uploaded data. Choose **DISABLED** .

e.	PREAMBLE A REQUIRED: Tells the TRAKKER whether to check 	for one specific preamble on all data entered. Choose **NO** .

f.	LASER SCANNER MODE: Tells the TRAKKER whether to allow 	continuous scanning of barcode labels without release of the laser 	trigger in between. Choose **ONE-SHOT TRIGGER** .

g.	APPEND TIME TO DATA: Instructs the TRAKKER to add the 	correct time to each data record as it is transmitted. Choose **NO** .

h.	TIME IN SECONDS: Tells the TRAKKER whether time displays 	should include seconds. Choose **YES** .

i.	RESUME IRL PROGRAM: Choose **NO** .

j.	AUTOMATIC SHUT—OFF: A time-out feature such that the 	TRAKKER will turn itself off after a specified period of inactivity in 	order to conserve battery power. You must enter your selection (in 	minutes) as a number. The TRAKKER will ignore the [space] key. 	We suggest a **10 minute** time-out period.

k.	BACKLIGHT TIMEOUT: A time-out feature on backlighting of 	the TRAKKER display screen intended to conserve battery power. 	Selections are made in seconds. We suggest a **60 second** time-out 	period.

6.	The next configuration heading is “Select or modify comm protocol?” Use 	the [space] key to select **POINT TO POINT** .

7.	Use the [enter] key to step through the comm protocol:

a.	CHECK CTS: Tells the TRAKKER whether or not to look for a CTS 	(clear to send) signal before transmitting data. Since **V** *IST* **A** uses 	XON/XOFF, choose **NO** .

b.	XON: When XON/XOFF protocol is used, the XON character must 	be specified here. Hold down the [ctrl] key and press **Q** . **DC1** should appear on the last TRAKKER display line. Press [enter] to 	continue.

c.	XOFF: Hold down the [ctrl] key and press **S** . Observe **DC3** and 	press [enter] to continue.

d.	BAUD RATE: The TRAKKER data transmission speed. **1200 baud** is recommended.

e.	PARITY: Selection is **DISABLED** .

f	DATA BITS: Select **8** .

g.	STOP BITS: Select **1** .

h.	TIMEOUT DELAY: Tells the TRAKKER how long to wait for the 	next character of a downloaded IRL program before declaring an 	error condition. Choose **10 seconds** .

i.	INTERCHAR DELAY: Tells the TRAKKER how long to pause 	between characters when uploading data to **V** *IST* **A** . **Choose 50 	milliseconds (ms)** .

j.	TURNAROUND DELAY: Delay time between receipt of a 	character from **V** *IST* **A** and acknowledgment by the TRAKKER. This 	parameter is not critical with an XON/XOFF protocol. **Choose 0 	ms** .

8.	When you have set the TURNAROUND DELAY, you will once again see 	the “Select or modify barcodes?” prompt. The TRAKKER is now 	configured for use with VISTA.

Press the [alt] key and then the [E] for escape to save any changes that 	you may have made. Once saved, they will remain in a non-volatile 	section of TRAKKER memory until the TRAKKER is re-configured.

If you made a mistake and want to exit the configuration mode without 	saving any changes, hold down the [crtl] key and press [Z]. Do this 	instead of the escape sequence ([alt], [E]) described above.

########### If the TRAKKER has been configured differently, first it must be RESET. For details on this procedure, refer to the INTERMEC 944X TRAKKER READERS User’s Manual. Next, you must CONFIGURE the TRAKKER, repeating steps 1-8 on Preparing the TRAKKER for Operation.

**Note:** The clock should be set on the TRAKKER before users start 	performing inventories. It is not necessary to press enter after responding **yes** to setting the clock.

**Setting the TRAKKER clock:**

After having turned the TRAKKER on, press [Ctrl]-[T].

The following will be displayed:

*Interfacing*

Interfacing the TRAKKER 9440 to a VT-320 auxiliary port

The auxiliary port of the VT-320 is a six pin modular jack, so you will need a cable with a six pin modular plug on one end and a male DB-25 connector on the other.

The Pharmacist Menu is shown in reverse video for clarity.

Auxiliary 												Port

The PRINTER SET UP SCREEN of the VT-320 will allow you to configure the CRT for use with a TRAKKER. To get to this screen:

1.	Hold the SHIFT key and press **SET UP**

2.	Use the cursor control keys (right arrow) to move the cursor to the box 	labeled Printer.

3.	Press the **ENTER** key.

From this point, you can set the software selectable features of the auxiliary port as follows:

1.	Speed: The baud rate of the auxiliary port. This must match the baud rate 	of the TRAKKER. **1200** is commonly used.

2.	Printer to Host Communication: This must be set to **Printer to Host** for

the TRAKKER upload/download operations.

3.	Print Mode: Determines how the auxiliary port is controlled. Proper 	setting is **Normal Print Mode** .

4.	XOFF: This selects whether or not the auxiliary port will use XON/XOFF 	data flow control. Proper setting is **XOFF** .

5.	Bits and Parity: Selects a character format for the auxiliary port. Must 	match the character format of the TRAKKER.

6.	Stop Bit: Selects the number of stop bits. Must match the format of the 	TRAKKER. **1** stop bit is commonly used.

7.	Print Region: Unimportant for downloading or uploading. Commonly 	set to **Print Full Page** .

8.	Printed Data Type: Used primarily with slaved printer. Not critical for 	downloading or uploading. Commonly set to **National Only** .

9.	Print Terminator: Selects whether or not the VT-320 should send a form 	feed at the end of each print operation. Proper setting is **No Terminator** .

Finally, you will need appropriate entries in your TERMINAL TYPE file (#3.2) and the DEVICE file (#3.5). For IRM, the routine PSDTER will allow you to setup the TERMINAL TYPE file (#3.2) and DEVICE file (#3.5) information. This routine may be run from programmers mode. Refer to page  in the Installation Guide for an example.

The following examples are known to work:

**In the TERMINAL TYPE file (#3.2):**

NAME          	: C-VT420 (9440)

FORM FEED          	: #

OPEN EXECUTE       	: W $C(0)

DESCRIPTION        	: TRAKKER 9440 TO AUXILIARY PORT OF VT420

OPEN PRINTER PORT  	: W $C(27)\_"[5i"

CLOSE PRINTER PORT 	: W $C(27)\_"[4i"

RIGHT MARGIN       	: 80

PAGE LENGTH        	: 9999

**In the DEVICE file (#3.5):**

NAME               	: TRAKKERSL

LOCATION           	: SLAVED 9440 FROM VT420 AUXILIARY PORT

MARGIN WIDTH       	: 80

PAGE LENGTH        	: 9999

MNEMONIC           	: TRAKKERSL

FORM FEED          	: #

BACK SPACE         	: $C(8)

SUB-TYPE           	: C-VT420 (9440)

TYPE               	: TERMINAL

$I                 	: 0 (zero)

-------------------------------------------------------------------

**Functions on the TRAKKER:**

[Ctrl]-[T]			This will give you access to set the clock.

[Ctrl]-[enter]-[E]		This will give you access to end an IRL session.

Simultaneously press the [Ctrl]-[enter] keys,

release them, then press [E].

[Ctrl]-[enter]-[C]		This will give you access to clear the data files.

Simultaneously press the [Ctrl]-[enter] keys,

release them, then press [C].

*[To clear the data files you must have already ended the IRL session.]*

**Example of using PSDTER routine**

**D ^XUP**

Setting up programmer environment

Access code: **XXXXX**

Terminal Type set to: **C-VT100**

Select OPTION NAME: **&lt;RET&gt;**

&gt; **D ^PSDTER**

Select one of the following:

1         Load all three barcode Terminal Types

2         Load the P-HP BARCODER Terminal Type

3         Load the P-KYOCERA-BARCODE Terminal Type

4         Load the C-VT420 (9440) Terminal Type

5         Select your own Terminal Type

6         Display

7         Nevermind

Enter response: **?**

If any of the selected Terminal Types already exist, I will ask for your

approval before proceeding.

Select one of the following:

1         Load all three barcode Terminal Types

2         Load the P-HP BARCODER Terminal Type

3         Load the P-KYOCERA-BARCODE Terminal Type

4         Load the C-VT420 (9440) Terminal Type

5         Select your own Terminal Type

6         Display

7         Nevermind

Enter response: **1** Load all three barcode Terminal Types

Current settings: *[If a P-HP BARCODER TERMINAL TYPE already exist, current settings will be displayed.]*

Are you sure that you want to stuff the Controlled Substances barcode

set-up into the P-HP BARCODER Terminal Type? No// **Y** ES

Updating P-HP BARCODER.

Update the DEVICE file? No// **?**

Yes, and I will add the P-HP BARCODER Terminal Type and update a few

fields in the device of your selection.

Update the DEVICE file? No// **&lt;RET&gt;**

Current settings: *[If a P-KYOCERA BARCODE TERMINAL TYPE already exist, current settings will be displayed.]*

Are you sure that you want to stuff the Controlled Substances barcode

set-up into the P-KYOCERA-BARCODE Terminal Type? No// **?**

Yes and I'll update OPEN EXECUTE, RIGHT MARGIN, PAGE LENGTH, Etc. fields.

Are you sure that you want to stuff the Controlled Substances barcode

set-up into the P-KYOCERA-BARCODE Terminal Type? No// **Y** ES

Updating P-KYOCERA-BARCODE.

Update the DEVICE file? No// **&lt;RET&gt;**

Are you sure that you want to stuff the Controlled Substances barcode

set-up into the C-VT420 (9440) Terminal Type? No// **Y** ES

Updating C-VT420 (9440).

Update the DEVICE file? No// **&lt;RET&gt;**

The HP LaserJet III and the Kyocera laser printer setup used in testing the printing of the VA FORM 10-2638 follows on the next pages.

**HP LaserJet III Printer Setup**

NAME: P-HP BARCODER                     SELECTABLE AT SIGN-ON: NO

RIGHT MARGIN: 0                       FORM FEED: #

PAGE LENGTH: 58                       BACK SPACE: $C(8)

OPEN EXECUTE: W $C(27)\_"E"\_$C(27)\_"&amp;l0O"\_$C(27)\_"(8U"\_$C(27)\_"(s0p"\_$S($G(PSDC

PI)=10:"10h14",1:"12h12")\_"v0s0b6T"

10 PITCH: $C(27)\_"(s10H"              12 PITCH: $C(27)\_"(s12H"

HIGH INTENSITY (BOLD): $C(27)\_"(s4b"  DEFAULT LINES PER INCH: $C(27)\_"&amp;l8C"

X LINES PER INCH: $C(27)\_"&amp;l12C"

BAR CODE OFF: "*"\_$C(27)\_"&amp;l0O"\_$C(27)\_"(8U"\_$C(27)\_"(s0p"\_$S($G(PSDCPI)=10:"1

0h14",1:"12h12")\_"v0s0b6T"

BAR CODE ON: $S($D(PSDX2):$C(27)\_"*p"\_(PSDX2-1*300+200)\_"y*p"\_(PSDX1-1*810+38)

\_"X",1:"")\_$C(27)\_"(0Y"\_$C(27)\_"(s0p8.1h12v0s0b0T*"

**Kyocera Laser Printer Setup**

NAME: P-KYOCERA-BARCODE                 SELECTABLE AT SIGN-ON: NO

RIGHT MARGIN: 0                       FORM FEED: #

PAGE LENGTH: 66                       BACK SPACE: $C(8)

OPEN EXECUTE: W "!R! RES;FONT "\_$S($G(PSDCPI)=10:1,1:6)\_";EXIT;"

10 PITCH: "!R! FONT1; EXIT;"          12 PITCH: "!R! FONT6; EXIT;"

DEFAULT LINES PER INCH: "!R! SLM 2; EXIT;"

X LINES PER INCH: "!R! SLPI 4.1; EXIT;"

BAR CODE OFF: "', 60, 60, 3, 6, 6, 6, 3, 6, 6, 6;"\_$S('$D(PSDX1):"",PSDX1=PSDC

NT:"MRP 0 , 60;",1:"")\_"EXIT;"

BAR CODE ON: "!R! FONT 6; UNIT D; "\_$S('$D(PSDX1):"",PSDX1=1:"MRP 0,-60 ; ",1:

"")\_$S('$D(PSDX1):"",1:"MRP "\_(PSDX1&gt;1*810+38)\_" , 0 ;")\_" BARC 19, N, '"

**LASER    PRINTER    STATUS    PAGE**

Software version         6.45 - 20  ,  released 04/90.
      Units : Inches.                   Page : Portrait.
      Current font :      1.            Current country :  0. 
      Copies :  1.                      Current emulation :  6.

**Margins                           Spacings**

Top        0.300                  Line        0.167
       Bottom    10.300                  Character   0.100
       Left       0.000                  Pen width   0.010
       Right      8.000

**Memory allocation (Kbytes)** User memory avail.  187.225         In use (System) 108.773
       Prescribe MCRO buff.  4.996         In use            0.000
       PCL MCRO buff         3.500         In use            0.000

Parallel buff. size  10.000
       RS232C buff. size    10.000
       Raster size         128.000

**Miscellaneous status**

Option (Comment)     Value   Option(Comment)       Value
       -------------------------------------------------------
       CO(Reserved)           0     P1(Default Emulation)   6
       C1(Page orientation)   0     P2(C.R. action)         1
       C2(Dflt font Num-mid.) 0     P3(L.F. action)         1
       C3(Dflt font Num-low)  1     P9(Escape Char.)       82
       C4(PCL MCRO buff.)     0     UO(Line/Inch\_high)      6
       C5(Dflt font Num-High) 0     U1(Line/Inch\_low)       0
       A1(Top margin\_high)    0     U2(Char/Inch\_high)     10
       A2(Top margin\_low)     0     U3(Char/Inch\_low)       0
       A3(Left margin\_high)   0     U5(Status page)         0
      A4(Left margin\_low)    0      U6(Country code)        0
      A5(Page length\_high)  13      U7(Dflt symbol set)     0
      A6(Page length\_low)   61      RO(Reserved)            6
      A7(Page width\_high)    8      R1(Reserved)            0
      A8(Page width\_low)    11      R2(Dflt paper size)     0
      HO(Prescribe macro)    0      R3(Reserved)            0
      H1(RS232C baud rate)  96      R4(Reserved             1
      H2(RS232C data bits)   8      R5(Raster size)         1
      H3(RS232C stop bit)    1      R6(Reserved)            0
      H4(RS232C parity bit)  0      R7(Other paper size)    0
      H5(RS232C protocol)    0      R8(D.W. Data length)    7
      H6(Zoff threshold[%]) 90      R9(Reserved)            0
      H7(Xon threshold[%])  70      MO(PAR buffer size)     1
      H8(RS232C buff. size)  1      M1(Reserved)            0
      H9(F.F. time out)      3      M2(Reserved)            0

Service information

/0024/0050/1061/0811/

### Disk Space

There are 271 routines total that take up approximately 949k of disk space.

What follows is a sample of global growth from a test site where nurses

were using the radio frequency device to record doses dispensed to

patients:

STATISTICAL INFORMATION FOR ^PSD

Beginning Global Size:               18,793 Blks  (19.2 Mb)

Ending Global Size:                    22,819 Blks  (23.4 Mb)

# Sample Sessions:                     7 Samples

Total # of Sample Days:                 168 Days

Avg Daily Normalized Global Growth:         24 Blks

Avg 28 Day Normalized Global Growth:    672 Blks

Avg 1 Year Normalized PSD Growth:      8,760 Blks  (9.0 Mb)

Avg 1 Year Projected PSD Size:       31,579 Blks  (32.3 Mb)

Avg 2 Year Projected PSD Size:       40,339 Blks  (41.3 Mb)

Avg 3 Year Projected PSD Size:       49,099 Blks  (50.3 Mb)

What follows is a sample of the global growth in the HL7 package that

occurred at a test site using the interface to narcotic dispensing

equipment:

* SAGG Trending Results for the HEALTH LEVEL SEVEN (HL7) Package *

Trending Period from: APR 14, 1996 - SEP 01, 1996

Site:  N-CHICAGO     (VAX-DSM)          Data Shown in Blocks

Global     APR 14      MAY 12      JUN 09      JUL 07      AUG 04      SEP 01

------------------------------------------------------------------------------

HL            654         696       1,152       1,974       2,164       3,832

[+42]      [+456]      [+822]      [+190]    [+1,668]

------------------------------------------------------------------------------

HLCS            2           2         170         431       1,420         416

[0]      [+168]      [+261]      [+989]    [-1,004]

------------------------------------------------------------------------------

HLMA          673         813         981       1,079       1,101       1,382

[+140]      [+168]       [+98]       [+22]      [+281]

------------------------------------------------------------------------------

Totals:     1,329       1,511       2,303       3,484       4,685       5,630

[+182]      [+792]    [+1,181]    [+1,201]      [+945]

### Journaling Globals and Mapping Routines

Journaling is recommended for the ^PSD global.

No specific recommendation is made for routine mapping.

### Nightly Background Job

There is one background TASKMAN job that should be scheduled to run nightly.

The *PSD PURGE* option deletes entries from the CS WORKSHEET file (#58.85) that have been processed.

## ## ## Appendix A

### Port Set up for HL7 Interface to Narcotic Dispensing Equipment

**ALPHA System**

To install the HL7 interface on a VAX system, complete the following steps:

1.	Set up the DECserver port for each non- **V** *IST* A system to which you will be connecting.

2.	Create the VMS terminal characteristics and protection.

3.	Create the appropriate entries in the **V** *IST* A Device file (#3.5).

An example of each step is provided on the following pages.

**Set Up the DECserver Port**

Port 48: AVAILABLE                              Server: DSV9

Character Size:         8                  Input Speed:        9600

Flow Control:         XON                  Output Speed:       9600

Parity:              None                  Modem Control:  Disabled

Stop Bits:        Dynamic

Access:            Remote                  Local Switch:       None

Backward Switch:     None                  Name:            LC-3-16

Break:           Disabled                  Session Limit:         1

Forward Switch:      None                  Type:               ANSI

Dedicated Service:  DHCP

Authorized Groups:  0

(Current)  Groups:  0

Enabled Characteristics:

Autoprompt

**Create LAT Port**

MC LATCP CREAT PORT LTA9048 /NOLOG

MC LATCP SET PORT /NODE= DSVn /PORT=LC-n-n /NOLOG LTA9048

**Create VMS Terminal Characteristics/Protection**

$!VOICE1

$ SET PROTECT=W:RWLP /DEVICE LTA9048

$ SET TERM/PERM/NOWRAP/HOSTSYNC/NOECHO/EIGHT/NOBROAD/ALTYPE/PASTHRU LTA9048

**Create VISTA Device File Entries**

NAME: VOICE1                                  $I: \_LTA9048:

LOCATION OF TERMINAL: RADIOLOGY              MARGIN WIDTH: 80

FORM FEED: #,*27,*91,*50,*74,*27,*91,*72

PAGE LENGTH: 24                              BACK SPACE: $C(8)

SUBTYPE: C-VT100                            TYPE: TERMINAL

NAME: NULL DEVICE                           $I: \_NLA0:

LOCATION OF TERMINAL: NULL DEVICE         MARGIN WIDTH: 255

FORM FEED: #                              PAGE LENGTH: 256

BACK SPACE: $C(8)                         SUBTYPE: P-OTHER

TYPE: TERMINAL

## ## Appendix B

### Starting the HL7 Interface to Narcotic Dispensing Equipment

1.  Check to make sure an incoming and outgoing filer are running:

&gt; **D ^XUP**

Setting up programmer environment

Access Code: **XXXXXX**

Terminal Type set to: **C-VT100**

Select OPTION NAME: **HL7 MAIN MENU** HL7 Main Menu

Select HL7 Main Menu Option: **V1.6 OPTIONS**

Select V1.6 OPTIONS Option: **COMMUNICATIONS SERVER**

Select Communications Server Option: **6** Systems Link Monitor

MESSAGING MONITOR

MESSAGES  MESSAGES   MESSAGES  MESSAGES  DEVICE

NODE       RECEIVED  PROCESSED  TO SEND   SENT      ON-LINE  STATE

*{Depending on which protocol you selected for your interface, you will see*

*one of the following:}*

PSD HLLP   0         0          0         0            N     SHUTDOWN

PSD X3.2   0         0          0         0            N     SHUTDOWN

Number of incoming filers running =&gt; Zero

Number of outgoing filers running =&gt; Zero

TYPE: (N) NEXT, (B) BACKUP, (Q) QUIT: **&lt;RET&gt;**

If you do not have incoming and outgoing filer running, use the Start

Default number of incoming and outgoing filers option to do so:

Select Communications Server Option: **M** anage incoming &amp; outgoing filers

Select Manage incoming &amp; outgoing filers Option: **S** tart default number of incoming &amp; outgoing filers

Incoming filer queued as task number 392779

Outgoing filer queued as task number 392780

To insure that filers are running after a system shutdown, the following is

recommended:

&gt; **D P^DI**

VA FileMan 21.0

Select OPTION: **ENTER OR ED** IT FILE ENTRIES

INPUT TO WHAT FILE: OPTION// **&lt;RET&gt;**

EDIT WHICH FIELD: ALL// **SCHEDULING RECOMMENDED**

THEN EDIT FIELD: **&lt;RET&gt;**

Select OPTION NAME: **HL** START DEFAULT FILERS

Start default number of incoming &amp; outgoing filers

SCHEDULING RECOMMENDED: **S** STARTUP

Select OPTION NAME: **&lt;RET&gt;**

2.  Start the lower level protocol:

Select Communications Server Option: **START LLP**

This option is used to launch the lower level protocol for the

appropriate device.  Please select the node with which you want

to communicate

Select HL LOGICAL LINK NODE: **PSD**

1   PSD HLLP

2   PSD X3.28

*{Select the appropriate protocol for your interface vendor.}*

Select one of the following:

F         FOREGROUND

B         BACKGROUND

Q         QUIT

Method for running the receiver: B// **&lt;RET&gt;** ACKGROUND

Job was queued as 392781.

Select Communications Server Option: **&lt;RET&gt;**

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: Controlled Substances Version 3 Installation Guide (Updated PSD*3*89)

## Table of Contents

Table of Contents	3

1	Introduction	1

1.1	Dependencies	1

1.2	Constraints	1

2	Roles and Responsibilities	2

3	Deployment	3

3.1	Timeline	3

3.1.1	Deployment Topology	4

3.1.2	Site Information (Locations, Deployment Recipients)	4

3.1.3	Site Preparation	5

3.2	Resources	5

3.2.1	Facility Specifics	5

3.2.2	Hardware	5

3.2.3	Software	5

3.2.4	Communications	5

3.2.4.1 Deployment/Installation/Back-Out Checklist	5

4	Installation	6

4.1	Pre-installation and System Requirements	6

4.1.1	Pre/Post Installation Overview	6

4.2	Platform Installation and Preparation	6

4.3	Download and Extract Files	6

4.4	Database Creation	7

4.5	Installation Scripts	7

4.6	Cron Scripts	7

4.7	Access Requirements and Skills Needed for the Installation	7

4.8	Installation Procedure	7

4.8.1	Patch Verification	8

4.9	Post-Installation Instructions	8

4.10	Routine Information	8

4.11	Database Tuning	8

5	Back-Out Procedure	9

5.1	Back-Out Strategy	9

5.2	Back-Out Considerations	9

5.3	Back-Out Criteria	9

5.4	Back-Out Risks	9

5.5	Authority for Back-Out	9

5.6	Back-Out Procedure	9

6	Rollback Procedure	10

## Introduction

This document describes how to deploy and install the Pharmacy Inbound Electronic Prescription Controlled Substance v5.0 VistA Patch (PSD*3.0*89).

The purpose of this plan is to provide a single, common document that describes how, when, where, and to whom the IEP patch PSD*3.0*89 will be deployed and installed, as well as how  it is to be backed out and rolled back, if necessary. The plan also identifies resources, communications plan, and rollout schedule. Specific instructions for installation, back-out, and rollback are included in this document.

### Dependencies

Patch PSD*3.0*89 possesses a direct application dependency on the VistA Outpatient

Pharmacy (OP) v.7.0 application and Controlled Substance v3.0 application. Patches PSO*7*617, PSD*3*73, and PSD*3*83 are required  to be installed before PSD*3.0*89.

### Constraints

There are no constraints for patch PSD*3.0*89.

## Roles and Responsibilities

This section outlines the roles and responsibilities for managing the deployment of the patch PSD*3.0*89.

<!-- image -->

|   **ID** | **Team**                                                                                                                             | **Phase / Role**   | **Tasks**                                                                                                            | **Project Phase (See Schedule)**   |
|----------|--------------------------------------------------------------------------------------------------------------------------------------|--------------------|----------------------------------------------------------------------------------------------------------------------|------------------------------------|
|        1 | Field Operations (FO), Enterprise Operations (EO), or Enterprise Program Management Office (EPMO) (depending upon project ownership) | Deployment         | Plan and schedule deployment (including orchestration with vendors)                                                  | Deployment                         |
|        2 | FO, EO, or EPMO  (depending upon project ownership)                                                                                  | Deployment         | Determine and document the roles and responsibilities of those involved in the deployment.                           | Design/Build                       |
|        3 | FO, or EO                                                                                                                            | Deployment         | Test for operational readiness                                                                                       | Design/Build                       |
|        4 | FO or EO                                                                                                                             | Deployment         | Execute deployment                                                                                                   | Design/Build                       |
|        5 | FO or EO                                                                                                                             | Installation       | Plan and schedule installation                                                                                       | Deployment                         |
|        6 | Regional Project Manager (PM)/ Field Implementation Services (FIS)/ Office of Policy and Planning (OPP) PM                           | Installation       | Ensure authority to operate and that certificate authority security documentation is in place                        | Design/Build                       |
|        7 | Regional PM/FIS/OPP PM/ Nat’l Education & Training                                                                                   | Installations      | Coordinate training                                                                                                  | Deployment                         |
|        8 | FO, EO, or Product Development (depending upon project ownership)                                                                    | Back-out           | Confirm availability of back- out instructions and back-out strategy (what are the criteria that trigger a back-out) | Deployment                         |
|        9 | FO, EO, or Product Development (depending upon project ownership)                                                                    | Post Deployment    | Hardware, Software and System Support                                                                                | Maintenance                        |

## Deployment

Patch PSD*3.0*89 is being released as part of the Pharmacy Inbound Electronic Prescription Controlled Substance v5.0 enhancement along with patch PSO*7.0*617. Patches PSO*7.0*617 and PSD*3.0*89 will be distributed via the FORUM Patch Module and may be deployed at any site without regard to deployment status at other sites.

### Timeline

The deployment and installation is scheduled to run for a period of thirty days, as depicted in the Master Deployment Schedule.

**Table 2: Master Deployment Schedule**

| **VIP Build**   | **Delivery Dates**   |
|-----------------|----------------------|
| N/A             |                      |

#### Deployment Topology

Patch PSD*3.0*89 will be released to all VistA sites.

<!-- image -->

**Figure 1: Deployment Topology (Targeted Architecture)**

#### Site Information (Locations, Deployment Recipients)

During IOC testing, patch PSD*3.0*89 will be deployed at the following sites:

- VA Honolulu Regional Office
- Health Administration Center (Meds by Mail)
- Indianapolis, IN VA Medical Center
- Central Texas, Temple VA Medical Center Pharmacy
- Erie, PA VA Medical Center

PSD*3.0*89 will be delivered to the Information Technology (IT) support staff responsible for the VistA installation at those sites. The software will be installed in the IOC test and production environments.

After National Release, Patch PSD*3.0*89 will be deployed at all sites running the Outpatient Pharmacy v.7.0 application.

#### Site Preparation

To prepare for the site, patches: PSO*7*617, PSD*3*73, and PSD*3*83 are required to be installed before PSD*3.0*89.

### Resources

Deployment of Patch PSD*3.0*89 requires an up-to-date VistA environment running the

Controlled Substance v3.0 application, as well as designated IT support available to perform the patch installation.

#### Facility Specifics

There are no facility-specific deployment or installation features of patch PSD*3.0*89.

#### Hardware

Patch PSD*3.0*89 does not require additional hardware capabilities other than what is currently used by a VistA installation at the sites.

#### Software

The following table describes software specifications required at each site prior to deployment.

**Table 3: Software Specifications**

| **Required Software**   | **Make**   |   **Version** | **Configuration**   | **Manufacturer**   | **Other**   |
|-------------------------|------------|---------------|---------------------|--------------------|-------------|
| Outpatient Pharmacy     |            |             7 | Standard            | VHA                |             |
| Controlled Substance    |            |             3 | Standard            | VHA                |             |

Please see the Roles and Responsibilities table in Section 2 for details about who is responsible for preparing the site to meet these software specifications.

#### Communications

No notifications are required for deployment of patch PSD*3.0*89 other than the patch description released through Forum.

#### Deployment/Installation/Back-Out Checklist

Sites should fill out the table below indicating who performed an activity and when it was performed prior to installation.

**Table 4: Deployment/Installation/Back-Out Checklist**

| **Activity**                                                                                                                     | **Day**   | **Time**   | **Individual who completed task**   |
|----------------------------------------------------------------------------------------------------------------------------------|-----------|------------|-------------------------------------|
| Deploy -The Deploy activity is performed when the patch is sent to site(s) by the National Patch Module or Release Agent.        |           |            |                                     |
| Install - The Install activity is performed when the patch is installed at the site(s).                                          |           |            |                                     |
| Back-Out - The optional Back-Out activity is performed in the event the patch must be uninstalled, or removed, from the site(s). |           |            |                                     |

## Installation

### Pre-installation and System Requirements

Access to the National VA Network and to the local network of each site is required to perform the installation, as well as the authority to install patches.

#### Pre/Post Installation Overview

There are no pre-installation or post-installation steps for this patch.

### Platform Installation and Preparation

Patch PSD*3.0*89 does not require any platform installation or preparation.

### Download and Extract Files

The documentation, described in the table below, will be in the form of Adobe Acrobat files. Documentation can be found on the VA Software Documentation Library at: [http://www.va.gov/vdl/](http://www.va.gov/vdl/) . Documentation can also be found at REDACTED.

**Table 5: Installation Documentation**

| **Title**                                           | **File Name**                                         | **FTP Mode**   |
|-----------------------------------------------------|-------------------------------------------------------|----------------|
| CONTROLLED SUBSTANCES (CS) TECHNICAL MANUAL         | PSD\_3\_P89\_TM.docx  PSD\_3\_P89\_TM.pdf             | Binary         |
| CONTROLLED SUBSTANCES (CS) SUPERVISOR’S USER MANUAL | PSD\_3\_P89\_UM\_SUPV.docx  PSD\_3\_P89\_UM\_SUPV.pdf | Binary         |
| Release Notes                                       | PSD\_3\_P89\_RN.docx  PSD\_3\_P89\_RN.pdf             | Binary         |
| IG                                                  | PSD\_3\_P89\_IG.docx  PSD\_3\_P89\_IG.pdf             | Binary         |

### Database Creation

No new database is required for patch PSD*3.0*89.

### Installation Scripts

No installation scripts are required for installation of patch PSD*3.0*89.

### Cron Scripts

No Cron scripts are required for installation of patch PSD*3.0*89.

### Access Requirements and Skills Needed for the Installation

Access to the National VA Network and to the local network of each site to receive patch PSD*3.0*89 is required to perform the installation, as well as the authority to install patches.

Knowledge of, and experience with, the Kernel Installation and Distribution System (KIDS) software is required. For more information, see Section V, Kernel Installation and Distribution System, in the [Kernel 8.0 &amp; Kernel Toolkit 7.3 Systems Management Guide.](http://www.va.gov/VDL/documents/Infrastructure/Kernel/krn8_0sm.docx)

### Installation Procedure

This patch may be installed with users on the system, but it is recommended that it be installed during non-peak hours to minimize potential disruption to users. Staff should not be processing prescriptions while patch is being installed. This patch should take less than 5 minutes to install.

There are no Menu Options to disable.

1. Distribution Load:

Load the KIDS Distribution from the Packman Message using the Packman function "Install/Check Message."

1. From the Kernel Installation and Distribution System Menu, select

the Installation Menu.  From this menu, you may elect to use the

following options. When prompted for the INSTALL NAME enter:

PSD*3.0*89

1. Backup a Transport Global - This option will create a backup build of patch

components.  Respond “BUILD” at the “Select one of the following: B

Build or R Routines” prompt.   **THIS IS CRITICAL TO ACCURATE PATCH

BACKUP ON YOUR SYSTEM. **

1. Compare Transport Global to Current System - This option will allow you to view all

changes that will be made when this patch is installed.  It compares all components of this patch (routines, DDs, templates, etc.).

1. Verify Checksums in Transport Global - This option will allow you to ensure the

integrity of the routines that are in the  transport global.

1. KIDS Installation:
    - 1.1. Install the patch using the KIDS Installation Menu action

"Install Package(s)" and the install name PSD*3.0*89.

2. Respond "NO" at the "Want KIDS to INHIBIT LOGONs during the install?" prompt.
3. Respond "NO" at the "Want to DISABLE Scheduled Options,

Menu Options, and Protocols?" prompt.

4. The KIDs install should take less than 1 minute.

#### Patch Verification

Kernel Installation &amp; Distribution System-&gt; Utilities-&gt; Install. File Print option can be used to check for any errors plus the status of the install being Completed.

### Post-Installation Instructions

There are no post-installation steps for this patch.

### Routine Information

The second line of each of these routines now looks like:

;;3.0;CONTROLLED SUBSTANCES;**[Patch List]**;Feb 13,1997;Build 18

The checksums below are new checksums, and

can be checked with CHECK1^XTSUMBLD.

Routine Name: PSDDSOR

Before: B86052358   After:B114292387  **40,42,45,67,73,89**

Routine Name: PSDDSOR1

Before: B34383843   After: B41609547  **40,67,73,83,89**

Routine Name: PSDDSOR2

Before: B23181227   After: B68638251  **40,42,45,73,89**

### Database Tuning

No database tuning is required before or after deployment of PSD*3.0*89.

**NOTE:** Installation of PSD*3.0*89 is completed. The following procedure is to be followed only if PSD*3.0*89 needs to be backed out.

<!-- image -->

**NOTE:** Due to the complexity of this patch (because of the data dicionarges), it is not recommended for back-out. However, in the event that a site decides to back-out this patch, the site should contact the NSD at 855-NSD-HELP (673-4357) and reference “Inbound eRx” to submit a YourIT ServiceNow ticket; the development team will assist with the process.

<!-- image -->

### Back-Out Strategy

The development team recommends that sites log a help desk ticket if it is a nationally released patch; otherwise, the site should contact the product development team directly for specific

solutions to their unique problems.

### Back-Out Considerations

The back-out should only be done if the local facility management determines that the Patch PSD*3.0*89 is not appropriate for that facility and should only be done as a last resort.

### Back-Out Criteria

Local Facility Management would need to determine patch PSD*3.0*89 is not appropriate for their facility.

### Back-Out Risks

By backing out PSD*3.0*89, the local facility will not have the use of enhanced report features for eRx controlled substance prescriptions.

### Authority for Back-Out

Local Facility Management has the authority to back-out patch PSD*3.0*89.

### Back-Out Procedure

The Back-out Procedure consists of restoring the routines introduced by the Patch PSD*3.0*89. Ensure the ‘Backup a Transport Global’ step in section 4.8 of this document is followed, so a backup of all the routines is available.

The backout procedure for this patch should only occur when there is concurrence from the Enterprise Product Support and Inbound ePrescribing development teams, because of

the complexity and risk involved in a backout. Normal installation back-up using KIDS  will back up only Mumps routines. For all non-routine components of this build, Enterprise Product Support will have a build available if needed.

The back-out is to be performed by persons with programmer-level access.

## Rollback Procedure

There is no data associated with patch PSD*3.0*89.
