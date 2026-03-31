---
title: XM*8*25 TCP/IP Service for Mailman
doc_type: TM
doc_label: Technical Manual
doc_layer: patch
doc_subject: TCP/IP Service for Mailman
app_code: XM
app_name: MailMan
section: INF
app_status: active
pkg_ns: XM
patch_ver: 8
patch_id: XM*8*25
group_key: "XM:XM:8"
file_numbers: []
security_keys: []
menu_options: 0
description: 
audience: 
keywords: 
  - service
  - xminet
  - cache
  - account
  - namespace
  - steps
  - mailman
  - create
  - node
  - sites
page_count: 0
word_count: 6319
section_count: 7
table_count: 0
figure_count: 0
appendix_count: 4
has_toc: False
is_stub: False
pub_date: March 2005
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Mailman/tcpip_service_for_mailman.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Mailman/tcpip_service_for_mailman.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=15"
---

![](xm-8-25-tcp-ip-service-for-mailman/001.png)

SupplEmental Instructions forPATCH XM\*8\*25

March 2005

V*IST*A Maintenance Project Product Line

Table of Contents

Introduction [1](#introduction)

Preliminary Steps [3](#preliminary-steps)

Overview of the Steps in this Section [3](#overview-of-the-steps-in-this-section)

The Preliminary Steps [4](#the-preliminary-steps)

Section 1 – Steps for sites that were VMS/DSM and are now VMS/CACHE [7](#section-1-steps-for-sites-that-were-vmsdsm-and-are-now-vmscache)

Overview of the Steps in this Section [7](#overview-of-the-steps-in-this-section-1)

The Steps for sites that were VMS/DSM and are now VMS/CACHE [8](#the-steps-for-sites-that-were-vmsdsm-and-are-now-vmscache)

Section 2 – Steps for sites that were NT/CACHE and are now VMS/CACHE [29](#section-2-steps-for-sites-that-were-ntcache-and-are-now-vmscache)

Overview of the Steps in this Section [29](#overview-of-the-steps-in-this-section-2)

The Steps for sites that were NT/CACHE and are now VMS/CACHE [30](#the-steps-for-sites-that-were-ntcache-and-are-now-vmscache)

Appendix A -- Copies of what the VMS User Account and Service look like [47](#appendix-a----copies-of-what-the-vms-user-account-and-service-look-like)

Appendix B -- Copy of the .com file to create the XMINET VMS User account [49](#appendix-b----copy-of-the-.com-file-to-create-the-xminet-vms-user-account)

Appendix C -- Copy of the .com file to create the TCP/IP Service [53](#appendix-c----copy-of-the-.com-file-to-create-the-tcpip-service)

Appendix D -- Copy of the .com file used by the Service [55](#appendix-d----copy-of-the-.com-file-used-by-the-service)

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
- [# # Preliminary Steps](#preliminary-steps)
  - [Overview of the Steps in this Section](#overview-of-the-steps-in-this-section)
  - [The Preliminary Steps](#the-preliminary-steps)
- [# Section 1 – Steps for sites that were VMS/DSM and are now VMS/CACHE](#section-1-steps-for-sites-that-were-vmsdsm-and-are-now-vmscache)
  - [Overview of the Steps in this Section](#overview-of-the-steps-in-this-section-1)
  - [The Steps for sites that were VMS/DSM and are now VMS/CACHE](#the-steps-for-sites-that-were-vmsdsm-and-are-now-vmscache)
- [Section 2 – Steps for sites that were NT/CACHE and are now VMS/CACHE](#section-2-steps-for-sites-that-were-ntcache-and-are-now-vmscache)
- [The instructions below are for sites that were NT/CACHE and are now VMS/CACHE. These sites had no pre-existing TCP/IP service for MailMan and ran the Mail Listener inside CACHE by jobbing the ^XMRONT routine manually or via the ^ZSTU routine.](#the-instructions-below-are-for-sites-that-were-ntcache-and-are-now-vmscache-these-sites-had-no-pre-existing-tcpip-service-for-mailman-and-ran-the-mail-listener-inside-cache-by-jobbing-the-xmront-routine-manually-or-via-the-zstu-routine)
  - [Overview of the Steps in this Section](#overview-of-the-steps-in-this-section-2)
  - [The Steps for sites that were NT/CACHE and are now VMS/CACHE](#the-steps-for-sites-that-were-ntcache-and-are-now-vmscache)
- [# Appendix A -- Copies of what the VMS User Account and Service look like](#appendix-a-copies-of-what-the-vms-user-account-and-service-look-like)
- [Appendix B -- Copy of the .com file to create the XMINET VMS User account](#appendix-b-copy-of-the-com-file-to-create-the-xminet-vms-user-account)
- [# Appendix C -- Copy of the .com file to create the TCP/IP Service](#appendix-c-copy-of-the-com-file-to-create-the-tcpip-service)
- [Appendix D -- Copy of the .com file used by the Service](#appendix-d-copy-of-the-com-file-used-by-the-service)
Vista MailMan uses a TCP/IP service to "listen" on a particular port for incoming TCP/IP connections from other systems. Listeners are necessary whenever Vista MailMan Systems need to initiate a connection to other VistA systems over TCP/IP.
Multi-threaded listeners are implemented using OpenVMS TCP/IP Services (a.k.a. Digital TCP/IP Services for OpenVMS, formerly known as UCX). The TCP/IP Multi-threaded Service on OpenVMS permits multiple TCP/IP clients to connect and run as concurrent processes up to the limits established by the system. TCP/IP listens on a particular port and launches the specified MailMan Listener process for each client connection.
Patch XM\*8.0\*25 introduced functionality allowing sites to run MailMan as a TCP/IP service at VMS/CACHE sites. Unfortunately, the patch instructions were incomplete. Sites currently fall into 4 categories for the purposes of this document:
1.  NT/CACHE sites.
> If you are currently an NT/CACHE site --- Stop. This document does not apply to your Configuration. You should continue to use the currently configured MailMan listener.
2.  VMS/DSM sites.
> If you are a VMS/DSM site --- Stop. This document does not apply to your Configuration. You should continue to use the currently configured MailMan listener.
3.  Sites that were VMS/DSM and are now VMS/CACHE.
> These sites had an existing TCP/IP service for MailMan and the service may still exist. These sites should follow the instructions in the Preliminary Steps and then proceed to Section 1 – Steps for sites that were VMS/DSM and are now VMS/CACHE.
4.  Sites that were NT/CACHE and are now VMS/CACHE.
> These sites had no pre-existing TCP/IP service for MailMan and ran the Mail Listener inside CACHE by jobbing the ^XMRONT manually or via the ^ZSTU routine. These sites should follow the instructions in the Preliminary Steps Section and then proceed to Section 2 – Steps for sites that were NT/CACHE and are now VMS/CACHE.

# # # Preliminary Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

STOP if you are an NT/CACHE or VMS/DSM site. This document does

Not apply to your Configuration. Continue to use your current MailMan listener.

All VMS/CACHE sites should follow the step described in this document

to disable their current MailMan listener and prevent it from accidentally

restarting upon your next CACHE reboot.

## Overview of the Steps in this Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is an overview of the steps in this section. Each step is then explained in detail.

1.  This patch requires XM\*8.0\*25. Verify that it is installed.
2.  Use the Cache RESJOB utility to stop the MailMan Listener on all nodes where it is running.
3.  On each node where MailMan is running Edit the ZSTU routine in %SYS to keep it from starting XMRONT when CACHE, or the Cluster starts.
4.  Proceed to the section that is appropriate to your prior configuration.

## The Preliminary Steps

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Review the Install File (#9.7) and verify the installation of XM\*8.0\*25.
2.  Stop the MailMan Listener on all nodes. You will need to perform the steps below on each Node where you run a MailMan Listener.
    1.  Log on and enter programmer mode. Then use the Cache System Status utility to locate the PID/JOB number of the MailMan listener. The job will be tied to port 25 and will be using the %ZISTCPS routine. It should look similar to the one below. Make note of the Process Number.

> Select Systems Manager Menu Option: Programmer Options

> Select Programmer Options Option: Programmer mode

> VAH\>D ^%SS

> Process Devices KB Namespace Routine CPU,Glob Pri UIC

> .

> .

> 204102F4 \|TCP\|1972 52 %SYS %cmtP 1310,192 4 1,4

> 2041665C \|TCP\|25 41 DEV %ZISTCPS 226,35 4 50,62 MailMan Listener.

> 204110C8 \|TCP\|9400 52 CML XWBTCPL 3064,404 4 200,201

> .

> .

2.  Use the %CD utility and move to the %SYS namespace. Then use the ^RESJOB utility to stop the job.

> DEV\>D ^%CD

> Namespace: %SYS

> You're in namespace %SYS

> Default directory is \_\$1\$DKA200:\[CACHESYS.ISC3A6.MGR\]

> %SYS\>D ^RESJOB

> Force a process to quit Cache

> Process ID (? for status report): 2041665C

> Process ID (? for status report):

> %SYS\>D ^%SS (Check again and make sure the MailMan Listener Job has stopped.

> Remember to perform the Steps above on each node that has a MailMan Listener running.

3.  On each node where the MailMan was running, move to the %SYS namespace with the CACHE %CD utility and then Edit the ZSTU routine, using your preferred routine editor, to keep it from starting ^XMRONT when CACHE, or the Cluster starts. If you use the CACHE cube remember to recompile the routine after you save it. Below is a 'before' and 'after' picture of the pertinent section of code. Comment out, or delete, the line that makes the call to the 'MAILMAN' method.

> Before

> ------------------------------------

> ZSTU ; Cache calls this routine at startup to perform these tasks automatically

> ;

> S \$ZT="ERR"

> ;S NSP="VAH" I \$E(\$P(\$ZU(86),"\*",2),1,3)'=\$E(\$ZU(110),1,3) S NSP=\$E(\$P(

> \$ZU(86),"\*",2),1,3)

> S NSP=\$ZU(90,4)

> D DISJRN

> D TASKMAN

> D BROKER

> D MAILMAN Comment out this line

> ;D 1809ENA

> ;D 1810ENA3

> ;D 1810ENA7

> ERR USE \$P WRITE !,\$ZERROR,! QUIT

> -------------------------------------

> After

> -------------------------------------

> ZSTU ; Cache calls this routine at startup to perform these tasks automatically

> ;

> S \$ZT="ERR"

> ;S NSP="VAH" I \$E(\$P(\$ZU(86),"\*",2),1,3)'=\$E(\$ZU(110),1,3) S NSP=\$E(\$P(

> \$ZU(86),"\*",2),1,3)

> S NSP=\$ZU(90,4)

> D DISJRN

> D TASKMAN

> D BROKER

> ; D MAILMAN Commented out per patch XM\*8\*29

> ;D 1809ENA

> ;D 1810ENA3

> ;D 1810ENA7

> ERR USE \$P WRITE !,\$ZERROR,! QUIT

> --------------------------------------

4.  Proceed to the section that is appropriate to your prior configuration.
    1.  If you are an NT/CACHE site --- Stop. This document does not apply to your Configuration. You should continue to use the currently configured MailMan listener.

> If you are a VMS/DSM site --- Stop. This document does not apply to your Configuration. You should continue to use the currently configured MailMan listener.

2.  If you were a VMS/DSM site and are now a VMS/CACHE site, go to Section 1 – Steps for sites that were VMS/DSM and are now VMS/CACHE.
3.  If you were an NT/CACHE site and are now a VMS/CACHE site, go to Section 2 – Steps for sites that were NT/CACHE and are now VMS/CACHE.

# # Section 1 – Steps for sites that were VMS/DSM and are now VMS/CACHE 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Instructions below are for Sites that were VMS/DSM and are now VMS/CACHE. These sites had an existing TCP/IP service for MailMan and the service may still exist. In addition some sites setup MailMan as a TCP/IP service during the VMS/DSM to VMS/CACHE conversions and a few sites were test sites for patch XM\*8.0\*25.

## Overview of the Steps in this Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Verify that you are not already running MailMan as a TCP/IP service. If the service exist and is enabled, you might have tested patch XM\*8.0\*25 or the conversion team might have set it up for you during the conversion.

> If you determine that you are already using MailMan as a TCP/IP service and it is setup correctly skip to step 8.

2.  Use the VMS Authorize utilities to gather information about the existing XMINET account and then retrieve the .COM files to be used later.
3.  Delete and recreate the OpenVMS account, usually called XMINET, which is used by the MailMan TCP/IP service and then make sure it has ownership of the XMINET directory and the files inside.
4.  Delete and recreate the XMINETMM TCP/IP Service for MailMan.
5.  Use the new XMINET_CACHE.COM command file to be used for the MailMan TCP/IP service or modify the pre-existing .COM file used when you were a VMS/DSM site.
6.  Test the new TCP/IP Service for MailMan.
7.  Troubleshooting.
8.  How to Control the Number of Log Files Created by TCP/IP.

## The Steps for sites that were VMS/DSM and are now VMS/CACHE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Determine if you are currently running MailMan as a TCP/IP service in a VMS/CACHE configuration.
    1.  On each node in the cluster, enter the TCP/IP utilities and use the TCP/IP command to SHOW SERVICE XMINETMM\* command to view the service.

999A01\$ TCPIP

TCPIP\> SHOW SERVICE XMINETMM\*

If either of the 2 statements below is true, then you are NOT using TCP/IP as a

Service; Skip to step 2.

If the XMINETMM service does not exists

> OR

The XMINETMM service does exist AND is DISABLED on all nodes

2.  You are running MailMan as a TCP/IP service if the following 2 statements are true:

If the service exists AND it is enabled on port 25, on any node in the cluster.

> AND

The ZSTU routine, in %SYS, already had the call to the MailMan method commented out

> If the 2 statements are BOTH true, you are probably running MailMan as a TCP/IP service. If that is the case you may simply check the following to make sure they are setup properly.

3.  Check the XMINET user, via MCR Authorize and compare it against the display in appendix A. Verify that the account settings for the existing XMINET account are the same as they appear in Appendix A or, if they are different, verify that the impact of the different settings is acceptable for your system.
4.  Check the XMINETMM TCP/IP Service, using the TCP/IP utilities and compare it against the service display in appendix A. Verify that the XMINETTMM service settings for the existing service are the same as they appear in Appendix A or, if they are different, verify that the impact of the different settings is acceptable for your system.
5.  Review the .COM file currently used by the service and make sure it uses the correct MailMan entry point for CACHE/VMS. The command lines should resemble the one below.

> Note -- You will need to remove the '!' comment character from the “csession” command line that Matches your configuration and edit it to reflect the correct \<namespace\> and \<configname\>

> Note – If you’re using the original command file, its CACHE command line uses “CCONTROL SESSION” to invoke the CACHE session. If you’re using “CCONTROL SESSION” you should change it to use “CSESSION”. This prevents duplicate process creation. See the Examples in the lines below.

\$!-------------------------------------------------------------

\$!-------------------------------------------------------------

\$! for CACHE

\$! Edit only one of the three "csession" lines below.

\$!

\$ assign 'f\$trnlnm("SYS\$NET")' SYS\$NET

\$!

\$! \#1 -- For Test Accounts

\$! If the configname is not the same as the node name, usually a test account,

\$! edit/use the csession line below

\$! Remove the comment character '!' from the beginning of the line.

\$! Replace \<PREFIX\>, including the \<\>, with the proper Test account prefix.

\$! Usually this is T or TST

\$! Replace \<namespace\>, including the \<\> with the correct namespace.

\$! Usually the namespace is TST for a Test account.

\$!

\$! an Example -- \$ csession "T''NODE'" "-U" "TST" "CACHEVMS^XMRUCX"

\$!

\$! csession "\<PREFIX\>''NODE'" "-U" "\<namespace\>" "CACHEVMS^XMRUCX"

\$!

\$! \#2 -- For most Production Accounts.

\$! If your configname is the same as your node name, usually a non-data

\$! center production site, edit/use the cesssion line below.

\$! Remove the comment character '!' from the beginning of the line.

\$! Replace \<namespace\>, including the \<\>, with the correct namespace,

\$! Usually the namespace is "VAH" for production.

\$!

\$! an Example -- \$ csession "''NODE'" "-U" "VAH" "CACHEVMS^XMRUCX"

\$!

\$! csession "''NODE'" "-U" "\<namespace\>" "CACHEVMS^XMRUCX"

\$!

\$! \#3 -- for Data-Center Production Accounts

\$! For a production Data Center site, edit/use the csession line below.

\$! Remove the comment character '!' from the beginning of the line.

\$! Replace \<NSP\>, including the \<\>, with the proper site prefix.

\$! Replace \<namespace\>, including the \<\> with the correct namespace.

\$! Usually the namespace is the same as the value used for NSP.

\$!

\$! an Example -- \$ csession "BRX''NODE'" "-U" "BRX" "CACHEVMS^XMRUCX"

\$!

\$! csession "\<NSP\>''NODE'" "-U" "\<namespace\>" "CACHEVMS^XMRUCX"

\$!

\$!-------------------------------------------------------------

\$!-------------------------------------------------------------

6.  In addition, you will need to add this section, just above the command line section, so the 'ip' symbol is defined. For the exact placement please look at the .com file in Appendix D.

> \$!-------------------------------------------------------------

> \$ bg == f\$extract(1,f\$locate(":",dev)-1,dev)

> \$ PIPE TCPIP SHOW DEVICE 'bg \| SEARCH SYS\$INPUT "''bg'" \| -

> (READ SYS\$INPUT host ; ip = f\$extract(55,15,host) ; define/job ip &ip) -

> && ip=f\$trnlnm("ip")

> \$!

> \$ define VistA\$IP "''ip'"

> \$!-------------------------------------------------------------

> If you determined that you are already running MailMan as a TCP/IP service AND that it seems to be configured properly then we suggest you go to step 8 for information on controlling the .LOG file version numbers. After reviewing step 8 you are done.

> If you have any questions, please log a NOIS and the appropriate HSITES support team will contact you.

2\. Use the Authorize utilities to SHOW the existing account and make note of the current UIC: and the current Default: values. Specifically make note of the DISK\$: value. You will then be able to reuse them when re-creating the account and the service. The account is usually called XMINET.

> 999A01\$ MCR AUTHORIZE

> UAF\> SHOW XMINET\*

> Username: XMINET Owner: XMINET

> Account: NETWORK UIC: \[50,50\] (\[XMINET\])

> CLI: DCL Tables: DCLTABLES

> Default: USER\$:\[XMINET\]

> UAF\> EXIT

> %UAF-I-NOMODS, no modifications made to system authorization file

> %UAF-I-RDBNOMODS, no modifications made to rights database

> 999A01\$

2.1 Use the OpenVMS command SET DEFAULT to move to the Default directory the old account was using, as noted in step in the step above and use FTP to retrieve the .COM files which will be used later.

> 999A01\$ SET DEFAULT USER\$:\[XMINET\]

2.2 Use the VMS SHOW DEFAULT command to verify your new default directory.

> 999A01\$ SHOW DEFAULT

> USER\$:\[XMINET\]

> If you are in the correct location go to the next step, if not, use the VMS command to SET DEFAULT to the correct directory.

2.3 For your convenience several VMS command files were created to assist with the creation of the new TCP/IP MailMan service. Listings of these files are included in this document and they should be downloaded from the \[ANONYMOUS.SOFTWARE\] directory at the following ftp sites:

> CIO Field Office FTP Address Directory

> ---------------------------------------------------------------------

> Vista download site -- REDACTED

> Albany -- REDACTED \[anonymous software\]

> Hines -- REDACTED \[anonymous software\]

> Salt Lake City -- REDACTED \[anonymous software\]

> Use the FTP utility to retrieve the following files.

> XMINET_CREATE_UAF.COM used to create the OpenVMS user account.

> XMINET_CREATE_SERVICE.COM used to create the TCP/IP service for MailMan.

> XMINET_CACHE.COM used by the MailMan service.

> Start FTP from VMS:

> 999A01\$ FTP

> Open/Connect to the download site:

> FTP\> O REDACTED

> 220 ISC5A4.REDACTED FTP Server (Version 5.3) Ready.

> Connected to REDACTED

> Name (REDACTED:REDACTEDa): anonymous

> 331 Guest login OK, send ident as password.

> Password:

> 230 Guest login OK, access restrictions apply.

> Move to the software directory:

> FTP\> cd SOFTWARE

> 250-CWD command successful.

> 250 New default directory is VA5\$:\[ANONYMOUS.SOFTWARE\]

> Set the transfer mode to ASCII:

> FTP\> ascii

> 200 TYPE set to ASCII.

> Get the files. An Example is shown for the retrieval of the XMINET_CREATE_UAF.COM file. Remember to ‘get’ all three files.

> FTP\> get XMINET_CREATE_UAF.COM

> 200 TYPE set to IMAGE.

> 200 PORT command successful.

> 150 Opening data connection for VA5\$:\[ANONYMOUS.SOFTWARE\]XMINET_CREATE_UAF.COM; (10.4.21.1,50857) (3296 bytes)

> 226 Transfer complete.

> local: \<Disk\>\$:\[\<Directory\>\]XMINET_CREATE_UAF.COM remote: XMINET_CREATE_UAF.COM

> 3296 bytes received in 00:00:00.28 seconds (11.14 Kbytes/s)

> Exit the FTP utility with the ‘bye’ command:

> FTP\> bye

> 221 Goodbye.

> Use the VMS DIRECTORY command to verify that all 3 files have been retrieved,

> And that that files size is correct:

> 999A01\$ DIRECTORY/SIZE

> Directory USER\$:\[XMINET\]

> XMINET_CACHE.COM 6

> XMINET_CREATE_SERVICE.COM 2

> XMINET_CREATE_UAF.COM 8

> Total of 3 files, 16 blocks.

3\. Delete and recreate the OpenVMS account, usually called XMINET, which is used by the MailMan TCP/IP service.

3.1 Make sure you noted the UIC: and Default Directory values for the account and then use the VMS authorize utilities and REMOVE the account.

> 999A01\$ \$ MCR AUTHORIZE

> 999A01\$ UAF\> REMOVE XMINET

> %UAF-I-REMMSG, record removed from system authorization file

> %UAF-I-RDBREMMSGU, identifier XMINET value \[000050,000050\] removed from rights

> database

> UAF\> EXIT

> %UAF-I-DONEMSG, system authorization file modified

> %UAF-I-RDBDONEMSG, rights database modified

3.2 Recreate a new OpenVMS user Account for MailMan by running the OpenVMS .COM file XMINET_CREATE_UAF.COM provided or by using the OpenVMS Authorize utility. You must have SYSPRV to do this. Below is an example of Account creation using the XMINET_CREATE_UAF.COM file. For simplicity we suggest you use the old values for UIC and Default Device/DISK\$.

> 999A01\$ @XMINET_CREATE_UAF.COM

> This will create a VMS user account called XMINET

> It will prompt for a UIC, and a DEVICE/DISK\$:

> It will then create the VMS user and set it's

> Default directory to DISK\$:\[XMINET\]

> Enter the UIC for XMINET (i.e. \[50,153\]) : \[50,50\]

> Enter the default device/disk for XMINET - make sure to include the :

> Generally, this will be USER\$:

> Enter the device (format device:) USER\$:

> %UAF-I-ADDMSG, user record successfully added

> %UAF-I-RDBADDMSGU, identifier XMINET value \[000050,000050\] added to rights

> database

> Username: XMINET Owner: XMINET

> Account: NETWORK UIC: \[50,50\] (\[XMINET\])

> CLI: DCL Tables: DCLTABLES

> Default: USER\$:\[XMINET\]

> LGICMD: NL:

> Flags: DisCtlY Restricted DisWelcome DisNewMail DisMail DisReport

> Primary days: Mon Tue Wed Thu Fri

> Secondary days: Sat Sun

> Primary 000000000011111111112222 Secondary 000000000011111111112222

> Day Hours 012345678901234567890123 Day Hours 012345678901234567890123

> Network: \##### Full access \###### \##### Full access \######

> Batch: ----- No access ------ ----- No access ------

> Local: ----- No access ------ ----- No access ------

> Dialup: ----- No access ------ ----- No access ------

> Remote: ----- No access ------ ----- No access ------

> Expiration: (none) Pwdminimum: 6 Login Fails: 0

> Pwdlifetime: 90 00:00 Pwdchange: (pre-expired)

> Last Login: (none) (interactive), (none) (non-interactive)

> Maxjobs: 0 Fillm: 300 Bytlm: 120000

> Maxacctjobs: 0 Shrfillm: 0 Pbytlm: 0

> Maxdetach: 0 BIOlm: 1024 JTquota: 4096

> Prclm: 32 DIOlm: 2048 WSdef: 13000

> Prio: 4 ASTlm: 2098 WSquo: 20000

> Queprio: 4 TQElm: 10 WSextent: 65536

> CPU: (none) Enqlm: 3005 Pgflquo: 120000

> Authorized Privileges:

> NETMBX TMPMBX

> Default Privileges:

> NETMBX TMPMBX

> %UAF-I-DONEMSG, system authorization file modified

> %UAF-I-RDBDONEMSG, rights database modified

> Making the XMINET account the owner of the

> USER\$:\[XMINET\] directory

> Process complete. New account XMINET created

> If the command file ran without errors you can move to step 3.3 and verify the settings for the new account.

> Alternatively you can create the XMINET account manually with the OpenVMS authorize Utility as shown below

> Remember to replace group with a valid UIC group, Member number with a unused/valid UIC member number, DISK\$: with the proper reference (usually USER\$) and the directory should be XMINET.

> Note the use of the continuation character " - " at the end of each line to allow the qualifiers to be entered on more than one line.

> 999A01\$ MCR AUTHORIZE

> UAF\> add XMINET/owner=XMINET -

> UAF\> /uic=\[group,member_number\]/device=DISK\$: -

> UAF\> /account=NETWORK/dir=\[XMINET\]/lgicmd=NL: -

> UAF\> /flags=(disctly,restricted,diswelcome,disnewmail,-

> UAF\> disreport,dismail,nodisuser) -

> UAF\> /primary=(mon,tue,wed,thur,fri,nosat,nosun) -

#### UAF\> /prclm=32/fillm=300/biolm=1024/diolm=2048/enqlm=3005 -

> UAF\> /bytlm=120000/wsdef=13000/wsquo=20000/wsextent=65536 -

> UAF\> /astlm=2098/Jtquota=4096/prio=4/pgflquo=120000 -

> UAF\> /priv=(tmpmbx,netmb,) -

> UAF\> /defpriv=(tmpmbx,netmb,) -

> UAF\> /network/nobatch/nolocal/nodialup/noremote

> %UAF-I-ADDMSG, user record successfully added

> %UAF-I-RDBADDMSGU, identifier XMINET value \[group, member_number\] added to rights database

3.3 Verify that the account settings for the new OpenVMS account are the same as they appear in Appendix A. If they are different, verify that the impact of the different settings is acceptable for your system. For security, make sure that the DisCtlY and Restricted flags are set. DO NOT set the Captive flag, as this will prevent the multi-threaded listener from working on Caché/VMS systems.

> 999A01\$ MCR AUTHORIZE

> UAF\> SHOW XMINET

> If everything checks out we are finished with the creation of the OpenVMS User account.

> If the Account is not setup correctly you may either modify the account to correct the Discrepancies or use the Authorize command REMOVE to delete the account and then follow the steps above to recreate it.

> Exit the OpenVMS Authorize utility:

> UAF\> EXIT

> %UAF-I-NOMODS, no modifications made to system authorization file

> %UAF-I-RDBNOMODS, no modifications made to rights database

3.4 Use the VMS DIRECTORY/SECURITY command to verify the ownership of the \[XMINET\] directory. If the directory ownership is correct you can move to the next step.

> 999A01\$ SHOW DEFAULT

> USER\$:\[000000\]

> 999A01\$ DIRECTORY/SECURITY USER\$:\[000000\]XMINET\*.\*

> Directory USER\$:\[000000\]

> XMINET.DIR;1 \[XMINET\]

> If the directory is already owned by XMINET skip to step 3.5

> If the ownership is not correct, use the SET FILE/OWNER command to give the new MailMan account ownership of the \[XMINET\] directory.

> 999A01\$ SETFILE/OWNER=XMINET USER\$:\[000000\]XMINET.DIR

> You can verify the results with the DIRECTORY/SECURITY command

> 999A01\$ DIRECTORY/SECURITY USER\$:\[000000\]XMINET.DIR

> Directory USER\$:\[000000\]

> XMINET.DIR;1 \[XMINET\] (RWE,RWE,RWE,RWE)

> Use the SET DEFAULT command to make sure USER\$:\[XMINET\] is your default directory.

> Then use the SHOW DEFAULT to confirm.

> 999A01\$ SET DEFAULT USER\$:\[XMINET\]

> 999A01\$ SHOW DEFAULT

> USER\$:\[XMINET\]

3.5 Now we need to make XMINET the owner of the files inside the directory. If you are not inside the \[XMINET\] directory use the SET DEFAULT command to move to the new directory. When a connection is made to the listener it will need to run the XMINET_CACHE.COM file to gain access to CACHE and MailMan. To do this the XMINET account, used by the TCP/IP Service will need ownership of the .COM file used by the Service.

> Verify that all the files are inside this directory as shown below. If the files are not in the directory you will need to move/copy them to the directory

> 999A01\$ DIRECTORY/SECURITY USER\$:\[XMINET\]\*.\*

> Directory USER\$:\[XMINET\]

> XMINET_CACHE.COM;9 \[SYSTEM\] (RWED,RWED,RE,)

XMINET_CREATE_SERVICE.COM;4 \[SYSTEM\] (RWED,RWED,RE,)

XMINET_CREATE_UAF.COM;8 \[SYSTEM\] (RWED,RWED,RE,)

> Use the VMS SET FILE/OWNER command to give the XMINET account ownership of the files inside the directory:

> 999A01\$ SET FILE/OWNER=XMINET USER\$:\[XMINET\]\*.\*;\*

> Verify that the ownership is now correct:

> 999A01\$ DIRECTORY/SECURITY USER\$:\[XMINET\]\*.\*

> Directory USER\$:\[XMINET\]

> XMINET_CACHE.COM;9 \[XMINET\] (RWED,RWED,RE,)

> XMINET_CREATE_SERVICE.COM;4 \[XMINET\] (RWED,RWED,RE,)

> XMINET_CREATE_UAF.COM;8 \[XMINET\] (RWED,RWED,RE,)

> If everything looks correct we can delete and recreate the new MailMan TCP/IP service.

> If something is not correct, review the instructions above for clues.

4.  Delete the existing XMINETMM service and then use the

XMINET_CREATE_SERVICE.COM file to recreate it or use

TCP/IP commands to recreate the service manually.

> Before deleting the service you need to disable in on any node where it is enabled and then remove it from the list of services which TCP/IP enables when the node is booted.

4.1.1 On Each node in the production cluster do the following

Show the XMINETMM service and disable it if it is enabled. Note each node where the service was enabled so you will know where to enable it later.

(Enter the TCIP utilities)

999A01\$ TCPIP

TCPIP\>

(Show the service)

TCPIP\> SHOW SERVICE XMINETMM

Service Port Proto Process Address State

XMINETMM 25 TCP,UDP XMINET 0.0.0.0 Enabled

(Disable the service)

TCPIP\> DISABLE SERVICE XMINETMM

(Verify that it is disabled)

TCPIP\> SHOW SERVICE XMINETMM

Service Port Proto Process Address State

XMINETMM 25 TCP,UDP XMINET 0.0.0.0 Disabled

(Remove it from the list of TCP/IP services to start when the node is booted)

TCPIP\> SET CONFIGURATION ENABLE NOSERVICE XMINETMM

(Verify that it was removed from the list of services to enable on boot. Note -- Your display may vary from this but XMINETMM should not be in the list)

TCPIP\> SHOW CONFIGURATION ENABLE SERVICE

Enable service

AXPINT, AXPINTM, BIND, LPD, METRIC, NTP, PINGBLAST, RPCSERVER_BCG,

RPCSERVER_BCR, RPCSERVER_BDG, RPCSERVER_BDR, RSH, VLINK, VLINK2

4.1.2 On ONE node in the production cluster, delete the service

Show the existing Service, ensure that it is DISABLED, and then delete it.

999A01\$ TCPIP

TCPIP\> SHOW SERVICE/FULL XMINETMM\*

Service: XMINETMM

State: Disabled

Port: 25 Protocol: TCP Address: 0.0.0.0

User_name: not defined Process: XMINET

(Delete the Service)

TCPIP\> SET NOSERVICE XMINETMM

Service Port Proto Process Address State:

XMINETMM 25 TCP XMINETMM 0.0.0.0 Disabled

Remove? \[N\]:Y

(Exit the TCP/IP utility with the EXIT command)

TCPIP\> EXIT

999A01\$

2.  We have provided a .com file named XMINET_CREATE_SERVICE.COM to create the XMINETMM service. Verify that your Default directory is USER\$:\[XMINET\] with the SHOW DEFAULT command. If your default directory is not correct you will need to SET DEFAULT to USER\$:\[XMINET\]. To create the service, run the XMINET_CREATE_SERVICE.COM file from the VMS command prompt. You may also create the service manually.

> Note -- The XMINET_CREATE_SERVICE.COM file will set the /file qualifier for the new XMINETMM service to XMINET_CACHE.COM. If you wish the /file qualifier to show the full path of DISK\$:\[XMINET\]XMINET_CACHE.COM you will need to edit the file and add the DISK\$:\[Directory\] information.

> Run the XMINET_CREATE_SERVICE.COM file to create the new service.

> 999A01\$ @XMINET_CREATE_SERVICE.COM

> Creating Service XMINETMM for port 25 with connection limit of 50

> Process Complete.

> Service Port Proto Process Address State

> XMINETMM 25 TCP XMINET 0.0.0.0 Disabled

> If you used the command file to create the service and the service is setup correctly go to step 4.3.

> Alternatively you can create the Service manually with the TCP/IP Utilities as shown below

> Note the use of the continuation character " - " at the end of each line to allow the qualifiers to be entered on more than one line.

> 999A01\$ TCPIP

> Enter the following commands to create the service.

TCPIP\> SET SERVICE XMINETMM/FILE=XMINET_CACHE.COM/PORT=25/PROCESS_NAME="XMINET" -

> /USER_NAME=XMINET/PROTOCOL=TCP -

> /REJECT=MESSAGE=("421^TOO MANY SMTP CHANNELS ACTIVE")/LIMIT=50

3.  After creating the XMINETMM service use the TCP/IP command SHOW SERVICE XMINETMM\* to verify that the service was created.

> 999A01\$ TCPIP SHOW SERVICE XMINETMM\*

> Service Port Proto Process Address State

> XMINETMM 25 TCP XMINET 0.0.0.0 Disabled

4.  Log onto one of the nodes, where you plan to run the MailMan TCP/IP Service, then enter the TCP/IP utility and enable the new XMINETMM TCP/IP service.

> 999A01\$ TCPIP

> TCPIP\> ENABLE SERVICE XMINETMM

5.  Verify that the Service started, and the details are correct with the TCP/IP SHOW SERVICE/FULL command. Pay special attention to the file, port number, and Limit fields to make sure they are correct and check the State field to verify that the service is Enabled.

> TCPIP\> SHOW SERVICE/FULL XMINETMM

> Service: XMINETMM

> State: Enabled

> Port: 25 Protocol: TCP Address: 0.0.0.0

> Inactivity: 5 User_name: XMINET Process: XMINET

> Limit: 50 Active: 0 Peak: 0

> File: XMINET_CACHE.COM

> Flags: Listen

> Socket Opts: Rcheck Scheck

> Receive: 0 Send: 0

> Log Opts: None

> File: not defined

> Security

> Reject msg: 421^too many SMTP channels active

> Accept host: 0.0.0.0

> Accept netw: 0.0.0.0

> If the Service definition is correct you can move to step 4.6

> If there are errors in the service definition we suggest you do the following to

> remove the corrupted service and repeat the steps used to create the service.

> (To delete the service)

> 999A01\$ TCPIP

> TCPIP\> SET NOSERVICE XMINETMM

> Service Port Proto Process Address State:

> XMINETMM 25 TCP XMINET 0.0.0.0 Disabled

> Remove? \[N\]:Y

6.  If the service is setup properly you should decide which node(s) in the cluster should run the service and enter the service into the TCP/IP permanent configuration database that enables services for startup. On each node where you want to enable the service at Startup you will want to enter the TCP/IP commands below

> Log onto the node where you want the service to run, and then enter the TCP/IP utilities with the TCP/IP command; then enter the TCP/IP commands below

> (Enable the service)

> TCPIP\> ENABLE SERVICE XMINETMM

> (Save service in the TCP/IP permanent configuration database for reboot)

> TCPIP\> SET CONFIG ENABLE SERVICE XMINETMM

> (Check the service)

> TCPIP\> SHO SERVICE/FULL XMINETMM

> Enter the TCP/IP commands below to display the services configured in the services database that will be enabled by the TCP/IP Services startup procedure. Your list may vary slightly but it should contain XMINETMM

> TCPIP\>SHOW CONFIGURATION ENABLE SERVICE

> Enable service:

> FTP, FTP_CLIENT, LPD, MOUNT, NFS, NFS_CLIENT, PCNFS,

> PORTMAPPER, REXEC, RSH, SMTP, SNMP, XMINETMM

> If the service appears to be setup and running you can exit the TCP/IP utilities and move to the next step. If there are problems you will need to review the prior steps and troubleshoot.

5.  Use the new XMINET_CACHE.COM command file to be used for the MailMan TCP/IP service or modify the pre-existing .COM file used when you were a VMS/DSM site.
    1.  If you used the .com files to create the XMINET user and the XMINETMM service or followed the instructions exactly, the XMINET_CACHE.COM file will be the .COM file invoked when a connection is made to the Listener. Before testing the new service, we suggest you TYPE and review the XMINET_CACHE.COM file for correctness. Pay special attention to the command line section as shown below and make sure the namespace is correct for your configuration. Most configurations use the VAH namespace but at some Datacenters it might be different. Edit the .COM file and make any required changes.

> Or

If you chose to use the .COM file from the pre-existing (VMS/DSM) XMINETMM service you will

need to edit it and replace the DSM specific command line section with the one below. Pay special

attention to the command line section as shown below and make sure the namespace is correct for

> your configuration. Most configurations use the VAH namespace but at some Data Centers it might be different. Edit the .COM file and make any required changes.

> Review the .COM file used by the service and make sure it uses the correct MailMan entry point for CACHE/VMS. The command lines should resemble the one below.

> Note -- You will need to remove the '!' comment character from the command line that Matches your configuration and edit it to reflect the correct \<namespace\> and \<configname\>

\$!-------------------------------------------------------------

\$!-------------------------------------------------------------

\$! for CACHE

\$! Edit only one of the three "csession" lines below.

\$!

\$ assign 'f\$trnlnm("SYS\$NET")' SYS\$NET

\$!

\$! \#1 -- For Test Accounts

\$! If the configname is not the same as the node name, usually a test account,

\$! edit/use the csession line below

\$! Remove the comment character '!' from the beginning of the line.

\$! Replace \<PREFIX\>, including the \<\>, with the proper Test account prefix.

\$! Usually this is T or TST

\$! Replace \<namespace\>, including the \<\> with the correct namespace.

\$! Usually the namespace is TST for a Test account.

\$!

\$! an Example -- \$ csession "T''NODE'" "-U" "TST" "CACHEVMS^XMRUCX"

\$!

\$! csession "\<PREFIX\>''NODE'" "-U" "\<namespace\>" "CACHEVMS^XMRUCX"

\$!

\$! \#2 -- For most Production Accounts.

\$! If your configname is the same as your node name, usually a non-data

\$! center production site, edit/use the cesssion line below.

\$! Remove the comment character '!' from the beginning of the line.

\$! Replace \<namespace\>, including the \<\>, with the correct namespace,

\$! Usually the namespace is "VAH" for production.

\$!

\$! an Example -- \$ csession "''NODE'" "-U" "VAH" "CACHEVMS^XMRUCX"

\$!

\$! csession "''NODE'" "-U" "\<namespace\>" "CACHEVMS^XMRUCX"

\$!

\$! \#3 -- for Data-Center Production Accounts

\$! For a production Data Center site, edit/use the csession line below.

\$! Remove the comment character '!' from the beginning of the line.

\$! Replace \<NSP\>, including the \<\>, with the proper site prefix.

\$! Replace \<namespace\>, including the \<\> with the correct namespace.

\$! Usually the namespace is the same as the value used for NSP.

\$!

\$! an Example -- \$ csession "BRX''NODE'" "-U" "BRX" "CACHEVMS^XMRUCX"

\$!

\$! csession "\<NSP\>''NODE'" "-U" "\<namespace\>" "CACHEVMS^XMRUCX"

\$!

\$!-------------------------------------------------------------

\$!-------------------------------------------------------------

> In addition, you will need to add this section, just above the command line section, so the 'ip' symbol is defined. For the exact placement please look at the .com file in Appendix D.

> \$!-------------------------------------------------------------

> \$ bg == f\$extract(1,f\$locate(":",dev)-1,dev)

> \$ PIPE TCPIP SHOW DEVICE 'bg \| SEARCH SYS\$INPUT "''bg'" \| -

> (READ SYS\$INPUT host ; ip = f\$extract(55,15,host) ; define/job ip &ip) -

> && ip=f\$trnlnm("ip")

> \$!

> \$ define VistA\$IP "''ip'"

> \$!-------------------------------------------------------------

5.  Attempt a connection to test the XMINETMM Service.

> The best method to test the XMINETMM service is to attempt to connect to a node running the service at port number 25. This is where the service listens for connection requests. Log onto any node in the cluster and attempt to Telnet to a Node in the cluster, which has the service enabled, at the designated port number and make sure it connects properly. An example is shown below.

> Telnet to the node and request a connection to a specific port

> The format on a VMS system is TELNET \<IP address\> \<Port#\>

> ( An Example to the REDACTED OI account at port 25)

> \$ TELNET 10.4.21.1 25

> (The request is allowed and VistA MailMan Answers)

> %TELNET-I-TRYING, Trying ... 10.4.21.1

> %TELNET-I-SESSION, Session 01, host 10.4.21.1, port 25

> 220 REDACTEDMailMan 8.0 ready

> (Type QUIT to drop the connection)

> QUIT

> 221 REDACTEDService closing transmission channel

> %TELNET-S-REMCLOSED, Remote connection closed

> -TELNET-I-SESSION, Session 01, host 10.4.21.1, port 25

> If the connection test is successful you can try sending mail from another Vista system, such as FORUM, to your system to verify that the service is working.

6.  If the connection test fails you should first look at the .LOG files, which are created in the DEFAULT directory for the service. If you followed the instructions explicitly the DEFAULT directory will be USER\$:\[XMINET\]. You can then TYPE and review the .LOG files for hints about what went wrong. Another valuable source of information is the VISTA error trap. If a review of both of these fails to yield an answer we suggest you log a NOIS call and the appropriate HSITES support team will contact you
8.  How to Control the Number of Log Files Created by TCP/IP.

> The XMINETMM TCP/IP service automatically creates log files in the XMINETMM directory named XMINET_CACHE.LOG;xxx (where "xxx" is a file version number). TCP/IP does this, and it cannot be prevented. The XMINET_CACHE.COM file will purge extra log files as part of its running. New versions of this file will be created until that file version number reaches the maximum number of 32767. This can be used to limit the number of log files by explicitly setting the log file to the highest version number (32767) on the XMINET_CACHE.LOG file. This results in the XMINET_CACHE.LOG file being renamed to XMINET_CACHE.LOG;32767, and no further versions of this log file are created. If a system manager needs to see the log file contents of new connections, they can rename that file to a lower version such as XMINET_CACHE.LOG;32760 and let new log files be created.

> It is recommended that you not limit the number of versions of the log file until you know that your XMINETMM service is working correctly; keeping the log files can help when diagnosing problems with the service/account.

> (Renaming to the highest version number)

> 999A01\$ SHOW DEFAULT

> USER\$:\[XMINET\]

> The format is RENAME OldFileName NewFileName

> 999A01\$ RENAME XMINET_CACHE.LOG XMINET_CACHE.LOG;32767You are done -- Stop.  

# Section 2 – Steps for sites that were NT/CACHE and are now VMS/CACHE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# The instructions below are for sites that were NT/CACHE and are now VMS/CACHE. These sites had no pre-existing TCP/IP service for MailMan and ran the Mail Listener inside CACHE by jobbing the ^XMRONT routine manually or via the ^ZSTU routine.

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

If you are currently an NT/CACHE site --- Stop. This document does not apply to your Configuration. You should continue to use the currently configured MailMan listener.

If you are a VMS/DSM site --- Stop. This document does not apply to your Configuration. You should continue to use the currently configured MailMan listener.

## Overview of the Steps in this Section

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1.  Create a directory, called XMINET, which will used by the TCP/IP service. It will become the home directory of the OpenVMS Mailman account.
2.  Use the FTP utilities and retrieve the .COM files, which can be used to perform several of the steps below.
3.  Create an OpenVMS User Account, called XMINET, to be used by the XMINETMM TCP/IP Service and then make sure it has ownership of the XMINET directory and the files inside.
4.  Create a TCP/IP Service, called XMINETMM, which will ‘listen’ for connection requests.
5.  Review the new XMINET_CACHE.COM command file to be used for the MailMan TCP/IP service and edit as needed.
6.  Attempt a connection to Test the Service.
7.  Troubleshooting
8.  How to Control the Number of Log Files Created by TCP/IP.

## The Steps for sites that were NT/CACHE and are now VMS/CACHE

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

1\. Create a directory, called XMINET, which will be used by the TCP/IP service. This will be used as the Home Directory for the MailMan OpenVMS user TCP/IP Service.

> Set Default to the DISK\$: where you plan to create the Directory. In the Example below we are going to create a new Directory called \[XMINET\] on the USER\$: Disk.

> In VMS \[000000\] (six zero’s) is the root level of the Disk.

> Set Default to the root level of USER\$: disk

> 999A01\>\> SET DEFAULT USER\$:\[000000\]

> You should use the VMS command SHOW DEFAULT and verify that you are in the correct location

> 999A01\$ SHOW DEFAULT

> USER\$:\[000000\]

> Create a new Directory.

> 999A01\$ CREATE/DIRECTORY \[XMINET\]

> Verify that the directory was created and use the SECURITY qualifier to check the ownership and protections. Note, at this point the new directory is probably owned by the system, or your account.

> 999A01\$ DIRECTORY/SECURITY XMINET\*.\*

> Directory USER\$:\[000000\]

> XMINET.DIR;1 \[1,1\]

> Total of 1 file.

> Now that we have a directory we can retrieve the .COM files to be used later.

2\. Retrieve the Pre-Configured OpenVMS DCL command files.

2.1 Use the OpenVMS command SET DEFAULT to move to the new directory

> 999A01\$ SET DEFAULT USER\$:\[XMINET\]

2.2 Use the VMS SHOW DEFAULT command to verify your new default directory.

> 999A01\$ SHOW DEFAULT

> USER\$:\[XMINET\]

> If you are in the correct location continue to step 2.3, if not, use the VMS command to SET DEFAULT to the correct directory.

2.3 For your convenience several VMS command files were created to assist with the creation of the new TCP/IP MailMan service. Listings of these files are included in this document and they should be downloaded from the \[ANONYMOUS.SOFTWARE\] directory at the following ftp sites:

> CIO Field Office FTP Address Directory

> ---------------------------------------------------------------------

> Vista download site -- REDACTED

> Albany -- REDACTED \[anonymous software\]

> Hines -- REDACTED \[anonymous software\]

> Salt Lake City -- REDACTED\[anonymous software\]

> Use the FTP utility to retrieve the following files.

> XMINET_CREATE_UAF.COM used to create the OpenVMS user account.

> XMINET_CREATE_SERVICE.COM used to create the TCP/IP service for MailMan.

> XMINET_CACHE.COM used by the MailMan service.

> Start FTP from VMS:

> 999A01\$ FTP

> Open/Connect to the download site

> FTP\> O REDACTED

> 220 ISC5A4REDACTED FTP Server (Version 5.3) Ready.

> Connected to REDACTED.

> Name (REDACTED:REDACTEDa): anonymous

> 331 Guest login OK, send ident as password.

> Password:

> 230 Guest login OK, access restrictions apply.

> Move to the software directory:

> FTP\> cd SOFTWARE

> 250-CWD command successful.

> 250 New default directory is VA5\$:\[ANONYMOUS.SOFTWARE\]

> Set the transfer mode to ASCII:

> FTP\> ascii

> 200 TYPE set to ASCII.

> Get all the files. An Example is shown for the retrieval of the XMINET_CREATE_UAF.COM file. Remember to ‘get’ all three files.

> FTP\> get XMINET_CREATE_UAF.COM

> 200 TYPE set to IMAGE.

> 200 PORT command successful.

> 150 Opening data connection for VA5\$:\[ANONYMOUS.SOFTWARE\]XMINET_CREATE_UAF.COM; (10.4.21.1,50857) (3296 bytes)

> 226 Transfer complete.

> local: \<Disk\>\$:\[\<Directory\>\]XMINET_CREATE_UAF.COM remote: XMINET_CREATE_UAF.COM

> 3296 bytes received in 00:00:00.28 seconds (11.14 Kbytes/s)

> Exit the FTP utility with the ‘bye’ command:

> FTP\> bye

> 221 Goodbye.

> Use the VMS DIRECTORY command to verify that all 3 files have been retrieved,

> And that that files size is correct:

> 999A01\$ DIRECTORY/SIZE

> Directory USER\$:\[XMINET\]

> XMINET_CACHE.COM 6

> XMINET_CREATE_SERVICE.COM 2

> XMINET_CREATE_UAF.COM 8

> Total of 3 files, 16 blocks.

3\. Create an OpenVMS User Account, called XMINET, to be used by the XMINETMM TCP/IP Service.

3.1 Verify that you do not have an existing OpenVMS account for MailMan by using the OpenVMS authorize utility.

> 999A01\$ MCR AUTHORIZE

> UAF\> SHOW XMINET\*

> If the account does not exist you will see a message like the one below (using the OpenVMS user account name XMINET as an example)

> UAF\> SHOW XMINET\*

> %UAF-W-BADSPC, no user matches specification

> If the account does exist, VMS will give detailed information about the account and you should verify that it is setup properly with the required \<Disk\>\$:\[\<Directory\>\], limits, rights and privileges or use the MCR authorize REMOVE command to delete the account. An account with the correct properties is shown in Appendix A.

3.2 Determine an unused User Identification Code (UIC), typically in the same group as other Caché for OpenVMS accounts such as CACHEMGR, CACHE_BACKUP, M2MSERVER, XWBSERVER, HLSEVEN etc. You will need this before you can perform the steps below.

> The UIC Specifies the user identification code (UIC). The UIC value is

> a group number in the range from 1 to 37776 (octal) and a member

> number in the range from 0 to 177776 (octal), which are separated

> by a comma and enclosed in brackets. HP reserves group 1 and

> groups 300-377 for its own use.

> While in the VMS Authorization utility, use the Authorize command "SHOW/BRIEF \[\*,\*\]" to produce a list of all the UICs. After looking at the list, you should be able to determine the group used by the General OpenVMS accounts. This is usually, but not always groups \[50,\] or \[200,\]. You can then determine an unused UIC combination to use.

> Note -- The UIC is an OCTAL value so it cannot end in 8 or 9; \[50,156\] would be good if unused but \[50,158\] would generate an error.

> First, Use the \[\*,\*\] listing to determine the Group Number of the general VMS accounts.

> 999A01\$ MCR AUTHORIZE

> UAF\> SHOW/BRIEF \[\*,\*\]

> Owner Username UIC Account Privs Pri Directory

> SYSTEM MANAGER DREDACTED \[1,5\] SYSTEM All 4 USER\$:\[CREDACTED\]

> SYSTEM MANAGER LREDACTED \[1,6\] SYSTEM All 4 SYS\$SYSROOT:\[SYSMGR\]

> REDACTED,ANDY REDACTEDA \[50,62\] All 4 USER\$:\[REDACTEDA\]

> REDACTED,RANDY REDACTEDR \[50,63\] Devour 4 USER\$:\[REDACTEDR\]

> CACHE_BACKUP CACHE_BACKUP \[50,153\] NETWORK All 4

> USER\$:\[CACHESYS.CACHE_BKUP\]

> BCKMON BCKMON \[50,153\] NETWORK All 4

> USER\$:\[BCKMON\]

> In the list above we can see than CACHE_BACKUP and BCKMON are in group 50.

> We can then look at group 50 to find an unused/open UIC. An example is shown below that list all the UIC values in Group 50 at a specific site. Determine an unused member_number and keep it for later use.

> UAF\> SHOW/BRIEF \[50,\*\]

> Owner Username UIC Account Privs Pri

> Directory

> DSM DSMMGR \[50,1\] All 4

> SYS\$SYSDEVICE:\[DSMMGR\]

> XMINETGLD XMINETGLD \[50,100\] NETWORK System 4

> SYS\$:\[XMINET_GLD\]

> XMINETRSK XMINETRSK \[50,101\] NETWORK System 4

> SYS\$:\[XMINET_RSK\]

> CACHE_BACKUP CACHE_BACKUP \[50,153\] NETWORK All 4

> USER\$:\[CACHESYS.CACHE_BKUP\]

> BCKMON BCKMON \[50,153\] NETWORK All 4

> USER\$:\[BCKMON\]

> GTMMARK GTMMARK \[50,157\] NETWORK All 4

> USER\$:\[GTMMARK\]

> REDACTED REDACTED \[50,160\] Normal

> 4 USER\$:\[ALEX

> After deciding which User Identification Code (UIC) to use for the new XMINET account you should exit the MCR Authorize utility with the EXIT command.

> UAF\> EXIT

> %UAF-I-NOMODS, no modifications made to system authorization file

> %UAF-I-RDBNOMODS, no modifications made to rights database

3.3 Create a new OpenVMS user Account for MailMan by running the OpenVMS .COM file XMINET_CREATE_UAF.COM provided or by using the OpenVMS Authorize utility. You must have SYSPRV to do this. Below is an example of Account creation using the XMINET_CREATE_UAF.COM file.

> 999A01\$ @XMINET_CREATE_UAF.COM

> This will create a VMS user account called XMINET

> it will prompt for a UIC, and a DEVICE/DISK\$:

> It will then create the VMS user and set it's

> Default directory to DISK\$:\[XMINET\]

> Enter the UIC for XMINET (i.e. \[50,153\]) : \[50,50\]

> Enter the default device/disk for XMINET - make sure to include the :

> Generally, this will be USER\$:

> Enter the device (format device:) USER\$:

> %UAF-I-ADDMSG, user record successfully added

> %UAF-I-RDBADDMSGU, identifier XMINET value \[000050,000050\] added to rights

> database

> Username: XMINET Owner: XMINET

> Account: NETWORK UIC: \[50,50\] (\[XMINET\])

> CLI: DCL Tables: DCLTABLES

> Default: USER\$:\[XMINET\]

> LGICMD: NL:

> Flags: DisCtlY Restricted DisWelcome DisNewMail DisMail DisReport

> Primary days: Mon Tue Wed Thu Fri

> Secondary days: Sat Sun

> Primary 000000000011111111112222 Secondary 000000000011111111112222

> Day Hours 012345678901234567890123 Day Hours 012345678901234567890123

> Network: \##### Full access \###### \##### Full access \######

> Batch: ----- No access ------ ----- No access ------

> Local: ----- No access ------ ----- No access ------

> Dialup: ----- No access ------ ----- No access ------

> Remote: ----- No access ------ ----- No access ------

> Expiration: (none) Pwdminimum: 6 Login Fails: 0

> Pwdlifetime: 90 00:00 Pwdchange: (pre-expired)

> Last Login: (none) (interactive), (none) (non-interactive)

> Maxjobs: 0 Fillm: 300 Bytlm: 120000

> Maxacctjobs: 0 Shrfillm: 0 Pbytlm: 0

> Maxdetach: 0 BIOlm: 1024 JTquota: 4096

> Prclm: 32 DIOlm: 2048 WSdef: 13000

> Prio: 4 ASTlm: 2098 WSquo: 20000

> Queprio: 4 TQElm: 10 WSextent: 65536

> CPU: (none) Enqlm: 3005 Pgflquo: 120000

> Authorized Privileges:

> NETMBX TMPMBX

> Default Privileges:

> NETMBX TMPMBX

> %UAF-I-DONEMSG, system authorization file modified

> %UAF-I-RDBDONEMSG, rights database modified

> Making the XMINET account the owner of the

> USER\$:\[XMINET\] directory

> Process complete. New account XMINET created

> If you used the XMINET_CREATE_UAF.COM file to create the XMINET account,

> And it ran without errors, skip to Step 3.4

> Alternatively, you can create the XMINET account manually with the OpenVMS authorize Utility as shown below.

> Remember to replace group with a valid UIC group, Member number with a unused/valid UIC member number, DISK\$: with the proper reference (usually USER\$) and the directory should be XMINET.

> Note the use of the continuation character " - " at the end of each line to allow the qualifiers to be entered on more than one line.

> 999A01\$ MCR AUTHORIZE

> UAF\> add XMINET/owner=XMINET -

> UAF\> /uic=\[group,member_number\]/device=DISK\$: -

> UAF\> /account=NETWORK/dir=\[XMINET\]/lgicmd=NL: -

> UAF\> /flags=(disctly,restricted,diswelcome,disnewmail,-

> UAF\> disreport,dismail,nodisuser) -

> UAF\> /primary=(mon,tue,wed,thur,fri,nosat,nosun) -

> UAF\> /prclm=32/fillm=300/biolm=1024/diolm=2048/enqlm=3005 -

> UAF\> /bytlm=120000/wsdef=13000/wsquo=20000/wsextent=65536 -

> UAF\> /astlm=2098/Jtquota=4096/prio=4/pgflquo=120000 -

> UAF\> /priv=(tmpmbx,netmb) -

> UAF\> /defpriv=(tmpmbx,netmb) -

> UAF\> /network/nobatch/nolocal/nodialup/noremote

> %UAF-I-ADDMSG, user record successfully added

> %UAF-I-RDBADDMSGU, identifier XMINET value \[group, member_number\] added to rights database

3.4 Verify that the account settings for the new OpenVMS account are the same as they appear in the example that follows; or, if they are different, verify that the impact of the different settings is acceptable for your system. For security, make sure that the DisCtlY and Restricted flags are set. DO NOT set the Captive flag, as this will prevent the multi-threaded listener from working on Caché/VMS systems.

> 999A01\$ MCR AUTHORIZE

> UAF\> SHOW XMINET

> See Appendix A for a sample of what the new VMS User account should look like

> If everything checks out we are finished with the creation of the OpenVMS User account.

> If the Account is not setup correctly you may either modify the account to correct the Discrepancies or use the Authorize command REMOVE to delete the account and then follow the steps above to recreate it.

> 999A01\$ UAF\> REMOVE XMINET

> %UAF-I-REMMSG, record removed from system authorization file

> %UAF-I-RDBREMMSGU, identifier XMINET value \[000050,000050\] removed from rights

> database

> Exit the OpenVMS Authorize utility.

> UAF\> EXIT

> %UAF-I-NOMODS, no modifications made to system authorization file

> %UAF-I-RDBNOMODS, no modifications made to rights database

> Now that we have an XMINET VMS account for MailMan, We need to ensure that it owns the new \[XMINET\] directory and the .COM files inside it.

3.5 If you used the XMINET_CREATE_UAF.COM file to create the account, the ownership of the \[XMINET\] directory should be correct. If the directory is not owned by XMINET you will need to reset the ownership using the OpenVMS SET FILE/OWNER commands. An example is shown below

> Use the VMS DIRECTORY/SECURITY command to verify the ownership of the directory

> 999A01\$ DIRECTORY/SECURITY USER\$:\[000000\]XMINET\*.\*

> Directory USER\$:\[000000\]

> XMINET.DIR;1 \[XMINET\]

> If the ownership is not correct, use the SET FILE/OWNER command to give the new MailMan account ownership of the \[XMINET\] directory.

> 999A01\$ SET FILE/OWNER=XMINET USER\$:\[000000\]XMINET.DIR

> You can verify the results with the DIRECTORY/SECURITY command

> 999A01\$ DIRECTORY/SECURITY USER\$:\[000000\]XMINET.DIR

> Directory USER\$:\[000000\]

> XMINET.DIR;1 \[XMINET\] (RWE,RWE,RWE,RWE)

> Use the SET DEFAULT command to make USER\$:\[XMINET\] your default directory.

> Then use the SHOW DEFAULT to confirm.

> 999A01\$ SET DEFAULT USER\$:\[XMINET\]

> 999A01\$ SHOW DEFAULT

> USER\$:\[XMINET\]

3.6 Now we need to make XMINET the owner of the .COM files inside the directory. If you are not inside the directory use the SET DEFAULT command to move to the new directory. When a connection is made to the listener it will need to run the XMINET_CACHE.COM file to gain access to CACHE and MailMan. To do this the VMS account, used by the TCP/IP Service will need ownership of the .COM file used by the Service.

> Verify that all the files are inside this directory as shown below. If the files are not in the directory you will need to move/copy them to the directory

> 999A01\$ DIRECTORY/SECURITY USER\$:\[XMINET\]\*.\*

> Directory USER\$:\[XMINET\]

> XMINET_CACHE.COM;9 \[SYSTEM\] (RWED,RWED,RE,)

XMINET_CREATE_SERVICE.COM;4 \[SYSTEM\] (RWED,RWED,RE,)

XMINET_CREATE_UAF.COM;8 \[SYSTEM\] (RWED,RWED,RE,)

Now, make the XMINET account the owner of the files in the directory.

> 999A01\$ SET FILE/OWNER=XMINET USER\$:\[XMINET\]\*.\*;\*

> Verify that the ownership is now correct.

> 999A01\$ DIRECTORY/SECURITY USER\$:\[XMINET\]\*.\*

> Directory USER\$:\[XMINET\]

> XMINET_CACHE.COM;9 \[XMINET\] (RWED,RWED,RE,)

> XMINET_CREATE_SERVICE.COM;4 \[XMINET\] (RWED,RWED,RE,)

> XMINET_CREATE_UAF.COM;8 \[XMINET\] (RWED,RWED,RE,)

> If everything looks correct we can create the new MailMan TCP/IP service.

> If something is not correct, review the instructions above for clues.

4\. Create a TCP/IP Service for VistA MailMan. This can be done with the XMINET_CREATE_SERVICE.COM file or you can use TCP/IP commands to create the service manually.

4.1 From the OpenVMS command prompt type ‘TCPIP’ to invoke the TCP/IP utilities

> 999A01\$ TCPIP

> TCPIP\>

> Use the SHOW SERVICE commands to make sure the service XMINETMM does not already exist.

> TCPIP\> SHOW SERVICE XMINET\*.\*

> If the service does not exist you will see a message similar to the one below and you can skip to step 4.2.

> %TCPIP-W-NORECORD, information not found

> -RMS-E-RNF, record not found

> If the service exist you can use the SHOW SERVICE/FULL command to see the details of the service and verify that it is setup properly. Pay special attention to the port number, and the file reference to make sure they are correct

> If there are errors in the service definition we suggest you do the following to remove the corrupted service and then recreate the service using the instructions below.

> (Disable the service)

> TCPIP\> DISABLE SERVICE XMINETMM

> (Remove it from the startup database)

> TCPIP\> SET CONFIG ENABLE NOSERVICE XMINETMM

> (To delete the service)

> TCPIP\> SET NOSERVICE XMINETMM

> Exit the TCP/IP utility with the EXIT command:

> TCPIP\> EXIT

> 999A01\$

2.  We have provided a .com file named XMINET_CREATE_SERVICE.COM to create the XMINETMM service. Run the XMINET_CREATE_SERVICE.COM file from the VMS command prompt to create XMINETMM the service. To use the .Com file, Verify that your Default directory is USER\$:\[XMINET\] with the SHOW DEFAULT command. If your default directory is not correct you will need to SET DEFAULT to USER\$:\[XMINET\]. If you wish to create the service manually, skip to step 4.3

> Note -- The XMINET_CREATE_SERVICE.COM file will set the /file qualifier for the new XMINETMM service to XMINET_CACHE.COM. If you wish the /file qualifier to show the full path of DISK\$:\[XMINET\]XMINET_CACHE.COM you will need to edit the file and add the DISK\$:\[Directory\] information.

> Run the XMINET_CREATE_SERVICE.COM file to create the new service.

> 999A01\$ @XMINET_CREATE_SERVICE.COM

> Creating Service XMINETMM for port 25 with connection limit of 50

> Process Complete.

> Service Port Proto Process Address State

> XMINETMM 25 TCP XMINET 0.0.0.0 Disabled

3.  Alternatively you can create the Service manually with the TCP/IP Utilities as shown below

> Note the use of the continuation character " - " at the end of each line to allow the qualifiers to be entered on more than one line.

> Enter the TCP/IP utilities

> 999A01\$ TCPIP

> Enter the following commands to create the service.

> TCPIP\> SET SERVICE XMINETMM/FILE=XMINET_CACHE.COM/PORT=25/PROCESS_NAME="XMINET" -

> /USER_NAME=XMINET/PROTOCOL=TCP -

> /REJECT=MESSAGE=("421^TOO MANY SMTP CHANNELS ACTIVE")/LIMIT=40

4.  After creating the XMINETMM service use the TCP/IP command SHOW SERVICE XMINETMM\* to verify that the service was created.

> 999A01\$ TCPIP SHOW SERVICE XMINETMM\*

> Service Port Proto Process Address State

> XMINETMM 25 TCP XMINET 0.0.0.0 Disabled

5.  Log onto one of the nodes, where you plan to run the MailMan TCP/IP Service, then enter the TCP/IP utility and enable the new XMINETMM TCP/IP service:

> 999A01\$ TCPIP

> TCPIP\> ENABLE SERVICE XMINETMM

6.  Verify that the service started, and the details are correct with the TCP/IP SHOW SERVICE/FULL command. Pay special attention to the file, port , and Limit fields to make sure they are correct and check the State field to verify that the service is Enabled.

> TCPIP\> SHOW SERVICE/FULL XMINETMM

> Service: XMINETMM

> State: Enabled

> Port: 25 Protocol: TCP Address: 0.0.0.0

> Inactivity: 5 User_name: XMINET Process: XMINET

> Limit: 50 Active: 0 Peak: 0

> File: XMINET_CACHE.COM

> Flags: Listen

> Socket Opts: Rcheck Scheck

> Receive: 0 Send: 0

> Log Opts: None

> File: not defined

> Security

> Reject msg: 421^too many SMTP channels active

> Accept host: 0.0.0.0

> Accept netw: 0.0.0.0

> If the Service definition is correct you can move to step 4.7

> If there are errors in the service definition we suggest you do the following to remove the corrupted service and repeat the steps used to create the service.

> (Disable the service)

> TCPIP\> DISABLE SERVICE XMINETMM

> (Remove it from the startup database)

> TCPIP\> SET CONFIG ENABLE NOSERVICE XMINETMM

> (To delete the service)

> TCPIP\> SET NOSERVICE XMINETMM

7.  If the service is setup properly you should decide which node(s) in the cluster should run the service and enter the service into the TCP/IP permanent configuration database that enables services for startup. On each node where you want to enable the service at Startup you will want to enter the TCP/IP commands below

> Log onto the node(s) where you want the service to run, and then enter the TCP/IP utilities with the TCP/IP command; then enter the TCP/IP commands below:

> (Enable the service)

> TCPIP\> ENABLE SERVICE XMINETMM

> (Save service in the TCP/IP permanent configuration database for reboot)

> TCPIP\> SET CONFIG ENABLE SERVICE XMINETMM

> (Check the service)

> TCPIP\> SHO SERVICE/FULL XMINETMM

> Enter the TCP/IP commands below to display the services configured in the services database that will be enabled by the TCP/IP Services startup procedure.

> (Your list may vary slightly but, it should contain XMINETMM)

> TCPIP\>SHOW CONFIGURATION ENABLE SERVICE

> Enable service:

> FTP, FTP_CLIENT, LPD, MOUNT, NFS, NFS_CLIENT, PCNFS,

> PORTMAPPER, REXEC, RSH, SMTP, SNMP, XMINETMM

> If the service appears to be setup and running you can exit the TCP/IP utilities and move to the next step. If there are problems you will need to review the prior steps and troubleshoot.

4.  Review the new XMINET_CACHE.COM command file to be used for the MailMan TCP/IP service and edit as needed.
    1.  If you used the .com files to create the XMINET user and the XMINETMM service or followed the instructions exactly, the XMINET_CACHE.COM file will be the .COM file invoked when a connection is made to the Listener. Before testing the new service, we suggest you TYPE and review the XMINET_CACHE.COM file for correctness. Pay special attention to the command line section as shown below and make sure the namespace is correct for your configuration. . Most configurations use the VAH namespace but at some Data Centers it might be different. Edit the .COM file, if needed, and make any required changes.

> Note -- You will need to remove the '!' comment character from the command line that Matches your configuration and edit it to reflect the correct \<namespace\> and \<configname\>

\$!-------------------------------------------------------------

\$!-------------------------------------------------------------

\$! for CACHE

\$! Edit only one of the three "csession" lines below.

\$!

\$ assign 'f\$trnlnm("SYS\$NET")' SYS\$NET

\$!

\$! \#1 -- For Test Accounts

\$! If the configname is not the same as the node name, usually a test account,

\$! edit/use the csession line below

\$! Remove the comment character '!' from the beginning of the line.

\$! Replace \<PREFIX\>, including the \<\>, with the proper Test account prefix.

\$! Usually this is T or TST

\$! Replace \<namespace\>, including the \<\> with the correct namespace.

\$! Usually the namespace is TST for a Test account.

\$!

\$! an Example -- \$ csession "T''NODE'" "-U" "TST" "CACHEVMS^XMRUCX"

\$!

\$! csession "\<PREFIX\>''NODE'" "-U" "\<namespace\>" "CACHEVMS^XMRUCX"

\$!

\$! \#2 -- For most Production Accounts.

\$! If your configname is the same as your node name, usually a non-data

\$! center production site, edit/use the cesssion line below.

\$! Remove the comment character '!' from the beginning of the line.

\$! Replace \<namespace\>, including the \<\>, with the correct namespace,

\$! Usually the namespace is "VAH" for production.

\$!

\$! an Example -- \$ csession "''NODE'" "-U" "VAH" "CACHEVMS^XMRUCX"

\$!

\$! csession "''NODE'" "-U" "\<namespace\>" "CACHEVMS^XMRUCX"

\$!

\$! \#3 -- for Data-Center Production Accounts

\$! For a production Data Center site, edit/use the csession line below.

\$! Remove the comment character '!' from the beginning of the line.

\$! Replace \<NSP\>, including the \<\>, with the proper site prefix.

\$! Replace \<namespace\>, including the \<\> with the correct namespace.

\$! Usually the namespace is the same as the value used for NSP.

\$!

\$! an Example -- \$ csession "BRX''NODE'" "-U" "BRX" "CACHEVMS^XMRUCX"

\$!

\$! csession "\<NSP\>''NODE'" "-U" "\<namespace\>" "CACHEVMS^XMRUCX"

\$!

\$!-------------------------------------------------------------

\$!-------------------------------------------------------------

6.  Attempt a connection to test the XMINETMM Service.

> The best method to test the XMINETMM service is to attempt to connect to a node running the service at port number 25. This is where the service listens for connection requests. Log onto any node in the cluster and attempt to Telnet to a Node in the cluster, which has the service enabled, at the designated port number and make sure it connects properly. An example is shown below.

> Telnet to the node and request a connection to a specific port

> The format on a VMS system is TELNET \<IP address\> \<Port#\>

> (An example using the REDACTED OI system at port 25)

> \$ TELNET 10.4.21.1 25

> (The request is allowed and VistA MailMan Answers)

> %TELNET-I-TRYING, Trying ... 10.4.21.1

> %TELNET-I-SESSION, Session 01, host 10.4.21.1, port 25

> 220 REDACTEDMailMan 8.0 ready

> (Type QUIT to drop the connection)

> QUIT

> 221 REDACTEDService closing transmission channel

> %TELNET-S-REMCLOSED, Remote connection closed

> -TELNET-I-SESSION, Session 01, host 10.4.21.1, port 25

> If the connection test is successful you can try sending mail from another Vista system, such as FORUM, to your system to verify that the service is working.

7.  If the connection test fails you should first look at the .LOG files, which are created in the DEFAULT directory for the service. If you followed the instructions explicitly the DEFAULT directory will be USER\$:\[XMINET\]. You can then TYPE and review the .LOG files for hints about what went wrong. Another valuable source of information is the VISTA error trap. If a review of both of these fails to yield an answer we suggest you log a NOIS call and the appropriate HSITES support team will contact you

8\. How to Control the Number of Log Files Created by TCP/IP.

> The XMINETMM TCP/IP service automatically creates log files in the \[XMINET\] directory named XMINET_CACHE.LOG;xxx (where "xxx" is a file version number). TCP/IP does this, and it cannot be prevented. The XMINET_CACHE.COM file will purge extra log files as part of its running. New versions of the log file will be created until that file version number reaches the maximum number of 32767. This can be used to limit the number of log files by explicitly setting the log file to the highest version number (32767) on the XMINET_CACHE.LOG file. This results in the XMINET_CACHE.LOG file being renamed to XMINET_CACHE.LOG;32767, and no further versions of this log file are created. If a system manager needs to see the log file contents of new connections, they can rename that file to a lower version such as XMINET_CACHE.LOG;32760 and let new log files be created.

> It is recommended that you not limit the number of versions of the log file until you know that your XMINETMM service is working correctly; keeping the log files can help when diagnosing problems with the service/account.

> (Renaming to the highest version number)

> 999A01\$ SHOW DEFAULT

> USER\$:\[XMINET\]

> The format is RENAME OldFileName NewFileName

> 999A01\$ RENAME XMINET_CACHE.LOG XMINET_CACHE.LOG;32767You are done -- Stop.

# # Appendix A -- Copies of what the VMS User Account and Service look like

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The XMINET VMS User Account:

> Username: XMINET Owner: XMINET

> Account: NETWORK UIC: \[50,50\] (\[XMINET\])

> CLI: DCL Tables: DCLTABLES

> Default: USER\$:\[XMINET\]

> LGICMD: NL:

> Flags: DisCtlY Restricted DisWelcome DisNewMail DisMail DisReport

> Primary days: Mon Tue Wed Thu Fri

> Secondary days: Sat Sun

> Primary 000000000011111111112222 Secondary 000000000011111111112222

> Day Hours 012345678901234567890123 Day Hours 012345678901234567890123

> Network: \##### Full access \###### \##### Full access \######

> Batch: ----- No access ------ ----- No access ------

> Local: ----- No access ------ ----- No access ------

> Dialup: ----- No access ------ ----- No access ------

> Remote: ----- No access ------ ----- No access ------

> Expiration: (none) Pwdminimum: 6 Login Fails: 0

> Pwdlifetime: 90 00:00 Pwdchange: (pre-expired)

> Last Login: (none) (interactive), (none) (non-interactive)

> Maxjobs: 0 Fillm: 300 Bytlm: 120000

> Maxacctjobs: 0 Shrfillm: 0 Pbytlm: 0

> Maxdetach: 0 BIOlm: 1024 JTquota: 4096

> Prclm: 32 DIOlm: 2048 WSdef: 13000

> Prio: 4 ASTlm: 2098 WSquo: 20000

> Queprio: 4 TQElm: 10 WSextent: 65536

> CPU: (none) Enqlm: 3005 Pgflquo: 120000

> Authorized Privileges:

> NETMBX TMPMBX

> Default Privileges:

> NETMBX TMPMBX

The XMINETMM TCP/IP MailMan Service:

> Service: XMINETMM

> State: Enabled

> Port: 25 Protocol: TCP Address: 0.0.0.0

> Inactivity: 5 User_name: XMINET Process: XMINET

> Limit: 50 Active: 0 Peak: 0

> File: XMINET_CACHE.COM

> Flags: Listen

> Socket Opts: Rcheck Scheck

> Receive: 0 Send: 0

> Log Opts: None

> File: not defined

> Security

> Reject msg: 421^too many SMTP channels active

> Accept host: 0.0.0.0

> Accept netw: 0.0.0.0

# Appendix B -- Copy of the .com file to create the XMINET VMS User account

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\$!XMINET_CREATE_UAF.COM

\$! This command file creates a XMINET user in the authorize file.

\$! Two questions will be asked, the UIC

\$! and the default device.

\$! ctt/hisc 11-february-1993

\$! ================================================

\$! 11/16/94 mods for XMINET by jd/washisc 11/16/94

\$!

\$! 03-02-05 mods for patch XM\*8\*29 to resemble CACHEMGR

\$! account at VMS/CACHE sites per conversion

\$! document page 12 by REDACTED @ OI-REDACTED

\$! ================================================

\$writeo :== write sys\$output

\$UIC:

\$writeo ""

\$writeo ""

\$writeo "This will create a VMS user account called XMINET."

\$writeo "It will prompt for a UIC, and a DEVICE/DISK\$:"

\$writeo "It will then create the VMS user and set it's"

\$writeo "Default directory to DISK\$:\[XMINET\]"

\$writeo ""

\$writeo "You can also enter ^ to exit the process"

\$writeo ""

\$inquire XMINET_uic "Enter the UIC for XMINET (i.e. \[50,153\]) "

\$if (XMINET_uic .eqs. "") .or. (XMINET_uic .eqs. "^") then goto exit

\$if f\$locate("\[","''XMINET_uic'") .eq. f\$length("''XMINET_uic'") .or. -

f\$locate("\]","''XMINET_uic'") .eq. f\$length("''XMINET_uic'") .or. -

f\$locate(",","''XMINET_uic'") .eq. f\$length("''XMINET_uic'") .or. -

f\$locate("8","''XMINET_uic'") .ne. f\$length("''XMINET_uic'") .or. -

f\$locate("9","''XMINET_uic'") .ne. f\$length("''XMINET_uic'")

\$then

\$ writeo ""

\$ writeo "Error --- Invalid UIC value or format."

\$ goto uic

\$endif

\$!

\$DEVICE:

\$writeo ""

\$writeo "Enter the default device/disk for XMINET - make sure to include the :"

\$writeo "Generally, this will be USER\$:"

\$writeo ""

\$writeo "You can also enter ^ to exit the process"

\$writeo ""

\$inquire/nopunc XMINET_dev "Enter the device (device:) "

\$if (XMINET_dev .eqs. "") .or. (XMINET_dev .eqs. "^") then goto exit

\$! Make sure the Device Specification contains a colon:

\$!

\$if f\$locate(":","''XMINET_dev'") .eq. f\$length("''XMINET_dev'")

\$then

\$ writeo ""

\$ writeo "Error --- device must contain a : "

\$ goto device

\$endif

\$! Make sure the chosen Disk/Directory a format is correct and the

\$! Device Exists on the system

\$if f\$getdvi("''XMINET_dev'","exists") .eqs. "FALSE"

\$ then

\$ writeo ""

\$ writeo "Error --- Device/Disk ''XMINET_dev' does not exist."

\$ goto device

\$endif

\$writeo ""

\$!

\$!

\$!

\$open/write XMINET_file XMINET_uaf.tmp

\$write/error=werr XMINET_file "\$run sys\$system:authorize"

\$write/error=werr XMINET_file "add XMINET/owner=XMINET -"

\$write/error=werr XMINET_file "/uic=''XMINET_uic'/device=''XMINET_dev' -"

\$write/error=werr XMINET_file "/account=NETWORK/dir=\[XMINET\]/lgicmd=NL: -"

\$write/error=werr XMINET_file "/flags=(disctly,restricted,diswelcome, -"

\$write/error=werr XMINET_file "disnewmail,disreport,dismail,nodisuser) -"

\$write/error=werr XMINET_file "/primary=(mon,tue,wed,thur,fri,nosat,nosun) -"

\$write/error=werr XMINET_file "/prclm=32/fillm=300/biolm=1024/diolm=2048 -"

\$write/error=werr XMINET_file "/enqlm=3005/queprio=4 -"

\$write/error=werr XMINET_file "/bytlm=120000/wsdef=13000/wsquo=20000 -"

\$write/error=werr XMINET_file "/wsextent=65536 -"

\$write/error=werr XMINET_file "/astlm=2098/Jtquota=4096/prio=4/pgflquo=120000 -"

\$write/error=werr XMINET_file "/priv=(tmpmbx,netmb) -"

\$write/error=werr XMINET_file "/defpriv=(tmpmbx,netmb) -"

\$write/error=werr XMINET_file "/network/nobatch/nolocal/nodialup/noremote"

\$write/error=werr XMINET_file "show XMINET"

\$write/error=werr XMINET_file "exit"

\$close XMINET_file

\$@XMINET_uaf.tmp

\$delete/nolog/noconf XMINET_uaf.tmp;\*

\$! Make the new account the owner of the \[XMINET\] directory

\$writeo ""

\$writeo "Making the XMINET account the owner of the "

\$writeo "''XMINET_dev'\[XMINET\] directory"

\$set file/owner='XMINET_uic' 'XMINET_dev'\[000000\]XMINET.dir

\$writeo ""

\$writeo "Process complete. New account XMINET created"

\$writeo ""

\$goto exit

\$WERR:

\$writeo "Error --- Unable to write to tmp file."

\$EXIT:

\$ exit

# # Appendix C -- Copy of the .com file to create the TCP/IP Service

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\$! XMINET_CREATE_SERVICE.COM

\$! Creates the XMINETMM Service for VMS/CACHE sites.

\$! Uses port \#25 by default. To Change alter the /port=nn

\$! qualifier

\$! -----------------------------------------

\$! Revision History

\$! Date Description

\$!------------------------------------------

\$! 11/16/94 mods for XMINET by REDACTED 11/16/94

\$! 10/20/04 XM\*8\*29 copy/mod by OI-REDACTED

\$!

\$! -----------------------------------------

\$! For output

\$writeo :== write sys\$output

\$writeo ""

\$writeo "Creating Service XMINETMM for port 25 with connection limit of 50

\$writeo ""

\$TCPIP set service xminetmm/file=xminet_cache.com/port=25/process_name="xminet" -

/user_name=XMINET/protocol=tcp -

/Reject=message=("421^too many SMTP channels active") -

/limit=50/LOG_OPTIONS=Addr

\$writeo ""

\$writeo "Process Complete."

\$writeo ""

\$TCPIP show service XMINETMM

\$!ucx enable service xminetmm

\$EXIT

# Appendix D -- Copy of the .com file used by the Service 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

\$!XMINET_CACHE.COM - for incoming connect requests

\$!Revision History

\$!Date Description

\$!-------------------------------------------------------------

\$! 03/28/05 XM\*8\*29 by acl/OI-REDACTED copy/mod of

\$! XWBSERVER_start.COM from XWB\*1.1\*35

\$!

\$!

\$!

\$!-------------------------------------------------------------

\$ set noon !Don't stop

\$ set noverify !change as needed

\$! set verify !change as needed

\$ say :== write sys\$output

\$! Purge at end

\$!

\$ dev=f\$trnlnm("sys\$net") !This is our MBX device

\$ NODE=F\$EDIT(F\$GETSYI("SCSNODE"),"COLLAPSE,TRIM") !Node Name

\$!

\$ say "Opening " + dev !This can be viewed in the log file

\$!

\$! With TCPIP Services for OpenVMS 5.3 ECO \#2 or higher,

\$! the below section can be removed.

\$!

\$! Check status of the BG device before going to VistA

\$ cnt=0

\$ CHECK:

\$ stat=f\$getdvi("''dev'","STS")

\$ if cnt .eq. 100

\$ then

\$ say "Could not open ''dev' - exiting"

\$ goto EXIT

\$ else

\$ if stat .ne. 16

\$ then

\$ cnt=cnt+1

\$ say "Stat: ''stat' Cnt:''cnt' Dev: ''dev' not ready!"

\$ wait 00:00:01 !Wait one second to assure connection

\$ goto CHECK

\$ else

\$ endif

\$ endif

\$! End of TCPIP Services for OpenVMS 5.3 ECO \#2 or higher, removal

\$!

\$!-------------------------------------------------------------

\$ bg == f\$extract(1,f\$locate(":",dev)-1,dev)

\$ PIPE TCPIP SHOW DEVICE 'bg \| SEARCH SYS\$INPUT "''bg'" \| -

(READ SYS\$INPUT host ; ip = f\$extract(55,15,host) ; define/job ip &ip) -

&& ip=f\$trnlnm("ip")

\$!

\$ define VistA\$IP "''ip'"

\$!-------------------------------------------------------------

\$ say "''dev' from host ''ip' is now ready for use."

\$!-------------------------------------------------------------

\$! \*\*Be sure the command line(s) in the COMMAND LINE SECTION

\$! \*\*below is correct for your system and if access control is enabled,

\$! \*\*that this account has access to this uci,vol & routine.

\$!

\$!-------------------------------------------------------------

\$! COMMAND LINE SECTION:

\$! =====================

\$! anything in \<\> needs to be replaced,including the \<\>, with local data

\$!-------------------------------------------------------------

\$! for DSM

\$! dsm/env=\<dsmmgr\>/uci=\<vah\>/vol=\<rou\> SOC^XMRUCX

\$!-------------------------------------------------------------

\$!-------------------------------------------------------------

\$! for CACHE

\$! Edit only one of the three "csession" lines below.

\$!

\$ assign 'f\$trnlnm("SYS\$NET")' SYS\$NET

\$!

\$! \#1 -- For Test Accounts

\$! If the configname is not the same as the node name, usually a test account,

\$! edit/use the csession line below

\$! Remove the comment character '!' from the beginning of the line.

\$! Replace \<PREFIX\>, including the \<\>, with the proper Test account prefix.

\$! Usually this is T or TST

\$! Replace \<namespace\>, including the \<\> with the correct namespace.

\$! Usually the namespace is TST for a Test account.

\$!

\$! an Example -- \$ csession "T''NODE'" "-U" "TST" "CACHEVMS^XMRUCX"

\$!

\$! csession "\<PREFIX\>''NODE'" "-U" "\<namespace\>" "CACHEVMS^XMRUCX"

\$!

\$! \#2 -- For most Production Accounts.

\$! If your configname is the same as your node name, usually a non-data

\$! center production site, edit/use the cesssion line below.

\$! Remove the comment character '!' from the beginning of the line.

\$! Replace \<namespace\>, including the \<\>, with the correct namespace,

\$! Usually the namespace is "VAH" for production.

\$!

\$! an Example -- \$ csession "''NODE'" "-U" "VAH" "CACHEVMS^XMRUCX"

\$!

\$! csession "''NODE'" "-U" "\<namespace\>" "CACHEVMS^XMRUCX"

\$!

\$! \#3 -- for Data-Center Production Accounts

\$! For a production Data Center site, edit/use the csession line below.

\$! Remove the comment character '!' from the beginning of the line.

\$! Replace \<NSP\>, including the \<\>, with the proper site prefix.

\$! Replace \<namespace\>, including the \<\> with the correct namespace.

\$! Usually the namespace is the same as the value used for NSP.

\$!

\$! an Example -- \$ csession "BRX''NODE'" "-U" "BRX" "CACHEVMS^XMRUCX"

\$!

\$! csession "\<NSP\>''NODE'" "-U" "\<namespace\>" "CACHEVMS^XMRUCX"

\$!

\$!-------------------------------------------------------------

\$!-------------------------------------------------------------

\$!

\$ exit:

\$ purge/keep=100 sys\$login:\*.log !Purge log files only

\$ logout/brief