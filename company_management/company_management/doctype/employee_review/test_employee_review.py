from frappe.tests.utils import FrappeTestCase
import frappe


class TestEmployeeReview(FrappeTestCase):
    """Test for Employee Review doctype"""

    def setUp(self):
        """Setup before tests"""
        self.company = frappe.get_doc(
            {
                "doctype": "Company",
                "company_name": "Test Company",
            }
        ).insert()
        self.department = frappe.get_doc(
            {
                "doctype": "Department",
                "department_name": "Test Department",
                "company": self.company.name,
            }
        ).insert()
        self.employee = frappe.get_doc(
            {
                "doctype": "Employee",
                "employee_name": "Test Employee",
                "department": self.department.name,
                "company": self.company.name,
                "email_address": "test@example.com",
                "mobile_number": "1234567890",
                "address": "Test Address",
                "designation": "Test Designation",
            }
        ).insert()
        self.employee_review = frappe.get_doc(
            {
                "doctype": "Employee Review",
                "employee": self.employee.name,
                "status": "Pending Review",
                "review_date": "2021-06-01",
                "feedback": "Test Feedback",
                "manager_comments": "Test Manager Comments",
            }
        ).insert()
        self.addCleanup(self.cleanup_records)

    def test_create_employee_review(self):
        """Test that an employee review is created successfully"""
        self.assertTrue(self.employee_review.name)
        self.assertEqual(self.employee_review.status, "Pending Review")
        self.assertEqual(self.employee_review.feedback, "Test Feedback")
        self.assertEqual(self.employee_review.manager_comments, "Test Manager Comments")

    def test_check_employee(self):
        """Test that employee is set"""
        self.assertEqual(self.employee_review.employee, self.employee.name)

    def test_employee_review_delete(self):
        """Test that employee's review is deleted"""
        frappe.delete_doc("Employee Review", self.employee_review.name, force=True)
        self.assertFalse(frappe.db.exists("Employee Review", self.employee_review.name))

    def cleanup_records(self):
        """Cleanup after tests."""
        frappe.delete_doc("Employee", self.employee.name, force=True)
        frappe.delete_doc("Department", self.department.name, force=True)
        frappe.delete_doc("Company", self.company.name, force=True)
        frappe.delete_doc("Employee Review", self.employee_review.name, force=True)
