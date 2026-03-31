---
title: PIMS Version 5.3 User Manual - Veteran ID Card Menu
doc_type: UM
doc_label: User Manual
doc_layer: anchor
doc_subject: Veteran ID Card Menu
app_code: ADT
app_name: Admission Discharge Transfer
section: CLI
app_status: active
pkg_ns: ADT
patch_ver: 5.3
patch_id: ADT*5.3
group_key: "ADT:ADT:5.3"
file_numbers: []
security_keys: []
menu_options: 0
description: The VIC Card replaces the old embossed card as a means of identifying veteran patients entitled to care and services at Veterans Affairs (VA) healthcare facilities. It includes such current technology features as the patient’s picture, a bar code, and a magnetic stripe upon which is encoded patient
audience: 
keywords: 
  - message
  - error
  - download
  - segment
  - datacard
  - communications
  - subsystem
  - application
  - card
  - please
page_count: 0
word_count: 2269
section_count: 0
table_count: 0
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Admis_Disch_Transfer_(ADT)/adt_vic.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Admis_Disch_Transfer_(ADT)/adt_vic.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=55"
---

PIMS V. 5.3 ADT Module User ManualVeteran ID Card Menu

Inpatient Card Download

Outpatient Card Download

Preadmission Card Download

Single Patient Download Request

DataCard’s HL7 Interface Technical Reference

  
Overview

The VIC Card replaces the old embossed card as a means of identifying veteran patients entitled to care and services at Veterans Affairs (VA) healthcare facilities. It includes such current technology features as the patient’s picture, a bar code, and a magnetic stripe upon which is encoded patient demographic information. A commercial system was purchased from DataCard Corp. to allow all VA medical centers (VAMCs) to make photo ID cards for patients. The system is connected to DHCP by a standard HL7 interface.

User training and all related training materials for using the photo capture station will be provided by DataCard Corp. at the time of installation.

DataCard’s HL7 Interface Technical Reference is provided after the option documentation.

The following is a brief description of the options contained in the Veteran ID Card Menu.

INPATIENT CARD DOWNLOAD

This option allows the user to batch download demographic information for inpatients to the DataCard PC server in order to produce VIC cards.

OUTPATIENT CARD DOWNLOAD

This option allows the user to batch download demographic information for clinic patients with future appointments to the DataCard PC server in order to produce VIC cards.

PREADMISSION CARD DOWNLOAD

This option allows the user to batch download demographic information for scheduled admissions to the DataCard PC server in order to produce VIC cards.

SINGLE PATIENT DOWNLOAD REQUEST

This option allows the user to download demographic information for a specified patient to the photo capture station.

Inpatient Card Download

The Inpatient Card Download option is used to batch download demographic information for all current inpatients to the DataCard PC server in order to produce VIC cards.

At multidivisional facilities, you will only be able to choose from those ward(s) associated with the selected division(s). Up to 20 individual divisions/wards may be selected.

You must hold the DGQE VIC DOWNLOAD security key to access this option.

Outpatient Card Download

The Outpatient Card Download option is used to batch download demographic information for all clinic patients with future appointments for a selected date range to the DataCard PC server in order to produce VIC cards.

At multidivisional facilities, you will only be able to choose from those clinic(s) associated with the selected division(s). Up to 20 individual divisions/clinics may be selected.

You must hold the DGQE VIC DOWNLOAD security key to access this option.

Preadmission Card Download

The Preadmission Card Download option is used to batch download demographic information for all scheduled admissions for a selected date range to the DataCard PC server in order to produce VIC cards.

At multidivisional facilities, you will be able to choose all divisions or up to 20 individual divisions may be selected.

You must hold the DGQE VIC DOWNLOAD security key to access this option.

Single Patient Download Request

The Single Patient Download Request option is used to download demographic information for a single patient to the photo capture station.

The following fields are checked for missing and/or inconsistent data elements in the patient's record.

> SEX STREET ADDRESS

> DATE OF BIRTH CITY

> MARITAL STATUS STATE

> RELIGION ZIP CODE

> SSN COUNTY

> ELIGIBILITY CODE PERIOD OF SERVICE

> CLAIM NUMBER

If any data elements are missing, they will be listed and you will be asked if you still wish to download the data. If there are no missing elements, the information will be automatically downloaded after the patient name is entered.

DataCard’s HL7 Interface Technical Reference

The HL7 interface that is implemented in the Veteran's Identification System is based on the information obtained from the document titled: HL7 Interface Specification Veteran Identification Card Version 1. The VIC system follows this document explicitly, and where deviations between the ANSI standard HL7 protocol and the standard defined in the document occur, the VIC system conforms to the standard defined in the document.

The VIC application provides a communication setup dialog to allow the user to configure the application to support several different RS-232 communications configurations. By default, the application is set to use COM2: at 9600 baud, no parity, 8 data bits and 1 stop bit. The flow control is set to use XON/XOFF by default. Numerous other communication setup options are available to suit the needs of each individual VA installation. Please see the Communication Setup configuration option in the application for a complete list of the options.

The VIC application communications subsystem is driven by the hardware interrupt of the COM port that is selected in the communications configuration. Therefore, it is very important that no other application is running, at the same time as VIC, that uses the same hardware interrupt (i.e., The Windows Terminal Emulator program and similar applications).

The VIC application uses the standard HL7 Hybrid Lower Layer Protocol for a transport mechanism. This includes the block length error checking and XOR checksum error checking. In addition, the VIC application performs an error check on the data stream to verify that the host system is using a compatible version (2.2) of the HL7 system. Any errors that are found in the Lower Layer Protocol data stream are logged to a local file (VICCOMM.ERR in the application's working directory) to aid in debugging communications problems and the appropriate message is returned to the V*IST*A host, as defined in the document Health Industry Level 7 Interface Standards Appendix B: Lower Layer Protocols. Since any errors in the Lower Layer Protocol render the data contained in the data stream unreliable, no additional processing occurs.

As stated previously, the HL7 application level protocol conforms to the standards detailed in the HL7 Interface Specification for the Veteran Identification Card. When an error occurs at the application level of translating an HL7 message, the VIC application formats and sends an appropriate response to the V*IST*A host. In addition, the error is logged to the VICCOMM.ERR file in the application's working directory.

DataCard’s HL7 Interface Technical ReferenceNote: The VICCOMM.ERR file is a text file that is to be used by the Systems Administrator and other support personnel to aid debugging problems that occur in the communications subsystem. Since the file will continue to grow as each communications error is detected, it should be monitored and periodically deleted (at least once per week) to avoid taking up unnecessary disk space.

The remainder of this document specifies the possible error codes and return values that can be returned to the V*IST*A host system within the Text Message field of the MSA message segment.

1000 Segment Mismatch

The HL7 message that was sent from the V*IST*A host contains a message segment that is incompatible with the message segment structure defined on the VIC system.

Returns:\|1 The segment number, from the beginning of the message, where

the error occurred.

1001 End of Structure

This error usually means that the communications subsystem is expecting more message segments than have been received, possibly the HL7 message is incomplete.

1002 Empty Structure

The HL7 message is empty.

1003 Invalid Message

The communications subsystem received an HL7 message that is not defined to VIC.

1004 Empty Segment

This error usually means that the communications subsystem is expecting more message fields for a segment than have been received, possibly the HL7 message is incomplete.

1005 Extra Segment(s)

This error usually means that the V*IST*A HL7 message has more message segments than are expected by the VIC communication subsystem.

DataCard’s HL7 Interface Technical Reference1006 No Current Segment

This is a severe VIC communications subsystem error. Please capture an ASCII representation of the message being sent to the VIC system, including the Lower Layer Protocol information, and submit it to DataCard.

1007 Out of Memory

This is a severe VIC communications subsystem error. Please capture an ASCII representation of the message being sent to the VIC system, including the Lower Layer Protocol information, and submit it to DataCard.

Returns:\|1 The amount of memory being allocated when the error occurred.

1008 Message Segment Not Found

This is a severe VIC communications subsystem error. Usually this error indicates that the HL7 Message definition file, HL7.DAT in the application's working directory, is corrupt. Please try restoring the HL7.DAT from a backup. If the error condition continues, please capture an ASCII representation of the message being sent to the VIC system, including the Lower Layer Protocol information, and submit it to DataCard.

Returns:Sl The name of the message segment that could not be found.

1009 Segment Too Long

While parsing the HL7 message, the VIC communications subsystem encountered more fields than were expected. This message can also indicate that the HL7 Message definition file, HL7.DAT in the application's working directory, is corrupt. Please try restoring the HL7.DAT from a backup and verify that the HL7 data stream from the V*IST*A does not contain extra data fields.

Returns:Sl The name of the message segment that is in error.

\|1 The position of the segment within the HL7 message.

1010 Invalid Message Type

The HL7 message is not recognized by the VIC communications subsystem. This message can indicate that the HL7 Message definition file, HL7.DAT in the application's working directory, is corrupt. Please try restoring the HL7.DAT from a backup and verify that the HL7 data stream from the V*IST*A contains a message type that is supported by the VIC communications subsystem.

Returns:Sl The offending message type.

DataCard’s HL7 Interface Technical Reference1011 Bad Field Separator

The character found after the segment name is not the defined field separator

character (^).

Returns:Sl The name of the segment that contains the erroneous character.

\|1 The position of the segment within the HL7 message.

1012 Parsing Error

This is a severe VIC communications subsystem error. Please capture an ASCII representation of the message being sent to the VIC system, including the Lower Layer Protocol information, and submit it to DataCard.

1013 Segment Out of Order

The segment that is received in the V*IST*A HL7 data stream is not the segment that is expected. This message can indicate that the HL7 Message definition file, HL7.DAT in the application's working directory, is corrupt. Please try restoring the HL7.DAT from a backup and verify that the HL7 data stream from the V*IST*A contains the proper message segments. If the error condition continues, please capture an ASCII representation of the message being sent to the VIC system, including the Lower Layer Protocol information and submit it to DataCard.

Returns:Sl The message segment that was found at the point of error.

S2 The message segment that was expected.

\|1 The position of the segment within the HL7 message.

1014 Field Too Long

The data field (or component) received from the V*IST*A HL7 data stream is longer than the maximum expected by the VIC communications subsystem.

Returns:S1 The name of the segment that contains the error.

S2 The name of the field that contains the error.

S3 The name of the component (if any) that contains the error.

\|1 The position of the segment in the message.

\|2 The field number within segment that is in error.

\|3 The component number (if any) within the field that contains the

error.

DataCard’s HL7 Interface Technical Reference1016 Table Undefined

This is a severe VIC communications subsystem error. Please capture an ASCII representation of the message being sent to the VIC system, including the Lower Layer Protocol information, and submit it to DataCard.

Returns:Sl The table name being referenced.

1017 Buffer Too Short

This is a severe VIC communications subsystem error. Please capture an ASCII representation of the message being sent to the VIC system, including the Lower Layer Protocol information, and submit it to DataCard.

Returns:Sl The table name being referenced.

\|1 The allocated size of the table being referenced.

\|2 The size needed for the table.

1018 File Error

A file necessary for the VIC communications subsystem could not be opened. This error could be caused by the permissions granted to the offending file. This message can also indicate that the HL7 Message definition file, HL7.DAT in the application's working directory, is corrupt. Please try restoring the HL7.DAT from a backup.

Returns:Sl The full path and file name of the file that could not be opened.

1019 Required Field Missing

A field that the VIC communications subsystem expects to find data in is empty in the V*IST*A HL7 data stream.

Returns:Sl The name of the table that contains the field.

S2 The name of the field that is missing.

1020 Required Composite Field Missing

A composite field that the VIC communications subsystem expects to find data in is empty in the V*IST*A HL7 data stream.

Returns:Sl The name of the table that contains the field.

S2 The name of the field that the composite is a member of.

S3 The name of the composite that is missing.

DataCard’s HL7 Interface Technical Reference1021 Invalid Buffer

This is a severe VIC communications subsystem error. Please capture an ASCII representation of the message being sent to the VIC system, including the Lower Layer Protocol information, and submit it to DataCard.

1022 Illegal Special Character

The field or composite contains a special character that is invalid for this type of field. Please verify that V*IST*A HL7 data stream contains only valid characters for each type of field defined.

Returns:S1 The name of the table that contains the erroneous field.

S2 The name of the field that contains the invalid character.

S3 The name of the component (if any) that contains the invalid

character.

2000 Table Error

This message indicates that the HL7 Message definition file, HL7.DAT in the application's working directory, is corrupt and cannot be loaded. Please restore the HL7.DAT from a backup.