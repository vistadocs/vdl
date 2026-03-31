---
consolidated_title: "kaajee classic release notes"
app_code: KAAJEE
doc_type: RN
master_source: "KAAJEE Classic 1.2 Release Notes"
master_pub_date: August 2020
consolidated_from: 2 versions
prior_versions:
  - "KAAJEE Classic Release Notes"
---

**KERNEL AUTHENTICATION &amp; AUTHORIZATION FOR J2EE (KAAJEE) VERSION 1.2.0**

**FOR WEBLOGIC (WL) VERSIONS 10.3.6 AND HIGHER**

**RELEASE NOTES**

August 2020

Department of Veterans Affairs (VA) Office of Information and Technology (OI&amp;T)

Product Development

<!-- image -->

*This page is left blank intentionally.*

<!-- image -->

Contents

**1.**

**Introduction	1-1**

1.1.

1.2.

1.3.

1.4.

Orientation	1-1

About KAAJEE, KAAJEE Classic	1-1

Distribution	1-1

For More Information	1-2

**2.**

**New Features / Changes for KAAJEE Version 1.2	2-1**

2.1.

2.2.

2.3.

2.4.

2.5.

2.6.

2.7.

2.8.

Upgraded Deployment Descriptors:	2-1

Design Changes to Better Support Additional SSL Use Cases	2-1

Configure Web.xml to Enable SSL	2-2

Integration of Kernel Patch XU*8*451: KAAJEE Login Page—Removal of Refresh Button.2-2 Administrator Security Role for LoginController	2-3

Sign-On/User Context (SSO/UC)-Enabled	2-4

Section 508 Issue Regarding Session Timeouts	2-4

Dependency Upgrades	2-4

August 2020

Kernel Authentication and Authorization Java (2) Enterprise Edition (KAAJEE) Release Notes

Version 1.2 on WebLogic 10.3.6 and higher

iii

<!-- image -->

Contents

*This page is left blank intentionally.*

iv

Kernel Authentication &amp; Authorization for J2EE (KAAJEE) 1.2.0 Release Notes

August 2020

<!-- image -->

1. Introduction

**1.1. Orientation**

Significant KAAJEE and Kaajee Security Provider release objects (JARs, EARs, WARs, etc.) contain a build number in the filenames (e.g., in "kaajee-1.2.0.xxx.jar" where "xxx" is the build number). Build numbers are increments with each new Developer Preview. Consult the following table for KAAJEE build increment details.

**1.2. About KAAJEE, KAAJEE Classic**

Kernel Authentication &amp; Authorization for Java 2 Enterprise Edition (KAAJEE) for Web-based Health ***e*** Vet applications on WebLogic 10.3.6 and higher, such as Pharmacy Re-Engineering (PRE), provides user authentication to grant access to applications, and retrieves VistA security keys for application authorization. KAAJEE takes advantage of the current user store in VistA to authenticate users in new Health ***e*** Vet applications. Considered an interim solution, KAAJEE will be enhanced to provide the connection to the Department of Veterans Affairs (VA) Enterprise user authentication (sign- on) system in the future. KAAJEE and Fat-client Kernel Authentication and Authorization (FatKAAT) use VistALink as a connectivity solution from Java 2 Platforms, Enterprise Edition (J2EE) applications to Mumps (M)/VistA.WebLogic Updates Project.

KAAJEE 1.2 is the successor to KAAJEE 1.1, which was originally released to support the BEA WebLogic Server 9.2 platform. Version 1.2 of KAAJEE now supports Oracle WebLogic Server 10.3.6 and higher, and is fully Fortify and TRM compliant.

Like KAAJEE 1.1, KAAJEE 1.2 provides a custom Authentication Provider "plug-in" for BEA WebLogic J2EE servers, including a set of web forms for web applications that allow web applications to authenticate and authorize an end-user using a Kernel system as the source of authentication and authorization. A form is presented upon protected resource request, gathering user A/V codes and presenting a list of pre-determined stations. Such functionality will be referred to as “KAAJEE Classic”, as to denote original implementation of a complete authentication process tied to VistA. Since VA has moved towards two-factory authentication mechanisms, a successor in KAAJEE family has sprung – Single Sign-On Web Application Plugin, SSOWAP. It is important to denote the differences between KAAJEE Classic and KAAJEE SSOWAP, notwithstanding User Interface similarities, the authentication mechanisms and deployment requirements are very different.

**1.3. Distribution**

Version 1.2 of KAAJEE Classic implements all current features of KAAJEE 1.1. Included in the distribution are the following:











KAAJEE 1.2 jar files

Folder of Login web forms for Forms Authentication to drop into a J2EE Web application JavaDoc Application Programming Interface (API) documentation for the user manager classes Deployment Descriptor examples

Complete source code for the KAAJEE Classic implementation

August 2020

Kernel Authentication and Authorization Java (2) Enterprise Edition (KAAJEE) Release Notes

Version 1.2 on WebLogic 10.3.6 and higher

1-1

<!-- image -->

Introduction

- Sample Web Application

/kaajee-1.2.0.xxx contains the following sub-folders:

-

-

-

-

-

/dd\_examples -- This folder contains sample deployment descriptors.

/doc -- This folder contains a readme.txt file.

/jars -- This folder contains the KAAJEE JAR file and related JSP files.

/javadoc -- This folder contains the KAAJEE javadocs.

/samples -- This folder contains the KAAJEE Sample Web application and its dependencies

/samples

/sso-ccow -- This folder contains elements to make the KAAJEE Sample Web application Single Sign-On (SSO CCOW) enabled.

/src -- This folder contains the KAAJEE Java source code.

**1.4. For More Information**

For more information on any new feature discussed in the Release Notes, please see the KAAJEE documentation set.

1-2

Kernel Authentication and Authorization Java (2) Enterprise Edition (KAAJEE) Release Notes

Version 1.2 on WebLogic 10.3.6 and higher

August 2020

<!-- image -->

<!-- image -->

<!-- image -->

New Features / Changes for KAAJEE Version 1.2

http, and if the page is not protected with 'CONFIDENTIAL' in the transport-guarantee tag in web.xml.

**Supported SSL Use Case 3** : KAAJEE login page only will be in SSL and target application protected page will be in non-SSL.

**Supported SSL Use Case 4:** Regardless of the protocol used for the welcome/non-protected page, KAAJEE login page and target application protected page are now in SSL. Once logged into SSL, all subsequent pages after the target 'CONFIDENTIAL' page remain be in SSL by default. As long as relative links are used while logged in that don't specify/change the protocol back to http, all referenced pages will remain in SSL. Downgrade to non-SSL is possible only if a link explicitly specifies a protocol change to http, and if the page is not protected with 'CONFIDENTIAL' in the transport-guarantee tag in web.xml.



Listed below is the use case that is NOT supported:

- KAAJEE login page is in non-SSL and target application protected page is in SSL.

**2.3. Configure Web.xml to Enable SSL**

To enable SSL for a particular protected page, in web.xml, for the &lt;security-constraint&gt;' element whose

&lt;web-resource-collection&gt; contains that page, set the value of the '&lt;transport-guarantee&gt;' sub-element to CONFIDENTIAL, within the '&lt;user-data-constraint&gt;' sub-element.Generally, form-based authentication would handle both authentication and authorization. Beginning with this build 005, KAAJEE only implements the user interface part of form-based authentication. The back-end security check is replaced with the ServletAuthentication.authenticate API. Therefore, all authorization failures are handled solely by container security. As such all users who are not authorized to access the targeted page after login will receive an http '403' error. To provide a more user-friendly error message, KAAJEE now distributes a 'loginerror403.jsp' file. The consuming application may use this page or another of their choosing. To use this page, add an '&lt;error-page&gt;' entry in web.xml similar to the one listed below:

&lt;error-page&gt;

&lt;error-code&gt;403&lt;/error-code&gt;

&lt;location&gt;/login/loginerror403.jsp&lt;/location&gt;

&lt;/error-page&gt;

**2.4. Integration of Kernel Patch XU*8*451: KAAJEE Login Page—Removal of Refresh Button.**

Kernel Patch XU*8*451 provides the following functionality and bug fixes:

Enhanced Login Functionality:

-

-

-

-

Removed Refresh button from KAAJEE login page.

Added JavaScript code for client-side sorting of Institutions. Provided Access and Verify code capability in one line.

Added support for parameter passing of Default Institution and Institution sorting preferences. This addresses the issues of persistent cookies when using Thin Clients and Terminal Servers.

Made the KAAJEE Login Web page more Section 508 friendlier.

2-2

Kernel Authentication and Authorization Java (2) Enterprise Edition (KAAJEE) Release Notes

Version 1.2 on WebLogic 10.3.6 and higher

August 2020

<!-- image -->

New Features / Changes for KAAJEE Version 1.2





Added KAAJEE Sample Web Application.

Updated Software Version Support:

-

-

Compiled and tested KAAJEE against Standard Data Service (SDS) 18.0. Compiled and tested KAAJEE against VistALink 1.6.1.xxx.

Fixed Response already committed error. The code that was fixed was associated with processing the persistent cookie information on the Application Server. This fix should also fix the extra M process that was created.

**2.5.**

**Administrator Security Role for LoginController**

The security role assignment has been upgraded in both web.xml and weblogic.xml. Change the weblogic.xml file in the KAAJEE server application to use KAAJEE in the run-as-principal-name element. It is important that the “KAAJEE” user account (principal) has administrative privileges. If a different principal is used for this purpose, the weblogic.xml file will have to reflect this change.

The format of identifying the cookie name in the &lt;session-descriptor&gt; in weblogic.xml has changed for WebLogic 10.3.6. The changes to each document are as follows:

web.xml:

&lt;servlet&gt;

&lt;servlet-name&gt;LoginController&lt;/servlet-name&gt;

&lt;servlet- class&gt;gov.va.med.authentication.kernel.servlet.LoginController

&lt;/servlet-class&gt;

&lt;run-as&gt;

&lt;role-name&gt;adminuserrole&lt;/role-name&gt;

&lt;/run-as&gt;

&lt;/servlet&gt;

&lt;security-role&gt;

&lt;role-name&gt;adminuserrole&lt;/role-name&gt;

&lt;/security-role&gt;

weblogic.xml:

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

August 2020

Kernel Authentication and Authorization Java (2) Enterprise Edition (KAAJEE) Release Notes

Version 1.2 on WebLogic 10.3.6 and higher

2-3

<!-- image -->

New Features / Changes for KAAJEE Version 1.2

**NOTE:** The Classpath on WebLogic 10.3.6 and higher Managed Servers, which is located on the Start Server tab, must now include the classpath to the KAAJEE SSPI JAR file. (i.e., wlKaajeeSecurityProviders-1.2.0.005.jar) in case of 1.2 implementation. KAAJEE SSPI 1.3 does not have that requirement.

**2.6. Sign-On/User Context (SSO/UC)-Enabled**

Developers now have the option to make KAAJEE-based applications Single Sign-On/User Context (SSO/UC)-enabled. See the KAAJEE Deployment Guide for the details on how to enable your application. The current implementation of single sign-on is based on the user context of the Clinical Context Object Workgroup (CCOW) standard.

KAAJEE architecture will now allow users to authenticate and sign on to multiple applications that are CCOW-enabled and Single Sign-On/User Context (SSO/UC)-aware using a single set of credentials, which will reduce the need for multiple IDs and passwords.

There is an SSO two-factor authentication implementation - SSO Web Application Plugin– KAAJEE SSOWAP. It is a separate distribution and is not part of this package.

**2.7. Section 508 Issue Regarding Session Timeouts**

KAAJEE now displays an alert dialogue box, warning the end-user how much time remains before the login session expires. This warning is displayed 30 seconds prior to the expiration of the user's login session. In order to provide this warning, KAAJEE utilizes JavaScript. Therefore, KAAJEE distributes a login.js file, which is exported as part of the login\javascript\ folder.

**2.8.	Dependency Upgrades**







WebLogic: KAAJEE is now dependent on WebLogic 10.3.6 and higher. VistALink: KAAJEE is now dependent on VistaLink 1.6.1

Java: KAAJEE is now dependent on Java 1.7

2-4

Kernel Authentication and Authorization Java (2) Enterprise Edition (KAAJEE) Release Notes

Version 1.2 on WebLogic 10.3.6 and higher

August 2020

<!-- image -->

August 2020

Kernel Authentication and Authorization Java (2) Enterprise Edition (KAAJEE) Release Notes

Version 1.2 on WebLogic 10.3.6 and higher

2-1

<!-- image -->

New Features / Changes for KAAJEE Security Provider Version 1.2

*This page is left blank intentionally.*

2-2

Kernel Authentication and Authorization Java (2) Enterprise Edition (KAAJEE) Release Notes

Version 1.2 on WebLogic 10.3.6 and higher

August 2020

<!-- image -->

---

## Appendix: Unique Sections from Prior Versions

_These sections appeared in earlier versions of this document but are not present in the current master. They may describe features, procedures, or configurations that were removed, superseded, or restructured._

### From: KAAJEE Classic Release Notes

## KERNEL AUTHENTICATION &amp; AUTHORIZATION FOR J2EE (KAAJEE)

## VERSION 8.0.749 FOR WEBLOGIC (WL) VERSIONS 12.2 AND HIGHER

## RELEASE NOTES

## March 2022

Department of Veterans Affairs (VA) Office of Information and Technology (OI&amp;T) Product Development

This page is left blank intentionally.

## Contents

|   1. | Introduction.................................................................................................................... 1-1   | Introduction.................................................................................................................... 1-1   |
|------|----------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
|      | 1.1.                                                                                                                                   | Orientation .............................................................................................................. 1-1         |
|      | 1.2.                                                                                                                                   | About KAAJEE, KAAJEE Classic .............................................................................. 1-1                        |
|      | 1.3.                                                                                                                                   | Distribution.............................................................................................................. 1-1         |
|      | 1.4.                                                                                                                                   | For More Information................................................................................................ 1-2               |
|    2 | New Features / Changes for KAAJEEVersion 8.0.749 ....................................................... 2-1                           | New Features / Changes for KAAJEEVersion 8.0.749 ....................................................... 2-1                           |
|      | 2.1.                                                                                                                                   | Upgraded Deployment Descriptors:............................................................................. 2-1                      |
|      | 2.2.                                                                                                                                   | Administrator Security Role for LoginController........................................................... 2-1                         |
|      | 2.3.                                                                                                                                   | Sign-On/User Context (SSO/UC)-Enabled.................................................................... 2-2                          |
|      | 2.4.                                                                                                                                   | Section 508 Issue Regarding Session Timeouts ............................................................. 2-2                         |
|      | 2.5.                                                                                                                                   | Dependency Upgrades............................................................................................... 2-2                 |

## This page is left blank intentionally.

## Introduction

## Orientation

Going forward significant KAAJEE Classic, KAAJEE SSOWAP and KAAJEE Security Provider release objects (JARs, EARs, WARs, ZIP) will correspond to a patch denomination in FORUM (e.g., in "kaajee8.0.749.jar" where "8.0.749" is the patch number).

## About KAAJEE, KAAJEE Classic

Kernel Authentication &amp; Authorization for Java 2 Enterprise Edition (KAAJEE) for Web-based Health e Vet applications on WebLogic 12.2 and higher, such as Pharmacy Re-Engineering (PRE), provides user authentication to grant access to applications, and retrieves VistA security keys for application authorization. KAAJEE takes advantage of the current user store in VistA to authenticate users in new Health e Vet applications. Considered an interim solution, KAAJEE will be enhanced to provide the connection to the Department of Veterans Affairs (VA) Enterprise user authentication (signon) system in the future. KAAJEE and Fat-client Kernel Authentication and Authorization (FatKAAT) use VistALink as a connectivity solution from Java 2 Platforms, Enterprise Edition (J2EE) applications to Mumps (M)/VistA.WebLogic Updates Project.

KAAJEE 1.2 is the successor to KAAJEE 1.1, which was originally released to support the BEA WebLogic Server 9.2 platform.  Version 1.2 of KAAJEE now supports Oracle WebLogic Server 10.3.6 and higher, and is fully Fortify and TRM compliant.

Like KAAJEE 1.2, KAAJEE Classic 8.0.749 provides a custom Authentication Provider "plug-in" for BEA WebLogic J2EE servers, including a set of web forms for web applications that allow web applications to authenticate and authorize an end-user using a Kernel system as the source of authentication and authorization. A form is presented upon protected resource request, gathering user A/V codes and presenting a list of pre-determined stations. Such functionality will be referred to as 'KAAJEE Classic', as to denote original implementation of a complete authentication process tied to VistA. Since VA has moved towards two-factory authentication mechanisms, a successor in KAAJEE family has sprung - Single Sign-On Web Application Plugin, SSOWAP. It is important to denote the differences between KAAJEE Classic and KAAJEE SSOWAP, notwithstanding User Interface similarities, the authentication mechanisms and deployment requirements are very different.

## Distribution

KAAJEE Classic 8.0.749 implements all current features of KAAJEE 1.2, except for those related to the persistent cookie handling and support.  Included in the distribution are the following:

- KAAJEE 8.0.749 jar file and its dependencies
- Folder of Login web forms for Forms Authentication to drop into a J2EE Web application
- JavaDoc Application Programming Interface (API) documentation for the user manager classes
- Deployment Descriptor examples
- Complete source code for the KAAJEE Classic implementation
- Sample Web Application

/kaajee-8.0.749 contains the following sub-folders:

-         /dd\_examples -- This folder contains sample deployment descriptors.
-         /doc -- This folder contains a readme.txt file.
-         /jars -- This folder contains the KAAJEE JAR file and related JSP files.
-         /javadoc -- This folder contains the KAAJEE javadocs.
-     /samples -- This folder contains the KAAJEE Sample Web application and its dependencies
-     /samples
- -/sso-ccow -- This folder contains elements to make the KAAJEE Sample Web application Single Sign-On (SSO CCOW) enabled.
-         /src  -- This folder contains the KAAJEE Java source code.

## For More Information

For more information on any new feature discussed in the Release Notes, please see the KAAJEE documentation set.

## This page is left blank intentionally.

1-3

## New Features / Changes for KAAJEE Version 8.0.749

## Upgraded Deployment Descriptors:

All KAAJEE deployment descriptors have been upgraded as recommended by the WebLogic 12.2 and higher documentation. It is recommended that consuming applications do the same.

For KAAJEE, the sample WebLogic deployment descriptors were changed from referencing DTD based document to a Schema based document.

KAAJEE product line is fully Fortify and TRM compliant. All the dependencies have been updated with the latest TRM-approved versions.

Persistent cookie handling and support has been removed from this release.

## Administrator Security Role for LoginController

The security role assignment has been upgraded in both web.xml and weblogic.xml. There is no more 'magic' AUTHENTICATED\_KAAJEE\_USER role. Change the weblogic.xml file in the KAAJEE server application to use KAAJEE in the run-as-principal-name element. It is important that the 'KAAJEE' user account (principal) has administrative privileges.  If a different principal is used for this purpose, the weblogic.xml file will have to reflect this change.

However, newer version of WebLogic (12.2) requires a configuration change in order to enable programmatic creation and removal of the users. Please see a new section in the Deployment Guide for details on Configuring Administrative User

The format of identifying the cookie name in the &lt;session-descriptor&gt; in weblogic.xml has changed for WebLogic 12.2. The changes to each document are as follows:

- web.xml:
- ·

```
<servlet> <servlet-name>LoginController</servlet-name> <servletclass>gov.va.med.authentication.kernel.servlet.LoginController </servlet-class> <run-as> <role-name>adminuserrole</role-name> </run-as> </servlet> <security-role> <role-name>adminuserrole</role-name> </security-role> weblogic.xml: <run-as-role-assignment>
```

```
<role-name>adminuserrole</role-name> <run-as-principal-name> KAAJEE </run-as-principal-name> </run-as-role-assignment> <session-descriptor> <cookie-name>kaajeeJSESSIONID</cookie-name> </session-descriptor>
```

## Sign-On/User Context (SSO/UC)-Enabled

Developers now have the option to make KAAJEE-based applications Single Sign-On/User Context (SSO/UC)-enabled. See the KAAJEE Deployment Guide for the details on how to enable your application. The current implementation of single sign-on is based on the user context of the Clinical Context Object Workgroup (CCOW) standard.

KAAJEE architecture will now allow users to authenticate and sign on to multiple applications that are CCOW-enabled and Single Sign-On/User Context (SSO/UC)-aware using a single set of credentials, which will reduce the need for multiple IDs and passwords.

There is an SSO two-factor authentication implementation  - SSO Web Application Plugin- KAAJEE SSOWAP. It is a separate distribution and is not part of this package.

## Section 508 Issue Regarding Session Timeouts

KAAJEE now displays an alert dialogue box, warning the end-user how much time remains before the login session expires. This warning is displayed 30 seconds prior to the expiration of the user's login session. In order to provide this warning, KAAJEE utilizes JavaScript. Therefore, KAAJEE distributes a login.js file, which is exported as part of the login\javascript\ folder.

## Dependency Upgrades

- WebLogic: KAAJEE is now dependent on WebLogic 12.2 and higher.
- VistALink: KAAJEE is now dependent on VistaLink 1.6.7
- Java: KAAJEE is now dependent on Java 1.8

2-2

## This page is left blank intentionally.
