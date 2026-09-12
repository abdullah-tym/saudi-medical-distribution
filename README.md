# Saudi Medical Distribution Compliance

Odoo 19 custom module for managing regulatory and cold-chain compliance workflows in Saudi medical distribution operations.

## Overview

This module extends Odoo Inventory and Products with compliance-focused features designed around Saudi medical distribution requirements, including SFDA registration tracking, cold-chain monitoring, temperature compliance, and batch release status.

## Key Features

### SFDA Registration Tracking
- Store SFDA registration numbers on medical products.
- Track regulatory information directly from the product form.

### Cold-Chain Management
- Mark products that require cold-chain handling.
- Configure minimum and maximum temperature limits.
- Automatically evaluate recorded transit temperature against product requirements.

### Temperature Compliance
- Record transit temperature directly on incoming receipts.
- Automatically determine whether the shipment is within the configured temperature range.
- Record temperature deviation remarks for audit purposes.

### SFDA Batch Compliance
- Track batch/lot release status:
  - Pending SFDA Inspection
  - Approved for Distribution
  - Rejected / Recalled
- Store a regulatory certificate reference for each lot.

### Inventory Integration
- Extends standard Odoo Product and Inventory models.
- Integrates compliance information directly into existing Odoo workflows.

## Example Workflow

1. Create a medical product.
2. Enter its SFDA registration number.
3. Enable **Cold Chain Required**.
4. Configure the permitted temperature range.
5. Receive the product through Odoo Inventory.
6. Record the shipment transit temperature.
7. Odoo automatically evaluates cold-chain compliance.
8. Record any temperature deviation remarks.
9. Track the SFDA release status of the relevant batch/lot.

## Example

For a product requiring **2°C–8°C**:

| Recorded Temperature | Result |
|---|---|
| 5°C | Compliant |
| 2°C | Compliant |
| 8°C | Compliant |
| 10°C | Non-compliant |

## Technical Implementation

**Platform:** Odoo 19

**Languages & Technologies:**
- Python
- XML
- Odoo ORM
- Odoo Models
- Odoo Views
- PostgreSQL
- Git / GitHub

**Odoo Models Extended:**
- `product.template`
- `stock.picking`
- `stock.lot`

The module uses Odoo's inheritance mechanism to extend standard models while keeping the implementation modular and upgrade-friendly.

## Module Structure

```text
saudi_medical_distribution/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   ├── product_template.py
│   ├── stock_picking.py
│   └── stock_lot.py
├── views/
│   ├── product_view.xml
│   ├── stock_picking_view.xml
│   └── stock_lot_view.xml
├── security/
│   └── ir.model.access.csv
└── demo/
    └── demo.xml
```

## Installation

1. Copy the module into your Odoo custom addons directory.
2. Make sure the custom addons directory is included in Odoo's addons path.
3. Restart Odoo.
4. Update the Apps list.
5. Install **Saudi Medical Distribution Compliance**.

For development:

```bash
python odoo-bin -c odoo.conf -d your_database -u saudi_medical_distribution
```

## Testing

The module was tested against an Odoo 19 development environment.

Example cold-chain test:

- Product minimum temperature: **2°C**
- Product maximum temperature: **8°C**
- Recorded temperature: **5°C** → compliant
- Recorded temperature: **10°C** → non-compliant

The module also includes SFDA batch release status tracking and regulatory certificate references.

## Purpose

This project demonstrates practical Odoo development skills including:

- Custom module development
- Python ORM development
- Model inheritance
- XML view inheritance
- Onchange business logic
- Inventory workflow customization
- Regulatory/business-rule implementation
- PostgreSQL-backed Odoo development
- Git version control

## Author

**Abdullah Abutayyem**

Junior Odoo / Python Developer

[GitHub](https://github.com/abdullah-tym)