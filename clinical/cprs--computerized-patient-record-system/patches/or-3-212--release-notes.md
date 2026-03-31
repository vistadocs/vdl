---
title: OR*3*212 Release Notes VBECS Interface
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: VBECS Interface
app_code: CPRS
app_name: Computerized Patient Record System
section: CLI
app_status: archive
pkg_ns: OR
patch_ver: 3
patch_id: OR*3*212
group_key: "CPRS:OR:3"
file_numbers: []
security_keys: []
menu_options: 0
description: The most recent entries in this list are linked to the location in the manual they describe. Click on a link or page number to go to that section.
audience: 
keywords: 
  - vbecs
  - blood
  - order
  - orders
  - bank
  - span
  - class
  - cprs
  - test
  - laboratory
page_count: 0
word_count: 4368
section_count: 0
table_count: 0
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: April 2009
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)_Archive/or_3_212rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)_Archive/or_3_212rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=338"
---

![](or-3-212-release-notes-vbecs-interface/001.png)

CPRS-VBECS Interface (OR\*3.0\*212) Release Notes

April 2009

Office of Enterprise Development

Computerized Patient Record System Product Line

<span id="_Toc107371093" class="anchor"></span>Revision History

The most recent entries in this list are linked to the location in the manual they describe. Click on a link or page number to go to that section.

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 12%" />
<col style="width: 30%" />
<col style="width: 21%" />
<col style="width: 18%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Date</strong></td>
<td><strong>Page</strong></td>
<td><strong>Change</strong></td>
<td><strong>Project Manager</strong></td>
<td><strong>Technical Writer</strong></td>
</tr>
<tr class="even">
<td>April 2009</td>
<td>All</td>
<td><blockquote>
<p>Initial Release</p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
<td><blockquote>
<p><mark>REDACTED</mark></p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

<span id="_Toc225584505" class="anchor"></span>Table of Contents

<span id="_Toc225584506" class="anchor"></span>Introduction

VBECS (VistA Blood Establishment Computer System) replaces the current blood bank functionality under VistA with a dedicated server providing blood ordering and other blood transfusion services. These servers will undergo a phased implementation in medical centers starting in early 2009. Once an operational VBECS server is in place at a medical center, it is detected by the Computerized Patient Record System (CPRS) which enables the new coordinated order dialog for blood products and the diagnostic lab tests that need to accompany them. VistA patch OR\*3.0\*212 provides the interface between CPRS and VBECS.

<span id="_Toc225584507" class="anchor"></span>Order Dialog

The new order dialog that is enabled by the presence of VBECS and OR\*3.0\*212 is unique in that it is a combination of two order dialogs. Blood Components and Diagnostic Tests related to Blood Bank Orders make this a complex order dialog:

![](or-3-212-release-notes-vbecs-interface/002.png)

Blood components that are orderable from this dialog are:

- RED BLOOD CELLS
- FRESH FROZEN PLASMA
- PLATELETS
- CRYOPRECIPITATE
- WHOLE BLOOD
- OTHER

Associated lab tests include:

- ABO/RH
- ANTIBODY SCREEN
- DIRECT ANTIGLOBULIN TEST
- TRANSFUSION REACTION WORKUP
- TYPE & SCREEN

When a blood component is chosen, and a TYPE & SCREEN has not been completed for the patient within a certain time, CPRS displays a reminder that the TYPE & SCREEN is required and does not allow order acceptance until it is added. Selecting Accept Order displays a message detailing any incomplete fields required for the order to be processed. The order is accessioned in the Laboratory package, the UID number from the Laboratory is used to accept orders in VBECS. This time period is set to 3 (three) days initially but can be changed with the parameter ORWDXVB VBECS TNS CHECK.

- Note: The new CPRS ordering process works in conjunction with VBECS which now creates a SF518-like form. Local processes need to be reevaluated in light of the new VistA capabilities and possibility of down-time.

This patch works with CPRS GUI Version 27 and above.

<span id="_Toc225584508" class="anchor"></span>OR\*3.0\*212 Required Patches

- OR\*3.0\*243
- VBECS BUNDLE 1.0

<span id="_Toc225584509" class="anchor"></span>Install Considerations

Everything in this section must be tested in a non-production environment (your test account) before installing this patch in your production account. The work you need to do:

- The new Blood Product dialog needs to be place in your local menus.
- Old Blood Bank Laboratory tests need to be modified by the Laboratory Information Manager (LIM) to output only (thus effectively disabling them).
- Re-do Quick orders that use the old Blood Bank Laboratory orderable items. They must be disabled or converted to the to the new VBECS Blood Bank Order Dialog items.
- Convert existing orders using Blood Bank Laboratory tests new orderable items.
- Consider Auto/DC Blood Orders; does your facility want to auto/dc Blood Bank Laboratory orders.
- VistA Parameters should be used to customize the blood bank interface. Set the OR VBECS LEGACY REPORT parameter to Yes.
- Incorporate local site procedures thru the Laboratory Test (#69.9) file.

You need to coordinate with the Laboratory Information Manager (LIM) and/or Clinical Applications Coordinator (CAC) in the performing and testing of this work.

<span id="_Toc225584510" class="anchor"></span>New Blood Product Dialog

Using the CPRS Order Menu Management, you can add the new order dialog, VBECS BLOOD BANK, to the Write Orders pane of CPRS. How each site adds this order dialog is determined by local needs.

<span id="_Toc225584511" class="anchor"></span>Old Blood Bank Laboratory Tests Disabled

On the day you go live with VBECS.

Old Blood Bank Laboratory Tests Orderable Items may have been renamed or added by your medical center. Original Blood Bank Laboratory Tests included:

- Transfusion Request
- Type and Screen
- Coombs (both direct and indirect)
- ABO/RH, but your site may have more

To disable old Blood Bank laboratory tests, the LIM needs to search for them in the LABORATORY TEST file (#60) and change the type field to OUTPUT as shown in this example:

DEV5A4:CPRS27\>d ^DII

VA FileMan 22.0

Select OPTION: 1 ENTER OR EDIT FILE ENTRIES

INPUT TO WHAT FILE: LABORATORY TEST// \<Enter\>

EDIT WHICH FIELD: ALL// NAME

THEN EDIT FIELD: TYPE

THEN EDIT FIELD: \<Enter\>

Select LABORATORY TEST NAME: ABO/RH

1 ABO/RH - LAB

2 ABO/RH TYPING

CHOOSE 1-2: 2 ABO/RH TYPING

NAME: ABO/RH TYPING//

TYPE: BOTH// OUTPUT OUTPUT (CAN BE DISPLAYED)

Select LABORATORY TEST NAME:

<span id="_Toc225584512" class="anchor"></span>Re-do Old Quick Orders

On the day of going live with VBECS.

Quick Orders that use old Blood Bank tests need to be disabled or re-written. You can use the search and replace orderables command \[ORCM SEARCH/REPLACE ORDERABLES\] to locate quick orders that use old Blood Bank Laboratory tests. Renaming them is an effective way to disable them. As an alternative, you can re-edit them to include the new lab orderable items.

Here is an example of searching for quick orders that use old lab orders:

Select OPTION NAME: ORCM SEARCH

1 ORCM SEARCH/REPLACE Search/replace components

2 ORCM SEARCH/REPLACE ORDERABLES Search/replace orderables

CHOOSE 1-2: 2 ORCM SEARCH/REPLACE ORDERABLES Search/replace orderables

Search/replace orderables

Search for: TRANSFUSION REQUEST

Quick Orders and Dialogs containing TRANSFUSION REQUEST

-------------------------------------------------------------------------

1 LRT TRANSFUSION REQUEST BLOOD RED

2 LRTZ TRANS REQ BLOOD RED

-------------------------------------------------------------------------

Replace with:

The type of quick order must be BLOOD PRODUCTS. Once BLOOD PRODUCTS has been chosen as TYPE, choices for Component or Test are narrowed down to:

- CRYOPRECIPITATE
- FRESH FROZEN PLASMA
- OTHER
- PLATELETS
- RED BLOOD CELLS
- WHOLE BLOOD

  or
- ABO/RH
- ANTIBODY SCREEN
- DIRECT ANTIGLOBULIN TEST
- TRANSFUSION REACTION WORKUP
- TYPE & SCREEN

Any Blood Bank Quick Orders that retains LAB as the Type of Order and selecting one of the old lab orderable items will fail to be processed.

<span id="_Toc225584513" class="anchor"></span>Convert Existing Orders

Immediately prior to live production of VBECS.

The print for old orders can be run at any time. Converting to new orders must be done before the test is performed in the lab. If you choose, you can let the lab take care of this at the time of the test, but doing it before hand may avoid some confusion.

Neither VBECS nor OR\*3.0\*212 convert old blood orders to the new system. Any pending orders at the time of installation need to be re-entered after installation. In order to do this you should get a list of pending lab orders prior to installing this patch in production. The screen capture below gives a recommended way to accomplish this:

DEV5A4:CPRS27\>d P^DII

VA FileMan 22.0

Select OPTION: 2 PRINT FILE ENTRIES

OUTPUT FROM WHAT FILE: LAB ORDER ENTRY// \<Enter\>

SORT BY: DATE ORDERED// \]

SORT BY: DATE ORDERED// @DATE ORDERED

START WITH DATE ORDERED: FIRST// \<Enter\>

WITHIN DATE ORDERED, SORT BY: SPECIMEN \# (multiple)

SPECIMEN \# SUB-FIELD: TEST (multiple)

TEST SUB-FIELD: @TEST/PROCEDURE

START WITH TEST/PROCEDURE: FIRST// TRANSFUSION REQUEST

GO TO TEST/PROCEDURE: LAST// TRANSFUSION REQUESTZ

WITHIN TEST/PROCEDURE, SORT BY:

STORE IN 'SORT' TEMPLATE: XXX FUTURE TESTS

Are you adding 'XXX FUTURE TESTS' as a new SORT TEMPLATE? No// Y (Yes)

DESCRIPTION:

1\>Future lab orders.

2\> \<Enter\>

EDIT Option: \<Enter\>

SHOULD TEMPLATE USER BE ASKED 'FROM'-'TO' RANGE FOR 'TEST/PROCEDURE'? NO//

FIRST PRINT FIELD: \]

FIRST PRINT FIELD: DATE ORDERED

THEN PRINT FIELD: SPECIMEN \# (multiple)

THEN PRINT SPECIMEN \# SUB-FIELD: TEST (multiple)

THEN PRINT TEST SUB-FIELD: TEST/PROCEDURE

THEN PRINT TEST SUB-FIELD:

THEN PRINT SPECIMEN \# SUB-FIELD: ORDER \#

THEN PRINT SPECIMEN \# SUB-FIELD: COLLECTION STATUS

THEN PRINT SPECIMEN \# SUB-FIELD: NAME

THEN PRINT SPECIMEN \# SUB-FIELD:

THEN PRINT FIELD:

Heading (S/C): LAB ORDER ENTRY LIST Replace \<Enter\>

STORE PRINT LOGIC IN TEMPLATE: XXX FUTURE TEST

Are you adding 'XXX FUTURE TEST' as a new PRINT TEMPLATE? No// Y (Yes)

START AT PAGE: 1//\<Enter\>

DEVICE: \<Enter\> HOME

...SORRY, LET ME THINK ABOUT THAT A MOMENT...

LAB ORDER ENTRY LIST SEP 9,2008 09:20 PAGE 1

DATE COLLECTION

ORDERED TEST/PROCEDURE ORDER \# STATUS

NAME

--------------------------------------------------------------------------------

AUG 25,2008 TRANSFUSION REQUEST 945 UNCOLLECTED

ORPATIENT,ONE

SEP 2,2008 TRANSFUSION REQUEST 972 UNCOLLECTED

CPRSPATIENT,SIX

OCT 9,2008 TRANSFUSION REQUEST 1074 UNCOLLECTED

USRPATIENT,THREE

TRANSFUSION REQUEST 1076 UNCOLLECTED

ORPATIENT,SEVENTEEN

NOV 2,2008 TRANSFUSION REQUEST 701 UNCOLLECTED

PSJPATIENT,EIGHT

NOV 3,2008 TRANSFUSION REQUEST 594

CPRSPATIENT,TWENTY

NOV 4,2008 TRANSFUSION REQUEST 829 UNCOLLECTED

CPRSPATIENT,FIVE

Select OPTION:

<span id="_Toc225584514" class="anchor"></span>Consider Auto/DC Blood Orders

Your facility should consider how you want the BLOOD PRODUCTS dialogue orders to auto/dc. Setting auto/dc is covered in Appendix G of the CPRS Technical Manual. We’ve included here an example of adding orders generated from the BLOOD PRODUCTS dialogue to be exempted from a particular patient movement:

Select CPRS Configuration (Clin Coord) Option: DO    DELAYED ORDERS/AUTO-DC SET-UP

 

Select one of the following:

   
          1         Auto-DC Rules  
          2         Release Events  
   
Enter response: 1  Auto-DC Rules  
 

Auto-DC events/rules          Oct 21, <2008@10:49:23>          Page:    1 of    1  
Auto-DC set up and maintenance - All entries/Truncated view  
    Event Name                               Display Text         Active?  Event  
1   ADMISSION                                ADMISSION              Y       A  
2   DEATH                                    DEATH                  Y       D  
3   DISCHARGE                                DISCHARGE              Y       D  
4   FROM ASIH                                FROM ASIH              Y       T  
5   FROM PASS                                FROM PASS              Y       T  
6   ON PASS                                  ON PASS                Y       T  
7   SPECIALTY CHANGE                         SPECIALTY CHANGE       Y       S  
8   SURGERY                                  SURGERY                N       O  
9   TO ASIH                                  TO ASIH                Y       T  
10  WARD TRANSFER                            WARD TRANSFER          N       T  
   
   
  
          Select number or enter action desired                              \>\>\>  
AE  Add/Edit              CD  Change display  
AI  Activate/Inactivate   DD  Detailed Display  
Select action: Quit// AE   Add/Edit

 

Select item(s): 7

 

Editing auto-dc rules takes effect immediately.  
   
NAME: SPECIALTY CHANGE//  
DISPLAY TEXT: SPECIALTY CHANGE//  
   
The TYPE OF EVENT, MAS MOVEMENT TYPE, and DIVISION fields can only be  
edited when the entry is inactive.  
   
DC REASON: Treating Specialty Change//  
Select EXCEPT FROM SPECIALTY: NH HOSPICE//  
  EXCEPT FROM SPECIALTY: NH HOSPICE//  
  Select TO SPECIALTY: NH LONG STAY SKILLED NURSING  
         //  
Select EXCEPT FROM SPECIALTY:  
Select TYPE OF ORDERS TO DC: DIETETICS//  
Select EXCEPT ORDERS IN DISPLAY GROUP: BLOOD PRODUCTS  
         //  
Select EXCEPT FOR ORDERABLE ITEM: MRSA CONTACT PRECAUTION  
         // ?  
    Answer with EXCLUDED ORDERABLE ITEMS EXCEPT FOR ORDERABLE ITEM  
   Choose from:  
   HOME OXYGEN THERAPY  
   HOME OXYGEN REQUEST  
   HOME O2  
   HOME OXYGEN  
   BLOOD PRODUCT ORDER PENDING  
   FALL RISK  
   PAGE ANESTHESIA  
   MRSA CONTACT PRECAUTION  
   
        You may enter a new EXCLUDED ORDERABLE ITEMS, if you wish  
        Enter an orderable item that should not be dc'd by this rule.  
        Only "active" orderable items can be selected  
   
 Answer with ORDERABLE ITEMS NAME, or INACTIVATED, or ID, or CODE, or  
     DISPLAY GROUP, or INPATIENT MED, or OUTPATIENT MED, or IV BASE, or  
     IV ADDITIVE, or SUPPLY, or NON-VA MEDS, or LAB SECTION, or TYPE, or  
     IMAGING TYPE, or COMMON PROCEDURE, or DIET TYPE, or  
     DIAGNOSTIC TEST, or SYNONYM, or SET  
 Do you want the entire ORDERABLE ITEMS List?  
Select EXCEPT FOR ORDERABLE ITEM: MRSA CONTACT PRECAUTION  
         //

<span id="_Toc225584515" class="anchor"></span>VistA Parameters

VBECS comes with the following parameters:

OR VBECS COMPONENT ORDER     List of Blood Components

OR VBECS ERROR MESSAGE Text for Network Error

OR VBECS LEGACY REPORT     Show Legacy (VISTA) Blood Bank Report

OR VBECS MODIFIERS     List of Component Modifiers

OR VBECS ON     VBECS Functionality Site Enabled

OR VBECS REASON FOR REQUEST     List of Reasons for Request

OR VBECS SUPPRESS NURS ADMIN     Suppress Nursing Admin Prompt

ORWDXVB VBECS TNS CHECK Max time between TYPE & SCREEN and order

These are available for local setup for the sites particular requirements or local needs.

The OR VBECS COMPONENT ORDER parameter determines the sequence in which the components appear in the selection list.

The OR VBECS ERROR MESSAGE contains text for the error message displayed when CPRS cannot contact the VBECS server to fill in dialog information. The VBECS order process can still proceed because the finished order is transmitted via HL7. You can replace the supplied text of this message with information about your own local procedures, possibly including the Blood Bank phone number.

The OR VBECS LEGACY REPORT parameter determines whether the Legacy (VistA) Blood Bank Report is displayed after the VBECS blood bank report is displayed. Currently this must be set to Yes for you to see this information.

The OR VBECS MODIFIERS parameter allows local configuration of the blood component modifiers. Specifically, it allows you to enter the sequence in which the modifiers should appear in the selection list.

The OR VBECS ON parameter toggles VBECS ON and OFF. Yes means ON, which is the default.

The OR VBECS REASON FOR REQUEST can be used to add site specific reasons for requests making them available for the clinician to select when placing an order.

The OR VBECS SUPPRESS NURS ADMIN parameter disables the prompt/pop-up that tells the user they must enter a Nursing Administration Order manually after entering a VBECS Blood order. Disabling this feature is usually done when a Nursing Administration order has been created and added to a VBECS order set or quick orders.

The ORWDXVB VBECS TNS CHECK parameter sets the number of days to check for a Type & Screen Order. The default is 3 days, but a site may override this by modifying this parameter.

<span id="_Toc225584516" class="anchor"></span>Incorporate Local Site Procedures

Many medical centers have a quick order type of IMMEDIATE DRAW or SEND PATIENT. If this is the case at your medical center you may want to make it the default Collection Type. This can be done by adjusting the contents of the LABORATORY SITE (#69.9) file thus:

Select FileMan (VA) Option: ENter or Edit File Entries

INPUT TO WHAT FILE: LABORATORY TEST// 69.9  LABORATORY SITE

                                          (1 entry)

EDIT WHICH FIELD: ALL// HOSPITAL SITE    (multiple)

   EDIT WHICH HOSPITAL SITE SUB-FIELD: ALL//

THEN EDIT FIELD:

Select LABORATORY SITE SITE NAME: HOSPITAL 

Select HOSPITAL SITE: DERM NEW NORTH COUNTY-BUSCH

         //

  HOSPITAL SITE: DERM NEW NORTH COUNTY-BUSCH//

  MAX DAYS FOR CONTINUOUS ORDERS: 370//

  ASK URGENCY:

  DEFAULT TYPE FOR QUICK ORDERS: SEND PATIENT//

<span id="_Toc225584517" class="anchor"></span>Installation Timeline

For best results, plan the install for a Saturday so that you can go live on Monday. Coordinate with Surgery and other services so that Blood Bank usage will be light at the beginning of the week.

Months Before

- Figure out how you want things to look in CPRS using your test account–what will need to be changed from Legacy Blood Bank ordering—menus, quick orders, consults? 
- What quick orders/menus/order sets/consults do you need to set up? 
- What will the new process flow be from order to transfusion completion? 
- Will transfusion reaction work-ups be handled differently? 
- Get the necessary service buy-in and approval (Surgery, Nursing, Medicine, Anesthesia, etc…) for changes in processes.
- Get ORELSE approval and waivers for Blood Bank staff; check that all Blood Bank staff have the necessary security keys.
- Schedule extra Blood Bank staff to be available during the day of you go live to help with validation, answer phone calls, etc.

Weeks/Days Before

- Conversion patches are installed, anomaly report run and mapping is completed by the Programmer, LIM and Blood Bank Supervisor.
- Schedule the Regional Server Admin Group for your day of go-live to be on stand-by.
- Get VBECS server admin access for your programmer that will be FTPing files to VBECs.
- Consider scheduling a local network person to be on standby for day-of to deal with existing Blood Bank orders for future dates (after go-live).

Day-Of

- Hour One: LIM and programmer begin installing patches, and run conversion.
- Hour Two: After conversion is complete and data validation is performed the LIM, Blood Bank supervisor, any extra Blood Band staff should come in.
- Hour Three: Programmer/LIM set up HL7 logical links, Monitor view etc…CACs come in to place order dialogue, set up order sets, quick orders, remove old menus.
- Hour Four:  LIM gives required menus to Blood Bank staff.
- Hour Five:  LIM adds users to system in VBECs and runs some order tests.
  - Hour Six:  Blood Bank supervisor begins setup of workload, quality control, products, etc. in VBECs. The programmer goes home.
- Hour Seven: Testing of order dialogue –then CACs go home.
- Hour Eight:  Blood Bank staff begins entering current inventory into VBECs–LIM goes home after some basic testing that all is well.
- Hour Nine:  Blood Bank supervisor and staff have complete access to VBECs.

<span id="_Toc225584518" class="anchor"></span>Troubleshooting OR\*3.0\*212

When will the VBECS Order Dialog be enabled?

The GUI dialog, and the orderable items related to this patch will appear in CPRS after:

1.  The patch OR\*3.0\*212 is installed
2.  The VBECS system is operational
3.  The order menu is configured with the VBECS menu item

Once VBECS is installed, VistA Blood Bank 5.2 is disabled and becomes read-only. Each medical center needs to make their providers aware of the change to VBECS so that the ordering of blood products proceeds smoothly.

What happens with orders that go to VBECS?

When an order contains both blood products and lab tests, the complex order is delivered to the laboratory to be collected and accessioned. The UID, Unique Identifier (ID) is used by VBECS to accept orders in the system.

What if the VBECS server is down?

When entering a VBECS order while the VBECS server is down, CPRS displays an error message.

1.  If you need the blood product right away, call the blood bank.
2.  If the order is for a future procedure, you need do nothing. CPRS keeps orders until the VBECS server is back on line. It will then file your blood order and proceed as normal.

Why doesn’t the order dialog display when Blood Bank is selected under the Write Orders Menu?

This would be because, during installation, the HL7 link port number was entered in the VistALink port instead of the correct VistALink port number. There is no warning message, just a modal hour glass. The user needs to Ctrl-Alt-Del and use the Task Manager to get out of the application, then restart CPRS.

The fix is to use FileMan to edit the 8989.5 file and enter the correct port number in the VistALink port number as in this example:

Select General Parameter Tools Option: lv  List Values for a Selected Parameter

Select PARAMETER DEFINITION NAME: vbecs

     1   VBECS VISTALINK    

     2   VBECS FUNCTIONALITY SITE ENABLED  OR VBECS ON   VBECS Functionality Sit

e Enabled

CHOOSE 1-2: 1  VBECS VISTALINK  

Values for VBECS VISTALINK

Parameter                      Instance             Value

-------------------------------------------------------------------------

PKG: VBECS                     LISTENER IP ADDRESS 

PKG: VBECS                     LISTENER PORT NUMBER \_\_\_\_

Blood orders never show completed or discontinued in CPRS

This is the opposite problem from the one described above. The HL7 port number is wrong, probably VistALink port number was entered by mistake.

The fix is to use the HL7 Edit Link command as shown in this screen capture:

Select Systems Manager Menu Option: hl7  HL7 Main Menu

          Event monitoring menu ...

          Systems Link Monitor

          Filer and Link Management Options ...

          Message Management Options ...

          Interface Developer Options ...

          Site Parameter Edit

   SM     Systems Link Monitor

   FM     Monitor, Start, Stop Filers

   LM     TCP Link Manager Start/Stop

   SA     Stop All Messaging Background Processes

   RA     Restart/Start All Links and Filers

   DF     Default Filers Startup

   SL     Start/Stop Links

   PI     Ping (TCP Only)

   ED     Link Edit

   ER     Link Errors ...

Select Filer and Link Management Options Option: ed  Link Edit

Select HL LOGICAL LINK NODE: vbecs-oERR 

                          HL7 LOGICAL LINK

-------------------------------------------------------------------------

                NODE: VBECS-OERR                     DESCRIPTION:

         INSTITUTION:                              

      MAILMAN DOMAIN:                              

           AUTOSTART: Enabled

          QUEUE SIZE: 1000 

            LLP TYPE: TCP                          

          DNS DOMAIN: \<Enter\>                             

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Exit     Save     Refresh

 

Enter a command or '^' followed by a caption to jump to a specific field.

COMMAND:                                 Press \<PF1\>H for help   

Select HL LOGICAL LINK NODE: vbec

     1   VBECS-OERR 

     2   VBECSPTM 

     3   VBECSPTU 

CHOOSE 1-3: 1  VBECS-OERR

                          HL7 LOGICAL LINK

-------------------------------------------------------------------------

  ┌─────────────────TCP LOWER LEVEL PARAMETERS───────────────────┐

  │                      VBECS-OERR                          │

  │                                                                     │

  │  TCP/IP SERVICE TYPE: SINGLE ENER                                   │

  │       TCP/IP ESS:                                                   │

  │          TCP/IP PORT: \_\_\_\_                                          │

  │          TCP/IP PORT (OPTIMIZED):                                   │

  │                                                                     │

  │   ACK TIMEOUT:                       RE-TRANSMISION ATTEMPTS:       │

  │  READ TIMEOUT:                     EXCEED RE-TRANSMIT ACTION:       │

  │    BLOCK SIZE:                                      SAY HELO:       │

  │                                  DIRECT CONNECT OPEN TIMEOUT:       │

  │STARTUP NODE:                                      PERSISTENT: NO    │

  │   RETENTION:                            UNI-DIRECTIONAL WAIT:       │

  └──────────────────────────────────────────────────────────┘

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

COMMAND:                                   Press \<PF1\>H for help   

<span id="_Toc225584519" class="anchor"></span>OR\*3.0\*212 Known Issues

<span id="_Toc225584520" class="anchor"></span>Fixed in CPRS 27N

The following errors are fixed in CPRS 27N. This means that if you already have CPRS 27N installed when you install VBECS and OR\*3.0\*212, you will not see these errors.

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<thead>
<tr class="header">
<th><h4 id="clearquest-number" class="unnumbered">ClearQuest Number</h4></th>
<th><h4 id="description" class="unnumbered">Description</h4></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>17255</td>
<td>Labs linked to Components display Lab Results Available even though there is no lab data.</td>
</tr>
<tr class="even">
<td>17335</td>
<td>Blood Component and Diagnostic Tests fields allow free text but the order will not be processed with free text in one or both of these fields.</td>
</tr>
<tr class="odd">
<td>17494</td>
<td>Urgency should default to Routine. However, when selecting a Diagnostic Tests before a component the Urgency changes to PRE-OP.</td>
</tr>
<tr class="even">
<td>16973</td>
<td>A duplicate Type and Screen warning does not appear for quick orders.</td>
</tr>
<tr class="odd">
<td>17349</td>
<td><p>For both quick orders and regular orders:</p>
<p>If the Blood Component and Diagnostic Test dialog has two tests, one of them Type and Screen, and you delete the other test, an error appears: An order of TYPE and SCREEN must be created with this order set. This error message appears even though there is a Type and Screen still in the order. You must delete Type and Screen and re-add it before the order is accepted.</p></td>
</tr>
<tr class="even">
<td>17489</td>
<td>VBECS Remote Data look up Blood Bank report only works if All Available Sites is selected.</td>
</tr>
<tr class="odd">
<td>17490</td>
<td>Urgency should be unpopulated for VBECS Quick Orders that have only the Type and Screen.</td>
</tr>
<tr class="even">
<td>17524</td>
<td>The Blood Order and Diagnostic Test sometimes gets hung up in the Diagnostic Test box. If this happens, the only way to recover is to use the key cord Ctrl-Alt-Delete, select the Task Manager, and do and End Task on CPRS.</td>
</tr>
<tr class="odd">
<td>17614</td>
<td>VBECS uses a different algorithm to fill in the Collection Type than Lab orders. Functionality needs to be changed to use the Lab algorithm in the Blood Order and Diagnostic Test dialog.</td>
</tr>
<tr class="even">
<td>17615</td>
<td>VBECS urgency is defaulting to Routine in the Blood Bank and Diagnostic Test dialog. It should be using the same algorithm as Lab to determine the default urgency.</td>
</tr>
</tbody>
</table>

<span id="_Toc225584521" class="anchor"></span>VBECS Server Down or HL7 Link Down

Information flows between CPRS and VBECS along two different paths as shown in this chart:

![](or-3-212-release-notes-vbecs-interface/003.png)

If the VistALink is down CPRS cannot retrieve information from the VBECS Server, but you still are able to place a VBECS order because CPRS works independently from VBECS. You are informed when the order dialog is opened and can then click on the Blood Bank Orders tab to continue.

If the HL7 link is down VistA must store the order for delivery when the HL7 link is restored.

If the VBECS Server is down, then both the VistALink and HL7 link are closed. You will get both messages, one when the order dialog is open and the other when CPRS accepts the order.

#### Note: If this is a delayed order, you need not take any action. CPRS will transmit the order to VBECS when communication is restored. If the HL7 link is down you must follow local manual procedures in the case that immediate action is required. This usually involves calling the blood bank.

If everything is proceeding normally when you click the Accept Order button, the dialog closes and you can see your pending order in the list of orders.

Two error messages may be displayed when CPRS cannot communicate with VBECS due to the server or one of the communications links being down. The first is this:

![](or-3-212-release-notes-vbecs-interface/004.png)

This message simply means that CPRS cannot retrieve certain data to fill in the order dialog. The text of this message can be changed locally with the use of the OR VBECS ERROR MESSAGE parameter.

CPRS will allow you to continue with and complete the order.

#### Note: You can still complete the order in CPRS after this message appears. Click on the Blood Bank Orders tab and continue.

The other error message that may appear is this:

![](or-3-212-release-notes-vbecs-interface/005.png)

This means that CPRS is having trouble transmitting the order to VBECS. The order has still been filed in Order Entry, the lab part of the order has still been sent to the lab application, and CPRS will transmit the order to VBECS when communications is restored. You only need to call the blood bank if the order is STAT, immediate, or if you need special products.

#### Note: If this is a delayed order, you need not take any action. CPRS will transmit the order to VBECS when communication is restored. You must call the blood bank if the order is for immediate action.