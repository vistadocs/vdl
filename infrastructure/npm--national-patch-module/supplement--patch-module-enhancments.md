---
title: NPM Patch Module Enhancments
doc_type: SUP
doc_label: Supplement
doc_layer: plain
doc_subject: 
app_code: NPM
app_name: National Patch Module
section: INF
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 0
description: > Patch summary option—These changes are fairly easy in the template. The pre-view window is the most involved.
audience: 
keywords: 
  - enhancements
  - changes
  - patch
  - moduleoutputs
  - operation
  - outstanding
  - problems
page_count: 0
word_count: 11
section_count: 0
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: True
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/National_Patch_Module_(NPM)/patch_module_enhancements.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/National_Patch_Module_(NPM)/patch_module_enhancements.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=20"
---

List of Enhancements/Changes for the Patch ModuleOutputs

> Patch summary option—These changes are fairly easy in the template. The pre-view window is the most involved.

> With or without routines—Some people don't want the routines to clutter up the display.

> It would be nice if routines could be displayed more horizontally in collating sequence.

> With or without a pre-view window.

> Currently the default is print by SEQ#(low to high), I always change to reverse SEQ\|# (high to low) I would think the default should be reverse.

> Display Under-development Patch for developers—this is an easy screen on the display option.

> Add patch description, or at least the pre-view window to the release bulletin. Some people just want to see a little about the patch and don't want to bother to look at it in the patch module.

> Add entered in error description for entered in error bulletin. It would be also good if the entered in error bulletin was KIDS installable so that the patch sequence could be maintained obvious at the sites.

> Remove Checksum and notes for routines from Patch message, and output. Just list routines.

> Print all patches for package by SEQ# in addition to the present category, priority, whatever.

> This is a little tricky since the SEQ# is not cross-referenced.

Operation

> Patch, bulletin distribution. Use mail groups instead of lists of support, developers in File \#11007.

> When a Patch is added generate a bulletin that becomes the Tracking Message.

> The competition bulletin gets built too many times.

> Allow releaser to return patch to underdevelopment. I don't know if this is an issue any more.

> Send Completed bulletins to all "support and verification"

> When loading a KIDS message:

> Patch load routine multiple in collating sequence from KIDS input.

> Maybe load second line information in routine section. The problem is the before checksum is not available.

> The developer can edit subject and hold date leaving the status as completed. There's probably no reason why the description couldn't be edited also.

> A description-edited bulletin could be sent, but maybe not the whole message. Or if KIDS hasn't changed, just send the text again without KIDS.

> When a Patch is added there should be a formatted description set up.

> At one time I worked on implementing a Package customizable template Method where each Package could load their own instructions. I think KIDS has standardized the installation so much that this is not really useful.

> Description:

> Preview Window—For NOIS#:

> Brief problem description, resolution, etc. This would be displayable before the patch is released, like in Summary Option.

> Installation Instructions:

> This is just a canned text of the KIDS installation.

> Routine Summary:

> This is just the area where the routines are listed with checksums before/after and second line patch sequence

> Categories:

> Add a new one—"executable"

> Change "routine" to "routine change"

Outstanding problems.

> Print new patch report will allocate error when a person just signs up or has too many new patches.

> The date of the input message is not displaying correctly in the developers input queue. It shows up as 1790 etc. The date on a network message is different than a local message.

> The input queue is just the q-patch with screens for package\*version. It would be better to have a server process the q-patch entries and put them into package queues. This is a little complicated; at least have an option that goes through q-patch and deletes entries that are released or don't have correct subject. Patch tries to delete them but it misses multiple entries.

> The present method of screening by Namespace\*version should include \*patch number. People usually put it in anyway and input messages are always patch number specific.

> There are two places where routines are screened for previous patches. One is when the developer enters the routine in the multiple, Patch "shouts" if it finds previous patches. This also happens when a person is ready to release the patch.

> The current screen doesn't check for Package version number so it will warn about routines patched in previous versions.

> The Internal Comments field doesn't work. Releasers don't like to go into the option for releasing to look at it. I think this could be replaced by adding text to the Patch tracking bulletin. When a developer completes the patch, it would create the patch message and then prompt you to add comments to the bulletin. I think there's an API to do it.