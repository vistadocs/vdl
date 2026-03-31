---
consolidated_title: "release notes ves"
app_code: VES
doc_type: RN
master_source: "Release Notes VES 6.5"
master_pub_date: revision_count: 0
consolidated_from: 17 versions
prior_versions:
  - "Release Notes VES 6.11"
  - "Release Notes VES 6.12"
  - "Release Notes VES 6.13"
  - "Release Notes VES 6.14.5"
  - "Release Notes VES 6.14"
  - "Release Notes VES 6.15"
  - "Release Notes VES 6.5.2"
  - "Release Notes VES 6.5.3"
  - "Release Notes VES 6.5.4"
  - "Release Notes VES 6.5.5"
  - "Release Notes VES 6.6.1"
  - "Release Notes VES 6.6"
  - "Release Notes VES 6.7.1"
  - "Release Notes VES 6.7"
  - "Release Notes VES 6.8.1"
  - "Release Notes VES 6.8.2"
---

### Release Notes for VHA Enrollment System - VES v6.5.0

03-20-2023

The mission of the Department of Veteran Affairs (VA) Office of Information and Technology (OIT) Development, Security, and Operations is to provide benefits to Veterans and their families. In order to meet this overarching goal, OIT is charged with providing high quality, effective and efficient IT services and Operations and Maintenance (O&amp;M) to persons and organizations that provide point-of-care services to our Veterans.

The VA’s goals for its Veterans and families include:

- Make it easier for Veterans and their families to receive the right benefits and meeting their expectations for quality, timeliness and responsiveness.
- Improve the quality and accessibility of health care, benefits and memorial services while optimizing value.
- Provide world-class health care delivery, by partnering with each Veteran to create a personalized, proactive strategy to optimize health and well-being, while providing state of the art disease management.
- Ensure awareness and understanding of the personalized, proactive and patient-driven health care model through education and monitoring.
- Provide convenient access to information regarding VA health benefits, medical records, health information, expert advice and ongoing support needed to make informed health decisions and successfully implement the Veteran’s personal health plans.
- Receive timely, high quality, personalized, safe, effective and equitable health care, not dependent upon geography, gender, age, culture, race, or sexual orientation.
- Strengthen collaborations with communities and organizations, such as the Department of Defense (DoD), Department of Health and Human Services (DHHS), academic affiliates and other service organizations.

To assist in meeting these goals, the Eligibility and Enrollment (E&amp;E) program will provide enterprise-wide enhancements and sustainment for the following systems/applications:

- The VHA Enrollment System (VES) is the authoritative system for VA enrollment and Community Care static eligibility determinations.
- Income Verification Match (IVM)/Enrollment Database (EDB) assists in determining priority grouping for health care eligibility.
- Veterans Information Systems and Technology Architecture (VistA) Registration, Eligibility &amp; Enrollment (REE) shares information with other VistA applications and enables registration and preliminary eligibility determinations and enrollment at VA Medical Centers (VAMC). VES makes the final eligibility determinations.

The Veteran’s On-Line Application (VOA), now referred to as Health Care Application (HCA), enables Veterans to self-enroll in VA health care and is another entry point for records to be added to VES.

E&amp;E defines VHA Profiles (VHAP) for which a client (Veteran, Service Member, or beneficiary) is eligible and ties them to the authority for care.

### Change Requests

| **Key**   | **Summary**                                                        |
|-----------|--------------------------------------------------------------------|
| VES-24488 | Add additional eligibility for Agent Orange and Ionizing Radiation |
| VES-24489 | Change the Combat Veteran Eligibility End Date Requirement         |
| VES-25708 | VHAP Copay Effective Date                                          |

### Epics

| **Key**   | **Summary**                                                                |
|-----------|----------------------------------------------------------------------------|
| VES-25772 | Copay Effective Date Analysis & Design - Phase 1 (VES)                     |
| VES-26119 | Change the Combat Veteran Eligibility End Date Requirement (VES)           |
| VES-26602 | Add additional eligibility for Agent Orange and Ionizing Radiation (VES)   |
| VES-27890 | Phase 2 - Remove Z07 Inconsistency Checks from VistA to ES - Analysis (ES) |

### Stories

| **Key**   | **Summary**                                                                           |
|-----------|---------------------------------------------------------------------------------------|
| VES-27141 | Implement Business Rules for CV End Date Calculation                                  |
| VES-27142 | Modification to Enrollment Determination Ruleflow                                     |
| VES-27143 | Batch Process for Cleanup                                                             |
| VES-27147 | Add New Option for AO and IR                                                          |
| VES-27148 | UI Changes for AO/IR Dropdown List Update on Eligibility and Military Service Screens |
| VES-27149 | UI Changes for AO/IR Popup Message for MSE on Military Service Screen                 |
| VES-28429 | Webhelp                                                                               |

### Bugs

| **Key**   | **Summary**                                                                                                    |
|-----------|----------------------------------------------------------------------------------------------------------------|
| VES-28225 | Application Error when update the MSE for enroll status: Rejected (Group G8)                                   |
| VES-28256 | VES6.4.1 eMIS Replacement_MSDS Query Status stays as Pending Response if there is an exception                 |
| VES-28360 | After removed Close Application or Cancelled/Declined enroll status CVE End date is blank                      |
| VES-28550 | VES removed the CVE end date for special enrollment period rule when enroll status is verified group 6         |
| VES-28310 | VES 6.5-VES user is able to select the new AO and IR locations though the corresponding MSE is deleted         |
| VES-28633 | VES 6.5-VES user is able to select the new AO and IR locations though the VET indicator is updated to NO       |
| VES-28780 | VES Modernization: MSDS Status stays in Pending Response for longer time has NPE                               |
| VES-28792 | Update MSDS rule flow to check Combat End Date in Combat Episode and Conflict End Date greater than 11/11/1998 |
| VES-28153 | Profile SVC:VA Profile transaction log displays the transaction status as 'Complete' instead of 'Error'        |
| VES-28535 | VES-Contact-Brk:CI inbound messages are getting set to 2025 instead of 2024                                    |

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: Release Notes VES 6.11

### Release Notes for VHA Enrollment System
VES 6.11.0

10-10-2024

The mission of the Department of Veteran Affairs (VA) Office of Information and Technology (OIT) Development, Security, and Operations is to provide benefits to Veterans and their families. In order to meet this overarching goal, OIT is charged with providing high quality, effective and efficient IT services and Operations and Maintenance (O&amp;M) to persons and organizations that provide point-of-care services to our Veterans.

The VA’s goals for its Veterans and families include:

- Make it easier for Veterans and their families to receive the right benefits and meeting their expectations for quality, timeliness and responsiveness.
- Improve the quality and accessibility of health care, benefits and memorial services while optimizing value.
- Provide world-class health care delivery, by partnering with each Veteran to create a personalized, proactive strategy to optimize health and well-being, while providing state of the art disease management.
- Ensure awareness and understanding of the personalized, proactive and patient-driven health care model through education and monitoring.
- Provide convenient access to information regarding VA health benefits, medical records, health information, expert advice and ongoing support needed to make informed health decisions and successfully implement the Veteran’s personal health plans.
- Receive timely, high quality, personalized, safe, effective and equitable health care, not dependent upon geography, gender, age, culture, race, or sexual orientation.
- Strengthen collaborations with communities and organizations, such as the Department of Defense (DoD), Department of Health and Human Services (DHHS), academic affiliates and other service organizations.

To assist in meeting these goals, the Eligibility and Enrollment (E&amp;E) program will provide enterprise-wide enhancements and sustainment for the following systems/applications:

- The VHA Enrollment System (VES) is the authoritative system for VA enrollment and Community Care static eligibility determinations.
- Income Verification Match (IVM)/Enrollment Database (EDB) assists in determining priority grouping for health care eligibility.
- Veterans Information Systems and Technology Architecture (VistA) Registration, Eligibility &amp; Enrollment (REE) shares information with other VistA applications and enables registration and preliminary eligibility determinations and enrollment at VA Medical Centers (VAMC). VES makes the final eligibility determinations.

The Veteran’s On-Line Application (VOA), now referred to as Health Care Application (HCA), enables Veterans to self-enroll in VA health care and is another entry point for records to be added to VES.

E&amp;E defines VHA Profiles (VHAP) for which a client (Veteran, Service Member, or beneficiary) is eligible and ties them to the authority for care.

### From: Release Notes VES 6.12

## Release Notes for VHA Enrollment System - VES 6.12.0

2-27-2025

The mission of the Department of Veteran Affairs (VA) Office of Information and Technology (OIT) Development, Security, and Operations is to provide benefits to Veterans and their families. In order to meet this overarching goal, OIT is charged with providing high quality, effective and efficient IT services and Operations and Maintenance (O&amp;M) to persons and organizations that provide point-of-care services to our Veterans.

The VA’s goals for its Veterans and families include:

- Make it easier for Veterans and their families to receive the right benefits and meeting their expectations for quality, timeliness and responsiveness.
- Improve the quality and accessibility of health care, benefits and memorial services while optimizing value.
- Provide world-class health care delivery, by partnering with each Veteran to create a personalized, proactive strategy to optimize health and well-being, while providing state of the art disease management.
- Ensure awareness and understanding of the personalized, proactive and patient-driven health care model through education and monitoring.
- Provide convenient access to information regarding VA health benefits, medical records, health information, expert advice and ongoing support needed to make informed health decisions and successfully implement the Veteran’s personal health plans.
- Receive timely, high quality, personalized, safe, effective and equitable health care, not dependent upon geography, gender, age, culture, race, or sexual orientation.
- Strengthen collaborations with communities and organizations, such as the Department of Defense (DoD), Department of Health and Human Services (DHHS), academic affiliates and other service organizations.

To assist in meeting these goals, the Eligibility and Enrollment (E&amp;E) program will provide enterprise-wide enhancements and sustainment for the following systems/applications:

- The VHA Enrollment System (VES) is the authoritative system for VA enrollment and Community Care static eligibility determinations.
- Income Verification Match (IVM)/Enrollment Database (EDB) assists in determining priority grouping for health care eligibility.
- Veterans Information Systems and Technology Architecture (VistA) Registration, Eligibility &amp; Enrollment (REE) shares information with other VistA applications and enables registration and preliminary eligibility determinations and enrollment at VA Medical Centers (VAMC). VES makes the final eligibility determinations.

The Veteran’s On-Line Application (VOA), now referred to as Health Care Application (HCA), enables Veterans to self-enroll in VA health care and is another entry point for records to be added to VES.

E&amp;E defines VHA Profiles (VHAP) for which a client (Veteran, Service Member, or beneficiary) is eligible and ties them to the authority for care.

### Change Requests

| **Key**   | **Summary**                                                                       |
|-----------|-----------------------------------------------------------------------------------|
| VES-9599  | Automate Employee Only and Employee Veteran VHAPs                                 |
| VES-24470 | Create Registration Only Form on va.gov                                           |
| VES-27342 | Add 180-Day Grace Period Indicator in Eligibility Screens                         |
| VES-28740 | Control Number of Records that Enter "Pending Review" Status to "Verified" Status |
| VES-28742 | Other Health Insurance (OHI) - Private - Eligibility Plus File                    |
| VES-29727 | Remove Rule that Blocks Multiple Transmissions to CCN for Records with VCE X      |
| VES-36767 | Enter, Store & View Comments for VFMP Sponsor or Beneficiary                      |
| VES-36906 | Search & View Historical Correspondence in VFMP System                            |
| VES-39195 | Automate TERA Eligibility                                                         |
| VES-39681 | Enable Confidential Address                                                       |
| VES-39869 | Personalized Handbook - TERA Indicator                                            |
| VES-42563 | Migrate OHI History from CP&E to VES                                              |
| VES-48353 | Create New VES User Role                                                          |
| VES-52629 | Change Member ID Label in VES                                                     |

### Epics

| **Key**   | **Summary**                                                                                                  | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|-----------|--------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VES-9770  | Automate Employee Only and Employee Veteran VHAPs                                                            | These carveout VHAPs currently exist as manuals in VES. This CR is a request for to automate them.  - Employee Only (Emp O) - carveout VHAP will have "Humanitarian" core VHAP. - Employee Veteran (Emp Vet) carveout VHAP will have one of the defined Veteran core VHAPs.  VES and Health Information Exchange (HIE) require unique VHAPs to meet requirements.                                                                                                                                           |
| VES-20919 | Receive Applications in VFMP System from Online Portal                                                       | CP&amp;E  As a VFMP Eligibility system User, I need the ability to receive applications/registrations for enrollment in VFMP programs from an online/web portal, so that I can support application and eligibility updates.                                                                                                                                                                                                                                                                                 |
| VES-20938 | Associate Pages of Electronic File to Person in VFMP System (Document Management)                            | CP&amp;E  As a VFMP Eligibility system, I need the ability to associate an electronic image/file to a person(s) within the enrollment system, so that I can associate an image/file to a person(s) within the enrollment system.                                                                                                                                                                                                                                                                            |
| VES-20952 | Assign Denial Reason to CHAMPVA Records in VFMP System                                                       | CP&amp;E  As a VFMP Eligibility system, I need the ability to create a denial reason and discontinue processing eligibility for Standard CHAMPVA, so that I can create a denial reason and discontinue processing eligibility when the categories for eligibility are not met.                                                                                                                                                                                                                              |
| VES-20953 | Generate and Send Denial Letter to Person in VFMP System                                                     | CP&amp;E  As a VFMP Eligibility system, I need the ability to generate notification correspondence indicating the reason(s) for denial and appeal rights, so that I can communicate via correspondence reasons for denial and appeal rights.                                                                                                                                                                                                                                                                |
| VES-20954 | Generate and Send Acceptance/Approval Letter with ID Card to Person in VFMP System                           | CP&amp;E  As a VFMP Eligibility system, I need the ability to generate notification correspondence indicating the enrollment status of "eligible" as well as additional instructions and ID card, so that I can generate notification correspondence of enrollment "eligible" and additional instructions with an ID card to the applicant.                                                                                                                                                                 |
| VES-20956 | Provide Ability to Update and Record Eligibility Status Changes in VFMP System                               | CP&amp;E  As a VFMP Eligibility system, I need the ability to provide the ability to record changes in eligibility status as the result of updated information received from authoritative sources, so that I can update information received from authoritative sources.                                                                                                                                                                                                                                   |
| VES-20966 | Re-calculate Person for Medicare Verification in VFMP System                                                 | CP&amp;E  As a VFMP Eligibility system, I need the ability to re-calculate Medicare Eligibility for persons selected for Medicare Verification and disentitle or reinstate the person from CHAMPVA based on business rules, so that I can update the applicant's eligibility.                                                                                                                                                                                                                               |
| VES-20968 | Generate Medicare Enrollment Correspondence in VFMP System                                                   | CP&amp;E  As a VFMP Eligibility system, I need the ability to generate Medicare Enrollment Requirement correspondence prior to the person's 65th birthday, so that I can send correspondence to the beneficiary regarding Medicare Enrollment Requirements.                                                                                                                                                                                                                                                 |
| VES-20972 | Receive Unsolicited VBA Data in VFMP System                                                                  | CP&amp;E  As a VFMP Eligibility system, I need the ability to receive unsolicited information that is a result of updates to Veteran and/or beneficiary/dependent information from the VBA system, so that I can determine eligibility.                                                                                                                                                                                                                                                                     |
| VES-20973 | Receive Notifications from VBA in VFMP System                                                                | CP&amp;E  As a VFMP Eligibility system, I need the ability to receive notifications from VBA systems when a relevant change is made that impacts VFMP eligibility, so that I can determine eligibility.                                                                                                                                                                                                                                                                                                     |
| VES-20977 | Re-Qualify a Sponsor After Receiving Unsolicited VBA Data in VFMP System                                     | CP&amp;E  As a VFMP Eligibility system, I need the ability to "re-qualify" a sponsor (Veteran)/dependent upon receipt of unsolicited VBA information, so that I can determine eligibility.                                                                                                                                                                                                                                                                                                                  |
| VES-20978 | Disentitle All Dependents Associated with an Unqualified Sponsor in VFMP System based on VBA data            | CP&amp;E  As a VFMP Eligibility system, I need the ability to disentitle all dependents associated to a sponsor who is determined to be "unqualified", upon receipt of unsolicited VBA information, so that I can determine eligibility.                                                                                                                                                                                                                                                                    |
| VES-20979 | Reprocess Eligibility for All Dependents Identified in Unsolicited VBA Updates in VFMP System                | CP&amp;E  As a VFMP Eligibility system, I need the ability to re-process eligibility for the dependents identified by VBA upon receipt of unsolicited VBA information, so that I can determine eligibility.                                                                                                                                                                                                                                                                                                 |
| VES-20980 | Disentitle Ineligible Beneficiary Identified in Unsolicited VBA Data in VFMP System                          | CP&amp;E  As a VFMP Eligibility system, I need the ability to disentitle a beneficiary who is determined to be "ineligible", upon receipt of unsolicited VBA information, so that I can determine eligibility.                                                                                                                                                                                                                                                                                              |
| VES-21003 | Register VFMP Person in Meds by Mail Group via Interface (TBD)                                               | CP&amp;E  As a VFMP Eligibility system, I need the ability to register a person who is enrolled in Standard, Caregiver CHAMPVA, SB or CWVV plan, in the Meds by Mail group, so that I can update eligibility.                                                                                                                                                                                                                                                                                               |
| VES-21005 | Register Specific Enrolled Persons to Pharmacy Benefits Manager via Eligibility Plus file                    | CP&amp;E  As a VFMP Eligibility system, I need the ability to register a person who is enrolled in the Standard, Caregiver CHAMPVA, SB or CWVV plan, in the PHARMACY BENEFIT MANAGER group, so that I can determine eligibility.                                                                                                                                                                                                                                                                            |
| VES-21010 | Provide Request and Response Capability to EE Service-For MVP, users can view fields within ES when queried. | CP&amp;E  As a VFMP Eligibility system, I need the ability to prepare and return a response to a request or query for the Eligibility-Enrollment (E/E) information to determine member's enrollment status in any/all OCC Health Care Plans/ Groups, so that I can determine eligibility.                                                                                                                                                                                                                   |
| VES-21048 | Store and Associate Correspondence with Person in VFMP System                                                | CP&amp;E  As a VFMP Eligibility system, I need the ability to electronically store and associate with the record all generated correspondence, so that I can generate correspondence for eligibility.                                                                                                                                                                                                                                                                                                       |
| VES-21058 | Send Automatic Denial Correspondence from VFMP System                                                        | CP&amp;E  As a VFMP Eligibility system, I need the ability to send automatic denial correspondence based on the specific denial reason to comply with the Appeals Modernization process, so that I can send automatic denial correspondence for eligibility.                                                                                                                                                                                                                                                |
| VES-21071 | Receive and Process VBA Data in VFMP System                                                                  | CP&amp;E  As a VFMP Eligibility system, I need the ability to receive and process VBA data/information that is the result of a query, so that I can manage data/information for eligibility.                                                                                                                                                                                                                                                                                                                |
| VES-21072 | Receive and Process VBA Data for CHAMPVA Applicants in VFMP System                                           | CP&amp;E  As a VFMP Eligibility system, I need the ability to receive and process unsolicited VBA data/information that is the result of an update that occurs at the VBA for persons who are enrolled in or who have applied for Standard CHAMPVA, so that I can manage data/information for eligibility.                                                                                                                                                                                                  |
| VES-21073 | Provide Ability to Query VBA Data for Persons of Interest in VFMP System                                     | CP&amp;E  As a VFMP Eligibility system, I need the ability to query VBA information for persons of interest during a periodic review of eligibility in the Standard CHAMPVA program, so that I can manage data/information for eligibility.                                                                                                                                                                                                                                                                 |
| VES-21074 | Interface with the Customer Relations Manager (CRM) System from VFMP System                                  | CP&amp;E  As a VFMP Eligibility system, I need the ability to interface with the Customer Relations Manager (CRM) system to support customer service activities, so that I can manage data/information for eligibility.                                                                                                                                                                                                                                                                                     |
| VES-21087 | Transmit Electronic Eligibility File to Meds by Mail System from VFMP System (via PED TAS)                   | CP&amp;E  As a VFMP Eligibility system, I need the ability to transmit an electronic file, containing eligibility information to Meds by Mail, so that I can manage data/information for eligibility.                                                                                                                                                                                                                                                                                                       |
| VES-21108 | Provide Ability to Send Daily Eligibility File to ClaimsXM via PEDTAS                                        | CP&amp;E  As a VFMP Eligibility system, I need the ability to transmit a daily electronic file, containing eligibility information to ClaimsXM, so that I can manage data/information for eligibility.                                                                                                                                                                                                                                                                                                      |
| VES-21111 | Provide Ability to Send Daily OHI File to VFMP Vendorization System from VFMP System (Elig. Plus File)       | CP&amp;E  As a VFMP Eligibility system, I need the ability to transmit a daily electronic file, containing changes to all Other Health Insurance (OHI) information to the vendorization system for Family Member Programs, so that I can manage data/information for eligibility.                                                                                                                                                                                                                           |
| VES-21126 | View OHI Data for Persons within VFMP System                                                                 | CP&amp;E  As a VFMP Eligibility system, I need the ability to view OHI information for a person, so that I can manage data/information for eligibility.                                                                                                                                                                                                                                                                                                                                                     |
| VES-21348 | CP&E Migration for CHAMPVA Standard (M-Development)                                                          | CP&amp;E  Migration of CHAMPVA Standard                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| VES-21637 | Process CHAMPVA Medicare Rules Phase 2                                                                       | CP&amp;E  Process CHAMPVA Medicare Rules Phase 2                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| VES-23169 | Send CP&E Eligibility Plus Files                                                                             | CP&amp;E  Send CP&amp;E Eligibility Plus Files                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| VES-28746 | Add OHI Information Existing Record                                                                          | CP&amp;E  As an OHI team member, I need the ability to add new insurance carriers to a beneficiary record, so that I can record new carriers for coordination of benefits.                                                                                                                                                                                                                                                                                                                                  |
| VES-28748 | Select OHI Plan Type                                                                                         | CP&amp;E  As an OHI team member, I need the ability to select an option from a list of recognized plan types, so that I can provide more information on the OHI.                                                                                                                                                                                                                                                                                                                                            |
| VES-28749 | Update Existing OHI Entries                                                                                  | CP&amp;E  As an OHI team member, I need the ability to update existing insurance carrier information, so that I can maintain an accurate record of OHI coverage.                                                                                                                                                                                                                                                                                                                                            |
| VES-28750 | Capture Beneficiary OHI History                                                                              | CP&amp;E  As an OHI team member, I need the ability to capture the history of updates made to a beneficiary's OHI record, so that I can monitor changes to the record and review individual employee work for quality assurance.                                                                                                                                                                                                                                                                            |
| VES-28751 | Delete Insurance Information                                                                                 | CP&amp;E  As an OHI team member, I need the ability to delete insurance information from a beneficiary's record, so that I can correct input errors.                                                                                                                                                                                                                                                                                                                                                        |
| VES-29703 | Eligibility End and Restart Changes (all VFMPs)                                                              | CP&amp;E  Eligibility End and Restart Changes                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| VES-32062 | Remove Rule that Blocks Multiple Transmissions to CCN for Records with VCE X                                 | Desired Functionality: As Office of Integrated Veteran Care (IVC) Community Care (CC) staff, I need CCN to receive the updated information for an ineligible individual previously shared with CCN, so CCN can process their claim using the most up-to-date information.                                                                                                                                                                                                                                   |
| VES-36764 | Create Registration Only Form Microservice - Phase 2                                                         | Desired Functionality: The online form will be a short form to collect the Veterans information Name, SSN, DOB, Address, Phone Number, Military Service Dates and Type of Registry Exam they are requesting. This information will feed into VES and place the Veteran in a Registration Only status if they do not wish to enroll. If the Veteran is already known to the system, we will capture the type of Registry Exam being requested. This will feed into future functionality listed in VES-24423. |
| VES-39220 | Automate TERA Eligibility (Phase 1 of 2)                                                                     | VES to automatically assign the TERA Indicator.                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| VES-42467 | Personalized handbook - TERA Indicator                                                                       | Desired Functionality: If Priority Group (PG) equals 6 and the TERA indicator equals YES, then display verbiage "Toxic Exposure Risk Activity" in the handbook and the insert letter FL400b.                                                                                                                                                                                                                                                                                                                |
| VES-43280 | VFMP View Eligibility Plus File Transmission Log                                                             | CP&amp;E  VFMP View Eligibility Plus File Transmission Log                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| VES-43798 | VFMP Add History Screens                                                                                     | CP&amp;E  VFMP Add History Screens                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| VES-43801 | VFMP Migration Updates - Correspondence History                                                              | CP&amp;E  VFMP Migration Updates - Correspondence History                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| VES-43803 | VFMP Determine CHAMPVA 180-Day Grace Period - Integration                                                    | CP&amp;E  VFMP Determine CHAMPVA 180-Day Grace Period                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| VES-48950 | Enforce Confidential and Temporary Address with Phone Number                                                 | Enforce Confidential and Temporary Address with Phone Number                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| VES-48958 | Create new VES user role                                                                                     | Create a new VES user role specific to Non-Medical Care Collection Fund (MCCF) Consolidated Patient Account Centers (CPAC) staff who have a business need to modify eligibility based on authoritative data from outside non-MCCF CPAC only sources.                                                                                                                                                                                                                                                        |
| VES-50747 | VES CP&E 508 Testing for Phase II                                                                            | CP&amp;E  508 Testing                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| VES-51402 | VFMP Migration Updates - Store Foreign Phone in Comments                                                     | CP&amp;E  VFMP Migration Updates - Store Foreign Phone in Comments                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| VES-51403 | VFMP Eligibility Plus Updates - OHI Eligibility Plus File Integration                                        | CP&amp;E  VFMP Eligibility Plus Updates - OHI Eligibility Plus File Integration                                                                                                                                                                                                                                                                                                                                                                                                                             |
| VES-52820 | Change Member ID Label in VES                                                                                | Change the Member ID label in VES on the Veteran Search Screen and on the Banner to reflect “Member ID (EDIPI).                                                                                                                                                                                                                                                                                                                                                                                             |

### Bugs

| **Key**   | **Summary**                                                                |
|-----------|----------------------------------------------------------------------------|
| VES-46153 | Facility Type RO-OC incorrectly displays as inactive and is not selectable |

### From: Release Notes VES 6.7.1

### Release Notes for VHA Enrollment System - VES 6.7.1

10-30-2023

The mission of the Department of Veteran Affairs (VA) Office of Information and Technology (OIT) Development, Security, and Operations is to provide benefits to Veterans and their families. In order to meet this overarching goal, OIT is charged with providing high quality, effective and efficient IT services and Operations and Maintenance (O&amp;M) to persons and organizations that provide point-of-care services to our Veterans.

The VA’s goals for its Veterans and families include:

- Make it easier for Veterans and their families to receive the right benefits and meeting their expectations for quality, timeliness and responsiveness.
- Improve the quality and accessibility of health care, benefits and memorial services while optimizing value.
- Provide world-class health care delivery, by partnering with each Veteran to create a personalized, proactive strategy to optimize health and well-being, while providing state of the art disease management.
- Ensure awareness and understanding of the personalized, proactive and patient-driven health care model through education and monitoring.
- Provide convenient access to information regarding VA health benefits, medical records, health information, expert advice and ongoing support needed to make informed health decisions and successfully implement the Veteran’s personal health plans.
- Receive timely, high quality, personalized, safe, effective and equitable health care, not dependent upon geography, gender, age, culture, race, or sexual orientation.
- Strengthen collaborations with communities and organizations, such as the Department of Defense (DoD), Department of Health and Human Services (DHHS), academic affiliates and other service organizations.

To assist in meeting these goals, the Eligibility and Enrollment (E&amp;E) program will provide enterprise-wide enhancements and sustainment for the following systems/applications:

- The VHA Enrollment System (VES) is the authoritative system for VA enrollment and Community Care static eligibility determinations.
- Income Verification Match (IVM)/Enrollment Database (EDB) assists in determining priority grouping for health care eligibility.
- Veterans Information Systems and Technology Architecture (VistA) Registration, Eligibility &amp; Enrollment (REE) shares information with other VistA applications and enables registration and preliminary eligibility determinations and enrollment at VA Medical Centers (VAMC). VES makes the final eligibility determinations.

The Veteran’s On-Line Application (VOA), now referred to as Health Care Application (HCA), enables Veterans to self-enroll in VA health care and is another entry point for records to be added to VES.

E&amp;E defines VHA Profiles (VHAP) for which a client (Veteran, Service Member, or beneficiary) is eligible and ties them to the authority for care.

### From: Release Notes VES 6.8.1

## Release Notes for VHA Enrollment System - VES 6.8.1

02-20-2024

The mission of the Department of Veteran Affairs (VA) Office of Information and Technology (OIT) Development, Security, and Operations is to provide benefits to Veterans and their families. In order to meet this overarching goal, OIT is charged with providing high quality, effective and efficient IT services and Operations and Maintenance (O&amp;M) to persons and organizations that provide point-of-care services to our Veterans.

The VA’s goals for its Veterans and families include:

- Make it easier for Veterans and their families to receive the right benefits and meeting their expectations for quality, timeliness and responsiveness.
- Improve the quality and accessibility of health care, benefits and memorial services while optimizing value.
- Provide world-class health care delivery, by partnering with each Veteran to create a personalized, proactive strategy to optimize health and well-being, while providing state of the art disease management.
- Ensure awareness and understanding of the personalized, proactive and patient-driven health care model through education and monitoring.
- Provide convenient access to information regarding VA health benefits, medical records, health information, expert advice and ongoing support needed to make informed health decisions and successfully implement the Veteran’s personal health plans.
- Receive timely, high quality, personalized, safe, effective and equitable health care, not dependent upon geography, gender, age, culture, race, or sexual orientation.
- Strengthen collaborations with communities and organizations, such as the Department of Defense (DoD), Department of Health and Human Services (DHHS), academic affiliates and other service organizations.

To assist in meeting these goals, the Eligibility and Enrollment (E&amp;E) program will provide enterprise-wide enhancements and sustainment for the following systems/applications:

- The VHA Enrollment System (VES) is the authoritative system for VA enrollment and Community Care static eligibility determinations.
- Income Verification Match (IVM)/Enrollment Database (EDB) assists in determining priority grouping for health care eligibility.
- Veterans Information Systems and Technology Architecture (VistA) Registration, Eligibility &amp; Enrollment (REE) shares information with other VistA applications and enables registration and preliminary eligibility determinations and enrollment at VA Medical Centers (VAMC). VES makes the final eligibility determinations.

The Veteran’s On-Line Application (VOA), now referred to as Health Care Application (HCA), enables Veterans to self-enroll in VA health care and is another entry point for records to be added to VES.

E&amp;E defines VHA Profiles (VHAP) for which a client (Veteran, Service Member, or beneficiary) is eligible and ties them to the authority for care.

### Change Requests

| **Key**   | **Summary**                                                                               |
|-----------|-------------------------------------------------------------------------------------------|
| VES-38125 | Captain James A. Lovell Federal Health Care Center (FHCC) Batch Registration for Recruits |

### Epics

| **Key**   | **Summary**        | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|-----------|--------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VES-38015 | FHCC Batch Process | The batch registration process is where recruits are being registered in the joint patient registration system. This allows the recruits to be jointly registered in both the local Composite Health Care System (CHCS) and VistA, correlated with VA & DoD identity enterprise applications for orders portability for labs, radiology and consults. This enables these orders to cross between the DoD and VA electronic health records (EHRs). There are 40,000 recruits processed by the facility who receive medical, dental and ancillary services annually. In addition, there are 5,000 other active-duty personnel here for advanced training that receive care and 15,000 more that are serviced remotely. |

### Bugs

| **Key**   | **Summary**                                                                 |
|-----------|-----------------------------------------------------------------------------|
| VES-39033 | Null pointer exception on ineligible type for previously ineligible records |

### From: Release Notes VES 6.13

## Release Notes for VHA Enrollment System - VES 6.13.0

05-27-2025

The mission of the Department of Veteran Affairs (VA) Office of Information and Technology (OIT) Development, Security, and Operations is to provide benefits to Veterans and their families. In order to meet this overarching goal, OIT is charged with providing high quality, effective and efficient IT services and Operations and Maintenance (O&amp;M) to persons and organizations that provide point-of-care services to our Veterans.

The VA’s goals for its Veterans and families include:

- Make it easier for Veterans and their families to receive the right benefits and meeting their expectations for quality, timeliness and responsiveness.
- Improve the quality and accessibility of health care, benefits and memorial services while optimizing value.
- Provide world-class health care delivery, by partnering with each Veteran to create a personalized, proactive strategy to optimize health and well-being, while providing state of the art disease management.
- Ensure awareness and understanding of the personalized, proactive and patient-driven health care model through education and monitoring.
- Provide convenient access to information regarding VA health benefits, medical records, health information, expert advice and ongoing support needed to make informed health decisions and successfully implement the Veteran’s personal health plans.
- Receive timely, high quality, personalized, safe, effective and equitable health care, not dependent upon geography, gender, age, culture, race, or sexual orientation.
- Strengthen collaborations with communities and organizations, such as the Department of Defense (DoD), Department of Health and Human Services (DHHS), academic affiliates and other service organizations.

To assist in meeting these goals, the Veteran Experience Services Enrollment and Eligibility (VESEE) program will provide enterprise-wide enhancements and sustainment for the following systems/applications:

- The VHA Enrollment System (VES) is the authoritative system for VA enrollment and Community Care static eligibility determinations.
- Income Verification Match (IVM)/Enrollment Database (EDB) assists in determining priority grouping for health care eligibility.
- Veterans Information Systems and Technology Architecture (VistA) Registration, Eligibility &amp; Enrollment (REE) shares information with other VistA applications and enables registration and preliminary eligibility determinations and enrollment at VA Medical Centers (VAMC). VES makes the final eligibility determinations.

The Veteran’s On-Line Application (VOA), now referred to as Health Care Application (HCA), enables Veterans to self-enroll in VA health care and is another entry point for records to be added to VES.

VESEE defines VHA Profiles (VHAP) for which a client (Veteran, Service Member, or beneficiary) is eligible and ties them to the authority for care.

### Change Requests

| **Key**   | **Summary**                                                                                          |
|-----------|------------------------------------------------------------------------------------------------------|
| VES-28738 | Meds by Mail (MbM) Indicator - Veteran Family Medical Program (VFMP) Meds by Mail Eligibility Status |
| VES-28740 | Control the Number of Records that Enter a "Pending Review" Status to "Verified" Status              |
| VES-28742 | Other Health Insurance (OHI) - Private - Eligibility Plus File                                       |
| VES-33122 | Allow Edit to Community Care (CC) Determination Date                                                 |
| VES-40556 | Create New Audit ID for Online 10-10EZR - Toxic Exposure Risk Activity (TERA) Updates                |
| VES-40586 | VBA Auto Registration                                                                                |
| VES-46416 | Restrict Southwest (SW) Asia Conditions Eligibility                                                  |
| VES-46769 | Allow Saving of Tribal Affiliation Start Date in VES when Veteran is Deceased                        |
| VES-54724 | Data Access Service (DAS) Connection for VFMP Print Vendor                                           |

### Epics

| **Key**   | **Summary**                                                                                                  | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|-----------|--------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VES-20919 | Receive Applications in VFMP System from Online Portal                                                       | CP&amp;E  As a VFMP Eligibility system User, I need the ability to receive applications/registrations for enrollment in VFMP programs from an online/web portal, so that I am able to support application and eligibility updates.                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| VES-21003 | Register VFMP Person in Meds by Mail Group via Interface                                                     | CP&amp;E  As a VFMP Eligibility system, I need the ability to register a person who is enrolled in Standard, Caregiver Civilian Health and Medical Program of the Department of Veterans Affairs (CHAMPVA), Spina Bifida (SB) or Children of Women Vietnam Veterans (CWVV) plan, in the MEDS BY MAIL group, so that I can update eligibility.                                                                                                                                                                                                                                                                                                                                    |
| VES-21005 | Register Specific Enrolled Persons to Pharmacy Benefits Manager via Eligibility Plus file                    | CP&amp;E  As a VFMP Eligibility system, I need the ability to register a person who is enrolled in the Standard, Caregiver CHAMPVA, SB or CWVV plan, in the PHARMACY BENEFIT MANAGER group, so that I can determine eligibility.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| VES-21010 | Provide Request and Response Capability to EE Service-For MVP, users can view fields within ES when queried. | CP&amp;E  As a VFMP Eligibility system, I need the ability to prepare and return a response to a request or query for the Eligibility-Enrollment (E/E) information to determine member's enrollment status in any/all OFFICE OF COMMUNITY CARE (OCC) HEALTH CARE Plans/ Groups, so that I can determine eligibility.                                                                                                                                                                                                                                                                                                                                                             |
| VES-21074 | Interface with the Customer Relations Manager (CRM) System from VFMP System                                  | CP&amp;E  As a VFMP Eligibility system, I need the ability to interface with the Customer Relations Manager (CRM) system to support customer service activities, so that I can manage data/information for eligibility.                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| VES-21087 | Transmit Electronic Eligibility File to Meds by Mail System from VFMP System (via PED TAS)                   | CP&amp;E  As a VFMP Eligibility system, I need the ability to transmit an electronic file, containing eligibility information to Meds by Mail, so that I can manage data/information for eligibility.                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| VES-21108 | Provide Ability to Send Daily Eligibility File to ClaimsXM via PEDTAS                                        | CP&amp;E  As a VFMP Eligibility system, I need the ability to transmit a daily electronic file, containing eligibility information to ClaimsXM, so that I can manage data/information for eligibility.                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| VES-21111 | Provide Ability to Send Daily OHI File to VFMP Vendorization System from VFMP System (Eligibility Plus File) | CP&amp;E  As a VFMP Eligibility system, I need the ability to transmit a daily electronic file, containing changes to all OHI information to the vendorization system for Family Member Programs, so that I can manage data/information for eligibility.                                                                                                                                                                                                                                                                                                                                                                                                                         |
| VES-21348 | CP&E Migration for CHAMPVA Standard (M-Development)                                                          | CP&amp;E  Migration of CHAMPVA Standard.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| VES-23169 | Send CP&E Eligibility Plus Files                                                                             | CP&amp;E  Send CP&amp;E Eligibility Plus Files.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| VES-26752 | Disable Existing CHAMPVA Fields within the VES Interface                                                     | CP&amp;E  Disable Existing CHAMPVA fields within the VES Interface.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| VES-28748 | Select OHI Plan Type                                                                                         | CP&amp;E  As an OHI team member, I need the ability to select an option from a list of recognized plan types, so that I can provide more information on the OHI.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| VES-41366 | VBA-Auto Registration 1.0.0                                                                                  | Desired Functionality: Create a Registration Only record if the Veteran or service member is not known to VES and set the Registration Only reason to C&P Exam.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| VES-43132 | Create New Work Item and Audit Trail for Online 1010EZ & 1010EZR TERA Update (Phase 2 of 2)                  | Adding of EZ/R notification events to VES.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| VES-46763 | Allow Edit to CC Determination Date                                                                          | Desired Functionality:  1. As OIT VES Administrator, I need the capability to assign to certain VES Integrated Veteran Care (IVC) users the permission allowing them to edit the date in the CC Determination Date field, so staff can resolve claims issues for Veteran or Collateral of Veteran. 2. As VES IVC user with appropriate permission, I need to be able to update the fields that allows editing of the CC Determination Date and capture of justification for edit, so I can resolve issue with date a Community Care eligibility became established and make available to systems and TPA processing the claims of Veterans, Collateral of Veteran, or providers. |
| VES-48959 | Restrict SW Asia Conditions Eligibility - VES                                                                | Desired Functionality:  1. As a VES user I should only be allowed to add SW Asia Conditions to Veterans who have served during a timeframe that matches August 2, 1990, through November 11, 1998. 2. As A VES user if a military service episode is null, I should not be allowed to add SW Asia Conditions. 3. As a VES user if a military service episode is incomplete, I should not be allowed to add SW Asia Conditions.                                                                                                                                                                                                                                                   |
| VES-51403 | VFMP Eligibility Plus Updates - OHI Eligibility Plus File Integration                                        | CP&amp;E  VFMP Eligibility Plus Updates - OHI Eligibility Plus File Integration.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |

### Bugs

| **Key**   | **Summary**                                                                                                |
|-----------|------------------------------------------------------------------------------------------------------------|
| VES-23856 | VES Triggering Messages to 200CRNR ID                                                                      |
| VES-27317 | Wrong period of service assigned for active duty sharing agreement                                         |
| VES-30815 | Health Level 7 (HL7) ORU~Z06 ZMT segment is empty                                                          |
| VES-39653 | Pending reason not being cleared out when eligibility is verified                                          |
| VES-41627 | Failed to invoke rule flow “ProcessVBAFromMVR”                                                             |
| VES-42434 | Duplicate Other Than Honorable Ch. 17 Letter (IB 10-1661)                                                  |
| VES-46741 | Z04 message from Community Care Network (CCN) OHI has subscriber name in wrong format for spouse insurance |
| VES-47277 | Null pointer exception on GMT Threshold Form                                                               |
| VES-50692 | Date of Marriage not printing on 10-10EZ                                                                   |
| VES-51914 | “scheduledJob.UserProfileAccountLockProcess” is missing criteria for never login                           |
| VES-54998 | Date of Marriage not printing on 10-10EZR                                                                  |
| VES-56233 | Federal Health Care Center (FHCC) active-duty registration process incorrectly defaulting birth sex        |

### From: Release Notes VES 6.14

## Release Notes for VHA Enrollment System - VES 6.14.0

08-18-2025

The mission of the Department of Veteran Affairs (VA) Office of Information and Technology (OIT) Development, Security, and Operations is to provide benefits to Veterans and their families. In order to meet this overarching goal, OIT is charged with providing high quality, effective and efficient IT services and Operations and Maintenance (O&amp;M) to persons and organizations that provide point-of-care services to our Veterans.

The VA’s goals for its Veterans and families include:

- Make it easier for Veterans and their families to receive the right benefits and meeting their expectations for quality, timeliness and responsiveness.
- Improve the quality and accessibility of health care, benefits and memorial services while optimizing value.
- Provide world-class health care delivery, by partnering with each Veteran to create a personalized, proactive strategy to optimize health and well-being, while providing state of the art disease management.
- Ensure awareness and understanding of the personalized, proactive and patient-driven health care model through education and monitoring.
- Provide convenient access to information regarding VA health benefits, medical records, health information, expert advice and ongoing support needed to make informed health decisions and successfully implement the Veteran’s personal health plans.
- Receive timely, high quality, personalized, safe, effective and equitable health care, not dependent upon geography, gender, age, culture, race, or sexual orientation.
- Strengthen collaborations with communities and organizations, such as the Department of Defense (DoD), Department of Health and Human Services (DHHS), academic affiliates and other service organizations.

To assist in meeting these goals, the Veteran Experience Services Enrollment and Eligibility (VESEE) program will provide enterprise-wide enhancements and sustainment for the following systems/applications:

- The VHA Enrollment System (VES) is the authoritative system for VA enrollment and Community Care static eligibility determinations.
- Income Verification Match (IVM)/Enrollment Database (EDB) assists in determining priority grouping for health care eligibility.
- Veterans Information Systems and Technology Architecture (VistA) Registration, Eligibility &amp; Enrollment (REE) shares information with other VistA applications and enables registration and preliminary eligibility determinations and enrollment at VA Medical Centers (VAMC). VES makes the final eligibility determinations.

The Veteran’s On-Line Application (VOA), now referred to as Health Care Application (HCA), enables Veterans to self-enroll in VA health care and is another entry point for records to be added to VES.

VESEE defines VHA Profiles (VHAP) for which a client (Veteran, Service Member, or beneficiary) is eligible and ties them to the authority for care.

### Change Requests

| **Key**   | **Summary**                                                                    |
|-----------|--------------------------------------------------------------------------------|
| VES-18141 | Add and Change Letters                                                         |
| VES-30671 | Enable VistA systems with the Address Override Functionality (VES web service) |
| VES-39195 | Automate Toxic Exposure Risk Activity (TERA) Eligibility                       |
| VES-46416 | Restrict Southwest (SW) Asia Conditions Eligibility                            |
| VES-58086 | Update Document Management Options                                             |

### Epics

| **Key**   | **Summary**                                                                    | **Description**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|-----------|--------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VES-32979 | Add and Change Letters (Phase 3)                                               | The following letters require a new Interface Control Document (ICD) creation and input to VES:  - IB-10-1442 Creditable Coverage Letter - IB-10-1432 Special Eligibility Proof Request - IB-10-1497 Returned Mail Letter - FL-10-257 Caregiver Letter  The remaining new letters can go on the existing 60-day Pre-Term Eligibility Letters ICD; however, they still require input into VES.  - IB-10-1648 VHA EED Decision Notice - Ineligible Special Guerrilla Unit - IB-10-1649 VHA-EED Decision Notice 60 Day Pre-Term Initial Ineligible Other Than Honorable - IB-10-1650 VHA-EED Decision Notice 60 Day Pre-Term Final Ineligible Other Than Honorable  |
| VES-36764 | Create Registration Only Form Microservice - Phase 2                           | The online form will be a short form to collect the Veteran information Name, Social Security Number (SSN), Date of Birth (DOB), Address, Phone Number, Military Service Dates and Type of Registry Exam they are requesting. This information will feed into VES and place the Veteran in a Registration-Only status if they do not wish to enroll. If the Veteran is already known to the system, we will capture the type of Registry Exam being requested.                                                                                                                                                                                                   |
| VES-46348 | Automate TERA Eligibility (Phase 2 of 3)                                       | Phase 2: Automate TERA Cohort 3  If the Veteran deployed in support of one of the following contingency operations, VES will automatically assign the TERA Indicator and Cohort 3:  - Operation Enduring Freedom - Operation Freedom’s Sentinel - Operation Iraqi Freedom - Operation New Dawn - Operation Inherent Resolve - Resolute Support Mission                                                                                                                                                                                                                                                                                                           |
| VES-48959 | Restrict SW Asia Conditions Eligibility - VES                                  | - VES users should only be allowed to add SW Asia Conditions to Veterans who have served during a timeframe that matches August 2, 1990, through November 11, 1998. - Users should not be allowed to add SW Asia Conditions if a military service episode is null or incomplete.                                                                                                                                                                                                                                                                                                                                                                                 |
| VES-56230 | Enable VistA systems with the Address Override Functionality - VES web service | VES web service is required to accept real-time address updates from VistA and relay them to VA Profile.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| VES-58343 | Update Document Management Options                                             | - Add the following options under Proof of Discharge: - Add a TERA Eligibility Option to Document Type - Add the following Document Names under TERA Eligibility - Under the Administration Document Type add the following Document Names  - NAVPERS 553 - NAVMC 553 - NAVCG 553 - DD Form 256 - NA Form 13038 - Award Letter - Rating Codesheet Decision - COD Administrative Decision  - TERA Memo - VA Form 10-7131 - Sec 1117 Memo - Sec 1119 Memo - VBA Veteran Flash - Rating Codesheet Decision Military Orders - VIS Report - VBMS PACT Deployments - ILER Report - VA Form 10-7131  - VA Form 20-0986 - Rating Codesheet Decision - VBA Correspondence |

### Bugs

| **Key**   | **Summary**                                                                       |
|-----------|-----------------------------------------------------------------------------------|
| VES-24416 | Z06 manual retransmit doesn't work                                                |
| VES-26508 | IVM conversion overriding an approved hardship                                    |
| VES-38146 | Address lines saved with beginning or trailing tabs and non-visible characters    |
| VES-39197 | 623A initial letter is being auto rejected                                        |
| VES-43279 | Implementation logic flawed for setPreTermInProcess                               |
| VES-60022 | TERA cohort data is not editable for records automatically set to “Yes” by system |
| VES-60054 | Help text is incorrect for Medicare entry                                         |
| VES-61488 | User Account Lock Date can be set to past artificial date                         |

### From: Release Notes VES 6.15

### Release Notes for VHA Enrollment System - VES 6.15.0

12-30-2025

The mission of the Department of Veteran Affairs (VA) Office of Information and Technology (OIT) Development, Security, and Operations is to provide benefits to Veterans and their families. In order to meet this overarching goal, OIT is charged with providing high quality, effective and efficient IT services and Operations and Maintenance (O&amp;M) to persons and organizations that provide point-of-care services to our Veterans.

The VA’s goals for its Veterans and families include:

- Make it easier for Veterans and their families to receive the right benefits and meeting their expectations for quality, timeliness and responsiveness.
- Improve the quality and accessibility of health care, benefits and memorial services while optimizing value.
- Provide world-class health care delivery, by partnering with each Veteran to create a personalized, proactive strategy to optimize health and well-being, while providing state of the art disease management.
- Ensure awareness and understanding of the personalized, proactive and patient-driven health care model through education and monitoring.
- Provide convenient access to information regarding VA health benefits, medical records, health information, expert advice and ongoing support needed to make informed health decisions and successfully implement the Veteran’s personal health plans.
- Receive timely, high quality, personalized, safe, effective and equitable health care, not dependent upon geography, gender, age, culture, race, or sexual orientation.
- Strengthen collaborations with communities and organizations, such as the Department of Defense (DoD), Department of Health and Human Services (DHHS), academic affiliates and other service organizations.

To assist in meeting these goals, the Veteran Experience Services Enrollment and Eligibility (VESEE) program will provide enterprise-wide enhancements and sustainment for the following systems/applications:

- The VHA Enrollment System (VES) is the authoritative system for VA enrollment and Community Care static eligibility determinations.
- Income Verification Match (IVM)/Enrollment Database (EDB) assists in determining priority grouping for health care eligibility.
- Veterans Information Systems and Technology Architecture (VistA) Registration, Eligibility &amp; Enrollment (REE) shares information with other VistA applications and enables registration and preliminary eligibility determinations and enrollment at VA Medical Centers (VAMC). VES makes the final eligibility determinations.

The Veteran’s On-Line Application (VOA), now referred to as Health Care Application (HCA), enables Veterans to self-enroll in VA health care and is another entry point for records to be added to VES.

VESEE defines VHA Profiles (VHAP) for which a client (Veteran, Service Member, or beneficiary) is eligible and ties them to the authority for care.

### From: Release Notes VES 6.7

### Release Notes for VHA Enrollment System - VES 6.7.0

09-18-2023

The mission of the Department of Veteran Affairs (VA) Office of Information and Technology (OIT) Development, Security, and Operations is to provide benefits to Veterans and their families. In order to meet this overarching goal, OIT is charged with providing high quality, effective and efficient IT services and Operations and Maintenance (O&amp;M) to persons and organizations that provide point-of-care services to our Veterans.

The VA’s goals for its Veterans and families include:

- Make it easier for Veterans and their families to receive the right benefits and meeting their expectations for quality, timeliness and responsiveness.
- Improve the quality and accessibility of health care, benefits and memorial services while optimizing value.
- Provide world-class health care delivery, by partnering with each Veteran to create a personalized, proactive strategy to optimize health and well-being, while providing state of the art disease management.
- Ensure awareness and understanding of the personalized, proactive and patient-driven health care model through education and monitoring.
- Provide convenient access to information regarding VA health benefits, medical records, health information, expert advice and ongoing support needed to make informed health decisions and successfully implement the Veteran’s personal health plans.
- Receive timely, high quality, personalized, safe, effective and equitable health care, not dependent upon geography, gender, age, culture, race, or sexual orientation.
- Strengthen collaborations with communities and organizations, such as the Department of Defense (DoD), Department of Health and Human Services (DHHS), academic affiliates and other service organizations.

To assist in meeting these goals, the Eligibility and Enrollment (E&amp;E) program will provide enterprise-wide enhancements and sustainment for the following systems/applications:

- The VHA Enrollment System (VES) is the authoritative system for VA enrollment and Community Care static eligibility determinations.
- Income Verification Match (IVM)/Enrollment Database (EDB) assists in determining priority grouping for health care eligibility.
- Veterans Information Systems and Technology Architecture (VistA) Registration, Eligibility &amp; Enrollment (REE) shares information with other VistA applications and enables registration and preliminary eligibility determinations and enrollment at VA Medical Centers (VAMC). VES makes the final eligibility determinations.

The Veteran’s On-Line Application (VOA), now referred to as Health Care Application (HCA), enables Veterans to self-enroll in VA health care and is another entry point for records to be added to VES.

E&amp;E defines VHA Profiles (VHAP) for which a client (Veteran, Service Member, or beneficiary) is eligible and ties them to the authority for care.

### From: Release Notes VES 6.8.2

## Release Notes for VHA Enrollment System - VES 6.8.2

03-04-2024

The mission of the Department of Veteran Affairs (VA) Office of Information and Technology (OIT) Development, Security, and Operations is to provide benefits to Veterans and their families. In order to meet this overarching goal, OIT is charged with providing high quality, effective and efficient IT services and Operations and Maintenance (O&amp;M) to persons and organizations that provide point-of-care services to our Veterans.

The VA’s goals for its Veterans and families include:

- Make it easier for Veterans and their families to receive the right benefits and meeting their expectations for quality, timeliness and responsiveness.
- Improve the quality and accessibility of health care, benefits and memorial services while optimizing value.
- Provide world-class health care delivery, by partnering with each Veteran to create a personalized, proactive strategy to optimize health and well-being, while providing state of the art disease management.
- Ensure awareness and understanding of the personalized, proactive and patient-driven health care model through education and monitoring.
- Provide convenient access to information regarding VA health benefits, medical records, health information, expert advice and ongoing support needed to make informed health decisions and successfully implement the Veteran’s personal health plans.
- Receive timely, high quality, personalized, safe, effective and equitable health care, not dependent upon geography, gender, age, culture, race, or sexual orientation.
- Strengthen collaborations with communities and organizations, such as the Department of Defense (DoD), Department of Health and Human Services (DHHS), academic affiliates and other service organizations.

To assist in meeting these goals, the Eligibility and Enrollment (E&amp;E) program will provide enterprise-wide enhancements and sustainment for the following systems/applications:

- The VHA Enrollment System (VES) is the authoritative system for VA enrollment and Community Care static eligibility determinations.
- Income Verification Match (IVM)/Enrollment Database (EDB) assists in determining priority grouping for health care eligibility.
- Veterans Information Systems and Technology Architecture (VistA) Registration, Eligibility &amp; Enrollment (REE) shares information with other VistA applications and enables registration and preliminary eligibility determinations and enrollment at VA Medical Centers (VAMC). VES makes the final eligibility determinations.

The Veteran’s On-Line Application (VOA), now referred to as Health Care Application (HCA), enables Veterans to self-enroll in VA health care and is another entry point for records to be added to VES.

E&amp;E defines VHA Profiles (VHAP) for which a client (Veteran, Service Member, or beneficiary) is eligible and ties them to the authority for care.

### Change Requests

| **Key**   | **Summary**                                             |
|-----------|---------------------------------------------------------|
| VES-38729 | Create Open Work Item for TERA From Online Applications |

### Epics

| **Key**   | **Summary**                                             | **Description**                                                                          |
|-----------|---------------------------------------------------------|------------------------------------------------------------------------------------------|
| VES-39038 | Create Open Work Item for TERA from Online Applications | Create an Open Work Item when a Veteran selects a TERA option on the Online Application. |
| VES-39431 | Receive TERA indicators from VOA                        | Receive TERA indicators from VOA                                                         |

### From: Release Notes VES 6.14.5

## Release Notes for VHA Enrollment System - VES 6.14.5

11-19-2025

The mission of the Department of Veteran Affairs (VA) Office of Information and Technology (OIT) Development, Security, and Operations is to provide benefits to Veterans and their families. In order to meet this overarching goal, OIT is charged with providing high quality, effective and efficient IT services and Operations and Maintenance (O&amp;M) to persons and organizations that provide point-of-care services to our Veterans.

The VA’s goals for its Veterans and families include:

- Make it easier for Veterans and their families to receive the right benefits and meeting their expectations for quality, timeliness and responsiveness.
- Improve the quality and accessibility of health care, benefits and memorial services while optimizing value.
- Provide world-class health care delivery, by partnering with each Veteran to create a personalized, proactive strategy to optimize health and well-being, while providing state of the art disease management.
- Ensure awareness and understanding of the personalized, proactive and patient-driven health care model through education and monitoring.
- Provide convenient access to information regarding VA health benefits, medical records, health information, expert advice and ongoing support needed to make informed health decisions and successfully implement the Veteran’s personal health plans.
- Receive timely, high quality, personalized, safe, effective and equitable health care, not dependent upon geography, gender, age, culture, race, or sexual orientation.
- Strengthen collaborations with communities and organizations, such as the Department of Defense (DoD), Department of Health and Human Services (DHHS), academic affiliates and other service organizations.

To assist in meeting these goals, the Veteran Experience Services Enrollment and Eligibility (VESEE) program will provide enterprise-wide enhancements and sustainment for the following systems/applications:

- The VHA Enrollment System (VES) is the authoritative system for VA enrollment and Community Care static eligibility determinations.
- Income Verification Match (IVM)/Enrollment Database (EDB) assists in determining priority grouping for health care eligibility.
- Veterans Information Systems and Technology Architecture (VistA) Registration, Eligibility &amp; Enrollment (REE) shares information with other VistA applications and enables registration and preliminary eligibility determinations and enrollment at VA Medical Centers (VAMC). VES makes the final eligibility determinations.

The Veteran’s On-Line Application (VOA), now referred to as Health Care Application (HCA), enables Veterans to self-enroll in VA health care and is another entry point for records to be added to VES.

VESEE defines VHA Profiles (VHAP) for which a client (Veteran, Service Member, or beneficiary) is eligible and ties them to the authority for care.

### Change Requests

| **Key**   | **Summary**                                                                                    |
|-----------|------------------------------------------------------------------------------------------------|
| VES-28738 | Meds by Mail (MbM) Indicator - Veteran and Family Member Program (VFMP) MbM Eligibility Status |
| VES-28740 | Control the Number of Records that Enter a "Pending Review" Status to "Verified" Status        |
| VES-28742 | Other Health Insurance (OHI) - Private - Eligibility Plus File                                 |
| VES-54724 | Data Access Service (DAS) Connection for VFMP Print Vendor                                     |

### ### Epics

| **Key**   | **Summary**                                                                                                                                                     | **Description**                                                                                                                                                                                                                                                            |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VES-20919 | Receive Applications in VFMP System from Online Portal                                                                                                          | Receive applications/registrations for enrollment in VFMP programs from an online/web portal, so that users are able to support application and eligibility updates.                                                                                                       |
| VES-21003 | Register VFMP Person in MbM Group via Interface                                                                                                                 | Register a person who is enrolled in Standard, Caregiver Civilian Health and Medical Program of the Department of Veterans Affairs (CHAMPVA), Spina Bifida (SB) or Children of Women Vietnam Veterans (CWVV) plan, in the MbM group, so that users can update eligibility. |
| VES-21010 | Provide Request and Response Capability to Eligibility-Enrollment (EE) Service-for Minimum Viable Product (MVP) – Users Can View Fields Within VES When Queried | Prepare and return a response to a request or query for the EE information to determine a member's enrollment status in any/all Office of Community Care (OCC) Health Care Plans/ Groups, so that users can determine eligibility.                                         |
| VES-21074 | Interface with the Customer Relations Manager (CRM) System from VFMP System                                                                                     | Interface with the CRM system to support customer service activities, so that users can manage data/information for eligibility.                                                                                                                                           |
| VES-21087 | Transmit Electronic Eligibility File to MbM System from VFMP System                                                                                             | Transmit an electronic file, containing eligibility information to MbM, so that users can manage data/information for eligibility.                                                                                                                                         |
| VES-21108 | Provide Ability to Send Daily Eligibility File to ClaimsXM via Payer Electronic Data Interchange (PEDTAS)                                                       | Transmit a daily electronic file, containing eligibility information to ClaimsXM, so that users can manage data/information for eligibility.                                                                                                                               |
| VES-21111 | Provide Ability to Send Daily OHI File to VFMP Vendorization System from VFMP System (Eligibility Plus File)                                                    | Transmit a daily electronic file, containing changes to all OHI information to the vendorization system for Family Member Programs, so that users can manage data/information for eligibility.                                                                             |
| VES-21348 | VFMP Migration for CHAMPVA Standard (M-Development)                                                                                                             | Migrate CHAMPVA Standard.                                                                                                                                                                                                                                                  |
| VES-22332 | Claims Processing & Eligibility (CP&E) Data Migration Requirements Specification Document (RSD)                                                                 | Create RSD for CP&E Data Migration.                                                                                                                                                                                                                                        |
| VES-23169 | Send VES VFMP Eligibility Plus Files                                                                                                                            | Send VES VFMP Eligibility Plus Files.                                                                                                                                                                                                                                      |
| VES-43801 | VFMP Migration Updates - Correspondence History                                                                                                                 | Update VFMP Migration - Correspondence History.                                                                                                                                                                                                                            |
| VES-51403 | VFMP Eligibility Plus Updates - OHI Eligibility Plus File Integration                                                                                           | Integrate VFMP Eligibility Plus Updates - OHI Eligibility Plus File.                                                                                                                                                                                                       |
| VES-51404 | VFMP Migration of Other Health Insurance (Child) RSD                                                                                                            | Create RSD for VFMP Migration of Other Health Insurance (Child).                                                                                                                                                                                                           |
| VES-52236 | VFMP VBA Query Worklist Item RSD                                                                                                                                | Create RSD for VFMP VBA Query Worklist Item.                                                                                                                                                                                                                               |
| VES-56083 | VES Landscape and Benchmark Analysis for Migration                                                                                                              | Capture performance data for use in migration strategy.                                                                                                                                                                                                                    |
| VES-61094 | VFMP Migration Updates – Correspondence (CORR) Address to Confidential Address                                                                                  | VFMP Migration Updates - CORR Address to Confidential Address.                                                                                                                                                                                                             |
| VES-61166 | Manage Eligibility and Enrollment Information in VES                                                                                                            | Manage Eligibility and Enrollment Information (VES 6.13.X and 6.14.X Rules and User Interface (UI) for VFMP initiative).                                                                                                                                                   |
| VES-63478 | VFMP Remove Setting of PENDING REVIEW Status for CHAMPVA RSD                                                                                                    | Create RSD for VFMP Remove Setting of PENDING REVIEW Status for CHAMPVA.                                                                                                                                                                                                   |

### From: Release Notes VES 6.5.3

### Release Notes for VHA Enrollment System - VES 6.5.3

05-15-2023

The mission of the Department of Veteran Affairs (VA) Office of Information and Technology (OIT) Development, Security, and Operations is to provide benefits to Veterans and their families. In order to meet this overarching goal, OIT is charged with providing high quality, effective and efficient IT services and Operations and Maintenance (O&amp;M) to persons and organizations that provide point-of-care services to our Veterans.

The VA’s goals for its Veterans and families include:

- Make it easier for Veterans and their families to receive the right benefits and meeting their expectations for quality, timeliness and responsiveness.
- Improve the quality and accessibility of health care, benefits and memorial services while optimizing value.
- Provide world-class health care delivery, by partnering with each Veteran to create a personalized, proactive strategy to optimize health and well-being, while providing state of the art disease management.
- Ensure awareness and understanding of the personalized, proactive and patient-driven health care model through education and monitoring.
- Provide convenient access to information regarding VA health benefits, medical records, health information, expert advice and ongoing support needed to make informed health decisions and successfully implement the Veteran’s personal health plans.
- Receive timely, high quality, personalized, safe, effective and equitable health care, not dependent upon geography, gender, age, culture, race, or sexual orientation.
- Strengthen collaborations with communities and organizations, such as the Department of Defense (DoD), Department of Health and Human Services (DHHS), academic affiliates and other service organizations.

To assist in meeting these goals, the Eligibility and Enrollment (E&amp;E) program will provide enterprise-wide enhancements and sustainment for the following systems/applications:

- The VHA Enrollment System (VES) is the authoritative system for VA enrollment and Community Care static eligibility determinations.
- Income Verification Match (IVM)/Enrollment Database (EDB) assists in determining priority grouping for health care eligibility.
- Veterans Information Systems and Technology Architecture (VistA) Registration, Eligibility &amp; Enrollment (REE) shares information with other VistA applications and enables registration and preliminary eligibility determinations and enrollment at VA Medical Centers (VAMC). VES makes the final eligibility determinations.

The Veteran’s On-Line Application (VOA), now referred to as Health Care Application (HCA), enables Veterans to self-enroll in VA health care and is another entry point for records to be added to VES.

E&amp;E defines VHA Profiles (VHAP) for which a client (Veteran, Service Member, or beneficiary) is eligible and ties them to the authority for care.

### From: Release Notes VES 6.5.2

### Release Notes for VHA Enrollment System - VES 6.5.2

04-28-2023

The mission of the Department of Veteran Affairs (VA) Office of Information and Technology (OIT) Development, Security, and Operations is to provide benefits to Veterans and their families. In order to meet this overarching goal, OIT is charged with providing high quality, effective and efficient IT services and Operations and Maintenance (O&amp;M) to persons and organizations that provide point-of-care services to our Veterans.

The VA’s goals for its Veterans and families include:

- Make it easier for Veterans and their families to receive the right benefits and meeting their expectations for quality, timeliness and responsiveness.
- Improve the quality and accessibility of health care, benefits and memorial services while optimizing value.
- Provide world-class health care delivery, by partnering with each Veteran to create a personalized, proactive strategy to optimize health and well-being, while providing state of the art disease management.
- Ensure awareness and understanding of the personalized, proactive and patient-driven health care model through education and monitoring.
- Provide convenient access to information regarding VA health benefits, medical records, health information, expert advice and ongoing support needed to make informed health decisions and successfully implement the Veteran’s personal health plans.
- Receive timely, high quality, personalized, safe, effective and equitable health care, not dependent upon geography, gender, age, culture, race, or sexual orientation.
- Strengthen collaborations with communities and organizations, such as the Department of Defense (DoD), Department of Health and Human Services (DHHS), academic affiliates and other service organizations.

To assist in meeting these goals, the Eligibility and Enrollment (E&amp;E) program will provide enterprise-wide enhancements and sustainment for the following systems/applications:

- The VHA Enrollment System (VES) is the authoritative system for VA enrollment and Community Care static eligibility determinations.
- Income Verification Match (IVM)/Enrollment Database (EDB) assists in determining priority grouping for health care eligibility.
- Veterans Information Systems and Technology Architecture (VistA) Registration, Eligibility &amp; Enrollment (REE) shares information with other VistA applications and enables registration and preliminary eligibility determinations and enrollment at VA Medical Centers (VAMC). VES makes the final eligibility determinations.

The Veteran’s On-Line Application (VOA), now referred to as Health Care Application (HCA), enables Veterans to self-enroll in VA health care and is another entry point for records to be added to VES.

E&amp;E defines VHA Profiles (VHAP) for which a client (Veteran, Service Member, or beneficiary) is eligible and ties them to the authority for care.

### From: Release Notes VES 6.5.4

### Release Notes for VHA Enrollment System - VES 6.5.4

05-16-2023

The mission of the Department of Veteran Affairs (VA) Office of Information and Technology (OIT) Development, Security, and Operations is to provide benefits to Veterans and their families. In order to meet this overarching goal, OIT is charged with providing high quality, effective and efficient IT services and Operations and Maintenance (O&amp;M) to persons and organizations that provide point-of-care services to our Veterans.

The VA’s goals for its Veterans and families include:

- Make it easier for Veterans and their families to receive the right benefits and meeting their expectations for quality, timeliness and responsiveness.
- Improve the quality and accessibility of health care, benefits and memorial services while optimizing value.
- Provide world-class health care delivery, by partnering with each Veteran to create a personalized, proactive strategy to optimize health and well-being, while providing state of the art disease management.
- Ensure awareness and understanding of the personalized, proactive and patient-driven health care model through education and monitoring.
- Provide convenient access to information regarding VA health benefits, medical records, health information, expert advice and ongoing support needed to make informed health decisions and successfully implement the Veteran’s personal health plans.
- Receive timely, high quality, personalized, safe, effective and equitable health care, not dependent upon geography, gender, age, culture, race, or sexual orientation.
- Strengthen collaborations with communities and organizations, such as the Department of Defense (DoD), Department of Health and Human Services (DHHS), academic affiliates and other service organizations.

To assist in meeting these goals, the Eligibility and Enrollment (E&amp;E) program will provide enterprise-wide enhancements and sustainment for the following systems/applications:

- The VHA Enrollment System (VES) is the authoritative system for VA enrollment and Community Care static eligibility determinations.
- Income Verification Match (IVM)/Enrollment Database (EDB) assists in determining priority grouping for health care eligibility.
- Veterans Information Systems and Technology Architecture (VistA) Registration, Eligibility &amp; Enrollment (REE) shares information with other VistA applications and enables registration and preliminary eligibility determinations and enrollment at VA Medical Centers (VAMC). VES makes the final eligibility determinations.

The Veteran’s On-Line Application (VOA), now referred to as Health Care Application (HCA), enables Veterans to self-enroll in VA health care and is another entry point for records to be added to VES.

E&amp;E defines VHA Profiles (VHAP) for which a client (Veteran, Service Member, or beneficiary) is eligible and ties them to the authority for care.

### From: Release Notes VES 6.5.5

### Release Notes for VHA Enrollment System - VES 6.5.5

05-26-2023

The mission of the Department of Veteran Affairs (VA) Office of Information and Technology (OIT) Development, Security, and Operations is to provide benefits to Veterans and their families. In order to meet this overarching goal, OIT is charged with providing high quality, effective and efficient IT services and Operations and Maintenance (O&amp;M) to persons and organizations that provide point-of-care services to our Veterans.

The VA’s goals for its Veterans and families include:

- Make it easier for Veterans and their families to receive the right benefits and meeting their expectations for quality, timeliness and responsiveness.
- Improve the quality and accessibility of health care, benefits and memorial services while optimizing value.
- Provide world-class health care delivery, by partnering with each Veteran to create a personalized, proactive strategy to optimize health and well-being, while providing state of the art disease management.
- Ensure awareness and understanding of the personalized, proactive and patient-driven health care model through education and monitoring.
- Provide convenient access to information regarding VA health benefits, medical records, health information, expert advice and ongoing support needed to make informed health decisions and successfully implement the Veteran’s personal health plans.
- Receive timely, high quality, personalized, safe, effective and equitable health care, not dependent upon geography, gender, age, culture, race, or sexual orientation.
- Strengthen collaborations with communities and organizations, such as the Department of Defense (DoD), Department of Health and Human Services (DHHS), academic affiliates and other service organizations.

To assist in meeting these goals, the Eligibility and Enrollment (E&amp;E) program will provide enterprise-wide enhancements and sustainment for the following systems/applications:

- The VHA Enrollment System (VES) is the authoritative system for VA enrollment and Community Care static eligibility determinations.
- Income Verification Match (IVM)/Enrollment Database (EDB) assists in determining priority grouping for health care eligibility.
- Veterans Information Systems and Technology Architecture (VistA) Registration, Eligibility &amp; Enrollment (REE) shares information with other VistA applications and enables registration and preliminary eligibility determinations and enrollment at VA Medical Centers (VAMC). VES makes the final eligibility determinations.

The Veteran’s On-Line Application (VOA), now referred to as Health Care Application (HCA), enables Veterans to self-enroll in VA health care and is another entry point for records to be added to VES.

E&amp;E defines VHA Profiles (VHAP) for which a client (Veteran, Service Member, or beneficiary) is eligible and ties them to the authority for care.

### From: Release Notes VES 6.6.1

### Release Notes for VHA Enrollment System - VES 6.6.1

09-18-2023

The mission of the Department of Veteran Affairs (VA) Office of Information and Technology (OIT) Development, Security, and Operations is to provide benefits to Veterans and their families. In order to meet this overarching goal, OIT is charged with providing high quality, effective and efficient IT services and Operations and Maintenance (O&amp;M) to persons and organizations that provide point-of-care services to our Veterans.

The VA’s goals for its Veterans and families include:

- Make it easier for Veterans and their families to receive the right benefits and meeting their expectations for quality, timeliness and responsiveness.
- Improve the quality and accessibility of health care, benefits and memorial services while optimizing value.
- Provide world-class health care delivery, by partnering with each Veteran to create a personalized, proactive strategy to optimize health and well-being, while providing state of the art disease management.
- Ensure awareness and understanding of the personalized, proactive and patient-driven health care model through education and monitoring.
- Provide convenient access to information regarding VA health benefits, medical records, health information, expert advice and ongoing support needed to make informed health decisions and successfully implement the Veteran’s personal health plans.
- Receive timely, high quality, personalized, safe, effective and equitable health care, not dependent upon geography, gender, age, culture, race, or sexual orientation.
- Strengthen collaborations with communities and organizations, such as the Department of Defense (DoD), Department of Health and Human Services (DHHS), academic affiliates and other service organizations.

To assist in meeting these goals, the Eligibility and Enrollment (E&amp;E) program will provide enterprise-wide enhancements and sustainment for the following systems/applications:

- The VHA Enrollment System (VES) is the authoritative system for VA enrollment and Community Care static eligibility determinations.
- Income Verification Match (IVM)/Enrollment Database (EDB) assists in determining priority grouping for health care eligibility.
- Veterans Information Systems and Technology Architecture (VistA) Registration, Eligibility &amp; Enrollment (REE) shares information with other VistA applications and enables registration and preliminary eligibility determinations and enrollment at VA Medical Centers (VAMC). VES makes the final eligibility determinations.

The Veteran’s On-Line Application (VOA), now referred to as Health Care Application (HCA), enables Veterans to self-enroll in VA health care and is another entry point for records to be added to VES.

E&amp;E defines VHA Profiles (VHAP) for which a client (Veteran, Service Member, or beneficiary) is eligible and ties them to the authority for care.
