from frappe.model.document import Document
import frappe


class Department(Document):
    def after_insert(self):
        frappe.msgprint("Department Updated")
        company = frappe.get_doc("Company", self.company)
        company.number_of_departments = frappe.db.count(
            "Department", {"Company": self.company}
        )
        company.save(ignore_permissions=True)

    def on_trash(self):
        frappe.msgprint("Department Deleted")
        company = frappe.get_doc("Company", self.company)
        company.number_of_departments = (
            frappe.db.count("Department", {"Company": self.company}) - 1
        )
        company.save(ignore_permissions=True)
