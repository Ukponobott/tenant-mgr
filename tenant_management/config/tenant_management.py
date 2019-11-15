from __future__ import unicode_literals
from frappe import _

def get_data():
    return [
      {
        "label":_("Tenant Manager"),
        "icon": "octicon octicon-briefcase",
        "items": [
            {
              "type": "doctype",
              "name": "Property",
              "label": _("Property"),
              "description": _("Properties which Tenants rent."),
            },
	    {
              "type": "doctype",
              "name": "Agent",
              "label": _("Agent"),
              "description": _("Agents that manage properites."),
            },
	    {
              "type": "doctype",
              "name": "Owner",
              "label": _("Owner"),
              "description": _("Owners that own properites."),
            },
            
            {
              "type": "doctype",
              "name": "Authorised Tenant",
              "label": _("Authorised Tenant"),
              "description": _("People who have made payment and rented a property"),
            },
            {
              "type": "doctype",
              "name": "Renting Transaction",
              "label": _("Renting Transaction"),
              "description": _("New rents and Rent renewals are the transactions taking place."),
            }
          ]
      }
  ]

