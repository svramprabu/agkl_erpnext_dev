# Copyright (c) 2023, svr and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
# Python program to Scan and Read a QR code 
from qrtools import QR 
 


class facilitator_attendance(Document):
	# pass
	@frappe.whitelist()
	def frm_call(self):
		frappe.msgprint(f"{self.qr_scan}")
		# doc = frappe.make_get_request(f"http://api.qrserver.com/v1/read-qr-code/?fileurl=\
		# 					{self.qr_scan}")
		# frappe.msgprint(f"{doc}")
		my_QR = QR(filename = f"{self.qr_scan}") 

# decodes the QR code and returns True if successful 
		my_QR.decode() 

# prints the data 
		frappe.msgprint (my_QR.data)