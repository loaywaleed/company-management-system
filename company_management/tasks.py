import frappe
from datetime import date


def daily():
    """Scheduled Job that handles days_employed field in Employee doctype"""
    employees = frappe.get_all("Employee", fields=["name", "hired_on", "days_employed"])
    for emp in employees:
        if emp.hired_on:
            days_employed = (date.today() - emp.hired_on).days
            frappe.db.set_value("Employee", emp.name, "days_employed", days_employed)
    frappe.db.commit()
