---
title: "Kernel 8.0 Developerâ€™s Guide: XML Parser User Guide"
doc_type: UG
doc_label: User Guide
doc_layer: anchor
doc_subject: "Developerâ€™s Guide: XML Parser"
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
  - document
  - strong
  - parser
  - node
  - table
  - contents
  - mxmldom
  - span
  - returns
  - class
page_count: 0
word_count: 5660
section_count: 17
table_count: 1
figure_count: 0
appendix_count: 1
has_toc: False
is_stub: False
pub_date: August 2025
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_xml_parser_ug.docx"
pdf_url: "https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg_xml_parser_ug.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=10"
---

---
title: |
  Kernel 8.0 Developer’s Guide:

  <span id="_Toc204259887" class="anchor"></span>XML Parser (VistA) Developer Tools  
  User Guide
---

![](kernel-8-0-developer-s-guide-xml-parser-user-guide/001.png)

August 2025

Department of Veterans Affairs (VA)

Office of Information and Technology (OIT)

Product Delivery Service (PDS)

<span id="_Toc234301875" class="anchor"></span>Revision History

![](kernel-8-0-developer-s-guide-xml-parser-user-guide/002.png) REF: For the archived document revision history, see “<u>Appendix A—Revision History Archive</u>.”

<table>
<caption><p><span id="_Ref453857073" class="anchor"></span>Table 1: XML ENTITY CATALOG (#950) File—Stores External Entities and Assoc Public Identifiers</p></caption>
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
<td><p>Initial document creation: <em>Kernel Developer’s Guide: XML Parser (VistA) Developer Tools User Guide</em>.</p>
<p>This is part of the VASS Documentation Redesign Project. The content in this document came from the original <em>Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide</em> document, which was too large and cumbersome to maintain; so, it was broken down into smaller user guides for ease of use and maintenance going forward.</p>
<p><strong>Software Versions:</strong></p>
<p><strong>Kernel 8.0</strong></p>
<p><strong>Toolkit 7.3</strong></p></td>
<td>VistA Application Shared Services (VASS) Development Team</td>
</tr>
</tbody>
</table>

<span id="_Ref453857073" class="anchor"></span>Table 1: XML ENTITY CATALOG (#950) File—Stores External Entities and Assoc Public Identifiers

Patch Revisions

For the current patch history related to this software, see the Patch Module on FORUM.

Table of Contents

<span id="_Toc234301876" class="anchor"></span>List of Figures

<span id="_Toc207256655" class="anchor"></span>List of Tables

[Table 1: XML ENTITY CATALOG (#950) File—Stores External Entities and Assoc Public Identifiers [3](#_Ref453857073)](#_Ref453857073)

[Table 2: XML Parser—Event Types [20](#_Ref453856326)](#_Ref453856326)

<span id="_Hlt412359042" class="anchor"></span>Orientation

![](kernel-8-0-developer-s-guide-xml-parser-user-guide/003.png) REF: For an orientation to this manual, please refer to the “Orientation” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_dg.pdf#Main_Orientation).

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Overview](#overview)
    - [Event-Driven Interface](#event-driven-interface)
    - [World Wide Web Consortium Document Object Model Specification](#world-wide-web-consortium-document-object-model-specification)
    - [Entity Catalog](#entity-catalog)
    - [Term Definitions and XML Parser Concept](#term-definitions-and-xml-parser-concept)
    - [Known Issues](#known-issues)
- [Application Programming Interfaces (APIs)](#application-programming-interfaces-apis)
  - [\$\$ATTRIB^MXMLDOM(): XML—Get First or Next Node Attribute Name](#attribmxmldom-xmlget-first-or-next-node-attribute-name)
  - [\$\$CHILD^MXMLDOM(): XML—Get Parent Node’s First or Next Child](#childmxmldom-xmlget-parent-nodes-first-or-next-child)
  - [\$\$CMNT^MXMLDOM(): XML—Extract Comment Text (True/False)](#cmntmxmldom-xmlextract-comment-text-truefalse)
  - [CMNT^MXMLDOM(): XML—Extract Comment Text (True/False)](#cmntmxmldom-xmlextract-comment-text-truefalse-1)
  - [DELETE^MXMLDOM(): XML—Delete Document Instance](#deletemxmldom-xmldelete-document-instance)
  - [\$\$EN^MXMLDOM(): XML—Initial Processing of XML Document, Build In-memory Image](#enmxmldom-xmlinitial-processing-of-xml-document-build-in-memory-image)
  - [\$\$NAME^MXMLDOM(): XML—Get Element Name](#namemxmldom-xmlget-element-name)
  - [\$\$PARENT^MXMLDOM(): XML—Get Parent Node](#parentmxmldom-xmlget-parent-node)
  - [\$\$SIBLING^MXMLDOM(): XML—Get Sibling Node](#siblingmxmldom-xmlget-sibling-node)
  - [\$\$TEXT^MXMLDOM(): XML—Extract Non-markup Text (True/False)](#textmxmldom-xmlextract-non-markup-text-truefalse)
  - [TEXT^MXMLDOM(): XML—Extract Non-markup Text (True/False)](#textmxmldom-xmlextract-non-markup-text-truefalse-1)
  - [\$\$VALUE^MXMLDOM(): XML—Get Attribute Value](#valuemxmldom-xmlget-attribute-value)
  - [EN^MXMLPRSE(): XML—Event Driven API](#enmxmlprse-xmlevent-driven-api)
    - [Details](#details)
    - [Example](#example)
  - [\$\$SYMENC^MXMLUTL(): XML—Replace XML Symbols with XML Encoding](#symencmxmlutl-xmlreplace-xml-symbols-with-xml-encoding)
    - [Example](#example-1)
  - [\$\$XMLHDR^MXMLUTL: XML—Get XML Message Header](#xmlhdrmxmlutl-xmlget-xml-message-header)
    - [Example](#example-2)
- [Appendix A—Revision History Archive](#appendix-arevision-history-archive)
The *Kernel 8.0 Developer’s Guide: XML Parser (VistA) Developer Tools User Guide* is part of the *Kernel 8.0 and Kernel Toolkit 7.3 Developer’s Guide*.

## Overview

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA Extensible Markup Language (XML) Parser is a full-featured, validating XML parser written in the M programming language and designed to interface with the VistA suite of M-based applications. It is *not* a standalone product. Rather, it acts as a server application that can provide XML parsing capabilities to any client application that subscribes to the application programming interface (API) specification detailed in this document.

The VistA XML Parser employs two very different API implementations:

- <u>Event-Driven Interface</u>
- <u>World Wide Web Consortium Document Object Model Specification</u>

The choice of which API to employ is in part dependent on the needs of the application developer. The event-driven interface requires the client application to process the document in a strictly top-down manner. In contrast, the in-memory model provides the ability to move freely throughout the document and has the added advantage of ensuring that the document is well formed and valid before any information is returned to the client application.

The VistA XML Parser employs an Entity Catalog to allow storage of external entities such as document type definitions. The Entity Catalog is a VA FileMan-compatible database and can be manipulated using the usual VA FileMan tools.

### Event-Driven Interface

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The event-driven interface is modeled after the widely used Simple API for XML (SAX) interface specification. In this implementation, a client application provides a special handler for each parsing event of interest. When the client invokes the parser, it conveys *not* only the document to be parsed, but also the entry points for each of its event handlers. As the parser progresses through the document, it invokes the client’s handlers for each parsing event for which a handler has been registered.

### World Wide Web Consortium Document Object Model Specification

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This API implementation is based on the World Wide Web Consortium (W3Cs) Document Object Model (DOM) specification. This API, which is built on top of the event-driven interface, first constructs an in-memory model of the fully parsed and validated document. It then provides methods to navigate through and extract information from the parsed document.

This API is layered on top of the event-driven API. In other words, it is a client of the event-driven API that in turn acts as a server to another client application.

The document image is represented internally as a tree with each node in the tree representing an element instance. Attributes (names and values), *non*-markup text, and comment text may be associated with any given node. For example, in <u>Figure 1</u> the XML document on the left is represented by the tree structure on the right.

<span id="_Ref453856331" class="anchor"></span>Figure 1: XML Document (left)—Tree Structure Diagram (right)

![](kernel-8-0-developer-s-guide-xml-parser-user-guide/004.png)

### Entity Catalog

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The XML ENTITY CATALOG (#950) file is used to store external entities and their associated public identifiers. When the XML parser encounters an external entity reference with a public identifier, it first looks for that public identifier in the entity catalog. If it finds the entity, it retrieves its value. Otherwise, it attempts to retrieve the entity value using the system identifier. The problem with using system identifiers is that they often identify resources that may have been relocated since the document was authored. (This is analogous to the problem with broken links in HTML documents.) Using public identifiers and an entity catalog allows one to build a collection of commonly used and readily accessible external entities (such as external document type definitions).

The XML ENTITY CATALOG (#950) file is a VA FileMan-compatible file that is very simple in structure as shown in <u>Table 1</u>.

<table>
<caption><p><span id="_Ref453856326" class="anchor"></span>Table 2: XML Parser—Event Types</p></caption>
<colgroup>
<col style="width: 12%" />
<col style="width: 16%" />
<col style="width: 17%" />
<col style="width: 53%" />
</colgroup>
<thead>
<tr class="header">
<th>Field #</th>
<th>Field Name</th>
<th>Datatype</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>.01</strong></td>
<td>ID</td>
<td><strong>FREE TEXT</strong><br />
(1-250)</td>
<td>The public identifier that is associated with this entity.</td>
</tr>
<tr class="even">
<td><strong>1</strong></td>
<td>VALUE</td>
<td><strong>WORD-PROCESSING</strong></td>
<td>The text associated with the entity.</td>
</tr>
</tbody>
</table>

<span id="_Ref453856326" class="anchor"></span>Table 2: XML Parser—Event Types

### Term Definitions and XML Parser Concept

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To understand the terms used in this section and the concept of the operation of an XML Parser, please review the W3C Architecture Domain website, [Extensible Markup Language (XML) page](http://www.w3.org/XML/).

The Toolkit VistA XML Parser Application Programming Interfaces (APIs) have been developed to assist you in creating an XML document.

Integration Control Registration \#3561 defines the various callable entry points in the MXMLDOM routine. These APIs are based on the W3C’s Document Object Model (DOM) specification. It first builds an “in-memory” image of the fully parsed and validated document and then provides a set of methods to permit structured traversal of the document and extraction of its contents. This API is layered on top of the event-driven API. In other words, it is a client of the event-driven API that in turn acts as a server to another client application.

![](kernel-8-0-developer-s-guide-xml-parser-user-guide/005.png) REF: The VistA Extensible Markup Language (XML) Parser technical and user documentation can be found on the [XML Parser (VistA) application on the VDL](http://www.va.gov/vdl/application.asp?appid=137).

### Known Issues

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following are known issues in this version of the XML parser:

- <u>Unsupported Character Encodings</u>
- <u>Retrieval of External Entities Using Non-Standard File Access Protocols</u>
- <u>File Access</u>
- <u>Entity Substitutions Text</u>
- <u>Enforcing Whitespace</u>

Some of these are due to certain limitations of the M programming language.

#### Unsupported Character Encodings

Unlike languages like Java that have multiple character encoding support built-in, M does *not* recognize character encodings that do *not* incorporate the printable ASCII character subset. Thus, 16-bit character encodings (such as Unicode) are *not* supported. Fortunately, many 8-bit character encodings do incorporate the printable ASCII character subset and can be parsed. Because of this limitation, the VistA XML Parser rejects any documents with unsupported character encodings.

#### Retrieval of External Entities Using Non-Standard File Access Protocols

The current version of the VistA XML Parser does *not* support retrieval of external entities using the HTTP or FTP protocols (or for that matter, any protocols other than the standard file access protocols of the underlying operating system). Client applications using the event-driven interface can intercept external entity retrieval by the parser and implement support for these protocols if desired.

#### File Access

The parser uses the Kernel function FTG^%ZISH for file access. This function reads the entire contents of a file into an M global. There are several nuances to this function that manifest themselves in parser operation:

- Files are opened with a time-out parameter. If an attempt is made to access a *non*-existent file, there is a delay of a few seconds before the error is signaled.
- Files are accessed in text mode. The result is that certain imbedded control characters are stripped from the input stream and never detected by the parser. Because these control characters are disallowed by XML, the parser does *not* report such documents as *non*-conforming.
- A line feed/carriage return sequence at the end of a document is stripped and *not* presented to the parser. Only in rare circumstances would this be considered significant data, but in the strictest sense should be preserved.

#### Entity Substitutions Text

The parser allows external entities to contain substitution text that in some cases would violate XML rules that state that a document *must* be conforming in the absence of resolving such references. In other words, XML states that a *non*-validating parser should be able to verify that a document is conforming without processing external entities. This restriction constrains how token streams can be continued across entities. The parser recognizes most, but *not* all, of these restrictions. The effect is that the parser is more lax in allowing certain kinds of entity substitutions.

#### Enforcing Whitespace

Parsers vary in how they enforce whitespace that is designated as required by the XML specification. This parser flags the absence of any required whitespace as a conformance error, even in situations where the absence of such whitespace would *not* introduce syntactic ambiguity. The result is that this parser rejects some documents that may be accepted by other parsers.

# Application Programming Interfaces (APIs)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The Toolkit VistA XML Parser Application Programming Interfaces (APIs) and Extrinsic Functions were developed to assist you in creating an XML document.

Integration Control Registration \#3561 defines the various callable entry points in the MXMLDOM routine. These APIs are based on the W3C’s Document Object Model (DOM) specification. It first builds an “in-memory” image of the fully parsed and validated document and then provides a set of methods to permit structured traversal of the document and extraction of its contents. This API is layered on top of the event-driven API. In other words, it is a client of the event-driven API that in turn acts as a server to another client application.

Several APIs are available for developers to work with the EXtensible Markup Language (XML). These APIs and Extrinsic Functions are described below.

## \$\$ATTRIB^MXMLDOM(): XML—Get First or Next Node Attribute Name

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: XML Parser (VistA)

ICR \#: 3561

Description: The \$\$ATTRIB^MXMLDOM extrinsic function returns the first or next attribute associated with the specified node.

Format: \$\$ATTRIB^MXMLDOM(handle,node\[,attrib\])

Input Parameters: handle: (required) The value (integer) returned by the <u>\$\$EN^MXMLDOM(): XML—Initial Processing of XML Document, Build In-memory Image</u> API, which created the in-memory document image.

node: (required) The node (integer) whose attribute name is being retrieved.

attrib: (optional) The name (string) of the last attribute retrieved by this call. If NULL or missing, the first attribute associated with the specified node is returned. Otherwise, the next attribute in the list is returned.

Output: returns: Returns:

- Name (string) of the first or next attribute associated with the specified node.
- NULL if there are none remaining.

## \$\$CHILD^MXMLDOM(): XML—Get Parent Node’s First or Next Child

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: XML Parser (VistA)

ICR \#: 3561

Description: The \$\$CHILD^MXMLDOM extrinsic function returns the node of the first or next child of a given parent node, or Zero (0) if there are none remaining.

Format: \$\$CHILD^MXMLDOM(handle,parent\[,child\])

Input Parameters: handle: (required) The value (integer) returned by the <u>\$\$EN^MXMLDOM(): XML—Initial Processing of XML Document, Build In-memory Image</u> API, which created the in-memory document image.

parent: (required) The node (integer) whose children are being retrieved.

child: (optional) If specified, this is the last child node (integer) retrieved. The function returns the next child in the list. If the parameter is Zero or missing, the first child is returned.

Output: returns: Returns:

- Child Node—The next child node (integer).
- Zero (0)—If there are none remaining.

## \$\$CMNT^MXMLDOM(): XML—Extract Comment Text (True/False)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: XML Parser (VistA)

ICR \#: 3561

Description: The \$\$CMNT^MXMLDOM extrinsic function extracts comment text associated with the specified node.

Format: \$\$CMNT^MXMLDOM(handle,node,text)

Input Parameters: handle: (required) The value (integer) returned by the <u>\$\$EN^MXMLDOM(): XML—Initial Processing of XML Document, Build In-memory Image</u> API, which created the in-memory document image.

node: (required) The node (integer) in the document tree that is being referenced by this API.

text: (required) This input parameter (string) *must* contain a closed local or global array reference that is to receive the text. The specified array is deleted before being populated.

Output: returns: Returns a Boolean value:

- True (*non*-Zero)—Text was retrieved.
- False (Zero)—Text was *not* retrieved.

## CMNT^MXMLDOM(): XML—Extract Comment Text (True/False)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: XML Parser (VistA)

ICR \#: 3561

Description: The CMNT^MXMLDOM API extracts comment text associated with the specified node.

Format: CMNT^MXMLDOM(handle,node,text)

Input Parameters: handle: (required) The value (integer) returned by the <u>\$\$EN^MXMLDOM(): XML—Initial Processing of XML Document, Build In-memory Image</u> API, which created the in-memory document image.

node: (required) The node (integer) in the document tree that is being referenced by this API.

text: (required) This input parameter (string) *must* contain a closed local or global array reference that is to receive the text. The specified array is deleted before being populated.

Output: returns: Returns a Boolean value:

- True (*non*-Zero)—Text was retrieved.
- False (Zero)—Text was *not* retrieved.

## DELETE^MXMLDOM(): XML—Delete Document Instance

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: XML Parser (VistA)

ICR \#: 3561

Description: The DELETE^MXMLDOM API deletes the specified document instance. A client application should always call this API when finished with a document instance.

Format: DELETE^MXMLDOM(handle)

Input Parameters: handle: (required) The value (integer) returned by the <u>\$\$EN^MXMLDOM(): XML—Initial Processing of XML Document, Build In-memory Image</u> API, which created the in-memory document image.

Output: none.

## \$\$EN^MXMLDOM(): XML—Initial Processing of XML Document, Build In-memory Image

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: XML Parser (VistA)

ICR \#: 3561

Description: The \$\$EN^MXMLDOM extrinsic function performs initial processing of the XML document. The client application *must* first call this entry point to build the in-memory image of the document before the remaining methods can be applied. The return value is a handle to the document instance that was created and is used by the remaining API calls to identify a specific document instance. The parameters for this entry point are listed by type, requirement (yes or no), and description.

Format: \$\$EN^MXMLDOM(doc\[,opt\])

Input Parameters: doc: (required) This string is either of the following:

- Closed reference to a global root containing the document.
- Filename and path reference identifying the document on the host system.

If a global root is passed, the document either:

- *Must* be stored in standard VA FileMan WORD-PROCESSING format.
- May occur in sequentially numbered nodes below the root node.

Thus, if the global reference is ^XYZ, the global *must* be of one of the following formats:

- ^XYZ(1,0) = “LINE 1”  
  >   
  > ^XYZ(2,0) = “LINE 2” ...

Or:

- ^XYZ(1) = “LINE 1”  
  >   
  > ^XYZ(2) = “LINE 2” ...opt: (optional) This string is a list of option flags that control parser behavior. Recognized option flags are:
- W—Do *not* report warnings to the client.
- V—Validate the document. If *not* specified, the parser only checks for conformance.
- 1—Terminate parsing on encountering a validation error. (By default, the parser terminates only when a conformance error is encountered.)
- 0—Terminate parsing on encountering a warning.

Output: returns: Returns:

- Successful—A *non*-Zero handle of the document instance if parsing completed successfully.
- Unsuccessful—Zero handle of document instance.

This handle is passed to all other API methods to indicate which document instance is being referenced. This allows for multiple document instances to be processed concurrently.

## \$\$NAME^MXMLDOM(): XML—Get Element Name

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: XML Parser (VistA)

ICR \#: 3561

Description: The \$\$NAME^MXMLDOM extrinsic function retrieves the name of the element at the specified node within the document parse tree.

Format: \$\$NAME^MXMLDOM(handle,node)

Input Parameters: handle: (required) The value (integer) returned by the <u>\$\$EN^MXMLDOM(): XML—Initial Processing of XML Document, Build In-memory Image</u> API, which created the in-memory document image.

node: (required) The node (integer) for which the associated element name is being retrieved.

Output: returns: Returns the name (string) of the element associated with the specified node.

## \$\$PARENT^MXMLDOM(): XML—Get Parent Node

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: XML Parser (VistA)

ICR \#: 3561

Description: The \$\$PARENT^MXMLDOM extrinsic function returns the parent node of the specified node, or Zero (0) if there is none.

Format: \$\$PARENT^MXMLDOM(handle,node)

Input Parameters: handle: (required) The value (integer) returned by the <u>\$\$EN^MXMLDOM(): XML—Initial Processing of XML Document, Build In-memory Image</u> API, which created the in-memory document image.

node: (required) The node (integer) in the document tree whose parent is being retrieved.

Output: returns: Returns:

- Parent Node—The parent node (string) of the specified node.
- Zero (0)—If there is no parent.

## \$\$SIBLING^MXMLDOM(): XML—Get Sibling Node

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: XML Parser (VistA)

ICR \#: 3561

Description: The \$\$SIBLING^MXMLDOM extrinsic function returns the node of the specified node’s immediate sibling, or Zero (0) if there is none.

Format: \$\$SIBLING^MXMLDOM(handle,node)

Input Parameters: handle: (required) The value (integer) returned by the <u>\$\$EN^MXMLDOM(): XML—Initial Processing of XML Document, Build In-memory Image</u> API, which created the in-memory document image.

node: (required) The node (integer) in the document tree whose sibling is being retrieved.

Output: returns: Returns:

- Node—The node (integer) corresponding to the immediate sibling of the specified node.
- Zero (0)—If there is no node (integer) corresponding to the immediate sibling of the specified node.

## \$\$TEXT^MXMLDOM(): XML—Extract Non-markup Text (True/False)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: XML Parser (VistA)

ICR \#: 3561

Description: The \$\$TEXT^MXMLDOM extrinsic function extracts *non*-markup text associated with the specified node.

Format: \$\$TEXT^MXMLDOM(handle,node,text)

Input Parameters: handle: (required) The value (integer) returned by the <u>\$\$EN^MXMLDOM(): XML—Initial Processing of XML Document, Build In-memory Image</u> API, which created the in-memory document image.

node: (required) The node (integer) in the document tree that is being referenced by this API.

text: (required) This input parameter (string) *must* contain a closed local or global array reference that is to receive the text. The specified array is deleted before being populated.

Output: returns: Returns a Boolean value:

- True (*non*-Zero)—Text was retrieved.
- False (Zero)—Text was *not* retrieved.

## TEXT^MXMLDOM(): XML—Extract Non-markup Text (True/False)

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: XML Parser (VistA)

ICR \#: 3561

Description: The TEXT^MXMLDOM API extracts *non*-markup text associated with the specified node.

Format: TEXT^MXMLDOM(handle,node,text)

Input Parameters: handle: (required) The value (integer) returned by the <u>\$\$EN^MXMLDOM(): XML—Initial Processing of XML Document, Build In-memory Image</u> API, which created the in-memory document image.

node: (required) The node (integer) in the document tree that is being referenced by this API.

text: (required) This input parameter (string) *must* contain a closed local or global array reference that is to receive the text. The specified array is deleted before being populated.

Output: returns: Returns a Boolean value:

- True (*non*-Zero)—Text was retrieved.
- False (Zero)—Text was *not* retrieved.

## \$\$VALUE^MXMLDOM(): XML—Get Attribute Value

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: XML Parser (VistA)

ICR \#: 3561

Description: The \$\$VALUE^MXMLDOM extrinsic function returns the value associated with the named attribute.

Format: \$\$VALUE^MXMLDOM(handle,node\[,attrib\])

Input Parameters: handle: (required) The value (integer) returned by the <u>\$\$EN^MXMLDOM(): XML—Initial Processing of XML Document, Build In-memory Image</u> API, which created the in-memory document image.

node: (required) The node (integer) whose attribute value is being retrieved.

attrib: (optional) The name of the attribute (string) whose value is being retrieved by this API.

Output: returns: Returns the value associated with the specified attribute.

## EN^MXMLPRSE(): XML—Event Driven API

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: XML Parser (VistA)

ICR \#: 4149

Description: The EN^MXMLPRSE API is an event-driven interface that is based on the well-established Simple API for XML (SAX) interface employed by many XML parsers. This API has a single method.  
  
In this implementation, a client application provides a special handler for each parsing event of interest. When the client invokes the parser, it conveys not only the document to be parsed, but also the entry points for each of its event handlers. As the parser progresses through the document, it invokes the client’s handlers for each parsing event for which a handler has been registered.

Format: EN^MXMLPRSE(doc,cbk\[,opt\])

Input Parameters: doc: (required) This string is either a closed reference to a global root containing the document or a filename and path reference identifying the document on the host system. If a global root is passed, the document *must* be stored in standard VA FileMan WORD-PROCESSING format or may occur in sequentially numbered nodes below the root node. Thus, if the global reference is “^XYZ”, the global *must* be of one of the following formats:

- ^XYZ(1,0) = “LINE 1”  
  >   
  > ^XYZ(2,0) = “LINE 2”...

Or:

- ^XYZ(1) = “LINE 1”  
  >   
  > ^XYZ(2) = “LINE 2”...cbk: (required) This is a local array, passed by reference that contains a list of parse events and the entry points for the handlers of those events. The format for each entry is:

> CBK(*\<event type\>*) = *\<entry point\>*

> The entry point *must* reference a valid entry point in an existing M routine and should be of the format tag^routine. The entry should *not* contain any formal parameter references. The application developer is responsible for ensuring that the actual entry point contains the appropriate number of formal parameters for the event type. For example, client application might register its STARTELEMENT event handler as follows:

CBK("STARTELEMENT") = "STELE^CLNT"

> The actual entry point in the CLNT routine *must* include two formal parameters as in the following example:

STELE(ELE,ATR) *\<handler code\>*

![](kernel-8-0-developer-s-guide-xml-parser-user-guide/006.png) REF: For the types of supported events and their required parameters, see the “[Details](#details)” section.

opt: (optional) This is a list of option flags that control parser behavior. Recognized option flags are:

- W—Do *not* report warnings to the client.
- V—Validate the document. If *not* specified, the parser only checks for conformance.
- 1—Terminate parsing on encountering a validation error. (By default, the parser terminates only when a conformance error is encountered.)
- 0—Terminate parsing on encountering a warning.

Output: returns: Returns the XML parsed string.

### Details

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The VistA XML Parser recognizes the event types listed in <u>Table 2</u>:

<table>
<colgroup>
<col style="width: 23%" />
<col style="width: 15%" />
<col style="width: 61%" />
</colgroup>
<thead>
<tr class="header">
<th>Event Type</th>
<th>Parameters</th>
<th>Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td><strong>STARTDOCUMENT</strong></td>
<td>None</td>
<td>Notifies the client that document parsing has commenced.</td>
</tr>
<tr class="even">
<td><strong>ENDDOCUMENT</strong></td>
<td>None</td>
<td>Notifies the client that document parsing has completed.</td>
</tr>
<tr class="odd">
<td><strong>DOCTYPE</strong></td>
<td>ROOT<br />
PUBID<br />
SYSID</td>
<td>Notifies the client that a <strong>DOCTYPE</strong> declaration has been encountered. The name of the document root is given by <strong>ROOT</strong>. The public and system identifiers of the external document type definition are given by <strong>PUBID</strong> and <strong>SYSID</strong>, respectively.</td>
</tr>
<tr class="even">
<td><strong>STARTELEMENT</strong></td>
<td>NAME<br />
ATTRLIST</td>
<td><p>An element (tag) has been encountered. The name of the element is given in <strong>NAME</strong>. The list of attributes and their values is provided in the local array <strong>ATTRLST</strong> in the format:</p>
<p><strong>ATTRLST(<em>&lt;name&gt;</em>) = <em>&lt;value&gt;</em></strong></p></td>
</tr>
<tr class="odd">
<td><strong>ENDELEMENT</strong></td>
<td>NAME</td>
<td>A closing element (tag) has been encountered. The name of the element is given in <strong>NAME</strong>.</td>
</tr>
<tr class="even">
<td><strong>CHARACTERS</strong></td>
<td>TEXT</td>
<td><em>Non</em>-markup content has been encountered. <strong>TEXT</strong> contains the text. Line breaks within the original document are represented as carriage return/line feed character sequences. The parser does <em>not</em> necessarily pass an entire line of the original document to the client with each event of this type.</td>
</tr>
<tr class="odd">
<td><strong>PI</strong></td>
<td>TARGET<br />
TEXT</td>
<td>The parser has encountered a processing instruction. <strong>TARGET</strong> is the target application for the processing instruction. <strong>TEXT</strong> is a local array containing the parameters for the instruction.</td>
</tr>
<tr class="even">
<td><strong>EXTERNAL</strong></td>
<td>SYSID<br />
PUBID<br />
GLOBAL</td>
<td>The parser has encountered an external entity reference whose system and public identifiers are given by <strong>SYSID</strong> and <strong>PUBID</strong>, respectively. If the event handler elects to retrieve the entity rather than allowing the parser to do so, it should pass the global root of the retrieved entity in the <strong>GLOBAL</strong> parameter. If the event handler wishes to suppress retrieval of the entity altogether, it should set both <strong>SYSID</strong> and <strong>PUBID</strong> to <strong>NULL</strong>.</td>
</tr>
<tr class="odd">
<td><strong>NOTATION</strong></td>
<td>NAME<br />
SYSID<br />
PUBIC</td>
<td>The parser has encountered a notation declaration. The notation name is given by <strong>NAME</strong>. The system and public identifiers associated with the notation are given by <strong>SYSID</strong> and <strong>PUBIC</strong>, respectively.</td>
</tr>
<tr class="even">
<td><strong>COMMENT</strong></td>
<td>TEXT</td>
<td>The parser has encountered a comment. <strong>TEXT</strong> is the text of the comment.</td>
</tr>
<tr class="odd">
<td><strong>ERROR</strong></td>
<td>ERR</td>
<td><p>The parser has encountered an error during the processing of a document. <strong>ERR</strong> is a local array containing information about the error. The format is:</p>
<ul>
<li><blockquote>
<p><strong>ERR(“SEV”) —</strong>Severity of the error; Where:</p>
</blockquote></li>
</ul>
<ul>
<li><p><strong>Zero (0) —</strong>Warning.</p></li>
<li><p><strong>1—</strong>Validation error.</p></li>
<li><p><strong>2—</strong>Conformance error.</p></li>
</ul>
<ul>
<li><blockquote>
<p><strong>ERR(“MSG”)—</strong>Brief text description of the error.</p>
</blockquote></li>
<li><blockquote>
<p><strong>ERR(“ARG”)—</strong>Token value the triggered the error (optional).</p>
</blockquote></li>
<li><blockquote>
<p><strong>ERR(“LIN”)—</strong>Number of the line being processed when the error occurred.</p>
</blockquote></li>
<li><blockquote>
<p><strong>ERR(“POS”)—</strong>Character position within the line where the error occurred.</p>
</blockquote></li>
<li><blockquote>
<p><strong>ERR(“XML”)—</strong>Original document text of the line where the error occurred.</p>
</blockquote></li>
</ul></td>
</tr>
</tbody>
</table>

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This is a simple example of how to use the VistA XML Parser with an XML document (file). The XML file contains a parent node named BOOKS. Nested within that parent node are child nodes named TITLE and AUTHOR.

Remember the following:

- The parent node is the node whose child nodes are being retrieved.
- The child node, if specified, is the last child node retrieved. The function returns the next child in the list. If the parameter is Zero or missing, the first child is returned.

A sample client of the event-driven API is provided in the MXMLTEST routine. This routine has an entry point EN(DOC,OPT); where DOC and OPT are the same parameters as described above for the parser entry point. This sample application simply prints a summary of the parsing events as they occur.

1.  Create an XML file:

> <span id="_Toc46896839" class="anchor"></span>Figure 2: VistA XML Parser Use—Example: Create XML File

> ^TMP(\$J,1) = \<?xml version='1.0'?\>

> ^TMP(\$J,2) = \<!DOCTYPE BOOK\>

> ^TMP(\$J,3) = \<BOOK\>

> ^TMP(\$J,4) = \<TITLE\>Design Patterns\</TITLE\>

> ^TMP(\$J,5) = \<AUTHOR\>Author1\</AUTHOR\>

> ^TMP(\$J,6) = \<AUTHOR\>Author2\</AUTHOR\>

> ^TMP(\$J,7) = \<AUTHOR\>Author3\</AUTHOR\>

> ^TMP(\$J,8) = \<AUTHOR\>Author4\</AUTHOR\>

> ^TMP(\$J,9) = \</BOOK\>

2.  Invoke simple API for XML (SAX) interface:

> <span id="_Toc500397798" class="anchor"></span>Figure 3: VistA XML Parser Use Example—Invoke SAX Interface

> D EN^MXMLTEST(\$NA(^TMP(\$J)),"V")

3.  Check Document Object Model (DOM) interface:

> <span id="_Toc500397799" class="anchor"></span>Figure 4: VistA XML Parser Use Example—Check DOM Interface

> \><span class="mark">S HDL=\$\$EN^MXMLDOM(\$NA(^TMP(\$J)))</span>

> \><span class="mark">W \$\$NAME^MXMLDOM(HDL,1)</span>

> BOOK

> \><span class="mark">S CHD=\$\$CHILD^MXMLDOM(HDL,1)</span>

> \><span class="mark">W \$\$NAME^MXMLDOM(HDL,CHD)</span>

> TITLE

> \><span class="mark">W \$\$TEXT^MXMLDOM(HDL,CHD,\$NA(VV))</span>

> 1

> \><span class="mark">ZW VV</span>

> VV(1)=Design Patterns

4.  List all sibling nodes:

<span id="_Toc500397800" class="anchor"></span>Figure 5: VistA XML Parser Use Example—List All Sibling Nodes

> \><span class="mark">S CHD=\$\$CHILD^MXMLDOM(HDL,1)</span>

> \><span class="mark">S SIB=CHD</span>

> \><span class="mark">F S SIB=\$\$SIBLING^MXMLDOM(HDL,SIB) Q:SIB'\>0 W !,SIB,?4,\$\$NAME^MXMLDOM(HDL,SIB)</span>

> 3 AUTHOR

> 4 AUTHOR

> 5 AUTHOR

> 6 AUTHOR

> \>

## \$\$SYMENC^MXMLUTL(): XML—Replace XML Symbols with XML Encoding

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: XML Parser (VistA)

ICR \#: 4153

Description: The \$\$SYMENC^MXMLUTL extrinsic function replaces reserved Extensible Markup Language (XML) symbols in a string with their XML encoding for strings used in an XML message.

Format: \$\$SYMENC^MXMLUTL(str)

Input Parameters: str: (required) String to be encoded in an XML message.

Output: returns: Returns the input string with XML encoding replacing reserved XML symbols.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc199951029" class="anchor"></span>Figure 6: \$\$SYMENC^MXMLUTL API—Example

\><span class="mark">S X=\$\$SYMENC^MXMLUTL("This line isn't &""\<XML\>"" safe as is.")</span>

\><span class="mark">W X</span>

This line isn&os;t &amp;&quot;&lt;XML&gt;&quot; safe as is.

## \$\$XMLHDR^MXMLUTL: XML—Get XML Message Header

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Reference Type: Supported

Category: XML Parser (VistA)

ICR \#: 4153

Description: The \$\$XMLHDR^MXMLUTL extrinsic function returns a standard Extensible Markup Language (XML) header for encoding XML messages.

Format: \$\$XMLHDR^MXMLUTL

Input Parameters: none.Output: returns: Returns a standard XML header.

### Example

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<span id="_Toc199951030" class="anchor"></span>Figure 7: \$\$XMLHDR^MXMLUTL API—Example

\><span class="mark">S X=\$\$XMLHDR^MXMLUTL</span>

\><span class="mark">W X</span>

\<?xml version="1.0" encoding="utf-8" ?\>

# Appendix A—Revision History Archive

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This section should be used to show all document revision history prior to the current year.

![](kernel-8-0-developer-s-guide-xml-parser-user-guide/007.png) REF: For the most recent, current year document revision history, see the “[Revision History](#_Toc234301875)” section.

| Date | Revision | Description | Author |
|------|----------|-------------|--------|
| TBD  | TBD      | TBD         | TBD    |

<span id="Glossary" class="anchor"></span>Glossary

![](kernel-8-0-developer-s-guide-xml-parser-user-guide/008.png) REF: For a glossary of terms specific to Kernel, see the “Glossary” section in the [*Kernel 8.0 Developer's Guide: Main Directory User Guide*](https://www.va.gov/vdl/documents/Infrastructure/Kernel/krn_8_0_sm.pdf#Main_Glossary).

![](kernel-8-0-developer-s-guide-xml-parser-user-guide/009.png) REF: For a list of commonly used terms and acronyms, see the VA Glossary Power App.