import frappe
from frappe import _
from utils import build_response


@frappe.whitelist(allow_guest=False, methods=["PATCH"])
def patch_employee(employee_id, fields):
    """Update an employee record with the patch fields."""
    try:
        # Get the employee document
        employee = frappe.get_doc("Employee", employee_id)

        # Update the employee with the provided fields
        employee.update(fields)
        employee.save()

        return build_response(
            "success", message="Employee updated successfully", data=employee.name
        )
    except Exception as e:
        frappe.log_error(frappe.get_traceback(), "Failed to update employee")
        return build_response("error", message=str(e))
