---
title: Fee Basis Annual Patch Manual
doc_type: POM
doc_label: Production Operations Manual
doc_layer: plain
doc_subject: 
app_code: FB
app_name: Fee Basis
section: FIN
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 0
description: "- [Revision History](#revision-history) - [Contents](#contents) - [Abbreviations for Fee Basis Annual (or Quarterly) Updates:](#abbreviations-for-fee-basis-annual-or-quarterly-updates) - [Updating the GPCIs (File \#162.96 routine FBZFSGYY).](#updating-the-gpcis-file-16296-routine-fbzfsgyy) - [Updati"
audience: 
keywords: 
  - span
  - class
  - mark
  - xtmp
  - cptm
  - year
  - number
  - gpci
  - rbrvs
  - fbzipa
page_count: 0
word_count: 9822
section_count: 1
table_count: 1
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: July 2024
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Financial_Admin/Fee_Basis/FB_PM.docx"
pdf_url: "https://www.va.gov/vdl/documents/Financial_Admin/Fee_Basis/FB_PM.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=40"
---

![](fee-basis-annual-patch-manual/001.png)

Fee Basis

Annual Update Instructions

July 2024

Office of Information Technology

Product Development

# Revision History


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Revision History](#revision-history)
- [Contents](#contents)
- [Abbreviations for Fee Basis Annual (or Quarterly) Updates:](#abbreviations-for-fee-basis-annual-or-quarterly-updates)
- [Updating the GPCIs (File \#162.96 routine FBZFSGYY).](#updating-the-gpcis-file-16296-routine-fbzfsgyy)
- [Updating the RVUs (File \#162.97 routine FBZRVUYY).](#updating-the-rvus-file-16297-routine-fbzrvuyy)
- [Updating the DOL Modifier information (File \#162.97, File \#162.98 routines FBZFSMYY and FBZFSRYY).](#updating-the-dol-modifier-information-file-16297-file-16298-routines-fbzfsmyy-and-fbzfsryy)
- [Updating the Conversion Factors (File \#162.99 routine FBZRVUYY).](#updating-the-conversion-factors-file-16299-routine-fbzrvuyy)
- [Update the Calculators (Routine FBAAFSR).](#update-the-calculators-routine-fbaafsr)
| Date      | Revision |     | Description |                  | Author(s)                          |
|-----------|----------|-----|-------------|------------------|------------------------------------|
| July 2024 |          | 1.0 |             | Document Created | <span class="mark">REDACTED</span> |

# Contents

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

# Abbreviations for Fee Basis Annual (or Quarterly) Updates:

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

FB – Fee Basis

GPCI – Geographic Practice Cost Index

RVU – Relative Value Unit

YY – Two digit year, e.g., 24 for 2024.

YYYY – Four digit year, e.g., 2024.

MM – Two digit month, e.g., 01 for January.

MMM – Three character representation of a month, e.g., JAN for January.

NNN – patch number

Notes:

In many of the routines, there is a reference to a directory containing files used in the update. In the routines in the document they have the format /home/sftp/patches/FILENAME.txt, for example /home/sftp/patches/PPRRVU24_JAN.csv. This corresponds to the directory structure on the server where the updates will be performed.

Misc:

1\. Do an RFIND for 09 in all of the new \*24 routines. This will help you identify places where you could have missed something.

2\. a. To back up the data use D ^%GOGEN, specifying the root of the global. For instance FB(162.97.

b\. To restore the global, first delete it using K ^FB(XXX.XX (I.E., FB(162.97,. Then, use D ^%GIGEN specifying the file you saved it to.

3\. To obtain the data, download the zips from the Center for Medicare and Medicaid Services (CMS) website.

  
Files Modified:

\#162.96 FEE BASIS GEOGRAPHIC INDEX (Modified by FBZFSGYY)

\#162.97 FEE BASIS CPT RVU (Modified by FBZRVUYY & FBZFSRYY)

\#162.98 FEE BASIS MODIFIER TABLE INDEX (Modified by FBZFSMYY)

\#162.99 FEE BASIS HCFA CONVERSION (Manually updated)

Routines to Modify:FBZFSGYY

Local routine to update GPCIs (Geographic Practice Cost Index)/Zip codes.

Updates file \#162.96 – FEE BASIS GEOGRAPHIC INDEX

FBZRVUYY

Local routine to update CPT RVUs. (Current Procedure Terminology, Relative Value Units).

Updates file \#162.97 – FEE BASIS CPT RVU

FBZFSMYY & FBZFSRYY

Local routine to update DOL MOD tables. (Department of Labor Modifier tables). Please note that the modifier tables are no longer being provided or used, so for now the data can just be copied from the previous year.

Updates file \#162.97 – FEE BASIS CPT RVU (FBZFSRYY)

Updates file \#162.98 – FEE BASIS MODIFIER TABLE INDEX (FBZFSMYY)

Before continuing, copy the previous years routines into this year’s dates. For example, copy FBZRVU23 to FBZRVU24. This is not necessary for the quarterly updates, only the annual. For the quarterly updates, edit the routines for that year. For example, when doing a quarterly update for 2024, update the FBZRVU24 routines.

  
Data sources:

Most of the data is obtained from the CMS (Center for Medicare Services) website. <http://www.cms.hhs.gov>

The information is contained under the *Medicare* section, in the *Medicare Fee-for-Service Payment* sub-section.

ZIP Code to Carrier Locality File – This file can be found under the *Fee Schedule – General Information* section of the website.

Link current as of February 2024. <http://www.cms.hhs.gov/FeeScheduleGenInfo/>

From the download, the file required is ZIP5_MMMY.TXT. Additionally, the file ZIP5lyout.txt describes the layout of the data in the file ZIP5_MMMY.TXT.

GPCIs and RVUs – A zip file containing these items can be found under The *PFS Relative Value Files* section of the *Physician Fee Schedule* sub-section. They are named RVUYYXX.ZIP, in this case XX represents the version. A – Initial release, B – Q2 update (April), C – Q3 update (July), D – Q4 update (October). Occasionally, there will be an R meaning revised. For example RVU24AR.

From the RVUYYXX.ZIP file, the necessary files are

YYLOCCO.(XLS, CSV, or TXT)

GPCIYY.CSV (CSV, or TXT)

PPRRVUYY.CSV (CSV, or TXT)

Link current as of February 2024. [PFS Relative Value Files \| CMS](https://www.cms.gov/medicare/payment/fee-schedules/physician/pfs-relative-value-files)

ZIP Codes – A file containing an up to date listing of ZIP codes is published to the anonymous.pub directory on the Albany development system. It can be accessed by ftp, or at VA4\$:\[ANONYMOUS.PUB\], or ANONYMOUS_DIR if you’re on the Albany development system. These are in the format “ZIPFILEMMYYYY.” The period is a part of the filename. Update as of Feb 2024, this file is no longer being created, per Jerry Simpson. The last file that was created was in August 2016. Jerry has provided the following file, which was last file created in August 2016. This is the file that was used for the update.

![](fee-basis-annual-patch-manual/002.png)

Modifier Level tables – Please note that the modifier level tables are no longer being provided by the DOL, and the modifier level tables are no longer used by the VA for VistA Fee Basis, so for now the data can just be copied from the previous year.

Generate STCTY_CARLOC.TXT.

1\. Start with an existing copy of STCTY_CARLOC.TXT (attached current as of 2009) ![](fee-basis-annual-patch-manual/003.png)

2\. Take the YYLOCCO.TXT file obtained in the RVUYYX.ZIP download, and the ZIPFILEMMYYYY file and update the county, carrier, and locality numbers as necessary. (Note, it may be necessary to add states/counties).

The format of the STCTY_CARLOC.TXT file is:

State \| County Number \| Carrier Number \| Locality Number \| County Name

The format of the ZIPFILEMMYYYY. file is:

ZIP \| State \| State Number \| County \| County Number

The YYLOCCO.TXT file contains all of the required information except for the County Number, that is obtained from the ZIPFILEMMYYYY. File.

# Updating the GPCIs (File \#162.96 routine FBZFSGYY). 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The files required are STCTY_CARLOC.TXT, GPCIYY.CSV (CSV, or TXT), ZIP5_MMMY.TXT, and ZIPFILEMMYYYY.

This requires modifying the highlighted portions of the routine FBZFSGYY.

FBZFSG09 ;WCIOFO/TCK-IMPORT GPCI/ZIP CODE DATA FROM HOST FILE ; 7/6/09 5:53pm

2 ;;3.5;FEE BASIS;NOT VERIFIED

3 Q

4 ;

LOCGPCI ; Import of CarrierLocality-\>GPCI data from HCFA file

6 K ^XTMP("FBLOC")

7 S ^XTMP("FBLOC",0)=\$\$FMADD^XLFDT(DT,+90)\_"^"\_DT

8 S FBSUB="FBLOC"

9 ;S ENF="\[BAUMANN.RBRVS2001\]01GPCIS.PRN"

10 ;S ENF="\[ENFINGER.RBRVS2002\]01GPCIS.PRN"

11 ;S ENF="\[HARTINJ\]GPCI04.PRN" ; this was from rvu4a

12 ;S ENF="\[HARTINJ\]GPCIS04.PRN"

13 ;S ENF="USER\$:\[KEHOET.RBRVS2006\]GPCIS06.PRN"

14 ;S ENF="USER\$:\[KEHOET.RBRVS2007\]GPCIS06.PRN"

15 ;S ENF="USER\$:\[KEHOET.RBRVS2008\]GPCIS08.PRN;6"

16 ;S ENF="USER\$:\[KEHOET.RBRVS2008\]GPCIS08.PRN;6"

17 ;S ENF="USER\$:\[CHANDARANAR.RBRVS2009\]GPCI09.TXT;1"

<span class="mark">18 S ENF="USER\$:\[CHANDARANAR.RVU09C\]GPCI09.CSV;1"</span> Point this to the correct file

<span class="mark">19 ; Host file format \| 2009 \| 2009 Q1-Q3</span>

<span class="mark">20 ; CARRIER 1-5 \| 1-5 \| Piece 1</span> This may need to be rearranged,

<span class="mark">21 ; LOCALITY 7-8 \| 9-10 \| Piece 2</span> if the layout of the data

<span class="mark">22 ; WORK GPCI 34-38 \| 45-49 \| Piece 4</span> changes. The commented out

<span class="mark">23 ; PE GPCI 43-47 \| 53-57 \| Piece 5</span> sections of code refer to the

<span class="mark">24 ; MP GPCI 53-57 \| 61-65 \| Piece 6</span> text based layout. The \$P

<span class="mark">25 S ENC("TOT")=0</span> portion refers to the csv

<span class="mark">26 O ENF</span> format. <span class="mark"></span>

<span class="mark">27 F U ENF S \$ZT="EOF^FBZFSG09" R ENX S \$ZT="" U IO D</span> Change to appropriate year. <span class="mark"></span>

<span class="mark">28 .;S CAR=\$TR(\$E(ENX,1,5)," ")</span>

<span class="mark">29 .S CAR=\$P(ENX,",",1)</span>

<span class="mark">30 .;S LOC=\$TR(\$E(ENX,9,10)," ")</span>

<span class="mark">31 .S LOC=\$P(ENX,",",2)</span>

<span class="mark">32 .;S WKGPCI=\$TR(\$E(ENX,45,49)," ")</span>

<span class="mark">33 .S WKGPCI=\$P(ENX,",",4)</span>

<span class="mark">34 .;S PEGPCI=\$TR(\$E(ENX,53,57)," ")</span>

<span class="mark">35 .S PEGPCI=\$P(ENX,",",5)</span>

<span class="mark">36 .;S MPGPCI=\$TR(\$E(ENX,61,65)," ")</span>

<span class="mark">37 .S MPGPCI=\$P(ENX,",",6)</span>

38 .I CAR'?5N!(LOC'?2N)!(WKGPCI'?1N1"."1.3N)!(PEGPCI'?1N1"."1.3N)!(MPGPC

I'?1N1"."1.3N) W !,"SKIPPING LINE ",ENX Q

39 .S ^XTMP("FBLOC",CAR_U_LOC)=WKGPCI_U_PEGPCI_U_MPGPCI

40 .S ENC("TOT")=ENC("TOT")+1

41 Q

42 ;

CNTYLOC ; Import of StateCounty-\>CarrierLocality data from file

44 K ^XTMP("FBCNTY")

45 S ^XTMP("FBCNTY",0)=\$\$FMADD^XLFDT(DT,+90)\_"^"\_DT

46 S FBSUB="FBCNTY",U="^"

47 F I=1:0 D Q:ENF="^"

<span class="mark">48 .R !,"ENTER ZIPCODE FILE NAME (USER\$:\[KEHOET.RBRVS2009\]STCTY_CARLOC.T</span>

<span class="mark">XT): ",ENF</span> (User is prompted for this filename)

49 .Q:ENF\["^"!(ENF="")

50 .;S ENF="\[BAUMANN.RBRVS2001\]STCTY_CARLOC.TXT"

51 .;S ENF="\[ENFINGER.RBRVS2002\]STCTY_CARLOC.TXT"

52 .;S ENF="\[HARTINJ\]STCTY_CARLOC.TXT"

53 .;S ENF="USER\$:\[KEHOET.RBRVS2006\]STCTY_CARLOC.TXT"

54 .;S ENF="USER\$:\[CHANDARANAR.RBRVS2009\]STCTY_CARLOC.TXT"

55 .; Host file format

56 .;

<span class="mark">57 .; STATE ABBR 1-2</span> This may need to be rearranged, <span class="mark"></span>

<span class="mark">58 .; COUNTY \# 4-6</span> if the layout of the data <span class="mark"></span>

<span class="mark">59 .; CARRIER 8-12</span> changes. <span class="mark"></span>

<span class="mark">60 .; LOCALITY 14-15</span>

<span class="mark">61 .;</span>

<span class="mark">62 .S ENC("TOT")=0</span>

<span class="mark">63 .O ENF</span>

<span class="mark">64 .F U ENF S \$ZT="EOF^FBZFSG09" R ENX S \$ZT="" U IO D</span> Change to appropriate year. <span class="mark"></span>

<span class="mark">65 ..S STATEA=\$TR(\$E(ENX,1,2)," ")</span>

<span class="mark">66 ..S COUNTY=\$E(ENX,4,6) ; will be blank for rest of state entries</span>

<span class="mark">67 ..S CARRIER=\$TR(\$E(ENX,8,12)," ")</span>

<span class="mark">68 ..S LOCALITY=\$TR(\$E(ENX,14,15)," ")</span>

69 ..I STATEA'?2A!(COUNTY'?1(3N,3" "))!(CARRIER'?5N)!(LOCALITY'?2N) W !,

"SKIPPING LINE ",ENX Q

70 ..S ^XTMP("FBCNTY",STATEA_COUNTY)=CARRIER_U_LOCALITY

71 ..S ENC("TOT")=ENC("TOT")+1

72 Q

73 ;

GETGPCI ;

75 N ZIP

76 K ^XTMP("FBGPCI")

77 S ^XTMP("FBGPCI",0)=\$\$FMADD^XLFDT(DT,+90)\_"^"\_DT

78 S FBSUB="FBGPCI",U="^"

79 ;S ENF="\[BAUMANN.RBRVS2001\]ZPLC0106.TXT"

80 ;S ENF="\[ENFINGER.RBRVS2002\]ZPLC0106.TXT"

81 ;S ENF="\[HARTINJ\]ZPLC0106.TXT"

82 ;S ENF="USER\$:\[KEHOET.RBRVS2008\]ZPLC0108.TXT"

83 ;S ENF="USER\$:\[CHANDARANAR.RBRVS2009\]ZIP5_JAN09.TXT"

<span class="mark">84 S ENF="USER\$:\[CHANDARANAR.RVU09C\]ZIP5_JUL09.TXT"</span> Point to correct file.

<span class="mark">85 .; Host file format</span> This may need to be rearranged, <span class="mark"></span>

<span class="mark">86 .;</span> if the layout of the data <span class="mark"></span>

<span class="mark">87 .; STATE ABBR 1-2</span> changes.

<span class="mark">88 .; ZIP 3-7</span>

<span class="mark">89 .; CARRIER 8-12</span>

<span class="mark">90 .; LOCALITY 13-14</span>

<span class="mark">91 .;</span>

<span class="mark">92 S ENC("TOT")=0</span>

<span class="mark">93 O ENF</span>

<span class="mark">94 F U ENF S \$ZT="EOF^FBZFSG09" R ENX S \$ZT="" U IO D</span> Change to appropriate year. <span class="mark"></span>

<span class="mark">95 .S STATEA=\$TR(\$E(ENX,1,2)," ")</span>

<span class="mark">96 .S ZIP=\$E(ENX,3,7) ; will be blank for rest of state entries</span>

<span class="mark">97 .S CARRIER=\$TR(\$E(ENX,8,12)," ")</span>

<span class="mark">98 .S LOCALITY=\$TR(\$E(ENX,13,14)," ")</span>

99 .I STATEA'?2A!(ZIP'?5N)!(CARRIER'?5N)!(LOCALITY'?2N) W !,"SKIPPING LI

NE ",ENX Q

100 .S ^XTMP("FBGPCI",ZIP)=CARRIER_U_LOCALITY

101 .S ENC("TOT")=ENC("TOT")+1

102 Q

103 ;

AACZIP ; Import of ZIP-\>CTY data from AAC file

<span class="mark">105 ; Host File format</span> This may need to be rearranged, <span class="mark"> </span>

<span class="mark">106 ; ZIP 1-5</span> if the layout of the data <span class="mark"></span>

<span class="mark">107 ; STATE ABBR 7-8</span> changes. <span class="mark"></span>

<span class="mark">108 ; STATE FIPS CODE? 10-11</span>

<span class="mark">109 ; COUNTY NAME 15-30</span>

<span class="mark">110 ; COUNTY \# 35-37</span>

111 K ^XTMP("FBZIPA")

112 S ^XTMP("FBZIPA",0)=\$\$FMADD^XLFDT(DT,+90)\_"^"\_DT

113 S FBSUB="FBZIPA",U="^"

114 S ENF=""

115 F I=1:0 D Q:ENF="^"

<span class="mark">116 .R !,"ENTER ZIPCODE FILE NAME (USER\$:\[KEHOET.RBRVS2009\]ZIPFILE012008.</span>

<span class="mark">TXT): ",ENF</span> (User is prompted for this filename)

117 .Q:ENF\["^"!(ENF="")

118 .;S ENF="USER\$:\[KEHOET.RBRVS2006\]ZIPFILE012006.TXT"

119 .;S ENF="USER\$:\[KEHOET.RBRVS2006\]ZIPFILE022006.TXT"

120 .;S ENF="USER\$:\[KEHOET.RBRVS2006\]ZIPFILE032006.TXT"

121 .;S ENF="USER\$:\[KEHOET.RBRVS2006\]ZIPFILE042006.TXT"

122 .;S ENF="USER\$:\[CHANDARANAR.RBRVS2009\]ZIPFILE112008.TXT"

123 .;S ENF="USER\$:\[CHANDARANAR.RVU09C\]ZIPFILE062009.TXT"

124 .Q:ENF="^"

125 .S ENC("TOT")=0,ENC("DUP")=0

126 .O ENF

<span class="mark">127 .S ENX="" F U ENF S \$ZT="EOF^FBZFSG09" R ENX S \$ZT="" U IO D</span> Change to appropriate year.

<span class="mark">128 ..S ZIP=\$TR(\$E(ENX,1,5)," ")</span>

<span class="mark">129 ..S STATEA=\$TR(\$E(ENX,7,8)," ")</span>

<span class="mark">130 ..S STATEN=\$TR(\$E(ENX,10,11)," ")</span>

<span class="mark">131 ..S CNTYNO=\$TR(\$E(ENX,35,37)," ")</span>

132 ..I ZIP'?5N W !,"ZIP ERR: ",ENX Q

133 ..I \$D(^XTMP("FBZIPA",ZIP)) D Q

134 ...S INS=\$G(^XTMP("FBZIPA","D",ZIP))

135 ...S INS=INS+1

136 ...S ^XTMP("FBZIPA","D",ZIP)=INS

137 ...S ENC("DUP")=ENC("DUP")+1

138 ...S ^XTMP("FBZIPA",ZIP,"D",INS,0)=""

139 ...S ^XTMP("FBZIPA",ZIP,"D",INS,1)=STATEA_U_CNTYNO

140 ..S ^XTMP("FBZIPA",ZIP,0)=""

141 ..S ^XTMP("FBZIPA",ZIP,1)=STATEA_U_CNTYNO

142 ..S ENC("TOT")=ENC("TOT")+1

143 Q

144 ;

EOF ; End Of File

146 S \$ZT=""

147 C ENF

148 ; update XTMP header

149 S ^XTMP(FBSUB,0)=DT\_"^^"\_ENC("TOT")\_U_ENC("TOT")

150 U IO

151 W !,"COUNT IN FILE ",ENF," = ",ENC("TOT")

152 I FBSUB\["ZIP" W !,"DUPLICATE ZIP CODES = ",ENC("DUP")

153 Q

154 ;

PROCDUP ; Process duplicate zip codes in XTMP("FBZIPA"

156 S END=0,U="^"

157 S ZIP="" F S ZIP=\$O(^XTMP("FBZIPA","D",ZIP)) Q:ZIP="" D Q:END

158 . W !!,"ZIP: ",ZIP," has duplicate entries."

159 . S I=0

160 . W !,?5,I+1,") ",^XTMP("FBZIPA",ZIP,0),!,?5," ",^XTMP("FBZIPA",ZIP

,1)

161 . S I=\$O(^XTMP("FBZIPA",ZIP,"D",I)) Q:'I D

162 . . W !,?5,I+1,") ",^XTMP("FBZIPA",ZIP,"D",I,0)

163 . . W !,?5," ",^XTMP("FBZIPA",ZIP,"D",I,1)

164 . S DIR(0)="NO^1:"\_(I+1)

165 . S DIR("A")="Select appropriate line"

166 . D ^DIR K DIR S:\$D(DTOUT)!\$D(DUOUT) END=1 Q:'Y

167 . S I=Y-1

168 . I I=0 S FBX(0)=^XTMP("FBZIPA",ZIP,0),FBX(1)=^XTMP("FBZIPA",ZIP,1)

169 . I I'=0 S FBX(0)=^XTMP("FBZIPA",ZIP,"D",I,0),FBX(1)=^XTMP("FBZIPA",Z

IP,"D",I,1)

170 . W !!,"Selected ",! ZW FBX

171 . K ^XTMP("FBZIPA",ZIP)

172 . S ^XTMP("FBZIPA",ZIP,0)=FBX(0)

173 . S ^XTMP("FBZIPA",ZIP,1)=FBX(1)

174 . K ^XTMP("FBZIPA","D",ZIP)

175 W !!,"Routine Complete"

176 Q

177 ;

FBZIPA ; Update FBZIPA with GPCIs

179 S U="^"

180 S ZIP=0 F S ZIP=\$O(^XTMP("FBZIPA",ZIP)) Q:ZIP="" D

181 . S Y1=\$G(^XTMP("FBZIPA",ZIP,1))

182 . I \$P(Y1,U,2)="" Q ; no county code

183 . S FBSC=\$P(Y1,U)\_\$P(Y1,U,2)

184 . S LOC=\$S(FBSC\]"":\$G(^XTMP("FBCNTY",FBSC)),1:"")

185 . I LOC="" S LOC=\$S(\$P(Y1,U)\]"":\$G(^XTMP("FBCNTY",\$P(Y1,U)\_" ")),1:

"")

186 . S GPCI=\$S(LOC\]"":\$G(^XTMP("FBLOC",LOC)),1:"")

187 . I GPCI="" D

188 . . S FBSC=^XTMP("FBGPCI",ZIP)

189 . . S GPCI=\$G(^XTMP("FBLOC",FBSC))

190 . I GPCI="" W !,"Could not determine GPCIs for ",ZIP," ",Y1 Q

191 . S ^XTMP("FBZIPA",ZIP,0)=GPCI

192 Q

193 ;

AACFB ; loop thru AAC zips and compare against existing data

195 W !,"comparing AAC zip codes with existing data in 162.96..."

196 S U="^"

197 F I="ZIP NEW","GPCI DIFF","GPCI MATCH","GPCI POPULATE" S CNT(I)=0

198 S ZIP=0 F S ZIP=\$O(^XTMP("FBZIPA",ZIP)) Q:ZIP="" D

199 . S AAC0=\$G(^XTMP("FBZIPA",ZIP,0))

200 . I \$P(AAC0,U)+\$P(AAC0,U,2)+\$P(AAC0,U,3)'\>0 Q ; ingore if no GPCIs

201 . S DA=\$O(^FB(162.96,"B",ZIP,0))

202 . I 'DA D Q ; new zip code

203 . . S CNT("ZIP NEW")=CNT("ZIP NEW")+1

204 . . W !,"NEW ZIP CODE: ",ZIP

205 . S DA(1)=\$O(^FB(162.96,DA,"CY","B","2009",0))

206 . I 'DA(1) D Q

207 . . W !,"MISSING CY 2009 FOR EXISTING ZIP: ",ZIP

208 . . S CNT("GPCI POPULATE")=CNT("GPCI POPULATE")+1

209 . S FBCY0=\$G(^FB(162.96,DA,"CY",DA(1),0))

210 . I \$P(FBCY0,U,2,4)="^^" S CNT("GPCI POPULATE")=CNT("GPCI POPULATE")+

1 Q

211 . I +\$P(AAC0,U)=+\$P(FBCY0,U,2),+\$P(AAC0,U,2)=+\$P(FBCY0,U,3),+\$P(AAC0,

U,3)=+\$P(FBCY0,U,4) S CNT("GPCI MATCH")=CNT("GPCI MATCH")+1

212 . E D

213 . . S CNT("GPCI DIFF")=CNT("GPCI DIFF")+1

214 . . W !,"DIFFERENT GPCI FOR ZIP: ",ZIP

215 . . W !," NEW GPCI : ",AAC0

216 . . W !," CURRENT GPCI: ",\$P(FBCY0,U,2,4)

217 ;

218 W !!

219 W !,"# New Zip Codes = ",CNT("ZIP NEW")

220 W !,"# GPCIs that will be Populated = ",CNT("GPCI POPULATE")

221 W !,"# GPCIs match = ",CNT("GPCI MATCH")

222 W !,"# GPCIs different = ",CNT("GPCI DIFF")

223 Q

224 ;

FBAAC ; loop thru existing data and compare against AAC zips

226 W !,"Check FB zip codes to determine if missing from the AAC data..."

227 S U="^"

228 F I="MISSING" S CNT(I)=0

229 S ZIP="" F S ZIP=\$O(^FB(162.96,"B",ZIP)) Q:ZIP="" D

230 . I '\$D(^XTMP("FBZIPA",ZIP)) D Q

231 . . S CNT("MISSING")=CNT("MISSING")+1

232 . . W !,"Existing ZIP ",ZIP," is missing from the AAC data."

233 . S AAC0=\$G(^XTMP("FBZIPA",ZIP,0))

234 . I \$P(AAC0,U)+\$P(AAC0,U,2)+\$P(AAC0,U,3)'\>0 W !,"ZIP EXISTS BUT NO GP

CI ",ZIP

235 W !!

236 W !,"# Missing = ",CNT("MISSING")

237 Q

238 ;

LOAD ; Load data into 162.96 using ^XTMP("FBZIPA" as source

240 S FBC("NZ")=0,FBC("Z")=0,FBC("I")=0,U="^"

241 S ZIP=0 F S ZIP=\$O(^XTMP("FBZIPA",ZIP)) Q:ZIP'\>0 D

242 . S FBY=^XTMP("FBZIPA",ZIP,0)

243 . ; skip if sum of GPCIs is zero

244 . I \$P(FBY,U)+\$P(FBY,U,2)+\$P(FBY,U,3)'\>0 S FBC("I")=FBC("I")+1 Q

245 . S FBC("Z")=FBC("Z")+1

246 . ;

247 . S Y=\$O(^FB(162.96,"B",ZIP,0))

248 . I 'Y D Q:Y'\>0

249 . . S FBC("NZ")=FBC("NZ")+1

250 . . K DA,DIC

251 . . S DIC="^FB(162.96,",DLAYGO=162.96,DIC(0)="L",X=ZIP

252 . . K DD,DO D FILE^DICN I Y'\>0 W !,"ERROR ADDING NEW ZIP ",ZIP

253 . . K DIC,DLAYGO

254 . ;

255 . K DA,DIC

256 . S DA(1)=+Y

<span class="mark">257 . S Y=\$O(^FB(162.96,DA(1),"CY","B",2009,0))</span> Change to appropriate year.

258 . I 'Y D Q:Y'\>0

259 . . S DIC="^FB(162.96,"\_DA(1)\_",""CY"",",DIC(0)="L",DIC("P")="162.961

A"

<span class="mark">260 . . S X=2009</span> Change to appropriate year.

<span class="mark">261 . . K DD,DO D FILE^DICN I Y'\>0 W !,"ERROR ADDING 2009 for ",ZIP</span> Change to appropriate year.

262 . . K DIC,DLAYGO

263 . S DA=+Y

264 . ;

265 . S DIE="^FB(162.96,"\_DA(1)\_",""CY"","

266 . S DR=".02///"\_\$P(FBY,U)\_";.03///"\_\$P(FBY,U,2)\_";.04///"\_\$P(FBY,U,3)

267 . D ^DIE K DIE,DR,DA

268 ;

269 W !!,"ZIP = ",FBC("Z")

270 W !,"NEW ZIP = ",FBC("NZ")

271 W !,!,"IGNORED ZIPS WITH ZERO GPCI = ",FBC("I")

272 Q

273 ;

<span class="mark">274 ;FBZFSG09Change to appropriate year.</span>

Once the routine has been modified. It is possible to load the GPCI data into file 162.96.

The steps are as follows (after transferring all necessary files into /home/sftp/patches in ASCII mode onto server that you will be performing this on:

A. D LOCGPCI^FBZFSGYY – loads carrier locality – GPCI data from file GPCIYYYY.TXT into ^XTMP("FBLOC")
B. D CNTYLOC^FBZFSGYY – loads state/county carrier locality data into ^XTMP("FBCNTY"). At prompt, enter /home/sftp/patches/STCTY_CARLOC.txt
C. GETGPCI ^FBZFSGYY – loads GPCI and County/Carrier locality data from file ZIP5_JANYYYY.txt into ^XTMP("FBGPCI")
D. D AACZIP^FBZFSGYY – loads zip code/state county data from the AAC file ZIPFILE.txt into ^XTMP("FBZIPA"). At prompt, enter /home/sftp/patches/ZIPFILE.txt
E. D PROCDUP^FBZFSGYY – checks/fixes any duplicate zip code entries.
F. D FBZIPA^FBZFSGYY – adds GPCIs to zip code list in ^XTMP(“FBZIPA”)
G. D AACFB^FBZFSGYY – compares zip code data with data in \#162.96. (optional).
H. D FBAAC^FBZFSGYY – compares data in \#162.96 with zip code data.

(optional). This finds missing zip codes, based on last year’s update.

I. D FBAAC^XRDZIP, then D NOZIP^XRDZIP – Finds zip codes from previous year in file 162.96 that are not in AAC zip code file. Add output from NOZIP^XRDZIP to file ZIPFILE.txt.
J. Kill all ^XTMP globals from steps A through D. Repeat steps A through F using updated file ZIPFILE.txt.
K. D FBAAC^FBZFSG24 to get missing zip codes again, based on last year’s update.
L. If output from step K shows no missing zip codes, D LOAD^FBZFSGYY – populates file 162.96 with data stored in ^XTMP(“FBZIPA”)

# Updating the RVUs (File \#162.97 routine FBZRVUYY). 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

FBZRVUY9 \\WCIOFO/SS,DMK,SAB-RVU IMPORT ; 10/23/08 11:48am

2 ;;3.5;FEE BASIS;\*\*109\*\*;JAN 30, 1995

3 ;

4 ;this routine was used to populate file \#162.97 with RVU values

5 ;for the year 2009 for the patch FB\*3.5\*109

6 ;the routine is not a part of the patch, it was used only to prepare

global for this patch

7 Q

EN ;

<span class="mark">9 D EN1("2009"\_U\_"USER\$:\[CHANDARANAR.RBRVS2009\]PPRRVU09.TXT;1")</span> Update to the appropriate year and file

10 Q

11 ;/\*\*

12 ;entry point

13 ;Load RVU data from the CMS file into the file \#162.97

USER ;\*/

15 N BFRET

16 ;promt for a calendar year and filename

17 S BFRET=\$\$PROMPTS()

18 I BFRET\<0 Q

19 D EN1(BFRET)

20 Q

21 ;

22 ;input:

23 ; 4_digits_year ^ full_path_and_filename

24 ;Example:

25 ; D EN1^<span class="mark">FBZRVUY9</span>("2009^USER\$:\[KEHOET.RBRVS2009\]PPRRVU09.TXT")

EN1(BFRET) ;load data to XTMP global

27 N FBZ

28 N FBCYEAR ;calendar year

29 N FBCMS ;total number of lines with RVU values in CMS file

30 N FBIMPRTD ;total number of imported RVU lines

31 N FBOK81 ; total number of CPTs that were found in CPT file \#81

32 N FBNOT81 ; total number of CPTs that were NOT found in CPT file \#81

33 N FBCNT ; total number of records that were examined using CPT file \#

81

34 N FBRECS ; total number of processed lines

35 N FBNEWCPT ; total number of new CPT (or CPT-MOD) parent records crea

ted in file \#162.97

36 N FBNEWCY ; total number of the new the year FBCY records created for

existing CPT (CPT-MOD)

37 N FBEDITCY ; total number of records updated for the existing year FB

CY

38 S FBCYEAR=+BFRET

39 S FBZ=0

40 S FBCMS=0

41 S FBIMPRTD=0

42 ;import RVU values into ^XTMP global

43 D HCFAIMP(\$P(BFRET,U,2),FBCYEAR,.FBCMS,.FBIMPRTD)

44 R !!,"Press any key to continue...",X

45 ;Q

46 ;check codes

47 S FBZ=\$\$EXAMHCFA()

48 S FBCNT=+FBZ ;total number of records that were examined using CPT fi

le \#81

49 S FBOK81=\$P(FBZ,U,2) ;total number of CPTs that were found in CPT fil

e \#81

50 S FBNOT81=\$P(FBZ,U,3) ; total number of CPTs that were NOT found in C

PT file \#81

51 ;load data from ^XTMP to \#162.97

52 S FBZ=\$\$LOAD(+BFRET)

53 S FBRECS=+FBZ ;total number of processed lines

54 S FBNEWCPT=\$P(FBZ,U,2) ;total number of new CPT (or CPT-MOD) parent r

ecords created in file \#162.97

55 S FBNEWCY=\$P(FBZ,U,3) ;total number of the new the year FBCY records

created for existing CPT (CPT-MOD)

56 S FBEDITCY=\$P(FBZ,U,4) ;total number of records updated for the exist

ing year FBCY

57 D REPORT(FBCYEAR,FBIMPRTD,FBCNT,FBOK81,FBNOT81,FBRECS,FBNEWCPT,FBNEWC

Y,FBEDITCY)

58 Q

59 ;/\*\*

60 ;report

REPORT(FBCY,FBIMPRTD,FBCNT,FBOK81,FBNOT81,FBRECS,FBNEWCPT,FBNEWCY,FBEDITCY) ;\*

/

62 W !!

63 W !,"===== Importing from text file into ^XTMP global ===============

"

64 W !,"Total number of imporetd records ...............................

",FBIMPRTD

65 W !

66 W !,"===== Checking if CPT codes are in CPT file \#81 ================

"

67 W !,"Total number of records that were examined using CPT file \#81...

",FBCNT

68 W !,"Total number of CPTs that were found in CPT file \#81............

",FBOK81

69 W !,"Total number of CPTs that were NOT found in CPT file \#81........

",FBNOT81

70 W !

71 W !,"===== Loading to file#162.97 ===================================

"

72 W !,"Total number of processed lines.................................

",FBRECS

73 W !,"Total number of new CPT (or CPT-MOD) parent records created"

74 W !,"in file \#162.97.................................................

",FBNEWCPT

75 W !,"Total number of the year ",FBCY," records created for existing"

76 W !,"CPT (CPT-MOD)...................................................

",FBNEWCY

77 W !,"Total number of records updated for the existing year ",FBCY,"..

.... ",FBEDITCY

78 W !

79 Q

80 ;

81 ;/\*\*

82 ;Prompts a calendar year and file to import from

83 ;output:

84 ; 4_digits_year ^ full_path_and_filename

85 ; -1 if user chose to quit

PROMPTS() ;\*/

87 N FBYEAR ;calendar year

88 N DIRECT ;directory

89 N FILENAME ;full pathname

90 N FULLPATH ;full pathname

91 N FBQ

92 S FBYEAR=0

93 S (DIRECT,FILENAME,FULLPATH)=""

94 S FBYEAR=\$\$CALYEAR()

95 I FBYEAR=-1 Q -1

96 S FBQ=0

97 F D Q:FBQ'=0

98 . S DIRECT=\$\$DIRECTRY() I DIRECT=-1 S FBQ=-1 Q

99 . S FILENAME=\$\$FILENAM() I FILENAME=-1 S FBQ=-1 Q

100 . S FULLPATH=DIRECT_FILENAME

101 . W !,"Verifying file ",FULLPATH," ..."

102 . S FBQ=\$\$CHCKFILE(FULLPATH)

103 . W " - ",\$S(FBQ=0:"wrong file name!",1:"OK")

104 I FBQ\<0 Q -1

105 Q FBYEAR_U_FULLPATH

106 ;

107 ;/\*\*

108 ;enter a calendar year

109 ;output:

110 ; 4 digits calendar year

CALYEAR() ;\*/

112 N FBQ

113 S FBQ=0

114 F D Q:FBQ\>0

115 . R !,"Please enter a calendar year for this fee schedule: ",X:30

116 . I X="^" S FBQ=2 Q

117 . I X="?" W !,"e.g. 2005" Q

118 . I X=""!(X'?4N) W !,"Please enter a 4-digit number or ^ to quit" Q

119 . S FBQ=1

120 Q:FBQ=2 -1

121 Q +X

122 ;

123 ;/\*\*

124 ;enter a directory

125 ;output:

126 ; directory as a string

DIRECTRY() ;\*/

128 N FBQ

129 S FBQ=0

130 F D Q:FBQ\>0

131 . R !,"Please enter the directory where ALL files reside: ",X:30

132 . I X="^" S FBQ=2 Q

133 . I X="" W !,"Enter the directory path or ^ to quit" Q

134 . I X="?" W !,"This is the directory path where ALL files reside.",!,

"e.g. USER\$:\[Directory\] or USER\$:\[Directory.subdirectory\]" Q

135 . S FBQ=1

136 Q:FBQ=2 -1

137 Q X

138 ;

139 ;/\*\*

140 ;enter filename

141 ;output:

142 ; filename as a string

FILENAM() ;\*/

144 N FBQ

145 S FBQ=0

146 F D Q:FBQ\>0

147 . R !,"Please enter the file name for HCFA RVU data: ",X:30

148 . I X="^" S FBQ=2 Q

149 . I X="" W !,"Enter filename or ^ to quit" Q

150 . S FBQ=1

151 Q:FBQ=2 -1

152 Q X

153 ;

154 ;

155 ;/\*\*

156 ;check whether the file exists

157 ;input:

158 ; full path and filename as a string

159 ;output:

160 ; 1 - file exists and can be opened

161 ; 0 - file was not found or cannot be opened

CHCKFILE(FULLPTH) ;\*/

163 O FULLPTH::5

164 I '\$T Q 0

165 C FULLPTH

166 Q 1

167 ;

168 ;

169 ;/\*\*

170 ;import data from CMS text file to ^XTMP global

171 ; creates ^XTMP("FBHCFA") with RVU HCPCS/CLT codes and RVU values

172 ;input:

173 ; FBFNAME - full pathname for the CMS file that contains RVU data (VM

S example: "\[SHAMUKS\]PPRRVU04.TXT")

174 ; FBYEAR - calendar year (example: 2008)

175 ;output:

176 ; .FBCNT total number of lines with RVUs in CMS file

177 ; .FBCNTOK total number of created ^XTMP records

HCFAIMP(FBFNAME,FBYEAR,FBCNT,FBCNTOK) ;\*/

179 N FBLINE,FBCPT,FBMOD,FBSTAT,WRVU,TNFPRVU,TFPRVU,MRVU,FBCPTM,FBNPFLG,F

BTRUE

180 ;FBCNTOK ;total number of created ^XTMP records

181 ;FBCNT ;total number of lines with RVUs in CMS file

182 W !,"Importing RVU values from the file:",FBFNAME,!

183 K ^XTMP("FBHCFA")

184 ;set ^XTMP to expire +120 days from now

185 S ^XTMP("FBHCFA",0)=\$\$FMADD^XLFDT(DT,+120)\_"^"\_DT

186 S (FBCNT,FBCNTOK)=0

187 ;open file

188 O FBFNAME

189 ;read file

<span class="mark">190 F U FBFNAME S \$ZT="EOF^FBZRVUY9" R FBLINE S \$ZT="" U IO D</span> Modify if file layout changes, modify to point to the correct routine. <span class="mark"></span>

<span class="mark">191 . ;echo lines</span>

<span class="mark">192 . W !,FBLINE</span>

<span class="mark">193 . Q:\$E(FBLINE,1,3)="HDR"</span>

<span class="mark">194 . S FBCNT=FBCNT+1</span>

<span class="mark">195 . S FBCPT=\$TR(\$E(FBLINE,1,5)," ")</span>

<span class="mark">196 . S FBMOD=\$TR(\$E(FBLINE,6,7)," ")</span>

<span class="mark">197 . S FBSTAT=\$E(FBLINE,58)</span>

<span class="mark">198 . ;Q:"^D^X^"\[(U_FBSTAT_U) ; deleted codes or statutory exclusion</span>

<span class="mark">199 . ;</span>

<span class="mark">200 . ;\<RVU\> don't need to determine status and analyze it</span>

<span class="mark">201 . ;\<RVU\> Q:"^A^R^T^"'\[(U_FBSTAT_U) only codes used for Medicare payme</span>

<span class="mark">nt</span>

<span class="mark">202 . ;</span>

<span class="mark">203 . ;\<RVU\> don't quit if NONPAYABLE</span>

<span class="mark">204 . ;\<RVU\> Q:\$E(FBLINE,59)="+" ; RVU's are not used for Medicare paymen</span>

<span class="mark">t</span>

<span class="mark">205 . ;</span>

<span class="mark">206 . S WRVU=\$TR(\$E(FBLINE,60,65)," ")</span>

<span class="mark">207 . S TNFPRVU=\$TR(\$E(FBLINE,67,72)," ")</span>

<span class="mark">208 . S TFPRVU=\$TR(\$E(FBLINE,85,90)," ")</span>

<span class="mark">209 . S MRVU=\$TR(\$E(FBLINE,104,110)," ")</span>

210 . I \$L(FBCPT)'=5!(WRVU'?1.3N1"."2N)!(TNFPRVU'?1.3N1"."2N)!(TFPRVU'?1.

3N1"."2N)!(MRVU'?1.3N1"."2N) W !,"SKIPPING LINE ",FBLINE Q

211 . I FBCPT="" W !,"ERROR CPT: ",FBLINE Q

212 . S FBCPTM=FBCPT\_\$S(FBMOD\]"":"-"\_FBMOD,1:"")

213 . ;I '\$D(^XTMP("FBDOL",FBCPTM)) D Q

214 . ;. W !,"MISSING CPT-MOD: ",FBCPTM,!,FBLINE

215 . ;S ^XTMP("FBHCFA",FBCPTM)="2004^^"\_WRVU_U_TNFPRVU_U_TFPRVU_U_MRVU

216 . ;RVU: adding the NONPAYABLE flag

217 . S FBNPFLG=\$S(((\$E(FBLINE,59)="+")!("^A^R^T^"'\[(U_FBSTAT_U))):1,1:0)

218 . S ^XTMP("FBHCFA",FBCPTM)=FBYEAR\_"^^"\_WRVU_U_TNFPRVU_U_TFPRVU_U_MRVU

\_U_U_FBNPFLG

219 . S FBCNTOK=FBCNTOK+1

220 Q

221 ;

222 ;/\*\*

223 ;check if there are any CPT codes in ^XTMP that are not in the CPT fi

le \#81

224 ;OK or warning message will be printed to the screen

225 ;input:

226 ; ^XTMP global needs to be in the system

227 ;output:

228 ; FBCNT^FBOKCNT^FBERCNT

229 ; where:

230 ; FBOKCNT - counter for OKs

231 ; FBERCNT - counter for errors

232 ; FBCNT - counter for all records that were examined

EXAMHCFA() ;\*/

234 N CPTM,FBCNT,FBOKCNT,FBERCNT

235 S (FBOKCNT,FBERCNT,FBCNT)=0

236 S CPTM=0 F S CPTM=\$O(^XTMP("FBHCFA",CPTM)) Q:CPTM="" D

237 . S FBCNT=FBCNT+1

238 . I '\$O(^ICPT("B",\$P(CPTM,"-"),0)) W !,"?CPT ",CPTM S FBERCNT=FBERCNT

+1 Q

239 . E W !,"OK - ",CPTM S FBOKCNT=FBOKCNT+1

240 Q FBCNT_U_FBOKCNT_U_FBERCNT

241 ;

242 ;/\*\*

243 ;load data from ^XTMP global into file# 162.97

244 ;input:

245 ; FBCY - calendar year

246 ;output:

247 ; FBRECS^FBNEWCPT^FBNEWCY^FBEDITCY

248 ; where:

249 ; FBRECS - total number of processed records

250 ; FBNEWCPT - total number of new CPT (or CPT-MOD) parent records crea

ted in file \#162.97

251 ; FBNEWCY - total number of the new the year FBCY records created for

existing CPT (CPT-MOD)

252 ; FBEDITCY - total number of records updated for the existing year FB

CY

LOAD(FBCY) ;\*/

254 N Y,FBNEWCPT,FBNEWCY,FBEDITCY,FBRECS,FBCPTM,FBY

255 S FBRECS=0 ;count processed records

256 S FBNEWCPT=0 ;count the new top-level records created in file \#162.97

257 S FBNEWCY=0 ;count new CY records

258 S FBEDITCY=0 ;count edited records

259 S FBCPTM=0

260 F S FBCPTM=\$O(^XTMP("FBHCFA",FBCPTM)) Q:FBCPTM="" D

261 . S FBRECS=FBRECS+1

262 . S FBY=^XTMP("FBHCFA",FBCPTM)

263 . I \$P(FBY,U)'=FBCY W !,FBCPTM," - ",\$P(FBY,U)," Wrong Year! - SKIPPE

D!"

264 . S Y=\$\$PROCREC(FBCPTM,FBCY,FBY)

265 . S FBNEWCPT=FBNEWCPT+\$P(Y,U,1)

266 . S FBNEWCY=FBNEWCY+\$P(Y,U,2)

267 . S FBEDITCY=FBEDITCY+\$P(Y,U,3)

268 Q FBRECS_U_FBNEWCPT_U_FBNEWCY_U_FBEDITCY

269 ;

270 ;process one line in XTMP global

271 ;FBCPTM CPT/MOD

272 ;FBCY - calendar year

273 ;FBY - XTMP node

PROCREC(FBCPTM,FBCY,FBY) ;

275 N Y,FBNEWCPT,FBNEWCY,FBEDITCY,FBCPT,FBCAT,FBIEN,FBIENCY

276 S (FBNEWCPT,FBNEWCY,FBEDITCY)=0

277 ;

278 W !,FBCPTM," : "

279 S FBCPT=\$P(FBCPTM,"-")

280 ;

281 ;\<RVU\> should we still be checking CPT file?

282 ;I '\$O(^ICPT("B",FBCPT,0)) W "CPT-MOD is not in ICPT file - NOT PROCE

SSED" Q FBNEWCPT_U_FBNEWCY_U_FBEDITCY

283 ;

284 ;\<RVU\> do not skip any value

285 ;\<RVU\> I \$P(FBY,U,3)+\$P(FBY,U,4)+\$P(FBY,U,5)+\$P(FBY,U,6)'\>0,\$P(FBY,U,

7)="" D Q

286 ;\<RVU\> . W !,"SUM OF RVUs '\> 0 and base units null. SKIPPING CPT-MOD

",FBCPTM

287 ;

288 S FBCAT=\$\$CPTCAT(FBCPT)

289 I FBCAT="" W "Unknown CPT category. "

290 ;

291 ;--- top level CPT record ------

292 ;check whether CPT/MOD is already in file \#162.97

293 ;FBIEN - ien for the top level record

294 S FBIEN=+\$O(^FB(162.97,"B",FBCPTM,0))

295 ;

296 ;if no entry for this CPT or CPT-CPTMOD combination then create one

297 ;if couldn't then quit

298 I FBIEN=0 D Q:FBIEN'\>0 FBNEWCPT_U_FBNEWCY_U_FBEDITCY

299 . S FBIEN=+\$\$NEWCPT(FBCPTM,FBCAT)

300 . I FBIEN'\>0 W !,"Error additing new CPT-MOD - NOT ADDED!" Q

301 . S FBNEWCPT=1

302 ;

303 ;--- calendar year multiple ----------

304 ;check whether CPT/MOD has already that year record in file \#162.97

305 S FBIENCY=\$O(^FB(162.97,FBIEN,"CY","B",FBCY,0))

306 ;

307 ;if no entry for the specified year then create one

308 ;if couldn't then quit

309 I FBIENCY'\>0 D Q:FBIENCY'\>0 FBNEWCPT_U_FBNEWCY_U_FBEDITCY

310 . S FBIENCY=+\$\$NEWCY(FBIEN,FBCY)

311 . I FBIENCY'\>0 W !,"Cannot create multiple record for "\_FBCY\_" RVUs -

NOT ADDED!"

312 . S FBNEWCY=1

313 ;

314 ;--- edit calendar year multiple ----------

315 S Y=\$\$EDITCY(FBIEN,FBIENCY,FBY)

316 I Y\>0 S FBEDITCY=1 W "OK"

317 I Y\<0 W "Error updating/populating RVUs - NOT UPDATED/ADDED!"

318 Q FBNEWCPT_U_FBNEWCY_U_FBEDITCY

319 ;

320 ;/\*

321 ;Create a new top-level record in file \#162.97 for

322 ;CPT or CPT-CPTMOD combination

323 ;input

324 ; FBCPTM - cpt or cpt-modifier

325 ; FBCAT - major category

326 ;output

327 ; \>0 - record number (ien) of the new record

328 ; \<1 - records was not created

NEWCPT(FBCPTM,FBCAT) ;\*/

330 N X,Y,DA,DIC,DLAYGO,DD,DO

331 S DIC="^FB(162.97,"

332 S DLAYGO=162.97

333 S DIC(0)="L"

334 S X=FBCPTM

335 I \$G(FBCAT)'="" S DIC("DR")=".02///"\_FBCAT

336 D FILE^DICN

337 Q +Y

338 ;/\*

339 ;Create a new record in a calendar year multiple

340 ;input:

341 ; FBIEN - ien of the parent entry (top-level)

342 ; FBCY - calendar year

343 ;output:

344 ; \>0 record number (ien) of the new CY multiple entry

345 ; \<1 was not created

NEWCY(FBIEN,FBCY) ;\*/

347 N DA,DIC,DD,DO,DLAYGO

348 S DA(1)=+FBIEN

349 S DIC="^FB(162.97,"\_DA(1)\_",""CY"","

350 S DIC(0)="L"

351 S DIC("P")="162.971A"

352 S X=FBCY

353 D FILE^DICN

354 Q +Y

355 ;

356 ;/\*

357 ;Edit existing year multiple node

358 ;input:

359 ; FBIEN - ien of the parent entry (top-level)

360 ; FBIENCY - record number (ien) of the CY multiple entry

361 ; FBY - content of the ^XTMP global with RVU values

362 ;output:

363 ; 1- succesful

364 ; -1 - failed

EDITCY(FBIEN,FBIENCY,FBY) ;\*/

366 N DA,DIE,DR,DTOUT,FBYEAR

367 S FBYEAR=+\$P(\$G(^FB(162.97,FBIEN,"CY",FBIENCY,0)),U)

368 I FBYEAR=0 W " Wrong CY ien " Q -1

369 I FBYEAR'=\$P(FBY,U) W " Wrong year " Q -1

370 S DA=FBIENCY

371 S DA(1)=FBIEN

372 S DIE="^FB(162.97,"\_DA(1)\_",""CY"","

373 S DR=""

374 I \$P(FBY,U,2)\]"" S DR=DR\_".02///"\_\$P(FBY,U,2)\_";"

375 S DR=DR\_".03///"\_\$P(FBY,U,3)\_";.04///"\_\$P(FBY,U,4)\_";.05///"\_\$P(FBY,U

,5)\_";.06///"\_\$P(FBY,U,6)\_";.08///"\_\$P(FBY,U,8)

376 D ^DIE

377 I \$D(DTOUT) Q -1

378 Q 1

379 ;

380 ;

381 ;/\*\*

382 ;return cpt major category

383 ;input:

384 ; cpt major category as a string

385 ;output:

386 ; null if none

387 ;

CPTCAT(FBCPT) ;\*/

389 N RET,X,Y

390 S RET=""

391 S X=\$P(\$\$CPT^ICPTCOD(FBCPT),U,4)

392 I X\>0 S Y=\$P(\$\$CAT^ICPTAPIU(X),U,4)

393 I \$L(\$G(Y))\>0,+\$O(^FB(162.99,"B",Y,0))=0 Q ""

394 I \$G(Y)\["EVALUATION" S Y="EVALUATION & MANAGEMENT"

395 I \$G(Y)\]"" S RET=Y

396 ;I "00100"'\]FBCPT&(FBCPT'\]"01999") S RET="ANESTHESIA"

397 ;I "10040"'\]FBCPT&(FBCPT'\]"69979") S RET="SURGERY"

398 ;I "70010"'\]FBCPT&(FBCPT'\]"79999") S RET="RADIOLOGY"

399 ;I "80049"'\]FBCPT&(FBCPT'\]"89399") S RET="LABORATORY"

400 ;I "90700"'\]FBCPT&(FBCPT'\]"99199") S RET="MEDICINE"

401 ;I "99201"'\]FBCPT&(FBCPT'\]"99499") S RET="EVALUATION & MANAGEMENT"

402 ;Q "TEST"

403 Q RET

404 ;

405 ;

406 ;/\*\*

407 ;End Of File

EOF ;\*/

409 S \$ZT=""

410 C FBFNAME

411 U IO

412 W !!,"COUNT IN FILE ",FBFNAME," = ",FBCNT

413 Q

414 ;

415 ;

Once the routine has been modified. It is possible to load the RVU data into file 162.97.

The steps are as follows:

1.  D EN^FBZRVUYY – This will import the RVUs into file 162.97.

# Updating the DOL Modifier information (File \#162.97, File \#162.98 routines FBZFSMYY and FBZFSRYY). 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

FBZFSMYY is used to import the modifier level tables.

FBZFSRYY is used to attach the modifier level table number to the CPT code.

Modify the COPY00 and COPYMOD tags in the routines to reflect the year for the update, then run those to populate the data in files 162.97 and 162.98.

FBZFSM09 ;WCIOFO/MJE/TCK-IMPORT DOL MOD LVL TABLE FROM HOST FILE ; 12/1/08 1:3

8am

2 Q

MLTI ; DOL import of modifier level tables from OWCP files

4 ; Data will be extracted from a host file (ENF) and

5 ; imported into ^XTMP("FBMLT",

<span class="mark">6 ; Host File format \| 2008</span> Modify if file layout changes <span class="mark"></span>

<span class="mark">7 ; TABLE 1-4 \| 1-3</span>

<span class="mark">8 ; MODIFIER 9-12 \| 6-7</span>

<span class="mark">9 ; PERCENT 21-25 \| 9-12</span>

10 ;

11 K ^XTMP("FBMLT")

12 S ^XTMP("FBMLT",0)=\$\$FMADD^XLFDT(DT,+90)\_"^"\_DT

13 ;S ENF="USER\$:\[KEHOET.RBRVS2007\]FS06MODS.PRN"

14 ;S ENF="USER\$:\[KEHOET.RBRVS2008\]FS08MODS.PRN"

<span class="mark">15 S ENF="USER\$:\[CHANDARANAR.RBRVS2009\]FS08MODS.PRN"</span> Point to the correct directory and file.

16 S ENC("TOT")=0

17 O ENF

18 ; loop thru host file

19 F U ENF S \$ZT="<span class="mark">EOF^FBZFSM09</span>" R ENX S \$ZT="" U IO D Modify to correct routine.

20 . Q:\$TR(ENX," ")="" ; blank line

21 . S TST=\$TR(\$E(ENX,1,3)," ") I \$L(TST)\<3 S TST=\$E("00"\_TST,\$L(TST),\$L

(TST)+2) ;add leading zeros

22 . I TST'?3N W !,"Skip ",ENX Q ; not detail line

23 . ; process detail line

<span class="mark">24 . S TBL=TST ;\$TR(\$E(ENX,1,3)," ")</span> Modify if file layout changes <span class="mark"> </span>

<span class="mark">25 . S MOD=\$TR(\$E(ENX,6,7)," ")</span>

<span class="mark">26 . S PCT=\$TR(\$E(ENX,9,12)," ")\_"0" ;add trailing zeros</span>

27 . S X=TBL_MOD_PCT

28 . ;I X'=\$TR(ENX," ") W !,"ERR: ",ENX Q

29 . I TBL'?3N W !,"TBL ERR: ",TBL Q

30 . I MOD'?2NU W !,"TABLE: ",TBL," MOD ERR: ",MOD Q

<span class="mark">31 . Q:MOD="10" ; OWCP modifiers</span>

<span class="mark">32 . I "^SD^GE^GN^GP^NR^RP^RR^SG^GG^GH"'\[(U_MOD_U) S MODX=\$\$MOD^ICPTMOD(</span>

<span class="mark">MOD,"E") ;ADD GG/GH for 2008 mods</span>

<span class="mark">33 . I MOD="GE" S MODX=\$\$MOD^ICPTMOD(193,"I")</span>

<span class="mark">34 . I MOD="GN" S MODX=\$\$MOD^ICPTMOD(368,"I")</span>

<span class="mark">35 . I MOD="NR" S MODX=\$\$MOD^ICPTMOD(85,"I")</span>

<span class="mark">36 . I MOD="RP" S MODX=\$\$MOD^ICPTMOD(107,"I")</span>

<span class="mark">37 . I MOD="RR" S MODX=\$\$MOD^ICPTMOD(108,"I")</span>

<span class="mark">38 . I MOD="GP" S MODX=\$\$MOD^ICPTMOD(370,"I")</span>

<span class="mark">39 . I MOD="SG" S MODX=\$\$MOD^ICPTMOD(111,"I")</span>

<span class="mark">40 . I MOD="GG" S MODX=\$\$MOD^ICPTMOD(384,"I")</span>

<span class="mark">41 . I MOD="GH" S MODX=\$\$MOD^ICPTMOD(366,"I")</span>

May have to add mod manually, in case it can’t be matched.

42 . I \$P(MODX,U)'\>0 W !,"TABLE "\_TBL\_" MOD ERR: "\_MOD Q

43 . I PCT'?1N1P3N W !,"TABLE "\_TBL\_" MOD: "\_MOD\_" %ERR "\_PCT Q

<span class="mark">44 . S ^XTMP("FBMLT","2008-"\_TBL,MOD)=PCT\*100</span> Modify to the current year.

45 . S ENC("TOT")=ENC("TOT")+1

46 ;

EOF ; End Of File

48 S \$ZT=""

49 C ENF

50 U IO

51 W !,"COUNT IN FILE ",ENF," = ",ENC("TOT")

52 Q

LOAD ;

54 S FBC("NZ")=0,FBC("Z")=0,FBC("MZ")=0,FBC("NMZ")=0

55 S TBLN=0 F S TBLN=\$O(^XTMP("FBMLT",TBLN)) Q:TBLN="" D

56 . S FBC("Z")=FBC("Z")+1

57 . S TBLD=\$G(^XTMP("FBMLT",TBLN))

58 . ;

59 . ; add table if not in file

60 . S Y=\$O(^FB(162.98,"B",TBLN,0))

61 . I 'Y D Q:Y'\>0

62 . . S FBC("NZ")=FBC("NZ")+1

63 . . K DA,DIC

64 . . S DIC="^FB(162.98,",DLAYGO=162.98,DIC(0)="L",X=TBLN

65 . . I TBLD\]"" S DIC("DR")=".02///^S X=TBLD"

66 . . W "ADDING TABLE "\_TBLD,!

67 . . K DD,DO D FILE^DICN I Y'\>0 W !,"ERROR ADDING NEW TABLE ",TBLN

68 . . K DIC,DLAYGO

69 . K DA,DIC

70 . S DA(1)=+Y

71 . ; process modifiers in table

72 . S MOD="" F S MOD=\$O(^XTMP("FBMLT",TBLN,MOD)) Q:MOD="" D

73 . . I MOD="99" Q ; skip 99 since multiple modifiers can be entered

74 . . S FBC("MZ")=FBC("MZ")+1

75 . . I '\$O(^DIC(81.3,"B",MOD,0)) W !,"NOT IN FILE SKIPPING MOD ",MOD Q

76 . . S DA=\$O(^FB(162.98,DA(1),"M","B",MOD,0))

77 . . I DA'\>0 D Q:DA'\>0

78 . . . S FBC("NMZ")=FBC("NMZ")+1

79 . . . S DIC="^FB(162.98,"\_DA(1)\_",""M"",",DIC(0)="L",DIC("P")="162.98

1A"

80 . . . S X=MOD

81 . . . W "ADDING MOD "\_MOD,!

82 . . . K DD,DO D FILE^DICN I Y'\>0 W !,"ERROR ADDING MOD "\_MOD\_" in ",T

BLN

83 . . . K DIC,DLAYGO

84 . . . S DA=+Y

85 . . ;

86 . . S DIE="^FB(162.98,"\_DA(1)\_",""M"","

87 . . S DR=".02///^S X="""\_^XTMP("FBMLT",TBLN,MOD)\_""""

88 . . W "ADDING PERCENTAGE "\_^XTMP("FBMLT",TBLN,MOD),!

89 . . D ^DIE K DIE

90 W !!,"TABLES = ",FBC("Z")

91 W !,"NEW TABLES = ",FBC("NZ")

92 W !!,"MODIFIERS = ",FBC("MZ")

93 W !,"NEW MODIFIERS = ",FBC("NMZ")

94 Q

95 ;

UNIMOD ; Unique Modifiers and associated %(s)

97 K FB

98 ; loop thru tables for year

99 S DA=0 F S DA=\$O(^FB(162.98,DA)) Q:'DA S Y=\$G(^(DA,0)) D

100 . Q:\$P(Y,U)'\["2009-"

101 . ; loop thru modifiers on table

102 . S DA1=0 F S DA1=\$O(^FB(162.98,DA,"M",DA1)) Q:'DA1 S Y1=\$G(^(DA1,0

)) D

103 . . I \$P(Y1,U)\]"",\$P(Y1,U,2)\]"" S FB(\$P(Y1,U),\$P(Y1,U,2))=""

104 ;

105 ; display list of modifiers and their percentage(s)

106 S MOD="" F S MOD=\$O(FB(MOD)) Q:MOD="" D

107 . I "^GE^GN^GP^NR^RP^RR^SG^"'\[(U_MOD_U) S MODX=\$\$MOD^ICPTMOD(MOD,"E")

108 . I MOD="GE" S MODX=\$\$MOD^ICPTMOD(193,"I")

109 . I MOD="GN" S MODX=\$\$MOD^ICPTMOD(368,"I")

110 . I MOD="NR" S MODX=\$\$MOD^ICPTMOD(85,"I")

111 . I MOD="RP" S MODX=\$\$MOD^ICPTMOD(107,"I")

112 . I MOD="RR" S MODX=\$\$MOD^ICPTMOD(108,"I")

113 . I MOD="GP" S MODX=\$\$MOD^ICPTMOD(370,"I")

114 . I MOD="SG" S MODX=\$\$MOD^ICPTMOD(111,"I")

115 . W !!,"MODIFIER ",MOD,?20,\$P(MODX,U,3)

116 . W !," PERCENT(S) PAID:"

117 . S PCT="" F S PCT=\$O(FB(MOD,PCT)) Q:PCT="" W " "\_PCT\_","

118 Q

119 ;

<span class="mark">COPY00 ; Create 2009 mod level tables by coping the 2008 tables</span>

<span class="mark">121 S TBLN="2008-"</span>

<span class="mark">122 F S TBLN=\$O(^FB(162.98,"B",TBLN)) Q:TBLN=""!(\$E(TBLN,1,5)'="2008-")</span>

<span class="mark">D</span>

<span class="mark">123 . S FBDA=\$O(^FB(162.98,"B",TBLN,0))</span>

<span class="mark">124 . Q:'FBDA</span>

<span class="mark">125 . ; determine number of new table</span>

<span class="mark">126 . S TBLN01="2009"\_"-"\_\$P(TBLN,"-",2)</span>

<span class="mark">127 . ;</span>

<span class="mark">128 . ; quit if 2009 table already defined</span>

<span class="mark">129 . Q:\$O(^FB(162.98,"B",TBLN01,0))</span>

<span class="mark">130 . ;</span>

<span class="mark">131 . ;W !,TBLN,?10,FBDA,?20,TBLN01 Q</span>

<span class="mark">132 . ;</span>

<span class="mark">133 . ; add 2009 table</span>

<span class="mark">134 . K DA,DIC</span>

<span class="mark">135 . S DIC="^FB(162.98,",DLAYGO=162.98,DIC(0)="L",X=TBLN01</span>

<span class="mark">136 . K DD,DO D FILE^DICN I Y'\>0 W !,"ERROR ADDING NEW TABLE ",TBLN01</span>

<span class="mark">137 . K DIC,DLAYGO</span>

<span class="mark">138 . Q:Y'\>0</span>

<span class="mark">139 . ;</span>

<span class="mark">140 . W !,TBLN,?10,FBDA,?20,TBLN01,?30,+Y</span>

<span class="mark">141 . ; copy data</span>

<span class="mark">142 . M ^FB(162.98,+Y)=^FB(162.98,FBDA)</span>

<span class="mark">143 . S \$P(^FB(162.98,+Y,0),U)=TBLN01</span>

<span class="mark">144 . ; don't need to index since only "B" x-refs exist</span>

<span class="mark">145 ;</span>

<span class="mark">146 ;FBZFSM09</span>

<span class="mark">FBZFSR09 ;WCIOFO/MJE/TCK-IMPORT DOL CPT DATA FROM HOST FILE ; 12/1/08 1:11am</span>

2 Q

DOLI ; DOL import of CPT/HCPCS data (mod level, RVUs) from OWCP files

4 K ^XTMP("FBDOL")

5 S ^XTMP("FBDOL",0)=\$\$FMADD^XLFDT(DT,+120)\_"^"\_DT

6 ;D IDOL("\[BAUMANN.RBRVS2001\]FS01_CODE_RVU_CF.PRN")

7 ;D IDOL("\[ENFINGER.RBRVS2002\]FS02_CODE_RVU_CF.PRN")

8 ;D IDOL("\[HARTINJ\]FS03_CODE_RVU_CF.PRN")

9 ;D IDOL("USER\$:\[HARTINJ\]FS04_CODE_RVU_CF.PRN")

10 ;D IDOL("USER\$:\[KEHOET.RBRVS2008\]FS08_CODE_RVU_CF.PRN;")

<span class="mark">11 D IDOL("USER\$:\[CHANDARANAR.RBRVS2009\]FS08CODE_RVU_CF.CSV;")</span> Modify to the correct filename.

12 Q

IDOL(ENF) ;

14 ; Data will be extracted from a host file (ENF) and

15 ; imported into ^XTMP("FBDOL",

<span class="mark">16 ; Host File format \| 2008 - FROM CSV</span> Modify if format changes. <span class="mark"></span>

<span class="mark">17 ; CPT 1-7 \| PIECE 1</span>

<span class="mark">18 ; STATUS 11-13 \| PIECE 4</span>

<span class="mark">19 ; MODIFIER 8-12 19-22 \| PIECE 2</span>

<span class="mark">20 ; MOD LEVEL 13-17 28-31 \| PIECE 3</span>

<span class="mark">21 ; WORK RVU 18-23 40-46 \| PIECE 5</span>

<span class="mark">22 ; PE RVU 24-29 49-56 \| PIECE 6</span>

<span class="mark">23 ; MP RVU 30-35 60-66 \| PIECE 8</span>

<span class="mark">24 ; ;CONV FACTOR 39-45 \| PIECE 10</span>

<span class="mark">25 ; ;BRIEF DESC 49-END \| PIECE 12</span>

26 ;

<span class="mark">27 S ENC("TOT")=0</span>

<span class="mark">28 O ENF</span>

<span class="mark">29 S ML="",DLM=\$C(44) ;\$C(9) - OLD, 44=,FOR CSV</span>

<span class="mark">30 F U ENF S \$ZT="EOF^FBZFSR09" R ENX S \$ZT="" U IO D</span> Modify to point to the correct routine.

<span class="mark">31 . S CPT=\$P(ENX,DLM)</span>

<span class="mark">32 . S STATUS=\$P(ENX,DLM,4)</span>

<span class="mark">33 . S MOD=\$P(ENX,DLM,2)</span>

<span class="mark">34 . S ML=\$TR(\$P(ENX,DLM,3)," ")</span>

<span class="mark">35 . I \$L(ML)\<3,ML'="" S ML=\$E("00"\_ML,\$L(ML),\$L(ML)+2) ;add leading zer</span>

<span class="mark">os</span>

<span class="mark">36 . S WRVU=\$P(ENX,DLM,5)</span>

<span class="mark">37 . S PRVU=\$P(ENX,DLM,7)</span>

<span class="mark">38 . S MRVU=\$P(ENX,DLM,8)</span>

<span class="mark">39 . ;S CF=\$P(ENX,DLM,10) S CF=\$TR(\$E(ENX,67,72)," ")</span>

<span class="mark">40 . ;S BDESC=\$P(ENX,DLM,12) \$E(ENX,49,\$L(ENX))</span>

<span class="mark">41 . ;I PRVU="\*\*\*\*\*\*" S PRVU="0.00" W !,"PE RVU = \*\*\*\*\*\* for CPT ",CPT,"</span>

<span class="mark">",MOD</span>

<span class="mark">42 . ;I \$L(CPT)'=5!(WRVU'?1.3N1"."2N)!(PRVU'?1.4N1"."2N)!(MRVU'?1.3N1"."</span>

<span class="mark">2N) Q</span>

43 . ;I CPT_STATUS_MOD_ML_WRVU_PRVU_MRVU'=\$TR(\$E(ENX,1,66)," ") W !,"ERR

: ",ENX

44 . I CPT="" W !,"ERROR CPT: ",ENX Q

45 . S CPTM=CPT\_\$S(MOD\]"":"-"\_MOD,1:"")

46 . ;I ML=6,CPTM="G0002" S ML=14 ; correct table is 14 per DOL

47 . ;I ML?1N W !,"Added 0 to mod level ",ML," for CPT ",CPTM S ML="0"\_M

L

48 . ;I ML=550 S ML=50 W !,"Change mod level '550' to '50' per DOL for C

PT ",CPTM

49 . W !,CPT_U_STATUS_U_MOD_U_ML_U_WRVU_U_PRVU_U_MRVU

50 . S ^XTMP("FBDOL",CPTM)="2008^"\_ML_U_WRVU_U_PRVU_U_MRVU

51 . S ENC("TOT")=ENC("TOT")+1

52 ;

EOF ; End Of File

54 S \$ZT=""

55 C ENF

56 U IO

57 W !,"COUNT IN FILE ",ENF," = ",ENC("TOT")

58 Q

DOLML ; DOL mod level fill-in for lines with a modifier

60 S MOD="",U="^"

61 S CPTM=0 F S CPTM=\$O(^XTMP("FBDOL",CPTM)) Q:CPTM="" D

62 . S ENX=\$G(^XTMP("FBDOL",CPTM))

63 . Q:\$P(ENX,U,2)\]"" ; has mod level already

64 . S ML=\$S(\$P(CPTM,U)\["-":\$P(\$G(^XTMP("FBDOL",\$P(CPTM,"-"))),U,2),1:""

)

65 . S IY=\$P(^XTMP("FBDOL",CPTM),U)

66 . I ML\]"" S \$P(^XTMP("FBDOL",CPTM),U,2)=ML Q

67 . I ML="" D GETMOD(CPTM,IY,.MOD)

68 . I MOD S \$P(^XTMP("FBDOL",CPTM),U,2)=MOD Q

69 . W !,"NO MOD LEVEL TABLE FOR CPTM ",CPTM

70 Q

71 ;

GETMOD(CPTM,IY,MOD) ;GET MOD DATA FROM PREVIOUS INCOME YEAR

73 N IEN,SIEN,TIEN

74 S IEN=0,(SIEN,MOD)=""

75 S IEN=\$O(^FB(162.97,"B",CPTM,0))

76 I IEN\>0 D

77 .I \$D(^FB(162.97,IEN,"CY","B",2008)) D

78 ..S SIEN=\$O(^FB(162.97,IEN,"CY","B",2008,0))

79 ..Q:SIEN'\>0

80 ..I \$D(^FB(162.97,IEN,"CY",SIEN)) D

81 ...S MOD=\$P(\$G(^FB(162.97,IEN,"CY",SIEN,0)),U,2)

82 ...I MOD="" D

83 ....I \$D(^FB(162.97,IEN,"CY","B",2007)) D

84 .....S SIEN=\$O(^FB(162.97,IEN,"CY","B",2007,0))

85 .....Q:SIEN'\>0

86 .....I \$D(^FB(162.97,IEN,"CY",SIEN)) D

87 ......S MOD=\$P(\$G(^FB(162.97,IEN,"CY",SIEN,0)),U,2)

88 I MOD="" S MOD=0

89 Q

90 ;

EXAMDOL ;

92 S CPTM=0 F S CPTM=\$O(^XTMP("FBDOL",CPTM)) Q:CPTM="" D

93 . I '\$O(^ICPT("B",\$P(CPTM,"-"),0)) W !,"?CPT ",CPTM

94 Q

95 ;

DOLSZ ; dol sum rvu = z

97 W !,"DOL sum of RVUs is zero"

98 S CPTM=0 F S CPTM=\$O(^XTMP("FBDOL",CPTM)) Q:CPTM="" D

99 . S FBX=\$G(^XTMP("FBDOL",CPTM))

100 . S SUM=0 F I=3:1:5 S SUM=SUM+\$P(FBX,U,I)

101 . I SUM'\>0 W !,CPTM,?10,FBX K ^XTMP("FBDOL",CPTM)

102 Q

103 ;

HCFAI ; HCFA IMPORT

105 ;S ENF="\[BAUMANN.RBRVS2001B\]PPRRVU01.TXT"

106 ;S ENF="\[ENFINGER.RBRVS2002\]PPRRVU02.TXT"

107 ;S ENF="\[HARTINJ\]PPRRVU03.TXT"

108 ;S ENF="\[HARTINJ\]PPRRVU0307.TXT"

109 ;S ENF="\[HARTINJ\]PPRRVU04.TXT"

110 ;S ENF="USER\$:\[KEHOET.RBRVS2008\]PPRRVU08.TXT"

111 S ENF="USER\$:\[KEHOET.RBRVS2008\]PPRRVU08.TXT"

112 K ^XTMP("FBHCFA")

113 S ^XTMP("FBHCFA",0)=\$\$FMADD^XLFDT(DT,+120)\_"^"\_DT

114 S ENC("TOT")=0

115 O ENF

116 F U ENF S \$ZT="<span class="mark">EOF^FBZFSR09</span>" R ENX S \$ZT="" U IO D Modify to point to the correct routine.

117 . Q:\$E(ENX,1,3)="HDR"

118 . S CPT=\$TR(\$E(ENX,1,5)," ")

119 . S MOD=\$TR(\$E(ENX,6,7)," ")

120 . S STA=\$E(ENX,58)

121 . ;Q:"^D^X^"\[(U_STA_U) ; deleted codes or statutory exclusion

122 . Q:"^A^R^T^"'\[(U_STA_U) ; only codes used for Medicare payment

123 . Q:\$E(ENX,59)="+" ; RVU's are not used for Medicare payment

124 . S WRVU=\$TR(\$E(ENX,61,65)," ")

125 . S TNFPRVU=\$TR(\$E(ENX,68,72)," ")

126 . S TFPRVU=\$TR(\$E(ENX,86,90)," ")

127 . S MRVU=\$TR(\$E(ENX,104,109)," ")

128 . I \$L(CPT)'=5!(WRVU'?1.2N1"."2N)!(TNFPRVU'?1.2N1"."2N)!(TFPRVU'?1.2N

1"."2N)!(MRVU'?1.2N1"."2N) W !,"SKIPPING LINE ",ENX Q

129 . I CPT="" W !,"ERROR CPT: ",ENX Q

130 . S CPTM=CPT\_\$S(MOD\]"":"-"\_MOD,1:"")

131 . ;I '\$D(^XTMP("FBDOL",CPTM)) D Q

132 . ;. W !,"MISSING CPT-MOD: ",CPTM,!,ENX

133 . S ^XTMP("FBHCFA",CPTM)="2008^^"\_WRVU_U_TNFPRVU_U_TFPRVU_U_MRVU

134 . S ENC("TOT")=ENC("TOT")+1

135 Q

136 ;

EXAMHCFA ;

138 S CPTM=0 F S CPTM=\$O(^XTMP("FBHCFA",CPTM)) Q:CPTM="" D

139 . I '\$O(^ICPT("B",\$P(CPTM,"-"),0)) W !,"?CPT ",CPTM

140 Q

141 ;

HCFASZ ; hcfa sum rvu = 0

143 W !,"HCFA sum of RVUs is zero"

144 S CPTM=0 F S CPTM=\$O(^XTMP("FBHCFA",CPTM)) Q:CPTM="" D

145 . S FBX=\$G(^XTMP("FBHCFA",CPTM))

146 . S SUM=0 F I=3:1:6 S SUM=SUM+\$P(FBX,U,I)

147 . I SUM'\>0 W !,CPTM,?10,FBX K ^XTMP("FBHCFA",CPTM)

148 Q

149 ;

HCFAC ; HCFA compare

151 S CPTM=0 F S CPTM=\$O(^XTMP("FBHCFA",CPTM)) Q:CPTM="" D

152 . S FBDA=\$O(^FB(162.97,"B",CPTM,0))

153 . I 'FBDA W !,CPTM," NOT IN FILE ",^XTMP("FBHCFA",CPTM)

154 . S FBDA1=\$S(FBDA:\$O(^FB(162.97,FBDA,"CY","B",2009,0)),1:"")

155 . I 'FBDA1 W !,CPTM," NOT IN FILE FOR CY ",^XTMP("FBHCFA",CPTM)

156 . I FBDA,FBDA1 D

157 . . S XTMP=\$G(^XTMP("FBHCFA",CPTM))

158 . . S FILE=\$G(^FB(162.97,FBDA,"CY",FBDA1,0))

159 . . I +\$P(XTMP,U,3)'=+\$P(FILE,U,3) W !,CPTM," WORK RVU'S DIFFERENT, N

EW: ",\$P(XTMP,U,3)," OLD: ",\$P(FILE,U,3)

160 . . I +\$P(XTMP,U,4)'=+\$P(FILE,U,4) W !,CPTM," NON-FAC PE RVU'S DIFFER

ENT, NEW: ",\$P(XTMP,U,4)," OLD: ",\$P(FILE,U,4)

161 . . I +\$P(XTMP,U,5)'=+\$P(FILE,U,5) W !,CPTM," FAC PE RVU'S DIFFERENT,

NEW: ",\$P(XTMP,U,5)," OLD: ",\$P(FILE,U,5)

162 . . I +\$P(XTMP,U,6)'=+\$P(FILE,U,6) W !,CPTM," MP RVU'S DIFFERENT, NEW

: ",\$P(XTMP,U,6)," OLD: ",\$P(FILE,U,6)

163 . ;I '\$D(^XTMP("FBDOL",CPTM)) W !,CPTM," ",^XTMP("FBHCFA",CPTM)

164 Q

165 ;

FBHCFA ; loop thru existing data and compare against HCFA list

167 W !,"Check CPT-Mod to determine if missing from the HCFA data..."

168 F I="MISSING" S CNT(I)=0

169 S CPTM="" F S CPTM=\$O(^FB(162.97,"B",CPTM)) Q:CPTM="" D

170 . S FBDA=\$O(^FB(162.97,"B",CPTM,0))

171 . Q:'\$D(^FB(162.97,FBDA,"CY","B",2009)) ; not in current year

172 . I '\$D(^XTMP("FBHCFA",CPTM)) D Q

173 . . S CNT("MISSING")=CNT("MISSING")+1

174 . . W !,"Existing CPT-Mod ",CPTM," is missing from the HCFA data."

175 W !!

176 W !,"# Missing = ",CNT("MISSING")

177 Q

178 ;

DOLC ; DOL compare

180 S CPTM="" F S CPTM=\$O(^XTMP("FBDOL",CPTM)) Q:CPTM="" D

181 . I '\$D(^XTMP("FBHCFA",CPTM)) W !,CPTM," ",^XTMP("FBDOL",CPTM)

182 Q

183 ;

LOAD ; load data into 162.97

185 S FBC("NZ")=0,FBC("Z")=0

186 S CPTM="" F S CPTM=\$O(^XTMP("FBHCFA",CPTM)) Q:CPTM="" D

187 . S FBC("Z")=FBC("Z")+1

188 . S FBY=^XTMP("FBHCFA",CPTM)

189 . S CPT=\$P(CPTM,"-")

190 . ;

191 . I '\$O(^ICPT("B",CPT,0)) W !,"NOT IN ICPT. SKIPPING CPT-MOD ",CPTM Q

192 . ;

193 . I \$P(FBY,U,3)+\$P(FBY,U,4)+\$P(FBY,U,5)+\$P(FBY,U,6)'\>0,\$P(FBY,U,7)=""

D Q

194 . . W !,"SUM OF RVUs '\> 0 and base units null. SKIPPING CPT-MOD ",CPT

M

195 . ;

196 . S CAT=\$\$CPTCAT(CPT)

197 . I CAT="" W !,"UNKNOWN CPT CATEGORY. ",CPTM

198 . ;

199 . S Y=\$O(^FB(162.97,"B",CPTM,0))

200 . I 'Y D Q:Y'\>0

201 . . S FBC("NZ")=FBC("NZ")+1

202 . . K DA,DIC

203 . . S DIC="^FB(162.97,",DLAYGO=162.97,DIC(0)="L",X=CPTM

204 . . I CAT\]"" S DIC("DR")=".02///"\_CAT

205 . . K DD,DO D FILE^DICN I Y'\>0 W !,"ERROR ADDING NEW CPT-MOD ",CPTM

206 . . K DIC,DLAYGO

207 . ;

208 . K DA,DIC

209 . S DA(1)=+Y

210 . S DA=\$O(^FB(162.97,DA(1),"CY","B",2009,0))

211 . I DA'\>0 D Q:DA'\>0

212 . . S DIC="^FB(162.97,"\_DA(1)\_",""CY"",",DIC(0)="L",DIC("P")="162.971

A"

213 . . S X=2009

214 . . K DD,DO D FILE^DICN I Y'\>0 W !,"ERROR ADDING 2008 RVUs for ",CPTM

215 . . K DIC,DLAYGO

216 . . S DA=+Y

217 . ;

218 . S DIE="^FB(162.97,"\_DA(1)\_",""CY"","

219 . S DR=""

220 . I \$P(FBY,U,2)\]"" S DR=DR\_".02///"\_\$P(FBY,U,2)\_";"

221 . S DR=DR\_".03///"\_\$P(FBY,U,3)\_";.04///"\_\$P(FBY,U,4)\_";.05///"\_\$P(FBY

,U,5)\_";.06///"\_\$P(FBY,U,6)

222 . D ^DIE K DA,DIE

223 W !!,"CPTM = ",FBC("Z")

224 W !,"NEW CPTM = ",FBC("NZ")

225 Q

226 ;

MRGDOL ; MERGE DOL DATA INTO FILED HFCA DATA

228 ; loop thru CPT-MODIFIERS

229 S CNT("MLA")=0,CNT("MLC")=0,CNT("MLD")=0

230 K DA

231 S DA(1)=0 F S DA(1)=\$O(^FB(162.97,DA(1))) Q:'DA(1) D

232 . S CPTM=\$P(\$G(^FB(162.97,DA(1),0)),U)

233 . I CPTM="" W !,"ERROR CPTM NULL FOR ENTRY ",DA(1)

234 . S DA=\$O(^FB(162.97,DA(1),"CY","B",2008,0)) Q:'DA ; no 2008 data

235 . S HCFA=\$G(^FB(162.97,DA(1),"CY",DA,0))

236 . S DOL=\$G(^XTMP("FBDOL",CPTM))

237 . I DOL="" W !,"MISSING DOL DATA FOR ",CPTM Q

238 . I +\$P(DOL,U,3)'=+\$P(HCFA,U,3) W !,CPTM," WORK RVU'S DIFFERENT, HCFA

: ",\$P(HCFA,U,3)," DOL: ",\$P(DOL,U,3)

239 . I +\$P(DOL,U,4)'=+\$P(HCFA,U,4) W !,CPTM," PE RVU'S DIFFERENT, HCFA:

",\$P(HCFA,U,4)," DOL: ",\$P(DOL,U,4)

240 . I +\$P(DOL,U,5)'=+\$P(HCFA,U,6) W !,CPTM," MP RVU'S DIFFERENT, HCFA:

",\$P(HCFA,U,6)," DOL: ",\$P(DOL,U,5)

241 . ; update mod level ---The following line comment out whne doing new

yr

242 . I \$P(HCFA,U,2)'=\$P(DOL,U,2) W !,"CURRENT ML: ",\$P(HCFA,U,2)," IS DI

FFERENT FROM DOL ML: ",\$P(DOL,U,2)," FOR ",CPTM

243 . I \$P(DOL,U,2)="" W !,"NO MOD LEVEL DATA FOR ",CPTM Q

244 . S TBLN="2008"\_"-"\_\$P(DOL,U,2)

245 . I '\$D(^FB(162.98,"B",TBLN)) W !,"TABLE: ",TBLN," IS NOT ON FILE FOR

",CPTM Q

246 . ;Q ; \*\*\* TEMP QUIT \*\*\*

247 . S DIE="^FB(162.97,"\_DA(1)\_",""CY"","

248 . S DR=".02///"\_\$P(DOL,U,2)

249 . I \$P(DOL,U,2)="",\$P(HCFA,U,2)'="" S DR=".02////@"

250 . D ^DIE K DIE

251 Q

252 ;

CPTCAT(CPT) ; return cpt category (or 0 if none)

254 N RET,X,Y

255 S RET=""

256 S X=\$P(\$\$CPT^ICPTCOD(CPT),U,4)

257 I X\>0 S Y=\$P(\$\$CAT^ICPTAPIU(X),U,4)

258 I \$G(Y)\["EVALUATION" S Y="EVALUATION & MANAGEMENT"

259 I \$G(Y)\]"" S RET=Y

260 ;I "00100"'\]CPT&(CPT'\]"01999") S RET="ANESTHESIA"

261 ;I "10040"'\]CPT&(CPT'\]"69979") S RET="SURGERY"

262 ;I "70010"'\]CPT&(CPT'\]"79999") S RET="RADIOLOGY"

263 ;I "80049"'\]CPT&(CPT'\]"89399") S RET="LABORATORY"

264 ;I "90700"'\]CPT&(CPT'\]"99199") S RET="MEDICINE"

265 ;I "99201"'\]CPT&(CPT'\]"99499") S RET="EVALUATION & MANAGEMENT"

266 Q RET

267 ;

COPYMOD ; COPY MOD LEVEL TABLES FROM 2008 TO 2009

269 S FBDA=0 F S FBDA=\$O(^FB(162.97,FBDA)) Q:'FBDA D

270 . S CY00=\$O(^FB(162.97,FBDA,"CY","B","2008",0))

271 . S CY01=\$O(^FB(162.97,FBDA,"CY","B","2009",0))

272 . Q:'CY00

273 . Q:'CY01

274 . S TBLN00=\$P(^FB(162.97,FBDA,"CY",CY00,0),U,2)

275 . S \$P(^FB(162.97,FBDA,"CY",CY01,0),U,2)=TBLN00

276 . W !,FBDA,?10,CY00,?20,CY01,?30,TBLN00

277 Q

278 ;

279 <span class="mark">;FBZFSR09</span> Modify to the current year.

Once the routines have been modified. It is possible to load the modifier data into files 162.97 and 162.98.

The steps are as follows:

A. D COPYMOD^FBZFSRYY– Since modifier level tables are no longer being used or provided, the data can just be copied from the previous year. This loads the data from the previous year modifier level data into file \#162.97
B. COPY00^FBZFSMYY– Since modifier level tables are no longer being used or provided, the data can just be copied from the previous year. This loads the data from the previous year modifier level data into file \#162.98

# Updating the Conversion Factors (File \#162.99 routine FBZRVUYY). 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Note that there are many references to the year, make sure to update all of them.

FBXIP109 ;ALB/RC-PATCH INSTALL ROUTINE ; 12/29/08 1:54pm

;;3.5;FEE BASIS;\*\*109\*\*;JAN 30, 1995;Build 10

Q

;

PS ; post-install entry point

; create KIDS checkpoints with call backs

N FBX

F FBX="EN" D

. S Y=\$\$NEWCP^XPDUTL(FBX,FBX\_"^FBXIP109")

. I 'Y D BMES^XPDUTL("ERROR Creating "\_FBX\_" Checkpoint.")

Q

;

EN ; Begin Post-Install

D CF ;Add Conv factors

D POV ;Update Place of Visit

Q

CF ; add conversion factors for calendar year <span class="mark">2009 RBRVS</span> fee schedule

; File 162.99 is being updated in the post install because the Fee

; Basis software examines this file to determine the latest available

; fee schedule. By doing this at the end of the patch installation,

; users can continue to use the payment options during the install.

D BMES^XPDUTL(" Filing conversion factor for <span class="mark">RBRVS 2009</span> fee schedule."

)

N DD,DO,DA,DIE,DR,X,Y

S DA(1)=0 F S DA(1)=\$O(^FB(162.99,DA(1))) Q:'DA(1) D

. S DA=\$O(^FB(162.99,DA(1),"CY","B",<span class="mark">2009</span>,0))

. I DA'\>0 D Q:DA'\>0

. . S DIC="^FB(162.99,"\_DA(1)\_",""CY"",",DIC(0)="L",DIC("P")="162.991A"

,DLAYGO=162.991

<span class="mark">. . S X=2009</span>

. . K DD,DO D FILE^DICN

. . K DIC,DLAYGO

. . S DA=+Y

. ;

. S DIE="^FB(162.99,"\_DA(1)\_",""CY"","

<span class="mark">. S DR=".02///"\_\$S(DA(1)=1:20.9150,1:36.0666)</span> Note the first conversion factor is the anesthesia factor, the second is the medical conversion factor.

. D ^DIE

Q

POV ;Update Place of Visit Ignore, this was an additional update specific to FB\*3.5\*109

;

;Add 67,68,69,56

D BMES^XPDUTL("Updating Place of Visit entries in the FEE BASIS PURPOSE

OF VISIT file (#161.82)")

N FBCNT,X,NEWENTRY,NEWCODE,NEWPOV,POVCHECK

F FBCNT=1:1 S NEWENTRY=\$P(\$T(NEWTABLE+FBCNT),";;",2) Q:NEWENTRY="EXIT"

D

.S NEWPOV=\$P(NEWENTRY,"^",1),NEWCODE=\$P(NEWENTRY,"^",2)

.S POVCHECK=\$O(^FBAA(161.82,"C",NEWCODE,"")) D

..I POVCHECK D BMES^XPDUTL("Code: "\_NEWCODE\_" already exists, please ve

rify this entry in the FEE BASIS PURPOSE OF VISIT file (#161.82).") Q

..N DIC,DA,DR,DLAYGO,DINUM

..S DIC="^FBAA(161.82,",DIC(0)="L",DLAYGO=161.82

..S X=NEWPOV,DIC("DR")="3///^S X=NEWCODE",DINUM=NEWCODE

..K DD,D0 D FILE^DICN K DIC,DA,DLAYGO

;Inactivate POV 20

N DA,DIE,DR

S DA=\$O(^FBAA(161.82,"B","CLASS IIr DENTAL TREATMENT",""))

S DIE="^FBAA(161.82,",DR="4///01/01/09"

D

.I DA D ^DIE Q

.D BMES^XPDUTL("Purpose of Visit 20, ""CLASS IIr DENTAL TREATMENT"", do

es not exist.")

Q

NEWTABLE ;New POVs Ignore, this was an additional update specific to FB\*3.5\*109

;;Dialysis^56

;;Outpatient Maternity Care Services^67

;;Bowel and Bladder care: Agency^68

;;Bowel and Bladder care: Family caregiver^69

;;EXIT

;FBXIP109

# Update the Calculators (Routine FBAAFSR). 

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

CALC(FBCY,FAC,FBCPTY0,FBGPCIY0,FBCF) ;

; Input

; FBCY = calendar year (4 digit)

; FAC = facility flag (0 or 1)

; FBCPTY0 = zero node from file 162.71

; FBGPCI0 = zero node from file 162.61

; FBCF = conversion factor (number)

; Returns \$ amount

;

N GPCI,RVU,FBI,TMP,TMPRVU

S FBAMT=0

<span class="mark">;Old formula for RBRVS pre-2007 payment amounts</span><span class="mark">I DOS\<3070101 D</span>

<span class="mark">.S RVU(1)=\$P(FBCPTY0,U,3)</span>

<span class="mark">I (DOS=3070101!(DOS\>3070101)&(DOS\<3080101)) D</span>

<span class="mark">.;New formula for RBRVS 2007 payment amounts</span>

<span class="mark">.;Multiply Work RVU by the Budget Neutrality Adjustor (0.8994)</span>

<span class="mark">.S TMP=\$P(FBCPTY0,U,3),TMPRVU=\$J((TMP\*(.8994)),".",2)</span>

<span class="mark">.S RVU(1)=TMPRVU</span>

<span class="mark">I (DOS=3080101!(DOS\>3080101)&(DOS\<3090101)) D</span>

<span class="mark">.;New formula for the RBRVS 2008 payment amounts</span>

<span class="mark">.;Multiply Work RVU by the Budget Neutrality Adjustor (0.8994)</span>

<span class="mark">.S TMP=\$P(FBCPTY0,U,3),TMPRVU=\$J((TMP\*(.8806)),".",2)</span>

<span class="mark">.S RVU(1)=TMPRVU</span>

<span class="mark">;RBRVS 2009 does not have a budget neutrality adjustor.</span>

<span class="mark">I (DOS=3090101!(DOS\>3090101)) D</span>

<span class="mark">.S RVU(1)=\$P(FBCPTY0,U,3)</span>

S RVU(2)=\$P(FBCPTY0,U,4+FAC)

S RVU(3)=\$P(FBCPTY0,U,6)

F FBI=2,3,4 S GPCI(FBI-1)=\$P(FBGPCIY0,U,FBI)

<span class="mark">S FBAMT=((RVU(1)\*GPCI(1))+(RVU(2)\*GPCI(2))+(RVU(3)\*GPCI(3)))\*FBCF</span>

; some procedures can't be performed in a facility setting by

; definition. the facility PE RVU for such a procedure is a null

; value.

; when facility setting - check for a null PE value and don't return am

t

I RVU(2)="",FAC S FBAMT=0 Q

Q

;

The line <span class="mark">S FBAMT=((RVU(1)\*GPCI(1))+(RVU(2)\*GPCI(2))+(RVU(3)\*GPCI(3)))\*FBCF</span> is the one that applies the actual calculation. In previous years, there has been a budget neutrality adjustor. Which has always been applied to RVU(1). The key to this section will be adding a line to handle the 2010 calculations. For example, if there isn’t a budget neutrality adjustor for 2010. The following modifications will need to be made:

Original

<span class="mark">I (DOS=3090101!(DOS\>3090101)) D</span>

<span class="mark">.S RVU(1)=\$P(FBCPTY0,U,3)</span>

S RVU(2)=\$P(FBCPTY0,U,4+FAC)

2010 version:

<span class="mark">I (DOS=3090101!(DOS\>3090101))&(DOS\<3100101) D</span>

<span class="mark">.S RVU(1)=\$P(FBCPTY0,U,3)</span>

I (DOS=3100101!(DOS\>3100101) D.S RVU(1)=\$P(FBCPTY0,U,3)

S RVU(2)=\$P(FBCPTY0,U,4+FAC)

Add the conversion factors for CY to file \#162.99. There are only six entries in this file so the data is normally entered manually, instead of updating the two routines above. Historically, there has been one conversion factor for anesthesia services and one conversion factor for all other services. The software checks this file to see what calendar years are available.

The steps are as follows:

A. Edit each one of the six entries in the file and enter the conversion factor for calendar year from the information printed in the Federal Register.

Steps to perform an update.1. Modify the routines as needed above.2. Create a build and transport the following items.Files:162.96162.97162.98162.99