---
consolidated_title: "kaajee quick setup guide"
app_code: KAAJEE
doc_type: SG-SET
master_source: "KAAJEE 1.0.1 Quick Setup Guide (WebLogic 8.1)"
master_pub_date: revision_count: 0
consolidated_from: 2 versions
prior_versions:
  - "KAAJEE 1.0.0 Quick Setup Guide (WebLogic 8.1)"
---

QUICK SETUP GUIDEKAAJEE 1.0.1.xxx & SSPI 1.0.0.010

Throughout this document, if you were a test site prior to the final release of KAAAJEE 1.0.1.xxx, we have notated those installation steps/procedures that have special information based on the final software upgrades that may affect how you install the released version of KAAJEE or other pertinent information. The upgrade information will be preceded by "UPGRADES:".

<table>
<colgroup>
<col style="width: 8%" />
<col style="width: 42%" />
<col style="width: 49%" />
</colgroup>
<thead>
<tr class="header">
<th><strong>Step</strong></th>
<th><strong>Procedure</strong></th>
<th><strong>Doc Reference</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>A</strong></td>
<td colspan="2"><strong>VistA M Server—KAAJEE-related Patches</strong></td>
</tr>
<tr class="even">
<td>1</td>
<td><p>Install the following Kernel patches in your VistA M Server account (listed in patch number order):</p>
<ul>
<li><p><sup>*</sup>XU*8.0*265</p></li>
<li><p><sup>*</sup>XU*8.0*329 (Original KAAJEE Patch)</p></li>
<li><p><sup>*</sup>XU*8.0*337</p></li>
<li><p><sup>*</sup>XU*8.0*361</p></li>
<li><p><sup>*</sup>XU*8.0*430</p></li>
<li><p>XU*8.0*451</p></li>
</ul>
<p><strong>UPGRADES:</strong></p>
<p>Skip this step if no new test versions of these patches are indicated. Otherwise, follow the e-mail and/or patch installation instructions and note any patch dependencies.</p>
<blockquote>
<p><sup>*</sup>Released patches.</p>
</blockquote></td>
<td><p><em>KAAJEE Installation Guide</em>, Chapter 3.</p>
<p>Download patches on FORUM Patch Module and KAAJEE Download Web site (<a href="http://vista.med.va.gov/kernel/kaajee/download.asp">http://vista.med.va.gov/kernel/kaajee/download.asp</a>). Install patches in sequence order.</p></td>
</tr>
<tr class="odd">
<td>2</td>
<td><p>Install the following RPC Broker patch in your VistA M Server account:</p>
<ul>
<li><p><sup>*</sup>XWB*1.1*35</p></li>
</ul>
<p><strong>UPGRADES:</strong></p>
<p><sup>*</sup>NA, Released patch.</p></td>
<td><p><em>KAAJEE Installation Guide</em>, Chapter 3.</p>
<p>Download patch on FORUM Patch Module.</p></td>
</tr>
<tr class="even">
<td><strong>B</strong></td>
<td colspan="2"><strong>Application Server</strong><strong>—KAAJEE SSPI Baseline</strong></td>
</tr>
<tr class="odd">
<td>1</td>
<td><p>Create Server Domain (e.g., kaajeewebdomain) on BEA WebLogic Application Server.</p>
<p><strong>UPGRADES:</strong></p>
<p>Skip this step if the domain has already been created.</p></td>
<td><em>KAAJEE Installation Guide</em>, Pages 4-3 to 4-10.</td>
</tr>
<tr class="even">
<td>2</td>
<td><p>Undeploy previous/old Security Service Provider Interface (SSPIs).</p>
<p><strong>UPGRADES:</strong></p>
<p>Before installing any new version of the KAAJEE SSPIs on the BEA WebLogic server, users <em>must</em> remove any previously installed KAAJEE SSPIs.</p>
<p><strong>VIRGIN INSTALLATIONS:</strong></p>
<p>Skip this step if you have <em>not</em> previously installed a previous version of the KAAJEE SSPIs.</p></td>
<td><em>KAAJEE Installation Guide</em>, Pages 4-11 to 4-13.</td>
</tr>
<tr class="odd">
<td>3</td>
<td><p>Deploy new/updated SSPIs.</p>
<p>Create an SSPI staging folder on the application server (i.e., &lt;SSPI_STAGING_FOLDER&gt;).</p>
<p><strong>UPGRADES:</strong></p>
<p>Skip this step if the staging area has already been created.</p></td>
<td><em>KAAJEE Installation Guide</em>, Page 4-14 to 4-15.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Decompress/Unzip the kaajee_security_provider_1.0.0.010.zip distribution in the BEA WebLogic Application Server staging folder (i.e., &lt;SSPI_STAGING_FOLDER&gt;).</td>
<td><em>KAAJEE Installation Guide</em>, Page 4-15 to 4-15.</td>
</tr>
<tr class="odd">
<td><strong>C</strong></td>
<td colspan="2"><strong>Application Server—KAAJEE SSPI Configuration</strong></td>
</tr>
<tr class="even">
<td>1</td>
<td><p><strong>Admin Server:</strong> In order for the classes contained in the SSPI, Apache connection pool jar files, and third party jar files to be found at run-time, modify either of the following files on the BEA WebLogic Admin Server:</p>
<ul>
<li><p>Linux—startWebLogic.sh</p></li>
<li><p>Windows—startWebLogic.cmd</p></li>
</ul></td>
<td><em>KAAJEE Installation Guide</em>, Pages 4-16 to 4-22.</td>
</tr>
<tr class="odd">
<td>2</td>
<td><strong>Managed Server(s):</strong> Modify the KAAJEE-related Class Path and Arguments on the BEA WebLogic Managed Server(s). Use the BEA WebLogic Server Console to navigate to the Remote Start tab on the Configuration tab to update the Managed Server(s) KAAJEE-related class path and arguments.</td>
<td><em>KAAJEE Installation Guide</em>, Pages 4-23 to 4-31.</td>
</tr>
<tr class="even">
<td><strong>D</strong></td>
<td colspan="2"><strong>Database—KAAJEE Baseline</strong></td>
</tr>
<tr class="odd">
<td>1</td>
<td><p>Contact the Database Administrator (DBA) to create a KAAJEE database schema and SSPI tables on the Oracle or Caché Database.</p>
<p><strong>UPGRADES:</strong></p>
<p>Skip this step if the DBA has already created the KAAJEE database schema and tables, unless it is specifically noted in the KAAJEE software release e-mail or Web site that changes are required.</p></td>
<td><em>KAAJEE Installation Guide</em>, Pages 4-31 to 4-34.</td>
</tr>
<tr class="even">
<td>2</td>
<td>Edit the KaajeeDatabase.properties file in the &lt;SSPI_STAGING_FOLDER&gt;/kaajee_<br />
security_provider/props directory.</td>
<td><em>KAAJEE Installation Guide</em>, Pages 4-34 to 4-35.</td>
</tr>
<tr class="odd">
<td>3</td>
<td><p>Restart the BEA WebLogic Application Server Domain:</p>
<ul>
<li><p>Linux—startWebLogic.sh</p></li>
<li><p>Windows—startWebLogic.cmd</p></li>
</ul></td>
<td><em>KAAJEE Installation Guide</em>, Page 4-36 to 4-37.</td>
</tr>
<tr class="even">
<td>4</td>
<td>Configure the Custom Security Authentication Providers in the BEA WebLogic Application Server.</td>
<td><em>KAAJEE Installation Guide</em>, Pages 4-38 to 4-45.</td>
</tr>
<tr class="odd">
<td><strong>E</strong></td>
<td colspan="2"><strong>Application Server—Miscellaneous</strong></td>
</tr>
<tr class="even">
<td>1</td>
<td><p>Configure Standard Data Services (SDS) 3.0 (or higher) JDBC connections with the BEA WebLogic Server.</p>
<p><strong>UPGRADES:</strong></p>
<p>Skip this step if the SDS JDBC connections have already been configured.</p></td>
<td><em>KAAJEE Installation Guide</em>, Page 4-45.</td>
</tr>
<tr class="odd">
<td>2</td>
<td>Edit the kaajeeConfig.xml file: Edit the Station Numbers in the &lt;station-numbers&gt; xml tags under the &lt;login-station-numbers&gt; tag with the appropriate Station Numbers that are valid for the user to log into for the Web-based application.</td>
<td><em>KAAJEE Installation Guide</em>, Pages 4-45 to 4-47.</td>
</tr>
<tr class="even">
<td>3</td>
<td>Test the KAAJEE installation using the KAAJEE Sample Web Application.</td>
<td><em>KAAJEE Installation Guide</em>, Pages 4-48 to 4-52.</td>
</tr>
<tr class="odd">
<td>4</td>
<td><p>Configure log4j for KAAJEE.</p>
<p><strong>UPGRADES:</strong></p>
<p>Skip this step if log4j has already been configured.</p></td>
<td><em>KAAJEE Installation Guide</em>, Pages 4-53 to 4-55.</td>
</tr>
</tbody>
</table>