from company_management.company_management.doctype import department
from frappe.model.document import Document
import frappe


class Project(Document):

    def after_insert(self):
        frappe.msgprint("Project Updated")
        company = frappe.get_doc("Company", self.company)
        department = frappe.get_doc("Department", self.department)
        company.number_of_projects = frappe.db.count(
            "Project", {"Company": self.company}
        )
        department.number_of_projects = frappe.db.count(
            "Project", {"Department": self.department}
        )
        department.save(ignore_permissions=True)
        company.save(ignore_permissions=True)

    def on_trash(self):
        frappe.msgprint("Project Deleted")
        company = frappe.get_doc("Company", self.company)
        department = frappe.get_doc("Department", self.department)
        company.number_of_projects = (
            frappe.db.count("Project", {"Company": self.company}) - 1
        )
        department.number_of_projects = (
            frappe.db.count("Project", {"Department": self.department}) - 1
        )
        department.save(ignore_permissions=True)
        company.save(ignore_permissions=True)
