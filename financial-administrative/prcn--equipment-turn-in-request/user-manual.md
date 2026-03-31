---
title: PRCN Version 1 User Manual
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: 
app_code: PRCN
app_name: Equipment / Turn-In Request
section: FIN
app_status: active
pkg_ns: PRCN
patch_ver: 1
patch_id: PRCN*1
group_key: "PRCN:PRCN:1"
file_numbers: []
security_keys: []
menu_options: 9
description: > You may be wondering how the Equipment/Turn-In Request module will change your job. You will be pleased to know that with the Equipment/Turn-In Request module, your job will not change much. The main difference is that you will be entering data via an on-line Equipment Request or Turn-In Request.
audience: 
keywords: 
  - blockquote
  - table
  - contents
  - step
  - class
  - equipment
  - request
  - turn
  - style
  - width
page_count: 0
word_count: 9366
section_count: 41
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: June 1996
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Equip_Turn-In_Request/prcn_1_um.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Equip_Turn-In_Request/prcn_1_um.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=113"
---

> [Department of Veterans Affairs Decentralized Hospital Computer Program](\l)

[EQUIPMENT/TURN-IN REQUEST USER MANUAL](#_bookmark0)

> [Version 1.0 June 1996](#_bookmark0)

> [Information Resource Management Field Office Washington, DC](#_bookmark0)

# [PREFACE](\l)


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [PREFACE](#preface)
- [CHAPTER 1 INTRODUCTION](#chapter-1-introduction)
  - [The Role of the Equipment/Turn-In Request Module](#the-role-of-the-equipmentturn-in-request-module)
  - [How to Use This Manual](#how-to-use-this-manual)
  - [Reference Numbering System](#reference-numbering-system)
  - [Package Management, Legal Requirements and Security Measures](#package-management-legal-requirements-and-security-measures)
  - [Package Operation](#package-operation)
- [CHAPTER 2 REQUESTOR](#chapter-2-requestor)
  - [Introduction](#introduction)
    - [Step 1](#step-1)
    - [Step 2](#step-2)
    - [Step 3](#step-3)
  - [Additional Equipment Requests](#additional-equipment-requests)
    - [Step 1](#step-1-1)
    - [Step 2](#step-2-1)
    - [Step 3](#step-3-1)
    - [Step 4](#step-4)
    - [Step 5](#step-5)
    - [Step 6](#step-6)
    - [Step 7](#step-7)
    - [Step 8](#step-8)
    - [Step 9](#step-9)
    - [Step 10](#step-10)
    - [Step 11](#step-11)
    - [Step 12](#step-12)
    - [Step 13](#step-13)
    - [Step 14](#step-14)
  - [Initial Equipment Requests](#initial-equipment-requests)
    - [Step 1](#step-1-2)
    - [Step 2](#step-2-2)
    - [Step 3](#step-3-2)
  - [Replacement Equipment Requests](#replacement-equipment-requests)
    - [Step 1](#step-1-3)
    - [Step 2](#step-2-3)
    - [Step 3](#step-3-3)
    - [Step 4](#step-4-1)
    - [Step 5](#step-5-1)
    - [Step 6](#step-6-1)
  - [Edit Equipment Request](#edit-equipment-request)
    - [Step 1](#step-1-4)
    - [Step 2](#step-2-4)
    - [Step 3](#step-3-4)
  - [Cancel Equipment Request](#cancel-equipment-request)
    - [Step 1](#step-1-5)
    - [Step 2](#step-2-5)
    - [Step 3](#step-3-5)
    - [Step 4](#step-4-2)
  - [Request Status Report](#request-status-report)
  - [Display/Print Equipment Request](#displayprint-equipment-request)
  - [Resubmit Requests](#resubmit-requests)
    - [Step 1](#step-1-6)
    - [Step 2](#step-2-6)
  - [Split Equipment Request](#split-equipment-request)
  - [Process Equipment Turn-Ins Menu](#process-equipment-turn-ins-menu)
    - [Enter Excess Equipment Turn-In Request](#enter-excess-equipment-turn-in-request)
    - [Step 2](#step-2-7)
    - [Step 3](#step-3-6)
    - [Edit Excess Equipment Turn-In Document](#edit-excess-equipment-turn-in-document)
    - [Cancel Excess Equipment Turn-In Request](#cancel-excess-equipment-turn-in-request)
- [CHAPTER 3 CMR RESPONSIBLE OFFICIAL](#chapter-3-cmr-responsible-official)
  - [Enter New Equipment Request](#enter-new-equipment-request)
  - [Edit Equipment Request](#edit-equipment-request-1)
  - [Cancel Equipment Request](#cancel-equipment-request-1)
  - [Request Status Report](#request-status-report-1)
  - [Display/Print Equipment Request](#displayprint-equipment-request-1)
  - [Approve Equipment Requests (CMR Responsible Official)](#approve-equipment-requests-cmr-responsible-official)
    - [Step 1](#step-1-7)
    - [Step 2](#step-2-8)
    - [Step 3](#step-3-7)
    - [Step 4](#step-4-3)
    - [Step 5](#step-5-2)
    - [Step 6](#step-6-2)
  - [Process Equipment Turn-Ins](#process-equipment-turn-ins)
  - [Approving Turn-In Request](#approving-turn-in-request)
    - [Enter Equipment Turn-In Request](#enter-equipment-turn-in-request)
    - [Step 1](#step-1-8)
    - [Step 2](#step-2-9)
    - [Step 3](#step-3-8)
    - [Edit Equipment Turn-In Request](#edit-equipment-turn-in-request)
    - [Cancel Turn-In Request](#cancel-turn-in-request)
    - [Display/Print Turn-In Request](#displayprint-turn-in-request)
    - [Approve Equipment Turn-In Request](#approve-equipment-turn-in-request)
    - [Step 1](#step-1-9)
    - [Step 2](#step-2-10)
- [CHAPTER 4 PERSONAL PROPERTY MANAGER (PPM)](#chapter-4-personal-property-manager-ppm)
  - [Review Equipment Request (PPM)](#review-equipment-request-ppm)
    - [Step 1](#step-1-10)
    - [Step 2](#step-2-11)
    - [Step 3](#step-3-9)
    - [Step 4](#step-4-4)
    - [Step 5](#step-5-3)
    - [Step 6](#step-6-3)
    - [Step 7](#step-7-1)
    - [Step 8](#step-8-1)
  - [Edit Equipment Request (PPM)](#edit-equipment-request-ppm)
  - [Cancel Equipment Request (PPM)](#cancel-equipment-request-ppm)
  - [Rank Equipment Requests](#rank-equipment-requests)
  - [Create 2237 (PPM)](#create-2237-ppm)
    - [Step 1](#step-1-11)
    - [Step 2](#step-2-12)
  - [Display/Print Equipment Request](#displayprint-equipment-request-2)
  - [Equipment Request Reports Menu](#equipment-request-reports-menu)
    - [Controlled Equipment Report](#controlled-equipment-report)
    - [Request Status Report](#request-status-report-2)
    - [Turn-In Status by CMR](#turn-in-status-by-cmr)
    - [Turn-In Status by Transaction Number](#turn-in-status-by-transaction-number)
    - [Turn-In Status Report](#turn-in-status-report)
  - [Process Turn-Ins Menu](#process-turn-ins-menu)
    - [Process Turn-In Request](#process-turn-in-request)
    - [Disposition of a Turn-In Document](#disposition-of-a-turn-in-document)
- [CHAPTER 5 ENGINEERING](#chapter-5-engineering)
    - [Step 1](#step-1-12)
    - [Step 2](#step-2-13)
    - [Step 3](#step-3-10)
    - [Step 4](#step-4-5)
    - [Step 5](#step-5-4)
    - [Step 6](#step-6-4)
    - [Step 7](#step-7-2)
    - [Step 8](#step-8-2)
    - [Step 9](#step-9-1)
    - [Step 10](#step-10-1)
    - [Step 11](#step-11-1)
- [CHAPTER 6 OTHER CONCURRING OFFICIALS](#chapter-6-other-concurring-officials)
    - [Step 1](#step-1-13)
    - [Step 2](#step-2-14)
    - [Step 3](#step-3-11)
    - [Step 3](#step-3-12)
- [CHAPTER 7 EQUIPMENT COMMITTEE](#chapter-7-equipment-committee)
  - [Rank Equipment Requests](#rank-equipment-requests-1)
  - [Equipment Request Cost Summary Report](#equipment-request-cost-summary-report)
  - [Outstanding Equipment Requests Report](#outstanding-equipment-requests-report)
  - [Process Equip Committee Decisions](#process-equip-committee-decisions)
    - [Step 1](#step-1-14)
    - [Step 2](#step-2-15)
    - [Step 3](#step-3-13)
    - [Step 4](#step-4-6)
    - [Step 5](#step-5-5)
  - [Service Priority Report](#service-priority-report)
    - [All Services](#all-services)
    - [One Service](#one-service)
- [CHAPTER 8 WAREHOUSE](#chapter-8-warehouse)
    - [Step 1](#step-1-15)
    - [Step 2](#step-2-16)
    - [Step 3](#step-3-14)
- [CHAPTER 9 TURN-INS](#chapter-9-turn-ins)
  - [Requestor](#requestor)
    - [Enter Excess Equipment Turn-In Request](#enter-excess-equipment-turn-in-request-1)
    - [Step 2](#step-2-17)
    - [Step 3](#step-3-15)
    - [Edit Excess Equipment Turn-In Document](#edit-excess-equipment-turn-in-document-1)
    - [Cancel Excess Equipment Turn-In Request](#cancel-excess-equipment-turn-in-request-1)
  - [CMR Official](#cmr-official)
    - [Enter Equipment Turn-In Request](#enter-equipment-turn-in-request-1)
    - [Edit Equipment Turn-In Request](#edit-equipment-turn-in-request-1)
    - [Cancel Turn-In Request](#cancel-turn-in-request-1)
    - [Display/Print Turn-In Request](#displayprint-turn-in-request-1)
    - [Approve Equipment Turn-In Request](#approve-equipment-turn-in-request-1)
    - [Step 1](#step-1-16)
    - [Step 2](#step-2-18)
  - [PPM Official](#ppm-official)
    - [Process Turn-In Request (Pending PPM Review)](#process-turn-in-request-pending-ppm-review)
    - [Process Turn-In Request (Work Order Completed)](#process-turn-in-request-work-order-completed)
    - [Final Disposition of a Turn-In](#final-disposition-of-a-turn-in)
- [CHAPTER 10 GLOSSARY](#chapter-10-glossary)
> [The Equipment Request/Turn-In Request Module Version 1.0 will provide support to a variety of administrative activities in your medical center, such as your non- expendable equipment requests and any equipment turn-ins.](#table-of-contents)
> June 1996 Equipment/Turn-In Request Version 1.0 i User Manual
> Preface
> ii Equipment/Turn-In Request Version 1.0 June 1996 User Manual

# CHAPTER 1 INTRODUCTION

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## The Role of the Equipment/Turn-In Request Module

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> You may be wondering how the Equipment/Turn-In Request Module will change your job. You will be pleased to know your job will not change much. The main difference is that you will be entering data in IFCAP to establish equipment requests or create a turn-in. Since you already use IFCAP, you are already halfway toward becoming a user of this module.

## How to Use This Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This guide shows you what you need to know about using the Equipment/Turn-In Request Module. Each procedure contained in the module is explained in full detail. Remember, you can always enter a question mark (?) to ask for help if you forget what to type or you feel unsure of what is required. Your Application Coordinator is also available to answer your questions.

## Reference Numbering System

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This guide is divided into explanations of each step that must be successfully completed before the items can be ordered through the normal IFCAP purchasing procedure. By the time you finish this guide, you will know how an equipment request is processed before purchase and how to turn in equipment items.

> Using a computer to help you do your job can be very exciting and challenging. Just like learning anything brand new, it can be frustrating in the beginning. Be patient with yourself. Soon you will be an "expert" in doing an Equipment Request or creating a Turn-In.

## Package Management, Legal Requirements and Security Measures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Functionally, the Equipment/Turn-In Request module has several organizational elements that use different components of the software. Non-expendable equipment must go through several approval steps before it can be ordered.

- Requestor
- Consolidated Memorandum of Receipt (CMR) Official
- Personal Property Manager (PPM)
- Equipment Committee
- Engineering
- Other Concurring Officials

> Turning in non-expendable equipment also requires several approval steps.

- Requestor

> June 1996 Equipment/Turn-In Request Version 1.0 1

> User Manual

> <span id="1.5__Package_Operation" class="anchor"></span>Introduction

- Consolidated Memorandum of Receipt (CMR) Official
- Personal Property Manager (PPM)
- Engineering
- Warehouse

## Package Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> All Equipment Requests and Turn-Ins must be completed on the computer. The information the computer requires should be familiar to you. If not, a question mark in response to a prompt from the computer provides you with information which should help you respond.

> The questions you see when processing non-expendable equipment requests are different from the questions you see when processing expendable requests. These differences stem from the different requirements. Instead of control points, your non-expendable equipment requests and turn-ins will be tracked by department or Consolidated Memoranda of Receipts (CMR) number. These requests will be sent to the appropriate CMR Responsible Official for approval. Once approved, the requests are released to the A&MM activity for processing.

2.  Equipment/Turn-In Request Version 1.0 June 1996 User Manual

# CHAPTER 2 REQUESTOR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> You may be wondering how the Equipment/Turn-In Request module will change your job. You will be pleased to know that with the Equipment/Turn-In Request module, your job will not change much. The main difference is that you will be entering data via an on-line Equipment Request or Turn-In Request.

### Step 1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <span id="_bookmark7" class="anchor"></span>Select the ‘Equipment Request Menu (Requestor)’ that has been set up on your main menu. Select ‘Enter New Equipment Request’ to begin the process. If your site parameters are set up for a multi-divisional site, you will be asked to identify the Station Number. If you are not at a multi-divisional site, the prompt will default to your Station Number.

### Step 2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> You will then be asked to select the CMR Name. Enter a question mark (?) to see the possible CMR numbers/names you can select from. The CMR Responsible Official is the individual designated as the responsible official for a particular CMR.

> Your non-expendable equipment request has now been assigned a temporary transaction number. This will be the identification number for this request during the life-cycle of this process. Upon approval of the request by the Equipment Committee, a 2237 will be established and assigned a permanent transaction number by the A&MM activity.

### Step 3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The next important prompt will be the Request Type. The request type will determine the next sequence of questions/steps. Additional means that this request is a normal request for new equipment. Initial means that this request is associated with a construction project. Replacement means that you will be asked to identify what existing equipment this new piece of equipment will replace. A corresponding Turn-In request will be generated along with a Replacement request.

## Additional Equipment Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> June 1996 Equipment/Turn-In Request Version 1.0 3

> User Manual

> <span id="2.4.1.1_Step_1" class="anchor"></span>Requestor

### Step 1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Begin the request by identifying the request type as Additional.

### Step 2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Date Required By field is required. A particular Sort or Classification can also be assigned to the request at this time. Any data entered here will be moved over to<span id="2.4.1.3_Step_3" class="anchor"></span> the 2237 when the request passes through all stages and is approved and funded.

### Step 3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> There must be at least one line item entered per request. A word-processing Description of the item will then be required. Other fields associated with each line item are: the Potential Vendor, the Vendor Product number, the Unit Cost, the Quantity Required, and the Contract \# field. When entering a possible vendor at the Potential Vendor field, the Vendor file (#440) will be checked for any matching vendors. Matching vendors will be filed in the Potential Vendor Ptr field and will show up there in the Display/Print or viewing of the request. If no matching vendor is found in the Vendor file (#440), then the free text vendor which was just entered will be filed in the Potential Vendor field and will show up for that field in the Display/Print or viewing of the request. In the next two screens, Cannon is an example of free text and ABC is an example of a vendor found in the Vendor file (#440). The last important field identifying a line item is the Parent System/ Component field. Components may be listed as individual parts that make up the parent system. The Parent item is the primary item tracked by AEMS/MERS, for which a CMR will have ultimate responsibility.

> 4 Equipment/Turn-In Request Version 1.0 June 1996 User Manual

<span id="_bookmark12" class="anchor"></span>Requestor

### Step 4

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> You will be prompted for another line item. You may enter as many line items as needed or press return to continue with the remaining questions.

### Step 5

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A justification of why the item or items are being requested is mandatory.

### Step 6

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Change in Personnel would be answered with a 'Yes' if additional personnel are needed to operate this equipment. If answered 'Yes', an explanation is required and should include information as to type of change in personnel, number of personnel and job level.

> June 1996 Equipment/Turn-In Request Version 1.0 5

> User Manual

> <span id="2.4.1.7_Step_7" class="anchor"></span>Requestor

### Step 7

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If there is a JCAHO or other safety deficiency, the requestor must explain what it is.

### Step 8

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If there is an increase in recurring costs you will be asked if there are sufficient funds budgeted for this increase and to explain the cause of the increase. Also, you must enter the approximate cost for supplies which may occur if this equipment is purchased. If there is a decrease in recurring costs, explain why there is a decrease and enter the approximate amount of the decrease. Entering no change will go on to the next step without asking for any further information.

> 6 Equipment/Turn-In Request Version 1.0 June 1996 User Manual

Requestor

### Step 9

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The next group of responses is dependent on whether extra training is needed in order to operate the requested equipment. If training is needed, then you must explain the type of training needed and provide an estimated training cost.

> June 1996 Equipment/Turn-In Request Version 1.0 7

> User Manual

> <span id="2.4.1.10_Step_10" class="anchor"></span>Requestor

### Step 10

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <span id="_bookmark19" class="anchor"></span>Answer 'Yes' if a maintenance contract recommended for the equipment being requested. If a maintenance contract is recommended, an explanation of why and an estimated cost of the contract are required.

### Step 11

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Please indicate if space is available for this equipment and where it will be located. The location may be available from the Space file. If the location is not available from the Space file, then a free text location is acceptable.

### Step 12

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Please indicate if utilities are required for installation of this equipment. This will help the Engineering department in their evaluation of the request.

> 8 Equipment/Turn-In Request Version 1.0 June 1996 User Manual

Requestor

### Step 13

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Please indicate if there is a point of contact for this request other than yourself. You may select the person from the New Person file (200).

### Step 14

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Send the request to the CMR Responsible Official responsible to review this request.

> After responding ‘Yes’, the CMR Responsible Official will see a message that a request is available for his/her review and approval when signing onto their Equipment Request Menu.

> June 1996 Equipment/Turn-In Request Version 1.0 9

> User Manual

> <span id="2.4.2_Initial_Equipment_Requests" class="anchor"></span>Requestor

## Initial Equipment Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Step 1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Initial equipment requests are requests that may go with a particular planned project. These should be items that are required when a project is completed, such as a new patient wing.

### Step 2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> <span id="_bookmark25" class="anchor"></span>For an initial equipment request, project number and project manager entries are required. When selecting a project, the Chief Engineer will default for the project manager.

### Step 3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Follow 2.4.1.2 Step 2 through 2.4.1.13 Step 14 to complete an initial request.

> 10 Equipment/Turn-In Request Version 1.0 June 1996 User Manual

<span id="2.4.3_Replacemt._Equip._Requests" class="anchor"></span>Requestor

## Replacement Equipment Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Step 1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If equipment needs to be replaced, a simultaneous turn-in request will be generated with the new requested equipment by selecting a replacement request type.

### Step 2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> As with initial type requests, replacement requests prompt you to enter a project<span id="_bookmark28" class="anchor"></span> number and project manager. Unlike an initial request, however, these are not required entries, and you may pass them by pressing return.

### Step 3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Follow 2.4.1.3 Step 3 to enter line items.

### Step 4

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In a replacement equipment request, part of entering line items includes entering the item which is being replaced. For every quantity entered, if an item has been designated as a Parent, you are required to enter a replacement item from the AEMS/MERs file. It is not mandatory to enter a replacement item if a requested item is a Component. The items from which you may select from will be limited to those items which fall under the CMR to which you are directing this request. For example, if you are requesting 3 replacement trucks, you must identify the three trucks which will be replaced and turned in.

> June 1996 Equipment/Turn-In Request Version 1.0 11

> User Manual

> <span id="_bookmark29" class="anchor"></span>Requestor

### Step 5

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> After selecting the correct replacement item, indicate why this item needs to be replaced. If the reason is not listed, enter other and enter a reason up to 70 characters.

### Step 6

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Follow 2.4.1.5 Step 5 through 2.4.1.14 Step 14 to complete a replacement equipment request. Reminder: There are now two requests on file, one replacement request and one turn-in request for the item being replaced.

## Edit Equipment Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If you exit the system before completing a new equipment request, or a request is returned by other reviewers, you may edit the request. You will not be allowed to edit the request type. If the request type is not accurate, you must cancel and re­ enter the request.

> 12 Equipment/Turn-In Request Version 1.0 June 1996 User Manual

<span id="2.5.1_Step_1" class="anchor"></span>Requestor

### Step 1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Answering ‘No’ to the question, ‘Do you want to edit this request?’ returns you to the menu.

### Step 2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Data editing begins with DATE REQUIRED BY for additional type requests and PROJECT NUMBER for replacement and initial requests. The prompts are the same as entering a new equipment request and defaults to information already entered. You will be prompted if this request is ready to go to the CMR Official. If<span id="_bookmark34" class="anchor"></span> you do not answer 'Y'es then you may edit the request further. Once it has gone to the CMR Responsible Official, no further editing is allowed unless it is returned to you as a result of non-approval by other responsible officials during the review process. Other options available are cancel or split the request. These options will be discussed in 2.6 Cancel Equipment Request and 2.10 Split Equipment Request.

### Step 3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Follow 2.4.1.2 through 2.4.1.14 to complete request.

## Cancel Equipment Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> You may need to cancel an equipment request that has not been approved by the CMR Responsible Official, the Personal Property Manager. It must be returned to your control before you may cancel it. You may also, at any time, cancel a request that has not been completed or forwarded to the CMR Responsible Official.

> June 1996 Equipment/Turn-In Request Version 1.0 13

> User Manual

> Requestor

### Step 1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Select the transaction you wish to cancel.

### Step 2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Information concerning this request will display for your review.

### Step 3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Enter a reason why the request is being cancelled.

### Step 4

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If the request is a replacement equipment request and has an associated turn-in document, you will be asked to cancel the turn-in document.

## Request Status Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If you would like to see the status of the equipment requests that you have entered, run the Request Status Report.

> 14 Equipment/Turn-In Request Version 1.0 June 1996 User Manual

<span id="2.8_Display/Print_Equipment_Req" class="anchor"></span>Requestor

## Display/Print Equipment Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use this menu option to print out a hardcopy of a request.

## Resubmit Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use this option to resubmit certain requests. The request will go back to pending Equipment Committee review and approval without having to go through all the steps again.

> June 1996 Equipment/Turn-In Request Version 1.0 15

> User Manual

> Requestor

### Step 1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Review the transactions that are eligible for resubmission.

### Step 2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Resubmitted requests are assigned the status which reflects the approval steps they have already been through.

## Split Equipment Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option allows for splitting a request if returned to the requestor. Any new transaction number will be the same as the old number, but have a new suffix added to it, e.g. A, B, C.

> 16 Equipment/Turn-In Request Version 1.0 June 1996 User Manual

Requestor

## Process Equipment Turn-Ins Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If you wish to turn-in equipment without ordering replacement equipment, select the Process Equipment Turn-Ins menu option so that the request may go through the proper channels.

### Enter Excess Equipment Turn-In Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Step 1

> Select the Enter Excess Equipment Turn-In Request option from the Process Turn- Ins menu. The first two entries you make establish the temporary request number for this turn-in document. If your site parameters are set up for a multi-divisional site, you will be asked to identify the Station Number, otherwise it will default to your station number.

> June 1996 Equipment/Turn-In Request Version 1.0 17

> User Manual

> Requestor

### Step 2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Select the CMR Responsible Official responsible for the equipment being turned in.

> Your equipment turn-in document has now been assigned a temporary transaction number. Refer to this number during the life cycle of the request.

### Step 3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> You will be asked next to select the items from the Equipment Inventory (AEMS/MERS) file that you wish to turn in. After you have selected and filled in the justification for turning in this equipment, it will go to the responsible CMR Responsible Official for review and approval.

> 18 Equipment/Turn-In Request Version 1.0 June 1996 User Manual

<span id="2.11.2_Edit_Excess_Equip/T-In_Doc" class="anchor"></span>Requestor

### Edit Excess Equipment Turn-In Document

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If a turn-in document has been left incomplete, then the ability exists for you, the requestor, to make changes and even add additional items.

### Cancel Excess Equipment Turn-In Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The ability to cancel an incomplete or returned turn-in document also exists.

> June 1996 Equipment/Turn-In Request Version 1.0 19

> User Manual

> [Requestor](#table-of-contents)

> [20 Equipment/Turn-In Request Version 1.0 June 1996 User Manual](#table-of-contents)

# CHAPTER 3 CMR RESPONSIBLE OFFICIAL

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Below you will see a brief description of the options and sub-menus found on the Equipment Request menu if you are the assigned CMR Responsible Official. A quick review of these descriptions should help you understand when to use an option. The rest of this manual goes into detail explaining <u>how</u> to use each option.

## Enter New Equipment Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A CMR Responsible Official can enter requests for equipment.

## Edit Equipment Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A CMR Responsible Official can also edit equipment requests if necessary. Please review Chapter 2 on how to edit Equipment Requests

## Cancel Equipment Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A CMR Responsible Official can also cancel equipment requests that he/she has entered. Please review Chapter 2 on how to cancel Equipment Requests.

> June 1996 Equipment/Turn-In Request Version 1.0 21

> User Manual

> CMR Responsible Official

## Request Status Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If you would like to see the status of equipment requests that you, the CMR Responsible Official, have approved, run the Request Status Report. It will print all the requests that were submitted to you.

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 47%" />
<col style="width: 15%" />
<col style="width: 13%" />
<col style="width: 1%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="4"><blockquote>
<p>Equipment Request Status Report by CMR Official ETRUSER , ONE</p>
</blockquote></th>
<th rowspan="3"></th>
</tr>
<tr class="odd">
<th></th>
<th></th>
<th><blockquote>
<p>Date</p>
</blockquote></th>
<th><blockquote>
<p>Status</p>
</blockquote></th>
</tr>
<tr class="header">
<th><blockquote>
<p>Transaction #</p>
</blockquote></th>
<th><blockquote>
<p>Status</p>
</blockquote></th>
<th><blockquote>
<p>Entered</p>
</blockquote></th>
<th><blockquote>
<p>Date</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>621-780-96-00004</p>
</blockquote></td>
<td><blockquote>
<p>Pending Equipment Committee Approval</p>
</blockquote></td>
<td><blockquote>
<p>02/09/96</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>08/03/96</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>621-780-96-00014</p>
</blockquote></td>
<td><blockquote>
<p>Pending Completion by Requestor</p>
</blockquote></td>
<td><blockquote>
<p>04/11/96</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>06/30/96</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>621-780-96-00017</p>
</blockquote></td>
<td><blockquote>
<p>Pending CMR Official Review</p>
</blockquote></td>
<td><blockquote>
<p>06/30/96</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>06/30/96</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>621-780-96-00019</p>
</blockquote></td>
<td><blockquote>
<p>Pending Completion by Requestor</p>
</blockquote></td>
<td><blockquote>
<p>06/30/96</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>06/30/96</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>621-781-96-00011</p>
</blockquote></td>
<td><blockquote>
<p>Ready for 2237 Processing</p>
</blockquote></td>
<td><blockquote>
<p>05/18/96</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>07/27/96</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>621-781-96-00001</p>
</blockquote></td>
<td><blockquote>
<p>Pending Equipment Committee Approval</p>
</blockquote></td>
<td><blockquote>
<p>06/21/96</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>08/03/96</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>621-781-96-00002</p>
</blockquote></td>
<td><blockquote>
<p>Ready for 2237 Processing</p>
</blockquote></td>
<td><blockquote>
<p>06/22/96</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>07/27/96</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>621-781-96-00004</p>
</blockquote></td>
<td><blockquote>
<p>Pending Equipment Committee Approval</p>
</blockquote></td>
<td><blockquote>
<p>07/31/96</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>08/03/96</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>621-781-96-00005</p>
</blockquote></td>
<td><blockquote>
<p>Pending Equipment Committee Approval</p>
</blockquote></td>
<td><blockquote>
<p>07/31/96</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>08/02/96</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>621-781-96-00008</p>
</blockquote></td>
<td><blockquote>
<p>Pending PPM Review</p>
</blockquote></td>
<td><blockquote>
<p>08/04/96</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>08/04/96</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>621-782-96-00002</p>
</blockquote></td>
<td><blockquote>
<p>Pending Equipment Committee Approval</p>
</blockquote></td>
<td><blockquote>
<p>07/28/96</p>
</blockquote></td>
<td colspan="2"><blockquote>
<p>08/02/96</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Display/Print Equipment Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use this menu option to print out a hardcopy of a request.

## Approve Equipment Requests (CMR Responsible Official)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The CMR Responsible Official must review and approve equipment requests. Ultimately the CMR Responsible Official is responsible for the inventory of that item. If the CMR Responsible Official does not approve the request at this time, it will be returned to the user with an explanation. If the CMR Responsible Official does approve this request, he/she must sign off his/her approval. At this time they may also assign a priority to this request. This priority assists the Equipment Committee in determining the importance of this item to the using service.

> 22 Equipment/Turn-In Request Version 1.0 June 1996 User Manual

> <span id="3.6.1_Step_1" class="anchor"></span>CMR Responsible Official

### Step 1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Select the option Approve Equipment Requests (CMR Official) from the menu option.

### Step 2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Select the request transaction to review.

### Step 3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Answer either ‘Yes’ to approve the request or ‘No’ to disapprove the request.

### Step 4

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If the request is not to be approved, an explanation is required. A mail message will be sent to the requestor which will include the explanation. See 3.6.6 Step 6 for a sample mail message.

> June 1996 Equipment/Turn-In Request Version 1.0 23

> User Manual

> <span id="3.6.5_Step_5" class="anchor"></span>CMR Responsible Official

### Step 5

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The next step is to identify a priority. This priority will show the PPM and the Equipment Committee the importance of this request.

### Step 6

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This is a sample mail message that will be sent to the requestor when a request is not approved.

## Process Equipment Turn-Ins

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The CMR Responsible Official must review and approve Turn-In documents since they are responsible for that equipment.

## Approving Turn-In Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The CMR Responsible Official will be notified when a turn-in request has been generated and will select the Process Equipment Turn-Ins Menu option.

> 24 Equipment/Turn-In Request Version 1.0 June 1996 User Manual

> <span id="3.7.1.1_Enter_Equip/T-In_Req" class="anchor"></span>CMR Responsible Official

> After selecting the Process Equipment Turn-Ins Menu option, the CMR Official will have the following selections.

### Enter Equipment Turn-In Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Select Enter Equipment Turn-In Request option from menu. A CMR Responsible Official can act as a requestor for entering turn-in documents.

### Step 1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Select the CMR Responsible Official record in which item(s) to be turned in are located.

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 56%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>422</p>
</blockquote></th>
<th><blockquote>
<p>SURGERY</p>
</blockquote></th>
<th><blockquote>
<p>ETRPROVIDER , ONE</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>423</p>
</blockquote></td>
<td><blockquote>
<p>SURGERY</p>
</blockquote></td>
<td><blockquote>
<p>ETRPROVIDER , ONE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>500</p>
</blockquote></td>
<td><blockquote>
<p>RADIOLOGY</p>
</blockquote></td>
<td><blockquote>
<p>ETRPROVIDER , TWO</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>666</p>
</blockquote></td>
<td><blockquote>
<p>RADIOLOGY</p>
</blockquote></td>
<td><blockquote>
<p>ETRUSER , THREE</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>780</p>
</blockquote></td>
<td><blockquote>
<p>ACQUISITION &amp; MATERIEL MGMT</p>
</blockquote></td>
<td><blockquote>
<p>ETRUSER , ONE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>781</p>
</blockquote></td>
<td><blockquote>
<p>ACQUISITION &amp; MATERIEL MGMT</p>
</blockquote></td>
<td><blockquote>
<p>ETRUSER , ONE</p>
</blockquote></td>
</tr>
</tbody>
</table>

> June 1996 Equipment/Turn-In Request Version 1.0 25

> User Manual

> <span id="3.7.1.1.2_Step_2" class="anchor"></span>CMR Responsible Official

### Step 2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Select the item or items to be turned in.

> Select REPLACEMENT ITEM NUMBER: ? \<RET\>

> Answer with TURN-IN LINE ITEM TURN-IN LINE ITEM NUMBER, or REPLACEMENT ITEM NUMBER

> You may enter a new TURN-IN LINE ITEM, if you wish

> Please select the entry from the Equipment Inventory file that you wish to turn-in.

> Choose From:

> 3 BLOOD CHEMICAL ANALYZER

9.  BATHTUB ETRVENDOR , F IVE UNIT
10. BATHTUB ETRVENDOR , F IVE UNIT
11. BATHTUB ETRVENDOR , F IVE UNIT

> 20 ETRVENDOR , S IX CONTROL MONITOR

22. ETRVENDOR , S IX CONTROL MONITOR
23. ETRVENDOR , S IX CONTROL MONITOR

> Select REPLACEMENT ITEM: 23 \<RET\> ETRVENDOR , S IX CONTROL MONITOR TURN-IN LINE ITEM TURN-IN LINE ITEM NUMBER: 1// \<RET\>

> TURN-IN LINE ITEM DESCRIPTION: ETRVENDOR , S IX CONTROL MONITOR

> Replace \<RET\>

> CSN: 1005-000667

> <span id="_bookmark52" class="anchor"></span>Description: ETRVENDOR , S IX CONTROL MONITOR

> Model \#: Serial \#:

> Manufacturer:

> Acquisition Value: \$150.00 CMR: 780 JUSTIFICATION: ? \<RET\>

> Choose From:

1.  Fair wear and tear
2.  Excess equipment failure/repair
3.  Upgrade
4.  State-of-art technology
5.  Replacement due to loss or damage
6.  Other

> Replacement Justification: 4 \<RET\> State-of-art technology Select REPLACEMENT ITEM NUMBER: \<RET\>

### Step 3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Send request to the appropriate CMR Responsible Official for review and approval.

### Edit Equipment Turn-In Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> See 2.11.2 for more information.

### Cancel Turn-In Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> See 2.11.3 for more information.

### Display/Print Turn-In Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> 26 Equipment/Turn-In Request Version 1.0 June 1996 User Manual

> CMR Responsible Official

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 37%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>25</p>
</blockquote></th>
<th>621-780-95-00007</th>
<th><blockquote>
<p>Turn-in Completed</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>26</p>
</blockquote></td>
<td>621-780-95-00012</td>
<td><blockquote>
<p>Pending PPM Final Disposition</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>27</p>
</blockquote></td>
<td>621-323-95-00002</td>
<td><blockquote>
<p>Pending PPM Final Disposition</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>28</p>
</blockquote></td>
<td>621-323-95-00003</td>
<td><blockquote>
<p>Pending Warehouse Pickup</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>29</p>
</blockquote></td>
<td>621-123-96-00006</td>
<td><blockquote>
<p>Cancelled Request</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>30</p>
</blockquote></td>
<td>621-123-96-00007</td>
<td><blockquote>
<p>Cancelled Request</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>31</p>
</blockquote></td>
<td>621-666-96-00001</td>
<td><blockquote>
<p>Pending Warehouse Pickup</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>38</p>
</blockquote></td>
<td>621-666-96-00010</td>
<td><blockquote>
<p>Pending PPM Review</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>39</p>
</blockquote></td>
<td>621-136-96-00002</td>
<td><blockquote>
<p>Pending PPM Review</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>49</p>
</blockquote></td>
<td>621-780-96-00001</td>
<td><blockquote>
<p>Pending CMR Official Review</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>50</p>
</blockquote></td>
<td>621-780-96-00002</td>
<td><blockquote>
<p>Pending Completion by Requestor</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>51</p>
</blockquote></td>
<td>621-780-96-00003</td>
<td><blockquote>
<p>Pending CMR Official Review</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>52</p>
</blockquote></td>
<td>621-780-96-00004</td>
<td><blockquote>
<p>Pending CMR Official Review</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>53</p>
</blockquote></td>
<td>621-780-96-00006</td>
<td><blockquote>
<p>Pending Completion by Requestor</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>54</p>
</blockquote></td>
<td>621-666-96-00013</td>
<td><blockquote>
<p>Pending Completion by Requestor</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><span id="_bookmark53" class="anchor"></span>55</p>
</blockquote></td>
<td>621-666-96-00015</td>
<td><blockquote>
<p>Pending Completion by Requestor</p>
</blockquote></td>
</tr>
</tbody>
</table>

### Approve Equipment Turn-In Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The CMR Responsible Official responsible for the equipment must review and approve any turn-in documents prior to review by the Personal Property Manager.

> June 1996 Equipment/Turn-In Request Version 1.0 27

> User Manual

> CMR Responsible Official

### Step 1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Select the request you wish to review.

### Step 2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The request will display on the screen.

> 28 Equipment/Turn-In Request Version 1.0 June 1996 User Manual

# CHAPTER 4 PERSONAL PROPERTY MANAGER (PPM)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Personal Property Manager (or PPM) has many levels of review for both equipment and turn-in requests. When you sign onto the Equipment Request Menu (PPM), you will see the number and status of equipment and turn-in requests.

## Review Equipment Request (PPM)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Step 1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Select request to review. You must determine whether or not the requested item is considered non-expendable (either capitalized or expensed). If you determine that the item is not non-expendable, the request is returned to the requestor with a mail message. A copy of the mail message will go to the CMR Responsible Official who approved the request. An explanation detailing why this item is not considered non-expendable will be included in this message.

> June 1996 Equipment/Turn-In Request Version 1.0 29

> User Manual

> <span id="_bookmark57" class="anchor"></span>PPM

### Step 2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Sample mail message to the requestor and CMR Responsible Official.

### Step 3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A request determined to be non-expendable is sent on to Engineering for their review and approval. See Chapter 5 for information that Engineering will provide for a request.

> 30 Equipment/Turn-In Request Version 1.0 June 1996 User Manual

<span id="4.1.4_Step_4" class="anchor"></span>PPM

### Step 4

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> After Engineering has reviewed and process the request, the request is returned to the PPM for further processing.

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 38%" />
<col style="width: 47%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>82</p>
</blockquote></th>
<th>621-666-96-00002</th>
<th><blockquote>
<p>Engineering Review Completed</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>83</p>
</blockquote></td>
<td>621-666-96-00007</td>
<td><blockquote>
<p>Engineering Review Completed</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>89</p>
</blockquote></td>
<td>621-136-96-00010</td>
<td><blockquote>
<p>Pending PPM Review</p>
</blockquote></td>
</tr>
</tbody>
</table>

### Step 5

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The PPM determines if there are any other persons who should review and give their approval for the items in a request. If no further review is needed, the request will go to be prepared for the Equipment Committee’s review.

> June 1996 Equipment/Turn-In Request Version 1.0 31

> User Manual

> <span id="4.1.6_Step_6" class="anchor"></span>PPM

### Step 6

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Select any person already in the Concurring Official File or select a new person from the New Person file (200). Also enter the date by which the Concurring Official(s) should either approve or disapprove the request. This date will appear on the mail message. See Chapter 6 for Concurring Official processing steps.

### Step 7

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If multiple concurring officials were assigned to review the request and opinions do not coincide, then the request will be approved if 50% or more approve or will disapprove if 50% or more do not approve the request.

### Step 8

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When concurrence is finished and the request is approved it will be returned to PPM to determine if an item can be designated as a controlled item. After answering that question, requests which are not Initial (associated with a project) will go directly to the Equipment Committee for approval. All other requests will go to be reviewed and ranked for the Equipment Committee.

> 32 Equipment/Turn-In Request Version 1.0 June 1996 User Manual

PPM

> Good afternoon ETRUSER , F IVE You last signed on today at 12:59 P.M.

> There is 1 equipment request Pending PPM Review.

> There are 2 equipment requests Concurrence Completed

> There are 5 equipment requests Ready for 2237 Processing. Select EQUIPMENT REQUEST TRANSACTION NUMBER: ?? \<RET\>

> Choose from:

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 43%" />
<col style="width: 40%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>83</p>
</blockquote></th>
<th>621-666-96-00007</th>
<th><blockquote>
<p>Concurrence Completed</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>89</p>
</blockquote></td>
<td>621-136-96-00010</td>
<td><blockquote>
<p>Pending PPM Review</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Select EQUIPMENT REQUEST TRANSACTION NUMBER: 83 \<RET\> 621-666-96-00007 Concurrence

> Completed

> Do you want to view the information related to this request? Yes// \<RET\> (Yes) DEVICE: HOME// \<RET\>

> TRANSACTION NUMBER: 621-666-96-00007 REQUESTOR: ETRUSER , FOUR

> REQUESTING SERVICE: ETRVENDOR , SEVEN

> REQUEST DATE/TIME: FEB 01, 1996@15:02:20 STATION NUMBER: 621 CMR RESPONSIBLE OFFICIAL: ETRUSER , THREE

> REQUEST STATUS: Concurrence Completed

> STATUS DATE: MAR 14, 1996 REQUEST TYPE: ADDITIONAL

> PROJECT NUMBER: TURN-IN REQUEST:

> REQUESTOR PHONE: DATE REQUIRED BY: MAY 01, 1996

> SORT: CLASSIFICATION:

> LINE ITEM:

> LINE ITEM NUMBER: 1 DESCRIPTION:

> FAX MACHINE - VENDOR PROD BRAND

> POTENTIAL VENDOR: ETRVENDOR , ONE

> POTENTIAL VENDOR PTR: VENDOR PRODUCT \#:

> UNIT COST: 550.00 QUANTITY REQUIRED: 1

> TOTAL COST: 550.00 CONTRACT \#:

> ITEM STATUS: CSN:

> JUSTIFICATION:

> NEED A FAX MACHINE FOR IRM

> CHANGE IN PERSONNEL: NO JCAHO,CAP,SAFETY DEFICIENCY: NO CHANGE IN RECURRING COSTS: INCREASE SUFFICIENT FUNDS BUDGETED?: YES ANNUAL RECURRING SUPPLY COST: 80.00 TRAINING NEEDED?: NO

> EST. TRAINING COST: MAINT. CONTRACT RECOMMENDED: YES

> MAINT. CONTRACT COST: 100.00 SPACE AVAILABLE?: YES

> LOCATION: COMPUTER INSTALLATION NEEDED?: YES UTILITIES REQUIRED:

> Electricity\>208V Other

> OTHER UTILITIES: PHONE LINE

> SERVICE CONTACT: SERVICE CONTACT PHONE: CHANGE IN PERSONNEL EXPLAIN:

> DEFICIENCY EXPLANATION:

> CHANGE RECUR COST EXPLAIN: NEED FAX PAPER,TONER

> TRAINING EXPLANATION:

> MAINT. CONTRACT JUSTIFICATION:

> NEED TO KEEP MACHINE IN RUNNING ORDER

> CMR OFFICIAL APPROVAL: YES CMR PRIORITY: 1

> Press RETURN to continue, or '^' to exit. \<RET\>

> NX EQUIPMENT?: YES ENG. MAINTENANCE TRAINING: NO

> ENG. TRAINING TUITION: ENG. TRAINING TRAVEL COST: ENG. TRAINING VENDOR:

> ENG. TRAINING LOCATION:

> CONSTRUCTION/RENOVATION: NO PROJECT NEEDED?:

> ENG. PROJECT \#: CONSTRUCTION/RENOVATION COST: CONSTRUCTION/RENOVATION TIME: SPECIAL INSTALLATION: YES SPECIAL INSTALLATION COST: 80.00 ADDITIONAL TEST EQUIP.: NO ADDITIONAL TEST EQUIP. COST: MAINTENANCE IMPACT COST: ENGINEERING CONTACT: ETRUSER , SEVEN ENGINEERING CONTACT PHONE: TOTAL ENGINEERING EST. COST: 80 ENG. MAINTENANCE CONTRACT: YES ENG. MAINT. CONTRACT TYPE: PM ENG. MAINT. OTHER CONTRACT: SETS MAINTENANCE MANUALS: 2

> June 1996 Equipment/Turn-In Request Version 1.0 33

> User Manual

> PPM

> 34 Equipment/Turn-In Request Version 1.0 June 1996 User Manual

PPM

## Edit Equipment Request (PPM)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Personl Property Manager may select a request to edit but may not editing any Engineering data. The request must be sent back if editing is needed.

> Select Equipment Request Menu (PPM) Option: EDIT \<RET\> Equipment Requests (PPM) Select EQUIPMENT REQUEST TRANSACTION NUMBER: ?? \<RET\>

> Choose from:

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 33%" />
<col style="width: 54%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>78</p>
</blockquote></th>
<th>621-123-96-00002</th>
<th><blockquote>
<p>Pending Equipment Committee Approval</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>82</p>
</blockquote></td>
<td>621-666-96-00002</td>
<td><blockquote>
<p>Pending Equipment Committee Review/Rank</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>83</p>
</blockquote></td>
<td>621-666-96-00007</td>
<td><blockquote>
<p>Pending Equipment Committee Review/Rank</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>89</p>
</blockquote></td>
<td>621-136-96-00010</td>
<td><blockquote>
<p>Pending PPM Review</p>
</blockquote></td>
</tr>
</tbody>
</table>

> Select EQUIPMENT REQUEST TRANSACTION NUMBER:

> Review/Rank

> 621-666-96-00007 \<RET\>

> Pending Equipment Committee

> Do you want to view the information related to this request? Yes// N \<RET\> (NO) Do you want to edit this request? No// Y \<RET\> (Yes)

> DATE REQUIRED BY: MAY 1,1996// \<RET\>

> SORT: \<RET\>

> CLASSIFICATION: \<RET\>

> Select LINE ITEM NUMBER: 1// \<RET\> LINE ITEM NUMBER: 1// \<RET\> DESCRIPTION:

> 1\>FAX MACHINE - VENDOR PROD BRAND \<RET\>

> 2\> \<RET\>

> EDIT Option: \<RET\>

> POTENTIAL VENDOR: ETRVENDOR , ONE// \<RET\>

> VENDOR PRODUCT \#: \<RET\>

> UNIT COST: 550.00// \<RET\> QUANTITY REQUIRED: 1// \<RET\> CONTRACT \#: \<RET\>

> PARENT SYSTEM / COMPONENT: PARENT SYSTEM// \<RET\>

> Select LINE ITEM NUMBER: \<RET\>

> JUSTIFICATION:

> 1\>NEED A FAX MACHINE FOR IRM \<RET\>

> 2\> \<RET\>

> EDIT Option: \<RET\>

> CHANGE IN PERSONNEL: NO// \<RET\> JCAHO,CAP,SAFETY DEFICIENCY: NO// \<RET\> CHANGE IN RECURRING COSTS: INCREASE// \<RET\> SUFFICIENT FUNDS BUDGETED?: YES// \<RET\> CHANGE RECUR COST EXPLAIN:

> 1\>NEED FAX PAPER,TONER \<RET\>

> 2\> \<RET\>

> EDIT Option: \<RET\>

> ANNUAL RECURRING SUPPLY COST: 80.00// \<RET\>

> TRAINING NEEDED?: NO// \<RET\>

> MAINT. CONTRACT RECOMMENDED: YES// \<RET\>

> MAINT. CONTRACT JUSTIFICATION:

> 1\>NEED TO KEEP MACHINE IN RUNNING ORDER \<RET\>

> 2\> \<RET\>

> EDIT Option: \<RET\>

> MAINT. CONTRACT COST: 100.00// \<RET\>

> SPACE AVAILABLE?: YES// \<RET\>

> LOCATION: COMPUTER// \<RET\> 1 B ETRVENDOR , SEVEN COMPUTER ROOM INSTALLATION NEEDED?: YES// \<RET\>

> Select UTILITIES REQUIRED: \<RET\>

> UTILITIES REQUIRED: Electricity\>208V// \<RET\>

> Select UTILITIES REQUIRED: \<RET\> OTHER UTILITIES: PHONE LINE// \<RET\> SERVICE CONTACT: \<RET\>

> SERVICE CONTACT PHONE: \<RET\>

> Resend to Engineering for Editing? No// \<RET\> (No)

> June 1996 Equipment/Turn-In Request Version 1.0 35

> User Manual

> <span id="4.3_Cancel_Equipment_Request_(PPM)" class="anchor"></span>PPM

## Cancel Equipment Request (PPM)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The PPM may select to cancel a request.

## Rank Equipment Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> After reviewing requests, a priority ranking should be assigned. You may select the default rank, enter a rank not yet assigned or enter a rank already in use. If you<span id="_bookmark65" class="anchor"></span> enter a rank in use, the other transactions’ priorities will shift downward accordingly.

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 33%" />
<col style="width: 54%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>77</p>
</blockquote></th>
<th>621-123-96-00001</th>
<th>Pending Equipment Committee Review/Rank</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>82</p>
</blockquote></td>
<td>621-666-96-00002</td>
<td>Pending Equipment Committee Review/Rank</td>
</tr>
<tr class="even">
<td><blockquote>
<p>83</p>
</blockquote></td>
<td>621-666-96-00007</td>
<td>Pending Equipment Committee Review/Rank</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 35%" />
<col style="width: 53%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>2</p>
</blockquote></th>
<th>621-123-96-00002</th>
<th><blockquote>
<p>HYDRAULIC LIFT</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td>621-781-95-00002</td>
<td><blockquote>
<p>WATERHEATER, 100 CUB</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>9</p>
</blockquote></td>
<td>621-780-95-00008</td>
<td><blockquote>
<p>BATHTUB/SINK</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>12</p>
</blockquote></td>
<td>621-323-95-00001</td>
<td><blockquote>
<p>TABLE SAW</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>15</p>
</blockquote></td>
<td>621-123-96-00003</td>
<td><blockquote>
<p>ETRVENDOR , E IGHT COPY MACHINE</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>16</p>
</blockquote></td>
<td>621-123-96-00001</td>
<td><blockquote>
<p>ETRVENDOR , NINE 120 COMPUTER</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>EQUIPMENT COMMITTEE RANKING: 16// <strong>5 &lt;RET&gt;</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

## Create 2237 (PPM)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Step 1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In order to create a new 2237 from a equipment request, you must be a valid control point. Review the Control Point Official and Control Point Clerk user manuals on how to become a valid control point. As much information as possible will be moved from the equipment request into the 2237 and will appear as defaults. You can accept these defaults or change them as necessary.

> 36 Equipment/Turn-In Request Version 1.0 June 1996 User Manual

PPM

> June 1996 Equipment/Turn-In Request Version 1.0 37

> User Manual

> <span id="4.5.2_Step_2" class="anchor"></span>PPM

### Step 2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If a 2237 was not completed, the equipment request will retain the permanent transaction number and allow you to complete the 2237 process.

## Display/Print Equipment Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Use this menu option to print a request to a print or to the screen.

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 33%" />
<col style="width: 54%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>83</p>
</blockquote></th>
<th>621-666-96-00007</th>
<th><blockquote>
<p>Pending Equipment Committee Review/Rank</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>84</p>
</blockquote></td>
<td>621-420-96-00001</td>
<td><blockquote>
<p>Approved - Funded</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>89</p>
</blockquote></td>
<td>621-136-96-00010</td>
<td><blockquote>
<p>Pending PPM Review</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>92</p>
</blockquote></td>
<td>621-136-96-00011</td>
<td><blockquote>
<p>Pending Engineering Signature</p>
</blockquote></td>
</tr>
</tbody>
</table>

> 38 Equipment/Turn-In Request Version 1.0 June 1996 User Manual

PPM

> This print can be queued.

> TRANSACTION NUMBER: 621-666-96-00007 REQUESTOR:ETRUSER , FOUR

> REQUESTING SERVICE: ETRVENDOR , SEVEN

> REQUEST DATE/TIME: FEB 01, 1996@15:02:20 STATION NUMBER: 621 CMR RESPONSIBLE OFFICIAL: ETRUSER , THREE

> REQUEST STATUS: Pending Equipment Committee Review/Rank

> STATUS DATE: MAR 14, 1996 REQUEST TYPE: ADDITIONAL

> PROJECT NUMBER: TURN-IN REQUEST:

> REQUESTOR PHONE: DATE REQUIRED BY: MAY 01, 1996

> SORT: CLASSIFICATION:

> LINE ITEM:

> LINE ITEM NUMBER: 1 DESCRIPTION:

> FAX MACHINE - VENDOR PROD BRAND

> POTENTIAL VENDOR: ETRVENDOR , ONE

> POTENTIAL VENDOR PTR: VENDOR PRODUCT \#:

> UNIT COST: 550.00 QUANTITY REQUIRED: 1

> TOTAL COST: 550.00 CONTRACT \#:

> ITEM STATUS: CSN:

> JUSTIFICATION:

> NEED A FAX MACHINE FOR IRM

> CHANGE IN PERSONNEL: NO JCAHO,CAP,SAFETY DEFICIENCY: NO CHANGE IN RECURRING COSTS: INCREASE SUFFICIENT FUNDS BUDGETED?: YES ANNUAL RECURRING SUPPLY COST: 80.00 TRAINING NEEDED?: NO

> EST. TRAINING COST: MAINT. CONTRACT RECOMMENDED: YES

> MAINT. CONTRACT COST: 100.00 SPACE AVAILABLE?: YES

> LOCATION: COMPUTER INSTALLATION NEEDED?: YES UTILITIES REQUIRED:

> Electricity\>208V Other

> <span id="_bookmark68" class="anchor"></span>OTHER UTILITIES: PHONE LINE

> SERVICE CONTACT: SERVICE CONTACT PHONE: CHANGE IN PERSONNEL EXPLAIN:

> DEFICIENCY EXPLANATION:

> CHANGE RECUR COST EXPLAIN: NEED FAX PAPER,TONER

> TRAINING EXPLANATION:

> MAINT. CONTRACT JUSTIFICATION:

> NEED TO KEEP MACHINE IN RUNNING ORDER

> CMR OFFICIAL APPROVAL: YES CMR PRIORITY: 1

> NX EQUIPMENT?: YES ENG. MAINTENANCE TRAINING: NO

> ENG. TRAINING TUITION: ENG. TRAINING TRAVEL COST: ENG. TRAINING VENDOR:

> ENG. TRAINING LOCATION:

> CONSTRUCTION/RENOVATION: NO PROJECT NEEDED?:

> ENG. PROJECT \#: CONSTRUCTION/RENOVATION COST: CONSTRUCTION/RENOVATION TIME: SPECIAL INSTALLATION: YES SPECIAL INSTALLATION COST: 80.00 ADDITIONAL TEST EQUIP.: NO ADDITIONAL TEST EQUIP. COST: MAINTENANCE IMPACT COST: ENGINEERING CONTACT: ETRUSER , SEVEN ENGINEERING CONTACT PHONE: TOTAL ENGINEERING EST. COST: 80 ENG. MAINTENANCE CONTRACT: YES ENG. MAINT. CONTRACT TYPE: PM ENG. MAINT. OTHER CONTRACT: SETS MAINTENANCE MANUALS: 2

> CONSTRUCT/RENOV DESCRIPTION:

> SPECIAL INSTALL DESCRIPTION:

> CALL PHONE COMPANY TO COME AND INSTALL NEW PHONE LINE ADDITIONAL TEST EQUIP EXPLAIN:

> ENG. REMARKS:

> CONCURRENCE NEEDED?: NO

> EQUIPMENT COMMITTEE RANKING: CONTROLLED ITEM?: NO SHORT DESCRIPTION:

## Equipment Request Reports Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This menu option allows for PPM to print certain specialized reports.

### Controlled Equipment Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> June 1996

> Equipment/Turn-In Request Version 1.0 39

> User Manual

> <span id="4.7.2_Request_Status_Report" class="anchor"></span>PPM

> The Controlled Equipment Report prints transactions that have controlled items.

### Request Status Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Request Status Report prints the status of all transactions for the PPM.

### Turn-In Status by CMR

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This report prints in CMR order.

> 40 Equipment/Turn-In Request Version 1.0 June 1996 User Manual

<table>
<colgroup>
<col style="width: 46%" />
<col style="width: 21%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"></th>
<th><blockquote>
<p><span id="4.7.4_Turn-In_Status_by_Service" class="anchor"></span>PPM</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>4.7.4 Turn-In Status by Service</strong></p>
<p>This report prints in Service order.</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p>START WITH REQUESTING SERVICE: FIRST// <strong>&lt;RET&gt;</strong></p>
<p>DEVICE: <strong>&lt;RET&gt;</strong></p>
<p>TURN-IN REPORT BY SERVICE</p>
</blockquote></td>
<td><blockquote>
<p>MAR 19,1996 14:13</p>
</blockquote></td>
<td><blockquote>
<p>PAGE 1</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>TRANSACTION # SERVICE CMR OFFICIAL EE # EQUIPMENT NAME</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="3"><blockquote>
<p>REQUESTING SERVICE: ENGINEERING 621-136-96-00002 ENG ETRUSER , THREE</p>
<p>51 HYDRAULIC LIFT BED REQUESTING SERVICE: ETRVENDOR , SEVEN</p>
<p>621-666-94-00013 IRM ETRUSER , THREE</p>
<p>37 ETRVENDOR1 , ONE</p>
<p>REQUESTING SERVICE: PATIENT CARE 621-780-94-00012 PTC ETRUSER , ONE</p>
<p>3 BLOOD CHEMICAL ANALYZER 621-780-95-00003 PTC ETRUSER , ONE</p>
<p>30 ETRVENDOR , S IX CONTROL MONITOR 621-780-95-00007 PTC ETRUSER , ONE</p>
<p>9 BATHTUB ETRVENDOR , F IVE UNIT</p>
<p>62 REFRIGERATOR,FOOD (23 cubft)</p>
</blockquote></td>
</tr>
</tbody>
</table>

### Turn-In Status by Transaction Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This report prints in turn-in transaction number order in the same format as 4.7.3 and 4.7.4.

### Turn-In Status Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This report prints turn-ins by their current status.

> June 1996 Equipment/Turn-In Request Version 1.0 41

> User Manual

> <span id="4.8_Process_Turn-Ins_Menu" class="anchor"></span>PPM

## Process Turn-Ins Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> PPM must review any turn-in requests to determine if a work order must be created in order for the equipment to be picked-up by the warehouse.

### Process Turn-In Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Disposition of a Turn-In Document

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> After Engineering has processed the work order (if one was needed), and the Warehouse has picked up the equipment, the turn-in is sent to the PPM for final disposition and processing of the item(s).

> 42 Equipment/Turn-In Request Version 1.0 June 1996 User Manual

# CHAPTER 5 ENGINEERING

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If you have been designated the Engineering contact person to process equipment requests, you may have, as a secondary menu, the option to Approve Equipment Requests. Select this option to process requests that have been forwarded to you from the Personal Property Manager. See Chapter 4.

### Step 1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Your main menu may look like the following:

### Step 2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Select the request you wish to review. The Engineering Department when reviewing an equipment request, must fill out information that may have an impact on them.

> June 1996 Equipment/Turn-In Request Version 1.0 43

> User Manual

> Engineering

### Step 3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Some fields that the requestor entered may be reviewed and changed by the Engineering department if needed.

### Step 4

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Another impact to the Engineering Department is whether anyone in there may need special training in order to maintain the requested equipment if it is acquired. If additional training is needed, other questions will need to be answered concerning tuition and travel costs associated with that training as well as the potential training vendor. When entering the training vendor, the Vendor file will be checked, or it will accept a free text vendor.

> 44 Equipment/Turn-In Request Version 1.0 June 1996 User Manual

Engineering

### Step 5

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The next question is whether any special construction/renovation is needed to accommodate the new equipment, if acquired. If you answer 'Yes', the next question will be whether a project had been submitted and approved in order to accomplish the necessary construction/renovation. The next inquiry will be for the project number. If a project has not yet been developed, this inquiry should be left blank. A description of the nature and location of the construction/renovation will be required in the next field. Enter the estimated construction/renovation cost and number of calendar days that would be required for completion of any special construction/renovation.

> June 1996 Equipment/Turn-In Request Version 1.0 45

> User Manual

> Engineering

### Step 6

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Special installation questions should only be answered if anything other than normal utility connections are needed in order for the equipment to be installed and made operational. For example, a room may be large enough to contain a large piece of equipment, but the door may have to be removed in order to move the equipment into the room, or plumbing might be required. This information will be entered in the special installation requirement word-processing field.

### Step 7

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If additional test equipment is needed to maintain the requested equipment in operational order, then the additional test equipment field must be answered 'Yes'.

> 46 Equipment/Turn-In Request Version 1.0 June 1996 User Manual

Engineering

### Step 8

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If there is another person who should be the Engineering contact for this request, enter it at this point.

### Step 9

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Whether Engineering desires a maintenance contract will be the next question that must be answered. Engineering desires to have at least a minimum of two sets of maintenance manuals on hand. Be sure to enter any estimated impact cost on the maintenance of the items in the request. This will be especially important to the Equipment Committee in their consideration of the request.

> June 1996 Equipment/Turn-In Request Version 1.0 47

> User Manual

> <span id="5.10_Step_10" class="anchor"></span>Engineering

### Step 10

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A general remarks field has been added for Engineering to make any comments not otherwise covered.

> 48 Equipment/Turn-In Request Version 1.0 June 1996 User Manual

Engineering

### Step 11

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Displaying a request for the Engineering user.

> Do you want to view the information related to this request? Yes// \<RET\> (Yes) DEVICE: HOME// \<RET\>

> TRANSACTION NUMBER: 621-666-96-00007 REQUESTOR: ETRUSER , FOUR

> REQUESTING SERVICE: ETRVENDOR , SEVEN

> REQUEST DATE/TIME: FEB 01, 1996@15:02:20 STATION NUMBER: 621 CMR RESPONSIBLE OFFICIAL: ETRUSER , THREE

> REQUEST STATUS: Pending Engineering Review

> STATUS DATE: MAR 13, 1996 REQUEST TYPE: ADDITIONAL

> PROJECT NUMBER: TURN-IN REQUEST:

> REQUESTOR PHONE: DATE REQUIRED BY: MAY 01, 1996

> SORT: CLASSIFICATION:

> LINE ITEM:

> LINE ITEM NUMBER: 1 DESCRIPTION:

> FAX MACHINE - VENDOR PROD BRAND

> POTENTIAL VENDOR: ETRVENDOR , ONE

> POTENTIAL VENDOR PTR: VENDOR PRODUCT \#:

> UNIT COST: 550.00 QUANTITY REQUIRED: 1

> TOTAL COST: 550.00 CONTRACT \#:

> ITEM STATUS: CSN:

> JUSTIFICATION:

> Press RETURN to continue, or '^' to exit. \<RET\>

> NEED A FAX MACHINE FOR IRM

> CHANGE IN PERSONNEL: NO JCAHO,CAP,SAFETY DEFICIENCY: NO CHANGE IN RECURRING COSTS: INCREASE SUFFICIENT FUNDS BUDGETED?: YES ANNUAL RECURRING SUPPLY COST: 80.00 TRAINING NEEDED?: NO

> EST. TRAINING COST: MAINT. CONTRACT RECOMMENDED: YES

> MAINT. CONTRACT COST: 100.00 SPACE AVAILABLE?: YES

> LOCATION: COMPUTER INSTALLATION NEEDED?: YES UTILITIES REQUIRED:

> Electricity\>208V Other

> OTHER UTILITIES: PHONE LINE

> SERVICE CONTACT: SERVICE CONTACT PHONE: CHANGE IN PERSONNEL EXPLAIN:

> DEFICIENCY EXPLANATION:

> CHANGE RECUR COST EXPLAIN: NEED FAX PAPER,TONER

> TRAINING EXPLANATION:

> MAINT. CONTRACT JUSTIFICATION:

> NEED TO KEEP MACHINE IN RUNNING ORDER

> CMR OFFICIAL APPROVAL: YES CMR PRIORITY: 1

> Press RETURN to continue, or '^' to exit. \<RET\>

> NX EQUIPMENT?: YES

> June 1996 Equipment/Turn-In Request Version 1.0 49

> User Manual

> Engineering

> 50 Equipment/Turn-In Request Version 1.0 June 1996 User Manual

# CHAPTER 6 OTHER CONCURRING OFFICIALS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Step 1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If you are assigned to be a Concurring Official, you will receive the following mail message from the Personal Property Manager.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 42%" />
<col style="width: 23%" />
<col style="width: 15%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Subj: From:</p>
</blockquote></th>
<th><blockquote>
<p>CONCURRENCE NEEDED [#32234]</p>
<p>ETRUSER , F IVE in ‘IN’ basket.</p>
</blockquote></th>
<th><blockquote>
<p>04 AUG 96 17:25</p>
</blockquote></th>
<th><blockquote>
<p>3 Lines Page 1</p>
</blockquote></th>
<th><blockquote>
<p>NEW</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="5"><blockquote>
<p>You were selected to review NX Equipment Request,<span id="_bookmark85" class="anchor"></span> Transaction #: 621-666-96-00007 for your concurring opinion. Please review and indicate your approval or not by AUG 16, 1996.</p>
</blockquote></td>
</tr>
</tbody>
</table>

### Step 2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> All designated concurring officials should be assigned the appropriate menu option in order to process requests sent to them.

### Step 3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> They may review the request prior to indicating their decision either to the screen or printer.

> June 1996 Equipment/Turn-In Request Version 1.0 51

> User Manual

> Other Concurring Officials

> TRANSACTION NUMBER: 621-666-96-00007 REQUESTOR: ETRUSER , FOUR

> REQUESTING SERVICE: ETRVENDOR , SEVEN

> REQUEST DATE/TIME: FEB 01, 1996@15:02:20 STATION NUMBER: 621 CMR RESPONSIBLE OFFICIAL: ETRUSER , THREE

> REQUEST STATUS: Pending Concurrence

> STATUS DATE: MAR 13, 1996 REQUEST TYPE: ADDITIONAL

> PROJECT NUMBER: TURN-IN REQUEST:

> REQUESTOR PHONE: DATE REQUIRED BY: MAY 01, 1996

> SORT: CLASSIFICATION:

> LINE ITEM:

> LINE ITEM NUMBER: 1 DESCRIPTION:

> FAX MACHINE - VENDOR PROD BRAND

> POTENTIAL VENDOR: ETRVENDOR , ONE

> POTENTIAL VENDOR PTR: VENDOR PRODUCT \#:

> UNIT COST: 550.00 QUANTITY REQUIRED: 1

> TOTAL COST: 550.00 CONTRACT \#:

> ITEM STATUS: CSN:

> JUSTIFICATION:

> Press RETURN to continue, or '^' to exit. \<RET\>

> NEED A FAX MACHINE FOR IRM

> CHANGE IN PERSONNEL: NO JCAHO,CAP,SAFETY DEFICIENCY: NO CHANGE IN RECURRING COSTS: INCREASE SUFFICIENT FUNDS BUDGETED?: YES ANNUAL RECURRING SUPPLY COST: 80.00 TRAINING NEEDED?: NO

> EST. TRAINING COST: MAINT. CONTRACT RECOMMENDED: YES

> MAINT. CONTRACT COST: 100.00 SPACE AVAILABLE?: YES

> LOCATION: COMPUTER INSTALLATION NEEDED?: YES UTILITIES REQUIRED:

> Electricity\>208V Other

> OTHER UTILITIES: PHONE LINE

> SERVICE CONTACT: SERVICE CONTACT PHONE: CHANGE IN PERSONNEL EXPLAIN:

> DEFICIENCY EXPLANATION:

> CHANGE RECUR COST EXPLAIN: NEED FAX PAPER,TONER

> TRAINING EXPLANATION:

> MAINT. CONTRACT JUSTIFICATION:

> NEED TO KEEP MACHINE IN RUNNING ORDER

> CMR OFFICIAL APPROVAL: YES CMR PRIORITY: 1

> Press RETURN to continue, or '^' to exit. \<RET\>

> NX EQUIPMENT?: YES ENG. MAINTENANCE TRAINING: NO

> ENG. TRAINING TUITION: ENG. TRAINING TRAVEL COST: ENG. TRAINING VENDOR:

> ENG. TRAINING LOCATION:

> CONSTRUCTION/RENOVATION: NO PROJECT NEEDED?:

> ENG. PROJECT \#: CONSTRUCTION/RENOVATION COST: CONSTRUCTION/RENOVATION TIME: SPECIAL INSTALLATION: YES SPECIAL INSTALLATION COST: 80.00 ADDITIONAL TEST EQUIP.: NO ADDITIONAL TEST EQUIP. COST: MAINTENANCE IMPACT COST: ENGINEERING CONTACT: ETRUSER , SEVEN ENGINEERING CONTACT PHONE: TOTAL ENGINEERING EST. COST: 80 ENG. MAINTENANCE CONTRACT: YES ENG. MAINT. CONTRACT TYPE: PM ENG. MAINT. OTHER CONTRACT: SETS MAINTENANCE MANUALS: 2

> CONSTRUCT/RENOV DESCRIPTION:

> SPECIAL INSTALL DESCRIPTION:

> CALL PHONE COMPANY TO COME AND INSTALL NEW PHONE LINE ADDITIONAL TEST EQUIP EXPLAIN:

> ENG. REMARKS:

> 52 Equipment/Turn-In Request Version 1.0 June 1996 User Manual

> Other Concurring Officials

### Step 3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Approving the request.

> June 1996 Equipment/Turn-In Request Version 1.0 53

> User Manual

> Other Concurring Officials

> 54 Equipment/Turn-In Request Version 1.0 June 1996 User Manual

# CHAPTER 7 EQUIPMENT COMMITTEE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If you are responsible for processing the Equipment Committee’s decisions, you may have the Equipment Committee menu assigned.

## Rank Equipment Requests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This option may be assigned to the Personal Property Manager (PPM) or be done at the Equipment Committee Level. Please review section 4.4 for information on how<span id="_bookmark87" class="anchor"></span> to do this option.

## Equipment Request Cost Summary Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This report (which must be run as a 132 Column report) will help the Equipment Committee in reviewing and approving requests. It provides a summary of all costs entered during the equipment request process.

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 9%" />
<col style="width: 6%" />
<col style="width: 5%" />
<col style="width: 8%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 6%" />
<col style="width: 7%" />
<col style="width: 9%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="12"><blockquote>
<p>EQUIPMENT REQUEST COST SUMMARY REPORT Mar 14, 1996 7:47 pm PAGE: 1</p>
<p>Annual Training Training Constr. Special Maint.</p>
<p>Line Item Recurring Training Contract Tuition Travel Renov. Install Equip Impact Total Transaction # Cost Cost Cost Cost Cost Cost Cost Cost Cost Cost</p>
<p>Service: ETRVENDOR1,TWO</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>621-123-96-00003</p>
</blockquote></td>
<td><blockquote>
<p>100.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td>0.00</td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td>100.00</td>
</tr>
<tr class="even">
<td colspan="12"><blockquote>
<p>Subtotal for ETRVENDOR1,TWO:</p>
<p>Service: ETRVENDOR,SEVEN</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>621-782-95-00003B</p>
</blockquote></td>
<td><blockquote>
<p>125.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td>0.00</td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td>125.00</td>
</tr>
<tr class="even">
<td><blockquote>
<p>621-782-95-00003D</p>
</blockquote></td>
<td><blockquote>
<p>215.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td>0.00</td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td>215.00</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>621-781-95-00001B</p>
</blockquote></td>
<td><blockquote>
<p>1000.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td>0.00</td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td>1000.00</td>
</tr>
<tr class="even">
<td><blockquote>
<p>621-780-95-00008</p>
</blockquote></td>
<td><blockquote>
<p>2250.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td>0.00</td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td>2250.00</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>621-323-95-00001</p>
</blockquote></td>
<td><blockquote>
<p>6000.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td><blockquote>
<p>200.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td>0.00</td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td>6200.00</td>
</tr>
<tr class="even">
<td><blockquote>
<p>621-123-96-00001</p>
</blockquote></td>
<td><blockquote>
<p>200.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td>0.00</td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td>200.00</td>
</tr>
<tr class="odd">
<td><blockquote>
<p>621-666-96-00002</p>
</blockquote></td>
<td><blockquote>
<p>1000.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td><blockquote>
<p>300.00</p>
</blockquote></td>
<td>0.00</td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td>1300.00</td>
</tr>
<tr class="even">
<td><blockquote>
<p>621-666-96-00007</p>
</blockquote></td>
<td><blockquote>
<p>550.00</p>
</blockquote></td>
<td><blockquote>
<p>80.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td><blockquote>
<p>100.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td><blockquote>
<p>80.00</p>
</blockquote></td>
<td>0.00</td>
<td><blockquote>
<p>0.00</p>
</blockquote></td>
<td>810.00</td>
</tr>
<tr class="odd">
<td colspan="12"><blockquote>
<p>Subtotal for ETRVENDOR,SEVEN: 12100.00</p>
</blockquote></td>
</tr>
</tbody>
</table>

> June 1996 Equipment/Turn-In Request Version 1.0 55

> User Manual

> <span id="7.3_Outstanding_Equip_Req_Rept" class="anchor"></span>Equipment Committee

## Outstanding Equipment Requests Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This report is an informational report for the Equipment Committee. It prints requests that are currently in the Equipment Committee’s review process. It will display the Parent System line items and other general information about the request.

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 17%" />
<col style="width: 14%" />
<col style="width: 14%" />
<col style="width: 12%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p>Requests by Service Priority</p>
</blockquote></th>
<th colspan="3"><blockquote>
<p>MAR 14,1996 19:47</p>
</blockquote></th>
<th><blockquote>
<p>PAGE 1</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="2"><blockquote>
<p>TRANSACTION # PRIORITY ITEM DESCRIPTION</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>TYPE COST QUANTITY PARENT SYSTEM</p>
<p>/ COMPONENT JUSTIFICATION</p>
</blockquote></td>
<td><blockquote>
<p>TOTAL</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>ETRVENDOR1 , TWO</p>
</blockquote></td>
<td colspan="3"></td>
<td></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>621-323-95-00001 1</p>
<p>REFRIGERATOR</p>
</blockquote></td>
<td colspan="3"><blockquote>
<p>REPL 3000.00 2</p>
<p>PARENT SYSTEM NEED NEW ONE</p>
</blockquote></td>
<td><blockquote>
<p>6000.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p><span id="_bookmark89" class="anchor"></span>ETRVENDOR , SEVEN</p>
</blockquote></td>
<td colspan="3"></td>
<td></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>621-666-96-00007</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>ADDI</p>
</blockquote></td>
<td><blockquote>
<p>550.00</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>550.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="6"><blockquote>
<p>FAX MACHINE - ETRVENDOR , ONE PARENT SYSTEM</p>
<p>NEED A FAX MACHINE FOR IRM</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Process Equip Committee Decisions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This menu should be used after priority ranking has been applied to requests and is used to assign a final decision on equipment requests. Select the methodology for processing requests. Five different methods have been created to provide quick and easy processing of requests.

> 56 Equipment/Turn-In Request Version 1.0 June 1996 User Manual

> <span id="7.4.1_Step_1" class="anchor"></span>Equipment Committee

### Step 1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> After selecting the method of approving/disapproving requests, a list of requests will display from which you can select the requests which will be processed accordingly. The following display shows the process for ‘Approve/Pending All Line Items’ which will change the status for all selected items to be ‘Approved-Pending Funding’. This status allows for the creation of a 2237 when appropriate funding is available.

<table>
<colgroup>
<col style="width: 6%" />
<col style="width: 8%" />
<col style="width: 24%" />
<col style="width: 28%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr class="header">
<th>Num#</th>
<th><blockquote>
<p>Rank</p>
</blockquote></th>
<th><blockquote>
<p>Request #</p>
</blockquote></th>
<th><blockquote>
<p>Service</p>
</blockquote></th>
<th>#</th>
<th><blockquote>
<p>Items</p>
</blockquote></th>
<th><blockquote>
<p>Amount</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>1</td>
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>621-782-95-00003D</p>
</blockquote></td>
<td><blockquote>
<p>ETRVENDOR , SEVEN</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>$ 215.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td>2</td>
<td><blockquote>
<p>14</p>
</blockquote></td>
<td><blockquote>
<p>621-781-95-00001B</p>
</blockquote></td>
<td><blockquote>
<p>ETRVENDOR , SEVEN</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>$ 1000.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>3</td>
<td><blockquote>
<p>9</p>
</blockquote></td>
<td><blockquote>
<p>621-780-95-00008</p>
</blockquote></td>
<td><blockquote>
<p>ETRVENDOR , SEVEN</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>$ 2250.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td>4</td>
<td><blockquote>
<p>12</p>
</blockquote></td>
<td><blockquote>
<p>621-323-95-00001</p>
</blockquote></td>
<td><blockquote>
<p>ETRVENDOR , SEVEN</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>$ 6200.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>5</td>
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>621-780-95-00013B</p>
</blockquote></td>
<td><blockquote>
<p>ETRVENDOR , SEVEN</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>$ 1499.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td>6</td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>621-780-95-00001</p>
</blockquote></td>
<td><blockquote>
<p>ETRVENDOR , SEVEN</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td><blockquote>
<p>$ 0.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>7</td>
<td><blockquote>
<p>9</p>
</blockquote></td>
<td><blockquote>
<p>621-323-95-00001A</p>
</blockquote></td>
<td><blockquote>
<p>ETRVENDOR , SEVEN</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>$ 6200.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td>8</td>
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>621-123-96-00001</p>
</blockquote></td>
<td><blockquote>
<p>ETRVENDOR , SEVEN</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>$ 200.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>9</td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>621-123-96-00003</p>
</blockquote></td>
<td><blockquote>
<p>ETRVENDOR1 , TWO</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>$ 100.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td>10</td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>621-666-96-00002</p>
</blockquote></td>
<td><blockquote>
<p>ETRVENDOR , SEVEN</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>$ 1300.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>11</td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>621-666-96-00007</p>
</blockquote></td>
<td><blockquote>
<p>ETRVENDOR , SEVEN</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>$ 810.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="7"><p>Select numbers to process: (1-11): <strong>1 &lt;RET&gt;</strong></p>
<p><span id="_bookmark91" class="anchor"></span>Qty: 5 Price: 25 Total: 125 Description:</p>
<blockquote>
<p>TEST ITEM 1</p>
</blockquote>
<p>Qty: 3 Price: 30 Total: 90 Description:</p>
<blockquote>
<p>TEST ITEM 2</p>
</blockquote>
<p>Does this request need a final confirmation from the responsible CMR Official?</p></td>
</tr>
</tbody>
</table>

### Step 2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Selecting ‘Disaprove All Line Items” means that all chosen requests will be returned to the requestor and CMR Official with the status of ‘Disapproved-Do No Resubmit’.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 24%" />
<col style="width: 28%" />
<col style="width: 9%" />
<col style="width: 8%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="7"><blockquote>
<p>DISAPPROVE ALL LINE ITEMS in the following Equipment Requests</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Num#</p>
</blockquote></td>
<td><blockquote>
<p>Rank</p>
</blockquote></td>
<td><blockquote>
<p>Request #</p>
</blockquote></td>
<td><blockquote>
<p>Service</p>
</blockquote></td>
<td>#</td>
<td><blockquote>
<p>Items</p>
</blockquote></td>
<td><blockquote>
<p>Amount</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>14</p>
</blockquote></td>
<td><blockquote>
<p>621-781-95-00001B</p>
</blockquote></td>
<td><blockquote>
<p>ETRVENDOR , SEVEN</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>$ 1000.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>9</p>
</blockquote></td>
<td><blockquote>
<p>621-780-95-00008</p>
</blockquote></td>
<td><blockquote>
<p>ETRVENDOR , SEVEN</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>$ 2250.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>12</p>
</blockquote></td>
<td><blockquote>
<p>621-323-95-00001</p>
</blockquote></td>
<td><blockquote>
<p>ETRVENDOR , SEVEN</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>$ 6200.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>621-780-95-00013B</p>
</blockquote></td>
<td><blockquote>
<p>ETRVENDOR , SEVEN</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>$ 1499.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>621-780-95-00001</p>
</blockquote></td>
<td><blockquote>
<p>ETRVENDOR , SEVEN</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>0</p>
</blockquote></td>
<td><blockquote>
<p>$ 0.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>6</p>
</blockquote></td>
<td><blockquote>
<p>9</p>
</blockquote></td>
<td><blockquote>
<p>621-323-95-00001A</p>
</blockquote></td>
<td><blockquote>
<p>ETRVENDOR , SEVEN</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>$ 6200.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>621-123-96-00001</p>
</blockquote></td>
<td><blockquote>
<p>ETRVENDOR , SEVEN</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>$ 200.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>8</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>621-123-96-00003</p>
</blockquote></td>
<td><blockquote>
<p>ETRVENDOR1 , TWO</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>$ 100.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>9</p>
</blockquote></td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>621-666-96-00002</p>
</blockquote></td>
<td><blockquote>
<p>ETRVENDOR , SEVEN</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>$ 1300.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>10</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>621-666-96-00007</p>
</blockquote></td>
<td><blockquote>
<p>ETRVENDOR , SEVEN</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>$ 810.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="7"><blockquote>
<p>Select numbers to process: (1-10): <strong>5 &lt;RET&gt;</strong></p>
</blockquote></td>
</tr>
</tbody>
</table>

> June 1996 Equipment/Turn-In Request Version 1.0 57

> User Manual

> Equipment Committee

### Step 3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Selecting ‘Defer All Line Items’ means that the requestor or CMR Official may resubmit the request at another time.

<table>
<colgroup>
<col style="width: 7%" />
<col style="width: 8%" />
<col style="width: 24%" />
<col style="width: 29%" />
<col style="width: 8%" />
<col style="width: 8%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="7"><blockquote>
<p>DEFER ALL LINE ITEMS in the following Equipment Requests</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Num#</p>
</blockquote></td>
<td><blockquote>
<p>Rank</p>
</blockquote></td>
<td><blockquote>
<p>Request #</p>
</blockquote></td>
<td><blockquote>
<p>Service</p>
</blockquote></td>
<td>#</td>
<td><blockquote>
<p>Items</p>
</blockquote></td>
<td><blockquote>
<p>Amount</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>14</p>
</blockquote></td>
<td><blockquote>
<p>621-781-95-00001B</p>
</blockquote></td>
<td>ETRVENDOR , SEVEN</td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>$ 1000.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>9</p>
</blockquote></td>
<td><blockquote>
<p>621-780-95-00008</p>
</blockquote></td>
<td>ETRVENDOR , SEVEN</td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>$ 2250.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><span id="_bookmark93" class="anchor"></span>3</p>
</blockquote></td>
<td><blockquote>
<p>12</p>
</blockquote></td>
<td><blockquote>
<p>621-323-95-00001</p>
</blockquote></td>
<td>ETRVENDOR , SEVEN</td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>$ 6200.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>4</p>
</blockquote></td>
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>621-780-95-00013B</p>
</blockquote></td>
<td>ETRVENDOR , SEVEN</td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>$ 1499.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>9</p>
</blockquote></td>
<td><blockquote>
<p>621-323-95-00001A</p>
</blockquote></td>
<td>ETRVENDOR , SEVEN</td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>$ 6200.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>6</p>
</blockquote></td>
<td><blockquote>
<p>5</p>
</blockquote></td>
<td><blockquote>
<p>621-123-96-00001</p>
</blockquote></td>
<td>ETRVENDOR , SEVEN</td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>$ 200.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>7</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>621-123-96-00003</p>
</blockquote></td>
<td><blockquote>
<p>ETRVENDOR1 , TWO</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>$ 100.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>8</p>
</blockquote></td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>621-666-96-00002</p>
</blockquote></td>
<td>ETRVENDOR , SEVEN</td>
<td></td>
<td><blockquote>
<p>3</p>
</blockquote></td>
<td><blockquote>
<p>$ 1300.00</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>9</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>621-666-96-00007</p>
</blockquote></td>
<td>ETRVENDOR , SEVEN</td>
<td></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>$ 810.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="7"><blockquote>
<p>Select numbers to process: (1-9): <strong>5 &lt;RET&gt;</strong></p>
<p>Qty: 2 Price: 3000 Total: 6000 Description:</p>
<p>REFRIGERATOR</p>
</blockquote></td>
</tr>
</tbody>
</table>

### Step 4

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Processing individual line items gives you the capability to partially approve or disapprove a request. You may either approve/disapprove multiple line items or even separate by the quantity requested. If the requestor asked for a quantity of two expensive items, and the budget could approve one, the item can be split.

> Requests will be split according to final status and quantity approved. The transaction number will remain the same but appended with A, B, C, etc. to show that it is split off the original request.

> 58 Equipment/Turn-In Request Version 1.0 June 1996 User Manual

> Equipment Committee

> PROCESS INDIVIDUAL LINE ITEMS in the following Equipment Requests Num# Rank Request \# Service \# Items Amount

> June 1996 Equipment/Turn-In Request Version 1.0 59

> User Manual

> Equipment Committee

### Step 5

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Mail messages will be sent to the requestor and CMR Official based upon the final decision of the Equipment Committee.

> 60 Equipment/Turn-In Request Version 1.0 June 1996 User Manual

> <span id="7.5_Service_Priority_Report" class="anchor"></span>Equipment Committee

## Service Priority Report

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Prints requests in service priority. User has a choice of printing for all services or selecting a particular service.

### All Services

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Each service starts a new page.

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 9%" />
<col style="width: 12%" />
<col style="width: 20%" />
<col style="width: 13%" />
<col style="width: 7%" />
<col style="width: 13%" />
</colgroup>
<thead>
<tr class="header">
<th></th>
<th></th>
<th colspan="5"></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td colspan="7"><blockquote>
<p>SERVICE: ETRVENDOR , SEVEN</p>
<p>621-666-96-00007 2 ADDITION</p>
</blockquote></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>FAX MACHINE - VENDOR</p>
</blockquote></td>
<td><blockquote>
<p>PRODUCT</p>
</blockquote></td>
<td><blockquote>
<p>PARENT SYSTE</p>
</blockquote></td>
<td><blockquote>
<p>550.00</p>
</blockquote></td>
<td><blockquote>
<p>1</p>
</blockquote></td>
<td><blockquote>
<p>550.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="2"><blockquote>
<p>621-323-95-00001 4</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>REPLACEM</p>
</blockquote></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td colspan="2"><blockquote>
<p>REFRIGERATOR</p>
</blockquote></td>
<td></td>
<td><blockquote>
<p>PARENT SYSTE</p>
</blockquote></td>
<td><blockquote>
<p>3000.00</p>
</blockquote></td>
<td><blockquote>
<p>2</p>
</blockquote></td>
<td><blockquote>
<p>6000.00</p>
</blockquote></td>
</tr>
<tr class="odd">
<td colspan="7"><blockquote>
<p>Press RETURN to continue or '^' to quit. <strong>&lt;RET&gt;</strong></p>
<p>REQUESTS BY SERVICE PRIORITY May 14, 1996 10:53 am PAGE: 4 TRANSACTION # PRIORITY TYPE COST QUANTITY TOTAL</p>
<p>PARENT SYSTEM</p>
<p>ITEM DESCRIPTION / COMPONENT JUSTIFICATION</p>
<p>SERVICE: ETRVENDOR1 , TWO</p>
<p>621-123-96-00005 3 ADDITION</p>
<p>ANOTHER ITEM FOR THE PARENT SYSTE 250.00 1 250.00</p>
<p>KITCHEN</p>
<p>Press RETURN to continue or '^' to quit. <strong>&lt;RET&gt;</strong></p>
<p>REQUESTS BY SERVICE PRIORITY May 14, 1996 10:53 am PAGE: 5 TRANSACTION # PRIORITY TYPE COST QUANTITY TOTAL</p>
<p>PARENT SYSTEM</p>
<p>ITEM DESCRIPTION / COMPONENT JUSTIFICATION</p>
<p>SERVICE: ENGINEERING</p>
<p>621-136-96-00010 1 ADDITION</p>
<p>IBM PENTIUM 120 W/16 MB PARENT SYSTE 300.00 2 600.00</p>
<p>MEMORY, ISA CARD</p>
<p>CONNER TAPE DRIVE PARENT SYSTE 450.00 2 900.00</p>
<p>-------­ 8300.00</p>
</blockquote></td>
</tr>
</tbody>
</table>

> June 1996 Equipment/Turn-In Request Version 1.0 61

> User Manual

> <span id="7.5.2_One_Service" class="anchor"></span>Equipment Committee

### One Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Selecting one service.

> 62 Equipment/Turn-In Request Version 1.0 June 1996 User Manual

# CHAPTER 8 WAREHOUSE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The warehouse menu allows the person who as been assigned the security key, PRCNWHSE, to assign someone to pick up equipment that is being turned in. The person assigned to pick up the item(s) must check in the turned-in item, and sign that it has been turned in before the Personal Property Manager can complete the final disposition of the item being turned in.

### Step 1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Assigning Someone to Pick-Up Turn-in Equipment

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 40%" />
<col style="width: 46%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>47</p>
</blockquote></th>
<th>621-132-96-00006</th>
<th>Pending Warehouse Pickup</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>49</p>
</blockquote></td>
<td>621-420-96-00028</td>
<td>Pending Warehouse Pickup</td>
</tr>
</tbody>
</table>

### Step 2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When the person assigned to pick up the item(s) has done so, the assigned Warehouse Official must sign onto the menu option and answer that it has been picked up. He/she is also given the chance to modify the DISPOSAL CONDITION CODE if it is other than what the PPM thought it would be.

> June 1996 Equipment/Turn-In Request Version 1.0 63

> User Manual

> Warehouse

> Select Option: PROC\<RET\>ess Equipment Turn-In Request (Warehouse) Select TURN-IN REQUEST TRANSCTION CODE: ? \<RET\>

> ANSWER WITH TURN-IN REQUEST NUMBER, OR TRANSACTIO N CODE CHOOSE FROM:

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 40%" />
<col style="width: 46%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>47</p>
</blockquote></th>
<th>621-132-96-00006</th>
<th>Pending Warehouse Pickup</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>49</p>
</blockquote></td>
<td>621-420-96-00028</td>
<td>Pending Warehouse Pickup</td>
</tr>
</tbody>
</table>

> Select TURN-IN REQUEST TRANSACTION CODE: 49 \<RET\> 621-420-96-00028 Pending Warehouse Pickup MFGR. EQUIPMENT NAME: BINDING SYSTEM

> MANUFACTURER: ETRVENDOR , FOUR

> MODEL: 750

> NXRN \#: 18329

> TOTAL ASSET VALUE: 3296.00

> SERIAL \#: 76096

> CATEGORY STOCK NUMBER: 3610-438983 ACQUISITION DATE: MAR 09,1992

> CMR: 420 SUPPLY (OFFICE) REPLACEMENT DATE: MAR 09, 2007 LOCATION:

> WAREHOUSE OFFICIAL: ETRUSER , ONE

> Is this the correct item turned in?: Y \<RET\>

> DISPOSAL CONDITION CODE: Used-Fair// ? \<RET\>

> Choose from:

1.  Unused-Good
2.  <span id="_bookmark99" class="anchor"></span>Unused-Fair
3.  Unused-Poor
4.  Used-Good
5.  Used-Fair
6.  Used-Poor
7.  Repairs Required-15% of a/c or less
8.  Repairs Required-16%-40% of a/c
9.  Repairs Required-41%-65% of a/c X Salvage

> S Scrap

> DISPOSAL CONDITION CODE: Used-Fair// X \<RET\> Salvage Hit RETURN to continue. \<RET\>

> ENTER YOUR ELECTRONIC SIGNATURE CODE: CODE \<RET\> Thank you.

### Step 3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> At this stage of the turn-in process, capitalized items will be handled differently from non-capitalized items. Capitalized items have sent an FA Code Sheet to FMS (Financial Management System) and must have an FD Code Sheet also sent to disposition the record in FMS. Turn-in of capitalized items also includes the updating of the general ledger in the Fixed Asset portion of FMS and the CMR must also be updated. Non-capitalized items will return to the PPM and allow the PPM to process the turn-in through the Final Disposition option. Capitalized items must wait until a FD Code Sheet is generated and a new FA Code Sheet has also been generated.

> 64 Equipment/Turn-In Request Version 1.0 June 1996 User Manual

# CHAPTER 9 TURN-INS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Requestor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If you wish to turn-in equipment without ordering replacement equipment, select the Process Equipment Turn-Ins menu option so that the request may go through the proper channels.

### Enter Excess Equipment Turn-In Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Step 1

> Select the Enter Excess Equipment Turn-In Request option from the Process Turn- Ins menu. The first two entries you make establish the temporary request number for this turn-in document. If your site parameters are set up for a multi-divisional site, you will be asked to identify the Station Number, otherwise it will automatically default to your station number.

### Step 2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Select the CMR Responsible Official responsible for the equipment being turned in.

> Your equipment turn-in document has now been assigned a temporary transaction number. Refer to this number during the life cycle of the request.

### Step 3

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> You will be asked next to select the items from the Equipment Inventory (AEMS/MERS) file that you wish to turn in. After you have selected and filled in the justification for turning in this equipment, it will go to the responsible CMR Responsible Official for review and approval.

> June 1996 Equipment/Turn-In Request Version 1.0 65

> User Manual

> Turn-Ins

### Edit Excess Equipment Turn-In Document

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If a turn-in document has been left incomplete, then the ability exists for you, the requestor, to make changes and even add additional items.

> 66 Equipment/Turn-In Request Version 1.0 June 1996 User Manual

<span id="9.1.3_Canc_Excess_Eqp/T-In_Request" class="anchor"></span>Turn-Ins

### Cancel Excess Equipment Turn-In Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The ability to cancel an incomplete or returned turn-in document also exists.

## CMR Official

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The CMR Responsible Official must review and approve Turn-In documents since they are responsible for that equipment.

### Enter Equipment Turn-In Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> A CMR Responsible Official can act as a requestor for entering turn-in documents. See 9.1.2 for more information.

### Edit Equipment Turn-In Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> See 9.1.3 for more information.

### Cancel Turn-In Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> See 9.1.4 for more information.

> June 1996 Equipment/Turn-In Request Version 1.0 67

> User Manual

> <span id="9.2.4_Display/Print_Turn-In_Req" class="anchor"></span>Turn-Ins

### Display/Print Turn-In Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 37%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>25</p>
</blockquote></th>
<th>621-780-95-00007</th>
<th><blockquote>
<p>Turn-in Completed</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>26</p>
</blockquote></td>
<td>621-780-95-00012</td>
<td><blockquote>
<p>Pending PPM Final Disposition</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>27</p>
</blockquote></td>
<td>621-323-95-00002</td>
<td><blockquote>
<p>Pending PPM Final Disposition</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>28</p>
</blockquote></td>
<td>621-323-95-00003</td>
<td><blockquote>
<p>Pending Warehouse Pickup</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>29</p>
</blockquote></td>
<td>621-123-96-00006</td>
<td><blockquote>
<p>Cancelled Request</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>30</p>
</blockquote></td>
<td>621-123-96-00007</td>
<td><blockquote>
<p>Cancelled Request</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>31</p>
</blockquote></td>
<td>621-666-96-00001</td>
<td><blockquote>
<p>Pending Warehouse Pickup</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>38</p>
</blockquote></td>
<td>621-666-96-00010</td>
<td><blockquote>
<p>Pending PPM Review</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>39</p>
</blockquote></td>
<td>621-136-96-00002</td>
<td><blockquote>
<p>Pending PPM Review</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>49</p>
</blockquote></td>
<td>621-780-96-00001</td>
<td><blockquote>
<p>Pending CMR Official Review</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>50</p>
</blockquote></td>
<td>621-780-96-00002</td>
<td><blockquote>
<p>Pending Completion by Requestor</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>51</p>
</blockquote></td>
<td>621-780-96-00003</td>
<td><blockquote>
<p>Pending CMR Official Review</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>52</p>
</blockquote></td>
<td>621-780-96-00004</td>
<td><blockquote>
<p>Pending CMR Official Review</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>53</p>
</blockquote></td>
<td>621-780-96-00006</td>
<td><blockquote>
<p>Pending Completion by Requestor</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>54</p>
</blockquote></td>
<td>621-666-96-00013</td>
<td><blockquote>
<p>Pending Completion by Requestor</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>55</p>
</blockquote></td>
<td>621-666-96-00015</td>
<td><blockquote>
<p>Pending Completion by Requestor</p>
</blockquote></td>
</tr>
</tbody>
</table>

### Approve Equipment Turn-In Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The CMR Responsible Official responsible for the equipment must review and approve any turn-in documents prior to review by the Personal Property Manager. The CMR Responsible Official will be notified when a turn-in request has been generated with an alert message.

### Step 1

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Select the request you wish to review.

> 68 Equipment/Turn-In Request Version 1.0 June 1996 User Manual

<span id="_bookmark106" class="anchor"></span>Turn-Ins

### Step 2

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The request will display on the screen.

## PPM Official

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The PPM processes turn-ins in three steps; reviewing turn-in requests, reviewing completed work orders, and sending to the warehouse for pickup. PPM must first review any turn-in requests to determine if a work order must be created in order for Engineering to disconnect or otherwise remove the equipment. After Engineering has performed its’ work order, the PPM needs to tell the warehouse that items(s) need to be picked-up by the warehouse. After the warehouse has picked up the item, the PPM will perform final disposition of the item.

> June 1996 Equipment/Turn-In Request Version 1.0 69

> User Manual

> Turn-Ins

### Process Turn-In Request (Pending PPM Review)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The PPM will review the item(s) being turned in and assign a preliminary DISPOSAL CONDITION CODE and possible DISPOSITION METHOD and makes the determination if a work order is needed. If a work order is needed for a particular item for Engineering, the PPM will be prompted, ‘Should a work order be generated for this line item?’ for each item in the request so they can create one and forward it to Engineering. Not all items in a request may need to have a work order produced for turn-in. See Engineering User Manual on how to process a work order. When the DATE COMPLETED has been entered by Engineering, the turn- in will return to the PPM.

> 70 Equipment/Turn-In Request Version 1.0 June 1996 User Manual

Turn-Ins

### Process Turn-In Request (Work Order Completed)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The PPM will send the request to the Warehouse to pick up the item(s) being turned in. See Chapter 8 Warehouse to review this step.

> June 1996 Equipment/Turn-In Request Version 1.0 71

> User Manual

> Turn-Ins

> Select Process Equipment Turn-Ins Menu Option: PROC\<RET\>ess Equipment Turn-In Request (PPM) Select TURN-IN REQUEST TRANSACTION CODE: ?? \<RET\>

> Choose from:

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 44%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>28</p>
</blockquote></th>
<th>621-323-95-00003</th>
<th><blockquote>
<p>Work Order Completed</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>35</p>
</blockquote></td>
<td>621-666-96-00006</td>
<td><blockquote>
<p>Work Order Completed</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>38</p>
</blockquote></td>
<td>621-666-96-00010</td>
<td><blockquote>
<p>Pending PPM Review</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>39</p>
</blockquote></td>
<td>621-136-96-00002</td>
<td><blockquote>
<p>Pending PPM Review</p>
</blockquote></td>
</tr>
</tbody>
</table>

> <span id="_bookmark110" class="anchor"></span>Select TURN-IN REQUEST TRANSACTION CODE: DEVICE: HOME// \<RET\>

> 28 \<RET\>

> 621-323-95-00003 Work Order Completed

> TRANSACTION CODE: 621-323-95-00003 REQUESTOR: ETRUSER , FOUR

> REQUESTING SERVICE: ETRVENDOR , SEVEN

> REQUEST DATE/TIME: AUG 15, 1995@17:47:42 STATION NUMBER: 621 CMR RESPONSIBLE OFFICIAL: ETRUSER , ONE

> REQUEST STATUS: Work Order Completed

> STATUS DATE: MAY 14, 1996 CMR OFFICIAL APPROVAL: YES CMR OFFICIAL EXPLANATION:

> NEED TO REPLACE MORE THAN ONE

> Is this request ready to go to Warehouse for pickup? Yes// \<RET\> (Yes)

> Select TURN-IN REQUEST TRANSACTION CODE: DEVICE: HOME// \<RET\>

> 35 \<RET\>

> 621-666-96-00006 Work Order Completed

> TRANSACTION CODE: 621-666-96-00006 REQUESTOR: ETRUSER , FOUR

> REQUESTING SERVICE: ETRVENDOR , SEVEN

> REQUEST DATE/TIME: JAN 26, 1996@10:42:46 STATION NUMBER: 621 CMR RESPONSIBLE OFFICIAL: ETRUSER , THREE

> REQUEST STATUS: Work Order Completed

> STATUS DATE: MAY 14, 1996 CMR OFFICIAL APPROVAL: YES CMR OFFICIAL EXPLANATION:

> Is this request ready to go to Warehouse for pickup? Yes// \<RET\> (Yes) Select TURN-IN REQUEST TRANSACTION CODE: \<RET\>

### Final Disposition of a Turn-In

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> After Engineering has processed the work order (if one was needed), and the Warehouse has picked up the equipment, the turn-in is sent back to the PPM for final disposition and processing of the item(s) which may include generating a FD code sheet for FMS.

> 72 Equipment/Turn-In Request Version 1.0 June 1996 User Manual

Turn-Ins

> June 1996 Equipment/Turn-In Request Version 1.0 73

> User Manual

> Turn-Ins

> 74 Equipment/Turn-In Request Version 1.0 June 1996 User Manual

# CHAPTER 10 GLOSSARY

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>2237</strong></p>
</blockquote></th>
<th><blockquote>
<p>VA Form 2237<strong>,</strong> used to request goods and services.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>AEMS-MERS</strong></p>
</blockquote></td>
<td><blockquote>
<p>Name of the computer system located at each medical center</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>to support Consolidated Memorandum of Receipts.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Application</strong></p>
</blockquote></td>
<td><blockquote>
<p>The individuals responsible for the implementation, training</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Coordinator</strong></p>
</blockquote></td>
<td><blockquote>
<p>and trouble-shooting of a software package within a service.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>IFCAP requires that there be an Application Coordinator</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>designated for Fiscal Service and the Control Points</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>(Requesting Services).</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Category Stock</strong></p>
</blockquote></td>
<td><blockquote>
<p>A number used to identify non-expendable types of</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Number</strong></p>
</blockquote></td>
<td><blockquote>
<p>equipment.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>CSN</strong></p>
</blockquote></td>
<td><blockquote>
<p>See Category Stock Number.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Equipment</strong></p>
</blockquote></td>
<td><blockquote>
<p>A section/division of A&amp;MM Service or similar activity</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Management</strong></p>
</blockquote></td>
<td><blockquote>
<p>responsible for screening all equipment requests. They are</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>accountable for all equipment (CMRs) at the facilities they</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>support.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>FMS</strong></p>
</blockquote></td>
<td><blockquote>
<p>Financial Management System - System that replaced</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>CALM.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Integrated Supply</strong></p>
</blockquote></td>
<td><blockquote>
<p>System in which catalog information exists. You can query</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Management</strong></p>
</blockquote></td>
<td><blockquote>
<p>for description and category stock number.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>System (ISMS)</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Item Master File</strong></p>
</blockquote></td>
<td><blockquote>
<p>A data base of items specific to each A&amp;MMS. This file</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>maintains a full description of the item and costs, as well as</p>
</blockquote></td>
</tr>
<tr class="even">
<td></td>
<td><blockquote>
<p>other related information<strong>,</strong> such as stock number, vendor,</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
<td><blockquote>
<p>contract number and a procurement history.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Item Master</strong></p>
</blockquote></td>
<td><blockquote>
<p>A computer generated number used to identify an item in the</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Number</strong></p>
</blockquote></td>
<td><blockquote>
<p>Item Master file.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>National Stock</strong></p>
</blockquote></td>
<td><blockquote>
<p>A number used to identify expendable supply items.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Number</strong></p>
</blockquote></td>
<td></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>NSN</strong></p>
</blockquote></td>
<td><blockquote>
<p>See National Stock Number.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> June 1996 Equipment/Turn-In Request Version 1.0 75

> User Manual

<table>
<colgroup>
<col style="width: 26%" />
<col style="width: 73%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>Glossary</p>
</blockquote></th>
<th></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>PPM/MMS</strong></p>
</blockquote></td>
<td><blockquote>
<p>Personal Property Management/Materiel Management Service.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Purchase Order</strong></p>
</blockquote></td>
<td><blockquote>
<p>A government document authorizing the purchase of the goods or services at the terms indicated.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Purchasing Agent</strong></p>
</blockquote></td>
<td><blockquote>
<p>The employee authorized to place orders with vendors.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Short Description</strong></p>
</blockquote></td>
<td><blockquote>
<p>A phrase which describes the item in the Item Master file. It is restricted to 3 to 60 characters and consists of what the item is, the kind of item and the size of item (i.e., GLOVE- SURGICAL-MED).</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Subaccount/BOC</strong></p>
</blockquote></td>
<td><blockquote>
<p>A Fiscal Code which related to financial accounting/budget information.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Tasked Job</strong></p>
</blockquote></td>
<td><blockquote>
<p>A job, usually a printout, that has been scheduled to run at a predetermined time. Tasked jobs are set up to run automatically.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>VA Form 2237</strong></p>
</blockquote></td>
<td><blockquote>
<p>VA Form 2237<strong>,</strong> used to request goods and services.</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p><strong>Vendor File</strong></p>
</blockquote></td>
<td><blockquote>
<p>An IFCAP (or FMS) file of vendors with which the facility does business. This file contains ordering and billing addresses, contract information, FPDS information and telephone numbers. File 440 contains information about the vendors that your station does business with. The debtor's address may be drawn from this file but is maintained separately. If the desired vendor is not in the file, contact A&amp;MM Service to have it added.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Vendor ID Number</strong></p>
</blockquote></td>
<td><blockquote>
<p>The ID number assigned to a vendor by FMS.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> 76 Equipment/Turn-In Request Version 1.0 June 1996 User Manual