# Copyright (c) 2024, Krutika Tatte and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document
from datetime import datetime
from frappe.utils import getdate



class Driver(Document):

	def validate(self):
		# print(self.first_name)
		self.set_full_name()
		self.calculate_age()


	def set_full_name(self):
		self.full_name = f"{self.first_name} {self.last_name}"

	def calculate_age(self):
		# today = datetime.today()
		# year = today.year OR
		year = getdate().year #this is best becoz we are using the func which already wriiten by frappe.(data.py file)
		dob = self.date_of_birth.split("-") #backend format of date id 1999-12-23 that's why we take dob[0]
		self.age = year - int(dob[0])

