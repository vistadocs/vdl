---
title: OR*3*190 Set Up Notes for Non-VA Medications CPRS GUI 24
doc_type: IG
doc_label: Installation Guide
doc_layer: patch
doc_subject: Set Up Notes for Non-VA Medications CPRS GUI 24
app_code: CPRS
app_name: Computerized Patient Record System
section: CLI
app_status: archive
pkg_ns: OR
patch_ver: 3
patch_id: OR*3*190
group_key: "CPRS:OR:3"
file_numbers: []
security_keys: []
menu_options: 0
description: If your site does not have an entry for the ORWDX WRITE ORDERS LIST parameter and your site uses the Package level settings for the ORWOR WRITE ORDERS LIST and ORWOR CATEGORY SEQUENCE parameters, no manual updates are required after patch installation. As part of the installation, patch OR\3.0\190 (
audience: 
keywords: 
  - parameter
  - order
  - entry
  - orders
  - press
  - sequence
  - write
  - prompt
  - values
  - results
page_count: 0
word_count: 2151
section_count: 0
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)_Archive/or_30_190_set_up_notes_for_non-va_meds.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)_Archive/or_30_190_set_up_notes_for_non-va_meds.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=338"
---

Set Up Notes for Non-VA Meds

If your site does not have an entry for the ORWDX WRITE ORDERS LIST parameter and your site uses the Package level settings for the ORWOR WRITE ORDERS LIST and ORWOR CATEGORY SEQUENCE parameters, no manual updates are required after patch installation. As part of the installation, patch OR\*3.0\*190 (CPRS GUI v.24) makes a new entry PSH OERR as sequence \#53 based on a decision from the CPRS Clinical Workgroup, which will put the selection Meds, Non-VA on the Writer Orders list in the CRPS GUI between the Meds, Inpatient and Meds, Outpatient selections as shown below:

![](or-3-190-set-up-notes-for-non-va-medications-cprs-gui-24/001.png)

This capture shows how the selection Meds, Non-VA should appear on the Write Orders list between Meds, Inpatient and Meds, Outpatient.

The installation also makes an entry for sequence \#68 in the ORWOR CATEGORY SEQUENCE parameter that puts the Non-VA Meds display group on the orders tab between inpatient and outpatient meds.

However, if your site has one of the following, the appropriate staff must update the necessary parameter(s):

- ORWDX entry exists. The ORWDX WRITE ORDERS LIST parameter overrides the ORWOR WRITE ORDERS LIST. Any entry for this parameter will cause the Meds, Non-VA selection not to display on the Write Order list. ORWDX WRITE ORDERS LIST must be updated to add the Non-VA Medications items to the order menu.
- ORWOR WRITE ORDERS LIST is not set at the Package level. To avoid making changes to local set up, developers export parameter changes at only the package level. No change will be made to other parameter level settings. ORWOR WRITE ORDERS LIST must be updated to place the “Meds, Non-VA” selection on the Write Orders list in the appropriate location.
- ORWOR CATEGORY SEQUENCE is not set at the Package level. Again, the exported setting is at the Package level only and must be changed manually for other parameter levels. ORWOR CATEGORY SEQUENCE must be updated to put the display group on the orders tab in the appropriate location.

Manually Updating ORWDX WRITE ORDERS LIST

If your site has assigned an order menu at any level of this parameter, you will need to add the Meds, Non-VA selection to the ORWDX WRITE ORDERS LIST parameter. You will need to add the PSH OERR dialog as one of the options. The CPRS Clinical Workgroup indicated that Non-VA Medications should display between Inpatient Medications and Outpatient Medications.

To make a change to the ORWDX WRITE ORDERS LIST parameter, IRM or other appropriate personnel should use the following steps:

1.  Login to the List Manager interface to your system.
2.  At the Option Name prompt, type ORMGR and press \<Enter\>.
3.  At the CPRS Manager Menu Option, type PE and press \<Enter\>.
4.  At the CPRS Configuration (Clin Coord) Option type MM and press \<Enter\>.
5.  At the Order Menu prompt, type all or part of the menu you need to change and press \<Enter\>.
6.  If necessary, locate the appropriate menu and type the menu number at the prompt and press \<Enter\>.
7.  At the next screen, type Add and press \<Enter\>.
8.  At the next prompt, type Menu and press \<Enter\>.
9.  At the Item prompt, type PSH OERR and press \<Enter\>.
10. At the Row prompt, type the row number where you want to place the Non-VA Meds selection and press \<Enter\>.
11. At the Column prompt, type the column number here you want to place the Non-VA Meds selection and press \<Enter\>.
12. At the Display Text prompt, type NonVA Meds and press \<Enter\>.

> **NOTE:** Hyphens or dashes are not allowed in the display text.

13. At the Mnemonic prompt, type a mnemonic if you want one and press \<Enter\>.
14. When prompted whether you want to enter another item, do not type anything and press \<Enter\>.

Below is an example of how to add this dialog entry to the ORWDX WRITE ORDERS LIST parameter:

Select OPTION NAME: ORMGR CPRS Manager Menu

Select CPRS Manager Menu Option: PE CPRS Configuration (Clin Coord)

Select CPRS Configuration (Clin Coord) Option: MM Order Menu Management

Select Order Menu Management Option: MN Enter/edit order menus

Select ORDER MENU: ZZ

1 ZZJD GUI WRITE ORDER LIST

2 ZZJD SUB MENU

3 ZZKCM WRITE ORDERS

4 ZZRAF ORDER DIALOG REPLACEMENT

CHOOSE 1-4: 1 ZZJD GUI WRITE ORDER LIST

Select Action: Next Screen// ADD Add ...

Menu Editor Mar 00, 2004@00:00:00 Page: 1 of 3

Menu: ZZJD GUI WRITE ORDER LIST Column Width: 80

1

\| PSO SUPPLY

\| JD Add New Orders

\| Allergy/Adverse Reaction

\| Outpatient Medications

\+ Inpatient Medications

\| IV Fluids

\| Imaging

\| Laboratory

\| VITAL SIGNS

1 Word Processing Order

\| ZZJD QO LOCAL DOSAGE

\| ZZJD QO1

\| ZZJD IVQO1

\| IV Potassium

\+ ZZJD QO2 FOR OUTPT

\| Word Processing Order

\|

Add: MEN Menu Items

ITEM: PSH OERR

ROW: 3

COLUMN: 1

There is another item in this position already!

Do you want to shift items in this column down? YES//

DISPLAY TEXT: NonVA Meds

MNEMONIC:

ITEM:

Rebuilding menu display ...

Manually Updating ORWOR WRITE ORDERS LIST

If your site uses a System-level setting for the ORWOR WRITE ORDERS LIST parameter, IRM or other appropriate personnel will need to add the PSH OERR entry with the appropriate sequence number to place it between your site’s entries for Inpatient Medications and Outpatient Medications according to the CPRS Clinical Workgroup so that the “Meds, Non-VA” selection is in the designated location.

To make an entry for PSH OERR in the ORWOR WRITE ORDERS LIST, use the following steps:

1.  Login to the List Manager interface to your system.
2.  At the Option Name prompt, type ORMGR and press \<Enter\>.
3.  At the CPRS Manager Menu Option, type IR and press \<Enter\>.
4.  At the CPRS Configuration (IRM) Option prompt, type XX and press \<Enter\>.
5.  List the current values for the parameter at the General Parameter Tools Option prompt by typing LV and pressing \<Enter\>.

Below is an example of how to list the values.

Select OPTION NAME: ORMGR CPRS Manager Menu menu

Select CPRS Manager Menu Option: IR CPRS Configuration (IRM)

Select CPRS Configuration (IRM) Option: XX General Parameter Tools

Select General Parameter Tools Option: LV List Values for a Selected Parameter

Select PARAMETER DEFINITION NAME: ORWOR WRITE ORDERS LIST Write Orders (Inpatient)

Values for ORWOR WRITE ORDERS LIST

Parameter Instance Value

----------------------------------------------------------------------------

PKG: ORDER ENTRY/RESULTS REPOR 30 FHW1

PKG: ORDER ENTRY/RESULTS REPOR 52 PSJ OR PAT OE

PKG: ORDER ENTRY/RESULTS REPOR 53 PSH OERR

PKG: ORDER ENTRY/RESULTS REPOR 55 PSO OERR

PKG: ORDER ENTRY/RESULTS REPOR 58 PSJI OR PAT FLUID OE

PKG: ORDER ENTRY/RESULTS REPOR 60 LR OTHER LAB TESTS

PKG: ORDER ENTRY/RESULTS REPOR 70 RA OERR EXAM

PKG: ORDER ENTRY/RESULTS REPOR 80 GMRCOR CONSULT

PKG: ORDER ENTRY/RESULTS REPOR 85 GMRCOR REQUEST

PKG: ORDER ENTRY/RESULTS REPOR 90 GMRVOR

PKG: ORDER ENTRY/RESULTS REPOR 99 OR GXTEXT WORD PROCESSING OR

Enter RETURN to continue or '^' to exit:

Parameter Instance Value

----------------------------------------------------------------------------

PKG: ORDER ENTRY/RESULTS REPOR 110 OR ADD MENU CLINICIAN

Parameter Instance Value

----------------------------------------------------------------------------

SYS: OEX.FO-SLC.MED.VA.GOV 15 ZZMEL MENU

SYS: OEX.FO-SLC.MED.VA.GOV 20 GMRAOR ALLERGY

SYS: OEX.FO-SLC.MED.VA.GOV 30 FHW1

SYS: OEX.FO-SLC.MED.VA.GOV 52 PSJ OR PAT OE

SYS: OEX.FO-SLC.MED.VA.GOV 55 PSO OERR

SYS: OEX.FO-SLC.MED.VA.GOV 58 PSJI OR PAT FLUID OE

SYS: OEX.FO-SLC.MED.VA.GOV 60 LR OTHER LAB TESTS

SYS: OEX.FO-SLC.MED.VA.GOV 70 RA OERR EXAM

SYS: OEX.FO-SLC.MED.VA.GOV 80 GMRCOR CONSULT

SYS: OEX.FO-SLC.MED.VA.GOV 85 GMRCOR REQUEST

SYS: OEX.FO-SLC.MED.VA.GOV 90 GMRVOR

SYS: OEX.FO-SLC.MED.VA.GOV 99 OR GXTEXT WORD PROCESSING OR

15. If necessary, edit the parameter by typing EP and pressing \<Enter\>.
16. At the Parameter Definition prompt, type ORWOR WRITE ORDERS LIST and press \<Enter\>.
17. At the Enter Selection prompt, type 3 for System level and press \<Enter\>.
18. At the Select Sequence prompt, type the number that will place it between Inpatient Medications and Outpatient Medications and press \<Enter\>.
19. At the Are you adding \<*number*\> as a new Sequence prompt, type YES and press \<Enter\>.
20. At the Sequence prompt, make sure the number you entered is displayed and press \<Enter\>.
21. At the Order Dialog prompt, type PSH OERR and press \<Enter\>.

The following example shows how to edit this parameter.

LV List Values for a Selected Parameter

LE List Values for a Selected Entity

LP List Values for a Selected Package

LT List Values for a Selected Template

EP Edit Parameter Values

ET Edit Parameter Values with Template

EK Edit Parameter Definition Keyword

Select General Parameter Tools Option: EP Edit Parameter Values

--- Edit Parameter Values ---

Select PARAMETER DEFINITION NAME: ORWOR WRITE ORDERS LIST Write Orders (Inpatient)

ORWOR WRITE ORDERS LIST may be set for the following:

1 User USR \[choose from NEW PERSON\]

2 Location LOC \[choose from HOSPITAL LOCATION\]

2.3 Service SRV \[choose from SERVICE/SECTION\]

2.7 Division DIV \[choose from INSTITUTION\]

3 System SYS \[DEVCUR.FO-SLC.MED.VA.GOV\]

Enter selection: 3 System DEVCUR.FO-SLC.MED.VA.GOV

--- Setting ORWOR WRITE ORDERS LIST for System: DEVCUR.FO-SLC.MED.VA.GOV ---

Select Sequence: 53

Are you adding 53 as a new Sequence? Yes// YES

Sequence: 53// 53

Order Dialog: PSH OERR

Select Sequence:

Manually Updating ORWOR CATEGORY SEQUENCE

CPRS exports the display group "NON-VA MEDICATIONS" as sequence/instance \# 68 at the Package-level for this parameter. This places Non-VA Med orders between inpatient and outpatient medication orders on the Orders tab and indicates the proper display group when the order is sent to Pharmacy.

If your site uses the System level for this parameter, your site's System-level values over-write the Package-level values and Non-VA Med will not display in the service column of the Orders tab. This could cause some confusion about which medications the patient is taking.

To check the parameter values and add the display group "NON-VA MEDICATIONS" at the System-level for this parameter, if necessary, use the following steps:

1.  Login to the List Manager interface to your system.
2.  At the Option Name prompt, type ORMGR and press \<Enter\>.
3.  At the CPRS Manager Menu Option prompt, type IR and press \<Enter\>.
4.  At the CPRS Configuration (IRM) Option prompt, type XX and press \<Enter\>.
5.  To list values for this parameter, at the General Parameter Tools Option prompt, type LV and press \<Enter\>.
6.  At the Parameter Definition Name prompt, type ORWOR CATEGORY SEQUENCE and press \<Enter\>.

> Below is an example of how to list the parameter values.

Select OPTION NAME: ORMGR CPRS Manager Menu

Select CPRS Manager Menu Option: IR CPRS Configuration (IRM)

Select CPRS Configuration (IRM) Option: XX General Parameter Tools

Select General Parameter Tools Option: LV List Values for a Selected

Parameter

Select PARAMETER DEFINITION NAME: ORWOR CATEGORY SEQUENCE Orders

Category Sequence

The display should look similar to what is below. If your site does not use the System level, you will see only PKG-level listings:

Values for ORWOR CATEGORY SEQUENCE

Parameter Instance Value

--------------------------------------------------------------------------

--

PKG: ORDER ENTRY/RESULTS REPOR 10 M.A.S.

PKG: ORDER ENTRY/RESULTS REPOR 20 ALLERGIES

PKG: ORDER ENTRY/RESULTS REPOR 30 VITALS/MEASUREMENTS

PKG: ORDER ENTRY/RESULTS REPOR 35 ACTIVITY

PKG: ORDER ENTRY/RESULTS REPOR 40 NURSING

PKG: ORDER ENTRY/RESULTS REPOR 50 DIETETICS

PKG: ORDER ENTRY/RESULTS REPOR 60 IV MEDICATIONS

PKG: ORDER ENTRY/RESULTS REPOR 65 OUTPATIENT MEDICATIONS

PKG: ORDER ENTRY/RESULTS REPOR 68 NON-VA MEDICATIONS

PKG: ORDER ENTRY/RESULTS REPOR 70 INPATIENT MEDICATIONS

PKG: ORDER ENTRY/RESULTS REPOR 75 LABORATORY

PKG: ORDER ENTRY/RESULTS REPOR 80 IMAGING

PKG: ORDER ENTRY/RESULTS REPOR 90 CONSULTS

PKG: ORDER ENTRY/RESULTS REPOR 100 PROCEDURES

PKG: ORDER ENTRY/RESULTS REPOR 110 SURGERY

PKG: ORDER ENTRY/RESULTS REPOR 120 OTHER HOSPITAL

SERVICES

If you have Package-level listings, you can halt. If you see one or more "SYS" listings, it indicates your site is not using the Package-level values and you must add NON-VA MEDICATIONS \#68 to your System level values as follows:

22. At the General Parameter Tools Option prompt, type EP and press \<Enter\>.
23. At the Parameter Definition Name prompt, type ORWOR CATEGORY SEQUENCE and press \<Enter\>.
24. At the Enter Selection prompt, type the number of the System level setting and press \<Enter\>.
25. At the Select Sequence prompt, type 68 and press \<Enter\>.
26. At the Are you adding 68 as a new Sequence prompt, type Y and press \<Enter\>.
27. The Sequence prompt should then appear with the number 68, press \<Enter\>.
28. At the Display Group prompt, type NON-VA MEDICATIONS and press \<Enter\>.

An example of how to make the entry for this sequence/instance is shown below.

LV List Values for a Selected Parameter

LE List Values for a Selected Entity

LP List Values for a Selected Package

LT List Values for a Selected Template

EP Edit Parameter Values

ET Edit Parameter Values with Template

EK Edit Parameter Definition Keyword

Select General Parameter Tools Option: EP Edit Parameter Values

--- Edit Parameter Values ---

Select PARAMETER DEFINITION NAME: ORWOR CATEGORY SEQUENCE Orders

Category Sequence

ORWOR CATEGORY SEQUENCE may be set for the following:

8 System SYS \[EXPCUR.FO-SLC.MED.VA.GOV\]

Enter selection: 8 System EXPCUR.FO-SLC.MED.VA.GOV

--- Setting ORWOR CATEGORY SEQUENCE for System: EXPCUR.FO-SLC.MED.VA.GOV

---

Select Sequence: 68

Are you adding 68 as a new Sequence? Yes// YES

Sequence: 68// 68

Display Group: NON-VA MEDICATIONS