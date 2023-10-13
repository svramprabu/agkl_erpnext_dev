# Copyright (c) 2023, svr and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class task_approval(Document):
	# pass

	# def validate(self):
	@frappe.whitelist()
	def frm_call(self,msg):
	
		doc = frappe.get_doc("task_queue",f"{self.task_name}")
		# i=1
		
		frappe.msgprint(f"{self.get('materials_required')[0]}")
		for each in doc.get("materials_required"):
			self.append("materials_required",{
			# "No.":f"{i}",
			"name_of_the_material":f"{each.name_of_the_material}",
			"quantity":f"{each.quantity}",
			"units" : f"{each.units}"
			})
			# i+=1

	