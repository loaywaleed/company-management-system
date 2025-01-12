<br />
<div align="center">
  <h3 align="center">Company Management System</h3>

  <p align="center">
    Company Management System
    <br />
    <a href="https://www.linkedin.com/in/loaywali/">Report Bug</a>
    ·
    <a href="https://www.linkedin.com/in/loaywali/">Request Feature</a>
  </p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#Running-tests">Tests</a></li>
    <li><a href="#Project-requirements-checklist">Requirements checklist</a></li>
    <li><a href="#Coding-Standard">Coding Standard</a></li>
    <li><a href="#Documentation">API documentation</a></li>
  </ol>
</details>


## About The Project

Company Management System used to manage employees, departments, companies, projects as well as handling workflows such as employee performance review.


### Built With

- Python
- Framework: Frappe


## Getting Started

First Clone the repo or download the zip file.

### Prerequisites

Make sure you have installed all frappe dependencies. You can find the Frappe framework and required dependencies in [Here](https://github.com/frappe/frappe).

### Installation


1. Setup frappe bench (if you don't have one)
   ```sh
   bench init frappe-bench --frappe-branch version-15
   ```
2. Get the app using:
   ```sh
   bench get-app company_management https://github.com/loaywaleed/company-management-systems.git
   ```
3. Create new site if you don't have one
    ```sh
    bench new-site site.local
    ```
4. Run migrate command
    ```sh
    bench migrate
5. Install the app to your site:
    ```sh
    bench --site site.local install-app company_management
    ```
6. Add your site to host or make the site the default one by using:
    ```sh
    bench use site.local
    ```
7. Export fixtures for workflows and scheduled tasks
    ```sh
    bench export-fixtures
    ```
8. Run the app
    ```sh
    bench start
    ```


### Running Tests
```sh
bench --site site.local run-tests --app company_management
```


## Approach

### Tech

#### Why did I choose Frappe?

I have used ERPNext before and familiar with Frappe so when I saw it gives an advantage, I decided to go for it to better maximize my chances. I definitely could have done it in Django (DRF) as well as I am well versed in it and have used it countless times and could do it too if needed.

#### How did I start out?

I have started by dividing the project into steps:
1. the first was **creating doctypes** for each model and any other necessary model needed to make the requirements work as efficient as I can.
2. THen I started testing the doctypes manually from the UI, to make sure everything is working flawlessly.
3. I moved on to **creating the roles and permissions necessary** (I choose HR/Admin, Manager, and Employee)
4. Then created the **workflow with the necessary states, doctype, transitions and permissions** and tested it on the UI to ensure it's working as expected.
5. Created **method controllers** to handle automatic calculations of things like number of exployees, number of departments etc.
6. Created a **scheduled task to handle "Days employeed field"** conditionally if the hired on field is set.
7. Created test cases for most of the app.
8. Finally, working on building the documentation.


#### Tricky parts?
I would say implementing the role based access control was tricky as well as replicating the app and ensuring it's easily installable.

## Project Requirements Checklist

## 1. Data Models

### User Accounts
- [x] Username, Email Address (Login ID), Role

### Company
- [x] Company Name
- [x] Auto-calculated fields: Departments count, Employees count, Projects count

### Department
- [x] Company (Select), Department Name
- [x] Auto-calculated fields: Employees count, Projects count

### Employee
- [x] Basic Info: Name, Email, Mobile, Address
- [x] Company & Department (Select fields)
- [x] Position & Employment Details: Designation, Hire Date, Days Employed (auto-calculated)

### Project
- [x] Basic Info: Name, Description, Start/End Dates
- [x] Relations: Company, Department, Assigned Employees (Multi-Select)


## 2. Employee Performance Review Cycle Workflow

### Stages
- [x] Pending Review
- [x] Review Scheduled
- [x] Feedback Provided
- [x] Under Approval
- [x] Review Approved
- [x] Review Rejected

### Stage Transitions
- [x] Pending Review → Review Scheduled (when review date confirmed)
- [x] Review Scheduled → Feedback Provided (when feedback recorded)
- [x] Feedback Provided → Under Approval (when submitted for review)
- [x] Under Approval → Review Approved (when approved by manager)
- [x] Under Approval → Review Rejected (when rejected by manager)
- [x] Review Rejected → Feedback Provided (when feedback updated)

## 3. Security & Permissions

### Role-Based Access Control
- [x] Implement different access levels (Admin, Manager, Employee)
- [x] Restrict data viewing and editing to authorized personnel
- [x] Implement secure authentication mechanism
- [x] Implement secure authorization mechanism

## 4. API Implementation

### Company Endpoints
- [x] GET List all companies
- [x] GET Retrieve single company

### Department Endpoints
- [x] GET List all departments
- [x] GET Retrieve single department

### Employee Endpoints
- [x] POST Create new employee
- [x] GET  List all employees
- [x] GET Retrieve single employee
- [x] PATCH Update employee (partial)
- [x] DELETE Delete employee
- [x] PUT Update employee (both partial and full update)

### Project Endpoints (Bonus)
- [x] POST Create new project
- [x] GET List all projects
- [x] GET Retrieve single project
- [x] PUT Update project
- [x] DELETE Delete project

### API Requirements
- [x] Implement secure data handling
- [x] Follow RESTful conventions
- [x] Create API documentation (in docs folder)
- [x] Document endpoints
- [ ] Document parameters (not all)
- [ ] Document expected responses (not all)

## 5. Testing

- [x] Unit Tests (Done)
- [x] Integration Tests (Not fully completed)

## 6. Logging
- [x] Mostly the built-in logging in Frappe



### Coding Standard
- Black code formatter


<p align="right">(<a href="#readme-top">back to top</a>)</p>


### Documentation
For detailed information, visit the documentation:
- [Postman API documentation](docs/BRAINWISE-API.json)
- [Demo](docs/DEMO.md)

