# Copyright (c) 2023, svr and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class testing_doctype(Document):
	pass

	# def validate(self):
	# 	self.get_doc_item()

	# def get_doc_item(self):
	# 	doc = frappe.get_doc('task_queue',self.test_data)
	# 	for each_mat in doc.get("materials_required"):
	# 		frappe.msgprint(f"Need {each_mat.name_of_the_material} in {each_mat.quantity}")
	# x = 
	# def execute_function(*args,**kwargs):
    # """
    # 	This fonction will be executed when the Execute Action Button will be clicked
    # """
    	# print('Hello World')
		# frappe.msgprint("Executed")
    # The data is transmitted via keyword argument
    	# print(kwargs)
	# 	frappe.msgprint("Hiiiii")
        # frappe.msgprint("Hi from server side")

		# @frappe.whitelist()
		# # def _validate(self):
		# def frm_call(self,msg):
		# 	# return super()._validate()
		# 	# frappe.msgprint(f"Hi everyone {self.test_data}")
		# 	return "Work done"		

		# pass
		