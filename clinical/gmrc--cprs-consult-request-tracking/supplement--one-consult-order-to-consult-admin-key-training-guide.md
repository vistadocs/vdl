---
title: One Consult - Order to Consult - Admin Key Training Guide
doc_type: TRG
doc_label: Training Guide
doc_layer: plain
doc_subject: One Consult - Order to Consult - Admin Key
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
menu_options: 0
description: 
audience: 
keywords: 
  - consult
  - admin
  - span
  - order
  - guide
  - training
  - class
  - anchor
  - figure
  - cprs
page_count: 0
word_count: 1293
section_count: 4
table_count: 3
figure_count: 0
appendix_count: 0
has_toc: False
is_stub: False
pub_date: December 2018
revision_count: 1
revision_newest: 12/07/2018
revision_oldest: 12/07/2018
docx_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Consult_Request_Tracking/oc_adminkey_tg.docx"
pdf_url: "https://www.va.gov/vdl/documents/Clinical/CPRS-Consult_Request_Tracking/oc_adminkey_tg.pdf"
app_url: "https://www.va.gov/vdl/application.asp?appid=62"
---

---
title: |
  <span id="_Toc205632711" class="anchor"></span>One Consult - Order to Consult – Admin Key

  Software Version 1.0.03

  Training Guide
---

![](one-consult-order-to-consult-admin-key-training-guide/001.png)

December 2018

Office of Information and Technology (OI&T)

Revision History

> **NOTE:** The revision history cycle begins once changes or enhancements are requested after the document has been baselined.

| Date       | Revision | Description              | Author   |
|------------|----------|--------------------------|----------|
| 12/07/2018 | 1.0      | Initial Document Release | AbleVets |

Table used for formatting, only.Revision History, including date of changes, version number, description of change, and author of change.

Table of Contents

List of Figures

# Introduction


<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

## Table of Contents

- [Introduction](#introduction)
  - [OR ADMIN RBP TO CC Only Consult Ordering](#or-admin-rbp-to-cc-only-consult-ordering)
  - [Discontinuing a COMMUNITY CARE -ADMIN or -DS Consult Immediately After Creation](#discontinuing-a-community-care-admin-or-ds-consult-immediately-after-creation)
    - [Discontinue from the Consults Tab](#discontinue-from-the-consults-tab)
  - [Admin Key and OREMAS Key Ordering](#admin-key-and-oremas-key-ordering)
This guide provides instructions on how to use the new OR ADMIN RBP TO CC security key ordering capabilities for CPRS users that currently hold the OREMAS key. The OREMAS key currently enables the CPRS user to place orders on behalf of a clinician with and order action of Signature on Chart. With the new OR ADMIN RBP TO CC security key release, the CPRS users will now have both OR ADMIN RBP TO CC and OREMAS key rights, which will enable them to enter orders with Signature on Chart and Administratively Released by Policy release options. Users with both keys will see a different behavior in CPRS workflow that is documented below. This workflow is not optimal, but without some underlying changes in CPRS, it cannot currently be avoided so this guide will provide instructions on how to work within this current workflow to place the COMMUNITY CARE -ADMIN or -DS consult orders that will be automatically release to the office of Community Care.

## OR ADMIN RBP TO CC Only Consult Ordering

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

To place orders using the Admin Key, the user should hold the OR ADMIN RBP TO CC security key (the Admin Key).

The CPRS user will follow the steps listed below to place orders with the OR ADMIN RBP TO CC only:

1.  Log in to CPRS.

<span id="_Toc531609355" class="anchor"></span>Figure 1: User Logged Into CPRS

![](one-consult-order-to-consult-admin-key-training-guide/002.png)

2.  From the Orders or Consults tab, create a consult. The consult must have a Service/Specialty name that starts with COMMUNITY CARE and contains -ADMIN or -DS. The consult Reason for Request template will display.

<span id="_Toc531609356" class="anchor"></span>Figure 2: Template: COMMUNITY CARE-ADMIN- Window

![](one-consult-order-to-consult-admin-key-training-guide/003.png)

3.  Complete the template and click OK. The Order a Consult window displays with Reason for Request template data from the template.

<span id="_Toc531609357" class="anchor"></span>Figure 3: Order a Consult

![](one-consult-order-to-consult-admin-key-training-guide/004.png)

4.  Complete order dialog fields and then click Accept Order. The Consult displays in the window in a pending status.

<span id="_Toc531609358" class="anchor"></span>Figure 4: Consult: Pending Status

![](one-consult-order-to-consult-admin-key-training-guide/005.png)

5.  On the Orders tab the consult order is in pending status and is displayed in bold font.
1.  The bold font is not normal CPRS workflow behavior and needs to be updated.

<span id="_Toc531609359" class="anchor"></span>Figure 5: Order Displayed in Bold Font

![](one-consult-order-to-consult-admin-key-training-guide/006.png)

6.  Refresh the Orders tab.
7.  Select File\>Refresh Patient. The Review/Sign Changes dialog box displays.

<span id="_Toc531609360" class="anchor"></span>Figure 6: Review/Sign Changes

![](one-consult-order-to-consult-admin-key-training-guide/007.png)

2.  Select New Patient and Review/Sign Changes will also cause this popup to appear, as would exiting CPRS.
8.  Click OK. The Status column now displays as pending and is no longer bold font.

<span id="_Toc531609361" class="anchor"></span>Figure 7: Pending Status

![](one-consult-order-to-consult-admin-key-training-guide/008.png)

## Discontinuing a COMMUNITY CARE -ADMIN or -DS Consult Immediately After Creation

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

### Discontinue from the Consults Tab

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

|                                                                                                                                                                                                                                            |                                                                                                                    |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| ![](one-consult-order-to-consult-admin-key-training-guide/009.png) | Discontinuing a Consult should always be done on the Consults tab. NEVER ATTEMPT TO DO THIS ON THE ORDERS TAB. |

It is possible that a user may realize that they have made a mistake in creating a consult and will need to discontinue the consult. To discontinue from the Consults tab, follow the steps listed below:

1.  From the Consults tab in CPRS, click on the consult in the left-hand panel to select it.

<span id="_Toc531609362" class="anchor"></span>Figure 8: Selecting a consult

![](one-consult-order-to-consult-admin-key-training-guide/010.png)

2.  From the Action menu, select Consult Tracking, and then select Discontinue. The Discontinue Consult: Comments dialog box displays.

<span id="_Toc531609363" class="anchor"></span>Figure 9: Selecting Discontinue from the Action menu

![](one-consult-order-to-consult-admin-key-training-guide/011.png)

3.  In the Discontinue Consult dialog box, enter comments in the Comments field.

<span id="_Toc531609364" class="anchor"></span>Figure 10: Discontinue Consult: Comments Field

![](one-consult-order-to-consult-admin-key-training-guide/012.png)

4.  Click OK. The consult detail now shows that the consult has been discontinued.

<span id="_Toc531609365" class="anchor"></span>Figure 11: Discontinued Consult

![](one-consult-order-to-consult-admin-key-training-guide/013.png)

## Admin Key and OREMAS Key Ordering

<!-- back-to-toc -->[↑ Table of Contents](#table-of-contents)

The CPRS user will follow the steps listed below to place orders with the OR ADMIN RBP TO CC Key and OREMAS Key:

1.  Log in to CPRS.

<span id="_Toc531609366" class="anchor"></span>Figure 12: User Logged Into CPRS

![](one-consult-order-to-consult-admin-key-training-guide/014.png)

2.  From the Orders or Consults tab, create a consult. The consult must have a Service/Specialty name that starts with COMMUNITY CARE and contains -ADMIN or -DS. The consult Reason for Request template will appear:

<span id="_Toc531609367" class="anchor"></span>Figure 13: COMMUNITY CARE-ADMIN- Window

![](one-consult-order-to-consult-admin-key-training-guide/015.png)

9.  Complete the template and click OK. The Order a Consult dialog window displays with Reason for Request template data from the template.

<span id="_Toc531609368" class="anchor"></span>Figure 14: Order a Consult

![](one-consult-order-to-consult-admin-key-training-guide/016.png)

10. Complete order dialog fields and then click Accept Order. The Consult displays in the window in a pending status.

<span id="_Toc531609369" class="anchor"></span>Figure 15: Consult

![](one-consult-order-to-consult-admin-key-training-guide/017.png)

11. On the Orders tab the consult order is in pending status and is displayed in bold font.
3.  The bold font is not normal CPRS workflow behavior and needs to be updated.

<span id="_Toc531609370" class="anchor"></span>Figure 16: Order Displayed in Bold Font

![](one-consult-order-to-consult-admin-key-training-guide/018.png)

12. Refresh the Orders tab.
13. Select File\>Refresh Patient. The Review/Sign Changes dialog box displays.

<span id="_Toc531609371" class="anchor"></span>Figure 17: Review/Sign Changes

![](one-consult-order-to-consult-admin-key-training-guide/019.png)

4.  Select New Patient and Review/Sign Changes will also cause this popup to appear, as would exiting CPRS.
5.  Since the Administrative User holds the OREMAS key, CPRS offers the option to sign the order or hold until it is signed.
14. Select the Signed on Chart radio button.
15. Click OK.

<span id="_Toc531609372" class="anchor"></span>Figure 18: Unable to Release Orders

![](one-consult-order-to-consult-admin-key-training-guide/020.png)

16. The user selects Hold until Signed.

<span id="_Toc531609373" class="anchor"></span>Figure 19: Hold until Signed Selected

![](one-consult-order-to-consult-admin-key-training-guide/021.png)

17. The user clicks OK. The order now shows Pending with no bold.

<span id="_Toc531609374" class="anchor"></span>Figure 20: Pending Status

![](one-consult-order-to-consult-admin-key-training-guide/022.png)