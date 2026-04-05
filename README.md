# IT Inventory Management — Odoo 17 Custom Module

A domain-specific inventory management module built on top of Odoo 17's stock and purchase modules, designed for companies managing IT equipment such as CCTV cameras, access points, network switches, and routers.

---

## Features

### IT Equipment Registry
- Custom product fields: Device Type, Serial Number, Warranty Expiry Date, Device Location, Minimum Stock Quantity
- Pre-loaded IT equipment products: CCTV Camera, Access Point, Network Switch, Router
- Dedicated IT Equipment category

### Smart Stock IN / Stock OUT Forms
- Stock IN form includes: Received By, Purchase Reference / Invoice No, Remarks
- Stock OUT form includes: Issued To (Department), Issued By, Purpose (Installation / Replacement / Repair / New Setup), Remarks
- Each form shows only relevant fields based on operation type

### Low Stock Alert
- Automatic red warning on product form when current stock falls below minimum quantity
- Visual indicator on Stock Level Report PDF (LOW / OK status)

### Reorder Wizard
- One-click wizard to create a Purchase Order when stock is low
- Select product, quantity, and vendor — Purchase Order generated instantly

### Stock Movement History
- Complete audit trail of every stock movement
- Columns: Date, Product, From Location, To Location, Quantity, Reference No, Type
- Filtered to show only IT equipment movements

### QWeb PDF Reports
- **Stock Level Report** — current stock of all IT equipment with low stock status
- **Stock Movement History Report** — full movement history with locations and references

### Purchase Orders Integration
- Direct link to Purchase Orders from IT Inventory menu
- Purchase Orders created via Reorder Wizard appear here

---

## Module Structure

```
it_inventory/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   ├── product_template.py       # IT fields + low stock alert compute
│   └── stock_picking.py          # Stock IN / Stock OUT custom fields
├── wizard/
│   ├── __init__.py
│   └── reorder_wizard.py         # Reorder wizard → Purchase Order
├── views/
│   ├── product_views.xml         # IT Equipment Info tab + stock report tree
│   ├── stock_picking_views.xml   # Stock IN/OUT form fields + movement history tree
│   ├── reorder_wizard_views.xml  # Reorder wizard form
│   └── menu_views.xml            # All menus and window actions
├── data/
│   └── product_category_data.xml # Pre-loaded IT category and products
├── security/
│   └── ir.model.access.csv
├── reports/
│   ├── stock_report_action.xml   # Report actions and menu actions
│   └── stock_report_template.xml # QWeb PDF templates
└── static/
    └── description/
        └── icon.png
```

---

## Models Used

| Model | Type | Purpose |
|---|---|---|
| `product.template` | Inherited | Added IT-specific fields |
| `stock.picking` | Inherited | Added Stock IN / OUT custom fields |
| `it.reorder.wizard` | New TransientModel | Reorder wizard |

---

## Dependencies

```python
'depends': ['stock', 'purchase', 'product']
```

| Module | Purpose |
|---|---|
| `stock` | Stock IN / OUT, warehouses, movement history |
| `purchase` | Purchase Order creation via wizard |
| `product` | Product template inheritance |


## How to Use

### Stock IN
1. IT Inventory → Stock In (Receipts) → New
2. Fill Receive From, Received By, Purchase Reference
3. Add product line → Validate

### Stock OUT
1. IT Inventory → Stock Out (Deliveries) → New
2. Fill Issued To (Department), Issued By, Purpose
3. Add product line → Validate

### Reorder Equipment
1. IT Inventory → Reorder Equipment
2. Select product, quantity, vendor
3. Click Create Purchase Order

### Reports
1. IT Inventory → Stock Level Report → Select products → Print → IT Stock Report
2. IT Inventory → Movement History → Select records → Print → IT Stock Movement History

---

## Technical Highlights

- Model inheritance using `_inherit` on `product.template` and `stock.picking`
- Computed field `it_low_stock_alert` using `@api.depends`
- Odoo 17 syntax — `invisible=` used instead of deprecated `attrs`
- Dedicated Stock IN / OUT actions with `domain` and `context` for operation type filtering
- QWeb PDF reports with dynamic LOW/OK status indicators
- TransientModel wizard for Purchase Order creation

---

## Author

**Laiba** — Odoo 17 Developer  
BSCS Student — Virtual University of Pakistan  
