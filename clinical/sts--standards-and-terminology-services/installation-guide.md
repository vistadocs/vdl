---
title: STS Version 2 VETS 10 Set Up Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: VETS 10 Set Up Guide
app_code: STS
app_name: Standards & Terminology Services
section: CLI
app_status: archive
pkg_ns: STS
patch_ver: 2
patch_id: STS*2
group_key: "STS:STS:2"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - strong
  - class
  - table
  - even
  - contents
  - terminology
  - concept
  - blockquote
  - vets
  - domain
page_count: 0
word_count: 6042
section_count: 15
table_count: 2
figure_count: 0
appendix_count: 4
has_toc: False
is_stub: False
pub_date: December 2010
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/Standards_and_Terminology_Services_Archive/sts_vets_10_setup_guide.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/Standards_and_Terminology_Services_Archive/sts_vets_10_setup_guide.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=402"
---

> Standards & Terminology Services (STS)

> VETS Deployment Services Production Release

> *Set Up Guide*

![](sts-version-2-vets-10-set-up-guide/001.png)

### Version 2.0

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### December 2010

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Department of Veterans Affairs

> Office of Information and Technology (OI&T) Office of Enterprise Development (OED)

> Revision History

| Date   | Version | Description                     | Author                         |
|------------|-------------|-------------------------------------|------------------------------------|
| July 2010  | 0.1         | V9 text uploaded for V10 start.     | <span class="mark">REDACTED</span> |
| Sept. 2010 | 0.2         | Initial changes from Schwann.       | <span class="mark">REDACTED</span> |
| Oct. 2010  | 0.3         | Rewrite text for V10. Edit, format. | <span class="mark">REDACTED</span> |
| Nov. 2010  | 0.4         | Update screen shots, step text.     | <span class="mark">REDACTED</span> |
| Dec. 2010  | 0.5         | Screen shots, validation.           | <span class="mark">REDACTED</span> |
| Dec. 2010  | 0.6         | Sent for Review                     | <span class="mark">REDACTED</span> |
| Dec. 2010  | 1.0         | Final for PDF                       | <span class="mark">REDACTED</span> |

> [Appendix A – WebLogic Server Installation Configuration 34](#appendix-a-weblogic-server-installation-configuration)

> [Appendix B – WebLogic Domain Installation Configuration 34](#appendix-b-weblogic-domain-installation-configuration)

> [Appendix C – Start/Stop and Deploy Scripts 35](#appendix-c-startstop-and-deploy-scripts)

> [Appendix D – STS V10 Detailed Configuration 35](#appendix-d-sts-v10-detailed-configuration)

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

    - [Version 2.0](#version-20)
    - [December 2010](#december-2010)
- [Introduction](#introduction)
- [PreInstallation](#preinstallation)
- [VETS V10 Build and Data Conversion Instructions](#vets-v10-build-and-data-conversion-instructions)
  - [Create VETS V10 Schemas Instructions](#create-vets-v10-schemas-instructions)
  - [Copy VETS V9 Data into the VETS V10 Schemas Instructions](#copy-vets-v9-data-into-the-vets-v10-schemas-instructions)
- [STS VETS Deployment Process](#sts-vets-deployment-process)
  - [Prerequisites](#prerequisites)
  - [Create a Basic Web Logic Domain](#create-a-basic-web-logic-domain)
  - [Create Web Logic Managed Servers](#create-web-logic-managed-servers)
  - [Create JDBC Data Sources](#create-jdbc-data-sources)
  - [Load file s into Web Logic Domain Directories](#load-file-s-into-web-logic-domain-directories)
  - [Create Server Start/Stop and Application Deployment Scripts](#create-server-startstop-and-application-deployment-scripts)
  - [Creating STS Application Users](#creating-sts-application-users)
  - [Con figure and Start Node Manager](#con-figure-and-start-node-manager)
  - [Log Con figuration](#log-con-figuration)
  - [Configure WebLogic for Production Mode](#configure-weblogic-for-production-mode)
  - [Start Managed WebLogic Servers and Deploy Applications](#start-managed-weblogic-servers-and-deploy-applications)
- [Glossary](#glossary)
  - [STS Terminology Glossary](#sts-terminology-glossary)
- [Appendix A – WebLogic Server Installation Configuration](#appendix-a-weblogic-server-installation-configuration)
- [Appendix B – WebLogic Domain Installation Configuration](#appendix-b-weblogic-domain-installation-configuration)
- [Appendix C – Start/Stop and Deploy Scripts](#appendix-c-startstop-and-deploy-scripts)
- [Appendix D – STS V10 Detailed Configuration](#appendix-d-sts-v10-detailed-configuration)
> This manual describes the STS VETS Version 10 Set Up procedures. The procedures include:
- Build and Data Conversion
- STS Deployment
- Copying New Configuration and Help Files
- Starting and Stopping WebLogic Servers
- Creating STS Application User

# PreInstallation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> STS VETS V10 uses an Oracle 11gR1 RAC database server. WebLogic 10.3.2 and Java 6 Update 20 must be installed.

# VETS V10 Build and Data Conversion Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> This section describes the steps you need to perform to create the VETS V10 database schemas and copy the VETS V9 data into the VETS V10 schema. The VETS V9 and V10 schemas can co- exist in the same database while the VETS V10 environment is validated and the VETS V9 environment can be archived.

> These tables list the V9 schema names and their corresponding V10 schema names in the environments that the V10 data creates from a V9 schema.

<table>
<colgroup>
<col style="width: 48%" />
<col style="width: 51%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p><strong>PRODUCTION (HDRP06)</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>V9 SCHEMA NAME</strong></td>
<td><strong>V10 SCHEMA NAME</strong></td>
</tr>
<tr class="even">
<td>DS_V09</td>
<td>DS_V10</td>
</tr>
<tr class="odd">
<td>NTRT_V09</td>
<td>NTRT_V09</td>
</tr>
<tr class="even">
<td>VHAT_V09</td>
<td>No longer used</td>
</tr>
<tr class="odd">
<td>VTS_V09</td>
<td>VTS_V09</td>
</tr>
<tr class="even">
<td>VUID_V09</td>
<td>Moved into VTS_V09 schema</td>
</tr>
</tbody>
</table>

<table>
<colgroup>
<col style="width: 48%" />
<col style="width: 51%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p><strong>SQA (ETSD07 on vhaislbll10)</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>V9 SCHEMA NAME</strong></td>
<td><strong>V10 SCHEMA NAME</strong></td>
</tr>
<tr class="even">
<td>DS_V09</td>
<td>DS_V10</td>
</tr>
</tbody>
</table>

| NTRT_V09 | NTRT_V09                  |
|----------|---------------------------|
| VHAT_V09 | No longer used            |
| VTS_V09  | VTS_V09                   |
| VUID_V09 | Moved into VTS_V09 schema |

<table>
<colgroup>
<col style="width: 48%" />
<col style="width: 51%" />
</colgroup>
<thead>
<tr class="header">
<th colspan="2"><blockquote>
<p><strong>Integration (STSI01 on vhaislbll26)</strong></p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>V8 SCHEMA NAME</strong></td>
<td><strong>V10 SCHEMA NAME</strong></td>
</tr>
<tr class="even">
<td>DS_V09</td>
<td>DS_V10</td>
</tr>
<tr class="odd">
<td>NTRT_V09</td>
<td>NTRT_V09</td>
</tr>
<tr class="even">
<td>VHAT_V09</td>
<td>No longer used</td>
</tr>
<tr class="odd">
<td>VTS_V09</td>
<td>VTS_V09</td>
</tr>
<tr class="even">
<td>VUID_V09</td>
<td>Moved into VTS_V09 schema</td>
</tr>
</tbody>
</table>

## Create VETS V10 Schemas Instructions

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Follow the steps below to create the V10 schemas:

1.  These steps are executed from a PC or UNIX server that has Oracle client installed and tnsnames.ora connection information to the database for the new VETS V10 schema.
2.  Execute the Oracle SQL script. build_v10_releasenumber_full_databasename.sql
    - The releasenumber is the latest database build number for V10.
    - The databasename is the name of the database that the build will be created on.
    - The build_v10_releasenumber_full_databasename.sql file calls other SQL files to build the environment.
    - All parameters needed to create the objects are specified in the

> build_v10_releasenumber_full_databasename.sql file.

3.  Review the script file before the script is executed to ensure that all of the information is correct.
    - All SQL files used in this step are stored in Perforce.
    - The objects that are created by this script can be viewed via this HTML data model contained in the zip file VETS_001009.zip.

Follow the step below to create the VETS V10 data model on a PC:

1.  Unload the zip files into a directory on your computer.

> \<FILE://\\vhaislmul1\Projects\ETS (STS)\VETS\Version 10\Toad Data Modeler\Reports\HTML\VETS_10.zip\>

2.  Open the file DS_NTRT_VTS_V10.html in a browser window to view the data model.

## Copy VETS V9 Data into the VETS V10 Schemas Instructions 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The conversion process below was designed so that the V9 and the V10 data reside in the same database. Follow the steps below to copy V9 data in to the V10 schemas:

1.  Copy the following files into the data_pump_dir directory on the database server:

> changegroup_seq_create.sql checksumrequest_seq_create.sql codesystem_seq_create.sql onceptstate_seq_create.sql concept_seq_create.sql copy_v9_to_v10_database.sh copy_v9_v10_ds.sql

> copy_v9_v10_ds_stsi01.sql (only for database stsi01 & stsi02) copy_v9_v10_ntrt.sql

> copy_v9_v10_vts.sql copy_v9_v10_vuid.sql deploymentconcept_seq_create.sql deploymenthistory_seq_create.sql deployment_seq_create.sql drop_v10_objs.sql grant_select_any_table.sql property_seq_create.sql regionchecksum_seq_create.sql relationship_seq_create.sql request_delete_rows.sql revoke_select_any_table.sql sitedatarequest_seq_create.sql sitedata_seq_create.sql state_seq_create.sql type_seq_create.sql v10_gather_stats_001002.sql

> version_seq_create.sql vhat_v10_cleanup.sql request_subset_update.sql

2.  The following files need to be edited to update the variables with the correct values:

> copy_v9_to_v10_database.sh

3.  Execute the shell script copy_v9_to_v10_database.sh on the database server to copy the data using this command:

> copy_v9_to_v10_database.sh 1\>copy_v9_to_v10_database.log 2\>&1

> This script can be executed against an empty V10 schema, or when data is in the V10 schema and data needs to be reloaded. The main tasks that this script performs are:

- Copies data directly from V9 tables into V10 tables using Insert/Select statements for tables that do not contain LONG RAW data.
- The data in the ds_v10 and vts_v10 schemas are truncated.
- Export/Import V9 NTRT table into a V10 NTRT table because table contains LONG RAW data
- Sets all sequences to correct values
- Sets all object permissions
- Moves indexes to correct tablespace
- Gathers schema statistics for all V10 schema All files used in this step are stored in Perforce.

# STS VETS Deployment Process

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> The STS VETS Deployment Process consists of installing a VETS V10 domain and configuring the scripts.

## Prerequisites 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> All software packages are installed into the base directory /u01/app. A different directory can be used as the base directory. If you use a different directory you need to replace any references to the base directories in this document to the directory you are using.

> All installation commands should run under the WebLogic UNIX system ID. Before installation, run the following command on the target server to make sure it is running Linux on x86_64 hardware. See the following sample output:

> *uname -a*

> Linux vhaislbll25.vha.med.va.gov 2.6.18-194.3.1.el5 \#1 SMP Sun May 2 04:17:42 EDT 2010 x86_64 x86_64 x86_64 GNU/Linux

- Verify /etc/hosts file

> Run the following command to make sure there is a separate line in /etc/hosts that resolves both short hostname and fully qualified domain name to the host IP address.

> *cat /etc/hosts \| grep \`hostname\`*

> <span class="mark">REDACTED</span> <span class="mark">REDACTED</span>

- Install Java 6 Update 20

> Download the Java installer file jdk-6u20-linux-x64.bin from the Java web site*.* Copy the file into the application base directory and make it executable.

> Run the following:

> ./jdk-6u20-linux-x64.bin

> Press the Enter button to progress through the License Agreement pages.

> At the prompt Do you agree to the above license terms? \[yes or no\], select Yes. Press the Enter button to continue.

> Java is installed into the /u01/app/jdk1.6.0_20 directory. The original installer file can be deleted at this point.

> Run the following command to create a symbolic link to the actual java location.

> ln -s jdk1.6.0_20 jdk1.6

- Install WebLogic version 10.3.2

> Download the WebLogic installer file wls1032_generic.jar from the Oracle web site. Copy the file into the application base directory.

> In the same base directory, create a file named wls1032.xml with the content shown in [<u>Appendix A</u>.](#appendix-a-weblogic-server-installation-configuration)

> Run the following command:

> /u01/app/jdk1.6/bin/java -jar wls1032_generic.jar \\

> -mode=silent -silent_xml=wls1032.xml

> The command takes a few minute to run.

> When the command is finished WebLogic is installed into /u01/app/wls1032 and the WebLogic home directory is /u01/app/wls1032/wls.

> The WebLogic installer file can be deleted to free up disk space.

> The following directories are defined for reference throughout this document:

> AppDir=/u01/app JavaHome=/u01/app/jdk1.6 BeaHome=/u01/app/wls1032 WlsHome=/u01/app/wls1032/wls

## Create a Basic Web Logic Domain

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> As WebLogic user ID, set up CLASSPATH by following command: CLASSPATH=/u01/app/wls1032/utils/config/10.3/config-launch.jar CLASSPATH=\$CLASSPATH:/u01/app/wls1032/wls/server/lib/weblogic.jar

> CLASSPATH=\$CLASSPATH:/u01/app/wls1032/modules/features/weblogic.server.modul es_10.3.2.0.jar

> export CLASSPATH

> Create a Python command file named basedomain.py ([<u>Appendix B</u>](#appendix-b-weblogic-domain-installation-configuration)) in the application base directory with the following commands.

> Note: Substitute with appropriate base directory values wherever needed.

> Create a WebLogic domain by running the following command. If it is successful, a new domain directory should be found in /u01/app/domains, e.g. v10.Prod.

> /u01/app/jdk1.6/bin/java weblogic.WLST basedomain.py

> Start the new WebLogic domain with following commands:

> cd /u01/app/domains/v10.Prod

> nohup /u01/app/domains/v10.Prod/bin/startWebLogic.sh & tail -f nohup.out

> The command will take a few minutes to run.

> Note: Your Username and Password are created when you run the command.

> Log in to the WebLogic Administration Console using the Administration Username and Password created in the basedomain.py script.

## Create Web Logic Managed Servers

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To create the WebLogic managed servers:

1.  Log in to the WebLogic Administration Console. Enter Username WebLogic and Password

> REDACTED.

> Following is a list of the managed servers you want to create:

<table>
<colgroup>
<col style="width: 50%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th>Name</th>
<th><blockquote>
<p>Listen Port</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>deployment</td>
<td><blockquote>
<p>7201</p>
</blockquote></td>
</tr>
<tr class="even">
<td>ntrt</td>
<td><blockquote>
<p>7202</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>vuid</td>
<td><blockquote>
<p>7203</p>
</blockquote></td>
</tr>
<tr class="even">
<td>browser</td>
<td><blockquote>
<p>7204</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>ted</td>
<td><blockquote>
<p>7208</p>
</blockquote></td>
</tr>
</tbody>
</table>

2.  In the Domain Structure box, expand Environment.
3.  Click and open Servers.
4.  ![](sts-version-2-vets-10-set-up-guide/002.png)In the Summary of Servers box, click the Configuration tab.
5.  Click the New button at the bottom of the Configuration box.
6.  In the Create a New Server box, complete the required fields (\* Indicates required fields) with the information for the first managed server you want to create.

> This example uses the first server listed under step 1, above.

> ![](sts-version-2-vets-10-set-up-guide/003.png)

7.  Complete the Server Listen Address field.

> The Server Listen Address is the IP address of the WebLogic host server.

8.  Leave the No, this is a stand-alone server. option selected.
9.  Click the Finish button.

> ![](sts-version-2-vets-10-set-up-guide/004.png)

10. In the Servers box, click the name (link) of the newly created server.
11. ![](sts-version-2-vets-10-set-up-guide/005.png)In the Machine pull down menu, choose the machine name where this server should reside.
12. Click the Save button.
13. Click the Server Start tab.
14. Complete the following fields with the correct information.

> Java Home: /u01/app/jdk1.6

#### Java Vendor: Sun

> BEA Home: /u01/app/wls1032

> Root Directory: /u01/app/domains/v10.prod

#### Classpath:

> /u01/app/domains/v10.prod/lib/antlr- 2.7.6.jar:/u01/app/wls1032/wls/server/lib/weblogic.jar:/u01/app/domains/v10.prod/sts. config

#### Arguments:

> REDACTED

> User Name: WebLogic Passwords: REDACTED

> Confirmed Passwords: REDACTED

> ![](sts-version-2-vets-10-set-up-guide/006.png)

15. Click the Save button.
16. Repeat the above steps to create the other managed servers.

## Create JDBC Data Sources 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Follow the steps below to create JDBC data sources:

1.  Log in to the WebLogic Administration Console. Enter Username WebLogic and Password

> REDACTED

> Following is a list of the data sources you want to create:

<table>
<colgroup>
<col style="width: 22%" />
<col style="width: 55%" />
<col style="width: 22%" />
</colgroup>
<thead>
<tr class="header">
<th>Name</th>
<th><blockquote>
<p>JNDI Name</p>
</blockquote></th>
<th><blockquote>
<p>Targets</p>
</blockquote></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Deployment</td>
<td><blockquote>
<p>jdbc/gov.va.med.term.deployment</p>
</blockquote></td>
<td><blockquote>
<p>deployment</p>
</blockquote></td>
</tr>
<tr class="even">
<td>NTRT</td>
<td><blockquote>
<p>jdbc/gov.va.med.term.ntrt</p>
</blockquote></td>
<td><blockquote>
<p>ntrt</p>
</blockquote></td>
</tr>
<tr class="odd">
<td>VETS</td>
<td><blockquote>
<p>jdbc/gov.va.med.term.services</p>
</blockquote></td>
<td><blockquote>
<p>browser, ntrt,</p>
<p>ted, vuid</p>
</blockquote></td>
</tr>
</tbody>
</table>

2.  In the Domain Structure box, expand Services.
3.  Expand JDBC.
4.  ![](sts-version-2-vets-10-set-up-guide/007.png)Click and open Data Sources.
5.  In the Summary of JDBC Data Sources box, click the New button.
6.  Complete the Name and JNDI Name fields.

> ![](sts-version-2-vets-10-set-up-guide/008.png)This example uses the first data source under step 1, above.

7.  Click the Next button.
8.  Click the Next button on the following page.
9.  Complete the Connections Properties page.

> ![](sts-version-2-vets-10-set-up-guide/009.png)

10. Click the Next button.
11. In the Select Targets box, select the Server where this data source will be deployed.
12. Click the Finish button.
13. Repeat these steps to create the other data sources.

## Load file s into Web Logic Domain Directories 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Run the following commands to create several new directories under the domain directory.

> cd /u01/app/domains/v10.prod

> mkdir apps checksum sts.config sts.log

2.  Copy the files listed in each of the following directories, from the build .WAR files and source repository.

> Note: For any update to application.properties or terminologyconfig.xml, sts.deployment

> should be restarted.

> apps/ntrt.war apps/sts.browser.war apps/sts.deployment.war apps/sts.ted.war

> apps/vuid.war lib/antlr-2.7.6.jar lib/log4j-1.2.14.jar lib/loglayout.jar

> sts.config/application.properties sts.config/BrowserConfig.xml sts.config/browserhelp.html sts.config/browserIntro.html sts.config/deploymenthelp.html sts.config/log4j.properties sts.config/ntrtdeployhistory.html sts.config/tedhelp.html sts.config/TerminologyConfig.xml

3.  Edit the application.properties file.

> Ensure all variables are appropriate for the target environment, particularly the following variables.

> application.server.name=PROD V10 listenerPort = 49990 msh.sendingFacility.namespaceId=660VM1

> gov.va.med.term.access.maint.messaging.hl7.factory.BusinessWareMessageDispatcher/ url=http://vhaislviev1:8080/fwclient2/Framework2ServletHTTPtoChannel

## Create Server Start/Stop and Application Deployment Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  For each managed server create start, stop, and bounce scripts in

> /u01/app/domains/v10.prod/bin directory.

> Examples of the scripts are shown in [<u>Appendix C</u>.](#appendix-c-startstop-and-deploy-scripts) For a different server, make sure all variables are changed accordingly.

2.  Create a master deploy script in the same domain bin directory. See [<u>Appendix C</u>.](#appendix-c-startstop-and-deploy-scripts)
3.  Run chmod u+x … on all above scripts to make sure that they are executable.
4.  Run the following commands to store user credentials referenced from the above scripts.

> cd /u01/app/domains/v10.prod/bin mkdir .security

> export CLASSPATH=\$CLASSPATH:/u01/app/wls1032/wls/server/lib/weblogic.jar echo y \| /u01/app/jdk1.6/bin/java -Duser.home=.security \\

> weblogic.Admin STOREUSERCONFIG -username WebLogic -password REDACTED chmod 700 .security

> chmod 400 .security/\*

## Creating STS Application Users

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To create STS Application Users:

1.  Log in to the WebLogic Administration Console. Enter Username WebLogic and Password

> REDACTED.

> Following is the group and user you want to create.

> Group: DSAdmin

> User: sts.admin

2.  In the Domain Structure box, click Security Realms.
3.  In the Summary of Security Realms box, click myrealm.

> ![](sts-version-2-vets-10-set-up-guide/010.png)

4.  Click the Users and Groups tab.
5.  ![](sts-version-2-vets-10-set-up-guide/011.png)Click the Groups tab.
6.  Click the New button.
7.  ![](sts-version-2-vets-10-set-up-guide/012.png)Complete the Name and Description fields.
8.  Click the OK button.
9.  On the Users and Groups page, click the Users tab.
10. Click the New button.
11. Complete the Name, Description, and Password fields.

> ![](sts-version-2-vets-10-set-up-guide/013.png)

12. Click the OK button.
13. Click on the name of the newly created user.
14. ![](sts-version-2-vets-10-set-up-guide/014.png)Click the Groups tab.
15. Select the Group you created in the previous steps.
16. Click the \> button to move that Group into the Chosen field.
17. Click the Save button.
18. Repeat these steps to create other users.

## Con figure and Start Node Manager

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To configure the node manager:

1.  Log in to the WebLogic Administration Console. Enter Username WebLogic and Password

> REDACTED.

2.  In the Domain Structure box, expand Environment.
3.  Click the Machines link.
4.  ![](sts-version-2-vets-10-set-up-guide/015.png)In the Summary of Machines box, click the machine name.
5.  Click the Node Manager tab.
6.  Complete the fields.

> ![](sts-version-2-vets-10-set-up-guide/016.png)

7.  Click the Save button.

> If the default listen port is not available on the server, change it to an available number.

8.  Open a terminal console and run the following commands to start the node manager. cd /u01/app/wls1032/wls/server/bin

> nohup /u01/app/wls1032/wls/server/bin/startNodeManager.sh &

> tail -f nohup.out

9.  If the default port 5556 is not used, edit the following file to update ListenPort with the same number configured in the Administration Console.

> /u01/app/wls1032/wls/common/nodemanager/nodemanager.properties

10. Kill and restart the node manager to pick up any change.

## Log Con figuration 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To configure the WebLogic server logs:

1.  Run the following commands in a terminal console to create a directory to hold all WebLogic server logs.

> cd /u01/app/domains mkdir logs

2.  Log in to the WebLogic Administration Console. Enter Username WebLogic and Password

> REDACTED.

3.  In the Domain Structure box, expand Environments.
4.  ![](sts-version-2-vets-10-set-up-guide/017.png)Click Servers.
5.  Click the admin server name.
6.  Click the Logging tab.

> ![](sts-version-2-vets-10-set-up-guide/018.png)

7.  Click the General tab.
8.  Change the Log file name to use the newly created log directory.
9.  In the Rotation type pull down menu, select By Time.
10. Uncheck Limit number of retained files.
11. Uncheck Rotate log file on startup.
12. Click the Save button.

> ![](sts-version-2-vets-10-set-up-guide/019.png)

13. Click the HTTP tab.
14. Change the Log file name to use the newly created log directory.
15. In the Rotation type pull down menu, select By Time.
16. Uncheck Limit number of retained files.
17. Uncheck Rotate log file on startup.
18. Click the Save button.
19. Repeat the above steps for all managed servers.

## Configure WebLogic for Production Mode 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To configure WebLogic for Production mode:

1.  Log in to the WebLogic Administration Console. Enter Username WebLogic and Password

> REDACTED.

2.  In the Domain Structures box, click the domain name.
3.  Click the General tab.
4.  Select the box for Production Mode.

> ![](sts-version-2-vets-10-set-up-guide/020.png)

5.  Click the Save button.

## Start Managed WebLogic Servers and Deploy Applications

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> To start the managed servers and deploy the applications:

1.  Log in to the WebLogic Administration Console. Enter Username WebLogic and Password

> REDACTED.

2.  In the Domain Structure box, expand Environment.
3.  Click Servers.

> <span id="_bookmark17" class="anchor"></span>![](sts-version-2-vets-10-set-up-guide/021.png)

4.  In the Summary of Servers box, click the Control tab.
5.  Check the box by the server name.
6.  Click the Start button.
7.  Run the following commands in a terminal console.

> cd /u01/app/domains/v10.prod/bin

> ./all_deploy.sh

# Glossary

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## STS Terminology Glossary

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
<li><p>A syntactically and semantically structured aggregation of vocabulary or other data that is the basic unit of clinical information. See also: template</p></li>
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
<td><strong>candidate version</strong></td>
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
<td>An identifiable item in the main body of SNOMED CT or in an authorized extension. Components include: concepts, descriptions, relationships, subsets, histories, and extensions.</td>
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
<td>Concept to concept linking is when one concept is explicitly associated with another concept. Types of concept to concept linking are the creation of Map Sets, Translation Services, and Pre and Post Coordinated terms.</td>
</tr>
<tr class="even">
<td><strong>context</strong></td>
<td><p>A context can be:</p>
<ol type="1">
<li><p>The environment in which it is appropriate to display a specific designation for a concept.</p></li>
<li><p>A specified part or field of a patient record, application, protocol, query, or communication in SNOMED CT.</p></li>
</ol></td>
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
<td><strong>data cleanup</strong></td>
<td>Activities that are taken to correct, normalize, and eliminate terms from a reference file before it is matched to a new standard. See also: standardization.</td>
</tr>
<tr class="even">
<td><strong>data model</strong></td>
<td>A schema that describes the way data is represented.</td>
</tr>
<tr class="odd">
<td><strong>data standardization</strong></td>
<td>The process of defining, creating, deploying, and maintaining a common terminology resource.</td>
</tr>
<tr class="even">
<td><strong>datatype</strong></td>
<td>A data storage format that can contain a specific type or range of values.</td>
</tr>
<tr class="odd">
<td><strong>deploy</strong></td>
<td><p>Deploy means:</p>
<ol type="1">
<li><p>Within general software development, to send electronically as a unit.</p></li>
<li><p>Within STS, to publish terminology content from the development to production environments.</p></li>
</ol></td>
</tr>
<tr class="even">
<td><strong>deployment</strong></td>
<td><p>A deployment is:</p>
<ol type="1">
<li><p>The process of publishing terminology content from the development environment to the production environment.</p></li>
<li><p>Groups of concepts that are ready to be tested and potentially added to the terminology.</p></li>
</ol></td>
</tr>
<tr class="odd">
<td><strong>description</strong></td>
<td>The text that represents a concept in human readable form. See also: designation (preferred).</td>
</tr>
<tr class="even">
<td><strong>designation</strong></td>
<td>A representation of a concept. See also: description, display form, expression, surface form, term</td>
</tr>
<tr class="odd">
<td><strong>development environment</strong></td>
<td>All the software and hardware components needed to create or edit a terminology. See also: authoring.</td>
</tr>
<tr class="even">
<td><strong>display form</strong></td>
<td>A representation of a concept. See also: designation (preferred), description, expression, surface form, term.</td>
</tr>
<tr class="odd">
<td><strong>domain</strong></td>
<td><p>A domain is:</p>
<ol type="1">
<li><p>A specialized discipline of medicine.</p></li>
<li><p>A set of terms belonging to a specialized discipline of medicine.</p></li>
<li><p>A set of terms associated within a VistA application.</p></li>
</ol></td>
</tr>
<tr class="even">
<td><strong>entity relationship model</strong></td>
<td>A graphical representation of work or information flow. Consists of entities (things), attributes (data), and relationships (connections between entities). Often used to model basic work or information flow. See also: information model, terminology model.</td>
</tr>
<tr class="odd">
<td><strong>Enterprise Terminology Services (ETS)</strong></td>
<td>The term ETS is no longer used. This team is now referred to as Standardization and Terminology Services (STS).</td>
</tr>
<tr class="even">
<td><strong>expression</strong></td>
<td>Human readable representation of a concept or the name of a concept. See also: designation (preferred), description, surface form.</td>
</tr>
<tr class="odd">
<td><strong>finalized version</strong></td>
<td>TDS content that has passed SQA testing and is sent to production sites for field use.</td>
</tr>
<tr class="even">
<td><strong>Health Data Repository (HDR)</strong></td>
<td>The HDR is a repository of clinical information normally residing on one or more independent platforms for use by clinicians and other personnel in support of patient- centric care.</td>
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
<td><strong>International Classification of Diseases – 9<sup>th</sup> edition – Clinical Modification (ICD- 9-CM)</strong></td>
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
<td>A structured specification, expressed graphically and/or narratively, of the information requirements of a domain. An information model describes the required classes of information and the properties of those classes, optionally including attributes, relationships, and other essential information. See also: entity relationship model, terminology model</td>
</tr>
<tr class="odd">
<td><strong>lexicon</strong></td>
<td><p>A lexicon is:</p>
<ol type="1">
<li><p>The vocabulary of a language. See: terminology.</p></li>
<li><p>Commonly used to refer to VistA’s Lexicon Utility.</p></li>
</ol></td>
</tr>
<tr class="even">
<td><strong>Logical Observation Identifiers, Names, And Codes (LOINC)</strong></td>
<td>The LOINC database provides a set of universal names and ID codes for identifying laboratory and clinical observations. LOINC codes are used to facilitate the exchange and pooling of clinical laboratory results, such as blood hemoglobin or serum potassium, for clinical care, outcomes management, and research.</td>
</tr>
<tr class="odd">
<td><strong>map entry</strong></td>
<td>The link between concepts from a source code system to one or more concepts from a target code system. Map entries may be from two standard code systems or from within the same code system. A map entry is an instance of the data in a map set.</td>
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
<td>A system of names and groupings, which is structured according to pre-established naming rules. See also: classification, taxonomy</td>
</tr>
<tr class="odd">
<td><strong>non-domain</strong></td>
<td>Content that is not part of a clinical domain.</td>
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
<td><strong>non-VistA</strong></td>
<td>Content that is not deployed to VistA.</td>
</tr>
<tr class="even">
<td><strong>normalization</strong></td>
<td>The process of identifying lexical variations of concepts that may include identification of synonyms.</td>
</tr>
<tr class="odd">
<td><strong>ontology</strong></td>
<td><p>Ontology is:</p>
<ol type="1">
<li><p>An explicit formal specification of how to represent the objects, concepts, and other entities that are assumed to exist in some area of interest and the relationships that hold among them. See also: terminology</p></li>
<li><p>All terms in a domain including the relationships among them.</p></li>
</ol></td>
</tr>
<tr class="even">
<td><strong>parent</strong></td>
<td>The supertype in a parent-child relationship. The child (subtype) is narrower and more specific while the parent (supertype) is broader and more general. The child inherits the characteristics of the parent.</td>
</tr>
<tr class="odd">
<td><strong>partial deployment</strong></td>
<td>Deploying one or more subsets within a Version instead of deploying the entire Version.</td>
</tr>
<tr class="even">
<td><strong>post-coordination</strong></td>
<td>The representation of a complex concept as a combination of two or more concepts. See also: pre-coordination.</td>
</tr>
<tr class="odd">
<td><strong>pre-coordination</strong></td>
<td>The representation of a complex concept as a single concept. See also: post-coordination.</td>
</tr>
<tr class="even">
<td><strong>preferred term</strong></td>
<td>The preferred human readable representation of a concept or the preferred name of a concept. Often used as the default display form of a concept. Synonyms: preferred designation, preferred expression.</td>
</tr>
<tr class="odd">
<td><strong>production environment</strong></td>
<td>The software and hardware that is used by end users, as opposed to developers and testers, to access terminology services in the VHA enterprise.</td>
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
<li><p>A comprehensive, consistent, and logically organized set of concepts that is designed to completely embody the expressive detail of a given domain, supported by a set of relationships that defines the elements within the domain and shows how their meanings relate to each other.</p></li>
<li><p>A controlled medical vocabulary intended for use as a reference to enable storage, retrieval, and analysis of clinical data.</p></li>
</ol></td>
</tr>
<tr class="even">
<td><strong>relationship</strong></td>
<td>An association between concepts. See also: semantics, semantic relationship.</td>
</tr>
<tr class="odd">
<td><strong>Standards Development Organization (SDO)</strong></td>
<td>Any entity whose primary activities are developing and maintaining standards that address the interests of a wide base of users outside the standards development organization</td>
</tr>
<tr class="even">
<td><strong>semantics</strong></td>
<td>The meanings assigned to terminology content. See also: semantic relationship.</td>
</tr>
<tr class="odd">
<td><strong>semantic relationship</strong></td>
<td>An association between two concepts that has a specific meaning.</td>
</tr>
<tr class="even">
<td><strong>service oriented architecture (SOA)</strong></td>
<td>The VistA architecture is an SOA whereby applications that provide functionality for use by other applications are created as a service that conforms to a set of VHA standardized design patterns.</td>
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
<td><strong>Systemized Nomenclature of Medicine (SNOMED) Clinical Terms (CT)</strong></td>
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
<li><p>A structured aggregation of one or more archetypes, with optional order, to represent clinical data. An HL7 template is a data structure, based on the HL7 RIM that expresses the data content that is needed in a specific clinical or administrative context. Templates are drawn from the RIM and make use of HL7 vocabulary domains. Templates are also described as constraints on HL7 artifacts.</p></li>
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
<tr class="even">
<td><strong>terminology deployment services</strong></td>
<td>Central distribution point for all terminology services. Updates are uploaded to the terminology deployment server, which in turn distributes them to targeted VistA sites.</td>
</tr>
<tr class="odd">
<td><strong>terminology model</strong></td>
<td>A terminology model provides a consistent structure and specifies the formal representation of a concept. The STS terminology model comprises of components such as concepts, designations, properties, and relationships. Other components of the STS terminology model include Subsets and Concept to Concept linking.</td>
</tr>
<tr class="even">
<td><strong>terminology server</strong></td>
<td>The software application and hardware that provide access to terminology content through a published set of API.</td>
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
<td><strong>test environment</strong></td>
<td>The software and hardware that is used by developers and testers as opposed to end users to test terminology services in the VHA enterprise.</td>
</tr>
<tr class="even">
<td><strong>translation</strong></td>
<td>After two terminologies have been mapped, a translation between the two is possible.</td>
</tr>
<tr class="odd">
<td><p><strong>Unified Medical Language System (UMLS)</strong></p>
<p><strong>Metathesaurus</strong></p></td>
<td>The UMLS Metathesaurus is a very large, multi-purpose, and multi-lingual vocabulary database that contains information about biomedical and health related concepts, their various names, and the relationships among them. It reflects and preserves the meanings, concept names, and relationships from its source vocabularies. It also supplies information that computer programs can use to create standard data, interpret user inquiries, interact with users to refine their questions, and convert the users' terms into the vocabulary used in relevant information sources.</td>
</tr>
<tr class="even">
<td><strong>value</strong></td>
<td>A quantitative or qualitative state that is assigned to a property.</td>
</tr>
<tr class="odd">
<td><strong>value domain</strong></td>
<td>All allowable values for a terminology, datatype, or value set. May be an infinite set of values.</td>
</tr>
<tr class="even">
<td><strong>value set</strong></td>
<td>A finite set of allowable values. Typically, a value set has a small number of values. If it has a large number of values, it may be a terminology.</td>
</tr>
<tr class="odd">
<td><strong>version</strong></td>
<td><p>A version is:</p>
<ol type="1">
<li><p>Formal changes in a terminology. May be used to find and track inactivated codes, determine the current code set, or track the history of a concept.</p></li>
<li><p>Also applies to formal revisions in computer code or programs.</p></li>
<li><p>An STS deployment that has passed internal testing. Can refer to a Candidate Version or a Finalized Version.</p></li>
</ol></td>
</tr>
<tr class="even">
<td><strong>Veterans Health Administration (VHA) Enterprise Terminology Services (VETS)</strong></td>
<td>VETS focuses on requirements for the deployment of and runtime access to terminology content in ERT for all VHA clinical applications.</td>
</tr>
<tr class="odd">
<td><strong>VHA Terminology (VHAT)</strong></td>
<td>VHAT is the terminology that is created and maintained by STS.</td>
</tr>
<tr class="even">
<td><strong>Veterans Health Information Systems and Technology Architecture (VistA)</strong></td>
<td>VistA is a term used to describe the VA’s health care information system. It encompasses in-house developed applications developed by VA staff, office automation applications, locally developed applications, and commercial-off-the-shelf applications.</td>
</tr>
<tr class="odd">
<td><strong>vocabulary</strong></td>
<td>A list of words or phrases with their meanings. See also: terminology.</td>
</tr>
<tr class="even">
<td><strong>Web Services Description Language (WSDL)</strong></td>
<td>WSDL is an XML-based language that provides a model for describing Web services. The meaning of the acronym has changed from version 1.2 where the D meant Definition.</td>
</tr>
</tbody>
</table>

# Appendix A – WebLogic Server Installation Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> File wls1032.xml content:

> \<?xml version="1.0" encoding="UTF-8"?\>

> \<bea-installer\>

> \<input-fields\>

> \<data-value name="BEAHOME" value="/u01/app/wls1032"/\>

> \<data-value name="WLS_INSTALL_DIR" value="/u01/app/wls1032/wls"/\>

> \<data-value name="COMPONENT_PATHS" value="WebLogic Server/Core Application Server\|WebLogic Server/Administration Console\|WebLogic Server/Configuration Wizard and Upgrade Framework\|WebLogic Server/WebLogic Web Server Plugins\|WebLogic Server/UDDI and Xquery Support"/\>

> \<data-value name="LOCAL_JVMS" value="/u01/app/jdk1.6"/\>

> \</input-fields\>

> \</bea-installer\>

# Appendix B – WebLogic Domain Installation Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> File basedomain.py content: readTemplate('/u01/app/wls1032/wls/common/templates/domains/wls.jar') create ('vhaislbll25.vha.med.va.gov','Machine')

> set('AdminServerName', ‘admin.v10.Prod’) cd('/Server/AdminServer')

> set('Name', ‘admin.v10.Prod’)

> cd('/Server/'+’admin.v10.Prod’) set('ListenAddress', '<span class="mark">REDACTED</span>0')

> set('ListenPort', <span class="mark">REDACTED</span>)

> cd('/Security/base_domain/User/weblogic') set('Name','weblogic') cd('/Security/base_domain/User/'+'weblogic') cmo.setPassword('REDACTED')

> writeDomain('/u01/app/domains/v10.Prod') closeTemplate()

# Appendix C – Start/Stop and Deploy Scripts

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> Script start_sts.deployment.sh content

> echo Starting weblogic server v10.deployment ...

> /u01/app/domains/v10.prod/bin/nodemanager/wlscontrol.sh \\

> -d v10.prod \\

> -r /u01/app/domains/v10.prod \\

> -s v10.deployment START

> Script stop_sts.deployment.sh content

> /u01/app/domains/v10.prod/bin/nodemanager/wlscontrol.sh \\

> -d v10.prod \\

> -r /u01/app/domains/v10.prod \\

> -s v10.deployment KILL

> Script bounce_sts.deployment.sh content

> /u01/app/domains/v10.prod/bin/stop_sts.deployment.sh sleep 30

> /u01/app/domains/v10.prod/bin/start_sts.deployment.sh Script deploy_sts.deployment.sh content

> cd /u01/app/domains/v10.prod/bin

> . /u01/app/wls1032/wls/server/bin/setWLSEnv.sh

> /u01/app/jdk1.6/bin/java -Duser.home=.security \\

> weblogic.Deployer -adminurl t3://10.5.20.180:7200 -stop -name sts.deployment

> /u01/app/jdk1.6/bin/java -Duser.home=.security \\

> weblogic.Deployer -adminurl t3://10.5.20.180:7200 -undeploy -name sts.deployment

> ./bounce_sts.deployment.sh

> /u01/app/jdk1.6/bin/java -Duser.home=.security \\

> weblogic.Deployer -adminurl t3://10.5.20.180:7200 -deploy -name sts.deployment \\

> -source /u01/app/domains/v10.prod/apps/sts.deployment.war \\

> -targets v10.deployment -nostage Script all_deploy.sh content

> /u01/app/domains/v10.prod/bin/deploy_sts.deployment.sh

> /u01/app/domains/v10.prod/bin/deploy_sts.browser.sh

> /u01/app/domains/v10.prod/bin/deploy_ntrt.sh

> /u01/app/domains/v10.prod/bin/deploy_sts.ted.sh

> /u01/app/domains/v10.prod/bin/deploy_vuid.sh

# Appendix D – STS V10 Detailed Configuration

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

> \[Host\] Name=vhaislbll25

> Domain=.vha.med.va.gov FQDN=%(Name)s%(Domain)s

> IP=10.5.20.180

> AppDir=/u01/app JavaHome=%(AppDir)s/jdk1.6 BeaHome=%(AppDir)s/wls1032 WlsHome=%(BeaHome)s/wls WlsInstaller=wls1032_generic.jar

> \[Domain\] Tag=v10

> BaseDir=@@Host_AppDir@@/domains Name=%(Tag)s.prod Home=%(BaseDir)s/%(Name)s PortGroup=72

> Serial=0 ProductionModeEnabled=true

> \[NodeManager\] ListenPort=5556

> \[AdminServer\] Serial=00

> Name=admin.@@Domain_Name@@ ListenAddress=@@Host_IP@@ ListenPort=@@Domain_PortGroup@@00 SSL_ListenPort=@@Domain_PortGroup@@99 AdministrationPort=@@Domain_PortGroup@@88 Url=t3://@@Host_IP@@:%(ListenPort)s SSL_Url=t3s://@@Host_IP@@:%(AdministrationPort)s

> Start_Arg= REDACTED

> \[User\] Admin_Name=weblogic Admin_Pass=REDACTED App_Group=DSAdmin App_Users=sts.admin App_User_Pswd_Char=

> \[ManagedServer\] SerialList=01,02,03,04,05

> Start_ArgMem= REDACTED

> Xverify:none

> Start_JavaHome=@@Host_JavaHome@@ Start_JavaVendor=Sun Start_BeaHome=@@Host_BeaHome@@ Start_RootDirectory=@@Domain_Home@@ Start_Username=@@User_Admin_Name@@ Start_Password=@@User_Admin_Pass@@ Start_ClassPath_A=%(Start_RootDirectory)s/lib/antlr-2.7.6.jar

> Start_ClassPath_B=@@Host_WlsHome@@/server/lib/weblogic.jar Start_ClassPath_C=%(Start_RootDirectory)s/sts.config \[\[need create dir\]\] Start_ClassPath=%(Start_ClassPath_A)s:%(Start_ClassPath_B)s:%(Start_ClassPath_C)s

> Name01=deployment ListenAddress01=@@Host_IP@@ ListenPort01=@@Domain_PortGroup@@01 SSL_ListenPort01=@@Domain_PortGroup@@11 AdministrationPort01=@@Domain_PortGroup@@21 Machine01=@@Host_FQDN@@ Url01=t3://@@Host_IP@@:%(ListenPort01)s

> Start_ArgMem01= REDACTED

> Start_Arg01=%(Start_ArgMem01)s -Dcds.jndi.provider.url=%(Url01)s

> Name02=browser ListenAddress02=@@Host_IP@@ ListenPort02=@@Domain_PortGroup@@04 SSL_ListenPort02=@@Domain_PortGroup@@14

> AdministrationPort02=@@Domain_PortGroup@@24 Machine02=@@Host_FQDN@@ Url02=t3://@@Host_IP@@:%(ListenPort02)s Start_Arg02=%(Start_ArgMem)s -Dcds.jndi.provider.url=%(Url02)s

> Name03=ntrt ListenAddress03=@@Host_IP@@ ListenPort03=@@Domain_PortGroup@@02

> SSL_ListenPort03=@@Domain_PortGroup@@12 AdministrationPort03=@@Domain_PortGroup@@22 Machine03=@@Host_FQDN@@ Url03=t3://@@Host_IP@@:%(ListenPort03)s Start_Arg03=%(Start_ArgMem)s -Dcds.jndi.provider.url=%(Url03)s

> Name04=ted ListenAddress04=@@Host_IP@@ ListenPort04=@@Domain_PortGroup@@08

> SSL_ListenPort04=@@Domain_PortGroup@@18 AdministrationPort04=@@Domain_PortGroup@@28 Machine04=@@Host_FQDN@@ Url04=t3://@@Host_IP@@:%(ListenPort04)s Start_Arg04=%(Start_ArgMem)s -Dcds.jndi.provider.url=%(Url04)s

> Name05=vuid ListenAddress05=@@Host_IP@@ ListenPort05=@@Domain_PortGroup@@03

> SSL_ListenPort05=@@Domain_PortGroup@@13 AdministrationPort05=@@Domain_PortGroup@@23 Machine05=@@Host_FQDN@@ Url05=t3://@@Host_IP@@:%(ListenPort05)s Start_Arg05=%(Start_ArgMem)s -Dcds.jndi.provider.url=%(Url05)s

> \[JDBC\]

> SerialList=01,02,03 Url=jdbc:oracle:thin:@vhaislbll25.vha.med.va.gov:1521:stsd01 DriverName=oracle.jdbc.OracleDriver KeepXaConnTillTxComplete=

> XaEndOnlyOnce=true XaSetTransactionTimeout=true

> XaRetryDurationSeconds=300 XaTransactionTimeout=120 InitialCapacity=1 CapacityIncrement=1 MaxCapacity=15 TestConnectionsOnReserve=true

> TestTableName=SQL SELECT 1 FROM DUAL GlobalTransactionsProtocol=TwoPhaseCommit

> Name01=Deployment User01=ds\_@@Domain_Tag@@ Password=.........

> Password_Key01=c2s106 JNDINames01=jdbc/gov.va.med.term.deployment Target01=@@ManagedServer_Name01@@

> Name02=VETS

> User02=vts\_@@Domain_Tag@@ Password=.........

> Password_Key02=c2s92 JNDINames02=jdbc/gov.va.med.term.services

> Target02=@@ManagedServer_Name01@@,@@ManagedServer_Name02@@,\\ @@ManagedServer_Name03@@,@@ManagedServer_Name04@@,\\ @@ManagedServer_Name05@@

> Name03=NTRT

> User03=ntrt\_@@Domain_Tag@@ Password=.........

> Password_Key03=c2s145 JNDINames03=jdbc/gov.va.med.term.ntrt Target03=@@ManagedServer_Name03@@ GlobalTransactionsProtocol03=OnePhaseCommit

> \[Log\] BaseDir=@@Domain_BaseDir@@/logs RotationType=byTime NumberOfFilesLimited=false RotateLogOnStartup=false