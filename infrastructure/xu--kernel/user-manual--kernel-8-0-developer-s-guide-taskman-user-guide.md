---
title: "Kernel 8.0 Developerâ€™s Guide: TaskMan User Guide"
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: "Developerâ€™s Guide: TaskMan"
app_code: XU
app_name: Kernel
section: INF
app_status: active
pkg_ns: XU
patch_ver: 8.0
patch_id: XU*8.0
group_key: "XU:XU:8.0"
file_numbers: []
security_keys: []
menu_options: 2
description: 
audience: 
keywords: 
  - task
  - taskman
  - ztload
  - tasks
  - device
  - table
  - contents
  - ztsk
  - span
  - print
page_count: 0
word_count: 16658
section_count: 37
table_count: 2
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: August 2025
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_taskman_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_taskman_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=10"
---

---
title: |
  Kernel 8.0 Developer’s Guide:

  <span id="_Toc204259574" class="anchor"></span>TaskMan Developer Tools  
  User Guide
---

![](kernel-8-0-developer-s-guide-taskman-user-guide/001.png)

August 2025

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Product Delivery Service (PDS)

<span id="_Toc234301875" class="anchor"></span>Revision History

![](kernel-8-0-developer-s-guide-taskman-user-guide/002.png) REF: For the archived document revision history, see “<u>Appendix A—Revision History Archive</u>.”

<table>
<caption><p><span id="_Ref502842948" class="anchor"></span>Table 1: TaskMan—ZTREQ Piece and Equivalent REQ^ZTLOAD Variable</p></caption>
<colgroup>
<col style="width: 14%" />
<col style="width: 12%" />
<col style="width: 43%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Revision</th>
<th>Description</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>08/28/2025</td>
<td>1.0</td>
<td><p>Initial document creation: <em>Kernel Developer’s Guide: TaskMan Developer Tools User Guide</em>.</p>
<p>This is part of the VASS Documentation Redesign Project. The content in this document came from the original <em>Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide</em> document, which was too large and cumbersome to maintain; so, it was broken down into smaller user guides for ease of use and maintenance going forward.</p>
<p><strong>Software Versions:</strong></p>
<p><strong>Kernel 8.0</strong></p>
<p><strong>Toolkit 7.3</strong></p></td>
<td>VistA Application Shared Services (VASS) Development Team</td>
</tr>
</tbody>
</table>

<span id="_Ref502842948" class="anchor"></span>Table 1: TaskMan—ZTREQ Piece and Equivalent REQ^ZTLOAD Variable

Patch Revisions

For the current patch history related to this software, see the Patch Module on FORUM.

Table of Contents

<span id="_Toc207255413" class="anchor"></span>List of Figures

<span id="_Toc207255414" class="anchor"></span>List of Tables

[Table 1: TaskMan—ZTREQ Piece and Equivalent REQ^ZTLOAD Variable [9](#_Ref502842948)](#_Ref502842948)

<span id="_Hlt412359042" class="anchor"></span>Orientation

![](kernel-8-0-developer-s-guide-taskman-user-guide/003.png) REF: For an orientation to this manual, please refer to the “Orientation” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg.pdf#Main_Orientation).

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Overview](#overview)
  - [How to Write Code to Queue Tasks](#how-to-write-code-to-queue-tasks)
    - [Queuers](#queuers)
    - [Tasks](#tasks)
- [Direct Mode Utilities](#direct-mode-utilities)
  - [\>D ^ZTMB: Start TaskMan](#d-ztmb-start-taskman)
  - [\>D RESTART^ZTMB: Restart TaskMan](#d-restartztmb-restart-taskman)
  - [\>D ^ZTMCHK: Check TaskMan’s Environment](#d-ztmchk-check-taskmans-environment)
  - [\>D RUN^ZTMKU: Remove Taskman from WAIT State Option](#d-runztmku-remove-taskman-from-wait-state-option)
  - [\>D STOP^ZTMKU: Stop Task Manager Option](#d-stopztmku-stop-task-manager-option)
  - [\>D WAIT^ZTMKU: Place Taskman in a WAIT State Option](#d-waitztmku-place-taskman-in-a-wait-state-option)
  - [\>D ^ZTMON: Monitor TaskMan Option](#d-ztmon-monitor-taskman-option)
- [Application Programming Interface (API)](#application-programming-interface-api)
  - [TOUCH^XUSCLEAN: Notify Kernel of Tasks that Run 7 Days or Longer](#touchxusclean-notify-kernel-of-tasks-that-run-7-days-or-longer)
  - [\$\$DEV^XUTMDEVQ(): Force Queuing—Ask for Device](#devxutmdevq-force-queuingask-for-device)
    - [Example](#example)
  - [EN^XUTMDEVQ(): Run a Task (Directly or Queued)](#enxutmdevq-run-a-task-directly-or-queued)
    - [Example](#example-1)
  - [\$\$NODEV^XUTMDEVQ(): Force Queuing—No Device Selection](#nodevxutmdevq-force-queuingno-device-selection)
    - [Example](#example-2)
  - [\$\$QQ^XUTMDEVQ(): Double Queue—Direct Queuing in a Single Call](#qqxutmdevq-double-queuedirect-queuing-in-a-single-call)
    - [Example](#example-3)
  - [\$\$REQQ^XUTMDEVQ(): Schedule Second Part of a Task](#reqqxutmdevq-schedule-second-part-of-a-task)
    - [Example](#example-4)
  - [DISP^XUTMOPT(): Display Option Schedule](#dispxutmopt-display-option-schedule)
    - [Example](#example-5)
  - [EDIT^XUTMOPT(): Edit an Option’s Scheduling](#editxutmopt-edit-an-options-scheduling)
  - [OPTSTAT^XUTMOPT(): Obtain Option Schedule](#optstatxutmopt-obtain-option-schedule)
    - [Example](#example-6)
  - [RESCH^XUTMOPT(): Set Up Option Schedule](#reschxutmopt-set-up-option-schedule)
  - [EN^XUTMTP(): Display HL7 Task Information](#enxutmtp-display-hl7-task-information)
  - [^%ZTLOAD: Queue a Task](#ztload-queue-a-task)
    - [Interactive Use of ^%ZTLOAD](#interactive-use-of-ztload)
    - [Non-Interactive Use of ^%ZTLOAD](#non-interactive-use-of-ztload)
    - [Queuing Tasks without an I/O Device](#queuing-tasks-without-an-io-device)
    - [Example](#example-7)
    - [Code Execution](#code-execution)
    - [Output](#output)
  - [\$\$ASKSTOP^%ZTLOAD: Stop TaskMan Task](#askstopztload-stop-taskman-task)
  - [DESC^%ZTLOAD(): Find Tasks with a Description](#descztload-find-tasks-with-a-description)
  - [DQ^%ZTLOAD: Unschedule a Task](#dqztload-unschedule-a-task)
  - [ISQED^%ZTLOAD: Return Task Status](#isqedztload-return-task-status)
  - [\$\$JOB^%ZTLOAD(): Return a Job Number for a Task](#jobztload-return-a-job-number-for-a-task)
  - [KILL^%ZTLOAD: Delete a Task](#killztload-delete-a-task)
  - [OPTION^%ZTLOAD(): Find Tasks for an Option](#optionztload-find-tasks-for-an-option)
  - [PCLEAR^%ZTLOAD(): Clear Persistent Flag for a Task](#pclearztload-clear-persistent-flag-for-a-task)
  - [\$\$PSET^%ZTLOAD(): Set Task as Persistent](#psetztload-set-task-as-persistent)
  - [REQ^%ZTLOAD: Requeue a Task](#reqztload-requeue-a-task)
    - [Example](#example-8)
    - [Code Execution](#code-execution-1)
    - [Output](#output-1)
  - [RTN^%ZTLOAD(): Find Tasks that Call a Routine](#rtnztload-find-tasks-that-call-a-routine)
  - [\$\$S^%ZTLOAD(): Check for Task Stop Request](#sztload-check-for-task-stop-request)
  - [STAT^%ZTLOAD: Task Status](#statztload-task-status)
  - [\$\$TM^%ZTLOAD: Check if TaskMan is Running](#tmztload-check-if-taskman-is-running)
  - [ZTSAVE^%ZTLOAD(): Build ZTSAVE Array](#ztsaveztload-build-ztsave-array)
- [Appendix A—Revision History Archive](#appendix-arevision-history-archive)
The *Kernel 8.0 Developer’s Guide: TaskMan Developer Tools User Guide* is part of the *Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide*.

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The TaskMan API consists of several callable entry points and an extrinsic variable. Use of these calls makes the creation, scheduling, and monitoring of background processing from within applications straightforward.

Developers *must* avoid directly setting information into TaskMan’s globals to queue tasks. In fact, the SAC specifies that TaskMan’s calls be used. The structure of the globals is *not* static; there is no commitment to support their current structure in the future.

![](kernel-8-0-developer-s-guide-taskman-user-guide/004.png) REF: For more information on why and when to use TaskMan to perform queuing, see the “TaskMan System Management: Overview” section in the [*Kernel 8.0 Systems Management: TaskMan User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_taskman_ug.pdf#System_Management_Overview).

## How to Write Code to Queue Tasks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Writing code to queue a task is *not* difficult; however, the coding *must* be done carefully and systematically. If you think of it in two parts, it is easier to write. These two parts are the queuer and the task:

- Queuer—Some code *must* invoke [^%ZTLOAD](#ztload-queue-a-task) to create and schedule the task. This code is the queuer. The most complex part of a queuer is determining which variables *must* be passed on to the task.  
    
  In one type of queuer, the program application makes its own calls to [^%ZTLOAD](#ztload-queue-a-task) to queue tasks. In the other common type of queuer, scheduled options, an option is scheduled to run as a task through the OPTION SCHEDULING (#19.2) file; TaskMan itself takes care of the queuing.
- Task—Some code *must* perform the actual work in the background. Sometimes the task shares code with an equivalent foreground activity. However, remember that a queued task runs under special conditions that *must* be considered. For example, no interactive dialogue with the user is possible.

Usually, both pieces of code should be planned together since they interact heavily.

### Queuers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As mentioned above, there are two common types of queuers:

- Application code that itself acts as the queuer by calling [^%ZTLOAD](#ztload-queue-a-task).
- Options that are scheduled (in which case, TaskMan itself acts as the queuer).

#### Calling ^%ZTLOAD to Create Tasks

One common way to create tasks is to call TaskMan’s main API, [^%ZTLOAD](#ztload-queue-a-task). You can use [^%ZTLOAD](#ztload-queue-a-task) interactively, or *non*-interactively.

![](kernel-8-0-developer-s-guide-taskman-user-guide/005.png) REF: For more information on queuing tasks with [^%ZTLOAD](#ztload-queue-a-task), see the “<u>^%ZTLOAD: Queue a Task</u>” section.

#### Calling EN^XUTMDEVQ to Create Tasks

The [EN^XUTMDEVQ](#enxutmdevq-run-a-task-directly-or-queued) API encapsulates the logic to handle both direct printing and queuing in a single call.

#### Creating Tasks Using Scheduled Options

You can also create options that you ask the sites to schedule on a regular basis. In this case, TaskMan itself (rather than application code) acts as the queuer. Site managers use TaskMan to queue options and can schedule these options to run again and again on some specified schedule.

You should be careful, because this creates a great possibility for confusion. Obviously, some options *cannot* be scheduled, in the same way that some routines *cannot* be queued. When you create options that should be scheduled, you should:

- Indicate whether an option can be scheduled through TaskMan and, if so, the *recommended* frequency of scheduling. Do this using the DESCRIPTION field of the option.
- Indicate the format of data to pass to the scheduled option through the TASK PARAMETERS field, if the option uses such data. Do this using the DESCRIPTION field of the option.
- Set the SCHEDULING RECOMMENDED field of the option to YES. This makes the option show up in a Kernel report that lists all options on the system that should be scheduled.
- Consider using a name for the option that reflects the fact that it is intended to be run only by TaskMan, if you create such an option.
- Give the option a parent (that is attach it to a menu). This prevents the option from being deleted by Kernel’s Delete Unreferenced Options \[XQ UNREF’D OPTIONS\] purge option. If the option *cannot* be used interactively, make sure that it is *not* attached to a menu that is part of a user’s menu tree. Instead, attach it to a menu that is *not* on any user’s menu tree. An example is Kernel’s ZTMQUEUABLE OPTIONS. It is *not* in any user menu tree. If you do *not* want to create your own menu to be a parent of queueable options, you are allowed to attach your option to Kernel’s ZTMQUEUABLE OPTIONS option and export ZTMQUEUABLE OPTIONS through KIDS’ USE AS LINK FOR MENU ITEMS action.

When you create options that queue tasks but that *cannot* be scheduled themselves, you should be especially clear in documenting this so that site managers does *not* try to schedule them.

Queued options differ from other tasks in only a few ways:

- They may have an entry and exit action and may set XQUIT in the entry action to avoid running.
- They can run on a scheduling cycle as defined by the system manager.
- They are designed explicitly for the system manager to use, since the option used to schedule options is available only to system managers.
- They can be better documented than normal tasks because the OPTION (#19) file entry provides a place for a permanent description of the task’s purpose and behavior (the DESCRIPTION field).
- If the option is scheduled regularly, data can be passed to your task from the OPTION SCHEDULING file’s (#19.2) TASK PARAMETERS field; the data is made available to the task at run time in the ZTQPARAM variable. The variable is only defined if an entry is made in the TASK PARAMETERS field when the task is scheduled. The format that is expected of information entered in the TASK PARAMETERS field should be described in the option’s DESCRIPTION field.

You should describe scheduling recommendations and the format, if any, for the TASK PARAMETERS field (as well as in the option’s DESCRIPTION field) in your software application installation guide for all the queueable options, since options are usually set on their schedules shortly after installation.

### Tasks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes information about Tasks. It applies whether the queuer that queued the task was a call to [^%ZTLOAD](#ztload-queue-a-task), or TaskMan itself was running the task because it was scheduled in the OPTION SCHEDULING (#19.2) file.

When you write a task, you create an API that TaskMan can call to perform the work. The submanager calls the API you specify to run the task. The submanager does more than pass your task a few parameters, however; it creates an entire specialized environment for the task, according to your specifications. Then the submanager calls your API, at which point your task begins running. When your task quits, control passes back to the submanager.

The interface between tasks and submanagers determines the special problems you *must* solve and the features you have available to do so. This interface consists of two parts:

- The environment and tools that the submanagers guarantee to the tasks.
- The responsibilities of the tasks themselves.

#### Key Variables and Environment When Task is Running

All VistA processes run in a guaranteed environment, with standard variables and devices available to the software. The guaranteed environment for tasks differs from that of foreground processes in some ways, however. This reflects the differences between the foreground and background, and the special services provided by TaskMan. The submanagers guarantee tasks the following variables and other features:

- DT: While this usually designates the date when a user signs on, here it contains the date when the task first began running (in VA FileMan format, of course).
- DUZ(): The entire DUZ array \[except DUZ(“NEWCODE”)\], as defined at the time of your call to the Program Interface, is always passed to your task. If DUZ was *not* properly set up at that time, then it is set to 0. If DUZ(0) was *not* properly set up, then the submanager attempts to look it up using your DUZ variable; if the lookup fails, it sets DUZ(0)=“”. The submanager does the same thing with DUZ(2).
- IO\*: All IO variables describing the output device that you receive are passed to you. If you request no output device, then IO, IO(0), and ZTIO all equal “”.
- ZTDESC: This contains the free-text description of your task that you passed to the Program Interface.
- ZTDTH: This contains the date and time (in \$HOROLOG format) that you wanted your task to begin running. Because delays from several sources can make your task begin late, this variable may be useful.
- ZTIO: This contains your original output device specifications.
- ZTQUEUED: This variable is always defined when your task begins and is only defined for background tasks. Many queued routines can run either in the foreground or in the background. The only reliable way to determine which situation is currently the case is using the M code:

\>IF \$D(ZTQUEUED)

- ZTRTN: This variable is the API that TaskMan will DO to start the task.
- ZTSK: Every task is passed its internal number so that it can make use of the Program Interface.
- Destination: Using ZTUCI, ZTIO, and ZTCPU, you can request a specific UCI on a specific volume set and CPU node where your task should run. The location you request is where the submanager calls your API. Remember that the SAC does *not* protect the TaskMan namespaced input variables to your task (such as ZTIO, ZTSK, and so on), however. The submanagers guarantee their values to the tasks, but once you begin running, their values may change. For example, the utilities you call may alter these variables, or your own code may. If your task needs to know these values throughout its execution, you should load them into your own namespaced variables, which you can then protect.
- Device: If you request an IO device for your task then, when the task starts, the device is open. The submanager even issues the USE command for you and after your task completes, it properly closes the device for you. If you leave it open when you are finished with it, the submanager can recycle the device more efficiently for use with other tasks.
- Error Trap: The submanager always sets an Error Trap before calling your task. This way, if your task errors out, the submanager can record that fact in the system error log, in TaskMan’s error log, and in the entry for your task in the TASKS (#14.4) file.
- Priority: Your task begins running with the priority specified if you request one.
- Saved Variables: The submanager passes any variables that the queuer saved using ZTSAVE. These act as input variables.
- Tools: The task can rely upon the following tools to assist it in meeting its responsibilities (as described below):
- [\$\$S^%ZTLOAD](#sztload-check-for-task-stop-request)
- ZTSTOP
- ZTQUEUED
- ZTREQ
- [KILL^%ZTLOAD](#killztload-delete-a-task)
- [^%ZTLOAD](#ztload-queue-a-task)
- Device Handler
- Resource devices
- SYNC FLAGs

#### Checking for Stop Requests

You should write tasks in such a way that your tasks honor stop requests. Since Kernel 7.0, users have been able to call the TaskMan User option to stop tasks that they started. A task should periodically check whether it has been asked to stop and should gracefully shut down when asked. This involves four steps:

1.  To check for a stop request, the task can execute the following code:

\>IF \$\$S^%ZTLOAD

If this evaluates to TRUE, the user has asked the task to stop. This check should occur periodically throughout the task; *not* so often as to increase significantly the task’s CPU usage, but often enough that the response time satisfies the users. For example, a report printout might check once per page, while a massive data compilation might check once every hundred or even thousand records. Very short tasks can choose *not* to check at all.

2.  The task may need to perform some internal flagging or cleanup. Stop requests from a user rarely come at ideal moments in the overall algorithm of the task, and the task may need to perform some work to prepare to quit.
3.  The task needs to notify the submanager that it responded to the user’s request to stop, so that the submanager can notify the user. The task should use the following code to do so:

\>SET ZTSTOP=1

The ZTSTOP flag is processed by the submanager when the task quits. Do *not*KILL this variable if you wish to pass it back to the submanager.

4.  The task should then quit. Depending on how deeply within loops these stop request checks are made, it may take some processing to work out of all loops and quit on short notice. The code may need to be adjusted to allow for this kind of exit.

In the end, checking for stop requests benefits *not* only the developer, by satisfying your users, but also the users themselves by making them feel more in control, and the system managers by freeing them up from stopping tasks for users.

#### Purging the Task Record

According to the SAC, tasks have a responsibility to remove their own records from the TASKS (#14.4) file when they complete. This serves two purposes. First, it helps keep the TASKS (#14.4) file small, which makes TaskMan more efficient. Second, because any tasks that cause errors never reaches the final commands to delete the task’s record, such tasks remain in the TASKS (#14.4) file after they complete. This greatly assists system management staff in identifying and troubleshooting problem tasks.

You have two methods to delete TASKS (#14.4) file entries:

- ZTREQ output variable
- [KILL^%ZTLOAD](#killztload-delete-a-task) API

The *recommended* method, simpler than the other, is to use the ZTREQ output variable to instruct the submanager to delete your task’s record after it finishes running. Do this with the following line of M code:

\>S ZTREQ="@"

Because the submanager does *not* get this variable back until after your task quits, you can set ZTREQ anywhere within the task and still ensure your task does *not* delete its record if it errors out.

![](kernel-8-0-developer-s-guide-taskman-user-guide/006.png) NOTE: If you KILL off the variable before the task quits, the submanager does *not* delete your task.

The other method is to call [KILL^%ZTLOAD](#killztload-delete-a-task) to delete the task’s record. This solution has two disadvantages:

- First, the ZTSK input variable to [KILL^%ZTLOAD](#killztload-delete-a-task) needs to equal the task number of the task to delete, which may *not* be the case if the task has called other utilities. The task can solve this problem by saving off ZTSK at the beginning and restoring it prior to calling [KILL^%ZTLOAD](#killztload-delete-a-task).
- Second, you *must* place the call at the end of the task, just prior to quitting, ensuring the record remains if the task encounters an error. This causes problems for tasks that lack a single exit point, but you can solve this by writing a new API for the task that does the main body of the task, performs the deletion, and then quits.

#### Checking For Background Execution: ZTQUEUED

When you share code for both foreground and background processing, you often need the code to behave differently under the two situations. The only reliable way to test whether the code is running in the background is to check if the ZTQUEUED variable is defined. It is only defined if the current running job is a task. You can check for its existence, and therefore, whether the code is truly running in the background, with the following M statement:

\>IF \$D(ZTQUEUED)

#### Post-Execution Commands: ZTREQ

Tasks can make the submanager execute a certain limited set of commands after the tasks complete. Use the ZTREQ output variable to describe these post-execution commands.

The use of ZTREQ to delete a task’s record has already been discussed above. ZTREQ can also be used to edit and/or reschedule the task.

- To reschedule the task to run again immediately:

\>S ZTREQ=""

- To requeue a modified version of your task:

Use ZTREQ to specify how to modify the existing task to run again. By optionally setting any of the various ^-pieces of ZTREQ, you can modify that aspect of how the rescheduled task runs. The purpose and format of each ^-piece roughly corresponds to the input variables of [REQ^%ZTLOAD](#reqztload-requeue-a-task) listed in <u>Table 1</u>:

| ZTREQ Piece | Equivalent REQ^%ZTLOAD Variable |
|-------------|---------------------------------|
| 1           | ZTDTH                       |
| 2           | ZTIO                        |
| 3           | ZTDESC                      |
| 4^5         | ZTRTN                       |

All of these ^-pieces in ZTREQ are optional; only set the pieces that affect parameters you want to change. However, in the case of leaving piece 2NULL, the task uses the same device that your task initially requested, which is *not* necessarily the device that it got. To reschedule the task to run on the device your task currently has, you *must* build up the ZTIO value using your IO variables.

- To edit the task without rescheduling it:

Set ^-piece 1 to @ and set the other pieces to the values you want. This is equivalent to setting ZTDTH=“@”, as described in the <u>REQ^%ZTLOAD: Requeue a Task</u> API. Remember, however, to include at least one caret (^) in ZTREQ to do this, since if ZTREQ=“@” the task is deleted.

Remember that ZTREQ is *not* an input parameter that you pass to the submanager; it is an output parameter from your task. The submanager does its best to honor your request, but if the request is impossible, then there is no way for you to find out. For example, if you specify that the submanager should requeue your task, then it attempts to do so; if it finds that your task has been deleted, there is no way for the submanager to let you know. When the submanager *cannot* honor your request, it ignores it.

#### Calling ^%ZTLOAD within a Task

Tasks can use all standard TaskMan API calls. There is no reason a task should *not* itself call the TaskMan API to do requeuing, deletion, or any of the other standard calls. The only way such calls are special is that they have many of the variables they need to pass already defined for them by the submanager.

You should be careful to avoid interference from these pre-defined variables; sometimes the submanager passes you the value you need for the API call, but sometimes you need a different one. For example, from within a task that has an IO device, to call [^%ZTLOAD](#ztload-queue-a-task) to queue a task without an IO device, you should set ZTIO to “”, because the input variable passed in by the submanager may still be defined. With a little care, these kinds of problems can easily be anticipated and prevented.

#### Calling the Device Handler (^%ZIS) within a Task

The main Device Handler API ([^%ZIS](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_device_handler_ug.pdf#zis)) by itself is *not* designed to open more than one I/O device beyond the already-open home device. Within a task, you are free to open one additional device (beyond the home device) using [^%ZIS](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_device_handler_ug.pdf#zis). If you need to open more than one device concurrently within a task, however, you should use Kernel’s multiple device APIs (that is [OPEN^%ZISUTL](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_device_handler_ug.pdf#open_zisutl), [USE^%ZISUTL](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_device_handler_ug.pdf#use_zisutl), and [CLOSE^%ZISUTL](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_device_handler_ug.pdf#close_zisutl)).

#### Long Running Tasks—Writing Two-step Tasks

A situation you should always consider is how to deal with jobs that take a long time to gather data and then print a report of that data. If you write this as a *single* job that *both* gathers and prints data, any requested IO device that is eventually used to print that data sits idle for a long period of time. Thus, the IO device is unused and unavailable to any other tasks during that entire period it takes to gather the data for your report.

If you write the task to start without a device, and to call the [^%ZIS](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_device_handler_ug.pdf#zis) API to open the device when the report is ready, two different problems occur:

1.  First, if the device is heavily used by tasks, then this task may never get a chance to open the device; TaskMan keeps it busy with other tasks.
5.  Second, if the task does manage somehow to grab the device away from TaskMan, it interferes with the fair distribution of resources, potentially running ahead of other tasks that have been waiting longer.

One way around this problem is to queue the task to a spool device. Spool devices are always available, which solves the problem of tying up a device. However, some system managers discourage use of spoolers, because of the possibility for disk crashes resulting from users who send excessively large reports to the spooler.

Therefore, the best solution to this problem involves splitting the job into two separate tasks:

1.  Gather—The first task runs without a device, gathers and generates the report data in the ^XTMP global, and schedules the second task (Print).
6.  Print—The second task runs with the IO device and prints the report data generated by the first task (Gather).

To perform these two separate but associated tasks, Kernel provides the following APIs:

- <u>\$\$QQ^XUTMDEVQ(): Double Queue—Direct Queuing in a Single Call</u>—This API creates the Gather and the Print tasks. The gather task is scheduled to run, while the print task is *not* scheduled.
- <u>\$\$REQQ^XUTMDEVQ(): Schedule Second Part of a Task</u>—At the end of the Gather task, it invokes the \$\$REQQ^XUTMDEVQ API to schedule the Print task.

#### Long Running Tasks—Using ^%ZIS

As an alternative to splitting the job into two separate tasks an interactive call can be made to [^%ZIS](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_device_handler_ug.pdf#zis) to allow the user to select the output device without opening it. The gather data portion of the job can then proceed without tying up the output device. When the job is ready to print it can open the output device using the variables that were saved when the [^%ZIS](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_device_handler_ug.pdf#zis) device selection call was made.

To allow for selection of the output device without opening it make sure the [^%ZIS](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_device_handler_ug.pdf#zis) input variable %ZIS contains N.

Some of the variables returned by the device selection call to [^%ZIS](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_device_handler_ug.pdf#zis) need to be saved for use when the device open call is made. These include:

- IO
- IO(“DOC”)
- IOM
- ION
- IOSL

If IO(“Q”) is 1 queuing has been selected, and your code should handle that and take care of the queuing.

The code excerpt in <u>Figure 1</u> shows the basic structure for allowing the user to select whether a job is queued or *not* and the output device to use.

<span id="_Ref502843465" class="anchor"></span>Figure 1: TaskMan—Sample Code Allowing Users to Select whether a Job is Queued or Not and the Output Device to Use

N POP,%ZIS

S %ZIS="NQ"

W !

D ^%ZIS

I POP G EXIT

I ION=("HOST FILE SERVER")!(ION="P-MESSAGE-HFS") S SAVEHFIO=IO

S SAVEIOP=ION\_";"\_\$G(IOST)\_";"\_\$G(IO("DOC"))\_";"\_\$G(IOM)\_";"\_\$G(IOSL)

;

I IO("Q") D Q

.;Queue the report.

.;If ZTIO is not explicitly set to null then %ZTLOAD will open

.;the device.

. S ZTIO=""

.

.

.

. D ^%ZTLOAD

.

.

.

I 'IO("Q") D Q

.;Run the report.

.

.

.

When it is time to print, the output device can be opened using the variables that were saved, as shown in <u>Figure 2</u>.

<span id="_Ref502843507" class="anchor"></span>Figure 2: TaskMan—Sample Code Printing to a Device Using Saved Variables

N IOP,POP,VDUZ,XMDUZ,XMQUIET,XMSUB,XMY,%ZIS

;Check for output to p-message. TaskMan will automatically copy

;^TMP("XM-MESS",\$J) to the tasked job.

I \$D(^TMP("XM-MESS",\$J)) D

. S XMQUIET=1

. S XMDUZ=\$G(^TMP("XM-MESS",\$J,"XMHOST","XMINSTR","FROM"))

. I XMDUZ="" S XMDUZ=^TMP("XM-MESS",\$J,"XMHOST","XMDUZ")

. S XMSUB=^TMP("XM-MESS",\$J,"XMHOST","XMSUB")

. S VDUZ=""

. F S VDUZ=\$O(^TMP("XM-MESS",\$J,"XMY",VDUZ)) Q:VDUZ="" S XMY(VDUZ)=""

. I \$D(XMY(DUZ)),\$D(^TMP("XM-MESS",\$J,"XMHOST","XMINSTR","SELF BSKT")

) S XMY(DUZ,0)=^TMP("XM-MESS",\$J,"XMHOST","XMINSTR","SELF BSKT")

S IOP=SAVEIOP

I \$D(SAVEHFIO) S %ZIS("HFSNAME")=SAVEHFIO

D ^%ZIS

I POP G EXIT

U IO

If p-message was selected then ^TMP(“XM-MESS”,\$J) is defined and contains all the information required to deliver the message. Setting XMQUIET=1 stops interactive processing by MailMan. XMDUZ is the sender and XMSUB is the subject. The VDUZ loop is the list of people to which the user has chosen to send the message. Finally, the check for “SELF BSKT” is to determine if the user has selected a particular basket to which the message is to be delivered.

#### Using SYNC FLAGs to Control Sequences of Tasks

You can use SYNC FLAGs together with resource type devices when queuing through [^%ZTLOAD](#ztload-queue-a-task), as a mechanism to ensure sequential processing of a series of tasks. The mechanism also ensures that subsequent tasks in the series do *not* run if a previous task errors out or completes unsuccessfully.

A SYNC FLAG is a unique, arbitrary FREE TEXT name you use as an identifying flag. You use SYNC FLAGs in conjunction with resource devices; when paired with a particular resource device, the pairing is called a SYNC FLAG pair.

The SYNC FLAG pair ties all tasks that have requested the same SYNC FLAG and the same resource together. If a task in a group of tasks is running, all other tasks queued with the same SYNC FLAG pair must wait until the running task has completed. If one task in the series does *not* finish successfully, then all other tasks using the same SYNC FLAG pair waits.

To build a series of tasks, you need to choose a resource device and queue the entire series of tasks in the same order that they should run, through [^%ZTLOAD](#ztload-queue-a-task). Use the ZTIO variable to queue all tasks in the series to the same resource device. Use the ZTSYNC parameter to use the same SYNC FLAG for each task in the series. TaskMan then runs the series of tasks in the same order that they were queued.

The SYNC FLAG pair uniquely identifies one group of tasks using one resource device. TaskMan builds a SYNC FLAG pair by concatenating the requested resource (from the [^%ZTLOAD](#ztload-queue-a-task) ZTIO input variable) with the name of the SYNC FLAG (from the [^%ZTLOAD](#ztload-queue-a-task) ZTSYNC input variable).

In any given task in the series of tasks, you indicate that the task completed successfully by KILLing the ZTSTAT variable or setting it to 0. Otherwise, no subsequent tasks can run.

The following describes how using SYNC FLAG pairs ensures sequential processing of a series of tasks:

1.  When a task is queued through [^%ZTLOAD](#ztload-queue-a-task), if the ZTSYNC is defined, then the SYNC FLAG defined by ZTSYNC is saved with that task.
7.  When TaskMan is ready to start the task, after it can allocate the resource device to which it was queued, it checks whether the SYNC FLAG pair (Resource_SYNC FLAG) exists in the TASK SYNC FLAG (#14.8) file.
8.  If the SYNC FLAG pair does *not* exist in the TASK SYNC FLAG (#14.8) file, TaskMan creates an entry for the SYNC FLAG pair in the TASK SYNC FLAG (#14.8) file and starts the task.

If, on the other hand, the SYNC FLAG pair already exists in the TASK SYNC FLAG (#14.8) file, then any task requiring the same SYNC FLAG must wait until the corresponding entry in the TASK SYNC FLAG (#14.8) file is deleted.

9.  If the task was able to start, the variable ZTSTAT is set to 1 in the running task.
- To indicate success (such as that the series of tasks should continue), you *must*KILLZTSTAT or set it to Zero. In this case, when your task completes, the SYNC FLAG pair for that task is cleared.
- To indicate failure (such as that the series of tasks should *not* continue) leave ZTSTAT set to 1.
10. When the task completes, TaskMan checks to see the value of ZTSTAT.
- If ZTSTAT is set to Zero (0) or *not* defined, TaskMan deletes the SYNC FLAG pair entry in the TASK SYNC FLAG (#14.8) file. This allows any future tasks in the series to run.
- If, on the other hand, ZTSTAT is left with a positive value, the task is assumed to have had some kind of error. In this case, the value of ZTSTAT is saved in the STATUS field of the SYNC FLAG pair entry, and the entry in the TASK SYNC FLAG (#14.8) file is *not* deleted. Subsequent jobs in the series are prevented from running.

If the task errors are out, the SYNC FLAG pair entry is also left in the TASK SYNC FLAG (#14.8) file, preventing subsequent jobs in the series from running. TaskMan puts a message in the STATUS field, saying that the task stopped due to an error.

# Direct Mode Utilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can use TaskMan’s direct mode utilities from both the Manager and Production UCIs. Developers *cannot* call them from applications, however.

## \>D ^ZTMB: Start TaskMan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ^ZTMB utility can be used to start TaskMan for the first time since system startup. As part of this startup, any tasks scheduled to begin at system startup are fired off.

## \>D RESTART^ZTMB: Restart TaskMan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RESTART^ZTMB utility restarts TaskMan. RESTART^ZTMB, unlike ^ZTMB, does *not* fire off the startup tasks and should be used whenever the startup tasks have already been initiated. The Restart Task Manager \[XUTM RESTART\] option uses this entry point.

## \>D ^ZTMCHK: Check TaskMan’s Environment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ^ZTMCHK utility provides the same functionality as the Check Taskman’s Environment \[XUTM CHECK ENV\] option but from Programmer mode.

## \>D RUN^ZTMKU: Remove Taskman from WAIT State Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The RUN^ZTMKU utility provides the same functionality as the Remove Taskman from WAIT State \[XUTM RUN\] option but from Programmer mode.

## \>D STOP^ZTMKU: Stop Task Manager Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The STOP^ZTMKU utility provides the same functionality as the Stop Task Manager \[XUTM STOP\] option but from Programmer mode.

## \>D WAIT^ZTMKU: Place Taskman in a WAIT State Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The WAIT^ZTMKU utility provides the same functionality as the Place Taskman in a WAIT State \[XUTM WAIT\] option but from Programmer mode.

## \>D ^ZTMON: Monitor TaskMan Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ^ZTMON utility provides the same functionality as the Monitor Taskman \[XUTM ZTMON\] option but from Programmer mode.

# Application Programming Interface (API)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Several TaskMan APIs and Extrinsic Functions are available for developers. These APIs and Extrinsic Functions are described below.

## TOUCH^XUSCLEAN: Notify Kernel of Tasks that Run 7 Days or Longer

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: TaskMan

ICR \#: 10052

Description: The TOUCH^XUSCLEAN API notifies Kernel of any tasks that run 7 days or longer. If a task appears to have been running longer than 7 days, Kernel assumes that it really is *not* running anymore and KILLs off its temp global and user stack.

If your task legitimately runs more than 7 days, your task should call the TOUCH^XUSCLEAN API once a day to notify Kernel. This API sets:

^XUTL(“XQ”,\$J,“KEEPALIVE”)=\$H

- If Kernel sees this node, and \$H is less than 7 days ago, Kernel leaves your task alone, unless it determines that your task is dead.
- If \$H is more than 7 days ago, Kernel assumes your task is dead and KILLs the temp global and user stack for that task.

There are no inputs or outputs to this API.

Format: TOUCH^XUSCLEAN

Input Parameters: none.

Output: none.

## \$\$DEV^XUTMDEVQ(): Force Queuing—Ask for Device

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: TaskMan

ICR \#: 1519

Description: The \$\$DEV^XUTMDEVQ extrinsic function encapsulates the logic to handle direct (FORCED) queuing in a single call and ask users for a device.

![](kernel-8-0-developer-s-guide-taskman-user-guide/007.png) NOTE: This API was released with Kernel Patch XU\*8.0\*275.

Format: \$\$DEV^XUTMDEVQ(ztrtn\[,ztdesc\]\[,%var\]\[,%voth\]\[,%zis\]\[,iop\]  
\[,%wr\])

Input Parameters: ztrtn: (required) The API that TaskMan will DO to start the task (job). You can specify it as any of the following:

- “LABEL^ROUTINE”
- “^ROUTINE”
- “ROUTINE”

ztdesc: (optional) Task description, up to 200 characters describing the task, with the software application name at the front. Default to name of \[tag\]^routine.

%var: (optional) ZTSAVE values for the task. Single value or passed by reference, this is used to S ZTSAVE(). It can be a string of variable names separated by “;”. Each ;-piece is used as a subscript in ZTSAVE.

%voth: (optional) Passed by reference, %VOTH(SUB)=“” or explicit value sub—this is any other [^%ZTLOAD](#ztload-queue-a-task) variable besides ZTRTN, ZTDESC, ZTIO, and ZTSAVE. For example:

%VOTH("ZTDTH")=\$H%zis: (optional) Default value MQ. Passed by reference, standard %ZIS variable array for calling the Device Handler.

iop: (optional) The IOP variable as defined in Kernel’s Device Handler.

%wr: (optional) If %WR\>0 then write text to the screen as to whether the queuing was successful.

Output: returns: Returns:

- 0—If run ZTRTN without queuing.
- -1—If unsuccessful device call or failed the [^%ZTLOAD](#ztload-queue-a-task) call.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The example in <u>Figure 3</u> is a job that consists of gathering information and then printing it. Assume that the gathering takes a few hours. You do *not* want the device that the user selects to be tied up for that time, so you divide the job into two tasks:

1.  Task 1: Gathers the information.
11. Task 2: Prints information.

Use the following APIs:

1.  \$\$DEV^XUTMDEVQ API—To select the device and queue up the print task.
12. <u>\$\$NODEV^XUTMDEVQ(): Force Queuing—No Device Selection</u> API—To schedule the gather task.
13. <u>REQ^%ZTLOAD: Requeue a Task</u> API—To schedule the print task when the gather task finishes.

![](kernel-8-0-developer-s-guide-taskman-user-guide/008.png) NOTE: You can also use the <u>\$\$REQQ^XUTMDEVQ(): Schedule Second Part of a Task</u> API to schedule the print task.

<span id="_Ref502765943" class="anchor"></span>Figure 3: \$\$DEV^XUTMDEVQ API—Example: Sample Code

ARHBQQ ;SFVAMC/GB - Demo of 'gather' and 'print' in 2 tasks ;1/19/06 08:31

;;1.1

DEV ;

N ARH,ARHZTSK,X

;The user doesn't know it, but he's actually queuing the second task,

;the "print" portion of the job. The only question the user will be

;asked is to select the device.

S ARH("ZTDTH")="@" ;Don't schedule the task to run, we'll do it later.

;In the following, the "Q" sets IOP=Q, which forces queuing.

S X=\$\$DEV^XUTMDEVQ("PRINT^ARHBQQ","ARHB Print",,.ARH,,"Q",1)

W !,"X=",X

Q:X\<1

N ARH

;Now queue the first task, the "gather" portion of the job. The user

;won't be asked any questions.

S ARHZTSK=X ; Save the ZTSK number of the "print" task.

S ARH("ZTDTH")=\$H ; Force the task to start now.

;To ask the user the start time, comment out the above line.

S X=\$\$NODEV^XUTMDEVQ("GATHER^ARHBQQ","ARHB Gather","ARHZTSK",.ARH,1)

W !,"X=",X

Q

## EN^XUTMDEVQ(): Run a Task (Directly or Queued)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: TaskMan

ICR \#: 1519

Description: The EN^XUTMDEVQ API encapsulates the logic to handle both direct printing and queuing in a single call.

EN^XUTMDEVQ calls [^%ZIS](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_device_handler_ug.pdf#zis) to query the user for device selection. The user can choose a device on which to run the job directly or choose to queue the job.

After calling [^%ZIS](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_device_handler_ug.pdf#zis), EN^XUTMDEVQ looks to see if the queuing was chosen. If so, EN^XUTMDEVQ uses the values from the ztrtn, ztdesc, and ztsave input parameters to queue the job to the chosen device. If the user did *not* choose to queue, EN^XUTMDEVQ runs the job directly using the ztrtn input parameter. Thus, EN^XUTMDEVQ provides a simple way to facilitate both queuing and running a job directly.

If the IOP variable is defined before calling EN^XUTMDEVQ, it has the same effect as it does if defined before a [^%ZIS](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_device_handler_ug.pdf#zis) call.

If the ZTPRI or ZTKIL variables are defined before calling EN^XUTMDEVQ, they has the same effect as they do if defined before an [^%ZTLOAD](#ztload-queue-a-task) call. Other [^%ZTLOAD](#ztload-queue-a-task) input variables have no effect, however.

You do *not* need to “USE IO” in the routine specified in the ztrtn input parameter; IO is the current device, whether the job is queued or run directly. Also, you do *not* need to pass Q in the top-level of the %ZIS input array; if the top-level of the array does *not* contain Q; Q is appended to it (to allow queuing).

Format: EN^XUTMDEVQ(ztrtn,ztdesc,.ztsave\[,.%zis\]\[,retztsk\])

Input Parameters: ztrtn: (required) The API that TaskMan will DO to start the task. You can specify it as any of the following:

- “LABEL^ROUTINE”
- “^ROUTINE”
- “ROUTINE”

ztdesc: (required) Task description, up to 200 characters describing the task, with the software application name at the front.

.ztsave: (required) Pass by reference. Set up this array in the same format as the ztsave input array is set up for the [^%ZTLOAD](#ztload-queue-a-task) TaskMan API. The array you set up in ztsave is passed directly as ztsave to TaskMan if the user chooses to queue the job.

.%zis: (optional) Pass by reference. String containing input specifications for the Device Handler. Set up the array in the same way as the %ZIS array is set up for the [^%ZIS](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_device_handler_ug.pdf#zis) API. The array you set up in the %zis input parameter is passed directly as %ZIS to the Device Handler.

All %ZIS subscripts from the regular [^%ZIS](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_device_handler_ug.pdf#zis) call (“A”, “B”, “HFSMODE”, and so on) can be passed in the %ZIS input array.

retztsk: (optional) This is the return task number (that is ZTSK). Put a number in this parameter, such that \$G(RETZTSK), then ZTSK exists as an output variable. Otherwise, ZTSK does *not* exist as an output variable.

Output Variable: ZTSK: If a number is entered in the retztsk input parameter, the task number assigned to a task is returned.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In this example (<u>Figure 4</u>), when calling the EN^XUTMDEVQ API the following inputs are used:

- Ztrtn input parameter = <span class="mark">P^ZZYZOPT</span>
- ztdesc input parameter = <span class="mark">Print from BUILD File</span>
- .ztsave input parameter =<span class="mark">.ZTSAVE</span>

![](kernel-8-0-developer-s-guide-taskman-user-guide/009.png) NOTE: This example did not pass in the optional .%zis and retztsk input parameters.

<span id="_Ref173240674" class="anchor"></span>Figure 4: EN^XUTMDEVQ API—Sample Report

ZZYZOPT ;ISC-SF/doc

;;1.0;;

EN ;

N ZZEN K X,DIC S DIC=9.6,DIC(0)="AEMO" D ^DIC

Q:+Y'\>0 S ZZEN=+Y

;

K ZTSAVE S ZTSAVE("ZZEN")=""

<span class="mark">D EN^XUTMDEVQ("P^ZZYZOPT","Print from BUILD File",.ZTSAVE)</span>

Q

P ;

; code for printout

;

W !,"Here goes the body of the report!"

W !,"ZZEN = ",ZZEN

Q

## \$\$NODEV^XUTMDEVQ(): Force Queuing—No Device Selection

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: TaskMan

ICR \#: 1519

Description: The \$\$NODEV^XUTMDEVQ extrinsic function encapsulates the logic to handle direct (FORCED) queuing in a single call and does *not* ask users for a device.

![](kernel-8-0-developer-s-guide-taskman-user-guide/010.png) NOTE: This API was released with Kernel Patch XU\*8.0\*275.

Format: \$\$NO DEV^XUTMDEVQ(ztrtn\[,ztdesc\]\[,%var\]\[,%voth\]\[,%wr\])

Input Parameters: ztrtn: (required) The API that TaskMan will DO to start the task (job). You can specify it as any of the following:

- “LABEL^ROUTINE”
- “^ROUTINE”
- “ROUTINE”

ztdesc: (optional) Task description, up to 200 characters describing the task, with the software application name at the front. Default to name of \[tag\]^routine.

%var: (optional) ZTSAVE values for the task. Single value or passed by reference, this is used to S ZTSAVE(). It can be a string of variable names separated by “;”. Each ;-piece is used as a subscript in ZTSAVE.

%voth: (optional) Passed by reference, %VOTH(SUB)=“” or explicit value sub—this is any other [^%ZTLOAD](#ztload-queue-a-task) variable besides ZTRTN, ZTDESC, ZTIO, and ZTSAVE. For example:

%VOTH("ZTDTH")=\$H

%wr: (optional) If %WR\>0 then write text to the screen as to whether the queuing was successful.

Output: returns: Returns:

- \> 0—Successful; Task \# (number of the job).
- -1—Unsuccessful; If failed, the [^%ZTLOAD](#ztload-queue-a-task) call.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The example in <u>Figure 5</u> is a job that consists of gathering information and then printing it. Assume that the gathering takes a few hours. You do *not* want the device that the user selects to be tied up for that time, so you divide the job into two tasks:

1.  Task 1: Gathers the information.
14. Task 2: Prints information.

Use the following APIs:

1.  <u>\$\$DEV^XUTMDEVQ(): Force Queuing—Ask for Device</u> API—To select the device and queue up the print task.
15. \$\$NODEV^XUTMDEVQ API—To schedule the gather task.
16. <u>REQ^%ZTLOAD: Requeue a Task</u> API—To schedule the print task when the gather task finishes.

![](kernel-8-0-developer-s-guide-taskman-user-guide/011.png) NOTE: You could also use the <u>\$\$REQQ^XUTMDEVQ(): Schedule Second Part of a Task</u> API to schedule the print task.

<span id="_Ref500336605" class="anchor"></span>Figure 5: \$\$NODEV^XUTMDEVQ API—Sample Code

ARHBQQ ;SFVAMC/GB - Demo of 'gather' and 'print' in 2 tasks ;1/19/06 08:31

;;1.1

DEV ;

N ARH,ARHZTSK,X

;The user doesn't know it, but he's actually queuing the second task,

;the "print" portion of the job. The only question the user will be

;asked is to select the device.

S ARH("ZTDTH")="@" ;Don't schedule the task to run, we'll do it later.

;In the following, the "Q" sets IOP=Q, which forces queuing.

S X=\$\$DEV^XUTMDEVQ("PRINT^ARHBQQ","ARHB Print",,.ARH,,"Q",1)

W !,"X=",X

Q:X\<1

N ARH

;Now queue the first task, the "gather" portion of the job. The user

;won't be asked any questions.

S ARHZTSK=X ; Save the ZTSK number of the "print" task.

S ARH("ZTDTH")=\$H ; Force the task to start now.

;To ask the user the start time, comment out the above line.

S X=\$\$NODEV^XUTMDEVQ("GATHER^ARHBQQ","ARHB Gather","ARHZTSK",.ARH,1)

W !,"X=",X

Q

## \$\$QQ^XUTMDEVQ(): Double Queue—Direct Queuing in a Single Call

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: TaskMan

ICR \#: 1519

Description: The \$\$QQ^XUTMDEVQ extrinsic function encapsulates the logic to handle direct queuing in a single call. This extrinsic function does a double queuing:

- Queue up the second task to a device, but do *not* schedule the task in TaskMan.
- Queue up the first task to ZTIO=“” and schedule it.

If it takes a long time to gather and print data, users should split the job into two tasks:

1.  Gather Data—The first task gathers the data.
17. Print Data—The second task prints the data.

Separating the data-gathering task from the data print task helps avoid unnecessarily tying up a printer while large amounts of data are gathered.

The task number of the second task (that is print data) is added to the saved variables with the name XUTMQQ. This makes it easier to schedule the second task when the first task (that is gather data) has finished.

To schedule the second task to run at the end of the first task, you *must* call the <u>\$\$REQQ^XUTMDEVQ(): Schedule Second Part of a Task</u> API.

![](kernel-8-0-developer-s-guide-taskman-user-guide/012.png) NOTE: This API was released with Kernel Patches XU\*8.0\*275 and updated with Kernel Patch XU\*8.0\*389.

Format: \$\$QQ^XUTMDEVQ(%rtn\[,%desc\]\[,%var1\]\[,%voth1\]\[,%zis\]\[,iop\]\[,%wr\],%rtn2\[,%desc2\]\[,%var2\]\[,%voth2\])

Input Parameters: %rtn: (required) First task that TaskMan runs, usually a search and build sorted data type process (that is gather data). The API that TaskMan will DO to start the task. You can specify it as any of the following:

- “LABEL^ROUTINE”
- “^ROUTINE”
- “ROUTINE”

The \[tag\]^routine that TaskMan runs.

%desc: (optional) First task description, up to 200 characters describing the task, with the software application name at the front. Defaults to name of \[tag\]^routine.

%var1: (optional) ZTSAVE values for the first task. Single value or passed by reference, this is used to SET ZTSAVE(). It can be a string of variable names separated by “;”. Each ;-piece is used as a subscript in ZTSAVE.

%voth1: (optional) First task other parameter. Passed by reference, %voth(sub)=“” or explicit value sub—this is any other %ZTLOAD variable besides ZTRTN, ZTDESC, ZTIO, and ZTSAVE. For example:

%VOTH("ZTDTH")=\$H%zis: (optional) Default value MQ. Passed by reference, standard %ZIS variable array for calling the Device Handler. Except for one difference, the second task of the job is tasked to this device call.

Exception:

- IF \$D(%ZIS)=0 then default value is MQ and call the Device Handler.
- IF \$D(%ZIS)=1,%ZIS=“” then queue the second task also with ZTIO=“” (that is do *not* do the Device Handler call).

iop: (optional) The IOP variable as defined in Kernel’s Device Handler. Default value Q—if IOP is passed and IOP does *not* start with Q; then Q; is added.

%wr: (optional) If %WR\>0 then write text to the screen as to whether the queuing was successful.

%rtn2: (required) Second task that TaskMan runs, usually a print process (that is print data).The API that TaskMan will DO to start the task. You can specify it as any of the following:

- “LABEL^ROUTINE”
- “^ROUTINE”
- “ROUTINE”%desc2: (optional) Second task description, up to 200 characters describing the task, with the software application name at the front. Default to name of \[tag\]^routine.

%var2: (optional) ZTSAVE values for the second task. Single value or passed by reference, this is used to S ZTSAVE(). It can be a string of variable names separated by “;”. Each ;-piece is used as a subscript in ZTSAVE.

- If %var1 is *not* passed and \$D(%VAR), then also send %VAR data to the second task.
- If \$D(%VAR1), then do *not* send %VAR data to the second task.

%voth2: (optional) Second task other parameter, usually *not* needed. Passed by reference, %voth(sub)=“” or explicit value sub—this is any other %ZTLOAD variable besides ZTRTN, ZTDESC, ZTIO, and ZTSAVE. For example:

%VOTH("ZTDTH")=\$H

![](kernel-8-0-developer-s-guide-taskman-user-guide/013.png) NOTE: If %voth1(“ZTDTH”) is passed, it is ignored as it is necessary to S ZTDTH=“@” for the second task—this creates the task but does *not* schedule it.

Output: ztsk1^ztsk2: Returns:

- ztsk1^ztsk2—If successfully queued:
- ztsk1 = ZTSK value of first task.
- ztsk2 = ZTSK value of second task.
- -1—If unsuccessful device call or failed %ZTLOAD call.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The example in <u>Figure 6</u> is a job that consists of gathering information and then printing it. Assume that the gathering takes a few hours. You do *not* want the device that the user selects to be tied up for that time, so you divide the job into two tasks. The first task gathers the information, and the second task prints it. Use the \$\$QQ^XUTMDEVQ API to select the device, schedule the gather task, and queue the print task. Use the <u>\$\$REQQ^XUTMDEVQ(): Schedule Second Part of a Task</u> API to schedule the print task when the gather task finishes.

![](kernel-8-0-developer-s-guide-taskman-user-guide/014.png) NOTE: This is the easiest way to divide a job into two tasks.

<span id="_Ref502648864" class="anchor"></span>Figure 6: \$\$QQ^XUTMDEVQ API—Sample Code

ARHBQQ ;SFVAMC/GB - Demo of 'gather' and 'print' in 2 tasks ;1/19/06 08:31

;;1.1

QQ ;

N X

S X=\$\$QQ^XUTMDEVQ("GATHERQ^ARHBQQ","ARHB Gather",,,,,1,"PRINTQ^ARHBQQ","ARHB Print")

W !,"X=",X

Q

GATHERQ ;

N ARHJ,X

S ZTREQ="@"

S ARHJ="ARHB-QQ"\_"-"\_\$J\_"-"\_\$H ; namespace + unique ID

K ^XTMP(ARHJ) ; Use ^XTMP to pass a lot of data between tasks.

S ^XTMP(ARHJ,0)=\$\$FMADD^XLFDT(DT,1)\_U_DT ; Save-thru and create dates.

S ^XTMP(ARHJ)="HI MOM!" ; Pretend this is a lot of data!

; XUTMQQ holds the ZTSK of the print task

S X=\$\$REQQ^XUTMDEVQ(XUTMQQ,\$H,"ARHJ") ; Schedule print task to start

Q

PRINTQ ;

S ZTREQ="@"

;U IO ; Don't need this if invoked using a ^XUTMDEVQ API.

W !,"The secret message is: '",\$G(^XTMP(ARHJ)),"'"

K ^XTMP(ARHJ)

Q

## \$\$REQQ^XUTMDEVQ(): Schedule Second Part of a Task

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: TaskMan

ICR \#: 1519

Description: The \$\$REQQ^XUTMDEVQ extrinsic function schedules the second task (that is print data) from the <u>\$\$QQ^XUTMDEVQ(): Double Queue—Direct Queuing in a Single Call</u> API.

If it takes a long time to gather and print data, users should split the job into two tasks:

Gather Data—The first task gathers the data.

Print Data—The second task prints the data.

Separating the data-gathering task from the data print task helps avoid unnecessarily tying up a printer while large amounts of data are gathered.

This API makes sure that only the scheduled time and any variables in %VAR are passed to the <u>REQ^%ZTLOAD: Requeue a Task</u>.

![](kernel-8-0-developer-s-guide-taskman-user-guide/015.png) NOTE: This API was released with Kernel Patch XU\*8.0\*389.

Format: \$\$REQQ^XUTMDEVQ(xutsk,xudth\[,\[.\]%var\])

Input Parameters: xutsk: (required) This input parameter is the TaskMan task to schedule the second task from the <u>\$\$QQ^XUTMDEVQ(): Double Queue—Direct Queuing in a Single Call</u> API and should be in the XUTMQQ variable.

xudth: (required) This input parameter is the new scheduled run time.

\[.\]%var: (optional) This input parameter is converted to the ZTSAVE variable; it is the same as the %var input parameter for the <u>\$\$DEV^XUTMDEVQ(): Force Queuing—Ask for Device</u> API.

Output: returns: Returns:

- 1—Successful.
- 0—Unsuccessful.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<u>Figure 7</u> is a job that consists of gathering information and then printing it. Assume that the gathering takes a few hours. You do *not* want the device that the user selects to be tied up for that time, so you divide the job into two tasks. The first task gathers the information, and the second task prints it. Use the <u>\$\$QQ^XUTMDEVQ(): Double Queue—Direct Queuing in a Single Call</u> API to select the device, schedule the gather task, and queue the print task. Use the \$\$REQQ^XUTMDEVQ API to schedule the print task when the gather task finishes.

![](kernel-8-0-developer-s-guide-taskman-user-guide/016.png) NOTE: This is the easiest way to divide a job into two tasks.

<span id="_Ref501007500" class="anchor"></span>Figure 7: \$\$REQQ^XUTMDEVQ API—Sample Code

ARHBQQ ;SFVAMC/GB - Demo of 'gather' and 'print' in 2 tasks ;1/19/06 08:31

;;1.1

QQ ;

N X

S X=\$\$QQ^XUTMDEVQ("GATHERQ^ARHBQQ","ARHB Gather",,,,,1,"PRINTQ^ARHBQQ","ARHB Print")

W !,"X=",X

Q

GATHERQ ;

N ARHJ,X

S ZTREQ="@"

S ARHJ="ARHB-QQ"\_"-"\_\$J\_"-"\_\$H ; namespace + unique ID

K ^XTMP(ARHJ) ; Use ^XTMP to pass a lot of data between tasks.

S ^XTMP(ARHJ,0)=\$\$FMADD^XLFDT(DT,1)\_U_DT ; Save-thru and create dates.

S ^XTMP(ARHJ)="HI MOM!" ; Pretend this is a lot of data!

; XUTMQQ holds the ZTSK of the print task

S X=\$\$REQQ^XUTMDEVQ(XUTMQQ,\$H,"ARHJ") ; Schedule print task to start

Q

PRINTQ ;

S ZTREQ="@"

;U IO ; Don't need this if invoked using a ^XUTMDEVQ API.

W !,"The secret message is: '",\$G(^XTMP(ARHJ)),"'"

K ^XTMP(ARHJ)

Q

## DISP^XUTMOPT(): Display Option Schedule

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: TaskMan

ICR \#: 1472

Description: The DISP^XUTMOPT API displays the schedule for an option.

Format: DISP^XUTMOPT(option_name)

Input Parameters: option_name: (required) The name of the option from the OPTION (#19) file for which the TaskMan schedule is to be displayed.

Output: returns: Returns the TaskMan option schedule.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc199950723" class="anchor"></span>Figure 8: DISP^XUTMOPT API—Example

\><span class="mark">D DISP^XUTMOPT(option_name)</span>

## EDIT^XUTMOPT(): Edit an Option’s Scheduling

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: TaskMan

ICR \#: 1472

Description: The EDIT^XUTMOPT API allows users to edit an option’s scheduling in the OPTION SCHEDULING (#19.2) file.

Format: EDIT^XUTMOPT(option_name)

Input Parameters: option_name: (required) The name of the option from the OPTION (#19) file whose schedule the user is to be allowed to edit.

Output: returns: Returns the requested option to edit the schedule.

## OPTSTAT^XUTMOPT(): Obtain Option Schedule

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: TaskMan

ICR \#: 1472

Description: The OPTSTAT^XUTMOPT API allows an application to find out when an option is scheduled and get other data.

Format: OPTSTAT^XUTMOPT(option_name,.root)

Input Parameters: option_name: (required) The name of the option from the OPTION (#19) file upon which to return data.

.root: (required) This parameter is passed by reference. This is an array because the same task can be scheduled more than once.

Output: .root: Returns an array of data about the option in question.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc199950724" class="anchor"></span>Figure 9: OPTSTAT^XUTMOPT API—Example

\><span class="mark">D OPTSTAT^XUTMOPT("OPTION NAME",.ROOT)</span>

Returns an array of data in ROOT (pass by ref) in the form:

ROOT=count ROOT(1)=task number^scheduled time^reschedule freq^special queuing flag

## RESCH^XUTMOPT(): Set Up Option Schedule

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: TaskMan

ICR \#: 1472

Description: The RESCH^XUTMOPT API allows an application to set up the schedule for an option.

Format: RESCH^XUTMOPT(option_name\[,when_to_run\]\[,device_to_use\]  
\[,reschedule_freq\]\[,flags\]\[,.error_array\])

Input Parameters: option_name: (required) The name of the option from the OPTION (#19) file to be rescheduled.

when_to_run: (optional) The new scheduled time for the option to run.

device_to_use: (optional) The device to use for the rescheduled option.

reschedule_freq: (optional) The frequency to run the rescheduled option.

flags: (optional) If the flag is set to an L, LAYGO a new entry if needed.

.error_array: (optional) Passed by reference.

Output Parameters: .error_array: (optional) This is set to -1 if the option was *not* found.

## EN^XUTMTP(): Display HL7 Task Information

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Controlled Subscription

Category: TaskMan

ICR \#: 3521

Description: The EN^XUTMTP API is displays the Health Level Seven (HL7)-related task information. First, the currently running tasks are examined in the SCHEDULE file. For each task found, examine the ROUTINE field. If the ROUTINE field contains HL, it is a Health Level Seven-related task.

Format: EN^XUTMTP(task\[,ztenv,ztkey,ztname,ztflag,xutmuci\])

Input Parameters: task: (required) TaskMan’s task ID.

ztenv: (optional) Set = 1.

ztkey: (optional) Set = 0.

ztname: (optional) Set = ,User name.

ztflag: (optional) Set = 1.

xutmuci: (optional) X ^%ZOSF(“UCI”) S XUTMUCI=YOutput: returns: Returns the HL7-related task information. The following is an example of the information displayed by this API:

> <span id="_Toc199950725" class="anchor"></span>Figure 10: EN^XUTMTP—Sample Display Information

261181: EN^HLCSLM, HL7 Link Manager. No device. DEV,MOU.  
From 12/31/2001 at 14:17, By XUUSER,THIRTY.  
Started running 12/31/2001 at 14:17. Job \#: 562039155

## ^%ZTLOAD: Queue a Task

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

^%ZTLOAD is the main API used to create and schedule tasks (commonly referred to as “queuing”). Queuing tells TaskMan to use a background partition to DO a certain API at a certain time, with certain other conditions established as described by the input variables.

Reference Type: Supported

Category: TaskMan

ICR \#: 10063

Description: The ^%ZTLOAD API, as used in code, behaves consistently so most queuers strongly resemble one another. The queuer can be written so that it is either interactive with the user or so that it is *not* interactive. The standard variations on this structure deserve attention.

Format: ^%ZTLOAD

Make sure to perform the following steps before calling this API:

1.  NEW all *non*-namespaced variables.
18. Set all input variables.
19. Call the API.

Input Variable: ZTRTN: (required) The API that TaskMan will DO to start the task. You can specify it as any of the following:

- “LABEL^ROUTINE”
- “^ROUTINE”
- “ROUTINE”

If it is *not* passed, the original API is used.

ZTDESC: (required) Task description, up to 200 characters describing the task, with the software application name at the front. While *not* required, use of this variable is *recommended*.

ZTDTH: (optional) Start time when TaskMan should start the task. It *must* be a date and time in VA FileMan or \$HOROLOG format. Setting it to @ causes the task to be created but *not* scheduled. If ZTDTH is *not* set, ^%ZTLOAD asks the user for the start time.

ZTIO: (optional) The I/O device the task should use. If ZTIO is NULL, no device is used. If undefined, the current I/O variables are used to select a device. ZTIO should only be used when the current I/O variables do *not* describe the needed device. If you do *not* need a device for a job, SET ZTIO=“”. The ZTIO variable accepts the same I/O formatting string as the [IOP](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_device_handler_ug.pdf#iop_zis) variable in the [^%ZIS](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_device_handler_ug.pdf#zis) API.

![](kernel-8-0-developer-s-guide-taskman-user-guide/017.png) REF: For more information, see the [*Kernel 8.0 Developers Guide: Device Handler Developer Tools User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_device_handler_ug.pdf).

ZTUCI: (optional) UCI the task should use. The current UCI is used if ZTUCI is undefined.

ZTCPU: (optional) Volume Set:CPU. Specifies the name of the volume set and CPU on which the task should run. The volume set can be passed in the first :-piece, and the CPU in the second. Neither piece of information is required; either can be passed without the other. If the CPU alone is passed, it *must* still be preceded by a “:” (such as :KDAISC6A1). If the volume set is *not* passed, TaskMan runs the task on the volume set it came from or on a Print Server. If the CPU is *not* passed, TaskMan runs the task on the CPU where TaskMan resides. Any volume set and/or CPU specified by the task’s I/O device takes precedence over the same information passed here.

![](kernel-8-0-developer-s-guide-taskman-user-guide/018.png) NOTE: On Caché systems, specifying which CPU a job should run on only works if you are running TaskMan from a DCL context. If you specify the CPU, but are *not* running TaskMan from a DCL context, the job may *not* run correctly.

ZTPRI: (optional) The CPU priority the task should receive. It should be an integer between 1 (low) and 10 (high). The site’s default for tasks is used if this is undefined.

ZTSAVE(): (optional) Input variable array. An array whose nodes specify input variables to the task beyond the usual set all tasks receive. There are four kinds of nodes this array can have:

- ZTSAVE(“VARIABLE”)—Set equal to NULL or to a value:
- If NULL, the current value of that variable is copied for the task.
- The variable is created with the value assigned \[such as ZTSAVE(“PSIN”)=42\].

The variable can be local or global, and it can be a variable or an individual array node.

- ZTSAVE(“OPEN ARRAY REFERENCE”)—Set to NULL to declare a set of nodes within an array to be input variables to the task \[such as ZTSAVE(“^UTILITY(\$J,”)\].
- ZTSAVE(“NAMESPACE\*”)—Set to NULL to save all local variables in a certain namespace \[such as ZTSAVE(“LR\*”)\].
- ZTSAVE(“\*”)—Used to save all local variables. *Non*-namespaced variables (esp. %, X, Y, and so on) may or may *not* be saved. Saving individual variables is more efficient. ZTSAVE nodes are saved just as they are typed, so special variables like \$J have one value when used to save the variables, and a different value when used to restore them for the task.

ZTKIL: (optional) KEEP UNTIL. Set this to the first day the Task File Cleanup can delete this task. It should be a date and time in VA FileMan or \$HOROLOG format. Use of this variable is *recommended* when ZTDTH equals @.

ZTSYNC: (optional) Name of a SYNC FLAG. Using SYNC FLAGs allows TaskMan to run the next task in a series of tasks only if the preceding task in the series completed successfully.

You can choose any name for a SYNC FLAG. You should namespace the name, however, and make it no longer than 30 characters in length.

To use SYNC FLAGs, the task *must* be queued to a device of type resource (through the ZTIO variable).

![](kernel-8-0-developer-s-guide-taskman-user-guide/019.png) REF: For complete information on how to use SYNC FLAGs, see the “<u>Using SYNC FLAGs to Control Sequences of Tasks</u>” section.

Output Variables: ZTSK: (Usually returned) The task number assigned to a task, returned whenever a task is successfully created. It can be used as an input variable to the other TaskMan application mode APIs.

![](kernel-8-0-developer-s-guide-taskman-user-guide/020.png) NOTE: If a task is queued to a volume set other than the one where it was created, it is usually assigned a new task number when it is moved.

If ZTSK is *not* defined after calling ^%ZTLOAD, either ZTRTN was *not* set up or the user canceled the creation when prompted for a start time. If a task is *not* created and if ^%ZTLOAD is being called by a foreground job, then ^%ZTLOAD displays a message to the user indicating that the task has been canceled.

![](kernel-8-0-developer-s-guide-taskman-user-guide/021.png) NOTE: ZTSK is *not* a system variable. It is KILLed and manipulated in many places. If the software needs to remember a task number, ZTSK should be set into some properly namespaced variable the application can protect.

ZTSK(“D”): START TIME (usually returned) contains the task’s requested start time in \$HOROLOG format. It is returned whenever ZTSK is returned and gives you a way to know the start time a user requests.

### Interactive Use of ^%ZTLOAD

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA Standards and Conventions (SAC) require that anywhere you let a user pick the output device you also let the user choose to queue the output.

Often, one part of the queuer is a call to [^%ZIS](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_device_handler_ug.pdf#zis) (the Device Handler). When you set up the variables for your call, include a Q in the variable %ZIS, so the Device Handler lets the user pick queuing. After the Device Handler call \[and after you check POP to ensure that a valid device was selected), you can check \$DATA(IO(“Q”)\] to see whether the user chose to queue to that device. If so, then you *must* queue the printout you were about to do directly, and your software should branch to the code to set up the task. A sample of the code for this kind of print queuer looks something like <u>Figure 11</u>:

<span id="_Ref199484799" class="anchor"></span>Figure 11: ^%ZTLOAD API—Print Queuer Sample Code

SELECT ;select IO device for report

S %ZIS="Q" D ^%ZIS

I POP D CANCEL Q

I \$D(IO("Q")) D QUEUE Q

D PRINT,^%ZISC Q

;

QUEUE ;queue the report

S ZTRTN="PRINT^ZZREPORT"

S ZTDESC="ZZ Application Daily Report 1"

S ZTSAVE("ZZRANGE")=""

D ^%ZTLOAD

I \$D(ZTSK)\[0 W !!?5,"Report canceled!"

E W !!?5,"Report queued!"

D HOME^%ZIS Q

The code to set up the task after the call to [^%ZIS](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_device_handler_ug.pdf#zis) has four steps:

1.  Set the ^%ZTLOAD input variables to define the task.
20. Call ^%ZTLOAD to queue the task.
21. Check \$DATA(ZTSK)#2 to find out whether a task was really queued and provides appropriate feedback.
22. Call [HOME^%ZIS](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_device_handler_ug.pdf#home_zis) API to reset its IO variables.

![](kernel-8-0-developer-s-guide-taskman-user-guide/022.png) NOTE: This queuer did *not* define the ZTIO variable. Print queuers can take advantage of the fact that they directly follow a [^%ZIS](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_device_handler_ug.pdf#zis) call that sets up all the IO variables they need. Under these conditions, the queuer code can rely on ^%ZTLOAD to identify the task’s IO device from the IO variables; thus, saving the developer the work of building the correct ZTIO string.

Notice also that when queuing output, we need *not* call [^%ZISC](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_device_handler_ug.pdf#zisc) to close the IO device, because when the user chooses to queue output the Device Handler does *not* open the device. Thus, all we need to do here is reset our IO variables with a [HOME^%ZIS](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_device_handler_ug.pdf#home_zis) call.

As usual in these kinds of queuers, we did *not* define ZTDTH but instead let ^%ZTLOAD ask the user when the report should run.

Finally, notice that we tell the task to begin at PRINT, the same tag used by the trigger code to start the foreground print when the user chooses *not* to queue. Under most circumstances, print queuers can use most of the same code for their tasks that the foreground print uses.

### Non-Interactive Use of ^%ZTLOAD

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Under certain conditions, queuers *must* create and schedule their tasks with no interaction with the user. Examples include queuers operating out of tasks or queuers that need to run without the users’ knowledge. Only two items *must* be changed from interactive queuers to make *non*-interactive queuers work:

1.  ZTDTH *must* be passed to ^%ZTLOAD and *must* contain a valid DATE/TIME value.
23. If the code to queue the task does *not* follow a call to [^%ZIS](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_device_handler_ug.pdf#zis), you *must* define the ZTIO variable yourself. Either set it or allow it to be built from the current I/O variables (if those I/O variables describe the proper device).

After the call to ^%ZTLOAD, you may (or may *not*) want to issue feedback messages.

### Queuing Tasks without an I/O Device

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Certain tasks need no IO device. These include primarily tasks that rearrange large amounts of data but produce no report, such as filing and compiling tasks. Two different kinds of *non*-IO tasks exist:

- Concurrent—Those that can run concurrently.
- Sequential—Those that *must* run sequentially.

Queuers for concurrent *non*-IO tasks need only set ZTIO to NULL, and TaskMan runs the task, with no IO device.

For sequential *non*-IO tasks, queuers *must* set the ZTIO variable to the name of a resource type device. TaskMan then ensures that the tasks run single file, one after the other in order by requested start time. Applications that need sequential *non*-IO tasks should instruct system managers in the Package Installation Guide to create a resource device with the desired characteristics so that these queuers can safely queue their tasks to them. Such devices should be namespaced by the software application that uses them. SYNC FLAGs can also be used to allow the next task in a series to start only if the previous task in the series completed successfully.

![](kernel-8-0-developer-s-guide-taskman-user-guide/023.png) REF: For more information on SYNC FLAGs, see the “<u>Using SYNC FLAGs to Control Sequences of Tasks</u>” section.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The example in <u>Figure 12</u> is a job that consists of gathering information and then printing it. Assume that the gathering takes a few hours. You do *not* want the device that the user selects to be tied up for that time, so you divide the job into two tasks:

1.  The first task gathers the information.
24. The second task prints it.

Use the following APIs:

1.  [^%ZIS: Standard Device Call](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_device_handler_ug.pdf#zis) API to select the device.
25. ^%ZTLOAD API to queue the print task.
26. ^%ZTLOAD API to schedule the gather task.
27. <u>REQ^%ZTLOAD: Requeue a Task</u> API to schedule the print task when the gather task finishes.

![](kernel-8-0-developer-s-guide-taskman-user-guide/024.png) NOTE: This process is made easier by using the <u>\$\$QQ^XUTMDEVQ(): Double Queue—Direct Queuing in a Single Call</u> and <u>\$\$REQQ^XUTMDEVQ(): Schedule Second Part of a Task</u> APIs.

<span id="_Ref500233278" class="anchor"></span>Figure 12: ^%ZTLOAD API—Sample Code

ARHBQQ ;SFVAMC/GB - Demo of 'gather' and 'print' in 2 tasks ;1/19/06 08:31

;;1.1

ZTLOAD ;

N ARH,ARHZTSK,X,ZTSAVE,%ZIS,ZTSK,ZTDTH,ZTRTN,ZTDESC,ZTIO,POP

W !,"Queue the second task (the print task) first.",!

;Let's deal with the second task first.

;The user doesn't know it, but he's actually queuing the second task,

;the "print" portion of the job. The only question the user will be

;asked is to select the device.

;

S %ZIS="QM"

S IOP="Q" ;Force queuing.

D ^%ZIS Q:POP ; Select Device

W !,"Finished with %ZIS."

;

S ZTDTH="@" ;Don't schedule the task to run, we'll do it later

;If we didn't need to set ZTDTH, we could use EN^XUTMDEVQ, but that

;I 'new's ZTDTH, so we can't set it.

;

;BTW, Did you know that there's a 5th parameter in EN^XUTMDEVQ?

;Usually, EN^XUTMDEVQ will 'new' ZTSK, so you can't get to it.

;If you put "1" as the 5th parameter, ZTSK will exist when EN returns.

;D EN^XUTMDEVQ("PRINT^ARHBQQ","ARHB Print",.ZTSAVE,.%ZIS,1)

;

S ZTRTN="PRINT^ARHBQQ"

S ZTDESC="ARHB Print"

D ^%ZTLOAD

D HOME^%ZIS

W !,"ZTSK=",\$G(ZTSK)

Q:'\$D(ZTSK)

S ARHZTSK=ZTSK

;

N ZTSAVE,%ZIS,ZTSK,ZTDTH,ZTRTN,ZTDESC,ZTIO,IOP

W !,"Now queue the first task (the gather task).",!

;Now queue the first task, the "gather" portion of the job.

;Since we don't need a device,

;the user will only be asked when to start the task.

;(I wasn't able to get EN^XUTMDEVQ to work for me. I tried setting

;IOP="Q;" to let it know that it should be queued and it didn't need

;a device, but it did nothing, and returned a null ZTSK.)

F I="ARHZTSK" S ZTSAVE(I)="" ; Save the ZTSK of the "print" task.

S ZTIO="" ; We don't need a device.

S IOP="Q" ; Force queuing.

S ZTRTN="GATHER^ARHBQQ"

S ZTDESC="ARHB Gather"

D ^%ZTLOAD

D HOME^%ZIS

W !,"ZTSK=",\$G(ZTSK)

Q

GATHER ;

N ARHJ

S ZTREQ="@"

S ARHJ="ARHB-QQ"\_"-"\_\$J\_"-"\_\$H ; namespace + unique ID

K ^XTMP(ARHJ) ; Use ^XTMP to pass a lot of data between tasks.

S ^XTMP(ARHJ,0)=\$\$FMADD^XLFDT(DT,1)\_U_DT ; Save-thru and create dates.

S ^XTMP(ARHJ)="HI MOM!" ; Pretend this is a lot of data.

D SPRINT

Q

SPRINT ; Now schedule the "print" task to run.

N ZTSK,ZTDTH,I,ZTRTN,ZTDESC,ZTIO,ZTSAVE ; Very important to NEW the

; input variables to REQ^%ZTLOAD, otherwise they retain the values of

; the currently running task, and you could unintentionally change the

; "print" task to rerun the "gather" task.

F I="ARHJ" S ZTSAVE(I)="" ; Let the "print" task know the "\$J" value.

S ZTSK=ARHZTSK

S ZTDTH=\$H

D REQ^%ZTLOAD

;Instead of the above 8 lines we could have simply:

;S X=\$\$REQQ^XUTMDEVQ(ARHZTSK,\$H,"ARHJ")

Q

PRINT ;

S ZTREQ="@"

U IO ; Don't need this if invoked using a ^XUTMDEVQ API.

W !,"The secret message is: '",\$G(^XTMP(ARHJ)),"'"

K ^XTMP(ARHJ)

Q

### Code Execution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc200270043" class="anchor"></span>Figure 13: ^%ZTLOAD API—Sample Code Execution

VAH\><span class="mark">D ZTLOAD^ARHBQQ</span>

Queue the second task (the print task) first.

QUEUE TO PRINT ON

DEVICE: HOME// <span class="mark">P-MESS</span>

1 P-MESSAGE-ENGWO-HFS-VXD HFS FILE ==\> MAILMESSAGE

2 P-MESSAGE-HFS-VXD HFS FILE ==\> MAILMESSAGE

Choose 1-2\> <span class="mark">2 \<Enter\></span> P-MESSAGE-HFS-VXD HFS FILE ==\> MAILMESSAGE

Subject: <span class="mark">MY PRINT</span>

Select one of the following:

M Me

P Postmaster

From whom: Postmaster// <span class="mark">\<Enter\></span>

Send mail to: XUUSER,ONE// <span class="mark">\<Enter\></span> XUUSER,ONE

Select basket to send to: IN// <span class="mark">\<Enter\></span>

And Send to: <span class="mark">\<Enter\></span>

Finished with %ZIS.

ZTSK=2921497

Now queue the first task (the gather task).

Requested Start Time: NOW// <span class="mark">\<Enter\></span> (JAN 25, 2005@11:30:35)

ZTSK=2921499

### Output

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc200270044" class="anchor"></span>Figure 14: ^%ZTLOAD API—Sample Output

Subj: MY PRINT \[#28881111\] 01/25/05@11:30 2 lines

From: POSTMASTER (Sender: XUUSER,ONE - COMPUTER SPECIALIST) In 'IN'

basket.

Page 1 \*New\*

--------------------------------------------------------------------------

The secret message is: 'HI MOM!'

Enter message action (in IN basket): Ignore//

## \$\$ASKSTOP^%ZTLOAD: Stop TaskMan Task

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: TaskMan

ICR \#: 10063

Description: The \$\$ASKSTOP^%ZTLOAD extrinsic function asks TaskMan to stop running a specified task. Also, it checks for the ZTNAME variable, and if defined, it uses it instead of DUZ to value the STOP FLAG (#59.1) field. ZTNAME is supported by applications calling this API to indicate the process that asked the task to stop.

Format: \$\$ASKSTOP^%ZTLOAD(ztsk)

Input Parameters: ztsk: (required) Task number of the TaskMan task to be stopped.

Output: returns: Returns:

- 0—“Busy”. If it returns “Busy”, it could mean that:
- Task is locked.
- Someone else is changing it.
- TaskMan is starting to run it.
- 1—“Task missing” or Task “Finished running”. If it returns:
- “Task missing”—It could mean that it was an incorrect input task number, but it is most likely that the task ran and was removed after running.
- “Finished running”—It means that the task was finished running before the API request could go through, so the API could *not* stop an already finished task.
- 2—“Asked to stop” or “Unscheduled”. If it returns:
- “Asked to Stop”—Task has started running and the stop flag has been set, so if the application checks ([\$\$S^%ZTLOAD](#sztload-check-for-task-stop-request)) it should stop.
- “Unscheduled”—It was successful, and the task is *not* scheduled any more.

## DESC^%ZTLOAD(): Find Tasks with a Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: TaskMan

ICR \#: 10063

Description: The DESC^%ZTLOAD API finds tasks with a specific description.

Format: DESC^%ZTLOAD(description,list)

Input Parameters: description: (required) The TaskMan task description.

Output Parameters: list: Returns a list of tasks with the specified description.

## DQ^%ZTLOAD: Unschedule a Task

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: TaskMan

ICR \#: 10063

Description: The DQ^%ZTLOAD API unschedules tasks. Unscheduling a task ensures that, after the call, it is *not* scheduled or waiting for a device, computer link, or partition in memory. Unscheduling is guaranteed to be successful if the task is currently defined in the TASKS (#14.4) file. However, unscheduling a task that has already started running does *not* stop the task in any way.

Format: DQ^%ZTLOAD

Make sure to perform the following steps before calling this API:

1.  NEW all *non*-namespaced variables.
28. Set all input variables.
29. Call the API.

Input Variables: ZTSK: (required) The number of the task to unschedule. This task *must* currently be defined in the TASKS (#14.4) file, or the call fails.

Output Variables: ZTSK(0): Returns:

- 1—Task was unscheduled successfully.
- 0—Task was *not* unscheduled successfully.

## ISQED^%ZTLOAD: Return Task Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: TaskMan

ICR \#: 10063

Description: The ISQED^%ZTLOAD API returns whether a task is currently pending. Pending means that the task is any of the following:

- Scheduled.
- Waiting for an I/O device.
- Waiting for a volume set link.
- Waiting for a partition in memory.

It also returns the DUZ of the task’s creator and the time the task was scheduled to start.

Format: ISQED^%ZTLOAD

Make sure to perform the following steps before calling this API:

1.  NEW all *non*-namespaced variables.
30. Set all input variables.
31. Call the API.

Input Variables: ZTSK: (required) Task number of the task to look up. The task *must* be currently defined on the volume set to be searched, or the lookup fails.

ZTCPU: (optional) The volume set TaskMan should search for the task being looked up. If it has *not* passed, TaskMan searches the current volume set. Unlike the [^%ZTLOAD](#ztload-queue-a-task) API ZTCPU input variable, this variable does *not* accept a second :-piece specifying the CPU. It only specifies a volume set to search.

Output Variables: ZTSK(0):ZTSK(0) is returned as follows:

- 1—Task ZTSK is currently scheduled or waiting on volume set ZTCPU.
- 0—Task ZTSK is *not* currently scheduled or waiting on volume set ZTCPU.
- NULL (“”)—The lookup was unsuccessful.

ZTSK(“E”): (sometimes returned) The error code, returned when some error condition prevented a successful lookup. The codes and their values are:

- IT—The task number was *not* valid (0, negative, or *non*-numeric).
- I—The task does *not* exist on the specified volume set.
- IS—The volume set is *not* listed in the VOLUME SET (#14.5) file.
- LS—The link to that volume set is *not* available.
- U—An unexpected error arose (such as disk full, protection, and so on).

ZTSK(“D”): (sometimes returned) The date and time the task was scheduled to start, in \$HOROLOG format. It is returned only if ZTSK(0) equals Zero (0) or 1.

ZTSK(“DUZ”): (sometimes returned) Holds the DUZ of the user who created the task. It is returned only if ZTSK(0) equals Zero (0) or 1.

## \$\$JOB^%ZTLOAD(): Return a Job Number for a Task

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: TaskMan

ICR \#: 10063

Description: The \$\$JOB^%ZTLOAD extrinsic function was released with Kernel Patch XU\*8.0\*339. It returns the job number for a running TaskMan task.

Format: JOB^%ZTLOAD(ztsk)

Input Parameters: ztsk: (required) Task number of the running TaskMan task. If the specified task is *not* running, it returns NULL.

Output: returns: Returns the job number for the specified running TaskMan task.

## KILL^%ZTLOAD: Delete a Task

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: TaskMan

ICR \#: 10063

Description: The KILL^%ZTLOAD API deletes a task. When a task is deleted by KILL^%ZTLOAD, the task referenced by ZTSK is *not* defined in the volume set’s task file. If the task was pending, it does *not* start, but if it had already started running, the effects of deleting its record are unpredictable.

![](kernel-8-0-developer-s-guide-taskman-user-guide/025.png) NOTE: Tasks can delete their own records through the use of the ZTREQ output variable.

Format: KILL^%ZTLOAD

Make sure to perform the following steps before calling this API:

1.  NEW all *non*-namespaced variables.
32. Set all input variables.
33. Call the API.

Input Variables: ZTSK: (required) Task number of the TaskMan task to delete.

Output Variables: ZTSK(0): Returns:

- 1—Successful deletion of the task.
- 0—Requested task number is invalid.

## OPTION^%ZTLOAD(): Find Tasks for an Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: TaskMan

ICR \#: 10063

Description: The OPTION^%ZTLOAD API finds TaskMan tasks for a specific option.

Format: OPTION^%ZTLOAD(option,list)

Input Parameters: option: (required) The name of the specific option.

Output Parameters: list: Returns a list of TaskMan tasks for the specified option.

## PCLEAR^%ZTLOAD(): Clear Persistent Flag for a Task

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: TaskMan

ICR \#: 10063

Description: The PCLEAR^%ZTLOAD API clears the persistent flag for a TaskMan task (clears the persistent node).

Format: PCLEAR^%ZTLOAD(ztsk)

Input Parameters: ztsk: (required) The TaskMan task number.

Output: none.

## \$\$PSET^%ZTLOAD(): Set Task as Persistent

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: TaskMan

ICR \#: 10063

Description: The \$\$PSET^%ZTLOAD extrinsic function sets a TaskMan task as persistent (sets the persistent node). A task that is marked as persistent is restarted if TaskMan finds that the lock on ^%ZTSCH(“TASK”,tasknumber) has been removed. This adds the requirement that the task only use incremental locks, that the entry in ^%ZTSK(task... be left in place as this restarts the task, and that the task can be restarted from the data that is in the ^%ZTSK(task,... global.

Format: \$\$PSET^%ZTLOAD(ztsk)

Input Parameters: ztsk: (required) The TaskMan task number.

Output: returns: Returns:

- 1—Flag was set.
- 0—Flag was *not* set.

## REQ^%ZTLOAD: Requeue a Task

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: TaskMan

ICR \#: 10063

Description: The REQ^%ZTLOAD API unschedules, edits, and reschedules a task. Unscheduling ensures the task is *not* pending but does *not* stop it from running. Editing is limited to the API, start time, description, and I/O device. Rescheduling is optional. However, if the task is *not* rescheduled, it is vulnerable to the Task File Cleanup option. The entire procedure is referred to as requeuing.

![](kernel-8-0-developer-s-guide-taskman-user-guide/026.png) CAUTION: Because requeuing does *not* involve stopping a running task, it is possible to wind up with the same task running in two different partitions if the algorithm is *not* designed carefully. This is *not* supported by TaskMan; thus, developers should use requeuing very carefully. Queuing a new task is usually a better way to accomplish the same goals.

![](kernel-8-0-developer-s-guide-taskman-user-guide/027.png) NOTE: Tasks can reschedule themselves through use of the ZTREQ output variable.

Format: REQ^%ZTLOAD

Make sure to perform the following steps before calling this API:

1.  NEW all *non*-namespaced variables.
34. Set all input variables.
35. Call the API.

Input Variables: ZTSK: (required) The TaskMan task number of the task to edit. It *must* be defined on the current volume set for the edit to succeed. It is *strongly recommended that this task not be currently running*.

ZTDESC: (optional) New description for the task. It should describe the task and name the software application that created the task.

ZTDTH: (optional) New start time for the task. Pass this as a date and time in VA FileMan or \$HOROLOG format. If *not* passed, the original start time is used again. If passed as @, the task is *not* rescheduled.

The ZTDTH input variable can also be passed as a rescheduling code. This code is a number followed by an S (seconds), an H (hours), or a D (days). This code represents an interval of time (such as 60S is 60 seconds) that is added to the current time (for seconds or hours) or the original start time (for days) to produce the new start time.

ZTIO: (optional) New I/O device for the task. It sets [IOP](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_device_handler_ug.pdf#iop_zis) in the [^%ZIS](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_device_handler_ug.pdf#zis) API, and can take all of [IOP](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_device_handler_ug.pdf#iop_zis)’s format specification strings.  
  
If the ZTIO variable is set to @, the task is rescheduled for no I/O device.  
  
If the ZTIO variable is set to NULL or it is *not* passed, the originally requested I/O device is used.

- ZTIO(“H”)—If *not* set, it is set to the value of the [IO("HFSIO")](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_device_handler_ug.pdf#hfsio_zis) variable in the [^%ZIS](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_device_handler_ug.pdf#zis) API.
- ZTIO(“P”)—If *not* set, it is set to the value of the [IOPAR](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_device_handler_ug.pdf#iopar_zis) variable in the [^%ZIS](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_device_handler_ug.pdf#zis) API.

ZTRTN: (optional) The API TaskMan will DO to start the task. You can specify it as any of the following:

- “LABEL^ROUTINE”
- “^ROUTINE”
- “ROUTINE”

If it is *not* passed, the original API is used.

ZTSAVE: (optional) Input variable array. An array whose nodes specify input variables to the task beyond the usual set all tasks receive. It is set up in the same format as the ZTSAVE input variable for the [^%ZTLOAD](#ztload-queue-a-task) API.

Output Variables: ZTSK(0): Returns:

- 1—Task is defined.
- 0—Task is *not* defined or ZTDTH was passed in a bad format.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The example in <u>Figure 15</u> is a job that consists of gathering information and then printing it. Assume that the gathering takes a few hours. You do *not* want the device that the user selects to be tied up for that time, so divide the job into two tasks:

1.  The first task gathers the information.
36. The second task prints it.

Use the [^%ZIS](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_device_handler_ug.pdf#zis) API to select the device, the <u>^%ZTLOAD: Queue a Task</u> API to queue the print task and schedule the gather task. Use the REQ^%ZTLOAD API to schedule the print task when the gather task finishes.

![](kernel-8-0-developer-s-guide-taskman-user-guide/028.png) NOTE: This process is made easier by using the <u>\$\$QQ^XUTMDEVQ(): Double Queue—Direct Queuing in a Single Call</u> and <u>\$\$REQQ^XUTMDEVQ(): Schedule Second Part of a Task</u> APIs.

<span id="_Ref501520268" class="anchor"></span>Figure 15: REQ^%ZTLOAD API—Sample Code

ARHBQQ ;SFVAMC/GB - Demo of 'gather' and 'print' in 2 tasks ;1/19/06 08:31

;;1.1

ZTLOAD ;

N ARH,ARHZTSK,X,ZTSAVE,%ZIS,ZTSK,ZTDTH,ZTRTN,ZTDESC,ZTIO,POP

W !,"Queue the second task (the print task) first.",!

;Let's deal with the second task first.

;The user doesn't know it, but he's actually queuing the second task,

;the "print" portion of the job. The only question the user will be

;asked is to select the device.

;

S %ZIS="QM"

S IOP="Q" ;Force queuing.

D ^%ZIS Q:POP ; Select Device

W !,"Finished with %ZIS."

;

S ZTDTH="@" ;Don't schedule the task to run, we'll do it later

;If we didn't need to set ZTDTH, we could use EN^XUTMDEVQ, but that

;I 'new's ZTDTH, so we can't set it.

;

;BTW, Did you know that there's a 5th parameter in EN^XUTMDEVQ?

;Usually, EN^XUTMDEVQ will 'new' ZTSK, so you can't get to it.

;If you put "1" as the 5th parameter, ZTSK will exist when EN returns.

;D EN^XUTMDEVQ("PRINT^ARHBQQ","ARHB Print",.ZTSAVE,.%ZIS,1)

;

S ZTRTN="PRINT^ARHBQQ"

S ZTDESC="ARHB Print"

D ^%ZTLOAD

D HOME^%ZIS

W !,"ZTSK=",\$G(ZTSK)

Q:'\$D(ZTSK)

S ARHZTSK=ZTSK

;

N ZTSAVE,%ZIS,ZTSK,ZTDTH,ZTRTN,ZTDESC,ZTIO,IOP

W !,"Now queue the first task (the gather task).",!

;Now queue the first task, the "gather" portion of the job.

;Since we don't need a device,

;the user will only be asked when to start the task.

;(I wasn't able to get EN^XUTMDEVQ to work for me. I tried setting

;IOP="Q;" to let it know that it should be queued and it didn't need

;a device, but it did nothing, and returned a null ZTSK.)

F I="ARHZTSK" S ZTSAVE(I)="" ; Save the ZTSK of the "print" task.

S ZTIO="" ; We don't need a device.

S IOP="Q" ; Force queuing.

S ZTRTN="GATHER^ARHBQQ"

S ZTDESC="ARHB Gather"

D ^%ZTLOAD

D HOME^%ZIS

W !,"ZTSK=",\$G(ZTSK)

Q

GATHER ;

N ARHJ

S ZTREQ="@"

S ARHJ="ARHB-QQ"\_"-"\_\$J\_"-"\_\$H ; namespace + unique ID

K ^XTMP(ARHJ) ; Use ^XTMP to pass a lot of data between tasks.

S ^XTMP(ARHJ,0)=\$\$FMADD^XLFDT(DT,1)\_U_DT ; Save-thru and create dates.

S ^XTMP(ARHJ)="HI MOM!" ; Pretend this is a lot of data.

D SPRINT

Q

SPRINT ; Now schedule the "print" task to run.

N ZTSK,ZTDTH,I,ZTRTN,ZTDESC,ZTIO,ZTSAVE ; Very important to NEW the

; input variables to REQ^%ZTLOAD, otherwise they retain the values of

; the currently running task, and you could unintentionally change the

; "print" task to rerun the "gather" task.

F I="ARHJ" S ZTSAVE(I)="" ; Let the "print" task know the "\$J" value.

S ZTSK=ARHZTSK

S ZTDTH=\$H

D REQ^%ZTLOAD

;Instead of the above 8 lines we could have simply:

;S X=\$\$REQQ^XUTMDEVQ(ARHZTSK,\$H,"ARHJ")

Q

PRINT ;

S ZTREQ="@"

U IO ; Don't need this if invoked using a ^XUTMDEVQ API.

W !,"The secret message is: '",\$G(^XTMP(ARHJ)),"'"

K ^XTMP(ARHJ)

Q

### Code Execution

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc200270046" class="anchor"></span>Figure 16: ^%ZTLOAD API—Sample Code Execution

VAH\><span class="mark">D ZTLOAD^ARHBQQ</span>

Queue the second task (the print task) first.

QUEUE TO PRINT ON

DEVICE: HOME// <span class="mark">P-MESS</span>

1 P-MESSAGE-ENGWO-HFS-VXD HFS FILE ==\> MAILMESSAGE

2 P-MESSAGE-HFS-VXD HFS FILE ==\> MAILMESSAGE

Choose 1-2\> <span class="mark">2 \<Enter\></span> P-MESSAGE-HFS-VXD HFS FILE ==\> MAILMESSAGE

Subject: <span class="mark">MY PRINT</span>

Select one of the following:

M Me

P Postmaster

From whom: Postmaster// <span class="mark">\<Enter\></span>

Send mail to: XUUSER,ONE// <span class="mark">\<Enter\></span> XUUSER,ONE

Select basket to send to: IN// <span class="mark">\<Enter\></span>

And Send to: <span class="mark">\<Enter\></span>

Finished with %ZIS.

ZTSK=2921497

Now queue the first task (the gather task).

Requested Start Time: NOW// <span class="mark">\<Enter\></span> (JAN 25, 2005@11:30:35)

ZTSK=2921499

### Output

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc200270047" class="anchor"></span>Figure 17: ^%ZTLOAD API—Sample Output

Subj: MY PRINT \[#28881111\] 01/25/05@11:30 2 lines

From: POSTMASTER (Sender: XUUSER,ONE - COMPUTER SPECIALIST) In 'IN'

basket.

Page 1 \*New\*

--------------------------------------------------------------------------

The secret message is: 'HI MOM!'

Enter message action (in IN basket): Ignore//

## RTN^%ZTLOAD(): Find Tasks that Call a Routine

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: TaskMan

ICR \#: 10063

Description: The RTN^%ZTLOAD API finds TaskMan tasks that call a specific routine.

Format: RTN^%ZTLOAD(routine,list)

Input Parameters: routine: (required) The name of the specific routine called.

Output: list: Returns a list of TaskMan tasks that call the specified routine.

## \$\$S^%ZTLOAD(): Check for Task Stop Request

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: TaskMan

ICR \#: 10063

Description: The \$\$S^%ZTLOAD extrinsic function is used within a task to determine if the task has been asked to stop. Using the \$\$S^%ZTLOAD() function in longer tasks is *highly recommended*. Tasks should test \$\$S^%ZTLOAD to check if the user who queued the task has requested that the task be stopped. If the task has been asked to stop, it should set the local variable ZTSTOP to 1 before quitting. This alerts the submanager to set the task’s status to STOPPED instead of FINISHED, to give the user feedback that the task has obeyed their request.

You can use the optional message parameter to inform the user of the progress of a job. It is displayed when the task is listed by one of the many options that list tasks.

Format: \$\$S^%ZTLOAD(\[message\])

Input Parameters: message: (optional) Allows you to leave a message for the creator of the TaskMan task.

Output: returns: Returns:

- 1—Creator of the task that has asked the task to stop.
- 0—For all other cases.

## STAT^%ZTLOAD: Task Status

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: TaskMan

ICR \#: 10063

Description: The STAT^%ZTLOAD API looks up tasks and retrieves their status. The status of a task returned by STAT^%ZTLOAD is expressed in the general terms of whether the task:

- Ran.
- Is running.
- Runs.

ZTSK(1) and ZTSK(2) return the code and text of the status. This status is an abstraction based on the more complex system used by TaskMan.

An active task is one that either is expected to start or is currently running. An inactive task does *not* start in the future without outside intervention; this can be because it:

- Has already completed.
- Was never scheduled.
- Was interrupted.

The “running” status is *not* based on direct examination of the system tables but is inferred from TaskMan’s information about the task.

When interpreting the output of STAT^%ZTLOAD, consider that:

- If a task is transferred to another volume set, it becomes undefined on the original volume set.
- A status of “running” is a guess.
- “Finished” does *not* necessarily mean the task accomplished what it set out to do.
- An interrupted task may or may *not* run correctly if edited and rescheduled.

Format: STAT^%ZTLOAD

Make sure to perform the following steps before calling this API:

1.  NEW all *non*-namespaced variables.
37. Set all input variables.
38. Call the API.

Input Variables: ZTSK: (required) The TaskMan task number to look up. It *must* be defined on the current volume set.

Output Variables: ZTSK(0): Returns:

- 1—Task is defined.
- 0—Task is *not* defined.

ZTSK(1): Numeric status code from 0 to 5 indicating the status of the task.

ZTSK(2): Status text describing the status of the task. Its value corresponds with the status code in ZTSK(1). The possible values and their meanings are as follows:

- ZTSK(1) = 0 and ZTSK(2) = “Undefined”—Task does *not* exist on this volume set.
- ZTSK(1) = 1 and ZTSK(2) = “Active: Pending”—Task is:
- Scheduled.
- Waiting for an I/O device.
- Waiting for a volume set link.
- Waiting for a partition in memory.
- ZTSK(1) = 2 and ZTSK(2) = “Active: Running”—Task has started running.
- ZTSK(1) = 3 and ZTSK(2) = “Inactive: Finished”—Task quit normally after running.
- ZTSK(1) = 4 and ZTSK(2) = “Inactive: Available”—Task was created without being scheduled or was edited without being rescheduled.
- ZTSK(1) = 5 and ZTSK(2) = “Inactive: Interrupted”—Task was interrupted before it would have quit normally. Causes can include:
- Bad data.
- User intervention.
- Hard error.
- Many other possibilities.

## \$\$TM^%ZTLOAD: Check if TaskMan is Running

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: TaskMan

ICR \#: 10063

Description: The \$\$TM^%ZTLOAD extrinsic function determines if TaskMan is running. Use this function if you need to know the status of TaskMan.

Format: \$\$TM^%ZTLOAD

Input Parameters: none.

Output: returns: Returns:

- 1—TaskMan is running on the current volume set.
- 0—TaskMan is *not* running on the current volume set.

## ZTSAVE^%ZTLOAD(): Build ZTSAVE Array

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: TaskMan

ICR \#: 10063

Description: The ZTSAVE^%ZTLOAD API stores a string of variables in the ZTSAVE array.

Format: ZTSAVE^%ZTLOAD(string_of_variables\[,kill_ztsave_flag\])

Input Parameters: string_of_variables: (required) Sting of variable names to be stored in the ZTSAVE array.

kill_ztsave_flag: (optional) Any positive value first KILLs the ZTSAVE array.

Output: returns: Stores the string of input variables in the ZTSAVE array.

# Appendix A—Revision History Archive

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section should be used to show all document revision history prior to the current year.

![](kernel-8-0-developer-s-guide-taskman-user-guide/029.png) REF: For the most recent, current year document revision history, see the “[Revision History](#_Toc234301875)” section.

| Date | Revision | Description | Author |
|------|----------|-------------|--------|
| TBD  | TBD      | TBD         | TBD    |

<span id="Glossary" class="anchor"></span>Glossary

![](kernel-8-0-developer-s-guide-taskman-user-guide/030.png) REF: For a glossary of terms specific to Kernel, see the “Glossary” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm.pdf#Main_Glossary).

![](kernel-8-0-developer-s-guide-taskman-user-guide/031.png) REF: For a list of commonly used terms and acronyms, see the VA Glossary Power App.