---
title: "Kernel 8.0 Developerâ€™s Guide: DNS User Guide"
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: "Developerâ€™s Guide: DNS"
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
  - domain
  - span
  - guide
  - kernel
  - table
  - developer
  - contents
  - class
  - xlfnslk
  - addresses
page_count: 0
word_count: 1421
section_count: 4
table_count: 1
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: August 2025
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_dns_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_dns_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=10"
---

---
title: |
  Kernel 8.0 Developer’s Guide:

  <span id="_Toc204259293" class="anchor"></span>Domain Name Service (DNS) Developer Tools  
  User Guide
---

![](kernel-8-0-developer-s-guide-dns-user-guide/001.png)

August 2025

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Product Delivery Service (PDS)

<span id="_Toc234301875" class="anchor"></span>Revision History

![](kernel-8-0-developer-s-guide-dns-user-guide/002.png) REF: For the archived document revision history, see “<u>Appendix A—Revision History Archive</u>.”

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
<td><p>Initial document creation: <em>Kernel Developer’s Guide: Domain Name Service (DNS) Developer Tools User Guide</em>.</p>
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

<span id="_Toc234301876" class="anchor"></span>List of Figures

<span id="_Ref38421374" class="anchor"></span>Orientation

![](kernel-8-0-developer-s-guide-dns-user-guide/003.png) REF: For an orientation to this manual, please refer to the “Orientation” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg.pdf#Main_Orientation).

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Overview](#overview)
- [Application Programming Interfaces (APIs)](#application-programming-interfaces-apis)
  - [\$\$ADDRESS^XLFNSLK(): Convert Domain Name to IP Addresses](#addressxlfnslk-convert-domain-name-to-ip-addresses)
    - [Examples](#examples)
  - [MAIL^XLFNSLK(): Get IP Addresses for a Domain Name](#mailxlfnslk-get-ip-addresses-for-a-domain-name)
    - [Examples](#examples-1)
- [Appendix A—Revision History Archive](#appendix-arevision-history-archive)
The *Kernel 8.0 Developer’s Guide: Domain Name Service (DNS) Developer Tools User Guide* is part of the *Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide*.

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Domain Name System (DNS) is a fundamental component of the internet infrastructure that translates human-readable domain names (like www.example.com) into numerical IP addresses (such as 192.0.2.1) that computers use to identify each other on the network. This translation is crucial because, while domain names are easy for humans to remember, computers and network devices use IP addresses to locate and communicate with each other.

Key Functions of DNS include:

- Domain Name Resolution: The primary function of DNS is to resolve domain names to IP addresses. When a user types a domain name into a web browser, the DNS system translates this domain name into an IP address that the browser can use to locate the web server. This process involves several steps and different types of DNS servers, including recursive resolvers, root name servers, TLD (Top-Level Domain) servers, and authoritative name servers.
- Hierarchical and Distributed System: DNS is designed as a hierarchical and distributed system to ensure scalability and reliability. The DNS hierarchy starts from the root level, followed by TLDs (such as .com, .org), and then second-level domains (like example.com). Each level can delegate authority to lower levels, allowing for a distributed management of domain names.
- Caching: To improve efficiency and reduce the load on DNS servers, DNS responses are often cached. This means that once a DNS resolver has translated a domain name to an IP address, it stores this information for a certain period. Subsequent requests for the same domain name can be answered from the cache, speeding up the resolution process.
- Load Balancing and Redundancy: DNS can be used to distribute traffic across multiple servers by associating a domain name with multiple IP addresses. This load balancing enhances the reliability and performance of websites and services. Additionally, DNS can provide redundancy by directing traffic to alternative servers if one server becomes unavailable.
- Security: DNS plays a role in internet security through mechanisms like DNSSEC (DNS Security Extensions), which helps prevent attacks such as DNS spoofing and cache poisoning. DNSSEC adds a layer of security by enabling the verification of DNS data authenticity.
- Global Accessibility: DNS is a global system that allows users from anywhere in the world to access websites and services using domain names. This global reach is essential for the functioning of the internet as a unified network.

# Application Programming Interfaces (APIs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Several Domain Name Service (DNS) APIs and Extrinsic Functions are available for developers. These APIs and Extrinsic Functions are described below.

## \$\$ADDRESS^XLFNSLK(): Convert Domain Name to IP Addresses

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Domain Name Service (DNS)

ICR \#: 3056

Description: The \$\$ADDRESS^XLFNSLK extrinsic function calls the Domain Name Service (DNS) to convert a domain name into its IP addresses. The IP addresses of the DNS being called are in the DNS IP (#8989.3,51) field in the KERNEL SYSTEM PARAMETERS (#8989.3) file.

![](kernel-8-0-developer-s-guide-dns-user-guide/004.png) NOTE: This API is IPv6 compliant.

Format: \$\$ADDRESS^XLFNSLK(domain_name\[,type\])

Input Parameters: domain_name: (required) This is the fully qualified domain name (such as \<REDACTED\>.VA.GOV).

type: (optional) This input parameter is from the set A: IPv4 address (the default), AAAA: IPv6 address, CNAME: alias.

Output: returns: Returns a comma-separated list of IP addresses that are associated with the input domain.

### Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### Example 1

<span id="_Toc199950563" class="anchor"></span>Figure 1: \$\$ADDRESS^XLFNSLK API—Example 1

\><span class="mark">S X=\$\$ADDRESS^XLFNSLK("\<REDACTED\>.VA.GOV")</span>

\><span class="mark">W X</span>

99.9.99.999

#### Example 2

<span id="_Toc199950564" class="anchor"></span>Figure 2: \$\$ADDRESS^XLFNSLK API—Example 2

\><span class="mark">S X=\$\$ADDRESS^XLFNSLK("www.google.com","AAAA" )</span>

\><span class="mark">W X</span>

2607:F8B0:400E:0C02:0000:0000:0000:0067

## MAIL^XLFNSLK(): Get IP Addresses for a Domain Name

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: Domain Name Service (DNS)

ICR \#: 3056

Description: The MAIL^XLFNSLK API calls the Domain Name Service (DNS) to get the MX records for a domain name with its IP addresses.

![](kernel-8-0-developer-s-guide-dns-user-guide/005.png) NOTE: This API is IPv6 compliant.

Format: MAIL^XLFNSLK(.return,domain_name)

Input Parameters: .return: (required) A local variable passed by reference to hold the return array.

domain_name: (required) This parameter is a fully qualified domain name (such as \<REDACTED\>.VA.GOV).

Output Parameters:.return: Returns data in the array passed in by reference. The data is subscripted by priority. The domain_name parameter is a fully qualified domain name (such as \<REDACTED\>.VA.GOV).

### Examples

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

#### IPv4 Example

<span id="_Toc199950565" class="anchor"></span>Figure 3: MAIL^XLFNSLK API Example: IPv4

\><span class="mark">K ZX D MAIL^XLFNSLK(.ZX,"\<REDACTED\>.VA.GOV") ZW ZX</span>

ZX=2

ZX(5)=a2.\<REDACTED\>.VA.GOV.^99.9.99.99

ZX(10)=a1.\<REDACTED\>.VA.GOV.^99.9.99.99

#### IPv6 Example

<span id="_Toc199950566" class="anchor"></span>Figure 4: MAIL^XLFNSLK API Example: IPv6

\><span class="mark">K ZX D MAIL^XLFNSLK(.ZX,"GMAIL.COM") ZW ZX</span>

ZX=5

ZX(5)="gmail-smtp-in.l.google.COM.^2607:F8B0:4001:0C0E:0000:0000:0000:001A"

ZX(10)="alt1.gmail-smtp-in.l.google.COM.^2607:F8B0:400D:0C0C:0000:0000:0000:001B"

ZX(20)="alt2.gmail-smtp-in.l.google.COM.^2607:F8B0:400C:0C0A:0000:0000:0000:001B"

ZX(30)="alt3.gmail-smtp-in.l.google.COM.^2A00:1450:400C:0C08:0000:0000:0000:001B"

ZX(40)="alt4.gmail-smtp-in.l.google.COM.^2A00:1450:400B:0C03:0000:0000:0000:001B"

# Appendix A—Revision History Archive

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section should be used to show all document revision history prior to the current year.

![](kernel-8-0-developer-s-guide-dns-user-guide/006.png) REF: For the most recent, current year document revision history, see the “[Revision History](#_Toc234301875)” section.

| Date | Revision | Description | Author |
|------|----------|-------------|--------|
| TBD  | TBD      | TBD         | TBD    |

<span id="Glossary" class="anchor"></span>Glossary

![](kernel-8-0-developer-s-guide-dns-user-guide/007.png) REF: For a glossary of terms specific to Kernel, see the “Glossary” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm.pdf#Main_Glossary).

![](kernel-8-0-developer-s-guide-dns-user-guide/008.png) REF: For a list of commonly used terms and acronyms, see the VA Glossary Power App.