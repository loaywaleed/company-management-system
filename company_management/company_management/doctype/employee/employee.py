from company_management.company_management.doctype import department
from frappe.model.document import Document
import frappe


class Employee(Document):
    def after_insert(self):
        frappe.msgprint("Employee Updated")
        company = frappe.get_doc("Company", self.company)
        department = frappe.get_doc("Department", self.department)
        company.number_of_employees = frappe.db.count(
            "Employee", {"Company": self.company}
        )
        department.number_of_employees = frappe.db.count(
            "Employee", {"Department": self.department}
        )
        department.save(ignore_permissions=True)
        company.save(ignore_permissions=True)

    def on_trash(self):
        frappe.msgprint("Employee Deleted")
        company = frappe.get_doc("Company", self.company)
        department = frappe.get_doc("Department", self.department)
        company.number_of_employees = (
            frappe.db.count("Employee", {"Company": self.company}) - 1
        )
        department.number_of_employees = (
            frappe.db.count("Employee", {"Department": self.department}) - 1
        )
        department.save(ignore_permissions=True)
        company.save(ignore_permissions=True)
