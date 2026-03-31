---
consolidated_title: "nursing user manual change pages"
app_code: NUR
doc_type: UM
master_source: "NUR*4*45 Nursing User Manual Change Pages"
master_pub_date: May 2018
consolidated_from: 2 versions
prior_versions:
  - "NUR*4*43 Nursing User Manual Change Pages"
---

Nursing User Manual Version 4.0

Change Pages for Patch NUR\*4.0\*45

VistA Health  
Systems Design & Development

![](nur-4-45-nursing-user-manual-change-pages/001.png)

May 2018
# Document Purpose


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Document Purpose](#document-purpose)
- [Scope of Patch NUR\4.0\45](#scope-of-patch-nur4045)
- [Updates to Nursing User Manual Version 4.0](#updates-to-nursing-user-manual-version-40)
  - [Section 3: Clinical / Chapter 2: Patient Assignments](#section-3-clinical-chapter-2-patient-assignments)
  - [Section 3: Clinical / Chapter 6: Miscellaneous Reports](#section-3-clinical-chapter-6-miscellaneous-reports)
This document presents the new functionality provided by Patch NUR\*4.0\*45 and should be considered an update to the content contained in the existing Nursing User Manual Version 4.0 (1997, updated 2000) PDF file. The new material presented in this document is provided in lieu of inserting revisions directly into the text of the existing Nursing User Manual Version 4.0 because no editable (MS Word) document can be located.

# Scope of Patch NUR\*4.0\*45

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch NUR\*4.0\*45 modifies the Nursing Patient Care Assignment Worksheet to display only the last four digits of each patient’s Social Security Number (SSN) and to remove the admitting diagnosis from the worksheet and replace it with the text “ON FILE.” Additionally, the Nursing End-of-Shift Report is modified to display oxygen levels with the patient’s vital signs, add a line of header information to clarify the purpose of the report sections, include new assessment categories that guide clinical staff when documenting patient problems, and hide contact information for the Attending Physician.

# Updates to Nursing User Manual Version 4.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The enhancements provided by patch NUR\*4.0\*45 impact two chapters in Section 3 (Clinical).

## Section 3: Clinical / Chapter 2: Patient Assignments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch NUR\*4.0\*45 modifies the Nursing Patient Care Assignment Worksheet to protect confidential patient information and help ensure patient privacy.

- Displays only the last four digits of each patient’s Social Security Number (SSN) on the worksheet. The full SSN no longer displays.
- Removes the admitting diagnosis from the worksheet and replaces it with the text “ON FILE.”

![](nur-4-45-nursing-user-manual-change-pages/002.png)

> Patient Care Assignment Worksheet Modifications

## Section 3: Clinical / Chapter 6: Miscellaneous Reports

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Patch NUR\*4.0\*45 enhances the Nursing End-of-Shift Report to facilitate communication between staff when shifts change and to help ensure patient privacy.

> ![](nur-4-45-nursing-user-manual-change-pages/003.png)

> End-of-Shift Report Modifications

- Adds an additional line of header information to the report to clarify the purpose of the various report sections. The new header information includes Situation, Background, Assessment, and Recommendation column headings.
- Includes oxygen levels in the Assessment section where the patient’s vitals (Latest Vitals) are displayed.
- Adds categories (Assessment, Safety, and Special Needs) to the Patient Problems section of the report.
- Displays only the last four digits of the patient’s Social Security Number (SSN). The full SSN no longer displays.

> Includes or excludes the Attending Physician’s voice and digital pager numbers by adding the PRINT ATT NUMS ON EOS RPT field (#10.6) to the NURS PARAMETERS file (#213.9) to act as a parameter that controls the display of the Attending Physician contact numbers. Initially, the value is set to NO and Attending Physician contact numbers are not displayed on the report. To display Attending Physician contact numbers on the report, set the value to YES using the Site Parameter File \[NURSFL-SITE\], which can be found using the following pathway:

> Nursing System Manager's Menu \[NURS-SYS-MGR\]  
> Nursing Features (all options) \[NURS-ALL\]  
> Administrative Site File Functions \[NURSFL-MENU\]  
> Site Parameter File \[NURSFL-SITE\]

> Your site might have modified the pathway, so check with your local IT operations if you are having difficulty accessing the option.

![](nur-4-45-nursing-user-manual-change-pages/004.png)

> Navigating to Option NURSFL-SITE to Display Site ParametersNote: The prompts following “PRINT ATT NUMS ON EOS RPT:NO//” are restricted. The user’s account must be set to “@” in the FILE MANAGER ACCESS CODE field of the NEW PERSON file or the final two prompts will not display.