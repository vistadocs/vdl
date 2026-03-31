---
title: OR*3*529 EHRM Cutover Note Quick Reference Guide
doc_type: QRG
doc_label: Quick Reference Guide
doc_layer: patch
doc_subject: EHRM Cutover Note
app_code: CPRS
app_name: Computerized Patient Record System
section: CLI
app_status: active
pkg_ns: OR
patch_ver: 3
patch_id: OR*3*529
group_key: "CPRS:OR:3"
file_numbers: []
security_keys: []
menu_options: 0
description: - [VistA Cutover Utilities Menu](#vista-cutover-utilities-menu) New Functionality This patch provides functionality to maintain continuity of care during a site's Cerner cutover by creating a report of recent clinical activity for every patient seen in the last three years that providers can cross-r
audience: 
keywords: 
  - time
  - cutover
  - strong
  - test
  - evaluation
  - document
  - reminders
  - wall
  - clock
  - patients
page_count: 0
word_count: 813
section_count: 2
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/or_3_p529_qr.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Comp_Patient_Recrd_Sys_(CPRS)/or_3_p529_qr.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=61"
---

## Table of Contents

  - [VistA Cutover Utilities Menu](#vista-cutover-utilities-menu)
New Functionality
This patch provides functionality to maintain continuity of care during a site's Cerner cutover by creating a report of recent clinical activity for every patient seen in the last three years that providers can cross-reference during the initial cutover period. This is done by automatically creating documents for a single, user-selected patient, or to initiate a task to create a document for every patient that has had an inpatient, outpatient, or clinic visit in the past three years.
> Note: The *VistA Cutover Utilities Menu* is locked by the ORVCO Security Key.

## VistA Cutover Utilities Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Run System Benchmark
2.  Test Data Retrieval
3.  Create VistA Cutover Document(s)
4.  Monitor/Stop Cutover Jobs (optional)

> Select VistA Cutover \<TEST ACCOUNT\> Option:

> Note: Before you begin testing or creating cutover documents, it is highly recommended to run the CPRS Coversheet Time Test released with CPRS 31b.

Optional Step - Run the CPRS Coversheet Time Test \[PXRM CPRS TESTER\]

The CPRS Coversheet Time Test is optional but will provide essential timing information when testing or creating the clinical reminders cutover document. The clinical reminders cutover document uses the reminders included on the CPRS Coversheet and places that information into the document text.

The main pieces of information to evaluate from the results are:

- Elapsed wall clock time
- Total CPU coversheet evaluation time
- Longest CPU evaluation time
- Longest wall clock evaluation time.”

If the CPRS Coversheet Time Test reports an “Elapsed wall clock time” of less than 1 second, move to Step 1 below.

If the “Elapsed wall clock time” is 1 second or higher, it is highly suggested to remove reminders from the CPRS coversheet settings that require the longest time to evaluate and/or the most CPU time. After making changes, perform the time test again to verify the improvement. The goal is to reduce the “Elapsed wall clock time” as low as possible while keeping as many of the desired reminders for the cutover document.

*(Continued from bottom of Column 1)*

Take note of your final “Elapsed wall clock time.” This time will be used to help estimate the total amount of time for the Clinical Reminders Cutover document.

> Example output below from the last sections of the CPRS Coversheet Time Test:

> Total number of reminders evaluated: 59

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p><strong>Elapsed wall clock time: 173 seconds</strong></p>
<p><strong>Total CPU coversheet evaluation time: 9995 milliseconds</strong></p>
<p><strong>Longest CPU evaluation time</strong></p>
<p><strong>Reminder: VA-CRC AVERAGE RISK (IEN=306)</strong></p>
<p><strong>Reminder CPU evaluation time: 2064 milliseconds</strong></p>
<p><strong>Longest wall clock evaluation time</strong></p>
<p><strong>Reminder: VA-CRC AVERAGE RISK (IEN=306)</strong></p>
<p><strong>Reminder wall clock evaluation time: 37 seconds</strong></p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Note: There are some national and local reminders that will take an extremely long time to evaluate. Any reminder with a “Reminder wall clock time” greater than 1 second should be removed from the default reminders for the CPRS coversheet.

Step 1 - Run System Benchmark

1)  Select Option 1 from the VistA Cutover Utilities menu. The benchmark will find patients to use for the benchmark testing. The test will take approximately five minutes to complete. Results of each test will display when finished and the benchmark will automatically set the optimum number of threads for the Test and Create options.

> Benchmark Tool :37:39

> \# of Patients Total Avg Max Est. Time to

> Test Threads Processed Time Thread Pt/Sec Completion

> 1 1 2286 31 30.00 76.20 15 min 34 sec

> 2 5 6931 33 30.00 231.03 5 min 08 sec

> 3 10 9848 33 28.00 351.71 3 min 22 sec

> 4 15 10000 30 24.20 413.22 2 min 52 sec

> 5 20 10000 26 22.15 451.47 2 min 38 sec

> 6 25 10000 23 20.08 498.01 2 min 23 sec

> 7 30 10000 22 18.90 529.10 2 min 15 sec

> 8 35 10000 23 19.43 514.67 2 min 18 sec

> 9 40 10000 24 20.40 490.20 2 min 25 sec

> \< Benchmark Testing Complete \>

> Press \<ENTER\> to continue

> Note: The estimated time to completion may vary significantly based on the difference in clinical data from the initial patients used for the benchmark versus the remaining patients and the amount of data needed to process. The number of threads to use is chosen based on your system’s current performance.

Step 2 - Run the Test Data Retrieval

1)  Select Option 2 from the VistA Cutover Utilities menu.  
    When asked, “Do you wish to select a single patient?”  
    enter NO and press \<Enter\>
2)  When asked, “Do you wish to test the Clinical Reminders cutover documents?”  
    accept the default entry of NO and press \<Enter\>
3)  When asked, “Continue for all patients?”  
    enter YES and press \<Enter\>.  
    A screen showing the progress of patient evaluation will display. Once all patients have been evaluated, the test process will begin. It is possible for the number of patients evaluated to be higher or lower than the number of total patients. The total patients are reported by FileMan and the evaluated patients are an actual count of the patient file.

Example output from the patient evaluation phase:

> Evaluating patients...110927 of 110927

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>65804 patients will be tested for the EHRM Cutover.</p>
<p>Press &lt;ENTER&gt; to continue</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

> Note: The number of patients that meet the criteria that will be tested should match exactly in the summary email received by the user at the completion of the test.

> Tip: Multiply the “Elapsed wall clock time” by the number of patients that will be tested to find the minimum amount of time in seconds to complete the clinical reminders test or document creation.

> *(Continued from bottom of Column 1)*

> Step 3 – Run the Create VistA Cutover Document(s)

1)  Select option 3 from the VistA Cutover Utilities menu.
2)  Please see your site’s schedule for cutover tasks before initiating either the summary or reminders document in Production.
3)  Once the job has finished, the user will receive a summary email message.

> Note: Wait for the summary document creation to complete before beginning the reminders document creation.

> Run the Monitor/Stop Cutover Jobs (Optional)Option 4 from the Vista Cutover Utilities menu allows the user to take actions while the cutover process is running, if necessary. There are 3 available actions: UPDATE (default), STOP, or QUIT.

- Pressing \<Enter\> will UPDATE the progress of the job(s), allowing the user to track progress real time. It is normal for the active threads to decrease as they finish but before the overall progress is 100%.
- Entering STOP will prompt the user for the job \# they wish to ask TaskMan to stop running. It can take several minutes for all of the running threads to cease activity. Once they have all stopped, the summary email will still be sent to the initiating user with partial results \[Stopped by Task Manager\] and will be included in the body of the message.
- Once both the summary and clinical reminders processes have finished in TEST mode, the total amount of time for each will be approximately 5-10% longer during the document creation process.

> Example output from the monitoring tool: