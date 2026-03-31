---
title: XWB*1.1*73 Readme File
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: Readme File
app_code: XWB
app_name: Remote Procedure Call (RPC) Broker
section: INF
app_status: active
pkg_ns: XWB
patch_ver: 1.1
patch_id: XWB*1.1*73
group_key: "XWB:XWB:1.1"
file_numbers: []
security_keys: []
menu_options: 0
description: ReadMe file for patch XWB\1.1\73 installation. There are no VistA M Server-side installation components for this patch.
audience: 
keywords: 
  - delphi
  - files
  - components
  - directory
  - your
  - source
  - vista
  - install
  - library
  - version
page_count: 0
word_count: 1017
section_count: 0
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: October 1997
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Remote_Proc_Call_Broker_(RPC)/xwb_1_1_73_rm_r.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Remote_Proc_Call_Broker_(RPC)/xwb_1_1_73_rm_r.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=23"
---

README File

Last Updated: 09/14/2021

============================================================================

Project: VistA Kernel Infrastructure Team

Software: RPC Broker Development Kit (BDK)

Current Version: 1.1

Original Software Release Date: October 1997

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Enterprise Program Management Office (EPMO)

============================================================================

This file contains any last-minute changes, new instructions (not found in

the documentation), and additional information to supplement the manuals.

ReadMe file for patch XWB\*1.1\*73 installation. There are no VistA M Server-side installation components for this patch.

> **NOTE:** This patch supports the following Delphi versions: XE8,

10.0, 10.1, 10.2, 10.3, and 10.4.

These components are only intended for use with the Delphi for Microsoft

Win32 version, and not Win64 or .NET.

> **NOTE:** If using FileMan Delphi Components (FMDC) and Kernel Delphi

Components (KDC), the Broker Development Kit (BDK) needs to be installed

first, then VA FileMan, and then Kernel.

This patch is provided as a zip file. To install it in the normal location,

move to the C:\Program Files (X86)\VistA directory. If you are a developer, you

can unzip the file in one location as a saved baseline, and make a

copy in the directory where you are doing your development. Any updates or

changes you make as part of your development should be passed to the VistA

Kernel Infrastructure team for review as a possible change to future

released versions of the BDK.

1\. Back up the existing BDK32 directory by renaming it (e.g., BDK32_P72)

in order to maintain the existing files.

2\. Unzip the provided zip file, making sure the "use folders" box is

checked, INTO the VistA directory - this will create the BDK32

directory and subdirectories under the VistA directory. These files

and subdirectories can be copied into a BDK32_P73 directory to

maintain the unmodified files for reference.

3\. After installing the zip file, there should be a BDK32 directory with

the following subdirectories:

\*BAPI32dll - BAPI32.DLL and sample header files.

\*BAPI32_73 - Source code for BAPI32_73.DLL.

\*Samples - Contains sample programs compiled with Delphi XE8:

\- BrokerEx: Contains BrokerExample.exe (includes CCOW and SSH code)

demonstrating Delphi GUI for VistA using 2-factor authentication (2FA).

\- BSE: Contains BseSample1.exe for Broker Security Enhancement (BSE).

\*Source - Contains source code and forms for the components.

4\. Open Delphi.

5\. Enter the library directories making sure that the directories are entered

into the Library fields.

6\. Open the menu Tools \| Options.

7\. Select the Library tab \[or open the menu Tools \| Options, expand the

Environment Options, then the Delphi Options, and select Library.\]

8\. Selected platform should be 32-bit Windows.

9\. Press the ellipsis (...) at the right of the combo box for Library Path.

10\. Either enter the directories in the edit box under the list box or press

the Folder at the right of the edit box and navigate to the

directories. For the default location, this is:

C:\Program Files (x86)\Vista\BDK32\Source

11\. Press Add.

12\. After entering the directory, press OK to close the dialogue.

If RPCBroker components already exist in the Delphi version:

1\. Select the menu Component \| Install Packages.

2\. Select the RPCBroker components (one at time).

3\. Press Remove to remove them.

4\. When finished, press the OK button.

To install the components into Delphi, it is best to compile and build them

in your version of the Delphi IDE, so that all of the necessary files are

placed in the proper default directories during installation. The location

of these default directories can vary depending on the version of operating system

you are using. The DesignTime package bundles the RunTime package into components

that are used when building applications, so the RunTime package *must* be

compiled before the DesignTime package is compiled and installed.

For your convenience, there are XWB_R\* (RunTime) and XWB_D\* (DesignTime)

projects set up for specific versions of Delphi, which may help resolve some

access violation errors for run time libraries in some versions. For example:

\* For Delphi 10 (Seattle) you would use the XWB_R10.dproj and the

XWB_D10.dproj files.

\* For Delphi XE8 you would use XWB_RXE8.dproj and the XWB_DXE8.dproj

files.

To install:

1\. Open Delphi and select the menu File \| Close All files, select

File \| Open, and then select the XWB_R\*.dpk or the XWB_R\*.dproj file

from the BDK32\Source directory.

2\. For the R or RunTime files, right-click on the XWB_R\*.bpl file

in the “Project Manager” frame, and then click Compile. Select the menu

File \| Close All (and respond yes if asked to save changes). \[The

RunTime files should always be compiled first, since the DesignTime

files are dependent upon them\].

3\. Select File \| Open to select the DesignTime XWB_D\*.dpk or the

XWB_D\*.dproj file. Right-click on the XWB_D\*.bpl file in the “Project

Manager” frame, and then click Build.

4\. Right-click on the XWB_D\*.bpl file in the “Project Manager” frame, and

then click Install to install or update the version of the components.

Select File \| Close All files (and respond yes if asked to save changes).

5\. The components are now installed and ready to use in your applications.

The contents of file "IAMBase.inc," which contains constants (defaults) used for

delegated 2-factor authentication (2FA) for Identity and Access Management, has

been moved into a new .pas file named IAMConstants.pas. The contents may be

edited if implementation is being tested in a non-production environment

with different values.

> **NOTE:** The RPC Broker Development Kit (BDK) uses wcrypt2.pas for certificate processing;

however, including the .pas file in the source tree for the BDK would cause

problems with developers using wcrypt2.pas in their other projects. The CPRS Team

pointed this out, and therefore, wcrypt2.pas is being referenced from the PKI

source tree, which was released in patch XU\*8.0\*639. It is imperative that you

include the path in the Delphi Library where your installation of the PKI source

tree is located. For instance, if you have your PKI source tree located in

C:\Projects\PKI then you should include C:\Projects\PKI in your Delphi Library

path; otherwise, the certificate functions will *not* be found and the BDK will

*not* compile/install. If you do *not* have patch XU\*8.0\*639 installed on your

development workstation, it may be downloaded from the any of the VA's FTP

sites. The address for the servers is: \<REDACTED\>.va.gov, and the patch

filename is: XU_8_0_P639.ZIP.