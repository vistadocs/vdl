---
title: "Kernel 8.0 Systems Management: TaskMan User Guide"
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: "Systems Management: TaskMan"
app_code: XU
app_name: Kernel
section: INF
app_status: active
pkg_ns: XU
patch_ver: 8.0
patch_id: XU*8.0
group_key: "XU:XU:8.0"
file_numbers: 
  - 14
security_keys: []
menu_options: 6
description: 
audience: 
keywords: 
  - taskman
  - task
  - tasks
  - strong
  - manager
  - table
  - volume
  - span
  - class
  - xutm
page_count: 0
word_count: 25987
section_count: 19
table_count: 7
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: August 2025
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_taskman_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm_taskman_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=10"
---

---
title: |
  Kernel 8.0 Systems Management:

  TaskMan User Guide
---

![](kernel-8-0-systems-management-taskman-user-guide/001.png)

August 2025

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Product Delivery Service (PDS)

<span id="_Toc234301875" class="anchor"></span>Revision History

![](kernel-8-0-systems-management-taskman-user-guide/002.png) REF: For the archived document revision history, see “<u>Appendix A—Revision History Archive</u>.”

<table>
<caption><p><span id="_Ref26361910" class="anchor"></span>Table 1: TaskMan System Configuration Terminology</p></caption>
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
<td>08/31/2025</td>
<td>1.1</td>
<td><p>Updates:</p>
<ul>
<li><p>Added bookmarks to all sections.</p></li>
<li><p>Updated references and links to the Kernel Developer’s Guide.</p></li>
</ul></td>
<td>VistA Application Shared Services (VASS) Development Team</td>
</tr>
<tr class="even">
<td>05/01/2025</td>
<td>1.0</td>
<td><p>Initial document creation: <em>Kernel Systems Management: TaskMan User Guide</em>.</p>
<p>This is part of the VASS Documentation Redesign Project. The content in this document came from the original <em>Kernel 8.0 and Kernel Toolkit 7.3 Systems Management Guide</em> document, which was too large and cumbersome to maintain; so, it was broken down into smaller user guides for ease of use and maintenance going forward.</p>
<p><strong>Software Versions:</strong></p>
<p><strong>Kernel 8.0</strong></p>
<p><strong>Toolkit 7.3</strong></p></td>
<td>VASS Development Team</td>
</tr>
</tbody>
</table>

<span id="_Ref26361910" class="anchor"></span>Table 1: TaskMan System Configuration Terminology

Patch Revisions

For the current patch history related to this software, see the Patch Module on FORUM.

Table of Contents

<span id="_Toc204581165" class="anchor"></span>List of Figures

<span id="_Toc204581166" class="anchor"></span>List of Tables

<span id="_Hlt412359042" class="anchor"></span>Orientation

![](kernel-8-0-systems-management-taskman-user-guide/003.png) REF: For an orientation to this manual, please refer to the “Orientation” section in the [*Kernel 8.0 Systems Management: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm.pdf#Main_Orientation).

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [TaskMan: User Interface](#taskman-user-interface)
  - [Creating Tasks](#creating-tasks)
    - [Background Jobs](#background-jobs)
    - [Queuing Output](#queuing-output)
    - [Other Sources of Tasks](#other-sources-of-tasks)
  - [Working with Tasks](#working-with-tasks)
    - [Selecting Tasks](#selecting-tasks)
    - [Tasks in the Task List](#tasks-in-the-task-list)
    - [Display Status of Tasks](#display-status-of-tasks)
    - [Stopping Tasks](#stopping-tasks)
    - [Editing Tasks](#editing-tasks)
    - [Listing and Printing Tasks](#listing-and-printing-tasks)
    - [Selecting Another Task](#selecting-another-task)
  - [Summary](#summary)
- [TaskMan: System Management—Overview](#taskman-system-managementoverview)
  - [TaskMan’s Division of Labor](#taskmans-division-of-labor)
    - [Queuers](#queuers)
    - [Manager](#manager)
    - [Submanagers](#submanagers)
  - [TaskMan’s Files](#taskmans-files)
    - [TaskMan Globals: ^%ZTSCH and ^%ZTSK](#taskman-globals-ztsch-and-ztsk)
    - [SCHEDULE File](#schedule-file)
    - [TASKS (#14.4) File](#tasks-144-file)
    - [Other Files](#other-files)
  - [System Configuration Terminology](#system-configuration-terminology)
  - [TaskMan Security Key](#taskman-security-key)
- [TaskMan: System Management—Configuration](#taskman-system-managementconfiguration)
  - [Defining TaskMan Environments](#defining-taskman-environments)
  - [Configuring TaskMan](#configuring-taskman)
    - [Edit TaskMan Parameters Menu](#edit-taskman-parameters-menu)
    - [TaskMan’s Reach](#taskmans-reach)
    - [TASKMAN SITE PARAMETERS (#14.7) File](#taskman-site-parameters-147-file)
    - [VOLUME SET (#14.5) File](#volume-set-145-file)
    - [UCI ASSOCIATION (#14.6) File](#uci-association-146-file)
    - [Sample Configuration: Standardized VA Caché and GT.M Configuration](#sample-configuration-standardized-va-caché-and-gtm-configuration)
  - [Manager Startup](#manager-startup)
  - [Multiple TaskMan Managers and Load Balancing](#multiple-taskman-managers-and-load-balancing)
    - [Configuration for Multiple Managers](#configuration-for-multiple-managers)
    - [Starting Up, Pausing, and Stopping Multiple Managers](#starting-up-pausing-and-stopping-multiple-managers)
    - [Load Balancing](#load-balancing)
    - [Monitor Taskman Option](#monitor-taskman-option)
  - [Device Handler’s Influence on TaskMan](#device-handlers-influence-on-taskman)
  - [Running TaskMan with a DCL Context](#running-taskman-with-a-dcl-context)
    - [Setup for Running TaskMan in a DCL Context in a Cache/VMS Environment](#setup-for-running-taskman-in-a-dcl-context-in-a-cachevms-environment)
    - [How to Restart TaskMan when Running in a DCL Context](#how-to-restart-taskman-when-running-in-a-dcl-context)
- [TaskMan: System Management—Operation](#taskman-system-managementoperation)
  - [TaskMan Management Menu](#taskman-management-menu)
    - [List Tasks Option](#list-tasks-option)
    - [Dequeue Tasks Option](#dequeue-tasks-option)
    - [Requeue Tasks Option](#requeue-tasks-option)
    - [Delete Tasks Option](#delete-tasks-option)
    - [Cleanup Task List Option](#cleanup-task-list-option)
  - [Taskman Management Utilities](#taskman-management-utilities)
    - [Monitor Taskman Option](#monitor-taskman-option-1)
    - [Check Taskman’s Environment Option](#check-taskmans-environment-option)
    - [Restart Task Manager Option](#restart-task-manager-option)
    - [Place Taskman in a WAIT State Option](#place-taskman-in-a-wait-state-option)
    - [Remove Taskman from WAIT State Option](#remove-taskman-from-wait-state-option)
    - [Stop Task Manager Option](#stop-task-manager-option)
    - [SYNC flag file control Option](#sync-flag-file-control-option)
    - [Clean Task File Option](#clean-task-file-option)
    - [Queuable Task Log Clean Up Option](#queuable-task-log-clean-up-option)
  - [Scheduling Options](#scheduling-options)
    - [Which Options to Queue](#which-options-to-queue)
  - [Taskman Error Log Menu](#taskman-error-log-menu)
    - [Show Error Log Option](#show-error-log-option)
    - [Clean Error Log Over Range Of Dates Option](#clean-error-log-over-range-of-dates-option)
    - [Purge Error Log Of Type Of Error Option](#purge-error-log-of-type-of-error-option)
    - [Delete Error Log Option](#delete-error-log-option)
  - [Troubleshooting](#troubleshooting)
    - [SCHEDULE File](#schedule-file-1)
    - [TASKS (#14.4) File](#tasks-144-file-1)
    - [Task Status Codes](#task-status-codes)
    - [Task Rejection Messages](#task-rejection-messages)
    - [TaskMan State Messages](#taskman-state-messages)
- [Appendix A—Revision History Archive](#appendix-arevision-history-archive)
The *Kernel 8.0 Systems Management: TaskMan User Guide* is part of the *Kernel 8.0 and Kernel Toolkit 7.3 Systems Management Guide*. TaskMan (aka Task Manager) is the Kernel module that schedules and processes background tasks.

# TaskMan: User Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Kernel TaskMan (TM) software allows you to run tasks (such as VA FileMan prints and sorts) in the background and lets you continue working without interruption.

## Creating Tasks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VistA runs in a multiprocessing environment, which means the computer can work on more than one job at a time. Each job the computer works on consumes a part of the computer’s resources. Initially, you have only one job, your interactive terminal session, with which to do your work. TaskMan, however, allows you to claim more of the computer’s resources by allowing you to schedule additional jobs to run in the background.

### Background Jobs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can queue additional tasks to run through TaskMan. Once started, these additional tasks (called background tasks) can run at the same time as the foreground jobs and without further dialog with the people who started them. Appropriate use of background tasks can cut your frustration by reducing the amount of time you *must* wait for the computer to do lengthy, repetitious work that does *not* need human intervention. Every task queued to run in the background reduces time spent waiting and uses the computer’s resources more efficiently.

### Queuing Output

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Most users use TaskMan by queuing reports, labels, and other kinds of output. Because output involves no dialog once it has begun and because it requires you to wait while it prints, it makes an ideal candidate for queuing. You can queue most output when the computer asks you to select a device to which the output should be sent. The series of prompts and responses to queue a job to a device usually looks something like <u>Figure 1</u>:

<span id="_Ref67467752" class="anchor"></span>Figure 1: Queuing Output—Sample User Dialog

DEVICE: <span class="mark">QUEUE TO PRINT ON \<Enter\></span>

DEVICE: <span class="mark">*\<Device Name\>* \<Enter\></span>

Requested time to print: NOW// <span class="mark">\<Enter\></span>

Request queued.

After you answer this series of prompts, the output is queued for TaskMan to start at the requested time, and you can continue with other work while TaskMan prints the output. When many tasks need the same device at the same time, TaskMan runs them in order based on the time they were requested.

### Other Sources of Tasks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

An application can create other kinds of tasks without your interaction. The application might offer to queue other kinds of work like large filing or complex data analysis jobs. Sometimes applications queue tasks without asking. For example, the delivery of MailMan messages is performed by a job running as a task. If that task is *not* running when someone uses the MailMan options, MailMan automatically uses their foreground job to queue the task without asking them. Although people may knowingly or unknowingly queue these other kinds of tasks, output remains the most common kind of work to queue.

## Working with Tasks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc193181814" class="anchor"></span>Figure 2: TaskMan User Option

System Command Options ... \[XUCOMMAND\]

User's Toolbox ... "TBOX" \[XUSERTOOLS\]

<span class="mark">TaskMan User</span> \[XUTM USER\]

TaskMan also allows you to examine or modify your own tasks. You can do this by using the TaskMan User \[XUTM USER\] option, located in the User’s Toolbox \[XUSERTOOLS\] menu on your SYSTEM COMMAND OPTIONS \[XUCOMMAND\] menu (aka Common menu). This option lets you monitor or manipulate one task at a time.

### Selecting Tasks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When you choose the TaskMan User \[XUTM USER\] option, it first asks you to select a task with which to work. TaskMan displays the “Select TASK:” prompt. If you enter a single question mark (?), you get some general help about the option; if you enter two question marks (??), you can get a list of every task that you have queued to run. Typically, you would enter two question marks at this prompt so that you can get a listing of your individual tasks, listed by task number. You then choose a task from the list of tasks to work with. Using the TaskMan Use \[XUTM USER\] option is shown in <u>Figure 3</u>:

<span id="_Ref511309494" class="anchor"></span>Figure 3: TaskMan User Option—Sample User Dialog

Select User's Toolbox Option: <span class="mark">TASKMAN USER \<Enter\></span>

Select TASK: <span class="mark">?? \<Enter\></span>

Please wait while I find your tasks...searching...finished!

----------------------------------------------------------------------------

1: (Task \#161325) ZTSK2^XMA02, Queued print for XUUSER,TWELVE. Device VER\$LW.

KRN,KDE. From TODAY at 14:22, By you. Scheduled for TODAY at 20:00

----------------------------------------------------------------------------

2: (Task \#161776) ZTSK^DIP4, DEVICE LIST. Device VER\$LW. KRN,KDE.

From TODAY at 14:22, By you. Scheduled for TODAY at 22:00

----------------------------------------------------------------------------

End of listing. Press RETURN to continue: <span class="mark">\<Enter\></span>

Select TASK: <span class="mark">161776 \<Enter\></span> DEVICE LIST

Taskman User Option

Display status.

Stop task.

Edit task.

Print task.

List own tasks.

Select another task.

Select Action (Task \# 161776):

You can select tasks either by task number or list number. In the list of tasks, the list number is at the left-hand side of each task listing and is followed by the task number for each task (in parentheses). The rest of the information helps identify where the task came from and what it does.

### Tasks in the Task List

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can only select tasks that are still in TaskMan’s task list. When a task finishes running, it usually removes itself from the task list. Thus, you should *not* get a listing of every task you have run in the last year! Tasks that do *not* clean up their entries usually get cleaned out by TaskMan several days after they complete. You should only have to select tasks that are still actively waiting to start, currently running, or encountered some kind of problem while running.

### Display Status of Tasks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once you have selected a task to work with, you can ask to see the status of that task, using the Display status (D) action. TaskMan uses a task’s status to try to explain how soon the task runs and why. The possible normal statuses for a task include:

- Scheduled for *\<date and time\>*.
- Being inspected by TaskMan.
- Waiting for a partition.
- Being prepared.
- Currently running.
- Completed *\<date and time\>*.

![](kernel-8-0-systems-management-taskman-user-guide/004.png) NOTE: Please keep in mind that TaskMan can only “guess” whether a task is currently running.

One of the following messages may show up if the task needs some system resource *not* currently available:

- Waiting for device *\<name of device\>*.
- Waiting for the link to *\<name of CPU\>* to be restored.

When you display the status of a task waiting for a device, TaskMan shows you how many tasks are in line for that device ahead of your task. Additional statuses exist for tasks that have encountered some kind of problem. For each situation it lists a different explanation of the problem. For example, if you use the Stop task option to stop a task, its status shows up as “Stopped by you.”

### Stopping Tasks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Under certain conditions, you may want to stop a task. The TaskMan User \[XUTM USER\] allows you to do this through the Stop task (ST) action. Your ability to stop a task depends on the task’s status, however. If the task has already been stopped, is finished, or it encountered a problem while running and you try to stop it, the Stop task action tells you that the task has already stopped. If the task has *not* yet started running, on the other hand, you can always stop it. If the task has started running, the Stop task action succeeds in stopping it only if the developer who wrote the task has designed the task to be stopped by a user. At any rate, it does *not* cause any problems if you try to stop a running task.

To stop a task, use the Stop task action. Once you stop a task, it remains in the TASKS (#14.4) file until you edit it to run again or until TaskMan purges it from the Task list.

### Editing Tasks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Edit task (E) action lets you edit a task’s output device, description, and run time.

The task *must* be unscheduled before it can be edited. The Edit task action asks if it’s OK to unschedule the task. To edit the task, answer YES. But once the task is unscheduled, it does *not* run unless you reschedule it by finishing each step of editing the task.

![](kernel-8-0-systems-management-taskman-user-guide/005.png) NOTE: You *cannot* edit a task that is already running.

Once the task is unscheduled, you can update the following task settings:

- When the task should start.
- Which device it should use (and whether a device is needed).
- What the description of the task should be.

Once you have had a chance to modify these three settings, you are asked whether the task should be rescheduled as shown (see <u>Figure 4</u>):

- If you answer YES, the task is updated to reflect the changes you specified.
- If you answer NO, however, no settings are changed, but the task remains unscheduled (and does *not* run until you use Edit Task to reschedule it).

<span id="_Ref85876439" class="anchor"></span>Figure 4: Edit Task Option—Sample User Dialog

Before you edit the task I'll make sure it's not scheduled, okay? YES// <span class="mark">\<Enter\></span>

Task ready for editing.

Currently, this task requests output device VER\$LW.

Do you want to change the output device for this task? NO// <span class="mark">Y \<Enter\></span>

Select Task's Output Device (^ for none): <span class="mark">P236 \<Enter\></span>

When should this task run?: AUG 16, 2004@22:00// <span class="mark">\<Enter\></span>

Task's purpose: DEVICE LIST// <span class="mark">\<Enter\></span>

161776: DEVICE LIST. P236. Next run time: AUG 16, 2004@22:00.

Shall I reschedule this task as shown? YES// <span class="mark">\<Enter\></span>

Task rescheduled.

### Listing and Printing Tasks

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can use the List own tasks (L) action to review your tasks. This action displays the same list as that given when you enter two question marks (??) at the “Select Task:” prompt.

The Print task action allows you to print out the description of the task that you have currently selected.

### Selecting Another Task

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Once in the TaskMan User \[XUTM USER\] option, you can choose to work with a different task by using the Select another task (SE) action. Enter another task number to work with a different task. If you are *not* sure what task you want to work with, you can get a list of all your tasks by entering two question marks (??).

## Summary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Most output in VistA is performed by creating tasks that run in the background. Once you become familiar with TaskMan’s queuing system, you can increase productivity by using some of TaskMan’s special features, including:

- Listing your future tasks.
- Displaying a task’s status.
- Stopping a running task.
- Editing a future task’s run time and output device.

# TaskMan: System Management—Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Kernel’s TaskMan module provides a standardized system for initiating and managing background processing. Since TaskMan handles all background processes, system managers have a unified set of controls that apply to all background processes on their systems.

Most of TaskMan’s processing does *not* involve interaction with users, rendering its operation virtually invisible. The explanations that follow provide information about the operation of TaskMan.

## TaskMan’s Division of Labor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

TaskMan uses a three-step system to start and manage background processing:

1.  Queuers

Foreground jobs *cannot* directly start any background jobs. Instead, they call the TaskMan Application Program Interface (API) to file requests in the TASKS (#14.4) and SCHEDULE files. The program code calling the TaskMan API is called a Queuer. The TASKS (#14.4) file is VA FileMan-compatible. The SCHEDULE file is *not* VA FileMan compatible.

![](kernel-8-0-systems-management-taskman-user-guide/006.png) REF: For a description of the TASKS (#14.4) and SCHEDULE file structure, see the “[Troubleshooting](#troubleshooting)” section in the “<u>TaskMan: System Management—Operation</u>” Section.

1.  Manager

The TaskMan manager program always runs in the background. The manager monitors the SCHEDULE file. As needed, it initiates background jobs (called submanagers) to perform the work requested by the foreground jobs.

2.  Submanagers

Each background job request is picked up by a TaskMan process called the submanager. The submanager is the job that runs each task. Submanagers handle contention for partitions and I/O devices by running the waiting tasks in order, first the oldest tasks and then the more recent ones.

### Queuers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Tasks run by TaskMan begin with code in a software application that decides to perform some work in the background. This code is a queuer. Most applications in VistA respond to a user’s request to queue some output, but other decisions may be involved. Two commonly used queuers are programs that create report output (by using the TaskMan API) and options that are scheduled through the OPTION SCHEDULING (#19.2) file.

#### Programs that Use the TaskMan API

One commonly used queuer is an application’s call to the TaskMan API to queue tasks. In this process the queuer defines the task and its environment. Applications are *not* allowed to do direct manipulation of the ^%ZTSCH and ^%ZTSK globals.

The TaskMan API consists of entry points that allow developers to create, manipulate, and inquire about tasks. The most widely used entry point, ^%ZTLOAD, lets developers queue tasks, which involves creating and scheduling them. First, an application sets the variables that ^%ZTLOAD needs to define the desired task. In turn, ^%ZTLOAD uses that information to create an entry in the TASKS (#14.4) file. ^%ZTLOAD then sets up a simple cross-reference to the new task in the SCHEDULE file, thereby finishing the queuing process.

After queuing the task, ^%ZTLOAD quits, returning control back to the queuer and leaving the next step in the process to the manager routines.

#### Option Scheduling through the OPTION SCHEDULING (#19.2) File

Another commonly used queuer is the OPTION SCHEDULING (#19.2) file. Menu Manager and TaskMan work together to allow certain options to be run as TaskMan tasks. These special options can be scheduled to run just once, or they can be set up to run over and over based on a rescheduling cycle. Such cycles can even include running the task whenever the computer system boots up.

### Manager

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

For tasks to run, at least one CPU in a configuration needs to run a manager. Only one manager process needs to run per CPU; the site determines how many CPUs should be configured to run a manager. The manager’s job is to route the tasks created by queuers. It normally always runs in the manager UCIs. It repeats the same loop of code all day long; every 2 seconds it looks for overdue tasks, every 15 seconds it checks the environment and performs some cleanup.

The environment check allows the system manager to control the manager even at its busiest. All commands to which the manager responds (described later) take effect here, between every task processed.

The manager looks for overdue tasks in the schedule list, comparing the current time to the start time of the tasks listed. If an overdue task is found, the manager removes it from the schedule list and inspects it. If the task is defined with a complete task record, the manager places it in a list of tasks ready to run. The manager places a task on one of several different lists depending on whether the task needs ownership of a currently unavailable I/O device. As its final step in processing each overdue task, the manager checks the number of submanagers available to process tasks and starts up new submanagers, if needed. The manager uses the JOB command (or %SPAWN if the manager is running in a DCL context on a Caché system).

The only variation on this scheme happens when the manager finds a task bound for a different Volume Set. Depending on the system configuration, such tasks may need to be run by the manager running on that other Volume Set. In this case, the current Volume Set’s manager copies the task over to the Volume Set on which the task should run and marks it as moved in the current TASKS (#14.4) file. In this process, the task is assigned a new task number, and the manager on that other Volume Set handles the task from there. If during this process the manager discovers that the link between the two Volume Sets has dropped, it saves the task in a list of tasks waiting for that Volume Set and checks periodically to see whether it has been restored. When the link recovers, the manager sends, in sequence, all waiting tasks to the other Volume Set.

The manager never actually runs the task but merely places it in a list as a task now available to be run by a submanager.

### Submanagers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Submanagers are the processes that run tasks. A manager starts submanagers whenever more are needed to handle the current workload of tasks, and they only last if they are needed. Submanagers loop back and forth between finding new tasks to run and running them.

To run each task, the submanager first removes the task from the list of waiting tasks on which it reside (such as the Job or the I/O list). Then it looks up the task’s entry in the TASKS (#14.4) file, unloading all information about the task. If the task needs a device, the submanager calls the Device Handler to get ownership of it and issues a USE command for it. Then the submanager sets up the partition for the task and does the following:

- Sets the priority.
- Cleans out unwanted variables.
- Sets up requested variables.
- Prints a page header on the device if one was requested.

Next, the submanager starts the task running at the task’s entry point. The submanager uses a DO command and runs the task’s entry point in its own partition. When the task finishes, the submanager cleans up after the task:

- Closes the output device.
- Performs any commands left for it by the task.

Running completely without user interaction, each task performs the work it was created to do and then quits, returning control to the submanager that started it. The task may leave instructions for its submanager, such as to requeue the task so that it runs again later or to delete the task’s entry from the TASKS (#14.4) file, but the task itself finishes before the submanager continues.

After submanagers have run all available tasks, they wait an interval before quitting. This period, called submanager retention time, allows the submanager to keep its partition open for new tasks for a while so that the manager need *not* start a new submanager. Every time a new task shows up during the retention time, the submanager starts its main loop over again, returning to retention again only after all new tasks have been run. When the submanagers eventually reach the end of their retention time, they quit.

<span id="_Toc193181817" class="anchor"></span>Figure 5: TaskMan Manager and Submanager Process Flow Diagram

![](kernel-8-0-systems-management-taskman-user-guide/007.png)

## TaskMan’s Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The two central files that facilitate task processing are:

- TASKS (#14.4) file
- SCHEDULE file (*not* VA FileMan-compatible)

TaskMan is configured by three configuration Files:

- VOLUME SET (#14.5)
- UCI ASSOCIATION (#14.6)
- TASKMAN SITE PARAMETERS (#14.7)

These files and the TaskMan routines fall within TaskMan’s namespace (ZTM) and numberspace. TaskMan user interface routines have been moved to the XUTM namespace beginning with Kernel 8.0 (they were previously in the ZTM namespace).

TaskMan also relies upon software components outside of its direct control. As an integral part of Kernel, TaskMan accesses several files controlled by other Kernel modules and calls many software entry points. TaskMan’s main external relation, however, is with VistA software applications through the queuers and the tasks they use.

### TaskMan Globals: ^%ZTSCH and ^%ZTSK

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ^%ZTSCH global holds the SCHEDULE file, and the ^%ZTSK global holds the TASKS (#14.4) file. Every environment controlled by a single manager needs each of these globals in its library UCI. % globals are used to make these files accessible to all UCIs in that environment so a single manager’s influence spans all those UCIs. When the environment spans Volume Sets, ^%ZTSCH and ^%ZTSK are translated across the Volume Sets included. They are never replicated because TaskMan updates them so frequently.

The ^%ZTSK global is mostly defined by VA FileMan (beginning with Kernel 8.0), but the ^%ZTSCH is not. Historically these globals were *not* VA FileMan-compatible. Now, the inquire, search, and print capabilities of VA FileMan can be used to study the TASKS (#14.4) file. At present, all edit access to these globals is restricted to the TaskMan options that edit the tasks in various ways.

![](kernel-8-0-systems-management-taskman-user-guide/008.png) REF: For a description of the structure of ^%ZTSCH and ^%ZTSK, see the “[Troubleshooting](#troubleshooting)” section in the “<u>TaskMan: System Management—Operation</u>” section.

### SCHEDULE File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The SCHEDULE file holds all lists and nodes that TaskMan uses to manage itself and to schedule tasks. Some of these lists are:

- Schedule List (or Time Queue)
- Waiting List (or IO Queue)
- Job List
- Compute Server Job List (or C List)
- Link List
- Status List
- Run Node
- TaskMan Error Log
- Error Screens

The SCHEDULE file‘s function is split between identifying the status of active tasks and of TaskMan itself.

![](kernel-8-0-systems-management-taskman-user-guide/009.png) REF: For more information on these lists, see the “<u>TaskMan: System Management—Operation</u>” section.

Most of the lists in the SCHEDULE file describe tasks, as follows:

- Schedule List—Sorts all scheduled tasks by time, according to when they are supposed to begin running.
- Waiting List—Stores each task whose running was delayed because its I/O device was busy.
- Job List—Holds those tasks that can begin running immediately.
- Link List—Stores tasks whose running is delayed because of a dropped link to another Volume Set.
- Task List—Describes all actively running tasks.
- Compute Server Job List—Describes all tasks waiting to start on a Compute Server (cross-CPU queuing).

The role of tracking the status of TaskMan itself is split between lists of information and individual nodes and flags. The Status List is where the manager keeps track of its current condition; it is a list because system administrators may choose to run more than one manager in the same TaskMan environment. The RUN node is a place where TaskMan stamps the current time; this node reveals when TaskMan stops running. The TaskMan Error Log is a simple list in which TaskMan stores each error that occurs either within TaskMan itself or within the tasks that it runs. The Error Screens are screens that can be established by system administrators to prevent the recording of certain errors.

These lists and nodes, as well as others *not* described here, are the primary data structures that TaskMan uses to schedule and run tasks.

### TASKS (#14.4) File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The TASKS (#14.4) file, unlike the SCHEDULE file, contains the tasks themselves.

Every task run by TaskMan is described by an entry in the TASKS (#14.4) file. Each entry is subscripted by a unique internal number, and ^%ZTSK(-1) always equals the number of the most recently created task. The lists and nodes in ^%ZTSCH store the tasks’ numbers that are scheduled to run. Each task’s entry consists of a ^%ZTSK(task \#, 0) node that contains most of the essential information about the task, several decimal nodes (.1, .2, .25, and .26) that store the remainder of the critical information, and several storage nodes under ^%ZTSK(task#,.3) that store the names and values of parameters that TaskMan creates for the task. Left unchecked, this file tends to grow.

![](kernel-8-0-systems-management-taskman-user-guide/010.png) REF: For a description of the various means of controlling this growth, see the “<u>TaskMan: System Management—Operation</u>” section.

### Other Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The TASKS (#14.4) and SCHEDULE files, taken together, describe all information about tasks on the system. A few more files are needed, however, to describe everything about how tasks are managed on the system.

The following three files are stored in ^%ZIS:

- VOLUME SET (#14.5) file—Describes the computer system’s Volume Sets and how they are configured into TaskMan environments.
- UCI ASSOCIATION (#14.6) file—Lists all UCIs on the system and which Volume Sets they belong to. In more complicated systems, it is also used to describe how the UCIs in different environments correspond with one another.
- TASKMAN SITE PARAMETERS (#14.7) file—Lets the system manager divide up the environments by both CPU and Volume Set. This allows a fine degree of control over such parameters as priority, partition size, and retention time.

Taken together, these files give system administrators precise and powerful control over TaskMan’s behavior.

Other minor pieces of information are scattered throughout other Kernel files, especially the DEVICE (#3.5) and OPTION SCHEDULING (#19.2) files.

## System Configuration Terminology

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

TaskMan operates close to the level of the system architecture. It *must* be capable of starting tasks in all environments within a computer system. This means it *must* know about those environments; consequently, the options, routines, files, and documentation somehow *must* refer to that architecture.

One problem presented by system configuration is terminology. Such system architecture features as UCIs, directories, Volume Sets, and namespaces are *not* part of the ANSI M standard, so different vendors use different terminology. Although it would be ideal for Kernel to use a universal terminology, none exists. For historical reasons, Kernel has settled on a terminology based on that of DSM-11 that includes the terms in <u>Table 1</u>:

| Term                   | Definition                                                                                                                                                                                                                                                                      |
|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UCI                | User Class Identifier. This is roughly equivalent to a “directory” or an “account”. A UCI refers to the environment limited to a particular set of routines and globals. In Caché terms, this is a “namespace.”                                                                 |
| Manager UCI        | Roughly equivalent to a “system UCI” or a “library UCI.” This is where the vendor’s system management routines are kept and where all %-namespaced routines and globals reside. Currently, all Kernel % routines and globals are mapped back to the Production account. |
| Volume Set         | On current systems, you just set this to the string “ROU”. This is the critical definition, since this is what affects how TaskMan starts background jobs.                                                                                                                  |
| CPU                | Also known as a “node” or “computer”, this designates a source of computing power and partitions. It is used both for controlling TaskMan’s behavior with parameters and for sending tasks to specific CPUs.                                                                    |
| Mounted Volume Set | Obsolete; no longer used.                                                                                                                                                                                                                                                       |

<span id="_Ref29376960" class="anchor"></span>Table 2: TASKMAN SITE PARAMETERS (#14.7) File—Field Entries

![](kernel-8-0-systems-management-taskman-user-guide/011.png) NOTE: The TaskMan topics in this section make use of this terminology.

## TaskMan Security Key

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The TaskMan module comes with one security key, ZTMQ. The ZTMQ security key does *not* completely lock any options. Instead, it affects the behavior of the following three options:

- Dequeue Tasks \[XUTM DQ\]
- Requeue Tasks \[XUTM REQ\]
- Delete Tasks \[XUTM DEL\]

Those who use these options without holding the ZTMQ security key can manipulate only their own tasks. Only the holder of the ZTMQ security key can use these options to manipulate any task on the system.

# TaskMan: System Management—Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section discusses the many issues surrounding the configuration of TaskMan.

## Defining TaskMan Environments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The part of configuring TaskMan for a system that requires the most creativity is deciding how to divide the system’s UCIs, Volume Sets, and CPUs into TaskMan environments. A TaskMan environment is the collection of UCIs from which entries can be made directly into a given manager’s TASKS (#14.4) and SCHEDULE files and that are within that manager’s reach. This requires looking at the system in terms of queuing and starting tasks. There are several options available. Many different configurations are possible.

One type of configuration has CPUs sharing the same Volume Set. Since this type of environment shares a single Volume Set among multiple CPUs, they also share a single TASKS (#14.4) and SCHEDULE file. However, the reach of managers *cannot* span CPUs. Therefore, you *must* decide which CPUs in that environment run managers, or whether some of them should rely on the other CPUs to run their tasks for them. Alpha clusters in VA are typically configured with managers on only one or a few CPUs.

A different configuration allows you to limit the number of places TaskMan runs. In this scenario, you pick certain CPUs to run TaskMan and give them managers and files to do the job. To have background processing support, the remaining Volume Sets need to be able to queue to one of the managers on the system. This entails translating the TASKS (#14.4) and SCHEDULE files of that manager, so they are visible to the unsupported Volume Set. To tell TaskMan that the one Volume Set runs no tasks but is instead supported by the other, you *must* configure the VOLUME SET (#14.5) file as described later in this section.

Another possible configuration is to allow tasks to run everywhere, which requires that you place managers within reach of every UCI and that you define your TaskMan environments accordingly. Under this configuration every CPU needs its own manager, and its own TASKS (#14.4) and SCHEDULE files.

One other configuration to keep in mind, of course, is to have a standalone environment disconnected from the rest of the computer system. Such environments make excellent test areas for developers. They are configured the same regardless of the configuration of the main system.

## Configuring TaskMan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

TaskMan’s three configuration files *must* be setup to properly reflect your system’s layout. The three files are:

- TASKMAN SITE PARAMETERS (#14.7)
- VOLUME SET (#14.5)
- UCI ASSOCIATION (#14.6)

### Edit TaskMan Parameters Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following three options on the Edit TaskMan Parameters \[XUTM PARAMETER EDIT\] menu allow you to edit each of the three configuration files:

- Site Parameters Edit \[XUTM BVPAIR\]

![](kernel-8-0-systems-management-taskman-user-guide/012.png) REF: For more information on the Site Parameters Edit \[XUTM BVPAIR\] option and the TASKMAN SITE PARAMETERS (#14.7) file, see the “[TASKMAN SITE PARAMETERS (#14.7) File](#taskman-site-parameters-14.7-file)” section.

- UCI Association Table Edit \[XUTM UCI\]

![](kernel-8-0-systems-management-taskman-user-guide/013.png) REF: For more information on the UCI Association Table Edit \[XUTM UCI\] option and the VOLUME SET (#14.5) file, see the “[UCI ASSOCIATION (#14.6) File](#uci-association-14.6-file)” section.

- Volume Set Edit \[XUTM VOLUME\]

![](kernel-8-0-systems-management-taskman-user-guide/014.png) REF: For more information on the Volume Set Edit \[XUTM VOLUME\] option and the UCI ASSOCIATION (#14.6) file, see the “[VOLUME SET (#14.5) File](#volume-set-14.5-file)” section.

Because the TASKMAN SITE PARAMETERS (#14.7) allows you to define parameters (such as TaskMan Job Limit) separately for each CPU on your system; you can optimize TaskMan’s behavior individually for each CPU.

You no longer need to stop and then restart TaskMan to change the TASKMAN JOB LIMIT on a CPU. Cross-references on the relevant fields locate every TaskMan on your system and inform them that they need to update their TaskMan parameter information. Thus, within a minute or so of making the changes, TaskMan on that CPU should be operating with the new value.

### TaskMan’s Reach

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The key issue that defines TaskMan’s configuration is its “reach,” those places where TaskMan can start background jobs. TaskMan’s reach extends to:

- All UCIs a submanager can access directly after using Kernel’s UCI switching facilities.
- All other managers TASKS (#14.4) and SCHEDULE files to which a given manager can WRITE using extended global reference.
- All UCIs on Print Servers with link access to the current Volume Set.

TaskMan’s reach does *not* include other sites on a wide area network, because they *cannot* be accessed through either UCI switching or through extended global reference. There are ways to simulate such a reach using server options, however. For purposes of TaskMan configuration, you generally think in terms of the reach of a single manager, which can only run tasks in the UCIs it can reach.

### TASKMAN SITE PARAMETERS (#14.7) File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc193181819" class="anchor"></span>Figure 6: Site Parameters Edit Option

SYSTEMS MANAGER MENU ... \[EVE\]

Task Manager ... \[XUTM MGR\]

Taskman Management Utilities ... \[XUTM UTIL\]

Edit Taskman Parameters ... \[XUTM PARAMETER EDIT\]

<span class="mark">Site Parameters Edit</span> \[XUTM BVPAIR\]

System managers *must* enter one set of site parameters into the TASKMAN SITE PARAMETERS (#14.7) file for each manager that runs in a different Volume Set/CPU.

<u>Table 2</u> lists the set of parameters that tells each manager how it should process tasks. The parameters are organized both by Volume Set and by CPU. This allows two CPUs that share a Volume Set to be treated differently if one is more powerful than the other.

<table>
<caption><p><span id="_Toc204581344" class="anchor"></span>Table 3: VOLUME SET (#14.5) File—Field Entries</p></caption>
<colgroup>
<col style="width: 42%" />
<col style="width: 57%" />
</colgroup>
<thead>
<tr class="header">
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>BOX-VOLUME PAIR (#.01)</td>
<td><p>The BOX-VOLUME PAIR field identifies a Volume Set and the CPU on which it is available. It contains the name of a Volume Set concatenated to the CPU (“box”) name: first the Volume Set name and then the CPU name. For example, if the Volume Set name is “<strong>KRN</strong>” and the name of the CPU (such as box) is “<strong>ABC999</strong>,” then the BOX-VOLUME PAIR would be “<strong>KRN:ABC999</strong>.”</p>
<p>For systems on which each CPU tends to have a unique Volume Set and vice versa, you can enter just the Volume Set name (such as “<strong>PSA</strong>” or “<strong>AAA</strong>”). This field’s value for the current process can be found by doing <strong>GETENV^%ZOSV</strong> and checking the fourth <strong>^</strong>-piece of <strong>Y</strong>. Since the Volume Set and CPU are identified, the TaskMan site parameters can be tuned for each specific Volume Set and CPU affected. Systems running managers on more than one CPU need one entry for each CPU where a manager is running.</p></td>
</tr>
<tr class="even">
<td>LOG TASKS? (#2)</td>
<td>Set the LOG TASKS? field to <strong>YES</strong> to make tasks log in and out through the signon log the way interactive users do. How to set this is up to the individual site; it does consume space and resources.</td>
</tr>
<tr class="odd">
<td>TASK PARTITION SIZE (#4)</td>
<td>The TASK PARTITION SIZE field is used to assign partition sizes for tasks. The value from this field is plugged directly into the <strong>JOB</strong> command used to create new submanagers. If this field is left blank, all tasks receive the operating system’s current default value. This field should only be used by system managers who thoroughly understand how their vendor’s version of M handles partition sizes with the <strong>JOB</strong> command.</td>
</tr>
<tr class="even">
<td>SUBMANAGER RETENTION TIME (#5)</td>
<td>The SUBMANAGER RETENTION TIME number determines how many seconds submanagers should wait while looking for new tasks. The purpose of this field is to reduce the number of <strong>JOB</strong> commands needed to process a site’s tasks. By keeping old submanagers around to run new tasks, new process creation is significantly reduced.</td>
</tr>
<tr class="odd">
<td>TASKMAN JOB LIMIT (#6)</td>
<td>If there are more active processes on the system than the number stored in the TASKMAN JOB LIMIT field, TaskMan does <em>not</em> create new submanagers to handle tasks. Task processing is left to existing submanagers until the number of processes falls back below this number. This number should be slightly lower than the MAX SIGNON ALLOWED (#41,2) field of the VOLUME SET (#41) Multiple field in the KERNEL SYSTEM PARAMETERS (#8989.3) file so that the system manager still has room to sign on when TaskMan is using its greatest number of partitions.</td>
</tr>
<tr class="even">
<td>TASKMAN HANG BETWEEN NEW JOBS (#7)</td>
<td><p>The TASKMAN HANG BETWEEN NEW JOBS field sets a delay between the creation of new submanagers, in <strong>seconds</strong>. It is useful as a throttle. For systems, this delay spaces out the use of the <strong>JOB</strong> command to avoid slowing users’ response time when the manager needs to JOB off many new processes in rapid succession.</p>
<p>For systems that create new processes cheaply, this delay is unnecessary. This delay also becomes less important when a high submanager retention time is used since higher retention times reduce the likelihood that TaskMan needs to create new processes.</p>
<p>Be sure <em>not</em> to combine a high <strong>TASKMAN HANG BETWEEN NEW JOBS</strong> value with a low <strong>SUBMANAGER RETENTION TIME</strong> value, since that increases the number of jobs per day TaskMan must start and can cause busy systems to fall behind. The number should be the lowest value that prevents the problem and can be left blank for systems with efficient <strong>JOB</strong> commands.</p></td>
</tr>
<tr class="odd">
<td>MODE OF TASKMAN (#8)</td>
<td><p>The MODE OF TASKMAN field determines how each CPU (BOX-VOLUME pair entry) should process tasks. You can set it to one of four values:</p>
<ul>
<li><p><strong>General Processor (“G”):</strong> The <strong>G</strong> type should be selected when the TASKS (#14.4) and Scheduling files are seen by only one Volume Set. For example, VA’s Alpha clusters have several CPUs, but each of them runs on the same Volume Set. The manager on a <strong>G</strong> type runs tasks created on the same Volume Set and tasks from any other Volume Set that explicitly requests the <strong>G</strong> type’s Volume Set. The <strong>G</strong> type sends tasks from another Volume Set that did <em>not</em> explicitly request its Volume Set back to the originating Volume Set, however.<br />
<br />
To transfer tasks to a <strong>G</strong> type, TaskMan uses extended global references to copy the task to the destination TASKS (#14.4) and Scheduling files and then removes the task from its own side. Submanagers started on a <strong>G</strong>-type processor process tasks in the Partition Waiting List and the Busy Device Waiting List.</p></li>
<li><p><strong>Print Server (“P”):</strong> The <strong>P</strong> type should be selected when multiple Volume Sets map to the same TASKS (#14.4) and Scheduling files, and you want to run the manager on the Volume Set/CPU in question.<br />
<br />
Like the <strong>G</strong> type, the manager on a <strong>P</strong> type runs tasks created on the same Volume Set and tasks from any other Volume Set/CPU that explicitly request the <strong>P</strong> type’s Volume Set/CPU. Unlike the <strong>G</strong> type, however, the <strong>P</strong> type also runs tasks from other Volume Sets that did <em>not</em> make an explicit Volume Set request. Tasks are transferred to a <strong>P</strong> type in the same way as to a <strong>G</strong> type, and submanagers behave the same.</p></li>
<li><p><strong>Compute Server (“C”):</strong> The <strong>C</strong> type should be selected when multiple Volume Sets map to the same TASKS (#14.4) and Scheduling files (as with the <strong>P</strong> type), but when the Volume Set/CPU in question runs users (<em>not</em> tasks). The manager does <em>not</em> start on a <strong>C</strong> type. Tasks that explicitly request to run on a <strong>C</strong> type are transferred to it by being placed in the Link Waiting List; a submanager is then jobbed across to the <strong>C</strong> type Volume Set/CPU. Submanagers started on a <strong>C</strong> type only process tasks in the Link Waiting List for their Volume Set.</p></li>
<li><p><strong>Other Non-TaskMan (“O”):</strong> Neither the manager nor the submanager runs on <strong>O</strong> types. Tasks sent from or to an <strong>O</strong> type are rejected.</p></li>
</ul>
<p>Because of the field’s crucial role in guiding TaskMan’s behavior, the field is required.</p></td>
</tr>
<tr class="even">
<td>VAX ENVIRONMENT FOR DCL (#9)</td>
<td><p>The VAX ENVIRONMENT FOR DCL field only has meaning to DSM for OpenVMS and Caché systems. It is set to the OpenVMS username of the DSM environment manager account. Setting it to this username causes the manager to use <strong>%SPAWN</strong> to SUBMIT submanagers to run. This method requires certain DCL command files exist, along with a TASKMAN OpenVMS user account and directory.</p>
<p>![](kernel-8-0-systems-management-taskman-user-guide/015.png) <strong>REF:</strong> For descriptions of the needed setups, see the “<a href="#running-taskman-with-a-dcl-context">Running TaskMan with a DCL Context</a>” section.</p>
<p>If the field is empty, the manager starts submanagers with the <strong>JOB</strong> command instead.</p></td>
</tr>
<tr class="odd">
<td>LOAD BALANCE ROUTINE (#21)</td>
<td><p>If you are running multiple managers (one per node), use the LOAD BALANCE ROUTINE field to set up load balancing between the managers on each node. It should be set to the name of an extrinsic function that returns a load rating for the node.</p>
<p>![](kernel-8-0-systems-management-taskman-user-guide/016.png) <strong>REF:</strong> For more information on load balancing, see the “<a href="#multiple-taskman-managers-and-load-balancing">Multiple TaskMan Managers and Load Balancing</a>” section.</p></td>
</tr>
</tbody>
</table>

<span id="_Toc204581344" class="anchor"></span>Table 3: VOLUME SET (#14.5) File—Field Entries

### VOLUME SET (#14.5) File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc193181820" class="anchor"></span>Figure 7: Volume Set Edit Option

SYSTEMS MANAGER MENU ... \[EVE\]

Task Manager ... \[XUTM MGR\]

Taskman Management Utilities ... \[XUTM UTIL\]

Edit Taskman Parameters ... \[XUTM PARAMETER EDIT\]

<span class="mark">Volume Set Edit</span> \[XUTM VOLUME\]

TaskMan knows about a system’s configuration from the values entered into the VOLUME SET (#14.5) file using the Volume Set Edit \[XUTM VOLUME\] option. The information stored in this file strongly affects TaskMan’s behavior. If you inaccurately describe your system, you usually notice very quickly as TaskMan begins processing tasks in a consistently incorrect way.

You need to make one entry in this file for each Volume Set that tasks can be queued to or from. These entries are only used when:

- A manager is running on the Volume Set and *must* look up information about its own environment.
- The Volume Set is a required volume; in which case every manager *must* check access to it when they start up.
- A task needs to run on the Volume Set; in which case the manager *must* look up how to get the task there.

<u>Figure 8</u> shows what is set up for FORUM:

<span id="_Ref26361965" class="anchor"></span>Figure 8: Sample Volume Set Setup on FORUM

VOLUME SET (14.5)

VOLUME SET: ROU INHIBIT LOGONS?: NO

LINK ACCESS?: NO TASKMAN FILES UCI: VAH

DAYS TO KEEP OLD TASKS: 1 TYPE: GENERAL PURPOSE VOLUME SET

SIGNON/PRODUCTION VOLUME SET: Yes

UCI ASSOCIATION (14.6)

Empty

TASKMAN SITE PARAMETERS (14.7 )

BOX-VOLUME PAIR: ROU:FORFORUM1 LOG TASKS?: NO

SUBMANAGER RETENTION TIME: 60 TASKMAN JOB LIMIT: 400

TASKMAN HANG BETWEEN NEW JOBS: 1 MODE OF TASKMAN: GENERAL PROCESSOR

OUT OF SERVICE: NO MIN SUBMANAGER CNT: 10

LOAD BALANCE ROUTINE: \$\$CACHE1() Auto Delete Tasks: Yes

Manager Startup Delay: 30

The value of ^%ZOSF(“VOL”) is FOR.

<table>
<caption><p><span id="_Ref240794218" class="anchor"></span>Table 4: UCI ASSOCIATION (#14.6) File—Partial and Complete Field Entries</p></caption>
<colgroup>
<col style="width: 42%" />
<col style="width: 57%" />
</colgroup>
<thead>
<tr class="header">
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>VOLUME SET (#.01)</td>
<td>The VOLUME SET field should be set to the name of a Volume Set. It is used in extended global references to reach this Volume Set and can be used in UCI-switching software to move submanagers between UCIs. If you are unsure how your Volume Sets are named, you can look at the value of <strong>^%ZOSF(“VOL”)</strong> in the Volume Set in question.</td>
</tr>
<tr class="even">
<td>TYPE (#.1)</td>
<td><p>The TYPE field is used to help resolve where tasks should run; it should properly identify the type of the Volume Set. Typically, it should be set to the same value as the MODE OF TASKMAN (#8) field for all BOX-VOLUME PAIRs associated with this Volume Set, in the TASKMAN SITE PARAMETERS (#14.7) file. This field <em>must</em> be filled in for all Volume Sets. This field can have the following values:</p>
<ul>
<li><p><strong>G—</strong>GENERAL PURPOSE VOLUME SET</p></li>
<li><p><strong>P—</strong>PRINT SERVER</p></li>
<li><p><strong>C—</strong>COMPUTE SERVER</p></li>
<li><p><strong>O—</strong>OTHER NON-TASKMAN VOLUME SET</p></li>
</ul>
<p>These values have the same meanings as the equivalent values for the MODE OF TASKMAN (#8) field in the TASKMAN SITE PARAMETERS (#14.7) file, as described previously in the “<a href="#taskman-site-parameters-14.7-file">TASKMAN SITE PARAMETERS (#14.7) File</a>” section. GENERAL PURPOSE VOLUME SET for Volume Sets is the rough equivalent of the MODE OF TASKMAN value GENERAL PROCESSOR for BOX-VOLUME PAIRs.</p>
<p>![](kernel-8-0-systems-management-taskman-user-guide/017.png) <strong>NOTE:</strong> The <strong>FILE SERVER</strong> value has been removed; Volume Sets for File Servers should be set to a TYPE of <strong>OTHER NON-TASKMAN VOLUME SET</strong>.</p></td>
</tr>
<tr class="odd">
<td>INHIBIT LOGONS? (#1)</td>
<td>Setting the INHIBIT LOGONS? field to <strong>YES</strong> causes TaskMan to notify Signon that logons are now prohibited and to enter a <strong>PAUSE</strong> state (stopping processing of tasks) until logons are allowed again. Under ordinary circumstances, system managers should leave this field as <strong>NULL</strong> or <strong>NO</strong>.</td>
</tr>
<tr class="even">
<td>LINK ACCESS (#2)</td>
<td><p>The LINK ACCESS field should always be set to <strong>NULL</strong> or <strong>YES</strong> for the usual kinds of configurations used in VistA. Answer <strong>NO</strong> to tell TaskMan that this Volume Set <em>cannot</em> be accessed by other Volume Sets using the local network links. Tasks that request a Volume Set without link access are rejected by TaskMan. Such Volume Sets are usually PC workstations linked into the larger network. They can access the core computers but <em>cannot</em> be accessed themselves.</p>
<p>Some system managers may wish to have a completely isolated computer for testing. They can cut it off from the rest of the world by making entries for all other Volume Sets and setting this field to <strong>NO</strong> for each of them. This explicitly tells TaskMan it <em>cannot</em> reach the other Volume Sets.</p></td>
</tr>
<tr class="odd">
<td>OUT OF SERVICE? (#3, Obsolete, see TYPE field)</td>
<td>The OUT OF SERVICE? field is obsolete and should only be set to <strong>NULL</strong>; use the TYPE (#.1) field.</td>
</tr>
<tr class="even">
<td>REQUIRED VOLUME SET? (#4, Obsolete)</td>
<td>The REQUIRED VOLUME SET? field is obsolete and should only be set to <strong>NULL</strong>.</td>
</tr>
<tr class="odd">
<td>TASKMAN FILES UCI (#5)</td>
<td>The TASKMAN FILES UCI field should be set to the name of the UCI that holds the <strong>^%ZTSCH</strong> and <strong>^%ZTSK</strong> globals (usually the manager UCI). The answer should <em>not</em> contain a comma and Volume Set name (such as <strong>VAH,PSA</strong>), just the UCI name (such as <strong>VAH</strong>). This field is required.</td>
</tr>
<tr class="even">
<td>TASKMAN FILES VOLUME SET (#6)</td>
<td><p>The TASKMAN FILES VOLUME SET field should be set to the name of the Volume Set that holds <strong>^%ZTSCH</strong> and <strong>^%ZTSK</strong>.</p>
<p>A <strong>NULL</strong> value means this Volume Set holds its own TaskMan files, which is usually the case.</p></td>
</tr>
<tr class="odd">
<td>REPLACEMENT VOLUME SET (#7)</td>
<td>The REPLACEMENT VOLUME SET field should be set to the name of a Volume Set to which tasks can be sent if this Volume Set is unavailable. A REPLACEMENT VOLUME SET should be essentially equivalent in features to the current one, since tasks that would normally run on the current one are running on the REPLACEMENT VOLUME SET instead. For many Volume Sets, no other Volume Set is equivalent, and tasks should wait for the link to be restored rather than run elsewhere. If tasks that need this Volume Set should wait, leave the field blank.</td>
</tr>
<tr class="even">
<td>DAYS TO KEEP OLD TASKS (#8)</td>
<td>The number stored in the DAYS TO KEEP OLD TASKS field is used by the <strong>Queuable Task Log Cleanup</strong> [XUTM QCLEAN] option to decide which tasks to delete. The decision only affects inactive tasks, as explained in the discussion of the <strong>Queuable Task Log Cleanup</strong> [XUTM QCLEAN] option. Values in this field <em>cannot</em> inadvertently cause TaskMan to delete scheduled or running tasks. If the field contains no value, <strong>XUTM QCLEAN</strong> keeps the last seven days’ tasks. A value of <strong>0</strong> here keeps your file very clean.</td>
</tr>
</tbody>
</table>

<span id="_Ref240794218" class="anchor"></span>Table 4: UCI ASSOCIATION (#14.6) File—Partial and Complete Field Entries

### UCI ASSOCIATION (#14.6) File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc193181822" class="anchor"></span>Figure 9: UCI Association Table Edit Option

SYSTEMS MANAGER MENU ... \[EVE\]

Task Manager ... \[XUTM MGR\]

Taskman Management Utilities ... \[XUTM UTIL\]

Edit Taskman Parameters ... \[XUTM PARAMETER EDIT\]

<span class="mark">UCI Association Table Edit</span> \[XUTM UCI\]

There are two different kinds of entries made into the UCI ASSOCIATION (#14.6) file using the UCI Association Table Edit \[XUTM UCI\] option:

- [Partial File Entries](#partial-file-entries)
- [Complete File Entries](#complete-file-entries)

#### Partial File Entries

File entries with the following first two fields filled in identify the valid UCIs on the system for TaskMan:

- FROM UCI (<u>Table 4</u>)
- FROM VOLUME SET (<u>Table 4</u>)

Every VistA site needs one entry of this type for each UCI to which tasks can be queued or from which tasks are created.

![](kernel-8-0-systems-management-taskman-user-guide/018.png) NOTE: Caché sites only need to fill in these first two fields.

![](kernel-8-0-systems-management-taskman-user-guide/019.png) REF: For a sample configuration, see the “[Sample Configuration: Standardized VA Caché and GT.M Configuration](#sample-configuration-standardized-va-caché-and-gt.m-configuration)” section.

#### Complete File Entries

File entries with all four fields (<u>Table 4</u>) completed collectively build a UCI ASSOCIATION TABLE.

A complete UCI ASSOCIATION TABLE tells TaskMan which UCI to use for tasks that *must* switch Volume Sets to reach an I/O device. This situation arises when an I/O device is in a different Volume Set than the Volume Set where the task was created. In such situations, the manager knows exactly where the task originated and knows to which Volume Set it *must* be moved, but it does *not* know in which UCI on that Volume Set it should run the task. A UCI ASSOCIATION TABLE entry supplies the missing information by linking equivalent UCIs together. When building a full UCI ASSOCIATION TABLE, you can omit entries where the UCIs on both Volume Sets have the same name because TaskMan assumes that same-named UCIs are equivalent if no entry is present.

<table>
<caption><p><span id="_Toc204581346" class="anchor"></span>Table 5: DEVICE (#3.5) file—TaskMan-related Field Entries</p></caption>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>FROM UCI (#.01)</td>
<td><p>The FROM UCI field should be set to the name of a UCI on your system. Enter only the UCI name (such as <strong>VAH</strong>). Do <em>not</em> include the Volume Set name (such as <strong>VAH,ROU</strong>).</p>
<ul>
<li><p>For entries requiring only two fields, this catalogs all UCIs on your system (and there should be an entry for each).</p></li>
<li><p>For four-field entries, this represents a UCI from which tasks are being transferred to reach their <strong>I/O</strong> device.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>FROM VOLUME SET (#1)</td>
<td><p>The FROM VOLUME SET field should be set to the name of the Volume Set that holds the UCI identified in the entry’s FROM UCI (#.01) field. Every Volume Set listed in this field should be described in the VOLUME SET (#14.5) file.</p>
<p>For four-field entries, this represents the Volume Set from which tasks are being transferred to reach their <strong>I/O</strong> device.</p></td>
</tr>
<tr class="odd">
<td>TO VOLUME SET (#2)</td>
<td>The TO VOLUME SET field is only used for entries that build a UCI Association Table. For such entries, it should be the name of the Volume Set to which tasks are being transferred to reach their <strong>I/O</strong> devices.</td>
</tr>
<tr class="even">
<td>TO UC (#3)I</td>
<td>As with TO VOLUME SET(#2), the TO UCI field is only used for entries that build a UCI Association Table. For such entries, it should be the name of the UCI to which tasks are transferred whenever they <em>must</em> be moved from the UCI on the first Volume Set to the second Volume Set to reach their <strong>I/O</strong> devices. As with the From UCI field, the Volume Set name should <em>not</em> be included.</td>
</tr>
</tbody>
</table>

<span id="_Toc204581346" class="anchor"></span>Table 5: DEVICE (#3.5) file—TaskMan-related Field Entries

### Sample Configuration: Standardized VA Caché and GT.M Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Sites that run managers on their satellites should make the appropriate TASKMAN SITE PARAMETERS (#14.7) file entries for each satellite and adjust their TaskMan Job Limit to reflect each satellite’s individual capacity.

<span id="_Toc193181823" class="anchor"></span>Figure 10: VOLUME SET (#14.5) File Standardized VA Caché and GT.M Configuration

VOLUME SET You need one entry, for ROU

TYPE GENERAL PURPOSE VOLUME SET

INHIBIT LOGONS? Blank or NO

LINK ACCESS? Blank or NO

OUT OF SERVICE? Blank or NO

REQUIRED VOLUME SET? Blank or NO

TASKMAN FILES UCI VAH

TASKMAN FILES VOLUME SET Leave this blank

REPLACEMENT VOLUME SET Leave this blank

DAYS TO KEEP OLD TASKS Up to you; can leave blank

SIGNON/PRODUCTION VOLUME SET Yes

<span id="_Toc193181824" class="anchor"></span>Figure 11: UCI ASSOCIATION (#14.6) File—Standardized VA Caché and GT.M Configuration

FROM UCI 1 entries: VAH

FROM VOLUME SET ROU

TO VOLUME SET Blank

TO UCI Blank

![](kernel-8-0-systems-management-taskman-user-guide/020.png) NOTE: You can leave this empty.

<span id="_Toc193181825" class="anchor"></span>Figure 12: TASKMAN SITE PARAMETERS (#14.7) File Standardized VA Caché and GT.M Configuration

BOX-VOLUME PAIR ROU:FORFORUM1

Your answer should be the volume set name

concatenated with the ":" concatenated with

the name of the Cache Configuration.

LOG TASKS? Blank or NO (unless TaskMan is running in a

DCL context, in which case set to YES)

DEFAULT TASK PRIORITY Blank

TASK PARTITION SIZE Blank

SUBMANAGER RETENTION TIME 60

TASKMAN JOB LIMIT 400 (2-5 lower than Max Signons)

TASKMAN HANG BETWEEN NEW JOBS 1

MODE OF TASKMAN GENERAL PROCESSOR

ENVIRONMENT FOR DCL Blank

OUT OF SERVICE Blank

MIN SUBMANAGER CNT 2

LOAD BALANCE ROUTINE Blank

Auto Delete Tasks Yes

Manager Startup Delay 30

## Manager Startup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You may want to configure your system so that, on CPUs where the manager should run, a manager starts up every time the CPU starts up. Otherwise, you need to manually start up the manager each time you start up those nodes that should run the manager.

For most sites, only one manager is needed to cover each environment. Therefore, this section focuses on starting up only a single manager.

Neither the manager nor the submanagers starts up on a BOX-VOLUME PAIR pair of the wrong type, so pay attention to how you fill in the MODE OF TASKMAN field of the TASKMAN SITE PARAMETERS (#14.7) file. If you want the manager to start, you *must* make sure this field is set to either a Print Server or a General Processor.

Getting the manager to start up when the system does is accomplished in the VA by the ZSTU routine in the %SYS namespace. This routine is provided by Enterprise Product Support (EPS).

## Multiple TaskMan Managers and Load Balancing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

TaskMan supports the running of multiple manager processes; however, only one manager process should run per CPU. Running multiple managers is probably useful only at large sites; at a large site, doing this can enable tasks to be processed more quickly than if only one CPU runs a manager. A bonus with multiple managers is that if one CPU running a manager becomes unavailable, managers still run on the other CPUs, with no further re-configuration required.

### Configuration for Multiple Managers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Each node that runs a TaskMan manager *must* have its own entry (BOX-VOLUME PAIR) in the TASKMAN SITE PARAMETERS (#14.7) file.

Each CPU *must* share access to a common ^%ZTSK and ^%ZTSCH global and have access to the same devices. Because of this, all CPUs *must* run the same M implementation.

### Starting Up, Pausing, and Stopping Multiple Managers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You need to start a manager on each CPU where a manager should run. Whatever steps you follow to start a single manager, you need to repeat for any additional nodes on which you want to run additional managers.

The options that place TaskMan in a WAIT state and stop TaskMan are *not* CPU-specific; they affect all running managers across the system.

### Load Balancing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The LOAD BALANCE ROUTINE field in the TASKMAN SITE PARAMETERS (#14.7) file holds the name of a function that returns a CPU’s load rating. This field is only useful if you are running multiple TaskMan managers.

To use load balancing, enter a routine name in the LOAD BALANCE ROUTINE field for each participating CPU’s BOX-VOLUME PAIR entry. Kernel patch XU\*8.0\*355 added the following routine for TaskMan load balancing in Caché:

\$\$CACHE2(@com-file,logical-name) in ^ZTM6

If the com-file value is set, that com-file runs each time TaskMan gets the balance value. The logical-name defaults to VISTA\$METRIC or uses the value entered. The normal way would be to have \$\$CACHE2() in the field and use the following two scripts:

- GET_METRIC.COM—This script sets the logical “VISTA\$METRIC.” It can be run by TaskMan or from the TM\$*\<node\>* batch queue with the METRIC_SCHEDULE.COM script.
- METRIC_SCHEDULE.COM—This script takes a parameter of the number of seconds to reschedule itself. It defaults to 15 seconds and runs under the “SYSTEM” user.

![](kernel-8-0-systems-management-taskman-user-guide/021.png) NOTE: These scripts are in the same directory as the TaskMan in DCL files.  
  
Use of TaskMan in DCL is optional.

It is all right to run multiple TaskMan managers without using load balancing; it is also all right if load balancing is set up and only one manager is running (that manager automatically takes all jobs itself). If one manager’s CPU has the LOAD BALANCE ROUTINE field filled in and another running manager’s CPU does not, the managers acts as if no load balancing is taking place. In short, the only ramification from various combinations of managers with the LOAD BALANCE ROUTINE field filled in or not is that load balancing might *not* take place.

The load balancing routine *must* be an extrinsic function that returns a positive value. The CPU with the highest value is the one that runs new tasks.

Cache Algorithms:

- \$\$Cache2()—Returns the TCPIP metric.
- \$\$Cache1()—Returns the Available jobs.

Each CPU performing load balancing compares its current CPU capacity with that of the other nodes running managers. If the current CPU has a lower rating than the other CPUs, it puts itself in a BALANCE state and waits to let the other CPUs take up the load before running more jobs itself.

Submanagers try and wait until there node is running before testing if they should exit.

### Monitor Taskman Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

On a system where multiple managers are running, the Monitor Taskman \[XUTM ZTMON\] option shows a combined view of the operation of multiple managers.

If the current node (the one where you are running the Monitor Taskman \[XUTM ZTMON\] option) has a lower rating than other nodes, Monitor TaskMan shows that the current node is in a BALANCE state.

## Device Handler’s Influence on TaskMan

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Certain DEVICE (#3.5) file fields strongly affect TaskMan’s behavior. System managers should keep these effects in mind as they configure their systems’ devices.

<table>
<caption><p><span id="_Ref197138575" class="anchor"></span>Table 6: Special Queueing Field Settings</p></caption>
<colgroup>
<col style="width: 44%" />
<col style="width: 55%" />
</colgroup>
<thead>
<tr class="header">
<th>Field</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>VOLUME SET(CPU) (#1.9)</td>
<td>If the VOLUME SET(CPU) field is <em>not</em> filled in, TaskMan considers this device to be available from all Volume Sets. If it is filled in, TaskMan makes sure all tasks that need this device start on the designated Volume Set.</td>
</tr>
<tr class="even">
<td>TYPE (#2)</td>
<td>Any tasks that <em>must</em> wait for HFS- or SPL-type devices are rescheduled for <strong>ten minutes</strong> in the future, instead of being placed in a list of waiting tasks. This is because these lists are checked through repeated opens, which may contaminate the output of these two special types of devices.</td>
</tr>
<tr class="odd">
<td>PRIORITY AT RUN TIME (#25)</td>
<td>The PRIORITY AT RUN TIME field overrides the default priority that system managers can establish for tasks using the <strong>Site Parameters Edit</strong> [XUTM BVPAIR] option on the <strong>Edit TaskMan Parameters</strong> [XUTM PARAMETER EDIT] menu.</td>
</tr>
<tr class="even">
<td>TASKMAN PRINT A HEADER PAGE? (#26)</td>
<td><p>If the TASKMAN PRINT A HEADER PAGE? field is set to <strong>YES</strong> for the device being opened by the submanager, a header page is printed. The header page distributed with TaskMan is very simple, and system managers can substitute their own locally written header pages. To do this, you <em>must</em> rename your header page routine as <strong>^%ZTMSH</strong>, the name of the one distributed with TaskMan.</p>
<p>Whenever you install new versions of Kernel, it overwrites <strong>^%ZTMSH</strong> with the default copy, so you should maintain your local version by doing the following:</p>
<ul>
<li><p>Keep your local header page routine saved somewhere under a local name.</p></li>
<li><p>After each Kernel install, re-save the locally named copy as <strong>^%ZTMSH</strong>.</p></li>
</ul></td>
</tr>
</tbody>
</table>

<span id="_Ref197138575" class="anchor"></span>Table 6: Special Queueing Field Settings

<u>Figure 13</u> shows an alternative to the default header page distributed with Kernel:

<span id="_Ref26362012" class="anchor"></span>Figure 13: Customized Header Page Routine

%ZZTMSH ;SEA/RDS-Local: Sample Header Page ;3/9/92 11:17 ;

;;1.0;Local;;

;

LOCAL ;Print The Local Header Page

;

B ;build text lines

S X1=\$P(\$G(^VA(200,DUZ,0)),U) I X1="" S X1="name unknown"

S X2=\$P(\$G(^VA(200,DUZ,5)),U,2) I X2="" S X2="unlisted mail stop"

S X3=\$P(\$G(^VA(200,DUZ,.13)),U,2) I X3="" S X3="unlisted phone number"

S ZZLINE1=\$\$FORMAT(" "\_X1\_" ("\_X2\_") "\_X3\_"",IOM)

S ZZLINE2=\$\$FORMAT(" "\_ZTDESC\_" ",IOM)

S ZZLINE3=\$\$FORMAT(" "\_ION\_" "\_\$\$HTE^XLFDT(\$H)\_"",IOM)

;

D ;display each line three times

F X=1:1:3 W !,ZZLINE1

W ! F X=1:1:3 W !,ZZLINE2

W ! F X=1:1:3 W !,ZZLINE3

Q

;

FORMAT(ZZTEXT,ZZIOM) ;local extrinsic function

;input: text to be formatted, and margin width

;output: text filled out to margin width -3 with \*characters

N ZZ1,ZZFILLED

S ZZ1=ZZIOM-3-\$L(ZZTEXT)\2

S \$P(ZZFILLED,"\*",ZZ1\*2+1)=""

S \$P(ZZFILLED,"\*",ZZ1+1)=ZZTEXT

I \$L(ZZFILLED)+3-ZZIOM S ZZFILLED=ZZFILLED\_"\*"

Q ZZFILLED

<span id="_Toc193181827" class="anchor"></span>Figure 14: Customized Header Page

\*\*\*\*\*\*\*\*\*\*\*\* XUUSER,ONE (OIFO) FTS 555-5555 \*\*\*\*\*\*\*\*\*\*\*\*

\*\*\*\*\*\*\*\*\*\*\*\* XUUSER,ONE (OIFO) FTS 555-5555 \*\*\*\*\*\*\*\*\*\*\*\*

\*\*\*\*\*\*\*\*\*\*\*\* XUUSER,ONE (OIFO) FTS 555-5555 \*\*\*\*\*\*\*\*\*\*\*\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* SAMPLE TASK \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* SAMPLE TASK \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* SAMPLE TASK \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

\*\*\*\*\*\*\*\*\*\*\* LAT DEVICE Jun 30, 1992@14:34:01 \*\*\*\*\*\*\*\*\*\*\*\*

\*\*\*\*\*\*\*\*\*\*\* LAT DEVICE Jun 30, 1992@14:34:01 \*\*\*\*\*\*\*\*\*\*\*\*

\*\*\*\*\*\*\*\*\*\*\* LAT DEVICE Jun 30, 1992@14:34:01 \*\*\*\*\*\*\*\*\*\*\*\*

## Running TaskMan with a DCL Context

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When run from a DCL context, TaskMan runs as an OpenVMS user. The manager runs as a job that originates from a node-specific OpenVMS batch queue and, by default, submits new submanagers to the same queue as needed.

One advantage to running TaskMan from a DCL context is that it allows jobs to be queued to specific CPUs. When a program calls ^%ZTLOAD, it can request that the job run on a specific CPU/node in your cluster (using the ZTCPU input variable). Unless you are running TaskMan in a DCL context (on Caché systems only), this request will probably fail (and possibly cause the task *not* to run). When TaskMan runs with a DCL context, however, the manager can submit the job as a new submanager to a given CPU’s TaskMan batch queue.

Depending on the %ZTSK and %ZTSCH mapping, multiple Cache environments on the same CPU can each run TaskMan in a DCL context. Although TaskMan in each Cache environment shares the same account, directory, DCL command files, and batch queue, jobs run in the environment specified in each environment’s VAX ENVIRONMENT FOR DCL site parameter.

![](kernel-8-0-systems-management-taskman-user-guide/022.png) NOTE: Kernel patch XU\*8.0\*355 added the \$\$CACHE2 routine for TaskMan load balancing and provides support for DCL context in Caché.

### Setup for Running TaskMan in a DCL Context in a Cache/VMS Environment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following steps show you how to set up TaskMan to run in a DCL context in Cache/VMS (see Kernel patch XU\*8.0\*355).

![](kernel-8-0-systems-management-taskman-user-guide/023.png) NOTE: The following procedure is just an example and must be modified for your site. You need to adjust the UIC \[100,20\] to match your system and indicate the location of the TaskMan directory.

1.  Create TASKMAN user that runs the TaskMan jobs:

<span id="_Toc193181828" class="anchor"></span>Figure 15: Create TASKMAN User

> ADD TASKMAN/OWNER="SYSTEM MANAGER" -

> /ACCOUNT=CACHE -

> /PRIV=(NETMBX,TMPMBX) -

> /DEFPRIV=(NETMBX,TMPMBX) -

> /DEVICE=USER\$/DIR=\[TASKMAN\]/LGICMD=LOGIN.COM -

> /FLAGS=(DisCtlY,DisWelcome,DisReport,DisForce_Pwd_Change,DisPwdDic,DisPwdHis) -

> /PASS=TASK\$MAN/UIC=\[100,20\]

3.  Create the TASKMAN directory:

> <span id="_Toc193181829" class="anchor"></span>Figure 16: Create the TASKMAN Directory

> Define/SYSTEM DHCP\$TASKMAN USER\$:\[TASKMAN\]

4.  Create the system logical name for the directory with the COM files.

![](kernel-8-0-systems-management-taskman-user-guide/024.png) NOTE: Be sure to also add to the STARTUP\$LOGICALS.COM file.

> <span id="_Toc193181830" class="anchor"></span>Figure 17: Create System Logical Name for the Directory with the COM Files

> Define/SYSTEM DHCP\$TASKMAN USER\$:\[TASKMAN\]

5.  Create the queues, as explained in this manual.

![](kernel-8-0-systems-management-taskman-user-guide/025.png) NOTE: Be sure to also add to the STARTUP\$DEFINE_QUEUES.COM file.

TaskMan submits jobs to the queue TM\$*\<node\>*. Because you use “run loginout” to detach the execution, you do *not* need a large JOB limit here.

> <span id="_Toc193181831" class="anchor"></span>Figure 18: Create System Logical Name for the Directory with the COM Files

> INIT/QUEUE/BATCH/OWNER=\[TASKMAN\] -

> /prot=(S:M,O:D,G:R,W:S)/JOB=5/AUTOSTART_ON=isfva2:: TM\$isfva2

6.  Load the following DCL command files into the \[TASKMAN\] directory:
- GET_METRIC.COM
- LOGIN.COM
- METRIC_SCHEDULE.COM
- ZTM2WDCL.COM
- ZTMS2WDCL.COM

These command files are in the cache-taskman sub-directory in the Anonymous FTP site.

![](kernel-8-0-systems-management-taskman-user-guide/026.png) NOTE: Get the files in ASCII mode.

> <span id="_Toc193181832" class="anchor"></span>Figure 19: Sample User Dialog to Retrieve DCL Command Files

> ABC999\$<span class="mark">SET DEF USER\$:\[TASKMAN\] \<Enter\></span>

> ABC999\$<span class="mark">FTP *\<REDACTED\>*.VA.GOV \<Enter\></span>

> 220 ABC999.*\<REDACTED\>*.VA.GOV FTP Server (Version 5.3) Ready.

> Connected to FTP.*\<REDACTED\>*.VA.GOV.

> Name (FTP.*\<REDACTED\>*.VA.GOV:fort): <span class="mark">ANONYMOUS \<Enter\></span>

> 331 Guest login OK, send ident as password.

> Password: <span class="mark">*XXXXXXXXXX* \<Enter\></span>

> 230 Guest login OK, access restrictions apply.

> FTP\> <span class="mark">CD CACHE-TASKMAN \<Enter\></span>

> FTP\> <span class="mark">LS \<Enter\></span>

> 150 Opening data connection for USR\$:\[ANONYMOUS.CACHE-TASKMAN\]\*.\*;\*

> GET_METRIC.COM

> LOGIN.COM

> METRIC_SCHEDULE.COM

> ZTM2WDCL.COM

> ZTMS2WDCL.COM

> FTP\> <span class="mark">ASCII \<Enter\></span>

> 200 TYPE set to ASCII.

> FTP\> <span class="mark">GET GET_METRIC.COM \<Enter\></span>

> FTP\> <span class="mark">GET LOGIN.COM \<Enter\></span>

> FTP\> <span class="mark">GET METRIC_SCHEDULE.COM \<Enter\></span>

> FTP\> <span class="mark">GET ZTM2WDCL.COM \<Enter\></span>

> FTP\> <span class="mark">GET ZTMS2WDCL.COM \<Enter\></span>

> FTP\> <span class="mark">BYE \<Enter\></span>

> 221 Goodbye.

![](kernel-8-0-systems-management-taskman-user-guide/027.png) NOTE: Repeat for each node in the TASKMAN SITE PARAMETERS (#14.7) file.

7.  Edit TaskMan Parameters:

> <span id="_Toc193181833" class="anchor"></span>Figure 20: Sample User Dialog to Edit TaskMan Parameters

> Select Edit Taskman Parameters Option: <span class="mark">SITE \<Enter\></span> Parameters Edit

> Select TASKMAN SITE PARAMETERS BOX-VOLUME PAIR: <span class="mark">ISC \<Enter\></span>

> 1 ISC:ISCABC999

> 2 ISC:ISCABC999

> CHOOSE 1-2: <span class="mark">1 \<Enter\></span> ISC:ISCABC999

> ...

> VAX ENVIROMENT FOR DCL: <span class="mark">ABC999 \<Enter\></span>

> ...

> Balance Interval: 30// <span class="mark">\<Enter\></span>

> LOAD BALANCE ROUTINE: <span class="mark">\$\$CACHE2("@DHCP\$TASKMAN:GET_METRIC.COM") \<Enter\></span>

> LOAD BALANCE ROUTINE: <span class="mark">\$\$CACHE2() \<Enter\></span>

### How to Restart TaskMan when Running in a DCL Context

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To manually restart TaskMan when TaskMan is running in a DCL context, you can either:

- Sign in as OpenVMS user TASKMAN and DO RESTART^ZTMB.
- Sign in from an OpenVMS account that has the OPER and SYSPRV privileges and DO RESTART^ZTMB. This submits the manager to run under the username TASKMAN.

In either case, however, do *not* use the Restart Task Manager \[XUTM RESTART\] option in the Kernel menus; it is *not* compatible with TaskMan in a DCL context.

<span id="_Toc193181834" class="anchor"></span>Figure 21: ZTM2WDCL.COM Command File

\$!-----------------------------------------------------------------------

\$! ZTM2WDCL.COM - Cache Run Taskman in a DCL Context

\$! \* KERNEL 8 \*

\$!

\$! P1 is the Cache config that taskman should start in.

\$! P2 is the namespace that taskman should start in.

\$! P3 = null to START and 1 to RESTART

\$!

\$! This file is submitted to the queue to run and it

\$! builds and runs the TMP_pid.\* files

\$!

\$! Build the file to run, can't pass arguments with RUN

\$ pid = F\$GETJPI("","PID")

\$ infile="TMP\_" + pid + ".ZTM"

\$ outfile = "TMP\_" + pid + ".log"

\$ SAY = "write output"

\$!

\$ entry="START"

\$ if p3 .eq. 1 then entry="RESTART"

\$!

\$! open and build the input file

\$ OPEN/write output 'infile'

\$ SAY "\$! Taskman temp file to run the Manager"

\$ SAY "\$! Delete this file if it is not open."

\$ SAY "\$ set verify"

\$ SAY "\$ csession ""''p1'"" ""-U"" ""''p2'"" ""''entry'^%ZTM0"""

\$ SAY "\$ exit"

\$ Close output

\$!

\$! If a log file is needed change \_NLA0: to 'outfile

\$ name = "ZTMS\_" + pid

\$ run sys\$system:loginout.exe -

/input='infile -

/output=\_NLA0: -

/detach /process='name

\$!

\$! Wait for loginout to run it then delete the file.

\$ wait 00:01

\$!

\$ del TMP\_\*.ZTM;1

\$ exit

<span id="_Toc193181835" class="anchor"></span>Figure 22: ZTMS2WDCL.COM Command File

\$!-----------------------------------------------------------------------

\$! ZTMS2WDCL.COM - Cache Start Submanager with a DCL Context

\$! \* KERNEL 8 \*

\$! p1 is the Cache config name

\$! p2 is the namespace to start.

\$! p3 is NOT used. (VOL for DSM)

\$!

\$! This file is submitted to the queue to run and it

\$! builds and runs the TMP_pid file

\$!

\$! Build the file to run, can't pass arguments with RUN

\$ pid = F\$GETJPI("","PID")

\$ infile = "TMP\_" + pid + ".ZTMS"

\$ outfile = "TMP\_" + pid + ".log"

\$ SAY = "write output"

\$!

\$! open and build the input file

\$ OPEN/write output 'infile'

\$ SAY "\$! Taskman temp file to run a submanager"

\$ SAY "\$! Delete this file if it is not open."

\$ SAY "\$ set verify"

\$ SAY "\$! ''P1' and ''P2'"

\$ SAY "\$ csession ""''p1'"" ""-U"" ""''p2'"" ""START^%ZTMS"""

\$ SAY "\$ exit"

\$ Close output

\$!

\$! If a log file is needed change \_NLA0: to 'outfile

\$ name = "ZTMS\_" + pid

\$ run sys\$system:loginout.exe -

/input='infile -

/output=\_NLA0: -

/detach /process='name

\$!

\$! Wait for loginout to run it then delete the file.

\$ wait 00:01

\$!

\$ del TMP\_\*.ZTMS;1

\$ exit

<span id="_Toc193181836" class="anchor"></span>Figure 23: Example of OpenVMS User TASKMAN on ALPHA AXP Systems

Username: TASKMAN Owner:

Account: UIC: \[50,20\] (\[DEV,TASKMAN\])

CLI: DCL Tables: DCLTABLES

Default: USER\$:\[TASKMAN\]

LGICMD: LOGIN

Flags: DisCtlY Restricted DisWelcome DisReport

Primary days: Mon Tue Wed Thu Fri

Secondary days: Sat Sun

No access restrictions

Expiration: (none) Pwdminimum: 6 Login Fails: 0

Pwdlifetime: 180 00:00 Pwdchange: 19-NOV-1992 14:12

Last Login: 20-NOV-1992 10:34 (interactive), 20-NOV-1992 10:44 (non-

interactive)

Maxjobs: 0 Fillm: 300 Bytlm: 64000

Maxacctjobs: 0 Shrfillm: 0 Pbytlm: 0

Maxdetach: 0 BIOlm: 300 JTquota: 4096

Prclm: 14 DIOlm: 900 WSdef: 2048

Prio: 4 ASTlm: 600 WSquo: 4096

Queprio: 0 TQElm: 10 WSextent: 16384

CPU: (none) Enqlm: 4096 Pgflquo: 100000

Authorized Privileges:

CMKRNL TMPMBX OPER NETMBX

Default Privileges:

CMKRNL TMPMBX OPER NETMBX

<span id="_Toc193181837" class="anchor"></span>Figure 24: Example of OpenVMS TASKMAN Queue

ABC999\$ SH QUE/FULL TM\$ABC999

Batch queue TM\$ABC999, available, on ABC999:

/BASE_PRIORITY=4 /JOB_LIMIT=50 /OWNER=\[DEV,TASKMAN\]

/PROTECTION=(S:E,O:D,G:R,W:W)

ABC999\$

# TaskMan: System Management—Operation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section describes how to operate TaskMan. It also discusses the following:

- [TaskMan Management Menu](#taskman-management-menu)
- [Taskman Management Utilities](#taskman-management-utilities)
- [Scheduling Options](#scheduling-options)
- [Taskman Error Log Menu](#taskman-error-log-menu)
- [Troubleshooting](#troubleshooting)

## TaskMan Management Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Taskman Management \[XUTM MGR\] menu is the main point of entry into the TaskMan options. It contains the following options:

- [Schedule/Unschedule Options](#scheduleunschedule-options) \[XUTM SCHEDULE\]
- [One-time Option Queue](#one-time-option-queue-option) \[XU OPTION QUEUE\]
- [Taskman Management Utilities](#taskman-management-utilities) \[XUTM UTIL\]
- [List Tasks](#list_tasks_option) \[XUTM INQ\]
- [Dequeue Tasks](#dequeue-tasks-option) \[XUTM DQ\]
- [Requeue Tasks](#requeue-tasks-option) \[XUTM REQ\]
- [Delete Tasks](#delete-tasks-option) \[XUTM DEL\]
- [Print Options that are Scheduled to run](#print-options-that-are-scheduled-to-run-option) \[XUTM BACKGROUND PRINT\]
- [Cleanup Task List](#cleanup-task-list-option) \[XUTM TL CLEAN\]
- [Print Options Recommended for Queueing](#print-options-recommended-for-queueing-option) \[XUTM BACKGROUND RECOMMENDED\]

The Taskman Management Utilities \[XUTM UTIL\] submenu and the scheduling-related options are discussed later in this section. The options for listing, dequeuing, requeuing, deleting, and cleaning up tasks are discussed first.

### List Tasks Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc193181838" class="anchor"></span>Figure 25: List Tasks Option

SYSTEMS MANAGER MENU ... \[EVE\]

Taskman Management ... \[XUTM MGR\]

List Tasks \[XUTM INQ\]

Beginning with Kernel 8.0, the TASKS (#14.4) file (in ^%ZTSK) is VA FileMan compatible (that is you can use VA FileMan to print out information about a task). However, the List Tasks \[XUTM INQ\] option also provides a way to examine tasks in the TASKS (#14.4) file. The List Tasks \[XUTM INQ\] option allows you to choose between several useful ways of selecting tasks. When you choose this menu, it presents you with the options shown in <u>Figure 26</u>:

<span id="_Ref511397799" class="anchor"></span>Figure 26: List Tasks Option Submenu Options

List Tasks Option

All your tasks.

Your future tasks.

Every task.

List of tasks.

Unsuccessful tasks.

Future tasks.

Tasks waiting for a device.

Running tasks.

Select Type Of Listing:

Several choices only appear on the list when there are tasks in those collections to be displayed. Remember, the TASKS (#14.4) file can be Volume Set/CPU-specific. This means that the option can only display tasks from the TASKS (#14.4) file on the current Volume Set/CPU.

Holders of the ZTMQ security key see a slightly different list of selections. Instead of “All your tasks” and “Your future tasks” they see “All of one user’s tasks” and “One user’s future tasks.” These two selections are generic versions of those available to normal users. They allow the holder to see any user’s tasks and start by prompting the holder for the user whose tasks should be shown. Other than that, they are identical to the selections used by normal users.

Although each submenu option choice shows a different set of tasks, the format for the output is the same. <u>Figure 27</u> is a sample display from the All your tasks suboption:

<span id="_Ref86032446" class="anchor"></span>Figure 27: All your tasks Suboption—Sample of TaskMan Tasks Running

All tasks that you created...

2572: ALIVE^XINDEX, XINDEX of 1 routine. Device QMS-17P. VAH,KXX.

From TODAY at 10:55, By you. Scheduled for TODAY at 12:05

End of listing. Press RETURN to continue:

In the upper left-hand corner of each entry is the task number. What follows the task number is either an option name (such as XUTM QCLEAN) or a routine entry point (such as ERROR^ZTMZT) depending on whether the task was a queued routine or a queued option. This is generally followed by a description of the task. The device to which the task was queued (if any), along with the account in which the task was/is scheduled to run, complete the first line. The next line contains the time the task was created followed by an identification of the creator. In the case of tasks that requeue themselves, this date and time represents when the task was last requeued.

When the creator’s DUZ number is *not* listed in the NEW PERSON (#200) file, the phrase “USER \#” followed by the DUZ is substituted. Finally, the status of the task is shown.

![](kernel-8-0-systems-management-taskman-user-guide/028.png) REF: For a list and description of the status messages, see the “[Troubleshooting](#troubleshooting)” section.

Each of these submenu options are described in the topics that follow.

#### All your tasks Option

The All your tasks action (see <u>Figure 27</u>) displays every task in the TASKS (#14.4) file on the current Volume Set/CPU that you created. If you have no tasks scheduled, the option gives you the message “You have no tasks in this Volume Set’s TASKS file.”

#### Your future tasks Option

The Your future tasks action displays those tasks you created that are currently scheduled to run. If there are none, the option tells you.

“Every task” lists every task in the TASKS (#14.4) file.

#### List of tasks Option

The List of tasks action allows you to list one or more tasks by task number. You can specify individual tasks separated by commas along with ranges of tasks using a hyphen.

#### Unsuccessful tasks Option

The Unsuccessful tasks action lists three kinds of tasks:

- Rejected by the manager’s validation process.
- Encountered an error while they were running.
- Unscheduled through the Dequeue Tasks option.

#### Future tasks Option

The Future tasks action shows all tasks that are in the Schedule List or the Waiting List. It does *not* show the tasks that are in the Job List. In other words, it shows all tasks that are scheduled to run but *not* those that are currently being run or those that are ready to be run. “Future Tasks” is *not* offered by the List Tasks option if the Schedule List and Waiting List are empty (an unlikely occurrence at most sites).

#### Tasks waiting for a device Option

The Tasks waiting for a device action shows just the Waiting List, which can be a useful way of isolating problem printers. If there are no tasks currently waiting for output devices to become available, the List Tasks option does *not* show this choice.

#### Running tasks Option

The Running tasks action shows tasks that are currently running.

![](kernel-8-0-systems-management-taskman-user-guide/029.png) REF: For a discussion of how TaskMan knows a task is running, see the “[Troubleshooting](#troubleshooting)” section.

### Dequeue Tasks Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc193181841" class="anchor"></span>Figure 28: Dequeue Tasks Option

SYSTEMS MANAGER MENU ... \[EVE\]

Taskman Management ... \[XUTM MGR\]

Dequeue Tasks \[XUTM DQ\]

The Dequeue Tasks \[XUTM DQ\] option allows you to unschedule a task so that the task still exists in the TASKS (#14.4) file but is no longer in the Schedule, Waiting, or Job List. The process of unscheduling a task is called “dequeuing”. This option allows you to dequeue any one task or range of tasks. A task that you dequeue has a status of NOT QUEUED in a List Tasks display.

The option first prompts you for the task number. Entering one question mark (?) gets you a short explanatory message but entering two question marks (??) puts you in the List Tasks \[XUTM INQ\] option to find the task you are interested in dequeuing. When you leave the List Tasks \[XUTM INQ\] option, you automatically return to the task number prompt.

If you enter the number of a nonexistent task, the List Tasks \[XUTM INQ\] option tells you and then prompts you for another task number. If you enter the number of a task that does exist, the option displays the task and asks you if you are sure. Answering NO returns you to the task number prompt, whereas a YES dequeues the task and then returns you to the task number prompt.

You can also enter a list of tasks to be dequeued. The list can include single tasks separated by commas and ranges of tasks consisting of two numbers separated by a hyphen. After you enter the list, you are asked if you want to know the actual number of tasks in the list. You are then asked if you want a display of the actual tasks that are about to be dequeued.

Only holders of the ZTMQ security key can dequeue any task. Others can only dequeue their own tasks as identified by their DUZ.

### Requeue Tasks Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc193181842" class="anchor"></span>Figure 29: Requeue Tasks Option

SYSTEMS MANAGER MENU ... \[EVE\]

Taskman Management ... \[XUTM MGR\]

Requeue Tasks \[XUTM REQ\]

A benefit of the Dequeue Tasks \[XUTM DQ\] option is that it is completely *non*-destructive. If you dequeue a task and subsequently change your mind, you can use the Requeue Tasks \[XUTM REQ\] option to requeue the task exactly the way that it was. You can also use this option to change some of the details of a task that is already queued.

As with the Dequeue Tasks \[XUTM DQ\] option, you are first prompted for a task number with the same help available. Here, you can only enter a single task, *not* a range. The task is then displayed, and you are asked for a new run time with the default being either the original or current run time (whichever applies). The next question is “Do you wish to requeue this task to a device?”, with the default depending on whether the task originally requested an output device. If you answer YES, the option asks you to specify an output device using the original output device (if there was one) as a default. The option also allows you to adjust the task’s priority.

The task is requeued according to your specifications. Requeuing involves completely dequeuing the task so that your task does *not* run twice, making the changes you requested, and placing the task back on the Schedule List. Notice that the task is *not* dequeued until after you specify the changes you want to make. If you want to modify a task that may start running soon, it is usually a good idea to dequeue it first.

The ZTMQ security key affects this option in two ways:

- Users who do *not* hold the ZTMQ security key are limited to requeuing only their own tasks.
- Users are *not* prompted to change the priority.

### Delete Tasks Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc193181843" class="anchor"></span>Figure 30: Delete Tasks Option

SYSTEMS MANAGER MENU ... \[EVE\]

Taskman Management ... \[XUTM MGR\]

Delete Tasks \[XUTM DEL\]

The Delete Tasks \[XUTM DEL\] option has the same structure as the Dequeue Tasks \[XUTM DQ\] option. The only difference is that where dequeuing a task just removes it from the lists (unschedules it); the Delete Tasks option also deletes the task from the TASKS (#14.4) file. When you have deleted a task, there is no reference to that task anywhere in TaskMan’s files.

Only holders of the ZTMQ security key can delete any task. Others can only delete their own tasks as identified by their DUZ.

### Cleanup Task List Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc193181844" class="anchor"></span>Figure 31: Cleanup Task List Option

SYSTEMS MANAGER MENU ... \[EVE\]

Taskman Management ... \[XUTM MGR\]

Cleanup Task List \[XUTM TL CLEAN\]

You can use the Cleanup Task List \[XUTM TL CLEAN\] option to remove a task entry from a task list for a job that is no longer running. This might happen when a process is forcibly exited, but TaskMan still believes the task is running. You can use this option to tell TaskMan which tasks you forcibly exited. TaskMan then removes those tasks from its list of running tasks.

## Taskman Management Utilities

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A submenu on the Taskman Management \[XUTM MGR\] menu, called TaskMan Management Utilities \[XUTM UTIL\] menu, provides several options to set up, monitor, and modify the TaskMan environment.

The TaskMan Management Utilities \[XUTM UTIL\] menu contains the following options:

- [Monitor Taskman](#monitor-taskman-option-1) \[XUTM ZTMON\]
- [Check Taskman’s Environment](#check-taskmans-environment-option) \[XUTM CHECK ENV\]
- [Edit Taskman Parameters](#edit-taskman-parameters-menu) \[XUTM PARAMETER EDIT\]
- [Restart Task Manager](#restart-task-manager-option) \[XUTM RESTART\]
- [Place Taskman in a WAIT State](#place-taskman-in-a-wait-state-option) \[XUTM WAIT\]
- [Remove Taskman from WAIT State](#remove-taskman-from-wait-state-option) \[XUTM RUN\]
- [Stop Task Manager](#stop-task-manager-option) \[XUTM STOP\]
- [Taskman Error Log](#taskman-error-log-menu) \[XUTM ERROR\]
- [Clean Task File](#clean-task-file-option) \[XUTM CLEAN\]
- [SYNC flag file control](#sync-flag-file-control-option) \[XUTM SYNC\]

These options are discussed in the sections that follow.

### Monitor Taskman Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc193181845" class="anchor"></span>Figure 32: Monitor Taskman Option

SYSTEMS MANAGER MENU ... \[EVE\]

Taskman Management ... \[XUTM MGR\]

Taskman Management Utilities ... \[XUTM UTIL\]

Monitor Taskman \[XUTM ZTMON\]

The Monitor Taskman \[XUTM ZTMON\] option gives you a screen of information about the current state of TaskMan and offers you several ways to get more information. The monitor focuses on the current state of the manager itself and on the contents of the *non*-VA FileMan-compatible [SCHEDULE file](#schedule_file).

![](kernel-8-0-systems-management-taskman-user-guide/030.png) REF: for more information on the *non*-VA FileMan-compatible SCHEDULE file, see Section <u>5.5.1</u>, “[SCHEDULE File](#schedule-file-1).”

As you use this option, you acquire an intuitive understanding of how these lists should look and behave when your system is healthy. Spending the time using this option to get that intuition saves you troubleshooting time by helping you to notice problems sooner.

#### RUN Node

The first section of the “Monitor TaskMan” screen reports whether the manager is currently running on your machine, and if so, whether it is being delayed. This is accomplished by comparing TaskMan’s RUN node to the M \$HOROLOG variable. Under normal circumstances they should be within 15 seconds of each other, though certain conditions can cause a difference of up to two minutes. Any difference greater than that, however, is a sign that the manager is being delayed, typically by a problematic device or a recurring error. Of course, the manager is also likely to fall behind if the system is saturated to the point where all jobs on the system are slow. The last line of the first section evaluates the difference and guesses at the manager’s current condition. The \$HOROLOG values are translated into an external format for your convenience in understanding the values.

<span id="_Ref86027017" class="anchor"></span>Figure 33: Sample Monitor TaskMan Screen

Checking TaskMan. Current \$H=54180,45147 (MAY 04, 1989 @12:32:27)

RUN NODE=54180,45145 (MAY 04, 1989 @12:32:25)

TaskMan is current.

Checking the Status List:

TaskMan job 4 status 54180,45145^RUN^Main Loop.

There are 3 idle submanagers

Checking the Schedule List:

TaskMan has 29 tasks in the Schedule List.

None of them are overdue.

Checking the IO Lists: Last TM scan: 54180,45146^\_TNA9995:

Device: \_TNA9995: is not available, and there are 7 tasks waiting.

Checking the Job List:

There are no tasks waiting for partitions.

For KDE:ISC6V2 there are 2 tasks. Not responding

Checking the Task List:

There are 5 tasks currently running.

Enter monitor action: UPDATE//

#### Status List

The Status List is where each manager periodically reports its status. The job number of the manager is reported both for ease of location on a system status report and to distinguish between multiple managers (if there are more than one). Under normal circumstances, the manager removes its entry from the Status List when it shuts down, but if a manager stops abnormally (such as RJD or FORCEX) its entry is usually left on the list. The list is updated and cleaned out whenever a new manager is started or restarted.

The status of a manager consists of three parts:

- Date and time—This date and time should equal the RUN node’s date and time, and like that node, it should be close to the current \$HOROLOG.
- Manager’s state.
- Description of special circumstances.

The manager can be in one of five states at any given time:

- BALANCE
- ERROR
- PAUSE
- RUN
- WAITRUN is the normal state, with a description of “Main Loop.”

The manager’s status is the most important piece of information the monitor gives, and it should always be the first thing checked when troubleshooting problems.

![](kernel-8-0-systems-management-taskman-user-guide/031.png) REF: For a detailed list and description of the possible state messages, see the “[Troubleshooting](#troubleshooting)” section.

#### Schedule List

The Schedule List always shows the number of tasks currently scheduled to run and checks the times for which they are scheduled to determine whether any of them should already have started. When many tasks are queued to run at the same time, it is *not* unusual for the manager to be a little late in sending off the last few.

When most of the tasks on the Schedule List are overdue, however, the manager is probably having problems keeping up. This is *not* a normal condition. If the problem is *not* a recurring error or a difficult output device, the most likely culprit is your default setup in the TASKMAN SITE PARAMETERS (#14.7) file. Another possible problem is that TaskMan is trapping many errors or trying to access a very slow link between Volume Sets. If the problem is error trapping, the Status List should regularly show the manager in an ERROR state. Also, remember that if the machine is saturated, all jobs on the system, including the manager, run slowly.

#### IO List

The IO List first shows the last time (\$H) a submanager checked the list and the last device checked. The check generally shows how many tasks are waiting for each device in the IO List. The occasional remark “Allocated” means that a submanager has already noticed that the device is available and has allocated the device to a task using the Device Allocation List. Devices should only be allocated for a short time before the submanager opens the device, making it unavailable.

Understanding how the IO List works can make this check very useful. Submanagers handle the Device IO Lists. Unusual behavior in these lists usually points to device or submanager problems.

There are three fundamental things to look for with this check:

- When a Device becomes Available—The submanagers should notice and start a task running on that device. If the submanagers do *not* do this, it is probably time to start looking for problems with the submanagers.
- When a Device is Allocated—A submanager should quickly make it unavailable. If this fails to occur, the submanagers may be having problems. There can be extenuating circumstances (such as the system being very slow) that explain these occurrences.
- When Many Tasks are Backed Up Waiting for the Same Device—Sometimes it is just because that device is busy. However, sometimes the device is off-line or out of paper.

#### Job List

The Job List is where tasks wait for partitions, so if many tasks are backed up here you know the submanagers are *not* picking them up. This can be caused by any of the following:

- A slow system.
- TaskMan reaching its job limit.
- TaskMan assigning tasks a priority that is too low for them to run.

Systems that are too busy back up in the Job List *not* the Schedule List. The Compute Server Job List is checked here and lets you know about tasks waiting to run on other CPUs and if the submanagers are *not* starting.

#### Task List

The Task List is where TaskMan keeps track of the tasks it has started running. Entries are set into this list when the submanagers start their tasks and are cleared when the tasks quit or cause errors to be trapped. KILLing a task by forcing its process to exit in the middle of execution (using such vendor-specific tools as RJD, RESJOB, FORCEX, KILLJOB, and so on) does *not* give the submanager a chance to clear the task from the Task List, so the Task List can become inaccurate. If you frequently KILL jobs but want to keep your Task List accurate, you need to manually remove the obsolete entries. The exit action of the KILL off a users’ job \[XURESJOB\] option helps you identify and remove from the list of running tasks those you have forcibly exited.

#### Monitor Action Prompt

After summarizing the status of the manager and the principal lists of the SCHEDULE file, the monitor offers you a choice of actions. They are displayed if you enter a single question mark (?) at the “Enter monitor action:” prompt:

<span id="_Ref86027381" class="anchor"></span>Figure 34: TaskMan Monitor Actions

Enter \<RET\> to update the monitor screen.

Enter ^ to exit the monitor.

Enter E to inspect the TaskMan Error File.

Enter S to see a system status listing.

Enter ? to see this message.

Enter ?? to inspect the tasks in the monitor's lists.

These actions (see <u>Figure 34</u>) attempt to bring together those utilities used most often in response to seeing a monitor screen. Updating is the most used choice since you often want to watch how the lists change over time. The TASKMAN ERROR file needs to be easily accessible, not only in case the manager enters an ERROR state, but also if a task that should take a long time to run leaves the Job List but never shows up in the Task List. This usually means the task hit an error and quit, which can be confirmed or disproved by a quick glance at the TaskMan Error Log. The System Status Report can be used to verify that tasks, submanagers, and the manager are indeed running as the monitor suggests.

Some actions at the Monitor Action prompt are *not* accessible when monitoring TaskMan from the manager’s account (using the direct-mode utility D ^ZTMON).

#### Inspecting the Tasks in the Monitor’s Lists

If you are in a non-library account, you can directly inspect the contents of the various lists. Do this by entering two question marks (??) at the “Enter monitor action:” prompt. You get the list of choices shown in <u>Figure 35</u>:

<span id="_Ref26362064" class="anchor"></span>Figure 35: Options for Inspecting Tasks in the TaskMan Monitor’s Lists

Help For Monitor Taskman Option

Schedule List.

Waiting Lists.

One Waiting List.

Job List.

Task List.

Link Lists.

Paired Task-Sync List.

Select Type Of Listing:

These listings use the same format as that of the List Tasks action and show you the contents of the lists at the time you look at them. For example:

- The One Waiting List listing prompts you to select a device, and the help for that prompt lets you see those devices that have tasks waiting.
- The Paired Task-Sync List listing shows the tasks associated with the selected Task-Sync Pair (that is: Sync Flag and IO Device) from the TASK SYNC FLAG (#14.8) file.

Many of these lists change very quickly. Thus, it is *not* unusual to enter the help with the intention of seeing the task that was shown by the main screen to be in the Job List, only to be informed by the help software that the Job List is now empty. These kinds of experiences are simply part of troubleshooting TaskMan.

While these monitor actions are useful, there are still times when you *must* leave the monitor to follow up on information you saw there. For example, you may want to check the list of unsuccessful tasks or to list a specific task; both these actions require using the List Tasks action.

Taken as a whole, the checks that make up the monitor can save you a lot of time in trying to evaluate TaskMan’s status. The example shown in <u>Figure 33</u> is of a healthy, and *not* very busy, manager. Monitors at sites usually show considerably more activity, especially in the Waiting Lists.

### Check Taskman’s Environment Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc193181849" class="anchor"></span>Figure 36: Check Taskman’s Environment Option

SYSTEMS MANAGER MENU ... \[EVE\]

Taskman Management ... \[XUTM MGR\]

Taskman Management Utilities ... \[XUTM UTIL\]

Check Taskman's Environment \[XUTM CHECK ENV\]

The Check Taskman’s Environment \[XUTM CHECK ENV\] option presents two screens of information about TaskMan’s environment on the current CPU:

- [First Screen](#first-screencheck-taskmans-environment-option)—The first screen (see <u>Figure 37</u>) performs all checks that the manager does whenever it starts, restarts, or encounters an error.
- [Second Screen](#second-screencheck-taskmans-environment-option)—The second screen (see <u>Figure 38</u>) shows what values the manager is using for its definition variables.

This information can be very useful in pinpointing startup problems, in verifying that the manager is using the information you want it to use and in getting a general feel for how you have defined your system’s task management.

#### First Screen—Check Taskman’s Environment Option

<span id="_Ref86026000" class="anchor"></span>Figure 37: Check TaskMan’s Environment Option—First Screen

Checking Task Manager's Environment.

Checking TaskMan's globals...

^%ZTSCH is defined!

^%ZTSK is defined!

^%ZTSK(0) is defined!

^%ZIS(14.5,0) is defined!

^%ZIS(14.6,0) is defined!

^%ZIS(14.7,0) is defined!

Checking the ^%ZOSF nodes required by TaskMan...

All ^%ZOSF nodes required by TaskMan are defined!

Checking the links to the required volume sets...

There are no volume sets whose links are required!

Checks completed...TaskMan's environment is okay!

Press RETURN to continue or '^' to exit:

This first screen (see <u>Figure 37</u>) goes through each step that the manager goes through when it starts or restarts and reports the results. If your manager is failing to start, this screen should identify any problem with the environment.

#### Second Screen—Check Taskman’s Environment Option

<span id="_Ref204688674" class="anchor"></span>Figure 38: Check TaskMan’s Environment Option—Second Screen

Here is the information that TaskMan has:

Operating System: OpenM-NT

Volume Set: ROU

Cpu-volume Pair: ROU:KDAABC999

TaskMan Files UCI and Volume Set: VAH,ROU

Log Tasks? N

Submanager Retention Time: 30

Min Submanager Count: 10

Taskman Hang Between New Jobs: 1

TaskMan running as a type: GENERAL

TaskMan is using VAX DSM environment: ABC999

TaskMan is using '\$\$CACHE@() for load balancing

Balance Interval: 10

Logons Inhibited?: N

Taskman Job Limit: 35

Max sign-ons: 40

Current number of active jobs: 25

End of listing. Press RETURN to continue:

The second screen (see <u>Figure 38</u>) reports more information about the current TaskMan environment:

- The first group of four items identifies the current TaskMan operating environment.
- The second group of items reports the values of some Kernel site parameters that are important to TaskMan.

![](kernel-8-0-systems-management-taskman-user-guide/032.png) REF: These parameters, as well as all other parameters that TaskMan uses, are described in detail in the “[TASKMAN SITE PARAMETERS (#14.7) File](#taskman-site-parameters-14.7-file)” section in the “<u>TaskMan: System Management—Configuration</u>” section.

- The third and last group of four items show if logons are being inhibited and how many partitions with which TaskMan currently must work. These values show how busy your system is, as well as how busy it can become. Their importance is also described in the discussion of parameters.

### Restart Task Manager Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc193181852" class="anchor"></span>Figure 39: Restart Task Manager Option

SYSTEMS MANAGER MENU ... \[EVE\]

Taskman Management ... \[XUTM MGR\]

Taskman Management Utilities ... \[XUTM UTIL\]

<span class="mark">Restart Task Manager</span> \[XUTM RESTART\]

The manager generally starts automatically when your system comes up. If the manager crashes or is stopped, you can use the Restart Task Manager \[XUTM RESTART\] option to restart it. The option first checks the RUN node and calculates whether it thinks the manager is currently running. If this option believes the manager is running, it asks you if you are sure you want to restart another TaskMan; you *must* answer YES to start the manager. If the Restart Task Manager \[XUTM RESTART\] option thinks the manager has stopped, it asks you for confirmation before jobbing out a new manager. If the XUTM RESTART option believes the manager to be active when you know for sure that it has failed, you can invoke the Stop Task Manager \[XUTM STOP\] option to prove to the XUTM RESTART option that the manager really has stopped. Then you can restart it.

### Place Taskman in a WAIT State Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc193181853" class="anchor"></span>Figure 40: Place Taskman in a WAIT State Option

SYSTEMS MANAGER MENU ... \[EVE\]

Taskman Management ... \[XUTM MGR\]

Taskman Management Utilities ... \[XUTM UTIL\]

<span class="mark">Place Taskman in a WAIT State</span> \[XUTM WAIT\]

The WAIT state (as described in the “[Troubleshooting](#troubleshooting)” section) is a condition in which the manager does nothing but wait for you to release it. Putting a stop to the manager’s activities without shutting down the manager can often be very useful. For example, with the manager in a WAIT state, you can look at the tasks after they are queued but before the manager has a chance to validate them. This can help you isolate problems caused by the queuing process from those caused by the validation process. Another time you may want to create a WAIT state is before restarting a manager that has stopped. This prevents the manager from processing any tasks when it first starts up; the manager checks out its environment and then waits for your command to continue. The Place Taskman in a WAIT State \[XUTM WAIT\] option gives you a way to switch the manager’s activities on and off without having to completely shut down and restart the manager.

When you select the XUTM WAIT option, you are also prompted with the question “Should active submanagers shut down after finishing their current tasks?”:

- If you answer YES, the submanagers on the current Volume Set/CPU quits when they finish a task instead of recycling.
- If you answer NO, the manager enters a WAIT state and the submanagers continue with their business.

If you also want to keep the submanagers from searching the Waiting List and the Job List for tasks, you need to explicitly say so at this prompt. This inhibition of the submanagers’ recycling remains in effect either until you remove the WAIT state or until a new manager starts or restarts, whichever comes first.

### Remove Taskman from WAIT State Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc193181854" class="anchor"></span>Figure 41: Remove Taskman from WAIT State Option

SYSTEMS MANAGER MENU ... \[EVE\]

Taskman Management ... \[XUTM MGR\]

Taskman Management Utilities ... \[XUTM UTIL\]

<span class="mark">Remove Taskman from WAIT State</span> \[XUTM RUN\]

The Remove Taskman from WAIT State \[XUTM RUN\] option simply undoes the effects of the Place Taskman in a WAIT State \[XUTM WAIT\] option, allowing the manager to process tasks and allowing the submanagers to recycle (if recycling had been inhibited).

### Stop Task Manager Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc193181855" class="anchor"></span>Figure 42: Stop Task Manager Option

SYSTEMS MANAGER MENU ... \[EVE\]

Taskman Management ... \[XUTM MGR\]

Taskman Management Utilities ... \[XUTM UTIL\]

<span class="mark">Stop Task Manager</span> \[XUTM STOP\]

The Stop Task Manager \[XUTM STOP\] option gives you a clean way to stop the manager from within the menu system. This option also asks if you want the submanagers to shut down when they finish what they are doing.

![](kernel-8-0-systems-management-taskman-user-guide/033.png) NOTE: The WAIT state takes precedence. While the manager is in a WAIT state, not even XUTM STOP option affects it until after you invoke the Remove Taskman from WAIT State \[XUTM RUN\] option to release it from the WAIT state; after it is released, it shuts down.

This option should always be used to shut down TaskMan, rather than simply KILLing the TaskMan process, which can leave the TaskMan globals in an improper state and even lose tasks.

### SYNC flag file control Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc193181856" class="anchor"></span>Figure 43: SYNC flag file control Option

SYSTEMS MANAGER MENU ... \[EVE\]

Taskman Management ... \[XUTM MGR\]

Taskman Management Utilities ... \[XUTM UTIL\]

<span class="mark">SYNC flag file control</span> \[XUTM SYNC\]

With the SYNC flag file control \[XUTM SYNC\] option, you can use the LIST TASKS option to view active/pending tasks associated with the same SYNC FLAG. This shows the tasks associated with the selected Task-Sync Pair (that is the SYNC FLAG and IODevice) from the TASK SYNC FLAG (#14.8) file. For any SYNC FLAG (#87) field entry in the TASKS (#14.4) file you can remove it from the file and delete all waiting tasks with the same SYNC FLAG. You can also choose START NEXT, which resumes running the series of tasks associated with that SYNC FLAG. This is useful when one task in a series of tasks that is synchronized with SYNC FLAG fails.

### Clean Task File Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The TASKS (#14.4) file grows every time a new task is queued. While the SAC requires applications to delete their tasks’ entries when they complete, it is possible that older applications may *not* do this. Other tasks abort with errors; still others are rejected. The result is that ^%ZTSK is always growing. Options are available that clean up the ^%ZTSK global.

<span id="_Toc193181857" class="anchor"></span>Figure 44: Clean Task File Option

SYSTEMS MANAGER MENU ... \[EVE\]

Taskman Management ... \[XUTM MGR\]

Taskman Management Utilities ... \[XUTM UTIL\]

<span class="mark">Clean Task File</span> \[XUTM CLEAN\]

In unusual circumstances, you may need to clean the ^%ZTSK global manually. Kernel provides the Queuable Task Log Clean Up \[XUTM QCLEAN\] option to regularly clean up the TASKS (#14.4) file in the background.

Only rarely are you *not* able to rely on the queued cleanup to perform this function. However, when necessary, you can use the interactive Clean Task File \[XUTM CLEAN\] option. First, XUTM CLEAN asks you if you are sure you want to clean out the old entries from the TASKS (#14.4) file. If you respond that you are, the option asks you how far back you want to keep old entries. The default is to keep old entries going back a week and to delete the older ones. After you provide this value, the option queues a task to do the cleanup. XUTM CLEAN *cannot* be queued.

### Queuable Task Log Clean Up Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Queuable Task Log Clean Up \[XUTM QCLEAN\] option, resides on the Parent of Queuable Options \[ZTMQUEUABLE OPTIONS\] menu. This option allows you to purge all entries for tasks that are no longer queued (for whatever reason) and to purge the TaskMan Error Log. It is very useful to be able to queue the cleanup to automatically run each night; XUTM QCLEAN has been distributed to provide this feature. The XUTM QCLEAN option should *not* be run interactively; indeed, it is *not* available from any of TaskMan’s menus. To queue this option, use the Schedule/Unschedule Options \[XUTM SCHEDULE\] option to queue it to run.

The date the Queuable Task Log Clean Up \[XUTM QCLEAN\] option starts purging the TASKS (#14.4) file is controlled by the DAYS TO KEEP OLD TASKS (#8) field parameter in the VOLUME SET (#14.5) file. A value of seven days is *recommended*. XUTM QCLEAN does *not* need an output device; therefore, you can leave that field blank. Once set up, the task automatically runs periodically, cleaning out inactive task entries that are older than the time-period specified in the DAYS TO KEEP OLD TASKS (#8) field. If you want to run this on all your machines, create an entry in the OPTION SCHEDULING (#19.2) file for each machine on which you want to run it.

## Scheduling Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

TaskMan lets you, the site manager, schedule options that run regularly as tasks. Menu Manager and TaskMan work together to give you this ability. All you must do is tell TaskMan which option you want to queue and how you want to queue it.

### Which Options to Queue

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The first requirement for queuing regards the option type. Only the Run, Print, and Action types of options can be queued. The second requirement is that the option (if a Run or Action type) *mustnot* involve user input! There is nothing to prevent you from queuing an option of the wrong type or from queuing one that prompts the user for input but doing so results in a failed task. You *must* be conscious of the nature of the task when you consider creating one that performs an option. If the option itself does *not* run in the background, then queuing it is pointless. Even options that themselves queue tasks probably *cannot* be queued, because most of these ask the user for an output device or a run time.

Software applications can make recommendations for scheduling of options. This is a great help to site managers.

![](kernel-8-0-systems-management-taskman-user-guide/034.png) REF: Recommendations for scheduling Kernel options can be found in the *Kernel Installation Guide* and the *Kernel 8.0 and Kernel Toolkit 7.3 Technical Manual*.

#### PARENT OF QUEUABLE OPTIONS Menu

Some options that are intended to be queued are *not* intended to be run interactively, so placing such options on a user menu could cause problems. The Parent of Queuable Options \[ZTMQUEUABLE OPTIONS\] menu, a menu-type option, has no parent in the menu tree and is intended to be used as the parent of all such options.

#### Printing Options Recommended to Run and Scheduled to Run

<span id="_Toc193181858" class="anchor"></span>Figure 45: Print Options Recommended for Queueing and Print Options that are Scheduled to Run Options

SYSTEMS MANAGER MENU ... \[EVE\]

Taskman Management ... \[XUTM MGR\]

<span class="mark">Print Options Recommended for Queueing \[XUTM BACKGROUND RECOMMENDED\]</span>

<span class="mark">Print Options that are Scheduled to run \[XUTM BACKGROUND PRINT\]</span>

#### Print Options Recommended for Queueing Option

The Print Options Recommended for Queueing \[XUTM BACKGROUND RECOMMENDED\] option displays all options in the OPTION SCHEDULING (#19.2) file that are *recommended* for scheduling by the option’s developer.

#### Print Options that are Scheduled to run Option

The Print Options that are Scheduled to run \[XUTM BACKGROUND PRINT\] option lists all currently scheduled options on your system. By comparing these two reports, you could see if any options recommended for scheduling are *not* scheduled on your system (and vice-versa).

#### Schedule/Unschedule Options

<span id="_Toc193181859" class="anchor"></span>Figure 46: Schedule/Unschedule Options Option

SYSTEMS MANAGER MENU ... \[EVE\]

Taskman Management ... \[XUTM MGR\]

<span class="mark">Schedule/Unschedule Options</span> \[XUTM SCHEDULE\]

The Schedule/Unschedule Options \[XUTM SCHEDULE\] option is a straightforward VA ScreenMan edit option, and it allows you to schedule and unschedule options. After you select the option to schedule, you are prompted for information about the task you want to set up. You can edit the following fields in the OPTION SCHEDULING (#19.2) file:

- QUEUED TO RUN AT WHAT TIME (#2) (see Section <u>5.3.1.4</u>)
- DEVICE FOR QUEUED JOB OUTPUT (#3) (see Section <u>5.3.1.7</u>)
- QUEUED TO RUN ON VOLUME SET (#5) (see Section <u>5.3.1.8</u>)
- RESCHEDULE FREQUENCY (#6) (see Section <u>5.3.1.9</u>)
- SPECIAL QUEUEING (#9) (see Section <u>5.3.1.11</u>)
- TASK PARAMETERS (#15) (see Section <u>5.3.1.10</u>)

The cross-references on these fields make calls to TaskMan’s API to update the TASKS (#14.4) file and ^%ZTSCH.

![](kernel-8-0-systems-management-taskman-user-guide/035.png) NOTE: To queue a task, its SCHEDULING RECOMMENDED (#209) field in the OPTION (#19) file *must* be set to YES.

#### Queued to Run At What Time

To queue an option, select the option and enter a time at least two minutes in the future into the QUEUED TO RUN AT WHAT TIME (#2) field in the OPTION SCHEDULING (#19.2) file. When you enter a time (and date) for the task to run, the task is immediately put on the Schedule List for that time.

#### How to Delete a Regularly Scheduled Task

Deleting a scheduled task is as simple as entering the at-sign (@) at the QUEUED TO RUN AT WHAT TIME (#2) field. TaskMan then searches the current TASKS (#14.4) file for the task that corresponds to the entry in the OPTION SCHEDULING (#19.2) file and deletes it.

If your system has multiple copies of the TaskMan globals, you *must* use the Schedule/Unschedule Options \[XUTM SCHEDULE\] option on the same Volume Set/CPU where your task originated, when you delete the task. Otherwise, the future task in the TASKS (#14.4) file is *not* found (and deleted) when you enter an at-sign (@) in the QUEUED TO RUN AT WHAT TIME (#2) field.

#### How to Requeue a Regularly Scheduled Task

Requeuing merely involves placing a new value in the QUEUED TO RUN AT WHAT TIME (#2) field. When you do this, the currently scheduled task is deleted (exactly as described above when deleting a scheduled task). Then, a new task is created at the new time to replace the previously scheduled task.

If your system has multiple copies of the TaskMan globals, you *must* use the Schedule/Unschedule Options \[XUTM SCHEDULE\] option on the same Volume Set/CPU where your task originated, when you requeue the task. Otherwise, the existing future task in the TASKS (#14.4) file is *not* found (and deleted) when you enter a new time in the QUEUED TO RUN AT WHAT TIME (#2) field.

#### Device For Queued Job Output

The DEVICE FOR QUEUED JOB OUTPUT (#3) field in the OPTION SCHEDULING (#19.2) file is where you can give the task an output device. For print (Report) type options this is obviously mandatory; for run or action types you need to consider if the option needs an output device. Modifying this value for an already-scheduled task merely causes a direct change to the currently scheduled task:

- Tasks with an output device are assigned a process name of:

Task \####

Where \#### is the task number.

- Tasks with no output device are assigned a process name of:

BTask \####

(with B meaning background)

#### Queued To Run On Volume Set

Use the QUEUED TO RUN ON VOLUME SET (#5) field in the OPTION SCHEDULING (#19.2) file to designate a Volume Set or CPU for the task other than your current one. This field is only useful for options that do *not* have a device selected because most devices are tied to a CPU, and thus, the task *must* run on the CPU that has that device.

Modifying this value for an already-scheduled task merely causes a direct change to the currently scheduled task.

Running a task on each CPU for a given option may at times be useful (such as the Non-interactive Build Primary Menu Trees \[XQBUILDTREEQUE\] option). In such cases, make multiple entries in the OPTION SCHEDULING (#19.2) file and use the QUEUED TO RUN ON VOLUME SET (#5) field to specify the Volume Set/CPU where each scheduled task should run.

If you leave the DEVICE FOR QUEUED JOB OUTPUT (#3) field blank, the task that performs the option runs without a device (or tries to). If you also leave the QUEUED TO RUN ON VOLUME SET (#5) field blank, the task runs on the current CPU without a device. If you fill in both fields, TaskMan uses the value of the QUEUED TO RUN ON VOLUME SET (#5) field, unless overridden by the VOLUME SET(CPU) (#1.9) field in the DEVICE (#3.5) file entry of the selected device.

#### Reschedule Frequency

Whenever a task starts running an option, it looks to see what is in the RESCHEDULE FREQUENCY (#6) field in the OPTION SCHEDULING (#19.2) file. If the field is blank, the option does *not* reschedule itself. If you have filled in this field, the task uses the value you placed in the field to figure out when you want it to run next. Then it updates the QUEUED TO RUN AT WHAT TIME (#2) field to reflect the new scheduled time. When this field is updated, the next task in the sequence is scheduled.

If you change the existing value in the RESCHEDULE FREQUENCY (#6) field, the new increment is used beginning after the next time the option runs.

There are several formats you can use in this field:

- Every “n” seconds.
- Hours.
- Days.
- Months (incremental).
- A particular day of the month.
- A list of times every “n” months.

![](kernel-8-0-systems-management-taskman-user-guide/036.png) REF: For a list of the code formats for the RESCHEDULE FREQUENCY (#6) field, see the “[Special Queueing](#special-queueing)” section.

For the incremental scheduling frequencies (every n seconds, hours, days, or months), the increment is added to the scheduled date and time in the QUEUED TO RUN AT WHAT TIME (#2) field to determine when the task should run next. As of Kernel 8.0, if the incremented time is in the past, however, TaskMan keeps adding the increment until a future time is reached, only then does it reschedule the task.

#### Task Parameters

Use the TASK PARAMETERS (#15) field in the OPTION SCHEDULING (#19.2) file to pass data to a scheduled option. TASK PARAMETERS holds a string that is passed to scheduled jobs through the ZTQPARAM variable. Ideally, the developer of an option that uses the TASK PARAMETERS string should describe the format and meaning of the string in the option’s DESCRIPTION (#3.5) field in the OPTION (#19) file.

#### Special Queueing

Use the SPECIAL QUEUEING (#9) field in the OPTION SCHEDULING (#19.2) file to designate which option is scheduled to be run by TaskMan.

![](kernel-8-0-systems-management-taskman-user-guide/037.png) NOTE: To queue a task, you must set the SCHEDULING RECOMMENDED (#209) field in the OPTION (#19) file to YES.

Valid values are listed in <u>Table 6</u>:

<table>
<caption><p><span id="_Toc193181860" class="anchor"></span>Table 7: Option Scheduling Frequency Code Formats</p></caption>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th>Value</th>
<th>Option Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>S</strong></td>
<td><strong>STARTUP—</strong>TaskMan queues the job to run whenever the TaskMan/computer is started (that is at System Boot). If you want to the run the startup option on multiple CPUs, make multiple entries in the OPTION SCHEDULING (#19.2) file and use the QUEUED TO RUN ON VOLUME SET (#5) field to specify on what Volume Set/CPU each should run.</td>
</tr>
<tr class="even">
<td><strong>SP</strong></td>
<td><strong>STARTUP/PERSISTENT—</strong>TaskMan queues the job as it does for “<strong>STARTUP</strong>". It marks it as a “<strong>PERSISTENT</strong>” task to be restarted if it stops unexpectedly.</td>
</tr>
<tr class="odd">
<td><strong>P</strong></td>
<td><p><strong>PERSISTENT—</strong>TaskMan runs it on its normal schedule, marking it as <strong>PERSISTENT</strong>. TaskMan restarts the task if it stops unexpectedly.</p>
<p>If the task completes in a normal fashion it is treated like any other regularly scheduled task and it is rescheduled based on the value in the RESCHEDULING FREQUENCY (#6) field in the OPTION SCHEDULING (#19.2) file.</p></td>
</tr>
</tbody>
</table>

<span id="_Toc193181860" class="anchor"></span>Table 7: Option Scheduling Frequency Code Formats

<table>
<caption><p><span id="_Ref21830851" class="anchor"></span>Table 8: Day Codes Used in Option Scheduling Frequency Code Formats</p></caption>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr class="header">
<th>Code</th>
<th>Frequency</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>nS</strong></td>
<td>Every <em><strong>n</strong></em> seconds.</td>
</tr>
<tr class="even">
<td><strong>nH</strong></td>
<td>Every <em><strong>n</strong></em> hours.</td>
</tr>
<tr class="odd">
<td><strong>nD</strong></td>
<td>Every <em><strong>n</strong></em> days.</td>
</tr>
<tr class="even">
<td><strong>nM</strong></td>
<td>Every <em><strong>n</strong></em> months.</td>
</tr>
<tr class="odd">
<td><strong>day[@time]</strong></td>
<td>Day of week (for Day codes, see <u>Table 8</u>).</td>
</tr>
<tr class="even">
<td><strong>D[@time]</strong></td>
<td>Every weekday.</td>
</tr>
<tr class="odd">
<td><strong>E[@time]</strong></td>
<td>Every weekend day (<strong>Sat,Sun</strong>).</td>
</tr>
<tr class="even">
<td><strong>nM(entry[,entry[,...]])</strong></td>
<td><p>Every <em><strong>n</strong></em> months, at each entry in the parameter list; the entries in the parameter list (for every <em>n</em> months only) can be:</p>
<table>
<caption><p><span id="_Toc193181862" class="anchor"></span>Table 9: Examples of Option Scheduling Frequency Code Formats</p></caption>
<colgroup>
<col style="width: 29%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Entry Format</strong></th>
<th><strong>Frequency</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>dd[@time]</strong></td>
<td>Day of month (such as <strong>15</strong>).</td>
</tr>
<tr class="even">
<td><strong>n<u>day</u>[@time]</strong></td>
<td>Nth day of week in month (such as <strong>1W,3W</strong>).</td>
</tr>
<tr class="odd">
<td><strong>L[@time]</strong></td>
<td>Last day of month.</td>
</tr>
<tr class="even">
<td><strong>L<u>day</u>[@time]</strong></td>
<td>Last specific DAY in month, (such as <strong>LM,LT,LW...</strong>).</td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

<span id="_Ref21830851" class="anchor"></span>Table 8: Day Codes Used in Option Scheduling Frequency Code Formats

| Day Code | Description |
|----------|-------------|
| M    | Monday      |
| T    | Tuesday     |
| W    | Wednesday   |
| R    | Thursday    |
| F    | Friday      |
| S    | Saturday    |
| U    | Sunday      |

<span id="_Ref433292846" class="anchor"></span>Table 10: ^%ZTSCH (SCHEDULE File) Nodes

| Code                     | Frequency                                                 |
|--------------------------|-----------------------------------------------------------|
| 12H                  | Every 12 hours.                                       |
| 14D                  | Every 14 days.                                        |
| 1M(1,15)             | First and 15th of the month.                              |
| 1M(L@23:45)          | Last day of the month at 11:45 pm.                    |
| 1M(LS)               | The last Saturday of the month.                           |
| 3M(15@12:00,L@12:00) | Noon (on the 15th and last days), every 3 months. |
| W@4pm                | Each Wednesday at 4 pm.                               |
| D                    | Each weekday.                                             |

<span id="_Ref85961274" class="anchor"></span>Table 11: TaskMan Task Status Codes

#### Problems with Scheduled Options

Once an option has been put on a schedule, it stays on that schedule unless one of the following happens:

- You delete the task.
- The running task aborts while setting up the next task in the sequence; the schedule sequence is broken.
- You dequeue the task that is scheduled to run the option. You *must* either requeue the task or use the Schedule/Unschedule Options \[XUTM SCHEDULE\] option to start the cycle over.
- You change the value in the RESCHEDULING FREQUENCY (#6) field in the OPTION SCHEDULING (#19.2) file. The new increment is used beginning after the next time the option runs.
- You change the value in the QUEUED TO RUN AT WHAT TIME (#2). The currently scheduled task is unscheduled, and a new one is scheduled for the time you specify.

Another peculiarity in this process involves using a monthly scheduling frequency. What should happen if on January 31st you queue an option and give it a monthly scheduling frequency? Other months lack a 31st day. In this situation, the task pretends there is a 31st day in every month. To avoid this, you can use the RESCHEDULING FREQUENCY (#6) field in the OPTION SCHEDULING (#19.2) file code 1M(L@time).

#### One-time Option Queue Option

<span id="_Toc193181863" class="anchor"></span>Figure 47: One-time Option Queue Option

SYSTEMS MANAGER MENU ... \[EVE\]

Taskman Management ... \[XUTM MGR\]

<span class="mark">One-time Option Queue</span> \[XU OPTION QUEUE\]

Use the One-time Option Queue \[XU OPTION QUEUE\] option to run at a special time one day without affecting its established schedule. It queues a task to run once, without affecting the option’s normal schedule in any way. This lets you handle the condition where you have an option queued to run periodically and you would like to queue it once to run at an irregular time without affecting its normal periodic schedule.

## Taskman Error Log Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The manager and submanagers keep track of all errors caused by their own software or by the tasks they start. They log their own errors in two places:

- ERROR LOG (#3.075) file
- TaskMan Error Log

Those errors caused by tasks are also recorded in the entries of the tasks themselves and can be seen with any of the various task listing options (List Tasks, TaskMan User, and so on). Just as there are options to display and purge the ERROR LOG (#3.075) file, there are options to do the same for the TaskMan Error Log.

When the Queuable Task Log Cleanup \[XUTM QCLEAN\] option cleans tasks from the TASKS (#14.4) file, it also cleans any corresponding entries in the TaskMan Error Log since it is hard to make sense of an error log entry without the task data.

Kernel strongly recommends that you report new errors to your OIFOs and follow up to ensure expeditious patching. If you do this, over time the number of errors occurring on your system diminishes. This also improves the value of the various error logging systems as indicators of significant events deserving investigation.

Allocation and store errors are often *not* logged in Kernel’s ERROR LOG (#3.075) file because the process of logging errors is complicated and usually requires the use of local variables. Local variables take up space and there is no excess space when these errors occur. However, TaskMan makes its simple entries in the TaskMan Error Log prior to calling the Kernel error logging utility. Thus, these errors are often recorded in the TaskMan Error Log, but *not* Kernel’s. You are encouraged to carefully monitor both places.

### Show Error Log Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc193181864" class="anchor"></span>Figure 48: Show Error Log Option

SYSTEMS MANAGER MENU ... \[EVE\]

Taskman Management ... \[XUTM MGR\]

Taskman Management Utilities ... \[XUTM UTIL\]

Taskman Error Log ... \[XUTM ERROR\]

<span class="mark">Show Error Log</span> \[XUTM ERROR SHOW\]

The Show Error Log \[XUTM ERROR SHOW\] option displays the errors currently stored in the TaskMan Error Log, showing the date and time that the error occurred in a readable format and showing the error message. After the listing, the option gives the number of errors in the error log.

Errors stored in the TaskMan Error Log historically are also cross-referenced to the TASKS (#14.4) file, linking tasks to the errors they cause.

### Clean Error Log Over Range Of Dates Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc193181865" class="anchor"></span>Figure 49: Clean Error Log Over Range Of Dates Option

SYSTEMS MANAGER MENU ... \[EVE\]

Taskman Management ... \[XUTM MGR\]

Taskman Management Utilities ... \[XUTM UTIL\]

Taskman Error Log ... \[XUTM ERROR\]

<span class="mark">Clean Error Log Over Range Of Dates</span> \[XUTM ERROR LOG CLEAN RANGE\]

After prompting for a “First date to purge:” and a “Final date to purge:”, the Clean Error Log Over Range Of Dates \[XUTM ERROR LOG CLEAN RANGE\] option removes the entries for all errors that occurred on and between the two dates. It prints the number of entries removed. If the first date is *not* earlier than the final date, no entries are removed.

Use this option to delete all but recent errors that deserve your attention. It is better to resolve specific kinds of errors as you encounter them. However, if there is a period during which you *cannot* resolve them fast enough to keep the log clean, this option helps you focus on the recent ones.

### Purge Error Log Of Type Of Error Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc193181866" class="anchor"></span>Figure 50: Purge Error Log Of Type Of Error Option

SYSTEMS MANAGER MENU ... \[EVE\]

Taskman Management ... \[XUTM MGR\]

Taskman Management Utilities ... \[XUTM UTIL\]

Taskman Error Log ... \[XUTM ERROR\]

<span class="mark">Purge Error Log Of Type Of Error</span> \[XUTM ERROR PURGE TYPE\]

With the Purge Error Log Of Type Of Error \[XUTM ERROR PURGE TYPE\] option you can delete from the TaskMan Error Log all entries for an error of a specific type. In fact, this option uses the M contains operator (\[); therefore, it removes every error whose message contains your input as a substring. For example, you can remove every error that occurred in a certain routine or even every error whose message contains a Q. After performing the purge, the option shows you how many entries were removed.

This option is the best way to keep the log clean. As you resolve certain kinds of errors and prevent them from happening again, you can remove all errors of that kind from the log. This leaves behind only those errors you have *not* resolved, helping you focus on the problems that remain.

### Delete Error Log Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc193181867" class="anchor"></span>Figure 51: Delete Error Log Option

SYSTEMS MANAGER MENU ... \[EVE\]

Taskman Management ... \[XUTM MGR\]

Taskman Management Utilities ... \[XUTM UTIL\]

Taskman Error Log ... \[XUTM ERROR\]

<span class="mark">Delete Error Log</span> \[XUTM ERROR DELETE\]

The Delete Error Log \[XUTM ERROR DELETE\] option completely deletes all errors in the TaskMan Error Log. If the error log is cleaned and purged as described above, you rarely need to use this option.

## Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The information given in this section *cannot* be used by application developers in their code. It is provided to help site managers troubleshoot problems with tasks and TaskMan. Consider this section a reference to TaskMan’s global structure and messages.

### SCHEDULE File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ^%ZTSCH global holds the *non*-VA FileMan-compatible SCHEDULE file, which consists of independent lists and nodes (see <u>Table 10</u>). This is where TaskMan processes tasks. This structure is *not* supported for use by application software. All task manipulation *must* be done through approved options and entry points. These structures *must* be free to change from version to version to easily adapt and meet the changing needs of VistA. On the following pages is an example of a global that contains one of each type of node used by TaskMan:

The initial node was used to create ^%ZTSCH before TaskMan was active, so that the global type and protection could be assigned.

| ^%ZTSCH Node                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|----------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ^%ZTSCH(next run time, task \#)          | This node stores the Schedule List. The task \# corresponds to an entry in the TASKS (#14.4) file, and the next run time is computed from the value in the sixth ^-piece of the entry’s 0 node (and is the total number of seconds contained in the next run time’s \$H translation). If the Schedule List entry equals a device name, the entry was *not* created through the Program Interface.                                                                                                                                                                                                                                                              |
| ^%ZTSCH(“C”)                             | This node stores the Compute Server Job List (C list). This list holds tasks that are ready to be run by submanagers on specific Compute Servers. A submanager cross-Volume Set jobbed to a Compute Server only runs tasks under this list for the Compute Server on which it is running and does *not* process the Device Waiting List or the Job List. The Volume Set, next run time, task \#, and device \$IO are stored here.                                                                                                                                                                                                                                  |
| ^%ZTSCH(“DEV”)                           | This node stores the Device Allocation List. This list is used by TaskMan to coordinate its allocation of devices to tasks. The presence of a node indicates that TaskMan has already allocated this device to a specific task that has *not* yet gained ownership of it. It tells TaskMan *not* to give the device to another task. When the task for whom the allocation node was established gains ownership of the device or fails due to possession by some interactive job, the node is KILLed off. The \$H value is used in case the task fails to remove its own node for some reason; after two minutes TaskMan KILLs the node on its next idle loop. |
| ^%ZTSCH(“ER”)                            | This node stores the TaskMan Error Log.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ^%ZTSCH(“ES”)                            | This node stores the Error Screens.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ^%ZTSCH(“IDLE”)                          | This node is used to ensure that the Manager’s idle loop activities are spaced out correctly in case multiple managers are being run in the same environment.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ^%ZTSCH(“IO”)                            | This node stores the Device Waiting List. The device \$IO value is the value for the task’s device and should *not* be the \$IO of a spool or host file device. The run time subscript (the total number of seconds contained in the run time’s \$H translation) prioritizes the tasks that should have started the longest time ago. The submanagers use the top node to space out access to the list and the last device so that only one submanager at a time is checking the list, and so that checks that find all devices still busy are followed by a short waiting period before the list is checked again.                                            |
| ^%ZTSCH(“JOB”)                           | This node stores the Job List. This list holds tasks that are ready to be run by submanagers. The run time is the total number of seconds contained in the run time’s \$H translation, and the task \# and device \$IO are what you would expect.                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ^%ZTSCH(“LINK”)                          | This node stores the Link Lists. The LINK node itself is only present when a link is down. It is used to time the checks that occur every fifteen minutes. The second level nodes should always be present with the current information on each of the CPUs and Volume Sets.                                                                                                                                                                                                                                                                                                                                                                                           |
| ^%ZTSCH(“LOAD”, load rating)             | This node is used to balance the CPU load among the various managers that work out of the current TASKS and Schedule files. It identifies the CPU that most recently checked its rating and decided to run. Managers more loaded (a lower rating) than this one wait to allow this Manager to pick up more of its share of the load.                                                                                                                                                                                                                                                                                                                                       |
| ^%ZTSCH(“LOADA”)                         | This node stores the Load List. This list records the ratings for all CPUs with managers processing this TASKS file. The first ^-piece, which flags the managers that decide to wait to balance the load, is used to tell the submanagers on those CPUs that they, too, should wait.                                                                                                                                                                                                                                                                                                                                                                                   |
| ^%ZTSCH(“LOGRSRC”)                       | This node flags whether submanagers should log resources for the capacity management software. This node is set for every Volume Set whenever the LOG RESOURCE USAGE? field of the KERNEL SYSTEM PARAMETERS (#8989.3) file is edited. A cross-reference keeps the ^%ZTSCH(“LOGRSRC”) node in synchronization with the LOG RESOURCE USAGE? field.                                                                                                                                                                                                                                                                                                                       |
| ^%ZTSCH(“NO-OPTION”)                     | If set, this node stops the submanagers from running any scheduled options. This is for the KIDS install process.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ^%ZTSCH(“RUN”)                           | This node is where the Manager periodically stamps the current time, leaving a way to determine whether it is currently active. Invoking the Stop Task Manager \[XUTM STOP\] option removes this node (see <u>Figure 52</u>).                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ^%ZTSCH(“STARTUP”, UCI, option \#)       | This node holds the Startup List. This list holds the internal number of all options that are specially queued to run every time the Manager starts up. The \$HOROLOG value reflects when the option was placed on this list.                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ^%ZTSCH(“STATUS”, \$J of Manager)        | This node holds the Status List. This list holds the periodically updated entries for each Manager active on your machine and reflects each Manager’s own perception of its current state.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| ^%ZTSCH(“STOP”)                          | This node prevents submanagers from running. While it is present, managers do *not* start new submanagers, submanagers waiting for tasks quit immediately, and those currently running tasks quit as soon as the tasks finish.                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ^%ZTSCH(“SUB”)                           | This node counts the number of submanagers waiting for new tasks. It is updated regularly by submanagers as they run tasks. The Manager uses this value to decide whether to JOB out new submanagers and adjusts its value during the idle loop whenever it believes it to be inaccurate.                                                                                                                                                                                                                                                                                                                                                                              |
| ^%ZTSCH(“SYNC”,device,sync flag,task \#) | This node stores the Task-Sync Pair Lists. These are the waiting tasks in order of execution by task \#, which are grouped by Device and assigned SYNC FLAG. All sub-nodes will always be present if there are Task-Sync Pair tasks that are waiting for execution while a running Task-Sync Pair task is active. Task-Sync Pair tasks are groups of tasks that run sequentially in Task \# order. Task-Sync Pair tasks that are running are removed from this list and placed on TaskMan’s currently running list, which is the ^%ZTSCH(“TASK”,task \#) node.                                                                                             |
| ^%ZTSCH(“TASK”, task \#)                 | This node holds the tasks TaskMan believes are currently running. Since entries are cleaned up when tasks quit or encounter errors, those that are forcibly exited by the system manager are left on the list even though they are *not* running. The Manager clears the list whenever the system starts up, and the system manager can manually remove inaccurate entries by using the exit action of the KILL off a users’ job \[XURESJOB\] option. The task data stored at each node allows TaskMan to list the tasks even when they clean out their TASKS (#14.4) file records when they start instead of when they quit.                                          |
| ^%ZTSCH(“UPDATE”, \$J of Manager)        | This node records when the Manager last updated its local information about the site parameters. This node is KILLed whenever the Manager should update (such as site parameters are changed).                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| ^%ZTSCH(“WAIT”)                          | This node puts the Manager into a WAIT state.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

<span id="_Ref29377440" class="anchor"></span>Table 12: TaskMan Rejection Messages

<span id="_Ref85965905" class="anchor"></span>Figure 52: ^%ZTSCH Global Structure

^%ZTSCH= ""

^%ZTSCH(next run time, task \#)= ""

^%ZTSCH(next run time, task \#)= (D1) device IOP value

^%ZTSCH("C", volume set)= count

^%ZTSCH("C", volume set, next run time, task \#) = device \$IO

^%ZTSCH("DEV", device \$IO)= \$H when device was allocated for a specific

==\>task

^%ZTSCH("ER")= "A1" or ""

^%ZTSCH("ER", \$H when error happened)= error message

^%ZTSCH("ER", \$H when error happened, 0)= context of error

^%ZTSCH("ES", error screen, 0)= ""

^%ZTSCH("ES", error screen, 1)= screened errors count

^%ZTSCH("IDLE")= \$H when the Manager's idle loop checks were last performed

^%ZTSCH("IO")= \$H when device waiting list was last checked without finding

==\> an available device^ \$IO of last device tried

^%ZTSCH("IO", device \$IO)=device type

^%ZTSCH("IO", device \$IO, run time, task \#)= ""

^%ZTSCH("JOB", run time, task \#) = device \$IO

^%ZTSCH("LINK")= "" or \$H when dropped link was last checked

^%ZTSCH("LINK", volume set)= 1 if link has dropped

^%ZTSCH("LINK", volume set, next run time, task \#)= ""

^%ZTSCH("LOAD", load rating) = cpu ^ \$H when rating was checked

^%ZTSCH("LOADA", cpu) = whether TM should wait ^ load rating ^ \$H

==\>when rating was checked ^ \$J of Manager

^%ZTSCH("LOGRSRC") = ""

^%ZTSCH("NO-OPTION")= ""

^%ZTSCH("RUN")= \$H when Manager last checked in

^%ZTSCH("STARTUP", UCI, option \#)= \$H when option was first queued for

==\>startup

^%ZTSCH("STATUS", \$J of Manager)= \$H when Manager last checked in \[1\] ^

==\>status \[2\] ^ description of status \[3\]

^%ZTSCH("STOP")= ""

^%ZTSCH("SUB")= count of Submanagers waiting for tasks

^%ZTSCH("TASK", task \#)= (A2) entry point \[1\] ^ (A3) routine \[2\] ^ (A4)

==\>option \# \[3\] ^ (A5) option name \[4\] ^ (C6)

==\>description \[5\] ^ device name \[6\] ^ (E1) UCI \[7\] ^

==\>(C3) creation time \[8\] ^ (C1) creator DUZ or (C2)

==\>creator name \[9\] ^ \$J of running task \[10\] ^ \$H

==\>when task actually started running \[11\]

^%ZTSCH("UPDATE", \$J of Manager)= \$H when the Manager last updated its

==\>parameters

^%ZTSCH("WAIT")= ""

### TASKS (#14.4) File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ^%ZTSK global holds this partially-VA FileMan-compatible file of tasks. It is structured with a descriptor node followed by sequential entries. The data dictionary for this file is 14.4, TASKS. It is a read-only file. The TASKS (#14.4) file has no cross-references, *not* even a top-level B cross-reference, and its descriptor node is updated by the Queuable Task Log Cleanup \[XUTM QCLEAN\] option.

Each entry itself contains a Zero node and several decimal nodes followed by several storage nodes. Like the SCHEDULE file, the TASKS (#14.4) file is *not* available for direct manipulation or examination by application software. Site managers, however, can print out information on entries in the TASKS (#14.4) file using VA FileMan.

<u>Figure 53</u> describes the nodes 0 through .26 for each entry in the TASKS (#14.4) file:

<span id="_Ref85961073" class="anchor"></span>Figure 53: TASKS (#14.4) File Nodes (1 of 2)

^%ZTSK(task \#, 0)= (#.01) Entry Point \[1F\] ^ (#2) Routine Name \[2F\] ^ (#3) User

==\>\[3P:200\] ^ (#4) Requested UCI \[4F\] ^ (#5) Creation Time (\$H)

==\>\[5F\] ^ (#6) Scheduled Run Time (\$H) \[6F\] ^ (#7) Type of Task

==\>\[7F\] ^ (#8) Option Number \[8N\] ^ (#9) Option Name \[9F\] ^ (#10)

==\>Creator Name \[10F\] ^

==\> (#11) Creation UCI \[11F\] ^ (#12) Creation Volume Set \[12F\] ^

==\>(#13) RESERVED \[13F\] ^ (#14) Requested Volume Set \[14F\] ^ (#15)

==\>Priority \[15N\] ^ (#16) Original Create date (\$H) \[16F\]

^%ZTSK(task \#, .01)= (#21) Original Destination UCI \[1F\] ^ (#22) Original

==\>Destination Volume \[2F\] ^

^%ZTSK(task \#, .02)= (#31) Current Destination UCI \[1F\] ^ (#32) Current

==\>Destination Volume Set \[2F\] ^ (#33) Hop Count \[3N\] ^

^%ZTSK(task \#,.03)= (#41) Task Description \[E1,240F\]^%ZTSK(D0,.04)= (#42) Schedule Time Seconds \[1N\] ^

^%ZTSK(task \#, .1)= (#51) Status Code \[1F\] ^ (#52) Last Update \$H \[2F\] ^ (#53)

==\>Status Notes \[3F\] ^ (#54) Job \[4N\] ^ ^ ^ ^ (#59.8) Remember

==\>Until \[8F\] ^ ^ (#59.1) Stop Flag \[10F\]^

^%ZTSK(task \#, .12, (#71) Error Count \[1N\] ^ (#72) Error \$H \[2F\] ^ (#73) Error

==\>Message \[3F\] ^

^%ZTSK(task \#, .2)= (#81) Device IOP value \[1F\] ^ (#82) \$IO value \[2F\] ^ (#83)

==\>Device Type \[3F\] ^ (#84) Device Sub-Type \[4F\] ^ (#85) Device

==\>%IS modifier \[5F\] ^ (#86) Host File Address \[6F\] ^ (#87) Sync Flag \[7F\] ^ (#88) IO

==\>Reschedule Count \[8N\] ^

^%ZTSK(task \#, .21)= (D8) device file entry \# \[1\] ^

^%ZTSK(task \#, .25)= (D7) device parameters \[1\] ^

The remaining nodes of each entry are used to pass variables to the task. If the task has been manipulated only using TaskMan’s Program Interface, then the entries look like <u>Figure 54</u>:

<span id="_Ref204580950" class="anchor"></span>Figure 54: TASKS (#14.4) File Nodes (2 of 2)

^%ZTSK(task \#, .3, "name")= (F2) value of saved variable

^%ZTSK(task \#, .3, "array(", node \#)= (F2) value of saved variable

^%ZTSK(task \#, .3, "array", node \#)= (F2) value of saved variable

The distinguishing characteristic here is the fact that the variables to be passed are all subscripted under the .3-node.

### Task Status Codes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section lists the various codes that may be found in the first ^-piece of the .1 node, the text displayed for that code by the List Tasks action, and the meaning of that code. These codes are set into the tasks at every point in processing where the status changes, along with a time stamp and an explanation where necessary.

Several of the codes correspond to the status of the SCHEDULE file entry for the task. If all applications used the Program Interface, the status code would always agree with the task’s real status. In fact, many applications still directly manipulate ^%ZTSCH and ^%ZTSK, and they often neglect to update the status codes. Whenever the SCHEDULE file disagrees with the status code, the SCHEDULE file is correct. This is the reason many of the codes listed in <u>Table 11</u> have multiple meanings.

Status codes 1 through 6 represent one of two common paths a task takes through TaskMan. The other common path replaces code 3 with A, where the task’s device is *not* immediately available.

<table>
<caption><p><span id="_Ref29300908" class="anchor"></span>Table 13: TaskMan PAUSE States</p></caption>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th>Status Code</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>0</strong></td>
<td>Incomplete or still being created.</td>
</tr>
<tr class="even">
<td><strong>1</strong></td>
<td><p>Scheduled for <em>&lt;Date and Time&gt;</em>.</p>
<p>TaskMan uses this status in every option and entry point that schedules a task.</p>
<p>If the task fails or errors out and TaskMan <em>cannot</em> trap the error, this status has a different meaning: “Stopped irregularly while scheduled.”</p></td>
</tr>
<tr class="odd">
<td><strong>2</strong></td>
<td><p>Being inspected by TaskMan.</p>
<p>The Manager sets this status when the time comes for a task to run. As it removes the task from the SCHEDULE file, it sets this code into the task.</p></td>
</tr>
<tr class="even">
<td><strong>3</strong></td>
<td><p>Waiting for a partition.</p>
<p>When the Manager places a task in the Job list of the SCHEDULE file, it gives the task this code.</p>
<p>If the task fails or errors out, and TaskMan <em>cannot</em> trap the error, this status has a different meaning: “Stopped irregularly while waiting for a partition.”</p></td>
</tr>
<tr class="odd">
<td><strong>4</strong></td>
<td><p>Being prepared.</p>
<p>The submanager gives a task this code when it removes the task from the Job list or Busy Device Waiting list to run it.</p></td>
</tr>
<tr class="even">
<td><strong>5</strong></td>
<td><p>Currently running.</p>
<p>The submanager gives a task this status just before it starts the task at its entry point.</p>
<p>If the task fails or errors out, and TaskMan <em>cannot</em> trap the error, this status has a different meaning: “Started running <em>&lt;Date and Time&gt;</em> and stopped irregularly.”</p></td>
</tr>
<tr class="odd">
<td><strong>6</strong></td>
<td><p>Completed &lt;date and time&gt;.</p>
<p>The submanager gives a task this status after the task quits.</p></td>
</tr>
<tr class="even">
<td><strong>A</strong></td>
<td><p>Waiting for device <em>&lt;Device Name or <strong>$I</strong>&gt;</em>.</p>
<p>The Manager or the submanager gives a task this status when it places the task in the Busy Device Waiting list.</p>
<p>If the task fails or errors out and TaskMan <em>cannot</em> trap the error, this status has a different meaning: “Stopped irregularly while waiting for a device.”</p></td>
</tr>
<tr class="odd">
<td><strong>B</strong></td>
<td><p>Rejected. <em>&lt;rejection message&gt;</em>.</p>
<p>The Manager or the submanager gives a task this status if it fails one of the basic validation tests. (The rejection messages are contained in the “<a href="#task-rejection-messages">Task Rejection Messages</a>” section.)</p></td>
</tr>
<tr class="even">
<td><strong>C</strong></td>
<td><p>Error <em>&lt;date and time&gt;</em>. <em>&lt;error message&gt;</em>.</p>
<p>The submanager gives a task this status if it traps an error after starting the task. The error message records the vendor-specific <strong>$ZE</strong> text.</p></td>
</tr>
<tr class="odd">
<td><strong>D</strong></td>
<td><p>Stopped by user.</p>
<p>The manager or the submanager gives a task this status if, when TaskMan removes the task from the SCHEDULE file for processing, it finds that the user has asked the task to stop. The submanager also assigns this status if, just before starting the task, it finds the stop request has been made. Finally, the submanager gives a task this status if the task uses the <strong>ZTSTOP</strong> output variable to report that it stopped in response to a user’s request.</p>
<p>![](kernel-8-0-systems-management-taskman-user-guide/038.png) <strong>REF:</strong> For an explanation of <strong>ZTSTOP</strong>, see the description of <strong>$$S^%ZTLOAD</strong> API in the <a href="https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_taskman_ug.pdf"><em>Kernel 8.0 Developer’s Guide: TaskMan: Developer Tools User Guide</em></a>. Kernel and Kernel Toolkit APIs are also available in HTML format at a VA Intranet website.</p></td>
</tr>
<tr class="even">
<td><strong>E</strong></td>
<td><p>Interrupted while running.</p>
<p>At startup, the Manager gives this status to any task listed in the Task list of the SCHEDULE file as still running.</p></td>
</tr>
<tr class="odd">
<td><strong>F</strong></td>
<td><p>Unscheduled by <em>&lt;Username or “you”&gt;</em>.</p>
<p>The <strong>Dequeue Tasks</strong> [XUTM DQ] and <strong>TaskMan User</strong> [XUTM USER] options and the <strong>DQ^%ZTLOAD</strong> entry point use this status for tasks they unschedule.</p></td>
</tr>
<tr class="even">
<td><strong>G</strong></td>
<td><p>Waiting for the link to &lt;volume set name&gt; to be restored.</p>
<p>The Manager uses this status for tasks that would have been transferred to a different TaskMan environment and deleted from this one, if the local area network link to the remote environment were functioning properly.</p>
<p>If the task fails or errors out, and TaskMan <em>cannot</em> trap the error, this status has a different meaning: “Stopped irregularly while waiting for a link.”</p></td>
</tr>
<tr class="odd">
<td><strong>H</strong></td>
<td><p>Edited without being scheduled.</p>
<p>The <strong>Requeue Tasks</strong> [XUTM REQ] and <strong>TaskMan User</strong> [XUTM USER] options and the <strong>REQ^%ZTLOAD</strong> entry point use this status when edited tasks are <em>not</em> subsequently rescheduled.</p></td>
</tr>
<tr class="even">
<td><strong>I</strong></td>
<td><p>Discarded by TaskMan because its record was incomplete.</p>
<p>The Manager or the submanager uses this status for tasks listed in the SCHEDULE file that lack critical information in the corresponding TASKS (#14.4) file entries.</p></td>
</tr>
<tr class="odd">
<td><strong>J</strong></td>
<td><p>Currently being edited.</p>
<p>This status has been set aside for possible use in future versions of TaskMan.</p></td>
</tr>
<tr class="even">
<td><strong>K</strong></td>
<td><p>Created without being scheduled.</p>
<p>The <strong>^%ZTLOAD</strong> entry point uses this status for tasks when the application passes <strong>ZTDTH=“@”</strong>. Kernel Toolkit utility <strong>^%ZTMOVE</strong> uses this value for the tasks it creates to transfer routines between Volume Sets manually.</p></td>
</tr>
<tr class="odd">
<td><strong>L</strong></td>
<td><p>Preparing this task caused the submanager an error <em>&lt;date and time&gt;</em>. <em>&lt;error msg&gt;</em>.</p>
<p>The submanager uses this status when it traps an error after claiming a task but before starting it.</p>
<p>The Manager does <em>not</em> yet record a corresponding status for the analogous situation. Tasks that never start, that are left with a status of <strong>2</strong>, have usually caused the Manager an error while it tried to examine them.</p></td>
</tr>
<tr class="even">
<td><strong>M</strong></td>
<td><p>Waiting for a partition on a Compute Server.</p>
<p>The Manager gives a task this code when it places the task in the Compute Server Job List.</p>
<p>If the task fails or errors out, and TaskMan <em>cannot</em> trap the error, this status has a different meaning: “Stopped irregularly while waiting for a partition on a Compute Server.”</p></td>
</tr>
</tbody>
</table>

<span id="_Ref29300908" class="anchor"></span>Table 13: TaskMan PAUSE States

### Task Rejection Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Under certain conditions TaskMan can avoid trapping obvious errors by checking the tasks themselves for internal consistency. Whenever it finds tasks with bad data, it rejects them. This involves unscheduling them, setting their status codes to B, and adding a brief explanatory message. These messages listed in <u>Table 12</u> can help identify bugs in application queuing software, in the local system configuration, or in TaskMan itself.

<table>
<caption><p><span id="_Ref29377543" class="anchor"></span>Table 14: TaskMan RUN States</p></caption>
<colgroup>
<col style="width: 38%" />
<col style="width: 61%" />
</colgroup>
<thead>
<tr class="header">
<th>TaskMan Rejection Message</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>BAD DESTINATION UCI</td>
<td><p>The Manager rejects a task for this reason under three different conditions:</p>
<ul>
<li><p>If the task is bound for the Manager’s own Volume Set, whatever value has been passed for the destination UCI <em>must</em> be a valid UCI on the current Volume Set. If <strong>^%ZOSF(“UCICHECK”)</strong> rejects the UCI, TaskMan rejects the task.</p></li>
<li><p>If the task is bound for a different Volume Set and the destination UCI is <em>not</em> listed in the UCI ASSOCIATION (#14.6) file under that Volume Set, the UCI <em>must</em> be accepted as a valid UCI on the current Volume Set so TaskMan can use File #14.6 to determine where the task should run. If <strong>^%ZOSF(“UCICHECK”)</strong> rejects the UCI, TaskMan rejects the task.</p></li>
<li><p>If the task is bound for a different Volume Set and that Volume Set’s link is down and its REPLACEMENT VOLUME SET is the current Volume Set, TaskMan rejects the task.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>BAD DESTINATION VOLUME SET</td>
<td>Every task’s destination Volume Set <em>must</em> be listed in the VOLUME SET (#14.5) file.</td>
</tr>
<tr class="odd">
<td>BAD IO DEVICE &lt;$I&gt;</td>
<td>If a port goes bad while many tasks wait for it in the Busy Device Waiting list, TaskMan traps an error whenever the port is tested for availability. When the submanager traps such an error, it rejects every task waiting for that device.</td>
</tr>
<tr class="even">
<td>INVALID OUTPUT DEVICE</td>
<td>The Manager performs a lookup on the devices that tasks request. If the <strong>^%ZIS</strong> call indicates that the device does <em>not</em> exist, TaskMan rejects the task.</td>
</tr>
<tr class="odd">
<td>INVALID ROUTINE NAME</td>
<td>If a task’s entry point is in a <strong>%</strong>-routine, the Manager tests for that routine’s existence in the library UCI. If the routine does <em>not</em> exist there, TaskMan rejects the task.</td>
</tr>
<tr class="even">
<td>NO DESTINATION UCI</td>
<td>When older applications bypassed the Program Interface, they sometimes scheduled tasks without specifying the destination UCI. The Manager rejects all such tasks.</td>
</tr>
<tr class="odd">
<td>NO LINK ACCESS TO VOLUME SET</td>
<td>If the VOLUME SET (#14.5) file entry for a task’s destination Volume Set indicates there is no link access to that Volume Set, the task is rejected.</td>
</tr>
<tr class="even">
<td>NO ROUTINE AT DESTINATION</td>
<td>If a task’s entry point is in a <em>non</em>-<strong>%</strong>-routine, then the check for the routine’s existence is done by the submanager prior to starting the task.</td>
</tr>
</tbody>
</table>

<span id="_Ref29377543" class="anchor"></span>Table 14: TaskMan RUN States

### TaskMan State Messages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When the Manager does *not* run, all background processing grinds to a halt. For this reason, the Manager’s condition is of vital importance to system managers. When problems are detected with background processing at a site, checking the Manager’s condition should be the first step. The Manager periodically records its state in the Status List. The Monitor TaskMan \[XUTM ZTMON\] option displays this list near the top of the screen. The various states and their meanings are described in the sections that follow.

#### BALANCE State

The Manager lists itself in this state if other managers (that are processing the same files) appear to have more CPU capacity available than the current Manager. While in the BALANCE state, the Manager does *not* process any tasks or start any new submanagers. The manager removes itself from the BALANCE state when it appears to have at least as much CPU capacity as the active Manager. In general, when many managers are working out of the same TASKS (#14.4) and SCHEDULE files, most of them are in the BALANCE state at any given time, with only the one or two least loaded managers processing tasks.

![](kernel-8-0-systems-management-taskman-user-guide/039.png) REF: For more information about TaskMan load balancing, see the “[Multiple TaskMan Managers and Load Balancing](#multiple-taskman-managers-and-load-balancing)” section in the “<u>TaskMan: System Management—Configuration</u>” section.

#### ERROR State

The Manager lists itself in the ERROR state after trapping errors. On some systems the process of recording an error is slow, so the presence of a distinct state helps identify the source of delay to the system manager. A troubleshooter who sees this state for TaskMan should immediately check the TaskMan Error list to see what kind of error is being recorded. Because TaskMan’s code is structured as a series of nested loops, it can very easily generate thousands of errors a day under certain conditions.

#### PAUSE State

The PAUSE state means that some external condition is preventing the Manager from processing tasks. The description always indicates the cause. While in the PAUSE state, the Manager waits until the problem is resolved, checking once every 60 seconds. <u>Table 13</u> lists the pause states:

| PAUSE State                                                              | Description                                                                                                                                                                                                                                                                                                                                     |
|--------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| The following required ^%ZOSF nodes are undefined, \<list of nodes\> | When the Manager starts, restarts, or recovers from a trapped error, its first order of business is to drop through some setup code that checks TaskMan’s environment. If any critical ^%ZOSF nodes are missing, it enters a PAUSE state and waits until the system manager restores the nodes.                                         |
| Required link to \<volume set name\> is down                             | The other key check in the setup code is to ensure that all Volume Sets listed in the VOLUME SET (#14.5) file as required can be reached. The Manager tests each required link and enters the PAUSE state if any tests cause an error. The Manager remains in the PAUSE state, periodically testing the links, until they are restored. |
| Logons Inhibited                                                         | When the system manager sets the INHIBIT LOGONS? field of the VOLUME SET (#14.5) file, TaskMan enters a PAUSE state and waits until the flag is cleared.                                                                                                                                                                                    |
| No Signons Allowed                                                       | The system manager can use the software switch to stop logons, which places TaskMan in the PAUSE state.                                                                                                                                                                                                                                     |

#### RUN State

The RUN state (see <u>Table 14</u>) indicates that the Manager is going about its business in a relatively normal manner, managing background tasks on your system.

| RUN State                 | Description                                                                                                                                                                                                               |
|---------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Start                     | The Manager sets this value before and after executing the setup code at system startup.                                                                                                                                  |
| Setup                     | The Manager identifies when it executes the setup code to test its environment.                                                                                                                                           |
| Restart                   | The Manager sets this value after executing the setup code during a restart.                                                                                                                                              |
| Main Loop                 | This should be the Manager’s usual state. This indicates the Manager is executing the main loop that checks the environment, processes the Schedule list, and performs idle loop activities when appropriate.             |
| TaskMan Job Limit Reached | When the total number of processes on the Manager’s CPU exceeds the TaskMan Job Limit given in the VOLUME SET (#14.5) file, the Manager can continue to process the Schedule list but *cannot* start any new submanagers. |

#### WAIT State

While in the WAIT state, the Manager does *not*:

- React to changes in its environment.
- Process tasks.
- Enter PAUSE states.
- Stop after the Stop Task Manager \[XUTM STOP\] option has been used.

The following two options let you create or undo the WAIT state:

- [Place Taskman in a WAIT State Option](#place-taskman-in-a-wait-state-option) \[XUTM WAIT\]
- [Remove Taskman from WAIT State Option](#remove-taskman-from-wait-state-option) \[XUTM RUN\]

TaskMan *cannot* enter this state on its own; it can only be initiated manually. This is essentially a tool for you to tightly control the processing of tasks on your machines. The description for this state always reads “TaskMan Waiting”.

# Appendix A—Revision History Archive

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section should be used to show all document revision history prior to the current year.

![](kernel-8-0-systems-management-taskman-user-guide/040.png) REF: For the most recent, current year document revision history, see the “[Revision History](#_Toc234301875)” section.

| Date | Revision | Description | Author |
|------|----------|-------------|--------|
| TBD  | TBD      | TBD         | TBD    |

<span id="_Toc204581284" class="anchor"></span>Glossary

![](kernel-8-0-systems-management-taskman-user-guide/041.png) REF: For a glossary of terms specific to Kernel, see the “Glossary” section in the [*Kernel 8.0 Systems Management: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm.pdf#Main_Glossary).

![](kernel-8-0-systems-management-taskman-user-guide/042.png) REF: For a list of commonly used terms and acronyms, see the VA Glossary Power App.