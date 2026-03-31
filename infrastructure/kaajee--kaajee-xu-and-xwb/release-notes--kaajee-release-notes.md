---
consolidated_title: "kaajee release notes"
app_code: KAAJEE
doc_type: RN
master_source: "KAAJEE 1.2.0 Release Notes"
master_pub_date: July 2020
consolidated_from: 2 versions
prior_versions:
  - "KAAJEE 1.1.0 Release Notes (WebLogic 9.2 and higher)"
---

<!-- image -->

**KERNEL AUTHENTICATION &amp; AUTHORIZATION FOR J2EE (KAAJEE) VERSION 1.2.0**

**and**

**SECURITY SERVICE PROVIDER INTERFACES (SSPI)**

**VERSION 1.2.0**

**FOR WEBLOGIC (WL) VERSIONS 10.3.6 AND HIGHER**

**RELEASE NOTES**

July 2020

Department of Veterans Affairs (VA)

Office of Information and Technology (OI&amp;T)

Product Development

*This page is left blank intentionally.*

Contents

1.	Introduction	1-1

1.1.	Orientation	1-1

1.2.	About KAAJEE	1-1

1.3.	Distribution	1-1

1.4.	For More Information	1-3

2.	New Features / Changes for KAAJEE Version 1.2	2-1

2.1.	Upgraded Deployment Descriptors:	2-1

2.2.	Design Changes to Better Support Additional SSL Use Cases	2-1

2.3.	Configure Web.xml to Enable SSL	2-2

2.4.	Integration of Kernel Patch XU*8*451: KAAJEE Login Page—Removal of Refresh Button.	2-2

2.5.	Administrator Security Role for LoginController	2-3

2.6.	Sign-On/User Context (SSO/UC)-Enabled	2-4

2.7.	Section 508 Issue Regarding Session Timeouts	2-4

2.8.	Dependency Upgrades	2-4

3.	New Features / Changes for KAAJEE Security Provider Version 1.2.0	3-1

3.1.	KAAJEE SSPI Upgraded to WebLogic's AuthenticationProviderV2 SSPI	3-1

*This page is left blank intentionally.*

## Introduction

### Orientation

Significant KAAJEE and Kaajee Security Provider release objects (JARs, EARs, WARs, etc.) contain a build number in the filenames (e.g., in "kaajee-1.2.0.xxx.jar" where "xxx" is the build number). Build numbers are increments with each new Developer Preview. Consult the following table for KAAJEE build increment details.

### About KAAJEE

Kernel Authentication &amp; Authorization for Java 2 Enterprise Edition (KAAJEE) for Web-based Health ***e*** Vet applications on WebLogic 10.3.6 and higher, such as Pharmacy Re-Engineering (PRE), provides user authentication to grant access to applications, and retrieves VistA security keys for application authorization. KAAJEE takes advantage of the current user store in  to authenticate users in new Health ***e*** Vet applications. Considered an interim solution, KAAJEE will be enhanced to provide the connection to the Department of Veterans Affairs (VA) Enterprise user authentication (sign-on) system in the future. KAAJEE and Fat-client Kernel Authentication and Authorization (FatKAAT) use VistALink as a connectivity solution from Java 2 Platforms, Enterprise Edition (J2EE) applications to Mumps (M)/VistA.WebLogic Updates Project.

KAAJEE 1.2 is the successor to KAAJEE 1.1, which was originally released to support the BEA WebLogic Server 9.2 platform.  Version 1.2 of KAAJEE now supports Oracle WebLogic Server 10.3.6 and higher, fully Fortify and TRM compliant.

Like KAAJEE 1.1, KAAJEE 1.2 provides a custom Authentication Provider "plug-in" for BEA WebLogic J2EE servers, including a set of web forms for web applications that allow web applications to authenticate and authorize an end-user using a Kernel system as the source of authentication and authorization.

### Distribution

Version 1.2 of KAAJEE implements all current features of KAAJEE 1.1. Included in the distribution are the following:

- KAAJEE 1.2 jar files
- Folder of Login web forms for Forms Authentication to drop into a J2EE Web application
- JavaDoc Application Programming Interface (API) documentation for the user manager classes
- Deployment Descriptor examples
- Complete source code for the KAAJEE implementation
- Sample Web Application

Kaajee Security Provider is a necessary component for KAAJEE implementing BEA WebLogic's custom Security Service Provider Interface (SSPI). The following are features of the KAAJEE SSPI:

- Compatibility with WebLogic 10.3.6 and higher:
    - Deployment Descriptors have stricter validation requirements
    - WebLogic Versions 10.3.6 and higher are dependent on JDK 1.7
    - KAAJEE is dependent on VistALink, which is now dependent on WebLogic 10.3.6 and higher.
- Directory Structure:
    - KAAJEE 1.2.0 retains the same directory structure as in KAAJEE 1.1.
    - The directory structure of the distribution zip files is as follows:

/kaajee\_security\_provider\_1.2.0.xxx – This is the KAAJEE SSPI &lt;root&gt; level folder containing the following files:

- build.xml—KAAJEE SSPI Ant build script.
- readme.txt—KAAJEE SSPI documentation (manual), which includes an introduction, change history, any special installation instructions, and any known issues/limitations.
- wlKaajeeSecurityProviders-1.2.0.xxx.jar—The KAAJEE SSPI software deployment jar file.
- wlKaajeeSecurityProviders-1.2.0.xxx.jar.MD5—The MD5 checksum value for the KAAJEE SSPI software deployment jar file.

/common\_pool\_jars -- This folder contains the following files:

- commons-collections4-4.1.jar
- commons-dbcp2-2.3.0.jar
- commons-pool2-2.5.0.jar

/props -- This properties folder contains the following files:

- KaajeeDatabase.properties
- KaajeeManageableAuthenticator.xml

/sql -- This folder contains the SQL scripts for the following databases:

- CacheTables.sql
- OracleTables.sql

/src -- This folder contains the KAAJEE SSPI Java source code (i.e., the application server software).

/kaajee-1.2.0.xxx contains the following sub-folders:

-         /dd\_examples -- This folder contains sample deployment descriptors.

-         /doc -- This folder contains a readme.txt file.

-         /jars -- This folder contains the KAAJEE JAR file and related JSP files.

-         /javadoc -- This folder contains the KAAJEE javadocs.

-     /samples -- This folder contains the KAAJEE Sample Web application

-     /samples

-     	/sso-ccow -- This folder contains elements to make the KAAJEE Sample
Web application Single Sign-On (SSO) enabled.

-         /src  -- This folder contains the KAAJEE Java source code.

### For More Information

For more information on any new feature discussed in the Release Notes, please see the KAAJEE documentation set.

*This page is left blank intentionally.*

## New Features / Changes for KAAJEE Version 1.2

### Upgraded Deployment Descriptors:

All KAAJEE deployment descriptors have been upgraded as recommended by the WebLogic 10.3.6 and higher documentation. It is recommended that consuming applications do the same.

For KAAJEE, the sample WebLogic deployment descriptors were changed from referencing DTD based document to a Schema based document.

KAAJEE product line is fully Fortify and TRM compliant. All the dependencies have been updated with the latest TRM-approved versions.

### Design Changes to Better Support Additional SSL Use Cases

Previously, KAAJEE only supported the Secure Sockets Layer (SSL) use case where SSL was used on the KAAJEE login page and controller servlet only.  Therefore, applications needing other SSL use cases such as SSL on their protected application pages and/or welcome page would have required other means to provide SSL (e.g., a load balancer such as Big-IP from F5 with the SSL Acceleration Module, which can provide encrypting to SSL and decrypting to non-SSL).

In addition to supporting only limited use cases for SSL, previous KAAJEE versions' redirect code to submit j\_username and j\_password to j\_security\_check was limited. The protocol (http or https) used for the targeted application page was dependent on whether the redirect was performed with a relative link vs. a complete URL reference. Also, the target page's protocol was dependent on how the security-constraints were defined in web.xml.

The former redirect code that redirected to the "magic servlet"  j\_security\_check has been replaced with a call to BEA WebLogic's ServletAuthentication.authenticate API. Upon successful authentication of the user, KAAJEE redirects to the original targeted URL (including original protocol) of the protected application page. The protocol (http or https) for this page is only subject to modification by any security-constraints defined in web.xml.

Furthermore, the previous SSL-related redirects have been removed from login.jsp.  In addition, the &lt;ssl-listen-port-number&gt; tag from the KAAJEE configuration file (i.e., kaajeeConfig.xml) has been removed.  Therefore, there is no longer a need to edit the KAAJEE configuration file for configuring SSL.  Instead, use the '&lt;transport-guarantee&gt;' sub-element in web.xml to configure SSL.  See the following for details.

Listed below are the SSL use cases that KAAJEE now supports:

- **Supported SSL Use Case** 1: No SSL. The welcome/non-protected page (if any), login page, and target protected page are in non-SSL mode.
- **Supported SSL Use Case 2** : Welcome/non-protected page is in SSL. All subsequent pages including KAAJEE login page remain be in SSL by default. All referenced pages will remain in SSL as long as relative links are used while logged in that don't specify/change the protocol back to http. Downgrade to non-SSL is possible only if a link explicitly specifies a protocol change to http, and if the page is not protected with 'CONFIDENTIAL' in the transport-guarantee tag in web.xml.
- **Supported SSL Use Case 3** : KAAJEE login page only will be in SSL and target application protected page will be in non-SSL.
- **Supported SSL Use Case 4:** Regardless of the protocol used for the welcome/non-protected page, KAAJEE login page and target application protected page are now in SSL. Once logged into SSL, all subsequent pages after the target 'CONFIDENTIAL' page remain be in SSL by default. As long as relative links are used while logged in that don't specify/change the protocol back to http, all referenced pages will remain in SSL. Downgrade to non-SSL is possible only if a link explicitly specifies a protocol change to http, and if the page is not protected with 'CONFIDENTIAL' in the transport-guarantee tag in web.xml.

Listed below is the use case that is NOT supported:

- KAAJEE login page is in non-SSL and target application protected page is in SSL.

### Configure Web.xml to Enable SSL

To enable SSL for a particular protected page, in web.xml, for the &lt;security-constraint&gt;' element whose &lt;web-resource-collection&gt; contains that page, set the value of the '&lt;transport-guarantee&gt;' sub-element to CONFIDENTIAL, within the '&lt;user-data-constraint&gt;' sub-element.Generally, form-based authentication would handle both authentication and authorization. Beginning with this build 005, KAAJEE only implements the user interface part of form-based authentication. The back-end security check is replaced with the ServletAuthentication.authenticate API. Therefore, all authorization failures are handled solely by container security. As such all users who are not authorized to access the targeted page after login will receive an http '403' error. To provide a more user-friendly error message, KAAJEE now distributes a 'loginerror403.jsp' file. The consuming application may use this page or another of their choosing. To use this page, add an '&lt;error-page&gt;' entry in web.xml similar to the one listed below:

&lt;error-page&gt;

&lt;error-code&gt;403&lt;/error-code&gt;

&lt;location&gt;/login/loginerror403.jsp&lt;/location&gt;

&lt;/error-page&gt;

### Integration of Kernel Patch XU*8*451: KAAJEE Login Page—Removal of Refresh Button.

Kernel Patch XU*8*451 provides the following functionality and bug fixes:

- Enhanced Login Functionality:

- Removed Refresh button from KAAJEE login page.
- Added JavaScript code for client-side sorting of Institutions.
- Provided Access and Verify code capability in one line.
- Added support for parameter passing of Default Institution and Institution sorting preferences. This addresses the issues of persistent cookies when using Thin Clients and Terminal Servers.
- Made the KAAJEE Login Web page more Section 508 friendlier.

- Added KAAJEE Sample Web Application.
- Updated Software Version Support:
    - Compiled and tested KAAJEE against Standard Data Service (SDS) 18.0.
    - Compiled and tested KAAJEE against VistALink 1.6.1.xxx.

- Fixed Response already committed error. The code that was fixed was associated with processing the persistent cookie information on the Application Server. This fix should also fix the extra M process that was created.

### Administrator Security Role for LoginController

The security role assignment has been upgraded in both web.xml and weblogic.xml. Changed the weblogic.xml file in the KAAJEE server application to use KAAJEE in the run-as-principal-name element. It is important that the “KAAJEE” user account (principal) has administrative privileges.  If a different principal is used for this purpose, the weblogic.xml file will have to reflect this change.

The format of identifying the cookie name in the &lt;session-descriptor&gt; in weblogic.xml has changed for WebLogic 10.3.6. The changes to each document are as follows:

- web.xml:

&lt;servlet&gt;

&lt;servlet-name&gt;LoginController&lt;/servlet-name&gt;

&lt;servlet-class&gt;gov.va.med.authentication.kernel.servlet.LoginController

&lt;/servlet-class&gt;

&lt;run-as&gt;

&lt;role-name&gt;adminuserrole&lt;/role-name&gt;

&lt;/run-as&gt;

&lt;/servlet&gt;

&lt;security-role&gt;

&lt;role-name&gt;adminuserrole&lt;/role-name&gt;

&lt;/security-role&gt;

- weblogic.xml:

&lt;run-as-role-assignment&gt;

&lt;role-name&gt;adminuserrole&lt;/role-name&gt;

&lt;run-as-principal-name&gt; **KAAJEE** &lt;/run-as-principal-name&gt;

&lt;/run-as-role-assignment&gt;

&lt;security-role-assignment&gt;

&lt;role-name&gt;AUTHENTICATED\_KAAJEE\_USER&lt;/role-name&gt;

&lt;principal-name&gt;AUTHENTICATED\_KAAJEE\_USER&lt;/principal-name&gt;

&lt;/security-role-assignment&gt;

&lt;session-descriptor&gt;

&lt;cookie-name&gt;kaajeeJSESSIONID&lt;/cookie-name&gt;

&lt;/session-descriptor&gt;

| <!-- image -->   | **NOTE:**  The Classpath on WebLogic 10.3.6 and higher Managed Servers, which is located on the Start Server tab, must now include the classpath to the KAAJEE SSPI JAR file. (i.e., wlKaajeeSecurityProviders-1.2.0.005.jar).   |
|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

### Sign-On/User Context (SSO/UC)-Enabled

Developers now have the option to make KAAJEE-based applications Single Sign-On/User Context (SSO/UC)-enabled. See the KAAJEE Deployment Guide for the details on how to enable your application. The current implementation of single sign-on is based on the user context of the Clinical Context Object Workgroup (CCOW) standard.

KAAJEE architecture will now allow users to authenticate and sign on to multiple applications that are CCOW-enabled and Single Sign-On/User Context (SSO/UC)-aware using a single set of credentials, which will reduce the need for multiple IDs and passwords.

### Section 508 Issue Regarding Session Timeouts

KAAJEE now displays an alert dialogue box, warning the end-user how much time remains before the login session expires. This warning is displayed 30 seconds prior to the expiration of the user's login session. In order to provide this warning, KAAJEE utilizes JavaScript. Therefore, KAAJEE distributes a login.js file, which is exported as part of the login\javascript\ folder.

### Dependency Upgrades

- WebLogic: KAAJEE is now dependent on WebLogic 10.3.6 and higher.
- VistALink: KAAJEE is now dependent on VistaLink 1.6.1
- Java: KAAJEE is now dependent on Java 1.7

## New Features / Changes for KAAJEE Security Provider Version 1.2.0

### KAAJEE SSPI codebase has been made Fortify and TRM compliant

The original Kernel Authentication &amp; Authorization for J2EE (KAAJEE) Security Provider was developed ten years ago, as the progress moves on, so does the “approved tools” list on TRM. KAAJEE SSPI now utilizes the log4j2, as well as updated apache commons libraries. The updated code has been Fortify remediated and scanned, achieving a successful certification.

### KAAJEE SSPI Upgraded to WebLogic's AuthenticationProviderV2 SSPI

The original Kernel Authentication &amp; Authorization for J2EE (KAAJEE) Security Provider was based on BEA WebLogic's AuthenticationProvider Security Service Provider Interface (SSPI). However, as of BEA WebLogic Server 10.3.6 and higher, this AuthenticationProvider SSPI has become deprecated. The KAAJEE Security Provider 1.2 now implements WebLogic's AuthenticationProvider 2 SSPI.

*This page is left blank intentionally.*