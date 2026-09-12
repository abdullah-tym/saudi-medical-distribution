# \# Saudi Medical Distribution Compliance

# 

# Odoo 19 custom module for managing regulatory and cold-chain compliance workflows in Saudi medical distribution operations.

# 

# \## Overview

# 

# This module extends Odoo Inventory and Products with compliance-focused features designed around Saudi medical distribution requirements, including SFDA registration tracking, cold-chain monitoring, temperature compliance, and batch release status.

# 

# \## Key Features

# 

# \- \*\*SFDA Registration Tracking\*\*

# &#x20; - Store SFDA registration numbers on medical products.

# &#x20; - Track regulatory information directly from the product form.

# 

# \- \*\*Cold-Chain Management\*\*

# &#x20; - Mark products that require cold-chain handling.

# &#x20; - Configure minimum and maximum temperature limits.

# &#x20; - Automatically evaluate recorded transit temperature against product requirements.

# 

# \- \*\*Temperature Compliance\*\*

# &#x20; - Record transit temperature directly on incoming receipts.

# &#x20; - Automatically determine whether the shipment is within the configured temperature range.

# &#x20; - Record temperature deviation remarks for audit purposes.

# 

# \- \*\*SFDA Batch Compliance\*\*

# &#x20; - Track batch/lot release status:

# &#x20;   - Pending SFDA Inspection

# &#x20;   - Approved for Distribution

# &#x20;   - Rejected / Recalled

# &#x20; - Store a regulatory certificate reference for each lot.

# 

# \- \*\*Inventory Integration\*\*

# &#x20; - Extends standard Odoo Product and Inventory models.

# &#x20; - Integrates compliance information directly into existing Odoo workflows.

# 

# \## Example Workflow

# 

# 1\. Create a medical product.

# 2\. Enter its SFDA registration number.

# 3\. Enable \*\*Cold Chain Required\*\*.

# 4\. Configure the permitted temperature range.

# 5\. Receive the product through Odoo Inventory.

# 6\. Record the shipment transit temperature.

# 7\. Odoo automatically evaluates cold-chain compliance.

# 8\. Record any temperature deviation remarks.

# 9\. Track the SFDA release status of the relevant batch/lot.

# 

# \### Example

# 

# For a product requiring \*\*2°C–8°C\*\*:

# 

# | Recorded Temperature | Result |

# |---|---|

# | 5°C | Compliant |

# | 2°C | Compliant |

# | 8°C | Compliant |

# | 10°C | Non-compliant |

# 

# \## Technical Implementation

# 

# \*\*Platform:\*\* Odoo 19

# 

# \*\*Languages \& Technologies:\*\*

# \- Python

# \- XML

# \- Odoo ORM

# \- Odoo Models

# \- Odoo Views

# \- PostgreSQL

# \- Git / GitHub

# 

# \*\*Odoo Models Extended:\*\*

# \- `product.template`

# \- `stock.picking`

# \- `stock.lot`

# 

# The module uses Odoo's inheritance mechanism to extend standard models while keeping the implementation modular and upgrade-friendly.

# 

# \## Module Structure

# 

# ```text

# saudi\_medical\_distribution/

# ├── \_\_init\_\_.py

# ├── \_\_manifest\_\_.py

# ├── models/

# │   ├── \_\_init\_\_.py

# │   ├── product\_template.py

# │   ├── stock\_picking.py

# │   └── stock\_lot.py

# ├── views/

# │   ├── product\_view.xml

# │   ├── stock\_picking\_view.xml

# │   └── stock\_lot\_view.xml

# ├── security/

# │   └── ir.model.access.csv

# └── demo/

# &#x20;   └── demo.xml

# Installation

# Copy the module into your Odoo custom addons directory.

# Make sure the custom addons directory is included in Odoo's addons path.

# Restart Odoo.

# Update the Apps list.

# Install Saudi Medical Distribution Compliance.

# 

# For development:

# 

# python odoo-bin -c odoo.conf -d your\_database -u saudi\_medical\_distribution

# Testing

# 

# The module was tested against an Odoo 19 development environment.

# 

# Example cold-chain test:

# 

# Product minimum temperature: 2°C

# Product maximum temperature: 8°C

# Recorded temperature: 5°C → compliant

# Recorded temperature: 10°C → non-compliant

# 

# The module also includes SFDA batch release status tracking and regulatory certificate references.

# 

# Purpose

# 

# This project demonstrates practical Odoo development skills including:

# 

# Custom module development

# Python ORM development

# Model inheritance

# XML view inheritance

# Onchange business logic

# Inventory workflow customization

# Regulatory/business-rule implementation

# PostgreSQL-backed Odoo development

# Git version control

# Author

# 

# Abdullah Abutayyem

# 

# Junior Odoo / Python Developer

# 

# GitHub: https://github.com/abdullah-tym

