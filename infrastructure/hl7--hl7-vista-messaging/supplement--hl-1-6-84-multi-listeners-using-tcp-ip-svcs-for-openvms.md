---
title: HL7 HL*1.6*84 Multi-Listeners Using TCP/IP Svcs for OpenVMS
doc_type: SUP
doc_label: Supplement
doc_layer: anchor
doc_subject: 
app_code: HL7
app_name: HL7 (VistA Messaging)
section: INF
app_status: active
pkg_ns: 
patch_ver: 1.6
patch_id: 
group_key: "HL7::1.6"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - service
  - table
  - port
  - hlseven
  - cache
  - contents
  - openvms
  - tcpip
  - command
  - number
page_count: 0
word_count: 9457
section_count: 29
table_count: 12
figure_count: 1
appendix_count: 0
has_toc: False
is_stub: False
pub_date: February 2004
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Health_Level_7_(HL7)/hl71_6p84sp.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Health_Level_7_(HL7)/hl71_6p84sp.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=8"
---

![](hl7-hl-1-6-84-multi-listeners-using-tcp-ip-svcs-for-openvms/001.png)

<span class="smallcaps">V*ist*A Health Level Seven (HL7)  
Multi-listeners using TCP/IP Services for OpenVMS</span><span class="smallcaps">Patch HL\*1.6\*84</span>

February 2004

Department of Veterans Affairs (VA)

VHA OI Health Systems Design & Development (HSD&D)

Messaging & Interface Services (M&IS)

<span id="_Toc2678770" class="anchor"></span>Revision History

The following table displays the revision history for this document. Revisions to the documentation are based on patches and new versions released to the field.

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 16%" />
<col style="width: 41%" />
<col style="width: 30%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Date</strong></td>
<td><strong>Revision</strong></td>
<td><strong>Description</strong></td>
<td><strong>Author</strong></td>
</tr>
<tr class="even">
<td>02/2004</td>
<td>HL*1.6*84</td>
<td><p>Supplement to patch description for Patch HL*1.6*84.</p>
<p>Patch HL*1.6*84 provides support for the use of OpenVMS TCP/IP Services for Caché/VMS. It also provides instructions for replacing existing TCP/IP services running on DSM/VMS.</p></td>
<td>REDACTED</td>
</tr>
</tbody>
</table>

Patch Revisions

For a complete list of patches related to this software, please refer to the Patch Module on FORUM.

<span id="_Toc83695347" class="anchor"></span><span class="smallcaps">Table of Contents</span>

<span id="_Toc2678771" class="anchor"></span><span class="smallcaps">Table of Figures</span>

[Figure 1: Multi-Threaded Listener link settings for DSM for OpenVMS using TCP/IP Services [5](#_Toc50862776)](#_Toc50862776)

[Figure 2: Multi-Threaded Listener link settings for CACHÉ for OpenVMS (using TCP/IP services) [17](#_Toc50862777)](#_Toc50862777)

#### <span id="_Toc2678772" class="anchor"></span>Orientation

This documentation uses several methods to highlight different aspects of the material. “Snapshots” of computer dialogue (or other online displays) are shown in a non-proportional font and enclosed within a box. User responses to on-line prompts are highlighted in boldface. Boldface is also used to highlight a descriptive word or sentence. The Return or Enter key is illustrated by the symbol \<Enter\> when displayed in computer dialogue and is included in examples only when it may be unclear to the reader that such a keystroke must be entered. The following example indicates that you should type two question marks followed by pressing the Return or Enter key when prompted to select an option:

Select Primary Menu option: ??

Figure 99: How to access online help

M (MUMPS – Massachusetts General Hospital Utility Multi-Programming System) code, variable names, acronyms, the formal name of options, actual field names, file names, and security keys are represented with all uppercase letters.

Various symbols are used throughout the documentation to alert the reader to special information. The following table gives a description of each of these symbols:

|                                                                                                     |                                                                                                       |
|-----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| Symbol                                                                                          | Description                                                                                       |
| ![](hl7-hl-1-6-84-multi-listeners-using-tcp-ip-svcs-for-openvms/002.png) | Used to inform the reader of general information including references to additional reading material. |
| ![](hl7-hl-1-6-84-multi-listeners-using-tcp-ip-svcs-for-openvms/003.png)                                                   | Used to caution the reader to take special notice of critical information.                            |

Assumptions about the Reader

This manual is written with the assumption that the reader is familiar with the following:

- <span class="smallcaps">V*ist*A</span> computing environment (e.g., Kernel Installation and Distribution System \[KIDS\]).
- VA FileMan data structures and terminology.
- M programming language.

Reference Materials

Readers who wish to learn more about the <span class="smallcaps">V*ist*A</span> Health Level Seven (HL7) software should consult the following:

- <span class="smallcaps">V*ist*A</span> Health Level Seven documentation is made available online in Adobe Acrobat Portable Document Format (PDF) at the [V*IST*A Documentation Library (VDL)](http://www.va.gov/vdl/Infrastructure.asp?appID=8).
- Patch HL\*1.6\*84 Installation Instructions can be found in the description for HL\*1.6\*84 located in the National Patch Module (i.e., Patch User Menu \[A1AE USER\]) on FORUM.

Readers who wish to learn more about the Health Level Seven (HL7), Inc., Standards should consult the <span class="smallcaps">V*ist*A</span> Health Level Seven (HL7) website: <http://vista.med.va.gov/messaging/hl7/index.asp> .

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [TCP/IP Services on OpenVMS](#tcpip-services-on-openvms)
  - [TCP/IP Services and VISTA HL7](#tcpip-services-and-vista-hl7)
  - [Requirements for Setting a TCP/IP Service on OpenVMS](#requirements-for-setting-a-tcpip-service-on-openvms)
    - [Pre-Configured DCL Command Procedure Files](#pre-configured-dcl-command-procedure-files)
  - [Recommended Naming Convention for OpenVMS Components](#recommended-naming-convention-for-openvms-components)
- [Creating a Multi-Threaded Listener for DSM on OpenVMS](#creating-a-multi-threaded-listener-for-dsm-on-openvms)
  - [Set Up a Logical Link in VISTA](#set-up-a-logical-link-in-vista)
  - [Create OpenVMS User Account](#create-openvms-user-account)
  - [Create OpenVMS Home Directory](#create-openvms-home-directory)
  - [Create a DCL Login Command Procedure](#create-a-dcl-login-command-procedure)
  - [Set Up and Enable the TCP/IP Service](#set-up-and-enable-the-tcpip-service)
    - [Set up the TCP/IP Service](#set-up-the-tcpip-service)
    - [Enable and Save the TCP/IP Service](#enable-and-save-the-tcpip-service)
  - [Access Control List (ACL) Issues](#access-control-list-acl-issues)
  - [Controlling the Number of Log Files Created by TCP/IP Services](#controlling-the-number-of-log-files-created-by-tcpip-services)
  - [Starting and Stopping the Listener](#starting-and-stopping-the-listener)
- [Replacing an Existing HLSEVEN Service with the HLS5000DSM Service for DSM on OpenVMS](#replacing-an-existing-hlseven-service-with-the-hls5000dsm-service-for-dsm-on-openvms)
  - [Disable the HLSEVEN TCP/IP Service](#disable-the-hlseven-tcpip-service)
  - [Remove the HLSEVEN TCP/IP Service](#remove-the-hlseven-tcpip-service)
  - [Create a DCL Login Command Procedure HLS5000DSM](#create-a-dcl-login-command-procedure-hls5000dsm)
  - [Set Up and Enable the TCP/IP Service](#set-up-and-enable-the-tcpip-service-1)
    - [Set Up the TCP/IP Service](#set-up-the-tcpip-service-1)
    - [Enable and Save the TCP/IP Service](#enable-and-save-the-tcpip-service-1)
- [Creating a Multi-Threaded Listener for Caché on OpenVMS](#creating-a-multi-threaded-listener-for-caché-on-openvms)
  - [Set Up Link](#set-up-link)
  - [Set Up OpenVMS User Account](#set-up-openvms-user-account)
  - [Set Up Home Directory for the HL7 User Account](#set-up-home-directory-for-the-hl7-user-account)
  - [Create a DCL Login Command Procedure for the HL7 User](#create-a-dcl-login-command-procedure-for-the-hl7-user)
  - [Set Up and Enable the TCP/IP Service](#set-up-and-enable-the-tcpip-service-2)
    - [Set Up the TCP/IP Service](#set-up-the-tcpip-service-2)
    - [Enable and Save the HLSEVEN TCP/IP Service](#enable-and-save-the-hlseven-tcpip-service)
  - [How to Control the Number of Log Files Created by TCP/IP Services](#how-to-control-the-number-of-log-files-created-by-tcpip-services)
  - [Starting and Stopping the Listener](#starting-and-stopping-the-listener-1)
- [Migration Instructions for DSM/VMS to Caché/VMS](#migration-instructions-for-dsmvms-to-cachévms)
  - [Disable the HL7 TCP/IP Service(s)](#disable-the-hl7-tcpip-services)
  - [Remove the HL7 TCP/IP Service(s)](#remove-the-hl7-tcpip-services)
  - [Modify the existing HLSEVEN User](#modify-the-existing-hlseven-user)
  - [Create a DCL Login Command Procedure HLS5000CACHE](#create-a-dcl-login-command-procedure-hls5000cache)
  - [Set Up and Enable the TCP/IP Service](#set-up-and-enable-the-tcpip-service-3)
    - [Set up the TCP/IP Service](#set-up-the-tcpip-service-3)
    - [Enable and Save the TCP/IP Service](#enable-and-save-the-tcpip-service-2)
- [Appendix](#appendix)
  - [HLSEVEN.COM DCL Login Command Procedure](#hlsevencom-dcl-login-command-procedure)
- [Glossary](#glossary)
This supplemental documentation is intended for use in conjunction with the Veterans Health Information System and Technology Architecture (V*IST*A) patch HL\*1.6\*84. It provides information that is specific to the use of the TCP/IP Services' functionality offered by the OpenVMS operating system.
Patch HL\*1.6\*84 has been created to provide the necessary code changes in the VistA HL7 package to enable Caché/VMS sites the external use of TCP/IP Services on OpenVMS for their multi-threaded listeners. This supplement to the patch includes instructions for V*IST*A sites that are planning to migrate to a Caché/VMS environment.
|                                                   |                                                                                                                                                                                                                                                                                                                          |
|---------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](hl7-hl-1-6-84-multi-listeners-using-tcp-ip-svcs-for-openvms/004.png) | Warning: After installation of patch HL\*1.6\*84, Cache/VMS sites will no longer have the capability of starting their multi-listeners through the V*IST*A HL7 options; therefore, Cache/VMS sites must immediately create and enable their multi-listeners as OpenVMS TCP/IP services, as described in this supplement. |
Current V*IST*A sites running on DSM/VMS already have the use of TCP/IP Services via the TCP/IP service HLSEVEN and patch HL\*1.6\*19. This supplement also includes instructions for DSM/VMS sites that will opt to change their current HLSEVEN service (and any other HL7 type service) to a TCP/IP service that conforms to the TCP/IP service configurations enforced by this supplement.

# TCP/IP Services on OpenVMS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Transmission Control Protocol/Internet Protocol (TCP/IP) is an open communications standard that enables any connected host to communicate with any other connected host. The 'TCP/IP Services' for OpenVMS is a product that implements several of the protocols in the TCP/IP standard for the OpenVMS operating system. This supplement focuses only on those TCP/IP services configured to run as a TCP/IP server (listener) process.

## TCP/IP Services and V*IST*A HL7

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A TCP/IP service configured to run as a server permits multiple remote TCP/IP clients to connect and run concurrently up to the limits established by the service. A server listens on a particular TCP/IP communication port and launches a specified DCL (Digital Command Language) Login Command file that serves as a startup process for each client connection process. This startup file contains the necessary commands to execute the entry point into V*IST*A HL7. In essence, the TCP/IP service performs as a multi-threaded HL7 listener.

The TCP/IP service running as a concurrent server provides a more robust functionality than a TaskMan-based V*IST*A HL7 multi-listener; thus, installation of TCP/IP services replaces and disables the functionality of the V*IST*A HL7 options for starting and stopping a multi-listener.

## Requirements for Setting a TCP/IP Service on OpenVMS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To set and enable a TCP/IP service, you need to create and configure the following components in V*IST*A HL7 and OpenVMS:

- V*IST*A HL7 logical link for the Multi-Threaded Listener.
- An OpenVMS account.
- An OpenVMS home directory.
- An OpenVMS DCL login command procedure. This is the startup command file that executes on every concurrent process. Default DCL login command files are provided in this document and can be downloaded as described in section 2.2.1.
- An OpenVMS TCP/IP service.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](hl7-hl-1-6-84-multi-listeners-using-tcp-ip-svcs-for-openvms/005.png)</td>
<td><ul>
<li><p>It is strongly recommended that the person implementing the instructions in this supplement have OpenVMS system administrator privileges to create the above components and be familiar with the OpenVMS TCP/IP Services Management Control Program.</p></li>
<li><p>You must choose the OpenVMS node where the TCP/IP service will be running. This is also the node whose IP address will be advertised to other systems as the location of your HL7 listener.</p></li>
</ul></td>
</tr>
</tbody>
</table>

### Pre-Configured DCL Command Procedure Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For your convenience, the DCL login command files, HLS5000CACHE.COM and HLS5000DSM.COM, are included in this supplement document, and they can be downloaded from the \[ANONYMOUS.SOFTWARE\] directory at the following ftp sites:

CIO Field Office FTP Address Directory

---------------------------------------------------------------------

Albany REDACTED \[anonymous software\]

Hines REDACTED \[anonymous software\]

Salt Lake City REDACTED \[anonymous software\]

## Recommended Naming Convention for OpenVMS Components

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following names are used in the description for creating a TCP/IP service and are referenced throughout this chapter. All these names are suggestions. Your site might already have its own naming convention:

- HLSEVEN―OpenVMS user account name for an HL7 TCP/IP service.
- \[HLSEVEN\]―Name of home directory for the above HLSEVEN user
- HL7―Name of the owner
- HLS\<port\>\<M environment\>.COM― Name of DCL login command procedure, where the \<port\> is the actual port number where the service will be listening, and the \<M environment\> is the actual V*IST*A M environment. For example:
  - HLS5000DSM.COM― represents the login command procedure for a TCP/IP service listening on port 5000 that starts up a DSM V*IST*A HL7 listener concurrent process.
  - HLS5000CACHE.COM― represents the login command procedure for a TCP/IP service listening on port 5000 that starts up a CACHE V*IST*A HL7 listener concurrent process..
- HLS\<port\>\<M environment\>― Name of a TCP/IP service, where the \<port\> is the actual port number where the service will be listening, and the \<M environment\> is the actual V*IST*A M environment. For example
  - HLS5000DSM― represents the TCP/IP service listening on port 5000 that starts up a DSM V*IST*A HL7 listener concurrent process.
  - HLS5000CACHE― represents the TCP/IP service listening on port 5000 that starts up a CACHE V*IST*A HL7 listener concurrent process.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](hl7-hl-1-6-84-multi-listeners-using-tcp-ip-svcs-for-openvms/006.png)</td>
<td><ul>
<li><p>You can set up more than one TCP/IP service for HL7, although it is not necessary to do this. To set up more than one TCP/IP service for HL7, follow the steps in this supplement for each listener; however, use different command file name and TCP/IP service name for each listener, with a different port number in each command file.</p></li>
<li><p>You can optionally use different user accounts and directories for each listener.</p></li>
</ul></td>
</tr>
</tbody>
</table>

# Creating a Multi-Threaded Listener for DSM on OpenVMS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Set Up a Logical Link in V*IST*A

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In V*IST*A HL LOGICAL LINK file (#870), create an entry for the Multi-Threaded Listener with the fields populated as follows:

Link Settings for Multi-Threaded Listener, DSM for OpenVMS using TCP/IP Services

|                     |                                                                                                   |     |
|---------------------|---------------------------------------------------------------------------------------------------|-----|
| Field           | Description                                                                                   |     |
| LLP TYPE            | TCP                                                                                               |     |
| TCP/IP Address      | null                                                                                              |     |
| TCP/IP Port         | Port to listen on, e.g., 5000 (make note of the exact port number)                                |     |
| TCP/IP Service Type | MULTI LISTENER                                                                                    |     |
| SHUTDOWN LLP ?      | null (setting this field to YES will cause each arriving connection to terminate immediately) |     |
| Startup Node        | null                                                                                              |     |
| Autostart           | null                                                                                              |     |
| Ack Timeout         | (Increase from default if network is slow)                                                        |     |

<span id="_Toc50862776" class="anchor"></span>Figure : Multi-Threaded Listener link settings for DSM for OpenVMS using TCP/IP Services

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](hl7-hl-1-6-84-multi-listeners-using-tcp-ip-svcs-for-openvms/007.png)</td>
<td><ul>
<li><p>The port number you select must be an available TCP/IP port number. The port number will also be used in the configuration and naming of the TCP/IP service described in the following sections.</p></li>
<li><p>If the HL7 multi-listener will be used by an application at the national level, you must register the port number with the DBIA manager on Forum.</p></li>
</ul></td>
</tr>
</tbody>
</table>

|                                                   |                                                                                                                                                                                                            |
|---------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](hl7-hl-1-6-84-multi-listeners-using-tcp-ip-svcs-for-openvms/008.png) | Because, the new HL7 listener will be externally controlled by the TCP/IP service on OpenVMS, the V*IST*A HL7 options for starting and stopping logical links will no longer have effect on this listener. |

## Create OpenVMS User Account

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](hl7-hl-1-6-84-multi-listeners-using-tcp-ip-svcs-for-openvms/009.png)</td>
<td><ul>
<li><p>Determine an unused User Identification Code (UIC), typically in the same group as other DSM for OpenVMS accounts.</p></li>
<li><p>Using the OpenVMS Authorize utility, add the new HLSEVEN account with the unused UIC. You must have SYSPRV to do this.</p></li>
<li><p>Verify that the account settings for the new HLSEVEN account are the same as they appear in the example that follows; or, if they are different, verify that the impact of the different settings is acceptable for your system. For security, make sure that the DisCtlY, Restricted, and Captive flags are set.</p></li>
</ul></td>
</tr>
</tbody>
</table>

There are two different ways to set up a new user account, and you are free to choose the one you prefer. The following two examples illustrate two different ways to set up an OpenVMS User account:

1.  One way to set up a OpenVMS User is to copy your existing XMINET (TCP/IP MailMan) account to a new account with an unused UIC. For example:

> \$ SET DEF USER\$ *(use your local user device-name)*

> \$ MC AUTHORIZE

> UAF\> COPY /ADD XMINET HLSEVEN/UIC=\[51,45\]/DIR=\[HLSEVEN\]

> %UAF-I-COPMSG, user record copied

> %UAF-W-DEFPWD, copied or renamed records must receive new password

> %UAF-I-RDBADDMSGU, identifier HLSEVEN value \[000051,000045\] added to rights database

> UAF\>

b\. Add the new HLSEVEN OpenVMS account. For example:

> \$ SET DEF USER\$ (use your local user device-name)

> \$ MC AUTHORIZE

> UAF\> ADD HLSEVEN /UIC=\[100,45\]/OWNER="HL7" - (must use continuation character "-")

> \_UAF\> /DEVICE=USER\$/DIRECTORY=\[HLSEVEN\] -

> \_UAF\> /NOACCESS/NETWORK/FLAGS=(DISCTLY,RESTRICTED,NODISUSER) -

> \_UAF\> /PRIV=(NETMBX,OPER,SHARE,TMPMBX) -

> \_UAF\> /DEF=(NETMBX,OPER,SHARE,TMPMBX)/LGICMD=NL:

> %UAF-I-ADDMSG, user record successfully added

> %UAF-I-RDBADDMSGU, identifier HLSEVEN value \[000100,000045\] added to rights data

> base

> UAF\>

> UAF\> SHOW HLSEVEN

> Username: HLSEVEN Owner: HL7

> Account: UIC: \[100,45\] (\[HLSEVEN\])

> CLI: DCL Tables: DCLTABLES

> Default: USER\$:\[HLSEVEN\]

> LGICMD: NL:

> Flags: DisCtlY Restricted

> Primary days: Mon Tue Wed Thu Fri

> Secondary days: Sat Sun

> Primary 000000000011111111112222 Secondary 000000000011111111112222

> Day Hours 012345678901234567890123 Day Hours 012345678901234567890123

> Network: \##### Full access \###### \##### Full access \######

> Batch: ----- No access ------ ----- No access ------

> Local: ----- No access ------ ----- No access ------

> Dialup: ----- No access ------ ----- No access ------

> Remote: ----- No access ------ ----- No access ------

> Expiration: (none) Pwdminimum: 6 Login Fails: 0

> Pwdlifetime: 90 00:00 Pwdchange: (pre-expired)

> Last Login: (none) (interactive), (none) (non-interactive)

> Maxjobs: 0 Fillm: 100 Bytlm: 64000

> Maxacctjobs: 0 Shrfillm: 0 Pbytlm: 0

> Maxdetach: 0 BIOlm: 150 JTquota: 4096

> Prclm: 8 DIOlm: 150 WSdef: 2000

> Prio: 4 ASTlm: 250 WSquo: 4000

> Queprio: 4 TQElm: 10 WSextent: 16384

> CPU: (none) Enqlm: 2000 Pgflquo: 50000

> Authorized Privileges:

> NETMBX OPER SHARE TMPMBX

> Default Privileges:

> NETMBX OPER SHARE TMPMBX

> UAF\> Exit

> %UAF-I-DONEMSG, system authorization file modified

> %UAF-I-RDBDONEMSG, rights database modified

> \$

> UAF\> SHOW HLSEVEN

> Username: HLSEVEN Owner: HL7

> Account: UIC: \[51,45\] (\[HLSEVEN\])

> CLI: DCL Tables: DCLTABLES

> Default: USER\$:\[HLSEVEN\]

> LGICMD: NL:

> Flags: DisCtlY Restricted Captive

> Primary days: Mon Tue Wed Thu Fri

> Secondary days: Sat Sun

> Primary 000000000011111111112222 Secondary 000000000011111111112222

> Day Hours 012345678901234567890123 Day Hours 012345678901234567890123

> Network: \##### Full access \###### \##### Full access \######

> Batch: ----- No access ------ ----- No access ------

> Local: ----- No access ------ ----- No access ------

> Dialup: ----- No access ------ ----- No access ------

> Remote: ----- No access ------ ----- No access ------

> Expiration: (none) Pwdminimum: 6 Login Fails: 0

> Pwdlifetime: 90 00:00 Pwdchange: (pre-expired)

> Last Login: (none) (interactive), (none) (non-interactive)

> Maxjobs: 0 Fillm: 500 Bytlm: 100000

> Maxacctjobs: 0 Shrfillm: 0 Pbytlm: 0

> Maxdetach: 0 BIOlm: 150 JTquota: 4096

> Prclm: 8 DIOlm: 18 WSdef: 1344

> Prio: 4 ASTlm: 176 WSquo: 2688

> Queprio: 4 TQElm: 10 WSextent: 65536

> CPU: (none) Enqlm: 3000 Pgflquo: 100000

> Authorized Privileges:

> NETMBX OPER SHARE TMPMBX

> Default Privileges:

> NETMBX OPER SHARE TMPMBX

> UAF\> EXIT

> %UAF-I-DONEMSG, system authorization file modified

> %UAF-I-RDBDONEMSG, rights database modified

## Create OpenVMS Home Directory

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This directory will house the DCL command procedure, which is executed whenever a client connects. A log file is created for every instance of a connection for that listener. Make sure that the owner of the directory is the HLSEVEN account.

For example, to create a home directory named \[HLSEVEN\] with ownership of HLSEVEN:

> \$ CREATE/DIR \[HLSEVEN\]/OWNER=HLSEVEN

## Create a DCL Login Command Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Create a DCL command procedure (shown below) in the home directory for HLSEVEN account and name it according to the recommended convention. Make sure the command procedure file is owned by the HLSEVEN account.

1.  To create a DCL login command procedure that will use a given port, for port 5000, name your command procedure file as HLS5000DSM.COM.
2.  Adjust the DSM command line (environment, UCI, and volume set) for your system.
3.  If access control is enabled, ensure that the HLSEVEN account has access to this UCI, volume set, and routine (see “Access Control List (ACL) Issues”, later in this chapter).
4.  In the DCL login command procedure, if necessary, replace the port number to the actual port number. For example, to use port=6788, change the following line:

> \$ dsm/env=dsmmgr/uci=vah/vol=rou/data="''x'^5000" PORT^HLCSTCPA

> to

> \$ dsm/env=dsmmgr/uci=vah/vol=rou/data="''x'^6788" PORT^HLCSTCPA

5.  Ensure that the name of the DCL login command file, as described in step 1, matches the port assignment. For example, if you changed the port number from 5000 to 6788, then rename your HLS5000DSM.COM file to HLS6788DSM.COM

For your convenience, you can cut and paste the following DCL login command procedure file into your OpenVMS HLSEVEN device and directory. In addition, you can download the file from the sites listed in section 2.2.1.

Sample DCL Login Command Procedure file follows next:

\$! HLS5000DSM.COM - for incoming tcp connect requests with port=5000 and

\$! using "DSM" command line to enter the M environment

\$! File name HLS5000DSM.COM is recommended to be changed to reflect the

\$! change of the TCPIP port number. For example, file name could be

\$! changed to HLS6788DSM.COM if port=6788.

\$!

\$!this file is copied and modifed from HLSEVEN.COM

\$! Revision History:

\$! Patch HL\*1.6\*19 & HL\*1.6\*56--Documentation only

\$! Patch HL\*1.6\*70--HL71_6P70.COM

\$! Patch HL\*1.6\*84--HLS5000CACHE.COM and HLS5000DSM.COM

\$!-------------------------------------------------------------

\$ set noon !Don't stop

\$ set noverify !change as needed

\$! set verify !change as needed

\$ purge/keep=5 sys\$login:\*.log !Purge log files only

\$ set proc/priv=(share) !Required for MBX device

\$ x=f\$trnlnm("sys\$net") !This is our MBX device

\$!

\$ write sys\$output "Opening "+x !This can be viewed in the log file

\$! Check status of the BG device before going to either DSM or Cache'

\$ cnt=0

\$ CHECK:

\$ stat=f\$getdvi("''x'","STS")

\$ if cnt .eq. 10

\$ then

\$ write sys\$output "Could not open ''x' - exiting"

\$ goto EXIT

\$ else

\$ if stat .ne. 16

\$ then

\$ cnt=cnt+1

\$ write sys\$output "''cnt'\> ''x' not ready!"

\$ wait 00:00:01 !Wait one second to assure connection

\$ goto CHECK

\$ else

\$ write sys\$output "''x' is now ready for use - entering DSM or Cache"

\$!-------------------------------------------------------------

\$! \*\*START OF INFORMATION ONLY SECTION\*\*

\$! This section describes the basic commands for starting a generic

\$! listener.

\$! For DSM, replace 5000 below with the actual port number, and

\$! change the file name to reflect the change of the port number

\$! as recommended above.

\$! dsm/env=dsmmgr/uci=vah/vol=rou/data="''x'^5000" port^hlcstcpa

\$! For Cache, replace 5000 below with the actual port number, and

\$! change the file name to reflect the change of the port number as

\$! recommended above.

\$! port=port number

\$! cache "-U" "VAH" "port^hlcstcpa"

\$! \*\*END OF INFORMATION ONLY SECTION\*\*

\$!-------------------------------------------------------------

\$! \*\*Be sure the command line(s) in the COMMAND LINE SECTION

\$! \*\*below is correct for your system and if access control is

\$! \*\*enabled, that this account has access to this uci,vol & routine.

\$! \*\*An entry in file 870 for this logical link with the specified

\$! \*\*unique port number and its device type as "MS"(Multi-threaded

\$! \*\*server) must be existed.

\$!

\$! \*\*Also, comment or uncomment the appropriate lines for your system.

\$!

\$!-------------------------------------------------------------

\$! COMMAND LINE SECTION:

\$! =====================

\$!-------------------------------------------------------------

\$! for DSM, replace 5000 below with the actual port number, and change

\$! the file name to reflect the change of the port number as recommended

\$! above.

\$ dsm/env=dsmmgr/uci=vah/vol=rou/data="''x'^5000" PORT^HLCSTCPA

\$!-------------------------------------------------------------

\$! For Cache, replace 5000 below with the actual port number, and change

\$! the file name to reflect the change of the port number as recommended

\$! above.

\$! PORT=5000

\$! cache "-U" "VAH" "PORT^HLCSTCPA"

\$ endif

\$ exit:

\$ logout/brief

## Set Up and Enable the TCP/IP Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To create the TCP/IP service to listen for connections, you must ensure the following:

- Choose the OpenVMS node where you want to run the TCP/IP service listener. This is also the node whose IP address will be advertised to other systems as the location of your HL7 listener;
- Choose the TCP/IP port number as chosen in section 3.1, Set Up a Logical Link in V*IST*A;
- Use the same user account as created in section 3.1, Create OpenVMS User Account; and
- Use the same DCL login command file name as the one created in section 3.4, Create a DCL Login Command Procedure.

### Set up the TCP/IP Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](hl7-hl-1-6-84-multi-listeners-using-tcp-ip-svcs-for-openvms/010.png)</td>
<td><ul>
<li><p>Since TCP/IP Services is node specific, make sure you are on the same node that you want the listener to run on.</p></li>
<li><p>It is possible to run the TCP/IP service on multiple nodes. This may or may not be necessary, depending on your site's configuration needs. For instance, the impersonator VMS feature allows for the possibility of all nodes in the cluster to become the surrogate. This allows for the listening process uninterrupted if the TCP/IP service is enabled on all nodes in the cluster. For this reason, it is recommended that you enable the TCP/IP service on all nodes in the cluster.</p></li>
</ul></td>
</tr>
</tbody>
</table>

Ensure that your new TCP/IP service uses the recommended naming convention. For example, to set up a service that will be listening on port 5000 and use a corresponding DCL login command file HLS5000DSM.COM.

Set the service name as HLS5000DSM as follows:

\$ TCPIP (must use continuation character "-" at end of long lines)

TCPIP\> SET SERVICE HLS5000DSM/USER=HLSEVEN/PROC=HLS5000DSM /PORT=5000-

\_TCPIP\> /PROTOCOL=TCP/REJECT=MESSAGE="All channels busy" -

\_TCPIP\> /LIMIT=50/FILE=USER\$:\[HLSEVEN\]HLS5000DSM.COM

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](hl7-hl-1-6-84-multi-listeners-using-tcp-ip-svcs-for-openvms/011.png)</td>
<td><ul>
<li><p>If you get an error because you mistyped any of the above lines or forgot to use the continuation character "-", we suggest you do the following to remove the corrupted service and repeat the above commands.</p></li>
</ul>
<blockquote>
<p>TCPIP&gt; SET CONFIG ENABLE NOSERVICE HLS5000DSM</p>
<p>TCPIP&gt; SET NOSERVICE HLS5000DSM</p>
</blockquote></td>
</tr>
</tbody>
</table>

TCPIP\> SHO SERVICE HLS5000DSM/FULL

Service: HLS5000DSM

State: Disabled

Port: 5000 Protocol: TCP Address: 0.0.0.0

User_name: not defined Process: HLS5000DSM

### Enable and Save the TCP/IP Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Since TCP/IP Services is node specific, make sure you are on the same node that you want the listener to run on.

TCPIP\> ENABLE SERVICE HLS5000DSM *(enable service immediately)*

TCPIP\> SET CONFIG ENABLE SERVICE HLS5000DSM *(save service for reboot)*

TCPIP\> SHO SERVICE/FULL HLS5000DSM

Service: HLS5000DSM

State: Enabled

Port: 5000 Protocol: TCP Address: 0.0.0.0

Inactivity: 5 User_name: HLSEVEN Process: HLS5000DSM

Limit: 50 Active: 0 Peak: 0

File: USER\$:\[HLSEVEN\] HLS5000DSM.COM

Flags: Listen

Socket Opts: Rcheck Scheck

Receive: 0 Send: 0

Log Opts: None

File: not defined

Security

Reject msg: All channels busy

Accept host: 0.0.0.0

Accept netw: 0.0.0.0

TCPIP\> SHO CONFIG ENABLE SERVICE

Enable service

FTP, FTP_CLIENT, HLS5000DSM, MPI, TELNET, XMINETMM

TCPIP\> EXIT

## Access Control List (ACL) Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Some sites use DSM's ACL feature, which controls access explicitly to each OpenVMS account that needs to enter that DSM environment. If your site is using ACL, you should set up the HLSEVEN account with PROGRAMMER access, and then specify the Volume set and UCI name that the HLSEVEN user account has authorization to access. Ensure that the OpenVMS HLSEVEN account prohibits Batch, Local, Dialup, and Remote logins, allowing only Network logins.

An example of setting this level of access for an HLSEVEN account is provided below:

\$ DSM /MAN ^ACL

Environment Access Utilities

1\. ADD/MODIFY USER (ADD^ACL)

2\. DELETE USER (DELETE^ACL)

3\. MODIFY ACTIVE AUTHORIZATIONS (^ACLSET)

4\. PRINT AUTHORIZED USERS (PRINT^ACL)

Select Option \> 1 \<Enter\> ADD/MODIFY USER

OpenVMS User Name: \> HLSEVEN

ACCESS MODE VOL UCI ROUTINE

----------- --- --- -------

No access rights for this user.

Access Mode (\[M\]ANAGER, \[P\]ROGRAMMER, or \[A\]PPLICATION): \> P

Volume set name: \> VAH

UCI: \> ROU

UCI: \> \<Enter\>

Volume set name: \> \<Enter\>

Access Mode (\[M\]ANAGER, \[P\]ROGRAMMER, or \[A\]PPLICATION): \> \<Enter\>

USER ACCESS MODE VOL UCI ROUTINE

---- ----------- --- --- -------

HLSEVEN PROGRAMMER ROU VAH

OK to file? \<Y\> \<Enter\>

OpenVMS User Name: \> \<Enter\>

OK to activate changes now? \<Y\> \<Enter\>

Creating access authorization file: USER\$:\[DSMMGR\]DSM\$ACCESS.DAT.

## Controlling the Number of Log Files Created by TCP/IP Services

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HLS5000DSM TCP/IP service automatically creates log files (TCP/IP services does this and it cannot be prevented) in the HLSEVEN directory named HLS5000DSM.LOG;xxx where 'xxx' is a file version number. New versions of this file will be created until that file version number reaches the maximum number of 32767. In order to minimize the number of log files created, you may want to initially rename this log file to the highest version number with the command:

\$ RENAME USER\$:\[HLSEVEN\]HLS5000DSM.LOG; USER\$:\[HLSEVEN\]HLS5000DSM.LOG;32767

Alternatively, you can set a limit on the number of versions of the log file that can concurrently exist in the HLSEVEN directory:

\$ SET FILE /VERSION_LIMIT=10 USER\$:\[HLSEVEN\]HLS5000DSM.LOG;

You probably should not limit the number of versions of the log file until you know that your HLS5000DSM service is working correctly; keeping the log files can help when diagnosing problems with the service/account.

## Starting and Stopping the Listener

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Although the multi-threaded listener for OpenVMS systems requires the setup of a link, you never actually start or stop this link with V*IST*A HL7 options. Instead, because the listener is implemented as a TCP/IP service, start it up and shut it down by using the generic tools TCP/IP services provides to enable and disable a TCP/IP service. For example:

TCPIP\> ENABLE SERVICE HLS5000DSM *(Start up* TCP/IP *service)*

TCPIP\> DISABLE SERVICE HLS5000DSM *(Stop* TCP/IP *service*)

# Replacing an Existing HLSEVEN Service with the HLS5000DSM Service for DSM on OpenVMS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you are a DSM/VMS site that is currently using an existing HLSEVEN service that uses the internal entry number of V*IST*A file \#870 as a parameter, and you intend to replace it with the recommended HLS5000DSM service, it is recommended that you follow the instructions listed below:

First, navigate to the OpenVMS device and directory where your HL7 user account is located and invoke the OpenVMS TCP/IP Services Management Control Program. For example:

\$SET DEF USER\$:\[HLSEVEN\] (use your local user device-name:\[HLSEVEN\])

\$TCPIP

TCPIP\>

## Disable the HLSEVEN TCP/IP Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

TCPIP\>DISABLE SERVICE HLSEVEN

## Remove the HLSEVEN TCP/IP Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

TCPIP\> SET CONFIG ENABLE NOSERVICE HLSEVEN

TCPIP\> SET NOSERVICE HLSEVEN

## Create a DCL Login Command Procedure HLS5000DSM

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Create a DCL command procedure file in the home directory for HLSEVEN account and name it according to the recommended convention.

For your convenience, you can cut and paste the following DCL login command procedure file into your OpenVMS HLSEVEN device and directory. Also, you can download the file from the sites listed in section 2.2.1.

Sample DCL Login Command Procedure file follows next:

\$! HLS5000DSM.COM - for incoming tcp connect requests with port=5000 and

\$! using "DSM" command line to enter the M environment

\$! File name HLS5000DSM.COM is recommended to be changed to reflect the

\$! change of the TCPIP port number. For example, file name could be

\$! changed to HLS6788DSM.COM if port=6788.

\$!

\$!this file is copied and modifed from HLSEVEN.COM

\$! Revision History:

\$! Patch HL\*1.6\*19 & HL\*1.6\*56--Documentation only

\$! Patch HL\*1.6\*70--HL71_6P70.COM

\$! Patch HL\*1.6\*84--HLS5000CACHE.COM and HLS5000DSM.COM

\$!-------------------------------------------------------------

\$ set noon !Don't stop

\$ set noverify !change as needed

\$! set verify !change as needed

\$ purge/keep=5 sys\$login:\*.log !Purge log files only

\$ set proc/priv=(share) !Required for MBX device

\$ x=f\$trnlnm("sys\$net") !This is our MBX device

\$!

\$ write sys\$output "Opening "+x !This can be viewed in the log file

\$! Check status of the BG device before going to either DSM or Cache'

\$ cnt=0

\$ CHECK:

\$ stat=f\$getdvi("''x'","STS")

\$ if cnt .eq. 10

\$ then

\$ write sys\$output "Could not open ''x' - exiting"

\$ goto EXIT

\$ else

\$ if stat .ne. 16

\$ then

\$ cnt=cnt+1

\$ write sys\$output "''cnt'\> ''x' not ready!"

\$ wait 00:00:01 !Wait one second to assure connection

\$ goto CHECK

\$ else

\$ write sys\$output "''x' is now ready for use - entering DSM or Cache"

\$!-------------------------------------------------------------

\$! \*\*START OF INFORMATION ONLY SECTION\*\*

\$! This section describes the basic commands for starting a generic

\$! listener.

\$! For DSM, replace 5000 below with the actual port number, and

\$! change the file name to reflect the change of the port number

\$! as recommended above.

\$! dsm/env=dsmmgr/uci=vah/vol=rou/data="''x'^5000" port^hlcstcpa

\$! For Cache, replace 5000 below with the actual port number, and

\$! change the file name to reflect the change of the port number as

\$! recommended above.

\$! port=port number

\$! cache "-U" "VAH" "port^hlcstcpa"

\$! \*\*END OF INFORMATION ONLY SECTION\*\*

\$!-------------------------------------------------------------

\$! \*\*Be sure the command line(s) in the COMMAND LINE SECTION

\$! \*\*below is correct for your system and if access control is

\$! \*\*enabled, that this account has access to this uci,vol & routine.

\$! \*\*An entry in file 870 for this logical link with the specified

\$! \*\*unique port number and its device type as "MS"(Multi-threaded

\$! \*\*server) must be existed.

\$!

\$! \*\*Also, comment or uncomment the appropriate lines for your system.

\$!

\$!-------------------------------------------------------------

\$! COMMAND LINE SECTION:

\$! =====================

\$!-------------------------------------------------------------

\$! for DSM, replace 5000 below with the actual port number, and change

\$! the file name to reflect the change of the port number as recommended

\$! above.

\$ dsm/env=dsmmgr/uci=vah/vol=rou/data="''x'^5000" PORT^HLCSTCPA

\$!-------------------------------------------------------------

\$! For Cache, replace 5000 below with the actual port number, and change

\$! the file name to reflect the change of the port number as recommended

\$! above.

\$! PORT=5000

\$! cache "-U" "VAH" "PORT^HLCSTCPA"

\$ endif

\$ exit:

\$ logout/brief

## Set Up and Enable the TCP/IP Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Set Up the TCP/IP Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](hl7-hl-1-6-84-multi-listeners-using-tcp-ip-svcs-for-openvms/012.png)</td>
<td><ul>
<li><p>Since TCP/IP Services is node specific, make sure you are on the same node that you want the listener to run on.</p></li>
<li><p>It is possible to run the TCP/IP service on multiple nodes. This may or may not be necessary, depending on your site's configuration needs. For instance, the impersonator VMS feature allows for the possibility of all nodes in the cluster to become the surrogate. This allows for the listening process uninterrupted if the TCP/IP service is enabled on all nodes in the cluster. For this reason, it is recommended that you enable the TCP/IP service on all nodes in the cluster.</p></li>
</ul></td>
</tr>
</tbody>
</table>

Ensure that your new TCP/IP service uses the recommended naming convention. To set up a service that will be listening on port 5000 and use a corresponding DCL login command file HLS5000DSM.COM.

Set the service name as HLS5000DSM as follows:

\$ TCPIP (must use continuation character "-" at end of long lines)

TCPIP\> SET SERVICE HLS5000DSM/USER=HLSEVEN/PROC=HLS5000DSM /PORT=5000-

\_TCPIP\> /PROTOCOL=TCP/REJECT=MESSAGE="All channels busy" -

\_TCPIP\> /LIMIT=50/FILE=USER\$:\[HLSEVEN\]HLS5000DSM.COM

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](hl7-hl-1-6-84-multi-listeners-using-tcp-ip-svcs-for-openvms/013.png)</td>
<td><ul>
<li><p>If you get an error because you mistyped any of the above lines or forgot to use the continuation character "-", we suggest you do the following to remove the corrupted service and repeat the above commands.</p></li>
</ul>
<blockquote>
<p>TCPIP&gt; SET CONFIG ENABLE NOSERVICE HLS5000DSM</p>
<p>TCPIP&gt; SET NOSERVICE HLS5000DSM</p>
</blockquote></td>
</tr>
</tbody>
</table>

TCPIP\> SHO SERVICE HLS5000DSM/FULL

Service: HLS5000DSM

State: Disabled

Port: 5000 Protocol: TCP Address: 0.0.0.0

User_name: not defined Process: HLS5000DSM

### Enable and Save the TCP/IP Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Since TCP/IP Services is node specific, make sure you are on the same node that you want the listener to run on.

TCPIP\> ENABLE SERVICE HLS5000DSM *(enable service immediately)*

TCPIP\> SET CONFIG ENABLE SERVICE HLS5000DSM *(save service for reboot)*

TCPIP\> SHO SERVICE/FULL HLS5000DSM

Service: HLS5000DSM

State: Enabled

Port: 5000 Protocol: TCP Address: 0.0.0.0

Inactivity: 5 User_name: HLSEVEN Process: HLS5000DSM

Limit: 50 Active: 0 Peak: 0

File: USER\$:\[HLSEVEN\] HLS5000DSM.COM

Flags: Listen

Socket Opts: Rcheck Scheck

Receive: 0 Send: 0

Log Opts: None

File: not defined

Security

Reject msg: All channels busy

Accept host: 0.0.0.0

Accept netw: 0.0.0.0

TCPIP\> SHO CONFIG ENABLE SERVICE

Enable service

FTP, FTP_CLIENT, HLS5000DSM, MPI, TELNET, XMINETMM

TCPIP\> EXIT

# Creating a Multi-Threaded Listener for Caché on OpenVMS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Set Up Link

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Create a new link entry in V*IST*A file HL LOGICAL LINK (#870) for the Multi-Threaded Listener as follows:

> *Note: If your site is migrating from DSM/VMS to Caché/VMS, your site can reuse any existing multi-listener logical link entry.*

Link Settings for Multi-Threaded Listener, CACHÉ for OpenVMS (using TCP/IP services):

|                     |                                                                                                   |     |
|---------------------|---------------------------------------------------------------------------------------------------|-----|
| Field           | Description                                                                                   |     |
| LLP TYPE            | TCP                                                                                               |     |
| TCP/IP Address      | null                                                                                              |     |
| TCP/IP Port         | Port to listen on, e.g., 5000 (make note of the exact port number)                                |     |
| TCP/IP Service Type | MULTI LISTENER                                                                                    |     |
| SHUTDOWN LLP ?      | null (setting this field to YES will cause each arriving connection to terminate immediately) |     |
| Startup Node        | null                                                                                              |     |
| Autostart           | null                                                                                              |     |
| Ack Timeout         | (Increase from default if network is slow)                                                        |     |

<span id="_Toc50862777" class="anchor"></span>Figure : Multi-Threaded Listener link settings for CACHÉ for OpenVMS (using TCP/IP services)

## Set Up OpenVMS User Account

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](hl7-hl-1-6-84-multi-listeners-using-tcp-ip-svcs-for-openvms/014.png)</td>
<td><ul>
<li><p>Determine an unused User Identification Code (UIC), typically in the same group as other Caché for OpenVMS accounts.</p></li>
<li><p>Using the OpenVMS Authorize utility, add the new HLSEVEN account with the unused UIC. You must have SYSPRV to do this.</p></li>
<li><p>Verify that the account settings for the new HLSEVEN account are the same as they appear in the example that follows; or, if they are different, verify that the impact of the different settings is acceptable for your system. For security, make sure that the DisCtlY and Restricted flags are set. DO NOT set the Captive flag as this will prevent the multi-threaded listener from working on Caché/VMS systems.</p></li>
</ul></td>
</tr>
</tbody>
</table>

Add the new HLSEVEN OpenVMS account. For example:

> \$ SET DEF USER\$ *(use your local user device-name)*

> \$ MC AUTHORIZE

> UAF\> ADD HLSEVEN /UIC=\[100,45\]/OWNER="HL7" - *(must use continuation character "-")*

> \_UAF\> /DEVICE=USER\$/DIRECTORY=\[HLSEVEN\] -

> \_UAF\> /NOACCESS/NETWORK/FLAGS=(DISCTLY,RESTRICTED,NODISUSER) -

> \_UAF\> /PRIV=(NETMBX,OPER,SHARE,TMPMBX) -

> \_UAF\> /DEF=(NETMBX,OPER,SHARE,TMPMBX)/LGICMD=NL:

> %UAF-I-ADDMSG, user record successfully added

> %UAF-I-RDBADDMSGU, identifier HLSEVEN value \[000100,000045\] added to rights data

> base

> UAF\>

> UAF\> SHOW HLSEVEN

> Username: HLSEVEN Owner: HL7

> Account: UIC: \[100,45\] (\[HLSEVEN\])

> CLI: DCL Tables: DCLTABLES

> Default: USER\$:\[HLSEVEN\]

> LGICMD: NL:

> Flags: DisCtlY Restricted

> Primary days: Mon Tue Wed Thu Fri

> Secondary days: Sat Sun

> Primary 000000000011111111112222 Secondary 000000000011111111112222

> Day Hours 012345678901234567890123 Day Hours 012345678901234567890123

> Network: \##### Full access \###### \##### Full access \######

> Batch: ----- No access ------ ----- No access ------

> Local: ----- No access ------ ----- No access ------

> Dialup: ----- No access ------ ----- No access ------

> Remote: ----- No access ------ ----- No access ------

> Expiration: (none) Pwdminimum: 6 Login Fails: 0

> Pwdlifetime: 90 00:00 Pwdchange: (pre-expired)

> Last Login: (none) (interactive), (none) (non-interactive)

> Maxjobs: 0 Fillm: 100 Bytlm: 64000

> Maxacctjobs: 0 Shrfillm: 0 Pbytlm: 0

> Maxdetach: 0 BIOlm: 150 JTquota: 4096

> Prclm: 8 DIOlm: 150 WSdef: 2000

> Prio: 4 ASTlm: 250 WSquo: 4000

> Queprio: 4 TQElm: 10 WSextent: 16384

> CPU: (none) Enqlm: 2000 Pgflquo: 50000

> Authorized Privileges:

> NETMBX OPER SHARE TMPMBX

> Default Privileges:

> NETMBX OPER SHARE TMPMBX

> UAF\> Exit

> %UAF-I-DONEMSG, system authorization file modified

> %UAF-I-RDBDONEMSG, rights database modified

> \$

## Set Up Home Directory for the HL7 User Account

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You need to create a home directory for the HL7 user account. This directory will house the DCL command procedure, which is executed whenever a client connects. A log file is created for every instance of a connection for that listener. Make sure that the owner of the directory is the HLSEVEN.

For example, to create a home directory named \[HLSEVEN\] with ownership of HLSEVEN:

\$ CREATE/DIR \[HLSEVEN\]/OWNER=HLSEVEN

## Create a DCL Login Command Procedure for the HL7 User

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Create a DCL command procedure (shown below) in the home directory for HLSEVEN account and name it according to the recommended convention. Make sure the command procedure file is owned by the HLSEVEN account.

1.  To create a DCL login command procedure that will use a given port, for port 5000, name your command procedure file as HLS5000CACHE.COM.
6.  Adjust the Caché command line (environment, UCI, and volume set) for your system.
7.  If access control is enabled, ensure that the HLSEVEN account has access to this UCI, volume set, and routine (see “Access Control List (ACL) Issues”, later in this chapter).
8.  In the DCL login command procedure, if necessary, replace the port number to the actual port number. For example, to use port=6788, change the following line:

> \$ PORT=5000

> to

> \$ PORT=6788

9.  Ensure that the name of the DCL login command file, as described in step 1, matches the port assignment. For example, if you changed the port number from 5000 to 6788, then rename your HLS5000CACHE.COM file to HLS6788CACHE.COM

For your convenience, you can cut and paste the following DCL login command procedure file into your OpenVMS HLSEVEN device and directory. Also, you can download the file from the sites listed in section 2.2.1.

Sample DCL Login Command Procedure file follows next:

\$! HLS5000CACHE.COM - for incoming tcp connect requests with port=5000 and

\$! using "cache" commnad line to enter the M environment

\$! File name HLS5000CACHE.COM is recommended to be changed to reflect the

\$! change of the TCPIP port number. For example, file name could be

\$! changed to HLS6788CACHE.COM if port=6788.

\$!

\$!this file is copied and modifed from HLSEVEN.COM

\$! Revision History:

\$! Patch HL\*1.6\*19 & HL\*1.6\*56--Documentation only

\$! Patch HL\*1.6\*70--HL71_6P70.COM

\$! Patch HL\*1.6\*84--HLS5000CACHE.COM and HLS5000DSM.COM

\$!-------------------------------------------------------------

\$ set noon !Don't stop

\$ set noverify !change as needed

\$! set verify !change as needed

\$ purge/keep=5 sys\$login:\*.log !Purge log files only

\$ set proc/priv=(share) !Required for MBX device

\$ x=f\$trnlnm("sys\$net") !This is our MBX device

\$!

\$ write sys\$output "Opening "+x !This can be viewed in the log file

\$! Check status of the BG device before going to either DSM or Cache'

\$ cnt=0

\$ CHECK:

\$ stat=f\$getdvi("''x'","STS")

\$ if cnt .eq. 10

\$ then

\$ write sys\$output "Could not open ''x' - exiting"

\$ goto EXIT

\$ else

\$ if stat .ne. 16

\$ then

\$ cnt=cnt+1

\$ write sys\$output "''cnt'\> ''x' not ready!"

\$ wait 00:00:01 !Wait one second to assure connection

\$ goto CHECK

\$ else

\$ write sys\$output "''x' is now ready for use - entering DSM or Cache"

\$!-------------------------------------------------------------

\$! \*\*START OF INFORMATION ONLY SECTION\*\*

\$! This section describes the basic commands for starting a generic

\$! listener.

\$! For DSM, replace 5000 below with the actual port number, and change

\$! the file name to reflect the change of the port number as recommended

\$! above.

\$! dsm/env=dsmmgr/uci=vah/vol=rou/data="''x'^5000" port^hlcstcpa

\$! For Cache, replace 5000 below with the actual port number, and change

\$! the file name to reflect the change of the port number as recommended

\$! above.

\$! port=port number

\$! cache "-U" "VAH" "port^hlcstcpa"

\$! \*\*END OF INFORMATION ONLY SECTION\*\*

\$!-------------------------------------------------------------

\$! \*\*Be sure the command line(s) in the COMMAND LINE SECTION

\$! \*\*below is correct for your system and if access control is enabled,

\$! \*\*that this account has access to this uci,vol & routine.

\$! \*\*An entry in file 870 for this logical link with the specified

\$! \*\*unique port number and its device type as "MS"(Multi-threaded

\$! \*\*server) must be existed.

\$!

\$!-------------------------------------------------------------

\$! COMMAND LINE SECTION:

\$! =====================

\$!-------------------------------------------------------------

\$! for DSM, replace 5000 below with the actual port number, and change

\$! the file name to reflect the change of the port number as recommended

\$! above.

\$! dsm/env=dsmmgr/uci=vah/vol=rou/data="''x'^5000" PORT^HLCSTCPA

\$!-------------------------------------------------------------

\$! For Cache, replace 5000 below with the actual port number, and change

\$! the file name to reflect the change of the port number as recommended

\$! above.

\$ PORT=5000

\$ cache "-U" "VAH" "PORT^HLCSTCPA"

\$ endif

\$ exit:

\$ logout/brief

## Set Up and Enable the TCP/IP Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To create the TCP/IP service to listen for connections, you must ensure the following:

- Choose the OpenVMS node where you want to run the TCP/IP service listener. This is also the node whose IP address will be advertised to other systems as the location of your HL7 listener;
- Choose the TCP/IP port number as chosen in section 3.1, Set Up a Logical Link in V*IST*A;
- Use the same user account as created in section 3.1, Create OpenVMS User Account; and
- Use the same DCL login command file name as the one created in section 3.4, Create a DCL Login Command Procedure.

### Set Up the TCP/IP Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](hl7-hl-1-6-84-multi-listeners-using-tcp-ip-svcs-for-openvms/015.png)</td>
<td><ul>
<li><p>Since TCP/IP Services is node specific, make sure you are on the same node that you want the listener to run on.</p></li>
<li><p>It is possible to run the TCP/IP service on multiple nodes. This may or may not be necessary, depending on your site's configuration needs. For instance, the impersonator VMS feature allows for the possibility of all nodes in the cluster to become the surrogate. This allows for the listening process uninterrupted if the TCP/IP service is enabled on all nodes in the cluster. For this reason, it is recommended that you enable the TCP/IP service on all nodes in the cluster.</p></li>
</ul></td>
</tr>
</tbody>
</table>

Ensure that your new TCP/IP service uses the recommended naming convention. For example, to set up a service that will be listening on port 5000 and use a corresponding DCL login command file HLS5000CACHE.COM.

Set the service name as HLS5000CACHE as follows:

\$ TCPIP (must use continuation character "-" at end of long lines)

TCPIP\> SET SERVICE HLS5000CACHE/USER=HLSEVEN/PROC=HLS5000CACHE /PORT=5000-

\_TCPIP\> /PROTOCOL=TCP/REJECT=MESSAGE="All channels busy" -

\_TCPIP\> /LIMIT=50/FILE=USER\$:\[HLSEVEN\]HLS5000CACHE.COM

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](hl7-hl-1-6-84-multi-listeners-using-tcp-ip-svcs-for-openvms/016.png)</td>
<td><ul>
<li><p>If you get an error because you mistyped any of the above lines or forgot to use the continuation character "-", we suggest you do the following to remove the corrupted service and repeat the above commands.</p></li>
</ul>
<blockquote>
<p>TCPIP&gt; SET CONFIG ENABLE NOSERVICE HLS5000CACHE</p>
<p>TCPIP&gt; SET NOSERVICE HLS5000CACHE</p>
</blockquote></td>
</tr>
</tbody>
</table>

TCPIP\> SHO SERVICE HLS5000CACHE/FULL

Service: HLS5000CACHE

State: Disabled

Port: 5000 Protocol: TCP Address: 0.0.0.0

User_name: not defined Process: HLS5000CACHE

### Enable and Save the HLSEVEN TCP/IP Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Since TCP/IP Services is node specific, make sure you are on the same node that you want the listener to run on.

TCPIP\> ENABLE SERVICE HLS5000CACHE *(enable service immediately)*

TCPIP\> SET CONFIG ENABLE SERVICE HLS5000CACHE *(save service for reboot)*

TCPIP\> SHO SERVICE/FULL HLS5000CACHE

Service: HLS5000CACHE

State: Enabled

Port: 5000 Protocol: TCP Address: 0.0.0.0

Inactivity: 5 User_name: HLSEVEN Process: HLS5000CACHE

Limit: 50 Active: 0 Peak: 0

File: USER\$:\[HLSEVEN\]HLS5000CACHE.COM

Flags: Listen

Socket Opts: Rcheck Scheck

Receive: 0 Send: 0

Log Opts: None

File: not defined

Security

Reject msg: All channels busy

Accept host: 0.0.0.0

Accept netw: 0.0.0.0

TCPIP\> SHO CONFIG ENABLE SERVICE

Enable service

FTP, FTP_CLIENT, HLS5000CACHE, MPI, TELNET, XMINETMM

TCPIP\> EXIT

## How to Control the Number of Log Files Created by TCP/IP Services

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HLS5000CACHE TCP/IP service automatically creates log files (TCP/IP services does this and it cannot be prevented) in the HLSEVEN directory named HLS5000CACHE.LOG;xxx where 'xxx' is a file version number. New versions of this file will be created until that file version number reaches the maximum number of 32767. In order to minimize the number of log files created, you may want to initially rename this log file to the highest version number with the command:

\$ RENAME USER\$:\[HLSEVEN\]HLS5000CACHE.LOG; USER\$:\[HLSEVEN\]HLS5000CACHE.LOG;32767

Alternatively, you can set a limit on the number of versions of the log file that can concurrently exist in the HLSEVEN directory:

\$ SET FILE /VERSION_LIMIT=10 disk\$:\[HLSEVEN\]HLSEVEN.LOG;

You probably should not limit the number of versions of the log file until you know that your HLS5000CACHE service is working correctly; keeping the log files can help when diagnosing problems with the service/account.

## Starting and Stopping the Listener

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Although the multi-threaded listener for OpenVMS systems requires the setup of a link, you never actually start or stop this link with V*IST*A HL7 options. Instead, because the listener is implemented as a TCP/IP service, start it up and shut it down by using the generic tools TCP/IP services provides to enable and disable a TCP/IP service. For example:

TCPIP\> ENABLE SERVICE HLS5000CACHE \<Enter\> *(Start up* TCP/IP *service)*

TCPIP\> DISABLE SERVICE HLS5000CACHE \<Enter\> *(Stop* TCP/IP *service)*

# Migration Instructions for DSM/VMS to Caché/VMS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It is required that your site have HL7 Patch HL\*1.6\*84 installed before migrating to Caché/VMS.

This section documents issues and considerations that may be involved in migrating from other platforms to Caché/VMS. At this time, the only platform documented is Digital Standard MUMPS (DSM)/Virtual Memory System (VMS). The platform Caché/NT is not included because there are not configuration changes needed on the NT platform prior to migrating to Caché/VMS. Since DSM sites will retain their underlying VMS operating system, all configuration changes documented in this chapter are related to VMS.

If you are a DSM/VMS site and you intend to migrate to Caché/VMS, it is recommended that you follow the instructions listed below to make the necessary changes VMS configuration. These changes MUST ONLY be done prior to migrating to Caché/VMS and just after shutting down DSM.

First, navigate to the OpenVMS device and directory where your HL7 user account is located and invoke the OpenVMS TCP/IP Services Management Control Program. For example:

\$SET DEF USER\$:\[HLSEVEN\] (use your local user device-name:\[HLSEVEN\])

\$TCPIP

TCPIP\>

## Disable the HL7 TCP/IP Service(s)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For example, to disable the HLSEVEN service, do the following:

TCPIP\>DISABLE SERVICE HLSEVEN

## Remove the HL7 TCP/IP Service(s)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For example, to remove the HLSEVEN service, do the following:

TCPIP\> SET CONFIG ENABLE NOSERVICE HLSEVEN

TCPIP\> SET NOSERVICE HLSEVEN

## Modify the existing HLSEVEN User

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Modify the existing HLSEVEN user and ensure that the CAPTIVE flags are not enabled. Here is an example:

\$ MC AUTHORIZE

UAF\> MODIFY HLSEVEN /FLAGS=(NOCAPTIVE)

%UAF-I-MDFYMSG, user record(s) updated

UAF\> EXIT

%UAF-I-DONEMSG, system authorization file modified

In the example above, you optionally changed the User Identification Code (UIC) . It is important to point out that if you do this, you must change the IDENTIFIER accordingly so that the HLSEVEN identifier corresponds to the new UIC. In addition, you must change both the OWNER_UIC of the \[HLSEVEN\] directory and any files inside that directory. You should end up with a HLSEVEN UAF entry similar to what is described in the Caché/VMS sites section.

## Create a DCL Login Command Procedure HLS5000CACHE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Create a DCL command procedure file in the home directory for HLSEVEN account and name it according to the recommended convention.

For your convenience, you can cut and paste the following DCL login command procedure file into your OpenVMS HLSEVEN device and directory. Also, you can download the file from the sites listed in section 2.2.1.

Sample DCL Login Command Procedure file follows next:

\$! HLS5000CACHE.COM - for incoming tcp connect requests with port=5000 and

\$! using "cache" commnad line to enter the M environment

\$! File name HLS5000CACHE.COM is recommended to be changed to reflect the

\$! change of the TCPIP port number. For example, file name could be

\$! changed to HLS6788CACHE.COM if port=6788.

\$!

\$!this file is copied and modifed from HLSEVEN.COM

\$! Revision History:

\$! Patch HL\*1.6\*19 & HL\*1.6\*56--Documentation only

\$! Patch HL\*1.6\*70--HL71_6P70.COM

\$! Patch HL\*1.6\*84--HLS5000CACHE.COM and HLS5000DSM.COM

\$!-------------------------------------------------------------

\$ set noon !Don't stop

\$ set noverify !change as needed

\$! set verify !change as needed

\$ purge/keep=5 sys\$login:\*.log !Purge log files only

\$ set proc/priv=(share) !Required for MBX device

\$ x=f\$trnlnm("sys\$net") !This is our MBX device

\$!

\$ write sys\$output "Opening "+x !This can be viewed in the log file

\$! Check status of the BG device before going to either DSM or Cache'

\$ cnt=0

\$ CHECK:

\$ stat=f\$getdvi("''x'","STS")

\$ if cnt .eq. 10

\$ then

\$ write sys\$output "Could not open ''x' - exiting"

\$ goto EXIT

\$ else

\$ if stat .ne. 16

\$ then

\$ cnt=cnt+1

\$ write sys\$output "''cnt'\> ''x' not ready!"

\$ wait 00:00:01 !Wait one second to assure connection

\$ goto CHECK

\$ else

\$ write sys\$output "''x' is now ready for use - entering DSM or Cache"

\$!-------------------------------------------------------------

\$! \*\*START OF INFORMATION ONLY SECTION\*\*

\$! This section describes the basic commands for starting a generic

\$! listener.

\$! For DSM, replace 5000 below with the actual port number, and change

\$! the file name to reflect the change of the port number as recommended

\$! above.

\$! dsm/env=dsmmgr/uci=vah/vol=rou/data="''x'^5000" port^hlcstcpa

\$! For Cache, replace 5000 below with the actual port number, and change

\$! the file name to reflect the change of the port number as recommended

\$! above.

\$! port=port number

\$! cache "-U" "VAH" "port^hlcstcpa"

\$! \*\*END OF INFORMATION ONLY SECTION\*\*

\$!-------------------------------------------------------------

\$! \*\*Be sure the command line(s) in the COMMAND LINE SECTION

\$! \*\*below is correct for your system and if access control is enabled,

\$! \*\*that this account has access to this uci,vol & routine.

\$! \*\*An entry in file 870 for this logical link with the specified

\$! \*\*unique port number and its device type as "MS"(Multi-threaded

\$! \*\*server) must be existed.

\$!

\$!-------------------------------------------------------------

\$! COMMAND LINE SECTION:

\$! =====================

\$!-------------------------------------------------------------

\$! for DSM, replace 5000 below with the actual port number, and change

\$! the file name to reflect the change of the port number as recommended

\$! above.

\$! dsm/env=dsmmgr/uci=vah/vol=rou/data="''x'^5000" PORT^HLCSTCPA

\$!-------------------------------------------------------------

\$! For Cache, replace 5000 below with the actual port number, and change

\$! the file name to reflect the change of the port number as recommended

\$! above.

\$ PORT=5000

\$ cache "-U" "VAH" "PORT^HLCSTCPA"

\$ endif

\$ exit:

\$ logout/brief

## Set Up and Enable the TCP/IP Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Set up the TCP/IP Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](hl7-hl-1-6-84-multi-listeners-using-tcp-ip-svcs-for-openvms/017.png)</td>
<td><ul>
<li><p>Since TCP/IP Services is node specific, make sure you are on the same node that you want the listener to run on.</p></li>
<li><p>It is possible to run the TCP/IP service on multiple nodes. This may or may not be necessary, depending on your site's configuration needs. For instance, the impersonator VMS feature allows for the possibility of all nodes in the cluster to become the surrogate. This allows for the listening process uninterrupted if the TCP/IP service is enabled on all nodes in the cluster. For this reason, it is recommended that you enable the TCP/IP service on all nodes in the cluster.</p></li>
</ul></td>
</tr>
</tbody>
</table>

Ensure that your new TCP/IP service uses the recommended naming convention. To set up a service that will be listening on port 5000 and use a corresponding DCL login command file HLS5000CACHE.COM,

Set the service name as HLS5000CACHE as follows:

\$ TCPIP (must use continuation character "-" at end of long lines)

TCPIP\> SET SERVICE HLS5000CACHE/USER=HLSEVEN/PROC=HLS5000CACHE /PORT=5000-

\_TCPIP\> /PROTOCOL=TCP/REJECT=MESSAGE="All channels busy" -

\_TCPIP\> /LIMIT=50/FILE=USER\$:\[HLSEVEN\]HLS5000CACHE.COM

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](hl7-hl-1-6-84-multi-listeners-using-tcp-ip-svcs-for-openvms/018.png)</td>
<td><ul>
<li><p>If you get an error because you mistyped any of the above lines or forgot to use the continuation character "-", we suggest you do the following to remove the corrupted service and repeat the above commands.</p>
<p>TCPIP&gt; <strong>SET CONFIG ENABLE NOSERVICE HLS5000CACHE</strong></p></li>
</ul>
<blockquote>
<p>TCPIP&gt; <strong>SET NOSERVICE HLS5000CACHE</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

TCPIP\> SHO SERVICE HLS5000CACHE/FULL

Service: HLS5000CACHE

State: Disabled

Port: 5000 Protocol: TCP Address: 0.0.0.0

User_name: not defined Process: HLS5000CACHE

### Enable and Save the TCP/IP Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Since TCP/IP Services is node specific, make sure you are on the same node that you want the listener to run on.

TCPIP\> ENABLE SERVICE HLS5000CACHE *(enable service immediately)*

TCPIP\> SET CONFIG ENABLE SERVICE HLS5000CACHE *(save service for reboot)*

TCPIP\> SHO SERVICE/FULL HLS5000CACHE

Service: HLS5000CACHE

State: Enabled

Port: 5000 Protocol: TCP Address: 0.0.0.0

Inactivity: 5 User_name: HLSEVEN Process: HLS5000CACHE

Limit: 50 Active: 0 Peak: 0

File: USER\$:\[HLSEVEN\] HLS5000CACHE.COM

Flags: Listen

Socket Opts: Rcheck Scheck

Receive: 0 Send: 0

Log Opts: None

File: not defined

Security

Reject msg: All channels busy

Accept host: 0.0.0.0

Accept netw: 0.0.0.0

TCPIP\> SHO CONFIG ENABLE SERVICE

Enable service

FTP, FTP_CLIENT, HLS5000CACHE, MPI, TELNET, XMINETMM

TCPIP\> EXIT

You are now ready to migrate to Caché. Perform the necessary steps for migration including any backups, disk conversions and shutdown of DSM.

After the migration is complete and Caché is activated for use, remember to enable the HL7 TCP/IP service(s), if you have not already done so.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 92%" />
</colgroup>
<tbody>
<tr class="odd">
<td>![](hl7-hl-1-6-84-multi-listeners-using-tcp-ip-svcs-for-openvms/019.png)</td>
<td><ul>
<li><p>If you’ve enabled the impersonator VMS feature, it is recommended that you enable the HL7 TCP/IP service(s) on all nodes in the cluster.</p></li>
</ul></td>
</tr>
</tbody>
</table>

# Appendix

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## HLSEVEN.COM DCL Login Command Procedure

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This DCL login command procedure file, HLSEVEN.COM, is included in the appendix for reference. This command procedure is no longer recommended as it is being replaced by command procedures that use the actual port number of its corresponding TCP/IP service.

\$!HLSEVEN.COM - for incoming tcp connect requests

\$! Revision History:

\$! Patch HL\*1.6\*19 & HL\*1.6\*56--Documentation only

\$! Patch HL\*1.6\*70--HL71_6P70.COM

\$! Patch HL\*1.6\*84--HL71_6P84.COM

\$!-------------------------------------------------------------

\$ set noon !Don't stop

\$ set noverify !change as needed

\$! set verify !change as needed

\$ purge/keep=5 sys\$login:\*.log !Purge log files only

\$ set proc/priv=(share) !Required for MBX device

\$ x=f\$trnlnm("sys\$net") !This is our MBX device

\$!

\$ write sys\$output "Opening "+x !This can be viewed in the log file

\$! Check status of the BG device before going to either DSM or Cache'

\$ cnt=0

\$ CHECK:

\$ stat=f\$getdvi("''x'","STS")

\$ if cnt .eq. 10

\$ then

\$ write sys\$output "Could not open ''x' - exiting"

\$ goto EXIT

\$ else

\$ if stat .ne. 16

\$ then

\$ cnt=cnt+1

\$ write sys\$output "''cnt'\> ''x' not ready!"

\$ wait 00:00:01 !Wait one second to assure connection

\$ goto CHECK

\$ else

\$ write sys\$output "''x' is now ready for use - entering DSM or Cache"

\$!-------------------------------------------------------------

\$! \*\*START OF INFORMATION ONLY SECTION\*\*

\$! This section describes the basic commands for starting a generic listener.

\$! for DSM TCP/IP

\$! dsm/env=dsmmgr/uci=vah/vol=rou/data="''x'^999" en^routine

\$! for Cache TCP/IP

\$! assign 'f\$trnlnm("SYS\$NET")' SYS\$NET

\$! ccontrol session \<configname\> "-U" "namespace" "tag^routine"

\$! For a Cache batch routine

\$! cache "-U" "VAH" "^routine"

\$! \*\*END OF INFORMATION ONLY SECTION\*\*

\$!-------------------------------------------------------------

\$! \*\*Be sure the command line(s) in the COMMAND LINE SECTION

\$! \*\*below is correct for your system and if access control is enabled,

\$! \*\*that this account has access to this uci,vol & routine.

\$! \*\*The number 999 should be replaced with the internal entry

\$! \*\*number in file 870 for this Logical Link.

\$!

\$! \*\*Also, comment or uncomment the appropriate lines for your system.

\$!

\$!-------------------------------------------------------------

\$! COMMAND LINE SECTION:

\$! =====================

\$!-------------------------------------------------------------

\$! for DSM

\$! dsm/env=dsmmgr/uci=vah/vol=rou/data="''x'^999" EN^HLCSTCP

\$!-------------------------------------------------------------

\$! for Cache

\$ assign 'f\$trnlnm("SYS\$NET")' SYS\$NET

\$ pipe (write sys\$output "D CACHEVMS^HLCSTCP(""999"")" \| cache -"U" "VAH")

\$!-------------------------------------------------------------

\$ endif

\$ exit:

\$ logout/brief

\$

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ACL                            | Access Control List                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| CALLABLE ENTRY POINT           | Authorized programmer call that may be used in any V*IST*A application package. The DBA maintains the list of DBIC-approved entry points.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| DATA                           | A representation of facts, concepts, or instructions in a formalized manner for communication, interpretation, or processing by humans or by automatic means. The information you enter for the computer to store and retrieve. Characters that are stored in the computer system as the values of local or global variables. VA FileMan fields hold data values for file entries.                                                                                                                                                                                                                                                                   |
| DBA                            | Database Administrator, oversees package development with respect to V*IST*A Standards and Conventions (SAC) such as namespacing. Also, this term refers to the Database Administration function and staff.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| DBIA                           | Database Integration Agreement, a formal understanding between two or more V*IST*A packages, which describes how data is shared or how packages interact. The DBA maintains a list of DBIAs.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| DCL                            | Digital Command Language                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| DEFAULT                        | Response the computer considers the most probable answer to the prompt being given. It is identified by double slash marks (//) immediately following it. This allows you the option of accepting the default answer or entering your own answer. To accept the default you simply press the Enter (or Return) key. To change the default answer, type in your response.                                                                                                                                                                                                                                                                             |
| DEPARTMENT OF VETERANS AFFAIRS | The Department of Veterans Affairs, formerly called the Veterans Administration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| DSM                            | Digital Standard MUMPS                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ENTRY                          | VA FileMan record. It is uniquely identified by an internal entry number (the .001 field) in a file.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| FIELD                          | In a record, a specified area used for the value of a data attribute. The data specifications of each VA FileMan field are documented in the file’s data dictionary. A field is similar to blanks on forms. It is preceded by words that tell you what information goes in that particular field. The blank, marked by the cursor on your terminal screen, is where you enter the information.                                                                                                                                                                                                                                                       |
| FILE                           | Set of related records treated as a unit. VA FileMan files maintain a count of the number of entries or records.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| FILE MANAGER (VA FILEMAN)      | The V*IST*A’s Database Management System (DBMS). The central component of the Kernel that defines the way standard V*IST*A files are structured and manipulated.                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| FORUM                          | The central E-mail system within V*IST*A. It is used by developers to communicate at a national level about programming and other issues. FORUM is located at the CIO Field Office - Washington, DC (162-2).                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| GLOBAL VARIABLE                | Variable that is stored on disk (M usage).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| HL7                            | Health Level Seven (HL7) is an application protocol for electronic data exchange in health care environments. The HL7 protocol is a collection of standard formats that specify the implementation of interfaces between computer applications from different vendors. This communication protocol allows healthcare institutions to exchange key sets of data amount different application systems. Flexibility is built into the protocol to allow compatibility for specialized data sets that have facility-specific needs.                                                                                                                      |
| HL7 BATCH PROTOCOL             | Protocol utilized to transmit a batch of HL7 messages. The protocol uses FHS, BHS, BTS and FTS segments to delineate the batch.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| KERNEL                         | Set of V*IST*A software routines that function as an intermediary between the host operating system and the V*IST*A application packages such as Laboratory, Pharmacy, IFCAP, etc. The Kernel provides a standard and consistent user and programmer interface between application packages and the underlying M implementation.                                                                                                                                                                                                                                                                                                     |
| LINK                           | Non-specific term referring to ways in which files may be related (via pointer links). Files have links into other files.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| MENU                           | List of choices for computing activity. A menu is a type of option designed to identify a series of items (other options) for presentation to the user for selection. When displayed, menu-type options are preceded by the word “Select” and followed by the word “option” as in Select Menu Management option: (the menu’s select prompt).                                                                                                                                                                                                                                                                                                         |
| MESSAGE                        | A message is the atomic unit of data transferred between systems. It is comprised of a group of segments in a defined sequence. Each message has a message type that defines its purpose. For example, the ADT Message type is used to transmit portions of a patient’s ADT data from one system to another. A three-character code contained within each message identifies its type.                                                                                                                                                                                                                                                               |
| MESSAGE TYPE                   | Each message has a message type that defines its purpose. For example, the ADT Message Type is used to transmit portions of a patient’s ADT data from one system to another. A 3-character code contained within each message identifies its type.                                                                                                                                                                                                                                                                                                                                                                                                   |
| NAMESPACING                    | Convention for naming V*IST*A package elements. The DBA assigns unique character strings for package developers to use in naming routines, options, and other package elements so that packages may coexist. The DBA also assigns a separate range of file numbers to each package.                                                                                                                                                                                                                                                                                                                                                          |
| NT                             | New Technology                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| OPTION                         | An entry in the OPTION file. As an item on a menu, an option provides an opportunity for users to select it, thereby invoking the associated computing activity. Options may also be scheduled to run in the background, non-interactively, by Task Manager.                                                                                                                                                                                                                                                                                                                                                                                         |
| PACKAGE                        | The set of programs, files, documentation, help prompts, and installation procedures required for a given software application. For example, Laboratory, Pharmacy, and PIMS are packages. A V*IST*A software environment composed of elements specified via the PACKAGE file (#9.4). Elements include files and associated templates, namespaced routines, and namespaced file entries from the OPTION, HELP FRAME, BULLETIN, and FUNCTION files. As public domain software, packages may be requested through the Freedom of Information Act (FOIA).                                                                                        |
| POINTER                        | The address at which a data value is stored in computer memory. A relationship between two VA FileMan files, a pointer is a file entry that references another file (forward or backward). Pointers can be an efficient means for applications to access data by referring to the storage location at which the data exists.                                                                                                                                                                                                                                                                                                                         |
| PROMPT                         | The computer interacts with the user by issuing questions called prompts, to which the user issues a response.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| RECORD                         | Set of related data treated as a unit. An entry in a VA FileMan file constitutes a record. A collection of data items that refer to a specific entity (e.g., in a name-address-phone number file, each record would contain a collection of data relating to one person).                                                                                                                                                                                                                                                                                                                                                                            |
| ROUTINE                        | Program or a sequence of instructions called by a program that may have some general or frequent use. M (previously referred to as MUMPS) routines are groups of program lines, which are saved, loaded, and called as a single unit via a specific name.                                                                                                                                                                                                                                                                                                                                                                                            |
| SAC                            | Standards and Conventions. Through a process of verification, V*IST*A packages are reviewed with respect to SAC guidelines as set forth by the Standards and Conventions Committee (SACC). Package documentation is similarly reviewed in terms of standards set by the Documentation Standards and Conventions Committee (DSCC).                                                                                                                                                                                                                                                                                                            |
| SACC                           | V*IST*A 's Standards and Conventions Committee. This Committee is responsible for maintaining the SAC.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| SEGMENT                        | An HL7 segment is a logical grouping of data fields. Segments of a message may be required or optional. They may occur only once in a message or they may be allowed to repeat. Each segment is identified by a unique three-character code known as the Segment ID.                                                                                                                                                                                                                                                                                                                                                                                 |
| SEGMENT (RECORD)               | A typed aggregate of fields (fields) describing one complete aspect of a message. For example, the information about one order is sent as type of segment (OBR), the information related to an observation is sent as another segment (OBX). The segment in a message is analogous to a record in a database, and in previous versions of the standard we used record in place of the word segment. We have changed the nomenclature to be consistent with HL7 and other standards organizations in this version.                                                                                                                                    |
| TCP/IP                         | Transmission Control Protocol/Internet Protocol                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| TEMPLATE                       | Means of storing report formats, data entry formats, and sorted entry sequences. A template is a permanent place to store selected fields for use later. Edit sequences are stored in the INPUT TEMPLATE file (#.402), print specifications are stored in the PRINT TEMPLATE file (#.4), and search or sort specifications are stored in the SORT TEMPLATE file (#.401).                                                                                                                                                                                                                                                                             |
| VA                             | The Department of Veterans Affairs, formerly called the Veterans Administration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| VA FILEMAN                     | Set of programs used to enter, maintain, access, and manipulate a database management system consisting of files. A package of online computer routines written in the M language, which can be used as a stand-alone database system or as a set of application utilities. In either form, such routines can be used to define, enter, edit, and retrieve information from a set of computer stored files.                                                                                                                                                                                                                                          |
| VARIABLE                       | Character, or group of characters, that refers to a value. M (previously referred to as MUMPS) recognizes 3 types of variables: local variables, global variables, and special variables. Local variables exist in a partition of main memory and disappear at sign-off. A global variable is stored on disk, potentially available to any user. Global variables usually exist as parts of global arrays. The term “global” may refer either to a global variable or to a global array. A special variable is defined by systems operations (e.g., \$TEST).                                                                                         |
| V*IST*A                | Veterans Health Information Systems and Technology Architecture (V*IST*A) (formerly the Decentralized Hospital Computer Program \[DHCP\]) of the Veterans Health Administration (VHA), Department of Veterans Affairs (VA). V*IST*A software, developed by VA, is used to support clinical and administrative functions at VA Medical Centers nationwide. It is written in M, and, via the Kernel runs on all major M implementations regardless of vendor. V*IST*A is composed of packages, which undergo a verification process to ensure conformity with namespacing and other V*IST*A standards and conventions. |
| VMS                            | Virtual Memory System                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
