---
title: VistA Imaging DICOM Gateway Routing Setup and User Guide
doc_type: UG
doc_label: User Guide
doc_layer: plain
doc_subject: VistA Imaging DICOM Gateway Routing Setup and
app_code: MAG
app_name: VistA Imaging System
section: CLI
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 0
description: > This manual explains how to configure and use the routing capability of the VistA DICOM Gateway. This manual also explains how to use the on-demand routing capability of the VistARad diagnostic workstation software.
audience: 
keywords: 
  - routing
  - table
  - contents
  - blockquote
  - dicom
  - gateway
  - class
  - rules
  - destination
  - strong
page_count: 0
word_count: 9731
section_count: 39
table_count: 3
figure_count: 0
appendix_count: 2
has_toc: False
is_stub: False
pub_date: July 2010
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Vista_Imaging_Sys/mag_routing_user_guide.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Vista_Imaging_Sys/mag_routing_user_guide.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=105"
---

> ![](vista-imaging-dicom-gateway-routing-setup-and-user-guide/001.png)

VistA Imaging DICOM Gateway Routing Setup and User Guide

> July 2010 – Revision 6 MAG\*3.0\*53

> Department of Veterans Affairs Office of Enterprise Development Health Provider Systems

> Routing Setup and User Guide VistA Imaging 3.0 Patch 53

> July 2010

> Property of the US Government

> This is a controlled document. No changes to this document may be made without the express written consent of the VistA Imaging development office.

> While every effort has been made to assure the accuracy of the information provided, this document may include technical inaccuracies and/or typographical errors. Changes are periodically made to the information herein and incorporated into new editions of this document.

> Product names mentioned in this document may be trademarks or registered trademarks of their respective companies, and are hereby acknowledged.

> VistA Imaging Office of Enterprise Development Department of Veterans Affairs

> Internet: <span class="mark">REDACTED</span>

> VA intranet: <span class="mark">REDACTED</span>

# Contents 


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Contents](#contents)
- [Introduction](#introduction)
  - [Terms of Use](#terms-of-use)
  - [About this Manual](#about-this-manual)
  - [Related Documents](#related-documents)
- [Routing Overview](#routing-overview)
  - [Routing Explained](#routing-explained)
  - [Routing Prerequisites](#routing-prerequisites)
  - [How Routing Works](#how-routing-works)
- [Defining Routing Rules](#defining-routing-rules)
  - [Routing Rules Explained](#routing-rules-explained)
  - [Destinations in Rules](#destinations-in-rules)
  - [Conditions in Rules](#conditions-in-rules)
  - [Routing Rule Priority](#routing-rule-priority)
  - [Routing Images from Prior Exams](#routing-images-from-prior-exams)
  - [Routing Rules and Compression](#routing-rules-and-compression)
  - [Load Balancing](#load-balancing)
  - [Routing Rule Tips](#routing-rule-tips)
- [Configuring Routing](#configuring-routing)
  - [Defining Imaging Destinations](#defining-imaging-destinations)
  - [Defining DICOM Storage SCP Destinations](#defining-dicom-storage-scp-destinations)
  - [Defining “Route Priors” Logic](#defining-route-priors-logic)
  - [DICOM Gateway Configuration](#dicom-gateway-configuration)
  - [Importing Routing Rules (Route.dic)](#importing-routing-rules-routedic)
  - [VistARad Configuration—Sending Sites](#vistarad-configurationsending-sites)
  - [VistARad Configuration—Receiving Sites](#vistarad-configurationreceiving-sites)
  - [Changes Affecting Routing System Configuration](#changes-affecting-routing-system-configuration)
- [Using Routing](#using-routing)
  - [Activating Routing](#activating-routing)
  - [Maintaining Routing](#maintaining-routing)
  - [Disabling Routing](#disabling-routing)
  - [Routing Gateway Menu Options](#routing-gateway-menu-options)
  - [Additional Routing Options](#additional-routing-options)
- [Using VistARad in a Routing System](#using-vistarad-in-a-routing-system)
  - [Displaying Routed Exams](#displaying-routed-exams)
  - [VistARad and On-Demand Routing](#vistarad-and-on-demand-routing)
- [Troubleshooting Routing](#troubleshooting-routing)
  - [Troubleshooting FAQs](#troubleshooting-faqs)
  - [Routing Support](#routing-support)
- [Appendix A: Routing Worksheets](#appendix-a-routing-worksheets)
  - [Imaging Destination Worksheet](#imaging-destination-worksheet)
  - [DICOM Storage SCP Destination Worksheet](#dicom-storage-scp-destination-worksheet)
  - [Routing Rule Definition Worksheet](#routing-rule-definition-worksheet)
  - [Routing Setup Checklist](#routing-setup-checklist)
- [Appendix B: Using MAGDecompressor](#appendix-b-using-magdecompressor)
  - [Licensing](#licensing)
  - [Setup](#setup)
  - [Logging](#logging)
- [Glossary](#glossary)
- [Index](#index)
    - [A](#a)
    - [B](#b)
    - [C](#c)
    - [D](#d)
    - [E](#e)
    - [F](#f)
    - [H](#h)
    - [I](#i)
    - [J](#j)
    - [K](#k)
    - [L](#l)
    - [M](#m)
    - [R](#r)
    - [S](#s)
    - [U](#u)
    - [V](#v)
    - [W](#w)
Contents

# Introduction 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This manual explains how to configure and use the routing capability of the VistA DICOM Gateway. This manual also explains how to use the on-demand routing capability of the VistARad diagnostic workstation software.

> This manual is intended for the following users:

- Imaging/radiology department staff who are responsible for setting up and maintaining a Routing Gateway.
- Clinical staffers who need to use VistARad for on-demand routing.

> For technical staff, this manual assumes familiarity with the DICOM Gateways, the VistA system in general, and Windows networking. For clinical staff, this manual assumes familiarity with the Windows environment and the VistARad diagnostic workstation software.

## Terms of Use

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In compliance with Food and Drug Administration (FDA) and VA policies, authorization to use the software described in this document is contingent on the execution of a Site Agreement between the VistA Imaging development group and the site where this software is installed.

> Once a routing system is enabled at a site, an updated Site Agreement must be filed before the configuration of a routing system can be significantly altered. In addition to any restrictions noted in the Site Agreement, the following restrictions apply:

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>![](vista-imaging-dicom-gateway-routing-setup-and-user-guide/002.png)</p>
</blockquote></th>
<th>Caution: Federal law restricts this device to use by or on the order of either a licensed practitioner or persons lawfully engaged in the manufacture or distribution of the product.</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>![](vista-imaging-dicom-gateway-routing-setup-and-user-guide/003.png)</p>
</blockquote></td>
<td>No modifications may be made to this software without the express written consent of the VistA Imaging National Project Manager.</td>
</tr>
<tr class="even">
<td><blockquote>
<p>![](vista-imaging-dicom-gateway-routing-setup-and-user-guide/004.png)</p>
</blockquote></td>
<td><p>The Food and Drug Administration classifies this software as a medical device. Modifications to the computer where this software is installed, such as the installation of unapproved hardware or software, will adulterate the medical</p>
<p>device. The use of an adulterated medical device violates US Federal Law (21CFR820).</p></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>![](vista-imaging-dicom-gateway-routing-setup-and-user-guide/005.png)</p>
</blockquote></th>
<th><p>US Federal regulations and VA internal policy prohibit unencrypted</p>
<p>transmission of patient information outside the VA's intranet.</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## About this Manual

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Using this Manual

> This document contains material of interest to several different types of users, including the types described in the table below:

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 69%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>User</strong></th>
<th><blockquote>
<p><strong>Please read…</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>All users</td>
<td><blockquote>
<p>The <a href="#routing-overview"><u>Routing Overview</u></a> and the <a href="#glossary"><u>Glossary</u>.</a> The <a href="#index"><u>Index</u></a> can also be used to find information about specific topics in this document.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Clinical users</td>
<td><blockquote>
<p>The <a href="#using-vistarad-in-a-routing-system"><u>Using VistARad in a Routing System</u></a> chapter.</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Users responsible for DICOM Gateway operation and maintenance</td>
<td><blockquote>
<p>The <a href="#using-routing"><u>Using Routing</u></a> chapter. You may also find useful information in the <a href="#troubleshooting-routing"><u>Troubleshooting Routing</u></a> and <a href="#defining-routing-rules"><u>Defining</u></a> <a href="#defining-routing-rules"><u>Routing Rules</u></a> chapters.</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Users responsible for installing or configuring a routing system</td>
<td><p>The <a href="#defining-routing-rules"><u>Defining Routing Rules</u></a> and <a href="#configuring-routing"><u>Configuring Routing</u></a> chapters.</p>
<blockquote>
<p>Installation worksheets are available in <a href="#appendix-a-routing-worksheets"><u>Appendix A</u>.</a></p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Conventions

> This manual uses the following conventions:

- Windows menu options, buttons, and other controls found in a graphical user interface are indicated by bold. Menu sequences are indicated by vertical bars ( \| ).
- DICOM Gateway menu options are referred to by the menu sequence used to execute that option. For example, “Run option 4-2-2 (Update Gateway Configuration Parameters)” means:
  1.  In the main DICOM Gateway menu, enter 4 (System Maintenance).
  2.  In the System Maintenance menu, enter 2 (Gateway Configuration).
  3.  In the Gateway Configuration menu, enter 2 (Update Gateway Configuration Parameters).
- Examples are shown in the Courier typeface.
- ![](vista-imaging-dicom-gateway-routing-setup-and-user-guide/006.png)Useful or supplementary information is indicated by a Note, and critical information is indicated by .
- Keyboard keys are shown in bold and in brackets.
- Cross-references are underlined. If this document is being used online, cross-references are shown in blue and are active links.

> Revision Table

<table>
<colgroup>
<col style="width: 19%" />
<col style="width: 9%" />
<col style="width: 71%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Date</strong></th>
<th><strong>Rev.</strong></th>
<th><strong>Notes</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>15 Apr 2010</td>
<td>6</td>
<td><p>Minor updates for patch 53 in Other Properties section. P53 introduced the capability to use the value of 205,45 (Origin Index) in a routing rule. General corrections and clean-up.</p>
<p><mark>REDACTED</mark></p></td>
</tr>
<tr class="even">
<td>01 Oct 2009</td>
<td>5</td>
<td><p>Updates for patch 54 (“if” allowable in routing rules, change to study-based, rather than image-based evaluation logic). Expand conventions section. Expand and clarify content related to DICOM Storage SCPs. Rewrite “Routing Overview” chapter.</p>
<p>Clarify instructions in Appendix B. General corrections and clean-up. <mark>REDACTED</mark></p></td>
</tr>
<tr class="odd">
<td>03 Apr 2006</td>
<td>4</td>
<td>Minor updates for patch 18. Change bars in margins indicate updated content. <mark>REDACTED</mark> (formerly rev 1.3)</td>
</tr>
<tr class="even">
<td>30 Jul 2005</td>
<td>3</td>
<td>Updates for patches 11 and 51. Change bars in margins indicate updated content. <mark>REDACTED</mark> l (formerly rev 1.2)</td>
</tr>
<tr class="odd">
<td>22 Sep 2003</td>
<td>2</td>
<td>Minor p22 updates in VistARad chapter. Added info about routing rules and priority that was not included in original rev. Minor clarifications and corrections throughout. <mark>REDACTED</mark> (formerly rev 1.1)</td>
</tr>
<tr class="even">
<td>20 Mar 2003</td>
<td>1.0</td>
<td>Final version for p9 release. <mark>REDACTED</mark></td>
</tr>
<tr class="odd">
<td>25 Jun 2002</td>
<td>.9</td>
<td>Draft. Based on 23 Sep 1999 “Autorouting Tutorial.” Updated for Patch 9, test 2 distribution.</td>
</tr>
</tbody>
</table>

## Related Documents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following documents contain additional information about routing:

- Patch Descriptions for patches 9, 11, 51, and 54
- Routing Guidance Document

> The following documents contain additional information about components in the routing system:

- DICOM Gateway User Guide
- DICOM Gateway Installation Guide
- VistARad User Guide

> These documents are available at <span class="mark">REDACTED</span>

# Routing Overview 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This chapter explains how routing functions within the VistA Imaging system. It covers the following topics:

- [<u>Routing Explained</u>](#routing-explained)
- [<u>Routing Prerequisites</u>](#routing-prerequisites)
- [<u>How Routing Works</u>](#how-routing-works)

## Routing Explained

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In VistA Imaging, routing is the combination of methods and software used to identify and transmit exams produced at one site to a storage location at another site. Scenarios where routing can be used include the following:

- Workload sharing between institutions or service providers
- Rapid access to exams at remote clinics or other facilities
- Remote specialist interpretation or consultation
- Off-hours, holiday, or emergency services
- Off-site contract radiology services for primary interpretation

> Routing is a function of the DICOM Gateway software. When properly configured, any DICOM Gateway can function as a Routing Gateway. Typically, a Routing Gateway runs on a dedicated computer. However, at sites that produce only a small volume of images, a Routing Gateway can coexist on the same computer as an Image or Text Gateway.

> Routing takes two forms: automatic and on-demand.

- In automatic routing, newly acquired exams are sent to one or more destinations based on a pre-defined set of routing rules.
- In on-demand routing, manually selected exams are transmitted to one or more destinations using VistARad or DICOM Gateway option 2-8-2 (Select DICOM Images for Transmission).

> Images can be routed to two different types of destinations:

- Imaging destinations, which are typically used by VistARad users for remote reading.
- DICOM Storage SCP (Service Class Provider) destinations, which are typically non- VistA Imaging components, such as a film printer or an external PACS (Picture Archiving and Communication System).

## Routing Prerequisites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> For a site to be authorized to use a routing system, the following conditions must be met:

- An executed Site Agreement must be filed with the VistA Imaging HSD&D group, and an updated site agreement must be filed if the routing system is altered (for example: if site information changes, if a new destination is added, or if routing volume increases by 50% or more).
- A contingency plan must be implemented at all sites in the routing system and filed with the VistA Imaging HSD&D group. The contingency plan must contain procedures to be followed should the routing system be unavailable.

> General hardware and operational requirements for routing are summarized below. For detailed information, contact your VistA Imaging Implementation Manager.

#### Infrastructure Requirements

> Routing relies on the following infrastructure:

- If remote interpretation is being performed, you will need one or more VistARad diagnostic workstations and sufficient VistARad-accessible storage space for routed exams.
- If compression will be used for routed images, you will need to purchase Aware JPEG2000 toolkit licenses for each system that will be transmitting or receiving compressed images. For more information about compression, see Appendix B.
- An Image Gateway and a Routing Gateway must be configured as described in this document.
- Sufficient Wide Area Network (WAN) capacity must be available to handle the anticipated volume of routed exams.

#### Operational Requirements

> The medical and IT management at a site implementing the routing system will need to develop policies establishing the following elements:

- Locations to which the exams may and may not be routed
- Reporting/transcription requirements for routed exams
- Bandwidth utilization guidelines and priorities
- Storage space and storage monitoring of routed exams at receiving sites
- Management of patient confidentiality and privacy issues related to routed exams
- Methods for addressing performance issues and/or misuse of the routing system

## How Routing Works

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following figure illustrates the processes used to route images both automatically and on-demand. Numbered items correspond to automatic routing steps described in the section below. Items marked with letters correspond to on-demand routing steps described on the next page.

![](vista-imaging-dicom-gateway-routing-setup-and-user-guide/007.png)

#### Automatic Routing

1.  The evaluation queue is populated by one or more DICOM Image Gateways; for each new image processed by the gateway, a new entry is added to the evaluation queue.
2.  The evaluation processor checks each entry in the evaluation queue against

> pre-defined routing rules. (The evaluation queue is part of the IMAGE BACKGROUND QUEUE File (#2006.03). Entries used by other processes are also stored in this file.)

1.  If an entry in the queue matches a routing rule for an Imaging destination (such as a remote VistARad workstation), a new entry identifying the image and the destination is added to SEND QUEUE File (#2006.035).
2.  If an entry in the queue matches a routing rule for a Storage SCP destination (such as a film printer), a new entry identifying the image and the destination is added to the DICOM IMAGE OUTPUT File (#2006.574).
3.  Images are sent to their respective destinations.
    1.  The transmission processor for Imaging destinations (3-1) reads the SEND QUEUE

> File (#2006.035).

1.  If an entry in the file matches one of the destinations serviced by this processor, the image is sent to the appropriate Imaging destination using information in the NETWORK LOCATION File (#2005.2).
2.  The transmission processor for DICOM Storage SCP destinations (2-8-2) reads the DICOM IMAGE OUTPUT File (#2006.574).
    1.  If an entry in the file matches one of destinations serviced by this processor, the image is sent to the appropriate Storage SCP using information in the DICOM TRANSMIT DESTINATION File (#2006.587).

#### On-Demand Routing

> In on-demand routing, images to be routed are selected manually. Images can be selected using either of the following methods:

1.  Using the Route Request dialog in VistARad (security key required). Using this method, exams can be sent to both Imaging destinations and Storage SCP destinations. This method can also be used at a remote VistARad to “pull” images to itself.
2.  Using the Select DICOM Images for Transmission option (2-8-1) on the DICOM Image Gateway. Using this method, images can be sent only to Storage SCPs.

> Once images are selected for routing, transmission is handled using the same process as automatic routing.

#### Automatic Routing of Prior Exams

> Automatic routing offers the option to include images from prior exams. When this option is used in a routing rule, the routing software will use the VistARad prefetch logic defined at the acquisition site to create a list of prior exams.

> Images from the prior exams will be routed using the same priority as the newly acquired exam and, when appropriate, will be purged based on the same retention period as the newly acquired exam. For more details about automatically routing priors, see page [<u>20</u>.](#routing-images-from-prior-exams)

#### Priority and Routing

> For automatically routed exams, the routing software uses the priority assigned in a routing rule and the clinical urgency of the exam to calculate a numeric value. Images with the highest priority value are transmitted first.

<table>
<colgroup>
<col style="width: 24%" />
<col style="width: 21%" />
<col style="width: 54%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Factor</strong></th>
<th><strong>Values</strong></th>
<th><strong>Notes</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Assigned priority</td>
<td><p>Low: +250</p>
<p>Medium: +500</p>
<p>High: +750</p></td>
<td><p>Priority is set in routing rules as described on page <a href="#defining-routing-rules"><u>7</u>.</a></p>
<p>If not explicitly set in a rule, the assigned priority is assumed to be Medium.</p></td>
</tr>
<tr class="even">
<td>Clinical urgency</td>
<td><p>Routine: +0</p>
<p>Urgent: +10</p>
<p>STAT: +20</p></td>
<td>Values are based on the clinical urgency assigned to the exam in the Radiology Package.</td>
</tr>
</tbody>
</table>

> When an exam is routed on-demand, VistARad’s Route Request dialog can be used to assign a priority of Low, Medium or High. (The clinical urgency of the exam is not used.) If a user selects an exam to be routed on-demand that is already in the transmission queue, the higher priority of the two instances will be used.

> Regardless of how an exam is routed, the following factors apply for determining relative priority:

- If two or more exams have the same priority, their images are processed on a First In, First Out (FIFO) basis.
- Because exams are routed on an image-by-image basis, it is possible for the images in a lower-priority exam to be interrupted mid-stream by the images in a

> higher-priority exam. If this happens, transmission of all lower-priority images will resume after transmission of all higher-priority images is complete.

#### Remote Reading with VistARad

> A properly configured VistARad workstation can be used to display and interpret exams routed from another site. Radiologists performing remote reading can use VistARad to log into the site that sent the routed exams, and then use VistARad’s exam lists to locate exams that have been routed to them. For additional information about working with routed exams, refer to page [<u>59</u>.](#displaying-routed-exams)

#### Image Handling for DICOM Storage SCPs

> When an image is routed to a DICOM Storage SCP, the transmission processor (2-8-2) determines if a DICOM-format image is available to route. If there is no DICOM-format image available, a DICOM-format image is reconstructed using available Targa files,

> associated text files, and the latest demographic data from VistA. The resulting image is then sent to the Storage SCP. The reconstructed image is retained for future use.

> If a DICOM-format image is already available, the header data is checked to ensure that it includes the most recent demographic data from VistA. The image is then sent to the Storage SCP.

#### Management of Routed Images

> For Imaging destinations, the amount of time routed images are retained is based on the value of the RETENTION PERIOD field in the applicable entry in the NETWORK LOCATION File (#2005.2). The first time the destination is connected to on a given day, the transmission processor (3-1) deletes any images that have been stored longer than the retention period. The age of an image is based on the transmission queue entry for that image, not on the date of the image itself.

> In general terms, any DICOM Storage SCP can have exams routed to it either automatically or on-demand. Apart from transmission logs, images routed to a DICOM Storage SCP are not tracked by the Imaging system. Retention, management, and deletion of routed images is the responsibility of the Storage SCP.

# Defining Routing Rules 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This chapter covers the following topics:

- [<u>Routing Rules Explained</u>](#routing-rules-explained)
- [<u>Destinations in Rules</u>](#destinations-in-rules)
- [<u>Conditions</u>](#conditions-in-rules)
- [<u>Routing Rule Priority</u>](#routing-rule-priority)
- [<u>Routing Rules and Compression</u>](#routing-rules-and-compression)
- [<u>Load Balancing</u>](#load-balancing)
- [<u>Routing Rule Tips</u>](#routing-rule-tips)

> Note Routing rules can be defined before the configuration of the routing system is complete, but cannot be tested until the setup of the routing system is finished.

## Routing Rules Explained

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Routing Gateway uses routing rules to determine which images are to be automatically routed and where the images are to be sent. A rules definition worksheet is located in [Appendix A.](#appendix-a-routing-worksheets)

> The definition of routing rules involves:

1.  Determining the needs of the staff at the sending and receiving sites.
2.  Determining what resources will be used at the receiving site.
3.  Translating the resulting information into a rule that can be executed by the routing software.
4.  Implementing the rules by importing them to a Routing Gateway.

> Once they are implemented, routing rules should be reviewed periodically and adjusted to accommodate changes in workload, staffing, and so on.

#### How Routing Rules Work

> A routing rule must contain at least one destination and one condition. A basic routing rule looks like:

> send(“destination”) when \[condition A

> condition B...\]

> When the evaluation processor is running, each potentially routable exam is checked against all available rules. If the first image in an exam matches all the conditions in a given rule, all images in that exam will be routed to the destination specified in the rule.

> Note that in earlier versions of the software, each image was evaluated individually. This meant that for some exams, such as exams containing images from two modalities, multiple rules were needed.

> Typical Routing Rules

> A common routing scenario is the need to send images to a different site for interpretation.

> send is the most frequently used command in the “destination line” of a rule, but other commands are available as well. For details, see page [<u>10</u>.](#destinations-in-rules)

> when or if indicates the presence of one or more conditions. If a rule contains more than one condition, all of the conditions must be met for an image to be routed. (In all examples provided in this section, when is used.)

> Rule conditions are described in detail on page [<u>11</u>.](#conditions-in-rules)

> Note Do not use spaces immediately after the send command, or before or after operators (=, !=, etc.).

> Operators in Rules

> The most frequently used operator in a rule is =, which indicates that a specific image property must match a supplied value in a condition for a rule to apply. In the following sample rule, all CR images are sent to Kansas City:

> Other operators can also be used. The following example uses !=, indicating that all images *except* CR images should be sent to Kansas City.

> Operators are described in detail on page [<u>17</u>](#_bookmark13).

> Wildcards in a Rule

> Use wildcards in a rule when you want a condition to be valid for more than one value. In the example below, all images, regardless of modality, will be routed.

> Wildcards are described in detail on page [<u>18</u>.](#values)

> Date/Time Conditions in Rules

> A rule using date/time conditions can be used to route images based on date, time of day, or type of day (such as weekday, holiday, and so on). A rule to route all CR images on certain days would look like:

> Date/time conditions are described in detail on page [<u>18</u>.](#values-for-datetime-properties)

## Destinations in Rules

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### send, dicom, and balance Commands

> The first parameter in a routing rule is one of the following commands: send, dicom, or

> balance.

> send is used for Imaging destinations such as remote VistARad workstations.

> dicom is used for DICOM Storage SCP destinations such as film printers.

> Use the balance command when you want to divide a pool of exams among multiple destinations (Imaging destinations only). For detailed information about using the balance command, see page [<u>21</u>.](#load-balancing)

> Note Do not use spaces between the send, dicom, or balance commands and the left parenthesis in the first line of a rule. If a space is present, the rule will not work.

#### Specifying Destinations

> In a rule, destinations are always indicated by parentheses. While quotation marks are required only if a destination name contains spaces or other special characters, it is recommended that quotation marks be used all the time for consistency.

> To automatically route similar exams to multiple destinations, multiple rules would be used, as shown below:

> The destination specified in a rule must be a valid Imaging destination (such as a VistARad workstation) or a valid DICOM Storage SCP destination (such as an external PACS or film printer). Destinations are described in more detail on pages [<u>25</u>](#naming-conventions-for-imaging-destinations) and [<u>35</u>.](#adding-storage-scp-destinations-for-routing-to-scu_list.dic)

## Conditions in Rules

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In routing rules, a condition is a comparison between a particular image property and a user-supplied value. The results of the comparison determine whether or not the rule will be applied to an image.

> A single when statement precedes all conditions in a rule. (Optionally, if can be used instead of when.)

> A routing rule can contain multiple conditions. (When defining multiple conditions for a rule, list the most restrictive condition first. This will minimize the amount of time needed to process the rule.)

> After the when (or if statement), each condition must be rendered as:

> \<property\>\<operator\>\<value\> where:

- \<property\> is one of the known attributes of an image. Properties that can be used in a condition are listed the following section.
- \<operator\> is a code for a type of comparison. Operators are described on page [<u>17</u>.](#_bookmark13)
- \<value\> is supplied by the user, and specifies what is being tested in the condition. Values are described on page [<u>18</u>.](#values-for-datetime-properties)

#### Properties

> The properties listed in this section can be used in routing rule conditions.

> Note While property names are not case-sensitive, property names are typically rendered in upper case.

> Frequently Used Properties

> MODALITY

> Abbreviation for the type of modality. Possible values are listed below. Retired values are indicated by (ret).

> AS Angioscopy (ret 2007) AU Audio

> BI Biomagnetic imaging BDUS Bone Densitometry

> (Ultrasound)

> BMD Bone Densitometry (X-Ray)

> CD Color flow Doppler CF Cinefluorography (ret)

> CP Culposcopy (ret 2007) CR Computed Radiography CS Cystoscopy (ret 2007) CT Computed Tomography DD Duplex Doppler

> DF Digital fluoroscopy (ret) DG Diaphanography

> DM Digital microscopy (ret 2007)

> DOC Document

> DS Digital Subtraction Angiography (ret)

> DX Digital Radiography EC Echocardiography

> (ret 2007)

> ECG Electrocardiography EPS Cardiac

> Electrophysiology ES Endoscopy

> FA Fluorescein angiography (ret 2007)

> FS Fundoscopy (ret 2007) GM General Microscopy HC Hard Copy

> HD Hemodynamic Waveform

> IO Intra-oral Radiography IVUS Intravascular

> Ultrasound

> KO Key Object Selection LP Laparoscopy

> (ret 2007)

> LS Laser surface scan MA Magnetic resonance

> angiography (ret 2007) MG Mammography

> MR Magnetic Resonance MS Magnetic resonance

> spectroscopy (ret 2007) NM Nuclear Medicine

> OCT Optical Coherence Tomography

> OP Ophthalmic Photography

> OPM Ophthalmic Mapping OPR Ophthalmic Refraction OPT Ophthalmic

> Tomography

> OPV Ophthalmic Visual Field OT Other

> PR Presentation State

> PT Positron emission tomography (PET)

> PX Panoramic X-Ray REG Registration

> RF Radio Fluoroscopy RG Radiographic imaging

> (conv. film/screen) RTDOSE Radiotherapy Dose RTIMAGE Radiotherapy Image RTPLAN Radiotherapy Plan RTRECORD RT Treatment Record RTSTRUCT Radiotherapy Structure

> Set

> SC Secondary Capture (VA addition)

> SEG Segmentation SM Slide Microscopy

> SMR Stereometric Relationship SR SR Document

> ST Single-photon emission computed tomography (SPECT)

> TG Thermography US Ultrasound

> VF Videofluorography (ret)

> VL Visible Light

> (not an official code) XA X-Ray Angiography XC External-camera

> Photography

> NOW

> Date and time that the rule is being processed. For more information, see page [<u>18</u>.](#values-for-datetime-properties)

> SOURCE

> Name of the site that originally acquired the image. The value for this field is determined as follows:

- If the ACQUISITION SITE field (#2005, .05) for an image entry contains a value, this value is considered the source. (For images acquired after Patch 11, ACQUISITION SITE is populated based on the value of Institution Name in

> Instrument.dic. For images acquired before Patch 11, ACQUISITION SITE is not populated.)

- If there is no value for ACQUISITION SITE, the credentials of the user are checked. If a value is defined for the current division (i.e., the location code for the DICOM Gateway from which the evaluation processor was started), the number of this division will be used.
- If the division number cannot be derived from a user's credentials, the KERNEL SITE PARAMETER field for the number of the institution will be used.

> Other Properties

> ABSTRACT_REF

> The network storage location of the image abstract.

> ACQUISITION_DEVICE

> The name of the device that generated the image as defined in the ACQUISITION DEVICE File (#2006.04), see Note below.

> BIG_JUKEBOX_PATH

> Full file path on jukebox for .BIG images.

> BIG_MAGNETIC_PATH

> Full file path for .BIG images. This field indicates on which magnetic server this file resides.

> CLASS

> The class of the image, as stored in the CLASS INDEX field (#2005, 41). Typical values are CLIN, ADMIN, CLIN/ADMIN, and ADMIN/CLIN, see Note below.

> CLINIC

> If an image is associated with a patient encounter (visit), the value of this parameter is the name of the clinic where the appointment occurred.

> DESCRIPTIVE_CATEGORY

> This is mainly for Document Imaging; it further describes the type of document image.

> EXAM_TIME

> Used to compare the date/time of the procedure to a user-supplied value. For more information about date/time-based comparisons, see page [<u>18</u>.](#values-for-datetime-properties)

> Note In older versions of the software, variations of this property (EXAM_TIME_FIRST, EXAM_TIME_LAST) could be used to base the comparison on the newest or oldest image in an exam. The current version of the software evaluates the first image encountered only, so all variations of this property are handled the same way.

> EXPORT_REQUEST_STATUS

> The value of this field, if defined, indicates if MailMan will send or has sent the image to another site. There are two possible values:

> 1 = EXPORT REQUESTED

> 0 = EXPORTED

> FILE_REF

> The unique filename of the image, as stored on the magnetic server and/or jukebox.

> IMAGE_SAVED

> Used to compare the date/time of the image capture to a user-supplied value. For more information about date/time-based comparisons, see page [<u>18</u>.](#values-for-datetime-properties)

> Note In older versions of the software, variations of this property (IMAGE_SAVED_FIRST, IMAGE_SAVED_LAST) could be used to base the comparison on the newest or oldest image in an exam. The current version of the software evaluates the first image encountered only, so all variations of this property are handled the same way.

> IQ

> Indicates if an image has questionable integrity, as specified in the IQ field (#2005, 13). This field is either empty or equal to YES. Note that images with questionable integrity may not be displayed by the software on the receiving system. (In VistARad, a warning is displayed if a user opens an image with questionable integrity.)

> LAST_ACCESS

> Used to compare the date/time of an image’s last access to a user-supplied value. For more information about date/time-based comparisons, see page [<u>18</u>.](#values-for-datetime-properties)

> Note In older versions of the software, variations of this property (LAST_ACCESS_FIRST, LAST_ACCESS_LAST) could be used to base the comparison on the newest or oldest image in an exam. The current version of the software evaluates the first image encountered only, so all variations of this property are handled the same way.

> MAGNETIC_REF

> The path for the network location of the stored image.

> MICROSCOPIC_OBJECTIVE

> Free text description of the Microscopic Objective selected by the pathologist.

> OBJECT_NAME

> The natural language name for the image, usually consisting of the patient name, social security number, and image description.

> OBJECT_TYPE

> The object type (such as still image, black and white image, or x-ray) as described in the OBJECT TYPE File (#2005.02).

> ORIGIN_INDEX

> The field indicates the source of image. There are five possible values: D = DoD

> F = Fee-basis study ordered by VA to be performed at a contract facility N = Other

> V = VA

> \<null\> = VA

> PACKAGE

> An abbreviation for the name of the package that the image is attached to, as defined in the PACKAGE INDEX field (#2005, 40). Possible values are: RAD, LAB, MED, NOTE, CP, SUR, PHOTOID, NONE, or CONS.

> PACS_PROCEDURE

> The name that identifies the procedure in the radiology reports file.

> PACS_UID

> The unique 26-character image identifier of the PACS image.

> PARENT_DATA

> The name of the file that contains the “Parent Data.” See also PARENT_DATA_FILE_IMAGE_POINTER, PARENT_GLOBAL_ROOT_D0 and PARENT_GLOBAL_ROOT_D1.

> PARENT_DATA_FILE_IMAGE_POINTER

> In the file identified by “Parent Data,” a multiple-valued field may exist that identifies groups of images. When there is such a “multiple,” the value of this parameter is the entry number in this multiple that points back to the parent image of the current image.

> PARENT_GLOBAL_ROOT_D0

> The internal entry number in the file identified by PARENT_DATA.

> PARENT_GLOBAL_ROOT_D1

> The value of this parameter is defined only for laboratory images to record the third subscript of ^LR(D0,"SP",D1) as a backward pointer for use in report display and image deletion.

> PATH_ACCESSION_NUMBER

> The Anatomic Pathology accession number — the identifying number for the slide.

> PATIENT

> The name of the patient.

> PROCEDURE

> An abbreviation for the procedure as stored in the PROCEDURE field (#2005, 6). Typical values are COL for colonoscopy, SUR for surgery, SP for surgical pathology, or XRAY for radiology.

> PROCEDURE_OR_EVENT

> The name of the procedure or event for which the image was created, as stored in the

> PROC/EVENT INDEX field (#2005, 43), see Note below..

> PROCEDURE_TIME

> This property works the same way as EXAM_TIME, described earlier in this section.

> RADIOLOGY_REPORT

> The name of the Radiology Report associated with the image.

> SAVED_BY

> The name of the person who logged in to capture the image.

> SHORT_DESCRIPTION

> A one-line description of the image or object record.

> SPECIALTY

> The specialty (or sub-specialty) for which the image was acquired, as stored in the

> SPEC/SUBSPEC INDEX field (#2005, 44), see Note below..

> SPECIMEN

> The specimen number of the slide given in the LAB DATA File (#63).

> SPECIMEN_DESCRIPTION

> The description given to the specimen in the LAB DATA File (#63).

> STAIN

> Free text description of the Histological Stain.

> SUMMARY

> A flag that indicates whether or not the image functions as a summary for a group. The value of this property is either empty, or equal to 0 (NO) or 1 (YES).

> TRACKING_ID

> The package that performed the Import (value looks like package name: ID-code).

> TYPE

> The type of image, as stored in the TYPE INDEX field (#2005, 42). Typical types are

> IMAGE, DIAGRAM, CONSENT, etc., see Note below.

> URGENCY

> A code indicating the clinical urgency of the exam. Possible values are ROUTINE, URGENT, and STAT.

> WORM_REF

> The network location of the jukebox platter where the image is stored (provided there is a jukebox in the Imaging system).

> <span id="_bookmark13" class="anchor"></span>Note There is a problem with the keywords ACQUISITION_DEVICE, CLASS, PROCEDURE_OR_EVENT, SPECIALTY and TYPE. The documentation says that the name of the referenced entry should be used. The name matching for these keywords does not work and the pointer value in the IMAGING file (#2005) must be used for matching instead. This problem will be corrected in a later patch so that the name of the reference entry can be used for matching, instead of having to use the pointer value.

> The following table shows the referenced file that is used to determine the value of the pointer that is needed for the match.

<table>
<colgroup>
<col style="width: 51%" />
<col style="width: 15%" />
<col style="width: 32%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Property Name</strong></th>
<th><blockquote>
<p><strong>Field #</strong></p>
</blockquote></th>
<th><blockquote>
<p><strong>Referenced File</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ACQUISITION_DEVICE</td>
<td><blockquote>
<p>107</p>
</blockquote></td>
<td><blockquote>
<p>2006.04</p>
</blockquote></td>
</tr>
<tr class="even">
<td>CLASS</td>
<td><blockquote>
<p>41</p>
</blockquote></td>
<td><blockquote>
<p>2005.82</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>PROCEDURE_OR_EVENT</td>
<td>6</td>
<td><blockquote>
<p>2005.85</p>
</blockquote></td>
</tr>
<tr class="even">
<td>SPECIALTY</td>
<td><blockquote>
<p>44</p>
</blockquote></td>
<td><blockquote>
<p>2005.84</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>TYPE</td>
<td><blockquote>
<p>42</p>
</blockquote></td>
<td><blockquote>
<p>2005.83</p>
</blockquote></td>
</tr>
</tbody>
</table>

> You must use FileMan to determine the number that must be used for the match. This example shows how to do this for CLASS.

> DVA\>D P^DI

> VA FileMan 22.0

> Select OPTION: PRINT FILE ENTRIES

> OUTPUT FROM WHAT FILE: IMAGE// 2005.82 IMAGE INDEX FOR CLASS

> (4 entries) SORT BY: NAME//

> START WITH NAME: FIRST// FIRST PRINT FIELD: NAME THEN PRINT FIELD: NUMBER THEN PRINT FIELD:

> Heading (S/C): IMAGE INDEX FOR CLASS LIST Replace DEVICE: HERE

> IMAGE INDEX FOR CLASS LIST FEB 26,2010 07:46 PAGE 1

> NAME NUMBER

<table>
<colgroup>
<col style="width: 69%" />
<col style="width: 30%" />
</colgroup>
<thead>
<tr class="header">
<th>ADMIN</th>
<th>8</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>ADMIN/CLIN</td>
<td>9</td>
</tr>
<tr class="even">
<td>CLIN</td>
<td>1</td>
</tr>
<tr class="odd">
<td><p>CLIN/ADMIN</p>
<p>Select OPTION:</p></td>
<td>7</td>
</tr>
</tbody>
</table>

> If you wanted to match on “CLIN”, you would have to match on the number 1, that is CLASS=1.

> (In a later patch, once the problem has been corrected, the match will use the name instead of the number, like CLASS=“CLIN”.)

#### Operators

> The following operators can be used in routing rule conditions:

| Operator | Image property must…                                                                                   |
|--------------|------------------------------------------------------------------------------------------------------------|
| =            | Match value in rule.                                                                                       |
| !=           | Not match value in rule.                                                                                   |
| \<           | Be less than a numeric value in rule. For date/time values, this operator can be used for “earlier than.”  |
| \>           | Be greater than a numeric value in rule. For date/time values, this operator can be used for “later than.” |
| \<=          | Be less than or equal to a numeric or date/time value in rule.                                             |
| \>=          | Be greater than or equal to a numeric or date/time value in rule.                                          |

> Note When operators are used, spaces between the operator and the operand are not allowed.

#### Values

> Values are the user-supplied part of a routing rule condition. Most values are text strings.

> Values are typically enclosed in quotation marks ("). If a value contains both upper and lowercase characters, or if it contains punctuation marks or spaces, quotation marks are required.

> Two types of wildcard characters can be used in routing rules: the asterisk (\*) and the question mark (?). The question mark allows one single character in a value to be “any character.” The asterisk allows one or more characters to be “any character.”

#### Values for Date/Time Properties

> When a condition based on date and time is used, the supplied value must adhere to FileMan conventions. Values for date/time conditions are presented as a range enclosed in braces { }.

> The most frequently used date/time property is NOW. NOW can be used to select the times that a staff member will be present by specifying certain days and times of day.[<sup>1</sup>](#_bookmark16) Note that all day abbreviations use the first three letters of the day name (Thursday = Thu).

> Date/time properties can also be used to specify holidays. In this context, holidays are those days that are marked as such in the sending site’s HOLIDAY File (#40.5). A rule to send images on holidays would be specified as:

> Date/time ranges use a 24-hour clock. While use of AM or PM indicators is not required they can be useful when the hours specified are 0:00 AM (midnight) and 12:00 PM (noon).

> When the routing software compares a date/time property in an image entry to a specified value, the date/time value is broken into components:

> Day of week Hour

> Day of month Minute

> Month Second

> Year

> The use of each component in an actual comparison depends on the specified value.

> <span id="_bookmark16" class="anchor"></span><sup>1</sup> The actual value of NOW is the moment when the rule is evaluated.

## Routing Rule Priority

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Automatically routed exams are assigned a default priority of Medium. This priority can be changed by adding a priority statement after the conditions for the rule.

> In addition to the priority that is derived from routing rules, the clinical urgency of an exam is taken into account for automatic routing. For more information, see page [<u>5</u>.](#priority-and-routing)

## Routing Images from Prior Exams

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Images from prior exams can be automatically routed by adding a priorstudy

> statement after the conditions for the rule.

> When priorstudy is set to YES, images from prior exams will be included based on routing-specific settings in the MAG RAD PRIOR EXAMS LOGIC File (#2006.65). Settings in this file are described in detail on page [<u>37</u>](#defining-route-priors-logic).

> Note Only priors acquired at the same site as the current exam can be automatically routed.

> When priorstudy is set to NO, or if the priorstudy statement is absent, images from prior exams will not be included.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>![](vista-imaging-dicom-gateway-routing-setup-and-user-guide/008.png)</p>
</blockquote></th>
<th><blockquote>
<p>Using <strong>priorstudy</strong> in a routing rule can significantly increase network traffic.</p>
<p>If a rule of this sort is implemented, be sure to monitor the network to ensure no problems arise.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Routing Rules and Compression

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Images routed to Imaging destinations (such as a VistARad workstation) can be compressed if the destination is set up as described in Appendix B. Images routed to DICOM Storage SCP destinations cannot be compressed.

> While the use of compression is dictated by a destination’s definition, rather than by routing rules, you will need to set up two rules if you want to route both compressed and uncompressed images. You will also need to set up two destinations in the NETWORK LOCATION File (#2005.2).

> The definitions of the two destinations in the NETWORK LOCATION File will be the same, except for the destination name and the setting for compression.

> The rules would also be the same, except for the destination name.

> This will allow both compressed and uncompressed images to be sent to the same destination.

## Load Balancing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The balance command can be used when you want do divide a pool of exams across multiple destinations. All destinations must be Imaging destinations (not DICOM Storage SCP destinations), and the total value of the percentages specified in the command must equal 100 percent.

> The balance command can also be used to route some exams and not others. In the sample rule below, 75% of the exams are not routed, while the remaining 25% are sent to KANSASCITY.

> When the balance command is used, two things determine which destination receives a given exam: the percentages specified in the rule and internal counters set by the routing software.

> The first time a load balancing rule is applied, the routing software begins distributing exams the same way a deck of cards is dealt: the first destination receives one exam, the second destination receives the next exam, and so on. Exams are evenly distributed until the destination with the lowest value specified in the balance command has received its allotted percentage of exams. Then that destination is skipped until the counter resets.

> Since load balancing is based on percentages, the counter is reset each time 100 exams have been sent.

> For example, if a rule specifies…

- The first 30 exams will be distributed evenly, with each destination receiving 10 exams. After DEST1 has received 10 exams, DEST1 is skipped until the counter resets.
- The next 60 exams are split evenly between DEST2 and DEST3 until DEST2 and DEST3 each have 40 exams. DEST2 now has its allotment of 40 exams, and will be skipped until the counter resets.
- The remaining 10 exams are sent to DEST3, giving that destination a total of 50 exams.
- Once 100 exams have been sent, the routing software resets its counters to zero, and starts distributing exams to all three destinations again.

> <span id="_bookmark21" class="anchor"></span>Resetting the Load Balancing Counter

> When routing rules are imported, the counters used for load balancing are all reset to zero. You can take advantage of this trait if you need to fine-tune or troubleshoot situations where load balancing is used. Note that it is not necessary to change routing rules to achieve this; you only need to re-import them.

## Routing Rule Tips

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following tips may be useful while creating or editing routing rules:

- When defining multiple conditions for a rule, list the most restrictive condition first. This will reduce the amount of time needed to process the rule.
- The number symbol (#) can be used for comments, or to disable a rule. When disabling a rule, precede each line in the rule with \#.
- For rules that serve DICOM Storage SCP destinations, use dicom instead of send.
- Either when or if can be used to set up comparisons in a routing rule.
- Make sure that there are no spaces between operators (described on page [<u>17</u>](#_bookmark13)) and other parameters in a rule.

> When rules are imported as described on page [<u>41</u>,](#creating-and-importing-a-routing-rules-file) the routing software will check the syntax used and will report on any problems detected.

> This page is intentionally blank.

# Configuring Routing 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### This chapter assumes that routing software has been installed, and that an initial set of routing rules has been defined.

> This chapter explains how to configure a routing system. The following table lists the configuration tasks described in this chapter.

| Configuration Task                                       | Performed By   | See Page…                                                |
|--------------------------------------------------------------|--------------------|--------------------------------------------------------------|
| Set up Imaging destinations                                  | All sites involved | [<u>24</u>](#defining-imaging-destinations)                  |
| Set up DICOM Storage SCP destinations                        | All sites involved | [<u>35</u>](#defining-dicom-storage-scp-destinations)        |
| Review/edit route priors logic                               | Sending site       | [<u>37</u>](#defining-route-priors-logic)                    |
| Image Gateway configuration                                  | Sending site       | [<u>40</u>](#image-gateway-configuration)                    |
| Routing Gateway configuration                                | Sending site       | [<u>41</u>](#routing-gateway-configuration)                  |
| Import routing rules                                         | Sending site       | [<u>41</u>](#importing-routing-rules-route.dic)              |
| VistARad site parameter setup                                | Sending site       | [<u>44</u>](#vistarad-configurationsending-sites)            |
| VistARad workstation setup                                   | Receiving site     | [<u>45</u>](#vistarad-configurationreceiving-sites)          |
| Alter configuration in response to changes in routing system | All sites involved | [<u>46</u>](#changes-affecting-routing-system-configuration) |

> A configuration checklist is also available in [<u>Appendix A</u>.](#appendix-a-routing-worksheets)

## Defining Imaging Destinations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> An Imaging destination (such as a remote VistARad workstation) is defined by creating an entry in the NETWORK LOCATION File (#2005.2), and implemented by creating a target folder and share where the routed images will be stored.

> Before you begin, you should establish naming conventions that are agreed upon by the sending and receiving sites.

> A destination definition worksheet is located on page [<u>69</u>.](#imaging-destination-worksheet)

#### Naming Conventions for Imaging Destinations

> The values that identify an Imaging destination are stored in the NETWORK LOCATION

> File (#2005.2) at the site where the Routing Gateway is installed.

> Before an Imaging destination is established, the sending and receiving sites need to decide how to identify themselves.

<table>
<colgroup>
<col style="width: 25%" />
<col style="width: 50%" />
<col style="width: 24%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Description</strong></th>
<th><strong>Notes</strong></th>
<th><strong>Field</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>The “official” destination name</td>
<td><p>Used to identify the destination in routing rules. Also specified at VistARad workstations that will be accessing routed images.</p>
<blockquote>
<p>Cannot match any other name in the NETWORK LOCATION File or in the DICOM TRANSMIT DESTINATION File (#2006.587).</p>
<p>Up to 30 characters, no spaces or punctuation.</p>
</blockquote></td>
<td>Network Location (#2005.2,.01)</td>
</tr>
<tr class="even">
<td>The computer and share name at the receiving site</td>
<td><blockquote>
<p>The name used should be meaningful to both the sending and receiving sites.</p>
</blockquote>
<p>Up to 63 characters, may contain any valid machine/share syntax.</p></td>
<td>Physical Reference (#2005.2,1)</td>
</tr>
<tr class="odd">
<td>Destination as reported to VistARad users</td>
<td><blockquote>
<p>Used in the RC column of VistARad’s exam lists.</p>
</blockquote></td>
<td>Site (#2005.2,25)</td>
</tr>
</tbody>
</table>

> The example on the next page illustrates how the key values in the NETWORK LOCATION

> File would be used in a sample routing system.

#### A Sample Routing System for Imaging Destinations

> Images are routed from the main hospital (VAMC1) to two different destinations. One of the destinations is an affiliated university that provides after-hours radiology coverage.

> The other destination is the office of a radiologist who provides consultations for ultrasound exams.

> NETWORK LOCATION File entries at VAMC1 (partial entries; other fields excluded)

> Name (#2005.2,.01): UNI TELERAD

> Phys. Ref. (2005.2.1): \\10.132.xxx.001\ROUTING\$\\

> Site (#2005.2,25): UNI TELE

> Name (#2005.2,.01): CONSULT US

> Phys. Ref. (2005.2.1): \\10.132.xxx.002\ROUTING\$\\

> Site (#2005.2,25): CON US

> Routing rules at VAMC1

send("UNI TELERAD")

> when MODALITY="\*" URGENCT=STAT

> NOW={MON 08:00PM to 11:59PM; TUE 12:00AM to 03:59PM; TUE 08:00PM to 11:59PM; WED 12:00AM to 03:59PM; WED 08:00PM to 11:59PM; THU 12:00AM to 03:59PM; THU 08:00PM to 11:59PM; FRI 12:00AM to 03:59PM; FRI 08:00PM to 11:59PM; SAT 12:00AM to 03:59PM; SAT 08:00PM to 11:59PM; SUN 12:00AM to 03:59PM; SUN 08:00PM to 11:59PM; MON 12:00AM to 03:59PM;

> send("CONSULT US") when MODALITY="US"

> Setup at affiliated university

> Storage folder share name: \\10.132.xxx.001\ROUTING\$\\

> VistARad CacheLocationID: UNI TELERAD

> Exam source in VistARad RC column: UNI TELE

> Setup at offsite ultrasound specialist’s office

> Storage folder share name: \\10.132.xxx.002\ROUTING\$\\

> VistARad CacheLocationID: CONSULT US

> Exam source in VistARad RC column: CON US

#### Storage Folders for Imaging Destinations

> This section explains how to create and verify a folder for an Imaging destination on a Windows-based server. The folder will be used as the storage location for routed images at a receiving site, and will be referenced in the NETWORK LOCATION File (#2005.2) entry that defines the destination.

> Folder Prerequisites

- Determine which credentials (user name and password) will be used by the routing software to access the storage folder. The routing software must have full access to the folder.

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>![](vista-imaging-dicom-gateway-routing-setup-and-user-guide/009.png)</p>
</blockquote></th>
<th><blockquote>
<p>Receiving sites need to establish a procedure by which user name/</p>
<p>password changes can be implemented without affecting routing. Unannounced password changes are a major cause of routing problems.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

- The sending site should work with the receiving site to estimate the amount of storage space needed based on the anticipated volume of transmitted images and the planned retention period.

> Folder Creation

> When the folder to be used as an Imaging destination is established, the receiving site will need to choose a logical folder name and share name. The share name will ultimately be referenced in the *sending* site’s NETWORK LOCATION File.

#### Creating and sharing a folder to be used as an Imaging destination

1.  Log in as an Administrator to the computer where you will be creating the folder, and start Windows Explorer.
2.  Select the drive (or folder) in which you want to create the new folder.
3.  Click File \| New \| Folder. After the new folder appears in the right side of the Explorer window, type the name of the new folder and press \<Enter\>.
4.  Right click the new folder, then click Sharing.
5.  On the Sharing tab, click the Sharing and Security option, then enter the share name you want used for the folder.
    - To minimize DNS issues, use the IP address instead of the computer name.
    - The combined string identifying the computer and the shared folder cannot be more than 63 characters long.
    - It is recommended that you make the folder a hidden share by adding a dollar sign (\$) to the end of the share name. A hidden share will be accessible by the routing software, but will not be visible to users browsing your network.
6.  After typing the share name, click Permissions.
7.  In the Permissions dialog, click Add, then select the user group/user name that the routing software will use to access this folder.
    - Include the user name and password for the user you choose in the NETWORK LOCATION File entry that references this folder.
    - Use the domain name as well as the user name. Example: VHAIS\VHAKANIU

> (note the absence of leading backslashes).

8.  After adding the “routing user,” set the access type for the routing user to Full.
9.  In the list of users allowed to access the folder, click the Everyone user group, then click Remove.
10. When you have finished, click OK to apply your changes and to close the Properties dialog.
11. Notify the sending site that the folder is available, and provide the site with the share name, user name and password.

> <span id="_bookmark26" class="anchor"></span>Folder Verification

> The sending site will need to verify that the folder can be remotely accessed and that files can be copied to and deleted from the folder.

#### Verifying a folder using Windows Explorer

1.  On the computer you will be using to test the folder, log in as an Administrator and then start Windows Explorer.
2.  In Windows Explorer, click Tools \| Map Network Drive Hash Subdirectory: \<set as appropriate for your site\> (value is Yes).
3.  In the Map Network Drive dialog, enter the drive letter, path, and user name (including domain name) that the routing software will be using. Then click OK.
4.  When prompted, enter the password that will be used by the routing software, then click OK.
5.  Select the folder to which you just mapped, copy a test file into the folder, and delete the file. If the file is successfully copied and deleted, the routing software should be able to use the folder.
6.  Disconnect the mapped drive.

> Note If you cannot map the folder, use the next set of steps below to provide more detailed information about the problem you are encountering.

#### Verifying a folder using the command line

1.  Log in as an Administrator to the computer you will be using to test the folder.
2.  Open a command prompt window (choose Start \| Run, then enter cmd).
3.  Enter the following command to map the folder to a local drive. Parameters shown in bold will need to be replaced with valid values established by the receiving site.
    - net use x: \\VHAxxxxxx\\sharename\\ password /u:username
4.  After mapping the drive, copy a test file to the folder, and then delete the file. If the file is successfully copied and deleted, the routing software should be able to use the folder.
    - copy any.file x:\\path\>
    - delete x:\\path\>\any.file
5.  When you are satisfied that the above parameters can be used to successfully access the folder, delete the test file, then terminate the test connection.
    - net use x: /delete

<table>
<colgroup>
<col style="width: 9%" />
<col style="width: 90%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>![](vista-imaging-dicom-gateway-routing-setup-and-user-guide/010.png)</p>
</blockquote></th>
<th><blockquote>
<p>Be sure to terminate the test connection. Letting a connection linger may</p>
<p>prevent the routing software from establishing its own connection to the folder.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

#### Imaging Destination Definition

> Imaging Destination Definition using FileMan

> The following steps explain how to create an Imaging destination using FileMan. For information about values for specific fields, refer to page [<u>31</u>.](#_bookmark28) A destination definition worksheet is also located on page [<u>69</u>.](#appendix-a-routing-worksheets)

> Editing the NETWORK LOCATION File at the sending site

1.  Log into the VistA Hospital Information System.
2.  Use FileMan to select the NETWORK LOCATION File (#2005.2) for editing.
3.  When you are prompted to select a network location, enter the name that you want used for the destination.

> Note The name must be entered in uppercase, cannot contain punctuation or spaces, and must be unique.

4.  Skip the prompt for PLACE. This field is not used for routing purposes.
5.  At the next prompt, enter the computer name and share name specified for the destination.
6.  At each new prompt, enter the desired values for each field. Be sure to enter Y at the

> ROUTER prompt.

> Note Typical values for a routing destination are shown below. For more detailed information about a particular field, enter "?" at the prompt, or refer to the next section.

> <span id="_bookmark27" class="anchor"></span>Imaging Destination Definition usingthe Background Processor

> The Background Processor software can also be used to define an Imaging destination in the NETWORK LOCATION File (#2005.2). (In the Background Processor, choose Edit \| Network Location Manager). A destination definition worksheet is also located on page [<u>69</u>.](#appendix-a-routing-worksheets)

> <span id="_bookmark28" class="anchor"></span>Imaging Destination Values

> Fields in the NETWORK LOCATION File are described below. These fields are listed in the order that they are defined in the file, and their descriptions assume that a routing destination is being defined.

> NETWORK LOCATION

> This field serves as the destination name for the location where image files will be sent, and is used in routing rules. The routing software will accept uppercase alphanumeric characters, but will not accept values that use lowercase characters or other punctuation marks.

> PLACE

> Not used for routing.

> PHYSICAL REFERENCE

> This field identifies the physical network location where routed images will be stored. This value must contain the computer name and the share name of the directory where routed images will be stored.

> \\ISWIMG01\IMAGE1\$\\

> \\TeleRad\Wichita\$\\

> This value must be entered using UNC (Universal Naming Convention) standards. This field is limited to 63 characters in length, and must end in a backslash ( \\ ).

> TOTAL SPACE, SPACE USED, FREE SPACE

> These fields are not used for routing.

> OPERATIONAL STATUS

> The value for this field can be 0 (off-line) or 1 (on-line). The routing software will set this value appropriately as it is operating. When no connection can be established, the routing software will set this field to 0 (off-line). Once this field is set to 0, the routing software will not attempt to reach the storage location referenced in this entry for 15 minutes. After 15 minutes have passed, the routing software will reset this field to 1 and then try to connect again.

> STORAGE TYPE

> The value of this field describes the media type for the storage location identified above. For routing destinations, the value will be MAGNETIC.

> HASH SUBDIRECTORY

> The value of this field determines if routed image files are stored in one single directory (value is Yes), or in a hierarchy of directories (value is Yes). This value should be set based on the needs of your site.

> ABSTRACT

> The value of this field indicates whether or not “abstract” files should be transmitted to this destination. Abstract files (also known as thumbnail or icon files) are used by Clinical Display workstations.

> FULL

> Set to Yes for routing. The value of this field indicates whether or not “full” files should be transmitted to this destination. Full files contain the complete image, potentially at a reduced resolution. (If an image is stored in DICOM format, the “full” file is a DICOM file, not a Targa file.)

> BIG

Set to Yes for routing. The value of this field indicates whether or not “big” files should be transmitted to this destination. Big files contain the complete image, always at the original resolution.

> TEXT

> Set to Yes for routing. The value of this field indicates whether or not text files should be transmitted to this destination. Text files contain the header information from the original DICOM file.

> DICOM

> Do not use.

> COMPRESSION

> A code that indicates which type of compression will be used for routed images. When the value of this field is equal to “J2K”, JPEG 2000 compression will be

> applied before the file is transmitted. When the value of this field is None, or if the field is empty, no compression will take place. All images that are sent to the destination will be treated in the same fashion, that is: either compressed or uncompressed.

> Note If compressed images are to be sent to a VistARad workstation, the MAG_Decompressor software will need to be installed on the workstation. See Appendix B for more information.

> Note You will need to purchase an Aware JPEG2000 Toolkit client license for each system that is receiving routed images. (Even if that system serves as a centralized temporary storage for multiple workstations, only a single client license is needed). For each system (DICOM Gateway) that is transmitting compressed routed images, you will need to purchase an Aware JPEG2000 server license. For more information, contact Clinical Project Support.

> USER NAME

> The user name of the account that the routing software will use to log into the shared folder defined in the PHYSICAL REFERENCE field.

> PASSWORD

> The password of the account that is used by the routing software to log into the destination. The password is case-sensitive and is stored in an encrypted format.

> MAINTAINCONNECTION

> This field is not used for routing, and should be left blank.

> MAX \# RETRY ON CONNECT

> Indicates the maximum number of successive attempts that will be made by the routing software to connect to a destination. A typical value is three attempts. If a successful connection cannot be made, the destination will be marked “off-line.” After 15 minutes, the destination will be marked “on-line,” and the routing software will begin trying to connect to this destination again.

> MAX \# RETRY ON TRANSMIT

> Indicates the maximum number of successive attempts the routing software will make to transmit a file to this destination. A typical value is five attempts. If the transmission fails after the defined number of attempts, the entry for the image in the transmission queue will be marked as failed. (There is a Routing Gateway menu option to re-transmit failed queue entries.)

> SYNTAX

> Indicates the format for the name of the physical location. Currently, only UNC

> (Universal Naming Convention) is accepted.

> SUBDIRECTORY

> Typically, this field is left blank. The value of this field determines if a subdirectory (under the directory specified in PHYSICAL REFERENCE) should be used to store files for this destination. If hashing is turned off, all transmitted files will be stored in the subdirectory specified in this field; if hashing is turned on, all transmitted files will be stored in subdirectories of this subdirectory.

> Select USER

> Do not use.

> RETENTION PERIOD

> The value of this field determines the number of days routed image files are stored at this destination. A typical value is five days, the maximum value that may be set is 365 days.

> Whenever a transmission processor (3-1) connects to a destination, it checks whether or not it has executed a purge for that destination on that day. If the connection in question is the first of the day and no purge has been executed yet, a purge will be initiated. During a purge, any image files older than the number of days specified by RETENTION PERIOD are deleted (note that files are always retained at the sending site).

> LAST PURGE DATE

> Do not change. This field is set by the transmission processor (3-1) when it executes a purge.

> SITE

> The value of this field is a code used by VistARad to identify the source of routed exams. The value of this field can be any text string. In the VistARad software, the value for this field will be shown in the RC (Remote Cache) exam list column.

> ROUTER

> The value of this field indicates whether or not the shared folder defined in the PHYSICAL REFERENCE field is being used as a routing destination. For routing, the value of this field must be Yes. Refer to the *Background Processor User Manual* for other uses of this field.

> TIME OFFLINE

> The value of this field will be filled in by the transmission processor (3-1) if it marks a destination as off-line. For more information, see MAX \# RETRY ON CONNECT.

> MUSE SITE \#, MUSE VERSION \#

> These fields are not used for routing.

## Defining DICOM Storage SCP Destinations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To define a DICOM Storage SCP destination (such as a film printer or external PACS), you will need to:

- Determine the names that will be used to identify the destination and gather information about the receiving application.
- Edit the SCU_List.dic file, a dictionary file used by the DICOM Gateway(s).
- Use the DICOM Gateway to load the contents of SCU_List.dic into the local DICOM Gateway database and into the DICOM TRANSMIT DESTINATION File (#2006.587) on VistA.

> A destination definition worksheet is located on page [<u>71</u>.](#dicom-storage-scp-destination-worksheet)

#### Naming Conventions for DICOM Storage SCP Destinations

> The first step in defining a DICOM Storage SCP destination is determining what to name the destination and how to identify the sender of DICOM images.

- The destination name can be up to 31 characters long (case-insensitive, punctuation is allowed), and must be unique. The name will ultimately be entered as the value for Application in SCU_List.dic.
- A title for the transmission processor (2-8-2) must be established. This value will ultimately be entered as the Calling AE in SCU_List.dic.

> The remaining information needed to define a DICOM Storage SCP destination is determined by the system that will be receiving the routed images. This information is described in detail on page [<u>36</u>.](#field-definitions)

#### Adding Storage SCP Destinations for Routing to SCU_List.dic

> This section explains how to update SCU_List.dic for routing, and how to load the contents of SCU_List.dic into the DICOM Gateway and VistA system databases. The steps below assume that a single instance of SCU_List.dic is used by all DICOM Gateways at a site.

1.  Stop all active DICOM processes by waiting until they reach an idle state, and then terminate them.
2.  On the DICOM Gateway, use a text editor to open x:\DICOM\Dict\SCU_List.dic, where x is the name of the drive used by the DICOM Gateway to store dictionary files.
3.  Add the information for each Storage SCP destination as shown below (comment lines are preceded by \#). Specific fields are defined in the next section.

> \# User Application List \# Format:

> \# line 1:App Name\|Called AE\|Calling AE\|Destination IP Address\|Socket \# line 2:\|Presentation Context Name\|Transfer Syntax Name

> \# line 3:\|\|Transfer Syntax Name (if there are more than one) \#

> MERGE EFILM\|VistA_Storage\|VistA_Send_Image\|111.222.33.44\|4006

> \|Modality Worklist Information Model - FIND\|Implicit VR Little Endian

> \|Verification SOP Class\|Implicit VR Little Endian

4.  Save the file.
5.  Open a terminal window and log into the DICOM Gateway software.
6.  In the first menu, enter 4 (System Maintenance).
7.  In the second menu, enter 2 (Gateway Configuration and DICOM Master Files).
8.  In the third menu, enter 5 (Update SCU_List.dic).
9.  When you are prompted to update the file, enter Y.
10. The file will be updated.

#### Field Definitions

> Fields defined in SCU_List.dic are described below. These fields are listed in the order that they appear in SCU_List.dic.

> App(lication) Name

> The name that will be used to identify the receiving application, and to identify the destination in a routing rule. The value for this field may be up to 31 characters long, is case-insensitive, and allows the use of punctuation.

> Called AE

> The Application Entity Title of the application that is being called. The value of this field is dictated by the system that will be receiving the DICOM transmission.

> Calling AE

> The Application Entity Title of the application that initiates the call (i.e., the Transmit DICOM Images to a DICOM SCP function of the DICOM Gateway). The value for

> this field may be up to 16 characters in length, is case-insensitive, and allows the use of punctuation.

> Destination IP

> The TCP/IP address of the machine that will be receiving the DICOM transmission. The IP address can be numeric (123.46.57.89), symbolic (xxx.yyy.med.va.gov), or a name stored in the local “hosts” file.

> Socket

> The TCP/IP port number of the system that will be receiving the DICOM transmission.

> Presentation Context

> The name of a presentation context supported by the system that will be receiving the DICOM transmission. Refer to the current DICOM standard for a complete list of possible values.

> Transfer Syntax

> The transfer syntax supported by the system that will be receiving the DICOM transmission. There are four possible transfer syntaxes:

> Implicit VR Little Endian Implicit VR Big Endian Explicit VR Little Endian Explicit VR Big Endian

## Defining “Route Priors” Logic

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Verifying that Prefetch is Enabled

> For priors to be included with automatically routed exams, prefetch must be enabled on VistA. Prefetch is generally enabled at sites using VistARad.

> You can verify that prefetch is enabled by checking the following settings.

- In the PROTOCOL File (#101), use FileMan to verify that MAGJ PREFETCH/SEND ORM

> is defined as a Subscriber to the RA REG protocol.

- In the APPLICATION PARAMETER File (#771), verify that MAGJ CLIENT is set to “Active.”

> Note The PREFETCH ACTIVE? setting in the VISTARAD SITE PARAMETERS FILE

> (#2006.69) does not affect the automatic routing of priors.

> For more information, refer to chapter 3 in the *Imaging System Installation Guide*.

#### How Prior Exam Routing Works

> The logic for automatically routing prior exams is triggered when a prior study

> statement is used in a routing rule. The baseline logic for routing priors is:

> For each exam being automatically routed, also route up to one matching prior exam up to 1800 days (about five years) old.

> Note Only priors from the same site as the current exam are considered. Priors from sites other than the current exam cannot be routed automatically (they can, however, be routed on-demand).

> This logic is stored in the MAG RAD PRIOR EXAMS LOGIC File (#2006.65). This file:

- Identifies, based on procedure name/CPT (Current Procedural Terminology) code, what qualifies as a prior exam.
- Determines the maximum number and age of exams to automatically route as priors.
- Determines the maximum number and age of exams to retrieve from the jukebox for VistARad prefetch.

#### Changing “Route Priors” Logic

> To change the logic used for automatic routing of prior exams, you will first need to identify the procedure name/CPT code of the current exams in question. Then you will need to edit the MAG RAD PRIOR EXAMS LOGIC File (#2006.65) as described below.

> Note Altering the settings used to identify a prior will affect VistARad’s prefetch function, as well as the auto-route priors capability. However, the settings that determine the number and age of priors to be automatically routed can be set independently from the similar settings used for prefetch.

#### To change “route priors” logic

1.  Log into the VistA Hospital Information System.
2.  Use FileMan to select the MAG RAD PRIOR EXAMS LOGIC File (#2006.65) for editing.
3.  Select fields .01, 1, 2, and 3 for editing.
4.  At the following prompt, enter the CPT code or description for the types of current exams you want to alter the route priors logic for. (Enter “?” to see a list of CPT codes and descriptions.)
5.  At the Select MATCHING CPT GROUP prompt, enter a CPT code that has been previously entered as being a match for the current exam, or enter a new CPT code to match to the current exam.

> Note Altering the settings for this prompt will affect VistARad’s prefetch function, as well as the auto-route priors capability.

6.  Set the following three prompts as desired for automatically routing priors. Details follow.

> AUTO-DISPLAY?

> Set to “YES” if exams that match the MATCHING CPT group selected in step 5 should be considered priors.

> DAYS LIMIT/AUTO-DISPLAY

> The value of this field should be set to an integer number. Studies that precede the current image by more than this number of days will not be candidates for automatic routing. Only studies that are less than the number of specified days will be included.

> VERSION LIMIT/AUTO-DISPLAY

> The value of this field should be set to an integer number. This number indicates

> the maximum number of prior studies that will be automatically routed for the current image.

7.  Select additional fields to edit, or exit FileMan.

## DICOM Gateway Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Sites that want to send images to other sites using routing will need to set the configuration file for all Image and Routing Gateways as described in the following sections.

> Note No configuration changes are needed for Text Gateways in a routing system.

#### Image Gateway Configuration

> Image Gateways at a site using automatic routing will need to have their configuration file set as described below.

> Note The following steps cover only routing-related configuration parameters. For information about other configuration parameters, refer to the DICOM Gateway Installation Guide.

#### To configure Image Gateways

1.  Open a terminal window and log into the DICOM Gateway software.
2.  Select option 4-2-2 (Update Gateway Configuration Parameters).
3.  Set the prompts indicated in bold below to Yes.
4.  Press \<Enter\> to cycle though the rest of the prompts and to exit the program.

#### Routing Gateway Configuration

> The system being used as a Routing Gateway will need to have its configuration file set as described below. Completing these steps will make the Routing Gateway menu option and its submenus available in the main DICOM Gateway Menu.

> Note The following steps cover only routing-related configuration parameters. For information about other configuration parameters, refer to the DICOM Gateway Installation Guide.

#### To configure the Routing Gateway

1.  Open a terminal window and log into the DICOM Gateway software.
2.  Select option 4-2-2 (Update Gateway Configuration Parameters).
3.  Set the prompts indicated in bold below to Yes.
4.  Press \<Enter\> to cycle though the rest of the prompts and to exit the program.

## Importing Routing Rules (Route.dic)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section covers the following topics:

- [<u>Creating and Importing a Routing Rules File</u>](#creating-and-importing-a-routing-rules-file)
- [<u>Verifying Imported Rules</u>](#verifying-imported-rules)
- [<u>Routing Rules and Multiple Routing Gateways</u>](#routing-rules-and-multiple-routing-gateways)

#### Creating and Importing a Routing Rules File

> Routing rules are initially defined in the \DICOM\Dict\Route.dic file, which is stored on the Routing Gateway. This file can be created and modified using any text-editing program.

> Routing rules take effect after Route.dic has been imported into a local table used by the Routing Gateway.

#### To create and import routing rules

> These steps assume that you have prepared your routing rules as described in the previous chapter.

1.  On the Routing Gateway, use a text editor to open x:\DICOM\Dict\Route.dic, where x is the name of the drive used by the Routing Gateway to store dictionary files.

> Note The first time routing rules are defined, Route.dic will need to be created. If you are modifying an existing file, it is recommended that you create a backup copy of the file.

2.  Enter your rules.
    - Route.dic must end with a line-feed.
    - To ensure proper termination of the last meaningful line, add the following comment lines after the last routing rule, such as:

> \# last update on \<date\>

> \# end of file

- If you are modifying existing rules, comment out the old rules instead of removing them. This will make it easier to revert to the original set of rules if it becomes necessary.
3.  Save the file into the directory noted in Step 1.
4.  On the Routing Gateway, stop the evaluation processor if it is running.
5.  Open a terminal window and log into the DICOM Gateway software.
6.  Select option 3-5 (Import Routing Rules).
7.  When you are prompted to build the Routing Table, enter Y.
8.  The file will be imported. If the import is successful, the following will be displayed. You will be prompted to return to the menu.

> Note If you are using load balancing, importing routing rules will cause internal counters that control load balancing to be reset. For more information, see page [<u>22</u>.](#_bookmark21)

> Note If multiple Routing Gateways are present, the steps for importing the modified rules file must be performed for all Routing Gateways, so all Gateways will use the same set of rules.

#### Verifying Imported Rules

1.  On the gateway where the rules reside, open a terminal window and log into the DICOM Gateway.
2.  Select option 3-10 (Display Routing Rules).
3.  The current set of routing rules will be displayed:
4.  After the rules are displayed and double-checked, press \<Enter\> to return to the menu.

#### Routing Rules and Multiple Routing Gateways

> If multiple evaluation processors need to be active (as could be the case at a consolidated site), each Routing Gateway can use its own local set of rules.

> However, it is usually better for all Routing Gateways to use a single set of rules stored in a shared directory. Using the same set of rules will make maintenance easier (changes to rules need to be made in only one Route.dic file, rather than several). This also allows each gateway in the pool to function as a backup for any other gateway.

## VistARad Configuration—Sending Sites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> For sites that will be *sending* routed images:

- The MAG VISTARAD SITE PARAMETERS File (#2006.69) needs to be edited.
- A site’s SITE CODE (IMAGING SITE PARAMETERS File (#2006.1)) must be set to a non-null value that will identify the sending site.

#### To set routing-related VistARad site parameters

1.  Open a terminal window and log into the VistA Hospital Information System.
2.  Access the VistARad System Options menu \[MAGJ MAIN\] and run the “E/E VistARad Site Parameters” option \[MAGJ VISTARAD SITE PARAMETERS\].
3.  Set the field shown in bold below to YES.

> <sup>1</sup> REMOTE LIST ONLY REMOTE CACHE? This field is obsolete, and can be ignored.

> <sup>2</sup> SITE SENDS TO REMOTE CACHE? Setting this field to YES turns on extra processing that is needed to manage routed exams properly. One result of setting this field to YES is the addition of the RC column to VistARad’s exam lists. The RC column is described on page [<u>59</u>.](#displaying-routed-exams)

> Note For information about other site parameters, refer to chapter 3 in the VistA Imaging Installation Guide.

4.  Use FileMan to check the value of your site’s SITE CODE field (#2006.1,.09). The value entered must not match any of the CacheLocationID values defined at receiving sites (see the next section for details).

## VistARad Configuration—Receiving Sites

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following steps must be performed for each VistARad workstation that will be used to display routed exams.

#### To set CacheLocationID in MAGJ.INI

1.  Log into the VistARad workstation as an administrator.
2.  Use Explorer or the Start \| Run menu option to open

> C:\Program Files\Vista\Imaging\MAG_VistaRad\MAGJ.INI.

3.  Locate the CacheLocationID line near the beginning of the file.
4.  For CacheLocationID, enter the destination name that contains local copies of routed images.
    - The value you enter must match an Imaging destination in the sending site’s

> NETWORK LOCATION File (#2005.2).

- Partial matching can be used to allow VistARad to access images from multiple Imaging destinations. For more information, see the next section.
5.  Save and close the file. After this change is made:
    - When a user logs into VistARad, the locally defined CacheLocationID is compared to the SITE CODE (IMAGING SITE PARAMETERS File (#2006.1)) of the site being logged into. If the two values are different, the VistARad software responds as if it were remote relative to the site being logged into, and enables logic for remote reading.
    - Each time an exam is opened, VistARad uses the value of CacheLocationID to find the corresponding entry in the NETWORK LOCATION File of the site being logged into. The storage location for that entry (which is presumably relative to VistARad), is checked for the exam in question. If the images are not present in

> that storage location, VistARad will retrieve the images across the WAN instead (i.e., from the primary image storage location).

#### Making Multiple Destinations Accessible to VistARad

> A VistARad workstation can be used to display images from multiple (local) destinations. This is possible because partial matching is used when the CacheLocationID is compared to the names of routing destinations defined in the NETWORK LOCATION File (#2005.2).

> For example, if a site is sending images to the destinations shown below, a VistARad workstation with its CacheLocationID set to DEMO would be able to access both destinations.

> DEMOMain, DEMOBackup

> Note that the partial matching used is based on leading characters. Continuing the above example, a destination named NewDEMO would not be treated as a match for workstations using Telerad as their CacheLocationID.

## Changes Affecting Routing System Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The following table lists situations that will require a change in routing configuration, and outlines the changes that will need to be made.

<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 59%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Routing System Change</strong></th>
<th><strong>Related Configuration Change</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Alteration of location, permissions, etc., of a Imaging destination folder</td>
<td>Update NETWORK LOCATION File (#2005.2) entry for the applicable destination.</td>
</tr>
<tr class="even">
<td>New destination, or name change of existing Imaging destination</td>
<td><ul>
<li><p>Update NETWORK LOCATION File entry for the applicable destination.</p></li>
<li><p>Update routing rules.</p></li>
<li><p>Stop and restart transmission processor (if one processor serves all destinations), or start a new instance of the transmission processor for the new destination.</p></li>
<li><p>Update VistARad workstation MAGJ.INI at receiving site.</p></li>
</ul></td>
</tr>
<tr class="odd">
<td>New Image Gateway / imaging modality</td>
<td><ul>
<li><p>Configure Image Gateway.</p></li>
<li><p>Review and update routing rules if needed.</p></li>
</ul></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 40%" />
<col style="width: 59%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Routing System Change</strong></th>
<th><strong>Related Configuration Change</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Change of radiology staff at sending or receiving site</td>
<td><ul>
<li><p>Review and update routing rules if needed.</p></li>
<li><p>Review NETWORK LOCATION File entry for destination and adjust if needed.</p></li>
<li><p>Determine if new staff members need on-demand routing privileges.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>Addition of new VistARad workstation</td>
<td>Update VistARad workstation MAGJ.INI.</td>
</tr>
<tr class="odd">
<td>Retirement of an existing destination</td>
<td>Remove destination reference from rules, stop the transmission processor for that destination, and disable/remove the destination definition parameters. See page <a href="#deactivating-destinations"><u>52</u></a> for details.</td>
</tr>
</tbody>
</table>

> This page is intentionally blank.

# Using Routing 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This chapter explains how to use the Routing Gateway. This chapter covers the following topics:

- [<u>Activating Routing</u>](#activating-routing)
- [<u>Maintaining Routing</u>](#maintaining-routing)
- [<u>Disabling Routing</u>](#disabling-routing)
- [<u>Routing Gateway Menu Options</u>](#routing-gateway-menu-options)
- [<u>Additional Routing Options</u>](#additional-routing-options)

> <span id="_bookmark44" class="anchor"></span>This chapter assumes that the Routing Gateway has been properly installed and configured.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>![](vista-imaging-dicom-gateway-routing-setup-and-user-guide/011.png)</p>
</blockquote></th>
<th><blockquote>
<p>US Federal regulations and VA internal policy prohibit unencrypted transmission of patient information outside the VA's intranet.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>![](vista-imaging-dicom-gateway-routing-setup-and-user-guide/012.png)</p>
</blockquote></td>
<td><blockquote>
<p>Routing can have a significant impact on network traffic. It is the responsibility of sites using routing to properly manage network demands related to routing. Before activating the routing software, notify your network administrator that there will be an increase (often a significant one) in network traffic to routing</p>
<p>destinations.</p>
</blockquote></td>
</tr>
</tbody>
</table>

## Activating Routing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The steps below explain how to start the processes that support automatic and on-demand routing.

#### Starting the evaluation processor

> Note If only on-demand routing is being used, the evaluation processor does not need to be started.

1.  Verify that Image Gateways in the routing system are processing images. If images are not being processed, no new entries will be added to the evaluation queue.
2.  Open a new terminal window and log into the gateway that you want to use to monitor the evaluation processor.
3.  Select option 3-3 (Start Evaluation Processor).
4.  Position and size the terminal window for subsequent monitoring. (No new information will be shown in the terminal window until the evaluation processor encounters entries in the evaluation queue.)

#### Starting a transmission processor (3-1) for Imaging destinations

1.  On a Routing Gateway, open a new terminal window and log into the DICOM Gateway software.
2.  Select option 3-1 (Start the Transmission Processor).
3.  A list of destinations will be displayed. To select all possible destinations, enter an asterisk (\*). To enter a partial list, follow the instructions at the prompt.
4.  The destinations you selected will be displayed. Enter a period when you are finished.
5.  Position and size the terminal window for subsequent monitoring.
6.  To start additional transmission processors, repeat steps 1 – 6 in a new terminal window.

#### Starting a transmission processor (2-8-2) for DICOM Storage SCP destinations

> Note It is recommended that this option (Transmit DICOM Images to a Storage SCP) be run on an Image Gateway, and not on a Routing Gateway (where the Start Transmission Processor process is running).

1.  Wait until there is an entry in the DICOM IMAGE OUTPUT File (#2006.574) for each destination that you want served by this instance of the Transmit DICOM processor. To do this, review the log file for the evaluation processor; see page [<u>51</u>](#using-routing-log-files) for details.
2.  On the Image Gateway that you want so use, open a new terminal window and log into the DICOM Gateway software.
3.  Select option 2-8-2 (Transmit DICOM Images to a Storage SCP).
4.  At the Ready to send DICOM Images from VistA? prompt, enter Y.

> Tip The “Transmit DICOM” processor can be stopped and restarted later to add any additional destinations that need to be serviced. (This logic does not apply to the transmission processor for Imaging destinations.)

5.  If entries from other locations are present, you will be prompted to select which entries you want to process.

> Note In this context, “location” is relative. For entries for automatically routed images, location is based on Instrument Name in instrument.dic. For images routed on-demand, location is based on the location specified in the configuration of the VistARad workstation or Image Gateway from which the image was routed.

> 7\. Position and size the terminal window for subsequent monitoring.

## Maintaining Routing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section provides a summary of maintenance tasks for a routing system and explains how to access routing-related log files.

#### Periodic Maintenance

> The following tasks should be performed periodically to control the size of the transmission queue and to detect potential routing problems.

<table>
<colgroup>
<col style="width: 56%" />
<col style="width: 22%" />
<col style="width: 21%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Task</strong></th>
<th><strong>Interval</strong></th>
<th><blockquote>
<p><strong>Menu Seq.</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Check terminal windows for evaluation and transmission processors.</td>
<td>2-3 times daily</td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Review log files for error messages.</td>
<td>Daily</td>
<td><blockquote>
<p>4-1-2</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Re-queue all failed entries in the transmission queue*.</td>
<td>As needed based on routing volume</td>
<td><blockquote>
<p>3-8</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Purge completed and expired entries in the transmission queue*.</td>
<td>Monthly</td>
<td><blockquote>
<p>3-7</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Remove obsolete entries from transmission queue*.</td>
<td>Monthly</td>
<td><blockquote>
<p>3-9</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Monitor available free space in Imaging destinations using the Background Processor’s Network Location Manager.</td>
<td>As needed</td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>Confirm access to routing destinations.</td>
<td>As needed</td>
<td><blockquote>
<p>N/A</p>
</blockquote></td>
</tr>
<tr class="even">
<td>Disable/delete entries for obsolete destinations.</td>
<td>As needed</td>
<td><blockquote>
<p>See page <a href="#deactivating-destinations"><u>52</u></a> for details.</p>
</blockquote></td>
</tr>
</tbody>
</table>

> \* Imaging destinations only.

#### Using Routing Log Files

> A log file is created for each evaluation and transmission processor session. Use these logs to review routing processes and to ensure that no errors have occurred.

> Note A DICOM Gateway retains the 20 most recently generated log files.

#### Displaying log files

1.  On the Gateway where the process in question was run from, open a terminal window and log into the DICOM Gateway software.
2.  Select option 4-1-2 (Display DICOM Message Log).
3.  At the Historical Log or New Activity? prompt, enter H.
4.  Enter the number of the log you want to view.
    - The transmission processor for Imaging destinations will have a description of

> Transmission Processor.

- The transmission processor for DICOM Storage SCPs will have a description of

> Send images to \<scp_name\>.

#### Deactivating Destinations

> When destinations are no longer needed, their definitions in VistA should be deactivated or removed. Deactivated destinations will not be available for either automatic or

> on-demand routing.

#### To deactivate an Imaging destination

> To clear an Imaging destination (such as a storage folder for remote VistARad workstations), do the following:

1.  On the Routing Gateway, use option 3-10 (Display Routing Rules) to ensure that all references to the destination in routing rules are either removed or commented out.
2.  On the Routing Gateway, make sure the destination is not being serviced by any transmission processors.
3.  Using the Background Processor (Edit \| Network Location Manager) or FileMan, set the destination OFFLINE, and clear the ROUTER field (set to NO if using FileMan).

> IMPORTANT Do not leave a destination (i.e., a Network Location intended for routing) online after clearing the ROUTER field. If you do so, the Background Processor may attempt to write images to the destination. For more information, see the *Background Processor User Manual*.

4.  After the retention period for the destination has expired, use option 3-7 (Purge completed and expired entries in the Transmission Queue) to clear any remaining entries for that destination from the queue.

#### To deactivate a DICOM Storage SCP Destinations

> To remove all DICOM Storage SCP destinations for a decommissioned gateway, use the “Clean Up Gateway (DICOM destinations)” option in the DICOM Menu Options menu \[MAGD DICOM MENU\] on VistA.

> To remove specific destinations:

1.  On the Routing Gateway, use option 3-10 (Display Routing Rules) to ensure that all references to the destination in routing rules are either removed or commented out.
2.  On the Image Gateway, make sure that the destination in question is not being served by any transmission processors (2-8-2).
3.  On the Image Gateway, open SCU_List.dic, and ensure that any references to the destination are removed or commented out.
4.  Load and update SCU_List.dic on all Image Gateways using option 4-2-6 (Update SCU_LIST.DIC).
5.  Ensure that the destinations have been removed by checking the DICOM TRANSMIT DESTINATION File (#2006.587) on VistA, or by logging into VistARad and checking the contents of the Route To box (be sure to start a new session for this).
6.  If the entry is not cleared, use FileMan to manually remove the entries from the

> DICOM TRANSMIT DESTINATION File.

> Note The destination could appear multiple times in the file, one entry for each gateway. Delete all entries for that destination. Note that this process could take several minutes to complete.

## Disabling Routing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Short-Term Routing Shutdown

> If routing needs to be disabled for a short period of time, the easiest thing to do is to stop all transmission processors. When this is done, images will still be evaluated and queued, but they will not be transmitted until the transmission processors are restarted.

> Before restarting routing:

- Use option 3-9 (Remove Obsolete Entries from Transmission Queue) to remove any entries for Imaging destinations.
- Optionally, use option 2-8-4 ((Re)Initialize Image Transmission Queue) to clear *all* entries for DICOM Storage SCP destinations (there is no way to selectively clear entries).

#### Long-Term Routing Shutdown

> If routing needs to be disabled for an extended period, perform the following:

- Stop the evaluation processor.
- Stop all transmission processors.
- Alter the configuration files for all Image Gateways to indicate that they are *not* part of a routing system (see page [<u>35</u>](#defining-dicom-storage-scp-destinations) for more information).
- If you do not want images that are already queued for transmission to be routed when routing is re-enabled, remove entries from all transmission queues.
- For Imaging destinations, wait until the retention period is expired, then use option 3-7 (Purge completed and expired entries in the Transmission Queue).
- For DICOM Storage SCPs, run option 2-8-4 ((Re)Initialize Image Transmission Queue). Because there is no retention setting, this can be run immediately.

## Routing Gateway Menu Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section describes the menu options associated with the Routing Gateway. Routing Gateway menu options are accessed by entering 3: Routing Gateway from the DICOM Gateway main menu.

#### Start the Transmission Processor (3-1)

> Use this option to start an instance of the transmission processor to service one or more Imaging destinations.

> Note As the transmission processor sends exams to Imaging destinations, it will map and un-map certain drives. For more information, see page [<u>63</u>.](#cant-start-evaluation-processorrule-evaluator-is-already-running)

> If a single transmission processor cannot manage a site’s routing workload, additional transmission processors, each sending images to a subset of destinations, can be started using this option. For detailed steps, see page [<u>48</u>.](#_bookmark44)

> Note: At sites where routing is used, it is recommended that the Transmit DICOM Images to a Storage SCP process be run on an Image Gateway, and not on a Routing Gateway where the Start Transmission Processor process is running.

#### Stop the Transmission Processor (3-2)

> Use this option to stop all running instances of transmission processors for Imaging destinations.

> Note Using this option can result in an incomplete exam being sent to a destination. If this occurs, the remainder of the exam will be transmitted when a transmission processor is re-started, provided that the applicable entries are still present in the transmission queue.

#### Start the Evaluation Processor (3-3)

> When this option is executed, an instance of the evaluation processor is started. Note that the evaluation processor is run on VistA, not on the Routing Gateway itself. However,

> the state of the evaluation processor can be monitored by leaving the appropriate terminal window open on the Routing Gateway.

> After it is started, the evaluation processor will examine routing-specific entries in the evaluation queue (a subset of the IMAGE BACKGROUND QUEUE File (#2006.03)). This file is populated by Image Gateways (provided that Image Gateways are configured as part of a routing system).

> The evaluation processor uses the evaluation queue and routing rules to determine which images are automatically routed. Entries for images that should be routed are added to the appropriate transmission queue. Entries for images that should not be automatically routed are deleted.

> Typically, only a single instance of the evaluation processor is needed for all automatic routing.

> For consolidated sites, an instance of the evaluation processor should be started for each division. (In this situation, a division is also called “place” and equates to an entry in the IMAGING SITE PARAMETERS File (#2006.1).) An evaluation processor uses the set of rules defined on the gateway that the processor was started on.

#### Stop the Evaluation Processor (3-4)

> When this option is executed, a flag is set that the evaluation processor will recognize as “stop evaluating.” The evaluation processor checks this flag after analyzing each image file against the routing rules.

#### Import Routing Rules (3-5)

> When this option is executed, the rules in \DICOM\Dict\Route.dic will be loaded into the Routing Gateway’s local database. For detailed steps about importing routing rules, see page [<u>41</u>.](#importing-routing-rules-route.dic)

> Be sure to stop the evaluation processor before importing new or edited routing rules.

#### Purge all completed entries in the Transmission Queue (3-6)

> Use this option to reduce the size of the transmission queue. Executing this option will remove entries for files that have been transmitted successfully.

> Note If this option is used, routed images will be “orphaned” at an Imaging destination rather than being deleted automatically (after the defined retention period); the images will remain until deleted manually.

> To purge completed entries without orphaning routed images, use the option described in the following section.

#### Purge completed and expired entries in the Transmission Queue (3-7)

> Use this option to control the size of the transmission queue for Imaging destinations. Executing this option will remove entries if both of the following conditions are met:

- The status of the entry indicates that an image file has been transmitted successfully.
- The entry is older than the RETENTION PERIOD (number of days) for the applicable destination.

> This option should be run once a month as part of a Routing Gateway’s periodic maintenance cycle.

#### Re-Queue all failed entries in the Transmission Queue (3-8)

> Use this option to try to re-send routed images that could not be sent within the number of attempts specified for that Imaging destination.

> This option should be run periodically as part of a Routing Gateway’s maintenance cycle. Sites that route a large number of exams, or that route high priority exams, should run this option daily. Sites that route a lower volume of exams may only need to run this option once a week.

#### Remove obsolete entries from Transmission Queue (3-9)

> Use this option when there is a backlog of outdated entries in the transmission queue for Imaging destinations. When this option is executed, you will be prompted to enter a cutoff date (the date can be entered using FileMan conventions). After the date is entered, all unprocessed queue entries older than the specified date will be removed.

> This option should be run once a month as part of a Routing Gateway’s periodic maintenance cycle.

#### Display Routing Rules (3-10)

> Use this option to display the current set of routing rules. This option is useful immediately after using option 5 to import a new set of rules.

> Note When this command is used to display a list of rules, the “if” command is used for conditions. In an actual rule, either if or when can be used to indicate a list of conditions.

## Additional Routing Options

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> In addition to the Routing Gateway, there are some routing-related features that reside on the DICOM Image Gateway and the VistARad workstation software.

> The following routing-related options are present on the DICOM Image Gateway Menu:

> 2-8-1 Select DICOM Images for Transmission 2-8-2 Transmit DICOM Images to a Storage SCP

> 2-8-3 Stop Image Transmission Queue Processor 2-8-4 (Re)initialize Image Transmission Queue

> These options are referenced where appropriate in this document. For detailed information about these options, see the *VistA Imaging DICOM Gateway User Guide*.

> Routing-related features available in VistARad are described in detail in the next chapter.

# Using VistARad in a Routing System 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This chapter explains how to use the VistARad diagnostic workstation software at sites that are part of a routing system. This chapter covers the following topics:

- [<u>Displaying Routed Exams</u>](#displaying-routed-exams)
- [<u>VistARad and On-Demand Routing</u>](#vistarad-and-on-demand-routing)

## Displaying Routed Exams

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When VistARad is configured to be used with routing, an additional column is displayed in the Manager’s exam lists. This column, the RC (remote cache) column, indicates which Imaging destinations, if any, an exam has been routed to.

> ![](vista-imaging-dicom-gateway-routing-setup-and-user-guide/013.png)Remote Cache Indicator

> Note that the RC column only indicates Imaging destinations specified in the NETWORK LOCATION File (#2005.2). The RC column does not indicate if an exam has been routed to a DICOM Storage SCP.

> When VistARad is being used for remote reading, exam lists are automatically filtered to show only those exams that are stored locally relative to the VistARad workstation (in the example above, the Remote Read Filter is cleared).

#### To display a routed exam

1.  Using VistARad, log into the site or division that the routed exam was sent from.
2.  Use an exam list to locate the routed exam you want to open. By default, only exams routed to you are shown.
    - If the Remote Read Filter button is not present at all, there are no routed exams in local storage. Even if you have the proper routing security keys, this button will display only if routed exams are available.
    - Exams routed to VistARad workstations are automatically deleted after a certain number of days. If a routed exam was deleted before you had a chance to review or interpret it, contact your Imaging Coordinator to have the exam re-routed or to have the retention period increased.
    - You can view all exams (routed and non-routed) by clearing the checkbox in the Remote Read Filter area near the top of the Manager window. However, any non-routed exams, if opened, will take longer to load because the images are not stored locally.
3.  Double-click the exam, or select the exam and click Open. A routed exam can be locked and marked as interpreted in the same manner as any other exam.

## VistARad and On-Demand Routing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> For on-demand routing to function:

- A VistARad user must be logged into a site that has a Routing Gateway.
- At the site being logged into, the VistA Imaging host, the Routing Gateway, and storage folders must be set up as described in this manual.
- A transmission processor must be servicing the applicable destinations.
- The user performing on-demand routing must have the MAGJ DEMAND ROUTE

> security key or the MAGJ DEMAND ROUTE DICOM security key.

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 91%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>![](vista-imaging-dicom-gateway-routing-setup-and-user-guide/014.png)</p>
</blockquote></th>
<th><blockquote>
<p>US Federal regulations and VA internal policy prohibit unencrypted transmission of patient information outside the VA's intranet.</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>![](vista-imaging-dicom-gateway-routing-setup-and-user-guide/015.png)</p>
</blockquote></td>
<td><blockquote>
<p>On-demand routing can have a significant impact on network traffic. It is the responsibility of sites using routing to properly manage network demands</p>
<p>related to routing.</p>
</blockquote></td>
</tr>
</tbody>
</table>

#### Using On-Demand Routing

> On-demand routing lets you send copies of exams to existing routing destinations. Use on-demand routing when you need to route exams that do not satisfy existing routing rules, or where automatic routing is not used.

> Note If you are frequently using on-demand routing for the same sorts of exams, contact your Imaging Coordinator and request that a change or addition be made to the rules used for automatic routing.

> Note You can also route exams on-demand using a DICOM gateway using option 2-8-1 (Select DICOM Images for Transmission). See the *DICOM User Guide* for details.

> Any exam that appears in a VistARad exam list can be routed on-demand. However, newly acquired exams should not be routed until they have a status of “examined” in VistARad’s exam lists (indicating that they have been QCed or case edited by a technologist).

#### To use on-demand routing

1.  Using VistARad, log into a site that has a Routing Gateway.

> Note If you have access to more than one division, log into the division where the exams to be routed were acquired.

2.  Use the exam lists in the Manager window to select the exams you want to send.
3.  Click the Route Exams button, located in the upper right corner of the exam list.

> Note If the Route Exams button is not present, your user account does not have any of the security keys for on-demand routing assigned.

4.  When the Route Request dialog opens, make sure all the exams you selected are shown.

> Note If a selected exam is not “online” (not available in short-term storage), a message will appear at the bottom of the Route Request window indicating that exam has been requested from the jukebox (long-term storage). Once the exam is available in short-term storage, you can select it for on-demand routing.

![](vista-imaging-dicom-gateway-routing-setup-and-user-guide/016.png)

5.  For each exam, click the Route To field to select where you want to send the exam.
    - In the Route To field, the first destinations listed are Imaging destinations (such as remote VistARad workstations).
    - If there are any DICOM Storage SCP destinations available (such as film printers), they will appear at the bottom of the Route To list and will be preceded by dcm.
    - Use the Default Route To box near the bottom of the dialog to choose a single destination for all listed exams.
6.  For each exam, use the Priority field to select the priority used to send the exam.
    - Use the Default Priority box near the bottom of the dialog to choose a single priority for all listed exams.
    - The priority assigned to exams for on-demand routing is not related to the exam priority indicated in VistARad’s exam lists.
7.  Confirm that the settings in the Route Request dialog are correct.
    - You can choose not to route a listed exam by selecting the Route To box for that exam and choosing the \[Do Not Route\] option.
    - You can click Cancel to close the Route Request dialog without routing any exams.
8.  Click OK to route the exams.
9.  When the exam is routed, the RC column entry for that exam will show the name of the receiving site. (Note that this only applies to exams routed to Imaging destinations. The RC column will not indicate if an exam has been routed to a DICOM Storage SCP.)

# Troubleshooting Routing 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This chapter covers the following topics:

- [<u>Troubleshooting FAQs</u>](#troubleshooting-faqs)
- [<u>Routing Support</u>](#routing-support)

## Troubleshooting FAQs

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The table below outlines some commonly encountered routing issues. Refer to the indicated page for details.

| Problem                                                                    | See…                                                                                       |
|--------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------|
| Can’t start evaluation processor—“rule evaluator is already running”           | [<u>below</u>](#cant-start-evaluation-processorrule-evaluator-is-already-running)              |
| Can’t select an Imaging destination for the transmission processor (3-1)       | page [<u>64</u>](#cant-select-an-imaging-destination-for-the-transmission-processor-3-1)       |
| Images not arriving at a destination                                           | page [<u>63</u>](#cant-start-evaluation-processorrule-evaluator-is-already-running)            |
| Routed images slow to arrive at destination                                    | page [<u>64</u>](#routed-images-slow-to-arrive-at-destination)                                 |
| Drive letters for Imaging destinations change intermittently                   | page [<u>64</u>](#routed-images-slow-to-arrive-at-destination)                                 |
| Only part of an exam has been routed                                           | page [<u>65</u>](#only-part-of-an-exam-has-been-routed)                                        |
| In VistARad, some images in a routed exam take a long time to open             | page [<u>65</u>](#in-vistarad-some-images-in-a-routed-exam-take-a-long-time-to-open)           |
| In VistARad, the RC column does not show all destinations                      | page [<u>66</u>](#in-vistarad-the-rc-column-does-not-show-all-destinations)                    |
| In VistARad, ”retired” destinations are still selectable for on-demand routing | page [<u>66</u>](#in-vistarad-retired-destinations-are-still-selectable-for-on-demand-routing) |
| An exam was routed more than once to the same destination                      | page [<u>66</u>](#an-exam-was-routed-more-than-once-to-the-same-destination)                   |
| Images cannot be purged/path could not be found                                | page [<u>66</u>](#images-cannot-be-purgedpath-could-not-be-found)                              |

#### Can’t start evaluation processor—“rule evaluator is already running”

> If a “rule evaluator is already running” message is displayed when you try to start the evaluation processor, run option 3-4 (Stop the Evaluation Processor), then re-try option 3-3 (Start the Evaluation Processor).

> Tip The evaluation processor is started from a Routing Gateway, but actually is executed on VistA. It will not be apparent that the evaluation processor is actually running if it was started from a different gateway, or if the terminal window showing evaluation processor activity is closed.

> If the message persists, there may be a lock issue on VistA that is preventing the process from starting. Check for lock on ^MAGDICOM(2006.563,1,"EVAL",location) where location is the internal entry number in File \#4 for the location of the DICOM Gateway. Contact Clinical Product Support if assistance is needed.

#### Can’t select an Imaging destination for the transmission processor (3-1)

> When option 3-1 (Start the Transmission Processor) is run, a list of available Imaging destinations is displayed. If a destination is missing, first determine if any other instances of the transmission processor are running, and if so, determine if they are already servicing the destination in question.

> If the destination isn’t already selected, there may be a lock issue on VistA that is preventing the destination from being selected. Check for lock on ^MAGQUEUE (“ROUTE”,location,destination) where location is the internal entry number in File \#4 for the location of the DICOM Gateway, and destination is the internal entry number in File \#2005.2 for the destination. Contact Clinical Product Support if assistance is needed for this.

#### Images not arriving at a destination

> If this is the first time routing is being used, verify that all configuration steps have been completed. (Configuration checklists are available in [<u>Appendix A.</u>](#appendix-a-routing-worksheets))

> If routing has been in use and the destination has worked in the past:

1.  Verify that the destination is online, that it is accessible, and that it has sufficient storage space available. If the destination is an Imaging destination, use the steps for testing folders on page [<u>28</u>.](#_bookmark26)
2.  Ensure that the images in question have been processed by the Image Gateways.
3.  If the destination is an Imaging destination, try to re-send images by running option 3-8 (Re-Queue all failed entries in the Transmission Queue). For details, see page [<u>57</u>.](#re-queue-all-failed-entries-in-the-transmission-queue-3-8)
4.  Review the routing log files to determine if the images were transmitted successfully. (If you have just used the re-queue failed entries option, wait 15-20 minutes before opening the log files.) See page [<u>51</u>](#using-routing-log-files) for steps on accessing log files.
5.  Check the routing rules for any recent changes by running option 3-10 (Display Routing Rules). See page [<u>57</u>](#display-routing-rules-3-10) for steps on reviewing routing rules.

#### Routed images slow to arrive at destination

> Given a T1 connection and light to moderate network traffic, the first images in a routed exam will typically begin arriving at a destination within minutes. However, any of the following can impact the delivery of routed exams:

- A backlog of images at the Image Gateway, which is responsible for adding entries to the evaluation queue.
- A backlog of entries in the transmission queues. If numerous large exams are flagged for routing in a brief period of time, there will be a delay while all the images in the exam are transmitted. In situations where multiple destinations are being used, additional transmission processors may be used to alleviate delays.
- Problems connecting to destinations. For Imaging destinations, the routing software will attempt to re-connect or retransmit the number of times specified for each destination in the NETWORK LOCATION File (#2005.2). For DICOM Storage SCP destinations, retry attempts are part of the DICOM transmission protocol. Failed connection or transmission attempts are logged by the Routing Gateway.
- The routing priority of a particular exam. For more information, see page [<u>66</u>.](#_bookmark65)

#### Drive letters for Imaging destinations change intermittently

> For each Imaging destination that it sends exams to, the transmission processor (3-1) will map a drive using the following progression of drive letters: Q – Z, then G – P. If a drive letter (Q, for example) is not available, it will move to the next letter (R, for example) and so on. When all entries for a particular destination have been processed, the applicable drive is unmapped.

> This logic is not used for DICOM Storage SCP destinations.

#### Only part of an exam has been routed

> The Routing Gateway transmits data on an image-by-image basis. If a transmission processor is disabled when an exam is partially transmitted, the exam is usually treated as “unrouted” until a transmission processor is re-started for that destination. If the proper entries are still in the appropriate transmission queue, the rest of the exam will be sent.

> In some situations, such as the presence of multiple Image Gateways or the use of

> on-demand routing, images from one exam will interrupt the transmission of images of an exam that is partially routed. This can occur because entries are added to the rule evaluation and transmission queues for each image, rather than for each exam. Usually, this behavior is invisible to the user.

#### In VistARad, some images in a routed exam take a long time to open

> If a partially routed exam is opened from VistARad, the VistARad software will first attempt to retrieve images from the local storage location identified in the MAGJ.INI file for that workstation. Images not found in local storage will be retrieved from their originating site.

> An exam may be partially routed because it has been interrupted by the transmission of a higher-priority exam. If this has happened, the rest of the images in the interrupted exam will be routed after routing of the higher-priority exam is complete.

> Also, the RC (Remote Cache) column may show that the exam has been routed before all images have been received. This can occur because the value in the RC column

> is dependent on a specific "representative image" in the routed exam. A "representative image" is the last image processed by an Image Gateway for a given exam. Typically, the representative image is also the last image in an exam's clinical sequence. However, images are processed on a first-in, first-out basis. If images are sent to the Image Gateways in an order other than the expected clinical sequence, that is also the order in which the images will be routed.

#### In VistARad, the RC column does not show all destinations

> <span id="_bookmark65" class="anchor"></span>The RC column in VistARad's exam lists will report the names of Imaging destinations. However, destinations that are DICOM Storage SCPs are considered “outside” the VistA system and their names are not reported in the RC column.

#### In VistARad, ‘retired’ destinations are still selectable for on-demand routing

> At sites where multiple versions of SCU_List.dic are used, DICOM Storage SCP destinations (shown with ‘dcm’ prefixes in VistARad) may linger after being removed from SCU_List.dic. See page [<u>52</u>](#deactivating-destinations) for information about disabling a destination.

#### An exam was routed more than once to the same destination

> For Imaging destinations, the transmission processor (3-1) will check to see if the image to be routed is already present at the destination. If a duplicate of the image is found, the transmission processor removes the redundant entry from the transmission queue, and moves on to the next entry in the queue.

> For DICOM Storage SCP destinations, image management and duplicate checking is the responsibility of the destination system.

#### Images cannot be purged/path could not be found

> Images sent to DICOM Storage SCP destinations are not purged.

> Images sent to Imaging destinations (such as a remote VistARad workstation) are purged after the retention period specified for that destination in the NETWORK LOCATION File (#2005.2).

> If the purge process for an Imaging destination fails, “Path cannot be found” messages will appear in the transmission processor (3-1) log files. The purge process will fail if the storage location specified for the destination is powered down or otherwise inaccessible.

> The purge process will also fail if the files that the process is attempting to delete are no longer present. This can happen if the files were deleted manually, or if the hardware or Physical Reference value in the NETWORK LOCATION File has been changed. To address the problem, the original directory structure needs to be recreated to allow the purge process to function normally. For assistance doing this, contact Clinical Product Support.

## Routing Support

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If additional assistance is needed, contact your Imaging Coordinator or local support staff. If the problem cannot be resolved locally, open a Remedy ticket, or contact CPS (Clinical Product Support) at 1-888-596-4357.

> Urgent after-hours service requests can be directed to the Expertise Center at 1-800-299-7282.

> This page is intentionally blank.

# Appendix A: Routing Worksheets 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This appendix contains worksheets that can be used while setting up a routing system. They can also be used for record-keeping purposes. The following worksheets are provided:

> [<u>Imaging Destination Worksheet</u>](#imaging-destination-worksheet)

> [<u>DICOM Storage SCP Destination Worksheet</u>](#dicom-storage-scp-destination-worksheet) [<u>Routing Rule Definition Worksheet</u>](#routing-rule-definition-worksheet)

> [<u>Routing Setup Checklist</u>](#routing-setup-checklist)

## Imaging Destination Worksheet

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> *Use this worksheet to record information about a specific Imaging destination. A sample Network Location File definition is provided on the next page.*

> Destination name[<sup>1</sup>](#appendix-a-routing-worksheets)

> Site served by destination

> General purpose of this destination

> Alternate/backup destination

> Storage folder name

> Destination computer/share name[<sup>2</sup>](#appendix-a-routing-worksheets)

> User name/password for destination

> Associated user group (if any) <sup>2</sup>

> File types transmitted to destination (circle those that apply) [<sup>3</sup>](#appendix-a-routing-worksheets)

> Abstract / Full / Text / Big

> Retention period? (in days) <sup>3</sup>

> <sup>1</sup> Specified in the .01 field in the NETWORK LOCATION file. Referenced in routing rules (Route.dic), and in the CacheLocationID parameter for VistARad workstations at receiving sites.

> <sup>2</sup> Specified by receiving sites when creating a storage folder. Referenced sending site’s NETWORK LOCATION file.

> <sup>3</sup> Specified in sending site’s NETWORK LOCATION file.

#### NETWORK LOCATION File Sample

> *For detailed information about specific fields, see page* [<u>31</u>*.*](#_bookmark27)

## DICOM Storage SCP Destination Worksheet

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> *Use this worksheet to record information about a specific DICOM Storage SCP destination.*

> Destination name[<sup>1</sup>](#network-location-file-sample)

> Site served by destination

> General purpose of this destination

> Alternate/backup destination

> Calling AE Title

> Called AE Title

> IP address/hostname

> Socket/port

> Presentation Context / Transfer Syntax (list all used)

> <sup>1</sup> Specified as the Application in the SCU_List.dic file, and referenced in routing rules (Route.dic).

#### DICOM Storage SCP Destination Sample

> *For detailed information about specific fields, see page [<u>36</u>.](#field-definitions)*

> \# User Application List \# Format:

> \# line 1:App Name\|Called AE\|Calling AE\|Destination IP Address\|Socket \# line 2:\|Presentation Context Name\|Transfer Syntax Name

> \# line 3:\|\|Transfer Syntax Name (if there are more than one) \#

> MERGE EFILM\|VistA_Storage\|VistA_Send_Image\|111.222.33.44\|4006

> \|Modality Worklist Information Model - FIND\|Implicit VR Little Endian

> \|Verification SOP Class\|Implicit VR Little Endian

## Routing Rule Definition Worksheet

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p><strong>Rule Request</strong> <em>(to be completed by Radiology staff or supervisor)</em></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p>Identify the purpose of the rule (circle one):</p>
</blockquote>
<ol type="a">
<li><p>Routine workload sharing</p></li>
<li><blockquote>
<p>Rapid access for clinic / facility <strong>c</strong> After-hours or holiday coverage <strong>d</strong> Second opinions / consults</p>
</blockquote></li>
</ol>
<ol start="5" type="a">
<li><p>Transfer of images to a non-local specialist / support for a new modality or imaging type</p></li>
<li><p>Other</p></li>
</ol></td>
</tr>
<tr class="even">
<td><blockquote>
<p>List each destination that this rule will serve:</p>
<p><strong>a d b e</strong></p>
<p><strong>c</strong></p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Will prior exams be included with this rule? (circle one): Yes No</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Will prior exams be included with this rule? (circle one): Yes No</p>
</blockquote></td>
</tr>
<tr class="odd">
<td><blockquote>
<p>Will all exams for this rule be sent to all listed destinations (circle one): Yes No</p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>If the answer to the above is <strong>NO</strong>, specify the % of exams each destination should receive (total must = 100%):</p>
<p><strong>a</strong> % <strong>d</strong> %</p>
<p><strong>b</strong> % <strong>e</strong> %</p>
<p><strong>c</strong> % local (not routed) %</p>
</blockquote></td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><blockquote>
<p>List conditions that will trigger the execution of the rule (fill in all that apply):</p>
</blockquote>
<ol type="a">
<li><p>Exam modality of:</p></li>
<li><p>Off hours/holiday coverage (specify hours/days)</p></li>
<li><p>Other</p></li>
</ol></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><blockquote>
<p><strong>Rule Impact/Review</strong> <em>(to be completed by Imaging Coordinator)</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td>Estimated amount of storage needed at each destination for this rule:</td>
</tr>
<tr class="odd">
<td>Bandwidth available between sending and receiving sites:</td>
</tr>
<tr class="even">
<td>Total number of exams expected to be transmitted per month:</td>
</tr>
<tr class="odd">
<td>Rule adheres to routing policies established by sending site (circle one): Yes No</td>
</tr>
<tr class="even">
<td>Rule adheres to routing policies established by receiving site (circle one): Yes No</td>
</tr>
<tr class="odd">
<td><blockquote>
<p><strong>Rule Implementation</strong> <em>(to be completed by staff responsible for Routing G/W)</em></p>
</blockquote></td>
</tr>
<tr class="even">
<td><blockquote>
<p>Rule as entered into the Route.dic file: (sample rules listed below)</p>
</blockquote></td>
</tr>
<tr class="odd">
<td></td>
</tr>
<tr class="even">
<td></td>
</tr>
<tr class="odd">
<td></td>
</tr>
<tr class="even">
<td></td>
</tr>
<tr class="odd">
<td>Route.dic imported to Routing Gateway (circle one): Yes No</td>
</tr>
<tr class="even">
<td><blockquote>
<p>Rule tested and found to be functional (circle one): Yes No</p>
</blockquote>
<p>Date</p></td>
</tr>
</tbody>
</table>

#### Sample Rules

> The following sample rules use the fictional destinations listed below: Imaging destinations (entered in the NETWORK LOCATION File (#2005.2))

> Archive Contractor1 Contractor2 Contractor3 ContractingReader LocalJukeBox LogBook

> DICOM Storage SCP destinations (entered in the DICOM TRANSMIT DESTINATION

> File (#2005.587) via SCU_List.dic):

> E-FilmApplication LaserShare

#### Example \#1:

> \# auto-route all images from a specific modality to a

> \# contractor who reads this type of images, using standard \# copy for transmission

> Send("ContractingReader") When MODALITY="CT"

#### Example \#2:

> \# auto-route all images to an archive, using standard copy \# for transmission

> Send("Archive")

> When MODALITY="\*"

#### Example \#3:

> \# auto-route all images from a remote site back to local \# storage at that site, using standard copy for

> \# transmission

> Send("LocalJukeBox") When MODALITY="\*"

> SOURCE="StElseWhere"

#### Example \#4:

> \# auto-route all important studies to an internal

> \# workstation, using standard copy for transmission Send("LogBook")

#### Example \#5:

> When MODALITY="\*" URGENCY="STAT"

> \# auto-route all images from a specific modality to three \# contractors, balancing the load, so that each contract \# receives a pre-determined fraction of the studies and

> \# leaving a pre-determined fraction for interpretation by \# local staff, using standard copy for transmission

> Balance("Contractor1"=20%, "Contractor2"=40%, "Contractor3"=20%, \<LOCAL\>=20%)

> When MODALITY="XA"

#### Example \#6:

> \# auto-route all images from a specific modality to a

> \# contractor who reads this type of images, using standard \# copy for transmission and giving these transmissions a

> \# high priority

> Send("ContractingReader") When MODALITY="XA"

> Priority High

#### Example \#7:

> \# auto-route all images from a specific modality to a

> \# printer, using the DICOM protocol for transmission and \# giving these transmissions a low priority

> Send("LaserShare") When MODALITY="CT"

> Priority Low

#### Example \#8:

> \# auto-route all images from a specific modality to a DICOM \# repository, using the DICOM protocol for transmission and \# including images from prior studies

> Send("E-FilmApplication") When MODALITY="CT"

> PriorStudy Yes

## Routing Setup Checklist

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Imaging Destination Setup

> a User name and password available for each destination?

2.  Folders created and shared for each destination?
3.  Ability to access and write to each storage folder verified?
4.  Network location entry defined for each destination?
5.  VistARad site parameters set up at sending site?
6.  CacheLocationID set on workstations at receiving sites?

#### DICOM Storage SCP Destination Setup

> a Destination information added to SCU_List.dic?

2.  SCU_List.dic updated on DICOM Gateway?
3.  Destination application accessible?

#### DICOM Gateway Setup

> a Image Gateways configured properly?

> b Routing Gateway configured properly?

#### Routing Rule Setup

> a Rules defined in Route.dic?

> b Route.dic imported successfully?

#### Routing Activation

> a Image Gateways processing images?

2.  Routing Gateway evaluation processor activated?
3.  Transmission processor(s) for all destinations activated?
4.  Images routed successfully?
5.  Images at receiving site purged at end of retention period (Imaging dests. only)

# Appendix B: Using MAG_Decompressor 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section explains how to install and configure the Automatic Decompression Service (MAG_Decompressor).

> MAG_Decompressor can be installed on a system serving as an Imaging destination (such as a VistARad workstation). MAG_Decompressor cannot be used on DICOM Storage SCP destinations, or on a DICOM Gateway.

> Once it is configured, MAG_Decompressor runs in the background and will de-compress routed images as they are received by the destination system.

> This service does not need to be installed on systems that receive only uncompressed routed images.

## Licensing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> You will need to purchase an Aware JPEG2000 Toolkit client license for each system that is receiving routed images. Even if that system serves as a centralized temporary storage for multiple workstations, only a single client license is needed. For each system (DICOM Gateway) that is transmitting compressed routed images, you will need to purchase an Aware JPEG2000 server license. For more information, contact Clinical Product Support.

## Setup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Distribution

> The decompression software installation file, MAG_Decompressor_Setup.exe, is distributed with the DICOM Gateway software, and is also available at the Imaging FTP site.

#### Installation

1.  As an administrator, log onto the system that will be receiving compressed images.
2.  Copy MAG_Decompressor_Setup.exe to a local location and double-click the file.
3.  As the InstallShield script is executed, click on Next, OK and Finish as appropriate. The software will be installed into its own folder under C:\Program Files\VistA Imaging.
4.  Use Windows Explorer to create a folder named \<drive\>\Complog, where

> \<drive\> is the drive were routed images are stored.

5.  Make sure the administrative user has write permission to this folder. (Right-click the new folder, click Properties, click the Security tab, and check the permissions list on the tab.)
6.  In the new \Complog folder, create a new file named log.txt. This “seed file” will become the decompression log file once the decompression service is started.
7.  Open the Environment Variables dialog as follows:
    1.  Right-click My Computer, and choose Properties.
    2.  In the System Properties dialog, click the Advanced tab, then click Environment Variables.
8.  For each variable below, select the variable, click Edit, then change the value as follows:

> DECOMP_LOG_FSPEC

> Enter the full path and file name of the log file created in steps 6 and 7 above. decompression service log file.

> DECOMP_LOG_FILE_MBYTES

> Set the maximum size permitted for the decompression service log file. The recommended value is 10MB. When the stated limit is reached, a new instance of the log file will be generated. (The 10 most recent files are retained).

> DECOMP_WATCH_DIR

> Specify the root folder to be monitored by the decompression service (the folder that is receiving compressed images).

> DECOMP_DELAY_MS

> Optionally, you can set the number of milliseconds that the service will wait after detecting a compressed file before beginning the decompression process. The default of 50ms is usually sufficient.

9.  Click OK to step back through the various dialogs and to apply your changes.
10. Activate MAG_Decompressor as follows
    1.  Open a command line window (click Start \| Run, then enter cmd), then switch to the MAG_Decompressor installation folder:

> cd \Program Files\VistA\Imaging\MAG_Decompressor \<Enter\>

2.  Enter dir at the prompt and verify that the files shown below are present.

> 04/13/2005 07:16a 856,064 awj2k.dll

> 05/02/2005 08:39a 53,248 MAG_Decompressor.exe

> Note If the DLL file is not present, contact the Imaging Group for information about acquiring a toolkit license. The decompression software will not work without the DLL file.

3.  Enter the following command to activate the program (The command will complete without any warning or error messages.)

> Mag_Decompressor –install \<Enter\>

4.  Close the command window.
11. Reboot the system.

#### Service Startup

> On the system receiving routed images, start the decompression service as follows:

1.  In the Control Panel, double-click Administrative Tools, then double-click Services.
2.  In the window that opens, locate the entry for the MAG J2K Decompressor Service.
3.  Right-click on the entry and select <u>Start</u>. Wait until the status display shows that the service is started.
4.  Right-click again on the entry and select Properties.
5.  In the Properties window, select Automatic as the startup type, then click OK.
6.  Verify that the status display shows that the service is Automatic, and close all remaining Control Panel windows.

> After activation, compressed routed files will be automatically decompressed as they are received.

## Logging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The decompression software will run automatically when needed. If problems are encountered, review the log files generated by the MAG_Decompressor software.

> Log files are stored in the location specified in the DECOMP_LOG_FSPEC system variable. The 10 most recently generated log files are retained.

#### Sample log entry:

> Selected log file error codes:

> 1..999 Aware JPEG2000 library errors 1000... Application errors:

> 2006: EIFILEREMOVE-- input file remove error (access violation) 3000: EOFILEEXISTS-- output file already exists

> 3001: EOFILEOPEN-- error while opening the output file

> 3003: EOFILEWRITE-- problem attempting to write the data to the output file 3004: EOFILERENAME-- error while renaming output file from .tmp to .\<ext\>

# Glossary 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> automatic routing The automatic delivery of selected images to one or more destinations. Automatic routing functions are managed using the Routing Gateway.
> destination A recipient of routed images. Destinations can be Imaging destinations, such as VistARad workstations, or DICOM Storage SCPs, such as a film printer or external PACS.
> DICOM IMAGE OUTPUT File (#2006.574) The FileMan file where transmission queue entries for DICOM Storage SCP destinations are stored. Entries can be added to this file by the evaluation processor (for automatic routing) or using Imaging Gateway option 2-8-1 (Select DICOM Images for Transmission).
> DICOM TRANSMIT DESTINATION File (#2006.587) The FileMan file where information about DICOM Storage SCP destinations is stored. This file should not be edited directly; to update the contents of this file, use the DICOM Gateway to update the SCU_List.dic file.
> evaluation processor The process responsible for managing the evaluation queue and for determining whether a newly acquired image should be automatically routed.
> IMAGE BACKGROUND QUEUE File (#2006.03) A multipurpose FileMan file where evaluation queue entries are stored. Entries intended for use by other processes are also stored in this file.
> locks Used on a VistARad workstation to prevent more than one radiologist from interpreting the same exam. A radiologist who opens a locked exam will be notified that the exam is locked. This radiologist will be able to display the exam, but not to update its status.
> NETWORK LOCATION File (#2005.2) The FileMan file where entries for all physical storage devices in the Imaging system, including Imaging destinations for routing, are stored.
> on-demand routing The transmission of manually selected exams to one or more destinations.
> Route.dic The DICOM Gateway dictionary file used to store routing rules.
> routing In the VistA system, the process responsible for sending images across a WAN to one or more remote locations. Routing can be performed automatically or on-demand.
> Routing Gateway A DICOM Gateway that is configured to manage the routing of images in the VistA system. A Routing Gateway is typically run on a dedicated
Glossary
> computer. Also, the set of menu options in the DICOM Gateway software specific to routing.
> routing rules The information used by the Routing Gateway to select images for automatic routing.
> routing system All of the software and hardware components related (but not necessarily limited to) routing. Parts of the routing system include the Routing Gateway, Image Gateways, and VistARad workstations.
> evaluation queue The queue used to determine whether newly acquired images will be automatically routed. This queue is populated by Image Gateways. Entries in this queue are compared to routing rules by the evaluation processor. Entries that meet the criteria in routing rules are added to the transmission queue.
> SCU_List.dic A dictionary file used by the DICOM Gateway that stores information about each DICOM Storage SCP that can receive routed DICOM images from VistA Imaging.
> SEND QUEUE (#2006.035) The FileMan file where transmission queue entries for Imaging destinations are stored. Entries can be added to this file by the evaluation processor (for automatic routing) or by a VistARad user (for on-demand routing).
> transmission processor The generic term for either of the two processes responsible for sending routed images to destinations. Imaging destinations are served by one or more instances of the transmission processor 3-1 (Start the Transmission Processor) associated with the Routing Gateway. DICOM Storage SCP destinations are served by one of more transmission processors 2-8-2 (Transmit DICOM Images to a Storage SCP) associated with the Image Gateway.
> transmission queue The generic term for either of two queues used by transmission processors. Entries in these queues identify images to be routed and where the images are to be sent. See also: SEND QUEUE File (#2006.035) and DICOM IMAGE OUTPUT File (#2006.574).
> VistARad The software used to display and interpret radiology exams. VistARad is also the primary tool used to display routed exams and to route exams on-demand.

# Index 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### A

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> after-hours coverage 9, 18 automatic routing
> defining rules for 7–23 described 1, 3–4, 87
prior exams 4, 20
*see also* routing

### B

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Background Processor 32
> balance command 10, 21

### C

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> cache, remote *see* RC column; storage folders CacheLocationID 46
> comments in routing rules 23
> completed trans. queue entries, purging 58 compression 21, 33, 83
> conditions, routing rule 11–22 configuration
> general information 81
> Routing Gateway 42
> routing rules 7–23
> VistARad 45–47 configuration files
> MAGJ.INI 46
Route.dic 42–44, 57, 87
SCU_List.dic 36–38, 88
coverage, after-hours 9, 18
> customer support 69

### D

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> date/time conditions 9, 18
> deleting routed exams 6, 35 destinations
> deactivating 53
> defining 25–38
> described 1, 87
> routing rules and 10–11, 10
> VistARad and 46–47
> DICOM Gateway *see also* Image Gateway; Routing Gateway
> DICOM IMAGE OUTPUT File (#2006.574) 87
> DICOM Storage SCP destinations deactivating 54
> described 1, 4
> in SCU_List.dic 36
> naming conventions 36 on-demand routing to 62 worksheet 75
> DICOM transmission processor starting 51
> stopping 55
> DICOM TRANSMIT DESTINATION File (#2006.587) 37, 87
> displaying routed exams 5, 61 displaying routing rules 58

### E

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> evaluation processor described 3, 87 log files for 52
> multiple instances 44
> starting 49, 56
> stopping 55, 57
> evaluation queue 3, 49, 88 exam lists
> filtering at receiving site 45 RC column in 35, 61, 68
> using for on-demand routing 63 exam locks 62, 87
> exams, routed compression 33, 83
> deleting 6, 35
> displaying 5, 61
> dividing between destinations 10, 21
> prior 4, 20
> priority of 5, 20 representative images in 68
> expired trans. queue entries, purging 58

### F

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> failed trans. queue entries, re-queuing 58 folders, storage
> for Imaging destinations 28–30 VistARad and 46–47

### H

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> hidden shares, creating 29 historical exams, routing 4, 20
> holidays, routing rules and 9, 18

### I

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> IMAGE BACKGROUND QUEUE File (#2006.03) 87
> Image Gateways 3, 68
> N
> naming conventions
> DICOM Storage SCP destinations 36 Imaging destinations 26
> NETWORK LOCATION FILE (#2005.2)
> described 87
> field descriptions 32–38 Imaging destinations in 30 sample values for 31, 74
> images, representative 68
> Imaging destinations compression 33, 83
> deactivating 53
> defining 30–35
> described 1, 4
> naming conventions 26 on-demand routing to 62 passwords for 29 storage folders for 28–30 user names for 29
> O
> obsolete trans. queue entries, purging 58 on-demand routing
> described 1, 4, 87
> requirements for 62
> using 62
> *see also* routing operators, routing rule 9, 18
> worksheet 73
> importing routing rules 42–44, 57

### J

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> JPEG 2000 33, 83

### K

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> keys, security 62

### L

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> lists *see* exam lists load balancing 10, 21
> locks, exam 62, 87
> log files 52

### M

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> MAG VISTARAD SITE PARAMETERS File 45
> MAG_Decompressor 83
> MAGJ DEMAND ROUTE DICOM key 62 MAGJ DEMAND ROUTE key 62 MAGJ.INI 46
> maintaining routing 52
> manual routing *see* on-demand routing modality, routing rules and 12
> multiple conditions in routing rules 8, 22 multiple evaluation processors 44
> P
> passwords 29
> patient information, transmission of vi prior exams, routing 4, 20
> priority, routing 5, 20 procedures: *see* exams
> purging the transmission queue 57, 58

### R

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> RC (Remote Cache) column 35, 61, 68 receiving sites
> configuration tasks for 25 displaying routed exams at 61 VistARad configuration for 46
> *see also* destinations related exams, routing 4, 20 Remedy Help Desk 69
> Remote Cache (RC) column 35, 61, 68 remote storage *see* storage folders representative images 68
> retention period 6, 35
> Route Request dialog 4, 62
> Route.dic 42–44, 57, 87 routed exams
> compression 33, 83
> deleting 6, 35
> displaying 5, 61
> dividing between destinations 10, 21
> priority of 5, 20 routing
> activating 49
> configuration 25–47, 47, 81
> studies *see* exams
> described 1–4, 65–69, 87
> disabling 55
> log files 52
> maintaining 52
> menu options for 56–59 on-demand 62–64
> Routing Gateway config. options 42 rules 7–23, 42–44
> terms of use v troubleshooting 65
> VistARad configuration 45–47
> Routing Gateway 56
> configuring 42
> described 87
> importing rules for 42–44 log files 52
> menu options for 56–59 using 49–55
> rules, routing conditions in 11–22
> date/time in 18
> described 7, 88
> destinations in 10
> displaying 44, 58
> importing 42–44, 57
> load balancing with 10, 21 multiple sets of 44 operators 18
> priority 5, 20
> tips 23
> wildcards 18
> worksheet 77

### S

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> SCU_List.dic 36–38, 88
> security keys 62
> send command (routing rules) 10
> SEND QUEUE File (#2006.035) 88
> *see also* transmission queue sending sites
> configuration tasks for 25 displaying routed exams at 61 VistARad configuration for 45
> shutdown, routing 55
> speed, routing, factors affecting 66 storage folders
> defining 28–30
> VistARad and 46–47
> T
> time of day, routing rules and 9, 18 transmission processor
> described 4, 88 imaging destinations
> drives mapped by 67 starting 50, 55, 56
> stopping 56 log files for 52
> Storage SCP destinations starting 50
> stopping 55 transmission queue
> populating 3, 56
> purging 57, 58
> re-queuing failed entries in 58 size of 52, 57
> troubleshooting routing 65

### U

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> unprocessed trans. queue entries, purging 58 user names 29

### V

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> values in rule conditions 18 verifying routing rules 44 VistARad
> configuring for routing 45–47 described 88
> displaying routed exams with 5, 61
> on-demand routing and 4, 62–64 using for multiple destinations 47

### W

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> weekend/weekdays, routing rules and 9, 18
> wildcards 9, 18 worklists *see* exam lists worksheets
> configuration 81
> destination 73, 75
> routing rule 77
