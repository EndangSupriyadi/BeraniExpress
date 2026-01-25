{
    "name": "Courier Core",
    "version": "1.0",
    "summary": "Courier Incident Log",
    "depends": ["base"],
    "data": [
        "security/ir.model.access.csv",
        "views/menu.xml",
        "views/courier_customer_views.xml",
        "views/courier_shipment_views.xml",
        "views/courier_incident_views.xml",
    ],
    "installable": True,
    "application": True,
}