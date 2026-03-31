---
consolidated_title: "bcbu cache installation guide"
app_code: PSB
doc_type: IG
master_source: "BCBU Cache Version 3 Installation Guide (updated PSB*3*84)"
master_pub_date: April 2015
consolidated_from: 3 versions
prior_versions:
  - "BCBU Cache Version 3 Installation Guide (updated PSB*3*91)"
  - "BCBU Cache Version 3 Installation Guide"
---

<!-- image -->

# Bar Code Medication Administration (BCMA)
BCMA Backup System (BCBU)
InterSystems Caché Installation Setup


April 2015

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Product Development (PD)

## Revision History

| Date   | Revision   | Description                                                                                                                                                                              | Author   |
|--------|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------|
| 4/2015 | PSB*3*84   | Document updated byREDACTED. Entire document reformatted.                                                                                                                                | REDACTED |
| 07/11  | PSB*3*65   | Footers updated; removed HSITES and added Product Development, removed VistA. Renamed instances of CACHE to Caché throughout the document. Updated version to reflect BCMA v3.0 version. |          |
| 08/03  | PSB*2*17   | Original Released Bar Code Medication Administration Backup System (BCBU) InterSystems Caché Workstation Installation Setup Guide.                                                       |          |

## Contents

1	InterSystems Caché Installation Setup	1

1.1	Caché Configuration Manager	6

1.1.1	Adding a Database	7

1.1.2	Adding a Namespace	12

1.1.3	Global and Routine Mapping	16

1.1.4	Global Mapping	17

1.1.5	Routine Mapping	19

1.1.6	Cache Licenses install	23

1.1.7	Removing Read/Archive Properties	24

1.2	Telnet Instructions	24

1.3	Setting up Telnet and Terminal Users	37

1.4	Setting up the BCMA Shortcut	45

1.4.1	Edit a TRM or VTRM device	50

## InterSystems Caché Installation Setup

This section illustrates step-by-step installation of Caché v2011, for use with Bar Code Medication Administration Backup System (BCBU) Workstation.

The Caché software was downloaded from the VA FTP sites and is located under the corresponding version of the CACHE folder. To start the setup locate the downloaded executable and run it.

Accept the license agreement and click **Next.**

<!-- image -->

Figure 1

Click **NEXT** at the Define Cache Instance Name.

<!-- image -->

Figure 2

Click **Next** at Destination Folder

<!-- image -->

Figure 3

Choose **Development** and click **Next** .

<!-- image -->

Figure 4

Continue following the instructions and accept the defaults for your system.

<!-- image -->

Figure 5

<!-- image -->

Figure 6

Click **Install**

<!-- image -->

Figure 7

Uncheck **Display the Getting Started page** and click **Finish** .

<!-- image -->

Figure 8

Upon the completion of a successful installation, a "Blue Cube" will appear on the PC toolbar in the lower right hand side of the screen.

<!-- image -->

Figure 9

### Caché Configuration Manager

Caché must be configured with databases, namespaces, and routines by using the Management Portal located on the Caché cube menu options.

Right clicking on the cube will display the menu options for Caché, and then choose **Management Portal** .

<!-- image -->

Figure 10

#### Adding a Database

The first step is to add a Database. From the Main Screen, choose the **Menu** button and then **Configure Databases** .

<!-- image -->

Figure 11

Select the **Local Database** option and then **Create New Database** button.

<!-- image -->

Figure 12

Type **VISTA** as the name of the database and enter **C:\BCMABU** into the Directory Selected field. Click **NEXT** to continue.

<!-- image -->

Figure 13

Verify values entered and click **FINISH** .

<!-- image -->

Figure 14

The newly created database should now appear in the list (bottom of the list) with C:\BCMABU\ as its directory.

<!-- image -->

Figure 15

#### Adding a Namespace

We will create the namespace VISTA and attach it to the VISTA database.

Click the **MENU** button and choose **Configure Namespaces** .

<!-- image -->

Figure 16

Click Create **New Namespace** button.

<!-- image -->

Figure 17

Type **VISTA** as the namespace and select **VISTA – C\BCMABU\** as the existing database. Click **Save** .

<!-- image -->

Figure 18

VISTA namespace should be seen in the listing of Caché Namespaces.

<!-- image -->

Figure 19

#### Global and Routine Mapping

Global and Routine Mappings are created under the Configuration Namespaces option by selecting Global Mappings and Routine Mappings for the VISTA namespace.

<!-- image -->

Figure 20

#### Global Mapping

Click Global Mappings for the **VISTA** namespace. Then click **New Global Mapping** to create the global mapping definition as shown in the following slide.

<!-- image -->

Figure 21

<!-- image -->

Figure 22

#### Routine Mapping

Click the **Menu** button (Figure 22) and then **Configure Namespaces** .

The Global Database Location is **VISTA** and the Global name is **%Z*.** Click **Apply** (Figure 21) and **Save Changes** .

Select Routine Mapping.

<!-- image -->

Figure 23

Select **New Routine Mapping** . Type the first routine name, **%DT*,** (Figure 24) in the space provided and select **VISTA** as the routine database location. Click **Apply** . Repeat this procedure for routine names % **RCR, %XU* and %Z*.** When complete, your routine mapping should appear as shown in Figure 25. Click **Save Changes** and close this window.

<!-- image -->

Figure 24

<!-- image -->

Figure 25

Shut down CACHÉ

Click the Blue Cube (PC toolbar in the lower right hand side of the screen) and choose Stop Cache.

<!-- image -->

Figure 26

You will see the following screen as CACHE shuts down.

<!-- image -->

Figure 27

#### Cache Licenses install

The license information is a text file sent to you by InterSystems (cache.key).

Copy and paste into the **C:\InterSystems\Cache\mgr** folder.

CACHE.DAT

Copy the **CACHÉ.DAT** file you downloaded from the VA FTP site and copy it to the **C:\BCMABU** folder.

You may receive a message stating the file is already present and do you want to replace it with the file you are importing. If so, answer **YES** .

#### Removing Read/Archive Properties

Using the "Windows Explorer", remove the Read and Archive Properties from the CACHÉ.DAT file. Right click “CACHÉ.DAT” and select "Properties" under the General Tab and Click Advance to remove Archive. Click Apply and then OK.

<!-- image -->

Figure 28

### Telnet Instructions

Start Caché. Note: The Cache Cube icon is Gray in color at this point, not Blue.

<!-- image -->

Figure 29

What we are going to do next is to move the **ZSTU** routine from the **VISTA** namespace to the **%SYS** namespace using the Management Portal.

Select Menu **button** then **View Routines.**

<!-- image -->

Figure 30

Select VISTA on left side of the screen.

Enter ZSTU in the Routines box and click **Export.**

<!-- image -->

Figure 31

Make sure the check box is selected for the routine (ZSTU.int).

Click **Export**

<!-- image -->

Figure 32

When finished, a message stating it was completed should appear.

<!-- image -->

Figure 33

Click the **Menu button** and then **View Routines** . See steps 1 -6 to accomplish the following: Select the **%SYS** namespace (left side of screen). Select **Import** from across the top. Select the **%SYS** namespace (left side of screen). Browse to the path where you exported the routine. Select the routine and click **OK** .

<!-- image -->

Figure 34

*Step 1.*

Select **%SYS** on left side of the screen, click the **Browse Button**

<!-- image -->

Figure 35

*Step 2* *.*

Select **C:\**

<!-- image -->

Figure 36

*Step 3* .

Click **BCMABU**

<!-- image -->

Figure 37

*Step 4* .

Click **export.ro** and then the **OK** button.

<!-- image -->

Figure 38

*Step 5* .

Click the **OPEN** button.

<!-- image -->

Figure 39

*Step 6* .

Make sure the box is checked by ZSTU.INT. Click **Import** . The successful completion message should appear as shown in the following screen.

<!-- image -->

Figure 40

The successful completion message should appear as shown in the following screen.

<!-- image -->

Figure 41

### Setting up Telnet and Terminal Users

We will be using the Management Portal to set up the Unknown User so the Telnet and Terminal Users will connect to the VISTA namespace using the routine ZU.

Click **HOME**

From **the Menu button** select **Manage Users** . The User Accounts will be displayed.

<!-- image -->

Figure 42

Click **Edit** for the Unknown User. Select **VISTA** as the Startup Namespace and enter **^ZU** as the Startup Tag^Routine. Click **Save** then **Close this window.**

(Note: For programmer access, %PMODE in Default Tag^Routine.)

<!-- image -->

Figure 43

After the edits are done the screen should look like this.

<!-- image -->

Figure 44

**IMPORTANT NOTE** : Stop and restart Caché. This will be the BCMA Backup Application. The start-up routine **ZSTU** will automatically start up TaskManager.

Verify certain parameters are set for proper operation.

From the Management Portal

Choose Menu, and then Manage Services. Click **%Service Telnet (** Figure 46 **)** and set **%Service Telnet Enabled = Yes and Public = Yes** . 
If not, click item and change the settings.

<!-- image -->

Figure 45

<!-- image -->

Figure 46

Return to **Home** , select **System Administration** ,then **Configuration** then **Device Settings** , then **Telnet Settings** then **GO** under *View or edit telnet definitions* . Set Telnet **Port** to **19210.** Default setting is 23. (Figures 47-48)

<!-- image -->

Figure 47

<!-- image -->

Figure 48

Click **Home** , then **Menu** then **Configure Memory** .

<!-- image -->

Figure 49

Make sure the “ *Start Cache on System Boot* ” is checked. If not, check it and click **Save** . Close this window.

<!-- image -->

Figure 50

### Setting up the BCMA Shortcut

To create the shortcut from scratch, right click anywhere on the desktop and select **New/Shortcut** .

<!-- image -->

Figure 51

Enter **C:\InterSystems\Cache\bin\css.exe CTERMINAL CACHE** in the *Type the location of the item box.* Click **Next** .

<!-- image -->

Figure 52

Enter BCBU in the *Type a name for this shortcut* and click Finish (Figure 53).

Copy the Shortcut BCBU Icon to the All User Desktop.

<!-- image -->

Figure 53

Double-click the BCBU shortcut icon to enter the Backup system on the PC Workstation. Use the appropriate access and verify code to access the system.

<!-- image -->

Figure 54

<!-- image -->

Figure 55

This completes the setup of InterSystems Caché on the BCBU contingency workstation. Refer to the BCBU VistA Install Guide to complete the package setup.

How to Setup the Printer in BCBU PC.

Hook up the printer to the PC.

Install the Window printer drivers.

Click BCBU icon on PC and log in as user that has programmer privileges.

Select Systems Manager Menu Option: *Device Management*

Select Device Management Option: *Device Edit*

Select Device Edit Option: *TRM, TRM, or VTRM Device Edit*

Select Terminal/Printer Device: BCBU

#### Edit a TRM or VTRM device

NAME: BCBU PRINTER		LOCATION: BCBU WORKSTATION

$I: |PRN| Name of the window’s printer

Example: Window's printer is Lexmark T650 PS3, then enter |PRN| Lexmark T650 PS3

Alt $I:

TYPE: TERMINAL

SUBTYPE: P-HP-P16

SIGN-ON/SYSTEM DEVICE: NO

VOLUME SET(CPU):

ASK DEVICE: NO			MARGIN WIDTH:

ASK PARAMETERS: NO		PAGE LENGTH:

QUEUING: FORCED			SUPPRESS FORM FEED:

Save and Exit.

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: BCBU Cache Version 3 Installation Guide

## ## Overview

This document contains instructions for the Upgrade to Caché 2017 on Microsoft Windows workstations.

### General Background Information

These instructions are specific to installing Caché on Windows workstations for the use of Caché with BCMA Backup system (BCBU).

### Prerequisites

Installation requires administrator privileges through local admin account logon or via user’s etoken with admin rights to the machine.

## Retrieve the Files Needed to Perform this Upgrade

The following table identifies the file required for the installation.

Table 1: Installation Files

| File Name                                         | Download Type   |
|---------------------------------------------------|-----------------|
| cache-2017.2.2.865.0-win_x64.exe (Windows 64-bit) | Binary          |

The files can be downloaded from VistA at, download.vista.med.va.gov, or retrieved via secure file transfer protocol (SFTP) from the following locations:

Table 2: OI Field Offices

| Field Office   | DNS Address   |
|----------------|---------------|
| REDACTED       | REDACTED      |
| REDACTED       | REDACTED      |

Use SFTP mode to transfer the required file. There are several ways this file can be downloaded. An example of performing an SFTP and download of the distribution is shown in section 2.1.

### Command Prompt SFTP

The following is a sample screen dialogue of the file retrieval using the Command Prompt.

1. Open a Windows Command Prompt Session (START &gt; enter CMD in the search programs and files box, right click on CMD and Run As Administrator). Note: etoken may be necessary and privileges may only be necessary depending on directory you download to.
2. Set the default to the target directory.
3. Verify the bytes received are the same size noted as the SFTP transfer size.

**Note:** Commands are highlighted in Bold Red and **vhausername** is your VA login

Microsoft Windows [Version 6.1.7601

Copyright (c) 2009 Microsoft Corporation. All rights reserved.

C:\Users\vhausername&gt;

C:\Users\vhausername&gt; **cd Desktop**

C:\Users\vhausername\Desktop&gt;

…Desktop&gt; **sftp -o StrictHostKeyChecking=no anonymous@download.vista.med.va.gov**

HOST ON LINE OpenVMS AXP (TM) Operating System, Version V8.3

Enter password for anonymous@download.vista.med.va.gov: **&lt;leave blank hit enter&gt;**

/$1$dga105/anonymous&gt; **cd cache/cache2017**

/$1$dga105/anonymous/cache/cache2017&gt; **ls**

CACHE-2017\_2\_2\_865\_0-WIN\_X64.ZIP;1

CACHE-2017\_2\_2\_865\_0-WIN\_X86.ZIP;1

/$1$dga105/anonymous/cache/cache2017&gt; **binary**

Transfer mode set to binary

/$1$dga105/anonymous/cache/cache2017&gt; **get CACHE-2017\_2\_2\_865\_0-WIN\_X64.ZIP**

&lt;Note Status will show as downloading and after complete&gt;

Downloaded /$1$dga105/anonymous/cache/cache2017/CACHE-2017\_2\_2\_865\_0-WIN\_X64.ZIP

to C:\Users\vhausername\Desktop\CACHE-2017\_2\_2\_865\_0-WIN\_X64.ZIP (438.51mB 1.0

2mB/s 00:07:11)

/$1$dga105/anonymous/cache/cache2017&gt; **exit**

Connection closed to download.vista.med.va.gov

C:\Users\vhausername\Desktop\

1. If there is a large difference in the file size downloaded to your workstation, the file did not transfer correctly and the download should be performed again.

## Unzip the file

Extract CACHE-2017\_2\_2\_865\_0-WIN\_X64.ZIP as follows:

1. Open the file menu and select **Extract All.**

Figure 1: Extract All File Menu Option

<!-- image -->

1. It will make a cache 2017 folder on the desktop during extraction, select **Extract.**

Figure 2: Pre-Extraction Dialog Box

<!-- image -->

Figure 3: Extraction Process Progress Bar

<!-- image -->

1. A popup window will show the executable when extraction is complete.

Figure 4: Post-Extraction File Folder

<!-- image -->

## InterSystems Caché Installation/Upgrade

This section illustrates step-by-step installation of Caché v2017 for use with Bar Code Medication Administration Backup System (BCBU) workstations. Using the newly extracted file folder (C:\Users\vhausername\Desktop\CACHE-2017\_2\_2\_865\_0-WIN\_X64), complete the following:

1. Open the file options menu for, **cache-2017.2.2.865.0-win\_x64.exe,** and select Run as Administrator

Figure 5: File Options Menu for the Extracted File

<!-- image -->

1. The user will have to select the appropriate etoken account or enter an administrator account and password.

Figure 6: User Account Control

<!-- image -->

1. If the Windows user account being used does not have required administrator privileges to perform this installation, the following dialog will be displayed. At which point the user will need to seek assistance from a privileged workstation administrator.

Figure 7: Not Having the Proper Privileges for Installation

<!-- image -->

1. If the proper credentials are recognized, then proceed with the New Installation.

**Note:** If this is a **FIRST TIME** installation of any version of Caché on your workstation, proceed to the First Time Installation section.

1. If this is an upgrade installation, select the Instance Name to be upgraded and then select **OK** .

Figure 8: Select Instance Dialog Box

<!-- image -->

1. Select **Upgrade** to begin.

Figure 9: Upgrading Instance Cache Options

<!-- image -->

Figure 10: Cache Updater in Progress

<!-- image -->

1. Select **Finish.**

Figure 11: Installation Complete

<!-- image -->

At this point Cache has been upgraded to version 2017 and no changes or additions should be needed. Start Cache back up by opening the Cache cube’s menu options in the system tray and selecting **Start** .

**Note** : This is optional. Once installation is complete, the zip file and Cache 2017 folder can be deleted from the desktop; if copies are needed again they can be downloaded again.

## First Time Installation

1. Run the install executable
2. Agree to the License Terms and select **Next** .

Figure 12: License Agreement

<!-- image -->

1. Select **Next** at the Define Cache Instance Name (Default name should be CACHE).

Figure 13: Cache Instance Name

<!-- image -->

1. Select **Next** at the Destination Folder (keep default).

Figure 14: Destination Folder

<!-- image -->

1. Choose **Development** and select **Next** .

Figure 15: Setup Type

<!-- image -->

1. Continue following the instructions and accept the system defaults.

Figure 16: Install Unicode Support?

<!-- image -->

Figure 17: Initial Security Settings?

<!-- image -->

1. Select **Install** .

Figure 18: Ready to Install the Program

<!-- image -->

1. Status bar will show during installation.

Figure 19: Installation Status Bar

<!-- image -->

1. Select **Finish** .

Figure 20: Installation Complete

<!-- image -->

After a successful installation, a **Blue Cube** will appear in the System Tray in the lower right hand corner of the screen.

Figure 21: Blue Cube Location

<!-- image -->

### Caché Configuration Manager

Caché must be configured with databases, namespaces, and routines by using the Management Portal located in the Caché cube’s menu options. Open the Caché cube’s menu options and select **Management Portal** .

Figure 22: Caché Management Portal

<!-- image -->

#### Adding a Database

The first step is to add a Database.

1. From the main screen, select **Menu,** then select **Configure Databases** .

Figure 23: Database Configuration

<!-- image -->

1. Select **Create New Database** .

Figure 24: Create New Database

<!-- image -->

1. Enter **VISTA** as the name of the database and enter **C:\BCMABU** into the Database Directory field. Select **Next** to continue. If that folder doesn’t exist, the user will be prompted to create it, answer **Yes** .

Figure 25: Create New Database

<!-- image -->

1. Verify the values entered are correct and select **Finish** .

Figure 26: Database Details

<!-- image -->

1. The newly created database should now appear in the list (bottom of the list) with C:\BCMABU\ as its directory.

Figure 27: Local Database List

<!-- image -->

#### Adding a Namespace

Creating the Namespace VISTA and attach it to the VISTA database.

1. From the main screen, select **Menu** and then select **Configure Namespaces** .

Figure 28: Configure Namespaces

<!-- image -->

1. Select **Create New Namespace** .

Figure 29: Create New Namespace

<!-- image -->

1. Enter **VISTA** as the Namespace and select **VISTA – C\BCMABU\** as the existing database for Globals and Routines. Uncheck Create a default Web application for this Namespace. Select **Save** .

Figure 30:

<!-- image -->

1. The VISTA Namespace should be seen in the listing of Caché Namespaces.

Figure 31: List of Namespaces

<!-- image -->

#### Global and Routine Mapping

Global and Routine Mappings are created under the Configuration Namespaces option by selecting Global Mappings and Routine Mappings for the VISTA Namespace.

Figure 32: Global and Routine Mapping

<!-- image -->

#### Global Mapping

1. Select **Global Mappings** for the VISTA Namespace. Then select **New** to create the global mapping definition as shown in the following slide.

Figure 33: Global Mapping Screen

<!-- image -->

1. The Global Database Location is **VISTA** and the Global name is **%Z*** . Select **OK** and **Save Changes.**

Figure 34: Mapping a New Global in a Namespace

<!-- image -->

#### Routine Mapping

1. Select **Menu** from the Namespaces screen, then select **Configure Namespaces** .
2. Select **Routine Mapping** for the VISTA Namespace.

Figure 35: Routine Mapping

<!-- image -->

1. Select **New** .
2. Select **VISTA** as the Routine Database Location.
    - 2.1. Enter the first routine name, **%DT*** , in the Routine Name field and select **Apply** .
    - 2.2. Enter, % **RCR** , as the second Routine Name and select **Apply** .
    - 2.3. Enter, **%XU*** , as the third Routine Name and select **Apply** .
    - 2.4. Enter, **%Z*** , as the fourth Routine Name and select **OK** .

Figure 36: Mapping a Routine in the VISTA Namespace

<!-- image -->

1. When finished with all four entries, the routine mapping should appear as shown below. Select **Save Changes** and close the window.

Figure 37: New Routine List

<!-- image -->

1. Shut down CACHÉ by opening the menu options for the Blue Cube located in the System Tray, in the lower right hand corner of the screen, and select **Stop Cache** .

Figure 38: Stop Cache Menu Option

<!-- image -->

1. Select Shut down and select **OK** .

Figure 39: Cache Shutdown Dialog Box

<!-- image -->

**Note:** The following screen is displayed as CACHE shuts down.

<!-- image -->

#### Cache Licenses install

The license information is a text file sent by InterSystems (cache.key).

Copy and paste the text file into the **C:\InterSystems\Cache\mgr** folder.

#### Cache DAT File install

Copy the **CACHE.DAT** file that was downloaded from the VA SFTP site and place it in the **C:\BCMABU** folder. A message may display, stating that the file is already present, proceed with replacing it? If this message is displayed, then answer **YES** .

**Note** : The file is located on the same SFTP servers as the Cache software but is under the anonymous\software folder. The name of the file to download will be BCBUCACHEV2014DATmmddyy.zip. Select the file with the latest date.

**Note:** The name of this file may change as patches/updates are applied.

Start Cache back up by reopening the menu options for the now Grey Cube (it shows as a Blue Cube when Cache is running) in the System Tray. Select **Start Cache** .

#### Moving ZSTU routine

The next step is to move the **ZSTU** routine from the **VISTA** Namespace to the **%SYS** Namespace using the Management Portal.

1. Select **Menu** , then select **View Routines.**

Figure 40: View Routines

<!-- image -->

1. Select the VISTA Namespace and enter **ZSTU*.*** in the Routines and include files box. The ZSTU routines will be listed. Check the box for ZSTU.int and select **Export.** The following screen will be displayed.

Figure 41: Export Routines

<!-- image -->

1. Select **Export** .
2. When finished, a message stating the process was completed should appear. Select **Done** .

Figure 42: Completed Export

<!-- image -->

Figure 43: Exported Routine

<!-- image -->

1. Select **Menu** and then select **View Routines** . See previous steps if needed. The **Look in** field should be set to Namespace and the Namespace should be **%SYS** . Select **Import** from across the top. Browse to the path of the exported routine (the default is C:\BCMABU). Select the file created in the export (if the name wasn’t changed when saving, then the default will be export.ro). Select **Next** , then select **Import** .

Figure 44: Import Routines

<!-- image -->

1. When complete the following screen will be display. Select **Done** .

Figure 45: Import Successful

<!-- image -->

### Setting up Terminal Users

Use the Management Portal to set up the Unknown User so the Terminal Users will connect to the VISTA namespace using the routine ZU.

1. From the **Menu** select **Manage Users** . The User accounts will be displayed.

Figure 46: Manage Users

<!-- image -->

1. Select the **UnknownUser** to edit it. Select VISTA as the Startup Namespace and enter **^ZU** as the Startup Tag^Routine. Select **Save** then close this window.

**Note:** For programmer access leave the Startup Tag^Routine blank.

Figure 47: Edit UnknownUser Account

<!-- image -->

1. After the edits are complete the User account list will appear like **Figure 48** .

Figure 48: User Account List

<!-- image -->

**IMPORTANT NOTE:** Stop and restart Caché. This will be the BCMA Backup Application. The start-up routine ZSTU will automatically start up TaskManager.

### Verify certain parameters are set for proper operation

1. From the Management Portal select **Menu** , then select **Configure Memory** .

Figure 49: System Memory Settings

<!-- image -->

1. Make sure the **Auto-start on System Boot** is checked. If it is not, then check it and select **Save** . Close this window.

### Setting up the BCMA Shortcut

1. To create the shortcut, open the options menu anywhere on the desktop and select **New &gt; Shortcut** .

Figure 50: Shortcut Menu Option

<!-- image -->

1. Enter **C:\InterSystems\Cache\bin\css.exe CTERMINAL CACHE** in the **Type the location of the item** box. Select **Next** .

Figure 51: Create Shortcut Location Dialog Box

<!-- image -->

1. Enter **BCBU** in the **Type a name for this shortcut** , and then select **Finish** .
2. Copy the Shortcut BCBU icon to the All User Desktop.

Figure 52: Create Shortcut Name Dialog Box

<!-- image -->

1. Open the BCBU shortcut icon to enter the Backup system on the workstation (BCMA Backup in Figure 53). Use the appropriate access and verify code to access the system.

Figure 53: Example Workstation Desktop

<!-- image -->

Figure 54: Opening the BCBU Shortcut

<!-- image -->

1. This completes the setup of InterSystems Caché on the BCBU contingency workstation. Refer to the BCBU VistA Install Guide to complete the package setup.

#### Setting up the printer for use with BCBU

1. Connect the printer to the computer.
2. Install the Windows printer drivers.
3. Select the BCBU icon on the computer and log in as a user that has programmer privileges.
4. Select the Systems Manager Menu Option: **Device Management**
5. Select the Device Management Option: **Device Edit**
6. Select the Device Edit Option: **TRM, TRM, or VTRM Device Edit**
7. Select the Terminal/Printer Device: **BCBU**

#### Edit a TRM or VTRM device

NAME: BCBU PRINTER		LOCATION: BCBU WORKSTATION

$I: |PRN| Name of the window’s printer

Example: Window's printer is Lexmark T650 PS3, then enter |PRN|Lexmark T650 PS3

Edit a TRM or VTRM device

NAME: BCBU PRINTER                              LOCATION: BCBU WORKSTATION

$I: |PRN|Lexmark T650 PS3

Alt $I:

TYPE: TERMINAL

SUBTYPE: P-HPLASER-P16

SIGN-ON/SYSTEM DEVICE: NO

VOLUME SET(CPU):

ASK DEVICE:                             	             	        MARGIN WIDTH:

ASK PARAMETERS: NO                            	           PAGE LENGTH:

QUEUING: ALLOWED                  SUPPRESS FORM FEED:

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND:

Save and Exit.
