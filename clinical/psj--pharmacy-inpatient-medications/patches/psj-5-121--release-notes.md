---
title: PSJ*5*121 Release Notes-IMO Project
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: IMO Project
app_code: PSJ
app_name: "Pharmacy: Inpatient Medications"
section: CLI
app_status: active
pkg_ns: PSJ
patch_ver: 5
patch_id: PSJ*5*121
group_key: "PSJ:PSJ:5"
file_numbers: []
security_keys: []
menu_options: 1
description: 
audience: 
keywords: 
  - orders
  - clinic
  - order
  - inpatient
  - contents
  - table
  - medications
  - cprs
  - location
  - bcma
page_count: 0
word_count: 3287
section_count: 11
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: April 2006
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Inpatient_Med/psj_5_p121_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Inpatient_Med/psj_5_p121_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=88"
---

> ![](psj-5-121-release-notes-imo-project/001.png)

Inpatient Medications for Outpatients (IMO)

####### Release Notes

PSJ\*5\*121

OR\*3\*215 (CPRS GUI V. 26)

SD\*5.3\*285

PSS\*1\*59 (Released 1/31/2005)

PSJ\*5\*111 (Released 1/31/2005)

PSJ\*5\*112 (Released 5/18/2005)

PSS\*1\*86 (Released 5/18/2005)

April 2006

VISTA Health Systems Design & Development

Table of Contents

*(This page included for two-sided copying.)*

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Functionality Included in IMO](#functionality-included-in-imo)
  - [CPRS General](#cprs-general)
  - [CPRS GUI Orders Tab](#cprs-gui-orders-tab)
  - [CPRS GUI Meds Tab](#cprs-gui-meds-tab)
  - [Inpatient Medications](#inpatient-medications)
- [Evaluate IMO before Implementing](#evaluate-imo-before-implementing)
- [Setting up IMO](#setting-up-imo)
  - [General](#general)
  - [Scheduling](#scheduling)
  - [CPRS](#cprs)
  - [Quick Orders](#quick-orders)
  - [Inpatient Medications](#inpatient-medications-1)
  - [Additional Tips to remember](#additional-tips-to-remember)
- [IMO and BCMA Working Together for Outpatients](#imo-and-bcma-working-together-for-outpatients)
The Inpatient Medications for Outpatients (IMO) project is designed to enable a Computerized Patient Record System (CPRS) V1.0 user to order a unit-dose medication that is dispensed by Inpatient Pharmacy and administered to an Outpatient in a clinic setting. It will also implement the display of those unit-dose orders, IV Fluid (Infusion) orders, and Nursing text orders written in an IMO location under a new display group named Clinic Orders. IMO allows VistA order checks to function for such medication orders. For the purposes of this document, IMO orders are defined as unit-dose medication orders, IV Fluid (Infusion) orders, and Nursing text orders written from an authorized IMO location.
IMO functionality depends on the installation of Scheduling patch SD\*5.3\*285, Order Entry patch OR\*3.0\*215, and previously released Pharmacy patches PSJ\*5\*111, PSJ\*5\*112, PSS\*1\*59 and PSS\*1\*86. In addition to modifying the existing clinic definition *Set up a Clinic* \[SDBUILD\] option, a new *Inpatient Medications to Clinic* \[SD IMO EDIT\] option has been added with SD\*5.3\*285. Through these options, sites can designate specific clinics as IMO authorized locations. CPRS uses this information to determine if an IMO order is allowed for a specified clinic.
IMO orders must be entered through CPRS.
IMPORTANT NOTE: It is recommended that SD\*5.3\*285 be installed immediately prior to or at least on the same day as patch OR\*3\*215 (CPRS GUI v26) in order to prevent the possibility of designating a clinic as an IMO location and/or the implementation of IMO functionality before the installation of OR\*3\*215.
IMPORTANT NOTE: At the time of release, an issue had been identified with expiring medication notifications for IMO orders. The way that expiring medications notification works, in CPRS, is that they are sent based on the display group of the order. Because IMO orders are displayed under the CLINIC ORDERS display group, no expiring meds notification is being performed. This problem will be corrected in OR\*3\*251. If your site makes extensive use of the expiring medication notifications, consider waiting until OR\*3\*251 before implementing IMO.
*(This page included for two-sided copying.)*

# Functionality Included in IMO

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If your site chooses to implement IMO, users will see several changes.

## CPRS General

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Users can change, copy, and renew IMO orders if the user is ordering from an IMO location. Users cannot transfer IMO orders.

## CPRS GUI Orders Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- A new CLINIC ORDERS display group has been created to group IMO orders on the Orders tab.
- Nursing Text Orders entered for an Outpatient at an IMO location will display under the CLINIC ORDERS display group unless it is part of a quick order that has a different display group defined. Existing text orders cannot be used. Create new or copy to new text orders for this location using the display group CLINIC ORDERS.
- When orders are placed from an IMO location for an Outpatient, CPRS will display IV fluid orders and IV Quick Orders under the CLINIC ORDERS group instead of the Infusion group.
- Users can view all IMO orders using one of the two following methods:
1.  Click the Orders tab.
2.  Select the Custom Order View command from the View menu. The Custom Order View dialog box displays.
3.  In the Service/Section pane, click + to expand PHARMACY.
4.  Select CLINIC ORDERS.

    Or
1.  Click the Orders tab.
2.  Select the Custom Order View command from the View menu. The Custom Order View dialog box displays.
3.  In the Service/Section pane, click All Services.
4.  Select Clinic Orders.
- The ordering location will appear in the Location column. Clinic staff and Inpatient staff should be oriented to look in the Location column for the origin of the orders.

## CPRS GUI Meds Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- IMO Nursing text orders do not display on the Meds tab.
- On the Meds tab, IMO orders of all statuses are displayed before active Inpatient orders at the top of the Inpatient Medication Orders panel, with ordering location (clinic) information in the far right column.

## Inpatient Medications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

From either the CPRS Orders Tab or the CPRS Meds Tab, orders written for Outpatients using the IMO functionality are treated like Inpatient orders. They are:

- Filled by Inpatient Pharmacy
- Dispensed by Inpatient Pharmacy
- Displayed by Inpatient Medications in the Active Medications Profile
- Detailed Order View displays the clinic location and appointment date and time for each IMO order

For further information, please refer to the Inpatient Medications documentation. The documentation can be found at <http://www.va.gov/vdl/Clinical.asp?appID=88>

# Evaluate IMO before Implementing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Before deciding to utilize this new IMO functionality, be sure to consider the following:

- Impacts on the Inpatient Pharmacy workload. Is sufficient pharmacy staff available to process and distribute the amount of medications that may be generated by the clinic(s) under consideration? Which clinic groups need to be created and which clinics will be in them? Who will add new clinics to the clinic groups as they are created?
- What changes in policies and procedures are needed to implement the switch from using Outpatient Pharmacy ‘done in clinic’ orders to IMO orders?
- How will clinic staff become aware of new orders? Will you print chart copies in the clinic, use the new orders view alert, use a bingo board, use a routing slip, use verbal communication between provider and nurse, or something else?
- How will Inpatient Pharmacy staff become aware of the new orders? Will you print service copies in the Pharmacy?
- How will Pharmacy know that the patient is moving to either a new clinic location or to an Inpatient location? This is key information to ensure that the medications are being delivered to the current patient location.
- Patient mix in the area you are planning to convert to IMO—Will you have a mixture of Inpatients, Outpatients and "to be admitted" patients as you would in recovery room (PACU) and dialysis? How will you handle patient movement so all patient orders to be administered in the IMO unit are clearly distinguished from Inpatient ward orders?
- How will the communication be handled when new clinics are set up – so that Pharmacy can appropriately set up for IMO, if needed?
- Ultimately – Will having full order checks and meds viewable in the medication profile make these impacts acceptable?

  Now that you have decided to use IMO, you have the option of allowing the orders to survive an admission. Before you decide on this, consider:
- What is the likelihood that a patient will be admitted to the hospital during this clinic’s treatment?
- If you decide to NOT Auto-DC on admission:
- Will having both IMO and Inpatient orders display together on the Meds tab cause too much confusion?
- Will having Inpatient orders in two locations on the orders tab cause too much confusion?
- IMO orders are not specifically broken out in the Pharmacy Inpatient Medications Patient Profile view. Will this cause confusion for pharmacists when attempting to process a patient’s order? Will your Pharmacist be able to use the Non-Verified pending orders option to process orders by clinic?
- If you do not set the display in BCMA parameter to yes, will having medications on the Meds tab that do not display in BCMA cause nursing providers to assume there is a discrepancy?
- If you do use BCMA, how will nursing providers know which meds are to be administered in clinic and which are for the ward nurse?
- How will users be trained to understand these display differences?
- If you decide to auto-discontinue IMO orders upon admission, how will you ensure the clinic nurses have seen and processed all orders before admission?
- If you decide for some clinics TO Auto-DC and other clinics to NOT Auto-DC, will the differences generate too much confusion?

  How will you document medication administration in IMO clinics?
- If you decide to use the MAR:
- Will you use the 24-hour MAR and MAR labels?
- Do you need to request printers and printer stock for your IMO clinics?
- Will nurses need to be re-trained on MAR procedures since many have forgotten since BCMA was implemented?
- If you decide to use progress note templates:
- Med administration documentation is in CPRS for easy review by Inpatient nurses and EPRP reviewers (if patient is admitted).
- No need to purchase printers, label stock or BCMA PCs and scanners.
- If you decide to use BCMA:
- How will care be coordinated between the Inpatient nurse and the Clinic nurse?
- Will having some clinic orders display in BCMA and some not be a problem?
- How will medications administered before admission be documented?

# Setting up IMO

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All required patches must be installed.

- SD\*5.3\*285
- OR\*3\*215 (CPRS GUI v26)
- PSJ\*5\*111 (released 1/31/2005)
- PSJ\*5\*112 (released 5/18/2005)
- PSS\*1\*59 (released 2/13/2005)
- PSS\*1\*86 (released 5/18/2005)

IMPORTANT NOTE:

- SD\*5.3\*285 patch needs to be installed immediately prior to or at least on the same day as patch OR\*3\*215 (CPRS GUI v26).
- After installation of OR\*3\*215, the Inpatient Meds for Outpatient (IMO) functionality included in patch SD\*5.3\*285 can be activated.
- Clinics should not be activated for IMO prior to installation of OR\*3\*215 and a thorough assessment of the clinic and work areas at the site.

## General

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Decide in which clinics (Hospital locations) you will implement IMO. Consider:

- Select one clinic to use as a prototype
- Start with a low volume clinic

## Scheduling

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Designate the clinic as an IMO location by setting the ADMINISTER INPATIENT MEDS? field (#2802) to YES, using either:

- *Set up a Clinic*
- *Inpatient Medications to Clinic*

## CPRS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you wish to use the Meds tab to place IMO orders:

- Using the *Edit Parameter Values* option: *add*, or have your IRM staff add, the order dialog \[PSJ OR PAT OE\] to the menu you have assigned to the Outpatient patient status under the \[ORWDX NEW MED\] parameter.
- Text orders, particularly those as part of a protocol that further define how/when/where/rate/etc. a medication is administered, should be evaluated to make sure they can be easily understood.
- Remember, the Inpatient Medications order and the text order that supports it will not always display in sequential order. Therefore, the text order should be worded to include sufficient information for the staff to determine which text order(s) support which medication orders, such as using an orderable item in the text order.
- If Local Display groups have been created and you wish for these to produce a headlight in Care Management under the TX column, you must add them as a member of the Nursing display group.

  Considerations/setup for the CLINIC ORDERS display group on the Orders tab:
- Choose what sequence number to assign to the Clinic Orders. Consider placing it close to the other medication display groups.
- Make an entry in the ORWOR CATEGORY SEQUENCE parameter at the package or system level depending on which level the site uses:
- Note: If your site uses the Package level settings, someone at your site will need to add Clinic Medications to the Package level settings. To change the parameter at the Package level, the user making the change must be in programmer mode.
- If you choose to view the nursing text orders under the CLINIC ORDERS display group, you will need to either view Pharmacy service/section or expand pharmacy to select the new CLINIC ORDERS service/section.
- Query Tool: If you are using queries to define orders by display groups, you will need to include the new display group for CLINIC ORDERS.

## Quick Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- Quick orders must be evaluated based on the new processes to determine if they need to be edited for use in IMO clinics.
- If patients are shared between locations, such as Inpatients receiving dialysis in the Dialysis Unit, it is helpful to use quick orders and include the ordering location in the provider comments. This helps reinforce where the medication should be administered, in addition to the Clinic Orders display group and the Location column.
- For all of the following examples we will start on the Order Menu Management \[ORCM MGMT\] option in VistA.
- Setting up Nursing Generic Text Orders
1.  Select QO Enter/Edit Generic Orders
2.  Enter Generic Order Name at the Select Generic Order Name prompt
3.  At the Type of Generic Order prompt select Nursing
4.  Enter Display Text (optional)
5.  Continue through the rest of the prompts and answer appropriately for your site.
6.  The text instructions are entered at the Instructions: prompt.
- The Type of Display Group prompt is used to determine under which display group text orders will appear. If the user setting up IMO enters a group other than nursing into this field, the text order will not follow the IMO rules.
- To add text orders to an order set, use these steps:
1.  Select ST Enter/edit order sets.
7.  Enter the order set name.
8.  If entering a new order set, the user can copy the contents of another order set into the new order set.
9.  At the Select Component Sequence#: prompt the user would select what sequence number they want the text order to appear in the order set.
10. At the Item prompt the user would select name of the text order to add to the order set.

## Inpatient Medications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Make the appropriate configuration changes in the new menu option: Clinic Definition \[PSJ CD\] under the *PARameters Edit Menu* \[PSJ PARAM EDIT MENU\] option.

- Determine the stop date calculation for each IMO clinic. Refer to the Inpatient Medications Technical Manual/Security Guide for a full explanation of the stop date calculation for unit-dose orders.
- Determine the desired Auto-DC behavior for each clinic.
- Determine if you want this clinic’s orders to display in BCMA.
- The option of setting the clinic location to IMO can be given to others outside of HAS/MAS. This is helpful for the Pharmacy ADPAC to have so they can do all steps in setting up the IMO clinic.

## Additional Tips to remember

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To successfully write Inpatient-medication orders for Outpatients, the Outpatients must meet at least one of the following criteria:

- They must have a scheduled appointment at an authorized hospital location for the current day or a day in the future.
- They must be currently checked in at an authorized Outpatient hospital location or the appointment must be for a date in the future.
- If patients do not meet either of these criteria, you can create a new visit for them at an authorized hospital location.

  IMO should be used as it was designed.
- IMO is designed to order Inpatient Medications for an Outpatient through CPRS, dispense the order from Inpatient Pharmacy, and administer the medication in a clinic.
- It is not intended to provide a method to dispense medications to be taken home for use at a later time. Medications for home use should continue to be ordered via the Outpatient Order Dialog in CPRS and Outpatient Pharmacy.
- IMO is not designed for ordering medications for Inpatients that happen to be in an IMO location (e.g. PACU or dialysis).

  The Clinic Definitions parameters will impact the display of orders.
- Stop date calculations will determine how long the order will appear active on the medication profile in Inpatient Medications. Refer to the Inpatient Medications V. 5.0 documentation for details on how stop dates are calculated.
- The Auto-DC parameter will determine whether the order will remain active if a patient is admitted to an Inpatient location. You may need to set a facility policy regarding whether an order placed in an Outpatient clinic should be administered after admission, or this may need to be defined based on the clinic. For example, you may wish to have chemotherapy or hemodialysis orders remain active due to the complexity of having to rewrite them after admission.
- The send to BCMA parameter is dependent upon the setting of the Auto-DC parameter and the status of the patient. If the IMO location Send to BCMA parameter is set to YES, and the Auto-DC parameter is set to NO, and the patient has a status of Inpatient, the medication order will display in BCMA and administration may be recorded via BCMA functionality. Conversely, if any of the three criteria is not met, the order will not display in BCMA for recording of the administration. In other words
- Display in BCMA requires all 3 conditions: Inpatient status; Auto-DC on admission=No; Send to BCMA=Yes

| Criteria                | Parameter              | Parameter | Setting | Display in BCMA?                      |
|-----------------------------|----------------------------|---------------|-------------|-------------------------------------------|
| Patient Status = Outpatient |                            | BCMA Display  | No          | No                                        |
| Patient Status= Outpatient  |                            | BCMA Display  | Yes         | Possibly, see “CAN BCMA BE USED WITH IMO” |
| Patient Status= Inpatient   | Auto-DC on Admission= No   | BCMA Display  | Yes         | Yes                                       |
| Patient Status= Inpatient   | Auto-DC on Admission = Yes | BCMA Display  | Yes         | No                                        |

*(This page included for two-sided copying.)*

# IMO and BCMA Working Together for Outpatients

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

BCMA can be utilized for IMO orders for Outpatients in a clinic location but it takes some work and a lot of process changes.

One test site has implemented this as follows

1.  Coordinate with MAS to set up “no count” wards and admit patients to those wards.
2.  Essentially, you have a clinic appointment that is made for the date of a procedure. So the orders that are written for that procedure are usually done ahead of time in the ambulatory care area, and they expect these orders to be performed in the clinic in the future. And you associate those orders with that visit.
3.  On the day of that visit, the patient is checked into a non-count ward that we have created. This allows some billing procedures to go through.
4.  The patient is also checked into the clinic. But they are not checked into the clinic right away, usually.
5.  That patient is checked into and out of the clinic as well as being checked into the non-count ward. Then, if the settings are correct, this allows the orders to appear in BCMA.
6.  Now, the AOD has to discharge these patients from the non-count clinic. We have found that for billing things to occur correctly that when they discharge them from this clinic, they do it one minute after the admission was made. This is a key step and the administrative staff must be very strong and accurate in patient movements.
7.  The second step is that they have to delete that admission before midnight. This keeps it from showing up on G&L reports.
8.  In addition to this, they also usually send a list of these patients for whom they’ve done this to someone in DSS that also reviews the orders with someone from billing—just to make sure that no extraneous charges slip through.

Additional information related to the IMO project can be found at <span class="mark">REDACTED</span>  
*(This page included for two-sided copying.)*