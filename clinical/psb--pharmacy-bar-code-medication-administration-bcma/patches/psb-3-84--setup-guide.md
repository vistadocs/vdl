---
title: PSB*3*84 BCBU Version 3 Securing the Cache Cube for BCMA Backup
doc_type: SG
doc_label: Security Guide
doc_layer: patch
doc_subject: BCBU Version 3 Securing the Cache Cube for BCMA Backup
app_code: PSB
app_name: "Pharmacy: Bar Code Medication Administration (BCMA)"
section: CLI
app_status: archive
pkg_ns: PSB
patch_ver: 3
patch_id: PSB*3*84
group_key: "PSB:PSB:3"
file_numbers: []
security_keys: []
menu_options: 0
description: Bar Code Medication Administration (BCMA) BCMA Backup System (BCBU) Securing the Cache Cube for BCMA Backup
audience: 
keywords: 
  - span
  - class
  - mark
  - password
  - portal
  - management
  - edit
  - bcma
  - backup
  - authentication
page_count: 0
word_count: 724
section_count: 1
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: April 2015
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Bar_Code_Med_Admin_(BCMA)_Archive/psb_3_p84_bcbu_sg.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Pharm-Bar_Code_Med_Admin_(BCMA)_Archive/psb_3_p84_bcbu_sg.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=387"
---

![](psb-3-84-bcbu-version-3-securing-the-cache-cube-for-bcma-backup/001.png)

Bar Code Medication Administration (BCMA)  
BCMA Backup System (BCBU)  
Securing the Cache Cube for BCMA Backup

April 2015

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Product Development (PD)

Revision History

| Date   | Revision   | Description   | Author                             |
|--------|------------|---------------|------------------------------------|
| 4/2015 | PSB\*3\*84 | New document. | <span class="mark">REDACTED</span> |

Documentation Revision HistoryDocumentation Revision History

Contents

[1 Create a New User [1](#create-a-new-user)](#create-a-new-user)

[2 Configure the Management Portal to Accept Password Authentication [3](#configure-the-management-portal-to-accept-password-authentication)](#configure-the-management-portal-to-accept-password-authentication)

# Create a New User


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Create a New User](#create-a-new-user)
- [Configure the Management Portal to Accept Password Authentication](#configure-the-management-portal-to-accept-password-authentication)
1.  From the Management Portal home page, go to the <span class="mark">System Administration, Security, Users</span> menu (\[System Administration\] \> \[Security\] \> \[Users\]).
![](psb-3-84-bcbu-version-3-securing-the-cache-cube-for-bcma-backup/002.png)
2.  On the ‘Users’ page, select <span class="mark">Create New User</span>.
> This displays the \[General\] tab of the Edit User page for creating and configuring users.
3.  On the Edit User page, set values for only the following user properties. <span class="mark">(Fill out the required fields below.)</span> The other fields are optional.
- <span class="mark">Name (required) — Unique user identifier (suggest using your VHAxxxnnnnnn ID).</span>
- <span class="mark">Password (required) — New password value. <u>(Remember this password!)</u></span>
- <span class="mark">Confirm Password (required) — Confirmation of new password value.</span>
- <span class="mark">User Enabled (required) — Whether or not the account is available for use.</span>
4.  Click the <span class="mark">Save</span> button to create the new user.
Once you have created a user account, you then need to edit its characteristics.
1.  On the Users page (\[System Administration\] \> \[Security\] \> \[Users\]), click *<span class="mark">Edit</span>* in the newly created user’s row. This displays the Edit User page for the user being edited.
2.  Go to the \[Roles\] tab at the top of the Edit Page.
> 3\. Move the ‘*%All’* from the ‘Available’ column to the ‘Selected’ column by clicking the right arrow \> and then click ‘<span class="mark">Assign</span>’ to assign the user to the role(s).
> After doing this, the user’s roles should contain the *‘%All’* role. (See example figure below.)
![](psb-3-84-bcbu-version-3-securing-the-cache-cube-for-bcma-backup/003.png)
Return to the \[General\] tab and click <span class="mark">Close</span>.
5.  Secure the other user accounts. Do this by editing the characteristics of the \_System, Admin, CSPSystem, and SuperUser accounts.
1.  On the Users page (\[System Administration\] \> \[Security\] \> \[Users\]), click *<span class="mark">Edit</span>* in the above mentioned user’s row. This displays the Edit User page for the user being edited.
2.  On the Edit User page, set values for only the Password\* and Confirm Password\* fields for these users. (Remember these passwords.)
3.  Click the <span class="mark">Save</span> button and <span class="mark">Close</span> button after you are finished editing each individual user above.

# Configure the Management Portal to Accept Password Authentication

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. To set credentials for Studio from the Management Portal home page, go back to the Security level, choose Services page (\[System Administration\] \> \[Security\] \> \[Services\]).

2\. Select the <span class="mark">%Service_Bindings</span>, under the ‘Allowed Authentication Methods’ definition, uncheck *Unauthenticate*d and ensure that Password <u>IS</u> checked. Click <span class="mark">SAVE</span>.

When finished the Services table should look like this.

![](psb-3-84-bcbu-version-3-securing-the-cache-cube-for-bcma-backup/004.png)

3\. To set credentials for the Management portal from the Management Portal home page, go back to the Security level, then to the Applications level, then to the Web Applications page.

(\[System Administration\] \> \[Security\] \> \[Applications\] \> \[Web Applications\]).

![](psb-3-84-bcbu-version-3-securing-the-cache-cube-for-bcma-backup/005.png)

4\. On the Web Applications page, the <span class="mark">/csp/sys</span> application represents the Management Portal home page. Select <span class="mark">Edit</span> in this row to edit the application. This displays the Edit Web Application page for the /csp/sys application.

5\. Under Allowed Authentication Methods, disable Unauthenticated access by ensuring it is <u>NOT</u> checked and enable Password access by ensuring it <u>IS</u> checked. Click <span class="mark">Save</span>, then <span class="mark">Close</span>.

![](psb-3-84-bcbu-version-3-securing-the-cache-cube-for-bcma-backup/006.png)

When finished the Web Application table should look like this.

> **NOTE:** If the Authentication Methods are different than this use the Edit for that name and correct to match this table.

![](psb-3-84-bcbu-version-3-securing-the-cache-cube-for-bcma-backup/007.png)

This configures the Portal to require password authentication (also known as “Caché login”) and not to allow unauthenticated access, and so that all its parts behave consistently.