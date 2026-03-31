---
title: OR*3*434 Release Notes CPRS GUI 31A
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: CPRS GUI 31A
app_code: CPRS
app_name: Computerized Patient Record System
section: CLI
app_status: archive
pkg_ns: OR
patch_ver: 3
patch_id: OR*3*434
group_key: "CPRS:OR:3"
file_numbers: []
security_keys: []
menu_options: 0
description: <span class="smallcaps">CPRS GUI</span> v<span class="smallcaps">31</span>a <span class="smallcaps">(Patch OR\3.0\434)</span><span class="smallcaps">Release Notes</span>
audience: 
keywords: 
  - span
  - cprs
  - class
  - return
  - clinic
  - anchor
  - order
  - legacy
  - parameter
  - appointments
page_count: 0
word_count: 1314
section_count: 0
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: October 2017
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)_Archive/or_30_434_rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)_Archive/or_30_434_rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=338"
---

<span class="smallcaps">CPRS GUI</span> v<span class="smallcaps">31</span>a <span class="smallcaps">(Patch OR\*3.0\*434)</span><span class="smallcaps">Release Notes</span>

![](or-3-434-release-notes-cprs-gui-31a/001.png)

<span class="smallcaps">October 2017</span>

Office of Information & Technology (OI&T)

Product Development (PD)

<span id="_Toc497395160" class="anchor"></span>Table of Contents

<span id="_Toc497395161" class="anchor"></span>Installation Requirements

<span id="_Toc497395162" class="anchor"></span>Required Patches

Below is a list of patches that you must verify are properly installed on your system before OR\*3.0\*434 can be installed:

- OR\*3.0\*421
- OR\*3.0\*423
- OR\*3.0\*424
- OR\*3.0\*425
- OR\*3.0\*436
- XU\*8\*659
- XWB\*1.1\*64
- FileMan 22.2 must be installed in the environment.

Although not required for the patch to install, there are many other patches that will need to be installed so that this version of the CPRS GUI will run properly. Please see the *CPRS v31a (OR\*3\*434) Deployment, Installation, Back-Out, and Rollback Guide* for further instructions.

<span id="_Toc497395163" class="anchor"></span>Release Method

CPRS GUI v31a consists of the OR\*3.0\*434 patch, documentation, and a GUI executables listed below:

- Patch OR\*3.0\*434
- The CPRS GUI: cprschart.exe

The main change in CPRS v31a is to implement two-factor authentication (2FA) using a user’s PIV card to access CPRS. Two other features in the CPRS v31a version are support for Return to Clinic (RTC) functionality so that a provider can let the scheduler know when the patient should return and support for the Joint Legacy Viewer (JLV), which will replace VistaWeb to view remote patient data.

For specific information on the CPRS GUI v31a installation, please see the *CPRS v31a (OR\*3\*434) Deployment, Installation, Back-Out, and Rollback Guide*.

<span id="_Toc497395164" class="anchor"></span>Known <span id="known_issue" class="anchor"></span>Issue

- Return to Clinic Additional Information Parameter: An issue was identified during testing with the Division level usage of the Additional Information field in the Return to Clinic dialog. The Division level is being determined by the division to which the user is signed in, rather than the division to which the clinic belongs.

  Workaround: Currently, the only workaround is to NOT use the Division level setting for this parameter. Use the System level setting.
- Numerical Values Not Displaying on Lab Graphs: When the CPRS team moved to a new version of the software used to create the CPRS GUI, a problem was found where the option to display numerical values for the Lab graph is not working correctly. If a user checks the option to display values, they will not display.

  Workaround: Lab values are available as they always are in the lab results. Users can also hover over a point on the graph and it will display the numerical value.

<span id="_Toc497395165" class="anchor"></span>New Features in CPRS v31a

There are several new features in CPRS v31a as described below.

<span id="_Toc497395166" class="anchor"></span>Two-Factor Authentication

To comply with the directive to add enhanced security to VistA and related applications, CPRS is implementing two-factor authentication (2FA) to access the application. For CPRS, 2FA means that to log in to CPRS the user must have something and the user must know something. In this case, the something the user has is his or her Personal Identification Verification (PIV) card, and the something the user knows is his or her Personal Identification Number (PIN) for his or her PIV.

This means that to log in to CPRS, the user will launch CPRS, insert or have their already PIV card inserted into a reader, and will then enter their (PIN) to get into CPRS.

<span id="_Toc497395167" class="anchor"></span>Return to Clinic

The Return to Clinic (RTC) feature enables providers to place an order requesting that scheduling set up a return appointment for the patient. This effort includes changes from both CPRS for the ordering and scheduling for other features.

> **NOTE:** The Return to Clinic dialog will only be accessible if the new Scheduling enhancements are in place, which will be released in patch SD\*5.3\*671. CACs can create Quick Orders and add the Return to Clinic Order Dialog to any menu before the SD patch is installed. If a user tries to access the Return to Clinic Order Dialog before the SD patch is installed, they will see an error message in CPRS stating the Order Dialog cannot be use until the SD patch is installed.

In CPRS, the RTC feature enables providers to create an order that will be sent to the scheduling package requesting one or more additional appointments be created for the patient.

Providers select or enter the following information:

- Clinic: The clinic the patient should return to
- Date: The return to clinic date
- Time Sensitive: Whether the appointment is Time-Sensitive
- Not Time Sensitive: If the appointment is not time-sensitive, the order will read “on or around”.
- Time Sensitive: If the appointment is Time Sensitive, the order text will read “no later than”.
- Number of Appointments: Providers enter the number of future appointments they would like to request. The maximum number of appointments is 60.
- Interval in day(s): Providers can enter the number of days between appointments. For example, a provider may want to request a number of appointments 14 days apart. The maximum interval is 30 days.
- Prerequisites (check all that apply): This item is available only if the site puts items into a parameter where prerequisites are defined. For example, if nothing is put in the parameter, the user will not have any selections in this field. However, if the site puts in labs or radiology, the provider can select as many of those items as apply.
- Comments: This is where the user can enter their own comments for the scheduler to see.
- More Information: (Not Editable) This field enables the site to display information they would like the provider to see while placing an order to request a return appointment. The text in this field is entered through a parameter, not entered by the provider.

As the user makes selections, an order description with the details of the order is created at the bottom of the dialog for the user to review.

Return to Clinic also has a notification, APPOINTMENT REQUEST CANCELLED, that tells the user if the order is discontinued. Use of this notification is optional, but site will have to turn on the alert if they want their users to receive it.

<span id="_Toc497395168" class="anchor"></span>Support for Joint Legacy View

The Joint Legacy Viewer (JLV) is the technology that will replace the VistaWeb as a way to view remote data. JLV will not be implemented with CPRS v31a, but coding has been done so that when your site chooses to implement JLV, CPRS is ready to make the changes needed.

The Joint Legacy Viewer (JLV) is a new way to view remote data and will eventually replace VistaWeb. JLV is available now. Some sites may not switch to JLV until VistAWeb is decommissioned, while others may choose to transition sooner. This transition should be made in collaboration with local Informatics staff and the JLV team.

CPRS v31a has a new parameter, ORWRP LEGACY VIEWER LABEL, to enable sites to change the text that appears on the button that now reads “VistaWeb” if that is how the site was set up.

<span id="_Toc497395169" class="anchor"></span>New Parameters

- Return to Clinic Parameters
- OR SD DIALOG PREREQ (prerequisites for appointments, such as labs, vitals, etc.)

Here is the listing of prerequisites in VistA.

> Select PARAMETER DEFINITION NAME: OR SD

> 1 OR SD ADDITIONAL INFORMATION RTC Order Dialog Additional Information

> 2 OR SD DIALOG PREREQ RTC Order Dialog Prerequisites

> CHOOSE 1-2: 2 OR SD DIALOG PREREQ RTC Order Dialog Prerequisites

> ------ Setting OR SD DIALOG PREREQ for System: TEST.DAYTON.MED.VA.GOV ------

> Select Instance: ?

> Instance Value

> -------- -----

> 1 LABS

> 2 VITALS

> 3 CONSULTS

> 4 NOTES

> 5 ENCOUNTER

> 7 Radiology

> 8 A1C lab

![](or-3-434-release-notes-cprs-gui-31a/002.png)

- OR SD ADDITIONAL INFORMATION (This parameter allows sites to have additional guidance or other important information to show in the dialog. For example: some clinics require consults rather than appointments.) Below is an example with example text. Nothing will display in this field unless the site enters something for the parameter value.

> **NOTE:** This parameter has a known issue. Please see the explanation in this document under [*Known Issue*](#known_issue).

![](or-3-434-release-notes-cprs-gui-31a/003.png)

- Med Order Button
- CPRS MOB DLL Name enables site to put the name of the DLL that should be used for the Med Order button, which is a feature used by nurses in the Bar Code Medication Administration (BCMA) and is also related to the One-Step Clinic Administration feature in CPRS.
- Joint Legacy Viewer
- ORWRP LEGACY VIEWER LABEL enables sites to change the label on the VistaWeb button to something else, such as JLV for Joint Legacy Viewer.