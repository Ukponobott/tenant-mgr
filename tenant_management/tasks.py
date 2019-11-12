# Copyright (c) 2013, Frappe
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.utils import date_diff, nowdate, formatdate, add_days

def daily():
	rent_period = frappe.db.get_value("Tenant Management Settings", None, "rent_period")

	overdue = get_overdue(rent_period)

	for member, items in overdue.iteritems():
		content = """<h2>Following Items are Overdue</h2>
		<p>Please return them as soon as possible</p><ol>"""

		for i in items:
			content += "<li>{0} ({1}) due on {2}</li>".format(i.property_name, i.property,
				formatdate(add_days(i.transaction_date, rent_period)))

		content += "</ol>"

		frappe.send(recipients=[frappe.db.get_value("Authorised Tenant", tenant, "email_id")],
			sender="test@example.com", subject="Property Rent Overdue", msg=content, bulk=True)

def get_overdue(rent_period):
	# check for overdue articles
	today = nowdate()

	overdue_by_member = {}
	properties_transacted = []

	for d in frappe.db.sql("""select name, property, property_name, tenant, first_name, last_name
		from `tabRenting Transaction` order by transaction_date desc, modified desc""", as_dict=1):

		if d.property in properties_transacted:
			continue

		if d.transaction_type=="Issue" and date_diff(today, d.transaction_date) > rent_period:
			overdue_by_member.setdefault(d.tenant, [])
			overdue_by_member[d.tenant].append(d)

		properties_transacted.append(d.property)
