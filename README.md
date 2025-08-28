
# Library Management with QWeb Reports

## Overview
This module is built using the **Odoo framework**. It manages library books and publishers, and provides functionality to generate custom **QWeb reports** for each book. Reports include detailed information such as **Title, Author, Publisher, ISBN, Published Date, and Availability**.

## Features
* Manage **Books** and **Publishers**.
* Book form view with fields:
  * Title
  * Author
  * Publisher
  * ISBN
  * Published Date
  * Availability (Available / On Loan)
* **Kanban and List views** for books with availability status.
  
* **QWeb Reports** for each book containing:
  * Publisher details
  * Author details
  * ISBN code
* Customization of existing records using **XPath**.
* Supports **external layouts** for report styling.
  
* Learned and implemented Odoo **QWeb directives**:
  * `t-name`
  * `t-call`
  * `t-foreach`
  * `web.html_container`

## Technical Details
* Created as a **custom Odoo module**.
* Views include:
  * **Form View** (Book details)
  * **Tree/List View** (All books with availability)
  * **Kanban View** (Book cards)
* Reports designed with **QWeb Templates**.
* Uses **XPath** to extend and customize existing invoices.


## Installation
1. Copy the module folder into your Odoo `addons` directory.
2. Restart the Odoo server.
3. Update the app list and install **Library Management**.


## Usage
* Navigate to **Library → Books**.
* Add new books with details such as title, author, publisher, ISBN, and availability.
* Generate QWeb reports directly from the form view or print menu.


## Future Improvements
* Integration with library members and borrowing history.
* Report export to PDF and Excel.
* Advanced search and filtering for books.

