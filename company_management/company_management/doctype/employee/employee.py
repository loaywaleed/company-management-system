from frappe.model.document import Document
import frappe


class Employee(Document):
    def after_insert(self):
        frappe.msgprint("Employee Updated")
        company = frappe.get_doc("Company", self.company)
        company.number_of_employees = frappe.db.count(
            "Employee", {"Company": self.company}
        )
        company.save(ignore_permissions=True)

    def on_trash(self):
        frappe.msgprint("Employee Deleted")
        company = frappe.get_doc("Company", self.company)
        company.number_of_employees = (
            frappe.db.count("Employee", {"Company": self.company}) - 1
        )
        company.save(ignore_permissions=True)
