# -*- coding: utf-8 -*-
# Copyright (c) 2019, Ukpono Obott and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document

class RentingTransaction(Document):
	def validate(self):
		transaction = frappe.get_list("Renting Transaction",
			fields=["transaction_type", "transaction_date"],
			filters = {
				"property": self.property,
				"transaction_date": ("<=", self.transaction_date),
				#"name": ("!=", self.name)
			})
		if self.transaction_type == "New Rent":
			if transaction and transaction[0].transaction_type == "New Rent":
				frappe.throw(_("Property {0} {1} has not been recorded as returned since {2}".format(
					self.property, self.property_name, transaction[0].transaction_date
				)))
		else:
			if not transaction or transaction[0].transaction_type != "New Rent":
				frappe.throw(_("Cannot renew rent for Property not previously rented"))
