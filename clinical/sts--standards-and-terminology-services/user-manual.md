---
title: STS Version 11 VETS 11 User Guide
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: VETS 11
app_code: STS
app_name: Standards & Terminology Services
section: CLI
app_status: active
pkg_ns: STS
patch_ver: 11
patch_id: STS*11
group_key: "STS:STS:11"
file_numbers: []
security_keys: []
menu_options: 2
description: > This manual describes the Standards & Terminology Services (STS) Department of Veterans Affairs (VA) Enterprise Terminology Service Version 11.0 User Interface (UI) menu options and their functionality. It includes workflows that have systematic instructions for authoring and deploying terminology
audience: 
keywords: 
  - strong
  - class
  - table
  - terminology
  - version
  - contents
  - even
  - concept
  - deployment
  - vets
page_count: 0
word_count: 6014
section_count: 4
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: August 2011
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Standards_and_Terminology_Services/sts_vets_v11_userguide.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Standards_and_Terminology_Services/sts_vets_v11_userguide.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=191"
---

> Standards & Terminology Services (STS) VA Enterprise Terminology Service (VETS)

> *User Guide*

![](sts-version-11-vets-11-user-guide/001.png)

> *Version 11.0*

> *August 2011*

> Department of Veterans Affairs

> Office of Information and Technology (OI&T) Office of Enterprise Development (OED)

> Revision History

| Date   | Version | Description          | Author                         |
|------------|-------------|--------------------------|------------------------------------|
| March 2011 | 0.1         | Updates for next version | <span class="mark">REDACTED</span> |
| July 2011  | 0.2         | Review, edit, format     | <span class="mark">REDACTED</span> |
# List of Figures


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [List of Figures](#list-of-figures)
- [Introduction](#introduction)
    - [Web Services](#web-services)
- [Terminology Editor](#terminology-editor)
    - [Technical advisory for users using accessibility technology](#technical-advisory-for-users-using-accessibility-technology)
- [Using STS VETS TED V11.0](#using-sts-vets-ted-v110)
    - [Lo gin](#lo-gin)
    - [Add a Map Set and Map Entry](#add-a-map-set-and-map-entry)
    - [Edit a Map Set and Map Entry](#edit-a-map-set-and-map-entry)
- [Terminology Deployment Service](#terminology-deployment-service)
    - [Workflow](#workflow)
- [Using STS VETS TDS V11.0](#using-sts-vets-tds-v110)
    - [Lo gin](#lo-gin-1)
    - [Update](#update)
    - [SCS](#scs)
    - [Deployment](#deployment)
    - [Version](#version)
    - [Finalized Version](#finalized-version)
    - [Logout](#logout)
- [Troubleshooting STS TDS V11.0](#troubleshooting-sts-tds-v110)
    - [Validate](#validate)
    - [Discovery](#discovery)
    - [Tools](#tools)
  - [History](#history)
  - [Link and Unlink](#link-and-unlink)
  - [Group Editor](#group-editor)
- [Glossary](#glossary)
    - [STS Terminology Glossary](#sts-terminology-glossary)
> [FIGURE 1. TED WORKFLOW 3](#_bookmark6)
> [FIGURE 2. TED LOGIN WINDOW 4](#_bookmark9)
> [FIGURE 3. MAP SET SELECTION WINDOW 5](#_bookmark11)
> [FIGURE 4. MAP SET: ADD WINDOW 5](#_bookmark12)
> [FIGURE 5. MAP SET: EDIT WINDOW 6](#_bookmark13)
> [FIGURE 6. MAP ENTRY WINDOW 7](#_bookmark14)
> [FIGURE 7. MAP ENTRY WINDOW WITH SEARCHED OPTIONS DISPLAYED 8](#_bookmark15)
> [FIGURE 8. MAP ENTRY WINDOW WITH SOURCE DESCRIPTION 8](#_bookmark16)
> [FIGURE 9. MAP ENTRY WINDOW WITH TARGET DESCRIPTION 9](#_bookmark17)
> [FIGURE 10. MAP ENTRY WINDOW WITH SOURCE AND TARGET 10](#_bookmark18)
> [FIGURE 11. MAP ENTRY WINDOW WITH ADD OPTION 10](#_bookmark19)
> [FIGURE 12. MAP ENTRY WINDOW WITH SUCCESSFUL MESSAGE 11](#_bookmark20)
> [FIGURE 13. MAP SET EDIT WINDOW 12](#_bookmark21)
> [FIGURE 14. MAP SET SELECTION WINDOW 13](#_bookmark23)
> [FIGURE 15. MAP SET EDIT WINDOW 13](#_bookmark24)
> [FIGURE 16. MAP ENTRY WINDOW 14](#_bookmark25)
> [FIGURE 17. TDS WORKFLOW 15](#_bookmark28)
> [FIGURE 18. LOGIN WINDOW 20](#_bookmark31)
> [FIGURE 19. STS DEPLOYMENT WINDOW 20](#_bookmark32)
> [FIGURE 20. IMPORT WINDOW 21](#_bookmark34)
> [FIGURE 21. REVIEW CHANGE SET WINDOW 22](#_bookmark35)
> [FIGURE 22. CHANGE SET SUMMARY WINDOW 23](#_bookmark36)
> [FIGURE 23. CONCEPT DETAIL WINDOW 24](#scs)
> [FIGURE 24. MANAGE SCS WINDOW 25](#deployment)
> [FIGURE 25. DEPLOYMENT CREATED WINDOW 26](#_bookmark41)
> [FIGURE 26. DISPLAY CHECKSUM RESULTS FOR SITES WINDOW 27](#_bookmark42)
> [FIGURE 27. VERIFY DEPLOYMENT AND TEST SITES WINDOW 28](#_bookmark43)
> [FIGURE 28. DEPLOYMENT RESULTS WINDOW WITH ACK POPULATED 29](#_bookmark44)
> [FIGURE 29. MANAGE DEPLOYMENT WINDOW 30](#_bookmark45)
> [FIGURE 30. CANDIDATE VERSION CREATED WINDOW 31](#_bookmark47)
> [FIGURE 31. VERIFY CANDIDATE VERSIONS AND TEST SITES WINDOW 32](#_bookmark48)
> [FIGURE 32. MANAGE VERSION WINDOW 34](#_bookmark49)
> [FIGURE 33. FINALIZED VERSIONS WINDOW 34](#_bookmark50)
> [FIGURE 34. VERIFY DEPLOYMENTS AND PRODUCTION SITES WINDOW 35](#_bookmark52)
> [FIGURE 35. PRODUCTION VALIDATION WINDOW 36](#logout)
> [FIGURE 36. DISCOVERY – SELECT SUBSETS/MAP SETS WINDOW 38](#_bookmark58)
> [FIGURE 37. DISCOVERY – SELECT DEPLOYMENT, CANDIDATE, OR VERSION TEST WINDOW 39](#_bookmark59)
> [FIGURE 38. DISCOVERY – SELECT SITES TEST WINDOW 40](#_bookmark60)
> [FIGURE 39. DISCOVERY RESULTS TEST WINDOW 41](#_bookmark61)
> [FIGURE 40. DISCOVERY RESULTS WINDOW 42](#_bookmark62)
> [FIGURE 41. DISCOVERY RESULTS WINDOW 42](#tools)
> [FIGURE 42. DEPLOYMENT HISTORY – SELECT DEPLOYMENTS WINDOW 43](#_bookmark66)
> [FIGURE 43. DEPLOYMENT HISTORY – SELECT SITES WINDOW 44](#_bookmark67)
> [FIGURE 44. DEPLOYMENT HISTORY – RESULTS WINDOW 45](#_bookmark68)
> [FIGURE 45. LINK VERSIONS WINDOW 46](#_bookmark70)
> [FIGURE 46. PARTIAL DEPLOYMENT OF A LINKED VERSION FROM VERSION DEPLOYMENT – SELECT VERSIONS TO](#_bookmark71) [DEPLOY WINDOW 47](#_bookmark71)
> [FIGURE 47. UNLINK VERSION WINDOW 47](#_bookmark72)
> [FIGURE 48. GROUP EDITOR WINDOW 48](#_bookmark74)

# Introduction

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This manual describes the Standards & Terminology Services (STS) Department of Veterans Affairs (VA) Enterprise Terminology Service Version 11.0 User Interface (UI) menu options and their functionality. It includes workflows that have systematic instructions for authoring and deploying terminology content. The manual is for users of the VA Enterprise Terminology Services (VETS) who perform the following tasks:

- Author Content
- Review and update functions performed by Domain Reviewers
- Deployment functions performed by Testing Coordinators and other authorized Deployers

> VETS is a suite of products that deliver standardized terminology content for use across the VA enterprise; including VistA and Clinical Data Repository/Health Data Repository (CHDR).

- The database used to house the terminology content served by VETS is the VA Terminology Server (VTS).
- VETS includes three types of terminology content, all are viewable in the Terminology Browser:
  - VHA Terminology (VHAT): a standardized terminology created and maintained for VA applications. It contains concepts that are unique to the VA as well as concepts that have been derived from authoritative sources such as Systematized Nomenclature of Medicine, Clinical Terms (SNOMED CT) or International Classification of Diseases, Clinical Modification (ICD-9-CM).
  - Standard Code Systems (SCS): data retrieved from Standard Development Organizations that are authoritative sources.
  - Map Sets: links between terminologies to support VA business needs. Map Sets may be created internally, adopted from a standard, or from another entity.
- Terminology Deployment Services (TDS) is the tool used by STS to manage and deploy VETS content.
- Terminology Editor (TED) is the tool used to add and edit Map Sets and Map Entries.

### Web Services 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> STS VETS v11.0 web services sometimes called application services, describes a standardized way of integrating Web-based [applications](http://www.webopedia.com/TERM/A/application.html) using two common protocols or architectures, Representational State Transfer (REST) and Simple Object Access Protocol (SOAP). SOAP is based on Web Services Description Language (WSDL). REST is an architectural style where resources are basic objects accessed by unique URIs. STS VETS v11.0 web services share business logic, data and processes through a programmatic interface across a network, enabling the applications to interface. [<u>http://www.webopedia.com/TERM/W/Web_Services.html</u>](http://www.webopedia.com/TERM/W/Web_Services.html)

# Terminology Editor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> TED is a web-based authoring tool that allows users to create new and edit existing Map Sets and Map Entries in the VA terminology repository. TED is a part of the VETS suite of terminology maintenance tools.

### Technical advisory for users using accessibility technology

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This application utilizes autocomplete technology on the Map Entry page. Autocomplete is a technology that assists you by predicting a word or phrase that you want to type without you typing it out completely. During product testing it was discovered that screen readers such as JAWS have trouble maintaining focus on the autocomplete-generated results drop down list when you are navigating the results using the up and down arrow keys. Results made up of approximately 30 or more characters in a string seem to cause screen readers to lose focus more frequently than results that are less than 30 characters in length. When the screen reader loses focus on the results drop down list it begins reading other artifacts on the page according to the TAB order. During product testing it was discovered that navigating results in the drop down list in a more restrained and deliberate fashion helps keep the screen reader focused on the drop down list. It is recommended that you allow the screen reader to read the entire set of characters for each result before navigating to the next result.

![](sts-version-11-vets-11-user-guide/002.png)

> <span id="_bookmark6" class="anchor"></span>Figure 1. TED Workflow

# Using STS VETS TED V11.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> TED consists of screens that allow you to add and edit Map Sets, and Map Entries within the Map Sets. You can sort information on the screens to view the content. The following icons are used in the TED application:

> ![](sts-version-11-vets-11-user-guide/003.png) ![](sts-version-11-vets-11-user-guide/004.png) - the green up and down arrows indicate the column sorted on and allow you to change the sort order. The down arrow indicates the sort order is descending, Z – A. The up arrow indicates the sort order is ascending, A – Z.

### Lo gin

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

- the Comma-Separated Value (CSV) icon allows you to export your data to a CSV file.

> ![](sts-version-11-vets-11-user-guide/005.png)Follow the steps below to log in to the STS VETS TED V11.0 application:

1.  Navigate to the application entry point.
2.  Enter your Username and Password in the boxes provided.
3.  Click the Login button or press Enter on your keyboard.

![](sts-version-11-vets-11-user-guide/006.png)

> <span id="_bookmark9" class="anchor"></span>Figure 2. TED Login Window

> When the log in is successful the current system name and the existing Map Sets display on the screen.

> Click the Refresh button to ensure the Map Set list contains the most current data.

> Your Username and Password are case sensitive. Consistent with VHA policy, your session times out after a period of 30 minutes of inactivity. At 25 minutes, a 5-minute warning message displays stating you have 5 minutes to respond before your session times out.

### Add a Map Set and Map Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section provides steps that describe how to Add a new Map Set and Map Entries.

1.  On the Home screen, click the Add New Map Set button.

> ![](sts-version-11-vets-11-user-guide/007.png)

> <span id="_bookmark11" class="anchor"></span>Figure 3. Map Set Selection Window

2.  On the Map Set: Add screen select and enter the information about the Map Set you are adding.

> ![](sts-version-11-vets-11-user-guide/008.png)Fields marked with an asterisk (\*) are required.

> <span id="_bookmark12" class="anchor"></span>Figure 4. Map Set: Add Window

> Source Code System and Version – from the pull down menu select the Source Code System for your Map Set. The Source Code System you select will determine what information is available in the Version pull down menu.

> Target Code System and Version – from the pull down menu select the Target Code System for your Map Set. The Target Code System you select will determine what information is available in the Version pull down menu.

> Preferred Name – the system will display a name reflecting the Source Code System and Target Code System you selected. You may edit the Preferred Name text.

> Textual Definition – in this field you may enter a very detailed definition of the Map Set.

> Description – in this field you may enter the use case for which the Map Set was created or a more generic description of the Map Set.

> Status – From the pull down menu, select the Status of your Map Set.

- Active – Map Set is active and in use
- Inactive – Map Set is inactive and no longer in use
3.  Click the Save Map Set button.

> ![](sts-version-11-vets-11-user-guide/009.png)Note: If you do not click the Save Map Set button before clicking the Add Map Entry button, a warning message displays The Map Set must be saved before adding entries. Click the OK button then click the Save Map Set button to save your new Map Set.

> <span id="_bookmark13" class="anchor"></span>Figure 5. Map Set: Edit Window

> The Map Set: Edit window displays a successful confirmation message. To add new Map Entries to the Map Set click the Add Map Entry button. The Map Entry window will then display.

4.  ![](sts-version-11-vets-11-user-guide/010.png)Click the Add Map Entry button to add Map Entries to your new Map Set.

> <span id="_bookmark14" class="anchor"></span>Figure 6. Map Entry Window

5.  Select Source Description or Source Code from the pull down menu.
6.  In the box, enter the Source Description or Source Code you want to add.

> You can enter the first three letters or numbers of the Description or Code in the text box to initiate a search.

> Note: All searches, in all search fields, can return a maximum of 1000 results.

> ![](sts-version-11-vets-11-user-guide/011.png)

> <span id="_bookmark15" class="anchor"></span>Figure 7. Map Entry Window with Searched Options Displayed

7.  ![](sts-version-11-vets-11-user-guide/012.png)Select the Source concept from the list. The Source concept will populate a row in the table.

> <span id="_bookmark16" class="anchor"></span>Figure 8. Map Entry Window with Source Description

8.  Enter the Target Code or Target Description in the search box.

> ![](sts-version-11-vets-11-user-guide/013.png)You can enter the first three numbers or letters of any Target Code or Target Description to initiate a search.

> <span id="_bookmark17" class="anchor"></span>Figure 9. Map Entry Window with Target Description

9.  Select the Target concept from the list.

> You can change the Map Entry Order to indicate the most significant mapping according to the Use Case. The Map Entry Order can be designated from 1 to 10, with 1 being the most significant.

> You can change the Membership Status from Active to Inactive.

> ![](sts-version-11-vets-11-user-guide/014.png)

> <span id="_bookmark18" class="anchor"></span>Figure 10. Map Entry Window with Source and Target

10. ![](sts-version-11-vets-11-user-guide/015.png)Click the Add link to add more Map Entries for this Source concept.

> <span id="_bookmark19" class="anchor"></span>Figure 11. Map Entry Window with Add Option

11. Repeat the steps to add all of your Map Entries for this Map Set.
12. Click the Clear link to clear a line from the screen that you added in error. This does not change the database; it only removes the row from the screen.
13. ![](sts-version-11-vets-11-user-guide/016.png)Click the Save button once you have entered your Map Entries.

> <span id="_bookmark20" class="anchor"></span>Figure 12. Map Entry Window with Successful Message

> A confirmation message displays stating your Map Entries are saved for this Map Set.

> Note: If you do not click the Save Map Entries button before clicking the Return to Edit Map Set button, a warning message displays There are unsaved changes on this page. Would you like to proceed to the Edit Map Set Page? Click the OK button if you do not want to save the changes. Click the Cancel button to return to the Map Entry with Add Option window to save your changes.

14. Click the Return to Edit Map Set button to view your new Map Set with saved Map Entries.

> ![](sts-version-11-vets-11-user-guide/017.png)

> <span id="_bookmark21" class="anchor"></span>Figure 13. Map Set Edit Window

15. Click the Edit link to edit a Map Entry.
16. Click the Add Map Entry button to add more Map Entries to the Map Set.

> You can use the Search box to find Map Entries that already exist in the Map Set. Type the first 3 numbers of the code or letters of the description of the Map Entry you are searching. Your search parameters are highlighted in all of the Map Entries that contain the parameters.

> Use the Display records pull down to display 25, 50, or 100 Map Entries per page.

> The page through buttons (First, Previous, Next, Last, etc.) allow you to move through the pages of existing Map Entries.

17. Click the CSV icon ![](sts-version-11-vets-11-user-guide/018.png) to export the Map Entries to a CSV file.
18. Click the Home tab to return to the Map Set Selection Window.

### Edit a Map Set and Map Entry

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Editing Map Sets and Map Entries uses many of the same steps as adding new Map Sets and Map Entries.

1.  On the Home page, click the Preferred Name link of the Map Set you want to edit.

> When you mouse over a Preferred Name Map Set link, the tool tip will read Edit Preferred Name Map Set or View Preferred Name Map Set. Only the Map Sets that read Edit are available for editing.

> ![](sts-version-11-vets-11-user-guide/019.png)

> <span id="_bookmark23" class="anchor"></span>Figure 14. Map Set Selection Window

> ![](sts-version-11-vets-11-user-guide/020.png)The Map Set: Edit window displays the Map Set you selected for editing.

> <span id="_bookmark24" class="anchor"></span>Figure 15. Map Set Edit Window

2.  You can edit the Preferred Name, Textual Definition, Description, and Status.
3.  Click the Save Map Set button to save your changes.

> Note: If you make changes to the Map Set and click the Edit button before clicking the Save Map Set button, your Map Set changes will not be saved.

4.  ![](sts-version-11-vets-11-user-guide/021.png)Click the Edit link to edit the Map Entry information.

> <span id="_bookmark25" class="anchor"></span>Figure 16. Map Entry Window

5.  On the Map Entry window, you can edit the Target Code and Target Description, the Map Entry Order, and the Membership Status.
6.  Click the Clear link to remove that row from the screen without changing the database.
7.  Click the Add link to add another Map Entry.
8.  If you Add a Map Entry, enter the Target Code and Target Description.
9.  Click the Save button to save your edits.

> Note: If you make changes to the Map Entry and do not click the Save button a pop up message displays There are unsaved changes on this page. Would you like to proceed to the edit Map Set page? Click the OK button to go to the Edit Map Set window, your edits will not be saved. Click the Cancel button to stay on the Map Entry window and click the Save button.

10. Click the Return to Edit Map Set button to return to the Map Set you are editing and view your changes.

# Terminology Deployment Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Terminology Deployment Service (TDS) allows the User to prepare, test, and deploy terminology.

### Workflow

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The workflow associated with TDS is displayed in the figure below. The following sections describe each phase in the diagram and the tools used during the phases.

![](sts-version-11-vets-11-user-guide/022.png)

> <span id="_bookmark28" class="anchor"></span>Preparation Phase

> Figure 17. TDS Workflow

> The first column, Preparation Phase, shows the workflow steps used to import content into VTS and to prepare it for use.

- Import and Export Content

> TDS imports and exports content depending on its type:

- Map Sets, VHAT, and Standards Development Organization (SDO) content can be imported as eXtensible Markup Language (XML) files.
- VHAT concepts and Map Sets can be exported as XML files.

> Import or Export files by selecting the Import option under the Update menu.

- Review

> During the review step, VHAT and Map Set content is checked for accuracy and consistency. Each Concept imported from VHAT can be reviewed separately.

> Review files by selecting the Review option under the Update menu.

- Change State to Ready To Test

> Each VHAT Concept is given a state parameter that shows its progress along the workflow. On initial import, the state assigned is Created. Once a VHAT Concept has passed the review step, its state is changed to Ready To Test. Only Concepts with a state of Ready To Test can progress to the next phase of the workflow.

> Change the state of files by selecting the Review option under the Update menu.

> Internal Test Phase

> The second column shows the workflow steps used within STS to test content.

- Create Deployment

> A Deployment consists of VHAT concepts or Map Sets that have been prepared to be sent to the VistA environments. Once VHAT terms are Ready To Test they are displayed on the Create Deployment screen and may be placed into a Deployment.

> Create a Deployment by selecting the Create option under the Deployment menu.

- Deploy Deployment

> Deployments may contain VHAT content or Map Sets. Deployments can be sent to any number of VistA environments that are used only for STS testing.

> Deploy a Deployment by selecting the Deploy option under the Deployment menu.

- Internal Testing

> VistA applications are tested to make sure that the terminology content performs as intended. Internal Testing is not performed in the TDS application.

- Change State to Ready To Be Versioned

> Once Internal Testing is complete; the Deployment is given the state of Ready To Be Versioned to indicate that it is ready for the next phase of the workflow.

> Change the state of the Deployment by selecting the Manage option under the Deployment menu.

> SQA Test Phase

> Prior to releasing the content for unrestricted production use, SQA independently tests the process of adding or updating content to VistA and the effects of the edited content on VistA environments.

- Create Candidate Version

> One or more Deployments that are Ready To Be Versioned may be combined into a single Candidate Version. Candidate Versions should contain Map Sets or VHAT content but not both. Versions at this stage of testing are qualified as Candidate Versions to indicate that they have not yet been approved by SQA.

> Create a Candidate Version by selecting the Create option under the Version menu.

- Deploy Candidate Version

> Candidate Versions can be sent to any number of VistA environments that are used only for SQA testing.

> Deploy the Candidate Version by selecting the Deploy CV option under the Version menu.

- SQA Testing

> VistA functions are tested to make sure that the terminology content is consumed by VistA applications as intended. SQA Testing is not performed in the TDS application.

> Production Phase

> Once content has completed SQA testing and has been approved by SQA as ready for unrestricted use by end-user applications, TDS is used to deploy content to production VistA applications at VA sites nationwide.

- Create Finalized Version

> Candidate Versions that have passed SQA testing are re-packaged as Finalized Versions in anticipation of distribution to VistA applications at production sites. For quality control purposes, each Finalized Version should contain only one Candidate Version so that the Finalized Version matches the conditions that the Candidate Version was certified under.

> Create a Finalized Version by selecting the Manage option under the Version menu.

- Deploy Finalized Version

> Final Versions can be sent to any of the production VA sites running VistA applications. Deploy a Finalized Version by selecting the Deploy option under the Version menu.

- Production Applications

> This point represents the intended end-result of the VETS deployment work flow, which is the application of terminology content for health care, research, teaching, and administrative purposes.

> Tools

> TDS contains many tools that are used throughout the Workflow phases.

- Validate

> This option produces a checksum from VTS and compares it with a Checksum for the same content from any of the VistA sites. Checksums are hexadecimal strings calculated from data in such a way that mismatched checksums indicate that data does not match between VTS and a VistA site. Checksums can be mismatched because of data corruption either during transport, or intentional or accidental changes at VistA sites. Checksums should be compared before and after each Deployment.

> Validate checksums by selecting the Test or Production options under the Validate menu.

- Discovery

> Discovery is used to determine the exact data differences leading to checksum mismatches. Differences (commonly referred to as diffs) include Map Sets or VHAT concepts that are present in VTS but not at the site, present at the site but not VTS, or present at both sites but differing in content or attributes.

> Discover data differences by selecting the Test or Production options under the Discovery menu.

- History

> This option shows the date and time that each Deployment, Candidate Version, or Finalized Version was sent to any of the internal, SQA, or production sites. It can be used to retrace the steps of deployment when investigating a checksum mismatch.

> Check history by selecting the History option under the Tools menu.

- Link and Unlink

> Two or more Finalized Versions can be linked, which causes them to be distributed

> together as a group. Linked Versions can contain Map Sets or VHAT content but not both. Although we intend to distribute Finalized Versions as single units, there are times when one version is created in order to replace specific content in another version. In this situation, linking the versions ensures that the new content replaces the previous content, not vice versa. Unlinking simply breaks a link should the need arise; e.g., if two versions were linked in error. Only Finalized Versions, not Candidate Versions, can be linked.

> Link or unlink the Finalized Versions by selecting the Link or Unlink options in the Tools menu.

- Group Editor

> VA sites may belong to a group, which allows a Finalized Version to be distributed to multiple sites by selecting a single group. A site can belong to only one group at a time.

> The Group Editor also allows you to create new groups and delete existing groups. Group sites by selecting the Group Editor option under the Tools menu.

- SCS Manage

> SCS Manage allows you to view Standard Code Systems and versions that are present in the repository.

> View Standard Code System content in the repository by using the Manage option under the SCS menu.

# Using STS VETS TDS V11.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The STS VETS TDS menu contains options that assist Domain Stewards, Primary Terminology Modelers, Modeling Reviewers, STS Testers, Testing Deployment Coordinators, Deployment Analysts, and SQA Team members to review, prepare, test, and deploy content to VistA sites.

> In addition to the menu options, links, and buttons the UI contains several icons. The icons assist in viewing and understanding the concept details. The icons include:

> Review

> The icons below display on the Concept Details screen in the Delta column when a change is made to the concept's state, properties, or relationships.

> ![](sts-version-11-vets-11-user-guide/023.png) - the white plus means a New Concept; designation, property, or relationship was added.

> ![](sts-version-11-vets-11-user-guide/024.png) - the white circle means the Concept's state was changed from inactive to active.

> ![](sts-version-11-vets-11-user-guide/025.png) - the blue slash means the concept was already in the system and the state was changed from active to inactive.

> ![](sts-version-11-vets-11-user-guide/026.png) - the white triangle means a change in property or relationship value. ![](sts-version-11-vets-11-user-guide/027.png) - the white X means a designation was removed from a concept.

> Validation and Discovery

> The icons below display during the Validation and Discovery procedures.

> ![](sts-version-11-vets-11-user-guide/028.png) - the red circle X and no data in the Receive Date column means that the Checksum has not been returned from the VistA site. The red circle X and a date in the Receive Date

> column means the Checksums do not match.

> ![](sts-version-11-vets-11-user-guide/029.png) - the red X means the site does not have the data or data has not been returned.

> ![](sts-version-11-vets-11-user-guide/030.png) - the green circle checkmark means the Checksum was returned from the VistA site.

> ![](sts-version-11-vets-11-user-guide/031.png) - the green checkmark means the data was received from the site and the Checksums match.

> ![](sts-version-11-vets-11-user-guide/032.png) - the blue circle question mark means the VistA Checksum matches a Checksum corresponding to a previous version of VTS. The system displays the previously matching version in the Version column. You only see the question mark from the Validate Production Sites window.

> Miscellaneous

> The icons below display on various screens throughout STS VETS TDS. ![](sts-version-11-vets-11-user-guide/033.png) - the plus and minus button expands and collapses the field.

> ![](sts-version-11-vets-11-user-guide/034.png) ![](sts-version-11-vets-11-user-guide/035.png) - the green up and down arrows indicate the column sorted on and allow you to change the sort order. The down arrow indicates the sort order is descending, Z – A. The

> up arrow indicates the sort order is ascending, A – Z.

### Lo gin

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \- the CSV icon allows you to export your data to a CSV file.

> ![](sts-version-11-vets-11-user-guide/036.png)Follow the steps below to log in to the STS VETS TDS application:

1.  Navigate to the application entry point.
2.  Enter your Username and Password in the boxes provided.
3.  Click the Login box or press Enter on your keyboard.

> ![](sts-version-11-vets-11-user-guide/037.png)

> <span id="_bookmark31" class="anchor"></span>Figure 18. Login Window

> ![](sts-version-11-vets-11-user-guide/038.png)Consistent with VHA policy, your session times out after a period of 30 minutes of inactivity. At 25 minutes, a 5-minute warning message displays and you have 5 minutes to respond before your session times out.

> <span id="_bookmark32" class="anchor"></span>Figure 19. STS Deployment Window

### Update

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> When the log in is successful the current system name, the menu on the left, and the environment window display on the screen.

> This option allows you to import new or changed content into the system. Follow the steps to import VHAT, Standard Code Systems, or Map Sets data.

1.  Click Import in the left navigation panel under Update. To import data:
    1.  On the Import window, click the Browse button to locate:

> a\. New VHAT content or changes to existing VHAT content.

> b\. A new Standard Code System or a new version of an existing Standard Code System.

> Imported SCS data is displayed in the Manage option in the left navigation panel under SCS. SCS data is not deployed and can only be viewed in the Terminology Browser.

> c\. A new Map Set or a new version of an existing Map Set.

2.  Click the Import button.

> When an import is successful, a message displays.

> To Export data:

1.  On the Import window, click the Export button.

> You can export VHAT content as XML files to your desktop.

> ![](sts-version-11-vets-11-user-guide/039.png)

> <span id="_bookmark34" class="anchor"></span>Figure 20. Import Window

> Follow the steps below to review the content changes and promote changes to the Ready To Test state.

1.  Click Review under the Update option.
2.  Select the Domains and States you want to review, and click the Get Changes

> ![](sts-version-11-vets-11-user-guide/040.png)button.

> <span id="_bookmark35" class="anchor"></span>Figure 21. Review Change Set Window

> There are five Concept States: Created, Ready To Review, Under Review, Failed Review, and Ready To Test. When a Concept is in the process of being created, authored, it is granted a Created state. When the Author is ready for the modeling review to review the content it is imported and granted a Ready to Review state. While the Concepts are being reviewed, the modeling reviewer changes the state to Under Review. If the Concepts are not approved, the modeling review changes the state to Failed Review, the Author can then change the state to Created, and the Concepts are available for Editing in the Terminology Editor (TED). When a modeling reviewer approves a Concept, they change the state to Ready To Test. This makes the Concept available to be included in a deployment.

> On the Change Set Summary window, select the Concept(s) you want to change the state of and select the state from the pull down menu, and click the Change State button.

> ![](sts-version-11-vets-11-user-guide/041.png)

> <span id="_bookmark36" class="anchor"></span>Figure 22. Change Set Summary Window

> The Concept names in the Preferred Name column are links to the Concept Details of each Concept. You can click the Preferred Name link to open the Concept Detail window of the Concept you wish to review.

> On the Concept Detail window, you can review the Concept’s details for accuracy and assign a State. There are five Concept States:

> Created - Assigned when an item first exists in the system. During this workflow, items can be edited.

> Ready To Review - Assigned to an item when editing is completed and content accuracy needs to be reviewed.

> Under Review - Assigned when a User is reviewing the item. When complete the item is promoted to Ready to Test or demoted to Created.

> Failed Review - Assigned when the Map Set has not passed review. A workflow of Failed Review prevents a Map Set from being included in a deployment.

> Ready To Test - Assigned when the item has passed review and is ready to be promoted into a deployment.

> When a concept is in the process of being authored in TED or when it is first imported into TDS it is granted a Created state. When the Author is ready for the modeling reviewer to review the content the Author grants a Ready To Review state. While the concepts are being reviewed, the modeling reviewer changes the state to Under Review. If the Concepts are not approved, the modeling reviewer changes the state to Failed Review. The Author can change the state back to Created and continue working in TED. When a modeling reviewer approves a concept, they change the state to Ready To Test. This makes the concept available to be included in a deployment.

> If the details are correct:

3.  Select Ready To Test in the pull down menu and click the Change State button.

> ![](sts-version-11-vets-11-user-guide/042.png)

### SCS

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Figure 23. Concept Detail Window

> This window also contains buttons to move through the concept list. Click the Previous or Next buttons to view the Concept Details of other concepts. You can return to the Change Set Summary window by clicking the View Summary button.

> The Concept Detail screen also displays the Designations; the textual expression of the concept, any properties and relationships associated to that Designation, and its participation in a Designation subset. Click the link to open the Associated Subset Detail to view the details of that Subset.

> Use the SCS Manage option to view the imported Standard Code Systems (SCS). SCS are not deployed but used by Map Sets for validation. Map Sets are dependent on SCS being in the system.

> Before importing Standard Code Systems in the Update Import option, use the Manage SCS window to see if the Code System is already in the system.

> Click Manage under the SCS option. The Manage SCS window displays the name of the Code Systems, Versions of the Code Systems, the number of Entries, and the date the Code System was imported in the VETS Import Date column. The Remove column displays the Remove option if that version of the Code System can be removed. Click the Remove link to remove the version from the system. If a Map Set in the system uses a particular SCS version, then that SCS version may not be removed.

> ![](sts-version-11-vets-11-user-guide/043.png)

### Deployment 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Figure 24. Manage SCS Window

> This section refers to the set up and preparation for the Internal Testing phase. Content testing is performed in VistA applications and is not covered in this manual.

> Follow the steps below to create a Deployment for internal testing:

1.  Click Create in the Deployment menu.
2.  On the Create Deployment – RTT Terms Displayed window, select the Ready To Test Concepts you want to deploy for testing and click the Create Deployment button.

> A successfully created deployments message, Deployment Details, and the size and text of the HL7 message display. The deployment name is the combination of the date and time that it was created.

> ![](sts-version-11-vets-11-user-guide/044.png)

> <span id="_bookmark41" class="anchor"></span>Figure 25. Deployment Created Window

> For a non-VistA deployment (content that is not deployed to the VistA sites but needs to be included in VHAT), no HL7 message is created.

> Note: The non-VistA content still needs to be carried through the Deployment -\> Candidate Version -\> Version process.

> If the deployment was not created successfully, an error message displays.

> Note: Performing a Checksum at this point tests for a connection as well as checking for consistency between VTS and VistA sites is recommended.

> On the Deployment Created window, if a Checksum has already been performed, you can click the Proceed to Deployment button to jump to the Deploy option.

3.  Click Test in the Validate menu.
4.  On the Validate Internal and SQA Sites window, select the Site, Domain, and Deployment you are checking on, and click the Request Checksum button.

> Requesting the Checksum generates and compares new Checksums for the criteria you selected. If the Checksums were previously requested for the criteria you selected and nothing new has been deployed to the VistA site, click the Compare Checksum button to view the Checksums.

> The Display Checksum Results for Sites window displays the Checksum status information. Click the Refresh button periodically until the Receive Date column is populated.

> ![](sts-version-11-vets-11-user-guide/045.png)

> <span id="_bookmark42" class="anchor"></span>Figure 26. Display Checksum Results for Sites Window

- A ![](sts-version-11-vets-11-user-guide/046.png) in the Match column and no date in the Receive Date column means that the Checksum has not been returned from the VistA site.
- A ![](sts-version-11-vets-11-user-guide/047.png) in the Match column and a date in the Receive Date column means that the Checksums between VTS and VistA do not match.
- A ![](sts-version-11-vets-11-user-guide/048.png) in the Match column means the Checksums between VTS and VistA match.
5.  Click Deploy in the Deployment menu.
6.  On the Deploy Deployment window, select the Deployment(s) you want to deploy, the Site(s) you want to deploy to, and click the Confirm Deployment button.

> The Verify Deployment and Test Sites window displays the selected Deployments, Sites, and the HL7 message and message size. The HL7 message is a visual cue that the deployment was formed correctly.

> ![](sts-version-11-vets-11-user-guide/049.png)

> <span id="_bookmark43" class="anchor"></span>Figure 27. Verify Deployment and Test Sites Window

7.  Click the Deploy button to deploy to the selected sites.

> The Deployment Results window displays a sent message and the deployment information. The acknowledgement (ACK) field is initially empty. Click refresh periodically until it is populated with either:

- Application Acknowledgement (AA) – the message made it to the site and was processed correctly.
- Application Error (AE) – the message was received at the site but was not processed correctly.

> ![](sts-version-11-vets-11-user-guide/050.png)

> <span id="_bookmark44" class="anchor"></span>Figure 28. Deployment Results Window with ACK Populated

> If the ACK field does not populate after considerable time, there may be a problem with the connection to the site.

8.  If the content is ready to be promoted to a Candidate Version, click Manage in the Deployment menu.
9.  On the Manage Deployment window, select the Deployment that is Ready To Be Versioned by putting a checkmark next to the deployment.

> Note: The Map Sets in the Deployment are links to their details. Click the Map Set name to view the details.

> ![](sts-version-11-vets-11-user-guide/051.png)

> <span id="_bookmark45" class="anchor"></span>Figure 29. Manage Deployment Window

> Checking the Deployment as Ready To Be Versioned makes it eligible for inclusion in a Candidate Version. The Concepts column displays the number of Concepts in the Deployment. The Map Entries column displays the number of Map Entries in the Map Set Deployment.

- Click the Remove link to remove a deployment in that row.

> Removing a deployment returns all of the concepts in that deployment to the Created state. However, if that deployment was deployed to VistA the system does not remove the update made to VistA. This will cause a checksum mismatch. To ensure checksum match you can remove the updates from VistA in the following ways:

> If a concept property, relationship, or status value was updated you can deploy the last Finalized Version containing concept with its previous values.

> If a new concept, designation, property, or relationship was introduced you can inactivate these new values, create a deployment, and deploy this to the test sites.

- Click the Remove link to remove a Map Set deployment in that row.

> If a Map Set deployment is removed and it has been deployed to VistA, the system does not remove the update made to VistA. This will cause a checksum mismatch. To ensure checksums match you can remove the updates from VistA in the following ways:

> If a status value was updated you must use TED to add the Map Entry to the Import file if it did not exist on the initial import, and redeploy.

### Version

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> If a new Map Entry was introduced you must use TED to inactivate it in the Import file and redeploy.

> This section refers to the set up and preparation for SQA Testing. Content testing is performed in VistA applications at the SQA sites and is not covered in this manual.

> Follow the steps below to create a Candidate Version:

1.  Click Create in the Version menu.
2.  On the Create Candidate Version window, select the Deployments you want to promote to a Candidate Version and click the Create Candidate Version button.

> The Candidate Version Created window displays a successful message, Candidate Version details, and the HL7 message and the message size. The Candidate Version’s name is the date and time that the Candidate Version was created.

> If the Candidate Version was not created successfully, an error message displays.

> ![](sts-version-11-vets-11-user-guide/052.png)For a non-VistA deployment (content that is not deployed to the VistA sites but needs to be included in the VHAT), no HL7 message is created.

> <span id="_bookmark47" class="anchor"></span>Figure 30. Candidate Version Created Window

> If a Checksum has already been performed, you can click the Proceed to Deployment

> button to jump to the Deploy option.

> Note: Performing Checksum at this point tests for a connection as well as checking for consistency between VTS and VistA sites.

3.  Click Test in the Validate menu.
4.  On the Validate Internal and SQA Sites window, select the SQA sites; the Domains, subsets, or Map Sets; Deployments, Candidate Versions, or Versions; and click the Request Checksum button.

> Requesting the Checksum generates and compares new Checksums for the criteria you selected. If the Checksums were previously requested for the criteria you selected and nothing new has been deployed to the VistA site, click the Compare Checksum button to view the Checksums.

> The Display Checksum Results for Sites window displays the Checksum status information. Click the Refresh button periodically until the Receive Date column is populated.

- A ![](sts-version-11-vets-11-user-guide/053.png) in the Match column and no date in the Receive Date column means that the Checksum has not been returned from the VistA site.
- A ![](sts-version-11-vets-11-user-guide/054.png) in the Match column and a date in the Receive Date column means that the Checksums between VTS and VistA do not match.
- A ![](sts-version-11-vets-11-user-guide/055.png) in the Match column means the Checksums between VTS and VistA match.
5.  Click Deploy CV in the Versions menu.
6.  On the Candidate Version Deployment – Select Candidate Version and Test Sites window select one or more Candidate Versions and the SQA sites, and click the Confirm Deployment button.

> ![](sts-version-11-vets-11-user-guide/056.png)The Verify Candidate Version and Test Sites window displays the selected Candidate Versions, Sites, and the HL7 message and the message size.

> <span id="_bookmark48" class="anchor"></span>Figure 31. Verify Candidate Versions and Test Sites Window

7.  Click the Deploy button to deploy the Candidate Version to the selected sites.

> The Deployment Result window displays a sent message and the deployment information. The ACK field is initially empty. Click refresh periodically until it is populated with either:

- AA – the message made it to the site and was processed correctly.
- AE – the message was received at the site but was not processed correctly.

> If the ACK field does not populate after considerable time, there may be a problem with the connection to the site.

8.  Click Manage in the Versions menu.

> The Candidate Version’s date and time stamp is a link to the Deployment Details window. The Deployment Details window displays Candidate Version details. You can view the HL7 message and export the content.

> On the Manage Version window, you can click the Remove link to remove the Candidate Version from the deployment list. All of the deployments it contains return to the Ready To Be Versioned state.

> However, if that deployment was deployed to VistA the system does not remove the update made to VistA. This will cause a Checksum mismatch. To ensure Checksum match you can remove the updates from VistA in the following ways:

> For a VHAT Deployment -

- If a concept property, relationship, or status value was updated you can deploy the last Finalized Version containing concept with its previous values
- If a new concept, designation, property, or relationship was introduced you can inactivate these new values, create a deployment, and deploy this to the test sites.

> For a Map Set Deployment -

- If a status value updated you must use TED to add the Map Entry to the Import file if it did not exist on the initial import, and redeploy.
- If a new Map Entry was introduced you must use TED to change the status in the Import file and redeploy.
9.  On the Manage Version window, select a Candidate Version you want to finalize and click the Finalize Version button.

> Finalized Version names are sequential numbers. The content in the new Finalized Version is now available for viewing in the Terminology Browser.

> ![](sts-version-11-vets-11-user-guide/057.png)

> <span id="_bookmark49" class="anchor"></span>Figure 32. Manage Version Window

> ![](sts-version-11-vets-11-user-guide/058.png)If the Candidate Version was successfully promoted to a Finalized Version, a successfully created version message displays.

> <span id="_bookmark50" class="anchor"></span>Figure 33. Finalized Versions Window

### Finalized Version

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Follow the steps below to deploy the Finalized Version to production:

1.  Click Deploy on the Version menu.

> Clicking the version number link opens the Version Details window. The version details also contain additional links to show further content details.

2.  On the Version Deployment window select the Version and click the Proceed to Site Selection button.

> You can select one or more subsets within a version to deploy a partial version.

> Non-VistA Versions do not have a checkbox, so they cannot be included in the deployment.

3.  On the SQA Deployment window select the Sites or Group Name, and click the

> Confirm Deployment button.

> The Verify Deployments and Production Sites window displays the selected versions or subsets within a version, Sites, and the HL7 message and the message size.

4.  ![](sts-version-11-vets-11-user-guide/059.png)Click the Deploy button to deploy the Finalized Version to the production sites.

> <span id="_bookmark52" class="anchor"></span>Figure 34. Verify Deployments and Production Sites Window

> The Deployment Result window displays a sent message and the deployment information. The ACK field is initially empty. Click refresh periodically until it is populated with either:

- AA – the message made it to the site and was processed correctly.
- AE – the message was received at the site but was not processed correctly.

> If the ACK field does not populate after considerable time, there may be a problem with the connection to the site.

5.  Click Production on the Validate menu.
6.  On the Validate Production Sites window select the Group Name or individual Production Site, select the Domain, and click the Request Checksum button.

> ![](sts-version-11-vets-11-user-guide/060.png)

### Logout 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Figure 35. Production Validation Window

> The Display Checksum Results for Sites window displays the Checksum status information. Click the Refresh button periodically until the Receive Date column is populated.

- A ![](sts-version-11-vets-11-user-guide/061.png) in the Match column and no data in the Receive Date column means that the Checksum has not been returned from the VistA site.
- A ![](sts-version-11-vets-11-user-guide/062.png) in the Match column and a date in the Receive Date column means that the Checksums between VTS and VistA do not match.
- A ![](sts-version-11-vets-11-user-guide/063.png) in the Match column means the Checksums between VTS and VistA match.
- A ![](sts-version-11-vets-11-user-guide/064.png) in the Match column means the VistA Checksum matches a Checksum corresponding to a previous version of VTS. The system displays the previously matching version in the Version column.

> Click the Logout link at the top of the environment window to log out of the system.

# Troubleshooting STS TDS V11.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The information in this section describes how to use the Tools in STS Terminology Deployment Service V11.0.

### Validate

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Validate menu contains options for Test and Production information. The process to obtain the data is the same for both the Test and Production information.

> This option produces a checksum from VTS and compares it with a Checksum for the same content from any of the VistA sites. Checksums are hexadecimal strings calculated from data in such a way that mismatched checksums indicate that data does not match between VTS and a VistA site. Checksums can be mismatched because of data corruption either during transport, or intentional or accidental changes at VistA sites. Checksums should be compared before and after each Deployment.

### Discovery

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Discovery menu contains options for Test and Production information. The process to obtain the data is the same for both the Test and Production menu options. The only difference is that in the Test Discovery you select Deployment and Candidate Version along with Finalized Version, and Internal or SQA sites to discover the data each contains. In the Production Discovery, you select Version and Production sites to discover the data they contain. In this section, the Test Discovery path is described.

> To display the actual content differences, follow the directions below:

> Click the Test option in the Discovery menu to open the Discovery – Select Subsets/Map Sets Test window. In this window, select the Subset or Map Set you want to view and click the Proceed to Deployment Selection button.

> ![](sts-version-11-vets-11-user-guide/065.png)

> <span id="_bookmark58" class="anchor"></span>Figure 36. Discovery – Select Subsets/Map Sets Window

> The Discovery – Select Deployment, Candidate, or Version Test window displays the Deployments, Candidate Versions, and Versions associated with the Subset or Map Set you selected. Select Deployment(s), Candidate Version(s), and Version, and click the Proceed to Site Selection button. The Versions are cumulative so selecting higher numbered versions includes content created for that version and everything in the prior versions.

> ![](sts-version-11-vets-11-user-guide/066.png)

> <span id="_bookmark59" class="anchor"></span>Figure 37. Discovery – Select Deployment, Candidate, or Version Test Window

> The Discovery – Select Sites Test window displays a list of SQA and Internal Sites. The date and time stamp in the Retrieved column corresponding to a site indicates the last time data was requested for the site. Click the View Data button to retrieve the data.

> Select one or more Sites and click the Request Data button.

> ![](sts-version-11-vets-11-user-guide/067.png)

> <span id="_bookmark60" class="anchor"></span>Figure 38. Discovery – Select Sites Test Window

> The Discovery Results window displays if the site selected has returned data.

- A ![](sts-version-11-vets-11-user-guide/068.png) indicates data has been returned from the VistA site.
- A ![](sts-version-11-vets-11-user-guide/069.png) indicates data has not yet returned.

> After the data has been returned from the VistA site, to view the differences between the results, click the View Differences button. Click the Refresh button to update the information.

> Note: All sites should return data before you click the View Differences button. Otherwise, data that has not yet returned might be misinterpreted as data that is missing from the VistA site.

> View Differences displays a table showing differences between VTS and site data.

> ![](sts-version-11-vets-11-user-guide/070.png)

> <span id="_bookmark61" class="anchor"></span>Figure 39. Discovery Results Test Window

> The bottom tables in Figures 40 and 41 show differences between VA Terminology Server (VTS) and site data. There are three situations leading to data discrepancies:

- In Figure 40 in the top three rows, the VTS column contains values, but the VistA column is blank. This means that some VTS data is not present at the VistA site.
- In Figure 41, the next seven rows display data that is present in VistA but not in VTS.
- In Figure 41, the following rows display the Field Name differences between VTS and VistA sites.

> Rows only display if there are data differences. If there are no differences between VTS and the VistA site, then the second table does not display. Instead, a message displays stating that there are no data differences.

> ![](sts-version-11-vets-11-user-guide/071.png)

> ![](sts-version-11-vets-11-user-guide/072.png)<span id="_bookmark62" class="anchor"></span>Figure 40. Discovery Results Window

### Tools

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Figure 41. Discovery Results Window

> Only differences for active designations display initially. To display differences for inactive designations, click the Show Inactive button.

> Note: Only active designations are used in the calculation of checksums. Inactive designations will not cause a checksum to be mismatched.

## History

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To view a summary of deployments that were sent to a site and whether or not the deployments were processed without error at the receiving site, follow the directions below:

> Click the History option in the Tools menu to open the Deployment History – Select Deployments window. This window displays a list of Deployments, Candidate Versions, and Versions. The names of Deployments, Candidate Versions, and Version numbers are links

> ![](sts-version-11-vets-11-user-guide/073.png)that opens a details window showing the content. Select the item you want to view and click the Proceed to Site Selection button.

> <span id="_bookmark66" class="anchor"></span>Figure 42. Deployment History – Select Deployments Window

> The Deployment History – Select Sites window displays a list of Internal, SQA, and Production sites. Select the Sites you want to view and click the View History button.

> ![](sts-version-11-vets-11-user-guide/074.png)

> <span id="_bookmark67" class="anchor"></span>Figure 43. Deployment History – Select Sites Window

> The Deployment History – Results window displays the history of the Sites selected. The Description field indicates the subsets that were deployed to the selected site. A partial version deployment is indicated if the Description field does not display all of the domains and subsets contained in the Version selected. Click the Refresh button to update the information.

> ![](sts-version-11-vets-11-user-guide/075.png)

> <span id="_bookmark68" class="anchor"></span>Figure 44. Deployment History – Results Window

> At the bottom of the Deployment History – Results window you have an Export option: CSV. This option allows you to export the history as a Comma-Separated Value (CSV) file. How you view the file depends on what application you use to read a .csv file.

## Link and Unlink

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To Link or Unlink versions, follow the directions below:

> Click the Link option on the Tools menu to open the Link Versions window. The Link Versions window displays a list of unlinked Versions. Select the versions to link and click the Link Versions button. A Linked Version can only contain VHAT Versions. V11.0 Map Sets cannot be linked.

> ![](sts-version-11-vets-11-user-guide/076.png)

> <span id="_bookmark70" class="anchor"></span>Figure 45. Link Versions Window

> Once a version is finalized, its content cannot be edited. If corrections to a Finalized Version are required, a subsequent version containing the revised content must be finalized and linked to the incorrect Finalized Version. This ensures the corrected content always deploys with the version that contained the mistake.

> Subsets within linked Versions can be deployed separately. For example, see Figure 46. The Version Deployment – Select Versions to Deploy window displays linked versions 40, 41, and 42. These versions contain content for two subsets: Nature of Order and TIU Titles.

> Selecting the checkbox by Nature of Order ensures that only the content for this subset deploys.

> ![](sts-version-11-vets-11-user-guide/077.png)

> <span id="_bookmark71" class="anchor"></span>Figure 46. Partial Deployment of a Linked Version from Version Deployment – Select Versions to Deploy Window

> ![](sts-version-11-vets-11-user-guide/078.png)Click the Unlink option on the Tools menu to open the Unlink Versions window. This window displays a list of Linked Versions. Select the Linked Versions that you want to unlink and click the Unlink Versions button.

> <span id="_bookmark72" class="anchor"></span>Figure 47. Unlink Version Window

## Group Editor

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To create, edit, or delete a Group follow the directions below:

> Click the Group Editor option on the Tools menu to open the Group Editor window. The Group Editor window displays lists of previously created groups and Production Sites.

> To create a new group click the Create Group checkbox, enter a group name in the box provided, select the sites you want to include in your group, and click the Save Group button. A site can only belong to one group at a time. The name of your group displays in the Group Name box. When you select your Group, the sites you included are also selected.

> Note: You cannot include apostrophes in Group Names, i.e. Jane Doe’s Group should be

> ![](sts-version-11-vets-11-user-guide/079.png)Jane Does Group.

> <span id="_bookmark74" class="anchor"></span>Figure 48. Group Editor Window

> To add new sites to a Group check the Group Name, select new sites to add, and click the

> Save Group button.

> To remove a site from a group, check the site and click Remove Group from Site(s) button. This will display a warning message. Click the OK button to continue removing the site from the group.

> To delete an entire Group, select the Group Name and click the Remove Group from Site(s) button. This will display a warning message. Click the OK button to continue the deletion of the group.

> Note: A group must have at least one member site. Removing all the member sites from a group results in the group name being deleted.

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The Glossary contains terms and acronyms referenced in the STS VETS Version 11.0 User Guide and applications.

### STS Terminology Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 79%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Term</strong></th>
<th><strong>Definition</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Application Program Interface (API)</strong></td>
<td><p>An API is:</p>
<ol type="1">
<li><p>The interface or set of functions, between the application software and the application platform.</p></li>
<li><p>The means by which an application designer enters and retrieves information.</p></li>
</ol></td>
</tr>
<tr class="even">
<td><strong>archetype</strong></td>
<td><p>An archetype is:</p>
<ol type="1">
<li><p>A syntactically and semantically structured aggregation of vocabulary or other data that is the basic unit of clinical information. See also: template.</p></li>
<li><p>A formal, reusable model of a concept for a given domain.</p></li>
</ol></td>
</tr>
<tr class="odd">
<td><strong>attribute</strong></td>
<td>A named characteristic of a concept that can be assigned a value. See also: property (preferred).</td>
</tr>
<tr class="even">
<td><strong>authoring</strong></td>
<td>The process of creating and editing terminology content. See also: development environment.</td>
</tr>
<tr class="odd">
<td><strong>Candidate Version</strong></td>
<td>Terminology Deployment Server (TDS) content that has passed internal testing and is sent to Software Quality Assurance (SQA) for quality assurance testing.</td>
</tr>
<tr class="even">
<td><strong>change set</strong></td>
<td>A generic term for any terminology content that is deployed by TDS; specifically an Initial Deployment, a Candidate Version, or a Finalized Version.</td>
</tr>
<tr class="odd">
<td><strong>characteristic</strong></td>
<td>An attribute or behavior of something. See also: property.</td>
</tr>
<tr class="even">
<td><strong>child</strong></td>
<td>The subtype in a parent-child relationship. The child (subtype) is narrower and more specific while the parent (supertype) is broader and more general. The child inherits the characteristics of the parent.</td>
</tr>
<tr class="odd">
<td><strong>classification</strong></td>
<td>Groupings of concepts for a given purpose where entries are found in one category.</td>
</tr>
<tr class="even">
<td><strong>code set</strong></td>
<td>Any set of codes used for encoding data elements, such as tables of terms, medical concepts, medical diagnosis codes, or medical procedure codes.</td>
</tr>
<tr class="odd">
<td><strong>component</strong></td>
<td>An identifiable item in the main body of SNOMED CT or in an authorized extension. Components include concepts, descriptions, relationships, subsets, histories, and extensions.</td>
</tr>
<tr class="even">
<td><strong>Computerized Patient Record System (CPRS)</strong></td>
<td>The CPRS is the people, data, rules and procedures, processing and storage devices, and communication and support facilities that provide the capture, storage, processing, communication, security, and presentation of computer-based patient record information.</td>
</tr>
<tr class="odd">
<td><strong>concept</strong></td>
<td>An abstract unit of thought.</td>
</tr>
<tr class="even">
<td><strong>concept equivalence</strong></td>
<td>Concept equivalence occurs when two concepts have the same meaning.</td>
</tr>
<tr class="odd">
<td><strong>concept to concept linking</strong></td>
<td>Concept to concept linking is when one concept is explicitly associated with another concept. Types of concept-to-concept linking are the creation of Map Sets, Translation Services, and Pre and Post Coordinated terms.</td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 79%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Term</strong></th>
<th><strong>Definition</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>context</strong></td>
<td><p>A context can be:</p>
<ol type="1">
<li><p>The environment in which it is appropriate to display a specific designation for a concept.</p></li>
<li><p>A specified part or field of a patient record, application, protocol, query, or communication in SNOMED CT.</p></li>
</ol></td>
</tr>
<tr class="even">
<td><strong>data cleanup</strong></td>
<td>Activities that are taken to correct, normalize, and eliminate terms from a reference file before it is matched to a new standard. See also: standardization.</td>
</tr>
<tr class="odd">
<td><strong>data model</strong></td>
<td>A schema that describes the way data is represented.</td>
</tr>
<tr class="even">
<td><strong>data standardization</strong></td>
<td>The process of defining, creating, deploying, and maintaining a common terminology resource.</td>
</tr>
<tr class="odd">
<td><strong>datatype</strong></td>
<td>A data storage format that can contain a specific type or range of values.</td>
</tr>
<tr class="even">
<td><strong>deploy</strong></td>
<td><p>Deploy means:</p>
<ol type="1">
<li><p>Within general software development, to send electronically as a unit.</p></li>
<li><p>Within STS, to publish terminology content from the development to production environments.</p></li>
</ol></td>
</tr>
<tr class="odd">
<td><strong>deployment</strong></td>
<td><p>A deployment is:</p>
<ol type="1">
<li><p>The process of publishing terminology content from the development environment to the production environment.</p></li>
<li><p>Groups of concepts that are ready to be tested and potentially added to the terminology.</p></li>
</ol></td>
</tr>
<tr class="even">
<td><strong>description</strong></td>
<td>The text that represents a concept in human readable form. See also: designation (preferred).</td>
</tr>
<tr class="odd">
<td><strong>designation</strong></td>
<td>A representation of a concept. See also: description, display form, expression, surface form, term.</td>
</tr>
<tr class="even">
<td><strong>development environment</strong></td>
<td>All the software and hardware components needed to create or edit a terminology. See also: authoring.</td>
</tr>
<tr class="odd">
<td><strong>display form</strong></td>
<td>A representation of a concept. See also: designation (preferred), description, expression, surface form, term.</td>
</tr>
<tr class="even">
<td><strong>domain</strong></td>
<td><p>A domain is:</p>
<ol type="1">
<li><p>A specialized discipline of medicine.</p></li>
<li><p>A set of terms belonging to a specialized discipline of medicine.</p></li>
<li><p>A set of terms associated within a VistA application.</p></li>
</ol></td>
</tr>
<tr class="odd">
<td><strong>entity relationship model</strong></td>
<td>A graphical representation of work or information flow. Consists of entities (things), attributes (data), and relationships (connections between entities). Often used to model basic work or information flow. See also: information model, terminology model.</td>
</tr>
<tr class="even">
<td><strong>expression</strong></td>
<td>Human readable representation of a concept or the name of a concept. See also: designation (preferred), description, surface form.</td>
</tr>
<tr class="odd">
<td><strong>Finalized Version</strong></td>
<td>TDS content that has passed SQA testing and is sent to production sites for field use.</td>
</tr>
<tr class="even">
<td><strong>Health Data Repository (HDR)</strong></td>
<td>The HDR is a repository of clinical information normally residing on one or more independent platforms for use by clinicians and other personnel in support of patient-centric care.</td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 79%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Term</strong></th>
<th><strong>Definition</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Health Level Seven (HL7)</strong></td>
<td><p>HL7 is:</p>
<ol type="1">
<li><p>One of the American National Standards Institute (ANSI) accredited Standards Developing Organizations (SDO) operating in the healthcare arena.</p></li>
<li><p>An interoperability specification for transactions produced and received by computer systems.</p></li>
</ol></td>
</tr>
<tr class="even">
<td><strong>homophone</strong></td>
<td>One of two or more words pronounced alike but different in meaning, derivation, or spelling.</td>
</tr>
<tr class="odd">
<td><strong>homonym</strong></td>
<td>One of two or more words spelled and pronounced alike but different in meaning.</td>
</tr>
<tr class="even">
<td><strong>International Classification of Diseases – 9<sup>th</sup> edition</strong> (<strong>ICD-9)</strong></td>
<td>ICD-9 classifies morbidity and mortality information for statistical purposes and for indexing of hospital records by disease and operations for data storage and retrieval.</td>
</tr>
<tr class="odd">
<td><strong>International Classification of Diseases – 9<sup>th</sup> edition – Clinical Modification (ICD-9-CM)</strong></td>
<td>ICD-9-CM is a clinical modification of the World Health Organization’s ICD-9. It purpose is to classify morbidity data for indexing medical records, medical care review, and ambulatory and other medical care programs as well as for basic health statistics.</td>
</tr>
<tr class="even">
<td><strong>initial deployment</strong></td>
<td>TDS content that has passed initial review and is sent to testing sites for internal evaluation.</td>
</tr>
<tr class="odd">
<td><strong>Internal Entry Number (IEN)</strong></td>
<td>A number used to identify an entry within a file. Every record has a unique internal entry number. In a VistA file, an IEN is a numerical identifier.</td>
</tr>
<tr class="even">
<td><strong>information model</strong></td>
<td>A structured specification, expressed graphically and/or narratively, of the information requirements of a domain. An information model describes the required classes of information and the properties of those classes, optionally including attributes, relationships, and other essential information. See also: entity relationship model, terminology model.</td>
</tr>
<tr class="odd">
<td><strong>lexicon</strong></td>
<td><p>A lexicon is:</p>
<ol type="1">
<li><p>The vocabulary of a language. See: terminology</p></li>
<li><p>Commonly used to refer to VistA’s Lexicon Utility.</p></li>
</ol></td>
</tr>
<tr class="even">
<td><strong>Logical Observation Identifiers, Names, And Codes (LOINC)</strong></td>
<td>The LOINC database provides a set of universal names and ID codes for identifying laboratory and clinical observations. LOINC codes are used to facilitate the exchange and pooling of clinical laboratory results, such as blood hemoglobin or serum potassium, for clinical care, outcomes management, and research.</td>
</tr>
<tr class="odd">
<td><strong>map entry</strong></td>
<td>The link between concepts from a source code system to one or more concepts from a target code system. Map entries may be from two standard code systems or from within the same code system. A map entry is an instance of the data in a Map Set.</td>
</tr>
<tr class="even">
<td><strong>map entry order</strong></td>
<td>The numeric order of the target code(s) for a source code.</td>
</tr>
<tr class="odd">
<td><strong>map set</strong></td>
<td>A collection of map entries with associated metadata.</td>
</tr>
<tr class="even">
<td><strong>metadata</strong></td>
<td>Attributes that describe the format and content of information to enable sharing of information between users and applications.</td>
</tr>
<tr class="odd">
<td><strong>modifier</strong></td>
<td>A word or phrase associated with a concept that changes its meaning.</td>
</tr>
<tr class="even">
<td><strong>nomenclature</strong></td>
<td>A system of names and groupings, which is structured according to pre-established naming rules. See also: classification, taxonomy.</td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 79%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Term</strong></th>
<th><strong>Definition</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>non-domain</strong></td>
<td>Content that is not part of a clinical domain.</td>
</tr>
<tr class="even">
<td><strong>non-VistA</strong></td>
<td>Content that is not deployed to VistA.</td>
</tr>
<tr class="odd">
<td><strong>normalization</strong></td>
<td>The process of identifying lexical variations of concepts that may include identification of synonyms.</td>
</tr>
<tr class="even">
<td><strong>New Term Rapid Turnaround (NTRT)</strong></td>
<td>The process to distribute standard reference files to VistA environments.</td>
</tr>
<tr class="odd">
<td><strong>ontology</strong></td>
<td><p>Ontology is:</p>
<ol type="1">
<li><p>An explicit formal specification of how to represent the objects, concepts, and other entities that are assumed to exist in some area of interest and the relationships that hold among them. See also: terminology.</p></li>
<li><p>All terms in a domain including the relationships among them.</p></li>
</ol></td>
</tr>
<tr class="even">
<td><strong>parent</strong></td>
<td>The supertype in a parent-child relationship. The child (subtype) is narrower and more specific while the parent (supertype) is broader and more general. The child inherits the characteristics of the parent.</td>
</tr>
<tr class="odd">
<td><strong>partial deployment</strong></td>
<td>Deploying one or more subsets within a version instead of deploying the entire version.</td>
</tr>
<tr class="even">
<td><strong>post-coordination</strong></td>
<td>The representation of a complex concept as a combination of two or more concepts. See also: pre-coordination.</td>
</tr>
<tr class="odd">
<td><strong>pre-coordination</strong></td>
<td>The representation of a complex concept as a single concept. See also: post- coordination.</td>
</tr>
<tr class="even">
<td><strong>preferred term</strong></td>
<td>The preferred human readable representation of a concept or the preferred name of a concept. Often used as the default display form of a concept. Synonyms: preferred designation, preferred expression.</td>
</tr>
<tr class="odd">
<td><strong>production environment</strong></td>
<td>The software and hardware that is used by end users, as opposed to developers and testers, to access terminology services in the VA enterprise.</td>
</tr>
<tr class="even">
<td><strong>property</strong></td>
<td>A named characteristic of a concept that can be assigned a value.</td>
</tr>
<tr class="odd">
<td><strong>qualifier</strong></td>
<td>A word or phrase associated with a concept that does not change its meaning.</td>
</tr>
<tr class="even">
<td><strong>reference file</strong></td>
<td>Non-patient VistA data file that contains reference or Terminology information not Patient Data.</td>
</tr>
<tr class="odd">
<td><strong>reference terminology</strong></td>
<td><p>Reference terminology is:</p>
<ol type="1">
<li><p>A comprehensive, consistent, and logically organized set of concepts that is designed to embody the expressive detail of a given domain, supported by a set of relationships that defines the elements within the domain and shows how their meanings relate to each other.</p></li>
<li><p>A controlled medical vocabulary intended for use as a reference to enable storage, retrieval, and analysis of clinical data.</p></li>
</ol></td>
</tr>
<tr class="even">
<td><strong>relationship</strong></td>
<td>An association between concepts. See also: semantics, semantic relationship.</td>
</tr>
<tr class="odd">
<td><strong>Standards Development Organization (SDO)</strong></td>
<td>Any entity whose primary activities are developing and maintaining standards that address the interests of a wide base of users outside the SDO.</td>
</tr>
<tr class="even">
<td><strong>semantics</strong></td>
<td>The meanings assigned to terminology content. See also: semantic relationship.</td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 79%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Term</strong></th>
<th><strong>Definition</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>semantic relationship</strong></td>
<td>An association between two concepts that has a specific meaning.</td>
</tr>
<tr class="even">
<td><strong>service oriented architecture (SOA)</strong></td>
<td>The VistA architecture is an SOA whereby applications that provide functionality for use by other applications are created as a service that conforms to a set of VHA standardized design patterns.</td>
</tr>
<tr class="odd">
<td><p><strong>Systemized Nomenclature of Medicine (SNOMED)</strong></p>
<p><strong>Clinical Terms (CT)</strong></p></td>
<td>SNOMED CT is a dynamic, scientifically validated clinical reference terminology that makes health care knowledge more usable and accessible.</td>
</tr>
<tr class="even">
<td><strong>standard code system (SCS)</strong></td>
<td>An organized collection of terms or concepts established by an authoritative source such as an SDO.</td>
</tr>
<tr class="odd">
<td><strong>standardization</strong></td>
<td>The process of defining, creating, deploying, and maintaining a common terminology resource.</td>
</tr>
<tr class="even">
<td><strong>Standards and Terminology Services (STS)</strong></td>
<td>STS includes project teams that were previously known as Data Standardization (DS) and ETS as well as the VETS and Enterprise Reference Terminology (ERT) subproject teams.</td>
</tr>
<tr class="odd">
<td><strong>subset</strong></td>
<td>A collection of concepts or designations that share a specified purpose or set of characteristics.</td>
</tr>
<tr class="even">
<td><strong>subtype</strong></td>
<td>The child in a parent-child relationship. The subtype (child) is narrower and more specific while the supertype (parent) is broader and more general. The subtype contains all the characteristics of the supertype.</td>
</tr>
<tr class="odd">
<td><strong>supertype</strong></td>
<td>The parent in a parent-child relationship. The supertype (parent) is broader and more general while the subtype (child) is narrower and more specific. All the characteristics of the supertype are included in the subtype.</td>
</tr>
<tr class="even">
<td><strong>surface form</strong></td>
<td>The term that 3M uses for a human readable representation of a concept, or the name of a concept. See also: designation (preferred).</td>
</tr>
<tr class="odd">
<td><strong>synonym</strong></td>
<td>A term or an expression that is an acceptable alternative to the preferred designation.</td>
</tr>
<tr class="even">
<td><strong>taxonomy</strong></td>
<td>A hierarchical classification of concepts.</td>
</tr>
<tr class="odd">
<td><strong>template</strong></td>
<td><p>A template is:</p>
<ol type="1">
<li><p>A structured aggregation of one or more archetypes, with optional order, to represent clinical data. An HL7 template is a data structure, based on the HL7 RIM that expresses the data content that is needed in a specific clinical or administrative context. Templates are drawn from the Reference Information Model (RIM) and make use of HL7 vocabulary domains. Templates are also described as constraints on HL7 artifacts.</p></li>
<li><p>A locally produced constraint specification that specifies which archetypes go together in an application dialog or message specification.</p></li>
</ol></td>
</tr>
<tr class="even">
<td><strong>term</strong></td>
<td>A human readable representation of a concept or name of a concept. See also: designation (preferred).</td>
</tr>
<tr class="odd">
<td><strong>terminology</strong></td>
<td>Set of concepts, designations, and relationships for a specialized subject area. The terms that are characterized by special reference within a discipline are called the terms of the discipline and, collectively, they form the terminology. Terms that function in general reference over a variety of languages are simply words and their totality is a vocabulary.</td>
</tr>
</tbody>
</table>
<table>
<colgroup>
<col style="width: 20%" />
<col style="width: 79%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Term</strong></th>
<th><strong>Definition</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Terminology Browser</strong></td>
<td>The Terminology Browser searches SCS, Map Sets, and VHAT. The Browser is a part of the VETS suite of terminology maintenance tools.</td>
</tr>
<tr class="even">
<td><strong>Terminology Deployment Services (TDS)</strong></td>
<td>TDS is the central distribution point for all terminology services. Updates are uploaded to the terminology deployment server, which in turn distributes them to targeted VistA sites.</td>
</tr>
<tr class="odd">
<td><strong>Terminology Editor (TED)</strong></td>
<td>TED is a web-based authoring tool that allows users to create new and edit existing Map Sets and Map Entries that exist in the VA terminology repository. TED is a part of the VETS suite of terminology maintenance tools.</td>
</tr>
<tr class="even">
<td><strong>terminology model</strong></td>
<td>A terminology model provides a consistent structure and specifies the formal representation of a concept. The STS terminology model comprises of components such as concepts, designations, properties, and relationships. Other components of the STS terminology model include Subsets and Concept to Concept linking.</td>
</tr>
<tr class="odd">
<td><strong>terminology server</strong></td>
<td>The software application and hardware that provide access to terminology content through a published set of API.</td>
</tr>
<tr class="even">
<td><strong>test environment</strong></td>
<td>The software and hardware that is used by developers and testers as opposed to end users to test terminology services in the VA enterprise.</td>
</tr>
<tr class="odd">
<td><strong>translation</strong></td>
<td>After two terminologies have been mapped, a translation between the two is possible.</td>
</tr>
<tr class="even">
<td><p><strong>Unified Medical Language System (UMLS)</strong></p>
<p><strong>Metathesaurus</strong></p></td>
<td>The UMLS Metathesaurus is a very large, multi-purpose, and multi-lingual vocabulary database that contains information about biomedical and health related concepts, their various names, and the relationships among them. It reflects and preserves the meanings, concept names, and relationships from its source vocabularies. It also supplies information that computer programs can use to create standard data, interpret user inquiries, interact with users to refine their questions, and convert the users' terms into the vocabulary used in relevant information sources.</td>
</tr>
<tr class="odd">
<td><strong>value</strong></td>
<td>A quantitative or qualitative state that is assigned to a property.</td>
</tr>
<tr class="even">
<td><strong>value domain</strong></td>
<td>All allowable values for a terminology, datatype, or value set. May be an infinite set of values.</td>
</tr>
<tr class="odd">
<td><strong>value set</strong></td>
<td>A finite set of allowable values. Typically, a value set has a small number of values. If it has a large number of values, it may be a terminology.</td>
</tr>
<tr class="even">
<td><strong>version</strong></td>
<td><p>A version is:</p>
<ol type="1">
<li><p>Formal changes in a terminology. May be used to find and track inactivated codes, determine the current code set, or track the history of a concept.</p></li>
<li><p>Also applies to formal revisions in computer code or programs.</p></li>
<li><p>An STS deployment that has passed internal testing. Can refer to a Candidate Version or a Finalized Version.</p></li>
</ol></td>
</tr>
<tr class="odd">
<td><strong>Department of Veterans Affairs (VA) Enterprise Terminology Services (VETS)</strong></td>
<td>VETS focuses on requirements for the deployment of and runtime access to terminology content in the Enterprise Reference Terminology (ERT) for all VA clinical applications.</td>
</tr>
<tr class="even">
<td><p><strong>VHA</strong></p>
<p><strong>Terminology (VHAT)</strong></p></td>
<td>VHAT is the terminology that is created and maintained by STS, in which Department of Veterans Affairs (VA) Unique Identifiers (VUID) are used to enable consistent, enterprise-wide use throughout the VHA.</td>
</tr>
</tbody>
</table>
| Term                                                                    | Definition                                                                                                                                                                                                                                              |
|-----------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Veterans Health Information Systems and Technology Architecture (VistA) | VistA is a term used to describe the VA’s health care information system. It encompasses in-house developed applications developed by VA staff, office automation applications, locally developed applications, and commercial-off-the- shelf applications. |
| vocabulary                                                              | A list of words or phrases with their meanings. See also: terminology.                                                                                                                                                                                      |
| VA Terminology Server (VTS)                                             | The VTS is used to house terminology served by VETS.                                                                                                                                                                                                        |
| Web Services Description Language (WSDL)                                | WSDL is an XML-based language that provides a model for describing Web services. The meaning of the acronym has changed from Version 1.2 where the D meant Definition.                                                                                      |
