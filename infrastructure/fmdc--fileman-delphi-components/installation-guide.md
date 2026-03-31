---
title: FMDC Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: plain
doc_subject: 
app_code: FMDC
app_name: FileMan Delphi Components
section: INF
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - delphi
  - fmdc
  - components
  - fileman
  - help
  - unit
  - contents
  - table
  - compiled
  - installed
page_count: 0
word_count: 2360
section_count: 12
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: March 1998
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Fileman_Delphi_Comp_(FMDC)/fmdc1_0p1ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Fileman_Delphi_Comp_(FMDC)/fmdc1_0p1ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=6"
---

![](fmdc-installation-guide/001.png)

FILEMAN DELPHI COMPONENTS(FMDC)INSTALLATION GUIDE

March 1998

V*IST*A Software Development

OpenV*IST*A Product Line

Table of Contents

Introduction [1](#introduction)

Relationship with VA FileMan [1](#relationship-with-va-fileman)

FMDC Web Site [1](#fmdc-web-site)

Technical Information [3](#technical-information)

Server Requirements [3](#server-requirements)

Server Package Components [3](#server-package-components)

Client (Developer Workstation): FMDC File Listing [4](#client-developer-workstation-fmdc-file-listing)

Developer Workstation Installation Procedure [5](#developer-workstation-installation-procedure)

Developer Workstation Requirements [5](#developer-workstation-requirements)

Skills Needed [5](#skills-needed)

Delphi 3: Installing the FMDC Components [6](#delphi-3-installing-the-fmdc-components)

Delphi 3: Integrating the FMDC.HLP Help File [8](#delphi-3-integrating-the-fmdc.hlp-help-file)

Delphi 2: Installing the FMDC Components [9](#delphi-2-installing-the-fmdc-components)

Delphi 2: Integrating the FMDC.HLP Help File [10](#delphi-2-integrating-the-fmdc.hlp-help-file)

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Relationship with VA FileMan](#relationship-with-va-fileman)
  - [FMDC Web Site](#fmdc-web-site)
- [Technical Information](#technical-information)
  - [Server Requirements](#server-requirements)
  - [Server Package Components](#server-package-components)
  - [Client (Developer Workstation): FMDC File Listing](#client-developer-workstation-fmdc-file-listing)
- [Developer Workstation Installation Procedure](#developer-workstation-installation-procedure)
  - [Developer Workstation Requirements](#developer-workstation-requirements)
  - [## Skills Needed](#skills-needed)
  - [Delphi 3: Installing the FMDC Components](#delphi-3-installing-the-fmdc-components)
  - [Delphi 3: Integrating the FMDC.HLP Help File](#delphi-3-integrating-the-fmdchlp-help-file)
  - [Delphi 2: Installing the FMDC Components](#delphi-2-installing-the-fmdc-components)
  - [Delphi 2: Integrating the FMDC.HLP Help File](#delphi-2-integrating-the-fmdchlp-help-file)
This Installation Guide provides instructions for installing the FileMan Delphi Components (FMDC) V. 1.0.
The FileMan Delphi Components make it easy for developers to work with VA FileMan data in Delphi applications. The components encapsulate the details of retrieving, validating and updating VA FileMan data within a Delphi application. This saves you from creating your own custom remote procedure calls (RPCs) when you need to access VA FileMan data.
The FileMan Delphi Components also include special enhanced features such as complete server-side error checking and data dictionary help.
If you're already familiar with Delphi, the time needed to develop an application to edit a set of VA FileMan fields using the FileMan Delphi Components is comparable to the time needed to create the same application using VA FileMan's roll-and-scroll ScreenMan interface.

## Relationship with VA FileMan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FileMan Delphi Components are part of VA FileMan. The server-side RPCs and routines that support the components are released in VA FileMan patch DI\*21\*34.

The components themselves, used by developers and compiled into Delphi applications, are also part of VA FileMan. Their versioning is separate, however, to make it easier to track the version of components vs. the version of VA FileMan; they will likely be on separate release schedules.

## FMDC Web Site

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FileMan Delphi Components web site provides up-to-date information including FAQs, troubleshooting tips, and any code or documentation updates. Check the web site:

- Before installing the FileMan Delphi Components.
- Periodically as you use the components, to keep in touch with the latest updates.

<http://vista.med.va.gov/fmdc/index.asp>

# Technical Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Server Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- RPC Broker V. 1.1 or Greater Installed  
    
  When you create an application with the FileMan Delphi Components, the server(s) your application connects to need to have the RPC Broker V. 1.1 or greater installed.
- Patch DI\*21\*34 Installed  
    
  When you create an application with the FileMan Delphi Components, the server(s) your application connects to need to have the FileMan Delphi Components Remote Procedure Calls (RPCs) and supporting M routines installed. These RPCs and routines are distributed as patch DI\*21\*34.  
    
  As part of VA FileMan, patch DI\*21\*34 will be installed on all production systems. If you need to install this patch on a particular server, however, follow the installation instructions provided with the patch.
- Patch DI\*21\*41 Installed  
    
  This patch includes an update to a DBS call to make it compatible with the FileMan Delphi Components.

## Server Package Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FileMan Delphi Components themselves do not export any package components for M servers. The companion VA FileMan DI\*21\*34 patch, however, exports routines and remote procedure calls (RPCs) for M servers.

## Client (Developer Workstation): FMDC File Listing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A single self-extracting .EXE file (FMDC1_0.EXE) is provided to install the FileMan Delphi Components on developer workstations. The files distributed are:

Documentation

FMDC1_0GS.PDF Getting Started Guide

Delphi 3 Installation

DIACCESS.DCU Diaccess compiled unit

DIDATAPROB.DCU Didataprob compiled unit

DIDATAPROB.DFM Form for didataprob unit

DIERR.DCU Dierr compiled unit

DIERR.DFM Form for dierr unit

DIHLP.DCU Dihlp compiled unit

DIHLP.DFM Form for dihlp unit

DITYPLIB.DCU Dityplib compiled unit

FMCMPNTS.DCR Resources for fmcmpnts unit

FMCMPNTS.DCU Fmcmpnts compiled unit

FMCNTRLS.DCR Resources for fmcntrls unit

FMCNTRLS.DCU Fmcntrls compiled unit

FMDC.CNT Contents file for Online Help

FMDC.DCP Compiled Package file for Delphi 3

FMDC.DPL Package library file for Delphi 3

FMDC.HLP Online Help

FMLOOKUP.DCR Resources for fmlookup unit

FMLOOKUP.DCU Fmlookup compiled unit

FMLOOKUP.DFM Form for fmlookup unit

Delphi 2 Installation

DIACCESS.DCU Diaccess compiled unit

DIDATAPROB.DCU Didataprob compiled unit

DIDATAPROB.DFM Form for didataprob unit

DIERR.DCU Dierr compiled unit

DIERR.DFM Form for dierr unit

DIHLP.DCU Dihlp compiled unit

DIHLP.DFM Form for dihlp unit

DITYPLIB.DCU Dityplib compiled unit

FMCMPNTS.DCR Resources for fmcmpnts unit

FMCMPNTS.DCU Fmcmpnts compiled unit

FMCNTRLS.DCR Resources for fmcntrls unit

FMCNTRLS.DCU Fmcntrls compiled unit

FMDC.CNT Contents file for Online Help

FMDC.HLP Online Help

FMDC.KWF Keyword file for integrating Online Help w/Delphi 2

FMLOOKUP.DCR Resources for fmlookup unit

FMLOOKUP.DCU Fmlookup compiled unit

FMLOOKUP.DFM Form for fmlookup unit

# Developer Workstation Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FileMan Delphi Components only need to be installed on developer workstations. To distribute the functionality of the FileMan Delphi Components to end-users, developers simply compile the functionality of the components into their own applications.

## Developer Workstation Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- 32-bit Windows operating system: Windows 95 or greater, or Windows NT 3.51 or greater
- Borland Delphi 2 or greater
- RPC Broker BDK (Broker Development Kit) V. 1.1 or greater
- Disk space:  
  - Delphi 2 support only: 600K  
  - Delphi 3 support only: 750K  
  - Delphi 2 and 3 support: 1350K

## ## Skills Needed

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To install the FileMan Delphi Components on a developer workstation, you will need to know how to do the following in the Microsoft Windows environment:

- Run an automated SETUP.EXE installation program
- Use Windows Explorer (or Windows NT Explorer)
- Create directories
- Copy, move and delete files
- Edit text files
- Use Delphi menu options

## Delphi 3: Installing the FMDC Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are two different installation procedures for the FileMan Delphi Components: one for Delphi 3 and one for Delphi 2.

To install the FileMan Delphi Components in Delphi 3

> 1\. Check the FMDC web site for any troubleshooting tips or updated installation instructions.

> 2\. If a previous version of the FileMan Delphi Components is installed in Delphi, you should remove it.

> a\. In Delphi 3, choose Component \| Install Packages.

> b\. If the previous version of the FileMan Delphi Components is in its own package, select that package in the Design Packages list and click Remove.  

> If the previous version of the FileMan Delphi Components is combined in the same package with non-FMDC components you wish to keep, select that package in the Design Packages and click Edit. In the package, select and remove each of the following units: Fmcmpnts, Fmcntrls, and Fmlookup.

> c\. Click OK to close the Project Options window.

> d\. Choose Tools \| Environment Options. Choose the Library tab, and edit the Library Path to remove the reference to the directory containing the old FileMan Delphi Components.

> e\. Switch to Windows Explorer from Delphi, and delete the contents of the directory containing the old FileMan Delphi Components. In particular, all DI\*.\* and FM\*.\*. files should be deleted if present.

> 3\. The TRPCBroker component (from the RPC Broker Development Kit) should already be installed in Delphi 3 before attempting to install the FMDC components into Delphi.

> 4\. Close Delphi. Run FMDC1_0.EXE. This copies the FileMan Delphi Components files to the directory of your choice. By default, the components are installed in "C:\PROGRAM FILES\VISTA\FMDC\\. This path may be longer than you want to include in Delphi's search paths; you may want to change the default location to a directory with a shorter path such as "C:\FMDC". The Delphi 3 version of the components is installed in the D3 subdirectory of the directory you specify.

> 5\. Start Delphi 3. Install the new FMDC package files:

> a\. Choose Component \| Install Packages from Delphi's menu.

> b\. Click Add.

> c\. In the Add Design Package dialog box, navigate to the directory where you installed the Delphi 3 version of the FileMan Delphi Components (e.g., \FMDC\D3). Choose the FMDC.DPL file and click Open. FileMan Delphi Components V1.0 should now be listed as a checked item in the list of Design Packages, and the components should now be visible on the FileMan tab on the component palette.

> ![](fmdc-installation-guide/002.png)

> 6\. If any of the FileMan Delphi Components were previously installed on different tab in the component palette (such as the Kernel tab), you'll need to manually move them to the FileMan tab. Choose Component \| Configure Palette in Delphi to do this.

> 7\. You may want to move the FileMan component palette tab to be the first or second tab in the component palette rather than last. Choose Component \| Configure Palette to do this.

## Delphi 3: Integrating the FMDC.HLP Help File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can integrate the FMDC.HLP help file with Delphi's help. This means that you can select a FileMan component on a Delphi form, or a FileMan component property in Delphi's Object Inspector, press F1, and automatically access the corresponding help file topic from FMDC.HLP.

To integrate FMDC.HLP with Delphi's Help:

1\. Exit Delphi if it is running.

2\. In Windows Explorer, select and delete the following files in the …\Delphi 3\HELP directory, if they are present:

> FMCD.HLP

> FMCD.CNT

> FMDC.HLP

> FMDC.CNT

> DELPHI3.GID  
> BROKER.GID  
> FMDC.GID

> FMCD.GID

The .GID files are hidden files; if you don't see them in Windows Explorer, choose Windows Explorer's View \| Options, and select Show All Files.

3\. Copy FMDC.CNT and FMDC.HLP into the …\Delphi 3\HELP directory.

4\. Using a text editor (e.g., Windows Notepad), open the DELPHI3.CFG file in the …\Delphi 3\HELP directory. In the "Third-Party Help" section of DELPHI3.CFG, add the following statement (if not already present):

> :LINK FMDC.HLP

Make sure the file referenced is the new name (fmdc.hlp) and not the old one (fmcd.hlp). Save DELPHI3.CFG.

5\. Start the Notepad or Wordpad accessory (or another text editor). Within the text editor, open the DELPHI3.CNT file in the ...\DELPHI 3\HELP directory.

6\. In DELPHI3.CNT's Index section (top of the file), add the following line (if not already present):

:Index FileMan Delphi Components =fmdc.hlp

Make sure the file referenced is the new name (fmdc.hlp) and not the old one (fmcd.hlp).

7\. Add the following line in DELPHI3.CNT's "Include" section (if not already present):

:Include fmdc.cnt

Make sure the file referenced is the new name (fmdc.cnt) and not the old one (fmcd.cnt).

8\. Save your changes to DELPHI3.CNT and close the file.

9\. To test the context-sensitive help: Start Delphi. On a blank form, add a FileMan component from the component palette to your form. Select the component on your form and press F1. Help for that component should automatically come up, after a brief delay.

## Delphi 2: Installing the FMDC Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are two different installation procedures for the FileMan Delphi Components: one for Delphi 3 and one for Delphi 2.

To install the FileMan Delphi Components in Delphi 2

1\. Check the FMDC web site for any troubleshooting tips or updated installation instructions.

2\. The TRPCBroker component (from the RPC Broker Development Kit) should already be installed in Delphi before attempting to install the FMDC components into Delphi.

3\. If a previous version of the FileMan Delphi Components is installed in Delphi, switch to the directory containing the FileMan Delphi Components. Delete all .DCU (Delphi Compiled Unit) files. You may also want to delete all other files in that directory, assuming no files are present other than those from an earlier installation of the FileMan Delphi Components.

4\. Run FMDC1_0.EXE. This installs the FileMan Delphi Components files in the directory of your choice. By default, the components are installed in "C:\PROGRAM FILES\VISTA\FMDC\\. This path may be longer than you want to include in Delphi's search paths; you may want to change the default location to a directory with a shorter path such as "C:\FMDC". The Delphi 2 version of the components is installed in the D2 subdirectory of the directory you specify.

5\. Start Delphi 2. In Delphi's Component menu, choose Install to open the Install Components dialog box.

6\. If a previous version of the FileMan Delphi Components is present, you should remove it. To do this, in the Components \| Install dialog box, look to see if any of the following installed units are present:

> Fmcmpnts  
> Fmcntrls  
> Fmlookup

If any of these installed units are present:

a\. Select them and click Remove.

b\. Edit the Search Path field to remove the reference to the directory containing the old FMDC installed units (if no other installed units are in that directory).

7\. Add the new FileMan Delphi Components units. Click Add in the Install Components dialog box. Use the Browse button to browse to the directory where you installed the Delphi 2 version of the FileMan Delphi Components. Select *Unit File (\*.DCU)* in the Files of Type list. One by one, add each of the following files as an installed unit:

> Fmcmpnts.dcu  
> Fmcntrls.dcu  
> Fmlookup.dcu

8\. Click OK to close the Install Components dialog box. Delphi rebuilds your component library. The installation of the FileMan Delphi Components should now be complete; the FMDC components should now be available in Delphi's component palette in a FileMan tab.

9\. If any of the FileMan Delphi Components were previously installed on another tab in the component palette (such as the Kernel tab), you'll need to manually move them to the FileMan tab. Choose Component \| Configure Palette in Delphi to do this.

## Delphi 2: Integrating the FMDC.HLP Help File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can integrate the FMDC.HLP help file with Delphi's help. This means that you can select a FileMan component on a Delphi form, or a FileMan component property in Delphi's Object Inspector, press F1, and automatically access the corresponding help file topic from FMDC.HLP.

To integrate FMDC.HLP with Delphi's Help:

1\. Delphi 2 should already be installed on your development PC.

2\. Exit Delphi if it is running.

3\. Copy the FMDC.HLP, FMDC.KWF and FMDC.CNT files to the ...\HELP subdirectory below the main DELPHI directory.

4\. Run the HELPINST application from the \Delphi2.0\HELP\TOOLS folder.

5\. Use HELPINST to open the DELPHI.HDX file. From HELPINST's File menu, choose Open. The DELPHI.HDX file is usually located in the \BIN subdirectory below the main DELPHI directory.

6\. Ordinarily, several keyword files should be listed when you open DELPHI.HDX, including DELPHI.KWF and CWG.KWF.  
  
If either FMDC.KWF or FMCD.KWF is listed, click that file once to select it, and then press HELPINST's red "-" button to delete it. Both should be removed from the list.

7\. Now click HELPINST's green "+" button, to add the FMDC.KWF file to HELPINST's list of .KWF files. You may need to navigate to the \HELP subdirectory of the main Delphi directory to find FMDC.KWF. Once selected, FMDC.KWF should be in HELPINST's list of .KWF files.

8\. Save the updated DELPHI.HDX file. From HELPINST's file menu, choose save. This completes the merging of this help file into Delphi's help.

9\. Exit HELPINST.

10\. Start Delphi. On a blank form, add one of the FileMan Delphi Components from the component palette to your form. Highlight the component and press F1 for help. If the help for that component comes up, you are all set.  
  
However, you may get the message:

> Cannot find the FMDC.HLP file. Do you want to try to find this file yourself?

If you get this message, click YES. Navigate to the HELP subdirectory of the main Delphi directory, and choose FMDC.HLP. Windows opens the help file, and the path to the help file should be remembered in the future.

You can find related information about merging help into Delphi's help in Delphi *Component Writer's Guide* manual (Delphi Version 2.0: pp. 77-81).