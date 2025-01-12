from frappe.tests.utils import FrappeTestCase
import frappe


class TestDepartment(FrappeTestCase):
    """Test for Department doctype"""

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
        self.addCleanup(self.cleanup_records)

    def test_create_department(self):
        """Test that a department is created successfully"""
        self.assertTrue(self.department.name)
        self.assertEqual(self.department.department_name, "Test Department")

    def test_check_company(self):
        """Test that company is set"""
        self.assertEqual(self.department.company, self.company.name)

    def test_department_default_values(self):
        """Test that default values are set"""
        self.assertEqual(self.department.number_of_employees, 0)
        self.assertEqual(self.department.number_of_projects, 0)

    def test_duplicate_department(self):
        """Test for duplicates"""
        with self.assertRaises(frappe.exceptions.DuplicateEntryError):
            frappe.get_doc(
                {
                    "doctype": "Department",
                    "department_name": "Test Department",
                    "company": self.company.name,
                }
            ).insert()

    def test_department_update(self):
        """Test that company's number of departments field is updated after department is created"""
        self.company.reload()
        self.assertEqual(self.company.number_of_departments, 1)

    def test_department_delete(self):
        """Test that company's number of departments field is updated after department is deleted"""
        frappe.delete_doc("Department", self.department.name, force=True)
        self.company.reload()
        self.assertEqual(self.company.number_of_departments, 0)

    def cleanup_records(self):
        """Cleanup after tests."""
        frappe.db.delete("Employee", {"department": self.department.name})
        frappe.db.delete("Project", {"department": self.department.name})
        frappe.delete_doc("Department", self.department.name, force=True)
        frappe.delete_doc("Company", self.company.name, force=True)
