---
title: FMDC Technical Manual and Security Guide
doc_type: TM
doc_label: Technical Manual
doc_layer: plain
doc_subject: FMDC  and Security Guide
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
  - fileman
  - delphi
  - table
  - contents
  - components
  - unit
  - fmdc
  - security
  - server
  - compiled
page_count: 0
word_count: 2495
section_count: 17
table_count: 4
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: July 1999
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Fileman_Delphi_Comp_(FMDC)/fmdc1_0p1tm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Fileman_Delphi_Comp_(FMDC)/fmdc1_0p1tm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=6"
---

![](fmdc-technical-manual-and-security-guide/001.png)

FILEMAN DELPHI COMPONENTS(FMDC)TECHNICAL MANUAL and  
SECURITY GUIDE

Version 1.0\*1

July 1999

VHA CIO Technical Services

Table of Contents

Introduction [3](#introduction)

Related Manuals [3](#related-manuals)

Implementation and Maintenance [5](#implementation-and-maintenance)

Files [5](#files)

M Server Files [5](#m-server-files)

Client (Developer Workstation): FMDC File Listing [5](#_Toc91297992)

Routines [8](#routines)

Exported Options [8](#exported-options)

Archiving and Purging [8](#archiving-and-purging)

Callable Routines/Entry Points/APIs [8](#callable-routinesentry-pointsapis)

External Interfaces [8](#external-interfaces)

External Relations [9](#external-relations)

Relationship with the VA FileMan (Server RPCs) [9](#relationship-with-the-va-fileman-server-rpcs)

Relationship with the RPC Broker (Server Routines) [10](#relationship-with-the-rpc-broker-server-routines)

Relationship with the RPC Broker Development Kit (BDK) [10](#relationship-with-the-rpc-broker-development-kit-bdk)

Internal Relations [10](#internal-relations)

Package-Wide Variables [10](#package-wide-variables)

Software Product Security [11](#software-product-security)

Security Management [11](#security-management)

Mail Groups and Alerts [11](#mail-groups-and-alerts)

Remote Systems [11](#remote-systems)

Interfacing [11](#interfacing)

Electronic Signatures [11](#electronic-signatures)

Menus [13](#menus)

Security Keys [13](#security-keys)

File Security [13](#file-security)

References [13](#references)

Official Policies [13](#official-policies)

Glossary [14](#glossary)

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Related Manuals](#related-manuals)
- [# # Implementation and Maintenance](#implementation-and-maintenance)
- [Files](#files)
  - [M Server Files](#m-server-files)
  - [Client (Developer Workstation): FMDC File Listing](#client-developer-workstation-fmdc-file-listing)
- [Routines](#routines)
- [Exported Options](#exported-options)
- [Archiving and Purging](#archiving-and-purging)
- [Callable Routines/Entry Points/APIs](#callable-routinesentry-pointsapis)
- [External Interfaces](#external-interfaces)
- [External Relations](#external-relations)
  - [Relationship with the VA FileMan (Server RPCs)](#relationship-with-the-va-fileman-server-rpcs)
  - [Relationship with the RPC Broker (Server Routines)](#relationship-with-the-rpc-broker-server-routines)
  - [Relationship with the RPC Broker Development Kit (BDK)](#relationship-with-the-rpc-broker-development-kit-bdk)
- [Internal Relations](#internal-relations)
- [Package-Wide Variables](#package-wide-variables)
- [Software Product Security](#software-product-security)
  - [Security Management](#security-management)
  - [Mail Groups and Alerts](#mail-groups-and-alerts)
  - [Remote Systems](#remote-systems)
  - [Interfacing](#interfacing)
  - [Electronic Signatures](#electronic-signatures)
  - [Menus](#menus)
  - [Security Keys](#security-keys)
  - [File Security](#file-security)
  - [References](#references)
  - [Official Policies](#official-policies)
- [# Glossary](#glossary)
The FileMan Delphi Components make it easy for developers to work with VA FileMan data in Delphi applications. The components encapsulate the details of retrieving, validating and updating VA FileMan data within a Delphi application. This saves you from creating your own custom remote procedure calls (RPCs) when you need to access VA FileMan data.
The FileMan Delphi Components also include special enhanced features such as complete server-side error checking and data dictionary help.
If you're already familiar with Delphi, the time needed to develop an application to edit a set of VA FileMan fields using the FileMan Delphi Components is comparable to the time needed to create the same application using VA FileMan's roll-and-scroll ScreenMan interface.

## Related Manuals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- *FileMan Delphi Components V. 1.0 Installation Guide*  
  Provides instructions for installing the FileMan Delphi Components.
- *FileMan Delphi Components V. 1.0 Getting Started Guide*  
  Gets you started with using the FileMan Delphi Components.
- *FMDC.HLP Help File*  
  Provides complete information on the FileMan Delphi Components, including full listings of each component's methods and properties.
- *VA FileMan Programmer Manual  
  *Provides complete information on the VA FileMan Database Server (DBS) API. The FMDC data access components are wrappers around calls in the VA FileMan Database Server (DBS) API. An online version of this documentation is available at the VA FileMan web page:  
    
  <http://www.va.gov/vdl/Infrastructure.asp?appID=6>

# # # Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FileMan Delphi Components do not have any site parameters, nor do they have any site configurability.

# Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## M Server Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FileMan Delphi Components do not export any files for M servers. VA FileMan (in patch DI\*21\*34 for version 21, and as a part of version 22), however, exports routines and remote procedure calls (RPCs) required for use by the FileMan Delphi components on any M servers they are used to access.

## Client (Developer Workstation): FMDC File Listing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A single self-extracting .EXE file (FMDC1_0.EXE or patched version, e.g., FMDC1_0P1.EXE) is provided to install the FileMan Delphi Components on developer workstations. The files distributed are:

Delphi 4 Installation

DIACCESS.DCU Diaccess compiled unit

DIACCESS.PAS Pascal source file

DIDATAPROB.DCU Didataprob compiled unit

DIDATAPROB.DFM Form for didataprob unit

DIDATAPROB.PAS Pascal source file

DIERR.DCU Dierr compiled unit

DIERR.DFM Form for dierr unit

DIERR.PAS Pascal source file

DIHLP.DCU Dihlp compiled unit

DIHLP.DFM Form for dihlp unit

DIHLP.PAS Pascal source file

DITYPLIB.DCU Dityplib compiled unit

DITYPLIB.PAS Pascal source file

FMCMPNTS.DCR Resources for fmcmpnts unit

FMCMPNTS.DCU Fmcmpnts compiled unit

FMCMPNTS.PAS Pascal source file

FMCNTRLS.DCR Resources for fmcntrls unit

FMCNTRLS.DCU Fmcntrls compiled unit

FMCNTRLS.PAS Pascal source file

FMDC.BPL Package library file for Delphi 4

FMDC.CNT Contents file for Online Help

FMDC.DCP Compiled Package file for Delphi 4

FMDC.DCU Compiled Unit for Delphi 4

FMDC.DPK Package source file for Delphi 4

FMDC.HLP Online Help

FMDC.RES Resource file

FMLOOKUP.DCR Resources for fmlookup unit

FMLOOKUP.DCU Fmlookup compiled unit

FMLOOKUP.DFM Form for fmlookup unit

FMLOOKUP.PAS Pascal source file

  
Delphi 3 Installation

DIACCESS.DCU Diaccess compiled unit

DIACCESS.PAS Pascal source file

DIDATAPROB.DCU Didataprob compiled unit

DIDATAPROB.DFM Form for didataprob unit

DIDATAPROB.PAS Pascal source file

DIERR.DCU Dierr compiled unit

DIERR.DFM Form for dierr unit

DIERR.PAS Pascal source file

DIHLP.DCU Dihlp compiled unit

DIHLP.DFM Form for dihlp unit

DIHLP.PAS Pascal source file

DITYPLIB.DCU Dityplib compiled unit

DITYPLIB.PAS Pascal source file

FMCMPNTS.DCR Resources for fmcmpnts unit

FMCMPNTS.DCU Fmcmpnts compiled unit

FMCMPNTS.PAS Pascal source file

FMCNTRLS.DCR Resources for fmcntrls unit

FMCNTRLS.DCU Fmcntrls compiled unit

FMCNTRLS.PAS Pascal source file

FMDC.CNT Contents file for Online Help

FMDC.DCP Compiled Package file for Delphi 3

FMDC.DCU Compiled Unit for Delphi 3

FMDC.DPK Package source file for Delphi 3

FMDC.DPL Package library file for Delphi 3

FMDC.HLP Online Help

FMDC.RES Resource file

FMLOOKUP.DCR Resources for fmlookup unit

FMLOOKUP.DCU Fmlookup compiled unit

FMLOOKUP.DFM Form for fmlookup unit

FMLOOKUP.PAS Pascal source file

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

# Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FileMan Delphi Components do not export any routines for M servers. VA FileMan (in patch DI\*21\*34 for version 21, and as a part of version 22), however, exports routines and remote procedure calls (RPCs) required for use by the FileMan Delphi components. These routines and RPCs need to be installed on any M servers that will be accessed by client applications compiled with the FileMan Delphi Components.

# Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FileMan Delphi Components do not export any options.

# Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FileMan Delphi Components do not store any data specific to the FMDC package, and therefore have no archiving or purging recommendations.

# Callable Routines/Entry Points/APIs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FileMan Delphi Components do not have any callable routines, entry points or APIs.

# External Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The external interfaces of the FileMan Delphi Components (components, objects and routines) are fully documented in the *FileMan Delphi Components Getting Started Manual* and in the online FMDC.HLP help file (distributed along with the component files).

The FileMan Delphi Components provide the following components for use in Delphi:

<table>
<colgroup>
<col style="width: 35%" />
<col style="width: 64%" />
</colgroup>
<tbody>
<tr class="odd">
<td><p>TFMFiler</p>
<p>TFMFinder</p>
<p>TFMFindOne</p>
<p>TFMGets</p>
<p>TFMHelp</p>
<p>TFMLister</p>
<p>TFMValidator</p>
<p>TFMLookUp</p>
<p>TFMCheckBox</p></td>
<td><p>TFMComboBox</p>
<p>TFMComboBoxLookUp</p>
<p>TFMEdit</p>
<p>TFMLabel</p>
<p>TFMListBox</p>
<p>TFMMemo</p>
<p>TFMRadioButton</p>
<p>TFMRadioGroup</p></td>
</tr>
</tbody>
</table>

The FileMan Delphi Components provide the following objects for use in Delphi:

> TFMErrorObj

> TFMFieldObj

> TFMHelpObj

> TFMRecordObj

The FileMan Delphi Components provide the following Pascal routines for use in Delphi:

> DeleteRecord

> LockNode

# External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In their initial release (FMDC 1.0), the FileMan Delphi Components were released as part of VA FileMan. The server-side RPCs and routines supporting FMDC were released in VA FileMan patch DI\*21\*34.

As of the release of patch FMDC\*1.0\*1, the FileMan Delphi Components are their own standalone package. They are assigned the namespace of FMDC (although there are currently no server side components in the FMDC namespace). A KIDS distribution is provided with patch FMDC\*1.0\*1 to update M server package files with the new FMDC package information.

The client side files and components are also now part of the FileMan Delphi Components package.

## Relationship with the VA FileMan (Server RPCs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As of patch FMDC\*1.0\*1, the FileMan Delphi Components have been granted integration agreements to use VA FileMan's DDR\* RPCs. To use these RPCs, the following minimum requirements for VA FileMan, on any server accessed using the FileMan Delphi Components, are:

- Patch DI\*21\*34 (or VA FileMan V. 22) Must be Installed  
    
  Client applications compiled with the FileMan Delphi Components require that the server(s) they connect to must have the support DDR\* RPCs and supporting DDR\* M routines installed. These RPCs and routines are distributed in patch DI\*21\*34, and also as part of VA FileMan V. 22.
- Patch DI\*21\*41 (or VA FileMan V. 22) Must be Installed  
    
  VA FileMan patch DI\*21\*41 (included in VA FileMan V. 22) provides a required update to make a DBS call compatible with the FileMan Delphi Components.

## Relationship with the RPC Broker (Server Routines)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- RPC Broker V. 1.1 or Greater Must be Installed  
    
  When you create an application with the FileMan Delphi Components, the server(s) your application connects to need to have the RPC Broker V. 1.1 or greater installed.

## Relationship with the RPC Broker Development Kit (BDK)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- The FileMan Delphi Components require that the RPC Broker BDK be installed in Delphi prior to installing the FileMan Delphi Components. The V. 1.0 FileMan Delphi Components are compatible with any RPC Broker V. 1.1 BDK, regardless of the patch level of the BDK.

# Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FileMan Delphi Components do not have any routines, files or options that cannot function independently.

# Package-Wide Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FileMan Delphi Components do not have any package-wide variables.

# Software Product Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Security Management

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User-level security for client applications compiled with the FileMan Delphi Components is controlled through Kernel's OPTION file, using the RPC Broker's security mechanisms:

- Users *without* programmer access to a server can run a particular client application that connects to an M server *only if* the application's corresponding "B"-type Kernel option has been assigned to that user by the M server's system manager. Furthermore, that Kernel option must register all of the RPCs used by the application in its RPC multiple.
- Developers *with* programmer access on a server (i.e., access to the server system and possession of the XUPROGMODE key on that system) can bypass the "B"-type Kernel option security requirements.

For more information on the RPC Broker's security mechanisms, please refer to the documentation for the RPC Broker package.

When developers create a Kernel "B"-type option for an application, they need to register all RPCs invoked by the client application. The RPCs they need to register can include custom ones designed specifically for that applications use, as well (if the client application uses any FileMan Delphi Components) the RPCs invoked by the particular FMDC components.

The table on the opposite page lists the RPCs invoked by FMDC components and Pascal routines.

## Mail Groups and Alerts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FileMan Delphi Components do not make use of mail groups, nor alerts.

## Remote Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FileMan Delphi Components, while supporting client/server connectivity for applications created by V*IST*A developers, do not, in and of themselves, transmit data to any remote systems or databases.

## Interfacing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Inprise Delphi (a commercial software development platform for building Windows client applications) is required to use the functionality provided in the FileMan Delphi Components. Delphi is an approved development platform for V*IST*A.

## Electronic Signatures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FileMan Delphi Components do not use electronic signatures.

RPCs Invoked by FMDC Components and Pascal Routines

|                         |                   |                      |
|-------------------------|-------------------|----------------------|
| FMDC Pascal Routine | Method        | Remote Procedure |
| DeleteRecord            | N/A               | DDR DELETE ENTRY     |
| LockNode                | N/A               | DDR LOCK/UNLOCK NODE |
| FMDC Component      | Method        | Remote Procedure |
| TFMCheckBox             | GetAndDisplayHelp | DDR GET DD HELP      |
|                         | GetHelp           | DDR GET DD HELP      |
|                         | Validate          | DDR VALIDATOR        |
| TFMComboBox             | GetAndDisplayHelp | DDR GET DD HELP      |
|                         | GetHelp           | DDR GET DD HELP      |
|                         | GetList           | DDR LISTER           |
|                         | GetMore           | DDR LISTER           |
|                         | Validate          | DDR VALIDATOR        |
| TFMComboBoxLookUp       | (always)          | DDR LISTER           |
|                         | (always)          | DDR FINDER           |
|                         | GetAndDisplayHelp | DDR GET DD HELP      |
|                         | GetHelp           | DDR GET DD HELP      |
|                         | Validate          | DDR VALIDATOR        |
| TFMEdit                 | GetAndDisplayHelp | DDR GET DD HELP      |
|                         | GetHelp           | DDR GET DD HELP      |
|                         | Validate          | DDR VALIDATOR        |
| TFMFiler                | Update            | DDR FILER            |
| TFMFinder               | GetFinderList     | DDR FINDER           |
| TFMFindOne              | GetIEN            | DDR FIND1            |
| TFMGets                 | GetAndFill        | DDR GETS ENTRY DATA  |
|                         | GetData           | DDR GETS ENTRY DATA  |
| TFMHelp                 | GetAndDisplayHelp | DDR GET DD HELP      |
|                         | GetHelp           | DDR GET DD HELP      |
| TFMLabel                | Validate          | DDR VALIDATOR        |
| TFMListBox              | GetAndDisplayHelp | DDR GET DD HELP      |
|                         | GetHelp           | DDR GET DD HELP      |
|                         | GetList           | DDR LISTER           |
|                         | GetMore           | DDR LISTER           |
|                         | Validate          | DDR VALIDATOR        |
| TFMLister               | GetList           | DDR LISTER           |
|                         | GetMore           | DDR LISTER           |
| TFMLookUp               | Execute           | DDR LISTER           |
| TFMMemo                 | GetAndDisplayHelp | DDR GET DD HELP      |
|                         | GetHelp           | DDR GET DD HELP      |
| TFMRadioButton          | GetAndDisplayHelp | DDR GET DD HELP      |
|                         | GetHelp           | DDR GET DD HELP      |
|                         | Validate          | DDR VALIDATOR        |
| TFMRadioGroup           | GetAndDisplayHelp | DDR GET DD HELP      |
|                         | GetHelp           | DDR GET DD HELP      |
|                         | Validate          | DDR VALIDATOR        |
| TFMValidator            | Validate          | DDR VALIDATOR        |

## Menus

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FileMan Delphi Components do not export any options.

## Security Keys

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FileMan Delphi Components do not export any security keys.

## File Security

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The FileMan Delphi Components do not export any files.

The FileMan Delphi Components, however, do provide generalized access to data in VA FileMan files, acting as Delphi component wrappers around VA FileMan's DBS (Database Server) calls. As with the underlying VA FileMan DBS calls, the FileMan Delphi Components do not rely on DUZ-based mechanisms to control access to data — neither Kernel's File Access Security (e.g., "Kernel Part Three") or VA FileMan's file security is used. Instead, security to files is controlled through the Kernel OPTION file. If a user has access to run the application through Kernel's (and the RPC Broker's) security mechanisms, then all database access *provided by the application* is enabled.

## References

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No particular regulations, VHA manuals or directives refer specifically to the FileMan Delphi Components.

## Official Policies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

No official polices refer specifically to the FileMan Delphi Components.

# # Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|            |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BDK        | Broker Development Kit. Provided with V*IST*A's RPC Broker software package, this contains the files necessary to connect to a V*IST*A M server from a Windows client.                                                                                                                                                                                                                                                                                                               |
| Components | In Delphi, components are building blocks from which an application can be constructed. Components include the visible parts of an application, such as buttons and memo fields, and invisible parts such as components that retrieve information from a server. Components can have properties, methods and events. Third parties (such as VHA OCIO Technical Services) can create and distribute components for use by Delphi developers along with the standard components distributed in Delphi. |
| DBS        | DataBase Server. VA FileMan's API that is optimized for accessing VA FileMan data from Windows clients.                                                                                                                                                                                                                                                                                                                                                                                              |
| Delphi     | A development product made by Inprise Corporation, and approved as a development platform for V*IST*A Windows client software.                                                                                                                                                                                                                                                                                                                                                               |
| DUZ        | The Kernel variable containing a user's identity.                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Inprise    | The company (formerly Borland) that makes Delphi.                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Objects    | Objects, in Delphi, are dynamically allocated portions of memory with a predetermined structure based on their Object Pascal class type.                                                                                                                                                                                                                                                                                                                                                             |
| Pascal     | The computer language used by Inprise Delphi (Delphi uses a version called Object Pascal).                                                                                                                                                                                                                                                                                                                                                                                                           |
| RPC Broker | The V*IST*A software development package that provides client/server connectivity between Windows clients and V*IST*A M servers.                                                                                                                                                                                                                                                                                                                                                     |
| Units      | Source code modules used in Pascal.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| VA FileMan | V*IST*A's main database management system (DBMS).                                                                                                                                                                                                                                                                                                                                                                                                                                            |