---
title: OR*3*243 and Associated Patches Installation Guide CPRS GUI 27
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: and Associated Patches  CPRS GUI 27
app_code: CPRS
app_name: Computerized Patient Record System
section: CLI
app_status: archive
pkg_ns: OR
patch_ver: 3
patch_id: OR*3*243
group_key: "CPRS:OR:3"
file_numbers: []
security_keys: []
menu_options: 0
description: <span class="smallcaps">CPRS GUI version 27</span><span class="smallcaps">(Patch# OR\3\243) and Associated Patches</span><span class="smallcaps">Installation Guide</span><span class="smallcaps">September 2008</span>
audience: 
keywords: 
  - cprs
  - orders
  - class
  - span
  - parameter
  - jaws
  - installation
  - order
  - files
  - patches
page_count: 0
word_count: 5782
section_count: 0
table_count: 0
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: September 2008
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)_Archive/or_30_243ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)_Archive/or_30_243ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=338"
---

![](or-3-243-and-associated-patches-installation-guide-cprs-gui-27/001.png)

<span class="smallcaps">CPRS GUI version 27</span><span class="smallcaps">(Patch# OR\*3\*243) and Associated Patches</span><span class="smallcaps">Installation Guide</span><span class="smallcaps">September 2008</span>

<span id="_Toc208213444" class="anchor"></span>Revision History

The most recent entries in this list are linked to the location in the manual they describe. Click on a link or page number to go to that section.

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 14%" />
<col style="width: 11%" />
<col style="width: 29%" />
<col style="width: 15%" />
<col style="width: 15%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Date</strong></td>
<td><strong>Version/<br />
Patch</strong></td>
<td><strong>Page</strong></td>
<td><strong>Change</strong></td>
<td><strong>Project Manager</strong></td>
<td><strong>Technical Writer</strong></td>
</tr>
<tr class="even">
<td>9/3/08</td>
<td>OR*3.0*300 (This is an informational patch only.)</td>
<td><a href="#related_patches">5</a></td>
<td><blockquote>
<p><a href="#related_patches">Removed patch RA*5.0*70 from list of related patches.</a></p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9/3/08</td>
<td>OR*3.0*300 (This is an informational patch only.)</td>
<td><a href="#Evalute_IV_Additives_and_solutions">12</a></td>
<td><blockquote>
<p><a href="#Evalute_IV_Additives_and_solutions">Added a step for sites to review entries for intravenous additive and solutions and change a field to Yes, so that users can change, renew, and copy orders with the IV additives and solutions.</a></p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
</tbody>
</table>

<span id="_Toc208213445" class="anchor"></span>Table of Contents

<span id="_Toc208213446" class="anchor"></span>CPRS GUI v27 Installation Requirements and Notes

CPRS GUI Version 27 consists of two host files and five patches that are not included in the two host files. The two host files are: OR_PSJ_PSO_27.KID and CPRS_BUNDLE_GUI_27_REQ_REL.KID. These two host files contain software patches that support CPRS GUI v27 functionality. The host files were created to simplify installation at Veterans Health Administration (VHA) facilities.

The five patches are: OR\*3.0\*281, OR\*3.0\*299, PSS\*1.0\*94, PSS\*1.0\*123 and GMTS\*2.7\*84. The PSS patches are distributed independent of the host files because of CMOP considerations. GMTS\*2.7\*84 is distributed independent of the host files because it requires OR\*3.0\*243 (CPRS GUI v27). OR\*3.0\*281 is distributed independent of the host files because it installs a menu option that sites should run to identify Radiology Quick Orders that need to be updated. The radiology quick orders cannot be updated until after the installation of OR\*3.0\*243, but the report will give sites an idea of the scope of the change, and sites should make plans accordingly. OR\*3.0\*299 requires OR\*3.0\*243 (CPRS GUI v27) and Identifies/Fixes Truncated Patient Instructions.

<span id="_Toc208213447" class="anchor"></span>Required Patches

Before you can install CPRS GUI v.27, you must verify that the following required patches are properly installed on your system:

- OR\*3.0\*232
- OR\*3.0\*245 
- OR\*3.0\*246
- OR\*3.0\*254
- OR\*3.0\*255
- OR\*3.0\*256
- OR\*3.0\*258
- OR\*3.0\*265
- OR\*3.0\*275
- OR\*3.0\*277
- PSS\*1.0\*94 (part of the CPRS v.27 installation sequence)
- PSS\*1.0\*112
- PSS\*1.0\*118
- XU\*8.0\*498
- YS\*5.01\*92

<span id="_Toc208213448" class="anchor"></span>Related <span id="related_patches" class="anchor"></span>Patches

To fully implement the new features in CPRS GUI v.27, the following related patches must be installed on your system:

- DG\*5.3\*703
- GMRC\*3.0\*55
- GMTS\*2.7\*85
- IB\*2.0\*339
- LR\*5.2\*364
- OR\*3.0\*281 (part of the installation sequence)
- PSJ\*5.0\*120
- PSJ\*5.0\*180
- PSO\*7.0\*292
- PSS\*1.0\*108
- PXRM\*2.0\*6
- RA\*5.0\*86
- RA\*5.0\*92
- YS\*5.01\*85

<span id="_Toc208213449" class="anchor"></span>Patches Distributed in the CPRS v.27 Related and Required Installation Bundle (CPRS_BUNDLE_GUI_27_REQ_REL.KID)

The CPRS development team bundled the following patches together to make it easier for sites to install them. The patches are either required for OR\*3.0\*243 installation or are related (meaning that they provide support from an ancillary package for CPRS changes). When you install the CPRS_BUNDLE_GUI_27_REQ_REL.KID host file, all of the patches in this bundle will be installed on your system.

- GMRA\*4.0\*38
- GMPL\*2.0\*35
- GMTS\*2.7\*80
- LR\*5.2\*365
- TIU\*1.0\*219
- WV\*1.0\*23

<span id="_Toc208213450" class="anchor"></span>Patches Distributed in the CPRS v.27 Primary Bundle (OR_PSJ_PSO_27.KID)

This host file, OR_PSJ_PSO_27.KID, contains the CPRS GUI v.27 patch (OR\*3.0\*243) and two required pharmacy patches. When you install this host file, the three patches listed below will be installed on your system.

- PSJ\*5.0\*134
- PSO\*7.0\*225
- OR\*3.0\*243

<span id="_Toc208213451" class="anchor"></span>Associated Patches to Be Installed after CPRS v.27

The following patches will be released separately from CPRS, but are part of the CPRS installation sequence.

- PSS\*1.0\*123 (part of the installation sequence)
- GMTS\*2.7\*84 (part of the installation sequence)
- OR\*3.0\*299 (part of the installation sequence)

<span id="_Toc208213452" class="anchor"></span>Internet Explorer Requirements

Internet Explorer v4.0 (IE4) or later is REQUIRED in order for CPRS GUI v27 to run. However, IE5.5 or later is required for PKI functionality.

<span id="_Toc208213453" class="anchor"></span>Installation Compliance Date

The compliance date for installation of OR\*3.0\*243 is 45 days. The extended compliance date is due to the complexity of CPRS GUI v27 and local training requirements.

The following patches have also extended their installation compliance dates to 45 days due to their interrelationship with CPRS GUI v27:

- GMRA\*4\*38
- GMPL\*2\*35
- GMTS\*2.7\*80
- GMTS\*2.7\*84
- LR\*5.2\*365
- OR\*3.0\*299
- PSJ\*5.0\*134
- PSO\*7.0\*225
- PSS\*1.0\*94
- PSS\*1.0\*123
- TIU\*1.0\*219
- WV\*1.0\*23

<span id="_Toc208213454" class="anchor"></span>OE/RR REPORTS file (#101.24)

Items in the OE/RR REPORTS file (#101.24) with entry numbers greater than 999 are reserved, and should not be used for local enhancements. If you have any local changes to items in this number range that you want to keep, move them to an internal number \<999. This patch will delete these entries numbers before proceeding with the install.

<span id="_Toc208213455" class="anchor"></span>Local Modifications to CPRS GUI v27 Source Code

CPRS GUI v27 is compiled with Delphi 2006. Modification of CPRS GUI v27 Source Code requires Delphi 2006.

CPRS GUI v27 was compiled with the VA 508 Accessibility Framework. Modification of CPRS GUI v27 source code requires the VA 508 Accessibility Framework. Documentation is accessible at the following web site.

<http://vaww.vista.med.va.gov/508WorkGroup/Delphi/home.asp>

<span id="_Toc208213456" class="anchor"></span>Software Retrieval

Download the necessary files from the FTP anonymous directories: download.vista.med.va.gov.

- CPRS_BUNDLE_GUI_27_REQ_REL.KID
- OR_PSJ_PSO_27.KID
- OR_30_243.ZIP

<span id="_Toc208213457" class="anchor"></span>CPRS GUI v27 Software Installation Instructions

This patch should be installed during non-peak hours to minimize disruption. No users should be accessing CPRS during the install as this prevents you from replacing CPRSChart.exe. Installation will take approximately 15 minutes or more, depending on the menu structure at your site.

Listed below are general installation instructions for installing the CPRS GUI v27 KIDS builds and other patches. For specific installation details, refer to the CPRS GUI v27 Software Installation Capture. Additionally, review the National Patch Module messages for each patch for patch-specific information.

1.  From the Kernel Installation and Distribution System (KIDS) Menu, select the Installation menu.
2.  Use Load a Distribution. You may need to prepend a directory name.
3.  If given the option to run any Environment Check Routine(s), answer "YES."
4.  From this menu, you may then elect to use the following options:
- Backup a Transport Global
- Compare Transport Global to Current System
- Verify Checksums in Transport Global
5.  When ready, select the Install Packages option.
6.  When prompted "Want KIDS to Rebuild Menu Trees Upon Completion of Install? Yes//", respond "YES."
7.  When prompted 'Want KIDS to INHIBIT LOGONs during the install? YES//', respond "YES."
8.  When prompted 'Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES//', respond YES. When prompted to select the options you would like to place out of order, enter the following:

OR OE/RR MENU CLINICIAN CPRS Clinician Menu

OR OE/RR MENU NURSE CPRS Nurse Menu

OR OE/RR MENU WARD CLERK CPRS Ward Clerk Menu

OR CPRS GUI CHART

9.  When prompted 'Delay Install (Minutes): (0-60): 0//; respond '0.'
10. Move the routines to other CPUs if appropriate.

<span id="_Toc208213458" class="anchor"></span>CPRS GUI v27 Software Installation Sequence

1.  Install OR\*3.0\*281 and run option ORCM RA SEARCH \[RADIOLOGY/IMAGING QUICK ORDER SEARCH\].

OR\*3.0\*281 installs a menu option ORCM RA SEARCH \[RADIOLOGY/IMAGING QUICK ORDER SEARCH\] that will assist sites in identifying Radiology Quick Orders that will need to be updated when sites install GUI v27.

The individual who runs the ORCM RA SEARCH menu option will receive a MailMan message that includes a report identifying Radiology Quick Orders. For additional information, see the patch description for OR\*3.0\*281.

> **NOTE:** You should review the report and plan the updates needed for quick orders BEFORE installing OR\*3\*243. The updates cannot be made until after the installation of OR\*3\*243, but you will need to make them as soon as possible.

2.  OR\*3.0\*243 (CPRS GUI v27) implements new functionality to collect/transmit a “Reason for Study” on Imaging/Radiology orders. Prior to CPRS GUI v.27, only the “Clinical History” was collected. Sites that have implemented a PACS system should evaluate their configuration to accommodate both a “Reason for Study” and “Clinical History.” 

Please alert your PACS administrator about this change to avoid problems with processing orders with a “Reason for Study.”

With the release of RA\*5.0\*75, REASON FOR STUDY is now required. REASON FOR STUDY is being passed in OBR 31.2.

CLINICAL HISTORY FOR EXAM is now optional. It is being passed in OBX 5.1.

3.  WARNING: Avoid installing CPRS GUI v27 software during the CMOP Transmission Process.  
    1.  Identify the scheduled times for the CMOP Transmission by accessing the following options:
- Setup Auto-transmission \[PSXR AUTO TRANSMIT\]
- Setup CS Auto-transmission \[PSXR AUTO TRANSMIT CS\]

  Note: These options allow the user to change the times of the two transmissions. Do not change the transmission times without first communicating with the CMOP.
  1.  Check to see if a CMOP transmission is currently in progress using FileMan:

Select OPTION:    INQUIRE TO FILE ENTRIES

 

OUTPUT FROM WHAT FILE: CMOP SYSTEM//

Select CMOP SYSTEM:    CMOP-NATIONAL     ACTIVE

ANOTHER ONE:

STANDARD CAPTIONED OUTPUT? Yes// N  (No)

FIRST PRINT FIELD: XMIT STATUS 

THEN PRINT FIELD:

Heading (S/C): CMOP SYSTEM LIST//

DEVICE:   VIRTUAL TELNET    Right Margin: 80//

CMOP SYSTEM LIST                               AUG  8,2008  11:26    PAGE 1

XMIT STATUS

--------------------------------------------------------------------------------

 

NO CURRENT TRANSMISSION

4.  WARNING: PSO\*7.0\*225 is a required patch that is included in OR_PSJ_PSO_27.KID.  It includes PSOLBL. If your site has implemented a Pharmacy Robot, it is likely that it will fail if PSOLBL has been modified locally. If your site has implemented a Pharmacy Robot, make a backup of PSOLBL before installing the CPRS GUI v27 software. After the install, you will need to compare the new PSOLBL to the backup and identify the differences implemented to support your Pharmacy Robot.
5.  Make sure all Nationally Released Required patches are installed.
6.  Make sure all Nationally Released Related patches are installed.
7.  CPRS v27 will be unable to run without the updated version of the BORLNDMM.DLL.

The updated BORLNDMM.DLL was initially distributed with OR\*3.0\*252, *Correct CPRSUpdate.EXE Defects.* OR\*3.0\*252 instructed sites to appropriately place the updated BORLNDMM.DLL.

If sites use CPRSUpdate to update versions of CPRS, place the new BORLNDMM.DLL in the GOLD directory, and it will be updated automatically the next time CPRS is run on a workstation that uses CPRSUpdate.

If your site does not use CPRSUpdate to update versions of CPRS, or you have workstations that are updated by means other than CPRSUpdate, the BORLNDMM.DLL will need to be placed in the workstation or network server's CPRS directory, or in a location that is reachable via the workstation's PATH variable, replacing any previous copies that are installed.

Make sure that:

- The <u>updated</u> BORLNDMM.DLL is placed in your GOLD directory, -or-
- NO BORLNDMM.DLL is in your GOLD directory.

CPRS GUI v27 Users will experience the following error if the BORLNDMM.DLL is not updated:

![](or-3-243-and-associated-patches-installation-guide-cprs-gui-27/002.png)

8.  Install PSS\*1.0\*94.

Please refer to the CPRS GUI v27 Installation Capture for installation details.

9.  Install Required and Related Patches for OR\*3.0\*243:  CPRS_BUNDLE_GUI_27_REQ_REL.KID

Please refer to the CPRS GUI v27 Installation Capture for installation details.

10. Install OR\*3.0\*243 (CPRS GUI v27), PSJ\*5.0\*134 and PSO\*7\*225:  OR_PSJ_PSO_27.KID

Please refer to the CPRS GUI v27 Installation Capture for installation details.

11. Install PSS\*1.0\*123.

Please refer to the CPRS GUI v27 Installation Capture for installation details.

12. Install GMTS\*2.7\*84.

Please refer to the CPRS GUI v27 Installation Capture for installation details.

13. Install OR\*3.0\*299.
- This patch creates a post install that repairs truncated patient instructions in the ORDERS file (#100). When a discrepancy is found between the patient instructions in the PRESCRIPTION file (#52) and the ORDERS file (#100), the text from the PRESCRIPTION file (#52) will be used to set the patient instructions into the ORDERS file (#100).
- The post install also creates the Modified Truncated Patient Instruction search report that shows what was done. The data is similar to the example below:

Patient/Division SSN Item/Dispense Status/RX# Stop/OIEN

CPRSOUTPATIENT,ONE 4695 ASPIRIN TAB DISCONTINUED 02/06/2008

DAYTON ASPIRIN 325MG BUFFER 2666542 12607212

14. Distribute CPRSCHART.EXE, CPRS.HLP, CPRS.CNT located in OR_30_243.ZIP.

These three files should be distributed to the same directory as the borlndmm.dll. Usually, these files are located in the CPRS directory.

15. Place the User and Technical Manual files in a location that can be accessed by CPRS users.
16. After CPRS v27 is installed into production, do the following:

> a\) Review the New Parameters exported with CPRS GUI v27 (see listing below). You will need to set the values for all new parameters.

> b\) Correct the Radiology quick orders you have identified from the search routine from the \[ORCM RA SEARCH\] option.

> c\) If your site has implemented the new Mental Health Assistant (PXRM\*2\*6 and YS\*5.01\*85) and OR USE MH DLL parameter is set to YES, make sure the following have been done:

- YS_MHA.dll and MHA3_DLL_Scoring.dll must be placed in the Common Files folder (same place as Vitals dll).
- YS Broker1 must be assigned as a secondary menu option for users that:
- Process MH tests in the new MHA3 executable
- Have access to reminder dialogs in CPRS
- Rebuild your Menus.

> d\) Review the MailMan message generated when you ran the following option. This option was implemented with OR\*3.0\*281:

ORCM RA SEARCH RADIOLOGY/IMAGING QUICK ORDER

> e\) Review the Quick Orders Mail Man message generated when you installed OR\*3.0\*243 or generate a new message by running the following option:

MR Medication Quick Order Report \[OR MEDICATION QO CHECKER\] which is located on ORDER MENU MANAGEMENT \[ORCM MGM\]

> f\) Review the ADMINISTRATION SCHEDULES for your site and make sure the TYPE OF SCHEDULE field (51.1,5) is set to “P” for all PRN schedules. Otherwise, users will think they are ordering a PRN order; but CPRS and Pharmacy will not treat the order as a PRN order.

PRN schedules may be updated using the following option under the PSS MGR menu:

> PSS SCHEDULE EDIT       Standard Schedule Edit

> g\) <span id="Evalute_IV_Additives_and_solutions" class="anchor"></span>Evaluate IV Additives and IV Solution.

Implementation of three new fields, IV Type, Route and Schedule, to the Infusion Order Dialog in CPRS GUI v.27 was done to address several PSIs, including: 

- PSI-06-014: How epidural routes appear on the IV tab in BCMA and appear in CPRS under IV fluids is contributing to medication errors.
- PSI-06-045: The CPRS IV dialogue lacks a field for the provider to enter the route of infusion.
- PSI-07-036: Epidural QO with default of IV route may result in epidural given via IV port.

Implementing these changes requires sites to evaluate their IV Additives and IV Solutions and to set the USED IN IV FLUID ORDER ENTRY fields to YES in the IV ADDITIVES file (#52.6) and IV SOLUTIONS file (#52.7); otherwise, CPRS users will NOT be able to change, copy or renew IV orders.

Update these two fields using the following options:

To update the IV Additives file:

> Select OPTION NAME: PSSJI DRUG

>      1   PSSJI DRUG       ADditives File

>      2   PSSJI DRUG INQUIRY       Drug Inquiry (IV)

> CHOOSE 1-2: 1  PSSJI DRUG     ADditives File

> ADditives File

> Select IV ADDITIVES PRINT NAME: DEXDEXAMETHASONE 

>                NATL FORM (NDC)

> PRINT NAME: DEXAMETHASONE//

> GENERIC DRUG: DEXAMETHASONE 4MG/ML 1ML INJ//

> USED IN IV FLUID ORDER ENTRY: YES//  This prompt should be set to YESTo update the IV Solutions file:

> Select OPTION NAME: PSSJI SOLN       PRimary Solution File (IV)

> PRimary Solution File (IV)

> Select IV SOLUTIONS PRINT NAME: DEX DEXTROSE 10%          500 ML 

>                NATL FORM; 500ML SOLN IN 1000ML BAG

> PRINT NAME: DEXTROSE 10%//

> PRINT NAME {2}:

> GENERIC DRUG: DEXTROSE 70% 500ML IN 1000ML BAG//

> VOLUME: 500 ML//

> Select ELECTROLYTES:

> Select SYNONYM: D10W//

> DRUG INFORMATION:

>   No existing text

>   Edit? NO//

> AVERAGE DRUG COST: 7.45//

> INACTIVATION DATE: JUN 21,1989//

> USED IN IV FLUID ORDER ENTRY: NO//  This prompt should be set to YES

> h\) Implement CPRS GUI v27 Functionality to Assist Visually Impaired Users. Place the JAWS Configuration Files as noted below. These files are included in OR_30_243.ZIP. Please see Appendix A of the User Manual for additional information such as keyboard short cuts.

> **NOTE:** This is optional and should be done for those users with visual disabilities.

<span id="_Toc208213459" class="anchor"></span>JAWS Configuration Files

JAWS is a screen reader application that enables a computer to verbally describe the controls and content of computer applications. For example, in CPRS, when a user changes tabs, JAWS will speak the name of the tab, such as “Orders”, enabling the visually-challenged user to navigate CPRS and complete necessary tasks.

Developers have created specialized scripts and CPRS components that enable JAWS to work more effectively with CPRS. As part of the CPRS GUI v.27 (OR\*3.0\*243) release a zip file (CPRS27_JAWS_SUPPORT_FILES.ZIP) including the JAWS scripts and supporting files is being distributed.

The improvements work only with JAWS 7.1 or later. However, JAWS 8.0.2173 or later is best because it fixes a bug that caused CPRS to crash when reading progress notes with JAWS. This fix is not in earlier versions of JAWS 8.0.

Usually it is best for JAWS users stay up to date with the latest releases of the product.

- JAWS.SR - DLL used for communication between JAWS and CPRS
- JAWSUPDATE - Used to update JAWS 7.1 to work with the component
- VA508APP.jcf - JAWS configuration file
- VA508APP.JSS - JAWS script file
- VA508JAWS.jss - JAWS script file
- VA508JAWSDispatcher – Application used for communication between JAWS and multiple applications using the JAWS.SR DLL
- VA508APP.jkm - JAWS keyboard mapping file
- VA508JAWS.jsd - Documentation companion file to the VA508JAWS.jss script file
- Vcredist_x86.exe is the Microsoft Visual C++ 2005 Redistributable.  It’s called by JAWSUpdate.exe.

To use the accessibility features, a user must copy these files into Program Files\Vista\Common Files, which is normally found on the workstation at C:\Program Files\Vista\Common Files. If the workstation is running JAWS 8.0.2173 or higher, nothing further is required.

If the workstation is running an earlier version of JAWS 8.0, or JAWS 7.1.500, the user must go to Program Files\Vista\Common Files and run JAWSUpdate.exe. JAWSUpdate installs a COM object for compatibility with these versions.

> **NOTE:** You must have administrative rights on the machine to run JAWSUpdate.exe. 

If the workstation is running a version of JAWS that is older than v 7.1.500, the new accessibility features in CPRS will not function. CPRS will function as it did without these changes, but the following error message will display:

![](or-3-243-and-associated-patches-installation-guide-cprs-gui-27/003.png)

<span id="_Toc208213460" class="anchor"></span>New Parameters Introduced with CPRS GUI v27

- OR ADMIN TIME HELP TEXT-- CPRS ADMINISTRATION TIMES HELP TEXT
- System level parameter
- This parameter defines the text message to display when the user clicks on the administration times on the complex dosage tab.
- This parameter determines the information that is displayed in the *Administration Time Information* pop-up or Hover Hint  that is displayed to the user.  The pop-up includes the administration times for the dose and the help text defined in this parameter.
- Access via:

> IR CPRS Configuration (IRM)

> XX General Parameter Tools

> EP Edit Parameter Values

- OR CLOZ INPT MSG--DISPLAY TEXT: MSG TO DISPLAY ON INPT ORD OF CLOZAPINE
- System level Parameter
- This parameter defines the text that advises users about the site’s policy regarding management of inpatient Clozapine orders.
- Clozapine is usually prescribed in an outpatient setting, but it can be ordered for inpatients. However, the special appropriateness order checks that occur when finishing in the backdoor Outpatient Pharmacy setting do not occur in the finishing process in backdoor Inpatient Pharmacy. In addition, backdoor Outpatient Pharmacy sends the clozapine information to the National Clozapine Coordinating Center (NCCC) database. Some sites have directed the ordering provider to place a corresponding outpatient order when placing an inpatient clozapine order. The sites that have this policy can use the new OR CLOZ INPT MSG parameter to help reinforce this policy to the ordering providers.
- Access via:

> PE CPRS Configuration (Clin Coord)

> GP GUI Parameters

> CLOZ GUI Edit Inpatient Clozapine Message

- OR DC REASON LIST—DISPLAY TEXT: DC REASON SEQUENCE
- System level parameter
- This parameter sets the display sequence of the DC Reason list
- This parameter determines the sequence sites want the order DC reasons to appear. Sites do not need to set a sequence for every DC Reasons. For example if a site wants to set the "Requesting Physician Cancelled" DC Reasons to the top of the list. Sites will set a value of 1 for that entry and CPRS will display the rest of the DC Reasons after the "Requesting Physician Cancelled" DC reason.
- Access via:

> IR CPRS Configuration (IRM)

> XX General Parameter Tools

> EP Edit Parameter Values

- OR FLAGGED ORD REASONS—DISPLAY TEXT: LIST OF GENERIC FLAG REASONS
- System level parameter
- This parameter allows sites to define standard generic reason's for flagging orders that the users can choose in the CPRS GUI.
- Access via:

> IR CPRS Configuration (IRM)

> XX General Parameter Tools

> EP Edit Parameter Values

- OR LAPSE ORDERS—DISPLAY TEXT: LAPSE UNSIGNED/UNRELEASED ORDER BY GROUP
- Division, System level parameter
- This parameter sets the number of days to keep unsigned/unreleased orders before lapsing them.
- The purpose of this parameter is to store the number of days that old orders will be lapsed.  This parameter is multi valued with an instance term of DISPLAY GROUPS.  Thus the way it works is that you can set "Display Group A" so that old orders from this display group will lapse in 10 days for instance.  Then you could have "Display Group B" set so that those orders would lapse when they are 20 days old. Display groups not individually set by this parameter are affected by the OR LAPSE ORDERS DFLT parameter.
- By lapsing, it is meant that the order is placed in a LAPSED status
- Access via:

> IR CPRS Configuration (IRM)

> XX General Parameter Tools

> EP Edit Parameter Values

- OR LAPSE ORDERS DFLT—DISPLAY TEXT: LAPSE UNSIGNED/UNRELEASED ORDER DEFAULT
- Division, system level parameter
- This parameter sets the default for the number of days that old orders will be lapsed when those orders are from a DISPLAY GROUP that does not have parameter OR LAPSE ORDERS set
- The purpose of this parameter is to store the number of days that old orders will be lapsed when those orders are from a DISPLAY GROUP that does not have parameter OR LAPSE ORDERS set.  The default value that is set in this parameter will affect all orders that do not have a specific DISPLAY GROUP value.  Thus if both "Display Group A" and "Display Group B" have parameter OR LAPSE ORDERS set for them but "Display Group C" does not, then orders from "Display Group C" will get lapsed in the number of days specified in OR LAPSE ORDERS DFLT.
- Access via:

> IR CPRS Configuration (IRM)

> XX General Parameter Tools

> EP Edit Parameter Values

- OR USE MH DLL—DISPLAY TEXT: Use MH DLL?
- System level parameter
- This parameter is a toggle that allows/disallows use of the Mental Health DLL in Clinical Reminder dialogs
- The purpose of this parameter is to allow sites to allow/disallow use of the Mental Health DLL when CPRS GUI v27 in installed. It is exported with a value of YES. If your site has not implemented PXRM\*2\*6 and YS\*5.01\*85, you should change this setting to NO.
- Access via:

> IR CPRS Configuration (IRM)

> XX General Parameter Tools

> EP Edit Parameter Values

- ORWLR LC CHANGED TO WC—DISPLAY TEXT:  MESSAGE FOR LC CHANGED TO WC
- Division, system, location, service, package level parameter
- This parameter defines the text that provides instructions regarding specimen collection for orders that have been changed from lab collect to ward collect.
- This will allow local customization of the message displayed to users when lab collect orders with continuous schedules are automatically changed to ward collect when lab collection is not available.  Parameter allows 80 characters of text.  The 80-character limit is necessary because this text will not wrap.  The PACKAGE value exported with the parameter is the existing "Please contact the ward staff to insure the specimen is collected." 
- Access via:

> IR CPRS Configuration (IRM)

> XX General Parameter Tools

> EP Edit Parameter Values

- OR RA RFS CARRY ON—DISPLAY TEXT: OR RA RFS CARRY ON
- System level parameter
- This parameter determines if CPRS will carry on the text entered in the Reason for Study field of the Radiology (Imaging) order dialog to subsequent orders in the same ordering session.
- By carry on means that when one order is entered the value entered in the Reason for Study field will be held and used again in subsequent Radiology orders.
- Access via:

> IR CPRS Configuration (IRM)

> XX General Parameter Tools

> EP Edit Parameter Values

<span id="_Toc208213461" class="anchor"></span>CPRS / VBECS Parameters

These parameters will not be evaluated by CPRS until VBECS is installed.

- OR VBECS COMPONENT ORDER –DISPLAY TEXT: List of Blood Components
- System, Division, Package, User level parameter
- This parameter allows a sequence to be assigned to Blood Components selectable from VBECS.
- Access via:

> IR CPRS Configuration (IRM)

> XX General Parameter Tools

> EP Edit Parameter Values

- OR VBECS MODIFIERS—DISPLAY TEXT: List of Component Modifiers
- System, Package level parameter
- This parameter allows local configuration of the blood component modifiers.
- Access via:

> IR CPRS Configuration (IRM)

> XX General Parameter Tools

> EP Edit Parameter Values

- OR VBECS REASON FOR REQUEST—DISPLAY TEXT: List of Reasons for Request
- System, Package level parameter
- This parameter allows local configuration of the Reasons for Request.
- Access via:

> IR CPRS Configuration (IRM)

> XX General Parameter Tools

> EP Edit Parameter Values

- OR VBECS SUPPRESS NURS ADMIN—DISPLAY TEXT: Suppress Nursing Admin Prompt
- System, Division, Package level parameter
- This parameter disables the prompt/pop-up that tells the user they must enter a Nursing Administration Order manually after entering a VBECS Blood order. Disabling this feature is usually done when a Nursing Administration order has been created and added to a VBECS order set.
- Access via:

> IR CPRS Configuration (IRM)

> XX General Parameter Tools

> EP Edit Parameter Values

- ORWDXVB VBECS TNS CHECK—DISPLAY TEXT: DAYS TO CHECK FOR TYPE & SCREEN
- Division, system level parameter
- This parameter is relevant for sites that have installed VBECS and OR\*3.0\*212.
- This parameter is used in the VBECS Order Dialog to check for recent orders for a Type & Screen order. The default is 3 days, but a site can override this number by setting this parameter to something different. If it doesn’t get set, the default of 3 days is used, which is standard in most circumstances.  It would be up to the Blood Bank to determine otherwise.
- Access via:

> IR CPRS Configuration (IRM)

> XX General Parameter Tools

> EP Edit Parameter Values

<span id="_Toc208213462" class="anchor"></span>CPRS GUI v27 Display Change for Existing Parameter – OR UNSIGNED ORDERS ON EXIT

- The OR UNSIGNED ORDERS ON EXIT parameter allows sites to control how orders are displayed on the Review/Sign Changes dialog. The parameter OR UNSIGNED ORDERS ON EXIT may be set to include NEW ORDERS ONLY, MY UNSIGNED ORDERS, or ALL UNSIGNED ORDERS. If sites include ALL UNSIGNED ORDERS, CPRS could display orders that were quite old, but had never been signed and the provider might sign orders that should not be signed.

To address this issue, the CPRS Clinical workgroup and the Patient Safety Workgroup, made some recommendations. If sites use the ALL UNSIGNED ORDERS options, the orders on the Review/Sign Changes dialog will be separated into three sections:

- My Unsigned Orders - This Session: This list contains all orders written by the current user in the current session.
- My Unsigned Orders - Previous Sessions: This list contains all orders written in previous sessions by the current user.
- Others’ Unsigned Orders - All Sessions: This list contains all orders written by other users.

This should enable providers to distinguish which orders belong to them and which do not.

Additionally, when the user discontinues an unsigned/unreleased order, if the order was placed in the current ordering session the order is DELETED.  If the order was placed in a different ordering session, then the order is CANCELLED. Deleted orders do not appear in the chart because other users never saw them, but it is possible that other clinicians saw the order placed in a different session so that information is retained in the chart and the order is given a CANCELLED status.

> **NOTE:** Note on Ordering Session—With CPRS 27, how CPRS behaves when a user discontinues (DC) an order is affected by the ordering session. If the order is Dc’d in the same ordering session in which it was created, then it is deleted and no longer remains in the database. If the order is Dc’d in a different ordering session, then the order is given a status of CANCELLED and is still in the database in file 100. Special attention should be given to when an ordering session actually ends.  It ends in one of the following 4 ways:

- The user switches patients
- The user closes CPRS
- The user performs a Review/Sign changes Action
- The user performs a Refresh Patient Information

<span id="_Toc208213463" class="anchor"></span>CPRS GUI v27 Changed Definition of Existing Parameter – ORWOR WRITE ORDERS LIST

- This parameter is used to list the order dialog names that should appear in the Write Orders list box of the CPRS GUI. This is the list of dialogs that should be used in the inpatient setting.

Since entry of an allergy was changed to be on the cover sheet, the GMRAOR ALLERGY ENTER/EDIT order dialog cannot be added to parameter ORWOR WRITE ORDERS LIST. The menus it was on work, but CPRS would not accept it on the write orders section nor on any new menus.

Resolution: Changed the definition of parameter ORWOR WRITE ORDERS LIST to allow entries of type ACTION from file 101.41. This was already allowed on order menus.

<span id="_Toc208213464" class="anchor"></span>CPRS GUI v27 Meds Tab Views Regulated by Existing Parameter—ORCH CONTEXT MEDS

- This parameter is used to specify a date range (in days) for Meds tab displays that dictate the length of time orders are displayed. The parameter provides strings of delimited ("; ) pieces, the first two of which are always a relative date range. Users can determine the date range of medications that display on the Medications tab through the Tools \| Options pull-down menu in CPRS.

This parameter functions independently of display settings for the Orders tab. If you need to alter the display range for expired medication orders on the Orders tab, please adjust the ORWOR EXPIRED ORDERS parameter accordingly.

- This parameter should be reviewed at both the system level and user level. If the system level parameter is set to “Value: ;T+1//” users will not see any EXPIRED Meds.  Listed below is an example setting ORCH CONTEXT MEDS to accommodate display of expired orders.

ORCH CONTEXT MEDS   Meds Tab Context

 

ORCH CONTEXT MEDS may be set for the following:

 

     1   User          USR    \[choose from NEW PERSON\]

     5   System        SYS    \[SITE NAME.MED.VA.GOV\]

 

Enter selection: 5  System   SITE NAME.MED.VA.GOV

 

-------- Setting ORCH CONTEXT MEDS  for System: SITE NAME.MED.VA.GOV --------

Value: T-120;T+1//

There isn’t a <u>separate parameter</u> for Outpatient Meds vs Inpatient Meds.  Outpatient medication reviewers need to go back 120 Days since there are typically a large number of Days Supply set at 90 and to capture this group the parameter will need to be set to go back in time.

On the other hand, users typically don’t need to see expired orders that far back in time for Inpatient Orders. Since there is only one parameter to manage both types of orders, the Inpatient Users may complain about seeing a bunch of Expired, Discontinued, and Dc/Edit Orders that they haven’t see in the past.

<span id="_Toc208213465" class="anchor"></span>New Graphing Resource Device

CPRS v.27 has improved performance on graphing patient data by using a “cache”, gathering the patient’s data in advance of using graphing functions. This avoids always fetching the data.

To ensure that there is not excessive system processing for data extraction, developers added a new resource device (ORWG GRAPHING RESOURCE) in CPRS v27. It is initially set to allow only three processes to be running at one time. The Resource Slots field can be changed to allow more or fewer processes to occur.

For additional information, please see the *CPRS Technical Manual*.

<span id="_Toc208213466" class="anchor"></span>CPRS GUI v27 Software

Patches Not Included in an OR\*3.0\*243 Bundle

<table>
<colgroup>
<col style="width: 37%" />
<col style="width: 62%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>PATCH</strong></th>
<th><strong>SUPPORTED FUNCTIONALITY</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>GMTS*2.7*84</td>
<td><p>Adds Reason for Study to OE/RR</p>
<p>Radiology Report and Health Summary</p></td>
</tr>
<tr class="even">
<td>OR*3.0*281</td>
<td><p>Identifies Radiology/Imaging Quick</p>
<p>Orders that may need editing</p></td>
</tr>
<tr class="odd">
<td>OR*3.0*299</td>
<td><p>Identifies and Repairs Truncated Patient</p>
<p>Instructions in the ORDERS file (100)</p></td>
</tr>
<tr class="even">
<td>PSS*1.0*94</td>
<td><p>Changes to input template</p>
<p>PSSJ SCHEDULE EDIT</p></td>
</tr>
<tr class="odd">
<td>PSS*1.0*123</td>
<td>Supports Millimole Functionality</td>
</tr>
</tbody>
</table>

<span id="_Toc208213467" class="anchor"></span>OR_PSJ_PSO_27.KID-- PRIMARY BUILD

<table>
<colgroup>
<col style="width: 37%" />
<col style="width: 62%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>PATCH</strong></th>
<th><strong>SUPPORTED FUNCTIONALITY</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>OR*3.0*243</td>
<td>Primary OR patch for CPRS GUI v27</td>
</tr>
<tr class="even">
<td>PSJ*5.0*134</td>
<td><p>Primary Inpatient Medications patch</p>
<p>supporting medication dialog changes</p></td>
</tr>
<tr class="odd">
<td>PSO*7.0*225</td>
<td><p>Primary Outpatient Pharmacy patch</p>
<p>supporting medication dialog changes</p></td>
</tr>
</tbody>
</table>

<span id="_Toc208213468" class="anchor"></span>CPRS_BUNDLE_GUI_27_REQ_REL.KID

<table>
<colgroup>
<col style="width: 37%" />
<col style="width: 62%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>PATCH</strong></td>
<td><strong>SUPPORTED FUNCTIONALITY</strong></td>
</tr>
<tr class="even">
<td>GMRA*4*38</td>
<td><p>Add “Entered in Error” Allergy Progress</p>
<p>Note to CPRS signature list</p></td>
</tr>
<tr class="odd">
<td>GMPL*2*35</td>
<td><p>SHAD—Environmental Indicator</p>
<p>(Shipboard Hazard And Defense)</p></td>
</tr>
<tr class="even">
<td>GMTS*2.7*80</td>
<td>Pharmacy Encapsulation</td>
</tr>
<tr class="odd">
<td>LR*5.2*365</td>
<td><p>Support for PSI-05-027, PSI-05-001</p>
<p>Reformat Lab Reports</p></td>
</tr>
<tr class="even">
<td>TIU*1.0*219</td>
<td><p>Graphing and Discharge Summary</p>
<p>Attending Selection List Changes</p></td>
</tr>
<tr class="odd">
<td>WV*1.0*23</td>
<td><p>Support for PSI-05-001, PSI-06-068,</p>
<p>PSI-06-134, PSI-07-014 and</p>
<p>PSI-07-031</p></td>
</tr>
</tbody>
</table>

<span id="_Toc208213469" class="anchor"></span>OR_30_243.ZIP

The JAWS files are included in this zip file. JAWS files must be installed when the JAWS screen reader is used.

All the files in the JAWS Support Files zip file (CPRS27_JAWS_SUPPORT_FILES.ZIP) should be copied into the Program Files\Vista\Common Files directory. One of these files, JAWSUPDATE.exe, must be run in order to enable the JAWS code.  This will install a Freedom Scientific COM object that is compatible with JAWS 7.1 or greater.  You must have administrator rights on your machine when you run JAWSUPDATE.  After running JAWSUPDATE, the user will no longer require administrator rights.  

See table below for files included in the CPRS_JAWS_SUPPORT_FILES.ZIP

<table>
<colgroup>
<col style="width: 39%" />
<col style="width: 22%" />
<col style="width: 0%" />
<col style="width: 37%" />
<col style="width: 0%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>FILE</strong></td>
<td><strong>VERSION</strong></td>
<td colspan="2"><strong>CONTENTS</strong></td>
<td></td>
</tr>
<tr class="even">
<td>Borlndmm.dll</td>
<td>10.0.2288.42451</td>
<td colspan="2">New Borland DLL</td>
<td></td>
</tr>
<tr class="odd">
<td>CPRSChart.exe</td>
<td>1.0.27.77</td>
<td colspan="2">CPRS GUI v27.77</td>
<td></td>
</tr>
<tr class="even">
<td>CPRSGUIUM.doc</td>
<td>N/A</td>
<td colspan="2">CPRS GUI User Manual</td>
<td></td>
</tr>
<tr class="odd">
<td>CPRSLMTM.doc</td>
<td>N/A</td>
<td colspan="2"><p>CPRS ListManager</p>
<p>Technical Manual</p></td>
<td></td>
</tr>
<tr class="even">
<td>OR_30_243RN.doc</td>
<td>N/A</td>
<td colspan="2">CPRS v27 Release Notes</td>
<td></td>
</tr>
<tr class="odd">
<td>JAWS.SR</td>
<td colspan="2">1.10</td>
<td colspan="2"><p>DLL used for communication</p>
<p>between JAWS and CPRS</p></td>
</tr>
<tr class="even">
<td>JAWSUpdate.exe</td>
<td colspan="2">N/A</td>
<td><p>Used to update JAWS 7.1 to</p>
<p>Work with the component</p></td>
<td></td>
</tr>
<tr class="odd">
<td>VA508APP.jcf</td>
<td colspan="2">N/A</td>
<td>JAWS configuration file</td>
<td></td>
</tr>
<tr class="even">
<td>VA508APP.jss</td>
<td colspan="2">N/A</td>
<td>JAWS script file</td>
<td></td>
</tr>
<tr class="odd">
<td>VA508JAWS.jss</td>
<td colspan="2">1137</td>
<td>JAWS script file</td>
<td></td>
</tr>
<tr class="even">
<td>VA508JAWSDispatcher.exe</td>
<td>N/A</td>
<td colspan="2"><p>Application used for</p>
<p>communication between JAWS</p>
<p>and multiple applications</p>
<p>using the JAWS.SR DLL</p></td>
<td></td>
</tr>
<tr class="odd">
<td>VA508APP.jkm</td>
<td colspan="2">N/A</td>
<td>JAWS keyboard mapping file</td>
<td></td>
</tr>
<tr class="even">
<td>VA508JAWS.jsd</td>
<td colspan="2">N/A</td>
<td><p>Documentation companion file</p>
<p>to the VA508JAWS.jss</p>
<p>script file</p></td>
<td></td>
</tr>
<tr class="odd">
<td>vcredist_x86.exe</td>
<td colspan="2">2.0.50727.42</td>
<td><p>Vcredist_x86.exe is the</p>
<p>Microsoft Visual C++ 2005</p>
<p>Redistributable.  It’s called</p>
<p>by JAWSUpdate.exe.</p></td>
<td></td>
</tr>
</tbody>
</table>

<span id="_Toc208213470" class="anchor"></span>CPRS GUI v27 Software Installation Capture

> Select OPTION NAME: XPD MAIN Kernel Installation & Distribution System

> Edits and Distribution ...

> Utilities ...

> Installation ...

> Patch Monitor Main Menu ...

> Select Kernel Installation & Distribution System Option: Installation

> OR\*3\*281 Installation Capture

> 1 Load a Distribution

> 2 Verify Checksums in Transport Global

> 3 Print Transport Global

> 4 Compare Transport Global to Current System

> 5 Backup a Transport Global

> 6 Install Package(s)

> Restart Install of Package(s)

> Unload a Distribution

> Select Installation Option: 6 Install Package(s)

> Select INSTALL NAME: OR,281 OR\*3.0\*281 Loaded from Distribution 8/6/08@11:

> 56:46

> =\> OR\*3\*281

> This Distribution was loaded on Aug 06, 2008@11:56:46 with header of

> OR\*3\*281

> It consisted of the following Install(s):

> OR\*3.0\*281

> Checking Install for Package OR\*3.0\*281

> Install Questions for OR\*3.0\*281

> Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO//

> Want KIDS to INHIBIT LOGONs during the install? NO//

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

> Enter the Device you want to print the Install messages.

> You can queue the install by enter a 'Q' at the device prompt.

> Enter a '^' to abort the install.

> Install Started for OR\*3.0\*281:

> Aug 06, 2008@11:57:31

> Build Distribution Date: Jul 29, 2008

> Installing Routines:

> Aug 06, 2008@11:57:32

> Installing PACKAGE COMPONENTS:

> Installing OPTION:

> Aug 06, 2008@11:57:32

> Updating Routine file...

> Updating KIDS files...

> OR\*3.0\*281 Installed.

> Aug 06, 2008@11:57:32

> Install Completed

> PSS\*1\*94 Installation Capture

> 1 Load a Distribution

> 2 Verify Checksums in Transport Global

> 3 Print Transport Global

> 4 Compare Transport Global to Current System

> 5 Backup a Transport Global

> 6 Install Package(s)

> Restart Install of Package(s)

> Unload a Distribution

> Select Installation Option: 6 Install Package(s)

> Select INSTALL NAME: PSS,94 PSS\*1.0\*94 Loaded from Distribution 8/6/08@12:

> 00:15

> =\> PSS\*1\*94

> This Distribution was loaded on Aug 06, 2008@12:00:15 with header of

> PSS\*1\*94

> It consisted of the following Install(s):

> PSS\*1.0\*94

> Checking Install for Package PSS\*1.0\*94

> Install Questions for PSS\*1.0\*94

> Want KIDS to INHIBIT LOGONs during the install? NO//

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

> Enter the Device you want to print the Install messages.

> You can queue the install by enter a 'Q' at the device prompt.

> Enter a '^' to abort the install.

> Install Started for PSS\*1.0\*94 :

> Aug 06, 2008@12:00:34

> Build Distribution Date: Mar 03, 2008

> Installing Routines:

> Aug 06, 2008@12:00:35

> Installing PACKAGE COMPONENTS:

> Installing INPUT TEMPLATE:

> Aug 06, 2008@12:00:35

> Updating Routine file...

> Updating KIDS files...

> PSS\*1.0\*94 Installed.

> Aug 06, 2008@12:00:35

> Install Completed

> CPRS_BUNDLE_GUI_27_REQ_REL.KID Installation Capture

> 1 Load a Distribution

> 2 Verify Checksums in Transport Global

> 3 Print Transport Global

> 4 Compare Transport Global to Current System

> 5 Backup a Transport Global

> 6 Install Package(s)

> Restart Install of Package(s)

> Unload a Distribution

> Select Installation Option: 1 Load a Distribution

> Enter a Host File: CPRS_BUNDLE_GUI_27_REQ_REL.KID

> KIDS Distribution saved on Jun 18, 2008@09:19:26

> Comment: CPRS27 REQUIRED BUNDLE - RELEASED

> This Distribution contains Transport Globals for the following Package(s):

> CPRS BUNDLE GUI 27.0

> WV\*1.0\*23

> TIU\*1.0\*219

> GMPL\*2.0\*35

> GMRA\*4.0\*38

> GMTS\*2.7\*80

> LR\*5.2\*365

> Distribution OK!

> Want to Continue with Load? YES//

> Loading Distribution...

> CPRS BUNDLE GUI 27.0

> WV\*1.0\*23

> TIU\*1.0\*219

> GMPL\*2.0\*35

> GMRA\*4.0\*38

> GMTS\*2.7\*80

> Build LR\*5.2\*365 has an Environmental Check Routine

> Want to RUN the Environment Check Routine? YES//

> LR\*5.2\*365

> Will first run the Environment Check Routine, LR365

> Sending transport global loaded alert to mail group G.LMI

> Use INSTALL NAME: CPRS BUNDLE GUI 27.0 to install this Distribution.

> 1 Load a Distribution

> 2 Verify Checksums in Transport Global

> 3 Print Transport Global

> 4 Compare Transport Global to Current System

> 5 Backup a Transport Global

> 6 Install Package(s)

> Restart Install of Package(s)

> Unload a Distribution

> Select Installation Option: 6 Install Package(s)

> Select INSTALL NAME: CPRS BUNDLE GUI 27.0 Loaded from Distribution 8/6/08

> @12:26:22

> =\> CPRS27 REQUIRED BUNDLE - RELEASED ;Created on Jun 18, 2008@09:19:26

> This Distribution was loaded on Aug 06, 2008@12:26:22 with header of

> CPRS27 REQUIRED BUNDLE - RELEASED ;Created on Jun 18, 2008@09:19:26

> It consisted of the following Install(s):

> CPRS BUNDLE GUI 27.0 WV\*1.0\*23 TIU\*1.0\*219 GMPL\*2.0\*35

> GMRA\*4.0\*38 GMTS\*2.7\*80 LR\*5.2\*365

> Checking Install for Package CPRS BUNDLE GUI 27.0

> Install Questions for CPRS BUNDLE GUI 27.0

> Checking Install for Package WV\*1.0\*23

> Install Questions for WV\*1.0\*23

> Checking Install for Package TIU\*1.0\*219

> Install Questions for TIU\*1.0\*219

> Incoming Files:

> 8925 TIU DOCUMENT (Partial Definition)

> Note: You already have the 'TIU DOCUMENT' File.

> 8925.95 TIU DOCUMENT PARAMETERS (Partial Definition)

> Note: You already have the 'TIU DOCUMENT PARAMETERS' File.

> Checking Install for Package GMPL\*2.0\*35

> Install Questions for GMPL\*2.0\*35

> Incoming Files:

> 9000011 PROBLEM (Partial Definition)

> Note: You already have the 'PROBLEM' File.

> Checking Install for Package GMRA\*4.0\*38

> Install Questions for GMRA\*4.0\*38

> Checking Install for Package GMTS\*2.7\*80

> Install Questions for GMTS\*2.7\*80

> Checking Install for Package LR\*5.2\*365

> Will first run the Environment Check Routine, LR365

> --- Environment Check is Ok ---

> Install Questions for LR\*5.2\*365

> Want KIDS to Rebuild Menu Trees Upon Completion of Install? YES//

> Want KIDS to INHIBIT LOGONs during the install? NO//

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

> Enter the Device you want to print the Install messages.

> You can queue the install by enter a 'Q' at the device prompt.

> Enter a '^' to abort the install.

> Install Started for CPRS BUNDLE GUI 27.0 :

> Aug 06, 2008@12:27:39

> Build Distribution Date: Jun 18, 2008

> Installing Routines:

> Aug 06, 2008@12:27:39

> Install Started for WV\*1.0\*23 :

> Aug 06, 2008@12:27:39

> Build Distribution Date: Aug 01, 2007

> Installing Routines:

> Aug 06, 2008@12:27:39

> Updating Routine file...

> Updating KIDS files...

> WV\*1.0\*23 Installed.

> Aug 06, 2008@12:27:39

> Install Started for TIU\*1.0\*219 :

> Aug 06, 2008@12:27:39

> Build Distribution Date: Feb 04, 2008

> Installing Routines:

> Aug 06, 2008@12:27:40

> Installing Data Dictionaries:

> Aug 06, 2008@12:27:40

> Installing PACKAGE COMPONENTS:

> Installing REMOTE PROCEDURE:

> Aug 06, 2008@12:27:40

> Running Post-Install Routine: ^TIUPS219

> Compiling TIU ENTER/EDIT DS Input Template of File 8925..

> 'TIUEDS1' ROUTINE FILED..

> 'TIUEDS2' ROUTINE FILED.....

> 'TIUEDS3' ROUTINE FILED.

> 'TIUEDS4' ROUTINE FILED.

> 'TIUEDS' ROUTINE FILED.....

> 'TIUEDS6' ROUTINE FILED.

> 'TIUEDS7' ROUTINE FILED....

> 'TIUEDS8' ROUTINE FILED.

> 'TIUEDS9' ROUTINE FILED.

> 'TIUEDS5' ROUTINE FILED..........

> 'TIUEDS11' ROUTINE FILED.

> 'TIUEDS12' ROUTINE FILED..

> 'TIUEDS13' ROUTINE FILED.

> 'TIUEDS10' ROUTINE FILED.

> 'TIUEDS14' ROUTINE FILED.

> Updating Routine file...

> The following Routines were created during this install:

> TIUXRC

> TIUXRC1

> TIUXRC2

> TIUXRC3

> TIUXRC4

> TIUXRC5

> TIUXRC6

> Updating KIDS files...

> TIU\*1.0\*219 Installed.

> Aug 06, 2008@12:27:41

> Install Started for GMPL\*2.0\*35 :

> Aug 06, 2008@12:27:41

> Build Distribution Date: Mar 21, 2008

> Installing Routines:

> Aug 06, 2008@12:27:41

> Installing Data Dictionaries:

> Aug 06, 2008@12:27:41

> Updating Routine file...

> Updating KIDS files...

> GMPL\*2.0\*35 Installed.

> Aug 06, 2008@12:27:41

> Install Started for GMRA\*4.0\*38 :

> Aug 06, 2008@12:27:41

> Build Distribution Date: May 04, 2007

> Installing Routines:

> Aug 06, 2008@12:27:41

> Running Post-Install Routine: POST^GMRAY38

> Updating Routine file...

> Updating KIDS files...

> GMRA\*4.0\*38 Installed.

> Aug 06, 2008@12:27:48

> Install Started for GMTS\*2.7\*80 :

> Aug 06, 2008@12:27:48

> Build Distribution Date: May 21, 2007

> Installing Routines:

> Aug 06, 2008@12:27:48

> Updating Routine file...

> Updating KIDS files...

> GMTS\*2.7\*80 Installed.

> Aug 06, 2008@12:27:48

> Install Started for LR\*5.2\*365 :

> Aug 06, 2008@12:27:48

> Build Distribution Date: Apr 23, 2008

> Installing Routines:

> Aug 06, 2008@12:27:48

> Installing PACKAGE COMPONENTS:

> Installing OPTION

> Aug 06, 2008@12:27:49

> Updating Routine file...

> Updating KIDS files...

> LR\*5.2\*365 Installed.

> Aug 06, 2008@12:27:49

> Updating Routine file...

> Updating KIDS files...

> CPRS BUNDLE GUI 27.0 Installed.

> Aug 06, 2008@12:27:49

> Install Completed

> Checksum Value Verification

> 1 Load a Distribution

> 2 Verify Checksums in Transport Global

> 3 Print Transport Global

> 4 Compare Transport Global to Current System

> 5 Backup a Transport Global

> 6 Install Package(s)

> Restart Install of Package(s)

> Unload a Distribution

> Select Installation Option: 2 Verify Checksums in Transport Global

> Select INSTALL NAME: OR PSJ PSO 27 1.0 Loaded from Distribution 8/6/08@12

> :42:05

> =\> CPRS27 AND REQUIRED PHARMACY PATCHES - RELEASED ;Created on Jun 18, 2

> This Distribution was loaded on Aug 06, 2008@12:42:05 with header of

> CPRS27 AND REQUIRED PHARMACY PATCHES - RELEASED ;Created on Jun 18, 2008@09:

> 54:06

> It consisted of the following Install(s):

> OR PSJ PSO 27 1.0 PSJ\*5.0\*134 PSO\*7.0\*225 OR\*3.0\*243

> Want each Routine Listed with Checksums: Yes// YES

> PACKAGE: OR PSJ PSO 27 1.0 Aug 06, 2008 12:43 pm PAGE 1

> -------------------------------------------------------------------------------

> 0 Routine checked, 0 failed.

> PACKAGE: PSJ\*5.0\*134 Aug 06, 2008 12:43 pm PAGE 1

> -------------------------------------------------------------------------------

> PSGOE1 Calculated 29072557

> PSGOE6 Calculated 24315055

> PSGOEC Calculated 67210353

> PSGOECS Calculated 48040655

> PSGOEF Calculated 63235308

> PSGOT Calculated 14273547

> PSGS0 Calculated 51528600

> PSIVCAL Calculated 65800854

> PSIVEDT Calculated 41996183

> PSIVORA Calculated 28909914

> PSIVORC Calculated 24718262

> PSIVORC1 Calculated 43227243

> PSIVOREN Calculated 27138020

> PSIVORFA Calculated 24701688

> PSIVORFB Calculated 50190472

> PSIVSP Calculated 37490534

> PSIVUTL1 Calculated 26385588

> PSJHL2 Calculated 36875797

> PSJHL3 Calculated 65300768

> PSJHL4 Calculated 72457593

> PSJHL4A Calculated 56736588

> PSJHL5 Calculated 31480184

> PSJHL9 Calculated 61245429

> PSJHLU Calculated 34501644

> PSJLIACT Calculated 40055313

> PSJLIVFD Calculated 39296093

> PSJLIVMD Calculated 77166995

> PSJOREN Calculated 15419073

> PSJORPOE Calculated 37937868

> PSJORRE Calculated 32121973

> PSJORRE1 Calculated 35337470

> PSJORREN Calculated 20851674

> PSJORRN Calculated 60756345

> PSJORRN1 Calculated 54888629

> PSJORRO Calculated 61708639

> PSJORUT2 Calculated 47514615

> PSJUTL Calculated 65061820

> 37 Routines checked, 0 failed.

> PACKAGE: PSO\*7.0\*225 Aug 06, 2008 12:43 pm PAGE 1

> -------------------------------------------------------------------------------

> PSOCAN3 Calculated 70221168

> PSOCAN3N Calculated 656532

> PSOCAN4 Calculated 42375050

> PSOCIDC2 Calculated 71704423

> PSOCP Calculated 67321239

> PSOCP1 Calculated 5367762

> PSOCPC Calculated 74796456

> PSOCPE Calculated 80668529

> PSODIAG Calculated 63590551

> PSOHLDA Calculated 10014334

> PSOHLNE1 Calculated 73330251

> PSOHLNE2 Calculated 60250922

> PSOHLNE3 Calculated 61361284

> PSOHLNE4 Calculated 17206219

> PSOHLNEW Calculated 80329211

> PSOHLPII Calculated 53884421

> PSOHLPIS Calculated 64280169

> PSOHLSN1 Calculated 71972158

> PSOHLSN2 Calculated 7919233

> PSOHLSN3 Calculated 4822097

> PSOHLSNC Calculated 54704997

> PSOHLUP Calculated 20030650

> PSOLBL Calculated 63143813

> PSOLBL1 Calculated 29469598

> PSOLLLI Calculated 66409595

> PSOLMAO Calculated 247627

> PSOLMPO Calculated 1183408

> PSOLMPO1 Calculated 1200387

> PSOLMPO2 Calculated 590140

> PSOLMRN Calculated 567748

> PSOLMUTL Calculated 10572703

> PSOMLLD2 Calculated 28319271

> PSOMLLDT Calculated 86446402

> PSON52 Calculated 62785056

> PSONEW Calculated 28292272

> PSONEW2 Calculated 32398190

> PSONEWF Calculated 38013501

> PSONEWG Calculated 25309370

> PSONFI Calculated 9036524

> PSOORFI1 Calculated 74027837

> PSOORFI2 Calculated 90909677

> PSOORFI3 Calculated 74814603

> PSOORFI5 Calculated 18224487

> PSOORFI6 Calculated 23497771

> PSOORFIN Calculated 59563720

> PSOORFL Calculated 917206

> PSOORNE4 Calculated 68513696

> PSOORNE5 Calculated 60780567

> PSOORNEW Calculated 72157265

> PSOORRL Calculated 64370128

> PSOORRL3 Calculated 23985690

> PSOORRLN Calculated 43625961

> PSOORRLO Calculated 39129717

> PSOORRNW Calculated 24091362

> PSOORUT1 Calculated 67437810

> PSOORUTL Calculated 42932698

> PSOPFSU0 Calculated 16719729

> PSOPFSU1 Calculated 33416502

> PSOPTPST Calculated 27932490

> PSORENW1 Calculated 60533620

> PSORENW4 Calculated 56219403

> PSORN52 Calculated 46207711

> PSORN52A Calculated 18565756

> PSORN52C Calculated 49927643

> PSORN52D Calculated 41922848

> 65 Routines checked, 0 failed.

> PACKAGE: OR\*3.0\*243 Aug 06, 2008 12:43 pm PAGE 1

> -------------------------------------------------------------------------------

> OCXOCMP Calculated 41613467

> OCXOCMP6 Calculated 40637033

> OCXOCMP8 Calculated 14209872

> OCXOCMPV Calculated 62658161

> OCXSEND Calculated 23135487

> OCXSEND3 Calculated 11211964

> OCXSEND4 Calculated 21759136

> OCXSEND5 Calculated 52984975

> OCXSEND6 Calculated 36540955

> OCXSEND7 Calculated 19892897

> OCXSEND8 Calculated 20772543

> OCXSENDA Calculated 19003008

> ORALWORD Calculated 47499175

> ORB3FUP1 Calculated 64991738

> ORB3FUP2 Calculated 68246237

> ORB3LAB Calculated 3813832

> ORBCMA1 Calculated 16067541

> ORBCMA32 Calculated 85583831

> ORBPRCHK Calculated 30311169

> ORCACT0 Calculated 52518165

> ORCACT01 Calculated 66127888

> ORCACT03 Calculated 8066015

> ORCACT2 Calculated 61910854

> ORCB Calculated 51269339

> ORCD Calculated 53571666

> ORCDFH1 Calculated 22101872

> ORCDLG1 Calculated 72953104

> ORCDLG2 Calculated 64872872

> ORCDLR Calculated 57494194

> ORCDLR1 Calculated 81262557

> ORCDLR2 Calculated 13639155

> ORCDPS1 Calculated 74826833

> ORCDPS2 Calculated 67090529

> ORCDPS3 Calculated 43323695

> ORCDPSH Calculated 17713696

> ORCDPSIV Calculated 96443893

> ORCFLAG Calculated 21880963

> ORCHANG2 Calculated 30221469

> ORCHANGE Calculated 41306460

> ORCHECK Calculated 47055177

> ORCMED Calculated 41444759

> ORCMEDT0 Calculated 17512805

> ORCMEDT1 Calculated 44493328

> ORCMEDT8 Calculated 77783054

> ORCSAVE Calculated 70416179

> ORCSAVE1 Calculated 30031657

> ORCSAVE2 Calculated 68713994

> ORCSEND Calculated 63497942

> ORCSEND1 Calculated 61198784

> ORCSEND3 Calculated 25727603

> ORCXPND1 Calculated 72217223

> ORCXPND3 Calculated 44348323

> ORDDPAPI Calculated 1521511

> ORDV02A Calculated 11152192

> ORDV03 Calculated 47046777

> ORDV04 Calculated 57992153

> ORDV04A Calculated 41731567

> ORDV06 Calculated 40307303

> ORDV06A Calculated 7403444

> ORDV08 Calculated 20597537

> ORDVX1 Calculated 5290851

> OREVNTX Calculated 73719059

> OREVNTX1 Calculated 72373665

> ORHLESC Calculated 6778413

> ORIMO Calculated 2288142

> ORKCHK Calculated 41864853

> ORKLR Calculated 31162442

> ORLP Calculated 76319972

> ORLPSR Calculated 54297693

> ORLPSRA Calculated 62257534

> ORLPSRB Calculated 38794452

> ORLSTVIZ Calculated 5546292

> ORMBLDP1 Calculated 3663295

> ORMBLDPS Calculated 74740266

> ORMBLDRA Calculated 9959617

> ORMEVNT Calculated 75252404

> ORMFH Calculated 63062271

> ORMFN Calculated 33381686

> ORMGMRC Calculated 44058430

> ORMLR Calculated 55346176

> ORMPS Calculated 79586894

> ORMPS1 Calculated 68866316

> ORMPS2 Calculated 46355925

> ORMPS3 Calculated 25338633

> ORMRA Calculated 62066557

> ORMTIM02 Calculated 17248840

> ORMTIME Calculated 9294457

> OROVRRPT Calculated 40771295

> ORPEAPI Calculated 385487

> ORPRF Calculated 13135968

> ORPRPM Calculated 62635453

> ORQ11 Calculated 63884857

> ORQ12 Calculated 36656064

> ORQ2 Calculated 39956511

> ORQ20 Calculated 49432908

> ORQ21 Calculated 35097340

> ORQPT Calculated 73861080

> ORQPTQ1 Calculated 54791820

> ORQQAL Calculated 28169891

> ORQQPL1 Calculated 62886431

> ORQQPL3 Calculated 55317795

> ORQQPXRM Calculated 18382115

> ORSRCHOR Calculated 77451785

> ORTSKLPS Calculated 5805034

> ORUDPA Calculated 4870592

> ORUTL1 Calculated 5293035

> ORWCIRN Calculated 9046507

> ORWCV Calculated 73405381

> ORWD Calculated 42948340

> ORWDAL32 Calculated 40874191

> ORWDBA1 Calculated 58828931

> ORWDBA3 Calculated 40638555

> ORWDBA4 Calculated 10113870

> ORWDBA7 Calculated 17868873

> ORWDFH Calculated 51608431

> ORWDGX Calculated 5976236

> ORWDLR Calculated 25735868

> ORWDLR32 Calculated 60083103

> ORWDLR33 Calculated 20970855

> ORWDOR Calculated 8588372

> ORWDPS1 Calculated 49131928

> ORWDPS2 Calculated 57106070

> ORWDPS32 Calculated 70700114

> ORWDPS33 Calculated 31468284

> ORWDPS4 Calculated 20050046

> ORWDVAL Calculated 2573377

> ORWDX Calculated 62342605

> ORWDX1 Calculated 51089138

> ORWDX2 Calculated 12248764

> ORWDXA Calculated 73502300

> ORWDXC Calculated 22991536

> ORWDXM1 Calculated 76690189

> ORWDXM2 Calculated 75208802

> ORWDXM3 Calculated 65753115

> ORWDXR Calculated 48540055

> ORWDXVB Calculated 43771926

> ORWDXVB1 Calculated 34643378

> ORWDXVB2 Calculated 24066583

> ORWGAPI Calculated 23670784

> ORWGAPI1 Calculated 30659117

> ORWGAPI2 Calculated 18274252

> ORWGAPI3 Calculated 30105389

> ORWGAPI4 Calculated 60283342

> ORWGAPI5 Calculated 9504422

> ORWGAPI6 Calculated 16567335

> ORWGAPI7 Calculated 6370115

> ORWGAPI8 Calculated 7954497

> ORWGAPIA Calculated 34887063

> ORWGAPIB Calculated 3779452

> ORWGAPIC Calculated 34311571

> ORWGAPID Calculated 59091643

> ORWGAPIE Calculated 14227801

> ORWGAPIF Calculated 5028214

> ORWGAPIP Calculated 70762744

> ORWGAPIR Calculated 41364234

> ORWGAPIT Calculated 57224397

> ORWGAPIU Calculated 23844957

> ORWGAPIW Calculated 11947849

> ORWGAPIX Calculated 23118742

> ORWGRPC Calculated 13989770

> ORWGTASK Calculated 79728825

> ORWGTEST Calculated 8668416

> ORWNSS Calculated 4680257

> ORWOD Calculated 64537880

> ORWOD1 Calculated 30304637

> ORWOR Calculated 35518390

> ORWORB Calculated 67054061

> ORWORR Calculated 66127235

> ORWORR1 Calculated 7659282

> ORWPCE Calculated 56892321

> ORWPCE1 Calculated 63376274

> ORWPCE2 Calculated 49058348

> ORWPS Calculated 62358507

> ORWPT Calculated 59655732

> ORWPT16 Calculated 11809182

> ORWRP Calculated 77665061

> ORWRP3 Calculated 10390812

> ORWRP4P Calculated 6881393

> ORWRP4V Calculated 25785819

> ORWTIU Calculated 10078381

> ORWTPD Calculated 13966510

> ORWTPL Calculated 25081990

> ORWTPP Calculated 19368874

> ORWTPR Calculated 16242046

> ORWTPT Calculated 20925260

> ORWTPUA Calculated 2193311

> ORWU Calculated 60173136

> ORWU2 Calculated 22524024

> ORY243 Calculated 79494059

> ORY2430 Calculated 15644892

> ORY24301 Calculated 71550908

> ORY24302 Calculated 79020665

> ORY24303 Calculated 78469831

> ORY24304 Calculated 86792017

> ORY24305 Calculated 58679499

> ORY24306 Calculated 66782929

> ORY24307 Calculated 70006769

> ORY24308 Calculated 66749787

> ORY24309 Calculated 8754768

> ORY2431 Calculated 40550963

> ORY2432 Calculated 26766774

> ORY2433 Calculated 12996416

> ORY2434 Calculated 13526318

> ORY243A Calculated 4754803

> ORY243ES Calculated 12630447

> ORY243R Calculated 5847434

> ORYDLG Calculated 14515305

> 207 Routines checked, 0 failed.

> Transport Global Print

> 1 Load a Distribution

> 2 Verify Checksums in Transport Global

> 3 Print Transport Global

> 4 Compare Transport Global to Current System

> 5 Backup a Transport Global

> 6 Install Package(s)

> Restart Install of Package(s)

> Unload a Distribution

> Select Installation Option: 3 Print Transport Global

> Select INSTALL NAME: OR PSJ PSO 27 1.0 Loaded from Distribution 8/6/08@12

> :42:05

> =\> CPRS27 AND REQUIRED PHARMACY PATCHES - RELEASED ;Created on Jun 18, 2

> This Distribution was loaded on Aug 06, 2008@12:42:05 with header of

> CPRS27 AND REQUIRED PHARMACY PATCHES - RELEASED ;Created on Jun 18, 2008@09:54:06

> It consisted of the following Install(s):

> OR PSJ PSO 27 1.0 PSJ\*5.0\*134 PSO\*7.0\*225 OR\*3.0\*243

> DEVICE: HOME// ;;9999 TELNET TERMINAL

> PACKAGE: OR PSJ PSO 27 1.0 Aug 06, 2008 12:43 pm PAGE 1

> -------------------------------------------------------------------------------

> TYPE: MULTI-PACKAGE TRACK NATIONALLY: YES

> NATIONAL PACKAGE: ALPHA/BETA TESTING: NO

> DESCRIPTION:

> BUNDLE BUILD OF OR\*3.0\*243 AND PSJ\*5.0\*134

> SEQUENCE OF BUILDS:

> 1 PSJ\*5.0\*134 Required to Continue

> 2 PSO\*7.0\*225 Required to Continue

> 3 OR\*3.0\*243 Required to Continue

> TYPE: SINGLE PACKAGE TRACK NATIONALLY: YES

> NATIONAL PACKAGE: INPATIENT MEDICATIONS ALPHA/BETA TESTING: NO

> DESCRIPTION:

> This patch contains changes in support of Computerized Patient

> Record System (CPRS) V. 1.0 GUI v27 release.

> 1\. MEDICATION ROUTE CHANGES

> ----------------------------

> \- Inpatient Medications V. 5.0 will use the medication route received from

> CPRS V. 1.0 as the default when finishing an IV order entered via CPRS

> V. 1.0. For new orders entered via Inpatient Medications V. 5.0, if all

> of the orderable items associated with an order contain the same default

> medication route, that route will be used as the default. If there are

> any differences, there will be no default medication route.

> \- Inpatient Medications V. 5.0 will send to BCMA V. 3.0 the full

> medication route name for display on the Virtual Due List (VDL).

> 2\. INFUSION RATE CHANGES

> -------------------------

> \- Inpatient Medications V. 5.0 now accepts infusion rate from CPRS in both

> ml/hour and as 'infuse over time'.

> \- In the order view screen for an order with an intermittent IV type, the

> infusion rate now displays as "Infuse Over" followed by the time. For

> example, "Infuse Over 30 minutes".

> The infusion rate for an intermittent IV order can be null.

> 3\. IV TYPE CHANGES

> -------------------

> \- Inpatient Medications V. 5.0 shall accept an IV type of "I"

> (Intermittent) or "C" (Continuous) from CPRS V. 1.0. When an IV type of

> CONTINUOUS is received, Inpatient Medications V. 5.0 defaults to an IV

> type of Admixture. When IV type of INTERMITTENT is received,

> Inpatient Medications V. 5.0 defaults to an IV type of Piggyback.

> Inpatient Medications V. 5.0 sends to CPRS V. 1.0 updates to an order's

> IV type.

> \- Inpatient Medications V. 5.0 now accepts schedule information from

> CPRS V. 1.0 for intermittent IV orders entered via the IV Fluid

> Ordering Dialog. Inpatient Medications V. 5.0 also sends to

> CPRS V. 1.0 any schedule changes for intermittent IV orders.

> \- A new field, IV TYPE CATEGORY (#128) is being added to the NON-

> VERIFIED ORDERS file (#53.1). The IV TYPE CATEGORY will be "C"

> (Continuous) for orders with an IV TYPE of Admixture, Hyperal,

> Non-Intermittent Syringe, or Chemotherapy with a CHEMOTHERAPY TYPE

> of Admixture, Hyperal, or Non-Intermittent Syringe. The IV TYPE

> CATEGORY will be "I" (Intermittent) for orders with an IV TYPE of

> Piggyback, Intermittent Syringe, or Chemotherapy with a CHEMOTHERAPY

> TYPE of Piggyback or Intermittent Syringe.

> 4\. RENEWED ORDER CHANGES

> -------------------------

> \- When discontinuing pending renewal orders, Inpatient Medications V. 5.0

> will provide the user an option to discontinue the pending renewal

> order and/or the original orders. The pharmacist shall be given the

> option to discontinue the pending order, both orders, or exit the

> discontinue function.

> 5\. REMOVE CALLS TO OBSOLETE ROUTINE

> ------------------------------------

> \- At the request of CPRS V. 1.0, active calls to obsolete routine OR3CONV

> have been removed from Inpatient Medications V. 5.0.

> 6\. EXPECTED FIRST DOSE FOR ONE-TIME ORDERS (HD 98365)

> ------------------------------------------------------

> Problem:

> During testing of the CPRS V. 1.0 GUI v26 release, sites reported a

> problem with an incorrect display of expected first dose for orders

> with a schedule type of "ONE TIME".

> Resolution:

> If the schedule type is "ONE TIME", do not display an Expected

> First Dose for the order.

> 7\. CORRECT ABBREVIATION OF MILLIMOLE (HD 145562)

> -------------------------------------------

> Problem:

> The correct abbreviation for the word MILLIMOLE, which is MMOL

> is not available in the system.

> Resolution:

> The abbreviation for Millimole, "MMOL", will be included in

> this patch.

> ENVIRONMENT CHECK: DELETE ENV ROUTINE:

> PRE-INIT ROUTINE: DELETE PRE-INIT ROUTINE:

> POST-INIT ROUTINE: DELETE POST-INIT ROUTINE:

> PRE-TRANSPORT RTN:

> UP SEND DATA USER

> DATE SEC. COMES SITE RSLV OVER

> FILE \# FILE NAME DD CODE W/FILE DATA PTRS RIDE

> -------------------------------------------------------------------------------

> 53.1 NON-VERIFIED ORDERS YES YES NO NO

> Partial DD: subDD: 53.1 fld: 128

> ROUTINE: ACTION:

> PSGOE1 SEND TO SITE

> PSGOE6 SEND TO SITE

> PSGOEC SEND TO SITE

> PSGOECS SEND TO SITE

> PSGOEF SEND TO SITE

> PSGOT SEND TO SITE

> PSGS0 SEND TO SITE

> PSIVCAL SEND TO SITE

> PSIVEDT SEND TO SITE

> PSIVORA SEND TO SITE

> PSIVORC SEND TO SITE

> PSIVORC1 SEND TO SITE

> PSIVOREN SEND TO SITE

> PSIVORFA SEND TO SITE

> PSIVORFB SEND TO SITE

> PSIVSP SEND TO SITE

> PSIVUTL1 SEND TO SITE

> PSJHL2 SEND TO SITE

> PSJHL3 SEND TO SITE

> PSJHL4 SEND TO SITE

> PSJHL4A SEND TO SITE

> PSJHL5 SEND TO SITE

> PSJHL9 SEND TO SITE

> PSJHLU SEND TO SITE

> PSJLIACT SEND TO SITE

> PSJLIVFD SEND TO SITE

> PSJLIVMD SEND TO SITE

> PSJOREN SEND TO SITE

> PSJORPOE SEND TO SITE

> PSJORRE SEND TO SITE

> PSJORRE1 SEND TO SITE

> PSJORREN SEND TO SITE

> PSJORRN SEND TO SITE

> PSJORRN1 SEND TO SITE

> PSJORRO SEND TO SITE

> PSJORUT2 SEND TO SITE

> PSJUTL SEND TO SITE

> REQUIRED BUILDS: ACTION:

> PSJ\*5.0\*152 Don't install, leave global

> PSJ\*5.0\*153 Don't install, leave global

> PSJ\*5.0\*180 Don't install, leave global

> PSJ\*5.0\*120 Don't install, leave global

> PSJ\*5.0\*174 Don't install, leave global

> PSJ\*5.0\*140 Don't install, leave global

> PSJ\*5.0\*141 Don't install, leave global

> PSJ\*5.0\*156 Don't install, leave global

> PSJ\*5.0\*157 Don't install, leave global

> PSJ\*5.0\*173 Don't install, leave global

> PSJ\*5.0\*201 Don't install, leave global

> PSO\*7.0\*225 Aug 06, 2008 12:43 pm PAGE 1

> -------------------------------------------------------------------------------

> TYPE: SINGLE PACKAGE TRACK NATIONALLY: YES

> NATIONAL PACKAGE: OUTPATIENT PHARMACY ALPHA/BETA TESTING: NO

> DESCRIPTION:

> The Enrollment VistA Changes (EVC) project is being undertaken to support

> technology and business changes that are occurring with the implementation

> of the Health Eligibility Center (HEC) Enrollment System Redesign (ESR)

> project. Some modified and new business functionality is being included in

> the new system and corresponding changes are necessary in VistA for

> preliminary determination of veterans Enrollment and Eligibility status.

> The EVC project has been rolled out in three phases. This release

> represents the third and last phase called EVC Release 2.

> This patch provides the functionality changes to determine, process and

> disseminate the newly added Environmental Indicator (EI) called Project

> 112/SHAD Exposure (a.k.a SHAD), where applicable.

> This patch also changed the EI, "Environmental Contaminant" to read

> as "Southwest Asia Conditions".

> 1\. For the following options, when creating a new order, renewing an

> existing order, copying an existing order to a new order, or editing

> an existing order that results in a new order, the copay status of the

> prescription needs to be determined for billing purposes.

> a\. Patient Prescription Processing \[PSO LM BACKDOOR ORDERS\]

> b\. Barcode Batch Prescription Entry \[PSO BATCH BARCODE\]

> c\. Complete Orders from OERR \[PSO LMOE FINISH\]

> If a patient is found eligible for SHAD then the prompt

> "Was treatment related to PROJ 112/SHAD?" will be presented to the

> pharmacist.

> A "YES" or "NO" response will be stored in the new fields, PROJ

> 112/SHAD field (#122.01) of the PRESCRIPTION file (#52) and in the PROJ

> 112/SHAD field (#8) of the ICD DIAGNOSIS sub-file (#52.052311) of the

> PRESCRIPTION file (#52).

> 2\. The Integration Control Registration (ICR) \#2534, provides

> Computerized Patient Record System V. 3.0 (CPRS) with all the eligible

> EI questions that will be prompted during the pharmacy order entry

> process. This ICR is modified to include the SHAD prompt.

> 3\. When a verbal or telephone order is placed in backdoor pharmacy, it

> requires an electronic signature from the provider. During the

> signature entry process in CPRS, the provider may update the SC, EI,

> or the ICD diagnosis information. This updated information is passed

> back to pharmacy via the ICR \#4666, which is modified to include the

> SHAD changes.

> 4\. The PENDING OUTPATIENT ORDERS file (#52.41) that stores the pharmacy

> orders entered via CPRS is modified to include the provider's response

> to the SHAD question. The provider's response will be stored in the

> new fields, PROJ 112/SHAD field (#110.2) of the PENDING OUTPATIENT

> ORDERS file (#52.41) and the PROJ 112/SHAD field (#8) of the DIAGNOSIS

> sub-file (#52.41311) of the PENDING OUTPATIENT ORDERS file (#52.41).

> 5\. During the release of a prescription, if the SHAD question applies and

> is unanswered, the MailMan message that is sent to the finishing

> pharmacist, ordering provider, and holders of the PSO COPAY key, to

> get answers to the EI questions will have the SHAD question if

> applicable.

> 6\. The Reset Copay Status/Cancel Charges \[PSOCP RESET COPAY STATUS\]

> option is modified to include the SHAD question wherever applicable.

> 7\. During label printing, if the prescription is flagged as SHAD then the

> text "NO COPAY" will be printed in the label.

> Unrelated to the Enrollment VistA Changes (EVC) features, this patch also

> provides the following changes to support CPRS v27.

> a\. To add the proper escape sequences to the standard HEALTH LEVEL

> SEVEN (HL7) encoding characters to messages sent to CPRS / remove

> escape sequences received from CPRS and replace them with standard HL7

> encoding characters. This will help avoid errors that can occur if

> special delimiting characters are encountered during parsing of the

> HL7 messages.

> b\. Integration Control Registration (ICR) \#2400, will be modified to

> provide new sorting sequences of the patient medication profile that

> is viewed under the CPRS-Meds Tab including the Non-VA medications.

> VIEW 0 or null - This provides the medication list as it was prior to

> GUI 27 so that other applications calling this API will not

> see any changes.

> VIEW 1 - This provides the medication list sorted by prescription

> Status Group and Stop Date/Expiration Date. Following is the

> order:

> Pending group

> Non-Verified

> Pending

> Active group:

> Active

> Hold

> Suspended (Active/Susp)

> Provider Hold

> Expired group

> Expired

> Discontinued/Deleted group

> Discontinued by Provider

> Discontinued (Edit)

> VIEW 2 - This provides the medication list sorted by prescription

> Status Group, Status, and Drug Name.

> Active group:

> Active

> Hold

> Pending group

> Non-Verified

> Pending

> Discontinued

> Discontinued by Provider

> Discontinued (Edit)

> VIEW 3 - This provides the medication list sorted by Drug Name,

> active/suspended and Stop Date/Expiration Date.

> c\. Flag/Un-Flag functionality (PSI-06-041)

> It was requested in the Remedy ticket \#133716 that the flagging

> capability that is available in CPRS be made available for

> Outpatient Pharmacy use. This patch provides the flagging

> functionality for Pending orders only.

> d\. As per the E3R numbers 19973 and 19876, to improve communication

> between the provider and the pharmacist, Outpatient Pharmacy will now

> send the actual comments made by the pharmacist to CPRS when a

> prescription is put on Hold, Discontinued, and Returned to Stock

> replacing the generic "per pharmacy request" text.

> e\. When the DC-Discontinue ListMan option is used to discontinue a

> pending "renewal" order, the software will now check for an active

> prescription for the same drug. If found it will prompt the following:

> "There is an active Rx for this pending order, Discontinue both

> (Y/N)".

> This will provide the user with the option to discontinue both pending

> and the active order.

> f\. A problem was reported in one of the error messages displayed on CPRS

> side when a provider tries to discontinue an Outpatient Pharmacy

> order from the Orders Tab and that order for some reason is

> not found in the PRESCRIPTION file (#52). The solution provided is to

> replace the error message "Unable to locate order" with "Invalid

> Pharmacy order number" to be in consistent with the Inpatient

> Medications V. 5.0 error messages.

> g\. At the request of CPRS active calls to obsolete routine OR3CONV have

> been removed from Outpatient Pharmacy V. 7.0.

> h\. When finishing a pending order placed in CPRS, it was reported that

> the patient instructions sent across to CPRS was getting truncated.

> This patch fixes the problem.

> i\. PSI-07-057 - Potential of inappropriate or misleading provider

> comments to be automatically included on new medication orders.

> To fix this problem CPRS is dropping (will not carry over) the

> original provider comments during renewals of Outpatient Pharmacy

> medications.

> To follow suit with CPRS, Outpatient Pharmacy is also dropping the

> original provider comments from all backdoor renewals.

> ENVIRONMENT CHECK: DELETE ENV ROUTINE:

> PRE-INIT ROUTINE: DELETE PRE-INIT ROUTINE:

> POST-INIT ROUTINE: DELETE POST-INIT ROUTINE:

> PRE-TRANSPORT RTN:

> UP SEND DATA USER

> DATE SEC. COMES SITE RSLV OVER

> FILE \# FILE NAME DD CODE W/FILE DATA PTRS RIDE

> -------------------------------------------------------------------------------

> 52 PRESCRIPTION YES YES NO NO

> Partial DD: subDD: 52 fld: 120

> fld: 122.01

> subDD: 52.052311 fld: 4

> fld: 8

> 52.41 PENDING OUTPATIENT ORDERS YES YES NO NO

> Partial DD: subDD: 52.41 fld: 33

> fld: 34

> fld: 35

> fld: 36

> fld: 37

> fld: 38

> fld: 109

> fld: 110.2

> subDD: 52.41311 fld: 4

> fld: 8

> ROUTINE: ACTION:

> PSOCAN3 SEND TO SITE

> PSOCAN3N SEND TO SITE

> PSOCAN4 SEND TO SITE

> PSOCIDC2 SEND TO SITE

> PSOCP SEND TO SITE

> PSOCP1 SEND TO SITE

> PSOCPC SEND TO SITE

> PSOCPE SEND TO SITE

> PSODIAG SEND TO SITE

> PSOHLDA SEND TO SITE

> PSOHLNE1 SEND TO SITE

> PSOHLNE2 SEND TO SITE

> PSOHLNE3 SEND TO SITE

> PSOHLNE4 SEND TO SITE

> PSOHLNEW SEND TO SITE

> PSOHLPII SEND TO SITE

> PSOHLPIS SEND TO SITE

> PSOHLSN1 SEND TO SITE

> PSOHLSN2 SEND TO SITE

> PSOHLSN3 SEND TO SITE

> PSOHLSNC SEND TO SITE

> PSOHLUP SEND TO SITE

> PSOLBL SEND TO SITE

> PSOLBL1 SEND TO SITE

> PSOLLLI SEND TO SITE

> PSOLMAO SEND TO SITE

> PSOLMPO SEND TO SITE

> PSOLMPO1 SEND TO SITE

> PSOLMPO2 SEND TO SITE

> PSOLMRN SEND TO SITE

> PSOLMUTL SEND TO SITE

> PSOMLLD2 SEND TO SITE

> PSOMLLDT SEND TO SITE

> PSON52 SEND TO SITE

> PSONEW SEND TO SITE

> PSONEW2 SEND TO SITE

> PSONEWF SEND TO SITE

> PSONEWG SEND TO SITE

> PSONFI SEND TO SITE

> PSOORFI1 SEND TO SITE

> PSOORFI2 SEND TO SITE

> PSOORFI3 SEND TO SITE

> PSOORFI5 SEND TO SITE

> PSOORFI6 SEND TO SITE

> PSOORFIN SEND TO SITE

> PSOORFL SEND TO SITE

> PSOORNE4 SEND TO SITE

> PSOORNE5 SEND TO SITE

> PSOORNEW SEND TO SITE

> PSOORRL SEND TO SITE

> PSOORRL3 SEND TO SITE

> PSOORRLN SEND TO SITE

> PSOORRLO SEND TO SITE

> PSOORRNW SEND TO SITE

> PSOORUT1 SEND TO SITE

> PSOORUTL SEND TO SITE

> PSOPFSU0 SEND TO SITE

> PSOPFSU1 SEND TO SITE

> PSOPTPST SEND TO SITE

> PSORENW1 SEND TO SITE

> PSORENW4 SEND TO SITE

> PSORN52 SEND TO SITE

> PSORN52A SEND TO SITE

> PSORN52C SEND TO SITE

> PSORN52D SEND TO SITE

> PROTOCOL: ACTION:

> PSO LM BACKDOOR SELECT ORDER SEND TO SITE

> PSO LM FLAG SEND TO SITE

> PSO LM NEW SELECT ORDER SEND TO SITE

> PSO PENDING ORDER MENU MERGE MENU ITEMS

> LIST TEMPLATE: ACTION:

> PSO LM PENDING ORDER SEND TO SITE

> REQUIRED BUILDS: ACTION:

> PSO\*7.0\*278 Don't install, leave global

> PSO\*7.0\*292 Don't install, leave global

> PSO\*7.0\*264 Don't install, leave global

> PSO\*7.0\*206 Don't install, leave global

> PSO\*7.0\*274 Don't install, leave global

> PSO\*7.0\*275 Don't install, leave global

> PACKAGE: OR\*3.0\*243 Aug 06, 2008 12:43 pm PAGE 1

> -------------------------------------------------------------------------------

> TYPE: SINGLE PACKAGE TRACK NATIONALLY: YES

> NATIONAL PACKAGE: ORDER ENTRY/RESULTS REPORTING ALPHA/BETA TESTING: NO

> DESCRIPTION:

> ENVIRONMENT CHECK: DELETE ENV ROUTINE:

> PRE-INIT ROUTINE: PRE^ORY243 DELETE PRE-INIT ROUTINE: No

> POST-INIT ROUTINE: POST^ORY243 DELETE POST-INIT ROUTINE: No

> PRE-TRANSPORT RTN:

> UP SEND DATA USER

> DATE SEC. COMES SITE RSLV OVER

> FILE \# FILE NAME DD CODE W/FILE DATA PTRS RIDE

> -------------------------------------------------------------------------------

> 100 ORDER YES YES NO NO

> Partial DD: subDD: 100 fld: 39

> fld: 55

> fld: 58

> fld: 94

> fld: 97

> fld: 98

> subDD: 100.008 fld: 4

> fld: 15

> 100.2 OE/RR PATIENT EVENT YES YES NO NO

> Partial DD: subDD: 100.2 fld: 14

> subDD: 100.25 fld: 4

> 100.21 OE/RR LIST YES YES NO NO

> 101.24 OE/RR REPORT YES NO YES REPL YES NO

> DATA SCREEN: I (Y=3)!((Y\>17)&(Y\<28))!(Y\>999)!(Y=48)

> 101.41 ORDER DIALOG NO NO YES REPL YES NO

> DATA SCREEN: I \$\$SENDDLG^ORY243(\$P(^(0),U))

> 101.43 ORDERABLE ITEMS YES YES NO

> HELP FRAME: ACTION:

> ORBA-AO SEND TO SITE

> ORBA-CV SEND TO SITE

> ORBA-EC SEND TO SITE

> ORBA-HNC SEND TO SITE

> ORBA-IR SEND TO SITE

> ORBA-MST SEND TO SITE

> ORBA-SC SEND TO SITE

> ORBA-SHD SEND TO SITE

> ROUTINE: ACTION:

> OCXOCMP SEND TO SITE

> OCXOCMP6 SEND TO SITE

> OCXOCMP8 SEND TO SITE

> OCXOCMPV SEND TO SITE

> OCXSEND SEND TO SITE

> OCXSEND3 SEND TO SITE

> OCXSEND4 SEND TO SITE

> OCXSEND5 SEND TO SITE

> OCXSEND6 SEND TO SITE

> OCXSEND7 SEND TO SITE

> OCXSEND8 SEND TO SITE

> OCXSENDA SEND TO SITE

> OR3CONV DELETE AT SITE

> OR3CONV1 DELETE AT SITE

> OR3POST DELETE AT SITE

> ORALWORD SEND TO SITE

> ORB3FUP1 SEND TO SITE

> ORB3FUP2 SEND TO SITE

> ORB3LAB SEND TO SITE

> ORBCMA1 SEND TO SITE

> ORBCMA32 SEND TO SITE

> ORBPRCHK SEND TO SITE

> ORCACT0 SEND TO SITE

> ORCACT01 SEND TO SITE

> ORCACT03 SEND TO SITE

> ORCACT2 SEND TO SITE

> ORCB SEND TO SITE

> ORCD SEND TO SITE

> ORCDFH1 SEND TO SITE

> ORCDLG1 SEND TO SITE

> ORCDLG2 SEND TO SITE

> ORCDLR SEND TO SITE

> ORCDLR1 SEND TO SITE

> ORCDLR2 SEND TO SITE

> ORCDPS1 SEND TO SITE

> ORCDPS2 SEND TO SITE

> ORCDPS3 SEND TO SITE

> ORCDPSH SEND TO SITE

> ORCDPSIV SEND TO SITE

> ORCFLAG SEND TO SITE

> ORCHANG2 SEND TO SITE

> ORCHANGE SEND TO SITE

> ORCHECK SEND TO SITE

> ORCMED SEND TO SITE

> ORCMEDT0 SEND TO SITE

> ORCMEDT1 SEND TO SITE

> ORCMEDT8 SEND TO SITE

> ORCSAVE SEND TO SITE

> ORCSAVE1 SEND TO SITE

> ORCSAVE2 SEND TO SITE

> ORCSEND SEND TO SITE

> ORCSEND1 SEND TO SITE

> ORCSEND3 SEND TO SITE

> ORCXPND1 SEND TO SITE

> ORCXPND3 SEND TO SITE

> ORDDPAPI SEND TO SITE

> ORDV02A SEND TO SITE

> ORDV03 SEND TO SITE

> ORDV04 SEND TO SITE

> ORDV04A SEND TO SITE

> ORDV06 SEND TO SITE

> ORDV06A SEND TO SITE

> ORDV08 SEND TO SITE

> ORDVX1 SEND TO SITE

> OREVNTX SEND TO SITE

> OREVNTX1 SEND TO SITE

> ORHLESC SEND TO SITE

> ORIMO SEND TO SITE

> ORKCHK SEND TO SITE

> ORKLR SEND TO SITE

> ORLP SEND TO SITE

> ORLPSR SEND TO SITE

> ORLPSRA SEND TO SITE

> ORLPSRB SEND TO SITE

> ORLSTVIZ SEND TO SITE

> ORMBLDP1 SEND TO SITE

> ORMBLDPS SEND TO SITE

> ORMBLDRA SEND TO SITE

> ORMEVNT SEND TO SITE

> ORMFH SEND TO SITE

> ORMFN SEND TO SITE

> ORMGMRC SEND TO SITE

> ORMLR SEND TO SITE

> ORMPS SEND TO SITE

> ORMPS1 SEND TO SITE

> ORMPS2 SEND TO SITE

> ORMPS3 SEND TO SITE

> ORMRA SEND TO SITE

> ORMTIM02 SEND TO SITE

> ORMTIME SEND TO SITE

> OROVRRPT SEND TO SITE

> ORPEAPI SEND TO SITE

> ORPRF SEND TO SITE

> ORPRPM SEND TO SITE

> ORQ11 SEND TO SITE

> ORQ12 SEND TO SITE

> ORQ2 SEND TO SITE

> ORQ20 SEND TO SITE

> ORQ21 SEND TO SITE

> ORQPT SEND TO SITE

> ORQPTQ1 SEND TO SITE

> ORQQAL SEND TO SITE

> ORQQPL1 SEND TO SITE

> ORQQPL3 SEND TO SITE

> ORQQPXRM SEND TO SITE

> ORSRCHOR SEND TO SITE

> ORTSKLPS SEND TO SITE

> ORUDPA SEND TO SITE

> ORUTL1 SEND TO SITE

> ORWCIRN SEND TO SITE

> ORWCV SEND TO SITE

> ORWD SEND TO SITE

> ORWDAL32 SEND TO SITE

> ORWDBA1 SEND TO SITE

> ORWDBA3 SEND TO SITE

> ORWDBA4 SEND TO SITE

> ORWDBA7 SEND TO SITE

> ORWDFH SEND TO SITE

> ORWDGX SEND TO SITE

> ORWDLR SEND TO SITE

> ORWDLR32 SEND TO SITE

> ORWDLR33 SEND TO SITE

> ORWDOR SEND TO SITE

> ORWDPS1 SEND TO SITE

> ORWDPS2 SEND TO SITE

> ORWDPS32 SEND TO SITE

> ORWDPS33 SEND TO SITE

> ORWDPS4 SEND TO SITE

> ORWDVAL SEND TO SITE

> ORWDX SEND TO SITE

> ORWDX1 SEND TO SITE

> ORWDX2 SEND TO SITE

> ORWDXA SEND TO SITE

> ORWDXC SEND TO SITE

> ORWDXM1 SEND TO SITE

> ORWDXM2 SEND TO SITE

> ORWDXM3 SEND TO SITE

> ORWDXR SEND TO SITE

> ORWDXVB SEND TO SITE

> ORWDXVB1 SEND TO SITE

> ORWDXVB2 SEND TO SITE

> ORWGAPI SEND TO SITE

> ORWGAPI1 SEND TO SITE

> ORWGAPI2 SEND TO SITE

> ORWGAPI3 SEND TO SITE

> ORWGAPI4 SEND TO SITE

> ORWGAPI5 SEND TO SITE

> ORWGAPI6 SEND TO SITE

> ORWGAPI7 SEND TO SITE

> ORWGAPI8 SEND TO SITE

> ORWGAPIA SEND TO SITE

> ORWGAPIB SEND TO SITE

> ORWGAPIC SEND TO SITE

> ORWGAPID SEND TO SITE

> ORWGAPIE SEND TO SITE

> ORWGAPIF SEND TO SITE

> ORWGAPIP SEND TO SITE

> ORWGAPIR SEND TO SITE

> ORWGAPIT SEND TO SITE

> ORWGAPIU SEND TO SITE

> ORWGAPIW SEND TO SITE

> ORWGAPIX SEND TO SITE

> ORWGRPC SEND TO SITE

> ORWGTASK SEND TO SITE

> ORWGTEST SEND TO SITE

> ORWNSS SEND TO SITE

> ORWOD SEND TO SITE

> ORWOD1 SEND TO SITE

> ORWOR SEND TO SITE

> ORWORB SEND TO SITE

> ORWORR SEND TO SITE

> ORWORR1 SEND TO SITE

> ORWPCE SEND TO SITE

> ORWPCE1 SEND TO SITE

> ORWPCE2 SEND TO SITE

> ORWPS SEND TO SITE

> ORWPT SEND TO SITE

> ORWPT16 SEND TO SITE

> ORWRP SEND TO SITE

> ORWRP3 SEND TO SITE

> ORWRP4P SEND TO SITE

> ORWRP4V SEND TO SITE

> ORWTIU SEND TO SITE

> ORWTPD SEND TO SITE

> ORWTPL SEND TO SITE

> ORWTPP SEND TO SITE

> ORWTPR SEND TO SITE

> ORWTPT SEND TO SITE

> ORWTPUA SEND TO SITE

> ORWU SEND TO SITE

> ORWU2 SEND TO SITE

> ORY243 SEND TO SITE

> ORY2430 SEND TO SITE

> ORY24301 SEND TO SITE

> ORY24302 SEND TO SITE

> ORY24303 SEND TO SITE

> ORY24304 SEND TO SITE

> ORY24305 SEND TO SITE

> ORY24306 SEND TO SITE

> ORY24307 SEND TO SITE

> ORY24308 SEND TO SITE

> ORY24309 SEND TO SITE

> ORY2431 SEND TO SITE

> ORY2432 SEND TO SITE

> ORY2433 SEND TO SITE

> ORY2434 SEND TO SITE

> ORY243A SEND TO SITE

> ORY243ES SEND TO SITE

> ORY243R SEND TO SITE

> ORYDLG SEND TO SITE

> OPTION: ACTION:

> OR CPRS GUI CHART SEND TO SITE

> OR INPT CLOZAPINE MESSAGE SEND TO SITE

> OR LAPSED ORDERS SEND TO SITE

> OR MEDICATION QO CHECKER SEND TO SITE

> OR PARAM COORDINATOR MENU USE AS LINK FOR MENU ITEMS

> ORB3 ARCHIVE PERIOD SEND TO SITE

> ORCM MGMT USE AS LINK FOR MENU ITEMS

> ORK ORD CHK OVERRIDE REPORT SEND TO SITE

> ORK ORDER CHK MGMT MENU USE AS LINK FOR MENU ITEMS

> ORLP TEAM LIST VISIBILITY SEND TO SITE

> ORLP TEAM MENU USE AS LINK FOR MENU ITEMS

> ORW PARAM GUI USE AS LINK FOR MENU ITEMS

> PARAMETER DEFINITION: ACTION:

> OR ADMIN TIME HELP TEXT SEND TO SITE

> OR CLOZ INPT MSG SEND TO SITE

> OR DC REASON LIST SEND TO SITE

> OR FLAGGED ORD REASONS SEND TO SITE

> OR LAPSE ORDERS SEND TO SITE

> OR LAPSE ORDERS DFLT SEND TO SITE

> OR MEDS TAB SORT SEND TO SITE

> OR RA RFS CARRY ON SEND TO SITE

> OR USE MH DLL SEND TO SITE

> OR VBECS ON SEND TO SITE

> OR VBECS SUPPRESS NURS ADMIN SEND TO SITE

> ORCH CONTEXT MEDS SEND TO SITE

> ORWDXVB VBECS TNS CHECK SEND TO SITE

> ORWLR LC CHANGED TO WC SEND TO SITE

> ORWOR EXPIRED ORDERS SEND TO SITE

> ORWOR WRITE ORDERS LIST SEND TO SITE

> ORWRP VISTAWEB DELETE AT SITE

> REMOTE PROCEDURE: ACTION:

> ORALWORD ALLWORD SEND TO SITE

> ORCDLR2 CHECK ALL LC TO WC SEND TO SITE

> ORCDLR2 CHECK ONE LC TO WC SEND TO SITE

> ORDDPAPI ADMTIME SEND TO SITE

> ORDDPAPI CLOZMSG SEND TO SITE

> ORQQPXRM MHDLL SEND TO SITE

> ORQQPXRM MHDLLDMS SEND TO SITE

> ORWCIRN VISTAWEB DELETE AT SITE

> ORWCIRN WEBCH DELETE AT SITE

> ORWDLR33 LC TO WC SEND TO SITE

> ORWDPS1 DOWSCH SEND TO SITE

> ORWDPS1 QOMEDALT SEND TO SITE

> ORWDPS1 SCHALL SEND TO SITE

> ORWDPS32 ALLIVRTE SEND TO SITE

> ORWDPS32 DLGSLCT SEND TO SITE

> ORWDPS32 DOSES SEND TO SITE

> ORWDPS32 DRUGMSG SEND TO SITE

> ORWDPS32 FORMALT SEND TO SITE

> ORWDPS32 ISSPLY SEND TO SITE

> ORWDPS32 IVAMT SEND TO SITE

> ORWDPS32 MEDISIV SEND TO SITE

> ORWDPS32 SCSTS SEND TO SITE

> ORWDPS32 VALQTY SEND TO SITE

> ORWDPS32 VALRATE SEND TO SITE

> ORWDPS32 VALSCH SEND TO SITE

> ORWDPS33 COMPLOC SEND TO SITE

> ORWDPS33 IVDOSFRM SEND TO SITE

> ORWDX LOADRSP SEND TO SITE

> ORWDX1 DCORIG SEND TO SITE

> ORWDX1 ORDMATCH SEND TO SITE

> ORWDX1 UNDCORIG SEND TO SITE

> ORWDX2 DCREASON SEND TO SITE

> ORWDXM1 BLDQRSP SEND TO SITE

> ORWDXM1 SVRPC SEND TO SITE

> ORWDXVB NURSADMN SEND TO SITE

> ORWDXVB SUBCHK SEND TO SITE

> ORWDXVB VBTNS SEND TO SITE

> ORWGRPC ALLITEMS SEND TO SITE

> ORWGRPC ALLVIEWS SEND TO SITE

> ORWGRPC CLASS SEND TO SITE

> ORWGRPC DATEITEM SEND TO SITE

> ORWGRPC DELVIEWS SEND TO SITE

> ORWGRPC DETAIL SEND TO SITE

> ORWGRPC DETAILS SEND TO SITE

> ORWGRPC FASTDATA SEND TO SITE

> ORWGRPC FASTITEM SEND TO SITE

> ORWGRPC FASTLABS SEND TO SITE

> ORWGRPC FASTTASK SEND TO SITE

> ORWGRPC GETDATES SEND TO SITE

> ORWGRPC GETPREF SEND TO SITE

> ORWGRPC GETSIZE SEND TO SITE

> ORWGRPC GETVIEWS SEND TO SITE

> ORWGRPC ITEMDATA SEND TO SITE

> ORWGRPC ITEMS SEND TO SITE

> ORWGRPC LOOKUP SEND TO SITE

> ORWGRPC PUBLIC SEND TO SITE

> ORWGRPC RPTPARAM SEND TO SITE

> ORWGRPC SETPREF SEND TO SITE

> ORWGRPC SETSIZE SEND TO SITE

> ORWGRPC SETVIEWS SEND TO SITE

> ORWGRPC TAX SEND TO SITE

> ORWGRPC TESTING SEND TO SITE

> ORWGRPC TESTSPEC SEND TO SITE

> ORWGRPC TYPES SEND TO SITE

> ORWORB AUTOUNFLAG ORDERS SEND TO SITE

> ORWPS ACTIVE SEND TO SITE

> ORWTIU GET SAVED CP FIELDS SEND TO SITE

> ORWTPP SAVESURR SEND TO SITE

> ORWU PARAMS SEND TO SITE

> ORWU2 COSIGNER SEND TO SITE

> INSTALL QUESTIONS:

> Default Rebuild Menu Trees Upon Completion of Install: NO

> Default INHIBIT LOGONs during the install: NO

> Default DISABLE Scheduled Options, Menu Options, and Protocols: NO

> REQUIRED BUILDS: ACTION:

> TIU\*1.0\*219 Don't install, leave global

> GMPL\*2.0\*35 Don't install, leave global

> PSS\*1.0\*112 Don't install, leave global

> OR\*3.0\*246 Don't install, leave global

> PSS\*1.0\*118 Don't install, leave global

> OR\*3.0\*255 Don't install, leave global

> OR\*3.0\*265 Don't install, leave global

> OR\*3.0\*254 Don't install, leave global

> OR\*3.0\*258 Don't install, leave global

> PSO\*7.0\*225 Don't install, leave global

> PSJ\*5.0\*134 Don't install, leave global

> PSS\*1.0\*94 Don't install, leave global

> YS\*5.01\*92 Don't install, leave global

> OR\*3.0\*232 Don't install, leave global

> LR\*5.2\*365 Don't install, leave global

> OR\*3.0\*275 Don't install, leave global

> WV\*1.0\*23 Don't install, leave global

> OR\*3.0\*256 Don't install, leave global

> OR\*3.0\*277 Don't install, leave global

> OR\*3.0\*245 Don't install, leave global

> XU\*8.0\*498 Don't install, leave global

> OR_PSJ_PSO_27.KID Installation Capture

> 1 Load a Distribution

> 2 Verify Checksums in Transport Global

> 3 Print Transport Global

> 4 Compare Transport Global to Current System

> 5 Backup a Transport Global

> 6 Install Package(s)

> Restart Install of Package(s)

> Unload a Distribution

> Select Installation Option: 6 Install Package(s)

> Select INSTALL NAME: OR PSJ PSO 27 1.0 Loaded from Distribution 8/6/08@12

> :42:05

> =\> CPRS27 AND REQUIRED PHARMACY PATCHES - RELEASED ;Created on Jun 18, 2

> This Distribution was loaded on Aug 06, 2008@12:42:05 with header of

> CPRS27 AND REQUIRED PHARMACY PATCHES - RELEASED ;Created on Jun 18, 2008@09:54:06

> It consisted of the following Install(s):

> OR PSJ PSO 27 1.0 PSJ\*5.0\*134 PSO\*7.0\*225 OR\*3.0\*243

> Checking Install for Package OR PSJ PSO 27 1.0

> Install Questions for OR PSJ PSO 27 1.0

> Checking Install for Package PSJ\*5.0\*134

> Install Questions for PSJ\*5.0\*134

> Incoming Files:

> 53.1 NON-VERIFIED ORDERS (Partial Definition)

> Note: You already have the 'NON-VERIFIED ORDERS' File.

> Checking Install for Package PSO\*7.0\*225

> Install Questions for PSO\*7.0\*225

> Incoming Files:

> 52 PRESCRIPTION (Partial Definition)

> Note: You already have the 'PRESCRIPTION' File.

> 52.41 PENDING OUTPATIENT ORDERS (Partial Definition)

> Note: You already have the 'PENDING OUTPATIENT ORDERS' File.

> Checking Install for Package OR\*3.0\*243

> Install Questions for OR\*3.0\*243

> Incoming Files:

> 100 ORDER (Partial Definition)

> Note: You already have the 'ORDER' File.

> 100.2 OE/RR PATIENT EVENT (Partial Definition)

> Note: You already have the 'OE/RR PATIENT EVENT' File.

> 100.21 OE/RR LIST

> Note: You already have the 'OE/RR LIST' File.

> 101.24 OE/RR REPORT (including data)

> Note: You already have the 'OE/RR REPORT' File.

> I will REPLACE your data with mine.

> 101.41 ORDER DIALOG (including data)

> Note: You already have the 'ORDER DIALOG' File.

> I will REPLACE your data with mine.

> 101.43 ORDERABLE ITEMS

> Note: You already have the 'ORDERABLE ITEMS' File.

> Want KIDS to Rebuild Menu Trees Upon Completion of Install? NO// YES

> Want KIDS to INHIBIT LOGONs during the install? NO// YES

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO// YES

> Enter options you wish to mark as 'Out Of Order': OR OE/RR MENU CLINICIAN

> CPRS Clinician Menu

> Enter options you wish to mark as 'Out Of Order': OR E OR/RR MENU NURSE

> Enter options you wish to mark as 'Out Of Order':

> Enter protocols you wish to mark as 'Out Of Order':

> Delay Install (Minutes): (0-60): 0//

> Enter the Device you want to print the Install messages.

> You can queue the install by enter a 'Q' at the device prompt.

> Enter a '^' to abort the install.

> DEVICE: HOME// TELNET TERMINAL

> Install Started for OR PSJ PSO 27 1.0 :

> Aug 06, 2008@12:45:32

> Build Distribution Date: Jun 18, 2008

> Installing Routines:

> Aug 06, 2008@12:45:32

> Install Started for PSJ\*5.0\*134 :

> Aug 06, 2008@12:45:32

> Build Distribution Date: Jun 18, 2008

> Installing Routines:

> Aug 06, 2008@12:45:32

> Installing Data Dictionaries:

> Aug 06, 2008@12:45:32

> Updating Routine file...

> The following Routines were created during this install:

> PSGXR3

> PSGXR31

> PSGXR310

> PSGXR311

> PSGXR312

> PSGXR32

> PSGXR33

> PSGXR34

> PSGXR35

> PSGXR36

> PSGXR37

> PSGXR38

> PSGXR39

> Updating KIDS files...

> PSJ\*5.0\*134 Installed.

> Aug 06, 2008@12:45:33

> Install Started for PSO\*7.0\*225 :

> Aug 06, 2008@12:45:33

> Build Distribution Date: Jun 18, 2008

> Installing Routines:

> Aug 06, 2008@12:45:33

> Installing Data Dictionaries:

> Aug 06, 2008@12:45:34

> Installing PACKAGE COMPONENTS:

> Installing PROTOCOL

> Located in the PSO (OUTPATIENT PHARMACY) namespace

> Installing LIST TEMPLATE

> Aug 06, 2008@12:45:34

> Updating Routine file...

> The following Routines were created during this install:

> PSOXZA

> PSOXZA1

> PSOXZA10

> PSOXZA11

> PSOXZA12

> PSOXZA13

> PSOXZA14

> PSOXZA2

> PSOXZA3

> PSOXZA4

> PSOXZA5

> PSOXZA6

> PSOXZA7

> PSOXZA8

> PSOXZA9

> Updating KIDS files...

> PSO\*7.0\*225 Installed.

> Aug 06, 2008@12:45:34

> Install Started for OR\*3.0\*243 :

> Aug 06, 2008@12:45:34

> Build Distribution Date: Jun 18, 2008

> Installing Routines:

> Aug 06, 2008@12:45:36

> Running Pre-Install Routine: PRE^ORY243

> Removing old data dictionaries.

> Deleting data dictionary for file \# 101.43

> Installing Data Dictionaries:

> Aug 06, 2008@12:45:39

> Installing Data: .......................................

> Aug 06, 2008@12:45:46

> Installing PACKAGE COMPONENTS:

> Installing HELP FRAME

> Installing REMOTE PROCEDURE

> Installing OPTION

> Installing PARAMETER DEFINITION:

> Aug 06, 2008@12:45:54

> Running Post-Install Routine: POST^ORY243

> Order Check Expert System Rule Transporter

> Created: NOV 2,2006 at 12:05 at CPRS27.FO-SLC.MED.VA.GOV

> Current Date: AUG 6,2008 at 12:45 at CHY1K.FO-BAYPINES.MED.VA.GOV

> Loading Data . . . . . . . . .

> Installing '863.8 OCX MDD PARAMETER' records... . .

> Installing '864.1 OCX MDD DATATYPE' records... . . .

> Installing '863.7 OCX MDD PUBLIC FUNCTION' records... .

> Installing '863.9 OCX MDD CONDITION/FUNCTION' records... .

> Installing '863.4 OCX MDD ATTRIBUTE' records... . . . .

> Installing '863.2 OCX MDD SUBJECT' records... .

> Installing '863.3 OCX MDD LINK' records... .

> Installing '860.9 ORDER CHECK NATIONAL TERM' records... . .

> Installing '860.8 ORDER CHECK COMPILER FUNCTIONS' records... .

> Installing '860.6 ORDER CHECK DATA CONTEXT' records... . . . .

> Installing '860.5 ORDER CHECK DATA SOURCE' records... . . . . .

> Installing '860.4 ORDER CHECK DATA FIELD' records...

> Installing '860.3 ORDER CHECK ELEMENT' records...

> ORDER CHECK ELEMENT: CLOZAPINE ANC \>= 1.5 & \< 2.0

> NAME: CLOZAPINE ANC \>= 1.5 & \< 2.0 ...Correct data Filed

> ELEMENT CONTEXT: CPRS ORDER PRESCAN ...Correct data Filed

> EXPRESSION SEQUENCE NUMBER: 1 ...Correct data Filed

> DATA FIELD 1: CLOZAPINE ANC W/IN 7 RESULT ...Correct data Filed

> OPERATOR/FUNCTION: GREATER THAN ...Correct data Filed

> CONDITIONAL VALUE 1: 1.499 ...Correct data Filed

> EXPRESSION SEQUENCE NUMBER: 2 ...Correct data Filed

> DATA FIELD 1: CLOZAPINE ANC W/IN 7 RESULT ...Correct data Filed

> OPERATOR/FUNCTION: LESS THAN ...Correct data Filed

> CONDITIONAL VALUE 1: 2.0 ...Correct data Filed

> EXPRESSION SEQUENCE NUMBER: 3 ...Correct data Filed

> DATA FIELD 1: CLOZAPINE ANC W/IN 7 FLAG ...Correct data Filed

> OPERATOR/FUNCTION: LOGICAL TRUE ...Correct data Filed

> Installing '860.2 ORDER CHECK RULE' records...

> ------------Missing multiple:--------------------------------------

> ORDER CHECK RULE: CLOZAPINE \[57\]

> TRUTH ELEMENTS: 1.5 \<= ANC \< 2.0 \[10\]

> TYPE: SIMPLE DEFINITION

> ELEMENT NAME: CLOZAPINE ANC \>= 1.5 & \< 2.0

> LABEL: 1.5 \<= ANC \< 2.0 ...Correct data Filed

> TYPE: SIMPLE DEFINITION ...Correct data Filed

> ELEMENT NAME: CLOZAPINE ANC \>= 1.5 & \< 2.0 ...Correct data Filed

> ------------Inconsistent Data--------------------------------------

> ORDER CHECK RULE: CLOZAPINE \[57\]

> RELATION ACTIONS: 1 \[1\]

> RELATION EXPRESSION field \[1\]

> \(R\) CPRS27.FO-SLC.MED.VA.GOV: CLOZAPINE AND (NO WBC W/IN 7 DAYS OR NO ANC W/IN 7 DAYS)

> \(L\) CHY1K.FO-BAYPINES.MED.VA.GOV: CLOZAPINE AND (WBC \< 3.0 OR ANC \< 1.5)

> RELATION EXPRESSION: CLOZAPINE AND (NO WBC W/IN 7 DAYS OR NO ANC W/IN 7 DAYS) ...Correct data Filed

> ------------Inconsistent Data--------------------------------------

> ORDER CHECK RULE: CLOZAPINE \[57\]

> RELATION ACTIONS: 1 \[1\]

> ORDER CHECK MESSAGE field \[6\]

> \(R\) CPRS27.FO-SLC.MED.VA.GOV: Clozapine orders require a CBC/Diff within past 7 days. Please order CBC/Diff with WBC and ANC immediately. Most recent results - \|CLOZ LAB RSLTS\|

> \(L\) CHY1K.FO-BAYPINES.MED.VA.GOV: WBC \< 3.0 and/or ANC \< 1.5 - pharmacy cannot fill clozapine order. Most recent results - \|CLOZ LAB RSLTS\|

> ORDER CHECK MESSAGE: Clozapine orders require a CBC/Diff within past 7 days. Please order CBC/Diff with WBC and ANC immediately. Most recent results - \|CLOZ LAB RSLTS\| ...Correct data Filed

> ------------Inconsistent Data--------------------------------------

> ORDER CHECK RULE: CLOZAPINE \[57\]

> RELATION ACTIONS: 2 \[2\]

> RELATION EXPRESSION field \[1\]

> \(R\) CPRS27.FO-SLC.MED.VA.GOV: CLOZAPINE AND (WBC \< 3.0 OR ANC \< 1.5)

> \(L\) CHY1K.FO-BAYPINES.MED.VA.GOV: CLOZAPINE AND NO WBC W/IN 7 DAYS

> RELATION EXPRESSION: CLOZAPINE AND (WBC \< 3.0 OR ANC \< 1.5) ...Correct data Filed

> ------------Inconsistent Data--------------------------------------

> ORDER CHECK RULE: CLOZAPINE \[57\]

> RELATION ACTIONS: 2 \[2\]

> ORDER CHECK MESSAGE field \[6\]

> \(R\) CPRS27.FO-SLC.MED.VA.GOV: WBC \< 3.0 and/or ANC \< 1.5 - pharmacy cannot fill clozapine order. Most recent results - \|CLOZ LAB RSLTS\|

> \(L\) CHY1K.FO-BAYPINES.MED.VA.GOV: Clozapine orders require a CBC/Diff within past 7 days. Please order CBC/Diff with WBC and ANC immediately. Most recent results - \|CLOZ LAB RSLTS\|

> ORDER CHECK MESSAGE: WBC \< 3.0 and/or ANC \< 1.5 - pharmacy cannot fill clozapine order. Most recent results - \|CLOZ LAB RSLTS\| ...Correct data Filed

> ------------Inconsistent Data--------------------------------------

> ORDER CHECK RULE: CLOZAPINE \[57\]

> RELATION ACTIONS: 3 \[3\]

> RELATION EXPRESSION field \[1\]

> \(R\) CPRS27.FO-SLC.MED.VA.GOV: CLOZAPINE AND 3.0 \<= WBC \< 3.5 AND ANC \>= 1.5

> \(L\) CHY1K.FO-BAYPINES.MED.VA.GOV: CLOZAPINE AND 3.0 \<= WBC \< 3.5 AND NO ANC W/IN 7 DAYS

> RELATION EXPRESSION: CLOZAPINE AND 3.0 \<= WBC \< 3.5 AND ANC \>= 1.5 ...Correct data Filed

> ------------Inconsistent Data--------------------------------------

> ORDER CHECK RULE: CLOZAPINE \[57\]

> RELATION ACTIONS: 3 \[3\]

> ORDER CHECK MESSAGE field \[6\]

> \(R\) CPRS27.FO-SLC.MED.VA.GOV: WBC between 3.0 and 3.5 with ANC \>= 1.5 - please repeat CBC/Diff including WBC and ANC immediately and twice weekly. Most recent results - \|CLOZ LAB RSLTS\|

> \(L\) CHY1K.FO-BAYPINES.MED.VA.GOV: \|CLOZWBC 30_35 TEXT\| Most recent results - \|CLOZ LAB RSLTS\|

> ORDER CHECK MESSAGE: WBC between 3.0 and 3.5 with ANC \>= 1.5 - please repeat CBC/Diff including WBC and ANC immediately and twice weekly. Most recent results - \|CLOZ LAB RSLTS\| ...Correct data Filed

> ------------Inconsistent Data--------------------------------------

> ORDER CHECK RULE: CLOZAPINE \[57\]

> RELATION ACTIONS: 4 \[4\]

> RELATION EXPRESSION field \[1\]

> \(R\) CPRS27.FO-SLC.MED.VA.GOV: CLOZAPINE AND 1.5 \<= ANC \< 2.0

> \(L\) CHY1K.FO-BAYPINES.MED.VA.GOV: CLOZAPINE AND 3.0 \<= WBC \< 3.5 AND ANC \>= 1.5

> RELATION EXPRESSION: CLOZAPINE AND 1.5 \<= ANC \< 2.0 ...Correct data Filed

> ------------Inconsistent Data--------------------------------------

> ORDER CHECK RULE: CLOZAPINE \[57\]

> RELATION ACTIONS: 4 \[4\]

> ORDER CHECK MESSAGE field \[6\]

> \(R\) CPRS27.FO-SLC.MED.VA.GOV: ANC between 1.5 and 2.0 - please repeat CBC/Diff including WBC and ANC immediately and twice weekly. Most recent results - \|CLOZ LAB RSLTS\|

> \(L\) CHY1K.FO-BAYPINES.MED.VA.GOV: WBC between 3.0 and 3.5 with ANC \>= 1.5 - please repeat CBC/Diff including WBC and ANC immediately and twice weekly. Most recent results - \|CLOZ LAB RSLTS\|

> ORDER CHECK MESSAGE: ANC between 1.5 and 2.0 - please repeat CBC/Diff including WBC and ANC immediately and twice weekly. Most recent results - \|CLOZ LAB RSLTS\| ...Correct data Filed

> ------------Extra multiple:----------------------------------------

> ORDER CHECK RULE: CLOZAPINE \[57\]

> RELATION ACTIONS: 5 \[5\]

> RELATION EXPRESSION: CLOZAPINE AND WBC \>= 3.5

> ORDER CHECK: CLOZAPINE APPROPRIATENESS

> ORDER CHECK MESSAGE: Clozapine - most recent results - \|CLOZ LAB RSLTS\|

> ...Correct data Filed

> No data filing errors.

> Transport Finished...

> ---Creating Order Check Routines-----------------------------------

> Build list of Active Rules, Elements and Datafields...

> 95 DATA FIELDS

> 78 ELEMENTS

> 38 RULES

> Compile DataField Navigation code...

> 100 DataField Navigation Code Arrays

> Compile Element Evaluation code...

> 72 Event Evaluation Code Arrays

> Compile Element MetaCode...

> 78 Element Metacode Arrays

> Get Compiler Function Code...

> 51 Compiler Include Functions

> Compile Rule Element Relation code...

> 54 Rule Element Relation Code Arrays

> Construct Decision Tree...

> 698 Sub-Routines

> Optimize Sub-Routines...

> 279 Sub-Routines

> 60.1% Optimization

> Assemble Routines...

> 40 OCXOZ\* Routines

> Converting Inpatient Medications Quick Orders to

> Unit Dose Medications Quick Orders.

> Delayed IV Order conversion has been queued, task number 123542

> Updating Routine file...

> The following Routines were created during this install:

> ORD2

> ORD21

> ORD210

> ORD211

> ORD212

> ORD213

> ORD214

> ORD215

> ORD216

> ORD22

> ORD23

> ORD24

> ORD25

> ORD26

> ORD27

> ORD28

> ORD29

> Updating KIDS files...

> OR\*3.0\*243 Installed.

> Aug 06, 2008@12:46:02

> Updating Routine file...

> Updating KIDS files...

> OR PSJ PSO 27 1.0 Installed.

> Aug 06, 2008@12:46:02

> Install Completed

> PSS\*1\*123 Installation Capture

> 1 Load a Distribution

> 2 Verify Checksums in Transport Global

> 3 Print Transport Global

> 4 Compare Transport Global to Current System

> 5 Backup a Transport Global

> 6 Install Package(s)

> Restart Install of Package(s)

> Unload a Distribution

> You have 6 new messages. (Last arrival: 08/06/08@12:46)

> Select Installation Option: 6 Install Package(s)

> Select INSTALL NAME: PSS,123 PSS\*1.0\*123 Loaded from Distribution 8/6/08@1

> 2:47:56

> =\> PSS\*1\*123

> This Distribution was loaded on Aug 06, 2008@12:47:56 with header of

> PSS\*1\*123

> It consisted of the following Install(s):

> PSS\*1.0\*123

> Checking Install for Package PSS\*1.0\*123

> Will first run the Environment Check Routine, PSSEC123

> Install Questions for PSS\*1.0\*123

> Incoming Files:

> 50.4 DRUG ELECTROLYTES (Partial Definition)

> Note: You already have the 'DRUG ELECTROLYTES' File.

> 52.6 IV ADDITIVES (Partial Definition)

> Note: You already have the 'IV ADDITIVES' File.

> Want KIDS to INHIBIT LOGONs during the install? NO//

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

> Enter the Device you want to print the Install messages.

> You can queue the install by enter a 'Q' at the device prompt.

> Enter a '^' to abort the install.

> DEVICE: HOME// TELNET TERMINAL

> Install Started for PSS\*1.0\*123 :

> Aug 06, 2008@12:48:14

> Build Distribution Date: Nov 06, 2007

> Installing Routines:

> Aug 06, 2008@12:48:14

> Installing Data Dictionaries:

> Aug 06, 2008@12:48:15

> Updating Routine file...

> The following Routines were created during this install:

> PSSVX6

> PSSVX61

> PSSVX62

> PSSVX63

> PSSVX64

> PSSVX65

> PSSVX66

> Updating KIDS files...

> PSS\*1.0\*123 Installed.

> Aug 06, 2008@12:48:15

Install Completed

> GMTS\*2.7\*84 Installation Capture

> 1 Load a Distribution

> 2 Verify Checksums in Transport Global

> 3 Print Transport Global

> 4 Compare Transport Global to Current System

> 5 Backup a Transport Global

> 6 Install Package(s)

> Restart Install of Package(s)

> Unload a Distribution

> Select Installation Option: 6 Install Package(s)

> Select INSTALL NAME: GMTS\*2.7\*84 Loaded from Distribution 8/6/08@12:48:54

> =\> GMTS\*2.7\*84 TEST v8

> This Distribution was loaded on Aug 06, 2008@12:48:54 with header of

> GMTS\*2.7\*84 TEST v8

> It consisted of the following Install(s):

> GMTS\*2.7\*84

> Checking Install for Package GMTS\*2.7\*84

> Install Questions for GMTS\*2.7\*84

> Want KIDS to INHIBIT LOGONs during the install? NO//

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

> Enter the Device you want to print the Install messages.

> You can queue the install by enter a 'Q' at the device prompt.

> Enter a '^' to abort the install.

> DEVICE: HOME// TELNET TERMINAL

> Install Started for GMTS\*2.7\*84 :

> Aug 06, 2008@12:49:18

> Build Distribution Date: Mar 10, 2008

> Installing Routines:

> Aug 06, 2008@12:49:18

> Updating Routine file...

> Updating KIDS files...

> GMTS\*2.7\*84 Installed.

> Aug 06, 2008@12:49:18

> Install Completed

> OR\*3\*299 Installation Capture

> 1 Load a Distribution

> 2 Verify Checksums in Transport Global

> 3 Print Transport Global

> 4 Compare Transport Global to Current System

> 5 Backup a Transport Global

> 6 Install Package(s)

> Restart Install of Package(s)

> Unload a Distribution

> Select Installation Option: 6 Install Package(s)

> Select INSTALL NAME: OR,299 OR\*3.0\*299 Loaded from Distribution 8/6/08@12:

> 49:44

> =\> OR\*3\*299

> This Distribution was loaded on Aug 06, 2008@12:49:44 with header of

> OR\*3\*299

> It consisted of the following Install(s):

> OR\*3.0\*299

> Checking Install for Package OR\*3.0\*299

> Install Questions for OR\*3.0\*299

> Want KIDS to INHIBIT LOGONs during the install? NO//

> Want to DISABLE Scheduled Options, Menu Options, and Protocols? NO//

> Enter the Device you want to print the Install messages.

> You can queue the install by enter a 'Q' at the device prompt.

> Enter a '^' to abort the install.

> DEVICE: HOME// TELNET TERMINAL

> Install Started for OR\*3.0\*299 :

> Aug 06, 2008@12:50:01

> Build Distribution Date: Aug 01, 2008

> Installing Routines:

> Aug 06, 2008@12:50:02

> Running Post-Install Routine: EN1^ORY299

> Requested Start Time: NOW// (AUG 06, 2008@12:50:05)

> The check for truncated Patient Instructions is queued

> (to start NOW).

> YOU WILL RECEIVE A MAILMAN MESSAGE WHEN TASK \#123543 HAS COMPLETED.

> Updating Routine file...

> Updating KIDS files...

> OR\*3.0\*299 Installed.

> Aug 06, 2008@12:50:05

> Install Completed