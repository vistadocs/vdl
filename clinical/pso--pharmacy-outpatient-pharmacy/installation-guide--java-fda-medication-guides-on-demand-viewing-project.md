---
title: Java-FDA Medication Guides On-Demand Viewing Project - Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: Java-FDA Medication Guides On-Demand Viewing Project
app_code: PSO
app_name: "Pharmacy: Outpatient Pharmacy"
section: CLI
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 0
description: > ![](java-fda-medication-guides-on-demand-viewing-project-installation-guide/001.png)
audience: 
keywords: 
  - demand
  - java
  - guide
  - software
  - installation
  - medication
  - guides
  - component
  - viewer
  - table
page_count: 0
word_count: 1846
section_count: 2
table_count: 3
figure_count: 12
appendix_count: 0
has_toc: False
is_stub: False
pub_date: February 2021
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy/PHAR_FDA_MED_GUIDE_ONDEMAND_PSN_570_IG.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Outpatient_Pharmacy/PHAR_FDA_MED_GUIDE_ONDEMAND_PSN_570_IG.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=90"
---

> ![](java-fda-medication-guides-on-demand-viewing-project-installation-guide/001.png)

FDA Medication Guides (PSN\*4\*570)On-Demand Java ComponentInstallation Guide

February 2021

Version 1.0.2.0

Product Development

# Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Revision History](#revision-history)
- [Section 1: Introduction](#section-1-introduction)
- [Section 2: Pre-Installation Considerations](#section-2-pre-installation-considerations)
  - [The FDA Med Guides On-Demand Viewer Java software component requires Java Runtime Environment (JRE), a third-party software component to display and print Portable Document Format (PDF) documents. Java Runtime Environment (JRE) must be properly installed and configured prior to installing and running the FDA Med Guides On-Demand Viewer Java software component.](#the-fda-med-guides-on-demand-viewer-java-software-component-requires-java-runtime-environment-jre-a-third-party-software-component-to-display-and-print-portable-document-format-pdf-documents-java-runtime-environment-jre-must-be-properly-installed-and-configured-prior-to-installing-and-running-the-fda-med-guides-on-demand-viewer-java-software-component)
- [Section 3: Installing On-Demand Java Software](#section-3-installing-on-demand-java-software)
<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 12%" />
<col style="width: 43%" />
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
<td>02/2021</td>
<td><blockquote>
<p>1.0.2.0</p>
</blockquote></td>
<td><blockquote>
<p>Fortify security fixes for the security analysis on 07/2020 released with patch PSN*4*570.</p>
<p>Update document to remove section detailing associated VistA patch installations from original release.</p>
<p>Update screen captures and label figures.</p>
</blockquote></td>
<td><blockquote>
<p>HPS Clinical Sustainment team</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>12/2014</td>
<td>1.0.1.0</td>
<td>Support the new secure CMOP Server using HTTPS functionality released with patches PSS*1*177 and PSN*4*364 and made formatting changes.</td>
<td>Enterprise Application Maintenance team</td>
</tr>
<tr class="even">
<td>04/2011</td>
<td>1.0</td>
<td>Original Version</td>
<td><mark>REDACTED</mark></td>
</tr>
</tbody>
</table>
*(This page included for two-sided copying.)*Table of Contents
*(This page included for two-sided copying.)*

# Section 1: Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This Installation Guide provides a description of the installation and deployment procedures for the

Department of Veterans Affairs (VA) Food and Drug Administration (FDA) Medication Guides

Increment 2 project. This guide focuses on the project’s FDA Med Guides Java On-Demand Viewer component. The FDA Med Guides On-Demand Viewer component is a Java-based application that manually displays a copy of an FDA medication guide Portable Document Format (PDF) file in a web browser on the user’s computer.

The Outpatient Pharmacy application was modified to allow pharmacists to manually display and print an FDA Medication Guide for a specific prescription when one is available. The National Drug File application was also modified to allow users to retrieve and print the FDA Medication Guides for specific VA Product entries when one is available. A Java software component has been created specifically for this project to allow the retrieval of the FDA Medication Guide from a web server repository via a web browser. The On-Demand Viewer Java software component must be installed in the user’s computer for the functionality to work correctly.

Before You Begin

| Important:                                                                                           | Administrator-level permissions are required to both install and uninstall the required FDA Medication Guide On-Demand Java software component on the individual workstations. |
|------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](java-fda-medication-guides-on-demand-viewing-project-installation-guide/002.png) |                                                                                                                                                                                |

The intended audience for this document is the Information Resources Management Service (IRMS) staff responsible for installing and configuring software on VA Windows computers.

Installation will take about 10-15 minutes and must be performed on every computer where the user needs to retrieve and display an FDA Medication Guide.

After installation is complete, the individual computers will need to be rebooted. Any logged-on users should be advised to log off.

# Section 2: Pre-Installation Considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## The FDA Med Guides On-Demand Viewer Java software component requires Java Runtime Environment (JRE), a third-party software component to display and print Portable Document Format (PDF) documents. Java Runtime Environment (JRE) must be properly installed and configured prior to installing and running the FDA Med Guides On-Demand Viewer Java software component.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Java Runtime Environment (JRE) is not distributed as part of this package. Download and install a VA TRM compliant version of Java Runtime Environment (JRE) prior to installation of the FDA Medication Guide On-Demand Viewer application.

According to the Technical Reference Model (TRM) forecast, Java Runtime Environment 1.8.271 is supported as of this writing.

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th>Note:</th>
<th rowspan="2"><p>To confirm whether Java 1.6 is already installed on the computer, or was installed correctly, open a command window and type the command:</p>
<p><strong>java -version</strong></p>
<p>Information text should appear in the command window, indicating the nomenclature of the java version. If Java is not installed, or not installed properly, the message returned will indicate:</p>
<p>“Java is not a recognized system command.”</p></th>
</tr>
<tr class="odd">
<th>![](java-fda-medication-guides-on-demand-viewing-project-installation-guide/003.png)</th>
</tr>
</thead>
<tbody>
</tbody>
</table>

Refer to the VA Technical Reference Model (TRM) [<u>http://trm.oit.va.gov/TRMHomePage.aspx</u>](http://trm.oit.va.gov/TRMHomePage.aspx) for the approved versions of Java Runtime Environment (JRE).

# Section 3: Installing On-Demand Java Software

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> **NOTE:** Administrator-level permissions are required to both install and uninstall the required software on the individual computers.

<span id="_Toc64532806" class="anchor"></span>3.1 Obtain ZIP distribution file

The FDA Medical Guide On-Demand Java software component is distributed as a ZIP-compressed file (PSN_4_P570.zip) containing a single EXE executable file. Download and Unzip the file contents into a temporary folder of your choice. After successfully installed, the zip file and setup file may be deleted.

The file can be obtained from the following location:

https://download.<span class="mark">REDACTED</span>/index.html/

Table 1: Downloadable File

| File Name      | Retrieval Format |
|----------------|------------------|
| PSN_4_P570.zip | BINARY           |

| Note:                                                                                                | Computers that are currently running the FDA Med Guides On-Demand Viewer Java component software can go directly to Section 3.5 Upgrading to a new version of On Demand. |
|------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ![](java-fda-medication-guides-on-demand-viewing-project-installation-guide/004.png) |                                                                                                                                                                          |

<span id="_Toc64532807" class="anchor"></span>3.2 Installing the On-Demand Component Software

To install and test the On-Demand Med Guide Viewer component software, follow these instructions.

> **NOTE:** Since the On-Demand Med Guide Viewer component software is a Java application, it requires that the Java Runtime Environment (JRE) be installed on the computer. JRE is not distributed as part of this package and must be separately downloaded and installed. JRE version 1.6 or newer, is required. If JRE 1.6 is already installed on the computer, you may skip this step.

1)  Run the executable installer.
2)  Locate the file named “On-Demand_Med_Guide_Viewer-x.x.x.x_setup.exe” (x.x.x.x represents a four-digit version number separated by dots.)
3)  Double-click on the file name to start/run the installer.
4)  The installer detects whether you already have a compatible version of Java installed on your PC. If not, the installer aborts and prompts you to download and install Java JRE.
5)  When JRE installation is complete, close the residual installer window.
6)  Reboot, when prompted to do so and continue.

Figure 1: Example of On-Demand Installer.

![](java-fda-medication-guides-on-demand-viewing-project-installation-guide/005.png)

Figure 2: Example of On-Demand Installation without JRE installed

![](java-fda-medication-guides-on-demand-viewing-project-installation-guide/006.png)

Figure 3: Example of Successful On-Demand Installation

![](java-fda-medication-guides-on-demand-viewing-project-installation-guide/007.png)

Figure 4: Example of installed On-Demand Viewer Java Software version 1.0.0.12 in Control Panel:

![](java-fda-medication-guides-on-demand-viewing-project-installation-guide/008.png)

Figure 5: Example of installed On-Demand Viewer Java Software in Windows Explorer C:\Program Files (x86)\Vista\PSO\On-Demand_FDA_med_guides

![](java-fda-medication-guides-on-demand-viewing-project-installation-guide/009.png)

3.  <span id="_Toc64532808" class="anchor"></span>Test the installation and the application software
1.  Logon to Vista on a computer with the FDA Med Guide On-Demand Viewer component software installed using the roll-scroll interface.
2.  Request display of a specific med guide document from Vista.
    1.  <u>Test for Outpatient Pharmacy Application users:</u>
    2.  Logon to the Outpatient Pharmacy Application \[PSO MANAGER\]
    3.  Select the Patient Prescription Processing option \[PSO LM BACKDOOR ORDERS\], a.k.a. “Backdoor Pharmacy”, which is located under the Rx (Prescriptions) menu \[PSO RX\].
    4.  Select any Division.
    5.  Select any Patient.
    6.  Select one of the patient’s prescriptions with a dispense drug matched to a VA Product that contains an associated FDA Medication Guide.
    7.  Select hidden action OTH (Other OP Actions).
    8.  Select Item MG (Display FDA Medication Guide).
    9.  <u>Test for National Drug File Application users:</u>
    10. Logon to the National Drug File Application \[PSNMGR\].
    11. Select the Display FDA Medication Guide option \[PSN MED GUIDE\].
    12. When prompted for ‘VA PRODUCT NAME’, enter a VA Product that contains an associated FDA Medication Guide.

Figure 6: Example of VistA Roll and Scroll “Display FDA Medication Guide” \[PSN MED GUIDE\] option

![](java-fda-medication-guides-on-demand-viewing-project-installation-guide/010.png)

3.  After a few seconds, an FDA med guide should display within Adobe Acrobat Reader, embedded within the default Web Browser. This is the PDF file that you requested in the previous step. If the browser window opens and the med guide is displayed, the software is correctly installed and properly working.

Figure 7: Example of Successful FDA Med Guide .pdf display in Web Brower.

![](java-fda-medication-guides-on-demand-viewing-project-installation-guide/011.png)

3.  <span id="_Toc64532809" class="anchor"></span>Additional Technical details
- The Java component software will automatically run in the background each time the PC is booted/rebooted. There is no visible evidence that it is running.
- After the software is installed, there are no obvious signs of its presence other than the display of a med guide when requested. When not in use, the software remains silently in the background awaiting instructions. No GUI is associated with the application.
- The software is (by default) typically installed in the folder shown below in Figure 8 and contains the files listed in this folder.
- Registry entries affected by this installation are shown below in Figures 9-11.

Figure 8: Example of On-Demand installation folder

![](java-fda-medication-guides-on-demand-viewing-project-installation-guide/012.png)

Figure 9: Example of On-Demand Registry Entries

![](java-fda-medication-guides-on-demand-viewing-project-installation-guide/013.png)

Figure 10: Example of On-Demand Registry Entries continued.

![](java-fda-medication-guides-on-demand-viewing-project-installation-guide/014.png)

Figure 11: Example of On-Demand Registry Entries continued.

![](java-fda-medication-guides-on-demand-viewing-project-installation-guide/015.png)

3.  <span id="_Toc64532810" class="anchor"></span>Upgrading to a new version of On-Demand

If an old version of the On-Demand Java component software already exists on the workstation, the following steps need to be performed.

1.  Uninstall the old version of the On-Demand Med Guide Viewer software by following the instructions given in section 3.6 Uninstalling the On-Demand Component.
2.  Then install the new version On-Demand Med Guide Viewer software by following the instructions given in section 3.2 Installing the On-Demand Component Software.
    3.  <span id="_Toc64532811" class="anchor"></span>Uninstalling the On-Demand Component
1.  To remove the software from your PC, use the standard Add/Remove applet provided by Windows.
2.  Click on the Start button.
3.  Select Control Panel.
4.  Select the Uninstall a program applet in the Control Panel.
5.  Scroll down to the listings in the applet starting with the letter “O”.
6.  Choose the On-demand Med Guide Viewer entry as shown below:
7.  Click on the Remove button or Double click the entry
8.  A removal tool appears on the screen indicating that the software has been removed.
9.  Reboot

Figure 12: Example of Uninstalling On-Demand Viewer Java Component Software

![](java-fda-medication-guides-on-demand-viewing-project-installation-guide/016.png)