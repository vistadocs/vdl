---
title: HL7 HL*1.6*118 Message Parsing Utilities Supplement
doc_type: SUP
doc_label: Supplement
doc_layer: anchor
doc_subject: 
app_code: HL7
app_name: HL7 (VistA Messaging)
section: INF
app_status: active
pkg_ns: 
patch_ver: 1.6
patch_id: 
group_key: "HL7::1.6"
file_numbers: []
security_keys: []
menu_options: 0
description: <span class="smallcaps">VistA Health Level Seven (HL7) Message Parsing Utilities </span><span class="smallcaps">Supplement to Patch Description </span><span class="smallcaps">Patch HL\1.6\118</span>
audience: 
keywords: 
  - header
  - segment
  - class
  - message
  - strong
  - table
  - component
  - parsing
  - even
  - contents
page_count: 0
word_count: 3027
section_count: 7
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: July 2004
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Health_Level_7_(HL7)/hl71_6p118_sp2.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Health_Level_7_(HL7)/hl71_6p118_sp2.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=8"
---

![](hl7-hl-1-6-118-message-parsing-utilities-supplement/001.png)

<span class="smallcaps">V*ist*A Health Level Seven (HL7)  
Message Parsing Utilities  
</span><span class="smallcaps">Supplement to Patch Description  
  
</span><span class="smallcaps">Patch HL\*1.6\*118</span>

<span class="smallcaps">July 2004</span>

Department of Veterans Affairs (VA)

VHA OI Health Systems Design & Development (HSD&D)

Messaging & Interface Services (M&IS)

<span id="_Toc2678770" class="anchor"></span>Revision History

The following table displays the revision history for this document. Revisions to the documentation are based on patches and new versions released to the field.

<table>
<colgroup>
<col style="width: 11%" />
<col style="width: 16%" />
<col style="width: 41%" />
<col style="width: 30%" />
</colgroup>
<tbody>
<tr class="odd">
<td><strong>Date</strong></td>
<td><strong>Revision</strong></td>
<td><strong>Description</strong></td>
<td><strong>Author</strong></td>
</tr>
<tr class="even">
<td>07/2004</td>
<td>V.1.0</td>
<td>Initial Draft. HL7 Message Parsing Utilities.<br />
Supplement to HL7 Site Manager &amp; Developer Manual Version 1.6*56</td>
<td>REDACTED</td>
</tr>
<tr class="odd">
<td>01/2004</td>
<td></td>
<td><p>$$GET moved to HLOPRS</p>
<p>PROCESSING MODE parsed from header</p></td>
<td>REDACTED</td>
</tr>
<tr class="even">
<td>2/12/2004</td>
<td></td>
<td>Changed HL2PRS* routines to HLOPRS* - due to decision to move the namespace</td>
<td>REDACTED</td>
</tr>
</tbody>
</table>

Patch Revisions

For a complete list of patches related to this software, please refer to the Patch Module on FORUM.

<span id="_Toc96063143" class="anchor"></span><span class="smallcaps">Table of Contents</span>

# Overview of the HL7 Parsing Utilities


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Overview of the HL7 Parsing Utilities](#overview-of-the-hl7-parsing-utilities)
- [Function Specifications](#function-specifications)
  - [\$\$STARTMSG^HLPRS(.HLMSG,IEN,.HEADER)](#startmsghlprshlmsgienheader)
    - [Message Header, MSH Segment](#message-header-msh-segment)
    - [Message Header, BHS Segment](#message-header-bhs-segment)
  - [\$\$NEXTSEG^HLPRS(.HLMSG,.SEGMENT)](#nextseghlprshlmsgsegment)
  - [\$\$GET^HLOPRS(.SEGMENT,SEQ,COMP,SUBCOMP,REP)](#gethloprssegmentseqcompsubcomprep)
  - [\$\$NEXTMSG^HLPRS(.HLMSG,.MSH)](#nextmsghlprshlmsgmsh)
    - [Message Header, MSH Segment](#message-header-msh-segment-1)
- [Examples of Message Parsing](#examples-of-message-parsing)
  - [Parsing a Single Messaging](#parsing-a-single-messaging)
  - [Parsing a Batch Message](#parsing-a-batch-message)
This supplement is meant to assist application developers who are using the HL7 package. A new set of utilities for parsing HL7 messages was introduced with patch HL\*1.6\*118. Prior to this patch, each application was responsible for parsing received messages with little assistance from the HL7 package. The new parsing utilities relieve the individual applications from most of the burden of parsing messages.
The HL7 parsing utilities provide applications with the ability to easily parse their messages. There are two additional benefits:
1.  For values within the message where instances of the HL7 encoding characters were replaced with an escape sequence, the parsed values are automatically restored to their original value.
2.  MSH and BHS segments when parsed are represented as arrays with each individual value is assigned a meaningful subscript, for example:
    1.  MSH(“MESSAGE TYPE”)=“ADT”
    2.  MSH(“EVENT”)=“A01”
The utilities consist of these four functions:
1.  \$\$STARTMSG: Starts the parsing process, returning the parsed header values.
2.  \$\$NEXTSEG: Advances the parsing process to the next segment within the message.
3.  \$\$GET: Obtains a particular value from the current segment.
4.  \$\$NEXTMSG: Advances the parsing process to the next message within the batch, returning the parsed header values (for batch messages only).

# Function Specifications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## \$\$STARTMSG^HLPRS(.HLMSG,IEN,.HEADER)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This function begins the parsing of the message, parsing the header and returning the individual values in the array HEADER().

<table>
<colgroup>
<col style="width: 18%" />
<col style="width: 81%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Input / Output</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Input</td>
<td>Internal Entry Number (IEN) of the message in the HL7 MESSAGE ADMINISTRATION file (#773)</td>
</tr>
<tr class="even">
<td>Output</td>
<td><p>Function returns 1 on success, 0 on failure. Failure would indicate that the message was not found.</p>
<p>HLMSG() (pass by reference, required): This array is used by the HL7 package to track the progress of parsing the message. The application MUST NOT touch it!</p>
<p>HEADER (pass by reference, optional): This array contains the results of parsing the message header. The format is provided in section 2.1.1 below:</p></td>
</tr>
</tbody>
</table>

### Message Header, MSH Segment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 47%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Sequence</strong></th>
<th><strong>Header</strong></th>
<th><strong>Description/Comment</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td>HEADER(“SEGMENT TYPE”)= “MSH”</td>
<td></td>
</tr>
<tr class="even">
<td>SEQ1</td>
<td>HEADER(“FIELD SEPARATOR”)</td>
<td>The 1<sup>st</sup> character field separator.</td>
</tr>
<tr class="odd">
<td>SEQ2</td>
<td><p>HEADER(“COMPONENT SEPARATOR”)</p>
<p>HEADER(“SUBCOMPONENT SEPARATOR”)</p>
<p>HEADER(“REPETITION SEPARATOR”)</p>
<p>HEADER(“ESCAPE CHARACTER”)</p></td>
<td>The four encoding characters.</td>
</tr>
<tr class="even">
<td>SEQ3</td>
<td>HEADER(“SENDING APPLICATION”)</td>
<td></td>
</tr>
<tr class="odd">
<td>SEQ4</td>
<td><p>HEADER(“SENDING FACILITY”,1)</p>
<p>HEADER(“SENDING FACILITY”,2)</p>
<p>HEADER(“SENDING FACILITY”,3)</p></td>
<td>First Component<br />
Second Component<br />
Third Component</td>
</tr>
<tr class="even">
<td>SEQ5</td>
<td>HEADER(“RECEIVING APPLICATION”)</td>
<td></td>
</tr>
<tr class="odd">
<td>SEQ6</td>
<td><p>HEADER(“RECEIVING FACILITY”,1)</p>
<p>HEADER(“RECEIVING FACILITY”,2)</p>
<p>HEADER(“RECEIVING FACILITY”,3)</p></td>
<td>First Component<br />
Second Component<br />
Third Component</td>
</tr>
<tr class="even">
<td>SEQ7</td>
<td>HEADER(“DT/TM OF MESSAGE”)</td>
<td>Converted to FileMan format.</td>
</tr>
<tr class="odd">
<td>SEQ8</td>
<td>HEADER(“SECURITY”)</td>
<td></td>
</tr>
<tr class="even">
<td>SEQ9</td>
<td><p>HEADER (“MESSAGE TYPE”)</p>
<p>HEADER(“EVENT”)</p>
<p>HEADER(“MESSAGE STRUCTURE”)</p></td>
<td>First Component<br />
Second Component<br />
Third Component</td>
</tr>
<tr class="odd">
<td>SEQ10</td>
<td>HEADER(“MESSAGE CONTROL ID”)</td>
<td>Message control ID.</td>
</tr>
<tr class="even">
<td>SEQ11</td>
<td><p>HEADER(“PROCESSING ID”)</p>
<p>HEADER(“PROCESSING MODE”)</p></td>
<td><p>First Component</p>
<p>Second Component</p></td>
</tr>
<tr class="odd">
<td>SEQ12</td>
<td>HEADER(“VERSION”)</td>
<td></td>
</tr>
<tr class="even">
<td>SEQ14</td>
<td>HEADER(“CONTINUATION POINTER”)</td>
<td>MESSAGE CONTROL ID of the message that this one continues.</td>
</tr>
<tr class="odd">
<td>SEQ15</td>
<td>HEADER(“ACCEPT ACK TYPE”)</td>
<td>ACCEPT ACKNOWLEDGMENT TYPE, &lt;AL or NE&gt;</td>
</tr>
<tr class="even">
<td>SEQ16</td>
<td>HEADER(“APP ACK TYPE”)</td>
<td>APPLICATION ACKNOWLEDGMENT TYPE, &lt;AL or NE&gt;</td>
</tr>
<tr class="odd">
<td>SEQ17</td>
<td>HEADER(“COUNTRY”)</td>
<td>COUNTRY CODE</td>
</tr>
</tbody>
</table>

### Message Header, BHS Segment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 41%" />
<col style="width: 6%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Sequence</strong></th>
<th colspan="2"><strong>Header</strong></th>
<th><strong>Description/Comment</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td colspan="2">HEADER(“SEGMENT TYPE”)= “BHS”</td>
<td></td>
</tr>
<tr class="even">
<td>SEQ1</td>
<td colspan="2">HEADER(“FIELD SEPARATOR”)</td>
<td>1<sup>st</sup> character field separator</td>
</tr>
<tr class="odd">
<td>SEQ2</td>
<td colspan="2"><p>HEADER(“COMPONENT SEPARATOR”)</p>
<p>HEADER(“SUBCOMPONENT SEPARATOR”)</p>
<p>HEADER(“REPETITION SEPARATOR”)</p>
<p>HEADER(“ESCAPE CHARACTER”)</p></td>
<td>The four encoding characters,</td>
</tr>
<tr class="even">
<td>SEQ3</td>
<td colspan="2">HEADER(“SENDING APPLICATION”)</td>
<td></td>
</tr>
<tr class="odd">
<td>SEQ4<br />
(See Note)</td>
<td colspan="2"><p>HEADER(“SENDING FACILITY”,1)</p>
<p>HEADER(“SENDING FACILITY”,2)</p>
<p>HEADER(“SENDING FACILITY”,3)</p></td>
<td>First Component<br />
Second Component<br />
Third Component</td>
</tr>
<tr class="even">
<td>SEQ5</td>
<td colspan="2">HEADER(“RECEIVING APPLICATION”)</td>
<td></td>
</tr>
<tr class="odd">
<td>SEQ6<br />
(See Note)</td>
<td colspan="2"><p>HEADER(“RECEIVING FACILITY”,1)</p>
<p>HEADER(“RECEIVING FACILITY”,2)</p>
<p>HEADER(“RECEIVING FACILITY”,3)</p></td>
<td>First Component<br />
Second Component<br />
Third Component</td>
</tr>
<tr class="even">
<td>SEQ7</td>
<td colspan="2">HEADER(“DT/TM OF MESSAGE”)</td>
<td>Converted to FileMan Format.</td>
</tr>
<tr class="odd">
<td>SEQ8</td>
<td colspan="2">HEADER(“SECURITY”)</td>
<td></td>
</tr>
<tr class="even">
<td>SEQ9</td>
<td colspan="3"><p>HEADER(“BATCH NAME/ID/TYPE”)<br />
<br />
The below fields are not defined by the standard within the BHS segment, but they are needed and are encoded in SEQ 9 by the VistA HL7 package:</p>
<ol type="1">
<li><blockquote>
<p>HEADER(“PROCESSING ID”)</p>
</blockquote></li>
<li><blockquote>
<p>HEADER(“ACCEPT ACK TYPE”)</p>
</blockquote></li>
<li><blockquote>
<p>HEADER(“APP ACK TYPE”)</p>
</blockquote></li>
</ol></td>
</tr>
<tr class="odd">
<td>SEQ10</td>
<td colspan="3"><p>HEADER(“BATCH COMMENT”)<br />
<br />
The VistA HL7 package, Version 1.6, currently requires that an application designate a batch message as being of a particular message type, event type, and version, and this information is encoded as components of SEQ10</p>
<ol type="1">
<li><blockquote>
<p>HEADER(“MESSAGE TYPE”)</p>
</blockquote></li>
<li><blockquote>
<p>HEADER(“EVENT”)</p>
</blockquote></li>
<li><blockquote>
<p>HEADER(“VERSION”)</p>
</blockquote></li>
</ol></td>
</tr>
<tr class="even">
<td>SEQ11</td>
<td>HEADER(“BATCH CONTROL ID”)</td>
<td colspan="2"></td>
</tr>
<tr class="odd">
<td>SEQ12</td>
<td>HEADER(“REFERENCE BATCH CONTROL ID”)</td>
<td colspan="2"></td>
</tr>
<tr class="even">
<td colspan="4"><em><strong>Note:</strong> The HL7 Version 2.4 Standards Manual does not document this, but components 2 &amp; 3 were added in an errata to be compatible with the MSH segment. It is documented in version 2.5 of the standard.</em></td>
</tr>
</tbody>
</table>

## \$\$NEXTSEG^HLPRS(.HLMSG,.SEGMENT)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This function advances parsing to the next segment.

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Input / Output</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Input</td>
<td>HLMSG() (pass by reference, required): This array is used by the HL7 package to track the current position in the message. The application MUST NOT touch it!</td>
</tr>
<tr class="even">
<td>Output</td>
<td><p>Function returns 1 on success, 0 if there are no more segments in this message. For batch messages, a return value of 0 does not preclude the possibility that there are additional individual messages within the batch.</p>
<p>HLMSG (pass by reference, required): This array is used by the HL7 package to track the current position in the message. The application MUST NOT touch it!</p>
<p>SEGMENT (pass by reference, required): The segment is returned in this array. SEGMENT(“SEGMENT TYPE”) is returned with the 3 letter HL7 segment type that always begins a segment. The structure is not further described here because it should not be accessed directly by the application developer. Use $$GET to obtain individual segment values. As a shortcut, $$GET^HLOPRS(0) may be used to return the segment type.</p></td>
</tr>
</tbody>
</table>

## \$\$GET^HLOPRS(.SEGMENT,SEQ,COMP,SUBCOMP,REP)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This function gets a value from a segment that was obtained by calling \$\$NEXTSEG. The SEQ, COMP, SUBCOMP, and REP parameters are optional. If not specified, they default to the value1. For example, \$\$GET^HLPRS(.SEGMENT,1) will return the value of the first field, first component, first subcomponent, in the first occurrence. Since many fields consist of a single simple value, this is a useful feature. \$\$GET^HLOPRS(0) may be used to return the segment type.

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Input / Output</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Input</td>
<td><ul>
<li><p>SEGMENT (required, pass by reference): The segment was placed in this array by $$NEXTSEG.</p></li>
<li><p>SEQ: The sequence number of the field, defaults to 1</p></li>
<li><p>COMP: The number of the component, defaults to 1</p></li>
<li><p>SUBCOMP: The number of the subcomponent, defaults to 1</p></li>
<li><p>REP: The occurrence number. For a non-repeating field, the occurrence number need not be provided, because it is always 1.</p></li>
</ul></td>
</tr>
<tr class="even">
<td>Output</td>
<td>Function returns the value on success, “” on failure or if the specified part is not valued.</td>
</tr>
</tbody>
</table>

## \$\$NEXTMSG^HLPRS(.HLMSG,.MSH)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Advances to the next message within the batch, with the MSH segment returned.

<table>
<colgroup>
<col style="width: 17%" />
<col style="width: 82%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Input / Output</strong></th>
<th><strong>Description</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Input</td>
<td>HLMSG (pass by reference, required) This array is used by the HL7 package to track the current position in the message. The application MUST NOT touch it!</td>
</tr>
<tr class="even">
<td>Output</td>
<td><p>Function returns 1 on success, 0 if there are no more messages</p>
<p>MSH (pass by reference, required): Returns the message header in the format provided in Section 3.4.1 below.</p></td>
</tr>
</tbody>
</table>

### Message Header, MSH Segment

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 12%" />
<col style="width: 47%" />
<col style="width: 39%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Sequence</strong></th>
<th><strong>Header</strong></th>
<th><strong>Description/Comment</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td></td>
<td>HEADER(“SEGMENT TYPE”)</td>
<td>“MSH”</td>
</tr>
<tr class="even">
<td>SEQ1</td>
<td>HEADER(“FIELD SEPARATOR”)</td>
<td>The 1<sup>st</sup> character field separator.</td>
</tr>
<tr class="odd">
<td>SEQ2</td>
<td><p>HEADER(“COMPONENT SEPARATOR”)</p>
<p>HEADER(“SUBCOMPONENT SEPARATOR”)</p>
<p>HEADER(“REPETITION SEPARATOR”)</p>
<p>HEADER(“ESCAPE CHARACTER”)</p></td>
<td>The four encoding characters.</td>
</tr>
<tr class="even">
<td>SEQ3</td>
<td>HEADER(“SENDING APPLICATION”)</td>
<td></td>
</tr>
<tr class="odd">
<td>SEQ4</td>
<td><p>HEADER(“SENDING FACILITY”,1)</p>
<p>HEADER(“SENDING FACILITY”,2)</p>
<p>HEADER(“SENDING FACILITY”,3)</p></td>
<td>First Component<br />
Second Component<br />
Third Component</td>
</tr>
<tr class="even">
<td>SEQ5</td>
<td>HEADER(“RECEIVING APPLICATION”)</td>
<td></td>
</tr>
<tr class="odd">
<td>SEQ6</td>
<td><p>HEADER(“RECEIVING FACILITY”,1)</p>
<p>HEADER(“RECEIVING FACILITY”,2)</p>
<p>HEADER(“RECEIVING FACILITY”,3)</p></td>
<td>First Component<br />
Second Component<br />
Third Component</td>
</tr>
<tr class="even">
<td>SEQ7</td>
<td>HEADER(“DT/TM OF MESSAGE”)</td>
<td>Converted to FileMan format.</td>
</tr>
<tr class="odd">
<td>SEQ8</td>
<td>HEADER(“SECURITY”)</td>
<td></td>
</tr>
<tr class="even">
<td>SEQ9</td>
<td><p>HEADER (“MESSAGE TYPE”)</p>
<p>HEADER(“EVENT”)</p>
<p>HEADER(“MESSAGE STRUCTURE”)</p></td>
<td>First Component<br />
Second Component<br />
Third Component</td>
</tr>
<tr class="odd">
<td>SEQ10</td>
<td>HEADER(“MESSAGE CONTROL ID”)</td>
<td>Message control ID.</td>
</tr>
<tr class="even">
<td>SEQ11</td>
<td>HEADER(“PROCESSING ID”)</td>
<td></td>
</tr>
<tr class="odd">
<td>SEQ12</td>
<td>HEADER(“VERSION”)</td>
<td></td>
</tr>
<tr class="even">
<td>SEQ14</td>
<td>HEADER(“CONTINUATION POINTER”)</td>
<td>MESSAGE CONTROL ID of the message that this one continues.</td>
</tr>
<tr class="odd">
<td>SEQ15</td>
<td>HEADER(“ACCEPT ACK TYPE”)</td>
<td>ACCEPT ACKNOWLEDGMENT TYPE, &lt;AL or NE&gt;</td>
</tr>
<tr class="even">
<td>SEQ16</td>
<td>HEADER(“APP ACK TYPE”)</td>
<td>APPLICATION ACKNOWLEDGMENT TYPE, &lt;AL or NE&gt;</td>
</tr>
<tr class="odd">
<td>SEQ17</td>
<td>HEADER(“COUNTRY”)</td>
<td>COUNTRY CODE</td>
</tr>
</tbody>
</table>

# Examples of Message Parsing

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Parsing a Single Messaging

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N HLMSG,HEADER,SEG

;\*\* start the parsing \*\*

I \$\$STARTMSG^HLPRS(.HLMSG,66077,.HEADER) W !,"STARTING THE MESSAGE!",! ZW HEADER

;\*\* the output \*\*

STARTING THE MESSAGE!

HEADER("ACCEPT ACK TYPE")=AL

HEADER("APP ACK TYPE")=NE

HEADER("CONTINUATION POINTER")=

HEADER("COUNTRY")=US

HEADER("DT/TM OF MESSAGE")=3040217.133516

HEADER("ENCODING CHARACTERS")=~\|\\

HEADER("EVENT")=A31

HEADER("FIELD SEPARATOR")=^

HEADER("MESSAGE CONTROL ID")=55366077

HEADER("MESSAGE TYPE")=ADT

HEADER("PROCESSING ID")=T

HEADER("RECEIVING APPLICATION")=RG CIRN

HEADER("RECEIVING FACILITY",1)=553

HEADER("RECEIVING FACILITY",2)=

HEADER("RECEIVING FACILITY",3)=

HEADER("SECURITY")=

HEADER("SEGMENT TYPE")=MSH

HEADER("SENDING APPLICATION")=RG CIRN

HEADER("SENDING FACILITY",1)=553

HEADER("SENDING FACILITY",2)=

HEADER("SENDING FACILTY",3)=

HEADER("VERSION")=2.3

;\*\* loop through the segments \*\*

F Q:'\$\$NEXTSEG^HLPRS(.HLMSG,.SEG) D

. .W !,"SEGMENT TYPE=",SEG("SEGMENT TY

PE")

. .I SEG("SEGMENT TYPE")="PID" W !,"PATIENT NAME IS ",\$\$GET^HLOPRS(.SEG,5,3)\_" "\_\$\$GET^HLOPRS(.SEG,5)

;\*\* the output \*\*

SEGMENT TYPE=PID

PATIENT NAME IS TWO CHESNEY

SEGMENT TYPE=NTE

SEGMENT TYPE=EVN

## Parsing a Batch Message

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

N HLMSG,MSH,HEADER,SEG

I \$\$STARTMSG^HLPRS(.HLMSG,662,.HEADER) W !,"STARTING THE MESSAGE! MESSAGE

HEADER IS ",HEADER("SEGMENT TYPE")

;\*\* output \*\*

STARTING THE MESSAGE! MESSAGE HEADER IS BHS

;loop through the messages

F Q:'\$\$NEXTMSG^HLPRS(.HLMSG,.MSH) D

.W !,"MESSAGE TYPE=",MSH("MESSAGE TYPE"),!," EVENT=",MSH("EVENT")

.;loop through the segments

.F Q:'\$\$NEXTSEG^HLPRS(.HLMSG,.SEG) D

. . W !,"SEGMENT TYPE=",SEG("SEGMENT TYPE")

. . I SEG("SEGMENT TYPE")="PID" W !,"PATIENT NAME IS ", \$\$GET^HLOPRS(.SEG,5,3)\_" "\_\$\$GET^HLOPRS(.SEG,5)

;\*\*output\*\*

MESSAGE TYPE=ORU

EVENT=Z07

SEGMENT TYPE=PID

PATIENT NAME IS NITSCHE

SEGMENT TYPE=PD1

SEGMENT TYPE=ZPD

SEGMENT TYPE=ZTA

SEGMENT TYPE=ZIE

SEGMENT TYPE=ZEL

SEGMENT TYPE=ZEL

SEGMENT TYPE=ZEL

SEGMENT TYPE=ZEN

SEGMENT TYPE=ZCD

SEGMENT TYPE=ZRD

SEGMENT TYPE=ZCT

SEGMENT TYPE=ZEM

SEGMENT TYPE=ZEM

SEGMENT TYPE=ZGD

SEGMENT TYPE=ZGD

SEGMENT TYPE=ZIC

SEGMENT TYPE=ZIR

SEGMENT TYPE=ZDP

SEGMENT TYPE=ZIC

SEGMENT TYPE=ZIR

SEGMENT TYPE=ZIO

SEGMENT TYPE=NTE

SEGMENT TYPE=IN1

SEGMENT TYPE=ZMT

SEGMENT TYPE=ZMT

SEGMENT TYPE=ZMT

SEGMENT TYPE=ZBT

SEGMENT TYPE=ZSP

SEGMENT TYPE=RF1