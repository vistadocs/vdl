---
title: FM 22.2 Release Notes
doc_type: RN
doc_label: Release Notes
doc_layer: anchor
doc_subject: 
app_code: DI
app_name: FileMan
section: INF
app_status: active
pkg_ns: DI
patch_ver: 22.2
patch_id: DI*22.2
group_key: "DI:DI:22.2"
file_numbers: []
security_keys: []
menu_options: 0
description: "<table> <caption>Template Revision History showing date template was created or revised, version number, description, and author.</caption> <colgroup> <col style=\\"width: 18%\\" /> <col style=\\"width: 10%\\" /> <col style=\\"width: 45%\\" /> <col style=\\"width: 25%\\" /> </colgroup> <thead> <tr class=\\"header\\"> <"
audience: 
keywords: 
  - table
  - contents
  - fileman
  - fields
  - changes
  - screenman
  - word
  - processing
  - dictionary
  - maximum
page_count: 0
word_count: 3504
section_count: 25
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: August 2016
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Fileman/fm22_2rn.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Fileman/fm22_2rn.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=5"
---

---
title: |
  VA FileMan 22.2

  Release Notes
---

![](fm-22-2-release-notes/001.png)

August 2016

Department of Veterans Affairs (VA)

Office of Information and Technology (OI&T)

Enterprise Program Management Office (EPMO)

Revision History

<table>
<caption>Template Revision History showing date template was created or revised, version number, description, and author.</caption>
<colgroup>
<col style="width: 18%" />
<col style="width: 10%" />
<col style="width: 45%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Version</th>
<th>Description</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>08/15/2016</td>
<td>1.1</td>
<td><p>Tech Edits:</p>
<ul>
<li><p>Removed author notes in Section <u>2.2.1</u>.</p></li>
<li><p>Updated Section <u>2.2.1.2</u>.</p></li>
</ul></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>08/07/2016</td>
<td>1.0</td>
<td>Initial release of VA FileMan 22.2 Release Notes.</td>
<td>VA FileMan 22.2 Development Team</td>
</tr>
</tbody>
</table>

Template Revision History showing date template was created or revised, version number, description, and author.

Table of Contents

# Principal Enhancements


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Principal Enhancements](#principal-enhancements)
  - [ScreenMan Enhancements](#screenman-enhancements)
    - [Use of Mouse in ScreenMan Forms](#use-of-mouse-in-screenman-forms)
    - [Record Selection as a Full ScreenMan Page](#record-selection-as-a-full-screenman-page)
    - [Expanded Multiples](#expanded-multiples)
    - [Custom Colors Option](#custom-colors-option)
    - [Quick Exit from Word Processing Pages](#quick-exit-from-word-processing-pages)
    - [Indication of Word-Processing Data](#indication-of-word-processing-data)
    - [Screen Print](#screen-print)
  - [Internationalization](#internationalization)
    - [VA FileMan is Translation-Ready](#va-fileman-is-translation-ready)
    - [New Entries in DIALOG File (#.84)](#new-entries-in-dialog-file-84)
    - [Many New Languages in File \#.85](#many-new-languages-in-file-85)
    - [New Dialog Framework for Data Dictionary Elements](#new-dialog-framework-for-data-dictionary-elements)
    - [New Entry Points to Help Translate DD Elements](#new-entry-points-to-help-translate-dd-elements)
    - [Consistent Date Formatting](#consistent-date-formatting)
    - [Date Internationalization Enhancement](#date-internationalization-enhancement)
    - [Upper/Lowercase Translations are Consistent](#upperlowercase-translations-are-consistent)
    - [Two- and Three-letter Language Abbreviations](#two-and-three-letter-language-abbreviations)
  - [Data Analysis Tools](#data-analysis-tools)
    - [Check all Pointers into a Given File](#check-all-pointers-into-a-given-file)
    - [Automatic Auditing](#automatic-auditing)
    - [Showing Past Changes to Data Dictionary](#showing-past-changes-to-data-dictionary)
    - [Showing Changes by a Specific User](#showing-changes-by-a-specific-user)
    - [Modified Auditing Menu](#modified-auditing-menu)
    - [Entry Access Audit](#entry-access-audit)
    - [Update The Meta Data Dictionary](#update-the-meta-data-dictionary)
    - [Improvements to the Verify Fields Utility](#improvements-to-the-verify-fields-utility)
    - [Comparing Data and Data Dictionaries across Environments](#comparing-data-and-data-dictionaries-across-environments)
  - [Ability to Edit Export Template](#ability-to-edit-export-template)
- [Other Enhancements](#other-enhancements)
  - [User Interface Changes](#user-interface-changes)
    - [Select Prompt: Extended Selection by IEN](#select-prompt-extended-selection-by-ien)
    - [Printing Multiples in Sorted Order](#printing-multiples-in-sorted-order)
    - [VA FileMan Browser Enhancements](#va-fileman-browser-enhancements)
  - [API Changes](#api-changes)
    - [Enhancements to FIND^DIC and LIST^DIC](#enhancements-to-finddic-and-listdic)
    - [New API to Create Sort Templates Silently](#new-api-to-create-sort-templates-silently)
  - [Data Dictionary Changes](#data-dictionary-changes)
    - [Auditable Word Processing Fields](#auditable-word-processing-fields)
    - [Word Processing Fields can be Made Uneditable](#word-processing-fields-can-be-made-uneditable)
    - [Set Explicit Maximum Length for Free-text Fields](#set-explicit-maximum-length-for-free-text-fields)
    - [Override of Character Limit in Globals](#override-of-character-limit-in-globals)
  - [Installation and Distribution Changes](#installation-and-distribution-changes)
    - [DIFROM: Keys and New-Style Indexes](#difrom-keys-and-new-style-indexes)
    - [DINIT: Virgin Install](#dinit-virgin-install)
- [Bug Fixes](#bug-fixes)
  - [Computed Expressions: Multiple Contains with Word-processing Fields](#computed-expressions-multiple-contains-with-word-processing-fields)
  - [Uppercasing](#uppercasing)
  - [DIFROM Maximum Routine Size](#difrom-maximum-routine-size)
  - [DIFROM Routine Size Calculation](#difrom-routine-size-calculation)
  - [Browser Display Routines Did Not Work on Caché](#browser-display-routines-did-not-work-on-caché)
  - [Maximum Routine Size](#maximum-routine-size)
  - [Browser Now Works without Kernel](#browser-now-works-without-kernel)
  - [Replace/With Maximum Length](#replacewith-maximum-length)
  - [Reverse Collation on Complex New Style Indexes When Doing Partial Matches](#reverse-collation-on-complex-new-style-indexes-when-doing-partial-matches)
  - [Q Flag on LIST^DIC and FIND^DIC and Partial Numeric Matches on Pointer Values](#q-flag-on-listdic-and-finddic-and-partial-numeric-matches-on-pointer-values)
  - [DDS3-1 New Options at Command Line](#dds3-1-new-options-at-command-line)
  - [DDS3-2 New Dialog on Existing Form](#dds3-2-new-dialog-on-existing-form)
  - [DDS3-3 New Capabilities from Record Selection Page](#dds3-3-new-capabilities-from-record-selection-page)
  - [DIB Warning-Data Global does Not Exist](#dib-warning-data-global-does-not-exist)
  - [DIKCUTL Non deleteable index](#dikcutl-non-deleteable-index)
  - [DIUTL NOW Returns Minutes](#diutl-now-returns-minutes)
- [Unit Tests](#unit-tests)

## ScreenMan Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Use of Mouse in ScreenMan Forms

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

ScreenMan does support the use of a mouse for emulators that support ANSI standard control sequences to turn the mouse on and off. However, the Department of Veterans Affairs has elected to turn this feature off due to support complications with Attachmate Reflection. The parameter DI SCREENMAN NO MOUSE needs to be established for SYSTEM and set to “Yes”. The DI SCREENMAN NO MOUSE parameter will be set to “YES” during the VA FileMan (FM) 22.2 installation.

### Record Selection as a Full ScreenMan Page

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ScreenMan Record Selection page can now be a full ScreenMan page using a computed multiple pointer, so that the user can select an entry by scrolling up or down. This new feature lets forms contain embedded lookups.

You can set this up automatically when you create a form. At the query “Do you want your Form to begin with a display of all entries, for selection,” answer “Yes.” The initial position can be set to be the user’s last selection, rather than first, last, or new.

### Expanded Multiples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Multiples within a single ScreenMan page can now be more than one line deep.

### Custom Colors Option

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The “Customize Colors” sub option within ScreenMan allows selection of ANSI colors for all ScreenMan presentations, on a parameterized basis (user, institution, etc.) using Kernel parameters.

### Quick Exit from Word Processing Pages

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

While Editing/Adding a ScreenMan word processing document, the user can enter two carriage returns (press Enter twice) at the end of the document to exit ScreenMan. This is new functionality, the user is no longer required to use \<PF1\>E to exit ScreenMan.

### Indication of Word-Processing Data

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A + now indicates, in a ScreenMan form, whether a word-processing field already contains data. If users have their PREFERRED EDITOR field set to “SCREEN EDITOR – VA FILEMAN”, the previous message “No existing Text” has been modified to “THERE ARE NO LINES!” if a word-processing field has no data.

### Screen Print

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\<PF1\>P allows printing of the screen (including all multiples).

## Internationalization

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### VA FileMan is Translation-Ready

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VA FileMan is in the process of converting all *non*-developer dialogues to use FM dialogues framework, so that translations can be table-driven.

### New Entries in DIALOG File (#.84)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Many new entries have been added to the DIALOG file (#.84) to handle end-user interactions.

### Many New Languages in File \#.85

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The LANGUAGE file (#.85) now includes entries for all ISO 639-2:1998 languages, as of the 11/21/2012 update to the standard.

### New Dialog Framework for Data Dictionary Elements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

File names, field labels, set values, and help messages can be entered into the ^DD schema for any of the living languages listed in the LANGUAGE file (#.85).

### New Entry Points to Help Translate DD Elements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new direct mode tool has been created to help translate the file name, field names, and help prompts. The call is DO LANG^DIALOGZ().

### Consistent Date Formatting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Formatting of date output is now consistently done throughout all the end-user routines. Changing the global node ^DD(“DD”) changes the way all VA FileMan dates are output. Re­running ^DINIT does not change this node.

### Date Internationalization Enhancement

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Date Internationalization has been enhanced so that when the international format is specified using the "I" flag, the returned display output is in the form DD MON YYYY instead of MON, DD YYYY.

### Upper/Lowercase Translations are Consistent

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VA FileMan’s internationalization framework has been made consistently independent of the ASCII character set, to improve support for international case conversion.

### Two- and Three-letter Language Abbreviations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The LANGUAGE file (#.85) now can store two and three letter abbreviations for languages.

## Data Analysis Tools

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Check all Pointers into a Given File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A fourth Data Dictionary utility (“find pointers into a file”) checks all files with pointers into a given File. The utility gives four kinds of output (here using PATIENT file \[#2\] as an example):

### Automatic Auditing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To improve version control for data dictionaries, DD changes are always audited in the DD AUDIT file (#.6). There is no need to turn on DD auditing file­by­file.

### Showing Past Changes to Data Dictionary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The “Show Past Changes to DDs” auditing option shows most DD changes since a certain date.

![](fm-22-2-release-notes/002.png) NOTE: This will be added in a future release and a ticket has been created in the VA SDM system. Service Desk Ticket has been opened to fix this issue as a VA FileMan Maintenance issue. Ticket number I7740738FY16 created on 2/26/16.

### Showing Changes by a Specific User

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

“Monitor a User” is now the second auditing option. It shows every entry in an audited file touched by a given user in an audited file.

### Modified Auditing Menu

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The auditing menu has been modified to be better organized and more intuitive.

### Entry Access Audit

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The ACCESSED^DIET function has been modified to replace a call that killed the variable DIC.

### Update The Meta Data Dictionary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Use the Update The Meta Data Dictionary option on the Data Dictionary Utilities menu to create the new META DATA DICTIONARY file (#.9). The Meta Data Dictionary lists all fields in all files in a searchable format.

### Improvements to the Verify Fields Utility

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A number of improvements have been made to the Verify Fields Utility.

#### Checks for Duplicates and Dangling Pointers

Verify Fields checks for duplicates and dangling pointers in cross-references. There is no new Verify Data menu and no new Verify Pointers option. The verify pointers functionality is invoked by the Verify Fields option on the Utilities menu.

#### Checks Index Values Do Not Exceed Thirty-Character Limit

Verify Fields checks that the index values do not exceed the thirty-character limit.

#### Output Displays Translated Field Label

If a user's language is set to a *non*-English language, and if a translation of a field label exists for that language, then Verify Fields output displays the translated field label.

#### Suppresses Accidental Echo of dates

A bug was fixed to suppress the accidental echo of dates in the Verify Fields output.

### Comparing Data and Data Dictionaries across Environments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

A new Transfer menu option, Namespace Compare, lets you identify differences in data and DDs between different MUMPS environments (on the same server), to help with version control.

## Ability to Edit Export Template

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

In prior versions of VA FileMan, if a user created an Export Template they were unable to edit that template like they could with a Sort, Print, and Edit Templates; with VA FileMan 22.2, the user is now able to edit an Export Template.

# Other Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## User Interface Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Select Prompt: Extended Selection by IEN

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Lookup enhancement: if the .01 field of the file being selected from is a pointer to another file, you can use a double accent grave (\`\`) to pick a pointed­to entry by its internal entry number (IEN).

### Printing Multiples in Sorted Order

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Until now, when printing sorted records, any subentries within those records were displayed unsorted, in order by internal entry number. A new B print specifier will ensure that subentries are displayed in order.

### VA FileMan Browser Enhancements

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can now print the text being browsed using PF1­PF1­P.

## API Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Enhancements to FIND^DIC and LIST^DIC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Third Argument (Fields)

Third argument (fields) can now be a computed expression, not just a field.

#### New E Flag Returns the Complete List of Matches

Fourth argument (flags) can now contain E, and it will return the complete list of matches even if errors are encountered during the generation of the results.

#### Eighth Parameter (Index) of LISTˆDIC

Eighth parameter (index) of LISTˆDIC can now be a sort template, a field, or a computed expression, if the new X flag is included.

### New API to Create Sort Templates Silently

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The BUILDNEW^DIBTED API silently creates a sort template.

## Data Dictionary Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Auditable Word Processing Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VA FileMan security has been improved by allowing word-processing fields to be audited.

### Word Processing Fields can be Made Uneditable

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference files and clinically significant text can now be protected from subsequent change.

### Set Explicit Maximum Length for Free-text Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Maximum Length of output for a Free Text field can now be set; it is not dependent on the input Transform. The Maximum Length value truncates the stored data during output if necessary. The Maximum Length can be set in the input Transform (Syntax) option on the VA FileMan's Utility Options sub-menu.

### Override of Character Limit in Globals

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

^DD(“STRING_LIMIT”), if set, overrides the standard 255-character limit throughout VA FileMan.

![](fm-22-2-release-notes/003.png) NOTE: The Post Install sets the limit to 4094.

## Installation and Distribution Changes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### DIFROM: Keys and New-Style Indexes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DIFROM has been extended to be able to transport keys and New Style indexes.

![](fm-22-2-release-notes/004.png) NOTE: This is specific to standalone VA FileMan (FM). The Department of Veterans Affairs does not use FM in this capacity.

### DINIT: Virgin Install

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VA FileMan has been changed to restore its ability to run correctly without any of the rest of Veterans Health Information Systems and Technology Architecture (VistA) being installed.

![](fm-22-2-release-notes/005.png) NOTE: This is specific to standalone VA FileMan. The Department of Veterans Affairs does not use FM in this capacity. A virgin install of FM 22.2 does not include the META DATA DICTIONARY file (#.9) and will not include all the languages in the LANGUAGE file (#.85).

# Bug Fixes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Computed Expressions: Multiple Contains with Word-processing Fields

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Computed Expressions with Multiple Contains, such as (WP1\["GREEN")!(WP2\["GREEN"), are now handled correctly for Word-processing Fields.

## Uppercasing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VA FileMan uppercasing code in DILIBF is now User Language aware. Previously, it worked for English only.

## DIFROM Maximum Routine Size

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DIFROM did not use ^DD(“ROU”) to determine the maximum routine size, but rather had it hard­coded to 9999.

## DIFROM Routine Size Calculation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DIFROM did not correctly count the size of routines it created making routines larger than the maximum size.

## Browser Display Routines Did Not Work on Caché

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

DR^DDBRU did not work on Caché due to the way %RSEL works on Caché.

## Maximum Routine Size

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Maximum routine size did not get set with the first installation of VA FileMan. The node ^DD(“ROU”) does not get initialized when installing VA FileMan for the first time.

## Browser Now Works without Kernel

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VA FileMan Browser now works without the DEVICE file (#3.5) and can be invoked from VA FileMan directly.

![](fm-22-2-release-notes/006.png) NOTE: This is specific to standalone VA FileMan. The Department of Veterans Affairs does not use FM in this capacity.

## Replace/With Maximum Length

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The replace prompt only supported input up to 245 characters long. Now, it supports any length such that the sum of the replace length, overhead of the field and existing characters do not exceed ˆDD("STRING_LIMIT").

## Reverse Collation on Complex New Style Indexes When Doing Partial Matches

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Previously, a compound New Style index configured to sort in reverse order still sorted in forward order upon partial matches even when it sorted in reverse when listing entries using “??”. Now, it correctly sorts in reverse order when displaying partial matches.

## Q Flag on LIST^DIC and FIND^DIC and Partial Numeric Matches on Pointer Values

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Previously, using Q flag on DBS DIC calls caused numeric matches on pointer fields to be partially matched a la text matches. Now, partial numeric matches are not allowed in these circumstances.

## DDS3-1 New Options at Command Line 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Two new items are available for selection at the “COMMAND:” prompt at the bottom of a ScreenMan screen: Quit and Previous Page. These commands are the equivalent of the previously available \<PF1\>Q and \<PF1\>\<ArrowUp\>.

## DDS3-2 New Dialog on Existing Form

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When entering EXIT at the Command Line after editing data, the form is exited and changes saved without asking a verifying question; question has been removed. Now \<PF1\>-E and EXIT at Command Line work the same way.

## DDS3-3 New Capabilities from Record Selection Page

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

You can Exit or Save data from the Record Selection page.

## DIB Warning-Data Global does Not Exist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

When ENTERING or EDITing a file, the user is notified by message “DATA GLOBAL DOES NOT EXIST” if the file header does not exist rather than just returning to the menu.

## DIKCUTL Non deleteable index

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Programmers may set the 666 node to “null” to protect a New Style index from being deleted. For example, programmers can issue the following command:

S ^DD("IX",321,666)=""

Where 321 is the assigned index number that needs to be protected from being deleted.

## DIUTL NOW Returns Minutes

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The \$\$NOWˆDIUTL function now returns the date and the minutes in the format as defined in ˆDD(“DD”).

# Unit Tests

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

VA FileMan 22.2 comes with Unit Tests for classical date/time calls and new features of the DBS LISTER and FINDER. All unit tests are under the namespace DMU.

Per SRP 3.5, DMU is not planned to be released part of VA FileMan 22.2.