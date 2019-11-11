# -*- coding: utf-8 -*-
# Copyright (c) 2019, Ukpono Obott and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe
from frappe.model.document import Document

class Property(Document):
	def get_status(self):
		transaction = frappe.get_list("Renting Transaction",
			fields=["transaction_type"],
			filters = {
				"property": self.name}, order_by="transaction_date desc", limit_page_length=1)
		if (transaction and transaction[0].transaction_type == "New Rent"):
			return "Rented"
		else:
			return "Available" 
	def make_view(self):
		self.status = self.get_status()
