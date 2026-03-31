---
title: Accounts Receivable Version 4.5 User Manual - Archive AR Records Menu
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: Archive AR Records Menu
app_code: PRCA
app_name: Accounts Receivable (AR)
section: FIN
app_status: active
pkg_ns: PRCA
patch_ver: 4.5
patch_id: PRCA*4.5
group_key: "PRCA:PRCA:4.5"
file_numbers: []
security_keys: []
menu_options: 0
description: ![](accounts-receivable-version-4-5-user-manual-archive-ar-records-menu/001.png)
audience: 
keywords: 
  - archive
  - records
  - bills
  - archived
  - temporary
  - contents
  - archival
  - table
  - marked
  - arpatient
page_count: 0
word_count: 1151
section_count: 7
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Accounts_Receivable_(AR)/3archive.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Accounts_Receivable_(AR)/3archive.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=29"
---

![](accounts-receivable-version-4-5-user-manual-archive-ar-records-menu/001.png)

# Archive AR Records Menu


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Archive AR Records Menu](#archive-ar-records-menu)
  - [Mark AR records for archival](#mark-ar-records-for-archival)
  - [detailed report of pending archive records](#detailed-report-of-pending-archive-records)
  - [UNMARK records marked for archival](#unmark-records-marked-for-archival)
  - [Build temporary archive file](#build-temporary-archive-file)
  - [remove AR records from Files](#remove-ar-records-from-files)
  - [purge temporary archive storage file](#purge-temporary-archive-storage-file)

## Mark AR records for archival

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option marks Accounts Receivable bills that have been selected to be archived onto other media, then purged from the site's system. To be selectable, the bill's date of last activity must occur within a specified time frame. The property that distinguishes that the bills have been marked is a status change to Pending Archive. See the Archive section in the Technical Manual for the archival procedure.

The initial prompts include a beginning and ending date which allows you to "filter out" the bills that should remain on your database. A stipulation on the ending date is that it's value cannot occur after the previous Fiscal Year of the current Fiscal Year. For example,

![](accounts-receivable-version-4-5-user-manual-archive-ar-records-menu/002.png)

This option is used to select all bills and their associated transactions that have had no activity for a long period of time, preparing them for archival. After selecting these bills, a mailman message/report will be generated containing a summary of the bills that have been selected for archival.

Have your IRM review this mail message to determine if your system contains enough disk space to support a temporary "swap" file that would hold the marked records. If there is not enough disk space, you will have to de-select some records until your disk contains enough space to support a swap file. If you have little room left on your disk (hence the reason to archive), it is recommended that you archive a few bills at a time. See the Unmark Records Marked For Archival option.

## detailed report of pending archive records

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option prints a detailed listing of all bills that have been marked for archive; i.e. bills with a status of Pending Archive. The report contains the bill numbers and their respective debtor, category, old status, balance, and date of last activity.

Supervisors should use this report to determine those veterans' bills that should not be archived and purged from the system. These include bills that may continue activity in the future. One example is Reimbursable Health Insurance bills which may be in litigation for long periods of time and could be recalled.

After determining particular bills that should not be archived (i.e. kept on the system) or there is not enough disk space, unmark appropriate bills to ensure they do not get archived or there is enough disk space to hold converted data. See the Unmark Records Marked For Archival option.

Status: PENDING ARCHIVE 11-NOV-93 9:35 AM PAGE 1

Old Bill Last Date

Bill No. Debtor Cat. Status Balance Activity

----------------------------------------------------------------------------

000-000000 ARpatient,one ARCHIVED 0.00 SEP 22,1994

000-K10011 ARpatient,two ARCHIVED 0.00 SEP 22,1994

000-K00023 ARpatient,three ARCHIVED 0.00 SEP 22,1994

000-K00024 ARpatient,four ARCHIVED 0.00 SEP 22,1994

000-K00025 ARpatient,five ARCHIVED 0.00 SEP 22,1994

000-K20001 ARpatient,six ARCHIVED 0.00 SEP 22,1994

000-K10018 ARpatient,seven ARCHIVED 0.00 SEP 22,1994

000-K10021 ARpatient,eight ARCHIVED 0.00 SEP 22,1994

000-K10025 ARpatient,nine ARCHIVED 0.00 SEP 22,1994

000-K00042 ARpatient,ten ARCHIVED 0.00 SEP 22,1994

000-K10035 ARpatient,eleven ARCHIVED 0.00 SEP 22,1994

11 Bills marked Pending Archive

## UNMARK records marked for archival

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option "de-selects" a particular bill that is pending archival. Valid bills to unmark include only bills that have already been marked for archival. See the Mark AR Records For Archival option.

After identifying bills to keep on your system, use this option to "unmark" them. This changes their status from Pending Archival to their previous status and ensures that they will not be archived then purged from the system.

## Build temporary archive file

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option converts the "marked" bills to a special format and stores them in a temporary file. The temporary file, File 430.8, acts as holding place for the records before the records are moved to separate medium. After you are certain that you have selected the appropriate bills to archive, review the report of all marked bills to ensure you would have enough disk space to store this data. See the Detailed Report Of Pending Archive Records option.

Choose this option to convert those selected bills to an archivable format. That data is then copied to the temporary file. When successfully completed, the software sends a message to the individual who initiated this option informing them of the number of converted records to File 430.8. Using a global save command, this temporary file can then be copied to other media such as disk, paper, tape, or CD-ROM.

This option will abort its process and display an error message if there is already data residing in the temporary file. To avoid this, delete the file's data after you've archived and removed the data from your system. See the Mark AR Records For Archival option and the Purge Temporary Archive Storage File option.

> **NOTE:** Neither this option, nor any other AR option, will actually archive data to a separate medium. This option only converts the data to a different format. IRM will be responsible for saving the temporary file to other media using a system utility such as global save or print.

## remove AR records from Files

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option searches for deleted records to be archived in File 430 and leave a stub record consisting of the archive date, bill number, and archive status. All corresponding transactions are deleted from File 433. After the job completes, File 430.8 is deleted. This means all profiles of archived bills will only display the bill number, status, and the archive date.

Use this option after you've copied the temporary file to the "archive" medium and you are certain that the archived data is no longer needed. Once this option processes, you will only be able to view the data on the medium to which it was archived. The software generates a mail message stating that the software has completed the procedure.

## purge temporary archive storage file

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This option clears the contents of the temporary archive file, 430.8. File 430.8 must be empty before new archivable data records can be converted and stored in it. See the Build Temporary Archive option.

Use this option when the archive job abnormally terminates or if you don't want to archive anything. This resets the file for future archives. For instance, suppose that you have built the temporary file, archived it, and have not yet removed the data records from the system. Then you determine you should start over, you must reset the temporary file by clearing its contents.