from frappe.tests.utils import FrappeTestCase
import frappe


class TestProject(FrappeTestCase):
    def setUp(self):
        """Setup before tests"""

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
                "email_address": "test@example.com",
                "mobile_number": "1234567890",
                "address": "Test Address",
                "designation": "Test Designation",
                "department": self.department.name,
                "company": self.company.name,
            }
        ).insert()
        self.project = frappe.get_doc(
            {
                "doctype": "Project",
                "project_name": "Test Project",
                "company": self.company.name,
                "department": self.department.name,
                "description": "Test Description",
                "assigned_employees": [{"employee": self.employee.name}],
            }
        ).insert()
        self.addCleanup(self.cleanup_records)

    def test_create_project(self):
        """Test that a company is created successfully"""
        self.assertTrue(self.project.name)
        self.assertEqual(self.project.company, "Test Company")
        self.assertEqual(self.project.project_name, "Test Project")
        self.assertEqual(self.project.company, self.company.name)
        self.assertEqual(self.project.department, self.department.name)
        self.assertEqual(self.project.description, "Test Description")
        self.assertEqual(
            self.project.assigned_employees[0].employee, self.employee.name
        )

    def test_check_department(self):
        """Test that department is set"""
        self.assertEqual(self.project.department, self.department.name)

    def test_check_company(self):
        """Test that company is set"""
        self.assertEqual(self.project.company, self.company.name)

    def test_project_updates_company_and_department(self):
        """Test that creating a project updates company and department"""
        self.company.reload()
        self.department.reload()
        self.assertEqual(self.company.number_of_projects, 1)
        self.assertEqual(self.department.number_of_projects, 1)

    def test_delete_project(self):
        """Test that deleting a project updates company and department"""
        self.project.delete()
        self.company.reload()
        self.department.reload()
        self.assertEqual(self.company.number_of_projects, 0)
        self.assertEqual(self.department.number_of_projects, 0)

    def cleanup_records(self):
        """Cleanup after tests."""
        frappe.db.delete("Department", {"company": self.company.name})
        frappe.db.delete("Employee", {"company": self.company.name})
        frappe.db.delete("Project", {"company": self.company.name})
        frappe.delete_doc("Company", self.company.name, force=True)
