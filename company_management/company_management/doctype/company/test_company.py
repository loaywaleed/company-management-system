from frappe.tests.utils import FrappeTestCase
import frappe


class TestCompany(FrappeTestCase):
    def setUp(self):
        """Setup before tests"""
        self.company = frappe.get_doc(
            {"doctype": "Company", "company_name": "Test Company"}
        ).insert()
        self.addCleanup(self.cleanup_records)

    def test_create_company(self):
        """Test that a company is created successfully"""
        self.assertTrue(self.company.name)
        self.assertEqual(self.company.company_name, "Test Company")
        self.addCleanup(self.cleanup_records)

    def test_company_default_values(self):
        """Test that default values are set"""
        self.assertEqual(self.company.number_of_departments, 0)
        self.assertEqual(self.company.number_of_employees, 0)
        self.assertEqual(self.company.number_of_projects, 0)

    def test_duplicate_company(self):
        """Test for duplicates"""
        with self.assertRaises(frappe.exceptions.DuplicateEntryError):
            frappe.get_doc(
                {
                    "doctype": "Company",
                    "company_name": "Test Company",
                }
            ).insert()

    def cleanup_records(self):
        """Cleanup after tests."""
        frappe.db.delete("Department", {"company": self.company.name})
        frappe.db.delete("Employee", {"company": self.company.name})
        frappe.db.delete("Project", {"company": self.company.name})
        frappe.delete_doc("Company", self.company.name, force=True)
