---
title: XU*8*207 KDC Readme
doc_type: RN
doc_label: Release Notes
doc_layer: patch
doc_subject: KDC Readme
app_code: XU
app_name: Kernel Delphi Components (KDC)
section: INF
app_status: active
pkg_ns: XU
patch_ver: 8
patch_id: XU*8*207
group_key: "XU:XU:8"
file_numbers: []
security_keys: []
menu_options: 0
description: "\ Kernel Delphi Components (KDC) V. 1.0 Readme: Patch XU\8.0\*207 initial release"
audience: 
keywords: 
  - delphi
  - components
  - kernel
  - component
  - provides
  - installation
  - help
  - date
  - alerts
  - readme
page_count: 0
word_count: 474
section_count: 0
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: April 2002
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel_Delphi_Components/kdc1_0rm.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel_Delphi_Components/kdc1_0rm.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=127"
---

Readme File

Last Updated: 04/26/2002

==========================================

Package: Kernel Delphi Components (KDC)

Current Version: 1.0

Original Release Date: April 2002

Dept. of Veterans Affairs

VHA OI System Design & Development (SD&D)

==========================================

This file contains any last minute changes, new instructions (not found in

the documentation),and additional information to supplement the manuals.

TABLE OF CONTENTS

-----------------

\* Kernel Delphi Components (KDC) V. 1.0 Readme: Patch XU\*8.0\*207 initial release

1: General Comments

2: Installation Notes

-------------------------------------------------------------------------------

Kernel Delphi Components (KDC) V. 1.0 Readme: Patch XU\*8.0\*207 initial release

-------------------------------------------------------------------------------

General Comments:

----------------

Patch XU\*8.0\*207 provides the following new Kernel Delphi Components:

\* XUAlert -- This is a non-visual component that provides an

object and a wide range of capabilities with respect to

alert processing. It provides a mechanism by which an alert

can be set up to run either by a GUI application or via

Roll-and-Scroll.

\* XUAlertSurrogate -- This is a non-visual component that provides an AlertSurrogate

object and abilities to set or clear it for a user.

\* XUAlertButton -- This button provides the ability to view and, as far as

possible, to process alerts. Users who hold the XQAL DELETE

security key (e.g., ADPACs) have additional capabilities

(e.g., forwarding alerts, deleting alerts for other users,

and creation of alerts).

\* XUDateTimeSelect -- This component provides a component for obtaining a date and

time, which can be entered in a number of different ways

(or, if the AllowDateRange property is set, a beginning

date and ending date).

\* XUMonthCalendar -- This component provides a calendar for display.

\* XU_NameRules -- This component should be placed on an application form as the

first component; all subsequent components will then be renamed

with a prefix according to the pending GUI SAC guidelines.

\* XUViewPropButton -- At run-time, this button can be used to explore the components

associated with the application's forms and the current values

of properties for those components.

For more information on the functionality and use of these Kernel Delphi Components (KDC),

please refer to the Help file that is included with this version (i.e., KDC.HLP).

Installation Notes:

------------------

Follow the installation instructions as written in the Installation Guide (i.e., KDC1_0IG.DOC).

The installation executable file for the Kernel Delphi Components (i.e., KDC1_0PG.EXE) will

automatically set up a directory structure similar to the following:

VISTA

\|

\|

Kernel

\|

\|

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\| \| \| \| \| \|

\| \| \| \| \| \|

D4 D5 D6 Help Samples Source

\|

\|

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\|\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

\| \| \| \| \|

\| \| \| \| \|

Calendar Demo Demo412 DemoSrvr IXUAlertHandler XUAlertBtnTest

This installation also automatically installs the Kernel Delphi Components (KDC) into Delphi

and integrates the KDC online help with Delphi's help. After dropping a component onto a form,

give it focus, and press the F1 key to open the Kernel Delphi Components' help file

(i.e., BROKER.HLP).

In the following \$(DELPHI) is used to represent the base Delphi directory for a specified

version (e.g., this might translate to C:\Program Files\Borland\Delphi4).

For Delphi V. 4 -- The .bpl files are placed in the \$(DELPHI)\Bin directory