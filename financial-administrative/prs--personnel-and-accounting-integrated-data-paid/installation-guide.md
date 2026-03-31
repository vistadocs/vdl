---
title: PAID Version 4 Installation Guide
doc_type: IG
doc_label: Installation Guide
doc_layer: anchor
doc_subject: 
app_code: PRS
app_name: Personnel and Accounting Integrated Data (PAID)
section: FIN
app_status: active
pkg_ns: PRS
patch_ver: 4
patch_id: PRS*4
group_key: "PRS:PRS:4"
file_numbers: []
security_keys: []
menu_options: 0
description: The Personnel and Accounting Integrated Data (PAID) distribution medium contains a file of routines. All of these routines begin with the PAID namespace PRS. All globals, options and keys created during the initialization process also begin with PRS. All PAID files have file numbers in the 450-459 n
audience: 
keywords: 
  - prsin
  - filed
  - prsa
  - prse
  - paid
  - prsd
  - prsdld
  - employee
  - prseed
  - prsdeu
page_count: 0
word_count: 2600
section_count: 0
table_count: 0
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: August 1995
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Pers_Acctg_Integ_Data_(PAID)/paid_ig.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Pers_Acctg_Integ_Data_(PAID)/paid_ig.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=51"
---

Decentralized Hospital Computer Program

PERSONNEL AND ACCOUNTING INTEGRATED DATA(PAID)INSTALLATION GUIDE

August 1995

Hines IRM Field Office

Hines, Illinois

Installation

The Personnel and Accounting Integrated Data (PAID) distribution medium contains a file of routines. All of these routines begin with the PAID namespace PRS. All globals, options and keys created during the initialization process also begin with PRS. All PAID files have file numbers in the 450-459 number range as assigned by the DBA.

PAID V. 4.0 contains a partial definition of the New Person file \#200. This partial definition will create a new field (PAID EMPLOYEE \#450) which is a pointer to the PAID Employee file \#450 and a new MUMPS cross-reference (AJ) on the SSN field \#9. These additions to the New Person file have been approved by the DBA and the Kernel developers.

This package minimally requires Kernel V. 7.0 or later and VA FileMan V. 21.0

or later. Kernel V. 8.0 is required to utilize the sign-on alerts portion of PAID 4.0. PAID 4.0 may be installed and used without this functionality. (Note: For those sites running Kernel V. 7.0, an index will show a fatal error until you install Kernel V. 8.0. This will not affect the way the package operates.)

It is not necessary to disable the system during the PAID 4.0 initialization. Initialization should not be done while users of the current version of the PAID package are entering data or transmitting data to the Austin Automation

Center. Installation will take approximately 45-60 minutes.

Installation:For all DHCP PAID V. 3.5 sites, this version must be installed after October 4, 1995 and before October 13, 1995.

1\) Disable mapping for any PRS routines. Mapping is not recommended for any PRS routines.

2\) Load the new routines into your account.

PRS8 PRS8AC PRS8CR PRS8CV PRS8DR PRS8EX PRS8EX0 PRS8HD

PRS8HR PRS8MISC PRS8MSC0 PRS8MT PRS8OC PRS8OT PRS8PP PRS8SB

PRS8ST PRS8SU PRS8TL PRS8TL1 PRS8UP PRS8UT PRS8VW PRS8VW1

PRS8VW2 PRS8WE PRS8WE2 PRSACED PRSACED1 PRSACED2 PRSACED3 PRSACED4

PRSACED5 PRSACED6 PRSADP PRSADP1 PRSADP2 PRSADPA PRSAEDL PRSAEDR

PRSAEDS PRSAENE PRSAENT PRSAENX PRSAES PRSALVB PRSALVE PRSALVL

PRSALVR PRSALVS PRSALVT PRSALVU PRSALVX PRSAOTE PRSAOTL PRSAOTR

PRSAOTS PRSAOTX PRSAPAS PRSAPEH PRSAPEM PRSAPEX PRSAPPH PRSAPPO

PRSAPPP PRSAPPQ PRSAPPU PRSAPPX PRSAPRE PRSAPRT PRSAPT1 PRSARPT2

PRSASAL PRSASC PRSASC1 PRSASC2 PRSASC3 PRSASR PRSASR1 PRSASU

PRSATAPE PRSATD1 PRSATD2 PRSATE PRSATE0 PRSATE1 PRSATE2 PRSATE3

PRSATE4 PRSATE5 PRSATEV PRSATH PRSATIM PRSATL PRSATP PRSATP0

PRSATP1 PRSATP2 PRSATPD PRSATPE PRSATPF PRSATPG PRSATPH PRSATPL

PRSATPP PRSATPX PRSATVC PRSAUD PRSAUDP PRSAUTL PRSAXMIT PRSAXSR

PRSD1150 PRSD450 PRSDADD PRSDAH PRSDAH1 PRSDAH2 PRSDAH3 PRSDAH4

PRSDCOMP PRSDDL PRSDENG PRSDERR PRSDEU01 PRSDEU02 PRSDEU03 PRSDEU04

PRSDEU05 PRSDEU06 PRSDEU07 PRSDEU08 PRSDEU09 PRSDEU10 PRSDEU11 PRSDEU12

PRSDFIL PRSDFOLL PRSDLD01 PRSDLD02 PRSDLD03 PRSDLD04 PRSDLD05 PRSDLD06

PRSDLD07 PRSDLD08 PRSDLD09 PRSDLD10 PRSDLD11 PRSDLD12 PRSDLD13 PRSDLD14

PRSDLD15 PRSDLD16 PRSDLD17 PRSDMISC PRSDPR01 PRSDPR02 PRSDPR03 PRSDPR04

PRSDPR05 PRSDPR06 PRSDPR07 PRSDPR08 PRSDPRIN PRSDPRNT PRSDPROC PRSDPTYP

PRSDRPT PRSDSERV PRSDSET PRSDSRC PRSDSRC1 PRSDSRC2 PRSDSRP PRSDSRP1

PRSDSRP2 PRSDSRP3 PRSDSRS PRSDSTAT PRSDUTIL PRSDV450 PRSDV459 PRSDVTBL

PRSDW450 PRSDXREF PRSDYTD PRSE PRSECAL PRSEDEL PRSEDEL1 PRSEDESC

PRSEED0 PRSEED1 PRSEED10 PRSEED12 PRSEED13 PRSEED14 PRSEED2 PRSEED3

PRSEED4 PRSEED5 PRSEED6 PRSEED7 PRSEED8 PRSEED9 PRSEEMP PRSEEMP1

PRSEEMP2 PRSEKILL PRSEMSG PRSEPMC PRSEPMD1 PRSEPMD4 PRSEPMD5 PRSEPMD6

PRSEPOL0 PRSEPOL1 PRSEPRG0 PRSERSTR PRSEUTL PRSEUTL1 PRSEUTL2 PRSEUTL3

PRSEUTL4 PRSEUTL5 PRSEUTL6 PRSIKIL PRSIN001 PRSIN002 PRSIN003 PRSIN004

PRSIN005 PRSIN006 PRSIN007 PRSIN008 PRSIN009 PRSIN00A PRSIN00B PRSIN00C

PRSIN00D PRSIN00E PRSIN00F PRSIN00G PRSIN00H PRSIN00I PRSIN00J PRSIN00K

PRSIN00L PRSIN00M PRSIN00N PRSIN00O PRSIN00P PRSIN00Q PRSIN00R PRSIN00S

PRSIN00T PRSIN00U PRSIN00V PRSIN00W PRSIN00X PRSIN00Y PRSIN00Z PRSIN010

PRSIN011 PRSIN012 PRSIN013 PRSIN014 PRSIN015 PRSIN016 PRSIN017 PRSIN018

PRSIN019 PRSIN01A PRSIN01B PRSIN01C PRSIN01D PRSIN01E PRSIN01F PRSIN01G

PRSIN01H PRSIN01I PRSIN01J PRSIN01K PRSIN01L PRSIN01M PRSIN01N PRSIN01O

PRSIN01P PRSIN01Q PRSIN01R PRSIN01S PRSIN01T PRSIN01U PRSIN01V PRSIN01W

PRSIN01X PRSIN01Y PRSIN01Z PRSIN020 PRSIN021 PRSIN022 PRSIN023 PRSIN024

PRSIN025 PRSIN026 PRSIN027 PRSIN028 PRSIN029 PRSIN02A PRSIN02B PRSIN02C

PRSIN02D PRSIN02E PRSIN02F PRSIN02G PRSIN02H PRSIN02I PRSIN02J PRSIN02K

PRSIN02L PRSIN02M PRSIN02N PRSIN02O PRSIN02P PRSIN02Q PRSIN02R PRSIN02S

PRSIN02T PRSIN02U PRSIN02V PRSIN02W PRSIN02X PRSIN02Y PRSIN02Z PRSIN030

PRSIN031 PRSIN032 PRSIN033 PRSIN034 PRSIN035 PRSIN036 PRSIN037 PRSIN038

PRSIN039 PRSIN03A PRSIN03B PRSIN03C PRSIN03D PRSIN03E PRSIN03F PRSIN03G

PRSIN03H PRSIN03I PRSIN03J PRSIN03K PRSIN03L PRSIN03M PRSIN03N PRSIN03O

PRSIN03P PRSIN03Q PRSIN03R PRSIN03S PRSIN03T PRSIN03U PRSIN03V PRSIN03W

PRSIN03X PRSIN03Y PRSIN03Z PRSIN040 PRSIN041 PRSIN042 PRSIN043 PRSIN044

PRSIN045 PRSIN046 PRSIN047 PRSIN048 PRSIN049 PRSIN04A PRSIN04B PRSIN04C

PRSIN04D PRSIN04E PRSIN04F PRSIN04G PRSIN04H PRSIN04I PRSIN04J PRSIN04K

PRSIN04L PRSIN04M PRSIN04N PRSIN04O PRSIN04P PRSIN04Q PRSIN04R PRSIN04S

PRSIN04T PRSIN04U PRSIN04V PRSIN04W PRSIN04X PRSIN04Y PRSIN04Z PRSIN050

PRSIN051 PRSIN052 PRSIN053 PRSIN054 PRSIN055 PRSIN056 PRSIN057 PRSIN058

PRSIN059 PRSIN05A PRSIN05B PRSIN05C PRSIN05D PRSIN05E PRSIN05F PRSIN05G

PRSIN05H PRSIN05I PRSIN05J PRSIN05K PRSIN05L PRSIN05M PRSIN05N PRSIN05O

PRSIN05P PRSIN05Q PRSIN05R PRSIN05S PRSIN05T PRSIN05U PRSIN05V PRSIN05W

PRSIN05X PRSIN05Y PRSIN05Z PRSIN060 PRSIN061 PRSIN062 PRSIN063 PRSIN064

PRSIN065 PRSIN066 PRSIN067 PRSIN068 PRSIN069 PRSIN06A PRSIN06B PRSIN06C

PRSIN06D PRSIN06E PRSIN06F PRSIN06G PRSIN06H PRSIN06I PRSIN06J PRSIN06K

PRSIN06L PRSIN06M PRSIN06N PRSIN06O PRSIN06P PRSIN06Q PRSIN06R PRSIN06S

PRSIN06T PRSIN06U PRSIN06V PRSIN06W PRSIN06X PRSIN06Y PRSIN06Z PRSIN070

PRSIN071 PRSIN072 PRSIN073 PRSIN074 PRSIN075 PRSIN076 PRSIN077 PRSIN078

PRSIN079 PRSIN07A PRSIN07B PRSIN07C PRSIN07D PRSIN07E PRSIN07F PRSIN07G

PRSIN07H PRSIN07I PRSIN07J PRSIN07K PRSIN07L PRSIN07M PRSIN07N PRSIN07O

PRSIN07P PRSIN07Q PRSIN07R PRSIN07S PRSIN07T PRSIN07U PRSIN07V PRSIN07W

PRSIN07X PRSIN07Y PRSIN07Z PRSIN080 PRSIN081 PRSIN082 PRSIN083 PRSIN084

PRSIN085 PRSIN086 PRSIN087 PRSIN088 PRSIN089 PRSIN08A PRSIN08B PRSIN08C

PRSIN08D PRSIN08E PRSIN08F PRSIN08G PRSIN08H PRSIN08I PRSIN08J PRSIN08K

PRSIN08L PRSIN08M PRSIN08N PRSIN08O PRSIN08P PRSIN08Q PRSIN08R PRSIN08S

PRSIN08T PRSIN08U PRSIN08V PRSIN08W PRSIN08X PRSIN08Y PRSIN08Z PRSIN090

PRSIN091 PRSIN092 PRSIN093 PRSIN094 PRSIN095 PRSIN096 PRSIN097 PRSIN098

PRSIN099 PRSIN09A PRSIN09B PRSIN09C PRSIN09D PRSIN09E PRSIN09F PRSIN09G

PRSIN09H PRSIN09I PRSIN09J PRSIN09K PRSIN09L PRSIN09M PRSIN09N PRSIN09O

PRSIN09P PRSIN09Q PRSIN09R PRSIN09S PRSIN09T PRSIN09U PRSIN09V PRSIN09W

PRSIN09X PRSIN09Y PRSIN09Z PRSIN0A0 PRSIN0A1 PRSIN0A2 PRSIN0A3 PRSINIS

PRSINIT PRSINIT1 PRSINIT2 PRSINIT3 PRSINIT4 PRSINIT5 PRSIPRE PRSIPST

PRSIPST1 PRSIPST2 PRSNTEG PRSNTEG0 PRSRASOR PRSRAU1 PRSRAU11 PRSREX1

PRSREX11 PRSRL1 PRSRL11 PRSRL12 PRSRL2 PRSRL21 PRSRL4 PRSRL41

PRSRLL PRSRLSOR PRSROSOR PRSROT1 PRSROT11 PRSRPSOR PRSRTLPR PRSRUT0

PRSRUTL

3\) Initialize the package by executing the PRSINIT routine. There are pre- and post-initialization routines. Be sure to answer "NO" each time the question "Want my data merged with yours?" is asked.

A sample installation dialog is shown below.

D ^PRSINIT

This version (#4.0)of ^PRSINIT' was created on 15-JUN-1995

(at HISC, by VA FileMan V.21.0)

I AM GOING TO SET UP THE FOLLOWING FILES:

200 NEW PERSON (Partial Definition)

> **NOTE:** You already have the 'NEW PERSON' File.

450 PAID EMPLOYEE

> **NOTE:** You already have the 'PAID EMPLOYEE' File.

450.11 PAID DOWNLOAD MESSAGE ERROR

> **NOTE:** You already have the 'PAID DOWNLOAD MESSAGE ERROR' File.

450.12 PAID DOWNLOAD MESSAGE

> **NOTE:** You already have the 'PAID DOWNLOAD MESSAGE' File.

452 PRSE STUDENT EDUCATION TRACKING

> **NOTE:** You already have the 'PRSE STUDENT EDUCATION TRACKING' File.

452.1 PRSE PROGRAM/CLASS

> **NOTE:** You already have the 'PRSE PROGRAM/CLASS' File.

452.2 PRSE EDUCATION PROGRAM/CLASS SUPPLIER

> **NOTE:** You already have the 'PRSE EDUCATION PROGRAM/CLASS SUPPLIER' File.

452.3 PRSE MANDATORY TRAINING (MI) CLASS GROUP

> **NOTE:** You already have the 'PRSE MANDATORY TRAINING (MI) CLASS GROUP' File.

452.4 PRSE EDUCATION PROGRAM/CLASS CATEGORY (including data)

> **NOTE:** You already have the 'PRSE EDUCATION PROGRAM/CLASS CATEGORY' File.

I will OVERWRITE your data with mine.

452.5 PRSE EDUCATION PRESENTATION MEDIA

> **NOTE:** You already have the 'PRSE EDUCATION PRESENTATION MEDIA' File.

452.51 PRSE EMPLOYEE PURPOSE OF TRAINING (including data)

> **NOTE:** You already have the 'PRSE EMPLOYEE PURPOSE OF TRAINING' File.

I will OVERWRITE your data with mine.

452.6 PRSE SVC REASONS FOR TRAINING

> **NOTE:** You already have the 'PRSE SVC REASONS FOR TRAINING' File.

452.7 PRSE PARAMETERS

> **NOTE:** You already have the 'PRSE PARAMETERS' File.

452.8 PRSE EDUCATION REGISTRATION

> **NOTE:** You already have the 'PRSE EDUCATION REGRISTRATION' File.

452.9 PRSE EDUCATION ACCREDITATION ORGANIZATIONS (including data)

> **NOTE:** You already have the 'PRSE EDUCATION ACCREDITATION ORGANIZATIONS' File.

Want my data merged with yours? NO

454 PAID CODE FILES (including data)

> **NOTE:** You already have the 'PAID CODE FILES' File.

Want my data merged with yours? NO

454.1 PAID COST CENTER/ORGANIZATION (including data)

> **NOTE:** You already have the 'PAID COST CENTER/ORGANIZATION' File.

Want my data merged with yours? NO

455.1 8B ERROR MESSAGE (including data)

> **NOTE:** You already have the '8B ERROR MESSAGE' File.

I will OVERWRITE your data with mine.

455.5 T&L UNIT

> **NOTE:** You already have the 'T&L UNIT' File.

457.1 TOUR OF DUTY (including data)

> **NOTE:** You already have the 'TOUR OF DUTY' File.

Want my data merged with yours? NO

457.2 SPECIAL TOUR INDICATOR (including data)

> **NOTE:** You already have the the 'SPECIAL TOUR INDICATOR' File.

I will OVERWRITE your data with mine.

457.3 TYPE OF TIME (including data)

> **NOTE:** You already have the 'TYPE OF TIME' File.

I will OVERWRITE your data with mine.

457.4 TIME REMARKS (including data)

> **NOTE:** You already have the 'TIME REMARKS' File.

I will OVERWRITE your data with mine.

457.5 PAY ENTITLEMENT (including data)

> **NOTE:** You already have the 'PAY ENTITLEMENT' File.

I will OVERWRITE your data with mine.

457.6 ENVIRONMENTAL DIFFERENTIALS (including data)

> **NOTE:** You already have the 'ENVIRONMENTAL DIFFERENTIALS' File.

I will OVERWRITE your data with mine.

458 TIME & ATTENDANCE RECORDS

> **NOTE:** You already have the 'TIME & ATTENDANCE RECORDS' File.

458.1 LEAVE REQUESTS

> **NOTE:** You already have the 'LEAVE REQUESTS' File.

458.2 OT/CT REQUESTS

> **NOTE:** You already have the 'OT/CT REQUESTS' File.

458.3 ENVIRONMENTAL DIFF. REQUESTS

> **NOTE:** You already have the 'ENVIRONMENTAL DIFF. REQUESTS' File.

458.5 PRIOR PP EXCEPTIONS

> **NOTE:** You already have the 'PRIOR PP EXCEPTIONS' File.

459 PAID PAYRUN DATA

> **NOTE:** You already have the 'PAID PAYRUN DATA' File.

SHALL I WRITE OVER FILE SECURITY CODES? No// YES

> **NOTE:** This package also contains BULLETINS

SHALL I WRITE OVER EXISTING BULLETINS OF THE SAME NAME? YES// YES

> **NOTE:** This package also contains FORMS

SHALL I WRITE OVER EXISTING FORMS OF THE SAME NAME? YES// YES

> **NOTE:** This package also contains SECURITY KEYS

SHALL I WRITE OVER EXISTING SECURITY KEYS OF THE SAME NAME? YES// YES

> **NOTE:** This package also contains OPTIONS

SHALL I WRITE OVER EXISTING OPTIONS OF THE SAME NAME? YES// YES

ARE YOU SURE EVERYTHING'S OK? NO// YES

...SORRY, THIS MAY TAKE A FEW MOMENTS........................... ................................................................ ................................................................................................................................

................................................................................................................................

................................................................

'PRSA LV TK' BULLETIN FILED -- Remember to add mail groups for new bulletins...................................................

................................................................

'PRSA ED CAN' Option Filed

'PRSA ED LST' Option Filed

'PRSA ED LST-SUP' Option Filed

'PRSA ED REQ' Option Filed

'PRSA ED/VCS' Option Filed

'PRSA EDIT' Option Filed

'PRSA EMP MENU' Option Filed

'PRSA EN EMP' Option Filed

'PRSA EN TAB' Option Filed

'PRSA LV BAL-EMP' Option Filed

'PRSA LV BAL-SUP' Option Filed

'PRSA LV BAL-TK' Option Filed

'PRSA LV CAN' Option Filed

'PRSA LV DISP' Option Filed

'PRSA LV EDIT' Option Filed

'PRSA LV LST' Option Filed

'PRSA LV LST-SUP' Option Filed

'PRSA LV PAY' Option Filed

'PRSA LV REQ' Option Filed

'PRSA OT APP' Option Filed

'PRSA OT CAN' Option Filed

'PRSA OT EDIT' Option Filed

'PRSA OT LST' Option Filed

'PRSA OT LST-SUP' Option Filed

'PRSA OT MENU' Option Filed

'PRSA OT PAY' Option Filed

'PRSA OT REQ' Option Filed

'PRSA PAY ASX' Option Filed

'PRSA PAY AUD' Option Filed

'PRSA PAY AUD-ED' Option Filed

'PRSA PAY AUD-LV' Option Filed

'PRSA PAY AUD-OT' Option Filed

'PRSA PAY AUD-PP' Option Filed

'PRSA PAY CLR' Option Filed

'PRSA PAY DECOMP' Option Filed

'PRSA PAY EXC' Option Filed

'PRSA PAY MENU' Option Filed

'PRSA PAY MGR' Option Filed

'PRSA PAY PPC' Option Filed

'PRSA PAY PPE' Option Filed

'PRSA PAY TD-MAN' Option Filed

'PRSA PAY TL-MAN' Option Filed

'PRSA PE DISP' Option Filed

'PRSA PM POST' Option Filed

'PRSA PP EMP' Option Filed

'PRSA PP OPEN' Option Filed

'PRSA PR' Option Filed

'PRSA PT D1' Option Filed

'PRSA PT D2' Option Filed

'PRSA PT D3' Option Filed

'PRSA PT MENU' Option Filed

'PRSA SUP ALERTS' Option Filed

'PRSA SUP CERT' Option Filed

'PRSA SUP MENU' Option Filed

'PRSA SUP PPE' Option Filed

'PRSA SUP REV' Option Filed

'PRSA SUP UNR' Option Filed

'PRSA SUP UNR-PAY' Option Filed

'PRSA SUP UNR-TK' Option Filed

'PRSA T&L DECOMP REPORT' Option Filed

'PRSA TD DISP' Option Filed

'PRSA TD EDIT' Option Filed

'PRSA TD LIST' Option Filed

'PRSA TH' Option Filed

'PRSA TK EMP-HOL' Option Filed

'PRSA TK MEN-EMP' Option Filed

'PRSA TK MENU' Option Filed

'PRSA TK POST' Option Filed

'PRSA TK TOUR-DISP' Option Filed

'PRSA TK TOUR-DISP-SUP' Option Filed

'PRSA TK TOUR-EDIT' Option Filed

'PRSA TL DISP' Option Filed

'PRSA TL EDIT' Option Filed

'PRSA TL EMP' Option Filed

'PRSA TP DAY LIST' Option Filed

'PRSA TP DAY LIST-PAY' Option Filed

'PRSA TP ENVIR. DIFF.' Option Filed

'PRSA TP MENU' Option Filed

'PRSA TP POST' Option Filed

'PRSA TP VCS' Option Filed

'PRSA TPD' Option Filed

'PRSA TPD PP' Option Filed

'PRSA TPD PP-EMP' Option Filed

'PRSA TPD PP-SUP' Option Filed

'PRSA TPE ALL' Option Filed

'PRSA TPE ALL-SUP' Option Filed

'PRSA TPE ONE' Option Filed

'PRSA TPE ONE-SUP' Option Filed

'PRSA TPE PPE' Option Filed

'PRSA UNREVIEW LIST' Option Filed

'PRSA VC POST' Option Filed

'PRSA XMIT' Option Filed

'PRSD' Option Filed

'PRSD 04 EMPLOYEE INQUIRY' Option Filed

'PRSD 04 EMPLOYEE INQUIRY MENU' Option Filed

'PRSD 04 PAYRUN DATA INQUIRY' Option Filed

'PRSD 04 PRINT EMPLOYEE FILES' Option Filed

'PRSD 04 SEARCH EMPLOYEE FILES' Option Filed

'PRSD 05 AD HOC REPORTS' Option Filed

'PRSD 05 CCORG EDIT' Option Filed

'PRSD 05 EMPLOYEE INQUIRY' Option Filed

'PRSD 05 EMPLOYEE INQUIRY MENU' Option Filed

'PRSD 05 PRINT EMPLOYEE FILE' Option Filed

'PRSD 05 SEARCH EMPLOYEE FILE' Option Filed

'PRSD COMPILE STRENGTH REPORT' Option Filed

'PRSD PRINT STRENGTH REPORT' Option Filed

'PRSD PROCESS PRS (STARTUP)' Option Filed

'PRSD SERVICE RECORD SCREEN' Option Filed

'PRSD UPDATE PAID CODES' Option Filed

'PRSE-ACC' Option Filed

'PRSE-ATTEND' Option Filed

'PRSE-ATTENDANCE' Option Filed

'PRSE-C.E.' Option Filed

'PRSE-CLAS' Option Filed

'PRSE-CLS-REG' Option Filed

'PRSE-CORD' Option Filed

'PRSE-DEMP' Option Filed

'PRSE-EE-CLAS-INFO' Option Filed

'PRSE-EE-EMP' Option Filed

'PRSE-EE-SVC' Option Filed

'PRSE-EMP' Option Filed

'PRSE-EMP-MI' Option Filed

'PRSE-FL-SITE' Option Filed

'PRSE-I-EMP' Option Filed

'PRSE-IND-CLS' Option Filed

'PRSE-IND-DEMP' Option Filed

'PRSE-IND-REG' Option Filed

'PRSE-INS-MENU' Option Filed

'PRSE-IRM' Option Filed

'PRSE-M.I.' Option Filed

'PRSE-MAN' Option Filed

'PRSE-MI-LIST' Option Filed

'PRSE-MI-MULT' Option Filed

'PRSE-MIEX' Option Filed

'PRSE-NCEATTEND' Option Filed

'PRSE-O.I.' Option Filed

'PRSE-OLDE' Option Filed

'PRSE-P-CAL' Option Filed

'PRSE-P-RSTR' Option Filed

'PRSE-PRT' Option Filed

'PRSE-SITE' Option Filed

'PRSE-SOR' Option Filed

'PRSE-STU-PURG' Option Filed

'PRSE-SUP' Option Filed

'PRSE-SYS-MGR' Option Filed

'PRSE-W.I.' Option Filed

'PRSR-SYSTEM-PAID REPORTS' Option Filed

'PRSREM-LEV-USED' Option Filed

'PRSRFI-EXP' Option Filed

'PRSRFI-LEV-USED' Option Filed

'PRSRFI-OT/CT' Option Filed

'PRSRFI-PAID SYSTEM REPORTS' Option Filed

'PRSRFI-PPA-RPT' Option Filed

'PRSRFI-T&L-RPT' Option Filed

'PRSRSU-EXP' Option Filed

'PRSRSU-LEV-MENU' Option Filed

'PRSRSU-LEV-PATR' Option Filed

'PRSRSU-LEV-REQ' Option Filed

'PRSRSU-LEV-USED' Option Filed

'PRSRSU-OT/CT' Option Filed

'PRSRSU-PAID SYSTEM REPORTS' Option Filed

'PRSRSU-PPA-RPT' Option Filed...........................

Compiling form: PRSA TD EDIT.

Compiling form: PRSA OT REQ.

Compiling form: PRSA TD DISP.

Compiling form: PRSA TL EDIT.

Compiling form: PRSA TL DISP.

Compiling form: PRSA LV REQ.

Compiling form: PRSA ED REQ.

Compiling form: PRSA VC POST.

Compiling form: PRSA PM POST.

Compiling form: PRSA TD TL.

Compiling form: PRSA TP POST1.

Compiling form: PRSA TE EDIT

NOTE THAT FILE SECURITY-CODE PROTECTION HAS BEEN MADE

Executing PAID 4.0 post-init

Converting data for Family Leave...

Finished

4\) After successful initialization, you may delete all of the PRSIN\* routines.

> **NOTE:** Due to the fact that we are shipping a partial file \#200, you may receive errors when running an index. These will not affect the way the package operates.

Security: It is strongly suggested that VA FileMan rarely be used to alter files since security at the VA FileMan level is much less strict. See the National Package Security chapter in the technical manual for further information.

Routine Mapping: None of the routines need to be mapped.

Journaling: Journaling of these PAID globals is recommended:

^PRSPC ^PRST

Disk Space Used: File 450 (PAID EMPLOYEE) uses approximately two thousand bytes per employee. It is in the PRSPC global.

File 458 (TIME & ATTENDANCE RECORDS) uses approximately 900 bytes per employee per pay period. It is in the PRST global.

File 459 (PAID PAYRUN DATA) uses approximately 400 bytes per employee per pay period. It is in the PRST global.

Files 458 and 459 will grow larger and more quickly relative to File 450.