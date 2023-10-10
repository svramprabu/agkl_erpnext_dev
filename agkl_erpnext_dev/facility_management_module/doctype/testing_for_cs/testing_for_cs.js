// Copyright (c) 2023, svr and contributors
// For license information, please see license.txt

frappe.ui.form.on('testing_for_cs', {
	// refresh: function(frm) {
	refresh: function(frm)
	{
		frm.add_custom_button('button1',{},'button')
		frm.add_custom_button('button2',{},'button')
	}
	// }
});
