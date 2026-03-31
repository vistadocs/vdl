---
title: MailMan Version 8 Quick Reference Card
doc_type: QRG
doc_label: Quick Reference Guide
doc_layer: anchor
doc_subject: Quick Reference Card
app_code: XM
app_name: MailMan
section: INF
app_status: active
pkg_ns: XM
patch_ver: 8
patch_id: XM*8
group_key: "XM:XM:8"
file_numbers: []
security_keys: []
menu_options: 0
description: "(NOTE: This Quick Reference Guide was originally based on a document created by the OI National Training and Education Office)"
audience: 
keywords: 
  - strong
  - class
  - message
  - messages
  - even
  - basket
  - recipients
  - toggle
  - header
  - mail
page_count: 0
word_count: 2406
section_count: 0
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: August 2002
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Mailman/xm_8_0_quickrefcard.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Mailman/xm_8_0_quickrefcard.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=15"
---

![](mailman-version-8-quick-reference-card/001.png)

MAILMANQUICK REFERENCE GUIDE

August 2002

VistA Health Systems Design & Development (HSD&D)

Infrastructure and Security Services (ISS)

(NOTE: This Quick Reference Guide was originally based on a document created by the OI National Training and Education Office)

Introduction

The VistA MailMan software is designed to allow users to send and receive mail from individuals or groups electronically through communication lines, modems, and other networks. These electronic mail messages (i.e., e-mail) can range from personal letters to formal bulletins extracting data from VA FileMan.

After reading messages, recipients can select from a variety of message actions (e.g., replying, saving, deleting, forwarding, querying, copying, or printing messages). Replies generate new messages seen by all recipients, creating an ongoing dialog among the recipients. Authors of messages can easily revise or edit message text, add or remove recipients, and further control the attributes of a message before sending it to others.

MailMan also allows users to appoint surrogates to process and manage their mail. In addition, mail groups can be set up to provide members with a forum for group discussion where ideas and concepts related to the group can be shared. Users can also filter their mail and search for specific messages in their own mailbox or anywhere on the system. Users can "introduce" themselves, provide office information, and create a banner to be displayed when a message is sent to them. Users can also choose a message reader and further customize the MailMan interface to suit their needs.

The main MailMan Menu consists of the following options:

> NML New Messages and Responses

> RML Read/Manage Messages

> SML Send a Message

> Query/Search for Messages

> Become a Surrogate (SHARED,MAIL or Other)

> Personal Preferences ...

> Other MailMan Functions ...

> Help (User/Group Info., etc.) ...

The purpose of this guide is to acquaint you with the basic features and functionality available with MailMan:

- Reading and Replying to Messages.
- Sending New Messages.
- Searching for Messages.
- Filtering Messages.

| ![](mailman-version-8-quick-reference-card/002.png) | REF: For more detailed information on these topics, please refer to the *MailMan Getting Started Guide* and the *MailMan User Manual*. |
|----------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|

Orientation and Helpful Hints

- Throughout this guide, user responses appear in boldface type (e.g., Enter an SSN to search for: 000123456 indicates that the user has entered 000123456 at the "Enter an SSN to search for:" prompt.)
- All of your responses *must* be followed by pressing the Enter key, which is represented by the symbol \<Enter\>.
- References to prompts are enclosed in quotation marks.
- You can activate online help by entering single, double, or triple question marks, according to the level of help you are seeking at most prompts.

  
Reading and Managing Mail

*Accessible from the Main MailMan Menu.*Prompts

Basket Action Prompt:

> Enter message number or command:

Basket Actions—Full Screen Readers

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Action<br />
Code</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>n</strong></td>
<td>Read message "n," where "n" is a sequence number in this basket or an internal message ID of any message on the system.</td>
</tr>
<tr class="even">
<td><p><strong>.n</strong></p>
<p><strong>.n-m,a,c-d</strong></p>
<p><strong>.*</strong></p></td>
<td>Select one, many, or all messages in a list for subsequent group action (message number is preceded by a decimal point).</td>
</tr>
<tr class="odd">
<td><p><strong>.-n</strong></p>
<p><strong>.-n-m,a,c-d</strong></p>
<p><strong>.-*</strong></p></td>
<td>Deselect one, many, or all messages in a list for subsequent group action (message number is preceded by a decimal point and then a hyphen).</td>
</tr>
<tr class="even">
<td><strong>C</strong></td>
<td>Change this mail basket's name (except for the "IN" and "WASTE" baskets).</td>
</tr>
<tr class="odd">
<td><strong>CD</strong></td>
<td>Display a summary or detailed list of messages (Toggle).</td>
</tr>
<tr class="even">
<td><strong>D</strong></td>
<td>Delete messages from this basket.</td>
</tr>
<tr class="odd">
<td><strong>F</strong></td>
<td>Forward messages from this basket.</td>
</tr>
<tr class="even">
<td><strong>FI</strong></td>
<td>Filter messages in this basket.</td>
</tr>
<tr class="odd">
<td><strong>H</strong></td>
<td>Print messages without a header.</td>
</tr>
<tr class="even">
<td><strong>L</strong></td>
<td>Make messages "new" at a later date and time.</td>
</tr>
<tr class="odd">
<td><strong>N</strong></td>
<td>List all new messages in this basket.</td>
</tr>
<tr class="even">
<td><strong>NT</strong></td>
<td>Make messages "new" or "not new" (Toggle)</td>
</tr>
<tr class="odd">
<td><strong>O</strong></td>
<td>Select or Deselect messages that were previously grouped (Toggle).</td>
</tr>
<tr class="even">
<td><strong>P</strong></td>
<td>Print messages with a header.</td>
</tr>
<tr class="odd">
<td><strong>Q</strong></td>
<td>Query (Search for) messages in this basket.</td>
</tr>
<tr class="even">
<td><strong>R</strong></td>
<td>Resequence the order of messages in this basket (remove the "gaps").</td>
</tr>
<tr class="odd">
<td><strong>S</strong></td>
<td>Save messages to another basket.</td>
</tr>
<tr class="even">
<td><strong>T</strong></td>
<td>Terminate messages from this basket.</td>
</tr>
<tr class="odd">
<td><strong>X</strong></td>
<td>Toggle the transmit priority in remote message queues (POSTMASTER only, Toggle).</td>
</tr>
<tr class="even">
<td><strong>Z</strong></td>
<td>Zoom In or Out on messages that were previously grouped (Toggle).</td>
</tr>
</tbody>
</table>

Prompts

Paging Action Prompts:

- First Page:

> Press ENTER or + to go to the next page. Enter +n to page forward n pages. Enter = to refresh this page; ^ to exit this list.

- Middle Page:

> Press ENTER or + to go to the next page. Enter +n to page forward n pages. Enter - to go to the previous page. Enter -n to page back n pages. Enter 0 to go to the first page; = to refresh this page; ^ to exit.

- Last Page:

> Press ENTER or ^ to exit this list. Enter - to go to the previous page. Enter -n to page back n pages. Enter 0 to go to the first page; = to refresh this page.

  
Paging Actions—Full Screen Readers

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Action<br />
Code</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>=</strong></td>
<td>Refresh the page.</td>
</tr>
<tr class="even">
<td><strong>+</strong></td>
<td>Advance to the next page (available when a list of messages spans more than one page).</td>
</tr>
<tr class="odd">
<td><strong>+n</strong></td>
<td>Page forward "n" number of pages (available when a list of messages spans more than one page).</td>
</tr>
<tr class="even">
<td><strong>-</strong></td>
<td>Return to the previous page (available when a list of messages spans more than one page).</td>
</tr>
<tr class="odd">
<td><strong>-n</strong></td>
<td>Page back "n" number of pages (available when a list of messages spans more than one page).</td>
</tr>
<tr class="even">
<td><strong>0</strong></td>
<td>Go to the first page (available when a list of messages spans more than one page).</td>
</tr>
<tr class="odd">
<td><strong>^</strong></td>
<td>Exit the list of messages in this basket.</td>
</tr>
</tbody>
</table>

Basket Actions—Classic Reader

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 77%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Action<br />
Code</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>?</strong></td>
<td>Display a summary list of messages.</td>
</tr>
<tr class="even">
<td><strong>??</strong></td>
<td>Display a detailed list of messages.</td>
</tr>
<tr class="odd">
<td><strong>?string</strong></td>
<td>Search for messages in this basket whose subject contains a certain keyword or phrase.</td>
</tr>
<tr class="even">
<td><strong>n</strong></td>
<td>Read message "n," where "n" is a sequence number in this basket or an internal message ID of any message on the system.</td>
</tr>
<tr class="odd">
<td><strong>C</strong></td>
<td>Change a mail basket's name (except for the "IN" and "WASTE" baskets).</td>
</tr>
<tr class="even">
<td><strong>D</strong></td>
<td>Delete messages from this basket.</td>
</tr>
<tr class="odd">
<td><strong>F</strong></td>
<td>Forward messages from this basket.</td>
</tr>
<tr class="even">
<td><strong>FI</strong></td>
<td>Filter messages in this basket.</td>
</tr>
<tr class="odd">
<td><strong>H</strong></td>
<td>Print messages without a header.</td>
</tr>
<tr class="even">
<td><strong>I</strong></td>
<td>Ignore this message and go to the next one in this basket.</td>
</tr>
<tr class="odd">
<td><strong>L</strong></td>
<td>Make messages "new" at a later date and time.</td>
</tr>
<tr class="even">
<td><strong>N</strong></td>
<td>List all new messages in this basket.</td>
</tr>
<tr class="odd">
<td><strong>P</strong></td>
<td>Print messages with a header.</td>
</tr>
<tr class="even">
<td><strong>Q</strong></td>
<td>Query (Search for) messages in this basket.</td>
</tr>
<tr class="odd">
<td><strong>R</strong></td>
<td>Resequence the order of messages in this basket (remove the "gaps").</td>
</tr>
<tr class="even">
<td><strong>S</strong></td>
<td>Save messages to another basket.</td>
</tr>
<tr class="odd">
<td><strong>T</strong></td>
<td>Terminate messages from this basket.</td>
</tr>
<tr class="even">
<td><strong>X</strong></td>
<td>Toggle the transmit priority in remote message queues (POSTMASTER only).</td>
</tr>
</tbody>
</table>

  
Message Actions (after reading a message)Prompts

Message Action Prompt:

> Enter message action (in IN basket): Ignore//

<table>
<colgroup>
<col style="width: 15%" />
<col style="width: 84%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Action<br />
Code</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>A</strong></td>
<td>Answer—Send a new message to the sender of the message.</td>
</tr>
<tr class="even">
<td><strong>B</strong></td>
<td><strong>B</strong>ack up to review the original message or a specific response.</td>
</tr>
<tr class="odd">
<td><strong>C</strong></td>
<td>Create a <strong>C</strong>opy of the message.</td>
</tr>
<tr class="even">
<td><strong>D</strong></td>
<td><strong>D</strong>elete the message.</td>
</tr>
<tr class="odd">
<td><strong>E</strong></td>
<td><strong>E</strong>dit a message you created but haven't sent to any other recipients other than yourself.</td>
</tr>
<tr class="even">
<td><strong>F</strong></td>
<td><strong>F</strong>orward the message to other recipients.</td>
</tr>
<tr class="odd">
<td><strong>H</strong></td>
<td>Print the message without a header (<strong>H</strong>eaderless).</td>
</tr>
<tr class="even">
<td><strong>I</strong></td>
<td><strong>I</strong>gnore the message, leave it in this basket.</td>
</tr>
<tr class="odd">
<td><strong>IN</strong></td>
<td>Make a message that you created <strong>IN</strong>formation Only (Toggle).</td>
</tr>
<tr class="even">
<td><strong>L</strong></td>
<td>Make a message "New" at a <strong>L</strong>ater date and time.</td>
</tr>
<tr class="odd">
<td><strong>N</strong></td>
<td>Toggle a message as "<strong>N</strong>ew" or "Not New."</td>
</tr>
<tr class="even">
<td><strong>P</strong></td>
<td><strong>P</strong>rint the message with a header.</td>
</tr>
<tr class="odd">
<td><strong>Q</strong></td>
<td><strong>Q</strong>uery the message to obtain general addressee information.</td>
</tr>
<tr class="even">
<td><strong>Q xxx</strong></td>
<td><strong>Q</strong>uery the message to obtain specific information on a particular recipient.</td>
</tr>
<tr class="odd">
<td><strong>QD</strong></td>
<td><strong>Q</strong>uery the message to obtain <strong>D</strong>etailed information on a all recipients.</td>
</tr>
<tr class="even">
<td><strong>QN</strong></td>
<td><strong>Q</strong>uery the message to obtain <strong>N</strong>etwork and detailed recipient information on a message.</td>
</tr>
<tr class="odd">
<td><strong>R</strong></td>
<td><strong>R</strong>eply to the message.</td>
</tr>
<tr class="even">
<td><strong>S</strong></td>
<td><strong>S</strong>ave the message to another basket.</td>
</tr>
<tr class="odd">
<td><strong>T</strong></td>
<td><strong>T</strong>erminate the message from this basket.</td>
</tr>
<tr class="even">
<td><strong>V</strong></td>
<td>Edit the <strong>V</strong>aporize Date so the message is deleted from your mailbox at a later date and time.</td>
</tr>
<tr class="odd">
<td><strong>W</strong></td>
<td><strong>W</strong>rite a new message while reading another message.</td>
</tr>
<tr class="even">
<td><strong>X</strong></td>
<td>E<strong>X</strong>tract KIDS or PackMan message (list of specific actions).</td>
</tr>
<tr class="odd">
<td><strong>^</strong></td>
<td>Exit the message.</td>
</tr>
</tbody>
</table>

Sending Mail

*Accessible from the Main MailMan Menu.*Prompts

> Select Message option: Transmit now//

  
Send Actions (before sending a message)

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 83%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Action<br />
Code</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>B</strong></td>
<td>Backup—Back up to review the message you're editing.</td>
</tr>
<tr class="even">
<td><strong>C</strong></td>
<td>Confidential (Toggle)—Only the designated recipient and not their surrogates can read it.</td>
</tr>
<tr class="odd">
<td><strong>D</strong></td>
<td>Delivery Basket Set—Specify the delivery basket for all recipients (dependent on each recipient's basket privileges).</td>
</tr>
<tr class="even">
<td><strong>ER</strong></td>
<td>Edit Recipients—Add or remove recipients.</td>
</tr>
<tr class="odd">
<td><strong>ES</strong></td>
<td>Edit Subject—Edit the subject text.</td>
</tr>
<tr class="even">
<td><strong>ET</strong></td>
<td>Edit Text—Edit the message text.</td>
</tr>
<tr class="odd">
<td><strong>I</strong></td>
<td>Information Only (Toggle)—Don't allow recipients to reply to it.</td>
</tr>
<tr class="even">
<td><strong>L</strong></td>
<td>Transmit Later—Send it to all recipients at a specified date and time.</td>
</tr>
<tr class="odd">
<td><strong>P</strong></td>
<td>Priority Delivery (Toggle)—Send it priority.</td>
</tr>
<tr class="even">
<td><strong>R</strong></td>
<td>Confirm Receipt (Toggle)—MailMan notifies you when a recipient has opened your message.</td>
</tr>
<tr class="odd">
<td><strong>S</strong></td>
<td>Scramble Text—Scramble the text when passing sensitive or private information (recipients must know the password to unscramble the text).</td>
</tr>
<tr class="even">
<td><strong>T</strong></td>
<td>Transmit Now—Send it now.</td>
</tr>
<tr class="odd">
<td><strong>V</strong></td>
<td>Vaporize Date Set—Automatically set it to be deleted from a recipient's mailbox at a specified date and time (recipients can modify or remove this date).</td>
</tr>
<tr class="even">
<td><strong>X</strong></td>
<td>Closed Message (Toggle)—Prevent recipients from forwarding it.</td>
</tr>
<tr class="odd">
<td><strong>^</strong></td>
<td>Cancel the message.</td>
</tr>
</tbody>
</table>