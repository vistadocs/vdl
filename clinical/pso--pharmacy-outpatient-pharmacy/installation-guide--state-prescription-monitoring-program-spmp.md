---
consolidated_title: "state prescription monitoring program (spmp) installation guide"
app_code: PSO
doc_type: IG
master_source: "PSO*7*451 State Prescription Monitoring Program (SPMP) Installation Guide"
master_pub_date: August 2016
consolidated_from: 2 versions
prior_versions:
  - "PSO*7*408 State Prescription Monitoring Program (SPMP) Installation Guide"
---

State Prescription Monitoring Program (SPMP) EnhancementPatch PSO\*7\*451

Installation, Back-Out, and Rollback Guide

![](pso-7-451-state-prescription-monitoring-program-spmp-installation-guide/001.png)

August 2016

Office of Information and Technology (OI&T)

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
- [Pre-installation and System Requirements](#pre-installation-and-system-requirements)
  - [System Requirements](#system-requirements)
  - [Platform Installation and Preparation](#platform-installation-and-preparation)
  - [Download and Extract Files](#download-and-extract-files)
  - [Database Creation](#database-creation)
  - [Installation Scripts](#installation-scripts)
  - [Cron Scripts](#cron-scripts)
  - [Access Requirements and Skills Needed for the Installation](#access-requirements-and-skills-needed-for-the-installation)
- [Installation Procedure](#installation-procedure)
  - [Installation from the Patch Description](#installation-from-the-patch-description)
- [Implementation Procedure](#implementation-procedure)
  - [Post-Install Routine (No Action Required)](#post-install-routine-no-action-required)
  - [Existing PSO SPMP NOTIFICATIONS Mailgroup (Action Required)](#existing-pso-spmp-notifications-mailgroup-action-required)
  - [New PSO SPMP ADMIN Security Key (Action Required)](#new-pso-spmp-admin-security-key-action-required)
  - [New RENAME FILE AFTER UPLOAD Parameter (May Require Action)](#new-rename-file-after-upload-parameter-may-require-action)
  - [New Transmission Configuration](#new-transmission-configuration)
    - [Register your Outpatient Pharmacy site with the SPMP (Action Required)](#register-your-outpatient-pharmacy-site-with-the-spmp-action-required)
    - [Open Network Traffic between your site and the SPMP (Action Required)](#open-network-traffic-between-your-site-and-the-spmp-action-required)
    - [OpenVMS Directory (May Require Action)](#openvms-directory-may-require-action)
    - [SPMP State Parameter Configuration (Action Required)](#spmp-state-parameter-configuration-action-required)
    - [Create a new SSH Key Pair (Action Required)](#create-a-new-ssh-key-pair-action-required)
    - [Customize the ASAP Definition with state specific data requirements (May Require Action)](#customize-the-asap-definition-with-state-specific-data-requirements-may-require-action)
    - [Test the Transmission (Action Required)](#test-the-transmission-action-required)
- [Back-Out Procedure](#back-out-procedure)
  - [Back-Out Strategy](#back-out-strategy)
  - [Back-Out Considerations](#back-out-considerations)
    - [Load Testing](#load-testing)
    - [User Acceptance Testing](#user-acceptance-testing)
  - [Back-Out Criteria](#back-out-criteria)
  - [Back-Out Risks](#back-out-risks)
  - [Authority for Back-Out](#authority-for-back-out)
  - [Back-Out Procedure](#back-out-procedure-1)
- [Rollback Procedure](#rollback-procedure)
  - [Rollback Considerations](#rollback-considerations)
  - [Rollback Criteria](#rollback-criteria)
  - [Rollback Risks](#rollback-risks)
  - [Authority for Rollback](#authority-for-rollback)
  - [Rollback Procedure](#rollback-procedure-1)
- [Additional Information](#additional-information)
  - [Documentation](#documentation)
- [Disaster Recovery and Continuity of Operations](#disaster-recovery-and-continuity-of-operations)
- [Appendix A](#appendix-a)
The Installation, Back-Out, Rollback Guide defines the ordered, technical steps required to install the product, and if necessary, to back-out the installation, and to roll back to the previously installed version of the product. It provides installation instructions for PSO\*7\*451, as managed through the State Prescription Monitoring Program (SPMP) Enhancement project.
During the implementation of PSO\*7\*408, it was discovered that some states had unique requirements that could not be addressed by current functionality. As a result transmissions to those states were rejected. Patch PSO\*7\*451 will enhance the SPMP functionality to allow VHA to fulfill specific state requirements and successfully transmit data to those states PDMPs. This patch also enhances the management of Secure SHell (SSH) Keys by streamlining the SSH Key creation and restricting user access to the Private SSH Key content. In addition, a few miscellaneous issues have also been addressed, which are described below.
All the changes introduced by this patch are related to the options under the State Prescription Monitoring Program (SPMP) Menu \[PSO SPMP MENU\] option which is located under the Supervisor Functions \[PSO SUPERVISOR\] menu option.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this Installation Guide is to provide installation steps for the SPMP Enhancement project patch PSO\*7\*451. The intended audience for this document is the Information Resources Management Service (IRMS) staff and Pharmacy staff responsible for installing and maintaining the Pharmacy files.

# Pre-installation and System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

PSO\*7\*437 is a required patch for PSO\*7\*451 so must be installed prior to installing PSO\*7\*451.

## System Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                               |                        |
|-------------------------------|------------------------|
| Package                       | Minimum Version Needed |
| VA FileMan                    | 22.0                   |
| Kernel                        | 8.0                    |
| MailMan                       | 8.0                    |
| Health Level 7                | 1.6                    |
| Order Entry/Results Reporting | 3.0                    |
| CMOP                          | 2.0                    |
| NDF                           | 4.0                    |
| Outpatient Pharmacy           | 7.0                    |
| Pharmacy Data Management      | 1.0                    |
| Controlled Substances         | 3.0                    |
| Toolkit                       | 7.3                    |
| Drug Accountability           | 3.0                    |

## Platform Installation and Preparation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Do not install this patch while Outpatient Pharmacy users are on the system. Installation will take no longer than three (3) minutes. Also, avoid scheduling this patch to install around 1:00 AM local time.

## Download and Extract Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Database Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Installation Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Cron Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

## Access Requirements and Skills Needed for the Installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N/A

# Installation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Installation from the Patch Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Use the INSTALL/CHECK MESSAGE option on the PackMan menu.
1.  From the Kernel Installation & Distribution System (KIDS) menu, select the Installation menu.
2.  From this menu, you may select to use the following options (when prompted for INSTALL NAME, enter PSO\*7.0\*451).
1.  Backup a Transport Global - This option will create a backup message of any routines exported with the patch. It will NOT back up any other changes such as DDs or templates.
1.  Compare Transport Global to Current System - This option will allow you to view all changes that will be made when the patch is installed. It compares all components of the patch (routines, DDs, templates, etc.).
2.  Verify Checksums in Transport Global - This option will ensure the integrity of the routines that are in the transport global.
3.  Print Transport Global - This option will allow you to view the components of the KIDS build.
3.  Use the Install Package(s) option and select the package PSO\*7.0\*451.
4.  When prompted "Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//" respond NO.
5.  When prompted "Want KIDS to INHIBIT LOGONs during the install? NO//" respond NO.
6.  When prompted "Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//" respond NO.

# Implementation Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Post-Install Routine (No Action Required)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The post-install routine in the patch PSO\*7\*451 will perform a few updates related to the SPMP functionality:

- The FILE ACCESS setting for the files below will be opened up so users can use FileMan to view and search their content. The files were unintentionally released in PSO\*7\*408 as restricted.
  - SPMP ASAP RECORD DEFINITION (#58.4)
  - SPMP EXPORT BATCH (#58.42)
- If SPMP parameters have been previously entered for a state, the new field/parameter RENAME FILE AFTER UPLOAD (#17) in the SPMP STATE PARAMETERS file (#58.41) will automatically be set to 1 (YES).
- If SPMP parameters have been previously entered for a state using Appriss AWARxE, the parameter setting workaround will be automatically corrected the following way:

<u>Before:</u>

     STATE SFTP SERVER IP ADDRESS: prodpmpsftp 54.175.203.159

     STATE SFTP SERVER USERNAME  : -oUser=username

<u>After:</u>

     STATE SFTP SERVER IP ADDRESS: sftp.pmpclearinghouse.net

     STATE SFTP SERVER USERNAME  : username@prodpmpsftp
- The mail group PSO SPMP NOTIFICATIONS will be changed to type PUBLIC. This mail group was incorrectly released as PRIVATE by PSO\*7\*408.

## Existing PSO SPMP NOTIFICATIONS Mailgroup (Action Required)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Subscribers to this mailgroup receive failure notifications regarding scheduled SPMP nightly transmissions to the states. Therefore, it is important that all pharmacy personnel involved with the SPMP transmissions subscribe to this mail group.

| ![](pso-7-451-state-prescription-monitoring-program-spmp-installation-guide/002.png) | Action: Verify the current subscribers of the PSO SPMP NOTIFICATIONS ADMIN mailgroup and add any pharmacy personnel that should be a member of the mailgroup and are not. |
|---------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## New PSO SPMP ADMIN Security Key (Action Required)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This new Security Key was created to restrict access to the following SPMP functionalities:

- ASAP Definition Customization updates through the View/Edit ASAP Definitions \[PSO SPMP ASAP DEFINITIONS\] option. Viewing the current ASAP Definition is not restricted.
- SPMP Parameters value updates through the View/Edit SPMP State Parameters \[PSO SPMP STATE PARAMETERS\] option. Viewing the current SPMP parameters is not restricted.
- SSH Key generation or replacement through the Manage Secure SHell (SSH) Keys \[PSO SPMP SSH KEY MANAGEMENT\] option. Viewing the current public key is not restricted.

| ![](pso-7-451-state-prescription-monitoring-program-spmp-installation-guide/003.png) | Action: The new security key PSO SPMP ADMIN should be assigned to the Outpatient Pharmacy coordinator at your site responsible for managing the State Prescription Monitoring Program (SPMP) functionality. |
|---------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## New RENAME FILE AFTER UPLOAD Parameter (May Require Action)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ![](pso-7-451-state-prescription-monitoring-program-spmp-installation-guide/004.png) | If your site is not currently transmitting SPMP data you can skip this step. |
|-------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|

| ![](pso-7-451-state-prescription-monitoring-program-spmp-installation-guide/005.png) | Action (Optional): If you are currently transmitting and you are aware that the renaming of the file is an issue for the state/vendor that you report to, you should set this parameter to NO. This is a known issue for West Virginia sites, so if your site is located in WV please set this field to NO. Please, see Appendix A for the full list of states that should have this parameter set to NO. |
|---------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

This new parameter was introduced in the View/Edit SPMP State Parameters \[PSO SPMP STATE PARAMETERS\] option to control whether the data export file should be created and uploaded with a .DAT (or .TXT) extension directly or if the file should be created and uploaded with a .UP extension and once the upload completes the file would be renamed to .DAT (or .TXT). This new parameter is being exported with a default value of YES.

NO - File will be uploaded as .DAT/.TXT directly (no renaming)

YES - File will be uploaded as .UP and then renamed to .DAT/.TXT

## New Transmission Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ![](pso-7-451-state-prescription-monitoring-program-spmp-installation-guide/006.png) | If your site is currently successfully transmitting data to the SPMP you can skip the subsequent installation steps as no further configuration is necessary. Just make sure the transmissions are not interrupted due to the installation of this patch by making sure the state has successfully received your data transmission in the days following this installation. |
|--------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

If your site has never transmitted data to the SPMP or if it did in the past but is no longer transmitting, or if your transmissions are not being successfully accepted due to issues related to state specific requirements or blocked connection, follow the steps below to successfully configure and perform SPMP data transmission.

### Register your Outpatient Pharmacy site with the SPMP (Action Required)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you haven’t yet registered with your SPMP you need to do so prior to transmitting data to them. In summary, you have to gather the Pharmacy information such as Pharmacy Name, Address, Phone \#, DEA \#, and NPI \#, and then fill out a form which is usually available online at their website where you can also find a detailed Implementation Guide. You must specify that you will be reporting data via Secure File Transfer Protocol (sFTP) using Secure SHell (SSH) Encryption keys. Some states refer to such type of registration as “sFTP Uploaders”.

Once you successfully register with the SPMP they will provide you with the following information: ASAP Version (e.g., 4.2), your assigned Username, the SPMP Server IP Address and in some cases the Port Number. They may also specify a specific Directory at their server where they want the data to be uploaded to. You will need this information when configuring the transmission in VistA.

Pharmacy Benefits Management (PBM) maintains a SharePoint site that might be a good source of information regarding the registration process.

<span class="mark">REDACTED</span>

### Open Network Traffic between your site and the SPMP (Action Required)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before you can start transmitting data to your SPMP your local site needs to work with the appropriate local.VA Regional and National support to request that the SSH traffic between your site and the state server be open for SPMP transmissions. This process consists of submitting a request through the <span class="mark">REDACTED</span>. This is a complex request and requires a number of steps to get it accomplished. Please, refer to the following document in the PBM repository for instructions on how to submit a request for your site:

<span class="mark">REDACTED</span>

Repository:

<span class="mark">REDACTED</span>

### OpenVMS Directory (May Require Action)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ![](pso-7-451-state-prescription-monitoring-program-spmp-installation-guide/007.png) | If your site has fully migrated to Linux you can skip this step. |
|-------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|

If your site has not fully migrated to Linux you will need a new OpenVMS directory (e.g. USER\$:\[SPMP\]) to be used by the SPMP transmissions. The proposed naming convention is only a recommendation. A more knowledgeable and experienced System Manager may choose to setup the extract directory using existing drives and definitions. The directory name chosen must have the appropriate READ, WRITE, EXECUTE, and DELETE privileges. You must have administrator privileges when you perform this task in order to assure the directory is set up/created with the necessary permissions.

The following is an example for you to follow to create the file transmission directory.

\$ CREATE/DIRECTORY USER\$:\[SPMP\] /own=CACHEMGR /PROTECTION=(S:RWED,O:RWED,G:RWED,W:RWED)/LOG

<u>NOTE:</u>

• The owner of the directory should be CACHEMGR.

• Where USER\$=the disk of your choice (e.g. USER\$, PQ\$, etc. - SYS\$ is not recommended).

• Confirm that the extract directory has similar protections and permissions.

\$DIR/PROT/OWNER SPMP.DIR

Directory USER\$:\[000000\]

SPMP.DIR;1 \[CACHEMGR\] (RWED,RWED,RWED,RWED)

| ![](pso-7-451-state-prescription-monitoring-program-spmp-installation-guide/008.png) | Action: Once the directory has been created, please pass this directory name (e.g., “USER\$:\[SPMP\]”) to the ADPAC/Pharmacy Chief/Pharmacy Informaticist. This will be used in the SPMP Site parameters “Outlined Below”. |
|---------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

### SPMP State Parameter Configuration (Action Required)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Next, you will need to work with the pharmacy ADPAC to correctly enter the SPMP parameters through the View/Edit SPMP State Parameters \[PSO SPMP STATE PARAMETERS\] option, which are explained below individually:

| ![](pso-7-451-state-prescription-monitoring-program-spmp-installation-guide/009.png) | The View/Edit SPMP State Parameters \[PSO SPMP STATE PARAMETERS\] option requires the PSO SPMP ADMIN Security Key for editing the parameters (see step 4.2). |
|---------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|

STATE  
Select the state that you want to enter, view or edit the SPMP parameters. There should be an entry for all states in which there is a physical Outpatient Pharmacy facility that either dispenses outpatient prescriptions or orders Consolidated Mail Outpatient Pharmacy (CMOP) prescriptions to be dispensed.

ASAP VERSION  
This is the American Society for Automation in Pharmacy (ASAP) version required for the SPMP data transmission which was obtained during Step 4.4.1. It should be one of the following versions: 1995, 3.0, 4.0, 4.1 or 4.2.

INCLUDE NON-VETERAN PATIENTS  
This field indicates whether controlled substances prescriptions dispensed to non-veteran patients should be included in the export file transmitted to a state. Due to VHA Regulations in place at the time of the release of this patch this field should be set to “NO”.

REPORTING FREQUENCY IN DAYS  
This is the frequency at which a state requires pharmacies to report data. The value must be entered in days and cannot be greater than 30. Example: 1 (daily), 7 (weekly), 3 (every 3 days), etc. This field should be set to 1 (one).

OPEN VMS LOCAL DIRECTORY  
If your site has fully migrated to Linux you can leave this field blank. Otherwise, you will need to fill this parameter with the local OpenVMS directory created on step 4.4.3 above.

UNIX/LINUX LOCAL DIRECTORY  
This is the name of the local Unix/Linux local directory where the SPMP export file will be created before it can be transmitted to the state (e.g., /srv/vista/okl/user/sftp/spmp/). When running this option for the first time there will be default directory (e.g., /srv/vista/okl/user/sftp/spmp/) and the option may prompt you for the following after pressing \<RET\> through it:

> The directory above could not be found.

> Would you like to create it now? N//

Answer YES.

FILE NAME PREFIX  
This is the prefix that will be appended to the name of the export file transmitted to the state. If the state has no specific requirement, the recommendation is that you use ‘SPMP\_\<Site \#\>\_’ format (e.g.,’SPMP_500\_’).

FILE EXTENSION  
The SPMP Implementation Guide for each specific state usually specifies which extension you should choose. If you’re unable to determine this information choose .DAT which is the most commonly used.

RENAME FILE AFTER UPLOAD  
This parameter controls whether the data export file should be created and uploaded with a .DAT (or .TXT) directly or if the file should be created and uploaded with a .UP extension and once the upload completes the file would be renamed to .DAT (or .TXT). This new parameter is being exported with a default value of YES. If you are not sure how to answer this parameter, leave it set to “YES”.

STATE SFTP SERVER IP ADDRESS  
This is the state sFTP IP address of the SPMP server to which the export file will be transmitted. This information should have been provided to you when you registered with the SPMP (Step 4.4.1).

STATE SFTP SERVER USERNAME  
This is the state sFTP username of the SPMP server to which the export file will be transmitted. This information should have been provided to you when you registered with the SPMP (Step 4.4.1).

STATE SFTP SERVER PORT \#  
This is the Port \# used by the state sFTP server to receive data. Usually states use the default sFTP port \#22 and in this case it does not need to be entered. This information should have been provided to you when you registered with the SPMP (Step 4.4.1) or it can be found in the SPMP Implementation Guide.

STATE FTP SERVER DIRECTORY  
This is the name of the remote state directory of the SPMP server to which the export file will be saved. Usually states do not require the file to be placed in a specific directory and in this case this field should be left blank. If required, this information can usually be found in the SPMP Implementation Guide.

SFTP TRANSMISSION MODE

> This field indicates whether the sFTP transmissions will happen automatically by a scheduled background job using SSH encryption keys or if it will be performed manually by a user. Please, choose “A” for Automatic Transmissions.

Example: View/Edit SPMP State Parameters \[PSO SPMP STATE PARAMETERS\]

Select State Prescription Monitoring Program (SPMP) Menu Option: SP View/Edit SPMP State Parameters

Select STATE: NEBRASKA// NEBRASKA

ASAP VERSION: 4.2// 4.2 ASAP 4.2

INCLUDE NON-VETERAN PATIENTS: NO// NO

REPORTING FREQUENCY IN DAYS: 1// 1

OPEN VMS LOCAL DIRECTORY: USER\$:\[SPMP\]

UNIX/LINUX LOCAL DIRECTORY: /srv/vista/neb/user/sftp/spmp/

Replace

The directory above could not be found.

Would you like to create it now? N// YES

FILE NAME PREFIX: SPMP\_

RENAME FILE AFTER UPLOAD: NO// YES

FILE EXTENSION: .DAT// .DAT

STATE SFTP SERVER IP ADDRESS: 999.99.9.99

STATE SFTP SERVER USERNAME: VAUSERNAME

STATE SFTP SERVER PORT \#:

STATE SFTP SERVER DIRECTORY:

SFTP TRANSMISSION MODE: A// AUTOMATIC \[RSA KEYS\]

### Create a new SSH Key Pair (Action Required)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once the SPMP State parameters have been entered the next step is to create a pair of SSH encryption keys that will be used for authenticating the sFTP connection to the state automatically bypassing the need for the user to type in an sFTP password. This will enable the transmissions to be scheduled to run overnight through TaskMan. Use the Manage Secure SHell (SSH) Keys \[PSO SPMP SSH KEY MANAGEMENT\] option and follow the steps below:

| ![](pso-7-451-state-prescription-monitoring-program-spmp-installation-guide/010.png) | The Manage Secure SHell (SSH) Keys \[PSO SPMP SSH KEY MANAGEMENT\] option requires the PSO SPMP ADMIN Security Key for creating or deleting SSH Key pairs (see step 4.2). |
|---------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

#### Verify that you don’t have an SSH Key pair in place for the state you are trying to set up transmissions. You can use the Action ‘V’ (View Public SSH Key) for this purpose, as seen in the example below:

> Select STATE: NEBRASKA//

> Select one of the following:

> V View Public SSH Key

> N Create New SSH Key Pair

> D Delete SSH Key Pair

> H Help with SSH Keys

> Action: V// v View Public SSH Key

> \[No SSH Key Pair found for NEBRASKA\]

> Press Return to continue:

The message \[No SSH Key Pair found for NEBRASKA\] displayed above indicates that there are no SSH keys for the state of Nebraska meaning that it is okay to proceed with the creation of a new SSH Key Pair.

#### If you are not sure how to create and share the Public SSH Key invoke the Action ‘H’ for detailed information to help you successfully create and share the key with the state.

> Action: V// Help with SSH Keys

> Secure SHell (SSH) Encryption Keys are used to automate the data transmission to the State Prescription Monitoring Programs (SPMPs). Follow the steps below to successfully setup SPMP transmissions from VistA to the state/vendor server:

> Step 1: Select the 'N' (Create New SSH Key Pair) Action and follow the

> Prompts to create a new pair of SSH keys. If you already have

> an existing SSH Key Pair you can skip this step.

> You can check whether you already have an existing SSH Key Pair

> through the 'V' (View Public SSH Key) Action.

> Encryption Type: DSA or RSA?

> ----------------------------

> Digital Signature Algorithm (DSA) and Rivest, Shamir & Adleman

> (RSA) are two of the most common encryption algorithms used by

> the IT industry for securely sharing data. The majority of SPMP

> servers can handle either type; however there are vendors that

> accept only one specific type. You will need to contact the

> SPMP vendor support to determine which type to select.

> Step 2: Share the Public SSH Key content with the state/vendor. In

> order to successfully establish SPMP transmissions the

> state/vendor will have to install/configure the new SSH Key

> created in step 1 for the user id they assigned to your site.

> Use the 'V' (View Public SSH Key) Action to retrieve the

> content of the Public SSH key. The Public SSH Key should not

> contain line-feed characters, therefore after you copy & paste

> it from the terminal emulator into an email or text editor make

> sure it contains only one line of text (no wrapping).

#### Once you have read the Help text above proceed to creating the SSH Key Pair by selecting the Action ‘N’ (Create New SSH Key Pair)

> Action: V// n Create New SSH Key Pair

> Enter your Current Signature Code: SIGNATURE VERIFIED

> Select one of the following:

> DSA Digital Signature Algorithm (DSA)

> RSA Rivest, Shamir & Adleman (RSA)

> SSH Key Encryption Type: DSA// ?

> Digital Signature Algorithm (DSA) and Rivest, Shamir & Adleman

> (RSA) are two of the most common encryption algorithms used by

> the IT industry for securely sharing data. The majority of SPMP

> servers can handle either type; however there are vendors that

> accept only one specific type. You will need to contact the

> SPMP vendor support to determine which type to select.

> Select one of the following:

> DSA Digital Signature Algorithm (DSA)

> RSA Rivest, Shamir & Adleman (RSA)

> SSH Key Encryption Type: DSA// Digital Signature Algorithm (DSA)

> Confirm Creation of SSH Keys for NEBRASKA? NO// YES

> Creating New SSH Keys, please wait...Done.

#### Once you have created the new SSH Key Pair use the Action ‘V’ (View Public SSH Key) one more time to retrieve the content of the Public SSH Key so that you can share with the state.

> Action: V// View Public SSH Key

> NEBRASKA's Public SSH Key (DSA) content (does not include dash lines):

> -----------------------------------------------------------------------

> ssh-dss NzaC1kc3MAAACBAOVOrS3sCHlFheWjM8wT0JHEtCx37c+0IRD0IJLjQIs0WLXvj

> 2qW/67OxYWymNqNVBWrUf1qoVbOkXtSAlnXp1ZtbMdZbkzeRIvUCG5PYx8RHHqI/BOZ604S

> JVJXdXAB2Z1JzOs/9Yhh9XCcwv1gJG5SMYtHvAAAAFQCWQqn1nhbsdePmMq+v543zDx0Scw

> sOqMj1HjVNjzjylpjbGBjh5QY+MhXxc0CtMZodvNV4aNukIU3MJ4w8hq9NnBA4U7dIrIgWo

> UlFRjK7yCwb3POCe/jxaefLJfqzZ7pUXIuSG1Vpn+adas7cASAUPlgJ/fwWBOUrB2aDhQJy

> fXhPLf1a0S0AAACAb+gJQb/Cx9Rl5vNdBbgbZ7myjpMoTTsSRJ9kUhxjJwuxDURA/9E17Oh

> kWgPZ3lFFGamsLniUDJIDGJTMod+XsfG04+leMR0PQbhHRnxhOL0VSQDSQuoENlt4WAeJpw

> ri74CZMBsJIKpn6vy3y37zil4OA=

> -----------------------------------------------------------------------

| ![](pso-7-451-state-prescription-monitoring-program-spmp-installation-guide/011.png) | Action: You will need to share the text content above (between the dash lines)with the state/vendor so they can install it on their server. The Public SSH Key sent to the vendor should not contain line-feed characters. After you copy & paste it from the terminal emulator into an email or text editor, make sure it contains only one line of text (no wrapping). |
|---------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

### Customize the ASAP Definition with state specific data requirements (May Require Action)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| ![](pso-7-451-state-prescription-monitoring-program-spmp-installation-guide/012.png) | If your state is not listed in the Appendix A at the end of this document you can skip this step. |
|-------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------|

Before you execute this step, go to the Appendix A in this document and verify if the state you are setting up transmissions for is listed. If so, take note of the specific customizations your state requires and use the View/Edit ASAP Definitions \[PSO SPMP ASAP DEFINITIONS\] option to perform the required adjustments so that your state will accept the data from your site.

| ![](pso-7-451-state-prescription-monitoring-program-spmp-installation-guide/013.png) | The View/Edit ASAP Definitions \[PSO SPMP ASAP DEFINITIONS\] option requires the PSO SPMP ADMIN Security Key for customizing the ASAP Definition Segments and Data Elements (see step 4.2). |
|---------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

| ![](pso-7-451-state-prescription-monitoring-program-spmp-installation-guide/014.png) | The specific customizations listed in the Appendix A have been identified as of February 2016. Therefore, please check with the SPMP of your state to make sure no additional specific requirements have been made since then. |
|---------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

Example 1: Customizing the AIR Segment (Additional Information Reporting) from NOT USED to REQUIRED through the View/Edit ASAP Definitions \[PSO SPMP ASAP DEFINITIONS\] option.

<u>ASAP Standard Version 4.2 Feb 25, 2016@11:35:59 Page: 1 of 1</u>

Element Delimiter: \* Segment Terminator: ~ End Of Line ESC: \$C(13,10)

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

MAIN HEADER

TH - Transaction HeaderIS - Information Source

PHARMACY HEADER

PHA - Pharmacy Header

PATIENT DETAIL

PAT - Patient Information

PRESCRIPTION DETAIL

DSP - Dispensing RecordPRE - Prescriber Information

CDI - Compound Drug Ingredient Detail (Not Used)

AIR - Additional Information Reporting (Not Used)

PHARMACY TRAILER

TP - Pharmacy Trailer

MAIN TRAILER

TT - Transaction Trailer

\+ Enter ?? for more actions\|\* Custom Segment/Element

CV Copy ASAP Version CE Customize Element ED Edit Delimiters

CS Customize Segment DC Delete Customization SH Show/Hide Details

Select Item(s): Quit// CS Customize Segment

SEGMENT ID: AIR Additional Information Reporting

REQUIREMENT: N// ?

Indicate if the segment is required, optional or not used by the ASAP

version.

Choose from:

R REQUIRED

O OPTIONAL

N NOT USED

REQUIREMENT: N// <span class="mark">REQUIRED</span>

Save Custom Segment? YES// YES Saving...OK

Example 2: Customizing the PAT17 Data Element (Patient’s Phone Number), which was requested by Massachusetts to be reported as “9999999999” when no phone number can be found for the patient. The current standard/default value for this field will be Pharmacy phone number if no valid phone number can be found for the patient.

\+ Enter ?? for more actions\|\* Custom Segment/Element

CV Copy ASAP Version CE Customize Element ED Edit Delimiters

CS Customize Segment DC Delete Customization SH Show/Hide Details

Select Item(s): Quit// CE Customize Element

DATA ELEMENT ID: PAT17 Phone Number

MAXIMUM LENGTH: 10// 10

REQUIREMENT: O// OPTIONAL

M SET EXPRESSION: \$\$PAT17^PSOASAP()// \$S(\$\$PAT17^PSOASAP()=\$\$PHA10^PSOASAP():"9999999999",1:\$\$PAT17^PSOASAP())

Save Custom Data Element? YES// Saving...OK

### Test the Transmission (Action Required)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once the state/vendor confirms installation of the SSH Key it is recommended that the site test the connection through a test transmission of a single prescription fill to make sure it is working properly. Search for a recently released Controlled Substance prescription and use the View/Export Single Prescription \[PSO SPMP SINGLE RX VIEW/EXPORT\] option to perform this step as shown below:

PRESCRIPTION: 999999 OXYCODONE HCL 5MG TABLET

Select one of the following:

0 Original (6/25/15) WINDOW

Fill: 0// Original (6/25/15) WINDOW

<u>View/Export Prescription Feb 25, 2016@09:08:46 Page: 1 of 6</u> Rx: 999999 - OXYCODONE HCL 5MG TABLET (Fill: Original)

Patient: TESTPATNAM,OUTPATIENT1 ASAP Version: 4.2

<u>\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_</u>

<u>TH Transaction Header</u>

TH\*4.2\*635-0\*01\*\*20160225\*090846\*T\*\*\~~

4.2 TH01 Version / Release Number

635-0 TH02 Transaction Control Number

01 TH03 Transaction Type

\* TH04 Response ID

20160225 TH05 Creation Date

090846 TH06 Creation Time

T TH07 File Type

\* TH08 Routing Number

~ TH09 Data Segment Terminator Character

<u>IS Information Source</u>

IS\*VA635\*OKLAHOMA CITY VA MEDICAL CENTER\*~

VA635 IS01 Unique Information Source ID

OKLAHOMA CITY VA MEDICAL CENTER IS02 Information Source Entity Name

\* IS03 Message

\+ Enter ?? for more actions\|\* Custom Segment/Element

VW View Rx AS View ASAP Definition

MP Medication Profile EXP Export Rx Fill

Select Item(s): Next Screen// EXP Export Rx Fill

Enter the type of record to be sent for this prescription fill:

N NEW

R REVISE

Record Type: NEW//

The Prescription Fill will be transmitted to the State

Confirm? N// y YES

Creating Batch \#999 for NEBRASKA...Done.

Exporting Batch \#999:

Writing to file /srv/vista/neb/user/sftp/spmp/SPMP_201602250909.UP...Done.

Transmitting file to the State (999.99.9.99)...

sFTP Server 6.4.0 Build 11.18.2011.31

File Successfully Transmitted.

Press Return to continue:

# Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Back-out pertains to a return to the last known good operational state of the software and appropriate platform settings.

## Back-Out Strategy

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

See Section 5.6.

## Back-Out Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

None

### Load Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

None

### User Acceptance Testing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User Acceptance Testing in progress.

## Back-Out Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The project is canceled and the implemented features are no longer wanted by the stakeholders.

## Back-Out Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following New Service Requests (NSRs), Remedy Ticket and Patient Safety will not be addressed:

- NSR 20150701: State Prescription Monitoring Program Enhancement

## Authority for Back-Out

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The authority would come from the IPT and the project manager Scott Soldan.

## Back-Out Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Restore Pre-Patch Routines</u> (MailMan)

1.  Go to the Backup of Patch PSO\*7\*451 message in Mailman.
2.  At the <u>Enter message action</u> prompt, enter “X” to “Xtract PackMan”
3.  At the <u>Select PackMan Function</u> prompt, enter the number 6 to “Install/Check Message”
4.  At the end of this process the pre-patch routines are restored.

> **NOTE:** See header “Install the Patch Backup” for detail

<u>Install the Patch Backup</u>BACKUP PATCH Basket, 144 messages (1-144), 117 new

\*=New/!=Priority.....Subject....................................From...

>   141. Backup of Patch PSO\*7\*451 install on Mar 01, 2016   ADPAC,ONE

IN Basket Message: 1// 141

Subj: Backup of XXXXX install on Mar 01, 2016 \[#000000\] 03/01/16@11:14

2016 lines

From: ADPAC,ONE In 'IN' basket.   Page 1

-----------------------------------------------------------------------

\$TXT PACKMAN BACKUP Created on Thursday, 03/1/16 at 11:14:50 by ADPAC,ONE

Enter message action (in IN basket): Ignore// Xtract PackMan

Select PackMan function: 6  INSTALL/CHECK MESSAGE

> **WARNING:** Installing this message will cause a permanent update of globals

and routines.

Do you really want to do this? NO// YES

Routines are the only parts that are backed up.  NO other parts

are backed up, not even globals.  You may use the 'Summarize Message'

option of PackMan to see what parts the message contains.

Those parts that are not routines should be backed up separately

if they need to be preserved.

Shall I preserve the routines on disk in a separate back-up message? YES// NO

No backup message built.

Line 123  Message \#000000  Unloading Routine Routine_Name1 (PACKMAN_BACKUP)

Line 345  Message \#000000  Unloading Routine Routine_Name2 (PACKMAN_BACKUP)

Line 567  Message \#000000  Unloading Routine Routine_Name3 (PACKMAN_BACKUP)

Line 789  Message \#000000  Unloading Routine Routine_Name4 (PACKMAN_BACKUP)

====================================================================<u>New Routine(s)</u>

The new routines below distributed by the patch PSO\*7\*451 can be deleted/removed by using the following option: Delete Routines \[XTRDEL\]

PSOASAP

PSOSPMA3

PSOSPMB3

PSOSPMKY

PSOSPMU0

PSOSPMU2

PSOSPMU3

This option can be found under the Routine Tools menu.

Select OPTION NAME: XUPROG Programmer Options

KIDS Kernel Installation & Distribution System ...

NTEG Build an 'NTEG' routine for a package

PG Programmer mode

Calculate and Show Checksum Values

Delete Unreferenced Options

Error Processing ...

Global Block Count

List Global

Map Pointer Relations

Number base changer

Routine Tools ...

Test an option not in your menu

Verifier Tools Menu ...

Select Programmer Options \<TEST ACCOUNT\> Option: ROUTINE Tools

%Index of Routines

Check Routines on Other CPUs

Compare local/national checksums report

Compare routines on tape to disk

Compare two routines

Delete Routines

First Line Routine Print

Flow Chart Entire Routine

Flow Chart from Entry Point

Group Routine Edit

Input routines

List Routines

Load/refresh checksum values into ROUTINE file

Output routines

Routine Edit

Routines by Patch Number

Variable changer

Version Number Update

Select Routine Tools Option: DELEte Routines

ROUTINE DELETE

All Routines? No =\> No

Routine: ROUT999

Routine:

1 routine

1 routines to DELETE, OK: NO// YES

ROUT999

Done.<u>Other Components</u>

New data dictionaries, options, protocols and security keys modifications must be removed using a follow-up backout patch.

<u>File Name (#) Field Name (#) New/Modified/Deleted</u>

SPMP ASAP RECORD DEFINITION (#58.4)

VERSION sub-file (#58.4001)

DATA ELEMENT DELIMITER CHAR (#.02) New

SEGMENT TERMINATOR CHAR (#.03) New

END OF LINE ESCAPE CHAR(S) (#.04) New

SEGMENT sub-file (#58.40011)

LEVEL (#.06) New

DATA ELEMENT sub-file (#58.400111)

ELEMENT VALUE (M EXPRESSION) (#.08) New

SPMP STATE PARAMETERS (#58.41)

RENAME FILE AFTER UPLOAD (#17) New

SFTP SSH KEY FORMAT (#18) New

SFTP SSH KEY ENCRYPTION (#19) New

<u>Option Name New/Modified/Deleted</u>

PSO SPMP ASAP DEFINITIONS New

PSO SPMP SSH KEY MANAGEMENT New

<u>Protocols New/Modified/Deleted</u>

PSO SPMP3 COPY VERSION New

PSO SPMP3 CUSTOMIZE DATA ELEMENT New

PSO SPMP3 CUSTOMIZE SEGMENT New

PSO SPMP3 DELETE CUSTOMIZATION New

PSO SPMP3 EDIT DELIMETERS New

<u>Security Key New/Modified/Deleted</u>

PSO SPMP ADMIN New

# Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Rollback Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A follow-up rollback patch would be needed to remove new data entries established by the data dictionary.

> **NOTE:** These new data entries are the result of a fields added to the data dictionary or the modification of an existing field in the data dictionary.

## Rollback Criteria

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The <u>back-out</u> of the SPMP patch PSO\*7\*451 that modified existing fields, and established new fields would be justification for rollback.

## Rollback Risks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

None

## Authority for Rollback

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The authority for rollback would come from the project IPT and the VA project manager, Scott Soldan.

## Rollback Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In the situation where a rollback would be necessary, the development team will be contacted and a rollback patch will be provided to the site to install. The rollback patch will roll back changes that cannot be affected by the installation back out routines outlined in section 5.6.

# Additional Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you have any questions concerning the implementation of this application, contact the VA Service Desk at 1-855-673-4357 directly or log a ticket via CA Service Desk Manager (SDM) application using the Incident Area: NTL.APP.VistA.Outpatient Pharmacy 7_0

## Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Updated documentation describing the new functionality introduced by this patch is available.

The preferred method is to use Secure File Transfer Protocol (sFTP) to retrieve the files from <span class="mark">REDACTED</span>

This transmits the files from the first available sFTP server. Sites may also elect to retrieve software directly from a specific server as follows:

| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
|------------------------------------|------------------------------------|------------------------------------|
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |

The documentation will be in the form of Adobe Acrobat files.

| File Description                                           | File Name              | FTP Mode |
|------------------------------------------------------------|------------------------|----------|
| Outpatient Pharmacy V. 7.0 Manager's User Manual           | PSO_7_MAN_UM_R0816.PDF | Binary   |
| Outpatient Pharmacy V. 7.0 Technical Manual/Security Guide | PSO_7_TM_R0816.PDF     | Binary   |
| SPMP Enhancement Installation Guide                        | PSO_7_P451_IG.PDF      | Binary   |
| SPMP Enhancement Release Notes                             | PSO_7_P451_RN.PDF      | Binary   |

Documentation can also be retrieved from the VA Software Documentation Library (VDL) on the Internet at the following address:

<http://www.va.gov/vdl>

# Disaster Recovery and Continuity of Operations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each VistA facility as well as regional data center is responsible for its own Disaster Recovery (DR) and Continuity of Operations (COOP). Please refer to the VistA Disaster Recovery and Continuity of Operations Plans at the specific facility. Most of these documents are considered confidential, as they contain information that could disrupt any of these facilities’ DR or COOP and cause catastrophic data loss. Therefore, the following links are to be considered as examples and not definitive plans for every facility:

- <span class="mark">REDACTED</span>
- <span class="mark">REDACTED</span>

# Appendix A

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

State/Vendor Specific (unique) requirements.

| ![](pso-7-451-state-prescription-monitoring-program-spmp-installation-guide/015.png) | The specific customizations listed here have been identified as of July 2016. Therefore, please check with the SPMP of your state to make sure no additional specific requirements have been made since then. |
|---------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

<u>California (ASAP 4.1)</u>PHA11 – Contact Name

Customize this data element to transmit the Pharmacy DEA# concatenated with the letter “B” (e.g, “AV123456B”). See Example 2 under Section 4.4.6 above.

<u>M SET EXPRESSION: \$\$PAT17^PSOASAP()//\$\$PHA03^PSOASAP()\_"B"</u>

Segment Terminator

In the Example 1 in Section 4.4.2 above, instead of selecting CE (Customize Element) select ED (Edit Delimiters) and delete the SEGMENT TERMINATOR CHAR for ASAP version 4.1, as shown below:

Select Item(s): Quit// ED Edit Delimiters

ASAP Version 4.1 delimiters:

DATA ELEMENT DELIMITER CHAR: \*// \*

SEGMENT TERMINATOR CHAR: ~// @ Deleted.

SEGMENT TERMINATOR CHAR:

END OF LINE ESCAPE CHAR(S): \$C(13,10)// \$C(13,10)

Save Changes? YES// Y

Rename File After Upload Parameter

Use the View/Edit SPMP State Parameters \[PSO SPMP STATE PARAMETERS\] option and set parameter RENAME AFTER UPLOAD to “NO”.

Pharmacy DEA# List

Atlantic Associates Inc., the vendor for the California PMP, requires that you send a list of DEA \#’s for all pharmacies from your site that are dispensing controlled substance prescription in California so that they can configure them before you start transmitting data to the California PMP.

<u>Illinois (ASAP 4.1)</u>Segment Terminator

In the Example 1 in Section 4.4.2 above, instead of selecting CE (Customize Element) select ED (Edit Delimiters) and delete the SEGMENT TERMINATOR CHAR for ASAP version 4.1, as shown below:

Select Item(s): Quit// ED Edit Delimiters

ASAP Version 4.1 delimiters:

DATA ELEMENT DELIMITER CHAR: \*// \*

SEGMENT TERMINATOR CHAR: ~// @ Deleted.

SEGMENT TERMINATOR CHAR:

END OF LINE ESCAPE CHAR(S): \$C(13,10)// \$C(13,10)

Save Changes? YES// Y

Rename File After Upload Parameter

Use the View/Edit SPMP State Parameters \[PSO SPMP STATE PARAMETERS\] option and set parameter RENAME AFTER UPLOAD to “NO”.

Pharmacy DEA# List

Atlantic Associates Inc., the vendor for the Illinois PMP, requires that you send a list of DEA \#’s for all pharmacies from your site that are dispensing controlled substance prescription in Illinois so that they can configure them before you start transmitting data to the Illinois PMP.

<u>Massachusetts (ASAP 4.2)</u>AIR - Additional Information Reporting (Segment)

The REQUIREMENT field for the AIR segment should be changed from NOT USED to REQUIRED, as shown by Example 1 in Section 4.4.6 above.

AIR05 - ID of Person Dropping Off or Picking Up Rx

Customize this data element to always send “VADELIVERY” (No space between “VA” and “DELIVERY”)

M SET EXPRESSION: \$\$AIR05^PSOASAP()//"VADELIVERY "PAT02 – ID Qualifier

Customize this data element to send “99” (Other) instead of “07” (Social Security Number).

M SET EXPRESSION: \$\$PAT02^PSOASAP()//"99 "PAT03 – ID of Patient

Customize this data element to send the patient’s Integration Control Number (ICN) instead of the Social Security Number (SSN).

M SET EXPRESSION: \$\$PAT03^PSOASAP()//+\$\$GETICN^MPIF001(PATIEN)

PAT08 – First Name

Customize this data element to the patient’s last name if the patient’s first name is blank. The patient’s last name will be reported twice, in the PAT07 and PAT08 fields.

M SET EXPRESSION: \$\$PAT08^PSOASAP()// \$S(\$\$PAT08^PSOASAP()="":\$\$PAT07^PSOASAP(),1:\$\$PAT08^PSOASAP())PAT17 – Phone number

Customize this data element to send “9999999999” in case a valid phone number cannot be found for the patient. See Example 2 under Section 4.4.6 above.

M SET EXPRESSION: \$\$PAT17^PSOASAP()// \$S(\$\$PAT17^PSOASAP()=\$\$PHA10^PSOASAP():"9999999999",1:\$\$PAT17^PSOASAP())Rename File After Upload Parameter

Use the View/Edit SPMP State Parameters \[PSO SPMP STATE PARAMETERS\] option and set parameter RENAME AFTER UPLOAD to “NO”.

<u>Montana (ASAP 4.1)</u>IS01 Unique Information Source ID

Customize this data element to send the Registration \# that Montana SPMP assigned to the VA Pharmacy during the registration Process (e.g., 53871184 was the number assigned to the Ft. Harrison VAMC):

M SET EXPRESSION: \$\$IS01^PSOASAP()// \$S(\$\$GET1^DIQ(5,STATEIEN,1)=”MT”:"53871184",1:\$\$IS01^PSOASAP*(*))<u>Michigan (ASAP 4.2)</u>PAT02 – ID Qualifier

Customize this data element to send “99” (Other) instead of “07” (Social Security Number).

M SET EXPRESSION: \$\$PAT02^PSOASAP()//"99 "PAT03 – Patient ID

Customize this data element to always send “000000000” instead of the Social Security Number (SSN) because the SSN is not the board-required form of ID for the state of Michigan.

M SET EXPRESSION: \$\$PAT03^PSOASAP()// \$S(\$\$GET1^DIQ(5,STATEIEN,1)="MI":"000000000",1:\$\$PAT03^PSOASAP())Rename File After Upload Parameter

Use the View/Edit SPMP State Parameters \[PSO SPMP STATE PARAMETERS\] option and set parameter RENAME AFTER UPLOAD to “NO”.

<u>New York (ASAP 4.2)</u>DSP17 - Date Sold

The standard ASAP definition was released with this field set to NOT USED, however the New York SPMP requires it.

REQUIREMENT: N// REQUIRED

<u>West Virginia (ASAP 4.2)</u>Rename File After Upload Parameter

Use the View/Edit SPMP State Parameters \[PSO SPMP STATE PARAMETERS\] option and set parameter RENAME AFTER UPLOAD to “NO”.

<u>Wyoming (ASAP 4.1)</u>Segment Terminator

In the Example 1 in Section 4.4.2 above, instead of selecting CE (Customize Element), select ED (Edit Delimiters) and delete the SEGMENT TERMINATOR CHAR for ASAP version 4.1, as shown below:

Select Item(s): Quit// ED Edit Delimiters

ASAP Version 4.1 delimiters:

DATA ELEMENT DELIMITER CHAR: \*// \*

SEGMENT TERMINATOR CHAR: ~// @ Deleted.

SEGMENT TERMINATOR CHAR:

END OF LINE ESCAPE CHAR(S): \$C(13,10)// \$C(13,10)

Save Changes? YES// Y

Rename File After Upload Parameter

Use the View/Edit SPMP State Parameters \[PSO SPMP STATE PARAMETERS\] option and set parameter RENAME AFTER UPLOAD to “NO”.

Pharmacy DEA# List

Atlantic Associates Inc., the vendor for the Wyoming PMP, requires that you send a list of DEA \#’s for all pharmacies from your site that are dispensing controlled substance prescription in Wyoming so that they can configure them before you start transmitting data to the Wyoming PMP.

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: PSO*7*408 State Prescription Monitoring Program (SPMP) Installation Guide

## State FTP Parameter Setup (State Prescription Monitoring Program (SPMP) Menu Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From the State Prescription Monitoring Program (SPMP) Menu \[PSO SPMP MENU\], select the Supervisor Functions \[PSO SUPERVISOR\] menu option and select SP View/Edit SPMP State Parameters.

Select Supervisor Functions \<TEST ACCOUNT\> Option: State Prescription Monitoring

Program (SPMP) Menu

ASAP View ASAP Definitions

SP View/Edit SPMP State Parameters

RX View/Export Single Prescription

BAT View/Export Batch

BP Export Batch Processing

RP Accounting Of Disclosures Report

UN Unmark Rx Fill as Administered In Clinic

View/Edit SPMP State Parameters

The state’s parameters are displayed as follows:

Select STATE: NEW YORK//

ASAP VERSION : 4.2 (this may vary from state to state)

INCLUDE NON-VETERAN PATIENTS: NO

REPORTING FREQUENCY IN DAYS : 1

OPEN VMS LOCAL DIRECTORY : USER\$:\[SPMP\]

UNIX/LINUX LOCAL DIRECTORY :

WINDOWS/NT LOCAL DIRECTORY :

FILE NAME PREFIX : SPMP_999\_ (this is unique to your site)

eg. NJ_561\_ (New Jersey and the site number)

FILE EXTENSION : .DAT

STATE SFTP SERVER IP ADDRESS: Vendor IP Address

STATE SFTP SERVER USERNAME : VA (user name provided by the vendor)

STATE SFTP SERVER PORT \# :

STATE SFTP SERVER DIRECTORY :

SFTP TRANSMISSION MODE : AUTOMATIC \[RSA KEYS\](This key should be

provided to the vendor)

SFTP PRIVATE KEY TEXT : \<hidden\>

SFTP PUBLIC KEY TEXT : \<hidden\>

> **NOTE:** OPEN VMS LOCAL DIRECTORY name will be provided by the System Administrator.

## Directory setup by System Administrator

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 87%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Steps</strong></th>
<th><strong>Follow these Instructions</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><strong>Step</strong></p>
<p>1</p></td>
<td><p><strong>File Transmission Directory Setup</strong></p>
<p>NOTE: The naming convention for directories is different for each Operating System (OS).</p>
<p>Be sure to follow the instructions for your particular OS.</p>
<p>a. <strong><u>Cache / VMS Sites</u></strong></p>
<p>NOTE: The proposed naming convention is only a recommendation (this is an example). A more knowledgeable and experienced System Manager may choose to setup the extract directory using existing drives and definitions. The directory name chosen must have the appropriate READ, WRITE, EXECUTE, and DELETE privileges.</p>
<ol type="1">
<li><blockquote>
<p>Create and setup a new VMS Directory named USER$:[SPMP].</p>
</blockquote></li>
<li><blockquote>
<p>The new directory <u>must</u> have READ, WRITE, EXECUTE, and DELETE privileges for the currently installed Cache instance (this might change from site to site).</p>
</blockquote></li>
</ol>
<blockquote>
<p>You must have administrator privileges when you perform this task in order to assure the directory is setup/created with the necessary permissions.</p>
<p>The following is an example for you to follow to create the file transmission directory.</p>
</blockquote>
<p>$ CREATE/DIRECTORY USER$:[SPMP] /own=CACHEMGR</p>
<p>/PROTECTION=(S:RWED,O:RWED,G:RWED,W:RWED)/LOG</p>
<blockquote>
<p>NOTE:</p>
</blockquote>
<ul>
<li><p>The owner of the directory should be CACHEMGR.</p></li>
<li><p>Where USER$=the disk of your choice (e.g. USER$, PQ$, etc. - SYS$ is not recommended).</p></li>
<li><p>Confirm that the extract directory has similar protections and permissions.</p></li>
</ul>
<p>$DIR/PROT/OWNER SPMP.DIR</p>
<p>Directory USER$:[000000]</p>
<p>SPMP.DIR;1           [CACHEMGR]            (RWED,RWED,RWED,RWED)</p>
<blockquote>
<p>NOTE: Please pass this directory name to the ADPAC/Pharmacy Chief/Pharmacy Informaticist</p>
</blockquote>
<p>b<strong><u>. Cache / MS Windows or NT Sites</u></strong></p>
<p>NOTE: The proposed naming conventions should be followed to avoid duplication. A more knowledgeable and experienced System Manager may choose to setup the extract directory using existing drives and definitions. The directory <u>must</u> have the appropriate READ, WRITE, EXECUTE, and DELETE privileges.</p>
<ol type="1">
<li><blockquote>
<p>Set up an MS Windows directory named D:\SPMP\.</p>
</blockquote></li>
<li><blockquote>
<p>The new directory <u>must</u> have READ, WRITE, EXECUTE, and DELETE privileges for the currently installed MS Windows instance.</p>
</blockquote></li>
</ol>
<blockquote>
<p>You must have administrator privileges when you perform this task in order to assure the directory is setup/created with the necessary permissions.</p>
</blockquote>
<p><strong>SPECIAL INSTRUCTIONS FOR WINDOWS/NT STATIONS</strong></p>
<p>The directory set up in the example is D:\SPMP. You <u>must</u> append a backslash ( \ ) to the MS Windows directory name when you enter a value in the View/Edit SPMP State Parameters [PSO SPMP STATE PARAMETERS] option in the VMS LOCAL DIRECTORY: field.</p>
<p>For example: D:\SPMP\</p></td>
</tr>
</tbody>
</table>

## Coordinator for Mail Group (PSO SPMP NOTIFICATIONS)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the background job fails to transmit the data to the state, a MailMan message is generated and sent to the subscribers of the PSO SPMP NOTIFICATIONS mail group. Below is an example of the message.

Example: \[PSO SPMP NOTIFICATIONS\]

Subj: NEW YORK Prescription Monitoring Program Transmission Failed  \[#194821\]

01/17/13@15:22  10 lines

From: SPMP SCHEDULED TRANSMISSION  In ‘IN’ basket.   Page 1

There was a problem with the transmission of information about Controlled

Substance prescriptions to the NEW YORK State Prescription Monitoring

Program (SPMP).

Batch \#: 54

Period : 10/10/12 thru 01/17/13

Error  : Error transmitting the file: %TCPIP-E-FTP_LOGREJ, login request rejected

Please, use the option Export Batch Processing \[PSO SPMP BATCH PROCESSING\] to

manually transmit this batch to the state.

Enter message action (in IN basket): Ignore//
