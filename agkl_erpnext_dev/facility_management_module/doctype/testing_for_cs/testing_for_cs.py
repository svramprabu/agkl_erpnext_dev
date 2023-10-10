# Copyright (c) 2023, svr and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class testing_for_cs(Document):
	def _validate(self):
		# return super()._validate()
		frappe.msgprint(f"Hi everyone {self.test_data}")

	# pass
