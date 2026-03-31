---
title: TMP Version 1.5 Release 4.6 Requirements Specifications
doc_type: RS
doc_label: Requirements Specification
doc_layer: anchor
doc_subject: Release 4.6 s
app_code: TMP
app_name: Telehealth Management Platform
section: CLI
app_status: active
pkg_ns: TMP
patch_ver: 1.5
patch_id: TMP*1.5
group_key: "TMP:TMP:1.5"
file_numbers: []
security_keys: []
menu_options: 0
description: "<table> <colgroup> <col style=\\"width: 13%\\" /> <col style=\\"width: 12%\\" /> <col style=\\"width: 26%\\" /> <col style=\\"width: 47%\\" /> </colgroup> <thead> <tr class=\\"header\\"> <th><strong><u>Functional Area</u></strong></th> <th><strong><u>Function</u></strong></th> <th><strong><u>Feature</u></strong></th> <"
audience: 
keywords: 
  - class
  - scheduling
  - management
  - telehealth
  - even
  - appointment
  - vista
  - appointments
  - notifications
  - resource
page_count: 0
word_count: 2277
section_count: 0
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: 
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Telehealth_Management_Platform/tmp_4-6_rs.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Telehealth_Management_Platform/tmp_4-6_rs.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=231"
---

<u>Menu Functions</u>

| <u>Functional Area</u>           | <u>Function</u>            | <u>For User/System Admin</u> | <u>Description</u>                                                                                                                                                                                                                                                         | <u>Parent Menu in Application</u> |
|--------------------------------------|--------------------------------|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|
| Scheduling                           | Appointments                   | User                             | Make/Cancel of required appointment types (Clinic Based, VA Video Connect, Store and Forward) with provider and patient side specifics that feeds to VistA. New appointments as well as RTC/Consults availability. Intra and Inter facility. Individual or Group appointments. | Scheduling                            |
| Scheduling                           | Reserved Resource              | User                             | Reserving a resource for various purposes (e.g. Room for group use, provider time block, etc.)                                                                                                                                                                                 | Scheduling                            |
| Scheduling                           | Patient Search                 | User                             | Search and view for Patients via MVI integration                                                                                                                                                                                                                               | Scheduling                            |
| Scheduling                           | Service Calendar               | User                             | Calendar view of scheduled services                                                                                                                                                                                                                                            | Scheduling                            |
| Scheduling                           | Request VOD                    | User                             | Initiate request for VA Video Connect between Provider and Patient (VR URL)                                                                                                                                                                                                    | Scheduling                            |
| Scheduling                           | Patients                       | User                             | Search and view for Patients within TMP                                                                                                                                                                                                                                        | Scheduling                            |
| Scheduling Package                   | Scheduling Package             | User                             | Scheduling templates used for creating appointments based on Specialty, Sub Specialty, Modality, Patient/Provider Sites. Intra and Inter facility. Individual or Group appointments. Includes resources required at participating sites.                                       | TeleHealth Administration             |
| Scheduling Package                   | TSAs                           | User                             | TeleHealth Service Agreements between VA Sites (notification and approvals process)                                                                                                                                                                                            | TeleHealth Administration             |
| Scheduling Package                   | Participating Sites            | User                             | Search and View of participating sites linked to scheduling packages                                                                                                                                                                                                           | TeleHealth Administration             |
| Provider Credentialing & Privileging | Telehealth Privileging         | User                             | Provider privileging to sites based on specialties                                                                                                                                                                                                                             | TeleHealth Administration             |
| Provider Credentialing & Privileging | PPE Reviews                    | User                             | Provider privileging reviews                                                                                                                                                                                                                                                   | TeleHealth Administration             |
| Provider Credentialing & Privileging | PPE Feedbacks                  | User                             | Provider privileging feedback requests                                                                                                                                                                                                                                         | TeleHealth Administration             |
| Scheduling Package                   | Archived Agreements            | User                             | Archived TeleHealth Service Agreements between VA Sites (pre scheduling package)                                                                                                                                                                                               | TeleHealth Administration             |
| Resource Management                  | Facilities                     | User                             | Management of facilities in the TeleHealth network                                                                                                                                                                                                                             | Resources                             |
| Resource Management                  | TMP Sites                      | User                             | Management of associated sites within facilities in TeleHealth network                                                                                                                                                                                                         | Resources                             |
| Resource Management                  | TMP Resource Groups            | User                             | Management of Telehealth bundled resources                                                                                                                                                                                                                                     | Resources                             |
| Resource Management                  | TMP Resources                  | User                             | Management of Telehealth resource types (e.g. room, technology, vista clinics with stop codes)                                                                                                                                                                                 | Resources                             |
| Resource Management                  | Components                     | User                             | Management of Telehealth component types (e.g. equipment such as codec, hardware, cameras, CPU’s, desktops, laptops, peripherals, etc.…)                                                                                                                                       | Resources                             |
| Resource Management                  | Users                          | User                             | Management of Telehealth users (sign on, permissions, roles, etc.)                                                                                                                                                                                                             | Resources                             |
| Resource Management                  | Teams                          | User                             | Management of Telehealth teams (e.g. facility/hub approvers, etc..)                                                                                                                                                                                                            | Resources                             |
| Resource Management                  | Inventory                      | User                             | Management of Telehealth cart inventory and location (Clinical, Specialty)                                                                                                                                                                                                     | Resources                             |
| Resource Management                  | Staging Components             | System                           | Management of import staging area for components                                                                                                                                                                                                                               | Resources                             |
| TMP Efficiencies                     | On Call Entries                | User                             | On call schedule (e.g. for provider)                                                                                                                                                                                                                                           | Phone Book                            |
| TMP Efficiencies                     | TMP Sites                      | User                             | Contact phone information for TMP Sites (e.g. emergency contact number, radiology tech phone number, radiology desk, etc..)                                                                                                                                                    | Phone Book                            |
| CRM Foundational                     | Dashboard                      | User                             | Telehealth Dashboard                                                                                                                                                                                                                                                           | Workplace                             |
| CRM Foundational                     | Activities                     | User                             | CRM foundational element                                                                                                                                                                                                                                                       | Workplace                             |
| CRM Foundational                     | Calendar                       | User                             | CRM foundational element                                                                                                                                                                                                                                                       | Workplace                             |
| CRM Foundational                     | Imports                        | System                           | CRM foundational element                                                                                                                                                                                                                                                       | Workplace                             |
| CRM Foundational                     | Duplicate Detection            | System                           | CRM foundational element                                                                                                                                                                                                                                                       | Workplace                             |
| CRM Foundational                     | Queues                         | System                           | CRM foundational element                                                                                                                                                                                                                                                       | Workplace                             |
| CRM Foundational                     | Articles                       | System                           | CRM foundational element                                                                                                                                                                                                                                                       | Workplace                             |
| CRM Foundational                     | Reports                        | User                             | Telehealth Management Reporting (e.g. inventory utilization metrics)                                                                                                                                                                                                           | Workplace                             |
| CRM Foundational                     | Announcements                  | System                           | CRM foundational element                                                                                                                                                                                                                                                       | Workplace                             |
| CRM Foundational                     | Feedback                       | System                           | CRM foundational element                                                                                                                                                                                                                                                       | Workplace                             |
| CRM Foundational                     | Support Resources              | System                           | CRM foundational element                                                                                                                                                                                                                                                       | Workplace                             |
| TeleHealth Configurations            | Specialties                    | User                             | Metadata Management Specialties                                                                                                                                                                                                                                                | MetaData & Configuration              |
| TeleHealth Configurations            | Specialty Sub-Types            | User                             | Metadata Management specialty sub-types                                                                                                                                                                                                                                        | MetaData & Configuration              |
| TeleHealth Configurations            | Manufacturers                  | User                             | Metadata Management manufacturers                                                                                                                                                                                                                                              | MetaData & Configuration              |
| TeleHealth Configurations            | Models                         | User                             | Metadata Management models                                                                                                                                                                                                                                                     | MetaData & Configuration              |
| TeleHealth Configurations            | Component Types                | User                             | Metadata Management component types                                                                                                                                                                                                                                            | MetaData & Configuration              |
| TeleHealth Configurations            | Cart Types                     | User                             | Metadata Management cart types                                                                                                                                                                                                                                                 | MetaData & Configuration              |
| TeleHealth Configurations            | Sites                          | User                             | Metadata Management sites                                                                                                                                                                                                                                                      | MetaData & Configuration              |
| TeleHealth Configurations            | Equipment                      | User                             | Metadata Management equipment                                                                                                                                                                                                                                                  | MetaData & Configuration              |
| TeleHealth Configurations            | Resource Groups                | User                             | Metadata Management resource groups                                                                                                                                                                                                                                            | MetaData & Configuration              |
| TeleHealth Configurations            | Services                       | System                           | Metadata Management services                                                                                                                                                                                                                                                   | MetaData & Configuration              |
| Integration                          | Video on Demand                | System                           | Integration data video on demand                                                                                                                                                                                                                                               | Integration                           |
| Integration                          | Integration Result             | System                           | Integration data integration result                                                                                                                                                                                                                                            | Integration                           |
| Integration                          | Integration Settings           | System                           | Integration data integration settings                                                                                                                                                                                                                                          | Integration                           |
| Integration                          | User DUZS                      | System                           | Integration data user duzs                                                                                                                                                                                                                                                     | Integration                           |
| Integration                          | Interface Settings             | System                           | Integration data interface settings                                                                                                                                                                                                                                            | Integration                           |
| Integration                          | Integration System Jobs        | System                           | Integration data integration system jobs                                                                                                                                                                                                                                       | Integration                           |
| Integration                          | URL Definitions                | System                           | Integration data URL definitions                                                                                                                                                                                                                                               | Integration                           |
| Integration                          | URL Variables                  | System                           | Integration data URL variables                                                                                                                                                                                                                                                 | Integration                           |
| Integration                          | Message Log                    | System                           | Integration data message log                                                                                                                                                                                                                                                   | Integrations                          |
| Integration                          | Interface Audit Log            | System                           | Integration data interface audit log                                                                                                                                                                                                                                           | Integration                           |
| Integration                          | Interface Definition           | System                           | Integration data interface definition                                                                                                                                                                                                                                          | Integration                           |
| Integration                          | Interface Message              | System                           | Integration data interface message                                                                                                                                                                                                                                             | Integration                           |
| Integration                          | Interface Endpoints            | System                           | Integration data interface endpoints                                                                                                                                                                                                                                           | Integration                           |
| Integration                          | Interface Message IO           | System                           | Integration data interface message io                                                                                                                                                                                                                                          | Integration                           |
| Integration                          | Message Maps                   | System                           | Integration data message maps                                                                                                                                                                                                                                                  | Integration                           |
| Integration                          | Entity to Message Translation  | System                           | Integration data entity to message translation                                                                                                                                                                                                                                 | Integration                           |
| Integration                          | Message to Message Translation | System                           | Integration data message to message translation                                                                                                                                                                                                                                | Integration                           |
| CRM Foundational                     | Administration                 | System                           | CRM foundational element                                                                                                                                                                                                                                                       | Settings                              |
| CRM Foundational                     | Auditing                       | System                           | CRM foundational element                                                                                                                                                                                                                                                       | Settings                              |
| CRM Foundational                     | Security                       | System                           | CRM foundational element                                                                                                                                                                                                                                                       | Settings                              |
| CRM Foundational                     | Data Management                | System                           | CRM foundational element                                                                                                                                                                                                                                                       | Settings                              |
| CRM Foundational                     | Service Management             | System                           | CRM foundational element                                                                                                                                                                                                                                                       | Settings                              |
| CRM Foundational                     | Plugin Settings                | System                           | CRM foundational element                                                                                                                                                                                                                                                       | Settings                              |
| CRM Foundational                     | Plugin Logs                    | System                           | CRM foundational element                                                                                                                                                                                                                                                       | Settings                              |
| CRM Foundational                     | Customizations                 | System                           | CRM foundational element                                                                                                                                                                                                                                                       | Settings                              |
| CRM Foundational                     | Solutions                      | System                           | CRM foundational element                                                                                                                                                                                                                                                       | Settings                              |
| CRM Foundational                     | Processes                      | System                           | CRM foundational element                                                                                                                                                                                                                                                       | Settings                              |
| CRM Foundational                     | Email Automation               | System                           | CRM foundational element                                                                                                                                                                                                                                                       | Settings                              |
| TMP Efficiencies                     | Video on Demand                | User                             | View all VOD data                                                                                                                                                                                                                                                              | Settings                              |
| CRM Foundational                     | Business Management            | System                           | CRM foundational element                                                                                                                                                                                                                                                       | Settings                              |
| CRM Foundational                     | Templates                      | System                           | CRM foundational element                                                                                                                                                                                                                                                       | Settings                              |
| CRM Foundational                     | System Jobs                    | System                           | CRM foundational element                                                                                                                                                                                                                                                       | Settings                              |
| CRM Foundational                     | Group Resources                | System                           | CRM foundational element                                                                                                                                                                                                                                                       | Settings                              |
| TeleHealth Configurations            | Provider Site Resources        | System                           | CRM foundational element                                                                                                                                                                                                                                                       | Settings                              |
| TeleHealth Configurations            | Patient Site Resources         | System                           | CRM foundational element                                                                                                                                                                                                                                                       | Settings                              |
| CRM Foundational                     | Product Catalog                | System                           | CRM foundational element                                                                                                                                                                                                                                                       | Settings                              |
| CRM Foundational                     | Document Management            | System                           | CRM foundational element                                                                                                                                                                                                                                                       | Settings                              |
| CRM Foundational                     | Dynamics Marketplace           | System                           | CRM foundational element                                                                                                                                                                                                                                                       | Settings                              |
| CRM Foundational                     | Email Configuration            | System                           | CRM foundational element                                                                                                                                                                                                                                                       | Settings                              |
| CRM Foundational                     | Activity Feeds Configuration   | System                           | CRM foundational element                                                                                                                                                                                                                                                       | Settings                              |
| CRM Foundational                     | Activity Feeds Rules           | System                           | CRM foundational element                                                                                                                                                                                                                                                       | Settings                              |
| CRM Foundational                     | Customer Center                | System                           | CRM foundational element                                                                                                                                                                                                                                                       | Help                                  |

<u>Features</u>

<table>
<colgroup>
<col style="width: 13%" />
<col style="width: 12%" />
<col style="width: 26%" />
<col style="width: 47%" />
</colgroup>
<thead>
<tr class="header">
<th><strong><u>Functional Area</u></strong></th>
<th><strong><u>Function</u></strong></th>
<th><strong><u>Feature</u></strong></th>
<th><strong><u>Description</u></strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Scheduling</td>
<td>Appointments</td>
<td>Make Appointment Clinic Based - Individual (CVT Modality)</td>
<td>As a TMP Scheduler, I need the ability to schedule an individual CB CVT appointment with required resources and send appropriate email notifications</td>
</tr>
<tr class="even">
<td>Scheduling</td>
<td>Appointments</td>
<td>Make Appointment Clinic Based - Individual (SFT Modality)</td>
<td>Ability to make individual CB SFT appointment with required resources and appropriate email notifications</td>
</tr>
<tr class="odd">
<td>Scheduling</td>
<td>Appointments</td>
<td>Make Appointment Clinic Based - Group (CVT Modality)</td>
<td>Ability to make group CB CVT appointment with required resources and appropriate email notifications</td>
</tr>
<tr class="even">
<td>Scheduling</td>
<td>Appointments</td>
<td>Make Appointment VA Video Connect - Individual (CVT Modality)</td>
<td>Ability to make individual VVC CVT appointment with required resources and appropriate email notifications</td>
</tr>
<tr class="odd">
<td>Scheduling</td>
<td>Appointments</td>
<td>Make Appointment VA Video Connect - Individual (SFT Modality)</td>
<td>Ability to make individual VVC SFT appointment with required resources and appropriate email notifications</td>
</tr>
<tr class="even">
<td>Scheduling</td>
<td>Appointments</td>
<td>Make Appointment VA Video Connect - Group (CVT Modality)</td>
<td>Ability to make group VVC CVT appointment with required resources and appropriate email notifications</td>
</tr>
<tr class="odd">
<td>Scheduling</td>
<td>Appointments</td>
<td>Make appointment Efficiency</td>
<td>All sides of the appointment can be made with either Patient or Provider side login by scheduler.</td>
</tr>
<tr class="even">
<td>Scheduling</td>
<td>Appointments</td>
<td>Cancel Appointment</td>
<td>Ability to cancel any TMP Scheduled appointment with associated resources and send appropriate email notifications (whole appointment cancellation, patient cancellation, patient site cancellation)</td>
</tr>
<tr class="odd">
<td>Scheduling</td>
<td>Appointments</td>
<td>Real time clinic updates</td>
<td>Ability to receive clinic updates from VistA</td>
</tr>
<tr class="even">
<td>Scheduling</td>
<td>Appointments</td>
<td>Find Available Times - Return to Clinic</td>
<td>View and Select RTC Orders associated with a Patient in order to link with appointment</td>
</tr>
<tr class="odd">
<td>Scheduling</td>
<td>Appointments</td>
<td>Find Available Times - Consults</td>
<td>View and Select Consult Orders associated with a Patient in order to link with appointment</td>
</tr>
<tr class="even">
<td>Scheduling</td>
<td>Appointments</td>
<td>Appointment Views</td>
<td>Various data views (e.g. by facility, by VIZN, by Site, Provider and Patient side)</td>
</tr>
<tr class="odd">
<td>Scheduling</td>
<td>Appointments</td>
<td>VistA: Integration of Make/Cancel/Complete of Appointments to VistA</td>
<td>Bi Directional integration to VistA with required fields. Appointments that are scheduled or canceled in the Telehealth Management Platform are automatically updated in VistA. Schedulers are no longer required to enter appointments into VistA after scheduling in the Telehealth Management Platform.</td>
</tr>
<tr class="even">
<td>Scheduling</td>
<td>Reserved Resource</td>
<td>Reserved Resource</td>
<td>Ability to reserve a resource for a block of time for various purposes (e.g. Room for group use, provider time block, etc.)</td>
</tr>
<tr class="odd">
<td>TMP Efficiencies</td>
<td>Notifications</td>
<td>Provider notifications</td>
<td>Email notifications as part of appointment scheduling. Also Providers who prescribe medication will receive email notifications that indicate if the patient site where the Veteran is being seen is DEA registered.</td>
</tr>
<tr class="even">
<td>TMP Efficiencies</td>
<td>Notifications</td>
<td>Patient notifications (and other interested parties requested)</td>
<td>Email notifications as part of appointment scheduling. Veterans who are being seen in their home can receive email notifications with an internet calendar server (iCal) to save appointment information to their calendar</td>
</tr>
<tr class="odd">
<td>TMP Efficiencies</td>
<td>Notifications</td>
<td>Staff notifications</td>
<td>Email notifications as part of appointment scheduling or<br />
approval processes (e.g. reminder emails)</td>
</tr>
<tr class="even">
<td>TMP Efficiencies</td>
<td>Notifications</td>
<td>Approval processes</td>
<td>Interfacility and Intrafacility approval process (approve or reject within email notification link)</td>
</tr>
<tr class="odd">
<td>Scheduling</td>
<td>Patient Search</td>
<td>Patient Search</td>
<td>Search and view for Patients in MVI through multiple screens (appointment scheduling, Patients views).</td>
</tr>
<tr class="even">
<td>Scheduling</td>
<td>Service Calendar</td>
<td>Calendar View</td>
<td>Calendar view of scheduled services</td>
</tr>
<tr class="odd">
<td>Scheduling</td>
<td>Request VOD</td>
<td>On Demand VOD</td>
<td>Request an On demand VA Video Connect between Provider and Patient (VR URL received)</td>
</tr>
<tr class="even">
<td>Scheduling</td>
<td>Patients</td>
<td>Patient Search</td>
<td>Search and view for Patients within TMP</td>
</tr>
<tr class="odd">
<td>Scheduling Package</td>
<td>Scheduling Package</td>
<td>Scheduling Package Template</td>
<td>Scheduling templates used for creating appointments and TSAs based on Specialty, Sub Specialty, Modality, Patient/Provider Sites. Intra and Inter facility. Individual or Group appointments. Includes resources required at participating sites. Usage type field to determine TSA vs. Scheduling use.</td>
</tr>
<tr class="even">
<td>Scheduling Package</td>
<td>Scheduling Package</td>
<td>Standardized Naming Convention</td>
<td>Automatically name packages based on standard naming convention (specialty, sub specialty, Individual/Group, etc.)</td>
</tr>
<tr class="odd">
<td>Scheduling Package</td>
<td>Scheduling Package</td>
<td>Appointment Template</td>
<td>Re-usable template for an appointment including standard duration times</td>
</tr>
<tr class="even">
<td>Scheduling Package</td>
<td>TSAs</td>
<td>Telehealth Service Agreements</td>
<td>History of approvals between VA Facilities with printable TSA and provider preference reports (interfacility)</td>
</tr>
<tr class="odd">
<td>Scheduling Package</td>
<td>TSAs</td>
<td>Telehealth Service Agreements</td>
<td>Approval process with notifications for TSAs (e.g. FTC=&gt;Service Chiefs=&gt;Chief of Staffs OR Hub Director =&gt; Chief of Staffs for hub scheduling packages)</td>
</tr>
<tr class="even">
<td>Scheduling Package</td>
<td>Participating Sites</td>
<td>Participating Site Views</td>
<td>Search and View of participating sites linked to scheduling packages</td>
</tr>
<tr class="odd">
<td>Provider Credentialing &amp; Privileging</td>
<td>Telehealth Privileging</td>
<td>Provider privileging to sites based on specialties</td>
<td>Initiate Credentialing &amp; Privileging<br />
-Create Home/Parent Privileging Record For Provider<br />
-Create Proxy/Secondary Privileging Record For Provider</td>
</tr>
<tr class="even">
<td>Provider Credentialing &amp; Privileging</td>
<td>PPE Reviews</td>
<td>Provider privileging reviews</td>
<td>The Telehealth Management Platform automatically acknowledges and logs such review requests, and triggers a notification to the requesting Service Chief when all requests for feedback have been responded to.</td>
</tr>
<tr class="odd">
<td>Provider Credentialing &amp; Privileging</td>
<td>PPE Feedbacks</td>
<td>Provider privileging feedback requests</td>
<td>PPE Process is initiated to provide a feedback-based evaluation of a provider’s process. The mechanism for this process includes the generation of automated requests to the Receiving facilities prompting for feedback related to the provider’s practice</td>
</tr>
<tr class="even">
<td>Scheduling Package</td>
<td>Archived Agreements</td>
<td>Archived TSA data views</td>
<td>Historical TeleHealth Service Agreements between VA Sites (pre scheduling package)</td>
</tr>
<tr class="odd">
<td>Resource Management</td>
<td>Facilities</td>
<td>Data management of facilities in the TeleHealth network</td>
<td>Management of facilities in the TeleHealth network</td>
</tr>
<tr class="even">
<td>Resource Management</td>
<td>TMP Sites</td>
<td>Data management of associated sites within facilities in TeleHealth network</td>
<td>Management of associated sites within facilities in TeleHealth network</td>
</tr>
<tr class="odd">
<td>Resource Management</td>
<td>TMP Resource Groups</td>
<td>Data management of Telehealth bundled resources</td>
<td>Technology, rooms, and users can be linked together as a resource group and simultaneously scheduled for an appointment (rather than having to schedule technology, rooms, and users separately); these resource groups can be viewed remotely, resulting in transparency of resource availability.</td>
</tr>
<tr class="even">
<td>Resource Management</td>
<td>TMP Resources</td>
<td>Data management of Telehealth resource types (e.g. room, technology, vista clinics with stop codes)</td>
<td>Management of Telehealth resource types (e.g. room, technology, vista clinics with stop codes)</td>
</tr>
<tr class="odd">
<td>Resource Management</td>
<td>Components</td>
<td>Data management of Telehealth component types (e.g. equipment such as codec, hardware, cameras, CPU’s, desktops, laptops, peripherals, etc.…)</td>
<td>Management of Telehealth component types (e.g. equipment such as codec, hardware, cameras, CPU’s, desktops, laptops, peripherals, etc.…)</td>
</tr>
<tr class="even">
<td>Resource Management</td>
<td>Users</td>
<td>Data management of Telehealth staff database (Providers, Preceptors, Telepresenters, etc.) along with TMP User information (sign on, permissions, roles, etc.)</td>
<td>Management of Telehealth staff database (Providers, Preceptors, Telepresenters, etc.) along with TMP User information (sign on, permissions, roles, etc.)</td>
</tr>
<tr class="odd">
<td>Resource Management</td>
<td>Teams</td>
<td>Data management of Telehealth teams (e.g. facility/hub approvers, etc..)</td>
<td>Management of Telehealth teams (e.g. facility/hub approvers, etc..)</td>
</tr>
<tr class="even">
<td>Resource Management</td>
<td>Inventory</td>
<td>Data management of Telehealth cart inventory and location (Clinical, Specialty)</td>
<td>Management of Telehealth cart inventory and location (Clinical, Specialty)</td>
</tr>
<tr class="odd">
<td>Additional TMP Efficiencies</td>
<td>On Call Entries</td>
<td></td>
<td>On call schedule (e.g. for provider)</td>
</tr>
<tr class="even">
<td>Additional TMP Efficiencies</td>
<td>TMP Sites</td>
<td></td>
<td>Contact phone information for TMP Sites (e.g. emergency contact number, radiology tech phone number, radiology desk, etc..)</td>
</tr>
<tr class="odd">
<td>CRM Foundational</td>
<td>Dashboard</td>
<td>Telehealth Dashboard</td>
<td>Combination of reports into one dashboard view (user definable)</td>
</tr>
<tr class="even">
<td>CRM Foundational</td>
<td>Reports</td>
<td>Telehealth Management Reporting</td>
<td>Reports can be easily generated at the National, Veterans Integrated Service Network (VISN) and Facility levels with desired levels of granularity (e.g. inventory utilization metrics)</td>
</tr>
<tr class="odd">
<td>TeleHealth Configurations</td>
<td>Specialties</td>
<td>Data Management Specialties</td>
<td>List of available specialties</td>
</tr>
<tr class="even">
<td>TeleHealth Configurations</td>
<td>Specialty Sub-Types</td>
<td>Data Management specialty sub-types</td>
<td>List of specialty sub types related to each specialty</td>
</tr>
<tr class="odd">
<td>TeleHealth Configurations</td>
<td>Manufacturers</td>
<td>Data Management manufacturers</td>
<td>List of available equipment manufacturers</td>
</tr>
<tr class="even">
<td>TeleHealth Configurations</td>
<td>Models</td>
<td>Metadata Management models</td>
<td>List of available equipment models</td>
</tr>
<tr class="odd">
<td>TeleHealth Configurations</td>
<td>Component Types</td>
<td>Metadata Management component types</td>
<td>List of available component types</td>
</tr>
<tr class="even">
<td>TeleHealth Configurations</td>
<td>Cart Types</td>
<td>Metadata Management cart types</td>
<td>List of available cart types</td>
</tr>
<tr class="odd">
<td>TeleHealth Configurations</td>
<td>Sites</td>
<td>Metadata Management sites</td>
<td>List of VA sites in the Telehealth network</td>
</tr>
<tr class="even">
<td>TeleHealth Configurations</td>
<td>Equipment</td>
<td>Metadata Management equipment</td>
<td>List of available equipment</td>
</tr>
<tr class="odd">
<td>TeleHealth Configurations</td>
<td>Resource Groups</td>
<td>Metadata Management resource groups</td>
<td>List of resources that are bundled together as a group</td>
</tr>
<tr class="even">
<td>TMP Efficiencies</td>
<td>Video on Demand</td>
<td>View all VOD data</td>
<td>View all VOD data initiated from TMP</td>
</tr>
<tr class="odd">
<td>Integrations</td>
<td>VistA</td>
<td>VistA: Appointment Scheduling</td>
<td>Appointments that are scheduled or canceled in the Telehealth Management Platform are automatically updated in VistA. Schedulers are no longer required to enter appointments into VistA after scheduling in the Telehealth Management Platform appointment make/cancel ;<br />
TMP Get Return to Clinic Orders/Consults<br />
TMP Make Appt to VistA<br />
TMP Cancel Appt to VistA<br />
VistA Login</td>
</tr>
<tr class="even">
<td>Integrations</td>
<td>VistA</td>
<td>VistA: Support for multiple VistA Systems</td>
<td>Mapping of VistA systems, stop codes list, etc.</td>
</tr>
<tr class="odd">
<td>Integrations</td>
<td>VistA</td>
<td>VistA: Proxy Add to</td>
<td>Unregistered Veterans who are scheduled through the Telehealth Management Platform will automatically be proxy registered into the distant VistA station.</td>
</tr>
<tr class="even">
<td>Integrations</td>
<td>MVI</td>
<td>Patient retrieval</td>
<td>Realtime</td>
</tr>
<tr class="odd">
<td>Integrations</td>
<td>TMS/IronBow</td>
<td>Component imports (TMS, IronBow)</td>
<td>Periodic batch load</td>
</tr>
<tr class="even">
<td>Integrations</td>
<td>VMR</td>
<td>Virtual Medical Room (VMR)</td>
<td>Realtime</td>
</tr>
<tr class="odd">
<td>Integrations</td>
<td>VVS</td>
<td>Video Visit Service (VVS)</td>
<td>Realtime</td>
</tr>
<tr class="even">
<td>Integrations</td>
<td>VIA</td>
<td>Vista Integration Adapter (VIA) - used to login to Vista stations so HealthShare is dependent on it</td>
<td>Realtime</td>
</tr>
<tr class="odd">
<td>Integrations</td>
<td>CDM</td>
<td>Initial system load of patient data</td>
<td>Initial batch load</td>
</tr>
</tbody>
</table>