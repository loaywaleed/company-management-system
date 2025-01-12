import frappe


def build_response(status, message=None, data=None):
    return {
        "status": status,
        "message": message,
        "data": data,
        "timestamp": frappe.utils.now_datetime(),
    }
