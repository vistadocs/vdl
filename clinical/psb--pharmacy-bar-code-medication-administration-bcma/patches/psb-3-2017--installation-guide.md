---
title: BCBU Cache Version 3 Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: 
app_code: PSB
app_name: "Pharmacy: Bar Code Medication Administration (BCMA)"
section: CLI
app_status: archive
pkg_ns: PSB
patch_ver: 3
patch_id: PSB*3*2017
group_key: "PSB:PSB:3"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - table
  - cache
  - contents
  - routine
  - bcbu
  - installation
  - vista
  - cach
  - namespace
  - global
page_count: 0
word_count: 2229
section_count: 8
table_count: 3
figure_count: 5
appendix_count: 0
has_toc: False
is_stub: False
pub_date: December 2019
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Bar_Code_Med_Admin_(BCMA)_Archive/bcbu_cache_2017_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Bar_Code_Med_Admin_(BCMA)_Archive/bcbu_cache_2017_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=387"
---

---
title: |
  Bar Code Medication Administration (BCMA)

  BCMA Backup System (BCBU)

  InterSystems Caché Installation Setup
---

![](bcbu-cache-version-3-installation-guide/001.png)

December 2019

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Product Development (PD)

Revision History

| Date    | Revision    | Description                                                                                                                                                                              | Author                             |
|---------|-------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------|
| 12/2019 | PSB\*3\*122 | Document updated for Cache version 2017                                                                                                                                                  | <span class="mark">REDACTED</span> |
| 04/2015 | PSB\*3\*84  | Document updated by Kevin Cownie. Entire document reformatted.                                                                                                                           | <span class="mark">REDACTED</span> |
| 07/2011 | PSB\*3\*65  | Footers updated; removed HSITES and added Product Development, removed VistA. Renamed instances of CACHE to Caché throughout the document. Updated version to reflect BCMA v3.0 version. |                                    |
| 08/2003 | PSB\*2\*17  | Original Released Bar Code Medication Administration Backup System (BCBU) InterSystems Caché Workstation Installation Setup Guide.                                                       |                                    |

Table 1: Installation Files

Table of Contents

# Overview


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Overview](#overview)
  - [General Background Information](#general-background-information)
  - [Prerequisites](#prerequisites)
- [Retrieve the Files Needed to Perform this Upgrade](#retrieve-the-files-needed-to-perform-this-upgrade)
  - [Command Prompt SFTP](#command-prompt-sftp)
- [Unzip the file](#unzip-the-file)
- [InterSystems Caché Installation/Upgrade](#intersystems-caché-installationupgrade)
- [First Time Installation](#first-time-installation)
  - [Caché Configuration Manager](#caché-configuration-manager)
    - [Adding a Database](#adding-a-database)
    - [Adding a Namespace](#adding-a-namespace)
    - [Global and Routine Mapping](#global-and-routine-mapping)
    - [Global Mapping](#global-mapping)
    - [Routine Mapping](#routine-mapping)
    - [Cache Licenses install](#cache-licenses-install)
    - [Cache DAT File install](#cache-dat-file-install)
    - [Moving ZSTU routine](#moving-zstu-routine)
  - [Setting up Terminal Users](#setting-up-terminal-users)
  - [Verify certain parameters are set for proper operation](#verify-certain-parameters-are-set-for-proper-operation)
  - [Setting up the BCMA Shortcut](#setting-up-the-bcma-shortcut)
    - [Setting up the printer for use with BCBU](#setting-up-the-printer-for-use-with-bcbu)
    - [Edit a TRM or VTRM device](#edit-a-trm-or-vtrm-device)
This document contains instructions for the Upgrade to Caché 2017 on Microsoft Windows workstations.

## General Background Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

These instructions are specific to installing Caché on Windows workstations for the use of Caché with BCMA Backup system (BCBU).

## Prerequisites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Installation requires administrator privileges through local admin account logon or via user’s etoken with admin rights to the machine.

# Retrieve the Files Needed to Perform this Upgrade

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following table identifies the file required for the installation.

| File Name                                         | Download Type |
|---------------------------------------------------|---------------|
| cache-2017.2.2.865.0-win_x64.exe (Windows 64-bit) | Binary        |

Table 2: OI Field Offices

The files can be downloaded from VistA at, download.vista.med.va.gov, or retrieved via secure file transfer protocol (SFTP) from the following locations:

| Field Office                       | DNS Address                        |
|------------------------------------|------------------------------------|
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |

Documentation Revision HistoryThe OI Field Offices table shows the locations where the files can be downloaded from organized using a Field Office and DNS Address column.

Use SFTP mode to transfer the required file. There are several ways this file can be downloaded. An example of performing an SFTP and download of the distribution is shown in section 2.1.

## Command Prompt SFTP

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is a sample screen dialogue of the file retrieval using the Command Prompt.

1.  Open a Windows Command Prompt Session (START \> enter CMD in the search programs and files box, right click on CMD and Run As Administrator). Note: etoken may be necessary and privileges may only be necessary depending on directory you download to.
2.  Set the default to the target directory.
3.  Verify the bytes received are the same size noted as the SFTP transfer size.

> Note: Commands are highlighted in Bold Red and vhausername is your VA login

Microsoft Windows \[Version 6.1.7601

Copyright (c) 2009 Microsoft Corporation. All rights reserved.

C:\Users\vhausername\>

C:\Users\vhausername\>cd Desktop

C:\Users\vhausername\Desktop\>

…Desktop\>sftp -o StrictHostKeyChecking=no anonymous@download.vista.med.va.gov

HOST ON LINE OpenVMS AXP (TM) Operating System, Version V8.3

Enter password for anonymous@download.vista.med.va.gov: \<leave blank hit enter\>

/\$1\$dga105/anonymous\>cd cache/cache2017

/\$1\$dga105/anonymous/cache/cache2017\>ls

CACHE-2017_2_2_865_0-WIN_X64.ZIP;1

CACHE-2017_2_2_865_0-WIN_X86.ZIP;1

/\$1\$dga105/anonymous/cache/cache2017\>binary

Transfer mode set to binary

/\$1\$dga105/anonymous/cache/cache2017\>get CACHE-2017_2_2_865_0-WIN_X64.ZIP

\<Note Status will show as downloading and after complete\>

Downloaded /\$1\$dga105/anonymous/cache/cache2017/CACHE-2017_2_2_865_0-WIN_X64.ZIP

to C:\Users\vhausername\Desktop\CACHE-2017_2_2_865_0-WIN_X64.ZIP (438.51mB 1.0

2mB/s 00:07:11)

/\$1\$dga105/anonymous/cache/cache2017\>exit

Connection closed to download.vista.med.va.gov

C:\Users\vhausername\Desktop\\

4.  If there is a large difference in the file size downloaded to your workstation, the file did not transfer correctly and the download should be performed again.

# Unzip the file

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Extract CACHE-2017_2_2_865_0-WIN_X64.ZIP as follows:

1.  Open the file menu and select Extract All.

> Figure 1: Extract All File Menu Option

> ![](bcbu-cache-version-3-installation-guide/002.png)

2.  It will make a cache 2017 folder on the desktop during extraction, select Extract.

> Figure 2: Pre-Extraction Dialog Box

> ![](bcbu-cache-version-3-installation-guide/003.png)

> Figure 3: Extraction Process Progress Bar

> ![](bcbu-cache-version-3-installation-guide/004.png)

3.  A popup window will show the executable when extraction is complete.

> Figure 4: Post-Extraction File Folder

> ![](bcbu-cache-version-3-installation-guide/005.png)

# InterSystems Caché Installation/Upgrade

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section illustrates step-by-step installation of Caché v2017 for use with Bar Code Medication Administration Backup System (BCBU) workstations. Using the newly extracted file folder (C:\Users\vhausername\Desktop\CACHE-2017_2_2_865_0-WIN_X64), complete the following:

1.  Open the file options menu for, cache-2017.2.2.865.0-win_x64.exe, and select Run as Administrator

> Figure 5: File Options Menu for the Extracted File

> ![](bcbu-cache-version-3-installation-guide/006.png)

2.  The user will have to select the appropriate etoken account or enter an administrator account and password.

> Figure 6: User Account Control

> ![](bcbu-cache-version-3-installation-guide/007.png)

3.  If the Windows user account being used does not have required administrator privileges to perform this installation, the following dialog will be displayed. At which point the user will need to seek assistance from a privileged workstation administrator.

> Figure 7: Not Having the Proper Privileges for Installation

> ![](bcbu-cache-version-3-installation-guide/008.png)

4.  If the proper credentials are recognized, then proceed with the New Installation.

> Note: If this is a FIRST TIME installation of any version of Caché on your workstation, proceed to the First Time Installation section.

5.  If this is an upgrade installation, select the Instance Name to be upgraded and then select OK.

> Figure 8: Select Instance Dialog Box

> ![](bcbu-cache-version-3-installation-guide/009.png)

6.  Select Upgrade to begin.

> Figure 9: Upgrading Instance Cache Options

> ![](bcbu-cache-version-3-installation-guide/010.png)

> Figure 10: Cache Updater in Progress

> ![](bcbu-cache-version-3-installation-guide/011.png)

7.  Select Finish.

> Figure 11: Installation Complete

> ![](bcbu-cache-version-3-installation-guide/012.png)

At this point Cache has been upgraded to version 2017 and no changes or additions should be needed. Start Cache back up by opening the Cache cube’s menu options in the system tray and selecting Start.

> **NOTE:** This is optional. Once installation is complete, the zip file and Cache 2017 folder can be deleted from the desktop; if copies are needed again they can be downloaded again.

# First Time Installation 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Run the install executable
2.  Agree to the License Terms and select Next.

> Figure 12: License Agreement

> ![](bcbu-cache-version-3-installation-guide/013.png)

3.  Select Next at the Define Cache Instance Name (Default name should be CACHE).

> Figure 13: Cache Instance Name

> ![](bcbu-cache-version-3-installation-guide/014.png)

4.  Select Next at the Destination Folder (keep default).

> Figure 14: Destination Folder

> ![](bcbu-cache-version-3-installation-guide/015.png)

5.  Choose Development and select Next.

> Figure 15: Setup Type

> ![](bcbu-cache-version-3-installation-guide/016.png)

6.  Continue following the instructions and accept the system defaults.

> Figure 16: Install Unicode Support?

> ![](bcbu-cache-version-3-installation-guide/017.png)

> Figure 17: Initial Security Settings?

> ![](bcbu-cache-version-3-installation-guide/018.png)

7.  Select Install.

> Figure 18: Ready to Install the Program

> ![](bcbu-cache-version-3-installation-guide/019.png)

8.  Status bar will show during installation.

> Figure 19: Installation Status Bar

> ![](bcbu-cache-version-3-installation-guide/020.png)

9.  Select Finish.

> Figure 20: Installation Complete

> ![](bcbu-cache-version-3-installation-guide/021.png)

After a successful installation, a Blue Cube will appear in the System Tray in the lower right hand corner of the screen.

Figure 21: Blue Cube Location

![](bcbu-cache-version-3-installation-guide/022.png)

## Caché Configuration Manager

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Caché must be configured with databases, namespaces, and routines by using the Management Portal located in the Caché cube’s menu options. Open the Caché cube’s menu options and select Management Portal.

Figure 22: Caché Management Portal

![](bcbu-cache-version-3-installation-guide/023.png)

### Adding a Database

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The first step is to add a Database.

1.  From the main screen, select Menu, then select Configure Databases.

> Figure 23: Database Configuration

> ![](bcbu-cache-version-3-installation-guide/024.png)

2.  Select Create New Database.

> Figure 24: Create New Database

> ![](bcbu-cache-version-3-installation-guide/025.png)

3.  Enter VISTA as the name of the database and enter C:\BCMABU into the Database Directory field. Select Next to continue. If that folder doesn’t exist, the user will be prompted to create it, answer Yes.

> Figure 25: Create New Database

> ![](bcbu-cache-version-3-installation-guide/026.png)

4.  Verify the values entered are correct and select Finish.

> Figure 26: Database Details

> ![](bcbu-cache-version-3-installation-guide/027.png)

5.  The newly created database should now appear in the list (bottom of the list) with C:\BCMABU\\ as its directory.

> Figure 27: Local Database List

> ![](bcbu-cache-version-3-installation-guide/028.png)

### Adding a Namespace

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Creating the Namespace VISTA and attach it to the VISTA database.

1.  From the main screen, select Menu and then select Configure Namespaces.

> Figure 28: Configure Namespaces

> ![](bcbu-cache-version-3-installation-guide/029.png)

2.  Select Create New Namespace.

> Figure 29: Create New Namespace

> ![](bcbu-cache-version-3-installation-guide/030.png)

3.  Enter VISTA as the Namespace and select VISTA – C\BCMABU\\ as the existing database for Globals and Routines. Uncheck Create a default Web application for this Namespace. Select Save.

> Figure 30:

> ![](bcbu-cache-version-3-installation-guide/031.png)

4.  The VISTA Namespace should be seen in the listing of Caché Namespaces.

> Figure 31: List of Namespaces

> ![](bcbu-cache-version-3-installation-guide/032.png)

### Global and Routine Mapping

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Global and Routine Mappings are created under the Configuration Namespaces option by selecting Global Mappings and Routine Mappings for the VISTA Namespace.

Figure 32: Global and Routine Mapping

![](bcbu-cache-version-3-installation-guide/033.png)

### Global Mapping

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Select Global Mappings for the VISTA Namespace. Then select New to create the global mapping definition as shown in the following slide.

> Figure 33: Global Mapping Screen

> ![](bcbu-cache-version-3-installation-guide/034.png)

2.  The Global Database Location is VISTA and the Global name is %Z\*. Select OK and Save Changes.

> Figure 34: Mapping a New Global in a Namespace

> ![](bcbu-cache-version-3-installation-guide/035.png)

### Routine Mapping

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Select Menu from the Namespaces screen, then select Configure Namespaces.
2.  Select Routine Mapping for the VISTA Namespace.

> Figure 35: Routine Mapping

> ![](bcbu-cache-version-3-installation-guide/036.png)

3.  Select New.
4.  Select VISTA as the Routine Database Location.
    1.  Enter the first routine name, %DT\*, in the Routine Name field and select Apply.
    2.  Enter, %RCR, as the second Routine Name and select Apply.
    3.  Enter, %XU\*, as the third Routine Name and select Apply.
    4.  Enter, %Z\*, as the fourth Routine Name and select OK.

> Figure 36: Mapping a Routine in the VISTA Namespace

> ![](bcbu-cache-version-3-installation-guide/037.png)

5.  When finished with all four entries, the routine mapping should appear as shown below. Select Save Changes and close the window.

> Figure 37: New Routine List

> ![](bcbu-cache-version-3-installation-guide/038.png)

6.  Shut down CACHÉ by opening the menu options for the Blue Cube located in the System Tray, in the lower right hand corner of the screen, and select Stop Cache.

> Figure 38: Stop Cache Menu Option

> ![](bcbu-cache-version-3-installation-guide/039.png)

7.  Select Shut down and select OK.

> Figure 39: Cache Shutdown Dialog Box

> ![](bcbu-cache-version-3-installation-guide/040.png)

> Note: The following screen is displayed as CACHE shuts down.

> ![](bcbu-cache-version-3-installation-guide/041.png)

### Cache Licenses install

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The license information is a text file sent by InterSystems (cache.key).

Copy and paste the text file into the C:\InterSystems\Cache\mgr folder.

### Cache DAT File install

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Copy the CACHE.DAT file that was downloaded from the VA SFTP site and place it in the C:\BCMABU folder. A message may display, stating that the file is already present, proceed with replacing it? If this message is displayed, then answer YES.

> **NOTE:** The file is located on the same SFTP servers as the Cache software but is under the anonymous\software folder. The name of the file to download will be BCBUCACHEV2014DATmmddyy.zip. Select the file with the latest date.

> **NOTE:** The name of this file may change as patches/updates are applied.

Start Cache back up by reopening the menu options for the now Grey Cube (it shows as a Blue Cube when Cache is running) in the System Tray. Select Start Cache.

### Moving ZSTU routine

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The next step is to move the ZSTU routine from the VISTA Namespace to the %SYS Namespace using the Management Portal.

1.  Select Menu, then select View Routines.

> Figure 40: View Routines

> ![](bcbu-cache-version-3-installation-guide/042.png)

2.  Select the VISTA Namespace and enter ZSTU\*.\* in the Routines and include files box. The ZSTU routines will be listed. Check the box for ZSTU.int and select Export. The following screen will be displayed.

> Figure 41: Export Routines

> ![](bcbu-cache-version-3-installation-guide/043.png)

3.  Select Export.
4.  When finished, a message stating the process was completed should appear. Select Done.

> Figure 42: Completed Export

> ![](bcbu-cache-version-3-installation-guide/044.png)

Figure 43: Exported Routine

![](bcbu-cache-version-3-installation-guide/045.png)

5.  Select Menu and then select View Routines. See previous steps if needed. The Look in field should be set to Namespace and the Namespace should be %SYS. Select Import from across the top. Browse to the path of the exported routine (the default is C:\BCMABU). Select the file created in the export (if the name wasn’t changed when saving, then the default will be export.ro). Select Next, then select Import.

Figure 44: Import Routines

![](bcbu-cache-version-3-installation-guide/046.png)

6.  When complete the following screen will be display. Select Done.

> Figure 45: Import Successful

> ![](bcbu-cache-version-3-installation-guide/047.png)

## Setting up Terminal Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the Management Portal to set up the Unknown User so the Terminal Users will connect to the VISTA namespace using the routine ZU.

1.  From the Menu select Manage Users. The User accounts will be displayed.

> Figure 46: Manage Users

> ![](bcbu-cache-version-3-installation-guide/048.png)

2.  Select the UnknownUser to edit it. Select VISTA as the Startup Namespace and enter ^ZU as the Startup Tag^Routine. Select Save then close this window.

> Note: For programmer access leave the Startup Tag^Routine blank.

> Figure 47: Edit UnknownUser Account

> ![](bcbu-cache-version-3-installation-guide/049.png)

3.  After the edits are complete the User account list will appear like Figure 48.

> Figure 48: User Account List

> ![](bcbu-cache-version-3-installation-guide/050.png)

> IMPORTANT NOTE: Stop and restart Caché. This will be the BCMA Backup Application. The start-up routine ZSTU will automatically start up TaskManager.

## Verify certain parameters are set for proper operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  From the Management Portal select Menu, then select Configure Memory.

> Figure 49: System Memory Settings

> ![](bcbu-cache-version-3-installation-guide/051.png)

2.  Make sure the Auto-start on System Boot is checked. If it is not, then check it and select Save. Close this window.

## Setting up the BCMA Shortcut

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  To create the shortcut, open the options menu anywhere on the desktop and select New \> Shortcut.

> Figure 50: Shortcut Menu Option

> ![](bcbu-cache-version-3-installation-guide/052.png)

2.  Enter C:\InterSystems\Cache\bin\css.exe CTERMINAL CACHE in the Type the location of the item box. Select Next.

> Figure 51: Create Shortcut Location Dialog Box

> ![](bcbu-cache-version-3-installation-guide/053.png)

3.  Enter BCBU in the Type a name for this shortcut, and then select Finish.
4.  Copy the Shortcut BCBU icon to the All User Desktop.

> Figure 52: Create Shortcut Name Dialog Box

> ![](bcbu-cache-version-3-installation-guide/054.png)

5.  Open the BCBU shortcut icon to enter the Backup system on the workstation (BCMA Backup in Figure 53). Use the appropriate access and verify code to access the system.

> Figure 53: Example Workstation Desktop

> ![](bcbu-cache-version-3-installation-guide/055.png)

> Figure 54: Opening the BCBU Shortcut

> ![](bcbu-cache-version-3-installation-guide/056.png)

6.  This completes the setup of InterSystems Caché on the BCBU contingency workstation. Refer to the BCBU VistA Install Guide to complete the package setup.

### Setting up the printer for use with BCBU

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Connect the printer to the computer.
2.  Install the Windows printer drivers.
3.  Select the BCBU icon on the computer and log in as a user that has programmer privileges.
4.  Select the Systems Manager Menu Option: Device Management
5.  Select the Device Management Option: Device Edit
6.  Select the Device Edit Option: TRM, TRM, or VTRM Device Edit
7.  Select the Terminal/Printer Device: BCBU

### Edit a TRM or VTRM device

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

NAME: BCBU PRINTER LOCATION: BCBU WORKSTATION

\$I: \|PRN\| Name of the window’s printer

Example: Window's printer is Lexmark T650 PS3, then enter \|PRN\|Lexmark T650 PS3

Edit a TRM or VTRM device

NAME: BCBU PRINTER LOCATION: BCBU WORKSTATION

\$I: \|PRN\|Lexmark T650 PS3

Alt \$I:

TYPE: TERMINAL

SUBTYPE: P-HPLASER-P16

SIGN-ON/SYSTEM DEVICE: NO

VOLUME SET(CPU):

ASK DEVICE: MARGIN WIDTH:

ASK PARAMETERS: NO PAGE LENGTH:

QUEUING: ALLOWED SUPPRESS FORM FEED:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND:

Save and Exit.