---
consolidated_title: "state prescription monitoring program (spmp) release notes"
app_code: PSO
doc_type: RN
master_source: "PSO*7*408 State Prescription Monitoring Program (SPMP) Release Notes"
master_pub_date: August 2014
consolidated_from: 2 versions
prior_versions:
  - "PSO*7*451 State Prescription Monitoring Program (SPMP) Release Notes"
---

> ![](pso-7-408-state-prescription-monitoring-program-spmp-release-notes/001.png)

State Prescription Monitoring Program (SPMP)Patch PSO\*7\*408Release Notes

August 2014

Product Development

Table of Contents

*(This page included for two-sided copying)*

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [New Menu with Options](#new-menu-with-options)
  - [New Files and Fields](#new-files-and-fields)
  - [New Templates](#new-templates)
  - [New Protocols](#new-protocols)
  - [New Routines](#new-routines)
  - [Mail Group](#mail-group)
  - [Security Keys](#security-keys)
  - [Patient Safety Issues](#patient-safety-issues)
- [Additional Information](#additional-information)
  - [Documentation](#documentation)
The State Prescription Monitoring Program (SPMP) menu is used to identify prescriptions for controlled substance drugs, Schedule 2 through 5, dispensed by Veterans Health Administration (VHA) Outpatient Pharmacy facilities, and to create and transmit an export file containing this information to the Prescription Drug Monitoring Program (PDMP) of each state. This menu allows VA Outpatient Pharmacies to comply with mandatory reporting to State Controlled Substance Rx databases as required by the Consolidated Appropriations Act, 2012, PL 112-74.
Each state has established its own PDMP to manage an electronic database that collects designated data on dispensed controlled substances. States distribute data from the database to individuals authorized under state law to receive the information for purposes of their profession. The information is reported to the state using the American Society for Automation in Pharmacy (ASAP) data format, which was developed by the Alliance of States with Prescription Monitoring Programs and the National Association of State Controlled Substances Authorities.
Notes:
1.  Prescription fills Administered in Clinic will not be sent to the states.
2.  Prescription fills Returned to Stock will send a VOID-type record to the state.
3.  The prescription transmissions to the states are recorded in the SPMP Activity Log section of each prescription.
4.  If the nightly background job responsible for transmitting prescriptions to the states fails, a MailMan message is sent to the recipients of the Mail Group PSO SPMP NOTIFICATIONS.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This release notes document provides a brief description of the new features and functions of the State Prescription Monitoring Program (SPMP) menu. More detailed information on the functionality can be found in the application user and technical manuals found on the Virtual Documentation Library (VDL).

## New Menu with Options 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 57%" />
<col style="width: 15%" />
<col style="width: 26%" />
</colgroup>
<thead>
<tr class="header">
<th>Option Name</th>
<th>Type</th>
<th>New/Modified/Deleted</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><p><em>Supervisor Functions</em> [PSO SUPERVISOR]</p>
<p>Note: This menu has been modified with the new sub-menu selection of State Prescription Monitoring Program Menu.</p></td>
<td>Menu</td>
<td>Modified</td>
</tr>
<tr class="even">
<td><p><em>State Prescription Monitoring Program (SPMP) Menu</em> [PSO SPMP MENU]</p>
<p>Note: The following seven options have been added under this new menu selection.</p></td>
<td>Menu</td>
<td>New</td>
</tr>
<tr class="odd">
<td><em>View ASAP Definitions</em> [PSO SPMP VIEW ASAP DEFINITIONS]</td>
<td>Action</td>
<td>New</td>
</tr>
<tr class="even">
<td><em>View/Edit SPMP State Parameters</em> [PSO SPMP STATE PARAMETERS]</td>
<td>Action</td>
<td>New</td>
</tr>
<tr class="odd">
<td><em>View/Export Single Prescription</em> [PSO SPMP SINGLE RX VIEW/EXPORT]</td>
<td>Action</td>
<td>New</td>
</tr>
<tr class="even">
<td><em>View/Export Batch</em> [PSO SPMP BATCH VIEW/EXPORT]</td>
<td>Action</td>
<td>New</td>
</tr>
<tr class="odd">
<td><em>Accounting Of Disclosures Report</em> [PSO SPMP DISCLOSURE REPORT]</td>
<td>Action</td>
<td>New</td>
</tr>
<tr class="even">
<td><p><em>Unmark Rx Fill as Administered In Clinic</em> [PSO SPMP UNMARK ADMIN CLINIC]</p>
<p>Note: The following nightly job option can be scheduled from the <em>Schedule/Unschedule</em> [XUTM SCHEDULE] option.</p></td>
<td>Action</td>
<td>New</td>
</tr>
<tr class="odd">
<td><em>Scheduled SPMP Data Export</em> [PSO SPMP SCHEDULED EXPORT]</td>
<td>Action</td>
<td>New</td>
</tr>
</tbody>
</table>

A detailed explanation of these new options are listed below.

The following options are under *Supervisor Functions* \[PSO SPMP MENU\]:

1.  *View ASAP Definitions* \[PSO SPMP VIEW ASAP DEFINITIONS\]  
    This option is used for viewing the ASAP data format and the data elements reported to the states. It provides detailed information about each segment and fields for the ASAP format versions 1995, 3.0, 4.0, 4.1, and 4.2.
2.  *View/Edit SPMP State Parameters* \[PSO SPMP STATE PARAMETERS\]  
    This option is used for viewing or editing the SPMP parameters for a specific state. The following fields can be updated via this option:
1.  ASAP VERSION  
    This is the format of the American Society for Automation in Pharmacy (ASAP) version required for the State Prescription Monitoring Program (SPMP) data transmission, which should be obtained from the State reporting authority.
- 1995 ASAP 1995
- 3.0 ASAP 3.0
- 4.0 ASAP 4.0
- 4.1 ASAP 4.1
- 4.2 ASAP 4.2
2.  TRANSMIT RETURN TO STOCK

    If ASAP Version is 1995 then this field will be prompted and indicates whether Return To Stock fills should automatically be transmitted to the state (in a separate file) or if reporting of such records will be handled manually. This field will not be shown if the ASAP Version is other than 1995.
3.  INCLUDE NON-VETERAN PATIENTS  
    This field indicates whether controlled substances prescriptions dispensed to non-veteran patients should be included in the export file transmitted to a state.
- 1 YES
- 0 NO
4.  REPORTING FREQUENCY IN DAYS  
    This is the frequency at which a state requires pharmacies to report data. The value represents the number of days between the transmissions of data to the state.
5.  OPEN VMS LOCAL DIRECTORY  
    This is the name of the local Open VMS secure directory where the State Prescription Monitoring Program (SPMP) export file will be created before it can be transmitted to the state (e.g., USER\$:\[SPMP\]).

> **NOTE:** If your site does not run VistA on an Open VMS operating system, this field can be left blank.

> **NOTE:** The directory name chosen must have the appropriate READ, WRITE, EXECUTE, and DELETE privileges. Further details can be found in the SPMP Installation Guide.

6.  UNIX/LINUX LOCAL DIRECTORY  
    This is the name of the local Unix/Linux secure directory where the State Prescription Monitoring Program (SPMP) export file will be created before it can be transmitted to the state (e.g., /usr/spmp/).

> **NOTE:** If your site does not run VistA on a Unix/Linux operating system, this field can be left blank.

7.  WINDOWS/NT LOCAL DIRECTORY  
    This is the name of the local Windows/NT secure directory where the State Prescription Monitoring Program (SPMP) export file will be created before it can be transmitted to the state (e.g., D:\SPMP\\.

> **NOTE:** If your site does not run VistA on a Windows/NT operating system, this field can be left blank.

8.  FILE NAME PREFIX  
    This is the prefix that will be appended to the name of the export file transmitted to the state

    (e.g., for New Jersey, station 561 “NJ_561\_”).
9.  FILE EXTENSION  
    This is the extension of the export file transmitted to the state.
- .TXT .TXT
- .DAT .DAT
10. STATE SFTP SERVER IP ADDRESS  
    This is the state FTP IP address of the State Prescription Monitoring Program (SPMP) server to which the export file will be transmitted (this should be obtained from the State reporting authority).
11. STATE SFTP SERVER USERNAME  
    This is the state FTP username of the State Prescription Monitoring Program (SPMP) server to which the export file will be transmitted (this should be obtained from the State reporting authority).
12. STATE SFTP SERVER PORT \#  
    This is the state FTP server port number of the State Prescription Monitoring Program (SPMP) server to which the export file will be transmitted.
13. STATE SFTP SERVER DIRECTORY  
    This is the name of the remote state directory of the State Prescription Monitoring Program (SPMP) server to which the export file will be saved.
14. SFTP TRANSMISSION MODE

    This field indicates whether the sFTP transmissions will happen automatically by a scheduled background job using RSA encryption keys or if it will be performed manually by a user.
15. SFTP PRIVATE KEY TEXT

    This is the Secure File Transfer Protocol (sFTP) private key text content. It is visible only if SFTP TRANSMISSION MODE is set to A - AUTOMATIC (refer to the SPMP Installation Guide for the private/public key details).
16. SFTP PUBLIC KEY TEXT

> This is the Secure File Transfer Protocol (sFTP) public key text content. It is visible only if SFTP TRANSMISSION MODE is set to A – AUTOMATIC

1.  *View/Export Single Prescription* \[PSO SPMP SINGLE RX VIEW/EXPORT\]  
    This option is used for viewing a specific prescription (the ASAP format of the prescription with all the segments and the medication profile). It also provides the option to manually transmit a prescription to the state.
2.  *View Export Batch* \[PSO SPMP BATCH VIEW/EXPORT\]  
    The information reported to a state is compiled into a batch, which can be for a single prescription or a collection of prescriptions, for a determined date range. This option is used for viewing information contained in one batch as well as the list of prescriptions in the batch. This option is also used to manually export a batch to the state.
3.  *Export Batch Processing* \[PSO SPMP BATCH PROCESSING\]  
    This option is used for monitoring all batches of data transmitted to the states. When users select a date range, a list of batches is presented from which they can select different actions to perform on a specific batch.
4.  *Accounting of Disclosures Report* \[PSO SPMP DISCLOSURE REPORT\]

> This option is used for generating a list of all prescriptions transmitted to states. This option allows for a date range selection as well as the selection of one, multiple, or all states and selection of one, multiple, or all patients. The list is sorted by state and then by patient.

5.  *Unmark Rx Fill as Administered In Clinic* \[PSO SPMP UNMARK ADMIN CLINIC\]

    This option is used for resetting the flag that indicates a prescription fill was 'Administered In Clinic'. The flag can only be set to 'No'. This option cannot be used to flag a window or mail prescription fill as 'Administered In Clinic'.

    The new background job, *Scheduled SPMP Data Export* \[PSO SPMP SCHEDULED EXPORT\], is scheduled by using the *Queue Background Jobs* \[PSO AUTOQUEUE JOBS\] option. This option is used for scheduling automatic transmission of batches to the states. It will regularly transmit the data to the state based on the parameters defined in the SPMP STATE PARAMETERS (#58.41) file. This option can also be accessed via the *Schedule/Unschedule* \[XUTM SCHEDULE\] option.

## New Files and Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| File Name                           | Field Name                          | New/Modified/Deleted |
|-------------------------------------|-------------------------------------|----------------------|
| SPMP ASAP RECORD DEFINITION (#58.4) |                                     | New                  |
|                                     | NAME (#.01)                         | New                  |
|                                     | VERSION (#1)                        | New                  |
|                                     | VERSION (#.01)                      | New                  |
|                                     | SEGMENT (#1)                        | New                  |
|                                     | SEGMENT ID (#.01)                   | New                  |
|                                     | SEGMENT NAME (#.02)                 | New                  |
|                                     | PARENT SEGMENT (#.03)               | New                  |
|                                     | REQUIREMENT (#.04)                  | New                  |
|                                     | POSITION (#.05)                     | New                  |
|                                     | DATA ELEMENT (#1)                   | New                  |
|                                     | ELEMENT ID (#.01)                   | New                  |
|                                     | ELEMENT NAME (#.02)                 | New                  |
|                                     | DATA FORMAT (#.03)                  | New                  |
|                                     | MAXIMUM LENGTH (#.04)               | New                  |
|                                     | POSITION (#.05)                     | New                  |
|                                     | REQUIREMENT (#.06)                  | New                  |
|                                     | DESCRIPTION (#.07)                  | New                  |
|                                     |                                     |                      |
| SPMP STATE PARAMETERS (#58.41)      |                                     | New                  |
|                                     | STATE (#.01)                        | New                  |
|                                     | ASAP VERSION (#1)                   | New                  |
|                                     | INCLUDE NON-VETERAN PATIENTS (#2)   | New                  |
|                                     | REPORTING FREQUENCY IN DAYS (#3)    | New                  |
|                                     | OPEN VMS LOCAL DIRECTORY (#4)       | New                  |
|                                     | FILE NAME PREFIX (#5)               | New                  |
|                                     | FILE EXTENSION (#6)                 | New                  |
|                                     | STATE FTP SERVER IP ADDRESS (#7)    | New                  |
|                                     | STATE FTP SERVER USERNAME (#8)      | New                  |
|                                     | STATE FTP SERVER PASSWORD (#9)      | New                  |
|                                     | STATE FTP SERVER DIRECTORY (#10)    | New                  |
|                                     | LAST EXPORT DATE/TIME RUN (#11)     | New                  |
|                                     | TRANSMIT RETURN TO STOCK (#12)      | New                  |
|                                     | UNIX/LINUX LOCAL DIRECTORY (#15)    | New                  |
|                                     | WINDOWS/NT LOCAL DIRECTORY (#16)    | New                  |
|                                     | SFTP PRIVATE KEY TEXT (#100)        | New                  |
|                                     | SFTP PUBLIC KEY TEXT (#200)         | New                  |
| SPMP EXPORT BATCH (#58.42)          |                                     | New                  |
|                                     | BATCH NUMBER (#.01)                 | New                  |
|                                     | STATE (#1)                          | New                  |
|                                     | EXPORT TYPE (#2)                    | New                  |
|                                     | BEGIN RELEASE DATE/TIME (#4)        | New                  |
|                                     | END RELEASE DATE/TIME (#5)          | New                  |
|                                     | EXPORT FILE NAME (#6)               | New                  |
|                                     | EXPORTED BY (#7)                    | New                  |
|                                     | DATE/TIME BATCH CREATED (#8)        | New                  |
|                                     | DATE/TIME BATCH EXPORTED (#9)       | New                  |
|                                     | ERRORS (#200)                       | New                  |
|                                     | ERROR MESSAGE (#.01)                | New                  |
|                                     | PRESCRIPTIONS (#100)                | New                  |
|                                     | PRESCRIPTION (#.01)                 | New                  |
|                                     | FILL (#1)                           | New                  |
|                                     | RECORD TYPE (#2)                    | New                  |
|                                     |                                     |                      |
| PRESCRIPTION (#52)                  |                                     | Modified             |
|                                     | ADMINISTERED IN CLINIC (#14)        | New                  |
|                                     | REFILL (#52.1)                      | Modified             |
|                                     | ADMINISTERED IN CLINIC (#23)        | New                  |
|                                     | RETURN TO STOCK LOG (#70)           | New                  |
|                                     |                                     |                      |
| RETURN TO STOCK LOG (#52.07)        |                                     | New                  |
|                                     | RETURN TO STOCK DATE/TIME (#.01)    | New                  |
|                                     | FILL NUMBER (#1)                    | New                  |
|                                     | FILL DATE (#2)                      | New                  |
|                                     | QUANTITY (#3)                       | New                  |
|                                     | DAYS SUPPLY (#4)                    | New                  |
|                                     | UNIT PRICE OF DRUG (#5)             | New                  |
|                                     | MAIL/WINDOW (#6)                    | New                  |
|                                     | REMARKS (#7)                        | New                  |
|                                     | PHARMACIST (#8)                     | New                  |
|                                     | LOT \# (#9)                         | New                  |
|                                     | CLERK (#10)                         | New                  |
|                                     | LOGIN DATE (#11)                    | New                  |
|                                     | DIVISION (#12)                      | New                  |
|                                     | IB NUMBER (#13)                     | New                  |
|                                     | COPAY EXCEEDING CAP (#14)           | New                  |
|                                     | DISPENSED DATE (#15)                | New                  |
|                                     | NDC (#16)                           | New                  |
|                                     | MANUFACTURER (#17)                  | New                  |
|                                     | DRUG EXPIRATION DATE (#18)          | New                  |
|                                     | PROVIDER (#19)                      | New                  |
|                                     | ADMINISTERED IN CLINIC (#20)        | New                  |
|                                     | RELEASED DATE/TIME (#21)            | New                  |
|                                     | GENERIC PROVIDER (#22)              | New                  |
|                                     | BINGO BOARD WAIT TIME (#23)         | New                  |
|                                     | FILLING PERSON (#24)                | New                  |
|                                     | CHECKING PHARMACIST (#25)           | New                  |
|                                     | PFSS ACCOUNT REFERENCE (#26)        | New                  |
|                                     | PFSS CHARGE ID (#27)                | New                  |
|                                     | DAW CODE (#28)                      | New                  |
|                                     | DATE/TIME NDC VALIDATED (#29)       | New                  |
|                                     | NDC VALIDATED BY (#30)              | New                  |
|                                     | BILLING ELIGIBILITY INDICATOR (#31) | New                  |
|                                     | EPHARMACY SUSPENSE HOLD DATE (#32)  | New                  |
|                                     |                                     |                      |

## New Templates

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Template Name                 | Type | New/Modified/Deleted |
|-------------------------------|------|----------------------|
| PSO SPMP BATCH PROCESSING     | List | New                  |
| PSO SPMP DISCLOSURE REPORT    | List | New                  |
| PSO SPMP VIEW ASAP DEFINITION | List | New                  |
| PSO SPMP VIEW/EXPORT BATCH    | List | New                  |
| PSO SPMP VIEW/EXPORT RX       | List | New                  |

## New Protocols

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Protocol Name                  | New/Modified/Deleted |
|--------------------------------|----------------------|
| PSO SPMP1 MANUAL BATCH EXPORT  | New                  |
| PSO SPMP1 MENU                 | New                  |
| PSO SPMP1 SELECT               | New                  |
| PSO SPMP1 STATE PARAMETERS     | New                  |
| PSO SPMP2 BATCH EXPORT         | New                  |
| PSO SPMP2 MENU                 | New                  |
| PSO SPMP2 SELECT               | New                  |
| PSO SPMP2 VIEW RAW DATA        | New                  |
| PSO SPMP3 MENU                 | New                  |
| PSO SPMP3 SHOW DETAILS         | New                  |
| PSO SPMP4 EXPORT RX            | New                  |
| PSO SPMP4 MEDICATION PROFILE   | New                  |
| PSO SPMP4 MENU                 | New                  |
| PSO SPMP4 VIEW ASAP DEFINITION | New                  |
| PSO SPMP4 VIEW RX              | New                  |
| PSO SPMP5 MENU                 | New                  |
| PSO SPMP5 SELECT               | New                  |

## New Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- PSO408PI
- [PSOASAP0](#_Toc330475130)
- PSORTSUT
- PSOSPML0
- PSOSPML1
- PSOSPML2
- PSOSPML3
- PSOSPML4
- PSOSPML5
- PSOSPML6
- PSOSPMSP
- PSOSPMU1
- PSOSPMUT

## Mail Group 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Mail Group Name    | New/Modified/Deleted |
|------------------------|--------------------------|
| PSO SPMP NOTIFICATIONS | New                      |

## Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No security keys have been added or modified by PSO\*7\*408.

## Patient Safety Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No patient safety issues (PSIs) have been associated with PSO\*7\*408.

# Additional Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you have any questions concerning the implementation of this application, contact the VA Service Desk at 1-888-596-4357 or directly log a Remedy ticket via Remedy Requester application using:

Category: Application-VistA

Type: Outpatient Pharmacy 7.0

Item: Other

## Documentation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Updated documentation describing the new functionality introduced by this patch is available.

The preferred method is to FTP the files from <span class="mark">REDACTED</span>

This transmits the files from the first available FTP server. Sites may also elect to retrieve software directly from a specific server as follows:

| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
|------------------------------------|------------------------------------|------------------------------------|
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |
| <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> | <span class="mark">REDACTED</span> |

The documentation will be in the form of Adobe Acrobat files.

| File Description                                           | File Name              | FTP Mode |
|------------------------------------------------------------|------------------------|----------|
| Outpatient Pharmacy V. 7.0 Manager's User Manual           | PSO_7_MAN_UM_R0814.PDF | Binary   |
| Outpatient Pharmacy V. 7.0 Technical Manual/Security Guide | PSO_7_TM_R0814.PDF     | Binary   |
| SPMP Installation Guide                                    | PSO_7_P408_IG.PDF      | Binary   |
| SPMP Release Notes                                         | PSO_7_P408_RN.PDF      | Binary   |

Documentation can also be retrieved from the VA Software Documentation Library (VDL) on the Internet at the following address:

<http://www4.va.gov/vdl>

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: PSO*7*451 State Prescription Monitoring Program (SPMP) Release Notes

## New Features and Functions Added

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are the new features and functions added to the SPMP Enhancement Patch PSO\*7.0\*451 release.

- New Security Key PSO SPMP ADMIN

This new security key was created to restrict access to the following SPMP functionalities:

- American Society for Automation in Pharmacy (ASAP) Definition Customization updates through the option View/Edit ASAP Definitions \[PSO SPMP ASAP DEFINITIONS\]. Visualization of the current ASAP Definition is not restricted.
- SPMP Parameters value updates through the option View/Edit SPMP State Parameters \[PSO SPMP STATE PARAMETERS\]. Visualization of the current SPMP parameters is not restricted.
- SSH Key generation or replacement through the option Manage Secure Shell (SSH) Keys \[PSO SPMP SSH KEY MANAGEMENT\]. Visualization of the current public key is not restricted.
- New option \[PSO SPMP SSH KEY MANAGEMENT\]

This new option completely hides the content of the Private SSH Key by removing them from the View/Edit SPMP State Parameters \[PSO SPMP STATE PARAMETERS\] option. This option is being introduced to allow management of the SSH Key functionality by the end-user, including generation, deletion and display of the public key.

- Full Customization Capabilities, including delimiters and End-Of-Line escape sequence

All ASAP standard Segments and Data Elements have been catalogued into VistA for versions 3.0, 4.0, 4.1 and 4.2. In addition, the View/Edit ASAP Definitions \[PSO SPMP ASAP DEFINITIONS\] option has been extensively modified to allow end-users manipulation of the final data content transmitted to state. Furthermore, end-users will also have the capability to create new ASAP versions by copying existing ones through this menu option.

- Rename file after upload now a parameter

The current transmission creates and sends the data file with the ".UP" file extension (for "upload"); once the file is transmitted a command within Secure File Transfer Protocol (sFTP) is issued to rename the file to the designated file extension set within the View/Edit SPMP State Parameters \[PSO SPMP STATE PARAMETERS\] option. This functionality was modified to allow the end-user to choose between creating and transmitting the file with the selected file extension, such as .DAT, or to create the file with a “.UP” extension, transmit it and then rename it. This new parameter is called RENAME FILE AFTER UPLOAD and can be updated through the View/Edit SPMP State Parameters \[PSO SPMP STATE PARAMETERS\] option.

- DSP17 (Date Sold) will now be reported

Previously not reported, the DSP17 Data Element will now be populated with the prescription fill released date.

- National Drug Code (NDC) for VOID will be the same as the NDC originally sent

When a VOID record is sent to the state the functionality will retrieve the actual NDC that was sent for the original record being voided. Before this patch the NDC was always retrieved from the NDC field (#31) in the DRUG file (#50) which could be different than the NDC for the original record.

## Enhancements and Modifications to Existing Functionality

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Mail Group PSO SPMP NOTIFICATIONS set to PUBLIC

> The mail group PSO SPMP NOTIFICATIONS was previously exported by patch PSO\*7.0\*408 as ‘Private’ and is now being modified to type ‘Public’.

- Misleading “File Successfully Transmitted” message for Linux OS now fixed

The previous algorithm used to identify whether the SPMP sFTP data transmission was successful was not 100% accurate for Linux Operating Systems. A new algorithm has been created and it will reflect the transmission status accurately.

- Option to Export Batch via the Background

When exporting an existing batch through the View/Export Batch \[PSO SPMP BATCH VIEW/EXPORT\] option the user will have the option to run the transmission on the Foreground or the Background. Previously manual transmissions always executed in the foreground. Adding the background option will help sites troubleshoot problems with the scheduled transmission which always runs on the background.

- “Hand-shaking” on non-Default Port \# issue resolved

When a transmission is first attempted it needs to “shake hands” with the new server before data can be exchanged between VistA and the new server. The previous patch PSO\*7.0\*408 did not take into account an alternate port \# (non-default 22) and failed to do the “hand-shaking” automatically. This patch addresses the problem.

- Field Lengths

The STATE SFTP SERVER IP ADDRESS (#7) and STATE SFTPSERVER USERNAME (#8) fields in the SPMP STATE PARAMETERS file (#58.41) have been expanded from 30 to 60 and 50 characters respectively.

- Phone Number fields

Phone number values have been restricted to a valid 10-digit numeric content. If such value cannot be found for a patient (e.g., PAT17) or a prescriber (e.g., PRE08) the pharmacy phone number is transmitted instead.

- VMS Log Capture

When a background transmission is performed on an OpenVMS Operating System and it fails, the sFTP transmission log will be captured in the Mailman message transmitted to the PSO SPMP NOTIFICATIONS mail group.

## Known Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no known issues specific to this release.
