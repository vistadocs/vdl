---
title: "LA*5.2*12 Laboratory: Universal Interface VITEK Literal Interface Document"
doc_type: INT
doc_label: Interface Specification
doc_layer: patch
doc_subject: "Laboratory: Universal Interface VITEK Literal Interface Document"
app_code: LA
app_name: "Laboratory: Universal Interface"
section: CLI
app_status: active
pkg_ns: LA
patch_ver: 5.2
patch_id: LA*5.2*12
group_key: "LA:LA:5.2"
file_numbers: []
security_keys: []
menu_options: 0
description: Approximately 50 VAMC facilities have purchased the bioMerieux Vitek Analyzer to perform automated microbiology laboratory testing. The bioMerieux Vitek Analyzer performs bacterial identification and susceptibility profiles. The main benefit from having an interface from the analyzer to a Laboratory
audience: 
keywords: 
  - vitek
  - table
  - code
  - contents
  - laboratory
  - instrument
  - dhcp
  - entry
  - organism
  - installation
page_count: 0
word_count: 5251
section_count: 19
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: April 1996
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Lab-Universal_Interface/vitek_la52_12_doc.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Lab-Universal_Interface/vitek_la52_12_doc.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=120"
---

Decentralized Hospital Computer Program

LABORATORY VITEK LITERALINTERFACE LA\*5.2\*12 PATCHDOCUMENTATION

April 1996

Information Resources Management Field Office

Birmingham, Alabama

# Preface


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Preface](#preface)
- [Introduction](#introduction)
  - [New Features:](#new-features)
  - [References:](#references)
  - [Documentation Notations:](#documentation-notations)
  - [Keywords and Phrases:](#keywords-and-phrases)
- [Pre-Installation Information](#pre-installation-information)
  - [Staffing Resources:](#staffing-resources)
  - [Test Account:](#test-account)
  - [Routines:](#routines)
  - [Disk Space:](#disk-space)
  - [## New Globals:](#new-globals)
  - [DHCP Software Requirements:](#dhcp-software-requirements)
  - [Installation Requirements:](#installation-requirements)
  - [Vitek Computer Requirements:](#vitek-computer-requirements)
  - [New Vitek Options:](#new-vitek-options)
  - [New DHCP Files:](#new-dhcp-files)
    - [MICRO INSTRUMENT SET-UP file (#61.38)](#micro-instrument-set-up-file-6138)
    - [LABORATORY INSTRUMENT CODE (LIC) file (#61.39](#laboratory-instrument-code-lic-file-6139)
- [LA\5.2\12 Patch Implementation Checklist](#la5212-patch-implementation-checklist)
  - [VITEK to DHCP Laboratory System Interface (LSI) Cable Wiring](#vitek-to-dhcp-laboratory-system-interface-lsi-cable-wiring)
- [bioMerieux Vitek Computer Setup](#biomerieux-vitek-computer-setup)
  - [Ports Setup](#ports-setup)
  - [Protocol Setup](#protocol-setup)
- [# LA\5.2\12 Patch Installation](#la5212-patch-installation)
- [Post-Installation Information](#post-installation-information)
  - [## ## Laboratory Microbiology Staff](#laboratory-microbiology-staff)
    - [Print DHCP and Vitek Code Entries](#print-dhcp-and-vitek-code-entries)
    - [Editing DHCP Files](#editing-dhcp-files)
    - [The DHCP ENTRY comes from the ETIOLOGY FIELD file (#61.2). The VITEK ENTRY originally comes from the VITEK and is loaded into ETIOLOGY FIELD file (#61.2) by the installation process. If there is a match to the VITEK entry in the ETIOLOGY FIELD file (#61.2) then the LOCAL ORGANISM ENTRY is filled in. A number in the LOCAL ORGANISM ENTRY is not valid; and indicates there was no match or more than one match which could not be resolved. If the organism is one you isolate then decide which entry in the ETIOLOGY FIELD file (#61.2). matches the Vitek entry. If there is no Etiology entry then you must create one and it has to have a SNOMED code. Follow the instructions in the Microbiology Section of the Lab documentation for Etiology File Entries.](#the-dhcp-entry-comes-from-the-etiology-field-file-612-the-vitek-entry-originally-comes-from-the-vitek-and-is-loaded-into-etiology-field-file-612-by-the-installation-process-if-there-is-a-match-to-the-vitek-entry-in-the-etiology-field-file-612-then-the-local-organism-entry-is-filled-in-a-number-in-the-local-organism-entry-is-not-valid-and-indicates-there-was-no-match-or-more-than-one-match-which-could-not-be-resolved-if-the-organism-is-one-you-isolate-then-decide-which-entry-in-the-etiology-field-file-612-matches-the-vitek-entry-if-there-is-no-etiology-entry-then-you-must-create-one-and-it-has-to-have-a-snomed-code-follow-the-instructions-in-the-microbiology-section-of-the-lab-documentation-for-etiology-file-entries)
    - [Vitek Literal Verification Process](#vitek-literal-verification-process)
- [Troubleshooting](#troubleshooting)
The Decentralized Hospital Computer Program (DHCP) Laboratory Literal Vitek Interface LA\*5.2\*12 Patch Documentation is designed to provide the Department of Veterans Affairs Medical Center (DVAMC), Information Resources Management Service (IRM), and the Laboratory Microbiology Staff with the necessary technical information required to efficiently and effectively implement, maintain, and manage the bi-directionally literal interface and the Vitek Automated Instrument to DHCP through the Laboratory System Interface (LSI). The LA\*5.2\*12 Patch Documentation also provides sufficient information about DHCP downloading data to Vitek and Vitek uploading data to DHCP.
Table of Contents
Introduction
New Features:
References:
Documentation Notations:
Keywords and Phrases:
Pre-Installation Information
Staffing Resources:
Test Account:
Routines:
Disk Space:
New Globals:
DHCP Software Requirements:
Installation Requirements:
Vitek Computer Requirements:
New Vitek Options:
New DHCP Files:
MICRO INSTRUMENT SET-UP file (#61.38)
LABORATORY INSTRUMENT CODE (LIC) file (#61.39
LA\*5.2\*12 Patch Implementation Checklist
VITEK to DHCP Laboratory System Interface (LSI) Cable Wiring
bioMerieux Vitek Computer Setup
Ports Setup
Protocol Setup
LA\*5.2\*12 Patch Installation
Post-Installation Information
Laboratory Microbiology Staff
Print DHCP and Vitek Code Entries
Editing DHCP Files
LABORATORY INSTRUMENT CODE FILE file (#61.39)
LOAD/WORK LIST file (#68.2)
AUTO INSTRUMENT file (#62.4)
MICRO INSTRUMENT SET-UP file (#61.38)
Vitek Literal Verification Process
Troubleshooting

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Approximately 50 VAMC facilities have purchased the bioMerieux Vitek Analyzer to perform automated microbiology laboratory testing. The bioMerieux Vitek Analyzer performs bacterial identification and susceptibility profiles. The main benefit from having an interface from the analyzer to a Laboratory Information System (LIS) is the improvement in overall efficiency of information handling. Data processed on the bioMerieux Vitek and in the DHCP Laboratory Database can be transferred electronically between both computer systems quickly and more efficiently than manual transfers. Manual data entry is not only labor intensive, but prone to transcription errors.

The bioMerieux Vitek has been interfaced to the DHCP Laboratory software for several years in the uni-directional and bi-directional modes. Previously the data stream from the bioMerieux Vitek was encoded, that is, the data coded is in a non human readable format.

Within the last five years bioMerieux Vitek released a new version of software using a literal interface (Literal PRM). In the last couple of years bioMerieux has introduced an additional software update, the bioLiaison incorporating the Literal PRM Interface with Graphical User Interface or GUI Version. The interface that is included in this update can be used with both the bioMerieux Vitek Literal PRM mode and the bioLiaison GUI Version. The bioMerieux Vitek, Inc., has indicated that the newer updates will be for the Literal PRM Interface or GUI version, not the encoded interface. There will be some updating of the encoded interface but eventually will be phased out.

This project encompasses all necessary activities involved with the interfacing of the bioMerieux Vitek automated microbiology analyzer to DHCP Laboratory software. These activities include:

Transmission of DHCP data to the bioMerieux Vitek analyzer in a format which is acceptable to the Vitek

Accepting result data as it is transmitted from the bioMerieux Vitek and interpreting the result data

Presenting the result data to DHCP Laboratory software in a format suitable for user verification of tests results

## New Features:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The DHCP Laboratory Vitek Literal Interface includes a Translation Table file, LABORATORY INSTRUMENT CODE (LIC) file (#61.39). The LIC file (#61.39) replaces the entries in the card entries that are stored in the AUTO INSTRUMENT file (#62.4).

The MICRO INSTRUMENT SET-UP file (#61.38) provides the site greater flexibility for setting up wild cards fields for the download, and whether to enable the LABORATORY TEST file (#60) culture ID Prefix Field.

## References:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Bidirectional Computer Interface Specification for bioLiaison Vitek, Part Number 510703-1, bioMerieux Vitek, 595 Anglum Drive, Hazelwood, MO. 63042-2395, Phone: 314-731-8500, Fax: 314-731-8800.

Bidirectional Computer Interface Operator’s Manual, 510710-1, REV 1094 bioMerieux Vitek, 595 Anglum Drive, Hazelwood, MO. 63042-2395, Phone: 314-731-8500, Fax: 314-731-8800.

DHCP Laboratory Technical Manual, V. 5.2, October 1994, pp. 114-143, Dept. of Veterans Affairs (DVA), Veterans Health Administration (VHA), Office of the Chief Information Officer (OCIO)

## Documentation Notations:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Computer dialogue appears in Courier font, no larger than 10 points.

Example: (Courier font 10 points).

User response appears in boldface type Courier font, no larger than 10 points.

After users have completed entering information the \<RET\> symbol appears in

boldface type.

The <u>underline</u> appears when a user’s response is required.

## Keywords and Phrases:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ASCII Control characters: ENQ, ACK, NAK, and EOT.

Bi-directional Computer Interface (BCI): Facilitates the exchange of data between the computer in a bioMerieux Vitek instrument and the DHCP computer.

bioLiaison (LSN): Refers to the Vitek patient database software.

Download: The process by which information is transferred from the host computer to the automated instrument.

Firmware: Broadly, the system software permanently stored in a computer’s read-only memory (ROM) or elsewhere in the computer’s circuitry. Firmware cannot be modified by the user.

LIS: Laboratory Information System

LSI: Laboratory System Interface

Session: Consists of a connection between the Vitek and the host to exchange information. A session can take place in only one direction at a time, where the initiator is the master and the other is the slave. ENQ initiates while EOT ends the communication/message.

Translation Table: Programming that converts data from one system to another facilitating electronic communication.

Upload: The transfer of information from the automated instrument to the host computer.

Vitek Literal Interface Software: Facilitates the exchange of data between the computer in a bioMerieux Vitek instrument and the DHCP computer.

# Pre-Installation Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section of the documentation provides pre-installation information that is necessary to ensure a successful installation of the LA\*5.2\*12 patch and implementation of the DHCP Laboratory Vitek Literal Interface.

## Staffing Resources:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. Personnel with VA FileMan capabilities are required for editing the following files:

> a\) ANTIMICROBIAL SUSCEPTIBILITY file (#62.06)

> b\) AUTO INSTRUMENT file (#62.4)

> c\) LOAD/WORK LIST file (#68.2)

> d\) ETIOLOGY FIELD file (#61.2)

> e\) LABORATORY INSTRUMENT CODE file (#61.39)

> f\) MICRO INSTRUMENT SET-UP file (#61.38)

2\. Personnel required for wiring Vitek cable to the LSI.

3\. Personnel required to setup port and protocol on the Vitek.

## Test Account:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A test account is not applicable due to the data required for testing. It is highly recommended to set up a Test Patient in your live account for data verification.

## Routines:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

LAMIVTL0 (Verification) LAMIVTLC (LAH Builder)

LAMIVTL1 (Verification) LAMIVTLP (LA Parser)

LAMIVTL2 (Verification) LAMIVTLX (Handshake)

LAMIVTL3 (Verification) LAMIVTLG (New LAGEN)

LAMIVTL4 (Verification) LAMIVTLD (Download Routine)

LAMIVTL5 (Verification) LAMIVTLB (Pre-Inits)

LAMIVTL6 (Verification) LAMIVTLE (Post-Inits)

## Disk Space:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Minimal</u> disk space growth will occur from the installation of the LA\*5.2\*12 patch.

## ## New Globals:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

MICRO INSTRUMENT SET-UP file (#61.38) is ^LAB(61.38.

LABORATORY INSTRUMENT CODE file (#61.39) global is ^LAB(61.39.

## DHCP Software Requirements:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DHCP Software Laboratory V. 5.2 Files

Laboratory V. 5.2 ANTIMICROBIAL SUSCEPTIBILITY file (#62.06)

VA FileMan V. 21 AUTO INSTRUMENT file (#62.4)

Kernel V. 8.0 ETIOLOGY FIELD file (#61.2)

LABORATORY INSTRUMENT CODE file (#61.39)

LOAD/WORK LIST file (#68.2)

MICRO INSTRUMENT SET-UP file (#61.38)

## Installation Requirements:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The LA\*5.2\*12 Patch installation is using the Kernel Installation and Distribution Systems (KIDS), a new module in Kernel Version 8.0.

## Vitek Computer Requirements:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VITEK VTK R02.0 (Graphical User Interface (GUI) version) or greater

The Vitek text-based software programs have been converted and updated to the new “graphical” platform.

Bi-directional Computer Interface (BCI) Version R020 or greater

The BCI facilitates the exchange of data between the computer in a bioMerieux Vitek instrument and the DHCP computer.

## New Vitek Options:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. Vitek Literal \[LA VITEK LITERAl\] option is used to access verify results. This option is added to the Microbiology \[LRMI\] menu by the KIDS installation process.

2\. Antibiotic Code Print \[LA PRINT ANTIBIOTIC\] option is used to print the antibiotic code entries from the new LIC file (#61.39). This option is added to Microbiology Print \[MICROBIOLOGY PRINT\] MENU by the KIDS installation process.

3\. Organism Code Print \[LA PRINT ORGANISM\] option is used to print the organism code entries from the new LIC file (#61.39. This option is added to Microbiology Print \[MICROBIOLOGY PRINT\] MENU by the KIDS installation process.

## New DHCP Files:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### MICRO INSTRUMENT SET-UP file (#61.38)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The MICRO INSTRUMENT SET-UP file (#61.38) is installed by KIDS. This file provides another dimension for performing tests on the Vitek. The Vitek only permits one test/accession number. This can be circumvented by entering a number between 0-9 in the prefix field of the LABORATORY TEST file (#60). Employing the logic that the Vitek will only accept up to a 6 digit accession number, and no accession shall exceed 99,999. The prefix number could be placed in front of the 5 digit accession. File (#61.38) also turns on the wild card fields for the Vitek.

> **WARNING:** Use of these wild card fields may overwrite historical data in the Vitek.

> **NOTE:** The development of the DHCP Laboratory Vitek Literal Interface project was done using an MSM (486) and ALPHA systems.

### LABORATORY INSTRUMENT CODE (LIC) file (#61.39

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The LABORATORY INSTRUMENT CODE (LIC) file (#61.39) (^LAB(61.39)) was created for the purpose of translating entries from information tables used by the laboratory automated instruments to entries located in DHCP files. For the DHCP Laboratory Vitek Literal Interface project, the LIC file (#61.39) facilitates the translation of the organism and antibiotic tables resident on the Vitek, to the DHCP Laboratory ETIOLOGY FIELD file (#61.2) and ANTIMICROBIAL SUSCEPTIBILITY file (#62.06) entries. The way this novel DHCP concept is accomplished is simple. The LIC file contains two multiple fields, the ORGANISM CODE field \#1, subfile (#61.391) and the ANTIBIOTIC CODE field \#2, subfile (#61.392). These are the main fields of the translator.

Using the organism as an example, once the Vitek identifies an organism it is uploaded across the interface to DHCP where it is matched to an entry in the ORGANISM CODE field \#1 subfile (#61.391) of the LIC file (#61.39). The organism subfile also contains an interpretation entry, which describes the organism code and a local entry that points to the DHCP ETIOLOGY FIELD file (#61.2). The pointing action completes the translation loop between the Vitek and DHCP. The antibiotics tested against the organism by the Vitek are translated in the same manner as the organism.

The LABORATORY INSTRUMENT CODE file (#61.39) is installed by using KIDS. Some local editing of this file will be required. The LIC file (#61.39) comes with most of the codes needed to run the DHCP Vitek Literal Interface. However, additional fields have been added. The LIC file (#61.39) was edited by Barbara McCoy, Microbiology Supervisor at Muskogee VAMC. The organism and antibiotic codes from the Vitek were stored on a 3.5 floppy diskette. The codes were retrieved from the floppy diskette using the LAMIVTLC and LAMIVTLP upload routines. These two routines store the codes in an ^LA(9999 global. A utility routine was also created to enter the codes, via user approval, into the LIC file (#61.39).

# LA\*5.2\*12 Patch Implementation Checklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This check list is provided to ensure a successful implementation of the DHCP Laboratory Vitek Literal Interface LA\*5.2\*12 patch. This checklist may be copied or removed from this section of the documentation for your convenience.

1\. Connect cable from Vitek to LSI 

2\. Set up bioMerieux Vitek Computer ports and protocol 

3\. Run KIDS install 

4\. Printout of antibiotic codes using the new 

Antibiotic Code Print \[LA PRINT ANTIBIOTIC\] option

5\. Printout of organism codes using the new 

Organism Code Print \[LA PRINT ORGANISM\] option

6\. Edit LIC file (#61.39) antibiotic field local entry pointing 

to the ANTIMICROBIAL SUSCEPTIBILITY file (#62.06)

7\. Edit LIC file (#61.39) organism field local entry pointing 

to the ETIOLOGY FIELD file (61.2)

8\. Edit LOAD/WORK LIST file (#68.2) 

9\. Edit AUTO INSTRUMENT file (#62.4) 

10\. Edit MICRO INSTRUMENT SET-UP file (#61.38) 

## VITEK to DHCP Laboratory System Interface (LSI) Cable Wiring

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](la-5-2-12-laboratory-universal-interface-vitek-literal-interface-document/001.png)

# bioMerieux Vitek Computer Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the following instructions for setting up the bioMerieux Vitek computer ports and protocol. The <u>underline</u> appears when a computer response is required.

## Ports Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. From the bioMerieux screen:

> Select - <u>bioLiaison Main menu</u>

2\. From the <u>bioLiaison</u> Main menu:

> Select - <u>BCI</u>

3\. From the bioMerieux Vitek Bidirectional Computer Interface screen:

> Select - <u>PORTS</u>

4\. From the Single Select List screen:

> Highlight - <u>TTY0 and click</u>

5\. From the bioMerieuxx System Maintenance Screen; Change/Show Characteristics of a TTY, edit the following settings:

> BAUD rate - <u>Click on the LIST box and select 2400</u>

> PARITY - <u>Click on the LIST box and select None</u>

> BITS per character - <u>Click on the LIST box and select 8</u>

> Number of STOP BITS - <u>Click on the LIST box and select 1</u>

## Protocol Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. From the <u>bioLiaison</u> Main menu:

> Select - <u>Protocol</u>

2\. From BCI Protocol Configuration (Port tty1) screen:

> Select - <u>Character Set ISO8859=1</u>

> Select - <u>Field \| (Select shift and bar key to enter the bar (\|) symbol)</u>

> Select - <u>Date (may leave blank)</u>

> Select - <u>Time (may leave blank)</u>

3\. From the bioMerieuxx Literal Communication Protocol Parameter menu select the following parameter and enter setup data:

> \<CR\>\<LF\> DELAYS RETRIES TIMEOUT

> STX DIS Last Master <u>10</u> \<ENQ\> Limit <u>3</u> Checksum <u>10</u>

> ETX DIS Inter Record <u>10</u> \<ENQ\> Interval <u>10</u> Host Response <u>10</u>

> RS DIS Inter Message <u>2</u> Checksum Limit <u>3</u>

> GS <u>ENA</u> Checksum Interval <u>10</u>

> ENQ DIS

> EOT DIS

# # LA\*5.2\*12 Patch Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The LA\*5.2\*12 Patch installation is using KIDS, a new module in Kernel V. 8.0. The LABORATORY INSTRUMENT CODE file (#61.39), MICRO INSTRUMENT SET-UP file (#61.38), and three new menu options are installed by this process .The LIC file (#61.39) comes with most of the entries needed to run the Vitek Literal Interface. However, some local editing of this will be required.

The LA\*5.2\*12 patch total installation time is less than 15 minutes.

Background jobs for Laboratory and other software packages are not affected by the LA\*5.2\*12 patch installation process.

All users may remain active on the system during the installation process.

Example:\>D ^XUP\<RET\>

Setting up programmer environment

Terminal Type set to: C-VT100

Select OPTION NAME: EVE Systems Manager Menu\<RET\>

Select Systems Manager Menu Option: Programmer Options \<RET\>

Select Programmer Options Option: Kernel Installation & Distribution System\<RET\>

Select Kernel Installation & Distribution System Option: MAILMan Menu\<RET\>

VA MailMan 7.1 service for HOAK.DAVID_R+@DEV.ISC-DALLAS.VA.GOV

You last used MailMan: 31 Mar 96 12:47

Your current banner is: Computer Programmer

Select MailMan Menu Option: REAd a message\<RET\>

Read MAIL BASKET: IN//\<RET\>

LAST Message Number: 1050 Messages in BASKET: 1050\<RET\>

IN Basket Message: 1// 1050\<RET\>

Subj: LA\*5.2\*12 TEST 2 \[#55472\] 31 Mar 96 12:43 5506 Lines

From: HOAK,DAVID R. in 'IN' basket. Page 1

------------------------------------------------------------------------------

\$TXT Created by HOAK,DAVID R. at DEV.ISC-DALLAS.VA.GOV (DIFROM) on SUNDAY, 03/31/96 at 12:43

\$END TXT

\$ROU XPDPINIT

XPDPINIT ;SFISC/RSD - Load a Packman Message using KIDS ; 6 Feb 95 14:48

;;8.0;KERNEL;\*\*5\*\*;Jul 10, 1995

I '\$D(^XMB(3.9,+\$G(XMZ),0)) W !!,"NO message to install!!" Q

I \$T(^XPDIPM)="" W !!,"KIDS doesn't exist!!" Q

G ^XPDIPM

\$END ROU XPDPINIT

\$TXT \$KIDS LA\*5.2\*12

\*\*INSTALL NAME\*\*

LA\*5.2\*12

"BLD",18,0)

LA\*5.2\*12^^0^2940927^n

"BLD",18,1,0)

Select MESSAGE Action: IGNORE (in IN basket)// X\<RET\>

Select PackMan function: INSTALL/CHECK MESSAGE\<RET\>

> **WARNING:** Installing this message will cause a permanent update of globals

and routines and run the INIT. Do you really want to do this? NO// Y\<RET\>

Shall I preserve what is on disk in a separate back-up message ? YES// N\<RET\>

No backup message built.

Line 3 Message \#55472 Unloading Routine ROU XPDPINIT

LA\*5.2\*12

The following Entries already exist in the INSTALL file:

LA\*5.2\*12 Install Completed

was loaded on Mar 31, 1996@12:48:58

OK to continue? NO// YES\<RET\>.

Want to Continue with Load? YES//\<RET\>

Will first run the Environment Check Routine, LAMIVTLB

.

Select PackMan function: \<RET\>

Select MESSAGE Action: IGNORE (in IN basket)// ^\<RET\>

Select MailMan Menu Option: \<RET\>

Select Kernel Installation & Distribution System Option: Installation\<RET\>

Select Installation Option: Install Package(s) \<RET\>

Select INSTALL NAME: LA\*5.2\*12 Loaded from Distribution 4/1/96@07:30: \<RET\>

49 =\> LA\*5.2\*12 TEST 2

This Distribution was loaded on Apr 01, 1996@07:30:49 with header of LA\*5.2\*12

It consisted of the following Install(s): LA\*5.2\*12 \<RET\>

Will first run the Environment Check Routine, LAMIVTLB

Envirnment Check is Ok ---

Install Questions for LA\*5.2\*12

61.38 MICRO INSTRUMENT SET-UP (including data)

> **NOTE:** You already have the 'MICRO INSTRUMENT SET-UP' File.

Want my data merged with yours? YES// .

61.39 LABORATORY INSTRUMENT CODE (including data)

> **NOTE:** You already have the 'LABORATORY INSTRUMENT CODE' File.

Want my data merged with yours? YES// .

Want to DISABLE Scheduled Options and Menu Options? YES// NO..

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// TELNET

LA\*5.2\*12

------------------------------------------------------------------------------

Install Started for LA\*5.2\*12 :

Apr 01, 1996@10:00:05..

Installing Routines:

Apr 01, 1996@10:00:07..

Installing Data Dictionaries: ..

Apr 01, 1996@10:00:09

Installing Data: ..

Apr 01, 1996@10:00:17

Installing PACKAGE COMPONENTS:

Installing PRINT TEMPLATE

Running Post-Install Routine: ^LAMIVTLE

Option \[LA VITEK LITERAL\] was added to \[MICROBILOLOGY\] MENU

------------------------------------------------------------------------------

Option \[LA PRINT ORGANISM\] was added to \[MICROBIOLOGY PRINT\] MENU

Option \[LA PRINT ANTIBIOTIC\] was added to \[MICROBIOLOGY PRINT\] MENU

Post install completed

Updating Routine file...

Updating KIDS files...

LA\*5.2\*12 Installed.

Install Completed

Post install completed

..

Updating Routine file...

Updating KIDS files...

LA\*5.2\*12 Installed.

Apr 01, 1996@07:31:36..

------------------------------------------------------------------------------

+------------------------------------------------------------+

100% \| 25 50 75 \|

Complete +------------------------------------------------------------+

Install Completed

# Post-Installation Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## ## ## Laboratory Microbiology Staff

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Print DHCP and Vitek Code Entries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. Print out a list of the DHCP and Vitek antibiotic code entries from the LIC file (#61.39) using the new Antibiotic Code Print \[LA PRINT ANTIBIOTIC\] option that was added to \[MICROBIOLOGY PRINT\] MENU by the installation process.

Example: Antibiotic code entries printout

LABORATORY INSTRUMENT CODE LIST MAR 25,1996 11:01 PAGE 1

VITEK CODE VITEK ENTRY DHCP ENTRY

------------------------------------------------------------------------------

amc Amoxicillin/CA Amoxicillin

gm Gentamicin GENTMCN

tax Cefotaxime CEFOTAXIME

mz Mezlocillin MEZLOCILLIN

pip Piperacillin PIPERACILLIN

chl CHLORAM

fos Fosfomycin Fosfomycin

FOSFOMYCIN

dx Doxycycline Doxycycline

DOXYCYCLINE

e Erythromycin ERYTHROMYCIN

ERYTHROMYCINE

efx Enrofloxacin(Vet.) Enrofloxacin(Vet.)

2\. Print out a list of the DHCP and Vitek organism code entries from the LIC file (#61.39) using the new Organism Code Print \[LA PRINT ORGANISM\] option that was added to \[MICROBIOLOGY PRINT\] MENU by the installation process.

Example: Organism code entries printout

LABORATORY INSTRUMENT CODE LIST MAR 25,1996 11:10 PAGE 1

VITEK CODE VITEK ENTRY DHCP ENTRY

------------------------------------------------------------------------------

TODAY Haemophiluslikebacilli- HAEMONCHUS, NOS

gvc Gramvariablecocci-

gbv Gramvariablebacilli-

gpc Grampositivecocci- GRAM POS ROD

gndip Gramnegativediplococci- GRAM NEG ROD

gnb Gramnegativebacilli- GRAM NEG ROD

gvl GARBAGE DISPOSAL APP

ecl E.colilikebacilli- ESCHERICHIA COLI

bhs BetahemolyticStrep- BETA HEMOLYTIC STREP

dl

camjej Campylobacterjejuni CAMPYLOBACTER JEJUNI

dil diphtheroidlikebacilli DIPHTHEROIDS

### Editing DHCP Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### The DHCP ENTRY comes from the ETIOLOGY FIELD file (#61.2). The VITEK ENTRY originally comes from the VITEK and is loaded into ETIOLOGY FIELD file (#61.2) by the installation process. If there is a match to the VITEK entry in the ETIOLOGY FIELD file (#61.2) then the LOCAL ORGANISM ENTRY is filled in. A number in the LOCAL ORGANISM ENTRY is not valid; and indicates there was no match or more than one match which could not be resolved. If the organism is one you isolate then decide which entry in the ETIOLOGY FIELD file (#61.2). matches the Vitek entry. If there is no Etiology entry then you must create one and it has to have a SNOMED code. Follow the instructions in the Microbiology Section of the Lab documentation for Etiology File Entries.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **IMPORTANT:** DO NOT change the antibiotic and organism codes on the Vitek or add to the HOST code. This will cause the Literal Interface to become inoperative.

#### LABORATORY INSTRUMENT CODE FILE file (#61.39)

The LIC file (#61.39) was created to enable editing of the ANTIMICROBIAL SUSCEPTIBILITY file (#62.06) and ETIOLOGY FIELD file (#61.2) for LOCAL ENTRIES.

Example: How to edit/add a new antibiotic code using VA FileMan Version 21.0.

Select OPTION: ENTER OR EDIT FILE ENTRIES\<RET\>

INPUT TO WHAT FILE: LABORATORY INSTRUMENT CODE//\<RET\>

EDIT WHICH FIELD: ALL// ANTIBIOTIC CODE\<RET\> (multiple)\<RET\>

EDIT WHICH ANTIBIOTIC CODE SUB-FIELD: ALL//\<RET\>

THEN EDIT FIELD: \<RET\>

Select LABORATORY INSTRUMENT CODE: VITEK\<RET\>

Select ANTIBIOTIC CODE: tet//\<RET\>

ANTIBIOTIC CODE: tet//\<RET\>

ANTIBIOTIC INTERPRETATION: Tetracycline\<RET\>

LOCAL ANTIBIOTIC ENTRY: TETRCLN//

Select LABORATORY INSTRUMENT CODE: VITEK\<RET\>

Select ANTIBIOTIC CODE: tet//amp \<RET\>

Are you adding ‘amp’ as a new ANTIBIOTIC CODE (the 8th for this LABORATORY

INSTRUMENT CODE)? N\<RET\>

(No) ??

Select ANTIBIOTIC CODE: tet// am

1 am

2 amc

3 ams

CHOOSE 1-3: 1\<RET\>

ANTIBIOTIC CODE: am

ANTIBIOTIC INTERPRETATION: Ampicillin

LOCAL ANTIBIOTIC ENTRY: AMPICLN

Example: How to edit/add a new organism code using VA FileMan Version 21.0.

Select OPTION: ENTER OR EDIT FILE ENTRIES\<RET\>

INPUT TO WHAT FILE: LABORATORY INSTRUMENT CODE//\<RET\>

EDIT WHICH FIELD: ALL// ORGANISM CODE (multiple)\<RET\>

EDIT WHICH ORGANISM CODE SUB-FIELD: ALL//\<RET\>

THEN EDIT FIELD:

Select LABORATORY INSTRUMENT CODE: VITEK\<RET\>

Select ORGANISM CODE: acibac\<RET\>

ORGANISM CODE: acibac//\<RET\>

ORGANISM INTERPRETATION: Acinetobacter baumannii

Replace

LOCAL ORGANISM ENTRY: ACINETOBACTER BAU

Are you adding ‘ACINETOBACTER BAU’ as a new ETIOLOGY FIELD (the 4773RD)???\<RET\>

Answer with ETIOLOGY FIELD NAME, or SNOMED CODE, or SYNONYM, or

\*BIOCHEMICAL WORKUP

LOCAL ORGANISM ENTRY: ACINETOBACTER BAU

Are you adding ‘ACINETOBACTER BAU’ as

a new ETIOLOGY FIELD (the 4773RD)? Y (Yes)

ETIOLOGY FIELD SNOMED CODE: 7001

ALREADY AN ENTRY

??

ANSWER MUST BE 2-7 CHARACTERS IN LENGTH

ETIOLOGY FIELD SNOMED CODE: 7000123

Select LABORATORY INSTRUMENT CODE: VITEK\<RET\>

Select ORGANISM CODE: acibac//e\<RET\>

1 e00007

2 e25922

3 e35218

4 e51446

5 ec

TYPE UP ‘^’ TO STOP, OR

CHOOSE 1-5: 1\<RET\>

ORGANISM CODE: e00007//\<RET\>

ORGANISM INTERPRETATION: Escherichiacoli//\<RET\>

LOCAL ORGANISM ENTRY: ESCHERICHIA COLI//\<RET\>

#### LOAD/WORK LIST file (#68.2)

The following example displays how to set up a Load/work List for the Vitek using VA FileMan 21.0 Enter or Edit File Entries option.

Example

Select OPTION: ENTER OR EDIT FILE ENTRIES\<RET\>

INPUT TO WHAT FILE: LOAD/WORK LIST//\<RET\>

EDIT WHICH FIELD: ALL//\<RET\>

Select LOAD/WORK LIST NAME: \`43 VITEK LITERAL\<RET\>

NAME: VITEK LITERAL//\<RET\>

LOAD TRANSFORM: UNIVERSAL//\<RET\>

TYPE: TRAY,CUP//\<RET\>

CUPS PER TRAY: 30//\<RET\>

FULL TRAY'S ONLY: NO//\<RET\>

EXPAND PANELS ON PRINT: \<RET\>

INITIAL SETUP: \<RET\>

VERIFY BY: ACCESSION//\<RET\>

SUPPRESS SEQUENCE \#:\<RET\>

INCLUDE UNCOLLECTED ACCESSIONS: NO//\<RET\>

SHORT TEST LIST: \<RET\>

AUTO MICRO EDIT TEMPLATE: ZZTHECULTURESPECIAL//\<RET\>

WKLD METHOD: BACTERIAL ID/SUSC AUTO VITEK//\<RET\>

MAJOR ACCESSION AREA: MICROBIOLOGY//\<RET\>

LAB SUBSECTION: MICROBIOLOGY//\<RET\>

WORK AREA: \<RET\>

DATE OF SETUP: MAR 21,1996//\<RET\>

FIRST TRAY: 1//\<RET\>

STARTING CUP: 1//\<RET\>

LAST TRAY: 1//\<RET\>

LAST CUP: 4//\<RET\>

BUILDING IN PROGRESS: NO//\<RET\>

Select PROFILE: VITEK//\<RET\>

PROFILE: VITEK//\<RET\>

Select TEST: ANAEROBE CULTURE & GRAM STAIN//\<RET\>

TEST: ANAEROBE CULTURE & GRAM STAIN//\<RET\>

SPECIMEN: \<RET\>

BUILD NAME ONLY: NO//\<RET\>

Select TEST: \<RET\>

ACCESSION AREA: MICROBIOLOGY//\<RET\>

Select TRAY \#:\<RET\>

Select Specimens to EXCLUDE!: \<RET\>

Select CONTROLS TO BEGIN WORKLIST: \<RET\>

Select CONTROLS TO END WORKLIST: \<RET\>

Select PROFILE: \<RET\>

USER ACCESS AUTHORIZATION: LRVERIFYLABONLY//\<RET\>

Select ADDITIONAL LAB TESTS: \<RET\>

#### AUTO INSTRUMENT file (#62.4)

The AUTO INSTRUMENT file (#62.4) contains all specific information related to each auto instrument in the Laboratory. It is necessary to review and edit this file prior to interfacing the Vitek instrument to run on-line. The following example displays how to add the Vitek Instrument to the AI file (#62.4) using VA FileMan 21.0 Enter or Edit File Entries.

Example

Select OPTION: ENTER OR EDIT FILE ENTRIES\<RET\>

INPUT TO WHAT FILE: AUTO INSTRUMENT//\<RET\>

EDIT WHICH FIELD: ALL//\<RET\>

Select AUTO INSTRUMENT NAME: VITEK3\<RET\>

NAME: VITEK3//\<RET\>

WKLD METHOD: \<RET\>

ECHO DEVICE: LSI \#1//\<RET\>

PROGRAM: LAMIVTLP//\<RET\>

LOAD/WORK LIST: VITEK LITERAL//\<RET\>

ENTRY for LAGEN ROUTINE: Accession cross-reference //\<RET\>

CROSS LINKED BY: +ID//\<RET\>

\*ECHO ALL INPUT: NO//\<RET\>

METHOD: VITEK//\<RET\>

DEFAULT ACCESSION AREA: MICROBIOLOGY//\<RET\>

OVERLAY DATA: YES//\<RET\>

NEW DATA: D NEW^LASET//\<RET\>

RESTART: D RESTART^LASET//\<RET\>

HANDSHAKE RESPONSE: D ^LAMIVTLX//\<RET\>

ACK TRIGGER VALUE: 5//\<RET\>

ACK RESPONSE VALUE: 6//\<RET\>

DIRECT DEVICE: \<RET\>

Select TEST: ^DEF\<RET\>

1 DEFAULT ACCESSION AREA

2 DEFAULT AUTO MICRO TEST

CHOOSE 1-2: 1\<RET\>

DEFAULT ACCESSION AREA: MICROBIOLOGY//\<RET\>

OVERLAY DATA: YES// ^LOAD\<RET\>

1 LOAD CHEM TESTS

2 LOAD/WORK LIST

CHOOSE 1-2: 1\<RET\>

LOAD CHEM TESTS: 1//\<RET\>

Select ALARM TERMINAL: ^\<RET\>

The following example displays how to view the new Vitek entry that was added to AI file (#62.4) using VA FileMan 21.0 Inquire option.

Example

NUMBER: 3 NAME: VITEK3

ECHO DEVICE: LSI \#1 PROGRAM: LAMIVTLP

LOAD/WORK LIST: VITEK LITERAL LOAD CHEM TESTS: 1

ENTRY for LAGEN ROUTINE: Accession cross-reference

CROSS LINKED BY: +ID \*ECHO ALL INPUT: NO

METHOD: VITEK DEFAULT ACCESSION AREA: MICROBIOLOGY

OVERLAY DATA: YES ACK TRIGGER VALUE: 5

ACK RESPONSE VALUE: 6

DEFAULT AUTO MICRO TEST: CULTURE & SUSCEPTIBILITY

HANDSHAKE RESPONSE: D ^LAMIVTLX NEW DATA: D NEW^LASET

RESTART: D RESTART^LASET

#### MICRO INSTRUMENT SET-UP file (#61.38)

The MICRO INSTRUMENT SET-UP file (#61.38) provides another dimension for performing tests on the Vitek. The Vitek only permits one test/accession number. This can be circumvented by entering a number between 0-9 in the prefix field of the LABORATORY TEST file (#60). Employing the logic that the Vitek will only accept up to a 6 digit accession number, and no accession shall exceed 99,999. The prefix number could be placed in front of the 5 digit accession. File (#61.38) also turns on the wild card fields for the Vitek.

> **CAUTION:** If you download entries on a patient and that patient already exists in the VITEK database, the "WILD CARD" fields are OVERWRITTEN to match the most recent entry. This includes the patient wild card field (pw2) currently being used for physician. If wild cards are used for location, the same thing would happen (overwriting of previous entries for the same patient). There are two concerns: 1) the epidemiology function in Vitek CANNOT! be used because Vitek can enter ONLY sort information for TABLE-DRIVEN fields and 2) each time a specimen is downloaded, physician name and patient location for the current specimen overwrites those on previous specimens for the same patient (if they exist). However, the DHCP record would be the official record, but as a back-up, the VITEK database is suspect because the ordering physician (which is required by CAP regulations to be on the report) may not be correct. (Patients could have cultures requested by one physician, get transferred to another location, and have more cultures requested by another physician) For those laboratories wishing to use the epidemiology functions in Vitek, TABLE-DRIVEN fields MUST be utilized. Therefore, we recommend that the option to use EITHER wild card fields OR table-driven fields be offered, as well as a mechanism to designate the codes to use for the various downloaded fields during set-up (i.e., FileMan edit by ADPAC).

> **NOTE:** Please reference the Bidirectional Computer Interface Operator’s Manual, 510710-1, REV 1094 or contact bioMerieux Vitek, 595 Anglum Drive, Hazelwood, MO. 63042-2395, Phone: 314-731-8500, Fax: 314-731-8800 for further instructions.

> **NOTE:** If you decide to use the wild card, make certain you change the wild card labels to reflect what you are doing. You will need to change both the data entry (patient data) report to report data.. Be certain to change both the text label and the data label for each wild card field. Delete the labels you will not be using. Follow the instructions given in the bioMerieux or bioLiaison manuals for changing data labels.

The following example displays how to setup Vitek in the MICRO INSTRUMENT SET-UP file (#61.38) using VA FileMan 21.0 Enter or Edit File Entries option.

Example

Select OPTION: ENTER OR EDIT FILE ENTRIES\<RET\>

INPUT TO WHAT FILE: LABORATORY INSTRUMENT CODE// MICRO INSTRUMENT SET-UP \<RET\>

(1 entry)

EDIT WHICH FIELD: ALL//\<RET\>

Select MICRO INSTRUMENT SET-UP FILE NAME: VITEK\<RET\>

NAME: VITEK//\<RET\>

PREFIX: YES//\<RET\>

Select WILD CARDS ON: YES//\<RET\>

WILD CARDS ON: YES//\<RET\>

w1: LRWRD//?\<RET\>

ENTER ONE

Choose from:

WARD LRWRD

DOC LRDOC

SPEC LRSPEC

TREATING SPECIALTY LRTREAT

BEEPER LRBEEP

w1: LRWRD//\<RET\>

w2: LRDOC//\<RET\>

w3: LRBEEP//\<RET\>

w4: LRSPEC//\<RET\>

w5: LRTREAT//\<RET\>

### Vitek Literal Verification Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a representation of the Vitek Literal verification card dependent data as observed with the new DHCP Laboratory Vitek Literal Interface system.

Example

Select Laboratory DHCP Menu Option: Microbiology menu\<RET\>

RB Results entry (batch)

RE Results entry

VS Verification of data by supervisor

VT Verification of data by tech

WKLD Review accession workload

Accessioning, standard (Microbiology)

Automated Microbiology Menu ...

Batch accessioning

Lab statistics menu ...

Long form accession list for microbiology

Microbiology print menu ...

VITEK

References ...

Results menu ...

Short accession list

Show list of accessions for a patient

Std/QC/Reps Manual Workload count

Supervisor menu ...

Select Microbiology menu Option: VITEK

Vitek Literal verification screen 1

Select auto instrument here: VITEK JR\<RET\>

Select ACCESSION AREA: MICROBIOLOGY//\<RET\>

Accession date: 96//\<RET\> (1996)

Work Load Area: VITEK

Enter the number portion of the Accession: 3161// 3815

There are 7 LAH entries associated with accession 3815

Select one of the following:

1 OK

2 NO

Enter response: OK//\<RET\>

ACC \# (3815) FEB 15,1996@10:57:48

DEMO,DENNIS S SSN: 000-00-0114 LOC: LAB

Specimen: FECES Sample: STOOL

GRAM STAIN 4+ nr

3 + nr

2+ gram negative rod

Is this the correct patient/specimen? ? Yes//\<RET\> (Yes)

DEMO,DENNIS S 000-00-0114

MI 96 3815

FECES STOOL

1 GRAM STAIN

2 CULTURE & SUSCEPTIBILITY

3 CAMPYLOBACTER CULTURE

Please enter the test number(s) or : ALL//\<RET\>

ENTER QUANTITY FOR ( KLEBSIELLA PNEUMONIAE ) : 4+ // (4+)

4+ ? Yes// (Yes)

COMMENT: //

ENTER QUANTITY FOR ( ESCHERICHIA COLI ) : 4+ // (4+)

4+ ? Yes// (Yes)

COMMENT: //

Isolate (1 )

KLEBSIELLA PNEUMONIAE

CARD gns-f3

AMIKACN \<=2 S A

CEFAZOLIN \<=8 S A

CEFOPERAZONE \<=8 S R

CEFOTAXIME \<=4 S A

CEFOXITIN 8 S A

CEFTAZIDIME \<=8 S A

CEFUROXIME \<=4 S R

CEPHALOTHIN 4 S A

NITROFURANTOIN \<=32 S A

TOBRMCN \<=0.5 S A

Enter RETURN to continue or '^' to exit:

Isolate (1 )

KLEBSIELLA PNEUMONIAE

CARD gns-f6

AMPICILLIN \>=32 R A

AMPICILLIN/SULBACTAM 16 I A

AZTREONAM \<=8 S R

CIPROFLOXACIN \<=0.5 S A

IMIPENUM \<=4 S R

MEZLOCILLIN \<=16 S R

OFLOXACIN \<=1 S A

PIPERACILLIN \<=8 S A

TICARCILLIN \>=256 R R

TICARCILLIN/CA \<=16 S R

TRMSULF \<=10 S A

Enter RETURN to continue or '^' to exit:

Isolate (2 )

ESCHERICHIA COLI

CARD gni

Enter RETURN to continue or '^' to exit:

Isolate (2 )

ESCHERICHIA COLI

CARD gns-f3

AMIKACN \<=2 S A

CEFAZOLIN \<=8 S A

CEFOPERAZONE \<=8 S R

CEFOTAXIME \<=4 S A

CEFOXITIN \<=2 S A

CEFTAZIDIME \<=8 S A

CEFUROXIME \<=4 S R

CEPHALOTHIN 8 S A

NITROFURANTOIN \<=32 S A

TOBRMCN \<=0.5 S A

Enter RETURN to continue or '^' to exit:

Isolate (2 )

ESCHERICHIA COLI

CARD gns-f6

AMPICILLIN \>=32 R A

AMPICILLIN/SULBACTAM 16 I A

AZTREONAM \<=8 S R

CIPROFLOXACIN \<=0.5 S A

IMIPENUM \<=4 S R

MEZLOCILLIN \>=256 R R

OFLOXACIN \<=1 S A

PIPERACILLIN \>=256 R A

TICARCILLIN \>=256 R R

TICARCILLIN/CA \<=16 S R

TRMSULF \<=10 S A

Enter RETURN to continue or '^' to exit:

BACT RPT STATUS: ??

Choose from:

F FINAL REPORT

P PRELIMINARY REPORT

BACT RPT STATUS: P PRELIMINARY REPORT

Select GRAM STAIN: 2+ gram negative rod //

Select BACT RPT REMARK:

DEMO,DENNIS S SSN: 000-00-0114

MI 96 3815 STOOL FECES

1\. KLEBSIELLA PNEUMONIAE (4+ )

: 2. ESCHERICHIA COLI (4+ )

: :

SUSC INTP SUSC INTP

AMIKACN \<=2 S \<=2 S \$\$\$\$

AMPICILLIN/SUL 16 I 16 I \$\$

AMPICILLIN \>=32 R \>=32 R \$

AZTREONAM \<=8\* S\* \<=8\* S\* \$\$\$\$

CEFAZOLIN \<=8 S \<=8 S \$

CEFOPERAZONE \<=8\* S\* \<=8\* S\* \$\$

CEFOTAXIME \<=4 S \<=4 S \$\$\$

CEFOXITIN 8 S \<=2 S \$\$

CEFTAZIDIME \<=8 S \<=8 S \$\$\$\$

CEFUROXIME \<=4\* S\* \<=4\* S\* \$\$\$\$

CEPHALOTHIN 4 S 8 S \$

IMIPENUM \<=4\* S\* \<=4\* S\* \$\$\$\$

MEZLOCILLIN \<=16\* S\* \>=256\*R\* \$\$\$\$

NITROFURANTOIN \<=32 S \<=32 S \$

OFLOXACIN \<=1 S \<=1 S \$\$\$

PRESS RETURN FOR MORE

DEMO,DENNIS S SSN: 000-00-0114

MI 96 3815 STOOL FECES

1\. KLEBSIELLA PNEUMONIAE (4+ )

: 2. ESCHERICHIA COLI (4+ )

: :

SUSC INTP SUSC INTP

PIPERACILLIN \<=8 S \>=256 R \$\$\$\$

TICARCILLIN \>=256\*R\* \>=256\*R\* \$\$\$\$

TICARCILLIN/CA \<=16\* S\* \<=16\* S\* \$\$\$\$

TRMSULF \<=10 S \<=10 S \$

('E'dit data, 'C'omments, 'O'rganism 'W'orklist) // ^

REMOVING ^LR DATA

-\>-\>-\>-\>-\>-\>-\>-\>-\>-\>-\>-\>-\>-\>-\>-\>-\>-\>-\>-\>-\>-\>-\>-\>-\>-\>-\>-\>-\>-\>-\>-\>-\>-\>-\>

100%

DONE

# Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. Problem: No Data in ^LA

*Possible Solutions:* Check Vitek protocal setting

Check wiring connections

2\. Problem: No Date in ^LAH

*Solutions:* Loadlist not defined

Loadlist not defined in LIC file (61.39)

Organism defined in LIC file (61.39

Antibiotic defined in LIC file (61.39

3\. Problem: Susceptibility not showing up on reports

*Solution:* Check the ANTIMICROBIAL SUSCEPTIBILITY file (#62.06) to see is the MIC from the Vitek matches that in the Vitek file (i.e. Vitek=0.5, file=.5, file must be changed to 0.5).