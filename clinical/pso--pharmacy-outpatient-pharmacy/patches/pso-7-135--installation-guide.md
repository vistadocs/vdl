---
title: PSO*7*135 ScripTalk Talking Prescription Labels Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: ScripTalk Talking Prescription Labels
app_code: PSO
app_name: "Pharmacy: Outpatient Pharmacy"
section: CLI
app_status: archive
pkg_ns: PSO
patch_ver: 7
patch_id: PSO*7*135
group_key: "PSO:PSO:7"
file_numbers: []
security_keys: []
menu_options: 0
description: The purpose of this Installation Guide is to provide an explanation of the installation process for the ScripTalk talking prescription labels software. The intended audience for this document is the Information Resources Management Service (IRMS) staff and Pharmacy staff responsible for installing
audience: 
keywords: 
  - scriptalk
  - device
  - install
  - label
  - pssjxr
  - installation
  - printer
  - contents
  - print
  - table
page_count: 0
word_count: 2599
section_count: 1
table_count: 3
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: November 2003
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy_Archive/pso_7_p135_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy_Archive/pso_7_p135_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=394"
---

> ![](pso-7-135-scriptalk-talking-prescription-labels-installation-guide/001.png)

SCRIPTALK TALKING PRESCRIPTION LABELS

######### 

######### INSTALLATION GUIDE

November 2003

PSS\*1\*72

PSO\*7\*135

V*IST*A Health Systems Design & Development

# Preface


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Preface](#preface)
- [Purpose](#purpose)
- [Scope](#scope)
- [Minimum Required Packages](#minimum-required-packages)
- [Required Patches](#required-patches)
- [Installation](#installation)
- [Installation Steps](#installation-steps)
- [Printer Installation](#printer-installation)
- [Testing ScripTalk](#testing-scriptalk)
<span class="mark">REDACTED</span>Veterans Affairs (VA) Medical Center’s Blind Rehabilitation Center (BRC) investigated En-Vision America’s ScripTalk program for a class III solution at their facility. (ScripTalk is a registered trademark of En-Vision America.). Their findings have provided the basis for this project and allowed ScripTalk services to be offered at other VA Medical Centers. We would like to thank <span class="mark">REDACTED</span>, for his extensive research and development work.
\<This page is intentionally left blank.\>
Table of Contents
\<This page is intentionally left blank.\>

# Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this Installation Guide is to provide an explanation of the installation process for the ScripTalk talking prescription labels software. The intended audience for this document is the Information Resources Management Service (IRMS) staff and Pharmacy staff responsible for installing and maintaining the Pharmacy files.

The ScripTalk project includes the installation of the PSS\*1\*72 and PSO\*7\*135 patches. Following the installation of these patches, patients can be ‘enrolled’ as ScripTalk patients and will be able to receive specially encoded labels on their medication containers. This will provide patients with substantial loss of vision a means of safely determining the contents and administration schedules of their medications.

# Scope

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span class="mark">REDACTED</span> Pharmacy Service, <span class="mark">REDACTED</span>VA Medical Center requested to convert ScripTalk class III software, that generates prescription labels with speech synthesized patient information, to class I software. This project will help increase a patient’s (individuals with visual impairments, dyslexia, and reading problems) ability to comply with their doctor’s orders. Audible prescription information also reduces prescription errors thereby reducing hospital/emergency room visits.

While installation of these patches is required, the use of the ScripTalk equipment is not mandated. If the site chooses to use this equipment, the ScripTalk Talking Prescription printers, readers and supplies can be purchased on <span class="mark">REDACTED</span>. En-Vision America can be reached via telephone at (309) 452-3088. Use of this printer will also require the “open-market” purchase of a micro print server. En-Vision America can help in determining which print server is needed. Many larger suppliers of computer hardware carry these print servers.

Using the ScripTalk Talking Prescriptions involves the installation of a specialty printer that prints to microchip-embedded label stock. The label will have printed text on it, along with the microchip containing the contents of the label. Pharmacy or other designated staff will enroll patients to receive these labels and issue those patients a special reader. When the patient holds a ScripTalk label near the reader and presses a button, the content of the label is read aloud.

\<This page is intentionally left blank.\>

# Minimum Required Packages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ScripTalk project will operate on standard hardware platforms used by the VHA facilities and require the following Department of Veterans Affairs (VA) software packages to support the enhancements requested.

|                          |                            |
|--------------------------|----------------------------|
| Package              | Minimum Version Needed |
|                          |                            |
| VA FileMan               | 22.0                       |
| Kernel                   | 8.0                        |
| MailMan                  | 8.0                        |
| Outpatient Pharmacy      | 7.0                        |
| Pharmacy Data Management | 1.0                        |

The above software is not included in this Patch and must be installed for this Patch to be completely functional.

\<This page is intentionally left blank.\>

# Required Patches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Prior to the installation of the ScripTalk Talking Prescription Labels patches, the following patches must be installed:

Outpatient Pharmacy V. 7.0

PSO\*7\*139

PSO\*7\*141

Pharmacy Data Management V. 1.0

PSS\*1\*72

![](pso-7-135-scriptalk-talking-prescription-labels-installation-guide/002.png)Note: PSS\*1\*72 and PSO\*7\*135 together accomplish the functionality required in the ScripTalk project. However, PSS\*1\*72 must be installed before PSO\*7\*135 as it sets up the data dictionary for the ScripTalk enrollees.

# Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For all facilities installing PSS\*1\*72 and PSO\*7\*135, Outpatient Pharmacy V. 7.0 users should be off the system while installing the patches.

![](pso-7-135-scriptalk-talking-prescription-labels-installation-guide/003.png)Note: It is recommended that PSS\*1\*72 and PSO\*7\*135 be installed during non-peak hours.

Sites will retrieve V*IST*A documentation from the following FTP addresses. The preferred method is to FTP the files from <span class="mark">REDACTED</span>. This transmits the files from the first available FTP server. Sites may also elect to retrieve software directly from a specific server as follows.

<u>OI Field Office</u> <u>FTP Address</u> <u>Directory</u>

<span class="mark">REDACTED</span>

Installation should take less than 5 minutes.

\<This page is intentionally left blank.\>

# Installation Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Install patch PSS\*1\*72 following the example displayed below. All user inputs are displayed in a bold font within the example.

Example: PSS\*1\*72 Install Process

Select Installation Option: 6 Install Package(s)

Select INSTALL NAME: PSS\*1.0\*72 Loaded from Distribution 10/14/03@13:54:30

=\> PSS\*1\*72

This Distribution was loaded on Oct 14, 2003@13:54:30 with header of

PSS\*1\*72

It consisted of the following Install(s):

PSS\*1.0\*72

Checking Install for Package PSS\*1.0\*72

Install Questions for PSS\*1.0\*72

Incoming Files:

55 PHARMACY PATIENT (Partial Definition)

> **NOTE:** You already have the 'PHARMACY PATIENT' File.

Want KIDS to INHIBIT LOGONs during the install? YES// NO

Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// NO

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// \<Enter\>

Install Started for PSS\*1.0\*72 :

Oct 14, 2003@15:04:13

Build Distribution Date: Jul 23, 2003

Installing Routines:

Oct 14, 2003@15:04:13

Installing Data Dictionaries:

Oct 14, 2003@15:04:15

Updating Routine file...

The following Routines were created during this install:

PSSJXR

PSSJXR1

PSSJXR10

PSSJXR11

PSSJXR12

PSSJXR13

PSSJXR14

PSSJXR15

PSSJXR16

PSSJXR17

PSSJXR18

PSSJXR19

PSSJXR2

-----------------------------------------report continues----------------------------------------

Example: PSS\*1\*72 Install Process (continued)

PSSJXR20

PSSJXR21

PSSJXR22

PSSJXR23

PSSJXR24

PSSJXR25

PSSJXR26

PSS\*1.0\*72

--------------------------------------------------------------------------------

PSSJXR27

PSSJXR28

PSSJXR3

PSSJXR4

PSSJXR5

PSSJXR6

PSSJXR7

PSSJXR8

PSSJXR9

Updating KIDS files...

PSS\*1.0\*72 Installed.

Oct 14, 2003@15:04:16

Install Message sent \# 150570

--------------------------------------------------------------------------------

\[------------------------------------------------------------\]

100% \| 25 50 75 \|

Complete \[------------------------------------------------------------\]

Install Completed

2.  Install patch PSO\*7\*135 following the example displayed below. All user inputs are displayed in a bold font within the example.

Example: PSO\*7\*135 Install Process

Select Installation Option: 6 Install Package(s)

Select INSTALL NAME: PSO\*7.0\*135 Loaded from Distribution 10/14/03@13:55:50

=\> PSO\*7\*135

This Distribution was loaded on Oct 14, 2003@13:55:50 with header of

PSO\*7\*135

It consisted of the following Install(s):

PSO\*7.0\*135

Checking Install for Package PSO\*7.0\*135

Install Questions for PSO\*7.0\*135

Incoming Files:

59 OUTPATIENT SITE (Partial Definition)

> **NOTE:** You already have the 'OUTPATIENT SITE' File.

Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES// NO

Want KIDS to INHIBIT LOGONs during the install? YES// NO

Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// NO

-----------------------------------------report continues----------------------------------------

  
Example: PSO\*7\*135 Install Process (continued)

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// \<Enter\>

Install Started for PSO\*7.0\*135 :

Oct 14, 2003@15:09:56

Build Distribution Date: Oct 08, 2003

Installing Routines:

Oct 14, 2003@15:09:56

PSO\*7.0\*135

--------------------------------------------------------------------------------

Installing Data Dictionaries:

Oct 14, 2003@15:09:57

Installing PACKAGE COMPONENTS:

Installing OPTION

Oct 14, 2003@15:09:59

Updating Routine file...

Updating KIDS files...

PSO\*7.0\*135 Installed.

Oct 14, 2003@15:09:59

Install Message sent \# 150572

--------------------------------------------------------------------------------

\[------------------------------------------------------------\]

100% \| 25 50 75 \|

Complete \[------------------------------------------------------------\]

Install Completed

# Printer Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](pso-7-135-scriptalk-talking-prescription-labels-installation-guide/004.png)Note: The ScripTalk printer installation and set up procedures are <u>also</u> located in the Outpatient Pharmacy V. 7.0 Technical Manual / Security Guide under the Barcodes and Label Printer Support section.

The TCP/IP-enabled printer must be physically connected to the network and then defined in the DEVICE (#3.5) and TERMINAL TYPE (#3.2) files. To connect the printer to the network, a micro print server is necessary for communication to V*IST*A. En-Vision America can assist in identifying the micro print server necessary for the site.

The following are examples of the file set-ups. These examples are provided to guide the user in this set up. Please note that these are only examples and there will be some differences in the settings.

Example: DEVICE File (#3.5) Set Up

NAME: WP706 \$I: USER\$:\[DSM_SPOOL\]WP706.TXT

LOCATION OF TERMINAL: ScripTalk ASK HOST FILE: NO

ASK HFS I/O OPERATION: NO BARCODE AVAIL: YES

OPEN PARAMETERS: (NEWVERSION,PROTECTION=(S:RWED,O:RWED,W:RWED))

SUBTYPE: P-ZEBRA-PHARM

Example: TERMINAL TYPE File (#3.2) Set Up

NAME: P-ZEBRA-PHARM SELECTABLE AT SIGN-ON: NO

RIGHT MARGIN: 132 FORM FEED: \#

PAGE LENGTH: 64 BACK SPACE: \$C(8)

CLOSE EXECUTE: U IO K IO(1,IO) S IO=\$ZIO C IO S

QUE="/QUEUE="\_\$E(ION,1,6)\_"/DELETE",QUE=\$ZC(%PRINT,IO,QUE)

NUMBER: 1 CTRL CODE ABBREVIATION: FI

FULL NAME: FORMAT INITIALIZATION CONTROL CODE: W "^XA",!,"^LH30,60^FS",!

NUMBER: 2 CTRL CODE ABBREVIATION: SB

FULL NAME: START OF BARCODE

CONTROL CODE: W "^BY2,3.0^FO70,25^B3N,N,80,Y,N"

NUMBER: 3 CTRL CODE ABBREVIATION: ST

FULL NAME: START OF TEXT

CONTROL CODE: W "^FO",PSJBARX,",",PSJBARY,"^A0N,30,20" S PSJBARY=PSJBARY+40

NUMBER: 6 CTRL CODE ABBREVIATION: EB

FULL NAME: END OF BARCODE CONTROL CODE: S LINE=LINE+1,PSJBARY=130

NUMBER: 7 CTRL CODE ABBREVIATION: STF

FULL NAME: START OF TEXT FIELD CONTROL CODE: W "^FD"

NUMBER: 8 CTRL CODE ABBREVIATION: SBF

FULL NAME: START OF BARCODE FIELD CONTROL CODE: W "^FD"

NUMBER: 9 CTRL CODE ABBREVIATION: ETF

FULL NAME: END OF TEXT FIELD CONTROL CODE: W "^FS",!

NUMBER: 10 CTRL CODE ABBREVIATION: SL

FULL NAME: START OF LABEL

CONTROL CODE: W "^XA",! S PSJBARY=50,PSJBARX=60

NUMBER: 11 CTRL CODE ABBREVIATION: EL

FULL NAME: END OF LABEL CONTROL CODE: W "^XZ",!

NUMBER: 12 CTRL CODE ABBREVIATION: EBF

FULL NAME: END OF BARCODE FIELD CONTROL CODE: W "^FS",!

# Testing ScripTalk

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once the ScripTalk printer is installed and connected to the network server, it will need to be defined for the division where it will be used and whether the labels should be automatically printed or will be queued for manual print. From the *ScripTalk Main Menu* option, choose the *Set Up and Test ScripTalk Device* option and then choose the *ScripTalk Device Definition Enter/Edit* option.

Example: Defining the ScripTalk Printer

Select ScripTalk Main Menu Option: ?

PT ScripTalk Patient Enter/Edit

QBAR Queue ScripTalk Label by Barcode

QRX Queue ScripTalk Label by Rx#

RPT ScripTalk Reports ...

Reprint a non-voided Outpatient Rx Label

PARM Set Up and Test ScripTalk Device ...

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select ScripTalk Main Menu Option: PARM Set Up and Test ScripTalk Device

Select Set Up and Test ScripTalk Device Option: ?

ScripTalk Device Definition Enter/Edit

Print Sample ScripTalk Label

Test ScripTalk Device

Reinitialize ScripTalk Printer

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select Set Up and Test ScripTalk Device Option: SCripTalk Device Definition Ente

r/Edit

Division: TROY 514

SCRIPTALK DEVICE: ?

Enter ScripTalk Device.

Answer with DEVICE NAME, or LOCAL SYNONYM, or \$I, or VOLUME SET(CPU), or

SIGN-ON/SYSTEM DEVICE, or FORM CURRENTLY MOUNTED

Do you want the entire DEVICE List? N (No)

SCRIPTALK DEVICE: S

1 SCRIPT\$PRT SPECIAL PRINTER USER\$:\[TCP\$SPOOL\]SCRIPT\$PRT.TXT

2 SPOOL COMPUTER ROOM 2

3 SYS..//./nul CONSOLE - CROOM PAA CONSOLE C-ROOM //./nul

4 SYS..100 PAA100 100

5 SYS..3 PAA3 3

Press \<RETURN\> to see more, '^' to exit this list, OR

CHOOSE 1-5: 1 SCRIPT\$PRT SPECIAL PRINTER USER\$:\[TCP\$SPOOL\]SCRIPT\$PRT.TXT

SCRIPTALK AUTO-PRINT SETTINGS: ?

Enter 'A' if ScripTalk label printing should be automatic, "M" if label

will be queued manually.

Choose from:

A AUTO PRINT

M MANUAL PRINT

SCRIPTALK AUTO-PRINT SETTINGS: A AUTO PRINT

After the printer is defined, a sample ScripTalk label can be generated. From the *ScripTalk Main Menu* option, choose the *Set Up and Test ScripTalk Device* option and then choose the *Print Sample ScripTalk Label* option.

Example: Printing a sample ScripTalk Label

Select Set Up and Test ScripTalk Device Option: PRint Sample ScripTalk Label

The following test data will be sent to the ScripTalk printer:

^XA

^FO250,700^XGE:RX.GRF^FS

^FO250,700^XGE:RX.GRF^FS

^AFR,20,10^FO531,50^FR^CI0^FD7305 N. MILITARY TRL Exp: January 01,2002^FS

^AFR,20,10^FO503,50^FR^CI0^FDRX#82382787 January 01,2001 Fill 01 OF 01^FS

^AFR,20,10^FO475,50^FR^CI0^FDONE OPPATIENT^FS

^AFR,20,10^FO447,50^FR^CI0^FDTAKE 1 CAPSULE THREE TIMES DAILY^FS

^AFR,20,10^FO419,50^FR^CI0^FD^FS

^AFR,20,10^FO391,50^FR^CI0^FD^FS

^AFR,20,10^FO363,50^FR^CI0^FD^FS

^AFR,20,10^FO335,50^FR^CI0^FDTWO OPPROVIDER MD^FS

^AFR,20,10^FO279,50^FR^CI0^FDQTY: 24 TABS^FS

^AFR,20,10^FO251,50^FR^CI0^FDAMOXICILLIN 500MG CAP^FS

^RX01,ONE OPPATIENT^FS

^RX02,AMOXICILLIN 500MG CAP^FS

^RX03,TAKE 1 CAPSULE THREE TIMES DAILY ^FS

^RX04,010101^FS

^RX05,00^FS

^RX06,020000^FS

^RX07,TWO OPPROVIDER^FS

^RX08,2925553888^FS

^RX09,82382787^FS

^RX10, ^FS

^PQ1,0,1,Y

^XZ

Task Queued !

Select Set Up and Test ScripTalk Device Option:

If the printer did not print the label, check to make sure that the printer is closed very tightly. It may not have been closed completely after loading the labels.

If the printer printed a blank label or one that is extremely faint, reinitialize the printer. Then try printing the sample label again.

Example: Reinitializing the Printer

Select Set Up and Test ScripTalk Device Option: ?

ScripTalk Device Definition Enter/Edit

Print Sample ScripTalk Label

Test ScripTalk Device

Reinitialize ScripTalk Printer

Enter ?? for more options, ??? for brief descriptions, ?OPTION for help text.

Select Set Up and Test ScripTalk Device Option: REinitialize ScripTalk Printer

Task Queued !

The *Test ScripTalk Device* option can be used to send one Zebra Print Language (ZPL) test string to the ScripTalk printer.

Once a test label is printed, it is ready to be read by the reader. To read the label, place it near the face of the reader and hit the round power button on the reader. A series of ticks will be heard as the reader finds and retrieves the information on the label. Then the reader will begin speaking.

![](pso-7-135-scriptalk-talking-prescription-labels-installation-guide/005.png)Note: The pharmacy should check each ScripTalk label for accuracy using the reader. The printer encodes the chip while printing the label, but nothing in or attached to V*IST*A can see or tell if the label is valid.

Next, test patients can be enrolled as ScripTalk patients. Choose the *ScripTalk Patient Enter/Edit* option from the *ScripTalk Main Menu* option.

Example: Enrolling a ScripTalk Patient

Select ScripTalk Main Menu Option: PT ScripTalk Patient Enter/Edit

Select PATIENT: OP

1 OPPATIENT,ONE 03-04-54 000456789 SC VETERAN

2 OPPATIENT,TWO 03-20-92 000123456 NON-VETERAN (OTHER)

CHOOSE 1-2: 1 OPPATIENT,ONE 03-04-54 000456789 SC VETERAN

SCRIPTALK PATIENT? N// YES

> **REMINDER:** CMOP does not fill ScripTalk prescriptions. Please select mail

status: 2 (DO NOT MAIL), 3 (LOCAL REGULAR MAIL) or 4 (LOCAL CERTFIED MAIL).

MAIL: 2 DO NOT MAIL

Select one of the following:

B BLIND VETERAN

L LOW VISION

INDICATION: // BLIND VETERAN

Select PATIENT:

![](pso-7-135-scriptalk-talking-prescription-labels-installation-guide/006.png)Note: The “MAIL:” prompt above is only displayed when the patient is set to a Consolidated Mail Outpatient Pharmacy (CMOP) status or does not have a mail status defined.

A progress note can be automatically placed in the ScripTalk patient’s chart to be signed when that patient is enrolled. To invoke this feature, ask the Text Integration Utility/Computerized Patient Record System (TIU/CPRS) coordinator at the site to create a note entitled “SCRIPTALK ENROLLMENT”. The note contents will be “*Patient Name* was enrolled in ScripTalk today, and is now eligible to receive prescriptions with encoded speech-capable labels.”

Once the device is hooked up and ‘talking’, any of the other *ScripTalk Main Menu* options can be chosen. If the device is defined for auto-print, and some patients are defined as ScripTalk patients, then whenever a V*IST*A label is queued, if the prescription belongs to a ScripTalk patient, a ScripTalk label should print at the same time.

For more information regarding the use of ScripTalk, please refer to the Outpatient Pharmacy V. 7.0 User Manual.