# Copyright (c) 2023, svr and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class task_approval(Document):
	# pass

	def validate(self):
	
		doc = frappe.get_doc("task_queue",f"{self.task_name}")
		for each in doc.get("materials_required"):
			self.append("materials_required",{
			"name_of_the_material":f"{each.name_of_the_material}",
			"quantity":f"{each.quantity}",
			"units" : f"{each.units}"
			})

	