---
title: Veteran's Crisis Line Version 1 User Guide
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: 
app_code: YS
app_name: Mental Health
section: CLI
app_status: active
pkg_ns: YS
patch_ver: 1
patch_id: YS*1
group_key: "YS:YS:1"
file_numbers: []
security_keys: []
menu_options: 0
description: The purpose of this user manual is to describe how to use the Department of Veterans Affairs (VA) National Veterans Crisis Line (VCL) Application. The Application replaces the manual call log (paper log documents) and allows for a seamless transition from VA Suicide Prevention Hotline to Suicide Pre
audience: 
keywords: 
  - veteran
  - span
  - call
  - calls
  - class
  - line
  - table
  - crisis
  - contents
  - anchor
page_count: 0
word_count: 13270
section_count: 39
table_count: 5
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: December 2014
revision_count: 5
revision_newest: 12/19/2014
revision_oldest: 6/14/2013
docx_url: "https://www.va.gov/vdl/documents/Clinical/Mental_Health/vcl_user_guide.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Mental_Health/vcl_user_guide.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=78"
---

---
title: <span id="_Toc387753538" class="anchor"></span>Department of Veterans Affairs
---

Veterans Crisis Line (VCL)

![](veteran-s-crisis-line-version-1-user-guide/001.png)

User Guide

December 2014

Revision History

|            |         |                                                                                                                                                                      |                                    |
|------------|---------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------|
| Date       | Version | Description                                                                                                                                                          | Author                             |
| 12/19/2014 | 1.4     | Added updates to Introduction section, added updated screens, added updated screens to Call Synopsis section.                                                        | <span class="mark">REDACTED</span> |
| 11/4/2014  | 1.3     | Added detail to “Administrator options for Reporting” section. Added figure captions and list of figures.                                                            | <span class="mark">REDACTED</span> |
| 7/5/2014   | 1.2     | Rewrite document based on Increment 3 code base and application changes.                                                                                             | <span class="mark">REDACTED</span> |
| 6/4/2014   | 1.1     | Added [Running Ad hoc Reports and](#_Toc389663552) [Exporting an Ad hoc Report to Excel sections to “Administration Options for Reporting” section.](#_Toc389663553) | <span class="mark">REDACTED</span> |
| 6/14/2013  | 1.0     | Initial Version                                                                                                                                                      | <span class="mark">REDACTED</span> |

Table of Contents

List of Figures

# Introduction to the Veterans Crisis Line Application


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction to the Veterans Crisis Line Application](#introduction-to-the-veterans-crisis-line-application)
  - [Purpose](#purpose)
  - [Overview](#overview)
  - [History](#history)
- [Accessing the VCL Call Log](#accessing-the-vcl-call-log)
- [Acute Care Risk Assessment and Log Sheet](#acute-care-risk-assessment-and-log-sheet)
  - [Responder Info](#responder-info)
  - [Patient Lookup](#patient-lookup)
  - [Caller Info](#caller-info)
  - [Veteran Info](#veteran-info)
  - [Acute Care Risk Assessment](#acute-care-risk-assessment)
  - [Suicidal Desire and Suicidal Intent](#suicidal-desire-and-suicidal-intent)
  - [Suicidal Capability](#suicidal-capability)
  - [Buffers Connectedness](#buffers-connectedness)
  - [Follow up Questions](#follow-up-questions)
  - [Call Synopsis](#call-synopsis)
  - [Self-Directed Violence](#self-directed-violence)
  - [Outcome of Call](#outcome-of-call)
- [The Suicide Prevention Coordinator Response Application](#the-suicide-prevention-coordinator-response-application)
  - [Open Hotline Calls](#open-hotline-calls)
  - [Open Hotline Call](#open-hotline-call)
- [Acute Care Risk Assessment and Log Sheet Changes](#acute-care-risk-assessment-and-log-sheet-changes)
  - [Response Form](#response-form)
- [Creating TIU Progress Notes](#creating-tiu-progress-notes)
- [Admin Application](#admin-application)
  - [All Administrative Options](#all-administrative-options)
  - [SSA Functions:](#ssa-functions)
  - [Call List](#call-list)
  - [Search for Open or Closed Calls by Date](#search-for-open-or-closed-calls-by-date)
  - [Search for Calls by Date, SSN, Name, and Phone](#search-for-calls-by-date-ssn-name-and-phone)
  - [Calls Needing Compassionate Care Follow-up](#calls-needing-compassionate-care-follow-up)
  - [Calls Needing Health Tech Follow-up](#calls-needing-health-tech-follow-up)
  - [Enter Calls](#enter-calls)
  - [Call List](#call-list-1)
  - [Search for Open or Closed Calls by Date](#search-for-open-or-closed-calls-by-date-1)
  - [## Search for Calls by Date, SSN, Name and Phone](#search-for-calls-by-date-ssn-name-and-phone-1)
  - [Calls Needing Compassionate Care Follow-up](#calls-needing-compassionate-care-follow-up-1)
  - [## Calls Needing Health Tech Follow-up](#calls-needing-health-tech-follow-up-1)
  - [## Users List](#users-list)
  - [Adding Users](#adding-users)
  - [Deactivating Users](#deactivating-users)
  - [Admin Permissions for Admin Applications](#admin-permissions-for-admin-applications)
- [Administrator Options for Reporting](#administrator-options-for-reporting)
  - [Creating Ad-Hoc/Custom Reports from Scratch](#creating-ad-hoccustom-reports-from-scratch)
  - [![](veteran-s-crisis-line-version-1-user-guide/082.png)](#veteran-s-crisis-line-version-1-user-guide082png)
  - [Adding Parameters to Existing Reports:](#adding-parameters-to-existing-reports)

## Purpose 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this user manual is to describe how to use the Department of Veterans Affairs (VA) National Veterans Crisis Line (VCL) Application. The Application replaces the manual call log (paper log documents) and allows for a seamless transition from VA Suicide Prevention Hotline to Suicide Prevention Coordinator (SPC).

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VCL application provides an electronic version of the call log. VCL also stores information from hotline calls, which provides the ability to retrieve and view call information as needed.

The VCL application has three components:

- Log Application used at the VA Suicide Prevention Hotline by Health Services Specialist (HSS) to log calls
- Response Application used at VA facilities by Suicide Prevention Coordinators (SPCs) to document referrals and save them in the Computerized Patient Record System (CPRS) as Progress Notes
- Admin Component which is nested with the Health Techs (HT) application. This component is used by hotline administrators and Social Services Assistants (SSA) to audit and administer the system.

#### In the Admin view, the Log Application stores call information that can later be used for data collection and reporting purposes.

2.  In the Admin view, the Log Application provides a mechanism for hotline staff to view Veteran demographic information. The application also provides the risk assessment module and the ability to identify the VA Medical Center (VAMC) closest to the caller’s physical location.
3.  In the admin view, the Log Application provides a means to refer a caller to a VAMC for follow-up care. The referral is directed to the VA Medical Center’s SPC in real time.
4.  The SPC Response Application allows the ability to document the hotline referral in CPRS in the form of a Text Integration Utility (TIU) Progress Note.
5.  The SPC Response Application ensures all progress notes have a common note title.
6.  The SPC Application is automatically updated when a SPC completes the referral process.
7.  In all applications there are prohibited characters that when entered in sequence will return a page fault. Entries such as \<%, @#, \<b\>, and \</i\> would cause the error to occur.
8.  Some users, according to their roles, will need the ability to have more than one application open at one time (i.e. Hotline and Admin applications open at the same time). Having two or three applications open in the same session is allowed and will not cause any issues. However, in internet explorer (IE), you cannot open multiple sessions of the same application, it will cause a page fault error. If there is a need for a user to do this, there is a way within IE to perform this action and instructions are provided in the document attached below.

![](veteran-s-crisis-line-version-1-user-guide/002.png)

\*\*NOTE: Throughout this document you will see the title HSS which corresponds to Call Responders within the Hotline application and Social Services Assistant (SSA) which corresponds to Health Tech’s within the ADMIN Application. \*\*

## History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VCL Project is an important function to support recent suicide prevention legislation. The Department of Veterans Affairs (VA) has begun operation of the national suicide prevention hotline (now called VCL) to ensure that veterans with emotional crises have round-the-clock access to trained professionals. The VA is partnering with the Substance Abuse and Mental Health Services Administration (SAMHSA) of the Department of Health and Human Services (HHS) and the National Suicide Prevention Lifeline to operate the national hotline. Veterans can call 1-800-273-TALK (8255) and press “1” to reach the VA hotline, which is staffed by mental health professionals 24/7/365 in Canandaigua, N.Y. who work closely with the callers’ local VA Suicide Prevention Coordinators and mental health providers to help the callers.

Recent Legislation has been passed requiring VHA to take specific actions in the effort to prevent Veteran suicides. The following summary is by Laura Strickler, with reporting from Sarah Fitzpatrick in Washington.

“On November 6, 2007, President Bush signed into law the Joshua Omvig Veterans Suicide Prevention Act. It’s named after a soldier who committed suicide in Grundy County, Iowa, in December 2005, after serving an 11-month tour in Iraq. The bill requires the Department of Veterans Affairs to meet deadlines in providing the following services:

- Train VA staff on suicide prevention and mental health care
- Staff each VA medical facility with a suicide prevention counselor
- Screen soldiers who seek care through the VA for mental health needs
- Support outreach and education for veterans and their families
- Research the most effective strategies for suicide prevention
- Create a peer support counseling program so veterans can help other veterans
- However, while the bill requires the VA to provide these services, it provides no funding.

On February 6, 2008, Representative Leonard Boswell (D-IA) and Representative Robin Hayes (R-NC) introduced the Armed Forces Suicide Prevention Act (H.R. 5223). This bill is focused on Department of Defense implementing a comprehensive suicide prevention program within all branches in the military, including National Guard and the Reserves. The Air Force implemented a suicide prevention program in the 1990’s. By 2002, the suicide rate had declined by 33% and researchers found a decrease in violent crime and family violence after program implementation. This bill is designed to help the VA and Department of Defense deal with the increase in mental health needs of Iraq and Afghanistan service personnel.

Both VA Central Office and Congress want periodic reports relating to Veteran suicide and suicide prevention efforts. Tracking cases may also allow for best practice identification.

The Suicide Prevention Hotline Web Application went live, nationwide, on 6/9/2009 and the first update was put into production on 11/22/2010.

# Accessing the VCL Call Log

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Crisis Line Health Science Specialists (HSS) use the VCL Application to record all calls being received.

1.  Enter <span class="mark">REDACTED</span> in the Internet Explorer (IE) address bar to access the VCL web application.
2.  A Security Disclaimer page will appear on screen. User will select the I Agree button and continue to login page. (see below) The application now has a timeout feature enabled after 30 minutes of inactivity. If the user is inactive on the application for 30 minutes they will receive a warning that the application will terminate in two minutes, if they want to continue working they can click continue working.

> \*\*NOTE: If an HSS has an active call in progress and leaves their machine to consult on the rescue it is imperative that they SAVE/SUBMIT the call before leaving the record – the application does not store “in progress” work so if they are gone for up to the 30 minute time period the entire record will be lost.

3.  Select the Veterans Integrated Service Network (VISN) (e.g., VISN 2) and site (e.g., Upstate NY HCS) and then enter the access and verify code, which is the same as your CPRS/ Veterans (Health) Information Systems and Technology Architecture (VistA) access and verify code pair.
4.  When VistA is down in Canandaigua, all HSS personnel with Capri access should use their access and verify code for Capri to sign on to the Veterans Crisis Line Application. Those without Capri access will have to use the word document option.
5.  Only users given access to the Veterans Crisis Line Application will be able to access the system. The list of users with approved access is maintained by the Veteran’s Crisis Line Call Center, Canandaigua, NY. Administrators at Canandaigua will be assigned to add new users or deactivate a user for HSS and SSA. Requests and approvals for SPC additions or deletions will be sent to the Administrator / Clinical Application Coordinator (CAC) @ Canandaigua and once written approval is received from site lead, requested changes will be made.

![](veteran-s-crisis-line-version-1-user-guide/003.png)

<span id="_Toc406762375" class="anchor"></span>Figure 1: Accessing the VCL Call Log

![](veteran-s-crisis-line-version-1-user-guide/004.png)

<span id="_Toc406762376" class="anchor"></span>Figure 2: VistA Login

*\*\*Note: Once you have logged in, you may save the web address in the IE “Favorites” menu for future ease of access.*

# Acute Care Risk Assessment and Log Sheet

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once you have successfully signed on to the application you will have access to the Report Menu.

![](veteran-s-crisis-line-version-1-user-guide/005.png)

<span id="_Toc406762377" class="anchor"></span>Figure 3: Report Menu

Reports Menu includes the Compassionate Care Call List and the Search for My Calls by Date.

![](veteran-s-crisis-line-version-1-user-guide/006.png)

<span id="_Toc406762378" class="anchor"></span>Figure 4: Reports Menu Links

Click on Compassionate Care Call List and all Veterans that agreed to a two week follow-up will appear two weeks after the original call was made (see screen below).

Choose responder from the drop-down list available. When you click on View Details a *<u>view only</u>*Hotline Call Detail screen appears with all the original call information. The HSS calls the Veteran and clicks on Record Follow-up and enters the results of the call in the Document Follow-up field (screen below). The HSS is required to attempt to reach the Veteran three times if no answer. If a HSS is not able to connect with the individual they will leave a message and click the Save follow-up button.

If the HSS does contact the veteran on the first or second call, then the HSS would enter the details of the call in the Document Follow-up and click the Close Follow-up and then click Save Follow-up and the Document would be permanently closed and removed from the list. If after three attempts the HSS has not reached the Veteran, they will document that they were unable to contact the Veteran and click Save Follow-up and the document will be permanently closed automatically because it is the 3<sup>rd</sup> call.

![](veteran-s-crisis-line-version-1-user-guide/007.png)

<span id="_Toc406762379" class="anchor"></span>Figure 5: Record Follow-Up

![](veteran-s-crisis-line-version-1-user-guide/008.png)

<span id="_Toc406762380" class="anchor"></span>Figure 6: Document Follow-up

When the Save Follow-up button is clicked in the Record Follow-up the information appears at the bottom of the Hotline Call Detail screen on all view detail screens for each of the calls made (see below). All notes will also appear next to the name on the Compassionate Care Call List screen until it is closed (See below).

![](veteran-s-crisis-line-version-1-user-guide/009.png)

<span id="_Toc406762381" class="anchor"></span>Figure 7: Compassionate Care Follow-up

![](veteran-s-crisis-line-version-1-user-guide/010.png)

<span id="_Toc406762382" class="anchor"></span>Figure 8: Compassionate Care Call Detail

To return to Call Log click Return to Call List and then Return to Call Log.Click on Search for My Calls by Date and the following screen is displayed. This screen allows you to search for prior referrals by date. You will be able to open and close in a *<u>view only</u>* format.

![](veteran-s-crisis-line-version-1-user-guide/011.png)

<span id="_Toc406762383" class="anchor"></span>Figure 9: Search for My Calls between Dates

To return to the Call Log click on Return to Menu and then Return to Call Log.

## Responder Info

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

*Note: Throughout the Log Website, the \*=required field denotes a section that must be completed.*

At the beginning of each shift, the HSS is required to sign into the Acute Care Risk Assessment & Log Sheet.

1.  Enter your five-digit Phone Station Line (this is the phone extension that the HSS is using).
2.  Your full name is entered in the Responder Name box on the first line of the log sheet when you sign-in.
3.  Click on the Set Call Time button to the left of the phone station line. Set Call Time needs to be clicked at the beginning of every call; the date and time of the call will be automatically populated.
4.  Click on Source of Call dropdown that includes:
    - Hotline 800
    - WT VAMCs
    - WT MOUs
    - Chat referral
    - Email referral
    - WT Central Office
    - WT Congress/White House
    - WT Civilian Facility
    - Coaching into Care
    - Fax-calls from Backup centers
    - WT Homeless Hotline
    - Compassionate Call Backs
    - Hotline International Calls
    - Care Givers
    - Text Transfer
    - Text
    - Vets for Warriors
    - VCL Back-up Centers
    - Facebook
    - WT VBA
    - Women Vets Line
    - Korea 118
    - MCL

![](veteran-s-crisis-line-version-1-user-guide/012.png)

<span id="_Toc406762384" class="anchor"></span>Figure 10: Source of Call Drop-Down

## Patient Lookup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patients can be identified one of two different ways.

Search Using combination of State/Facility/Name:

- User clicks Select State and selects the patients state from the drop down entries
- User clicks Select Site and then picks the patients facility
- In the Name Search field, User enters:
- Enter the Veteran’s last name, comma (no spaces) and part of the Veteran’s first name, or first letter of the last name and the last 4 digits of the Social Security Number (SSN)
- Click Find Veteran. A list of potential matching patients will be shown in the box. (If there are more names available than shown in the scroll box, click the down arrow button to see them.)
- Click on the Veteran’s Name. The Veteran’s date of birth and SSN will appear to the right to verify the Veteran selection.
- If correct, click Select Veteran. The Veteran’s name, SSN and age will be automatically populated on the Acute Care Risk Assessment & Log Sheet.

Search Using Name – the Search Using Name is the most commonly used Search:

- User enters the Veteran’s last name, comma (no spaces) and part of the Veteran’s first name, or first letter of the last name and the last 4 digits of the SSN
- Click Find Veteran. A list of potential matching patients will be shown in the box. (If there are more names available than shown in the scroll box, click the down arrow button to see them.)
- Click on the Veteran’s Name. The Veteran’s date of birth and SSN will appear to the right to verify the Veteran selection.
- If correct, click Select Veteran. The Veteran’s name, SSN and age will be automatically populated on the Acute Care Risk Assessment & Log Sheet.

> ![](veteran-s-crisis-line-version-1-user-guide/013.png)

<span id="_Toc406762385" class="anchor"></span>Figure 11: Select Veteran

## Caller Info

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Caller Phone \# is a required field\*, the Caller Phone number is a 10 digit number with no dashes or spaces and can be 15 digits if international \# is checked. If the “international \#” field is checked, this field can also be zero entries (e.g. 011 entries). Once you have entered the number, HSS should Check for Previous Calls by clicking the box. When clicked the following box will appear. Also, when you click Open Call a *read only* view of the prior calls will be displayed.

![](veteran-s-crisis-line-version-1-user-guide/014.png)

<span id="_Toc406762386" class="anchor"></span>Figure 12: Check for Previous Calls

The Caller Name is a required field\* and is free text. Callers may not always give their full name. If only a first name or part of a name is available, you can still enter that information in the field.

The Caller is Veteran field is only checked when the caller is a Veteran.

The Relationship to Vet is a required\* field and has a drop-down box that includes the following selections:

1.  Vet (self)
2.  Family Member
3.  Friend
4.  Non Vet
5.  Unknown

The Best way to contact field is alpha-numeric and can be a telephone number or a short note

![](veteran-s-crisis-line-version-1-user-guide/015.png)

<span id="_Toc406762387" class="anchor"></span>Figure 13: Relationship to Vet

> ![](veteran-s-crisis-line-version-1-user-guide/016.png)

<span id="_Toc406762388" class="anchor"></span>Figure 14: Best way to Contact

## Veteran Info

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. If the caller is identified and selected in the Veteran Look Up section, the Veteran Name, SSN, Age, Gender, Is Veteran, Active Duty, andVeteran Status will be automatically populated.

2\. If the caller was not identified in the Look Up section, the information will need to be obtained and entered manually. \*\Note: This will occur when the Veteran is not enrolled or registered with the VA.*

3\. If the patient refuses to give a name, you must check Anonymous.

4\. The Gender field is a drop-down box with a default of Unable to Determine, or a choice of Male or Female.

5\. The Is Veteran and Active Duty fields are drop-downs boxes with selections of Yes, No, or Refuse to Answer

6\. The Veteran Status field has a default of Unknown with additional choices of:

- Not Registered
- Registered, Not Enrolled
- Enrolled, No Service received from VA
- Enrolled, Receives Services
- Caller Would Not Say

7\. Nearest Facility to Patient \*

> a\. Click Select Facility. Once you have identified the nearest facility in the Web Facilities Finder, select the facilities. This list is in alphabetic order. Scroll through the list until you find the correct facility and click on it. It will then appear in the box. Even though this is not a mandatory field this must be populated in order to submit a record.

> \*\*NOTE: Select State & Select City options are not used in the application\*\*

> ![](veteran-s-crisis-line-version-1-user-guide/017.png)

<span id="_Toc406762389" class="anchor"></span>Figure 15: Veteran Info

## Acute Care Risk Assessment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

What Prompted the Call?

Select the box that is most appropriate. More than one box may be selected. Remember, this is a \*mandatory field. Choices that may be checked are:

- Substance Use / Addiction
- Loneliness
- Suicidal Crisis
- Suicidal thoughts
- Needed info on suicide
- Mental health / illness
- Post-Disaster Needs
- Economic Problems
- Homelessness Issues
- Physical Illness
- Abuse / Violence
- Relationship Problems
- Sexual Orientation Issues
- Family Problems (parent/child)
- Death of a family member / friend
- Other
- Complaint about VA
- Homicidal Thoughts
- Homicidal Crisis
- Legal Issue
- Chronic Pain
- MST
- Joblessness
- TBI
- Anger Issues
- Employment Issues
- Needed Information
- Medical Issues
- Benefits / Payment Concern
- PTSD Symptoms
- Medication Refill / Issue
- Sleep Issues
- 3<sup>rd</sup> Party Concerns
- Concern with Overall VA Care
- Sexual Abuse / Assault (Non-MST)

![](veteran-s-crisis-line-version-1-user-guide/018.png)

<span id="_Toc406762390" class="anchor"></span>Figure 16: What Prompted Call?

Suicide Risk Assessment Screening Questions

\*There are three questions, with drop-down boxes, requiring Yes or No responses.

1\. Are you thinking of suicide?

2\. Have you thought of suicide in the last two months?

3\. Have you ever attempted to end your life?

A Comment field is provided after each question if more information needs to be recorded.

> **NOTE:** If any box is answered YES, the remainder of the risk assessment MUST be completed. You will proceed to Suicidal Desire and Suicidal Intent.

If all three answers are NO, the call responder can page down to Follow-up Questions or the HSS may choose to complete the sections within the Suicidal Desire and Suicidal Intent.

![](veteran-s-crisis-line-version-1-user-guide/019.png)

<span id="_Toc406762391" class="anchor"></span>Figure 17: Suicide Risk Assessment Screening Questions

## Suicidal Desire and Suicidal Intent

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HSS MUST complete the Suicidal Desire and Suicidal Intent sections when a caller answers YES to any of the Suicide Risk Assessment Screening Questions.

Suicidal Desire:

- Desire to harm self and/or others? Selections include: No Answer, None, Moderate, High
- Psychological Pain? Selections include: No Answer, None, Moderate, High
- Perceived burden on Others? Selections include: No Answer, None, Moderate, High
- Helplessness? Selections include: No Answer, None, Moderate, High
- Hopelessness? Selections include: No Answer, None, Moderate, High
- Feeling Trapped? Selections include: No Answer, None, Moderate, High
- Feeling *Intolerably* Alone? Selections include: No Answer, None, Moderate, High

Suicidal Intent: When answering questions for a caller in the Suicidal Intent area the following fields and responses can be selected from the drop-down boxes:

- Has caller expressed intent to die? Selections include: Unclear (default), Yes, No
- Do you have a plan to hurt self or others? Selections include: No Answer, Self, Others, No Plan
- Who are you planning to hurt (if not self)? Open text field.
- What would you use to hurt self or others? Open text field.
- How would you hurt self or others? Open text field.
- Are you able to follow through with your plan? Selections include: Yes, No, Did not respond
- Do you have the means to carry it out? Selections include: Yes, No, Did Not Respond
- When do you plan to do this? Selections include: No Answer, Today, Tomorrow, Soon, Right Now, Other
- Have you put any plans into action? Selections include: No Answer, Yes, No
- If “Yes”, what are those plans? This is a text field for appropriate response information.

![](veteran-s-crisis-line-version-1-user-guide/020.png)

<span id="_Toc406762392" class="anchor"></span>Figure 18: Suicidal Desire and Suicidal Intent

## Suicidal Capability

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Suicidal Capability is also required when a caller answers YES to any of the Suicide Risk Assessment Screening Questions. Suicidal Capability includes Substance Abuse and Other Risk Factors sections.

This section may also be used for callers who are not suicidal, but have related issues in substance abuse or other risk factors.

Suicidal Capability:

- Have you tried to kill yourself before? Response options include: No Answer, Yes and No
- If YES, was it in the past year? Response options include: No Answer, Yes and No
- Have you had a close friend or family member die by suicide? Response options include: No Answer, Yes and No
- Do you have access to means to hurt yourself or others? Response options include: No Answer, Yes and No
- Do you have Access to a gun? Response options include: No Answer, Yes and NoSubstance Abuse:
- Currently Intoxicated? Response options include: Difficult to Determine (default), Yes, and No
- Currently using/withdrawing from drugs? Response options include: Difficult to Determine (default), Yes, and No
- Drugs involved? Response options include:
  - None (default)
  - Alcohol
  - Marijuana
  - Cocaine or Crack
  - Meth
  - Hallucinogens
  - Drugs + Alcohol
  - Other
  - None
  - Opiates
- Are you currently overusing prescription drugs? Response options include: Difficult to Determine (default), Yes, and No
- Have you stopped taking your prescribed meds? Responses include Difficult to Determine (default), Yes, and No
- If Yes, how many days has it been since your last dose? A number can be entered in the box.

Other Risk Factors – Do you sense from the caller:Difficult to Deal With / Delusional? Difficult to determine is the default, with Yes and No as options.

Tiredness?Difficult to determine is the default, with Yes and No as options

Sleeplessness/Insomnia?Difficult to determine is the default with Yes and No as options

High Anxiety?Difficult to determine is the default with Yes and No as options

High Anger?Difficult to determine is the default with Yes and No as options

Chronic Pain?Difficult to determine is the default with Yes and No as options

![](veteran-s-crisis-line-version-1-user-guide/021.png)

<span id="_Toc406762393" class="anchor"></span>Figure 19: Suicidal Capability

## Buffers Connectedness

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Buffers Connectedness is an area where the HSS will confirm that the callers have either or both Immediate and Social Support Networks to help them through difficult times.

Immediate support: For both questions in this area, No Answer is the default response, with No and Yes as options.

Is someone with you?Is there someone you can call?Social Supports:

- Who/What do you feel supported by?Names One Person or Thing is the default, with Feels No Support and No Answer as options
- Does the caller appear to have plans for the future? Unclear is the default, with Yes and No as options
- Does the caller seem to be ambivalent about living?Unclear is the default, with Yes and No as options
- Does the caller seem to have core values/beliefs? Unclear is the default, with Yes and No as options
- Does the caller seem to have a sense of purpose?Unclear is the default, with Yes and No as options
- How would you rate the caller’s engagement with you?Unclear is the default, with Low, Moderate, High and None as options.

![](veteran-s-crisis-line-version-1-user-guide/022.png)

<span id="_Toc406762394" class="anchor"></span>Figure 20: Social Supports

## Follow up Questions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

While the follow-up questions are more difficult to obtain, they often provide valuable information in supporting the patient’s future behavior.

- When did the caller serve? There is no default. The options are:
  - None
  - OEF/OIF 8/1990-
  - Gulf War 8/1990-
  - Vietnam 2/1961 – 5/19/1975
  - Served Between Major Conflicts
  - Korean War 6/1950 – 1/55
  - World War II 12/1941 – 12/1946
  - World War I 4/1917 – 11/1918
  - Career Military (served more than one period)
- In which branch did the caller serve?None is the default, and the other option are:
  - Army
  - Navy
  - Air Force
  - Marines
  - Coast Guard
  - National Guard
  - Reserves
- How did you hear about us? Check as many boxes as apply to the caller. Options are:
  - Internet (web, email)
  - Phonebook
  - Newspaper
  - Magazine/Newsletter
  - Brochure
  - Radio
  - TV
  - Wallet Cards
  - Friend/Family
  - Physician
  - Faith-based leader
  - Counselor/Therapist
  - Pen/Magnet Giveaways
  - Bus/Train/Billboards
  - Other
  - VA Letter
  - VA Voicemail
  - It was on Safety Plan
  - Military Crisis Line Promotion
- Callers Needs Met? This is a Mandatory field\* -- as default, with Yes, No? as options.

![](veteran-s-crisis-line-version-1-user-guide/023.png)

<span id="_Toc406762395" class="anchor"></span>Figure 21: Follow-Up Questions

## Call Synopsis

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Call Synopsis is a text box for a Brief description of the details of the conversation with the caller. This could include, but would not be limited to, addressing where the Veteran is currently located, telephone contact information, and details of a request by the Veteran regarding the VA facility s/he wishes to be seen at, and any other related details to the call. This text box has unlimited wrapping and will accommodate both text and numeric entries.

Checked Capri Info? Is a dropdown box with, Did not ask (default), Veteran refused and Yes as the possible options. This should be filled out for all referrals

Two Week Follow-Up Section HSS should ask all Veterans with referrals.

Would it be ok if we call you in two weeks to see how you are doing? Responses include Yes, No (default), Did not Ask

Additional Identifying & Demographic Information

Text boxes are for Brief descriptions of information related to the call that the HSS enters during the call that might be helpful to the SPC in providing the Veteran with the appropriate care.

These six sections include:

- History of Present Illness (include current mental status and current suicidal ideation, planning and intent).
- Psychiatric History and Treatment
- Social and Developmental History
- Family History of Suicide
- Current Serious Medical Illnesses
- History of Current, Recent and Past Suicidal Ideation, Planning and Attempts

Clinical Impressions and Formulation of Suicide Risk: This is a Mandatory field\*. There is no default; Moderate to Low Risk, Moderate to High Risk, and High Risk are the options.

![](veteran-s-crisis-line-version-1-user-guide/024.png)

<span id="_Toc406762396" class="anchor"></span>Figure 22: Additional Identifying and Demographic Information

## Self-Directed Violence

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Self-Directed Violence (SDV) is a mandatory field for all calls. These questions are answered in the order presented.

During SDV entry – User can go back to the previous entry by using the back button. This enables the User to go back to back to the previous entry if you want to change the response.

Using the Decision Trees shown below to determine SDV:

BEGIN WITH THESE THREE QUESTIONS:

1.  Is there any indication that the person engaged in Self-Directed Violent <u>Behavior,</u> either preparatory or potentially harmful?
    1.  (Refer to Key Terms Shown Below)
    2.  IF NO, proceed to Question 2
    3.  IF YES, proceed to Question 3
2.  Is there any indication that the person had Self-Directed Violence related <u>thoughts?</u>
    1.  IF NO to Questions 1 and 2, there is insufficient evidence to suggest Self-Directed Violence -\>NO SDV TERM
    2.  IF YES, proceed to Decision Tree A
3.  Did the behavior involve any <u>injury?</u>

SDV KEY TERMS:

<u>Self-Directed Violence</u>: Behavior that is self-directed and deliberately results in injury or the potential for injury to oneself.

<u>Suicidal Intent:</u> There is past or present evidence (explicit and/or implicit) that at the time of injury the individual intended to kill self and wished to die and that the individual understood the probable consequences of his or her actions.

<u>Preparatory Behavior:</u> Acts or preparation towards engaging in Self-Directed Violence, but before potential for injury has begun. This can include anything beyond a verbalization or thought, such as assembling a method (e.g., buying a gun, collecting pills) or preparing for one’s death by suicide (e.g., writing a suicide note, giving things away).

<u>Physical Injury (paraphrased):</u> A bodily lesion resulting from acute overexposure to energy (this can be mechanical, thermal, electrical, chemical, or radiant) interacting with the body in amounts or rates that exceed the threshold of physiological tolerance (e.g., bodily harm due to suffocation, poisoning or overdoses, lacerations, gunshot wounds, etc.). Refer to the Classification System for the Centers for Disease Control and Prevention definition.

<u>Interrupted by Self or Other:</u> A person takes steps to injure self but is stopped by self/another person prior to fatal injury.

<u>Suicide Attempt:</u> A non-fatal self-inflicted potentially injurious behavior with any intent to die as a result of the behavior.

<u>Suicide:</u> Death caused by self-inflicted injurious behavior with any intent to die as a result of the behavior.

> **REMINDER:** Behaviors Trump Thoughts  

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Decision Tree A: Thoughts

![](veteran-s-crisis-line-version-1-user-guide/025.png)

<span id="_Toc406762397" class="anchor"></span>Figure 23: Decision Tree A: Thoughts

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Decision Tree B: Behaviors, Without Injury

![](veteran-s-crisis-line-version-1-user-guide/026.png)

<span id="_Toc406762398" class="anchor"></span>Figure 24: Decision Tree B: Behaviors, Without Injury

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

Decision Tree C: Behaviors, With Injury

![](veteran-s-crisis-line-version-1-user-guide/027.png)

<span id="_Toc406762399" class="anchor"></span>Figure 25: Decision Tree C: Behaviors, With Injury

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

After completing entry of SDV questions, the user will see the assigned SDV Classification on the Hotline form. This information is then populated in the RESPONSE application with the appropriate SDV Code for SPC use. Examples of the SDV Classification as entered during a call and the Classification code as displayed in Response Application is shown below:

![](veteran-s-crisis-line-version-1-user-guide/028.png)

<span id="_Toc406762400" class="anchor"></span>Figure 26: SDV Classification

![](veteran-s-crisis-line-version-1-user-guide/029.png)

<span id="_Toc406762401" class="anchor"></span>Figure 27: Outcome of Call

Examples of the SDV questions are shown below:

![](veteran-s-crisis-line-version-1-user-guide/030.png)

<span id="_Toc406762402" class="anchor"></span>Figure 28: SDV Questions Example 1

![](veteran-s-crisis-line-version-1-user-guide/031.png)

<span id="_Toc406762403" class="anchor"></span>Figure 29: SDV Questions Example 2

![](veteran-s-crisis-line-version-1-user-guide/032.png)

<span id="_Toc406762404" class="anchor"></span>Figure 30: SDV Questions Example 3

![](veteran-s-crisis-line-version-1-user-guide/033.png)

<span id="_Toc406762405" class="anchor"></span>Figure 31: SDV Questions Example 4

## Outcome of Call

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Outcome of Call is the only section where all questions are Mandatory\*. Each question requires a very specific answer.

What was the outcome of the call? Response options include: \* Mandatory

- Call disconnected / Texter stopped responding
- Prank Call
- Rescue called without suicidal behavior
- Caller stayed on line until the call ended normally
- Rescue Called with suicidal behavior
- Rescue Called with suicide completion
- Responder Terminated Call(Inappr behavior – 10 min rule)
- Caller went voluntarily to ER
- Text transfer to VCL
- Noteworthy caller protocol followed
- Facility transportation plan
- Responder attempted to contact Veteran and left message
- Responder attempted to contact Veteran and was unsuccessful

What action did you take? Response options include: \* Mandatory

- Referral generated, sent to SPC
- Caller refused referral, BUT ACCEPTED SPC \#
- Caller refused referral and refused any contact with SPC
- Warm transfer to approved resource
- Warm Transfer to caller’s VA PCP
- Caller responded to Intervention
- Warm Transfer to regular crisis line
- Provided a local number to call
- No action possible
- Non-vet, no SPC referral
- Text transfer to VCL
- Warm transfer to Vets4Warriors

Refer call to SPC? The options are Yes, or No \* Mandatory

Referral Type? Response Options should completed for all referrals and include: \* Mandatory

- Routine
- Info Only
- Emergent
- Urgent

Submit Call Info: When you have completed all Mandatory fields\* and other fields necessary to explain the call, click Submit Call Info. A message will appear if a mandatory field was not completed.

![](veteran-s-crisis-line-version-1-user-guide/034.png)

<span id="_Toc406762406" class="anchor"></span>Figure 32: Mandatory Field Error Message

For example, “Please select one reason for call” will be displayed. When completed, the data will be processed directly into the database. If a referral is made to a VA Medical Center, the VCL Call Log will be made accessible to that medical center’s SPC In their Web Response Application.

![](veteran-s-crisis-line-version-1-user-guide/035.png)

<span id="_Toc406762407" class="anchor"></span>Figure 33: Outcome of Call

After the call information is submitted to the database, the screen will be cleared except for the Responder’s Name and Phone Station/Line, and the call responder will be ready to take another call.

Remember when you answer a new call, click “Set Call Time” to activate the date and time for the new call.

# The Suicide Prevention Coordinator Response Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a referral is made from the Hotline to a VA Medical Center, the SPC will use the VCL Response Application to access the referral and complete additional information on the actions taken as a result of the referral. The VCL Response Application can be accessed directly from Internet Explorer (IE) by entering <span class="mark">REDACTED</span>in the IE address bar*.* A Security Disclaimer page will appear on screen. User will select the I Agree button and continue to login page. The application now has a timeout feature enabled after 15 minutes of inactivity. If the user is inactive on the application for 15 minutes they will receive a warning that the application will terminate in two minutes, if they want to continue working they can click continue working.

The SPC signs in using their VistA Log-in pair.

Users must select their VISN and local site for login and then enter their access and verify code which is the same as their CPRS/VistA access and verify code pair.

Users will only be able to log into their local site, using their VistA access and verify code pair. Only users that are identified as requiring access to the Response Application will be able to access the system. The list of users requiring access is maintained by the site VA Suicide Prevention Office.

![](veteran-s-crisis-line-version-1-user-guide/036.png)

<span id="_Toc406762408" class="anchor"></span>Figure 34: VCL Response Application

## Open Hotline Calls 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the VCL Call Log is submitted, it is immediately processed into the hotline’s database and an open call response is created in the Crisis Center Response location. The screen includes three options:

1)  Open Calls for This Site (with no response): A listing of all open call responses which have never been opened/reviewed previously or those calls that the quick save button has not been enabled (e.g. SPC may have record open for editing but has not completed the quick save). Once the quick save is enabled, the record is moved to Open Call Response in Progress. An individual SPC will only be able to view calls referred to their medical center.
2)  Open Call Responses in Progress: Lists all open call responses previously viewed but not returned to the Hotline SSA for close-out.
3)  Open Calls with No Site Specified: Lists all open call responses that have no VA site identified for follow up by a SPC.

When you click on any of the tabs, a listing of all calls available to be completed will appear.

## Open Hotline Call 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Open Hotline Calls includes the calls that have not been addressed by the SPC.

Click on Select and the record opens.

![](veteran-s-crisis-line-version-1-user-guide/037.png)

<span id="_Toc406762409" class="anchor"></span>Figure 35: Open Hotline Calls

Find Past referrals Button: Allows a SPC to retrieve via *read only* closed referrals by date range. This function can also be used as a report mechanism to identify the total number of calls for a specific time period. To access this feature, click on the button at the top of the page labeled Find Past Referrals.

If you wish to look at all closed referrals for a specific time, select a date range and click the Is Closed box. If you wish to include all the referrals that remain open you would unclick the Is Closed box. If you are looking for a specific referral and know the approximate date, put in that date range and click the Is Closed box. You may now search the resulting list. When you wish to return to the open referrals page click on the Return to Calls Page or click Logout if you wish to end your session.

![](veteran-s-crisis-line-version-1-user-guide/038.png)

<span id="_Toc406762410" class="anchor"></span>Figure 36: Search for Calls Between Dates

# Acute Care Risk Assessment and Log Sheet Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once a call is selected, the Acute Care Risk Assessment & Log Sheet created by the Hotline HSS appears and the Hotline Call Detail tab is highlighted. You will notice that the font’s sizes have increased and the answer to each question is bold now.

![](veteran-s-crisis-line-version-1-user-guide/039.png)

<span id="_Toc406762411" class="anchor"></span>Figure 37: Hotline Call Detail

The Response Application allows the SPC to change data only in the Veteran information area of the record. To enable this feature the SPC must go to the bottom of the Acute Care Risk Assessment & Log Sheet and click Enable Editing.

![](veteran-s-crisis-line-version-1-user-guide/040.png)

<span id="_Toc406762412" class="anchor"></span>Figure 38: Enable Editing

Some referrals will not have complete or accurate Veteran information. Once the SPC is able to identify a Veteran as a registered patient, they can locate the Veteran using their local VistA system. Locate the Find Veteran Box in the upper left-hand corner of the screen.

- User may search for Veteran by entering the Veteran’s last name followed by a comma and first name (no spaces).
- User may also search for Veteran by entering the entire SSN of the Veteran.
- User may also search for Veteran by entering the first letter of Veteran last name followed by the last 4 digits of the Veteran’s SSN. This method is the most utilized when performing search.
- Once search criteria has been entered, click Find Veteran. A list of potential matching patients will be shown in the box. (If there are more names available than shown in the scroll box, click the down arrow button to see them.)
- Click on the Select Veteran button. Information will auto-fill from the patient’s VistA file into the Patient Name, SSN, Age, and Gender fields in the Patient Info.

*Note: The original data is maintained in the database for historical purposes. All other patient information is also populated for the patient from the VistA / CPRS system. Applicable High Risk for Suicide Patient Record Flags (PRFs), if applicable, should now be shown on the patient file.*

If any other information in the Veteran Info area needs to be corrected, it must be done manually using the Enable Editing. This includes Is Veteran, Active Duty, Veteran Status and Nearest Facility to Veteran.

Once all changes are made, click on Save Changes to Call Info at the bottom of the form; all changes will be made and you will be returned to the updated form.

*\*\*Note: If the patient has been sent to an SPC or facility in error, after clicking Enable Editing locate the Nearest Facility the Patient box and select the correct facility. Then click Save Changes to Call Info.*

When you return to the Acute Care Risk Assessment & Log Sheet, you will have three choices:

1.  Return to Call List – Second Button in upper left-hand corner
2.  Go to the Response Form – Button next to Hotline Call Detail
3.  Or Logout – The First Button on the top of the form

If this is a new call, the SPC should click on Response Form.

![](veteran-s-crisis-line-version-1-user-guide/041.png)

<span id="_Toc406762413" class="anchor"></span>Figure 39: Response Form Tab

## Response Form

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you clicked on Response Form, the form below will appear. You still have the options of Return to Call List, Hotline Call Detail, and Logout from the Response Form.

Response Data: In the upper left-hand corner of the Response Form is the Response Data box, which includes the Patient Name, SSN, and SPC Responder’s name.

Quick Save/ Indicate Response: Located below the Response Data box. This is used to confirm receipt of the patient information and add any immediate notes regarding the patient. This will alert the Hotline SSA that the referral has been received. This should be completed as soon as possible after receipt of the referral. This option is provided to allow communication between the SPC and SSA at the Hotline. Clicking this button will not pass information to CPRS. A progress note will only be created when the SPC clicks on the Save Response Data and Create Progress Note button at the end of the form.

Patient Outcomes: Directly to the right of the Response Data patient identifier box is the Patient Outcomes area. Included in this area are checkboxes to quickly identify the outcome of your work with the patient. Multiple boxes may be checked, based on your follow-up.

Progress Note Additions: This box is a free-text area that allows the SPC to add additional content to the progress note that is passed to CPRS.

Is Patient On High Risk List: Shown strictly for informational purposes and cannot be updated from this form. The SPC would have to add the flag in CPRS if indicated. The default setting is No. If the record has not been linked to a patient’s VistA file using the Find Patient option on the Hotline Call Detail tab, then this field will be set to No, even if the patient has a Patient Record Flag for High Risk for Suicide on their chart. By using the Find Patient option, this field will be set to match the patient’s VistA file.

![](veteran-s-crisis-line-version-1-user-guide/042.png)

<span id="_Toc406762414" class="anchor"></span>Figure 40: Progress Note Additions

# Creating TIU Progress Notes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Response Application allows SPC’s to create a progress note from the application. Information from the Acute Risk Assessment and Call LogSheet will automatically be inserted into the progress note. Additionally, the information from the Response Application, including Patient Outcomes and additional text entered by the SPC, will be included in the progress note.

Set Note Title, Appointment or Location Title:

Directly below the Progress Note addition box is the Set Note Title, Appointments or Location Title area.

Note Titles:

In the text box provided, enter enough text to help identify the progress note title that will be used within CPRS, click Get Note Titles, the system will then refresh. Once the refresh process is complete, click the down-arrow and click Select Note Title. Select the appropriate note title. The recommended title is Mental Health Hotline Report.

Get Patient Appointments: *CURRENTLY THIS IS NOT USED IN APPLICATION*

This feature allows a note to be attached to a specific appointment. If an appointment(s) has been set up for the patient, click on Get Patient Appointments, and the system will refresh. Once the system is refreshed, click on the Select Appointments. If an appointment(s) is scheduled, the appointment date will appear in the drop-down box; select the appropriate appointment to link the progress note with.

Locations: *CURRENTLY THIS IS NOT USED IN APPLICATION*

If there is no appointment or encounter to which to attach the note and you still need to write a progress note, you must choose a location for the note. Every progress note must be linked to a location. The SPC will have to identify the correct clinic location to be used for documenting the response to the Hotline referral. Follow the same process to populate the location as you did for note titles. Enter enough information in the search fields to narrow the pick-list.

Historical Note:

The historical option is used to document efforts to reach a Veteran who has been referred from the Hotline. If you do not reach the Veteran but want to provide documentation of the fact that s/he was referred from the Hotline and your attempts to reach him/her check the Historical box.

If you click Historical Note, the Response Application system will prompt you for your electronic signature when you finalize the Response Form by clicking Save Response Data and Create Progress Note. Once that is done, your note will appear as a completed progress note in CPRS, and no encounter information will be entered.

If you do not click Historical Note and finalize the Response Form by clicking Save Response Data and Create Progress Note, the note will be passed to CPRS as an unsigned note. It will appear on the author’s list of view alerts, and the user will have to go into CPRS to sign the note and enter encounter data.

The Response Application cannot pass encounter information to CPRS, so in those cases where the SPC interacted directly with the Veteran in a face-to-face or telephone contact, the Historical box should be left unchecked, and the note and encounter completed in CPRS.

Save Response Data Only: Use this field only if a Veteran is not eligible for VA care. Information is entered only to the VCL Database. This field is activated by Selecting “Toggle Note Writing Settings On/Off” and turning the settings off. This will NOT send a note to CPRS and will only save the information to the VCL database. The Save Response data only field is now activated and SPC is able to enter a note and save response data.

Save Response Data and Create Progress Note: When clicked, the referral is processed in CPRS through TIU and also entered in the VCL Database.

![](veteran-s-crisis-line-version-1-user-guide/043.png)![](veteran-s-crisis-line-version-1-user-guide/044.png)

<span id="_Toc406762415" class="anchor"></span>Figure 41: Save Response Data and Create Progress Note

If Save Response Data and Create Progress Note button is clicked, the following box is displayed:

![](veteran-s-crisis-line-version-1-user-guide/045.png)

<span id="_Toc406762416" class="anchor"></span>Figure 42: Progress Note Message

After clicking OK, the following box is displayed.

![](veteran-s-crisis-line-version-1-user-guide/046.png)

<span id="_Toc406762417" class="anchor"></span>Figure 43: Progress Note Confirmation

The note is then passed to CPRS as an unsigned note. A CPRS alert for an unsigned note is also generated. The user will then go CPRS to complete the encounter and sign the note.

For a Historical note, the note can be signed directly from the Response Application. When the Historical box is checked, you will be prompted to enter your CPRS signature code:

![](veteran-s-crisis-line-version-1-user-guide/047.png)

<span id="_Toc406762418" class="anchor"></span>Figure 44: Historical Note

After you have entered the signature code and click Sign Note, the following is displayed:

![](veteran-s-crisis-line-version-1-user-guide/048.png)

<span id="_Toc406762419" class="anchor"></span>Figure 45: Saved Progress Note Notification

Click OK. The completed note is passed to CPRS. No encounter information is required for a note that is marked as Historical.

The final process is for the SSA at the Hotline to review the input and notes and either close the referral or contact the SPC for more information.

A separate Administrative Application will be used for the purpose of follow-up activities and provide reporting capabilities.

# Admin Application

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Individuals having access to the Admin Application access will sign on to <span class="mark">REDACTED</span>A Security Disclaimer page will appear on screen. User will select the I Agree button and continue to login page. The application now has a timeout feature enabled after 15 minutes of inactivity. If the user is inactive on the application for 15 minutes they will receive a warning that the application will terminate in two minutes, if they want to continue working they can click continue working.

Users will login to the application using their VistA Log-in pair and choose their appropriate admin type in the drop-down box and click Login. User roles that are allowed in the Admin Application are HSS, SSA, Admin and Super Admin. Users requesting access to this application will notify (in writing) the Administrator(s) at Veteran’s Crisis Line Call Center, Canandaigua, NY who will perform add and/or deactivate users for all roles.

> ![](veteran-s-crisis-line-version-1-user-guide/049.png)

<span id="_Toc406762420" class="anchor"></span>Figure 46: User Type Drop-Down

- Once in the Admin application, the following options are available for ADMIN and SUPER ADMIN: Enter Calls, Call List, Search for Open or Closed Calls by Date, Search for Calls by date, SSN, Name, and Phone, Calls Needing Compassionate Care Follow-up. Calls Needing Health Tech Follow-up, User List, Add Users, Deactivate Users and Reporting.

> ![](veteran-s-crisis-line-version-1-user-guide/050.png)

<span id="_Toc406762421" class="anchor"></span>Figure 47: ADMIN and SUPER ADMIN Menu Options

Call Responders have access to: Enter CallsSSAs have access to: Enter Calls, Call List, Search for Open or Closed Calls by Date, Search for Calls by date, SSN, Name, and Phone, Calls Needing Compassionate Care Follow-up,Calls Needing Health Tech Follow-up.Administrative Personnel - Hotline Clinical Applications Coordinator (CAC) have access to all options in the Administrator application.

Super Admins access is limited to the CAC and Developer and is used primarily to return closed referral to SPC’s.

Each of the roles and field inputs allowed are explained below.

## All Administrative Options 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Listed below, which is displayed on the opening screen, are all the administrative options. ONLY ADMINS / SUPER ADMINS have access to the full list. To access any of the administrative options, click on the option and a working screen for that options will appear.

![](veteran-s-crisis-line-version-1-user-guide/051.png)

<span id="_Toc406762422" class="anchor"></span>Figure 48: Administrative Options

Logged in as CR – Enter Calls:

If you are logged into the ADMIN APPLICATION as HSS, you will see the following options on the menu:

![](veteran-s-crisis-line-version-1-user-guide/052.png)

<span id="_Toc406762423" class="anchor"></span>Figure 49: Call Responder Menu Options

This option is used by HSS, SSA or Administrators to enter referrals that were completed on paper when the hotline back-up contingency plan is initiated. The Enter Calls option allows the creator to enter the actual start and end time, and choose the appropriate HSS using the drop down list. Veteran lookup is performed using one of the following two methods for searching:

Search Using combination of State/Facility/Name:

- User clicks Select State and selects the patients state from the drop down entries
- User clicks Select Site and then picks the patients facility
- In the Name Search field, User enters:
- Enter the Veteran’s last name, comma (no spaces) and part of the Veteran’s first name, or first letter of the last name and the last 4 digits of the SSN
- Click Find Veteran. A list of potential matching patients will be shown in the box. (If there are more names available than shown in the scroll box, click the down arrow button to see them.)
- Click on the Veteran’s Name. The Veteran’s date of birth and SSN will appear to the right to verify the Veteran selection.
- If correct, click Select Veteran. The Veteran’s name, SSN and age will be automatically populated on the Acute Care Risk Assessment & Log Sheet.

Search Using Name – the Search Using Name is the most commonly used Search:

- User enters the Veteran’s last name, comma (no spaces) and part of the Veteran’s first name, or first letter of the last name and the last 4 digits of the SSN
- Click Find Veteran. A list of potential matching patients will be shown in the box. (If there are more names available than shown in the scroll box, click the down arrow button to see them.)
- Click on the Veteran’s Name. The Veteran’s date of birth and SSN will appear to the right to verify the Veteran selection.
- If correct, click Select Veteran. The Veteran’s name, SSN and age will be automatically populated on the Acute Care Risk Assessment & Log Sheet.

User will continue to enter the call information into the HOTLINE application. All information needed to populate this screen is provided from the original hand written entry.

\*\*NOTE: In the ADMIN APPLICATION-Enter Calls, there is no entry for the SDV classification.\*\*

![](veteran-s-crisis-line-version-1-user-guide/053.png)

<span id="_Toc406762424" class="anchor"></span>Figure 50: Veteran Search

![](veteran-s-crisis-line-version-1-user-guide/054.png)

<span id="_Toc406762425" class="anchor"></span>Figure 51: Hotline Call Entry Screen

## SSA Functions:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

User logs into the ADMIN application as HT. User will see the following options on the main menu page of the ADMIN Application.

![](veteran-s-crisis-line-version-1-user-guide/055.png)

<span id="_Toc406762426" class="anchor"></span>Figure 52: SSA Functions

## Call List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option allows SSA to complete the following:

> Choose Site to View calls from: Select the VISN and the VA site within that VISN. This will show just this sites calls.

> View Calls: This option allows you to view calls by type. Available selections are:

- With No Response
- In Progress by SPC
- With Response but Not Approved
- Responded to and sent back to SPC
- Calls Not Marked as Referrals
- All Calls for the CAC only No Response and Not Marked as referrals have the option of turning off a referral in No Response or turning on a referral in Not Marked as referrals.

> Number of Records to Display: The options are 10, 50 or 100 records. The records are displayed by Call Start, Call End, Caller Phone Number, Caller Name, Veterans Name, Is a Referral, Has SPC Response, and Location (Site).

![](veteran-s-crisis-line-version-1-user-guide/056.png)

<span id="_Toc406762427" class="anchor"></span>Figure 53: Admin View Call List

Clicking on Select brings up the Hotline Call Detail (Screen below). This screen is identical to the screen created by HSS and viewed by the SPC and, when completed, includes the Compassionate Care Follow-up. There are three tabs on the screen:

![](veteran-s-crisis-line-version-1-user-guide/057.png)

<span id="_Toc406762428" class="anchor"></span>Figure 54: Hotline Call Detail Tab

Hotline Call Detail, the screen above, and has all the information provided by the call responder to the SPC as well as the Compassionate Care follow-up, which appears at the bottom of the “How did you hear about us?” screen.

![](veteran-s-crisis-line-version-1-user-guide/058.png)

<span id="_Toc406762429" class="anchor"></span>Figure 55: How did You Hear About Us

![](veteran-s-crisis-line-version-1-user-guide/059.png)

<span id="_Toc406762430" class="anchor"></span>Figure 56: Compassionate Care Follow-up

If you click on Response Form tab, the form below appears. You still have the options of Health Tech Follow Up, Return to Call List, Hotline Call Detail, and Logout from the Response Form.

The Response Form (screen below) allows you to view the actions taken by the SPC.

![](veteran-s-crisis-line-version-1-user-guide/060.png)

<span id="_Toc406762431" class="anchor"></span>Figure 57: Response Form

Health Tech Follow-up (screen below). This screen allows the health tech to enter four different follow ups and save the comments. There is a 24-hour, one week, two week, and one month follow up. After each level is completed, the next level appears and displays the comment from the previous level. It also replaces the Red X on the Calls Needing Health Tech Follow-up to a Green check on the level entered.

![](veteran-s-crisis-line-version-1-user-guide/061.png)

<span id="_Toc406762432" class="anchor"></span>Figure 58: Health Tech Follow-Up

## Search for Open or Closed Calls by Date

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Click on Search for Calls Between Dates Date (screen below). This function is used primarily to identify open referrals.

![](veteran-s-crisis-line-version-1-user-guide/062.png)

<span id="_Toc406762433" class="anchor"></span>Figure 59: Search for Calls Between Dates

## Search for Calls by Date, SSN, Name, and Phone

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Click on Search for Open or Closed Calls by Date (screen below). Notice that the Start and End Date function and the Referral Only check box are *separate* from the Veterans SSN, Veterans Name and the Call Phone \#. All searches are initiated by clicking the Search Button.

The Start and End Date can be used with or without the Referrals Only check box. When the box *is not* checked, the resulting screen will show all calls between the two dates entered. When Referrals Only *is* checked, the resulting screen will show all referrals between the two dates.

ORVeteran SSN will identify all calls where the SSN appears. You can enter the complete SSN to limit the number of calls that will show or the last four only which will show all calls that have the same last four in the number.

Veterans Name allows you to enter the complete name, the first, last or middle name and will bring up all matches for all calls in the database. The full name is the least likely to bring up the name, while the first or last or middle used separately will bring up all matches to the name and make it easier to find the individual you are looking for in all calls.

Caller Phone \#: Enter the ten digits of the phone number. The system has the ability to strip out spaces, dashes or special characters to identify all call matching the phone number in the database.

![](veteran-s-crisis-line-version-1-user-guide/063.png)

<span id="_Toc406762434" class="anchor"></span>Figure 60: Hotline Call List Criteria

## Calls Needing Compassionate Care Follow-up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Click on Calls Needing Compassionate Care Follow-up (screen below). This screen is used by hotline supervisors to track and monitor Compassionate Carefollow-ups. This screen allows the supervisor to view follow-up calls by call responder. This screen also allows the supervisor to view call backs that are past due.

When the call responder enters a note, the name, date and time the call responder completed the following up, is captured in the field at the bottom of the Hotline Call Detail. If there is no contact after three tries, the call responder creates a note, documenting they were unable to contact Veteran. The note is saved the same way.

![](veteran-s-crisis-line-version-1-user-guide/064.png)

<span id="_Toc406762435" class="anchor"></span>Figure 61: Compassionate Care Follow-up

## Calls Needing Health Tech Follow-up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This screen is used to track and access the follow-up status for all referral calls both by the SSA (using for tracking and follow-up) and by the hotline supervisors to monitor the status of follow ups on all calls having referrals. The SSA has the ability to add the current follow-up status for each level of the call referral by accessing the call from this screen or from any other screen where call access is available. The SSA will then click on the tab Health Tech Follow-up. When a level of follow-up is completed, the Red X on the Screen changes to a Green Check Mark.

![](veteran-s-crisis-line-version-1-user-guide/065.png)

![](veteran-s-crisis-line-version-1-user-guide/066.png)

<span id="_Toc406762436" class="anchor"></span>Figure 62: Calls Needing Health Tech Follow-up

User will choose a call from the list and click the Select button. If you click on Response Form tab, the form below appears. You still have the options of Health Tech Follow Up, Return to Call List, Hotline Call Detail, and Logout from the Response Form.

The Response Form (screen below) allows you to view the actions taken by the SPC. Additionally, you will be able to add a note for the SPC and/or close the referral.

1.  Add Note for SPC and/or Close Call & Response: This is a free-text area that allows you to add additional content specifically for the SPC.
2.  Close Call and Response: Check the Close Call and Response box only if the referral had been responded to by the SPC and all actions for the referral have been addressed. You then need to click on the Save Note and/or Close Call box. The referral will then be closed.

If you determine that the referral is not closed, you can use the Health Tech Note box to write a brief note to the SPC, detailing the SSA findings. Click on the Save Note and/or Close Call box. By clicking the Save Note and/or Close Call box, the application allows for the SSA note to return to the SPC for further action.

![](veteran-s-crisis-line-version-1-user-guide/067.png)

<span id="_Toc406762437" class="anchor"></span>Figure 63: View Action by SPCs

ADMIN Functions:

User logs into the ADMIN application as Admin. User will see the following options on the main menu page of the ADMIN Application.

![](veteran-s-crisis-line-version-1-user-guide/068.png)

<span id="_Toc406762438" class="anchor"></span>Figure 64: Admin Functions

## Enter Calls

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option is used by HSS, SSA or Administrators to enter referrals that were completed on paper when the hotline back-up contingency plan is initiated. The Enter Calls option allows the creator to enter the actual start and end time, and choose the appropriate HSS using the drop down list. Veteran lookup is performed using one of the following two methods for searching:

Search Using combination of State/Facility/Name:

- User clicks Select State and selects the patients state from the drop down entries
- User clicks Select Site and then picks the patients facility
- In the Name Search field, User enters:
- Enter the Veteran’s last name, comma (no spaces) and part of the Veteran’s first name, or first letter of the last name and the last 4 digits of the SSN
- Click Find Veteran. A list of potential matching patients will be shown in the box. (If there are more names available than shown in the scroll box, click the down arrow button to see them.)
- Click on the Veteran’s Name. The Veteran’s date of birth and SSN will appear to the right to verify the Veteran selection.
- If correct, click Select Veteran. The Veteran’s name, SSN and age will be automatically populated on the Acute Care Risk Assessment & Log Sheet.

Search Using Name – the Search Using Name is the most commonly used Search:

- User enters the Veteran’s last name, comma (no spaces) and part of the Veteran’s first name, or first letter of the last name and the last 4 digits of the SSN
- Click Find Veteran. A list of potential matching patients will be shown in the box. (If there are more names available than shown in the scroll box, click the down arrow button to see them.)
- Click on the Veteran’s Name. The Veteran’s date of birth and SSN will appear to the right to verify the Veteran selection.
- If correct, click Select Veteran. The Veteran’s name, SSN and age will be automatically populated on the Acute Care Risk Assessment & Log Sheet.

User will continue to enter the call information into the HOTLINE application. All information needed to populate this screen is provided from the original hand written entry.

\*\*NOTE: In the ADMIN APPLICATION-Enter Calls, there is no entry for the SDV classification.\*\*

## Call List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Choose Site to View calls from: Select the VISN and the VA site within that VISN. This will show just this sites calls.

View Calls: This option allows you to view calls by type. Available selections are:

- With No Response
- In Progress by SPC
- With Response but Not Approved
- Responded to and sent back to SPC
- Calls Not Marked as Referrals
- All Calls the CAC only No Response and Not Marked as referrals have the option of turning off a referral in No Response or turning on a referral in Not Marked as referrals.

## Search for Open or Closed Calls by Date

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Click on Search for Open or Closed Calls by Date. This function is used primarily to identify open referrals.

## ## Search for Calls by Date, SSN, Name and Phone

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Click on Search for Open or Closed Calls by Date (screen below). Notice that the Start and End Date function and the Referral Only check box are *separate* from the Veterans SSN, Veterans Name and the Call Phone \#. All searches are initiated by clicking the Search Button.

The Start and End Date can be used with or without the Referrals Only check box. When the box *is not* checked, the resulting screen will show all calls between the two dates entered. When Referrals Only *is* checked, the resulting screen displays all referrals between the two dates.

ORVeteran SSN will identify all calls where the SSN appears. You can enter the complete SSN to limit the number of calls that will show or the last four only which will show all calls that have the same last four in the number.

Veterans Name allows you to enter the complete name, the first, last or middle name and will bring up all matches for all calls in the database. The full name is the least likely to bring up the name, while the first or last or middle used separately will bring up all matches to the name and make it easier to find the individual you are looking for in all calls.

> Caller Phone \#: Enter the ten digits of the phone number. The system has the ability to strip out spaces, dashes or special characters to identify all call matching the phone number in the database.

## Calls Needing Compassionate Care Follow-up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This screen is used by hotline supervisors to track and monitor Compassionate Carefollow-ups. This screen allows the supervisor to view follow-up calls by call responder. This screen also allows the supervisor to view call backs that are past due.

## ## Calls Needing Health Tech Follow-up

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This screen is used to track and access the follow-up status for all referral calls both by the SSA (using for tracking and follow-up) and by the hotline supervisors to monitor the status of follow ups on all calls having referrals.

## ## Users List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This screen includes all individuals who have been granted access to any part of the Application. This list can be sorted by User Type. Available choices in this sort include:

- All
- CR
- SPC
- HT
- Admin
- Super Admin.

The CAC and all the hotline supervisors have the ability to grant access to the different levels of the Application. This function also allows the individual with access ability view 10, 50 and 100 individuals at a time. The information on each person includes ID \#, VistaDUZ, Username, Site located at, and User Type.

![](veteran-s-crisis-line-version-1-user-guide/069.png)

<span id="_Toc406762439" class="anchor"></span>Figure 65: User Type

## Adding Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To add a user, click Add Users.

1.  Select the user’s VISN and Site location
2.  Enter the user’s last name, and first few initials of their first name (no spaces). Click on Find User. Search will return available individuals matching search criteria in display.
3.  Select the correct individual.
4.  Select the type of position being set up.
5.  Click Add User. The application will create the user and will not create duplicates if entered twice.

> \*\* NOTE: Admins are able to add Users up to the Admin level. Super Admins are able to add all User types.

> ![](veteran-s-crisis-line-version-1-user-guide/070.png)

<span id="_Toc406762440" class="anchor"></span>Figure 66: Add User from Specific Site

## Deactivating Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To deactivate a user, click Deactivate User

1.  Enter the name of the individual’s last name
2.  Click the user role from the drop-down box
3.  Click on the user to be deactivated
4.  Click Deactivate User

> \*\*NOTE: Admins are able to deactivate users up to the Admin level only. Super Admins are able to deactivate all User Types.

> ![](veteran-s-crisis-line-version-1-user-guide/071.png)

<span id="_Toc406762441" class="anchor"></span>Figure 67: Deactivate User

## Admin Permissions for Admin Applications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Access to the Admin Application is granted by the CAC. The following is a breakdown of permissions by job type to the admin function.

1.  Call Responders

> Enter Calls

2.  Health Tech’s

> Enter Call

> Call List

> Search for Open or Closed calls by Date

> Search for Calls by Date, SSN, Name, and Phone

> Calls Needing Compassionate Care Follow-up

> Calls Needing Health Tech Follow-up

3.  Admin-Hotline CACs

> Enter Call

> Call List

> Search for Open or Closed calls by Date

> Search for Calls by Date, SSN, Name, and Phone

> Calls Needing Compassionate Care Follow-up

> Calls Needing Health Tech Follow-up

> User List

> Add Users

> Deactivate Users

> Report

> Fiscal Year Referral Counts by Type

> Fiscal Year Call Counts by Type

> Custom Reports

4.  Super Admins-CACs and Developers

> All of Admin options along with the ability to return referrals to SPC, when the referral is requested by the SPC, or needs to be returned due to progress note being entered into the wrong patients CPRS chart.

# Administrator Options for Reporting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All Reports are exportable to Microsoft Excel and can be printed or saved from there. There are two “canned reports” available for downloading.

![](veteran-s-crisis-line-version-1-user-guide/072.png)

<span id="_Toc406762442" class="anchor"></span>Figure 68: Reporting Menu Options

Administrative Reports

Fiscal Year Referral Counts by Type: This report is used to track all referrals and the type of follow-up done by the SPC’s. The report is by type, by month, and by fiscal year. The types include:

- Total SPC Referrals
- Veteran is ineligible for VA services and referred to community services
- Immediate Evaluation at VA or CBOC provided
- Admissions to inpatient hospitals
- SPC contacted Veteran/arranged for care
- Referral to other VA Services such as OIF/OEF program, substance abuse program or homeless program, given SPC \#, etc.
- 911 Rescue provided – No F/U desired
- 911 Rescue provided with F/U arranged by SPC
- Enrolled in VA Health Care System
- No Contact – unable to contact Veteran or Veteran refused care – information about VA given

| Type                                                                                                               | Oct | Nov | Dec | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep | Totals | % of Total Calls |
|------------------------------------------------------------------------------------------------------------------------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|------------|----------------------|
| Total SPC Referrals                                                                                                    | 5611    | 5318    | 5429    | 5588    | 0       | 0       | 0       | 2       | 9       | 26      | 33      | 0       | 22016      |                      |
| Veteran is ineligible for VA services and referred to community services                                               | 81      | 87      | 64      | 68      | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 300        | 1%                   |
| Immediate Evaluation at VA or CBOC provided                                                                            | 97      | 84      | 104     | 66      | 0       | 0       | 0       | 0       | 3       | 2       | 2       | 0       | 358        | 2%                   |
| Admissions to inpatient hospitals                                                                                      | 492     | 500     | 485     | 541     | 0       | 0       | 0       | 0       | 1       | 4       | 1       | 0       | 2024       | 9%                   |
| SPC contacted veteran/arranged for care                                                                                | 4426    | 4228    | 4329    | 4280    | 0       | 0       | 0       | 0       | 5       | 9       | 13      | 0       | 17290      | 79%                  |
| Referral to other VA Services such as OIF/OEF program, substance abuse program or homeless program, given SPC \#, etc. | 62      | 82      | 63      | 78      | 0       | 0       | 0       | 0       | 2       | 1       | 4       | 0       | 292        | 1%                   |
| 911 Rescue provided - No F/U desired                                                                                   | 24      | 20      | 25      | 36      | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 0       | 105        | %                    |
| 911 Rescue provided with F/U arranged by SPC                                                                           | 104     | 87      | 109     | 124     | 0       | 0       | 0       | 0       | 0       | 3       | 1       | 0       | 428        | 2%                   |
| Enrolled in VA Health Care System                                                                                      | 434     | 453     | 429     | 423     | 0       | 0       | 0       | 0       | 1       | 0       | 1       | 0       | 1741       | 8%                   |
| No Contact - unable to contact veteran or veteran refused care - information about VA given                            | 1185    | 1090    | 1100    | 1042    | 0       | 0       | 0       | 0       | 1       | 12      | 11      | 0       | 4441       | 20%                  |

Fiscal Year Call Counts by Type: This report tracks the types of calls received by type of call and type of action taken. The report is by type, by month, and by fiscal year. This report does not include pranks or hang-ups. The types reported in this report are:

- Is Vet
- Family/Friend of Vet
- Is Active Duty
- SPC Referral
- Warm Transfer
- Rescues without Follow-up
- Rescues with Follow-up
- Total Unique Calls

| Type             | Oct | Nov | Dec | Jan | Feb | Mar | Apr | May | Jun | Jul | Aug | Sep |
|----------------------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|---------|
| Is Vet               | 22669   | 21487   | 23653   | 23389   | 0       | 0       | 0       | 4       | 11      | 39      | 36      | 0       |
| Family/Friend of Vet | 2617    | 2588    | 2523    | 2932    | 0       | 0       | 0       | 0       | 4       | 4       | 4       | 0       |
| Is Active Duty       | 270     | 278     | 190     | 245     | 0       | 0       | 0       | 1       | 3       | 1       | 4       | 0       |
| SPC Referrals        | 5611    | 5318    | 5429    | 5588    | 0       | 0       | 0       | 1       | 6       | 23      | 25      | 0       |
| Warm Transfers       | 277     | 305     | 308     | 320     | 0       | 0       | 0       | 0       | 2       | 1       | 2       | 0       |
| Rescues w/out FU     | 75      | 74      | 76      | 55      | 0       | 0       | 0       | 0       | 0       | 2       | 1       | 0       |
| Rescues with FU      | 256     | 249     | 262     | 283     | 0       | 0       | 0       | 0       | 1       | 1       | 2       | 0       |
| Total Unique Calls   | 28266   | 26749   | 29061   | 29989   | 0       | 0       | 0       | 4       | 14      | 40      | 40      | 0       |

*\*\*Note: All Ad Hoc reports or queries are done using a SQL query tool by the CAC and must be requested through Victoria Bridges or Caitlin Thompson.*

Click the Custom Reports link, to navigate to the SQL Server Reporting Services (SSRS) home page.

The following page, with default folders is displayed.

![](veteran-s-crisis-line-version-1-user-guide/073.png)

<span id="_Toc406762443" class="anchor"></span>Figure 69: SQL Server Reporting Services

The two folders of most interest on this page are:

- User Reports
  - Click on the User Reports folder, in order to view and run any of the pre-built reports, which have been published by the VCL adminstrators.
- VCL One
  - Click on the VCL One folder, in order to view and run any of the pre-built reports, which were created as per original requirements.

Clicking on the Report Builder link allows the user to open the Report Builder tool.

![](veteran-s-crisis-line-version-1-user-guide/074.png)

<span id="_Toc406762444" class="anchor"></span>Figure 70: Report Builder

The Report Builder is structured in a similar way to other Microsoft software. It is consistent with the word processing and spreadsheet software installed on any GFE running Windows.

![](veteran-s-crisis-line-version-1-user-guide/075.png)

<span id="_Toc406762445" class="anchor"></span>Figure 71: New Report

Select Table or Matrix Wizard, in order to create a tabular report using the wizard:

![](veteran-s-crisis-line-version-1-user-guide/076.png)

<span id="_Toc406762446" class="anchor"></span>Figure 72: Table or Matrix Wizard

The wizard will prompt you to select a dataset. Select Create… and click Next:

![](veteran-s-crisis-line-version-1-user-guide/077.png)

<span id="_Toc406762447" class="anchor"></span>Figure 73: Create a dataset

Next is a one-time step, in case the dataset has not been selected:

![](veteran-s-crisis-line-version-1-user-guide/078.png)

<span id="_Toc406762448" class="anchor"></span>Figure 74: Select Data Source

Now the wizard will display a report editor, which has a drag-and-drop canvas where you can select the tables and columns that you need in your report.

![](veteran-s-crisis-line-version-1-user-guide/079.png)

<span id="_Toc406762449" class="anchor"></span>Figure 75: Design a query

## Creating Ad-Hoc/Custom Reports from Scratch

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](veteran-s-crisis-line-version-1-user-guide/080.png)

<span id="_Toc406762450" class="anchor"></span>Figure 76: Selecting an Entity

![](veteran-s-crisis-line-version-1-user-guide/081.png)

<span id="_Toc406762451" class="anchor"></span>Figure 77: Entity Fields

## ![](veteran-s-crisis-line-version-1-user-guide/082.png)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc406762452" class="anchor"></span>Figure 78: Select a Field

The user can add a new title to a report:

<span id="_Toc406762453" class="anchor"></span>![](veteran-s-crisis-line-version-1-user-guide/083.png)Figure 79: Add a new Title

Click Run Report to generate a report based on selected data, and filtering criteria.

![](veteran-s-crisis-line-version-1-user-guide/084.png)

<span id="_Toc406762454" class="anchor"></span>Figure 80: Run Report

After you have successfully created and tested your report, you may publish it so that it is available for others to use later.

> **NOTE:** This function is only available to “Super Admins” who have been setup as part of the VCLREPORTMANAGER Active Directorygroup at AITC.

Thus, in the above manner, the Microsoft Report Builder tool has been seamlessly built in to the VCL custom report functionality. It is a powerful and flexible report building tool, which may be used either in the “Wizard” mode (recommended for tabular, matrix and chart-type reports). Or it may be used directly, by advanced users, by simply cutting and pasting your select statements into a text-based editor.

Microsoft Report Builder is an industry standard product offering from that company. Further detail, in the form of tutorials, training and documentation regarding the usage of this powerful tool, may be obtained from the Microsoft home page for this product.

## Adding Parameters to Existing Reports:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Click on an existing report to open a parameter screen, where you can add parameters such as the latest run dates, user names, VISN’s etc.

<span id="_Toc406762455" class="anchor"></span>![](veteran-s-crisis-line-version-1-user-guide/085.png)Figure 81: Adding Parameters

Supply the input year in the specified format, and click View Report.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 21%" />
<col style="width: 10%" />
<col style="width: 12%" />
<col style="width: 4%" />
<col style="width: 7%" />
<col style="width: 10%" />
<col style="width: 7%" />
<col style="width: 6%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="5">Rescue By VISN By Site By Month<br />
(Fiscal year runs Oct 1 - Sep 30)</th>
<th></th>
<th></th>
<th></th>
<th></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>VISN</td>
<td>Site Name</td>
<td>October</td>
<td>November</td>
<td colspan="2">December</td>
<td>January</td>
<td>June</td>
<td>July</td>
<td>August</td>
</tr>
<tr class="odd">
<td rowspan="2"> </td>
<td> </td>
<td>731</td>
<td>688</td>
<td colspan="2">728</td>
<td>750</td>
<td>4</td>
<td>14</td>
<td>11</td>
</tr>
<tr class="even">
<td>Total</td>
<td>731</td>
<td>688</td>
<td colspan="2">728</td>
<td>750</td>
<td>4</td>
<td>14</td>
<td>11</td>
</tr>
<tr class="odd">
<td rowspan="2">5</td>
<td>BALTIMORE, MD</td>
<td> </td>
<td> </td>
<td colspan="2"> </td>
<td> </td>
<td> </td>
<td>1</td>
<td> </td>
</tr>
<tr class="even">
<td>Total</td>
<td> </td>
<td> </td>
<td colspan="2"> </td>
<td> </td>
<td> </td>
<td>1</td>
<td> </td>
</tr>
<tr class="odd">
<td rowspan="3">6</td>
<td>RICHMOND, VA</td>
<td>1</td>
<td> </td>
<td colspan="2"> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
</tr>
<tr class="even">
<td>SALEM, VA</td>
<td> </td>
<td>1</td>
<td colspan="2"> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
</tr>
<tr class="odd">
<td>Total</td>
<td>1</td>
<td>1</td>
<td colspan="2"> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
</tr>
<tr class="even">
<td rowspan="3">9</td>
<td>MEMPHIS, TN</td>
<td> </td>
<td> </td>
<td colspan="2"> </td>
<td>2</td>
<td> </td>
<td> </td>
<td> </td>
</tr>
<tr class="odd">
<td>MOUNTAIN HOME, TN</td>
<td> </td>
<td> </td>
<td colspan="2"> </td>
<td>1</td>
<td> </td>
<td> </td>
<td> </td>
</tr>
<tr class="even">
<td>Total</td>
<td> </td>
<td> </td>
<td colspan="2"> </td>
<td>3</td>
<td> </td>
<td> </td>
<td> </td>
</tr>
<tr class="odd">
<td rowspan="2">20</td>
<td>ROSEBURG, OR</td>
<td>1</td>
<td>2</td>
<td colspan="2"> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
</tr>
<tr class="even">
<td>Total</td>
<td>1</td>
<td>2</td>
<td colspan="2"> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
</tr>
<tr class="odd">
<td rowspan="3">22</td>
<td>LOMA LINDA, CA</td>
<td> </td>
<td> </td>
<td colspan="2">1</td>
<td>1</td>
<td> </td>
<td> </td>
<td> </td>
</tr>
<tr class="even">
<td>SAN DIEGO, CA</td>
<td>1</td>
<td> </td>
<td colspan="2"> </td>
<td> </td>
<td> </td>
<td> </td>
<td> </td>
</tr>
<tr class="odd">
<td>Total</td>
<td>1</td>
<td> </td>
<td colspan="2">1</td>
<td>1</td>
<td> </td>
<td> </td>
<td> </td>
</tr>
<tr class="even">
<td>Grand Total</td>
<td> </td>
<td>734</td>
<td>691</td>
<td colspan="2">729</td>
<td>754</td>
<td>4</td>
<td>15</td>
<td>11</td>
</tr>
</tbody>
</table>

Acronyms and Abbreviations

| Term | Definition                                                    |
|----------|-------------------------------------------------------------------|
| Admin    | Administration Assistant                                          |
| CAC      | Clinical Application Coordinator                                  |
| CBOC     | Community Based Outpatient Clinic                                 |
| CPRS     | Computerized Patient Record System                                |
| CR’s     | Call Responders                                                   |
| ER       | Emergency Room                                                    |
| FU – F/U | Follow-up                                                         |
| GFE      | Government Furnished Equipment                                    |
| HHS      | Health and Human Services                                         |
| HSS      | Health Science Specialist                                         |
| HT       | Health Technician                                                 |
| ID       | Identification                                                    |
| IE       | Internet Explorer                                                 |
| MCL      | Military Crisis Line                                              |
| MOU      | Memorandum of Understanding                                       |
| MPI      | Master Patient Index                                              |
| MST      | Military Sexual Trauma                                            |
| OEF/OIF  | Operation Enduring Freedom/Operation Iraqi Freedom                |
| PCP      | Primary Care Physician                                            |
| PRF      | Patient Record Flag                                               |
| PTSD     | Post-Traumatic Stress Disorder                                    |
| SAMHSA   | Substance Abuse and Mental Health Services Administration         |
| SDV      | Self-Directed Violence                                            |
| SHL      | Suicide Hotline                                                   |
| SPC      | Suicide Prevention Coordinator                                    |
| SSA      | Social Services Specialist                                        |
| SSN      | Social Security Number                                            |
| TBI      | Traumatic Brain Injury                                            |
| TIU      | Text Integration Utility                                          |
| VA       | The Department of Veterans Affairs                                |
| VAMC     | The Department of Veterans Affairs Medical Center                 |
| VBA      | Veterans Benefit Administration                                   |
| VCL      | Veterans Crisis Line                                              |
| Vet      | Veteran                                                           |
| VISN     | Veterans Integrated Service Network                               |
| VistA    | Veterans (Health) Information Systems and Technology Architecture |
| VISTADUZ | VistA Designated User Code                                        |
| VSC      | Veterans Service Center                                           |
| WT       | Warm Transfer                                                     |