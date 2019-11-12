frappe.listview_settings['Properties'] = {
	add_fields: ["status"],
	get_indicator: function(doc) {
		return [__(doc.status), {
			"Available": "green",
			"Rented": "red",
		}[doc.status], "status,=," + doc.status];
	}
};
