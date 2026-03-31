---
title: VDEF Version 1 Technical Manual
doc_type: TM
doc_label: Technical Manual
doc_layer: anchor
doc_subject: 
app_code: VDEF
app_name: VistA Data Extraction Framework
section: INF
app_status: active
pkg_ns: VDEF
patch_ver: 1
patch_id: VDEF*1
group_key: "VDEF:VDEF:1"
file_numbers: 
  - 101
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - vdef
  - request
  - table
  - contents
  - queue
  - entry
  - processor
  - event
  - package
  - monitor
page_count: 0
word_count: 5475
section_count: 18
table_count: 22
figure_count: 0
appendix_count: 4
has_toc: False
is_stub: False
pub_date: December 2004
revision_count: 3
revision_newest: 8/5/09
revision_oldest: 6/9/09
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Vista_Data_Ex_(VDEF)/vdef_1_0_technical_manual.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Vista_Data_Ex_(VDEF)/vdef_1_0_technical_manual.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=144"
---

VistA Data Extraction Framework 1.0

Technical Manual

Document Revision 1.8

![](vdef-version-1-technical-manual/001.png)

VA Office of Information and Technology (OI&T)

Veterans Health Information Technology (VHIT)

VistA Messaging Services

(*This page left blank for two sided printing*)

Revision History

|                |          |                                                                                                              |          |
|----------------|----------|--------------------------------------------------------------------------------------------------------------|----------|
| Date           | Revision | Description                                                                                                  | Author   |
| December 2004  | 1.0      | Created document                                                                                             | REDACTED |
| January, 2006  | 1.1      | VDEF\*1.0\*3 - Documents false VDEF alerts and restarting VDEF queue processor.                              | REDACTED |
| October, 2007  | 1.2      | Technical Edit                                                                                               | REDACTED |
| April 3, 2009  | 1.3      | Remove the residual information about HLO. (VDEF_CR7)                                                        | REDACTED |
| April 13 2009  | 1.4      | Reformatted document, accepted changes, revised diagram, removed comments, uploaded to ClearCase. (VDEF_CR7) | REDACTED |
| April 15, 2009 | 1.5      | Provided additional information in P4 & P14 (VDEF_CR7)                                                       | REDACTED |
| April 21, 2009 | 1.5      | Technical Edit (VDEF_CR7)                                                                                    | REDACTED |
| 6/9/09         | 1.6      | Technical Edit – incorporated changes from development and SQA. (VDEF_CR7)                                   | REDACTED |
| 7/23/09        | 1.7      | Technical Edit . (VDEF_CR7)                                                                                  | REDACTED |
| 8/5/09         | 1.8      | Technical Edit . (VDEF_CR7)                                                                                  | REDACTED |

(*This page left blank for two sided printing*)

Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Implementation and Maintenance](#implementation-and-maintenance)
  - [VDEF Initialization at System Startup](#vdef-initialization-at-system-startup)
  - [VDEF Request Queue Population](#vdef-request-queue-population)
  - [VDEF Request Fulfillment by the Request Processor](#vdef-request-fulfillment-by-the-request-processor)
  - [VDEF Monitoring and Other Site-Wide Parameters](#vdef-monitoring-and-other-site-wide-parameters)
    - [Custodial Package Deactivation](#custodial-package-deactivation)
    - [Request Processor Scheduling](#request-processor-scheduling)
    - [VDEF Request Queue Processor Monitor](#vdef-request-queue-processor-monitor)
  - [VDEF Status](#vdef-status)
  - [Deleting Request Queue Entries](#deleting-request-queue-entries)
- [Files](#files)
- [Routines](#routines)
- [Exported Options](#exported-options)
- [Archiving and Purging](#archiving-and-purging)
- [# Entry Points/Callable Routines/APIs](#entry-pointscallable-routinesapis)
  - [Entry Point \$\$QUEUE^VDEFQM](#entry-point-queuevdefqm)
    - [Calling Syntax](#calling-syntax)
    - [Input Parameters](#input-parameters)
    - [Function Return Value](#function-return-value)
  - [Entry Point SETDLMS^VDEFEL](#entry-point-setdlmsvdefel)
    - [Calling Syntax](#calling-syntax-1)
    - [Input Parameters](#input-parameters-1)
    - [Output Value](#output-value)
  - [Entry Point \$\$XCN200^VDEFEL()](#entry-point-xcn200vdefel)
    - [Calling Syntax](#calling-syntax-2)
    - [Prerequisite](#prerequisite)
    - [Input Parameters](#input-parameters-2)
    - [Function Return Value](#function-return-value-1)
  - [Entry Point \$\$TS^VDEFEL()](#entry-point-tsvdefel)
    - [Calling Syntax](#calling-syntax-3)
    - [Input Parameter](#input-parameter)
    - [Function Return Value](#function-return-value-2)
  - [Entry Point POSTKID^VDEFVU()](#entry-point-postkidvdefvu)
    - [Calling syntax](#calling-syntax-4)
    - [Input Variables](#input-variables)
    - [Output](#output)
  - [Entry Point ERR^VDEFREQ()](#entry-point-errvdefreq)
    - [Calling syntax](#calling-syntax-5)
    - [Input Parameter](#input-parameter-1)
    - [Output](#output-1)
- [External Interfaces](#external-interfaces)
- [External Relations](#external-relations)
  - [Integration Agreements](#integration-agreements)
  - [Package Dependencies](#package-dependencies)
- [Internal Relations](#internal-relations)
- [Package-Wide Variables](#package-wide-variables)
- [Software Products Security](#software-products-security)
  - [Mail Groups and Alerts](#mail-groups-and-alerts)
  - [Remote Systems](#remote-systems)
    - [Acknowledgements](#acknowledgements)
  - [Contingency Planning](#contingency-planning)
- [Appendix A: VDEF Shut Down Procedures](#appendix-a-vdef-shut-down-procedures)
- [Appendix B: VDEF Initial Setup Procedures](#appendix-b-vdef-initial-setup-procedures)
- [Appendix C: VDEF Files](#appendix-c-vdef-files)
- [Appendix D: VDEF Alert Messages](#appendix-d-vdef-alert-messages)
VistA Data Extraction Framework (VDEF) is a VistA package that uses hard-coded MUMPS (M) routines to create and deliver Health Level 7 (HL7) messages. The VDEF package supports queuing requests for messages, control of the timing of message creation, monitoring of the request queue, and recording of errors encountered during message creation. The hard-coded programs are M programs belonging to an application’s namespace. Messages are delivered using the VistA HL7 package.

# Implementation and Maintenance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VDEF package is installed as a regular Kernel Installation and Distribution System (KIDS) build. Once installed, Information Resource Management (IRM) staff will need to set up and activate the appropriate HL7 link parameters and add the VDEF STARTUP OPTION to the list of Scheduled Startup Options. (See Section 4.1 of the *VDEF Installation and User Configuration Guide* for details.)

Once the configuration process is complete and the decision has been made to turn on VDEF messaging, IRM staff will need to go into the VDEF Configuration and Status menu and select a number of menu options. (See Section 4 of the *VDEF Installation and User Configuration Guide* for details.)

Once these tasks are performed, VDEF messaging will be activated. VDEF messaging consists of the activities outlined in the sections below.

| Note | Per VHA Directive 2004-038, this package should not be modified after installation. |
|----------|-------------------------------------------------------------------------------------|

## VDEF Initialization at System Startup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VDEF STARTUP OPTION was released as part of the original VDEF build. Once IRM staff adds it to the list of Scheduled Startup Option in TaskMan during the VDEF installation, then VDEF will become fully functional. Please refer to the *VDEF Installation and User Configuration Guide* for details on how to set it up in TaskMan.

When VistA is brought up, TaskMan will run the VDEF STARTUP OPTION scheduled option. When the option runs, it submits the following TaskMan processes for subsequent execution:

- VDEF Checked Out Monitor
- VDEF Request Processor for \<name of Request queue\> (one per Request Queue)
- VDEF Request Processor Monitor

IRM staff can prevent this VDEF STARTUP OPTION from starting any VDEF TaskMan processes except the VDEF Monitor. In the Suspend/Run Request Queue option, they will need to change the field from “running” to “suspend” in the VDEF Request Queue. However, the VDEF Monitor cannot be prevented from running at VistA Startup unless the VDEF STARTUP OPTION is removed from the list of Scheduled Startup Options and the task that is scheduled to run the VDEF Monitor with TaskMan is deleted. This should only occur if VDEF is being completely uninstalled at the site.

## VDEF Request Queue Population

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When certain events occur within the VistA application, the VistA software issues a call to the VDEF Application Programmer Interface (API). (Refer to the API specification for \$\$QUEUE^VDEFQM below.)

Each VDEF Request contains the VDEF Event Type that contains the HL7 Message Type and Event Type, and two Name-Value Pairs, which tell VDEF what data to extract. The recognized VDEF Event Types are stored in the VDEF EVENT DESCRIPTION file (#577).

It should be noted that custodial package-specific KIDS build deploys individual VDEF Event Type entries in the VDEF EVENT DESCRIPTION file (#577). For example, a KIDS build will deploy the Event Types that cover files like the GMRV VITAL MEASUREMENT. If a particular VDEF Event Type is not installed at a given site, then the VDEF API will reject any VDEF Requests for this Event Type.

When \$\$QUEUE^VDEFQM is called, the VDEF API retrieves the default Requestor from the VDEF REQUESTOR file (#579.1). Once the Requestor is established, the VDEF API checks the following:

- Whether this Requestor is active, and
- Whether the custodial package for this VDEF Event Type has VDEF messaging turned on.

If these conditions are satisfied, the VDEF API creates an entry in the Request Queue associated with the given requestor.

| WARNING | IRM staff can disable the creation of VDEF Requests for a given interface by deactivating a Requestor (see above). Be advised that preventing the generation of VDEF messages for one or more of the custodial packages for which it is enabled will result in a loss of synchronization between VistA and the remote systems that receive these custodial package messages. Once synchronization is lost for a custodial package, there is no easy way of getting the remote system(s) back in synch with VistA. Only turn VDEF messaging off for a custodial package if the custodial package is also disabled for all remote systems receiving this custodial package’s data. Deactivation at the requestor level should only occur when that requestor system (e.g., HDR) is being completely disabled. |
|-------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## VDEF Request Fulfillment by the Request Processor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Upon system startup, through the VDEF STARTUP OPTION, TaskMan initiates one Request Processor job (EN^VDEFREQ) for every Request Queue. Once started, each Request Processor verifies that its assigned Request Queue has not been suspended since the Processor last ran. If it has, then the Request Processor does not start.

The Request Processor then checks if the current date/time falls inside the timeframe defined for this RUN TIME sub file (#579.32) when it should not run. If it does fall within this timeframe, the request Processor waits to run at the end of that timeframe and starts processing the Request queue.

After processing any queued up requests, the Request Processor waits for the number of seconds defined in the WAKEUP PERIOD to elapse. Then it processes new all entries in the Request Queue that are assigned to it that have accumulated while it was in the wait loop. It repeats this cycle continuously.

IRM staff can use the Suspend/RUN Request Queue menu option to stop the Request Processor for an individual Request Queue. Request Processor tasks check internal TaskMan flags to see if they have been asked to stop after completing every VDEF Request. IRM staff can also use the Request Queue Parameters options on the VDEF Configuration and Status menu to change the WAKEUP PERIOD value for the Queue, or define timeframes when individual Request Processors will not run (see the description of the VDEF Request Processor Schedule menu option below).

If the Request Processor for a Request Queue is suspended, VDEF requests continue to accumulate in it until it is turned on again. The main reason for suspending a Request Processor is likely to be system performance deterioration due to VDEF activities running during regular business hours.

| WARNING | There is no loss of functionality associated with suspending a Request Processor for a certain period of time and then turning it back on. The only impact on the system is that it may cause the receiving remote systems to fall further behind VistA while the processor is down and while it is catching up. Although the remote systems will catch up, suspending a queue could, depending on the nature of the data involved, result in a patient safety issue. |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

When a Request Processor is running, it examines the assigned Request Queue for Queued up Requests. If any are found, the Request Processor takes the first Queued Up request and changes the status to “Checked Out.” The Request Processor then calls the VDEF message-building M routine for the Internal Entry Number (IEN) specified in the Name/Value Pair that was sent the trigger application's VDEF API call. The IEN is the IEN of the primary global that the data associated with the trigger event will be found.

Once each HL7 message is built, the Request Processor retrieves the VistA HL7 protocol for this VDEF Event Type, identifies its associated subscriber protocols, calls VistA HL7, and passes the body of the message to it for delivery to the designated remote systems. If the VistA HL7 package encounters a problem and returns an error (e.g., if the Dynamic Addressing array passed to VDEF was invalid), then the Request Processor marks the Request as “Errored Out” and stores the error text returned by VistA HL7 in the Request’s Error field.

Once the HL7 message for a given request has been generated, the Request Processor changes the status of the Request from “Checked Out” to “Processed” and moves on to the next Queued-up request.

Because maintenance requests are eventually routed to their destination remote systems via the VistA HL7 package, IRM staff may need to monitor and possibly adjust VDEF-specific VistA HL7 filters and links as per their standard VistA HL7 monitoring procedures.

IRM staff can modify the following parameters for any of the VDEF Request Queues using menu option VDEF Request Queue Parameters:

- <u>ARCHIVAL PARAMETER</u>: A minimum amount of time (in days, hours, minutes, and seconds) that a processed VDEF Request remains in this Request Queue before it is purged by the VDEF Monitor (see below).
- <u>REQUEST QUEUE WAKEUP PERIOD</u>: A period of time (in days, hours, minutes, and seconds) that TaskMan uses to calculate how long to wait before it resumes processing the Request queue.

VDEF Request Processors use two more configuration settings that are not Request Queue specific. These settings can be viewed and changed via the option VDEF Site-Wide Parameters on the VDEF Configuration and Status menu and are as follows:

- VDEF SYSTEM: \<system’s domain name\>//
- VDEF MONITOR DELAY: 5M//

## VDEF Monitoring and Other Site-Wide Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VDEF Monitor process MONITOR^VDEFCONT is submitted by the VDEF STARTUP OPTION at VistA startup (see above). It is not associated with any specific queue, so there is only one VDEF Monitor process per VistA system. The VDEF Monitor resubmits itself every so many seconds based on the value of the VDEF MONITOR DELAY parameter that can be changed in the Site-Wide Parameters option.

When the VDEF Monitor runs, it checks all Request Queues for Checked Out entries. If it finds any, it gets the Check Out date and time, and the current system date and time for each Checked Out entry and compares the time difference against the “CHECK-OUT TIME LIMIT” at File-579.3 Field-.05. If it is greater than the allowed time (or Check-Out Time Limit), the VDEF Monitor sends an alert to the VDEF NATIONAL ALERTS group specified in the VDEF ALERTS mail group and re-queues the request.

The VDEF Monitor also looks at all processed entries in each Request Queue, starting with the oldest one. The entries that have been in the “Processed” state longer than the value of the ARCHIVAL PARAMETER for that Request Queue are deleted.

The other site-wide parameters that IRM staff can modify are described in the following sections 2.4.1 to 2.4.3.

### Custodial Package Deactivation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When a custodial package-specific VDEF KIDS build is installed at a site, a custodial package record is added to the VDEF Custodial Package file (#579.6) only if it is a new entry and a VDEF Event record is created in the VDEF EVENT DESCRIPTION file (#577). They are both created with status defaulted to INACTIVE.

IRM staff can activate and deactivate VDEF messaging for individual custodial packages using the menu option VDEF Custodial Package. When prompted for the custodial package to (de)activate, IRM staff can either enter “??” to list all custodial packages that currently have VDEF messaging installed on site, or enter an individual custodial package to (de)activate VDEF messaging. When trying to deactivate (but not when trying to activate) VDEF messaging for a custodial package, a warning is generated because VistA and the receiving system(s) become out of sync and there is no easy way to “re-sync” them.

The only custodial package for which IRM staff cannot deactivate VDEF messaging is Registration. If IRM staff select and attempt to deactivate it, an error message will be displayed.

### Request Processor Scheduling

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A Request Queue Processor runs at the interval specified in the REQUEST QUEUE WAKEUP PERIOD and processes the “Queued up” Requests in the Request Queue for which it is responsible. During peak operating hours when the system is under heavy load, IRM staff may decide to suspend the VDEF queue processing temporarily. IRM staff can prevent a Request Processor from running by manually suspending it using the VDEF Suspend/Run Request Queue option. <u>Although useful as an ad hoc tool, it is a manual process and IRM staff will need to remember to un-suspend the Processor when the load becomes more manageable</u>.

An alternative to manual suspension and continuation of Request Processors is the VDEF Request Processor Schedule menu option. When IRM staff access it and identify the Request Queue whose behavior needs to be modified, IRM staff can define any number of scheduling rules for the Request Processor that handles that Request Queue.

For every rule, IRM staff must enter the following information:

- <u>ENTRY</u>: A unique alphanumeric identifier for this scheduling rule.
- <u>DAY OF THE WEEK</u>: The day of the week to which this scheduling rule applies (e.g., Sunday or Wednesday).
- <u>FORCED STATUS</u>: Running or Suspended
- <u>FROM TIME</u>: The time (in military time format) that the Request Processor for this Request Queue will be in the FORCED STATUS.
- <u>TO TIME</u>: The time (in military time format) when the Request Processor for this Request Queue will resume normal execution.

Once this information is entered, the Request Processor checks all the rules that apply to the current day of the week. It will not run if the current time falls within any of the time windows defined for it.

### VDEF Request Queue Processor Monitor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VDEF Request Queue Processor Monitor MONITOR^VDEFCONT is submitted by the VDEF STARTUP OPTION at VistA startup. It is not associated with any specific queue, so there will be only one of these processes. The VDEF Request Queue Process Monitor checks several things in the VDEF system and then goes into a ten-minute wait loop. It then continuously repeats the checks.

The monitor first checks to see if any Request Queue Processors are in the suspended state or have stopped running. It does this for each Request Queue that is defined in VDEF. If either of the above checks is true, the monitor will generate an alert. If a Request Queue Processor has stopped, it will be restarted by the monitor by creating a new TaskMan task for EN^VDEFREQ.

Then it checks for any requests that are hung in the Checked Out status and re-queues the requests to be processed again. It also does the same check for requests that are in the Errored Out status.

Then it goes into a ten-minute wait loop.

## VDEF Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option can be used to view the current status of the core VDEF components, including:

- Logical links used by VDEF: VDEFVIEn
- VDEF Requestors’ activation status: MAINTENANCE.
- VDEF Request Processors’ suspension status and the number of Queued Up, Checked Out, and Errored Out entries in their associated request Queues.

## Deleting Request Queue Entries

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To delete an unnecessary VDEF request, use VA FileMan's Enter/Edit Option to delete the subentry in the REQUEST QUEUE ENTRIES multiple of the VDEF REQUEST QUEUE file (#579.3). Delete a subentry only when you are sure that the request was erroneous or that it has been otherwise processed. You can also manually change the status of a request by editing the REQUEST ENTRY STATUS field of the subentry. Check the ERROR TEXT field (#.17) of the REQUEST QUEUE ENTRIES multiple for information that might explain a problem with a VDEF request.

Section 6 of the *VDEF Installation and User Configuration Guide* describes in detail when to delete a record and how to do it.

You should not delete a VDEF record unless directed to do so by the VDEF Custodial developer.

# Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following FileMan files belong to this package:

|                 |                        |
|-----------------|------------------------|
| File Number | File Name          |
| 577             | VDEF EVENT DESCRIPTION |
| 577.4           | VDEF EVENT SUBTYPES    |
| 579.1           | VDEF REQUESTOR         |
| 579.2           | VDEF DESTINATION       |
| 579.3           | VDEF REQUEST QUEUE     |
| 579.5           | VDEF SITE PARAMETERS   |
| 579.6           | VDEF CUSTODIAL PACKAGE |

# Routines

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following M routines belong to this package:

- VDEFCONT
- VDEFEL
- VDEFKIDS
- VDEFMON
- VDEFMNU
- VDEFMNU1
- VDEFQM
- VDEFREQ
- VDEFREQ1
- VDEFUTIL
- VDEFVU

# Exported Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following options are delivered with this package:

|                                            |                                    |                                        |                                                                                                           |
|--------------------------------------------|------------------------------------|----------------------------------------|-----------------------------------------------------------------------------------------------------------|
| Menu Name                              | Menu Text                      | Parent Option                      | Comments                                                                                              |
| VDEF STARTUP OPTION                        | VDEF STARTUP OPTION                | No parent: queueable option.           | This Scheduled Option is run at system startup. It initiates the individual Request Queue processor jobs. |
| VDEF CONFIGURATION MENU                    | VDEF Configuration and Status      | No parent: assign at IRM’s discretion. | Main VDEF menu                                                                                            |
| VDEF Activate/Inac Requestor               | Activate/INACTIVATE Requestor      | VDEF Configuration and Status          | Completely turns off VDEF messaging for a VDEF Requestor.                                                 |
| VDEF Site-Wide Parameters                  | Site-Wide Parameters               | VDEF Configuration and Status          | Configures VDEF parameters for the whole VistA site.                                                      |
| VDEF Request Queue Parameters              | Request Queue Parameters           | VDEF Configuration and Status          | Configures parameters for a VDEF Request Queue.                                                           |
| VDEF Suspend/Run Request Queue             | Suspend/RUN Request Queue          | VDEF Configuration and Status          | Suspends generation of HL7 messages for a given VDEF Request Queue.                                       |
| VDEF Custodial Package Activate/Deactivate | VDEF Custodial Package             | VDEF Configuration and Status          | Completely turns off VDEF message queuing for all VDEF Events associated with a given custodial package.  |
| VDEF Request Processor Schedule            | Request Processor Schedule         | VDEF Configuration and Status          | Tells the Request Processor for a given Request Queue when not to run.                                    |
| VDEF Status                                | Status of VDEF components          | VDEF Configuration and Status          | Displays the current status of VDEF messaging.                                                            |
| VDEF Event API                             | VDEF Event API Activate/Inactivate | VDEF Configuration and Status          | Completely turns off VDEF message queuing for all VDEF Events for a given VDEF Event.                     |

# Archiving and Purging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VDEF Request Queue file (#579.3) has a parameter associated with it (ARCHIVAL PARAMETER field \[#.04\]) which tells the VDEF Monitor TaskMan process how long to wait after each request was fulfilled before deleting it from the queue. It is estimated that the most that this file will grow is 100Mb per day, which is based on about 300 bytes per one VDEF request and up to 300,000 VDEF requests per day. The ARCHIVAL PARAMETER field needs to be set up based on the actual volume of VDEF transactions per day and the disk space available.

| Note | Entries in the Request Queue file may accumulate if the Request Processor responsible for processing them is suspended for a prolonged period of time. Unprocessed (“Queued up”) entries in the Request Queue file are never deleted. Therefore, if a VDEF Request Processor is suspended indefinitely, but the VDEF Requestor that is associated with it remains Activated, then the Request Queue file will continue growing and will eventually fill up the User Class Identifier (UCI). It is important to make sure to Deactivate VDEF Requestors completely and not just Suspend their associated Request Processor if VDEF processing is to be turned off for a Requestor. |
|----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

# # Entry Points/Callable Routines/APIs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are several utilities in VDEFEL that can be used in writing extraction routines. They perform common, frequently needed functions. The Entry Points for VDEFEL are listed below:

## Entry Point \$\$QUEUE^VDEFQM

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Calling Syntax

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\$\$QUEUE^VDEFQM(event_ID,name_value_pairs,\[.text_message\])

### Input Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Event_ID

| Type | Description                                                                     | Optionality | Repeatability | Constraints                                                                                                                     | Example |
|----------|-------------------------------------------------------------------------------------|-----------------|-------------------|-------------------------------------------------------------------------------------------------------------------------------------|-------------|
| By Value | A string comprised of an HL7 Message Type and an HL7 Event Type separated by a "^". | Required        | None              | The value must be defined in the list of known VDEF Message Type/Event Type combinations in the VDEF EVENT Description file (#577). | "ORU^R01"   |

Name_Value_Pairs

| Type | Description                                                                                                                                                                                                                     | Optionality | Repeatability | Constraints                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Example              |
|----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|
| By Value | A string comprised of the following format: SUBTYPE=\<text\>^IEN=nn where the Subtype text is a code based on the application’s domain and the clinical event and the IEN is the IEN of the primary file associated with the event. | Required        | None              | All Subtype names must be defined for this Message Type/Event Type in the VDEF EVENT Description file (#577.4). The name “SUBTYPE” is reserved for the purposes of uniquely identifying the request sub-type when more than one VDEF Event is defined for a Message Type/Event Type combination. For example, the HL7 message type/event ORU^R01 is used by multiple VistA domains to send unsolicited results. In these cases, the Subtype is used to differentiate the sending domain’s unique message contents within the structure of the ORU^R01. | "SUBTYPE=VTLS^IEN=12345" |

Text_Message

| Type     | Description                                        | Optionality | Repeatability | Constraints | Example          |
|--------------|--------------------------------------------------------|-----------------|-------------------|-----------------|----------------------|
| By Reference | Acceptance or rejection text returned by the VDEF API. | Optional        | None              |                 | “Invalid Event Type” |

### Function Return Value

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Type       | Description                                                                                                         | Example |
|----------------|-------------------------------------------------------------------------------------------------------------------------|-------------|
| Function Value | A number whose value is 1 if the HL7 request was queued up for processing and 0 if it was not queued up for processing. | 1           |

## Entry Point SETDLMS^VDEFEL

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This Entry Point sets HL7 delimiters into individual variables based either on elements of HL() array or default HL7 delimiter values.

### Calling Syntax 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

SETDLMS^VDEFEL

### Input Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Type                    | Description               | Optionality | Repeatability | Constraints | Example |
|-----------------------------|-------------------------------|-----------------|-------------------|-----------------|-------------|
| Passed through symbol table | HL() as set by INIT^HLFNC2(). | Optional        | None              |                 |             |

### Output Value

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Type | Description        | Default |
|----------|------------------------|-------------|
| SEPC     | Component Separator    | ~           |
| SEPS     | Subcomponent Separator | &           |
| SEPR     | Repetition Separator   | \|          |
| SEPE     | Escape Character       | \\          |
| SEPF     | Field Separator        | ^           |

## Entry Point \$\$XCN200^VDEFEL()

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This Entry Point is given an IEN from the NEW PERSON file (#200) and the source of the NEW PERSON file, then returns an XCN data type. A source of the data is passed to the API to identify the HL7 field where the person information comes from.

### Calling Syntax

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\$\$XCN200^VDEFEL(DUZ,SRC)

### Prerequisite 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

HL7 delimiter (SEPC=”~”) was set by SETDLMS^VDEFEL or \$E(HL(“ECH”),1).

### Input Parameters

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Type       | Description                                                              | Optionality | Repeatability | Constraints                                                             | Example |
|----------------|------------------------------------------------------------------------------|-----------------|-------------------|-----------------------------------------------------------------------------|-------------|
| DUZ - By Value | Internal Entry Number from the NEW PERSON file (#200).                       | Required        | None              |                                                                             | 12345       |
| SRC – By Value | Pass a string to the second parameter to identify where the data originates. | Optional        | None              | Default value of 'VistA200' is used if nothing is passed in this parameter. | PHARMACIST  |

### Function Return Value

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 51%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Type</strong></th>
<th><strong>Description</strong></th>
<th><strong>Example</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Return Value</td>
<td>Function returns XCN data type.</td>
<td><p>W $$XCN200^VDEFEL(520637377)</p>
<p>520637377~LASTNAME~FIRSTNAME~~~~~VistA200</p>
<p>W $$XCN200^VDEFEL(520637377,”PHARMACIST”)</p>
<p>520637377~LASTNAME~FIRSTNAME~~~~~PHARMACIST</p></td>
</tr>
</tbody>
</table>

## Entry Point \$\$TS^VDEFEL()

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This Entry Point returns an HL7 TS data type.

### Calling Syntax

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\$\$TS^VDEFEL(datetime)

### Input Parameter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 10%" />
<col style="width: 21%" />
<col style="width: 9%" />
<col style="width: 10%" />
<col style="width: 30%" />
<col style="width: 18%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Type</strong></th>
<th><strong>Description</strong></th>
<th><strong>Optionality</strong></th>
<th><strong>Repeatability</strong></th>
<th><strong>Constraints</strong></th>
<th><strong>Example</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>By Value</td>
<td>Date/Time Value</td>
<td>Required</td>
<td>None</td>
<td>Format must be $H, internal FileMan format, or one of the external formats supported by FileMan</td>
<td><p>($H)</p>
<p>("3140820.154420")</p>
<p>("AUG 23, 2004@100923")</p></td>
</tr>
</tbody>
</table>

### Function Return Value

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 48%" />
<col style="width: 37%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Type</strong></th>
<th><strong>Description</strong></th>
<th><strong>Example</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Return Value</td>
<td>Function returns a TS data type, including time zone. No time zone is returned if no time is included in input.</td>
<td><p>W $$TS^VDEFEL($H)</p>
<p>20040820182643-0400</p>
<p>W $$TS^VDEFEL("3140820.154420")</p>
<p>20140820154420-0400</p>
<p>W $$TS^VDEFEL("AUG 23, 2004@100923")</p>
<p>20040823100923-0400</p></td>
</tr>
</tbody>
</table>

## Entry Point POSTKID^VDEFVU()

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This Entry Point is used in a post-init to add an entry to the VDEF Event Description file (#577) and, if necessary, to the VDEF Event Subtype (#577.4) and VDEF Custodial Package (#579.6) files. An individual call contains information for a single entry in the VDEF Event Description file (#577). If necessary, an Event Description is added for a new entry in the VDEF Event Subtype file (#577.4).

### Calling syntax

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

POSTKID^VDEFVU(MSGTYP,EVNTYP,SUBTYP,PROTO,CUSTPKG,EXTROUT,EVDESC,SUBDESC)

### Input Variables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  <u>MSGTYP</u>: External value for the MESSAGE TYPE field (.06) in the VDEF Event Description file (#577). (Corresponds to the .01 field of an existing entry in HL7 MESSAGE TYPE file \[#771.2\].)
2.  <u>EVNTYP</u>: External value for the EVENT TYPE field (.02) in the VDEF Event Description file (#577). (Corresponds to the .01 field of an existing entry in the HL7 EVENT TYPE CODE file \[#779.001\].)
3.  <u>SUBTYPE</u>: External value for the EVENT SUBTYPE field (.03) in the VDEF Event Description file (#577). (Corresponds to the .01 field of an entry in the VDEF Event Subtype file \[#577.4\]). If the entry does not exist in the VDEF Event Subtype file (#577.4), a new entry will be added for a new Subtype. An application should only add new VDEF Event Subtypes after the subtype has been authorized in writing by the DBA (in DaIS).
4.  <u>PROTO</u>: External value for the VISTA HL7 PROTOCOL field (.07) in the VDEF Event Description file (#577) (Corresponds to the .01 field of entry in the PROTOCOL file \[#101\].) A new entry in the Protocol file can be sent as part of the KIDS build.
5.  <u>CUSTPKG</u>: External value for the CUSTODIAL PACKAGE field (.09) in the VDEF Event Description file (#577) (Corresponds to the external value of the .01 of entry in the VDEF Event Description file \[#579.6\] that, in turn, corresponds to the .01 field in the PACKAGE file \[#9.4\].) If the entry does not exist in the VDEF Custodial Package file, a new entry will be added.
6.  <u>EXTROUT</u>: Value of the EXTRACTION PROGRAM field (.3) in the VDEF Event Description file (#577), the routine that will perform the extraction.
7.  <u>EVDESC</u>: Value of the EVENT DESCRIPTION field (1) in the VDEF Event Description file (#577).
8.  <u>SUBDESC</u>: Value of the EVENT DESCRIPTION field (.02) in the VDEF Event Subtype file (#577.4). The parameter is required only if a new entry is being made in the VDEF Event Subtype file (#577.4).

All input variables are required except for SUBDESC (parameter 8).

### Output

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Other than the creation of the desired file entries, this call’s only output are the error messages that are passed to the KIDS system for display when a problem is detected with the call.

## Entry Point ERR^VDEFREQ()

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This Entry Point is used to record an error encountered during message building being done as the result of a request passed to the VDEF queue. Use this API only inside a message building routine that is invoked by VDEF. The string passed to the API will be filed with the queued request that encounters the error in file 579.3.

### Calling syntax

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ERR^VDEFREQ(ERROR_STRING)

### Input Parameter

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

| Type | Description | Optionality | Repeatability | Constraints                                    | Example                                             |
|----------|-----------------|-----------------|-------------------|----------------------------------------------------|---------------------------------------------------------|
| By Value | Error String    | Required        | None              | A string containing the error message to be filed. | The requested entry in the Patient file does not exist. |

### Output

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are no return values. The input error message is filed in File \#579.3.

# External Interfaces

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VDEF package includes new HL7 Logical Links: VDEFVIEn. The VDEFVIEn links are used to deliver HL7 messages triggered by maintenance activities inside the VistA application to the local site’s Interface Engine. See the *VDEF Installation and Configuration Guide*, Section 3, for further HL7 Link configuration details.

# External Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

There are numerous Integration Agreements (IAs) covering the interdependencies between VDEF and the individual clinical domains from which VDEF extracts data to build its HL7 messages.

## Integration Agreements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The message building routines can make use of the following IAs to VDEF APIs:

| IA# | Access to VDEF Feature                  |
|---------|---------------------------------------------|
| 4253    | VDEF message building request               |
| 4248    | Message-building utilities                  |
| 4571    | Error recording                             |
| 4447    | Adding entries to VDEF files in KIDS builds |

The VDEF routines make use of the following IAs:

<table>
<colgroup>
<col style="width: 32%" />
<col style="width: 32%" />
<col style="width: 35%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Routine</strong></th>
<th><strong>IA#</strong></th>
<th><strong>Access to</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>VDEFREQ</td>
<td>3552</td>
<td>$$PARAM^HLCS2</td>
</tr>
<tr class="even">
<td>VDEFQM</td>
<td>4271</td>
<td>Lookup into #771.2</td>
</tr>
<tr class="odd">
<td>VDEFQM</td>
<td>4321</td>
<td>Lookup into #779.001</td>
</tr>
<tr class="even">
<td>VDEFMNU</td>
<td>1373</td>
<td>File #101 access</td>
</tr>
<tr class="odd">
<td>VDEFMNU</td>
<td>10063</td>
<td>$$JOB^%ZTLOAD</td>
</tr>
<tr class="even">
<td>VDEFMNU</td>
<td>4322</td>
<td>($P(^HLCS(870,link,0),U,12)</td>
</tr>
<tr class="odd">
<td>VDEFREQ1</td>
<td>4316</td>
<td>Access to #869.3</td>
</tr>
<tr class="even">
<td>VDEFCONT</td>
<td>10063</td>
<td><p>$$S^%ZTLOAD</p>
<p>$$ASKSTOP^%ZTLOAD</p></td>
</tr>
<tr class="odd">
<td>VDEFKIDS</td>
<td>10063</td>
<td><p>$$ASKSTOP^%ZTLOAD</p>
<p>RTN^%ZTLOAD</p></td>
</tr>
<tr class="even">
<td>VDEFKIDS</td>
<td>10103</td>
<td>$$FMADD^XLFDT</td>
</tr>
<tr class="odd">
<td>VDEFUTIL</td>
<td>10103</td>
<td>$$HTE^XLFDT</td>
</tr>
</tbody>
</table>

## Package Dependencies

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following packages must be properly installed in order for the VDEF to function properly:

| Required Applications | Minimum Version Number | Required Patches |
|---------------------------|----------------------------|----------------------|
| Kernel                    | 8.0                        | 257 SEQ \#234        |
| FileMan                   | 22.0                       | 105 SEQ \#111        |
| MailMan                   | 8.0                        | 13 SEQ \#13          |
| HL7                       | 1.6                        | 98 Seq \#85          |
| MailMan                   | N/A                        | XM\*DBA\*152         |

# Internal Relations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VDEF options and TaskMan processes are mostly independent of each other except as stated below. If there is no Request data to be processed, the Request Processor goes into a wait loop before checking the request queue for more entries to be processed.

# Package-Wide Variables 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All non-VistA standard local M variables used by VDEF are renewed at the beginning of each program. There are no package-wide variables.

# Software Products Security 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Mail Groups and Alerts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

All alerts generated by VDEF will be routed to the VDEF NATIONAL ALERTS mail group using the Application VDEF ALERTS. IRM staff should edit this Mail Group to make sure that the appropriate local IRM staff is included in the Mail Group. A MailMan message containing the text of the alert is also sent to the VDEF developer on FORUM and Outlook.

## Remote Systems

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The HDR-IMS is the first system to which VDEF will transmit HL7 messages. However, VDEF is capable of supporting a number of destinations for HL7 messages.

VistA HL7 destinations use the VistA HL7 package to transmit the generated HL7 messages to their remote systems. When using VistA HL7 destinations, HL7 messages may be delivered to multiple remote systems as long as the VistA HL7 subscriber information is set up properly for the affected HL7 Event Types.

At this time, VDEF software does not use any form of encryption beyond what is currently built into VistA HL7 and the BusinessWare Interface Engine. This approach is used because all recipients of the VDEF-generated HL7 data are behind the Department of Veterans Affairs (VA) firewall.

### Acknowledgements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Regarding maintenance requests, when a software trigger inside VistA calls the VDEF API (see this document for the API specification), the API returns “1” if the request was successfully queued up for processing or “0” otherwise. If the returned value is “0,” the VDEF API also returns a free text error message in an output parameter. Once the VDEF request is fulfilled and the resulting HL7 message is passed on to VistA HL7 for delivery to one or more remote systems, the VistA HL7 package will be responsible for processing the acknowledgements from those systems.

## Contingency Planning

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VDEF has the following built-in mechanisms that prevent adverse impact on the VistA system:

- Manual suspension of Request Queue Processor using the VDEF Suspend/RUN Request Queue menu option is designed to alleviate ad hoc performance problems that VDEF may cause.
- Automatic suspension of Request Processor using the VDEF Request Processor Schedule option is designed to alleviate chronic performance problems during peak load hours.

# Appendix A: VDEF Shut Down Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to section 5 of the *VDEF Installation and User Configuration Guide* for instructions on the procedures for shutting down various portions of the VDEF processing.

# Appendix B: VDEF Initial Setup Procedures

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Refer to the *VDEF Installation and User Configuration Guide*.

# Appendix C: VDEF Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

![](vdef-version-1-technical-manual/002.png)

# Appendix D: VDEF Alert Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following is the list of alerts that VDEF can generate.

1.  VDEF CHECKED OUT MONITOR FAILED TO START. CHECK ERROR TRAP.

The scheduled task MONITOR^VDEFCONT did not start as requested by the VDEF STARTUP OPTION.

2.  RECORD \<IEN\> IN QUEUE \<Queue name\> HUNG IN CHECKED OUT STATUS.

The request specified by the IEN in the queue specified in the QUEUE NAME has been in the Checked Out status longer than the allowed time period.

3.  VDEF REQUEST PROCESS \<Queue name\> FAILED TO START. CHECK ERROR TRAP.

The task EN^VDEFREQ failed to start as requested by the VDEF STARTUP OPTION.

4.  VDEF QUEUE PROCESS MONITOR DID NOT START. CHECK ERROR TRAP.

The task MONITOR^VDEFMON failed to start as requested by the VDEF STARTUP OPTION.

5.  VDEF HAS REQUEUED CHECKED OUT RECORDS. NO ACTION NEEDED.

The VDEF queue process monitor has re-queued one or more requests that were hung in the Checked Out status.

| Note | “NO ACTION NEEDED” is only true when this alert is not occurring every ten minutes. When this alert occurs every ten minutes, that is an indication that there is one or more VDEF requests that are getting hung in the Checked Out status and being re-queued but never processed. The alert cycle will continue until there is operator intervention to correct the problem with the request records. |
|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

6.  VDEF HAS REQUEUED ERRORED OUT RECORDS. NO ACTION NEEDED.

The VDEF queue process monitor has re-queued one or more requests that were in the Errored Out status.

| Note | “NO ACTION NEEDED” is only true when this alert is not occurring every ten minutes. When this alert occurs every ten minutes, that is an indication that there is one or more VDEF requests that are getting hung in the Errored Out status and being re-queued but never processed. The alert cycle will continue until there is operator intervention to correct the problem with the request records. |
|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

7.  VDEF QUEUE PROCESS MONITOR HAS EXITED.

The MONITOR^VDEFMON process has stopped running in response to a request to stop from TaskMan.

8.  VDEF QUEUE '\<Queue name\>' AUTO-RESTARTED. NO ACTION REQUIRED.

The MONITOR^VDEFMON process has found that the request queue process is not running and has restarted it by creating a new EN^VDEFREQ task.

9.  VDEF QUEUE '\<Queue name\>' IS SUSPENDED. PLEASE START IT.

The MONITOR^VDEFMON process has found that a Request Queue is in the Suspended state and needs to be reset to the Running state.

10. VDEF REQUEST QUEUE PROCESSOR FOR \<Queue name\> HAS EXITED.

The request queue process EN^VDEFREQ has stopped running in response to a request to stop from TaskMan or because the request queue status has changed to Suspended.