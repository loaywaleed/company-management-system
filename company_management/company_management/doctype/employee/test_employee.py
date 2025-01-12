from company_management.company_management.doctype import company
from frappe.tests.utils import FrappeTestCase
import frappe


class TestEmployee(FrappeTestCase):
    """Test for Employee doctype"""

    def setUp(self):
        """Setup before tests"""
        if frappe.db.exists("Company", "company_name"):
            self.company = frappe.get_doc("Company", "company_name")
        else:
            self.company = frappe.get_doc(
                {"doctype": "Company", "company_name": "Test Company"}
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
        self.addCleanup(self.cleanup_records)

    def test_create_employee(self):
        """Test that an employee is created successfully"""
        self.assertTrue(self.employee.name)
        self.assertEqual(self.employee.employee_name, "Test Employee")
        self.assertEqual(self.employee.email_address, "test@example.com")
        self.assertEqual(self.employee.mobile_number, "1234567890")
        self.assertEqual(self.employee.address, "Test Address")
        self.assertEqual(self.employee.designation, "Test Designation")

    def test_check_department(self):
        """Test that department is set"""
        self.assertEqual(self.employee.department, self.department.name)

    def test_check_company(self):
        """Test that company is set"""
        self.assertEqual(self.employee.company, self.company.name)

    def test_employee_update(self):
        """Test that department's number of employees field is updated after employee is created"""
        self.department.reload()
        self.assertEqual(self.department.number_of_employees, 1)

    def test_employee_delete(self):
        """Test that department's number of employees field is updated after employee is deleted"""
        frappe.delete_doc("Employee", self.employee.name, force=True)
        self.department.reload()
        self.assertEqual(self.department.number_of_employees, 0)

    def cleanup_records(self):
        """Cleanup after tests."""
        frappe.delete_doc("Employee", self.employee.name, force=True)
        frappe.delete_doc("Department", self.department.name, force=True)
        frappe.delete_doc("Company", self.company.name, force=True)
