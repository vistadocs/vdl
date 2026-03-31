---
consolidated_title: "blind rehab centralized server installation/implementation guide"
app_code: ANRV
doc_type: IG-IMP
master_source: "Blind Rehab Version 5.1.10 Centralized Server Installation/Implementation Guide"
master_pub_date: September 2024
consolidated_from: 7 versions
prior_versions:
  - "Blind Rehab Version 5.1.13 Centralized Server Installation/Implementation Guide"
  - "Blind Rehab Version 5.1.14 Centralized Server Installation/Implementation Guide"
  - "Blind Rehab Version 5.1.15 Centralized Server Installation/Implementation Guide"
  - "Blind Rehab Version 5.1.16 Centralized Server Installation/Implementation Guide"
  - "Blind Rehab Version 5.1.17 Centralized Server Installation/Implementation Guide"
  - "Blind Rehab Version 5.1.18 Centralized Server Installation/Implementation Guide"
---

---
title: |
  Blind Rehabilitation (ANRV)

  Blind Rehabilitation Centralized Server Installation/Implementation Guide
---

![](blind-rehab-version-5-1-10-centralized-server-installation-implementation-guide/001.png)

September 2024Version 1.0

Revision History

|                |         |                  |                 |
|----------------|---------|------------------|-----------------|
| Date           | Version | Description      | Author          |
| September 2024 | 1.0     | Technical Update | Robert Eckstein |

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Audience](#audience)
  - [Scope/Deliverables](#scopedeliverables)
  - [Purpose](#purpose)
- [Table of Server Configurations](#table-of-server-configurations)
- [WebLogic Administrator Steps](#weblogic-administrator-steps)
  - [Deployment of Compiled \.ear File](#deployment-of-compiled-ear-file)
  - [Roll Back \.ear File](#roll-back-ear-file)
- [Appendix A Sample config.xml file](#appendix-a-sample-configxml-file)
- [Appendix C – sample JVM Server startup arguments](#appendix-c-sample-jvm-server-startup-arguments)
- [Appendix D – WebLogic server commands](#appendix-d-weblogic-server-commands)
- [Appendix E – Troubleshooting](#appendix-e-troubleshooting)
The Blind Rehabilitation Services application provides enhanced tracking, and reporting, of the blind rehabilitation services provided to veterans by: Visual Impairment Service Teams (VIST) Coordinators Blind Rehabilitation Centers (BRCs) Blind Rehabilitation Outpatient Specialists (BROS) Visual Impairment Services Outpatient Rehabilitation (VISOR) Programs Visual Impairment Center to Optimize Remaining Sight (VICTORS)Features include: Electronic referral process to track patient applications for service Notifications feature to alert users of pending referrals Encounters/Progress Notes will be automatically created Nationwide centralization of Blind Rehabilitation services data to allow nationwide reporting Ad-hoc reporting capabilities Allows ability to track BR patient care access across institutions Patients can be referred or transferred to other institutions if they move without having to recreate patient data.

## Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This document has been prepared for system administrators and database administrators who need to set up pre-production and/or production environments in the VA Enterprises Cloud (VAEC). It is presumed that readers of this document understand basic concepts of the VAEC BR v5.1 environments as well as any system specialties that might pertain to the installation of the BR v5.1 software.

## Scope/Deliverables

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The scope of this plan encompasses the Blind Rehabilitation Services, and their related responsibilities. The plan specifies the steps and software necessary to install and configure BR v5.1 on a Linux server environment.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The purpose of this document is to assist the IO and support in the installation/configuration of BR v5.1.

# Table of Server Configurations

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 16%" />
<col style="width: 20%" />
<col style="width: 23%" />
<col style="width: 22%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr class="header">
<th>Environment</th>
<th>Domain Name</th>
<th>Admin Server</th>
<th>Managed Servers</th>
<th>DB name: port</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>Dev (Single VM)</strong></td>
<td>brs-dev</td>
<td>AdminServer(admin)</td>
<td><p>ManagedServer001</p>
<p>ManagedServer002</p></td>
<td>DBA has Info</td>
</tr>
<tr class="even">
<td><strong>SQA (Single VM)</strong></td>
<td>brs-sqa</td>
<td>AdminServer(admin)</td>
<td><p>ManagedServer001</p>
<p>ManagedServer002</p></td>
<td>DBA has Info</td>
</tr>
<tr class="odd">
<td><strong>Pre-Prod</strong></td>
<td>brs-ppd</td>
<td><p>Region 1</p>
<p>AdminServer(admin)</p></td>
<td><p>Region 1</p>
<p>ManagedServer001</p>
<p>ManagedServer002</p>
<p>ManagedServer003</p>
<p>ManagedServer004</p></td>
<td>DBA has Info</td>
</tr>
<tr class="even">
<td><strong>Production</strong></td>
<td>brs-prd</td>
<td><p>Region 1</p>
<p>AdminServer(admin)</p></td>
<td><p>Region 1</p>
<p>ManagedServer001</p>
<p>ManagedServer002</p>
<p>ManagedServer003</p>
<p>ManagedServer004</p></td>
<td>DBA has Info</td>
</tr>
</tbody>
</table>

# WebLogic Administrator Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Deployment of Compiled \*.ear File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  The deployed BR 5.1 ear (BR_EAR_5.1.7.23.ear) files must be uploaded to the server by a member of the BR Team.
2.  Run the following command:
    1.  \$ cp BR_EAR\_\<version\>.ear /u01/app/oracle/user_projects/domains/brs-ppd/appStage
    2.  \$ cd /u01/app/oracle/user_projects/domains/brs-ppd/appStage
    3.  \$ chown weblogic:weblogic \*

> Or:

4.  \$ cp BR_EAR\_\<version\>.ear/u01/app/oracle/user_projects/domains/brs-prd/appStage
5.  \$ cd /u01/app/oracle/user_projects/domains/brs-prd/appStage
6.  \$ chown weblogic:weblogic \*
3.  Now go into WebLogic and deploy the ear file as an application.
4.  Go into the WebLogic admin console and click on the domain. Select the JTA tab click and change the Timeout Second: to 600 and save the change.

## Roll Back \*.ear File

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  The previously deployed BR 5.1 ear(master/BR_EAR_5.1.6.18.ear) file must be uploaded to the server by a member of the BR Team. (files can be obtained from Jenkins)
2.  Run the following command:
    1.  \$ cp BR_EAR\_\<version\>.ear /u01/app/oracle/user_projects/domains/brs-ppd/appStage
    2.  \$ cd /u01/app/oracle/user_projects/domains/brs-ppd/appStage
    3.  \$ chown weblogic:weblogic \*

> Or:

4.  \$ cp BR_EAR\_\<version\>.ear/u01/app/oracle/user_projects/domains/brs-prd/appStage
5.  \$ cd /u01/app/oracle/user_projects/domains/brs-prd/appStage
6.  \$ chown weblogic:weblogic \*
3.  Now go into WebLogic and deploy the ear file as an application.
4.  Go into the WebLogic admin console and click on the domain. Select the JTA tab click and change the Timeout Second: to 60 and save the change.

# Appendix A Sample config.xml file

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

As you are troubleshooting BR one of the areas that commonly has issues is the default installed config.xml file. Below is a standardized config.xml file that can be copied in place of the stock one to solve some classpath and file issues.

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Start of sample config.xml \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> \<?xml version='1.0' encoding='UTF-8'?\>

> \<domain xmlns="http://xmlns.oracle.com/weblogic/domain" xmlns:sec="http://xmlns.oracle.com/weblogic/security" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:wls="http://xmlns.oracle.com/weblogic/security/wls" xsi:schemaLocation="http://xmlns.oracle.com/weblogic/security/wls http://xmlns.oracle.com/weblogic/security/wls/1.0/wls.xsd http://xmlns.oracle.com/weblogic/domain http://xmlns.oracle.com/weblogic/1.0/domain.xsd http://xmlns.oracle.com/weblogic/security/xacml http://xmlns.oracle.com/weblogic/security/xacml/1.0/xacml.xsd http://xmlns.oracle.com/weblogic/security/providers/passwordvalidator http://xmlns.oracle.com/weblogic/security/providers/passwordvalidator/1.0/passwordvalidator.xsd http://xmlns.oracle.com/weblogic/security http://xmlns.oracle.com/weblogic/1.0/security.xsd"\>

> \<name\>brs-dev\</name\>

> \<domain-version\>12.2.1.4.0\</domain-version\>

> \<security-configuration\>

> \<name\>brs-dev\</name\>

> \<realm\>

> \<sec:authentication-provider xsi:type="wls:default-authenticatorType"\>

> \<sec:name\>DefaultAuthenticator\</sec:name\>

> \<sec:control-flag\>SUFFICIENT\</sec:control-flag\>

> \</sec:authentication-provider\>

> \<sec:authentication-provider xsi:type="wls:default-identity-asserterType"\>

> \<sec:name\>DefaultIdentityAsserter\</sec:name\>

> \<sec:active-type\>AuthenticatedUser\</sec:active-type\>

> \<sec:active-type\>weblogic-jwt-token\</sec:active-type\>

> \</sec:authentication-provider\>

> \<sec:authentication-provider xsi:type="wls:active-directory-authenticatorType"\>

> \<sec:name\>ActiveDirectoryAuthenticator\</sec:name\>

> \<sec:control-flag\>SUFFICIENT\</sec:control-flag\>

> \<wls:host\>vaaac3dc2.aac.dva.va.gov\</wls:host\>

> \<wls:port\>3268\</wls:port\>

> \<wls:user-name-attribute\>sAMAccountName\</wls:user-name-attribute\>

> \<wls:principal\>AAC\aitcwladqry\</wls:principal\>

> \<wls:user-base-dn\>DC=va,DC=gov\</wls:user-base-dn\>

> \<wls:credential-encrypted\>{AES256}plf8YjWk+ChAaAIxWpYiWmIsJTySblQuEtjzbahV0S4=\</wls:credential-encrypted\>

> \<wls:user-from-name-filter\>(&amp;(sAMAccountName=%u)(objectclass=user))\</wls:user-from-name-filter\>

> \<wls:all-users-filter\>(memberOf=CN=AITC WEBLOGIC Admins,OU=Groups,OU=AAC,DC=aac,DC=dva,DC=va,DC=gov)\</wls:all-users-filter\>

> \<wls:group-base-dn\>OU=Groups,OU=AAC,DC=aac,DC=dva,DC=va,DC=gov\</wls:group-base-dn\>

> \<wls:all-groups-filter\>(distinguishedName=CN=AITC WEBLOGIC Admins,OU=Groups,OU=AAC,DC=aac,DC=dva,DC=va,DC=gov)\</wls:all-groups-filter\>

> \<wls:use-retrieved-user-name-as-principal\>true\</wls:use-retrieved-user-name-as-principal\>

> \<wls:use-token-groups-for-group-membership-lookup\>true\</wls:use-token-groups-for-group-membership-lookup\>

> \</sec:authentication-provider\>

> \<sec:role-mapper xmlns:xac="http://xmlns.oracle.com/weblogic/security/xacml" xsi:type="xac:xacml-role-mapperType"\>

> \<sec:name\>XACMLRoleMapper\</sec:name\>

> \</sec:role-mapper\>

> \<sec:authorizer xmlns:xac="http://xmlns.oracle.com/weblogic/security/xacml" xsi:type="xac:xacml-authorizerType"\>

> \<sec:name\>XACMLAuthorizer\</sec:name\>

> \</sec:authorizer\>

> \<sec:adjudicator xsi:type="wls:default-adjudicatorType"\>

> \<sec:name\>DefaultAdjudicator\</sec:name\>

> \</sec:adjudicator\>

> \<sec:credential-mapper xsi:type="wls:default-credential-mapperType"\>

> \<sec:name\>DefaultCredentialMapper\</sec:name\>

> \</sec:credential-mapper\>

> \<sec:cert-path-provider xsi:type="wls:web-logic-cert-path-providerType"\>

> \<sec:name\>WebLogicCertPathProvider\</sec:name\>

> \</sec:cert-path-provider\>

> \<sec:cert-path-builder\>WebLogicCertPathProvider\</sec:cert-path-builder\>

> \<sec:name\>myrealm\</sec:name\>

> \<sec:password-validator xmlns:pas="http://xmlns.oracle.com/weblogic/security/providers/passwordvalidator" xsi:type="pas:system-password-validatorType"\>

> \<sec:name\>SystemPasswordValidator\</sec:name\>

> \<pas:min-password-length\>8\</pas:min-password-length\>

> \<pas:min-numeric-or-special-characters\>1\</pas:min-numeric-or-special-characters\>

> \</sec:password-validator\>

> \</realm\>

> \<default-realm\>myrealm\</default-realm\>

> \<credential-encrypted\>{AES256}SLOKVPAmeTBz8ksEk1ZgSsDhOxiUnBwJ0SLRM3RwUsFcqAmQhzfatOSM6zTAx+IzqV8X4kmTSFgobhH1iR1COLd4m2fSwZVjiumg/dq2HDEsnBgMReEjDNil/gaQEKw6\</credential-encrypted\>

> \<node-manager-username\>weblogic\</node-manager-username\>

> \<node-manager-password-encrypted\>{AES256}JeEcne3opGZCPXSzCKcYfoAUq0piJ4uUwka1DEGJCz4=\</node-manager-password-encrypted\>

> \</security-configuration\>

> \<jta\>

> \<timeout-seconds\>60\</timeout-seconds\>

> \<abandon-timeout-seconds\>86400\</abandon-timeout-seconds\>

> \<forget-heuristics\>true\</forget-heuristics\>

> \<before-completion-iteration-limit\>10\</before-completion-iteration-limit\>

> \<max-transactions\>10000\</max-transactions\>

> \<max-unique-name-statistics\>1000\</max-unique-name-statistics\>

> \<checkpoint-interval-seconds\>300\</checkpoint-interval-seconds\>

> \<unregister-resource-grace-period\>30\</unregister-resource-grace-period\>

> \</jta\>

> \<log\>

> \<file-name\>logs/brs-dev.log\</file-name\>

> \<rotation-type\>bySize\</rotation-type\>

> \<number-of-files-limited\>true\</number-of-files-limited\>

> \<file-count\>15\</file-count\>

> \<file-min-size\>65535\</file-min-size\>

> \<rotate-log-on-startup\>false\</rotate-log-on-startup\>

> \</log\>

> \<server\>

> \<name\>AdminServer\</name\>

> \<web-server\>

> \<keep-alive-enabled\>true\</keep-alive-enabled\>

> \<keep-alive-secs\>30\</keep-alive-secs\>

> \<https-keep-alive-secs\>60\</https-keep-alive-secs\>

> \<post-timeout-secs\>30\</post-timeout-secs\>

> \<max-post-size\>-1\</max-post-size\>

> \<send-server-header-enabled\>false\</send-server-header-enabled\>

> \<wap-enabled\>false\</wap-enabled\>

> \<accept-context-path-in-get-real-path\>false\</accept-context-path-in-get-real-path\>

> \</web-server\>

> \<listen-address\>vac11appbrs800.va.gov\</listen-address\>

> \<server-life-cycle-timeout-val\>30\</server-life-cycle-timeout-val\>

> \<startup-timeout\>0\</startup-timeout\>

> \</server\>

> \<server\>

> \<name\>ManagedServer001\</name\>

> \<ssl\>

> \<enabled\>false\</enabled\>

> \<listen-port\>8002\</listen-port\>

> \<server-private-key-alias\> vac11appbrs800.va.gov\</server-private-key-alias\>

> \<server-private-key-pass-phrase-encrypted\>{AES256}YkBZpAY20X8RKHwcF3FEs2pvoteUfU16j5UV6fx/m/0=\</server-private-key-pass-phrase-encrypted\>

> \</ssl\>

> \<log\>

> \<rotation-type\>bySize\</rotation-type\>

> \<number-of-files-limited\>true\</number-of-files-limited\>

> \<file-count\>15\</file-count\>

> \<file-min-size\>65535\</file-min-size\>

> \<rotate-log-on-startup\>false\</rotate-log-on-startup\>

> \<log-file-severity\>Warning\</log-file-severity\>

> \<stdout-severity\>Error\</stdout-severity\>

> \<domain-log-broadcast-severity\>Error\</domain-log-broadcast-severity\>

> \<memory-buffer-severity\>Error\</memory-buffer-severity\>

> \<log4j-logging-enabled\>false\</log4j-logging-enabled\>

> \<redirect-stdout-to-server-log-enabled\>false\</redirect-stdout-to-server-log-enabled\>

> \<domain-log-broadcaster-buffer-size\>10\</domain-log-broadcaster-buffer-size\>

> \</log\>

> \<machine\>Machine001 (localhost)\</machine\>

> \<listen-port\>8001\</listen-port\>

> \<listen-port-enabled\>true\</listen-port-enabled\>

> \<cluster\>Cluster001\</cluster\>

> \<cluster-weight\>100\</cluster-weight\>

> \<replication-group\>primary\</replication-group\>

> \<preferred-secondary-group\>secondary\</preferred-secondary-group\>

> \<web-server\>

> \<web-server-log\>

> \<number-of-files-limited\>false\</number-of-files-limited\>

> \</web-server-log\>

> \</web-server\>

> \<listen-address\> vac11appbrs800.va.gov\</listen-address\>

> \<administration-port\>9002\</administration-port\>

> \<java-compiler\>javac\</java-compiler\>

> \<server-start\>

> \<class-path\>\$CLASSPATH\</class-path\>

> \<arguments\>-d64 -server -Xms2g -Xmx2g -XX:+UnlockCommercialFeatures -XX:+ResourceManagement -XX:+FlightRecorder -XX:+UseG1GC -Dweblogic.security.SSL.minimumProtocolVersion=TLSv1.2 -Dweblogic.security.SSL.protocolVersion=TLSv1.2 -Djava.awt.headless=true -Dweblogic.unicast.HttpPing=true\</arguments\>

> \<username\>weblogic\</username\>

> \<password-encrypted\>{AES256}Lak1s/R9MGBGoTltG508vSKZIputn+rMpyjDe6EIKA4=\</password-encrypted\>

> \</server-start\>

> \<jta-migratable-target\>

> \<user-preferred-server\>ManagedServer001\</user-preferred-server\>

> \<cluster\>Cluster001\</cluster\>

> \</jta-migratable-target\>

> \<startup-mode\>RUNNING\</startup-mode\>

> \<server-life-cycle-timeout-val\>120\</server-life-cycle-timeout-val\>

> \<startup-timeout\>0\</startup-timeout\>

> \<graceful-shutdown-timeout\>0\</graceful-shutdown-timeout\>

> \<ignore-sessions-during-shutdown\>false\</ignore-sessions-during-shutdown\>

> \<client-cert-proxy-enabled\>true\</client-cert-proxy-enabled\>

> \<weblogic-plugin-enabled\>true\</weblogic-plugin-enabled\>

> \<key-stores\>CustomIdentityAndCustomTrust\</key-stores\>

> \<custom-identity-key-store-file-name\>/u01/app/oracle/user_projects/domains/brs-dev/HEV_CONFIG/certificate_stores/keystore.jks\</custom-identity-key-store-file-name\>

> \<custom-identity-key-store-type\>JKS\</custom-identity-key-store-type\>

> \<custom-identity-key-store-pass-phrase-encrypted\>{AES256}eS1gXUjTPd4JIPRniY6hSQ90cn6zFD/0mi1UdlQ8sDA=\</custom-identity-key-store-pass-phrase-encrypted\>

> \<custom-trust-key-store-file-name\>/u01/app/oracle/user_projects/domains/brs-dev/HEV_CONFIG/certificate_stores/cacerts\</custom-trust-key-store-file-name\>

> \<custom-trust-key-store-type\>JKS\</custom-trust-key-store-type\>

> \<custom-trust-key-store-pass-phrase-encrypted\>{AES256}Wyq3RBjHIRtbyZvrrChWhvzHTTVVR+cit3jrp6mLQ0w=\</custom-trust-key-store-pass-phrase-encrypted\>

> \<server-diagnostic-config\>

> \<wldf-diagnostic-volume\>Low\</wldf-diagnostic-volume\>

> \</server-diagnostic-config\>

> \</server\>

> \<server\>

> \<name\>ManagedServer002\</name\>

> \<ssl\>

> \<enabled\>false\</enabled\>

> \<listen-port\>8004\</listen-port\>

> \<server-private-key-alias\> vac11appbrs800.va.gov\</server-private-key-alias\>

> \<server-private-key-pass-phrase-encrypted\>{AES256}a9pXTJLJbzh5xVNnRebRc2p6rf8SVLPdH/u38l2p/FY=\</server-private-key-pass-phrase-encrypted\>

> \</ssl\>

> \<log\>

> \<rotation-type\>bySize\</rotation-type\>

> \<number-of-files-limited\>true\</number-of-files-limited\>

> \<file-count\>15\</file-count\>

> \<file-min-size\>65535\</file-min-size\>

> \<rotate-log-on-startup\>false\</rotate-log-on-startup\>

> \<log-file-severity\>Warning\</log-file-severity\>

> \<stdout-severity\>Error\</stdout-severity\>

> \<domain-log-broadcast-severity\>Error\</domain-log-broadcast-severity\>

> \<memory-buffer-severity\>Error\</memory-buffer-severity\>

> \<log4j-logging-enabled\>false\</log4j-logging-enabled\>

> \<redirect-stdout-to-server-log-enabled\>false\</redirect-stdout-to-server-log-enabled\>

> \<domain-log-broadcaster-buffer-size\>10\</domain-log-broadcaster-buffer-size\>

> \</log\>

> \<machine\>Machine001 (localhost)\</machine\>

> \<listen-port\>8003\</listen-port\>

> \<listen-port-enabled\>true\</listen-port-enabled\>

> \<cluster\>Cluster001\</cluster\>

> \<cluster-weight\>100\</cluster-weight\>

> \<replication-group\>primary\</replication-group\>

> \<preferred-secondary-group\>secondary\</preferred-secondary-group\>

> \<web-server\>

> \<web-server-log\>

> \<number-of-files-limited\>false\</number-of-files-limited\>

> \</web-server-log\>

> \</web-server\>

> \<listen-address\> vac11appbrs800.va.gov\</listen-address\>

> \<administration-port\>9002\</administration-port\>

> \<java-compiler\>javac\</java-compiler\>

> \<server-start\>

> \<class-path\>\$CLASSPATH\</class-path\>

> \<arguments\>-d64 -server -Xms2g -Xmx2g -XX:+UnlockCommercialFeatures -XX:+ResourceManagement -XX:+FlightRecorder -XX:+UseG1GC -Dweblogic.security.SSL.minimumProtocolVersion=TLSv1.2 -Dweblogic.security.SSL.protocolVersion=TLSv1.2 -Djava.awt.headless=true -Dweblogic.unicast.HttpPing=true\</arguments\>

> \<username\>weblogic\</username\>

> \<password-encrypted\>{AES256}mcl9pEpFrw9pQMfTrA+QCaIrhOOtBGTTABigDZjj5HI=\</password-encrypted\>

> \</server-start\>

> \<jta-migratable-target\>

> \<user-preferred-server\>ManagedServer002\</user-preferred-server\>

> \<cluster\>Cluster001\</cluster\>

> \</jta-migratable-target\>

> \<startup-mode\>RUNNING\</startup-mode\>

> \<server-life-cycle-timeout-val\>120\</server-life-cycle-timeout-val\>

> \<startup-timeout\>0\</startup-timeout\>

> \<graceful-shutdown-timeout\>0\</graceful-shutdown-timeout\>

> \<ignore-sessions-during-shutdown\>false\</ignore-sessions-during-shutdown\>

> \<client-cert-proxy-enabled\>true\</client-cert-proxy-enabled\>

> \<weblogic-plugin-enabled\>true\</weblogic-plugin-enabled\>

> \<key-stores\>CustomIdentityAndCustomTrust\</key-stores\>

> \<custom-identity-key-store-file-name\>/u01/app/oracle/user_projects/domains/brs-dev/HEV_CONFIG/certificate_stores/keystore.jks\</custom-identity-key-store-file-name\>

> \<custom-identity-key-store-type\>JKS\</custom-identity-key-store-type\>

> \<custom-identity-key-store-pass-phrase-encrypted\>{AES256}mbfwOv3gqttSVCEw9PG0KOO3RSmCMlHHNkNssbDAHCI=\</custom-identity-key-store-pass-phrase-encrypted\>

> \<custom-trust-key-store-file-name\>/u01/app/oracle/user_projects/domains/brs-dev/HEV_CONFIG/certificate_stores/cacerts\</custom-trust-key-store-file-name\>

> \<custom-trust-key-store-type\>JKS\</custom-trust-key-store-type\>

> \<custom-trust-key-store-pass-phrase-encrypted\>{AES256}4VA1f1yS1qrEoqZ4g9P1QwLpt8R32rAdpLa2DTBndrQ=\</custom-trust-key-store-pass-phrase-encrypted\>

> \<server-diagnostic-config\>

> \<wldf-diagnostic-volume\>Low\</wldf-diagnostic-volume\>

> \</server-diagnostic-config\>

> \</server\>

> \<cluster\>

> \<name\>Cluster001\</name\>

> \<default-load-algorithm\>round-robin\</default-load-algorithm\>

> \<cluster-messaging-mode\>unicast\</cluster-messaging-mode\>

> \<cluster-broadcast-channel\>\</cluster-broadcast-channel\>

> \<service-age-threshold-seconds\>180\</service-age-threshold-seconds\>

> \<weblogic-plugin-enabled\>true\</weblogic-plugin-enabled\>

> \<member-warmup-timeout-seconds\>30\</member-warmup-timeout-seconds\>

> \<number-of-servers-in-cluster-address\>2\</number-of-servers-in-cluster-address\>

> \<dynamic-servers\>

> \<maximum-dynamic-server-count\>0\</maximum-dynamic-server-count\>

> \</dynamic-servers\>

> \</cluster\>

> \<production-mode-enabled\>true\</production-mode-enabled\>

> \<embedded-ldap\>

> \<name\>brs-dev\</name\>

> \<credential-encrypted\>{AES256}Q4pIZkAiWBxYV+0TLhFC/s6Nq6D+SZcZNtkJ9jhyFVOOjL8ow7Tvi2+hBtIONXlL\</credential-encrypted\>

> \<backup-hour\>23\</backup-hour\>

> \<backup-minute\>5\</backup-minute\>

> \<backup-copies\>7\</backup-copies\>

> \<cache-enabled\>true\</cache-enabled\>

> \<cache-size\>32\</cache-size\>

> \<cache-ttl\>60\</cache-ttl\>

> \<refresh-replica-at-startup\>false\</refresh-replica-at-startup\>

> \<master-first\>false\</master-first\>

> \<timeout\>0\</timeout\>

> \<anonymous-bind-allowed\>false\</anonymous-bind-allowed\>

> \</embedded-ldap\>

> \<administration-port-enabled\>false\</administration-port-enabled\>

> \<configuration-version\>12.2.1.4.0\</configuration-version\>

> \<cluster-constraints-enabled\>false\</cluster-constraints-enabled\>

> \<app-deployment\>

> \<name\>vlj_clin1s1_502\</name\>

> \<target\>Cluster001\</target\>

> \<module-type\>rar\</module-type\>

> \<source-path\>HEV_CONFIG/vlj_clin1s1_502\</source-path\>

> \<security-dd-model\>DDOnly\</security-dd-model\>

> \<staging-mode xsi:nil="true"\>\</staging-mode\>

> \<plan-staging-mode xsi:nil="true"\>\</plan-staging-mode\>

> \<cache-in-app-directory\>false\</cache-in-app-directory\>

> \</app-deployment\>

> \<app-deployment\>

> \<name\>BR_EAR_5.1.0\</name\>

> \<target\>Cluster001\</target\>

> \<module-type\>ear\</module-type\>

> \<source-path\>servers/AdminServer/upload/ BR_EAR_5.1.0.ear/app/ BR_EAR_5.1.0.ear\</source-path\>

> \<security-dd-model\>DDOnly\</security-dd-model\>

> \<staging-mode xsi:nil="true"\>\</staging-mode\>

> \<plan-staging-mode xsi:nil="true"\>\</plan-staging-mode\>

> \<cache-in-app-directory\>false\</cache-in-app-directory\>

> \</app-deployment\>

> \<library\>

> \<name\>vljConnector#1.6@1.6\</name\>

> \<target\>Cluster001\</target\>

> \<module-type xsi:nil="true"\>\</module-type\>

> \<source-path\>HEV_CONFIG/vljConnector-1.6.1.010.jar\</source-path\>

> \<security-dd-model\>DDOnly\</security-dd-model\>

> \<staging-mode xsi:nil="true"\>\</staging-mode\>

> \<plan-staging-mode xsi:nil="true"\>\</plan-staging-mode\>

> \<cache-in-app-directory\>false\</cache-in-app-directory\>

> \</library\>

> \<library\>

> \<name\>vljFoundationsLib#1.6@1.6\</name\>

> \<target\>Cluster001\</target\>

> \<module-type xsi:nil="true"\>\</module-type\>

> \<source-path\>HEV_CONFIG/vljFoundationsLib-1.6.1.010.jar\</source-path\>

> \<security-dd-model\>DDOnly\</security-dd-model\>

> \<staging-mode xsi:nil="true"\>\</staging-mode\>

> \<plan-staging-mode xsi:nil="true"\>\</plan-staging-mode\>

> \<cache-in-app-directory\>false\</cache-in-app-directory\>

> \</library\>

> \<machine\>

> \<name\>Machine001 (localhost)\</name\>

> \<node-manager\>

> \<nm-type\>Plain\</nm-type\>

> \<listen-address\>localhost\</listen-address\>

> \<listen-port\>5556\</listen-port\>

> \<debug-enabled\>false\</debug-enabled\>

> \</node-manager\>

> \</machine\>

> \<migratable-target\>

> \<name\>ManagedServer001 (migratable)\</name\>

> \<notes\>This is a system generated default migratable target for a server. Do not delete manually.\</notes\>

> \<user-preferred-server\>ManagedServer001\</user-preferred-server\>

> \<cluster\>Cluster001\</cluster\>

> \</migratable-target\>

> \<migratable-target\>

> \<name\>ManagedServer002 (migratable)\</name\>

> \<notes\>This is a system generated default migratable target for a server. Do not delete manually.\</notes\>

> \<user-preferred-server\>ManagedServer002\</user-preferred-server\>

> \<cluster\>Cluster001\</cluster\>

> \</migratable-target\>

> \<admin-server-name\>AdminServer\</admin-server-name\>

> \<jdbc-system-resource\>

> \<name\>vha-stddata-datasource\</name\>

> \<target\>Cluster001\</target\>

> \<descriptor-file-name\>jdbc/vha-stddata-datasource-jdbc.xml\</descriptor-file-name\>

> \</jdbc-system-resource\>

> \<internal-apps-deploy-on-demand-enabled\>false\</internal-apps-deploy-on-demand-enabled\>

> \</domain\>

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* End of sample config.xml \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

# Appendix C – sample JVM Server startup arguments

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Along with the classpath statement the other startup parameter that must be set for a JVM server to start correctly is the startup arguments. Below is a copy of working server startup arguments from a previous install. Just like the classpath statement in Appendix B, you must make sure the paths to these files really do exist on your server or you will have issues starting the server successfully.

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* Start of sample SERVER ARGUMENTS \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

> -d64 -server -Xms2g -Xmx2g -XX:+UnlockCommercialFeatures -XX:+ResourceManagement -XX:+FlightRecorder -XX:+UseG1GC -Dweblogic.security.SSL.minimumProtocolVersion=TLSv1.2 -Dweblogic.security.SSL.protocolVersion=TLSv1.2 -Djava.awt.headless=true -Dweblogic.unicast.HttpPing=true

> \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\* END of sample SERVER ARGUMENTS \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

# Appendix D – WebLogic server commands

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Below is a listing of some useful command to use when running BR on WebLogic

1.  Command to start WebLogic and Node Manager –

> cd \$DOMAIN_HOME ; rm nohup.out ; nohup ./startWebLogic.sh &

> cd \$DOMAIN_HOME/bin ; rm nohup.out ; nohup ./startNodeManager.sh &

2.  Command to start the WebLogic Admin server

> \$ /u01/app/domains/BR_DIST_DEV_DOMAIN/startWebLogic.sh &

3.  How to mail a file from the server to someone:

> \$ uuencode FILE Name_of_file_in_email \|mailx -s 'SUBJECT' EMAILADDRESS

4.  Vim command to do a global replace (example is to replace Dev with DEV):

> :%s/Dev/DEV/g

5.  Command to determine if instances of WebLogic are running:

> \$ ps aux \| grep weblogic

# Appendix E – Troubleshooting

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

BR is a very complicated environment that depends on many pieces to function correctly. Once set up correctly, it functions well with very few problems. But during the setup it can be hard to figure out which piece is not working, and the cryptic messages thrown in the WebLogic log files doesn’t always point you in the right direction. Below are several sections that will help you determine where to hunt for an error in the system.

1.  Another common error is when you try to start the managed server and it fails and gives you a message in the WebLogic console that says “Server failed to start and is not re-startable”. A lot of times this points to a bad classpath somewhere in the system. This can be a missing file that the server is looking for, or a file in a different directory than the server expects. When this happens try the following steps. Copy all the different classpath statements to notepad, format them one line each and go through every line using a locate command to make sure the files are actually there. If there is a missing jar file listed move the jar file into the expected directory as it is listed in the CLASSPATH.
2.  If you are having issues with starting the server for the first time, check to make sure that there are no Introscope or other monitoring software packages installed on the server, both the host operating system(RedHat) or on the Admin/managed VMs. These types of products can cause major installation issues with BR. These types of products should only be deployed to the system after BR is functioning properly and completely installed.
3.  If for some reason you did not follow the directions in the document to install and start most of the system as the weblogic user, then you will have permission issues with files throughout the system. At that point the best solution is to delete the WebLogic installation completely, delete ALL WebLogic directories and restart the installation from scratch.