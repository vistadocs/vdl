---
title: Patient Care Encounter Version 1 Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: 
app_code: PX
app_name: Patient Care Encounter (PCE)
section: CLI
app_status: active
pkg_ns: PX
patch_ver: 1
patch_id: PX*1
group_key: "PX:PX:1"
file_numbers: []
security_keys: []
menu_options: 0
description: - [Namespaces](#namespaces) - [Resource Requirements](#resource-requirements) - [Required or Recommended Software to be installed before PCE](#required-or-recommended-software-to-be-installed-before-pce) - [## Global Maximum Limit](#global-maximum-limit) - [Global List](#global-list) - [Files Instal
audience: 
keywords: 
  - encounter
  - patient
  - visit
  - pxce
  - care
  - install
  - tracking
  - global
  - installation
  - located
page_count: 0
word_count: 11125
section_count: 15
table_count: 27
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: 
revision_count: 1
revision_newest: 11/19/04
revision_oldest: 11/19/04
docx_url: "https://www.va.gov/vdl/documents/Clinical/Patient_Care_Encounter_(PCE)/pxig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Patient_Care_Encounter_(PCE)/pxig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=82"
---

## Table of Contents

  - [Namespaces](#namespaces)
  - [Resource Requirements](#resource-requirements)
  - [Required or Recommended Software to be installed before PCE](#required-or-recommended-software-to-be-installed-before-pce)
  - [## Global Maximum Limit](#global-maximum-limit)
  - [Global List](#global-list)
  - [Files Installed by PCE](#files-installed-by-pce)
  - [Routines Installed with this Version (four builds):](#routines-installed-with-this-version-four-builds)
  - [Special considerations](#special-considerations)
  - [Orient MAS Users](#orient-mas-users)
  - [Recommended time for installation](#recommended-time-for-installation)
  - [Scanned encounter form data](#scanned-encounter-form-data)
  - [Estimated Installation Time](#estimated-installation-time)
  - [Dispositions](#dispositions)
  - [Checkout Interview](#checkout-interview)
Patient Care Encounter (PCE)V. 1.0 Installation GuideAugust 1996Introduction
> Related Manuals
Installation and Implementation ChecklistPre-Installation
> Namespaces
> Resource Requirements
> Required/Recommended Software to be Installed before PCE
> Global Maximum Limit
> Global List
> Files Installed by PCE
> Routines Installed
> Special Considerations
> Recommended Time for Installation
> Scanned Encounter Form Data
> Estimated Installation Time
Installation InstructionsPost-Installation-PCE and Visit Tracking Set-upAppendix A - Visit Creation Activation LevelsAppendix B - Orientation of MAS Staff to PCE  
Revision History
Initiated on 11/19/04
|          |                                                                     |                 |                                    |
|----------|---------------------------------------------------------------------|-----------------|------------------------------------|
| Date     | Description (Patch \# if applic.)                                   | Project Manager | Technical Writer                   |
| 11/19/04 | Manual updated to comply with SOP 192-352 Displaying Sensitive Data |                 | <span class="mark">REDACTED</span> |
|          |                                                                     |                 |                                    |
|          |                                                                     |                 |                                    |
|          |                                                                     |                 |                                    |
|          |                                                                     |                 |                                    |
|          |                                                                     |                 |                                    |
|          |                                                                     |                 |                                    |
|          |                                                                     |                 |                                    |
|          |                                                                     |                 |                                    |
|          |                                                                     |                 |                                    |
Introduction
Patient Care Encounter (PCE) V. 1.0 facilitates the collection, management, and display of outpatient encounter data, including providers, procedure codes, and diagnostic codes, in compliance with the October 1, 1996 mandate from the Undersecretary of Health. PCE also enables the documentation of patient education, examinations, treatments, skin tests, and immunizations, as well as the collection and management of other clinically significant data, including the defining of Health Factors and Health Maintenance Reminders to be displayed on Health Summaries. Other summary reports relating to encounters can be generated through PCE.
Visit Tracking V. 2.0 is a utility which enables the creation, editing, and deletion of encounters in the Visit file (9000010). Visit Tracking can be used by a variety of DHCP modules, with potential benefits for clinical, administrative, and fiscal applications. It allows DHCP to link patient encounter-related data across DHCP packages to an entry in the Visit file.
The *Patient Care Encounter (PCE)/Visit Tracking Installation Guide* is designed to provide VAMC IRM staff with the necessary technical information to install, set up, and maintain the PCE/Visit Tracking package.
Related Manuals
*Patient Care Encounter V. 1.0 User ManualPatient Care Encounter V. 1.0 Technical ManualAutomated Information Collection System (AICS) User ManualHealth Summary V. 2.7 User Manual*
Installation and Implementation Checklist
> **NOTE:** This checklist outlines the steps for installing and implementing PCE and Visit Tracking to give you an overview and a checklist to work with. Be sure to read the more detailed instructions that follow in this manual, as well as in the *Patient Care Encounter Technical* and *User Manuals.Pre-installation*
- 1. Namespaces
  PCE: PX
  Visit Tracking: VSIT
- 2. Ensure that you have adequate Resource Requirements.
MSM SITES: Increase your Stack/Stap to 24k to avoid STKOV errors, and the size of your partitions to 85k for selected options to avoid PGMOV errors.
DSM SITES: Expand string length for data and global references to accommodate Standards and Conventions (SAC) 2.3.2.2 which extends the full evaluated length of a global reference to 200 characters. (Some sites have elected to perform these steps only for the ^TMP and ^XTMP globals, since those are the only globals for which PCE is known to require expanded strings and subscripts.)
- 3. Make sure the required DHCP software packages are installed before you install PCE/Visit Tracking.
- 4. Check your maximum global limit for the volume set. It must be able to accommodate the addition of 20 new globals. On Alphas, use the ^VOLMAN utility from the MGR UCI.
- 5. Ensure proper global protection. To avoid protection errors, set the global protection for ^APPPCTRL( to READ, WRITE, and PURGE/DELETE. (This only applies to sites who have already installed PCE Patient/IHS Subset (PXPT).)
- 6. Review files to be installed.
- 7. Review routines to be installed.
- 8. Note post-installation processes regarding the VISIT TRACKING PARAMETERS file and routines included from other packages (AUPN from IHS, Health Summary patch \#8, and SD-name spaced routines from patch 27 of Scheduling v. 5.3).
- 9. We recommend that you install PCE/Visit Tracking first in a training or test account. Orient your MAS users to the differences they will see in options as a result of PCE/Scheduling integration (See Appendix B for details). Make sure all of the set-up works as intended before you install into production.
- 10. Install PCE on a weekend or evening when clinic activity is minimal to avoid visit creation and database errors during installation. Do a full back up on your system.
- 11. Ensure that no scanned encounter form data is being uploaded into PCE during the installation.
- 12. It takes approximately 15 minutes to install PCE on either MSM or DSM systems.
  *Installation*
- 13. Delete routines: PX\* and VSIT\*
- 14. Verify that DUZ ("AG"), DT, DTIME , and U are defined, and DUZ(0)=“@”.
- 15. Do ^XUP and select the Kernel Installation & Distribution System.
- 16. Select the Installation menu option, then select the Load a Distribution option. At the prompt "Enter a Host File:" enter the directory and the filename PX1_0.KID.
- 17. Run the option "Verify Checksums in Transport Global" to verify that all routines have the correct checksum. If there are any discrepancies, do not run the Install Package(s) option. Instead, run the Unload a Distribution option to remove the Transport Global from your system. Call your IRM Field Office and report the problem.
- 18. From the Installation Menu of the KIDS menu, run the option "Install Package(s)." Select the package 'VISIT' and proceed with install.
- 19. On a mapped system, rebuild your map set.
- 20. Move routines to all systems, as appropriate.
- 21. Enable journaling for PCE and Visit Tracking globals.
- 22. Use the KIDS Build File Print option if you would like a complete listing of package components (e.g., routines and options) exported with this software.
- 23. Use the KIDS Install File Print option if you'd like to print out the results of the installation process.
*Post-installation*
- 24. Use the Visit Tracking Parameters Edit option to ensure that the entries in the VISIT TRACKING PARAMETERS file (150.9) are correct.
- 25. Set PCE Site Parameters through the PCE Site Parameters option on the PCE Site Parameters Menu.
- 26. Make sure that new Scheduling, Integrated Billing, PCE, and Visit Tracking EVENTS are on the appropriate ITEM protocols.
- 27. Assign PCE menu and options.
- 28. Set up a clinic for use with Dispositions. Define the Disposition Clinic in the PCE Parameters file (8.5).
- 29. Review entries contained in PCE Supporting Files. Entries in each of the supporting files should be evaluated and assigned an appropriate status through the “Activate/Inactivate Table Items” option.
- 30. Edit the report parameters using the *PCE Report Parameter Edit* option.
- 31. Create PXCA PCE ERROR BULLETIN as a mail group in MAIL GROUP file (#3.8).
- 32. Create VSIT CREATE ERROR as a mail group in MAIL GROUP file (#3.8).
- 33. Activate PCE components in the Health Summary Component file.
- 34. Implement the PCE Reminder/Maintenance items to appear on Health Summaries for each clinic. Also coordinate these with the Encounter Form designs for each clinic.
- 35. (optional) Add Health Summary, Problem List, and Progress Notes as actions on PCE screens to allow quick access to those programs while using PCE.
Pre-Installation

## Namespaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patient Care Encounter: PX

Visit Tracking Namespace: VSIT

## Resource Requirements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patient Care Encounter is used as a clinical repository for data from many sources, including scanning devices such as PANDAS and TELEFORM, the Automated Information Collection System (AICS), the Graphical User Interface (GUI) physician workstation, and manual data entry options in Scheduling and PCE.

The table below lists estimated disk space requirements for PCE/Visit Tracking for four levels of facility complexity. Estimates are based on adding 83k to the database for every 100 encounters, where each encounter averages two procedures, one diagnosis, and one provider. Each visit averages 1.9 encounters, based on stop code reporting per visit transmitted to Austin.

|                      |                                          |                                            |
|----------------------|------------------------------------------|--------------------------------------------|
| Complexity Level | Average \# of Ambulatory Visits/Year | Estimated Disk Space Requirements/Year |
| 1                    | 254,018                                  | 400mb                                      |
| 2                    | 149,101                                  | 234mb                                      |
| 3                    | 92,761                                   | 146mb                                      |
| 4                    | 71,371                                   | 112mb                                      |

MSM SITES: Increase your Stack/Stap to 24k to avoid STKOV errors.

To avoid PGMOV errors, add an entry and exit action to dynamically increase/decrease the partition size for the following options:

Appointment Management \[SDAM APPT MGT\]

Appointment Check-in/Check-out \[SDAM APPT CHECK IN/OUT\]

Add/Edit Stop Codes \[SDADDEDIT\]

Check-in/Unsched. Vsit \[SDI\]

Make Appointment \[SDM\]

Multiple Appointment Booking \[SDMULTIBOOK\]

Disposition an Application \[DG DISPOSITION APPLICATION\]

Disposition Log Edit \[DG DISPOSITION EDIT\]

Entry action: S %K=85 D INT^%PARTSIZ

Exit action: S %K=40 D INT^%PARTSIZDSM SITES: Expand string length for data and global references to accommodate Standards and Conventions (SAC) 2.3.2.2 which extends the full evaluated length of a global reference to 200 characters. (Some sites have elected to perform these steps only for the ^TMP and ^XTMP globals, since those are the only globals for which PCE is known to require expanded strings and subscripts.)

Since the current default for maximum global reference length is 128 for DSM sites, do the following:

What UCI: MGR

YOU'RE IN UCI: MGR,DEV

\>D ^VOLMAN

Volume Management Utilities

1\. ADD (ADD^VOLMAN)

2\. CREATE (CREATE^VOLMAN)

3\. EXTEND (EXTEND^VOLMAN)

4\. MAXIMUM GLOBALS (MAXGLO^VOLMAN2)

5\. STRING LENGTH (EXPSTR^VOLMAN2)

Select Option \> 5. STRING LENGTH

Volume Set to set EXPANDED STRING LENGTH flag for \> ^TMP

Expanded string length for data and global references is currently DISALLOWED on this Volume Set:

255 bytes is the maximum data length, and

128 bytes is the maximum global reference length.

When you enable expanded strings and global references on a Volume Set, then:

512 bytes is the maximum data length, and

249 bytes is the maximum global reference length.

\*\*\* WARNING \*\*\* Once you have enabled a Volume Set for use with expanded strings and subscripts, that flag may NOT be reset.

Allow expanded string lengths on Volume Set ^TMP \[Y OR N\] ? \<N\> Y

Expanded string length is now ENABLED on Volume Set ^TMP.

> **NOTE:** The new settings will not take effect until the DSM configuration is shut down and re-started on all nodes. Consult your DSM manuals for more information.

## Required or Recommended Software to be installed before PCE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 28%" />
<col style="width: 17%" />
<col style="width: 26%" />
<col style="width: 0%" />
<col style="width: 27%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Package</strong></td>
<td><strong>Minimum Version</strong></td>
<td colspan="2"><strong>Required or Recommended</strong></td>
<td><strong>Comments</strong></td>
</tr>
<tr class="even">
<td>Kernel</td>
<td>8.0</td>
<td>Required</td>
<td colspan="2">The NEW PERSON File Patch, XU*8*27, may also be installed prior to PCE.</td>
</tr>
<tr class="odd">
<td>VA FileMan</td>
<td>21</td>
<td>Required</td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td>Patient Information Management System (PIMS)</td>
<td>5.3</td>
<td>Required</td>
<td colspan="2">Completely patched.</td>
</tr>
<tr class="odd">
<td>Order Entry/Results Reporting (OE/RR)</td>
<td>2.5</td>
<td>Required</td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td>Automated Information Collection System (AICS)</td>
<td>2.1</td>
<td>Required</td>
<td colspan="2">Completely patched.</td>
</tr>
<tr class="odd">
<td>Health Summary</td>
<td>2.7</td>
<td>Recommended</td>
<td colspan="2"><p>Completely patched (including patch GMTS*2.7*8).</p>
<p>You must have version 2.7 to use PCE components.</p></td>
</tr>
<tr class="even">
<td>Problem List</td>
<td>2.0</td>
<td>Recommended</td>
<td colspan="2">If you want to link diagnoses to problems, or to populate Problem List from encounter forms.</td>
</tr>
<tr class="odd">
<td>Clinical Lexicon</td>
<td>1.0</td>
<td>Recommended</td>
<td colspan="2">For use with Problem List.</td>
</tr>
<tr class="even">
<td>PCE Patient/IHS Subset (PXPT)</td>
<td>1.0</td>
<td>Required</td>
<td colspan="2">PXPT's tasked job to synchronize the Patient file (2) with the Patient/IHS file (9000001) must be finished before you install PCE/Visit Tracking.</td>
</tr>
</tbody>
</table>

## ## Global Maximum Limit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Twenty new globals are added to your system as a result of this install. Check your maximum global limit for the volume set. It must be able to accommodate the addition of 20 new globals. On Alphas, use the ^VOLMAN utility from the MGR UCI.

## Global List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Below are lists of globals that will be installed and which MUST have proper global protection. To avoid protection errors, set the global protection for ^APPPCTRL( to READ, WRITE, and PURGE/DELETE. (This only applies to sites who have already installed PCE Patient/IHS Subset (PXPT).)

*Alpha cluster configuration (DSM)*: the PCE and Visit Tracking Globals must be set and protected on the proper volume set using the %GLOMAN utility.

*486 configurations (MSM)*: use the %GCH system utility to create and change globals and their attributes.

Each new global will need to have the global root set manually equal to null (S ^AUPNVSIT="").

On both Alpha, and 486 systems, all globals should be defined as follows for the install:

|                 |            |           |           |              |
|-----------------|------------|-----------|-----------|--------------|
|                 | System | World | Group | UCI/USER |
| Alpha (DSM) | RWP        | RWP       | RWP       | RWP          |
| (MSM)       | RWD        | RWD       | RWD       | RWD          |

JournalingMSM: should be enabled for all globals after the install is completed.

DSM: should be enabled for globals, as noted in the global lists on the next pages, after the install is completed.

## Files Installed by PCE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The IHS/VA joint-sharing files installed by PCE include:

*Visit Tracking*

|                           |             |              |                     |                |
|---------------------------|-------------|--------------|---------------------|----------------|
| File Name             | File \# | Global   | Data            | Journaling |
| Visit                     | 9000010     | ^AUPNVSIT(   | NO                  | ON             |
| Ancillary DSS ID          | 150.1       | ^VSIT(150.1, | YES                 |                |
| Visit Site Codes          | 150.2       | ^VSIT(150.2, | YES                 |                |
| Visit Tracking Parameters | 150.9       | ^DIC(150.9   | Set in post-install |                |

*  
PCE*

|                                     |             |              |          |                |
|-------------------------------------|-------------|--------------|----------|----------------|
| File Name                       | File \# | Global   | Data | Journaling |
| PCE Code Mapping                    | 811.1       | ^PXD(811.1,  | YES      |                |
| PCE Taxonomy                        | 811.2       | ^PXD(811.2,  | YES      |                |
| PCE Reminder Type                   | 811.8       | ^PXD(811.8,  | YES      |                |
| PCE Reminder/ Maintenance Item      | 811.9       | ^PXD(811.9,  | YES      |                |
| PCE Parameters                      | 815         | ^PX(815,     | YES      |                |
| PXCA Device Interface Module Errors | 839.01      | ^ PX(839.01, | NO       | ON             |
| Data Source                         | 839.7       | ^ PX(839.7,  | YES      |                |
| Patient/IHS                         | 9000001     | ^AUPNPAT(    | NO       | ON             |
| V Provider                          | 9000010.06  | ^AUPNVPRV(   | NO       | ON             |
| V POV                               | 9000010.07  | ^AUPNVPOV(   | NO       | ON             |
| V Immunization                      | 9000010.11  | ^AUPNVIMM(   | NO       | ON             |
| V Skin Test                         | 9000010.12  | ^AUPNVSK(    | NO       | ON             |
| V Exam                              | 9000010.13  | ^AUPNVXAM(   | NO       | ON             |
| V Treatment                         | 9000010.15  | ^AUPNVTRT(   | NO       | ON             |
| V Patient Ed                        | 9000010.16  | ^AUPNVPED(   | NO       | ON             |
| V CPT                               | 9000010.18  | ^AUPNVCPT(   | NO       | ON             |
| V Health Factors                    | 9000010.23  | ^AUPNVHF(    | NO       | ON             |
| Location                            | 9999999.06  | ^AUTTLOC(    | NO       |                |
| Education Topics                    | 9999999.09  | ^AUTTEDT(    | YES      | ON             |
| Immunization                        | 9999999.14  | ^AUTTIMM(    | YES      |                |
| Exam                                | 9999999.15  | ^AUTTEXAM(   | YES      |                |
| Treatment                           | 9999999.17  | ^AUTTTRT(    | YES      |                |
| Provider Narrative                  | 9999999.27  | ^AUTNPOV(    | NO       | ON             |
| Skin Test                           | 9999999.28  | ^AUTTSK(     | YES      |                |
| Health Factors                      | 9999999.64  | ^AUTTHF(     | YES      | ON             |

> **NOTE:** Sites using Kernel Part 3 (optional) need to set user access to these files. See the Security section of the *PCE Technical Manual* for information.

Other DHCP files used by Patient Care Encounter (PCE):

|                          |             |             |                                       |
|--------------------------|-------------|-------------|---------------------------------------|
| File Name            | File \# | Global  | Comment                           |
| Eligibility              | 8           | ^DIC(8      |                                       |
| New Person               | 200         | ^VA(200     |                                       |
| Clinic Stop              | 40.7        | ^DIC(40.7   |                                       |
| Hospital Location        | 44          | ^SC(        |                                       |
| Expressions              | 757.01      | ^GMP(757.01 | Clinical Lexicon install not required |
| ICD Diagnosis            | 80          | ^ICD9(      |                                       |
| ICD Operation/ Procedure | 80.1        | ^ICD0(      |                                       |
| Problem                  | 9000011     | ^AUPNPROB(  | Problem List not required             |
| Patient                  | 2           | ^DPT(       |                                       |
| CPT                      | 81          | ^ICPT(      |                                       |

## Routines Installed with this Version (four builds):

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*PCE Build*

AUPNPAT AUPNSICD AUTNPOV IBDFPCE PXAI PXAICPT PXAICPTV

PXAIHF PXAIHFV PXAIIMM PXAIIMMV PXAIPED PXAIPEDV PXAIPL

PXAIPOV PXAIPOVV PXAIPRV PXAIPRVV PXAISK PXAISKV PXAIUPRV

PXAIVST PXAIVSTV PXAIXAM PXAIXAMV PXAPI PXAPIDEL PXAPIEED

PXAPIIB PXAPIUTL PXBAICS PXBAPI PXBAPI1 PXBAPI2 PXBAPI21

PXBAPI22 PXBCC PXBDCPT PXBDPL PXBDPOV PXBDPRV PXBDREQ

PXBDSTP PXBDVST PXBGCPT PXBGCPT2 PXBGCPT4 PXBGHF PXBGIMM

PXBGPED PXBGPL PXBGPL2 PXBGPOV PXBGPOV2 PXBGPOV3 PXBGPOV4

PXBGPRV PXBGPRV2 PXBGPRV3 PXBGPRV4 PXBGSK PXBGSTP PXBGSTP2

PXBGVST PXBGXAM PXBHLP0 PXBHLP1 PXBHLP2 PXBHLP3 PXBHLP4

PXBHLPR PXBMCPT PXBMCPT2 PXBMPOV PXBMPRV PXBMSTP PXBPCPT

PXBPCPT1 PXBPL PXBPPOV PXBPPOV1 PXBPPRV PXBPPRV1 PXBPQUA

PXBPSTP PXBPSTP1 PXBPVST PXBPWCH PXBSTOR PXBSTOR1 PXBUTL

PXBUTL0 PXBUTL1 PXBUTL2 PXBUTL3 PXCA PXCA0 PXCACPT

PXCACPT1 PXCADX PXCADXP1 PXCADXP2 PXCADXPL PXBPVST PXBPWCH

PXBSTOR PXBSTOR1 PXBUTL PXBUTL0 PXBUTL1 PXBUTL2 PXBUTL3

PXCA PXCA0 PXCACPT PXCACPT1 PXCADX PXCADXP1 PXCADXP2

PXCADXPL PXCAERR PXCAHF PXCAPED PXCAPL PXCAPL1 PXCAPL2

PXCAPOV PXCAPOV1 PXCAPRV PXCASK PXCASOR PXCATRT PXCAVIMM

PXCAVST PXCAVST1 PXCAVST2 PXCAXAM PXCE PXCEAE PXCEAE1

PXCEAE2 PXCEAPPM PXCECPT PXCECSTP PXCEDATE PXCEE800 PXCEEXP

PXCEHELP PXCEHF PXCEHIST PXCEHLOC PXCEINTR PXCENEW PXCEPAT

PXCEPED PXCEPOV PXCEPOV1 PXCEPRV PXCESDA1 PXCESDA3 PXCESDAM

PXCESIT PXCESK PXCETRT PXCEVFI1 PXCEVFI2 PXCEVFI4 PXCEVFI5

PXCEVFIL PXCEVIMM PXCEVSIT PXCEVST PXCEXAM PXEDIEL PXEDIELU

PXEDILUD PXEDIM PXEDIP PXIPENV PXIPOST PXIPOST1 PXIPREI

PXKCO PXKCO1 PXKCOC PXKCOC1 PXKCODX PXKCODX1 PXKCOP

PXKCOV PXKCOV1 PXKENC PXKFCPT PXKFCPT1 PXKFHF PXKFIMM

PXKFIMM1 PXKFPED PXKFPOV PXKFPRV PXKFSK PXKFSK1 PXKFTRT

PXKFVST PXKFXAM PXKMAIN PXKMAIN1 PXKMAIN2 PXKMASC PXKMASC1

PXKVST PXNTEG PXNTEG0 PXPT PXPTPOST PXRHS01 PXRHS02

PXRHS03 PXRHS04 PXRHS05 PXRHS06 PXRHS07 PXRHS08 PXRHS12

PXRHS13 PXRHS14 PXRM PXRMAFOP PXRMAGE PXRMCF PXRMCFOP

PXRMCODE PXRMDATE PXRMDEV PXRMDGOP PXRMDGPT PXRMDISC PXRMEDIT

PXRMEDU PXRMEXAM PXRMFOUT PXRMHF PXRMHFOP PXRMICD9 PXRMIMM

PXRMLAB PXRMLOG PXRMMEAS PXRMOBES PXRMPINF PXRMPROB PXRMPROC

PXRMPROP PXRMPT PXRMRAD PXRMRAOP PXRMREDT PXRMRINQ PXRMSKIN

PXRMSTDC PXRMTAXP PXRMTEDT PXRMTF PXRMTFOP PXRMTGOP PXRMTP

PXRMTPA PXRMTYPE PXRMUNIQ PXRMUTIL PXRMVCOP PXRMVCPT PXRMVPOP

PXRMVPOV PXRMWCHK PXRRADUT PXRRECQ PXRRECSE PXRRFDD PXRRFDP

PXRRFDQ PXRRFDSD PXRRFDSE PXRRGPRT PXRRGUT PXRRLCCP PXRRLCD

PXRRLCHP PXRRPCE PXRRPCE1 PXRRPCE2 PXRRPCE3 PXRRPCE4 PXRRPCE5

PXRRPCEQ PXRRPCR PXRRPCR1 PXRRPCR2 PXRRPCR3 PXRRPCR4 PXRRPRD

PXRRPRDP PXRRPRPL PXRRPRSP PXRRSC PXSCH1 PXSCH2 PXSCH3

PXSCH4 PXTTEDC PXTTEDE PXTTEDQ PXTTU1 PXUTL1 PXUTLSCC

PXUTLSTP PXUTLVST PXXDPT

*  
Visit Tracking 2.0 Build*

AUPNVSIT VSIT VSIT0 VSITASK VSITBUL VSITCK VSITCK1 VSITDEF

VSITFLD VSITGET VSITHLP VSITIENV VSITIPOS VSITIPRE VSITKIL

VSITNTEG VSITOE VSITPUT VSITPUT1 VSITSTAT VSITVAR VSITVID

*Scheduling Patch 27 Build*

SDACS SDAMBAE SDAMBAE5 SDAMBAE6 SDAMEX1 SDAPI SDAPIAE

SDAPIAE0 SDAPIAE1 SDAPIAP SDAPICO SDAPICO1 SDAPIDP SDAPIER SDCO

SDCO1 SDCO2 SDCO3 SDCO4 SDCO5 SDCO6 SDCO9 SDCOAM

SDCODEL SDPARM SDPARM1 SDPARM2 SDPCE SDPCE0 SDPCE1 SDPCE2

SDSTP SDSTP2 SDSTP3 SDVSIT SDVSIT0 SDVSIT2 SDYDPOST SDYDPRE

*Health Summary Patch GMTS\*2.7\*8 Build*

GMTSP8 GMTSPXEP GMTSPXFP GMTSPXHR GMTSPXIM GMTSPXOP GMTSPXSK GMTSPXTP

GMTSPXXP GMTSVS GMTSVSS

## Special considerations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- A post-installation routine adds a default institution entry to the VISIT TRACKING PARAMETERS file (150.9).
- The post-installation process also checks to see if the VISIT TRACKING PARAMETERS file (150.9) has an entry. If not, it will configure it with default values. Review the Visit Tracking site parameters by using the Visit Tracking Parameters Edit option (See the PCE/Visit Tracking Setup section).
- The PCE and Visit Tracking packages export four AUPN prefix name spaced routines used within data dictionaries of the AUPN-prefixed globals: AUPNPAT, AUPNSICD, AUPNVSIT, and AUPNPOV.
- Sites must pick a date to begin using new Scheduling Checkout Interview prompts. This date has to be between the day after installation and October 1, 1996.
- Patch GMTS\*2.7\*8 is exported with PCE. This patch contains routines which accommodate Health Maintenance Reminder items and Clinical Reminder components in Health Summary v. 2.7.
- The SD-name spaced routines exported by PCE comprise patch 27 of Scheduling v. 5.3. These routines are required to support the integration of PCE and Scheduling functionality.

## Orient MAS Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Orient your MAS users to changes in Appointment Manager and Disposition functionality. See Appendix B for details.

## Recommended time for installation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

We recommend that you install PCE/Visit Tracking on a weekend or evening when clinic activity is minimal, to avoid visit creation and database errors. It is not necessary to take users off the system, but you should do a full back-up before installing. You may want to disable specified options during the installation.

## Scanned encounter form data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Ensure that no scanned form data is being uploaded into PCE during the installation.

## Estimated Installation Time

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

It takes approximately 15 minutes to install PCE/Visit Tracking on either MSM or DSM systems.

  
Installation Instructions

We recommend that you install PCE/Visit Tracking first in a training or test account. Orient your MAS users to the differences they will see in options as a result of PCE/Scheduling integration. Make sure all of the set-up works as intended and your users are familiar with the changes before you install into production.

13. Delete PX\* and VSIT\* routines:
14. Verify that DUZ ("AG"), DT, DTIME , and U are defined, and DUZ(0)=“@”.

Installation. PCE uses the KIDS utility to install its routines, files, and data. We don't recommend tasking this install because the post-install steps must be done before PCE and Scheduling will work.

15. Do ^XUP and select the Kernel Installation & Distribution System.

\>D ^XUP

Setting up programmer environment

Access Code:

Terminal Type set to: C-VT100

Select OPTION NAME: KERNEL INSTALLATION & DISTRIBUTION XPD MAIN Kernel Installation & Distribution System

Edits and Distribution ...

Utilities ...

Installation ...

Select Installation & Distribution System Option: Installation16. Select the Installation menu option, then select the Load a Distribution option. At the prompt "Enter a Host File:" enter your directory name and the filename PX1_0.KID.

Select Installation & Distribution System Option: Installation

Load a Distribution

Print Transport Global

Compare Transport Global to Current System

Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Backup a Transport Global

Select Installation Option: L Load a DistributionEnter a Host File: (*directory name*)PX1_0.KID

  
17. Run the option "Verify Checksums in Transport Global" to verify that all routines have the correct checksum. If there are any discrepancies, do not run the Install Package(s) option. Instead, run the Unload a Distribution option to remove the Transport Global from your system. Call your IRM Field Office and report the problem.
18. From the Installation Menu on the KIDS menu, run the option "Install Package(s)." Select the package 'VISIT TRACKING 2.0' and proceed with the install.

If the installation aborts, run the Unload a Distribution option to remove the Transport Global from your system. Enter the name of each package separately when prompted for package name (i.e., Visit Tracking, PCE, Scheduling, etc.). Call your IRM Field Office and report the problem.

Select Installation & Distribution System Option: Installation

Load a Distribution

Print Transport Global

Compare Transport Global to Current System

Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Backup a Transport Global

Select Installation Option: INSTALL PACKAGE(S)

Select INSTALL NAME: VISIT TRACKING 2.0

When asked if you wish to disable options, disable PIMS options which allow editing of data stored in PCE files and PCE Data Entry options.

*PIMS options*

|                                                           |                                                        |
|-----------------------------------------------------------|--------------------------------------------------------|
| Option Name                                           | Option Text                                        |
| DG ADMIT PATIENT                                          | Admit a Patient                                        |
| SDAM APPT MGT                                             | Appointment Management                                 |
| SDAM APPT CHECK IN/OUT                                    | Appointment Check-in/Check-out                         |
| SD CANCEL APPOINTMENT                                     | Cancel Appointment                                     |
| SDI                                                       | Check-in/Unsched. Visit                                |
| SDAPPEND                                                  | Append Ancillary Test for Appt. Appointment Management |
| DG DISPOSITION APPLICATION Appointment Check-in/Check-out | Disposition an Application Cancel Appointment          |
| DG DISPOSITION EDIT                                       | Disposition Log Edit                                   |
| SDM                                                       | Make Appointment                                       |
| SD MULTIBOOK                                              | Multiple Appointment Booking                           |

*PCE data entry options*

|                                |                                         |
|--------------------------------|-----------------------------------------|
| Option Name                | Option Text                         |
| PXCE ENCOUNTER DATA ENTRY      | PCE Encounter Data Entry                |
| PXCE ENCOUNTER ENTRY SUPER     | PCE Encounter Data Entry - Supervisor   |
| PXCE ENCOUNTER ENTRY & DELETE  | PCE Encounter Data Entry and Delete     |
| PXCE ENCOUNTER ENTRY NO DELETE | PCE Encounter Data Entry without Delete |

19. On a mapped system, rebuild your map set. If you map scheduling, we suggest you map the following routines also:

AUPNVSIT PXAPI PXB\* PXK\* VSIT0 VSITCK VSITCK1

VSITDEF VSITFLD VSITGET VSITKIL VSITPUT VSITPUT1 VSITSTAT

VSITVAR VSITVID

20. Move PX\*, AU\*, and VSIT\*, and the GMTS, IB, and SD routines listed below to appropriate systems, according to your local configurations.

GMTSP8 GMTSPXEP GMTSPXFP GMTSPXHR GMTSPXIM GMTSPXOP GMTSPXSK

GMTSPXTP GMTSPXXP GMTSVS GMTSVSS IBDFPCE SDACS SDAMBAE

SDAMBAE5 SDAMBAE6 SDAMEX1 SDAPI SDAPIAE SDAPIAE0 SDAPIAE1

SDAPIAP SDAPICO SDAPICO1 SDAPIDP SDAPIER SDCO SDCO1 SDCO2

SDCO3 SDCO4 SDCO5 SDCO6 SDCO9 SDCOAM SDCODEL SDPARM

SDPARM1 SDPARM2 SDPCE SDPCE0 SDPCE1 SDPCE2 SDSTP SDSTP2

SDSTP3 SDVSIT SDVSIT0 SDVSIT2 SDYDPOST SDYDPRE

21. Enable journaling for PCE and Visit Tracking globals.

See the global list in the pre-installation information for files using these globals:

^AUPNVSIT ^AUPNVPRV ^AUPNVPOV ^AUPNVIMM ^AUPNVSK ^AUPNVXAM ^AUPNVTRT

^AUPNVPED ^AUPNVCPT ^AUPNVHF ^AUTTEDT ^AUTTHF ^PX

22. Use the KIDS Build File Print option if you would like a complete listing of package components (e.g., routines and options) exported with this software. You will need to print each build exported with PCE.
23. Use the KIDS Install File Print option if you'd like to print out the results of the installation process.

  
*Installation Capture ExampleThis capture reflects an installation of PCE/VT/SD/HS into an account in which no previous version existed.*

\>ZW DUZ

DUZ=2

DUZ(0)=@

DUZ(1)=

DUZ(2)=660

DUZ("AG")=V

DUZ("BUF")=1

DUZ("LANG")=

\>D ^XUP

Setting up programmer environment

Terminal Type set to: C-VT220

Select OPTION NAME: XPD MAIN Kernel Installation & Distribution System

Edits and Distribution ...

Utilities ...

Installation ...

Select Kernel Installation & Distribution System Option: Installation

Load a Distribution

Print Transport Global

Compare Transport Global to Current System

Verify Checksums in Transport Global

Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Backup a Transport Global

Select Installation Option: Load a Distribution

Enter a Host File: (*DIRECTORY NAME)*PX1_0.KID

KIDS Distribution saved on Aug 14, 1996@17:16:26

Comment: PCE v1.0, Visit Tracking v2.0, Scheduling v5.3\*27 and Health Summary v2.7\*8

This Distribution contains Transport Globals for the following Package(s):

VISIT TRACKING 2.0

PCE PATIENT CARE ENCOUNTER 1.0

SD\*5.3\*27

GMTS\*2.7\*8

Want to Continue with Load? YES// \[ENTER\]

Loading Distribution...

Want to RUN the Environment Check Routine? YES// \[ENTER\]

Will first run the Environment Check Routine, VSITIENV

Will first run the Environment Check Routine, PXIPENV

Use VISIT TRACKING 2.0 to install this Distribution.

Load a Distribution

Print Transport Global

Compare Transport Global to Current System

Verify Checksums in Transport Global

Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Select Installation Option: Verify Checksums in Transport Global

Select INSTALL NAME: VISIT TRACKING 2.0 Loaded from Distribution 8/14/96@17:37:50

=\> PCE v1.0, Visit Tracking v2.0, Scheduling v5.3\*27 and Health Summary v2.7\*8 ;Created on Aug 14, 1996@17:16:26

DEVICE: HOME//\[ENTER\]

PACKAGE: VISIT TRACKING 2.0 Aug 14, 1996 1:39 pm PAGE 1

---------------------------------------------------------------------------

22 Routine checked, 0 failed.

Load a Distribution

Print Transport Global

Compare Transport Global to Current System

Verify Checksums in Transport Global

Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Backup a Transport Global

Select Installation Option: Verify Checksums in Transport Global

Select INSTALL NAME: PCE PATIENT CARE ENCOUNTER 1.0 Loaded from Distribution 8/14/96@17:37:50

=\> PCE v1.0, Visit Tracking v2.0, Scheduling v5.3\*27 and Health Summary v2.7\*8 ;Created on Aug 14, 1996@17:16:26

DEVICE: HOME// \[ENTER\]

PACKAGE: PCE PATIENT CARE ENCOUNTER 1.0 Aug 14, 1996 1:39 pm PAGE 1

---------------------------------------------------------------------------

301 Routine checked, 0 failed.

Load a Distribution

Print Transport Global

Compare Transport Global to Current System

Verify Checksums in Transport Global

Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Backup a Transport Global

Select Installation Option: Verify Checksums in Transport Global

Select INSTALL NAME: SD\*5.3\*27 Loaded from Distribution 8/14/96@17:37:50

=\> PCE v1.0, Visit Tracking v2.0, Scheduling v5.3\*27 and Health Summary v2.7\*8 ;Created on Aug 14, 1996@17:16:26

DEVICE: HOME// \[ENTER\]

PACKAGE: SD\*5.3\*27 Aug 14, 1996 1:39 pm PAGE 1

---------------------------------------------------------------------------

39 Routine checked, 0 failed.

Load a Distribution

Print Transport Global

Compare Transport Global to Current System

Verify Checksums in Transport Global

Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Backup a Transport Global

Select Installation Option: Verify Checksums in Transport Global

Select INSTALL NAME: GMTS\*2.7\*8 Loaded from Distribution 8/14/96@17:37:51

=\> PCE v1.0, Visit Tracking v2.0, Scheduling v5.3\*27 and Health Summary v2.7\*8 ;Created on Aug 14, 1996@17:16:26

DEVICE: HOME// \[ENTER\]

PACKAGE: GMTS\*2.7\*8 Aug 14, 1996 1:39 pm PAGE 1

---------------------------------------------------------------------------

11 Routine checked, 0 failed.

Load a Distribution

Print Transport Global

Compare Transport Global to Current System

Verify Checksums in Transport Global

Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Backup a Transport Global

Select Installation Option: Install Package(s)

Select INSTALL NAME: VISIT TRACKING 2.0 Loaded from Distribution 8/14/96@17:37:50

=\> PCE v1.0, Visit Tracking v2.0, Scheduling v5.3\*27 and Health Summary v2.7\*8 ;Created on Aug 14, 1996@17:16:26

This Distribution was loaded on Aug 14, 1996@17:37:50 with header of

PCE v1.0, Visit Tracking v2.0, Scheduling v5.3\*27 and Health Summary v2.7\*8 ;Created on Aug 14, 1996@17:16:26

It consisted of the following Install(s):

VISIT TRACKING 2.0

PCE PATIENT CARE ENCOUNTER 1.0

SD\*5.3\*27

GMTS\*2.7\*8

Will first run the Environment Check Routine, VSITIENV

Install Questions for VISIT TRACKING 2.0

150.1 ANCILLARY DSS ID (including data)

150.2 VSIT SITE CODES (including data)

150.9 VISIT TRACKING PARAMETERS

9000010 VISIT

Will first run the Environment Check Routine, PXIPENV

Install Questions for PCE PATIENT CARE ENCOUNTER 1.0

357.69 TYPE OF VISIT (including data)

> **NOTE:** You already have the 'TYPE OF VISIT' File.

I will MERGE your data with mine.

811.1 PCE CODE MAPPING (including data)

811.2 PCE TAXONOMY (including data)

811.8 PCE REMINDER TYPE (including data)

811.9 PCE REMINDER/MAINTENANCE ITEM (including data)

815 PCE PARAMETERS (including data)

839.01 PCE DEVICE INTERFACE MODULE ERRORS

839.7 PCE DATA SOURCE (including data)

9000001 PATIENT/IHS

> **NOTE:** You already have the 'PATIENT/IHS' File.

9000010.06V PROVIDER

9000010.07V POV

9000010.11V IMMUNIZATION

9000010.12V SKIN TEST

9000010.13V EXAM

9000010.15V TREATMENT

9000010.16V PATIENT ED

9000010.18V CPT

9000010.23V HEALTH FACTORS

9999999.06LOCATION

> **NOTE:** You already have the 'LOCATION' File.

9999999.09EDUCATION TOPICS (including data)

9999999.14IMMUNIZATION (including data)

9999999.15EXAM (including data)

9999999.17TREATMENT (including data)

9999999.27PROVIDER NARRATIVE

> **NOTE:** You already have the 'PROVIDER NARRATIVE' File.

9999999.28SKIN TEST (including data)

9999999.64HEALTH FACTORS (including data)

This is the Institution that Patient entries in the PATIENT/IHS file

(#9000001) will be associated with.

Select INSTITUTION:

Enter the date to start using the new Scheduling/PCE prompts.

All appointments/standalones on or after this date will use the new

prompts. All appointments/standalones before this date will continue to

use the old prompts.

Date: (8/15/96 - 10/1/96): T+1 (AUG 15, 1996)

Install Questions for SD\*5.3\*27

43 MAS PARAMETERS (Partial Definition)

> **NOTE:** You already have the 'MAS PARAMETERS' File.

44 HOSPITAL LOCATION (Partial Definition)

> **NOTE:** You already have the 'HOSPITAL LOCATION' File.

Install Questions for GMTS\*2.7\*8

142.1 HEALTH SUMMARY COMPONENT (Partial Definition)

> **NOTE:** You already have the 'HEALTH SUMMARY COMPONENT' File.

Want to DISABLE Scheduled Options, Menu Options, and Protocols? YES// \[ENTER\]

Enter the Device you want to print the Install messages.

You can queue the install by enter a 'Q' at the device prompt.

Enter a '^' to abort the install.

DEVICE: HOME// PRINTER

Load a Distribution

Print Transport Global

Compare Transport Global to Current System

Verify Checksums in Transport Global

Install Package(s)

Restart Install of Package(s)

Unload a Distribution

Backup a Transport Global

Select Installation Option: \[ENTER\]

Edits and Distribution ...

Utilities ...

Installation ...

Select Kernel Installation & Distribution System Option: \[ENTER\]

Do you really want to halt? YES// \[ENTER\]

Halting at 1:47 pm

\>H

*Printer Output*

Install Started for VISIT TRACKING 2.0 :

Aug 14, 1996@17:42:27

Installing Routines:.......................

Aug 14, 1996@17:42:29

Running Pre-Install Routine: ^VSITIPRE.

Installing Data Dictionaries: .....

Aug 14, 1996@17:42:38

Installing Data: ..

Aug 14, 1996@17:42:44

Installing PACKAGE COMPONENTS:

Installing INPUT TEMPLATE..

Installing PROTOCOL..

Located in the VSIT (VISIT TRACKING) namespace..

Installing OPTION..

Aug 14, 1996@17:42:49

Running Post-Install Routine: ^VSITIPOS..

Looking at the VISIT TRACKING PRARMETERS file.

I am going to add an entry to the DEFAULT INSTITUTION field \#.04

of the VISIT TRACKING PARAMETERS file.

I am going to add an entry to the DEFAULT TYPE field \#.03

of the VISIT TRACKING PARAMETERS file.

Set the Visit id in the Visit Tracking Parameters file

if not already set

Making sure that these protocols are not disabled.

VSIT PATIENT STATUS

Updating Routine file......

Updating KIDS files........

VISIT TRACKING 2.0 Installed.

Aug 14, 1996@17:42:53

Not a production UCI

NO Install Message sent

Install Started for PCE PATIENT CARE ENCOUNTER 1.0 :

Aug 14, 1996@17:42:53

Installing Routines:......................................................

Aug 14, 1996@17:43:28

Running Pre-Install Routine: ^PXIPREI.

Installing Data Dictionaries: ............................

Aug 14, 1996@17:44:07

Installing Data: ..

Aug 14, 1996@17:44:33

Installing PACKAGE COMPONENTS:

Installing BULLETIN..

Installing PRINT TEMPLATE..............

Installing SORT TEMPLATE......

Installing INPUT TEMPLATE.....

Installing DIALOG.....

Installing PROTOCOL..

Located in the PX (PCE PATIENT CARE ENCOUNTER) namespace...

Located in the PX (PCE PATIENT CARE ENCOUNTER) namespace..

Located in the PX (PCE PATIENT CARE ENCOUNTER) namespace..

Located in the PX (PCE PATIENT CARE ENCOUNTER) namespace..

Located in the PX (PCE PATIENT CARE ENCOUNTER) namespace..

Located in the PX (PCE PATIENT CARE ENCOUNTER) namespace..

Located in the PX (PCE PATIENT CARE ENCOUNTER) namespace..

Located in the PX (PCE PATIENT CARE ENCOUNTER) namespace..

Located in the PX (PCE PATIENT CARE ENCOUNTER) namespace..

Located in the PX (PCE PATIENT CARE ENCOUNTER) namespace..

Located in the PX (PCE PATIENT CARE ENCOUNTER) namespace..

Located in the PX (PCE PATIENT CARE ENCOUNTER) namespace..

Located in the PX (PCE PATIENT CARE ENCOUNTER) namespace..

Located in the PX (PCE PATIENT CARE ENCOUNTER) namespace..

Located in the PX (PCE PATIENT CARE ENCOUNTER) namespace..

Located in the PX (PCE PATIENT CARE ENCOUNTER) namespace..

Located in the PX (PCE PATIENT CARE ENCOUNTER) namespace..

Located in the PX (PCE PATIENT CARE ENCOUNTER) namespace..

Located in the PX (PCE PATIENT CARE ENCOUNTER) namespace..

Located in the PX (PCE PATIENT CARE ENCOUNTER) namespace..

Located in the PX (PCE PATIENT CARE ENCOUNTER) namespace..

Located in the PX (PCE PATIENT CARE ENCOUNTER) namespace..

Located in the PX (PCE PATIENT CARE ENCOUNTER) namespace..

Located in the PX (PCE PATIENT CARE ENCOUNTER) namespace..

Located in the PX (PCE PATIENT CARE ENCOUNTER) namespace..

Located in the PX (PCE PATIENT CARE ENCOUNTER) namespace..

Located in the PX (PCE PATIENT CARE ENCOUNTER) namespace..

Located in the PX (PCE PATIENT CARE ENCOUNTER) namespace..

Located in the PX (PCE PATIENT CARE ENCOUNTER) namespace..

Located in the PX (PCE PATIENT CARE ENCOUNTER) namespace..

Located in the PX (PCE PATIENT CARE ENCOUNTER) namespace..

Located in the PX (PCE PATIENT CARE ENCOUNTER) namespace..

Located in the PX (PCE PATIENT CARE ENCOUNTER) namespace..

Located in the PX (PCE PATIENT CARE ENCOUNTER) namespace..

Located in the PX (PCE PATIENT CARE ENCOUNTER) namespace..

Located in the PX (PCE PATIENT CARE ENCOUNTER) namespace..

Located in the PX (PCE PATIENT CARE ENCOUNTER) namespace..

Located in the PX (PCE PATIENT CARE ENCOUNTER) namespace..

Located in the PX (PCE PATIENT CARE ENCOUNTER) namespace..

Located in the PX (PCE PATIENT CARE ENCOUNTER) namespace...

Located in the PX (PCE PATIENT CARE ENCOUNTER) namespace..

Located in the PX (PCE PATIENT CARE ENCOUNTER) namespace..

Located in the PX (PCE PATIENT CARE ENCOUNTER) namespace..

Located in the PX (PCE PATIENT CARE ENCOUNTER) namespace..

Located in the PX (PCE PATIENT CARE ENCOUNTER) namespace..

Located in the PX (PCE PATIENT CARE ENCOUNTER) namespace..

Located in the PX (PCE PATIENT CARE ENCOUNTER) namespace..

Located in the PX (PCE PATIENT CARE ENCOUNTER) namespace..

Located in the PX (PCE PATIENT CARE ENCOUNTER) namespace..

Located in the PX (PCE PATIENT CARE ENCOUNTER) namespace..

Located in the PX (PCE PATIENT CARE ENCOUNTER) namespace..

Located in the PX (PCE PATIENT CARE ENCOUNTER) namespace..

Located in the PX (PCE PATIENT CARE ENCOUNTER) namespace..

Located in the PX (PCE PATIENT CARE ENCOUNTER) namespace..

Located in the PX (PCE PATIENT CARE ENCOUNTER) namespace..

Located in the PX (PCE PATIENT CARE ENCOUNTER) namespace..

Installing LIST TEMPLATE.....

Installing OPTION........................................................

Aug 14, 1996@17:45:14

Running Post-Install Routine: ^PXIPOST..

Populating the LOCATION File \#9999999.06 from the Institution File.

Populating the PXPT fields of the PCE PARAMETERS file (#815)

Now remove the old PCC MASTER CONTROL file (#9001000)

Adding items to PXCE SDAM LIST MENU protocol.

SDAM LIST CHECKED IN

SDAM LIST NO SHOWS

SDAM LIST ALL

SDAM LIST NO ACTION

SDAM LIST CANCELLED

SDAM LIST FUTURE

SDAM LIST INPATIENT

SDAM LIST NON-COUNT

SDAM LIST CHECKED OUT

Adding items to PXCE MAIN HIDDEN ACTIONS protocol.

VALM NEXT SCREEN

VALM PREVIOUS SCREEN

VALM UP ONE LINE

VALM DOWN A LINE

VALM REFRESH

VALM PRINT SCREEN

VALM PRINT LIST

VALM RIGHT

VALM LEFT

VALM TURN ON/OFF MENUS

VALM SEARCH LIST

VALM LAST SCREEN

VALM FIRST SCREEN

VALM GOTO PAGE

VALM BLANK 2

VALM BLANK 3

VALM BLANK 4

Adding items to PXCE ADD/EDIT HIDDEN protocol.

VALM NEXT SCREEN

VALM PREVIOUS SCREEN

VALM UP ONE LINE

VALM DOWN A LINE

VALM REFRESH

VALM PRINT SCREEN

VALM PRINT LIST

VALM RIGHT

VALM LEFT

VALM TURN ON/OFF MENUS

VALM SEARCH LIST

VALM LAST SCREEN

VALM FIRST SCREEN

VALM GOTO PAGE

VALM BLANK 2

Adding item to PXCE GMTS HS ADHOC protocol.

Adding item to PXCE GMPL OE DATA ENTRY protocol.

Adding item to PXCE GMRP REVIEW SCREEN protocol.

Making sure that these protocols are not disabled.

PXCA DATA EVENT

PXCE ADD/EDIT

PXCE ADD/EDIT DISPLAY BRIEF

PXCE ADD/EDIT DISPLAY DETAIL

PXCE ADD/EDIT HIDDEN

PXCE ADD/EDIT INTERVIEW

PXCE ADD/EDIT KNOWN ENCOUNTER

PXCE ADD/EDIT MENU

PXCE ADD/EDIT PATIENT CHANGE

PXCE ADD/EDIT STOP CODE

PXCE BLANK 1

PXCE BLANK 2

PXCE BLANK 3

PXCE BLANK 4

PXCE BLANK HS

PXCE BLANK PL

PXCE BLANK PN

PXCE BLANK SELECT NEW PATIENT

PXCE CHANGE CLINIC STOP

PXCE CHANGE HOSPITAL LOCATION

PXCE CPT ADD

PXCE DATE CHANGE PXCE DELETE V-FILE

PXCE DISPLAY DETAIL

PXCE EDIT V-FILE

PXCE ENCOUNTER EDIT

PXCE ENCOUNTER LIST

PXCE EXAM ADD

PXCE GMPL OE DATA ENTRY

PXCE GMRP REVIEW SCREEN

PXCE GMTS HS ADHOC

PXCE HEALTH FACTORS ADD

PXCE HISTORICAL ENCOUNTER

PXCE HOSPITAL LOCATION VIEW

PXCE IMMUNIZATION ADD

PXCE INTERVIEW

PXCE MAIN HIDDEN ACTIONS

PXCE MAIN MENU

PXCE NEW ENCOUNTER

PXCE PATIENT CHANGE

PXCE PATIENT ED ADD

PXCE POV ADD

PXCE PROVIDER ADD

PXCE QUIT

PXCE QUIT COMPLETELY

PXCE SDAM DISPLAY DETAIL

PXCE SDAM EXPAND

PXCE SDAM INTERVIEW

PXCE SDAM LIST

PXCE SDAM LIST MENU

PXCE SDAM MENU

PXCE SDAM STANDALONE

PXCE SDAM UPDATE ENCOUNTER

PXCE SKIN TEST ADD

PXCE TREATMENT ADD

PXK CPT-SCH TO V-CPT

PXK SDAM TO V-FILES

PXK VISIT DATA EVENT

Recompile protocol menus used by List Manager.

PXCE MAIN MENU

PXCE MAIN HIDDEN ACTIONS

PXCE SDAM MENU

PXCE SDAM LIST MENU

PXCE ADD/EDIT MENU

PXCE ADD/EDIT HIDDEN..

Add "PXRM" Application Group to file 60, 71, 120.51

Done only if not there already.

Adding "PXRM" Application Group to ^DIC(60,

Adding "PXRM" Application Group to ^DIC(71,

Adding "PXRM" Application Group to ^DIC(120.51,

Activate the selection package interfaces in AICS for PCE

Add "PXRS" Application Group to file 80, 80.1, 81

Done only if not there already.

Adding "PXRS" Application Group to ^DIC(80,

Adding "PXRS" Application Group to ^DIC(80.1,

Adding "PXRS" Application Group to ^DIC(81,.

Attach other packages' protocol to PCE's protocols.

Adding protocol IBDF PCE EVENT to extended action protocol PXCA DATA EVENT

... already there

Adding protocol IBDF PCE EVENT to extended action protocol PXK VISIT DATA EVENT

... already there..

Deleting old package file entries & Deleting old Order Parameters.

Deleting Package ++ PCE PATIENT/IHS SUBSET.

Populating the Patient/IHS File \#9000001 via the following queued job ...

The job is task \# 12691

Updating Routine file......

Updating KIDS files........

PCE PATIENT CARE ENCOUNTER 1.0 Installed.

Aug 14, 1996@17:46:29

Not a production UCI

NO Install Message sent

Install Started for SD\*5.3\*27 :

Aug 14, 1996@17:46:30

Installing Routines:........................................

Aug 14, 1996@17:46:38

Running Pre-Install Routine: ^SDYDPRE.

\>\>\> Deleting Provider screen on file 44 ...

Installing Data Dictionaries: ....

Aug 14, 1996@17:46:47

Installing PACKAGE COMPONENTS:

Installing PROTOCOL....

Located in the SD (SCHEDULING) namespace..

Located in the SD (SCHEDULING) namespace..

Located in the SD (SCHEDULING) namespace..

Aug 14, 1996@17:46:54

Running Post-Install Routine: ^SDYDPOST.

\>\>\> Enabling New CPT Protocols

Updating Routine file......

Updating KIDS files.......

SD\*5.3\*27 Installed.

Aug 14, 1996@17:47:01

Install Started for GMTS\*2.7\*8 :

Aug 14, 1996@17:47:01

Installing Routines:............

Aug 14, 1996@17:47:03

Installing Data Dictionaries: ..

Aug 14, 1996@17:47:06

Running Post-Install Routine: ^GMTSP8.

Adding VITAL SIGNS OUTPATIENT component to HEALTH SUMMARY COMPONENT (142.1) file

.

Component Installed.

Adding VITAL SIGNS SELECTED OUTPAT. component to HEALTH SUMMARY COMPONENT (142.1) file.

Component Installed.

Installing new components in AD HOC Health Summary.

Rebuilding Ad Hoc Summary.................................................

...........

Done.

Updating Routine file......

Updating KIDS files.......

GMTS\*2.7\*8 Installed.

Aug 14, 1996@17:47:14

Not a production UCI

NO Install Message sent

Post-Installation - PCE and Visit Tracking Set-up

This section describes the basic steps for setting up PCE and Visit Tracking. As noted, not all of these actions will be necessary, depending on your site's preferences.

24. Use the Visit Tracking Parameters Edit option to ensure that the entries in the VISIT TRACKING PARAMETERS file (150.9) are correct. (This option is not on a menugo through MenuMan to access it.) The post-installation routine ^VSITIPOS, which is called automatically by the installation process, checks to see if the VISIT TRACKING PARAMETERS file (150.9) has an entry. If not, it will configure it with default values.
- Answer the SITE PART OF VISIT ID prompt with TEST ACCOUNT if this is in your test or training account.
- Answer with the three-letter identifier for your facility if you are in production. NOTE: If the SITE PART OF VISIT ID is not entered, entries will not be created in the Visit file (9000010).

\>D ^XUP

Select OPTION NAME: VSIT TRACKING PARM EDIT Visit Tracking Parameters edits.

Select VISIT TRACKING PARAMETERS NAME: 1

DEFAULT TYPE: VA//\[ENTER\]

DEFAULT INSTITUTION: *Enter your institution name here*

Select PACKAGE: PCE PATIENT CARE ENCOUNTER PX

...OK? Yes// \[ENTER\] (Yes)

PACKAGE: PCE PATIENT CARE ENCOUNTER//\[ENTER\]

ACTIVE FLAG: ON//\[ENTER\]

Select PACKAGE: SCHEDULING SD

...OK? Yes// \[ENTER\] (Yes)

PACKAGE: SCHEDULING//\[ENTER\]

ACTIVE FLAG: OFF// ON

Select PACKAGE:\[ENTER\]

SITE PART OF VISIT ID: ??

This is a three letter identifier for this computer system that is

unique in the VA, or "TEST" for a test account. This is appended after a

"-" onto the sequence number to form the unique Visit Id in the VA

system. It is important that this is set to the correct value and not

changed.

Choose from:

ALBANY, NY ALN

ALBUQUERQUE, NM ALB

ALEXANDRIA, LA ALX

ALLEN PARK, MI ALL

ALTOONA, PA ALT

..

Select VISIT TRACKING PARAMETERS NAME:\[ENTER\]  
25. Set PCE Site Parameters through the PCE Site Parameters option located on the PCE Site Parameters Menu. Set your default view as Appointment or Encounter, and enter numbers for computing the offset dates — a number subtracted from today’s date is the Beginning Patient Date Offset (e.g., -30) and a number added to today’s date is the Ending Patient Date Offset (e.g., 1). Do not put in specific dates, but count backwards and forward from the current date.

The Multiple Primary Diagnosis prompt lets sites who use scanning devices choose whether to receive warnings and continue processing the data after the software denotes one primary diagnosis, or to receive errors and prevent the encounter from being processed if more than one diagnosis is listed as primary.

You can also view the switch-over date which determines when the Scheduling interface for checkouts and dispositions will be effective, and the Health Summary start date which determines the starting date for displaying PCE data on Health Summaries. We recommend that the Health Summary start date not be set earlier than the SD/PCE Switch-over date, because the accuracy and completeness of PCE data can't be guaranteed before that date.

Select PCE IRM Main Menu Option: SP PCE Site Parameter Menu

SITE PCE Site Parameters Edit

RPT PCE HS/RPT Parameter Menu ...

DISP PCE Edit Disposition Clinics

Select PCE Site Parameter Menu Option: SIT PCE Site Parameters Edit

Select PCE PARAMETERS ONE: 1

STARTUP VIEW: APPOINTMENT//\[ENTER\]

BEGINNING PATIENT DATE OFFSET: -30//\[ENTER\]

ENDING PATIENT DATE OFFSET: 1//\[ENTER\]

BEGINNING HOS LOC DATE OFFSET: -7//\[ENTER\]

ENDING HOS LOC DATE OFFSET: 0//\[ENTER\]

RETURN WARNINGS: YES//\[ENTER\]

MULTIPLE PRIMARY DIAGNOSES: RETURN WARNING// ?

If errors are returned by the Device Interface then the whole encounter is not processed.

Choose from:

0 RETURN WARNING

1 RETURN ERROR

MULTIPLE PRIMARY DIAGNOSES: RETURN WARNING//\[ENTER\]

SD/PCE SWITCH OVER DATE: AUG 15,1996

HEALTH SUMMARY START DATE: SEP 1,1996

Select PCE PARAMETERS ONE: \[ENTER\]  
26. Make sure that the following EVENTS are on the ITEM multiples of the appropriate protocols:

|                     |                                                       |
|---------------------|-------------------------------------------------------|
| EVENT           | PROTOCOL                                          |
| SDAM PCE EVENT      | ITEM multiple of the PXK VISIT DATA EVENT protocol    |
| IBDF PCE EVENTS     | ITEM multiple of the PXK VISIT DATA EVENT protocol    |
| PXK SDAM TO V-FILES | ITEM multiple of the SDAM APPOINTMENT EVENTS protocol |
| IBDF PCE EVENTS     | ITEM multiple of PXCA DATA EVENT protocol             |
| VSIT PATIENT STATUS | ITEM multiple of DGPM MOVEMENT EVENTS protocol        |

*Example of EVENT placement on PROTOCOLS.*

\>D P^DI

VA FileMan 21.0

Select OPTION: INQUIRE TO FILE ENTRIES

OUTPUT FROM WHAT FILE: PROTOCOL (3091 entries)

Select PROTOCOL NAME: PXK VISIT DATA EVENT VISIT RELATED DATA

ANOTHER ONE: SDAM APPOINTMENT EVENTS Appointment Event Driver

ANOTHER ONE: PXCA DATA EVENT PCE Device Interface Module's Data Event

ANOTHER ONE: DGPM MOVEMENT EVENTS....

STANDARD CAPTIONED OUTPUT? Yes// \[ENTER\] (Yes)

Include COMPUTED fields: (N/Y/R/B): NO// \[ENTER\] - No record number (IEN), no Computed Fields

NAME: PXK VISIT DATA EVENT ITEM TEXT: VISIT RELATED DATA

TYPE: extended action CREATOR: EATON,DENIS

DESCRIPTION: This is a Protocol that PIMS can hook onto to find the

data that was collected by PCE using List Manager, Scanning etc.

PIMS has developed a protocol, SDAM PCE EVENT, which will use the visit

related data to do an auto-checkout.

ITEM: SDAM PCE EVENTITEM: IBDF PCE EVENT

EXIT ACTION: K PXKSPX ENTRY ACTION: S PXKSPX=1

TIMESTAMP: 56796,37384

NAME: SDAM APPOINTMENT EVENTS ITEM TEXT: Appointment Event Driver

TYPE: extended action CREATOR: EATON,DENIS

PACKAGE: SCHEDULING

DESCRIPTION: This extended action contains all the actions that need

to be performed when an action is taken upon an appointment, such as

checking in.

ITEM: ORU PATIENT MOVMT

ITEM: IBACM OP LINK SEQUENCE: 1

ITEM: DG MEANS TEST REQUIRED

ITEM: VAFED EDR OUTPATIENT CAPTURE

ITEM: SDAM LATE ENTRY SEQUENCE: 2

ITEM: RMPR SCH EVENT SEQUENCE: 3

ITEM: DVBA C&P SCHD EVENT SEQUENCE: 8

ITEM: PXK SDAM TO V-FILES

ENTRY ACTION: D ANC^SDVSIT2 TIMESTAMP: 56796,37371

NAME: PXCA DATA EVENT

ITEM TEXT: PCE Device Interface Module's Data Event

TYPE: extended action CREATOR: EATON,DENIS

DESCRIPTION: This is the event point invoked by PCE Device Interface Module when it has not found any errors in the data passed to it. This makes the data available to other users of the data including users of any Local data that may be included.

ITEM: IBDF PCE EVENT

TIMESTAMP: 56796,37383

NAME: DGPM MOVEMENT EVENTS ITEM TEXT: MOVEMENT EVENTS v 5.0

TYPE: extended action CREATOR: SCHLEHUBER,PAMELA

PACKAGE: REGISTRATION

DESCRIPTION:

At the completion of a patient movement the following events

take place through this option:

1\. The PTF record is updated when a patient is admitted,

discharged or transferred.

2\. The appointment status for a patient is updated to 'inpatient'

for admissions and 'outpatient' for discharges. Admissions

to the domiciliary have an 'outpatient' appointment status.

3\. When a patient is admitted, dietetics creates a dietetic

patient file entry and creates an admission diet order.

When a patient is discharged, all active diet

orders are discontinued. If a patient is absent or on

pass, the diet orders are suspended.

4\. Inpatient Pharmacy cancels all active orders when a

patient is admitted, discharged or on unauthorized absence.

A patient can not be given Unit Dose meds unless s/he is

admitted to a ward. The patient can receive IV meds; however.

When a patient is transferred, an inpatient system parameter

is used to determine whether or not the orders should be

cancelled. When a patient goes on authorized absence, the

inpatient system parameter is used to determine whether the

orders should be cancelled, placed on hold or no action taken.

When a patient returns from authorized absence any orders

placed on hold will no longer be on hold.

5\. With ORDER ENTRY/RESULTS REPORTING v2.2,

MAS OE/RR NOTIFICATIONS may be displayed to

USERS defined in an OE/RR LIST for the patient. These notifications

are displayed for admissions and death discharges.

FILE LINK: 11754;DIC(19,

ITEM: ORU AUTOLIST

ITEM: ORU PATIENT MOVMT

ITEM: FHWMAS

ITEM: GMRVOR DGPM

ITEM: PSJ OR PAT ADT

ITEM: IB CATEGORY C BILLING SEQUENCE: 10

ITEM: DG MEANS TEST DOM SEQUENCE: 8

ITEM: DGJ INCOMPLETE EVENT SEQUENCE: 6

ITEM: DGOERR NOTE SEQUENCE: 7

ITEM: DGPM TREATING SPECIALTY EVENT SEQUENCE: 1

ITEM: VAFED EDR INPATIENT CAPTURE

ITEM: SD APPT STATUS SEQUENCE: 2

ITEM: GMRADGPM MARK CHART

ITEM: YS PATIENT MOVEMENT

ITEM: DVB ADMISSION HINQ

ITEM: VSIT PATIENT STATUS

TIMESTAMP: 56803,40994

Select PROTOCOL NAME: \[ENTER\]27. Assign PCE menus and options.

PCE IRM Main Menu

SP PCE Site Parameters Menu ...

TBL PCE Table Maintenance ...

INFO PCE Information Only ...

RM PCE Reminder Maintenance Menu ...

CR PCE Clinical Reports ...

HOME Directions to Patient's Home Add/Edit

CO PCE Coordinator Menu ...

CL PCE Clinician Menu

- Assign the *PCE IRM Main Menu* to IRM staff or coordinators who will be responsible for setting up PCE, maintaining the entries in the PCE tables (such as Patient Education, Immunization, Treatments, etc.), and defining the clinical reminders/maintenance system for your site.
- Assign the *PCE Coordinator Menu* to the Application Coordinator(s) who will use all of the PCE options.

  Assign data entry options on the Coordinator's Menu as follows:
- Assign *PCE Encounter Data Entry - Supervisor* to users who can document a clinical encounter and can also delete any encounter entries, even though they are not the creator of the entries. Users who have this option can also edit the Provider Narrative Category.
- Assign *PCE Encounter Data Entry* to data entry staff who can document a clinical encounter and who can delete their own entries.
- Assign *PCE Encounter Date Entry and Delete* to users who can document a clinical encounter and can also delete any encounter entries, even though they are not the creator of the entries.
- Assign *PCE Encounter Data Entry without Delete* to users who can document a clinical encounter , but should not be able to delete any entries, including ones that they have created.
- Assign the *PCE Clinician Menu* to clinicians who will be entering or editing data and using clinical reports.
- Assign *Directions to Patient's Home Add/Edit* to anyone who needs to enter directions to a patient's home‑especially useful for Hospital-Based Home Care staff (directions can be viewed on Health Summaries).
28. Create a DISPOSITION CLINIC for each division in your facility using the "Set Up a Clinic" option on the Scheduling Supervisor Menu. If you are a multi-divisional facility and you want to credit disposition workload for each division, you will need to set up a DISPOSITION CLINIC for each division. Make sure you define each DISPOSITION CLINIC so that it is easily associated with the division for which you want to credit workload. See APPENDIX B in this manual for more detailed instructions.
- If you are a single-division facility, you should define only one DISPOSITION CLINIC.
- The DISPOSITION CLINICS will ONLY be used with Dispositions.
- PCE recommends creating a clinic defined as Disposition, with a Stop Code number of 102. This clinic should be used with all dispositions.

Define the DISPOSITION CLINIC in the PCE Parameters file (815), using the *PCE Edit Disposition Clinics* option..

29. Review entries contained in PCE Supporting Files: Data is exported for Education Topics, Examinations, Health Factors, Immunizations, Skin Tests, and Treatments.

Use the *Activate/Inactivate Table Items* option to review and assign an appropriate status for entries.

With the exception of “treatments,” data is exported with a status of “active.” Unless you activate current entries or create new entries for “Treatments,” users will not be able to add treatments to an encounter.

*Example of activating Treatment items*

Select PCE Coordinator Menu Option: TBL PCE Table Maintenance

Select PCE Table Maintenance Option: ACT Activate/Inactivate Table Items

E Exams

ET Education Topics

H Health Factors

I Immunizations

S Skin Tests

T Treatments

Select Activate/Inactivate Table Items Option: T Treatments

Select TREATMENT NAME: WOUND CARE

INACTIVE FLAG: INACTIVE// ??

This field is used to inactivate a treatment type. If this

field contains a "1" then the treatment is inactive.

Inactive treatments cannot be selected in the manual data

entry process. Treatment entries should be made inactive when

they are no longer used. Do not delete the entry or change

the meaning of the treatment entry. To make an inactive

treatment type active, enter the "@" symbol to delete the "1"

from the field.

Choose from:

1 INACTIVE

INACTIVE FLAG: INACTIVE// @

Select TREATMENT NAME: *Continue to enter treatments, as needed.*30. Edit the Report Parameters using the *PCE Report Parameter Edit* option. This option is used to define parameters that will be used by the PCE Report Module. You need to identify which clinics are considered Emergency Room clinics by clinicians. You also need to identify the lab test names that are used by your site to identify the following types of Lab tests: Glucose, Cholesterol, LDL Cholesterol, and HBA1C.

To get a printout of current definitions in the PCE Parameters fields for these fields, use the PCE HS/RPT Parameters Print.

*  
Example of editing report parameters*

Select PCE Coordinator Menu Option: parm PCE HS/RPT Parameter Menu

PRNT PCE HS/RPT Parameters Print

HS PCE HS Disclaimer Edit

RPT PCE Report Parameter Edit

Select PCE HS/RPT Parameter Menu Option: RPT PCE Report Parameter Edit

Select PCE PARAMETERS ONE: 1

Select ER CLINIC NAME: Triage

Are you adding 'Triage' as a new REPORT ER CLINIC NAMES (the 1ST for this PCE PARAMETERS)? y (Yes)

Select ER CLINIC NAME: \[ENTER\]

Select GLUCOSE NAMES: ?

Answer with REPORT EMERGENCY CLINICS GLUCOSE NAMES

You may enter a new REPORT EMERGENCY CLINICS, if you wish

Enter the name(s) of the BLOOD GLUCOSE lab assays as they appear in

the Laboratory Test (60) file . DO NOT INCLUDE Glucose Tolerance or

Fluid Glucose test names.

LAB TEST STORED ONLY AT THE "CH" NODE

Answer with LABORATORY TEST NAME, or LOCATION (DATA NAME), or PRINT NAME

Do you want the entire LABORATORY TEST List? n (No)

Select GLUCOSE NAMES: glu

1 GLUCAGON

2 GLUCOSE

3 GLUCOSE, OTHER

4 GLUTAMINE

5 GLUTETHIMIDE

TYPE '^' TO STOP, OR

CHOOSE 1-5:

6 GLU URINE GLUCOSE

CHOOSE 1-6: 6 URINE GLUCOSE

Are you adding 'URINE GLUCOSE' as a new REPORT EMERGENCY CLINICS (the 1ST for this PCE PARAMETERS)? y (Yes)

Select GLUCOSE NAMES:\[ENTER\]

Select CHOLESTEROL NAMES: ??

This field will contain the names of any and all TOTAL CHOLESTEROL

assays as they appear in the Laboratory Test (60) file to allow the

clinic reporting module of the Patient Care Encounter Package to

monitor Quality of Care Markers. Entries should be made either by IRM

personnel or the Clinical coordinator.

Select CHOLESTEROL NAMES: chol

1 CHOLESTEROL

2 CHOLESTEROL CRYSTALS

3 CHOLINESTERASE

4 CHOLYLGLYCINE

CHOOSE 1-4: 1

Are you adding 'CHOLESTEROL' as

a new REPORT CHOLESTEROL NAMES (the 1ST for this PCE PARAMETERS)? y (Yes)

Select CHOLESTEROL NAMES: \[ENTER\]

Select LDL CHOLESTEROL NAMES: ??

This field will contain the names of any and all LDL CHOLESTEROL

assays as they appear in the Laboratory Test (60) file to allow the

clinic reporting module of the Patient Care Encounter Package to

monitor Quality Assurance

Select LDL CHOLESTEROL NAMES: CHOLYLGLYCINE

Are you adding 'CHOLYLGLYCINE' as a new REPORT LDL CHOLESTEROL NAMES (the 1ST for this PCE PARAMETERS)? y (Yes)

Select LDL CHOLESTEROL NAMES:\[ENTER\]

Select HBA1C NAMES: ?

Answer with REPORT HBA1C NAMES

You may enter a new REPORT HBA1C NAMES, if you wish

Enter the name(s) of the Glycosolated Hemoglobin assays as they

appear in the Laboratory Test (60) file.

LABS STORED ONLY AT THE "CH" NODE

Answer with LABORATORY TEST NAME, or LOCATION (DATA NAME), or

PRINT NAME Do you want the entire LABORATORY TEST List? n (No)

Select HBA1C NAMES: glycoSYLATED HEMOGLOBIN A1C

Are you adding 'GLYCOSYLATED HEMOGLOBIN A1C' as

a new REPORT HBA1C NAMES (the 1ST for this PCE PARAMETERS)? y (Yes)

Select HBA1C NAMES:\[ENTER\]

Select PCE PARAMETERS ONE:\[ENTER\]  
31. Create a PXCA PCE ERROR BULLETIN mail group in MAIL GROUP file (#3.8) and add at least one member. Then add this mail group to the MAIL GROUP field on the PXCA PCE ERROR BULLETIN bulletin.

\>D ^XUP

Setting up programmer environment

Terminal Type set to: C-VT220

Select OPTION NAME: XMEDITMG Mail group edit

Mail group edit

Select MAIL GROUP NAME: PXCA PCE ERROR BULLETIN

Are you adding 'PXCA PCE ERROR BULLETIN' as

a new MAIL GROUP? Y (Yes)

MAIL GROUP COORDINATOR: TEDD,DR

NAME: PXCA PCE ERROR BULLETIN Replace

Select MEMBER: TEDD,DR

Are you adding 'TEDD,DR' as a new MEMBER (the 1ST for this MAIL GROUP)? Y (Yes)

Select MEMBER:\[ENTER\]

DESCRIPTION:

1\> \[ENTER\]

TYPE: PU public

ORGANIZER: TEDD,DR

COORDINATOR: TEDD,DR// \[ENTER\]

Select AUTHORIZED SENDER: \[ENTER\]

ALLOW SELF ENROLLMENT?: N NO

Select MEMBER GROUP NAME:\[ENTER\]

Select REMOTE MEMBERS:\[ENTER\]

Select DISTRIBUTION LIST:\[ENTER\]

Select MAIL GROUP NAME:\[ENTER\]

\>D P^DI

VA FileMan 21.0

Select OPTION: ENTER OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: BULLETIN

EDIT WHICH FIELD: ALL// MAIL GROUP (multiple)

EDIT WHICH MAIL GROUP SUB-FIELD: ALL// .01 MAIL GROUP

THEN EDIT MAIL GROUP SUB-FIELD:\[ENTER\]

THEN EDIT FIELD:\[ENTER\]

Select BULLETIN NAME: PXCA PCE ERROR BULLETIN

Select MAIL GROUP: PXCA PCE ERROR BULLETIN TEDD,DR

Are you adding 'PXCA PCE ERROR BULLETIN' as

a new MAIL GROUP (the 1ST for this BULLETIN)? Y (Yes)

Select MAIL GROUP: \[ENTER\]

Select BULLETIN NAME: \[ENTER\]

Select OPTION: \[ENTER\]

\> H32. Create VSIT CREATE ERROR as a mail group, as described above, adding appropriate members. Visit Tracking sends a message to this mail group when it has an error that prevents it from creating a visit

33. Activate PCE components in the Health Summary Component file. All the PCE components will need to be enabled, with the exception of PCE Measurements Non-Tabular and Measurements Selected.

Once you rebuild your AD HOC Health Summary , all the enabled PCE Components plus the two new Vitals components, VITAL SIGNS OUTPATIENT and VITAL SIGNS SELECTED OUTPAT. will be selectable from the Ad Hoc Health Summary Type.

34. Implement the PCE Reminder/Maintenance items to appear on Health Summaries. The Clinical Reminders feature of PCE uses a combination of PCE Table Maintenance options, PCE Clinical Reminders options, PCE Taxonomy options, Health Summary Create/Modify Health Summary Type options, and AICS Encounter Form options.

Follow the steps starting below, as applicable, to implement Clinical Reminders: NOTE: *Most of these steps are optional, to be performed to modify items to meet site needs.*

1\) Use the *List Reminder Definitions* option to print the nationally distributed reminder definitions. As a rule, print both the "VA" and "VA-\*" prefixed reminder definitions, if available. Determine if you want to use the distributed definitions.

*Example of List Reminder Definitions (1st page)*

Select PCE Reminder Maintenance Menu Option: RL List Reminder Definitions

DEVICE: \[ENTER\] VAX RIGHT MARGIN: 80// \[ENTER\]

PCE REMINDER/MAINTENANCE ITEM LIST MAY 22,1996 08:57 PAGE 1

---------------------------------------------------------------------------

BREAST CANCER SCREEN

-----------------------------------

Print Name: Breast Cancer Screen

Related VA-\* Reminder: 555002

Reminder Description:

Mammogram should be given every 2 years to female patients, ages 50-69.

The "VA-\*Breast Cancer Screen" reminder is based on the following

"Breast Cancer Screen" guidelines specified in the "Guidelines for

Health Promotion and Disease Prevention", M-2, Part IV, Chapter 9.

Target Condition: Early detection of breast cancer.

Target Group: All women ages 50-69.

2\) Identify the reminders that your site wants to implement. Copy, as necessary, using the *Copy Reminder Item* option. After copying the reminders, you will be able to alter the new reminders to meet your site's needs.

> **NOTE:** The "VA-" prefix represents the nationally distributed set. When you copy items, the VA-prefix is dropped. "VA-\*" represents the minimum requirements as defined by the National Center for Health Promotion (NCHP). As an alternative, a local site reminder item can be created using the *Edit Taxonomy Item* option.

3\) Use the Health Summary package to activate Clinical Reminders and Clinical Maintenance components. Then rebuild the Adhoc Health Summary Type.

a\. Identify which Health Summary Type is used by the implementing clinic.

b\. Add the Clinical Reminders and/or the Clinical Maintenance components to the Health Summary Type.

c\. Edit component parameters, identifying desired selection items.

4\) If a taxonomy definition related to a reminder needs modification, do the following steps:

a\. Copy the taxonomy using the *Copy Taxonomy Item* option.

b\. Modify the taxonomy, using the *Edit Taxonomy Item* option.

c\. Copy the related Reminder.

d\. Modify the Reminder to reflect the newly created taxonomy, using the *Add/Edit Reminder Item* option.

e\. As an alternative, to copying a taxonomy, local site taxonomy items can be created, using the *Edit Taxonomy Item*.

5\) Modify the Treatment, Immunization, Patient Ed, Skin Test, Exam, and Health Factors files, if necessary, through the *PCE Table Maintenance* option.

> **NOTE:** If clinical reminders are not showing up correctly on Health Summaries, see the PCE User Manual, Appendix A-7, for troubleshooting information which IRM staff with programmer access can use.

6\) Coordinate the use of Encounter Forms (through the AICS package) with the use of Health Summary Clinical Maintenance Components. Make sure that the relevant encounter forms contain all appropriate list bubbles for PCE data: Health Factors, Exams, Immunizations, Diagnosis, Patient Education, Procedures, and Skin Tests.

7\) Inactivate reminders which will not be used, with the *Activate/Inactive Reminders* option.

  
35 . (optional) Add Health Summary, Problem List, and Progress Notes as actions on PCE screens for quick access to those programs from PCE.

\>D P^DI

VA FileMan 21.0

Select OPTION: ENTER OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: 101 PROTOCOL

(2978 entries)

EDIT WHICH FIELD: ALL// ITEM

EDIT WHICH ITEM SUB-FIELD: ALL// .01 ITEM

THEN EDIT ITEM SUB-FIELD: MNEMONIC

THEN EDIT ITEM SUB-FIELD: \[ENTER\]

THEN EDIT FIELD: \[ENTER\]

Select PROTOCOL NAME: PXCE SDAM MENU Appointment Menu AV

Select ITEM: PXCE BLANK HS// \[ENTER\]

ITEM: PXCE BLANK HS// PXCE GMTS HS ADHOC Health Summary HS

MNEMONIC: HS

Select ITEM: PXCE BLANK PN

...OK? Yes// \[ENTER\] (Yes)

ITEM: PXCE BLANK PN// PXCE GMRP REVIEW SCREEN Progress Notes PN

MNEMONIC: PN

Select ITEM: PXCE BLANK PL

...OK? Yes// \[ENTER\] (Yes)

ITEM: PXCE BLANK PL// PXCE GMPL OE DATA ENTRY Patient Problem List PL

MNEMONIC: LP

Select ITEM: \[ENTER\]

Select PROTOCOL NAME: PXCE MAIN MENU

Select ITEM: PXCE BLANK HS// \[ENTER\]

ITEM: PXCE BLANK HS// PXCE GMTS HS ADHOC Health Summary HS

MNEMONIC: HS

Select ITEM: PXCE BLANK PN

...OK? Yes// \[ENTER\] (Yes)

ITEM: PXCE BLANK PN// PXCE GMRP REVIEW SCREEN Progress Notes PN

MNEMONIC: PN

Select ITEM: PXCE BLANK PL

...OK? Yes// \[ENTER\] (Yes)

ITEM: PXCE BLANK PL// PXCE GMPL OE DATA ENTRY Patient Problem List PL

MNEMONIC: LP

Select ITEM: \[ENTER\]

Select PROTOCOL NAME: \[ENTER\]

Appendix A - Visit Creation Activation Levels

Activation of the Visit Tracking package can occur at multiple levels. The following are examples of encounter creation scenarios:

- Creation of Primary encounters for appointments and standalones via manual data entry, scanned encounter forms, and data passed to PCE/Visit Tracking from ancillary packages.
- Creation of Occasion of Service encounters by ancillary packages such as Laboratory and Radiology via manual data entry and data passed to PCE/Visit Tracking from ancillary packages.
- Creation of Stop Code encounters via manual data entry. This type of encounter will be discontinued effective 10/1/96.
- Creation of historical encounters for clinically significant data that is NOT used for billing or workload purposes. These encounter entries are done via manual data entry.

Appendix B - Orientation of MAS Staff to PCE

Orient your MAS users to changes in their Appointment Management and Disposition functionality resulting from PCE/Scheduling integration.

## Dispositions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Create a DISPOSITION CLINIC for each division in your facility using the "Set Up a Clinic" option on the Scheduling Supervisor Menu.

- If you are a multi-divisional facility and you want to credit disposition workload for each division, set up a DISPOSITION CLINIC for each division. Make sure you define each DISPOSITION CLINIC so that it is easily associated with the division for which you want to credit workload.
- If you are a single-division facility, you should define only one DISPOSITION CLINIC.
- The DISPOSITION CLINICS are *only* used with Dispositions.
- PCE recommends creating a clinic defined as Disposition, with a Stop Code number of 102. This clinic should be used with all dispositions.
- Use "PCE Edit Disposition Clinics" option located on the "PCE Site Parameter Menu" to enter the DISPOSITION CLINICs that were defined for use with Dispositions for your facility. The purpose of this is to restrict the Hospital Location for a Disposition to DISPOSITION CLINICs only.
- In single-division facilities, the hospital location for Dispositions is stuffed automatically, and you are not prompted to select a DISPOSITION HOSPITAL LOCATION.

*PCE Edit Disposition Clinics Example:*

Select PCE Site Parameter Menu Option: PCE Edit Disposition Clinics

Select PCE PARAMETERS ONE: 1

Select DISPOSITION HOSPITAL LOCATIONS: ?

Answer with DISPOSITION HOSPITAL LOCATIONS

Choose from:

DISPOSITION 1

DISPOSITION 2

You may enter a new DISPOSITION HOSPITAL LOCATIONS, if you wish

Answer with HOSPITAL LOCATION NAME, or ABBREVIATION

Do you want the entire 58-Entry HOSPITAL LOCATION List? n

Select DISPOSITION HOSPITAL LOCATIONS: DISPOSITION 1

## Checkout Interview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Checkout Interview has been changed by PCE to comply with new requirements that every encounter must have a provider, diagnosis, and procedure associated with it. You still enter the checkout information through the same menu and options, but the appearance on your computer screen changes when you get to the prompts relating to the new requirements.

You are prompted to enter Provider (and to designate if it's the Primary Provider), Service-connection status, Diagnosis (you must designate a primary diagnosis), and Procedure (or CPT codes). You may also designate if the Diagnosis should be added to the patient's Problem List.

A provider key isn't required for the providers entered here.

REMEMBER: Entering one or two question marks provides help (including lists of acceptable CPT codes, Diagnoses, and Stop Codes) on how to respond to prompts.

*Steps to use this option:*1. Select Checkout from the Appointment Manager Menu and select the appointment you want to check out.<u>Appt Mgt Module Jul 29, 1996 17:54:16 Page: 1 of 2</u>

Patient: PCEPATIENT,ONE (6789) Outpatient

Total Appointment Profile 06/29/96 thru 04/24/99

<u>Clinic Appt Date/Time Status\_\_\_\_\_\_\_\_\_\_\_\_\_</u>

1 Cardiology Jul 09, 1996 09:00 No Action Taken

2 Diabetes Clinic Jul 18, 1996 16:48 Action Req/Checked Out

3 Old Jul 18, 1996 16:53 Checked Out

4 Cardiology Jul 22, 1996 09:00 Checked Out

5 Diabetes Clinic Jul 22, 1996 11:00 Checked Out

6 Cardiology Jul 23, 1996 09:00 No Action Taken

+ Enter ?? for more actions

CI Check In PT Change Patient CO Check Out

UN Unscheduled Visit CL Change Clinic EC Edit Classification

MA Make Appointment CD Change Date Range PR Provider Update

CA Cancel Appointment EP Expand Entry DX Diagnosis Update

NS No Show AE Add/Edit DE Delete Check Out

DC Discharge Clinic RT Record Tracking CP Procedure Update

AL Appointment Lists PD Patient Demographics

Select Action: Next Screen// CO=6 Check Out

> **NOTE:** The response CO=6 above is a shortcut to selecting the action Check-Out (CO) and then selecting which appointment to do the Checkout on. If you only entered CO, you would then be prompted to select an appointment.

  
2. Answer prompts about follow-up appointment, check-out date and time, and classification.

6 Cardiology Jul 23, 1996 09:00 No Action Taken

Do you wish to make a follow-up appointment? YES// NO

Check out date and time: NOW// (JUL 29, 1996@17:54)

--- Classification --- \[Required\]

Was treatment for SC Condition? NO

Was treatment related to Agent Orange Exposure? NO

Was treatment related to Ionizing Radiation Exposure? NO

Was treatment related to Environmental Contaminant Exposure? NO*You now see the new screens from PCE.*3. Enter all providers associated with this encounter.

One primary provider must be designated for each encounter.

PAT/APPT/CLINIC: PCEPATIENT,ONE JUL 23, 1996@09:00 CARDIOLOGY

PROVIDER: ...There is 1 PROVIDER associated with this encounter.

<u>Previous Entry: PCEPROVIDER,ONE\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_</u>

- - E N C O U N T E R P R O V I D E R S - -

<u>No. PROVIDER</u>

1 PCEPROVIDER,ONE\* PRIMARY

Enter PROVIDER: PCEPROVIDER,TWO4. Enter the diagnoses. Specify which is the primary diagnosis for this encounter, and if it should be added to the Problem List.PAT/APPT/CLINIC: PCEPATIENT,ONE JUL 23, 1996@09:00 CARDIOLOGY

ICD CODE: V70.3 --MED EXAM NEC-ADMIN PURP PRIMARY

<u>\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_</u>- - E N C O U N T E R D I A G N O S I S (ICD9 CODES) - -

<u>No. ICD DESCRIPTION</u>

No DIAGNOSIS for this Encounter.

Enter Diagnosis : V70.3--MED EXAM NEC-ADMIN PURP

ONE primary diagnosis must be established for each encounter!

Is this the PRIMARY DIAGNOSIS for this ENCOUNTER? YES// \[ENTER\]

Enter NEXT Diagnosis: \[ENTER\]

Would you like to add this Diagnosis to the Problem List? NO// YES

Enter PROVIDER associated with PROBLEM: TEDD,DR // \[ENTER\]  
> **NOTE:** If more than one diagnosis is entered, you are only prompted once, at the end, to add any of them to the Problem List.

PAT/APPT/CLINIC:PCEPATIENT,ONE JUL 29, 1996@18:08 ADMITTING AND SCREEN

ICD CODE: ...There is 1 PROVIDER associated with this encounter.

<u>Previous Entry: 557.9\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_</u>

- - E N C O U N T E R D I A G N O S I S (ICD9 CODES) - -

<u>No. ICD DESCRIPTION</u>

1 446.1\* MUCOCUTAN LYMPH NODE SYN

2 557.9\* VASC INSUFF INTEST NOS

3 227.0\* BENIGN NEOPLASM ADRENAL PRIMARY

Enter NEXT Diagnosis: \[ENTER\]

Would you like to add any Diagnoses to the Problem List? NO// YES

Select 1 or several Diagnoses (eg 1,3,4,7,3-6,2-5): 1

Enter PROVIDER associated with PROBLEM: DEFA,TANA // \[ENTER\]5. Next enter the procedure(s) performed.PAT/APPT/CLINIC: PCEPATIENT,ONE JUL 23, 1996@09:00 CARDIOLOGY

<u>PROVIDER: ...There is 1 PROVIDER associated with this encounter.\_\_\_\_\_\_\_</u>

- - E N C O U N T E R P R O C E D U R E S (CPT CODES) - -

<u>No. CPT CODE QUANTITY DESCRIPTION PROVIDER\_\_\_\_\_\_\_\_</u>

Enter PROCEDURE (CPT CODE): 22600-- NECK SPINE FUSION

How many times was this procedure performed: 1// \[ENTER\]

Enter PROVIDER associated with PROCEDURE: PCEPROVIDER,ONE // PCEPROVIDER,TENYou may enter more procedures, along with the associated provider.PAT/APPT/CLINIC: PCEPATIENT,ONE JUL 23, 1996@09:00 CARDIOLOGY

PROVIDER: ...Enter the provider associated with the CPT'S.....

<u>CPT: ...There is 1 PROCEDURE associated with this encounter.\_\_\_\_\_\_</u>

- - E N C O U N T E R P R O C E D U R E S (CPT CODES) - -

<u>No. CPT CODE QUANTITY DESCRIPTION PROVIDER\_\_\_\_\_\_\_\_</u>

1 22600\* 1 NECK SPINE FUSION PCEPROVIDER,TEN

Enter NEXT PROCEDURE (CPT CODE): \[ENTER\]6. To delete a Provider, Diagnosis, or Procedure, enter the @ symbol and the number of the item to be deleted (e.g. @1).  
7. You are then taken back to the Scheduling screens.<u>Check Out Jul 29, 1996 18:12:52 Page: 1 of 2</u>

Patient: PCEPATIENT,ONE (5678) Clinic: ADMITTING AN

Disposition Date/Time: Jul 29, 1996 18:08 Checked Out: YES

CLASSIFICATION \[Required\]

1 Treatment for SC Condition: YES

2 Agent Orange Exposure: Not Applicable

3 Ionizing Radiation Exposure: Not Applicable

4 Environmental Contaminants: Not Applicable

PROVIDER \[Required\] DIAGNOSIS \[Required\]

1 PCEPROVIDER,TEN 1 446.1 MUCOCUTAN LYMPH NODE SYN

2 557.9 VASC INSUFF INTEST NOS

3 227.0 BENIGN NEOPLASM ADRENAL

\+ Enter ?? for more actions

CD (Check Out Date) EC Edit Classification PD Patient Demographics

AP Appointment PR Provider Update RT Record Tracking

DC Discharge Clinic DX Diagnosis Update CP Procedure Update

AE Add/Edit IN Interview

Select Action: Next Screen// DX Diagnosis Update

> **NOTE:** If you don't answer the Procedure prompt when you're using the Add/Edit action to add a Standalone Encounter, you will be prompted for Stop Code (you can only add one Stop Code at a time). If you don't enter anything at the Procedure or Stop Code prompts , you are prompted to delete the encounter.PAT/APPT/CLINIC: PCEPATIENT,ONE JUL 29, 1996@13:00 HAND

PROVIDER: ...Enter the provider associated with the CPT'S.....

<u>CPT: ...There are 0 PROCEDURES associated with this encounter.</u>

- - E N C O U N T E R P R O C E D U R E S (CPT CODES) - -

<u>No. CPT CODE QUANTITY DESCRIPTION PROVIDER</u>

No CPT CODES for this Encounter.

Enter PROCEDURE (CPT CODE): \[ENTER\]PAT/APPT/CLINIC: PCEPATIENT,ONE JUL 29, 1996@13:00 HAND

STOP CODE: ..There are 0 STOP CODES associated with this ENCOUNTER

<u>\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_</u>

- - E N C O U N T E R S T O P C O D E S - -

No. CODE DESCRIPTION

No STOP CODE for this ENCOUNTER.

Enter a STOP CODE: \[ENTER\]

You Must have a STOP CODE or a PROCEDURE to complete this action.

Do you want to delete this encounter? NO// YESOnline Help for Checkout Interview

Extensive help is available at all prompts within the Checkout Interview. The examples below demonstrate the layered structure for getting more detailed help.

NOTE that the help appears above the prompt.

Examples of help at the Provider prompt:PAT/APPT/CLINIC: PCEPATIENT,ONE JUL 29, 1996@13:00 HAND

PROVIDER: ...There is 1 PROVIDER associated with this encounter.

- - E N C O U N T E R P R O V I D E R S - -

No. PROVIDER

1 PCEPROVIDER,ONE PRIMARY

Enter a PROVIDER associated with this patient ENCOUNTER.

You can enter partial names to receive a short list.

Above is a list of PROVIDERS already entered. If there are any

additional ones, they should be entered at this time.

\* indicates that the entry has been visited during this session.

For more detailed HELP and selection lists enter ??

Enter PROVIDER: ?- - E N C O U N T E R P R O V I D E R S - -

To receive detailed help for ADD or DELETE enter the following:

A to get help on how to ADD providers.

D to get help on how to DELETE providers.

E to get help on how to EDIT providers.

To receive more SELECTION LISTS enter the following:

1 to get a list of ALL active providers.

2 to get a list of CLINIC providers.

3 to get a list of ENCOUNTER FORM providers.

Enter '^' to leave HELP CENTER

Enter a letter or number for additional help: APAT/APPT/CLINIC: PCEPATIENT,ONE JUL 29, 1996@13:00

PROVIDER: ...There is 1 PROVIDER associated with this encounter.

<u>\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_</u>

\- - E N C O U N T E R P R O V I D E R S - -

To ADD a PROVIDER enter one of the following:

PROVIDER NAME (eg. PCEPROVIDER,FIVE)

PARTIAL LAST NAME of the PROVIDER (eg. PCE or PCEPRO)

Enter '^' to leave HELP CENTER

Enter a letter or number for additional help: 1PAT/APPT/CLINIC: PCEPATIENT,ONE JUL 29, 1996@13:00

PROVIDER: ...There is 1 PROVIDER associated with this encounter.

<u>\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_</u>

HELP SCREEN - - A L L P R O V I D E R S - -

ITEM NAME

1 PCEPROVIDER,THREE

2 PCEPROVIDER,FOUR

3 PCEPROVIDER,FIVE

4 PCEPROVIDER,EIGHT

5 PCEPROVIDER,NINE

6 PCEPROVIDER,ELEVEN

7 PCEPROVIDER,SIX

8 PCEPROVIDER,TWELVE

9 PCEPROVIDERA,ONE

10 PCEPROVIDERA,TWO

Enter '^' to quit, '-' for previous page.

Select a single 'ITEM NUMBER' or 'RETURN' to continue: ^