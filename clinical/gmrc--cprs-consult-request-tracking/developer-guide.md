---
title: Standardized Episodes of Care (SEOC) API Manual
doc_type: API
doc_label: API Manual
doc_layer: plain
doc_subject: Standardized Episodes of Care (SEOC)
app_code: GMRC
app_name: "CPRS: Consult/Request Tracking"
section: CLI
app_status: active
pkg_ns: 
patch_ver: 
patch_id: 
group_key: 
file_numbers: []
security_keys: []
menu_options: 1
description: 
audience: <!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)
keywords: 
  - hptc
  - care
  - false
  - acupuncture
  - billingcode
  - precertrequired
  - codetype
  - description
  - null
  - other
page_count: 0
word_count: 11188
section_count: 12
table_count: 2
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: June 2020
revision_count: 0
revision_newest: 
revision_oldest: 
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Consult_Request_Tracking/seoc_api.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Consult_Request_Tracking/seoc_api.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=62"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>Care Coordination (CC) Standard Episodes of Care (SEOC)

  API Manual
---

![](standardized-episodes-of-care-seoc-api-manual/001.png)

June 2020

Office of Information and Technology (OIT)

Revision History

> **NOTE:** The revision history cycle begins once changes or enhancements are requested after the document has been baselined.

<table>
<caption><p>Table 1: Environments</p></caption>
<colgroup>
<col style="width: 17%" />
<col style="width: 12%" />
<col style="width: 45%" />
<col style="width: 24%" />
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
<td>June 2020</td>
<td>0.8</td>
<td>Initial Draft – v1.10 and above</td>
<td>AbleVets</td>
</tr>
<tr class="even">
<td>August 2019</td>
<td>0.7</td>
<td>Initial Draft – GMRC*3.0*143<br />
v1.9</td>
<td>AbleVets</td>
</tr>
<tr class="odd">
<td>May 2019</td>
<td>0.6</td>
<td>Initial Draft – GMRC*3.0*126<br />
v1.8</td>
<td>AbleVets</td>
</tr>
<tr class="even">
<td>March 2019</td>
<td>0.5</td>
<td>Initial Draft – GMRC*3.0*120<br />
v1.7</td>
<td>AbleVets</td>
</tr>
<tr class="odd">
<td>January 2019</td>
<td>0.4</td>
<td>Initial Draft – GMRC*3.0*117<br />
v1.6</td>
<td>AbleVets</td>
</tr>
<tr class="even">
<td>October 2018</td>
<td>0.3</td>
<td>Initial Draft – GMRC*3.0*116<br />
v1.5</td>
<td>AbleVets</td>
</tr>
<tr class="odd">
<td>August 2018</td>
<td>0.2</td>
<td>Initial Draft – GMRC*3.0*108<br />
v1.0.04.1</td>
<td>AbleVets</td>
</tr>
<tr class="even">
<td>July 2018</td>
<td>0.1</td>
<td>Initial Draft – GMRC*3.0*103<br />
v1.0.03</td>
<td>AbleVets</td>
</tr>
</tbody>
</table>

Table 1: Environments

Table of Contents

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [Purpose](#purpose)
  - [Audience](#audience)
  - [Overview of SEOC](#overview-of-seoc)
- [Package Orientation](#package-orientation)
- [API Description](#api-description)
- [SEOC JSON Schema](#seoc-json-schema)
  - [Get Active, Discontinued, and Date Hold SEOCs v1: /v1/seoc](#get-active-discontinued-and-date-hold-seocs-v1-v1seoc)
  - [Get Active, Discontinued, and Date Hold SEOCs v2: /v2/seoc](#get-active-discontinued-and-date-hold-seocs-v2-v2seoc)
  - [Get Active SEOCs v1: /v1/seoc/active](#get-active-seocs-v1-v1seocactive)
  - [Get Active SEOCs v2: /v2/seoc/active](#get-active-seocs-v2-v2seocactive)
- [JSON Response by Endpoint](#json-response-by-endpoint)
  - [Get Active, Discontinued, and Date Hold SEOCs v1: /v1/seoc \[abbreviated\]](#get-active-discontinued-and-date-hold-seocs-v1-v1seoc-abbreviated)
  - [Get Active, Discontinued, and Date Hold SEOCs v2: /v2/seoc \[abbreviated\]](#get-active-discontinued-and-date-hold-seocs-v2-v2seoc-abbreviated)
  - [Get Active SEOCs v1: /v1/seoc/active \[abbreviated\]](#get-active-seocs-v1-v1seocactive-abbreviated)
  - [Get Active SEOCs v2: /v2/seoc/active \[abbreviated\]](#get-active-seocs-v2-v2seocactive-abbreviated)
The Care Coordination (CC) Standardized Episodes of Care (SEOC) is a reference database for managing care bundles for use by Veterans Information Systems and Technology Architecture (VistA) and other Department of Veterans Affairs (VA) systems. Services are grouped together within the SEOC system into bundles so that clinicians can add these bundles to patients consult records in a standardized fashion, reducing the amount of time spent manually entering consult instructions, and providing uniformity among the patient records and across facilities for how patient care is prescribed for similar complaints.
These bundles group together one or more services that are preselected for different specialties to be added to the consult records. In addition, the clinician is provided with information regarding prescribing rules and preauthorization requirements, so they can make the most informed decisions regarding patient care.
Additionally, SEOC data will be accessible outside of the VistA/Computerized Patient Record System (CPRS) system so that users of downstream applications will be accessing the centralized data, and SEOC descriptions, reducing the chances of disconnects.

## Purpose

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual provides technical descriptions for accessing the endpoints of the SEOC Representational State Transfer (REST) Application Programming Interface (API) which have been made available to partner systems running within the internal VA network boundary.

From time to time improvements are made to the SEOC System. The latest information about SEOC, as well as the latest version of this manual, is posted on the VA Software Document Library on the [CPRS: Consult/Request Tracking](https://www.va.gov/vdl/application.asp?appid=62) page.

## Audience

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Information in this manual is technical in nature and is intended to be used by Veterans Affairs Medical Center (VAMC) Information Resource Management Service (IRMS) staff members and Clinical Application Coordinators (CACs).

## Overview of SEOC

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The SEOC System provides an interface for downstream systems to access SEOCs from the SEOC database via a REST API. The SEOC record(s) will be returned to the calling application (such as the Consult Toolbox) in JavaScript Object Notation (JSON) format.

# Package Orientation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

This manual provides technical descriptions of REST API calls available and a sample JSON message.

This manual should assist you in:

- Calling the SEOC API endpoints that are available for general use on the internal VA network.
- Developing parsing routines necessary to consume the JSON data returned by the API calls.

# API Description

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

Method: GET --header 'Accept: application/json'

| Environment \<env\> | Description        | Data Source |
|---------------------|--------------------|-------------|
| dev.                | Development server | Test data   |
| sqa.                | SQA server         | Test data   |
| uat.                | UAT server         | Prod data   |
|                     | Production server  | Prod data   |

Table 2: Response Messages (Errors)

Request URLs:Base URL: [Error! Hyperlink reference not valid.]()API Version: /v1 or /v2

Endpoints/Paths:

- Get Active, Discontinued and Date Hold SEOCs: /seoc
- Get active SEOCs: /seoc/active

Example Fully Formed URLs:

> In Development, retrieve the V2 SEOCs in Active, Discontinued and Date Hold States:

> <https://dev.seocapi.va.gov/v2/seoc>

In Production, retrieve the V1 Active SEOCs:

> <https://seocapi.va.gov/v1/seoc/active>

Request Headers:

{  
"Accept": "\*/\*"  
}

| HTTP Status Code | Reason           | Response Model | Headers |
|------------------|------------------|----------------|---------|
| 200              | OK               | string         |         |
| 400              | Bad request      |                |         |
| 401              | Unauthorized     |                |         |
| 404              | Not Found        |                |         |
| 500              | Unexpected error |                |         |

Response Message (Success): 200 OK

Response Headers:

{  
"content-type": "application/json;charset=UTF-8",  
"content-length": "\<*length*\>",  
"date": "Tue, 10 Apr 2018 20:17:03 GMT",  
"": ""  
}

# SEOC JSON Schema

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Get Active, Discontinued, and Date Hold SEOCs v1: /v1/seoc

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>{</p>
<p>"$schema": "http://json-schema.org/draft-04/schema#",</p>
<p>"title": "The Root Schema",</p>
<p>"type": "object",</p>
<p>"additionalProperties": false,</p>
<p>"required": [</p>
<p>"Seocs"</p>
<p>],</p>
<p>"properties": {</p>
<p>"Seocs": {</p>
<p>"title": "The Seocs Schema",</p>
<p>"type": "array",</p>
<p>"items": {</p>
<p>"title": "The Items Schema",</p>
<p>"type": "object",</p>
<p>"additionalProperties": false,</p>
<p>"required": [</p>
<p>"Seoc"</p>
<p>],</p>
<p>"properties": {</p>
<p>"Seoc": {</p>
<p>"title": "Seoc",</p>
<p>"type": "object",</p>
<p>"additionalProperties": false,</p>
<p>"properties": {</p>
<p>"id": {</p>
<p>"type": "integer"</p>
<p>},</p>
<p>"seocKey": {</p>
<p>"type": "integer"</p>
<p>},</p>
<p>"name": {</p>
<p>"type": "string",</p>
<p>"maxLength": 150</p>
<p>},</p>
<p>"seocId": {</p>
<p>"type": "string"</p>
<p>},</p>
<p>"versionNumber": {</p>
<p>"type": "string",</p>
<p>"maxLength": 25</p>
<p>},</p>
<p>"description": {</p>
<p>"type": "string",</p>
<p>"maxLength": 2000</p>
<p>},</p>
<p>"effectiveDate": {</p>
<p>"type": "string",</p>
<p>"format": "date"</p>
<p>},</p>
<p>"endDate": {</p>
<p>"type": ["string", "null"],</p>
<p>"format": "date"</p>
<p>},</p>
<p>"duration": {</p>
<p>"type": "integer"</p>
<p>},</p>
<p>"REV": {</p>
<p>"type": "boolean"</p>
<p>},</p>
<p>"proceduralOverview": {</p>
<p>"type": "string",</p>
<p>"maxLength": 5000</p>
<p>},</p>
<p>"maxAllowableVisits": {</p>
<p>"type": ["integer", "null"]</p>
<p>},</p>
<p>"disclaimer": {</p>
<p>"type": "string",</p>
<p>"maxLength": 2000</p>
<p>},</p>
<p>"activatedTimestamp": {</p>
<p>"type": "string",</p>
<p>"format": "date"</p>
<p>},</p>
<p>"activatedBy": {</p>
<p>"type": "string",</p>
<p>"maxLength": 80</p>
<p>},</p>
<p>"discontinuedTimestamp": {</p>
<p>"type": ["string", "null"],</p>
<p>"format": "date"</p>
<p>},</p>
<p>"discontinuedBy": {</p>
<p>"type": ["string", "null"],</p>
<p>"maxLength": 80</p>
<p>},</p>
<p>"status": {</p>
<p>"type": "string"</p>
<p>},</p>
<p>"QASP": {</p>
<p>"type": "string"</p>
<p>},</p>
<p>"categoryOfCare": {</p>
<p>"type": "string"</p>
<p>},</p>
<p>"serviceLine": {</p>
<p>"type": "string"</p>
<p>},</p>
<p>"services": {</p>
<p>"type": "array",</p>
<p>"items": {</p>
<p>"$ref": "#/properties/Seocs/items/properties/Seoc/definitions/PayableService"</p>
<p>}</p>
<p>},</p>
<p>"hptcs": {</p>
<p>"type": "array",</p>
<p>"items": {</p>
<p>"$ref": "#/properties/Seocs/items/properties/Seoc/definitions/Hptc"</p>
<p>}</p>
<p>}</p>
<p>},</p>
<p>"required": ["id", "seocKey", "name", "seocId", "versionNumber", "description", "effectiveDate", "duration", "REV", "proceduralOverview", "disclaimer", "activatedTimestamp", "activatedBy", "status", "QASP", "categoryOfCare", "serviceLine", "services", "hptcs"],</p>
<p>"definitions": {</p>
<p>"PayableService": {</p>
<p>"type": "object",</p>
<p>"additionalProperties": false,</p>
<p>"properties": {</p>
<p>"id": {</p>
<p>"type": "integer"</p>
<p>},</p>
<p>"description": {</p>
<p>"type": "string",</p>
<p>"maxLength": 2000</p>
<p>},</p>
<p>"frequency": {</p>
<p>"type": ["integer", "null"]</p>
<p>},</p>
<p>"frequencytype": {</p>
<p>"type": ["string", "null"]</p>
<p>},</p>
<p>"visits": {</p>
<p>"type": ["integer", "null"]</p>
<p>},</p>
<p>"codedBy": {</p>
<p>"type": ["string", "null"]</p>
<p>},</p>
<p>"codedtimestamp": {</p>
<p>"type": ["string", "null"],</p>
<p>"format": "date"</p>
<p>},</p>
<p>"coderequired": {</p>
<p>"type": "string"</p>
<p>},</p>
<p>"clinicalService": {</p>
<p>"type": "string"</p>
<p>},</p>
<p>"billingCodes": {</p>
<p>"type": "array",</p>
<p>"items": {</p>
<p>"$ref": "#/properties/Seocs/items/properties/Seoc/definitions/BillingCode"</p>
<p>}</p>
<p>},</p>
<p>"serviceHptcs": {</p>
<p>"type": "array",</p>
<p>"items": {</p>
<p>"$ref": "#/properties/Seocs/items/properties/Seoc/definitions/ServiceHptc"</p>
<p>}</p>
<p>}</p>
<p>},</p>
<p>"required": ["id", "description", "clinicalService"]</p>
<p>},</p>
<p>"BillingCode": {</p>
<p>"type": "object",</p>
<p>"additionalProperties": false,</p>
<p>"properties": {</p>
<p>"id": {</p>
<p>"type": "integer"</p>
<p>},</p>
<p>"description": {</p>
<p>"type": "string",</p>
<p>"maxLength": 2000</p>
<p>},</p>
<p>"precertRequired": {</p>
<p>"type": "boolean"</p>
<p>},</p>
<p>"billingCode": {</p>
<p>"type": "string",</p>
<p>"maxLength": 25</p>
<p>},</p>
<p>"codeType": {</p>
<p>"type": "string",</p>
<p>"maxLength": 25</p>
<p>},</p>
<p>"deactivated": {</p>
<p>"type": ["boolean", "null"]</p>
<p>}</p>
<p>},</p>
<p>"required": ["id", "description", "precertRequired", "billingCode", "codeType"]</p>
<p>},</p>
<p>"Hptc": {</p>
<p>"type": "object",</p>
<p>"additionalProperties": false,</p>
<p>"properties": {</p>
<p>"hptc": {</p>
<p>"type": "string",</p>
<p>"maxLength": 10</p>
<p>},</p>
<p>"classification": {</p>
<p>"type": "string",</p>
<p>"maxLength": 100</p>
<p>},</p>
<p>"specialization": {</p>
<p>"type": ["string", "null"],</p>
<p>"maxLength": 100</p>
<p>},</p>
<p>"grouping": {</p>
<p>"type": "string",</p>
<p>"maxLength": 100</p>
<p>}</p>
<p>},</p>
<p>"required": ["hptc"]</p>
<p>},</p>
<p>"ServiceHptc": {</p>
<p>"type": "object",</p>
<p>"additionalProperties": false,</p>
<p>"properties": {</p>
<p>"HPTC": {</p>
<p>"type": "string",</p>
<p>"maxLength": 10</p>
<p>}</p>
<p>},</p>
<p>"required": ["HPTC"]</p>
<p>}</p>
<p>}</p>
<p>}</p>
<p>}</p>
<p>}</p>
<p>}</p>
<p>}</p>
<p>}</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Get Active, Discontinued, and Date Hold SEOCs v2: /v2/seoc

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>{</p>
<p>"$schema": "http://json-schema.org/draft-04/schema#",</p>
<p>"title": "The Root Schema",</p>
<p>"type": "object",</p>
<p>"additionalProperties": false,</p>
<p>"required": [</p>
<p>"Seocs"</p>
<p>],</p>
<p>"properties": {</p>
<p>"Seocs": {</p>
<p>"title": "The Seocs Schema",</p>
<p>"type": "array",</p>
<p>"items": {</p>
<p>"title": "The Items Schema",</p>
<p>"type": "object",</p>
<p>"additionalProperties": false,</p>
<p>"required": [</p>
<p>"Seoc"</p>
<p>],</p>
<p>"properties": {</p>
<p>"Seoc": {</p>
<p>"title": "Seoc",</p>
<p>"type": "object",</p>
<p>"additionalProperties": false,</p>
<p>"properties": {</p>
<p>"id": {</p>
<p>"type": "integer"</p>
<p>},</p>
<p>"seocKey": {</p>
<p>"type": "integer"</p>
<p>},</p>
<p>"name": {</p>
<p>"type": "string",</p>
<p>"maxLength": 150</p>
<p>},</p>
<p>"seocId": {</p>
<p>"type": "string"</p>
<p>},</p>
<p>"versionNumber": {</p>
<p>"type": "string",</p>
<p>"maxLength": 25</p>
<p>},</p>
<p>"description": {</p>
<p>"type": "string",</p>
<p>"maxLength": 2000</p>
<p>},</p>
<p>"effectiveDate": {</p>
<p>"type": "string",</p>
<p>"format": "date"</p>
<p>},</p>
<p>"endDate": {</p>
<p>"type": ["string", "null"],</p>
<p>"format": "date"</p>
<p>},</p>
<p>"duration": {</p>
<p>"type": "integer"</p>
<p>},</p>
<p>"REV": {</p>
<p>"type": "boolean"</p>
<p>},</p>
<p>"PRCT": {</p>
<p>"type": "boolean"</p>
<p>},</p>
<p>"proceduralOverview": {</p>
<p>"type": "string",</p>
<p>"maxLength": 5000</p>
<p>},</p>
<p>"maxAllowableVisits": {</p>
<p>"type": ["integer", "null"]</p>
<p>},</p>
<p>"disclaimer": {</p>
<p>"type": "string",</p>
<p>"maxLength": 2000</p>
<p>},</p>
<p>"QASP": {</p>
<p>"type": "string"</p>
<p>},</p>
<p>"categoryOfCare": {</p>
<p>"type": "string"</p>
<p>},</p>
<p>"serviceLine": {</p>
<p>"type": "string"</p>
<p>},</p>
<p>"services": {</p>
<p>"type": "array",</p>
<p>"items": {</p>
<p>"$ref": "#/properties/Seocs/items/properties/Seoc/definitions/PayableService"</p>
<p>}</p>
<p>},</p>
<p>"hptcs": {</p>
<p>"type": "array",</p>
<p>"items": {</p>
<p>"$ref": "#/properties/Seocs/items/properties/Seoc/definitions/Hptc"</p>
<p>}</p>
<p>}</p>
<p>},</p>
<p>"required": ["id", "seocKey", "name", "seocId", "versionNumber", "description", "effectiveDate", "duration", "REV", "PRCT", "proceduralOverview", "disclaimer", "QASP", "categoryOfCare", "serviceLine", "services", "hptcs"],</p>
<p>"definitions": {</p>
<p>"PayableService": {</p>
<p>"type": "object",</p>
<p>"additionalProperties": false,</p>
<p>"properties": {</p>
<p>"id": {</p>
<p>"type": "integer"</p>
<p>},</p>
<p>"description": {</p>
<p>"type": "string",</p>
<p>"maxLength": 2000</p>
<p>},</p>
<p>"frequency": {</p>
<p>"type": ["integer", "null"]</p>
<p>},</p>
<p>"frequencyType": {</p>
<p>"type": "string"</p>
<p>},</p>
<p>"visits": {</p>
<p>"type": ["integer", "null"]</p>
<p>},</p>
<p>"codeRequired": {</p>
<p>"type": "string"</p>
<p>},</p>
<p>"clinicalServices": {</p>
<p>"type": "array",</p>
<p>"items": {</p>
<p>"$ref": "#/properties/Seocs/items/properties/Seoc/definitions/ClinicalService"</p>
<p>}</p>
<p>},</p>
<p>"billingCodes": {</p>
<p>"type": "array",</p>
<p>"items": {</p>
<p>"$ref": "#/properties/Seocs/items/properties/Seoc/definitions/BillingCode"</p>
<p>}</p>
<p>},</p>
<p>"serviceHptcs": {</p>
<p>"type": "array",</p>
<p>"items": {</p>
<p>"$ref": "#/properties/Seocs/items/properties/Seoc/definitions/ServiceHptc"</p>
<p>}</p>
<p>}</p>
<p>},</p>
<p>"required": ["id", "description", "clinicalServices"]</p>
<p>},</p>
<p>"ClinicalService": {</p>
<p>"type": "object",</p>
<p>"additionalProperties": false,</p>
<p>"properties": {</p>
<p>"clinicalService": {</p>
<p>"type": "string"</p>
<p>}</p>
<p>},</p>
<p>"required": ["clinicalService"]</p>
<p>},</p>
<p>"BillingCode": {</p>
<p>"type": "object",</p>
<p>"additionalProperties": false,</p>
<p>"properties": {</p>
<p>"id": {</p>
<p>"type": "integer"</p>
<p>},</p>
<p>"precertRequired": {</p>
<p>"type": "boolean"</p>
<p>},</p>
<p>"billingCode": {</p>
<p>"type": "string",</p>
<p>"maxLength": 25</p>
<p>},</p>
<p>"codeType": {</p>
<p>"type": "string",</p>
<p>"maxLength": 25</p>
<p>}</p>
<p>},</p>
<p>"required": ["id", "precertRequired", "billingCode", "codeType"]</p>
<p>},</p>
<p>"Hptc": {</p>
<p>"type": "object",</p>
<p>"additionalProperties": false,</p>
<p>"properties": {</p>
<p>"hptc": {</p>
<p>"type": "string",</p>
<p>"maxLength": 10</p>
<p>}</p>
<p>},</p>
<p>"required": ["hptc"]</p>
<p>},</p>
<p>"ServiceHptc": {</p>
<p>"type": "object",</p>
<p>"additionalProperties": false,</p>
<p>"properties": {</p>
<p>"HPTC": {</p>
<p>"type": "string",</p>
<p>"maxLength": 10</p>
<p>}</p>
<p>},</p>
<p>"required": ["HPTC"]</p>
<p>}</p>
<p>}</p>
<p>}</p>
<p>}</p>
<p>}</p>
<p>}</p>
<p>}</p>
<p>}</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Get Active SEOCs v1: /v1/seoc/active

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>{</p>
<p>"$schema": "http://json-schema.org/draft-04/schema#",</p>
<p>"title": "The Root Schema",</p>
<p>"type": "object",</p>
<p>"additionalProperties": false,</p>
<p>"required": [</p>
<p>"Seocs"</p>
<p>],</p>
<p>"properties": {</p>
<p>"Seocs": {</p>
<p>"title": "The Seocs Schema",</p>
<p>"type": "array",</p>
<p>"items": {</p>
<p>"title": "The Items Schema",</p>
<p>"type": "object",</p>
<p>"additionalProperties": false,</p>
<p>"required": [</p>
<p>"Seoc"</p>
<p>],</p>
<p>"properties": {</p>
<p>"Seoc": {</p>
<p>"title": "Seoc",</p>
<p>"type": "object",</p>
<p>"additionalProperties": false,</p>
<p>"properties": {</p>
<p>"name": {</p>
<p>"type": "string",</p>
<p>"maxLength": 150</p>
<p>},</p>
<p>"seocId": {</p>
<p>"type": "string"</p>
<p>},</p>
<p>"description": {</p>
<p>"type": "string",</p>
<p>"maxLength": 2000</p>
<p>},</p>
<p>"duration": {</p>
<p>"type": "integer"</p>
<p>},</p>
<p>"proceduralOverview": {</p>
<p>"type": "string",</p>
<p>"maxLength": 5000</p>
<p>},</p>
<p>"maxAllowableVisits": {</p>
<p>"type": ["integer", "null"]</p>
<p>},</p>
<p>"disclaimer": {</p>
<p>"type": "string",</p>
<p>"maxLength": 2000</p>
<p>},</p>
<p>"categoryOfCare": {</p>
<p>"type": "string"</p>
<p>},</p>
<p>"serviceLine": {</p>
<p>"type": "string"</p>
<p>}</p>
<p>},</p>
<p>"required": ["name", "seocId", "description", "duration", "proceduralOverview", "disclaimer", "categoryOfCare", "serviceLine"]</p>
<p>}</p>
<p>}</p>
<p>}</p>
<p>}</p>
<p>}</p>
<p>}</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

## Get Active SEOCs v2: /v2/seoc/active

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>{</p>
<p>"$schema": "http://json-schema.org/draft-04/schema#",</p>
<p>"title": "The Root Schema",</p>
<p>"type": "object",</p>
<p>"additionalProperties": false,</p>
<p>"required": [</p>
<p>"Seocs"</p>
<p>],</p>
<p>"properties": {</p>
<p>"Seocs": {</p>
<p>"title": "The Seocs Schema",</p>
<p>"type": "array",</p>
<p>"items": {</p>
<p>"title": "The Items Schema",</p>
<p>"type": "object",</p>
<p>"additionalProperties": false,</p>
<p>"required": [</p>
<p>"Seoc"</p>
<p>],</p>
<p>"properties": {</p>
<p>"Seoc": {</p>
<p>"title": "Seoc",</p>
<p>"type": "object",</p>
<p>"additionalProperties": false,</p>
<p>"properties": {</p>
<p>"name": {</p>
<p>"type": "string",</p>
<p>"maxLength": 150</p>
<p>},</p>
<p>"seocId": {</p>
<p>"type": "string"</p>
<p>},</p>
<p>"description": {</p>
<p>"type": "string",</p>
<p>"maxLength": 2000</p>
<p>},</p>
<p>"duration": {</p>
<p>"type": "integer"</p>
<p>},</p>
<p>"proceduralOverview": {</p>
<p>"type": "string",</p>
<p>"maxLength": 5000</p>
<p>},</p>
<p>"disclaimer": {</p>
<p>"type": "string",</p>
<p>"maxLength": 2000</p>
<p>},</p>
<p>"categoryOfCare": {</p>
<p>"type": "string"</p>
<p>},</p>
<p>"serviceLine": {</p>
<p>"type": "string"</p>
<p>},</p>
<p>"previewText": {</p>
<p>"type": "string"</p>
<p>}</p>
<p>},</p>
<p>"required": ["name", "seocId", "description", "duration", "proceduralOverview", "disclaimer", "categoryOfCare", "serviceLine", "previewText"]</p>
<p>}</p>
<p>}</p>
<p>}</p>
<p>}</p>
<p>}</p>
<p>}</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>

# JSON Response by Endpoint

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The following sections include sample response messages for each endpoint.

## Get Active, Discontinued, and Date Hold SEOCs v1: /v1/seoc \[abbreviated\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

{

"Seocs": \[{

"Seoc": {

"id": 181,

"seocKey": 1,

"name": "Acupuncture Initial",

"seocId": "PMR_ACUPUNCTURE INITIAL_1.0.4",

"versionNumber": "1.0.4",

"description": "This authorization covers services associated with all medical care listed below for the referred condition on the consult.",

"effectiveDate": "01-03-2019",

"endDate": null,

"duration": 90,

"REV": false,

"proceduralOverview": "1. Initial outpatient evaluation for this episode of care\r\n2. A maximum of twelve (12) acupuncture visits is approved for this episode of care. Approved services include acupuncture with or without electrostimulation. A maximum of one additional unit of acupuncture (with or without electrostimulation) is allowed when the re-insertion of needles is supported in medical documentation\r\n3. If indicated, approved modalities that can be utilized during the approved acupuncture visits noted in &#x23;2 above can include: manual therapy and therapeutic exercise procedures including but not limited to: cupping, myofascial release, and therapeutic exercises\r\n4. Outpatient re-evaluation during this episode of care as clinically indicated.",

"maxAllowableVisits": null,

"disclaimer": "\*Additional acupuncture care beyond this trial must provide documentation of: Objective measures demonstrating the extent of meaningful clinical improvement to date; and rationale for the additional treatment requested (e.g. to reach further durable improvement, or for ongoing pain management); and any further information supporting the need for additional care \*Additional consultations needed relevant to the patient complaint/condition require VA review and approval.",

"activatedTimestamp": "01-03-2019",

"activatedBy": "VHAISDDavisR",

"discontinuedTimestamp": null,

"discontinuedBy": "SystemUser",

"status": "Active",

"QASP": "Complementary & Integrative HC Services",

"categoryOfCare": "ACUPUNCTURE",

"serviceLine": "Physical Medicine and Rehabilitation",

"services": \[{

"id": 675,

"description": "Initial outpatient evaluation for this episode of care",

"frequency": null,

"frequencytype": "",

"visits": 999,

"coderequired": "YES",

"codedBy": null,

"codedtimestamp": "01-03-2019",

"clinicalService": "35-Chiropractic",

"billingCodes": \[{

"id": 7345,

"description": "Office or other outpatient visit for the evaluation and management of a new patient, which requires these 3 key components: A problem focused history; A problem focused examination; Straightforward medical decision making. Counseling and/or coordination of care with other physicians, other qualified health care professionals, or agencies are provided consistent with the nature of the problem(s) and the patient's and/or family's needs. Usually, the presenting problem(s) are self limited or minor.",

"precertRequired": false,

"billingCode": "99201",

"codeType": "CPT",

"deactivated": null

}, {

"id": 7346,

"description": "Office or other outpatient visit for the evaluation and management of a new patient, which requires these 3 key components: An expanded problem focused history; An expanded problem focused examination; Straightforward medical decision making. Counseling and/or coordination of care with other physicians, other qualified health care professionals, or agencies are provided consistent with the nature of the problem(s) and the patient's and/or family's needs. Usually, the presenting problem(s) are of",

"precertRequired": false,

"billingCode": "99202",

"codeType": "CPT",

"deactivated": null

}, {

"id": 7347,

"description": "Office or other outpatient visit for the evaluation and management of a new patient, which requires these 3 key components: A detailed history; A detailed examination; Medical decision making of low complexity. Counseling and/or coordination of care with other physicians, other qualified health care professionals, or agencies are provided consistent with the nature of the problem(s) and the patient's and/or family's needs. Usually, the presenting problem(s) are of moderate severity. Typically, 3",

"precertRequired": false,

"billingCode": "99203",

"codeType": "CPT",

"deactivated": null

}, {

"id": 7348,

"description": "Office or other outpatient visit for the evaluation and management of a new patient, which requires these 3 key components: A comprehensive history; A comprehensive examination; Medical decision making of moderate complexity. Counseling and/or coordination of care with other physicians, other qualified health care professionals, or agencies are provided consistent with the nature of the problem(s) and the patient's and/or family's needs. Usually, the presenting problem(s) are of moderate to high",

"precertRequired": false,

"billingCode": "99204",

"codeType": "CPT",

"deactivated": null

}, {

"id": 7349,

"description": "Office or other outpatient visit for the evaluation and management of a new patient, which requires these 3 key components: A comprehensive history; A comprehensive examination; Medical decision making of high complexity. Counseling and/or coordination of care with other physicians, other qualified health care professionals, or agencies are provided consistent with the nature of the problem(s) and the patient's and/or family's needs. Usually, the presenting problem(s) are of moderate to high sev",

"precertRequired": false,

"billingCode": "99205",

"codeType": "CPT",

"deactivated": null

}, {

"id": 7350,

"description": "Office or other outpatient visit for the evaluation and management of an established patient, that may not require the presence of a physician or other qualified health care professional. Usually, the presenting problem(s) are minimal. Typically, 5 minutes are spent performing or supervising these services. ",

"precertRequired": false,

"billingCode": "99211",

"codeType": "CPT",

"deactivated": null

}, {

"id": 7351,

"description": "Office or other outpatient visit for the evaluation and management of an established patient, which requires at least 2 of these 3 key components: A problem focused history; A problem focused examination; Straightforward medical decision making. Counseling and/or coordination of care with other physicians, other qualified health care professionals, or agencies are provided consistent with the nature of the problem(s) and the patient's and/or family's needs. Usually, the presenting problem(s) are",

"precertRequired": false,

"billingCode": "99212",

"codeType": "CPT",

"deactivated": null

}, {

"id": 7352,

"description": "Office or other outpatient visit for the evaluation and management of an established patient, which requires at least 2 of these 3 key components: An expanded problem focused history; An expanded problem focused examination; Medical decision making of low complexity. Counseling and coordination of care with other physicians, other qualified health care professionals, or agencies are provided consistent with the nature of the problem(s) and the patient's and/or family's needs. Usually, the present",

"precertRequired": false,

"billingCode": "99213",

"codeType": "CPT",

"deactivated": null

}, {

"id": 7353,

"description": "Office or other outpatient visit for the evaluation and management of an established patient, which requires at least 2 of these 3 key components: A detailed history; A detailed examination; Medical decision making of moderate complexity. Counseling and/or coordination of care with other physicians, other qualified health care professionals, or agencies are provided consistent with the nature of the problem(s) and the patient's and/or family's needs. Usually, the presenting problem(s) are of mod",

"precertRequired": false,

"billingCode": "99214",

"codeType": "CPT",

"deactivated": null

}, {

"id": 7354,

"description": "Office or other outpatient visit for the evaluation and management of an established patient, which requires at least 2 of these 3 key components: A comprehensive history; A comprehensive examination; Medical decision making of high complexity. Counseling and/or coordination of care with other physicians, other qualified health care professionals, or agencies are provided consistent with the nature of the problem(s) and the patient's and/or family's needs. Usually, the presenting problem(s) are ",

"precertRequired": false,

"billingCode": "99215",

"codeType": "CPT",

"deactivated": null

}

\],

"serviceHptcs": \[{

"HPTC": "111NR0200X"

}, {

"HPTC": "111NX0100X"

}, {

"HPTC": "111NX0800X"

}, {

"HPTC": "111NP0017X"

}, {

"HPTC": "111NS0005X"

}, {

"HPTC": "111NT0100X"

}, {

"HPTC": "111NI0900X"

}, {

"HPTC": "111NN0400X"

}, {

"HPTC": "111NN1001X"

}, {

"HPTC": "111N00000X"

}, {

"HPTC": "111NI0013X"

}, {

"HPTC": "111NR0400X"

}

\]

}, {

"id": 676,

"description": "A maximum of twelve (12) acupuncture visits is approved for this episode of care. Approved services include acupuncture with or without electrostimulation. A maximum of one additional unit of acupuncture (with or without electrostimulation) is allowed when the re-insertion of needles is supported in medical documentation.",

"frequency": null,

"frequencytype": "",

"visits": 12,

"coderequired": "YES",

"codedBy": null,

"codedtimestamp": "01-03-2019",

"clinicalService": "35-Chiropractic",

"billingCodes": \[{

"id": 7299,

"description": "Acupuncture, 1 or more needles; without electrical stimulation, initial 15 minutes of personal one-on-one contact with the patient.",

"precertRequired": false,

"billingCode": "97810",

"codeType": "CPT",

"deactivated": null

}, {

"id": 7300,

"description": "Acupuncture, 1 or more needles; without electrical stimulation, each additional 15 minutes of personal one-on-one contact with the patient, with re-insertion of needle(s) (List separately in addition to code for primary procedure) ",

"precertRequired": false,

"billingCode": "97811",

"codeType": "CPT",

"deactivated": null

}, {

"id": 7301,

"description": "Acupuncture, 1 or more needles; with electrical stimulation, initial 15 minutes of personal one-on-one contact with the patient.",

"precertRequired": false,

"billingCode": "97813",

"codeType": "CPT",

"deactivated": null

}, {

"id": 7302,

"description": "Acupuncture, 1 or more needles; with electrical stimulation, each additional 15 minutes of personal one-on-one contact with the patient, with re-insertion of needle(s) (List separately in addition to code for primary procedure) ",

"precertRequired": false,

"billingCode": "97814",

"codeType": "CPT",

"deactivated": null

}

\],

"serviceHptcs": \[{

"HPTC": "111NR0200X"

}, {

"HPTC": "111NX0100X"

}, {

"HPTC": "111NX0800X"

}, {

"HPTC": "111NP0017X"

}, {

"HPTC": "111NS0005X"

}, {

"HPTC": "111NT0100X"

}, {

"HPTC": "111NI0900X"

}, {

"HPTC": "111NN0400X"

}, {

"HPTC": "111NN1001X"

}, {

"HPTC": "111N00000X"

}, {

"HPTC": "111NI0013X"

}, {

"HPTC": "111NR0400X"

}

\]

}, {

"id": 677,

"description": "If indicated, approved modalities that can be utilized during the approved acupuncture visits noted in &#x23;2 above can include: manual therapy and therapeutic exercise procedures including but not limited to: cupping, myofascial release, and therapeutic exercises.",

"frequency": null,

"frequencytype": "",

"visits": 999,

"coderequired": "YES",

"codedBy": null,

"codedtimestamp": "01-03-2019",

"clinicalService": "35-Chiropractic",

"billingCodes": \[{

"id": 7240,

"description": "Application of a modality to 1 or more areas; vasopneumatic devices",

"precertRequired": false,

"billingCode": "97016",

"codeType": "CPT",

"deactivated": null

}, {

"id": 7252,

"description": "Therapeutic procedure, one or more areas, each 15 minutes; therapeutic exercises to develop strength and endurance, range of motion and flexibility",

"precertRequired": false,

"billingCode": "97110",

"codeType": "CPT",

"deactivated": null

}, {

"id": 7253,

"description": "Therapeutic procedure, 1 or more areas, each 15 minutes; neuromuscular reeducation of movement, balance, coordination, kinesthetic sense, posture, and/or proprioception for sitting and/or standing activities",

"precertRequired": false,

"billingCode": "97112",

"codeType": "CPT",

"deactivated": null

}, {

"id": 7257,

"description": "Therapeutic procedure, 1 or more areas, each 15 minutes; massage, including effleurage, petrissage and/or tapotement (stroking, compression, percussion)",

"precertRequired": false,

"billingCode": "97124",

"codeType": "CPT",

"deactivated": null

}, {

"id": 7259,

"description": "Unlisted therapeutic procedure (specify)",

"precertRequired": false,

"billingCode": "97139",

"codeType": "CPT",

"deactivated": null

}, {

"id": 7260,

"description": "Manual therapy techniques (eg, mobilization/manipulation, manual lymphatic drainage, manual traction), 1 or more regions, each 15 minutes",

"precertRequired": false,

"billingCode": "97140",

"codeType": "CPT",

"deactivated": null

}, {

"id": 7274,

"description": "Therapeutic activities, direct (one-on-one) patient contact by the provider (use of dynamic activities to improve functional performance), each 15 minutes",

"precertRequired": false,

"billingCode": "97530",

"codeType": "CPT",

"deactivated": null

}

\],

"serviceHptcs": \[{

"HPTC": "111NR0200X"

}, {

"HPTC": "111NX0100X"

}, {

"HPTC": "111NX0800X"

}, {

"HPTC": "111NP0017X"

}, {

"HPTC": "111NS0005X"

}, {

"HPTC": "111NT0100X"

}, {

"HPTC": "111NI0900X"

}, {

"HPTC": "111NN0400X"

}, {

"HPTC": "111NN1001X"

}, {

"HPTC": "111N00000X"

}, {

"HPTC": "111NI0013X"

}, {

"HPTC": "111NR0400X"

}

\]

}, {

"id": 678,

"description": "Outpatient re-evaluation during this episode of care as clinically indicated.",

"frequency": null,

"frequencytype": "",

"visits": 999,

"coderequired": "YES",

"codedBy": null,

"codedtimestamp": "01-03-2019",

"clinicalService": "35-Chiropractic",

"billingCodes": \[{

"id": 7350,

"description": "Office or other outpatient visit for the evaluation and management of an established patient, that may not require the presence of a physician or other qualified health care professional. Usually, the presenting problem(s) are minimal. Typically, 5 minutes are spent performing or supervising these services. ",

"precertRequired": false,

"billingCode": "99211",

"codeType": "CPT",

"deactivated": null

}, {

"id": 7351,

"description": "Office or other outpatient visit for the evaluation and management of an established patient, which requires at least 2 of these 3 key components: A problem focused history; A problem focused examination; Straightforward medical decision making. Counseling and/or coordination of care with other physicians, other qualified health care professionals, or agencies are provided consistent with the nature of the problem(s) and the patient's and/or family's needs. Usually, the presenting problem(s) are",

"precertRequired": false,

"billingCode": "99212",

"codeType": "CPT",

"deactivated": null

}, {

"id": 7352,

"description": "Office or other outpatient visit for the evaluation and management of an established patient, which requires at least 2 of these 3 key components: An expanded problem focused history; An expanded problem focused examination; Medical decision making of low complexity. Counseling and coordination of care with other physicians, other qualified health care professionals, or agencies are provided consistent with the nature of the problem(s) and the patient's and/or family's needs. Usually, the present",

"precertRequired": false,

"billingCode": "99213",

"codeType": "CPT",

"deactivated": null

}, {

"id": 7353,

"description": "Office or other outpatient visit for the evaluation and management of an established patient, which requires at least 2 of these 3 key components: A detailed history; A detailed examination; Medical decision making of moderate complexity. Counseling and/or coordination of care with other physicians, other qualified health care professionals, or agencies are provided consistent with the nature of the problem(s) and the patient's and/or family's needs. Usually, the presenting problem(s) are of mod",

"precertRequired": false,

"billingCode": "99214",

"codeType": "CPT",

"deactivated": null

}, {

"id": 7354,

"description": "Office or other outpatient visit for the evaluation and management of an established patient, which requires at least 2 of these 3 key components: A comprehensive history; A comprehensive examination; Medical decision making of high complexity. Counseling and/or coordination of care with other physicians, other qualified health care professionals, or agencies are provided consistent with the nature of the problem(s) and the patient's and/or family's needs. Usually, the presenting problem(s) are ",

"precertRequired": false,

"billingCode": "99215",

"codeType": "CPT",

"deactivated": null

}

\],

"serviceHptcs": \[{

"HPTC": "111NR0200X"

}, {

"HPTC": "111NX0100X"

}, {

"HPTC": "111NX0800X"

}, {

"HPTC": "111NP0017X"

}, {

"HPTC": "111NS0005X"

}, {

"HPTC": "111NT0100X"

}, {

"HPTC": "111NI0900X"

}, {

"HPTC": "111NN0400X"

}, {

"HPTC": "111NN1001X"

}, {

"HPTC": "111N00000X"

}, {

"HPTC": "111NI0013X"

}, {

"HPTC": "111NR0400X"

}

\]

}

\],

"hptcs": \[{

"hptc": "171100000X",

"classification": "Acupuncturist",

"specialization": "",

"grouping": "Other Service Providers"

}

\]

}

}, {

"Seoc": {

"id": 122,

"seocKey": 1,

"name": "Acupuncture Initial",

"seocId": "PMR_ACUPUNCTURE INITIAL_1.0.3",

"versionNumber": "1.0.3",

"description": "This authorization covers services associated with all medical care listed below for the referred condition on the consult.",

"effectiveDate": "12-07-2018",

"endDate": "01-03-2019",

"duration": 90,

"REV": false,

"proceduralOverview": "1. Initial outpatient evaluation for this episode of care\r\n2. A maximum of twelve (12) acupuncture visits is approved for this episode of care. Approved services include acupuncture with or without electrostimulation. A maximum of one additional unit of acupuncture (with or without electrostimulation) is allowed when the re-insertion of needles is supported in medical documentation\r\n3. If indicated, approved modalities that can be utilized during the approved acupuncture visits noted in &#x23;2 above can include: manual therapy and therapeutic exercise procedures including but not limited to: cupping, myofascial release, and therapeutic exercises\r\n4. Outpatient re-evaluation during this episode of care as clinically indicated.",

"maxAllowableVisits": 999,

"disclaimer": "\*Additional acupuncture care beyond this trial must provide documentation of: Objective measures demonstrating the extent of meaningful clinical improvement to date; and rationale for the additional treatment requested (e.g. to reach further durable improvement, or for ongoing pain management); and any further information supporting the need for additional care \*Additional consultations needed relevant to the patient complaint/condition require VA review and approval.",

"activatedTimestamp": "12-14-2018",

"activatedBy": "VACOHOLTE",

"discontinuedTimestamp": "01-03-2019",

"discontinuedBy": "SystemUser",

"status": "Discontinued",

"QASP": "Complementary & Integrative HC Services",

"categoryOfCare": "ACUPUNCTURE",

"serviceLine": "Physical Medicine and Rehabilitation",

"services": \[{

"id": 7,

"description": "Initial outpatient evaluation for this episode of care",

"frequency": null,

"frequencytype": "",

"visits": 999,

"coderequired": "YES",

"codedBy": "VACOHOLTE",

"codedtimestamp": "12-14-2018",

"clinicalService": "35-Chiropractic",

"billingCodes": \[{

"id": 7345,

"description": "Office or other outpatient visit for the evaluation and management of a new patient, which requires these 3 key components: A problem focused history; A problem focused examination; Straightforward medical decision making. Counseling and/or coordination of care with other physicians, other qualified health care professionals, or agencies are provided consistent with the nature of the problem(s) and the patient's and/or family's needs. Usually, the presenting problem(s) are self limited or minor.",

"precertRequired": false,

"billingCode": "99201",

"codeType": "CPT",

"deactivated": null

}, {

"id": 7346,

"description": "Office or other outpatient visit for the evaluation and management of a new patient, which requires these 3 key components: An expanded problem focused history; An expanded problem focused examination; Straightforward medical decision making. Counseling and/or coordination of care with other physicians, other qualified health care professionals, or agencies are provided consistent with the nature of the problem(s) and the patient's and/or family's needs. Usually, the presenting problem(s) are of",

"precertRequired": false,

"billingCode": "99202",

"codeType": "CPT",

"deactivated": null

}, {

"id": 7347,

"description": "Office or other outpatient visit for the evaluation and management of a new patient, which requires these 3 key components: A detailed history; A detailed examination; Medical decision making of low complexity. Counseling and/or coordination of care with other physicians, other qualified health care professionals, or agencies are provided consistent with the nature of the problem(s) and the patient's and/or family's needs. Usually, the presenting problem(s) are of moderate severity. Typically, 3",

"precertRequired": false,

"billingCode": "99203",

"codeType": "CPT",

"deactivated": null

}, {

"id": 7348,

"description": "Office or other outpatient visit for the evaluation and management of a new patient, which requires these 3 key components: A comprehensive history; A comprehensive examination; Medical decision making of moderate complexity. Counseling and/or coordination of care with other physicians, other qualified health care professionals, or agencies are provided consistent with the nature of the problem(s) and the patient's and/or family's needs. Usually, the presenting problem(s) are of moderate to high",

"precertRequired": false,

"billingCode": "99204",

"codeType": "CPT",

"deactivated": null

}, {

"id": 7349,

"description": "Office or other outpatient visit for the evaluation and management of a new patient, which requires these 3 key components: A comprehensive history; A comprehensive examination; Medical decision making of high complexity. Counseling and/or coordination of care with other physicians, other qualified health care professionals, or agencies are provided consistent with the nature of the problem(s) and the patient's and/or family's needs. Usually, the presenting problem(s) are of moderate to high sev",

"precertRequired": false,

"billingCode": "99205",

"codeType": "CPT",

"deactivated": null

}, {

"id": 7350,

"description": "Office or other outpatient visit for the evaluation and management of an established patient, that may not require the presence of a physician or other qualified health care professional. Usually, the presenting problem(s) are minimal. Typically, 5 minutes are spent performing or supervising these services. ",

"precertRequired": false,

"billingCode": "99211",

"codeType": "CPT",

"deactivated": null

}, {

"id": 7351,

"description": "Office or other outpatient visit for the evaluation and management of an established patient, which requires at least 2 of these 3 key components: A problem focused history; A problem focused examination; Straightforward medical decision making. Counseling and/or coordination of care with other physicians, other qualified health care professionals, or agencies are provided consistent with the nature of the problem(s) and the patient's and/or family's needs. Usually, the presenting problem(s) are",

"precertRequired": false,

"billingCode": "99212",

"codeType": "CPT",

"deactivated": null

}, {

"id": 7352,

"description": "Office or other outpatient visit for the evaluation and management of an established patient, which requires at least 2 of these 3 key components: An expanded problem focused history; An expanded problem focused examination; Medical decision making of low complexity. Counseling and coordination of care with other physicians, other qualified health care professionals, or agencies are provided consistent with the nature of the problem(s) and the patient's and/or family's needs. Usually, the present",

"precertRequired": false,

"billingCode": "99213",

"codeType": "CPT",

"deactivated": null

}, {

"id": 7353,

"description": "Office or other outpatient visit for the evaluation and management of an established patient, which requires at least 2 of these 3 key components: A detailed history; A detailed examination; Medical decision making of moderate complexity. Counseling and/or coordination of care with other physicians, other qualified health care professionals, or agencies are provided consistent with the nature of the problem(s) and the patient's and/or family's needs. Usually, the presenting problem(s) are of mod",

"precertRequired": false,

"billingCode": "99214",

"codeType": "CPT",

"deactivated": null

}, {

"id": 7354,

"description": "Office or other outpatient visit for the evaluation and management of an established patient, which requires at least 2 of these 3 key components: A comprehensive history; A comprehensive examination; Medical decision making of high complexity. Counseling and/or coordination of care with other physicians, other qualified health care professionals, or agencies are provided consistent with the nature of the problem(s) and the patient's and/or family's needs. Usually, the presenting problem(s) are ",

"precertRequired": false,

"billingCode": "99215",

"codeType": "CPT",

"deactivated": null

}

\],

"serviceHptcs": \[{

"HPTC": "111NR0200X"

}, {

"HPTC": "111NX0100X"

}, {

"HPTC": "111NX0800X"

}, {

"HPTC": "111NP0017X"

}, {

"HPTC": "111NS0005X"

}, {

"HPTC": "111NT0100X"

}, {

"HPTC": "111NI0900X"

}, {

"HPTC": "111NN0400X"

}, {

"HPTC": "111NN1001X"

}, {

"HPTC": "111N00000X"

}, {

"HPTC": "111NI0013X"

}, {

"HPTC": "111NR0400X"

}

\]

}, {

"id": 8,

"description": "A maximum of twelve (12) acupuncture visits is approved for this episode of care. Approved services include acupuncture with or without electrostimulation. A maximum of one additional unit of acupuncture (with or without electrostimulation) is allowed when the re-insertion of needles is supported in medical documentation.",

"frequency": null,

"frequencytype": "",

"visits": 12,

"coderequired": "YES",

"codedBy": "VACOHOLTE",

"codedtimestamp": "12-14-2018",

"clinicalService": "35-Chiropractic",

"billingCodes": \[{

"id": 7299,

"description": "Acupuncture, 1 or more needles; without electrical stimulation, initial 15 minutes of personal one-on-one contact with the patient.",

"precertRequired": false,

"billingCode": "97810",

"codeType": "CPT",

"deactivated": null

}, {

"id": 7300,

"description": "Acupuncture, 1 or more needles; without electrical stimulation, each additional 15 minutes of personal one-on-one contact with the patient, with re-insertion of needle(s) (List separately in addition to code for primary procedure) ",

"precertRequired": false,

"billingCode": "97811",

"codeType": "CPT",

"deactivated": null

}, {

"id": 7301,

"description": "Acupuncture, 1 or more needles; with electrical stimulation, initial 15 minutes of personal one-on-one contact with the patient.",

"precertRequired": false,

"billingCode": "97813",

"codeType": "CPT",

"deactivated": null

}, {

"id": 7302,

"description": "Acupuncture, 1 or more needles; with electrical stimulation, each additional 15 minutes of personal one-on-one contact with the patient, with re-insertion of needle(s) (List separately in addition to code for primary procedure) ",

"precertRequired": false,

"billingCode": "97814",

"codeType": "CPT",

"deactivated": null

}

\],

"serviceHptcs": \[{

"HPTC": "111NR0200X"

}, {

"HPTC": "111NX0100X"

}, {

"HPTC": "111NX0800X"

}, {

"HPTC": "111NP0017X"

}, {

"HPTC": "111NS0005X"

}, {

"HPTC": "111NT0100X"

}, {

"HPTC": "111NI0900X"

}, {

"HPTC": "111NN0400X"

}, {

"HPTC": "111NN1001X"

}, {

"HPTC": "111N00000X"

}, {

"HPTC": "111NI0013X"

}, {

"HPTC": "111NR0400X"

}

\]

}, {

"id": 9,

"description": "If indicated, approved modalities that can be utilized during the approved acupuncture visits noted in &#x23;2 above can include: manual therapy and therapeutic exercise procedures including but not limited to: cupping, myofascial release, and therapeutic exercises.",

"frequency": null,

"frequencytype": "",

"visits": 999,

"coderequired": "YES",

"codedBy": "VACOHOLTE",

"codedtimestamp": "12-14-2018",

"clinicalService": "35-Chiropractic",

"billingCodes": \[{

"id": 7240,

"description": "Application of a modality to 1 or more areas; vasopneumatic devices",

"precertRequired": false,

"billingCode": "97016",

"codeType": "CPT",

"deactivated": null

}, {

"id": 7252,

"description": "Therapeutic procedure, one or more areas, each 15 minutes; therapeutic exercises to develop strength and endurance, range of motion and flexibility",

"precertRequired": false,

"billingCode": "97110",

"codeType": "CPT",

"deactivated": null

}, {

"id": 7253,

"description": "Therapeutic procedure, 1 or more areas, each 15 minutes; neuromuscular reeducation of movement, balance, coordination, kinesthetic sense, posture, and/or proprioception for sitting and/or standing activities",

"precertRequired": false,

"billingCode": "97112",

"codeType": "CPT",

"deactivated": null

}, {

"id": 7257,

"description": "Therapeutic procedure, 1 or more areas, each 15 minutes; massage, including effleurage, petrissage and/or tapotement (stroking, compression, percussion)",

"precertRequired": false,

"billingCode": "97124",

"codeType": "CPT",

"deactivated": null

}, {

"id": 7259,

"description": "Unlisted therapeutic procedure (specify)",

"precertRequired": false,

"billingCode": "97139",

"codeType": "CPT",

"deactivated": null

}, {

"id": 7260,

"description": "Manual therapy techniques (eg, mobilization/manipulation, manual lymphatic drainage, manual traction), 1 or more regions, each 15 minutes",

"precertRequired": false,

"billingCode": "97140",

"codeType": "CPT",

"deactivated": null

}, {

"id": 7274,

"description": "Therapeutic activities, direct (one-on-one) patient contact by the provider (use of dynamic activities to improve functional performance), each 15 minutes",

"precertRequired": false,

"billingCode": "97530",

"codeType": "CPT",

"deactivated": null

}

\],

"serviceHptcs": \[{

"HPTC": "111NR0200X"

}, {

"HPTC": "111NX0100X"

}, {

"HPTC": "111NX0800X"

}, {

"HPTC": "111NP0017X"

}, {

"HPTC": "111NS0005X"

}, {

"HPTC": "111NT0100X"

}, {

"HPTC": "111NI0900X"

}, {

"HPTC": "111NN0400X"

}, {

"HPTC": "111NN1001X"

}, {

"HPTC": "111N00000X"

}, {

"HPTC": "111NI0013X"

}, {

"HPTC": "111NR0400X"

}

\]

}, {

"id": 10,

"description": "Outpatient re-evaluation during this episode of care as clinically indicated.",

"frequency": null,

"frequencytype": "",

"visits": 999,

"coderequired": "YES",

"codedBy": "VACOHOLTE",

"codedtimestamp": "12-14-2018",

"clinicalService": "35-Chiropractic",

"billingCodes": \[{

"id": 7350,

"description": "Office or other outpatient visit for the evaluation and management of an established patient, that may not require the presence of a physician or other qualified health care professional. Usually, the presenting problem(s) are minimal. Typically, 5 minutes are spent performing or supervising these services. ",

"precertRequired": false,

"billingCode": "99211",

"codeType": "CPT",

"deactivated": null

}, {

"id": 7351,

"description": "Office or other outpatient visit for the evaluation and management of an established patient, which requires at least 2 of these 3 key components: A problem focused history; A problem focused examination; Straightforward medical decision making. Counseling and/or coordination of care with other physicians, other qualified health care professionals, or agencies are provided consistent with the nature of the problem(s) and the patient's and/or family's needs. Usually, the presenting problem(s) are",

"precertRequired": false,

"billingCode": "99212",

"codeType": "CPT",

"deactivated": null

}, {

"id": 7352,

"description": "Office or other outpatient visit for the evaluation and management of an established patient, which requires at least 2 of these 3 key components: An expanded problem focused history; An expanded problem focused examination; Medical decision making of low complexity. Counseling and coordination of care with other physicians, other qualified health care professionals, or agencies are provided consistent with the nature of the problem(s) and the patient's and/or family's needs. Usually, the present",

"precertRequired": false,

"billingCode": "99213",

"codeType": "CPT",

"deactivated": null

}, {

"id": 7353,

"description": "Office or other outpatient visit for the evaluation and management of an established patient, which requires at least 2 of these 3 key components: A detailed history; A detailed examination; Medical decision making of moderate complexity. Counseling and/or coordination of care with other physicians, other qualified health care professionals, or agencies are provided consistent with the nature of the problem(s) and the patient's and/or family's needs. Usually, the presenting problem(s) are of mod",

"precertRequired": false,

"billingCode": "99214",

"codeType": "CPT",

"deactivated": null

}, {

"id": 7354,

"description": "Office or other outpatient visit for the evaluation and management of an established patient, which requires at least 2 of these 3 key components: A comprehensive history; A comprehensive examination; Medical decision making of high complexity. Counseling and/or coordination of care with other physicians, other qualified health care professionals, or agencies are provided consistent with the nature of the problem(s) and the patient's and/or family's needs. Usually, the presenting problem(s) are ",

"precertRequired": false,

"billingCode": "99215",

"codeType": "CPT",

"deactivated": null

}

\],

"serviceHptcs": \[{

"HPTC": "111NR0200X"

}, {

"HPTC": "111NX0100X"

}, {

"HPTC": "111NX0800X"

}, {

"HPTC": "111NP0017X"

}, {

"HPTC": "111NS0005X"

}, {

"HPTC": "111NT0100X"

}, {

"HPTC": "111NI0900X"

}, {

"HPTC": "111NN0400X"

}, {

"HPTC": "111NN1001X"

}, {

"HPTC": "111N00000X"

}, {

"HPTC": "111NI0013X"

}, {

"HPTC": "111NR0400X"

}

\]

}

\],

"hptcs": \[{

"hptc": "103GC0700X",

"classification": "Clinical Neuropsychologist",

"specialization": "Clinical",

"grouping": "Behavioral Health & Social Service Providers"

}

\]

}

}

\]

}

## Get Active, Discontinued, and Date Hold SEOCs v2: /v2/seoc \[abbreviated\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

{

"Seocs": \[{

"Seoc": {

"id": 181,

"seocKey": 1,

"name": "Acupuncture Initial",

"seocId": "PMR_ACUPUNCTURE INITIAL_1.0.4",

"versionNumber": "1.0.4",

"description": "This authorization covers services associated with all medical care listed below for the referred condition on the consult.",

"effectiveDate": "01-03-2019",

"endDate": null,

"duration": 90,

"REV": false,

"PRCT": false,

"proceduralOverview": "1. Initial outpatient evaluation for this episode of care\r\n2. A maximum of twelve (12) acupuncture visits is approved for this episode of care. Approved services include acupuncture with or without electrostimulation. A maximum of one additional unit of acupuncture (with or without electrostimulation) is allowed when the re-insertion of needles is supported in medical documentation\r\n3. If indicated, approved modalities that can be utilized during the approved acupuncture visits noted in &#x23;2 above can include: manual therapy and therapeutic exercise procedures including but not limited to: cupping, myofascial release, and therapeutic exercises\r\n4. Outpatient re-evaluation during this episode of care as clinically indicated.",

"maxAllowableVisits": null,

"disclaimer": "\*Additional acupuncture care beyond this trial must provide documentation of: Objective measures demonstrating the extent of meaningful clinical improvement to date; and rationale for the additional treatment requested (e.g. to reach further durable improvement, or for ongoing pain management); and any further information supporting the need for additional care \*Additional consultations needed relevant to the patient complaint/condition require VA review and approval.",

"QASP": "Complementary & Integrative HC Services",

"categoryOfCare": "ACUPUNCTURE",

"serviceLine": "Physical Medicine and Rehabilitation",

"hptcs": \[{

"hptc": "171100000X"

}

\],

"services": \[{

"id": 675,

"description": "Initial outpatient evaluation for this episode of care",

"frequency": null,

"frequencyType": "",

"visits": 999,

"codeRequired": "YES",

"clinicalServices": \[{

"clinicalService": "35-Chiropractic"

}

\],

"billingCodes": \[{

"id": 7345,

"precertRequired": false,

"billingCode": "99201",

"codeType": "CPT"

}, {

"id": 7346,

"precertRequired": false,

"billingCode": "99202",

"codeType": "CPT"

}, {

"id": 7347,

"precertRequired": false,

"billingCode": "99203",

"codeType": "CPT"

}, {

"id": 7348,

"precertRequired": false,

"billingCode": "99204",

"codeType": "CPT"

}, {

"id": 7349,

"precertRequired": false,

"billingCode": "99205",

"codeType": "CPT"

}, {

"id": 7350,

"precertRequired": false,

"billingCode": "99211",

"codeType": "CPT"

}, {

"id": 7351,

"precertRequired": false,

"billingCode": "99212",

"codeType": "CPT"

}, {

"id": 7352,

"precertRequired": false,

"billingCode": "99213",

"codeType": "CPT"

}, {

"id": 7353,

"precertRequired": false,

"billingCode": "99214",

"codeType": "CPT"

}, {

"id": 7354,

"precertRequired": false,

"billingCode": "99215",

"codeType": "CPT"

}

\],

"serviceHptcs": \[{

"HPTC": "111NR0200X"

}, {

"HPTC": "111NX0100X"

}, {

"HPTC": "111NX0800X"

}, {

"HPTC": "111NP0017X"

}, {

"HPTC": "111NS0005X"

}, {

"HPTC": "111NT0100X"

}, {

"HPTC": "111NI0900X"

}, {

"HPTC": "111NN0400X"

}, {

"HPTC": "111NN1001X"

}, {

"HPTC": "111N00000X"

}, {

"HPTC": "111NI0013X"

}, {

"HPTC": "111NR0400X"

}

\]

}, {

"id": 676,

"description": "A maximum of twelve (12) acupuncture visits is approved for this episode of care. Approved services include acupuncture with or without electrostimulation. A maximum of one additional unit of acupuncture (with or without electrostimulation) is allowed when the re-insertion of needles is supported in medical documentation.",

"frequency": null,

"frequencyType": "",

"visits": 12,

"codeRequired": "YES",

"clinicalServices": \[{

"clinicalService": "35-Chiropractic"

}

\],

"billingCodes": \[{

"id": 7299,

"precertRequired": false,

"billingCode": "97810",

"codeType": "CPT"

}, {

"id": 7300,

"precertRequired": false,

"billingCode": "97811",

"codeType": "CPT"

}, {

"id": 7301,

"precertRequired": false,

"billingCode": "97813",

"codeType": "CPT"

}, {

"id": 7302,

"precertRequired": false,

"billingCode": "97814",

"codeType": "CPT"

}

\],

"serviceHptcs": \[{

"HPTC": "111NR0200X"

}, {

"HPTC": "111NX0100X"

}, {

"HPTC": "111NX0800X"

}, {

"HPTC": "111NP0017X"

}, {

"HPTC": "111NS0005X"

}, {

"HPTC": "111NT0100X"

}, {

"HPTC": "111NI0900X"

}, {

"HPTC": "111NN0400X"

}, {

"HPTC": "111NN1001X"

}, {

"HPTC": "111N00000X"

}, {

"HPTC": "111NI0013X"

}, {

"HPTC": "111NR0400X"

}

\]

}, {

"id": 677,

"description": "If indicated, approved modalities that can be utilized during the approved acupuncture visits noted in &#x23;2 above can include: manual therapy and therapeutic exercise procedures including but not limited to: cupping, myofascial release, and therapeutic exercises.",

"frequency": null,

"frequencyType": "",

"visits": 999,

"codeRequired": "YES",

"clinicalServices": \[{

"clinicalService": "35-Chiropractic"

}

\],

"billingCodes": \[{

"id": 7240,

"precertRequired": false,

"billingCode": "97016",

"codeType": "CPT"

}, {

"id": 7252,

"precertRequired": false,

"billingCode": "97110",

"codeType": "CPT"

}, {

"id": 7253,

"precertRequired": false,

"billingCode": "97112",

"codeType": "CPT"

}, {

"id": 7257,

"precertRequired": false,

"billingCode": "97124",

"codeType": "CPT"

}, {

"id": 7259,

"precertRequired": false,

"billingCode": "97139",

"codeType": "CPT"

}, {

"id": 7260,

"precertRequired": false,

"billingCode": "97140",

"codeType": "CPT"

}, {

"id": 7274,

"precertRequired": false,

"billingCode": "97530",

"codeType": "CPT"

}

\],

"serviceHptcs": \[{

"HPTC": "111NR0200X"

}, {

"HPTC": "111NX0100X"

}, {

"HPTC": "111NX0800X"

}, {

"HPTC": "111NP0017X"

}, {

"HPTC": "111NS0005X"

}, {

"HPTC": "111NT0100X"

}, {

"HPTC": "111NI0900X"

}, {

"HPTC": "111NN0400X"

}, {

"HPTC": "111NN1001X"

}, {

"HPTC": "111N00000X"

}, {

"HPTC": "111NI0013X"

}, {

"HPTC": "111NR0400X"

}

\]

}, {

"id": 678,

"description": "Outpatient re-evaluation during this episode of care as clinically indicated.",

"frequency": null,

"frequencyType": "",

"visits": 999,

"codeRequired": "YES",

"clinicalServices": \[{

"clinicalService": "35-Chiropractic"

}

\],

"billingCodes": \[{

"id": 7350,

"precertRequired": false,

"billingCode": "99211",

"codeType": "CPT"

}, {

"id": 7351,

"precertRequired": false,

"billingCode": "99212",

"codeType": "CPT"

}, {

"id": 7352,

"precertRequired": false,

"billingCode": "99213",

"codeType": "CPT"

}, {

"id": 7353,

"precertRequired": false,

"billingCode": "99214",

"codeType": "CPT"

}, {

"id": 7354,

"precertRequired": false,

"billingCode": "99215",

"codeType": "CPT"

}

\],

"serviceHptcs": \[{

"HPTC": "111NR0200X"

}, {

"HPTC": "111NX0100X"

}, {

"HPTC": "111NX0800X"

}, {

"HPTC": "111NP0017X"

}, {

"HPTC": "111NS0005X"

}, {

"HPTC": "111NT0100X"

}, {

"HPTC": "111NI0900X"

}, {

"HPTC": "111NN0400X"

}, {

"HPTC": "111NN1001X"

}, {

"HPTC": "111N00000X"

}, {

"HPTC": "111NI0013X"

}, {

"HPTC": "111NR0400X"

}

\]

}

\]

}

}, {

"Seoc": {

"id": 122,

"seocKey": 1,

"name": "Acupuncture Initial",

"seocId": "PMR_ACUPUNCTURE INITIAL_1.0.3",

"versionNumber": "1.0.3",

"description": "This authorization covers services associated with all medical care listed below for the referred condition on the consult.",

"effectiveDate": "12-07-2018",

"endDate": "01-03-2019",

"duration": 90,

"REV": false,

"PRCT": false,

"proceduralOverview": "1. Initial outpatient evaluation for this episode of care\r\n2. A maximum of twelve (12) acupuncture visits is approved for this episode of care. Approved services include acupuncture with or without electrostimulation. A maximum of one additional unit of acupuncture (with or without electrostimulation) is allowed when the re-insertion of needles is supported in medical documentation\r\n3. If indicated, approved modalities that can be utilized during the approved acupuncture visits noted in &#x23;2 above can include: manual therapy and therapeutic exercise procedures including but not limited to: cupping, myofascial release, and therapeutic exercises\r\n4. Outpatient re-evaluation during this episode of care as clinically indicated.",

"maxAllowableVisits": 999,

"disclaimer": "\*Additional acupuncture care beyond this trial must provide documentation of: Objective measures demonstrating the extent of meaningful clinical improvement to date; and rationale for the additional treatment requested (e.g. to reach further durable improvement, or for ongoing pain management); and any further information supporting the need for additional care \*Additional consultations needed relevant to the patient complaint/condition require VA review and approval.",

"QASP": "Complementary & Integrative HC Services",

"categoryOfCare": "ACUPUNCTURE",

"serviceLine": "Physical Medicine and Rehabilitation",

"hptcs": \[{

"hptc": "103GC0700X"

}

\],

"services": \[{

"id": 7,

"description": "Initial outpatient evaluation for this episode of care",

"frequency": null,

"frequencyType": "",

"visits": 999,

"codeRequired": "YES",

"clinicalServices": \[{

"clinicalService": "35-Chiropractic"

}

\],

"billingCodes": \[{

"id": 7345,

"precertRequired": false,

"billingCode": "99201",

"codeType": "CPT"

}, {

"id": 7346,

"precertRequired": false,

"billingCode": "99202",

"codeType": "CPT"

}, {

"id": 7347,

"precertRequired": false,

"billingCode": "99203",

"codeType": "CPT"

}, {

"id": 7348,

"precertRequired": false,

"billingCode": "99204",

"codeType": "CPT"

}, {

"id": 7349,

"precertRequired": false,

"billingCode": "99205",

"codeType": "CPT"

}, {

"id": 7350,

"precertRequired": false,

"billingCode": "99211",

"codeType": "CPT"

}, {

"id": 7351,

"precertRequired": false,

"billingCode": "99212",

"codeType": "CPT"

}, {

"id": 7352,

"precertRequired": false,

"billingCode": "99213",

"codeType": "CPT"

}, {

"id": 7353,

"precertRequired": false,

"billingCode": "99214",

"codeType": "CPT"

}, {

"id": 7354,

"precertRequired": false,

"billingCode": "99215",

"codeType": "CPT"

}

\],

"serviceHptcs": \[{

"HPTC": "111NR0200X"

}, {

"HPTC": "111NX0100X"

}, {

"HPTC": "111NX0800X"

}, {

"HPTC": "111NP0017X"

}, {

"HPTC": "111NS0005X"

}, {

"HPTC": "111NT0100X"

}, {

"HPTC": "111NI0900X"

}, {

"HPTC": "111NN0400X"

}, {

"HPTC": "111NN1001X"

}, {

"HPTC": "111N00000X"

}, {

"HPTC": "111NI0013X"

}, {

"HPTC": "111NR0400X"

}

\]

}, {

"id": 8,

"description": "A maximum of twelve (12) acupuncture visits is approved for this episode of care. Approved services include acupuncture with or without electrostimulation. A maximum of one additional unit of acupuncture (with or without electrostimulation) is allowed when the re-insertion of needles is supported in medical documentation.",

"frequency": null,

"frequencyType": "",

"visits": 12,

"codeRequired": "YES",

"clinicalServices": \[{

"clinicalService": "35-Chiropractic"

}

\],

"billingCodes": \[{

"id": 7299,

"precertRequired": false,

"billingCode": "97810",

"codeType": "CPT"

}, {

"id": 7300,

"precertRequired": false,

"billingCode": "97811",

"codeType": "CPT"

}, {

"id": 7301,

"precertRequired": false,

"billingCode": "97813",

"codeType": "CPT"

}, {

"id": 7302,

"precertRequired": false,

"billingCode": "97814",

"codeType": "CPT"

}

\],

"serviceHptcs": \[{

"HPTC": "111NR0200X"

}, {

"HPTC": "111NX0100X"

}, {

"HPTC": "111NX0800X"

}, {

"HPTC": "111NP0017X"

}, {

"HPTC": "111NS0005X"

}, {

"HPTC": "111NT0100X"

}, {

"HPTC": "111NI0900X"

}, {

"HPTC": "111NN0400X"

}, {

"HPTC": "111NN1001X"

}, {

"HPTC": "111N00000X"

}, {

"HPTC": "111NI0013X"

}, {

"HPTC": "111NR0400X"

}

\]

}, {

"id": 9,

"description": "If indicated, approved modalities that can be utilized during the approved acupuncture visits noted in &#x23;2 above can include: manual therapy and therapeutic exercise procedures including but not limited to: cupping, myofascial release, and therapeutic exercises.",

"frequency": null,

"frequencyType": "",

"visits": 999,

"codeRequired": "YES",

"clinicalServices": \[{

"clinicalService": "35-Chiropractic"

}

\],

"billingCodes": \[{

"id": 7240,

"precertRequired": false,

"billingCode": "97016",

"codeType": "CPT"

}, {

"id": 7252,

"precertRequired": false,

"billingCode": "97110",

"codeType": "CPT"

}, {

"id": 7253,

"precertRequired": false,

"billingCode": "97112",

"codeType": "CPT"

}, {

"id": 7257,

"precertRequired": false,

"billingCode": "97124",

"codeType": "CPT"

}, {

"id": 7259,

"precertRequired": false,

"billingCode": "97139",

"codeType": "CPT"

}, {

"id": 7260,

"precertRequired": false,

"billingCode": "97140",

"codeType": "CPT"

}, {

"id": 7274,

"precertRequired": false,

"billingCode": "97530",

"codeType": "CPT"

}

\],

"serviceHptcs": \[{

"HPTC": "111NR0200X"

}, {

"HPTC": "111NX0100X"

}, {

"HPTC": "111NX0800X"

}, {

"HPTC": "111NP0017X"

}, {

"HPTC": "111NS0005X"

}, {

"HPTC": "111NT0100X"

}, {

"HPTC": "111NI0900X"

}, {

"HPTC": "111NN0400X"

}, {

"HPTC": "111NN1001X"

}, {

"HPTC": "111N00000X"

}, {

"HPTC": "111NI0013X"

}, {

"HPTC": "111NR0400X"

}

\]

}, {

"id": 10,

"description": "Outpatient re-evaluation during this episode of care as clinically indicated.",

"frequency": null,

"frequencyType": "",

"visits": 999,

"codeRequired": "YES",

"clinicalServices": \[{

"clinicalService": "35-Chiropractic"

}

\],

"billingCodes": \[{

"id": 7350,

"precertRequired": false,

"billingCode": "99211",

"codeType": "CPT"

}, {

"id": 7351,

"precertRequired": false,

"billingCode": "99212",

"codeType": "CPT"

}, {

"id": 7352,

"precertRequired": false,

"billingCode": "99213",

"codeType": "CPT"

}, {

"id": 7353,

"precertRequired": false,

"billingCode": "99214",

"codeType": "CPT"

}, {

"id": 7354,

"precertRequired": false,

"billingCode": "99215",

"codeType": "CPT"

}

\],

"serviceHptcs": \[{

"HPTC": "111NR0200X"

}, {

"HPTC": "111NX0100X"

}, {

"HPTC": "111NX0800X"

}, {

"HPTC": "111NP0017X"

}, {

"HPTC": "111NS0005X"

}, {

"HPTC": "111NT0100X"

}, {

"HPTC": "111NI0900X"

}, {

"HPTC": "111NN0400X"

}, {

"HPTC": "111NN1001X"

}, {

"HPTC": "111N00000X"

}, {

"HPTC": "111NI0013X"

}, {

"HPTC": "111NR0400X"

}

\]

}

\]

}

}

\]

}

## Get Active SEOCs v1: /v1/seoc/active \[abbreviated\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

{

"Seocs": \[{

"Seoc": {

"seocId": "PMR_ACUPUNCTURE INITIAL_1.0.4",

"name": "Acupuncture Initial",

"serviceLine": "Physical Medicine and Rehabilitation",

"categoryOfCare": "ACUPUNCTURE",

"description": "This authorization covers services associated with all medical care listed below for the referred condition on the consult.",

"duration": 90,

"proceduralOverview": "1. Initial outpatient evaluation for this episode of care\r\n2. A maximum of twelve (12) acupuncture visits is approved for this episode of care. Approved services include acupuncture with or without electrostimulation. A maximum of one additional unit of acupuncture (with or without electrostimulation) is allowed when the re-insertion of needles is supported in medical documentation\r\n3. If indicated, approved modalities that can be utilized during the approved acupuncture visits noted in &#x23;2 above can include: manual therapy and therapeutic exercise procedures including but not limited to: cupping, myofascial release, and therapeutic exercises\r\n4. Outpatient re-evaluation during this episode of care as clinically indicated.",

"disclaimer": "\*Additional acupuncture care beyond this trial must provide documentation of: Objective measures demonstrating the extent of meaningful clinical improvement to date; and rationale for the additional treatment requested (e.g. to reach further durable improvement, or for ongoing pain management); and any further information supporting the need for additional care \*Additional consultations needed relevant to the patient complaint/condition require VA review and approval.",

"maxAllowableVisits": null

}

}, {

"Seoc": {

"seocId": "PMR_ACUPUNCTURE-CHRONIC CARE MANAGEMENT_1.2.2",

"name": "Acupuncture-Chronic Care Management",

"serviceLine": "Physical Medicine and Rehabilitation",

"categoryOfCare": "ACUPUNCTURE",

"description": "This authorization covers services associated with all medical care listed below for the referred condition on the consult.",

"duration": 180,

"proceduralOverview": " This referral is for continued pain management (having already completed the initial trial). This includes cases that have not resolved or plateaued but have shown acupuncture be successful. Possible explanations for need of continued care may include emerging complicating factors, substantial change in treatment plan, or unintended gaps in treatment plan. \r\unsuccessful acupuncture treatment for chronic pain management includes: \r\n- Assessment of patient function after a withdrawal of care \[REQUIRED\] \r\n- Consideration of other indicated medical, psychological, behavioral, and/or social interventions \[REQUIRED\] \r\n- Inclusion of appropriate, individualized active care strategies such as home exercise and self-management approaches \[REQUIRED\] \r\nMust include one or more of the following: \r\n- Continued durable improvement in condition being treated \r\n- Continued functional improvement demonstrated by: clinically meaningful improvement on validated disease-specific outcomes instruments; return to work; and/or documented improvement in activities of daily living \r\n- Continued documented decreased utilization of medications\r\n1. One outpatient re-evaluation during this episode of care (if indicated)\r\n2. A maximum of eight (8) acupuncture visits is approved for this episode of care. Approved services include acupuncture with or without electrostimulation. A maximum of one additional unit of acupuncture (with or without electrostimulation) is allowed when the re-insertion of needles is supported in medical documentation\r\n3. If indicated, approved modalities that can be utilized during the approved acupuncture visits noted in &#x23;2 above can include: manual therapy and therapeutic exercise procedures including but not limited to: cupping, myofascial release, and therapeutic exercises.",

"disclaimer": "\*Additional consultations needed relevant to the patient complaint/condition require VA review and approval.",

"maxAllowableVisits": null

}

}, {

"Seoc": {

"seocId": "PMR_ACUPUNCTURE-CONTINUATION OF INITIAL CARE_1.1.2",

"name": "Acupuncture-Continuation of Initial Care",

"serviceLine": "Physical Medicine and Rehabilitation",

"categoryOfCare": "ACUPUNCTURE",

"description": "This authorization covers services associated with all medical care listed below for the referred condition on the consult.",

"duration": 90,

"proceduralOverview": "This referral is for continuation of the initial trial and includes cases that have not resolved or plateaued within the initial 12 visits but have shown acupuncture to be successful. Possible explanations for the need of continued care include emerging complicating factors, substantial change in treatment plan, or unintended gaps in treatment plan. \r\unsuccessful acupuncture treatment includes: \r\n- Durable improvement in condition being treated, or \r\n- Durable functional improvement demonstrated by: clinically meaningful improvement on validated disease-specific outcomes instruments; return to work; and/or documented improvement in activities of daily living, or \r\n- Documented decreased utilization of medications\r\n\r\n1. Outpatient re-evaluation during this episode of care as clinically indicated\r\n2. A maximum of eight (8) acupuncture visits is approved for this episode of care. Approved services include acupuncture with or without electrostimulation. A maximum of one additional unit of acupuncture (with or without electrostimulation) is allowed when the re-insertion of needles is supported in medical documentation\r\n3. If indicated, approved modalities that can be utilized during the approved acupuncture visits noted in &#x23;2 above can include: manual therapy and therapeutic exercise procedures including but not limited to: cupping, myofascial release, and therapeutic exercises.",

"disclaimer": "\*Additional acupuncture care beyond this trial must provide documentation of: Objective measures demonstrating the extent of meaningful clinical improvement to date; AND Rationale for the additional treatment requested (e.g. to reach further durable improvement, or for ongoing pain management); AND Any further information supporting the need for additional care \r\n\*Additional consultations needed relevant to the patient complaint/condition require VA review and approval.",

"maxAllowableVisits": null

}

}

\]

}

## Get Active SEOCs v2: /v2/seoc/active \[abbreviated\]

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

<table>
<colgroup>
<col style="width: 100%" />
</colgroup>
<thead>
<tr class="header">
<th><p>{</p>
<p>"Seocs": [{</p>
<p>"Seoc": {</p>
<p>"seocId": "PMR_ACUPUNCTURE INITIAL_1.0.4",</p>
<p>"name": "Acupuncture Initial",</p>
<p>"serviceLine": "Physical Medicine and Rehabilitation",</p>
<p>"categoryOfCare": "ACUPUNCTURE",</p>
<p>"description": "This authorization covers services associated with all medical care listed below for the referred condition on the consult.",</p>
<p>"duration": 90,</p>
<p>"proceduralOverview": "1. Initial outpatient evaluation for this episode of care\r\n2. A maximum of twelve (12) acupuncture visits is approved for this episode of care. Approved services include acupuncture with or without electrostimulation. A maximum of one additional unit of acupuncture (with or without electrostimulation) is allowed when the re-insertion of needles is supported in medical documentation\r\n3. If indicated, approved modalities that can be utilized during the approved acupuncture visits noted in &amp;#x23;2 above can include: manual therapy and therapeutic exercise procedures including but not limited to: cupping, myofascial release, and therapeutic exercises\r\n4. Outpatient re-evaluation during this episode of care as clinically indicated.",</p>
<p>"disclaimer": "*Additional acupuncture care beyond this trial must provide documentation of: Objective measures demonstrating the extent of meaningful clinical improvement to date; and rationale for the additional treatment requested (e.g. to reach further durable improvement, or for ongoing pain management); and any further information supporting the need for additional care *Additional consultations needed relevant to the patient complaint/condition require VA review and approval.",</p>
<p>"previewText": "VHA Office of Community Care - Standardized Episode of Care\r\nAcupuncture Initial\r\n\r\nSEOC ID:PMR_ACUPUNCTURE INITIAL_1.0.4\r\nDescription:This authorization covers services associated with all medical care listed below for the referred condition on the consult.\r\nDuration:90 days\r\n\r\nProcedural Overview:\r\n1. Initial outpatient evaluation for this episode of care\r\n2. A maximum of twelve (12) acupuncture visits is approved for this episode of care. Approved services include acupuncture with or without electrostimulation. A maximum of one additional unit of acupuncture (with or without electrostimulation) is allowed when the re-insertion of needles is supported in medical documentation\r\n3. If indicated, approved modalities that can be utilized during the approved acupuncture visits noted in &amp;#x23;2 above can include: manual therapy and therapeutic exercise procedures including but not limited to: cupping, myofascial release, and therapeutic exercises\r\n4. Outpatient re-evaluation during this episode of care as clinically indicated.\r\n\r\n*Additional acupuncture care beyond this trial must provide documentation of: Objective measures demonstrating the extent of meaningful clinical improvement to date; and rationale for the additional treatment requested (e.g. to reach further durable improvement, or for ongoing pain management); and any further information supporting the need for additional care *Additional consultations needed relevant to the patient complaint/condition require VA review and approval."</p>
<p>}</p>
<p>}, {</p>
<p>"Seoc": {</p>
<p>"seocId": "PMR_ACUPUNCTURE-CHRONIC CARE MANAGEMENT_1.2.2",</p>
<p>"name": "Acupuncture-Chronic Care Management",</p>
<p>"serviceLine": "Physical Medicine and Rehabilitation",</p>
<p>"categoryOfCare": "ACUPUNCTURE",</p>
<p>"description": "This authorization covers services associated with all medical care listed below for the referred condition on the consult.",</p>
<p>"duration": 180,</p>
<p>"proceduralOverview": " This referral is for continued pain management (having already completed the initial trial). This includes cases that have not resolved or plateaued but have shown acupuncture be successful. Possible explanations for need of continued care may include emerging complicating factors, substantial change in treatment plan, or unintended gaps in treatment plan. \r\nSuccessful acupuncture treatment for chronic pain management includes: \r\n- Assessment of patient function after a withdrawal of care [REQUIRED] \r\n- Consideration of other indicated medical, psychological, behavioral, and/or social interventions [REQUIRED] \r\n- Inclusion of appropriate, individualized active care strategies such as home exercise and self-management approaches [REQUIRED] \r\nMust include one or more of the following: \r\n- Continued durable improvement in condition being treated \r\n- Continued functional improvement demonstrated by: clinically meaningful improvement on validated disease-specific outcomes instruments; return to work; and/or documented improvement in activities of daily living \r\n- Continued documented decreased utilization of medications\r\n1. One outpatient re-evaluation during this episode of care (if indicated)\r\n2. A maximum of eight (8) acupuncture visits is approved for this episode of care. Approved services include acupuncture with or without electrostimulation. A maximum of one additional unit of acupuncture (with or without electrostimulation) is allowed when the re-insertion of needles is supported in medical documentation\r\n3. If indicated, approved modalities that can be utilized during the approved acupuncture visits noted in &amp;#x23;2 above can include: manual therapy and therapeutic exercise procedures including but not limited to: cupping, myofascial release, and therapeutic exercises.",</p>
<p>"disclaimer": "*Additional consultations needed relevant to the patient complaint/condition require VA review and approval.",</p>
<p>"previewText": "VHA Office of Community Care - Standardized Episode of Care\r\nAcupuncture-Chronic Care Management\r\n\r\nSEOC ID:PMR_ACUPUNCTURE-CHRONIC CARE MANAGEMENT_1.2.2\r\nDescription:This authorization covers services associated with all medical care listed below for the referred condition on the consult.\r\nDuration:180 days\r\n\r\nProcedural Overview:\r\n This referral is for continued pain management (having already completed the initial trial). This includes cases that have not resolved or plateaued but have shown acupuncture be successful. Possible explanations for need of continued care may include emerging complicating factors, substantial change in treatment plan, or unintended gaps in treatment plan. \r\nSuccessful acupuncture treatment for chronic pain management includes: \r\n- Assessment of patient function after a withdrawal of care [REQUIRED] \r\n- Consideration of other indicated medical, psychological, behavioral, and/or social interventions [REQUIRED] \r\n- Inclusion of appropriate, individualized active care strategies such as home exercise and self-management approaches [REQUIRED] \r\nMust include one or more of the following: \r\n- Continued durable improvement in condition being treated \r\n- Continued functional improvement demonstrated by: clinically meaningful improvement on validated disease-specific outcomes instruments; return to work; and/or documented improvement in activities of daily living \r\n- Continued documented decreased utilization of medications\r\n1. One outpatient re-evaluation during this episode of care (if indicated)\r\n2. A maximum of eight (8) acupuncture visits is approved for this episode of care. Approved services include acupuncture with or without electrostimulation. A maximum of one additional unit of acupuncture (with or without electrostimulation) is allowed when the re-insertion of needles is supported in medical documentation\r\n3. If indicated, approved modalities that can be utilized during the approved acupuncture visits noted in &amp;#x23;2 above can include: manual therapy and therapeutic exercise procedures including but not limited to: cupping, myofascial release, and therapeutic exercises.\r\n\r\n*Additional consultations needed relevant to the patient complaint/condition require VA review and approval."</p>
<p>}</p>
<p>}, {</p>
<p>"Seoc": {</p>
<p>"seocId": "PMR_ACUPUNCTURE-CONTINUATION OF INITIAL CARE_1.1.2",</p>
<p>"name": "Acupuncture-Continuation of Initial Care",</p>
<p>"serviceLine": "Physical Medicine and Rehabilitation",</p>
<p>"categoryOfCare": "ACUPUNCTURE",</p>
<p>"description": "This authorization covers services associated with all medical care listed below for the referred condition on the consult.",</p>
<p>"duration": 90,</p>
<p>"proceduralOverview": "This referral is for continuation of the initial trial and includes cases that have not resolved or plateaued within the initial 12 visits but have shown acupuncture to be successful. Possible explanations for the need of continued care include emerging complicating factors, substantial change in treatment plan, or unintended gaps in treatment plan. \r\nSuccessful acupuncture treatment includes: \r\n- Durable improvement in condition being treated, or \r\n- Durable functional improvement demonstrated by: clinically meaningful improvement on validated disease-specific outcomes instruments; return to work; and/or documented improvement in activities of daily living, or \r\n- Documented decreased utilization of medications\r\n\r\n1. Outpatient re-evaluation during this episode of care as clinically indicated\r\n2. A maximum of eight (8) acupuncture visits is approved for this episode of care. Approved services include acupuncture with or without electrostimulation. A maximum of one additional unit of acupuncture (with or without electrostimulation) is allowed when the re-insertion of needles is supported in medical documentation\r\n3. If indicated, approved modalities that can be utilized during the approved acupuncture visits noted in &amp;#x23;2 above can include: manual therapy and therapeutic exercise procedures including but not limited to: cupping, myofascial release, and therapeutic exercises.",</p>
<p>"disclaimer": "*Additional acupuncture care beyond this trial must provide documentation of: Objective measures demonstrating the extent of meaningful clinical improvement to date; AND Rationale for the additional treatment requested (e.g. to reach further durable improvement, or for ongoing pain management); AND Any further information supporting the need for additional care \r\n*Additional consultations needed relevant to the patient complaint/condition require VA review and approval.",</p>
<p>"previewText": "VHA Office of Community Care - Standardized Episode of Care\r\nAcupuncture-Continuation of Initial Care\r\n\r\nSEOC ID:PMR_ACUPUNCTURE-CONTINUATION OF INITIAL CARE_1.1.2\r\nDescription:This authorization covers services associated with all medical care listed below for the referred condition on the consult.\r\nDuration:90 days\r\n\r\nProcedural Overview:\r\nThis referral is for continuation of the initial trial and includes cases that have not resolved or plateaued within the initial 12 visits but have shown acupuncture to be successful. Possible explanations for the need of continued care include emerging complicating factors, substantial change in treatment plan, or unintended gaps in treatment plan. \r\nSuccessful acupuncture treatment includes: \r\n- Durable improvement in condition being treated, or \r\n- Durable functional improvement demonstrated by: clinically meaningful improvement on validated disease-specific outcomes instruments; return to work; and/or documented improvement in activities of daily living, or \r\n- Documented decreased utilization of medications\r\n\r\n1. Outpatient re-evaluation during this episode of care as clinically indicated\r\n2. A maximum of eight (8) acupuncture visits is approved for this episode of care. Approved services include acupuncture with or without electrostimulation. A maximum of one additional unit of acupuncture (with or without electrostimulation) is allowed when the re-insertion of needles is supported in medical documentation\r\n3. If indicated, approved modalities that can be utilized during the approved acupuncture visits noted in &amp;#x23;2 above can include: manual therapy and therapeutic exercise procedures including but not limited to: cupping, myofascial release, and therapeutic exercises.\r\n\r\n*Additional acupuncture care beyond this trial must provide documentation of: Objective measures demonstrating the extent of meaningful clinical improvement to date; AND Rationale for the additional treatment requested (e.g. to reach further durable improvement, or for ongoing pain management); AND Any further information supporting the need for additional care \r\n*Additional consultations needed relevant to the patient complaint/condition require VA review and approval."</p>
<p>}</p>
<p>}</p>
<p>]</p>
<p>}</p></th>
</tr>
</thead>
<tbody>
</tbody>
</table>