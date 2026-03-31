---
title: "Kernel 8.0 Developerâ€™s Guide: User User Guide"
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: "Developerâ€™s Guide: User"
app_code: XU
app_name: Kernel
section: INF
app_status: active
pkg_ns: XU
patch_ver: 8.0
patch_id: XU*8.0
group_key: "XU:XU:8.0"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - span
  - class
  - person
  - example
  - xuser
  - table
  - contents
  - returns
  - mark
  - date
page_count: 0
word_count: 5862
section_count: 19
table_count: 1
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: August 2025
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_user_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_user_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=10"
---

---
title: |
  Kernel 8.0 Developer’s Guide:

  User Developer Tools  
  User Guide
---

![](kernel-8-0-developer-s-guide-user-user-guide/001.png)

August 2025

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Product Delivery Service (PDS)

<span id="_Toc234301875" class="anchor"></span>Revision History

![](kernel-8-0-developer-s-guide-user-user-guide/002.png) REF: For the archived document revision history, see “<u>Appendix A—Revision History Archive</u>.”

<table>
<colgroup>
<col style="width: 14%" />
<col style="width: 12%" />
<col style="width: 43%" />
<col style="width: 29%" />
</colgroup>
<thead>
<tr class="header">
<th>Date</th>
<th>Revision</th>
<th>Description</th>
<th>Author</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>08/28/2025</td>
<td>1.0</td>
<td><p>Initial document creation: <em>Kernel Developer’s Guide: User Developer Tools User Guide</em>.</p>
<p>This is part of the VASS Documentation Redesign Project. The content in this document came from the original <em>Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide</em> document, which was too large and cumbersome to maintain; so, it was broken down into smaller user guides for ease of use and maintenance going forward.</p>
<p><strong>Software Versions:</strong></p>
<p><strong>Kernel 8.0</strong></p>
<p><strong>Toolkit 7.3</strong></p></td>
<td>VistA Application Shared Services (VASS) Development Team</td>
</tr>
</tbody>
</table>

Patch Revisions

For the current patch history related to this software, see the Patch Module on FORUM.

Table of Contents

<span id="_Toc207256074" class="anchor"></span>List of Figures

<span id="_Ref38421374" class="anchor"></span>Orientation

![](kernel-8-0-developer-s-guide-user-user-guide/003.png) REF: For an orientation to this manual, please refer to the “Orientation” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg.pdf#Main_Orientation).

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [Application Programming Interfaces (APIs)](#application-programming-interfaces-apis)
  - [\$\$CODE2TXT^XUA4A72(): Get HCFA Text](#code2txtxua4a72-get-hcfa-text)
  - [\$\$GET^XUA4A72(): Get Specialty and Subspecialty for a User](#getxua4a72-get-specialty-and-subspecialty-for-a-user)
  - [\$\$IEN2CODE^XUA4A72(): Get VA Code](#ien2codexua4a72-get-va-code)
  - [\$\$DTIME^XUP(): Reset DTIME for USER](#dtimexup-reset-dtime-for-user)
    - [Examples](#examples)
  - [DUZ^XUP(): Set the DUZ Variable](#duzxup-set-the-duz-variable)
  - [\$\$ACTIVE^XUSER(): Status Indicator](#activexuser-status-indicator)
    - [Examples](#examples-1)
  - [\$\$DEA^XUSER()—Get User’s DEA Number](#deaxuserget-users-dea-number)
    - [Examples](#examples-2)
  - [\$\$DETOX^XUSER()—Get Detox/Maintenance ID Number](#detoxxuserget-detoxmaintenance-id-number)
  - [DIV4^XUSER(): Get User Divisions](#div4xuser-get-user-divisions)
    - [Example](#example)
  - [\$\$LOOKUP^XUSER(): New Person File Lookup](#lookupxuser-new-person-file-lookup)
    - [Examples](#examples-3)
  - [\$\$NAME^XUSER(): Get Name of User](#namexuser-get-name-of-user)
    - [Examples](#examples-4)
  - [\$\$PROVIDER^XUSER(): Providers in New Person File](#providerxuser-providers-in-new-person-file)
    - [Examples](#examples-5)
  - [\$\$SDEA^XUSER()—Check for Prescribing Privileges](#sdeaxusercheck-for-prescribing-privileges)
  - [\$\$VDEA^XUSER()—Check if User Can Sign Controlled Substance Orders](#vdeaxusercheck-if-user-can-sign-controlled-substance-orders)
  - [\$\$KCHK^XUSRB(): Check If User Holds Security Key](#kchkxusrb-check-if-user-holds-security-key)
    - [Examples](#examples-6)
  - [DIVGET^XUSRB2(): Get Divisions for Current User](#divgetxusrb2-get-divisions-for-current-user)
  - [DIVSET^XUSRB2(): Set Division for Current User](#divsetxusrb2-set-division-for-current-user)
  - [USERINFO^XUSRB2(): Get Demographics for Current User](#userinfoxusrb2-get-demographics-for-current-user)
- [Appendix A—Revision History Archive](#appendix-arevision-history-archive)
The *Kernel 8.0 Developer’s Guide: User Developer Tools User Guide* is part of the *Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide*.

# Application Programming Interfaces (APIs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Several User APIs and Extrinsic Functions are available for developers. These APIs and Extrinsic Functions are described below.

## \$\$CODE2TXT^XUA4A72(): Get HCFA Text

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: User

ICR \#: 1625

Description: The \$\$CODE2TXT^XUA4A72 extrinsic function returns the three parts of the Health Care Financing Administration (HCFA) text from the PERSON CLASS (#8932.1) file based on passing in the Internal Entry Number (IEN) or the VA’s Vcode.

Format: \$\$CODE2RXT^XUA4A72(ien_or_vcode)

Input Parameters: ien_or_vcode: (required) Pass in either the Internal Entry Number (IEN) or the VA Vcode for the text that should be returned.

Output: returns: Returns HCFA text.

## \$\$GET^XUA4A72(): Get Specialty and Subspecialty for a User

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: User

ICR \#: 1625

Description: The \$\$GET^XUA4A72 extrinsic function returns the following:

IEN^Profession^Specialty^Sub-specialty^Effect date^Expired date^VA code

For the person identified by the DUZ in effect on the date passed in, in internal VA FileMan format (TODAY if no date passed in).

![](kernel-8-0-developer-s-guide-user-user-guide/004.png) NOTE: This API was released with Kernel Patch XU\*8.0\*27.

It returns:

- -1—If DUZ does *not* point to a valid user or user has never had a Person Class assigned.
- -2—If no active Person Class on that date.

Format: \$\$GET^XUA4A72(duz\[,date\])

Input Parameters: duz: (required) Internal Entry Number (IEN) for the person being checked in the NEW PERSON (#200) file.

date: (optional) Date in internal VA FileMan format, to indicate effective date for determination.

Output: returns: Returns:

- \-1—If DUZ does *not* point to a valid user or user has never had a Person Class assigned.
- -2—If no active Person Class on that date.

## \$\$IEN2CODE^XUA4A72(): Get VA Code

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: User

ICR \#: 1625

Description: The \$\$IEN2CODE^XUA4A72 extrinsic function returns the VA CODE from the PERSON CLASS (#8932.1) file that corresponds to the Internal Entry Number (IEN) passed in. If the IEN passed in does *not* match a valid entry in the PERSON CLASS (#8932.1) file, an empty string is returned.

![](kernel-8-0-developer-s-guide-user-user-guide/005.png) NOTE: This API was released with Kernel Patch XU\*8.0\*27.

Format: \$\$IEN2CODE^XUA4A72(ien)

Input Parameters: ien: (required) Internal Entry Number (IEN) in the PERSON CLASS (#8932.1) file.

Output: returns: Returns the VA CODE.

## \$\$DTIME^XUP(): Reset DTIME for USER

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: User

ICR \#: 4409

Description: The \$\$DTIME^XUP extrinsic function resets the DTIME variable for the user identified by the duz input parameter. This extrinsic function accepts two parameters:

- IEN or DUZ of the user in the NEW PERSON (#200) file.
- IEN of the device in the DEVICE (#3.5) file.

The return value should be assigned to the DTIME variable as shown in the examples. This DTIME variable is used on all timed READs where interactive responses are required for a given user.

Format: \$\$DTIME^XUP(\[duz\]\[,ios\])

Input Parameters: duz: (optional) The Internal Entry Number (IEN) or DUZ of the user in the NEW PERSON (#200) file.

ios: (optional) The IEN of the device in the DEVICE (#3.5) file. This IEN should be the same value of ios if present and should reflect the current sign-on device of the user.

Output: returns: The return value is based on the first available data found in the following fields/files (listed in search order):

1.  TIMED READ (# OF SECONDS) (#200.1) field of the NEW PERSON (#200) file.
2.  TIMED READ (# OF SECONDS) (#51.1) field of the DEVICE (#3.5) file.
3.  DEFAULT TIMED READ (SECONDS) (#210) field of the KERNEL SYSTEM PARAMETERS (#8989.3) file.
4.  (default) If *no* data is available in any of the three fields above, then the return value defaults to 300 seconds.

### Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Example 1

Sending DUZ only, returns the value in the TIMED READ (# OF SECONDS) (#200.1) field in the NEW PERSON (#200) file:

<span id="_Toc199950794" class="anchor"></span>Figure 1: \$\$DTIME^XUP API—Example 1

\><span class="mark">S DTIME=\$\$DTIME^XUP(DUZ)</span>

\><span class="mark">W DTIME</span>

1800

#### Example 2

Sending DUZ and IOS, returns the value in the TIMED READ (# OF SECONDS) (#200.1) field in the NEW PERSON (#200) file:

<span id="_Toc199950795" class="anchor"></span>Figure 2: \$\$DTIME^XUP API—Example 2

\><span class="mark">S DTIME=\$\$DTIME^XUP(DUZ,IOS)</span>

\><span class="mark">W DTIME</span>

1800

#### Example 3

Sending IOS only, returns the value in the TIMED READ (# OF SECONDS) (#51.1) field in the DEVICE (#3.5) file:

<span id="_Toc199950796" class="anchor"></span>Figure 3: \$\$DTIME^XUP API—Example 3

\><span class="mark">S DTIME=\$\$DTIME^XUP(,IOS)</span>

\><span class="mark">W DTIME</span>

500

#### Example 4

*Not* Sending DUZ or IOS returns the value in the DEFAULT TIMED READ (SECONDS) (#210) field in the KERNEL SYSTEM PARAMETERS (#8989.3) file:

<span id="_Toc199950797" class="anchor"></span>Figure 4: \$\$DTIME^XUP API—Example 4a

\><span class="mark">S DTIME=\$\$DTIME^XUP(,)</span>

\><span class="mark">W DTIME</span>

400

Or:

<span id="_Toc199950798" class="anchor"></span>Figure 5: \$\$DTIME^XUP API—Example 4b

\><span class="mark">S DTIME=\$\$DTIME^XUP()</span>

\><span class="mark">W DTIME</span>

400

#### Example 5

*Not* Sending DUZ or IOS *and* no value is in DEFAULT TIMED READ (SECONDS) (#210) field in the KERNEL SYSTEM PARAMETERS (#8989.3) file:

<span id="_Toc199950799" class="anchor"></span>Figure 6: \$\$DTIME^XUP API—Example 5

\><span class="mark">S DTIME=\$\$DTIME^XUP()</span>

\><span class="mark">W DTIME</span>

300

## DUZ^XUP(): Set the DUZ Variable

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Controlled Subscription

Category: User

ICR \#: 4129

Description: The DUZ^XUP API sets the DUZ variable equal to the input parameter. Also, it sets up the components of the DUZ array. For example, some applications need the DUZ to be a *non*-human user in the NEW PERSON (#200) file, which is identified as an application-specific user name. This allows all filing and database activities appear to have been performed by a *non*-human user instead of by background processes (such as Postmaster). Also, when processing information initiated by HL7 messages, DUZ may *not* have been defined correctly, or *not* defined at all. This presents a challenge for any HL7-based application, because many VistA applications expect a correct DUZ array to be present. For example, when creating a Text Integration Utilities (TIU) note, DUZ is *not* part of the input parameter, but it is simply expected to be present. This API allows the application to set the DUZ so that it can file TIU notes correctly for providers as indicated by HL7 messages. Also, other applications expect the DUZ array to be present by default. It has been observed that failure to populate the correct provider’s information in a DUZ array may result in a crash or somebody else’s DUZ being used as a provider for something they did *not* request.

Format: DUZ^XUP(da)

Input Parameters: da: (required) This is the internal entry number (IEN) of the user in the NEW PERSON (#200) file to which you want to set the DUZ value and DUZ array.

Output Variable: DUZ: Returns the DUZ variable equal to the input parameter. Also, it sets up the components of the DUZ array.

## \$\$ACTIVE^XUSER(): Status Indicator

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: User

ICR \#: 2343

Description: The \$\$ACTIVE^XUSER extrinsic function returns the active status indicator and latest signon information of a user in the NEW PERSON (#200) file.

Format: \$\$ACTIVE^XUSER(ien)

Input Parameters: ien: (required) Internal Entry Number (IEN) of the user to be checked in the NEW PERSON (#200) file.

Output: returns: Returns any of the following codes:

- “”—NULL, no user record found.
- 0—User *cannot* sign on.
- 0^DISUSER—User *cannot* sign on because of DISUSER flag.
- 0^TERMINATED^FMDATE—User terminated on date indicated.
- 1^NEW—A new user, can sign on.
- 1^ACTIVE^FMDATE—An active user, last signon date.

### Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Example 1

<u>Figure 7</u> is an example of an Active User in the NEW PERSON (#200) file:

<span id="_Ref501638084" class="anchor"></span>Figure 7: \$\$ACTIVE^XUSER API—Example 1

\><span class="mark">S X=\$\$ACTIVE^XUSER(1529)</span>

\><span class="mark">WRITE X</span>

1^ACTIVE^3030321.093756

#### Example 2

<u>Figure 8</u> is an example of a Terminated User in the NEW PERSON (#200) file:

<span id="_Ref501638068" class="anchor"></span>Figure 8: \$\$ACTIVE^XUSER API—Example 2

\><span class="mark">S X=\$\$ACTIVE^XUSER(957)</span>

\><span class="mark">WRITE X</span>

0^TERMINATED^2980504

#### Example 3

<u>Figure 9</u> is an example of a User with no record in the NEW PERSON (#200) file, returns a NULL string:

<span id="_Ref501638042" class="anchor"></span>Figure 9: \$\$ACTIVE^XUSER API—Example 3

\><span class="mark">S X=\$\$ACTIVE^XUSER(999999999)</span>

\><span class="mark">W X</span>

\>

#### Example 4

<u>Figure 10</u> is an example of a User in the NEW PERSON (#200) file with the DISUSER flag set:

<span id="_Ref501638052" class="anchor"></span>Figure 10: \$\$ACTIVE^XUSER API—Example 4

\><span class="mark">S X=\$\$ACTIVE^XUSER(111)</span>

\><span class="mark">W X</span>

0^DISUSER

## \$\$DEA^XUSER()—Get User’s DEA Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: User: DEA ePCS Utility

ICR \#: 2343

Description: The \$\$DEA^XUSER extrinsic function returns a user’s DEA number, if it exists in the DEA# (#53.2) Multiple field in the NEW PERSON (#200) file. If the DEA# (#53.2) field value is NULL, the value returned depends on the optional flag input parameter.

![](kernel-8-0-developer-s-guide-user-user-guide/006.png) NOTE: Fee Basis and C&A providers only return DEA# or NULL.

![](kernel-8-0-developer-s-guide-user-user-guide/007.png) NOTE: This API was originally requested as part of the Public Key Infrastructure (PKI) Project. This API was updated with Kernel Patch XU\*8.0\*580, which was created in support of the Drug Enforcement Agency (DEA) e-Prescribing of Controlled Substances (ePCS) Utility. This utility uses Public Key Infrastructure (PKI) and meets the requirements proposed by the DEA Interim Final Rule (IFR) for Electronic Prescriptions for Controlled Substances effective as of June 1, 2010.

Format: \$\$DEA^XUSER(\[flag\],ien\[,date\])

Input Parameters: flag: (optional) This flag controls what is returned when the user does *not* have a value in the DEA# (#53.2) field of the NEW PERSON (#200) file. If the flag is:

- NULL or 0—This routine checks to see if the user has values in the VA# (#53.3) field of the NEW PERSON (#200) file and the (new) FACILITY DEA NUMBER (#52) field of the INSTITUTION (#4) file. If values are found in both of those fields, this routine returns the following:

FACILITY DEA NUMBER (#52) field\_“-”\_VA# (#53.3) field

- 1—This routine checks to see if the user has a value in the VA# (#53.3) field of the NEW PERSON (#200) file. If a value is found in that field, this routine returns that field value. Otherwise, this routine returns an empty string.

ien: (required) This is the NEW PERSON (#200) file IEN for the entry to be checked.

date: (optional) The date to be checked against the DEA# Expiration Date instead of default DT (today's date).

Output: returns: Returns the DEA#: DEA# (#53.2) field value or the value returned based on the (optional) flag input parameter.

### Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Example 1

The following are the data values for this example:

- DEA# (#53.2) field = AB1234567.
- FACILITY DEA NUMBER (#52) field = VA7654321.
- VA# (#53.3) field = 789.

If the flag input parameter is NULL or 0, this API would return AB1234567.

If the flag input parameter is 1, this API would return AB1234567.

#### Example 2

The following are the data values for this example:

- DEA# (#53.2) field = NULL.
- FACILITY DEA NUMBER (#52) field = VA7654321.
- VA# (#53.3) field = 789.

If the flag input parameter is NULL or 0, this API would return VA7654321-789.

If the flag input parameter is 1, this API would return 789.

#### Example 3

The following are the data values for this example:

- DEA# (#53.2) field = NULL.
- FACILITY DEA NUMBER (#52) field = VA7654321.
- VA# (#53.3) field = NULL.

If the flag input parameter is NULL or 0, this API would return “” (an empty string).

If the flag input parameter is 1, this API would return “” (an empty string).

In both cases, it returns an empty string.

#### Example 4

The following are the data values for this example:

- DEA# (#53.2) field = NULL.
- FACILITY DEA NUMBER (#52) field = VA7654321.
- VA# (#53.3) field = 789.
- PROVIDER TYPE (#53.6) field = FEE BASIS or C&A.

If the flag input parameter is NULL or 0, this API would return “” (an empty string).

If the flag input parameter is 1, this API would return “” (an empty string).

In both cases, it returns an empty string.

#### Example 5

The following are the data values for this example:

- DEA# (#53.2) field = AB1234567 but expired.
- FACILITY DEA NUMBER (#52) field = VA7654321.
- VA# (#53.3) field = 789.
- PROVIDER TYPE (#53.6) field is *not* = FEE BASIS nor C&A.

If the PSOEPCS EXPIRED DEA FAILOVER XPAR parameter is set to Yes, this API would return VA7654321-789.

If the PSOEPCS EXPIRED DEA FAILOVER XPAR parameter is set to No, this API would return NULL ("").

#### Example 6

The following are the data values for this example:

- DEA# (#53.2) field = AB1234567.
- DEA EXPIRATION DATE = 3201105.

If the date parameter “3201104" passed in is less than DEA EXPIRATION DATE, this API would return "AB1234567".

If the date parameter "3201106" passed in is greater than DEA EXPIRATION DATE, this API would return NULL ("").

## \$\$DETOX^XUSER()—Get Detox/Maintenance ID Number

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: User: DEA ePCS Utility

ICR \#: 2343

Description: The \$\$DETOX^XUSER extrinsic function obtains the value stored in the DETOX/MAINTENANCE ID NUMBER (#53.11) field in the NEW PERSON (#200) file. It returns one of the following:

- User’s DETOX/MAINTENANCE ID number—If it exists in the DETOX/MAINTENANCE ID NUMBER (#53.11) field of the NEW PERSON (#200) file.
- NULL—If DETOX/MAINTENANCE ID number is NULL or the DEA EXPERATION DATE (#747.44) field in the NEW PERSON (#200) file is unpopulated.
- DEA EXPIRATION DATE (#747.44)—This date is returned when the DETOX/MAINTENANCE ID number is valid, but the DEA EXPIRATION DATE has expired.

![](kernel-8-0-developer-s-guide-user-user-guide/008.png) NOTE: This API was released with Kernel Patch XU\*8.0\*580, which was created in support of the Drug Enforcement Agency (DEA) e-Prescribing of Controlled Substances (ePCS) Utility. This utility uses Public Key Infrastructure (PKI) and meets the requirements proposed by the DEA Interim Final Rule (IFR) for Electronic Prescriptions for Controlled Substances effective as of June 1, 2010.

Format: \$ \$DETOX^XUSER(ien\[,date\])

Input Parameters: ien: (required) The IEN of the user in the NEW PERSON (#200) file.

date: (optional) The date to be checked against the DEA# Expiration Date instead of default DT (today's date).

Output: returns: Returns: one of the following:

- User’s DETOX/MAINTENANCE ID number—If valid.
- NULL—DETOX/MAINTENANCE ID number is NULL or the DEA EXPERATION DATE (#747.44) field in the NEW PERSON (#200) file is unpopulated.
- DEA EXPIRATION DATE (#747.44)—When the DETOX/MAINTENANCE ID number is valid, but the DEA EXPIRATION DATE has expired.

## DIV4^XUSER(): Get User Divisions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Controlled Subscription

Category: User

ICR \#: 2533

Description: The DIV4^XUSER API returns all divisions for a user. It returns:

- 1—If the user has a Division entry in the NEW PERSON (#200) file. It indicates that the array of POINTERs to the Institution file has been defined.
- 0—The array of POINTERs to the INSTITUTION (#4) file has *not* been defined.

Format: DIV4^XUSER(.array\[,duz\])

Input Parameters: .array: (required) This parameter is a local variable (that is array name) passed by reference.

duz: (optional) The Internal Entry Number (IEN) of the user in the NEW PERSON (#200) file. If DUZ is *not* passed as a parameter, the function defaults to the value of DUZ in the application’s partition.

Output Parameters: .array: Returns:

- 1—If the user has a Division entry in the NEW PERSON (#200) file. It indicates that the array of POINTERs to the Institution file has been defined.  
  >   
  > The array includes all IENs for the INSTITUTION (#4) file that have been assigned to the user.  
  >   
  > The array is defined and left in the application’s partition, if the user indicated by the value of the duz input parameter has divisions defined in the respective NEW PERSON (#200) file entry. The format is:

ARRAY(\[^DIC(4 IEN\])

- 0—The array of POINTERs to the INSTITUTION (#4) file has *not* been defined.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc199950804" class="anchor"></span>Figure 11: DIV4^XUSER API—Example

\><span class="mark">S X=\$\$DIV4^XUSER(.ZZ,duz)</span>

## \$\$LOOKUP^XUSER(): New Person File Lookup

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: User

ICR \#: 2343

Description: The \$\$LOOKUP^XUSER extrinsic function does a user lookup on the NEW PERSON (#200) file screening out users that are terminated. You are first asked to enter a name of a user in the NEW PERSON (#200) file. By default, the function then asks if the correct user name was selected. For example:

> Select NEW PERSON NAME: <span class="mark">XUUSER,THREE \<Enter\></span>

> Is XUUSER,THREE the one you want? YES//

If the optional input parameter is set to Q then the second, confirmation prompt is suppressed. The return is in the same format as a call to DIC (that is IEN^NAME). Adding new entries is *not* allowed.

Format: \$\$LOOKUP^XUSER(\[""\])

Input Parameters: “”: (optional) This optional input parameter does the following:

- NULL (default)—Do *not* suppress the NEW PERSON (#200) file name confirmation prompt for each entry selected.
- A—Screen out terminated users.
- Q—Suppress the NEW PERSON (#200) file name confirmation prompt for each entry selected.
- AQ—Screen out terminated users and suppress the NEW PERSON (#200) file name confirmation prompt for each entry selected.

Output: returns: Returns the Internal Entry Number (IEN) and name of the user in the NEW PERSON (#200) file entered after the “Select NEW PERSON NAME:” prompt (IEN^NAME).

### Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Example 1

<u>Figure 12</u> is an example of a lookup of an active user when *not* passing in the optional Q parameter:

<span id="_Ref499806852" class="anchor"></span>Figure 12: \$\$LOOKUP^XUSER API—Example 1: Showing Confirmation Prompt

\><span class="mark">S LRDOC=\$\$LOOKUP^XUSER("") \<Enter\></span>

Select NEW PERSON NAME: <span class="mark">? \<Enter\></span>

Answer with NEW PERSON NAME, or INITIAL, or SSN, or VERIFY CODE, or

NICK NAME, or SERVICE/SECTION, or DEA#, or ALIAS

Do you want the entire 1601-Entry NEW PERSON List? <span class="mark">N \<Enter\></span> (No)

Select NEW PERSON NAME: <span class="mark">XUUSER,TWO E \<Enter\></span> TX COMPUTER SPECIALIST

Is XUUSER,TWO E the one you want? YES// <span class="mark">\<Enter\></span>

\><span class="mark">W LRDOC</span>

1529^XUUSER,TWO E

#### Example 2

<u>Figure 13</u> is an example of a lookup of an active user when passing in the optional Q parameter:

<span id="_Ref499806864" class="anchor"></span>Figure 13: \$\$LOOKUP^XUSER API—Example 2: Suppressing Confirmation Prompt

\><span class="mark">S LRDOC=\$\$LOOKUP^XUSER("Q") \<Enter\></span>

Select NEW PERSON NAME: <span class="mark">XUUSER,TWO E \<Enter\></span> TX COMPUTER SPECIALIST

\><span class="mark">W LRDOC</span>

1529^XUUSER,TWO E

#### Example 3

<u>Figure 14</u> is an example of a lookup of a terminated user when passing in the optional A parameter:

<span id="_Ref499806878" class="anchor"></span>Figure 14: \$\$LOOKUP^XUSER API—Example 3: Terminated User

\><span class="mark">S LRDOC=\$\$LOOKUP^XUSER("A")</span>

Select NEW PERSON NAME: <span class="mark">XUUSER,EIGHT \<Enter\></span> EX

This user was terminated on May 04, 1998

Select NEW PERSON NAME:

## \$\$NAME^XUSER(): Get Name of User

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: User

ICR \#: 2343

Description: The \$\$NAME^XUSER extrinsic function returns the full name of the specified user in a mixed case displayable format. The user’s given name (that is First Last) is returned unless a second parameter of F is passed in to get the Family name (that is Last,First).

Format: \$\$NAME^XUSER(ien\[,format\])

Input Parameters: ien: (required) Internal Entry Number (IEN) of the provider to be checked in the NEW PERSON (#200) file.

format: (optional) This parameter indicates if the user’s name should be returned formatted by Family or Given name, respectively. Possible values are:

- F—Family (such as “Xuuser,Two”).
- G (default)—Given (such as “Two Xuuser”).

Output: returns: Returns user’s family or given name.

### Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Example 1

Retrieving the user name in Given format:

<span id="_Toc199950808" class="anchor"></span>Figure 15: \$\$NAME^XUSER API—Example 1

\><span class="mark">S X=\$\$NAME^XUSER(1529)</span>

\><span class="mark">W X</span>

Two E Xuuser

#### Example 2

Retrieving the user name in Family format:

<span id="_Toc199950809" class="anchor"></span>Figure 16: \$\$NAME^XUSER API—Example 2

\><span class="mark">S X=\$\$NAME^XUSER(1529,"F")</span>

\><span class="mark">W X</span>

Xuuser,Two E.

## \$\$PROVIDER^XUSER(): Providers in New Person File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: User

ICR \#: 2343

Description: The \$\$PROVIDER^XUSER extrinsic function indicates any provider in the NEW PERSON (#200) file. The definition of a provider is any entry in the NEW PERSON (#200) file that does *not* have a termination date. A second parameter can also be added to invoke other checks, such as whether to include visitors.

![](kernel-8-0-developer-s-guide-user-user-guide/009.png) NOTE: This API was requested to be added by the Computerized Patient Record System (CPRS) Development Team.  
  
Additional parameters may be added in the future in order to perform other tests/checks.

Format: \$\$PROVIDER^XUSER(xuda,xuf)

Input Parameters: xuda: (required) Internal Entry Number (IEN) of the provider to be checked in the NEW PERSON (#200) file.

xuf: (optional) Flag to control processing:

- 0 or Not Passed—Do *not* include visitors.
- 1—Include visitors.

Output: returns: Returns any of the following codes:

- 1—Provider has a record and no termination date.
- 0^TERMINATED^*FMDATE*—Provider terminated on date indicated.
- “”—NULL, no provider record found.

### Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Example 1

<u>Figure 17</u> is an example of an Active Provider in the NEW PERSON (#200) file:

<span id="_Ref502645279" class="anchor"></span>Figure 17: \$\$PROVIDER^XUSER API—Example 1

\><span class="mark">S X=\$\$PROVIDER^XUSER(1529)</span>

\><span class="mark">WRITE X</span>

1

#### Example 2

<u>Figure 18</u> is an example of a Terminated Provider in the NEW PERSON (#200) file:

<span id="_Ref502645298" class="anchor"></span>Figure 18: \$\$PROVIDER^XUSER API—Example 2

\><span class="mark">S X=\$\$PROVIDER^XUSER(957)</span>

\><span class="mark">W X</span>

0^TERMINATED^2980504

#### Example 3

<u>Figure 19</u> is an example of a Provider with no record in the NEW PERSON (#200) file, returns a NULL string:

<span id="_Ref502645309" class="anchor"></span>Figure 19: \$\$PROVIDER^XUSER API—Example 3

\><span class="mark">S X=\$\$PROVIDER^XUSER(000999999)</span>

\><span class="mark">W X</span>

\>

## \$\$SDEA^XUSER()—Check for Prescribing Privileges

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: User: DEA ePCS Utility

ICR \#: 2343

Description: The \$\$SDEA^XUSER extrinsic function uses the following “Privileges Algorithm” to check for prescribing privileges:

- Blank = never answered (Allow all schedules but system to send the following electronic message: “DEA credentials have *not* been populated, call TBD responsible person.”)
- Any or all fields are answered = provide explicit set of permissions (that have been identified).
- If it is answered that Prescriber has No privileges for all schedules = remove DEA number or VA number from the NEW PERSON (#200) file.
- If Prescriber has been issued a DEA number, you have privileges.
- If the Prescriber has been issued a VA number, this is a presumption of privileges.

![](kernel-8-0-developer-s-guide-user-user-guide/010.png) NOTE: Not all of these checks apply to documentation of *non*-VA medication.

![](kernel-8-0-developer-s-guide-user-user-guide/011.png) REF: This API calls the <u>\$\$DEA^XUSER()—Get User’s DEA Number</u> API.

![](kernel-8-0-developer-s-guide-user-user-guide/012.png) NOTE: This API was released with Kernel Patch XU\*8.0\*580, which was created in support of the Drug Enforcement Agency (DEA) e-Prescribing of Controlled Substances (ePCS) Utility. This utility uses Public Key Infrastructure (PKI) and meets the requirements proposed by the DEA Interim Final Rule (IFR) for Electronic Prescriptions for Controlled Substances effective as of June 1, 2010.

Format: \$\$SDEA^XUSER(\[fg,\]ien,psdea\[,date\])

Input Parameters: fg: (optional) This flag is used for [\$\$DEA^XUSER](#deaxuserget-users-dea-number) call, see the flag input parameter in the <u>\$\$DEA^XUSER()—Get User’s DEA Number</u> API.

ien: (required) This is the NEW PERSON (#200) file IEN for the entry to be checked.

psdea: (required) This parameter is DEA schedule. DEA schedule is a 2-6 position field. It comes from the DRUG (#50) file in Pharmacy. This API uses this field to verify the provider is allowed to write orders for specific controlled substances. For example, if the schedule is 2A, this indicates a controlled substance, schedule 2.

Chart for all values:

- MANUFACTURED IN PHARMACY
- SCHEDULE 1 ITEM
- SCHEDULE 2 ITEM
- SCHEDULE 3 ITEM
- SCHEDULE 4 ITEM
- SCHEDULE 5 ITEM
- LEGEND ITEM:
- 9—OVER-THE-COUNTER
- L—DEPRESSANTS AND STIMULANTS
- A—NARCOTICS AND ALCOHOLS
- P—DATED DRUGS
- I—INVESTIGATIONAL DRUGS
- M—BULK COMPOUND ITEMS
- C—CONTROLLED SUBSTANCES - NON NARCOTIC
- R—RESTRICTED ITEMS
- S—SUPPLY ITEMS
- B—ALLOW REFILL (SCH. 3, 4, 5 ONLY)
- W—NOT RENEWABLE
- F—NON REFILLABLE
- E—ELECTRONICALLY BILLABLE
- N—NUTRITIONAL SUPPLEMENT
- U—SENSITIVE DRUG

date: (optional) The date to be checked against the DEA# Expiration Date instead of default DT (today's date).

Output: returns: Returns: DEA# or Facility DEA\_“-”\_user VA# like the [\$\$DEA^XUSER](#deaxuserget-users-dea-number) call.

- 1—DEA# is NULL from the [\$\$DEA^XUSER](#deaxuserget-users-dea-number) call.
- 2—When all schedules equals 0.
- 4^expiration date—DEA# expiration date has expired. It checks if the DEA# and expiration date are *not*NULL. The expiration date is returned in external format.

## \$\$VDEA^XUSER()—Check if User Can Sign Controlled Substance Orders

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: User: DEA ePCS Utility

ICR \#: 2343

Description: The \$\$VDEA^XUSER extrinsic function determines if a user in the NEW PERSON (#200) file can sign orders for controlled substances.

![](kernel-8-0-developer-s-guide-user-user-guide/013.png) NOTE: This API was released with Kernel Patch XU\*8.0\*580, which was created in support of the Drug Enforcement Agency (DEA) e-Prescribing of Controlled Substances (ePCS) Utility. This utility uses Public Key Infrastructure (PKI) and meets the requirements proposed by the DEA Interim Final Rule (IFR) for Electronic Prescriptions for Controlled Substances effective as of June 1, 2010.

Format: \$VDEA^XUSER(.return,ien)

Input Parameters: .return: (required) This is a reference to an array where the reasons why the user *cannot* sign orders for controlled substances, and which DEA schedules the user can prescribe is returned. For example:

RETURN(“Is permitted to prescribe all schedules.”)=“”ien: (required) This is the IEN of the user in the NEW PERSON (#200) file.

Output Parameters: .return: This array contains the reasons why the user *cannot* sign orders for controlled substances, and which DEA schedules the user can prescribe. For example:

RETURN(“Is *not* permitted to prescribe any schedules.”)=“”Output: returns: Returns:

- 1—If the user can sign orders for controlled substances.
- 0—If the user is *not* able to sign orders for controlled substances.

## \$\$KCHK^XUSRB(): Check If User Holds Security Key

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Controlled Subscription

Category: User

ICR \#: 2120

Description: The \$\$KCHK^XUSRB extrinsic function checks to see if a user holds a given security key.

Format: \$\$KCHK^XUSRB(key\[,ien\])

Input Parameters: key: (required) The name of the security key to be checked.

ien: (optional) Internal Entry Number (IEN). It defaults to DUZ.

Output: returns: Returns:

- 1—User holds security key.
- 0—User does *not* hold security key.

### Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Example 1

<u>Figure 20</u> illustrates the results when a user holds a security key input:

<span id="_Ref500922903" class="anchor"></span>Figure 20: \$\$KCHK^XUSRB API—Example 1

\><span class="mark">S X=\$\$KCHK^XUSRB("XUPROGMODE")</span>

\><span class="mark">W X</span>

1

#### Example 2

<u>Figure 21</u> illustrates the results when a user does *not* hold the security key input:

<span id="_Ref500922919" class="anchor"></span>Figure 21: \$\$KCHK^XUSRB API—Example 2

\><span class="mark">S X=\$\$KCHK^XUSRB("XUMGR")</span>

\><span class="mark">W X</span>

0

#### Example 3

<u>Figure 22</u> illustrates the results when checking if another user holds a security key input by including their IEN:

<span id="_Ref500922928" class="anchor"></span>Figure 22: \$\$KCHK^XUSRB API—Example 3

\><span class="mark">S X=\$\$KCHK^XUSRB("XUPROGMODE",30)</span>

\><span class="mark">W X</span>

1

## DIVGET^XUSRB2(): Get Divisions for Current User

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Controlled Subscription

Category: User

ICR \#: 4055

Description: The DIVGET^XUSRB2 API retrieves the list of divisions for the current user.  
  
(This was developed as a Broker Remote Procedure Call \[RPC\] and all RPCs have as the first parameter the return/output parameter.)

Format: DIVGET^XUSRB2(ret,ien)

Input Parameters: ret: (required) Name of the subscripted return array. In every API that is used as an RPC, the first parameter is the return array.

ien: (required) The DUZ or user name of the user for whom you are getting the division list.

Output Parameters: ret(): Returns a subscripted output array. If + of the value at the first level 0 subscript of the return value is false, then the user does *not* have any divisions from which to select.

Otherwise, for each division that a user has, a node is present in the return value, at the first subscript level, starting at Zero (0) and incrementing from there. The value of the node is three pieces:

ien^division name^station \#

## DIVSET^XUSRB2(): Set Division for Current User

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Controlled Subscription

Category: User

ICR \#: 4055

Description: The DIVSET^XUSRB2 API sets the division for the current user.  
  
(This was developed as a Broker RPC and all RPCs have as the first parameter the return/output parameter.)

Format: DIVSET^XUSRB2(ret,div)

Input Parameters: ret: (required) Name of the subscripted return array. In every API that is used as an RPC, the first parameter is the return array.

div: (required) This is the division to select. If passed with a leading grave accent (\`) an Internal Entry Number (IEN) is being passed and is processed as such.

Output: ret(): Returns a Boolean value in the subscripted output array:

- True (*non*-Zero)—Division selection is considered successful.
- False (Zero)—Division selection failed.

## USERINFO^XUSRB2(): Get Demographics for Current User

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Controlled Subscription

Category: User

ICR \#: 4055

Description: The USERINFO^XUSRB2 API retrieves various user demographic information for the current user.

![](kernel-8-0-developer-s-guide-user-user-guide/014.png) NOTE: This was developed as a Broker/VistALink RPC and all RPCs have as the first parameter the return/output parameter.

Format: USERINFO^XUSRB2(ret)

Input Parameters: ret: (required) Name of the subscripted return array. In every API that is used as an RPC, the first parameter is the return array.

Output: ret(): Returns a subscripted output array:

- RET(1)—User’s name from the .01 field of the NEW PERSON (#200) file.
- RET(2)—Concatenated user name from the NAME COMPONENTS(#20) file.
- RE(3)—Logged on division:

ien^name^number

- RET(4)—User’s title from the NEW PERSON (#200) file.
- RET(5)—User’s service section from NEW PERSON (#200) file (external format).
- RET(6)—User’s language from the NEW PERSON (#200) file.
- RET(7)—User’s timeout.

# Appendix A—Revision History Archive

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section should be used to show all document revision history prior to the current year.

![](kernel-8-0-developer-s-guide-user-user-guide/015.png) REF: For the most recent, current year document revision history, see the “[Revision History](#_Toc234301875)” section.

| Date | Revision | Description | Author |
|------|----------|-------------|--------|
| TBD  | TBD      | TBD         | TBD    |

<span id="Glossary" class="anchor"></span>Glossary

![](kernel-8-0-developer-s-guide-user-user-guide/016.png) REF: For a glossary of terms specific to Kernel, see the “Glossary” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm.pdf#Main_Glossary).

![](kernel-8-0-developer-s-guide-user-user-guide/017.png) REF: For a list of commonly used terms and acronyms, see the VA Glossary Power App.