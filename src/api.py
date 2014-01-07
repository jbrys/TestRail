"""api.py: api functions for testrail api wrapper"""
import requests
import json
import settings

# Will error without setting the header
headers = {"Content-Type": "application/json"}

def pretty(payload):
    print json.dumps(payload, sort_keys=True,
                     indent=4, separators=(',', ':'))

def get_case(id):
    """Returns an existing test case."""
    req = requests.get(settings.URL + 'get_case/' + str(id),
                       auth=(settings.USR, settings.PWD), headers=headers)
    return req.json()

def get_cases(project_id, suite_id):
    """Returns a list of test cases for a test suite."""
    id = project_id

    req = requests.get(settings.URL + 'get_cases/' + str(id),
                       params={'suite_id': suite_id},
                       auth=(settings.USR, settings.PWD), headers=headers)
    return req.json()

# def get_cases(project_id, suite_id, section_id):
#     """Returns a list of test cases for a test suite."""
#     id = project_id
#
#     req = requests.get(settings.URL + 'get_cases/' + str(id),
#                        params={'suite_id': suite_id, 'section_id': section_id},
#                        auth=(settings.USR, settings.PWD), headers=headers)
#     return req.json()

def get_case_fields():
    """Returns a list of available test case custom fields."""

    req = requests.get(settings.URL + 'get_case_fields/',
                       auth=(settings.USR, settings.PWD), headers=headers)
    return req.json()

def add_case(fields, section_id):
    """Creates a new test case."""

    req = requests.post(settings.URL + 'add_case/' + str(section_id),
                        auth=(settings.USR, settings.PWD), headers=headers,
                        data=fields)
    return req.json()

def update_case(fields, id):
    """Updates an existing test case (partial updates are supported, i.e. you can submit and update specific
    fields only). This method supports the same POST fields as add_case."""

    req = requests.post(settings.URL + 'update_case/' + str(id),
                        auth=(settings.USR, settings.PWD), headers=headers,
                        data=fields)
    return req.json()

def delete_case(id):
    """Deletes and existing test case."""

    req = requests.post(settings.URL + 'delete_case/' + str(id),
                        auth=(settings.USR, settings.PWD), headers=headers)
    return req.json()

def get_milestone(milestone_id):
    """Returns an existing milestone."""
    req = requests.get(settings.URL + 'get_milestone/' + str(milestone_id),
                       auth=(settings.USR, settings.PWD), headers=headers)
    return req.json()

def get_milestones(project_id):
    """Returns a list of milestones for a project."""
    req = requests.get(settings.URL + 'get_milestones/' + str(project_id),
                       auth=(settings.USR, settings.PWD), headers=headers)
    return req.json()

def get_project(project_id):
    """Returns an existing project."""
    req = requests.get(settings.URL + 'get_project/' + str(project_id),
                       auth=(settings.USR, settings.PWD), headers=headers)
    return req.json()

def get_projects():
    """Returns a list of projects."""
    req = requests.get(settings.URL + 'get_projects/',
                       auth=(settings.USR, settings.PWD), headers=headers)
    return req.json()

def get_plan(plan_id):
    """Returns an existing test plan."""
    req = requests.get(settings.URL + 'get_plan/' + str(plan_id),
                       auth=(settings.USR, settings.PWD), headers=headers)
    return req.json()

def get_plans(project_id):
    """Returns a list of test plans for a project."""
    req = requests.get(settings.URL + 'get_plans/' + str(project_id),
                       auth=(settings.USR, settings.PWD), headers=headers)
    return req.json()

def get_run(run_id):
    """Returns an existing test run."""
    req = requests.get(settings.URL + 'get_run/' + str(run_id),
                       auth=(settings.USR, settings.PWD), headers=headers)
    return req.json()

def get_runs(project_id):
    """Returns a list of test runs for a project. Only returns those test runs that are not part of a test plan."""
    req = requests.get(settings.URL + 'get_runs/' + str(project_id),
                       auth=(settings.USR, settings.PWD), headers=headers)
    return req.json()

def get_section(section_id):
    """Returns an existing section."""
    req = requests.get(settings.URL + 'get_section/' + str(section_id),
                       auth=(settings.USR, settings.PWD), headers=headers)
    return req.json()

def get_sections(suite_id):
    """Returns a list of sections for a project and test suite."""
    req = requests.get(settings.URL + 'get_sections/' + str(suite_id),
                       auth=(settings.USR, settings.PWD), headers=headers)
    return req.json()

def get_test(test_id):
    """Returns an existing test."""
    req = requests.get(settings.URL + 'get_test/' + str(test_id),
                       auth=(settings.USR, settings.PWD), headers=headers)
    return req.json()

def get_tests(run_id):
    """Returns a list of tests for a test run."""
    req = requests.get(settings.URL + 'get_tests/' + str(run_id),
                       auth=(settings.USR, settings.PWD), headers=headers)
    return req.json()

def get_results(test_id):
    """Returns a list of test results for a test."""
    req = requests.get(settings.URL + 'get_results/' + str(test_id),
                       auth=(settings.USR, settings.PWD), headers=headers)
    return req.json()

def get_results_for_case(run_id, case_id):
    """Returns a list of test results for a test run and case combination"""
    req = requests.get(settings.URL + '/%d/%d' % (run_id, case_id),
                       auth=(settings.USR, settings.PWD), headers=headers)
    return req.json()

def get_suite(suite_id):
    """Returns an existing test suite."""
    req = requests.get(settings.URL + 'get_suite/' + str(suite_id),
                       auth=(settings.USR, settings.PWD), headers=headers)
    return req.json()

def get_suites(project_id):
    """Returns a list of test suites for a project"""
    req = requests.get(settings.URL + 'get_suites/' + str(project_id),
                       auth=(settings.USR, settings.PWD), headers=headers)

    return req.json()