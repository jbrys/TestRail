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


def get_cases(project_id, suite_id, section_id=None):
    """Returns a list of test cases for a test suite."""
    id = project_id
    params = {'suite_id': suite_id}
    if section_id is not None:
        params = {'suite_id': suite_id, 'section_id': section_id}

    req = requests.get(settings.URL + 'get_cases/' + str(id),
                       params=params,
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


def add_case(section_id, **kwargs):
    """Creates a new test case."""
    fields = {}

    for key in kwargs:
        fields[key] = kwargs[key]

    req = requests.post(settings.URL + 'add_case/' + str(section_id),
                        auth=(settings.USR, settings.PWD), headers=headers,
                        data=json.dumps(fields))
    return req.json()


def update_case(id, **kwargs):
    """Updates an existing test case (partial updates are supported, i.e. you can submit and update specific
    fields only). This method supports the same POST fields as add_case."""
    fields = {}

    for key in kwargs:
        fields[key] = kwargs[key]

    req = requests.post(settings.URL + 'update_case/' + str(id),
                        auth=(settings.USR, settings.PWD), headers=headers,
                        data=json.dumps(fields))

    return req


def delete_case(id):
    """Deletes and existing test case."""

    req = requests.post(settings.URL + 'delete_case/' + str(id),
                        auth=(settings.USR, settings.PWD), headers=headers)
    return req.json()


def get_case_fields():
    """Returns a list of available test case custom fields."""

    req = requests.get(settings.URL + 'get_case_fields/',
                       auth=(settings.USR, settings.PWD), headers=headers)
    return req.json()


def get_case_types():
    """Use the following API methods to request details about case type"""
    req = requests.get(settings.URL + 'get_case_types/',
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


def add_milestone(project_id, **kwargs):
    """Creates a new milestone."""
    fields = {}

    for key in kwargs:
        fields[key] = kwargs[key]

    req = requests.post(settings.URL + 'add_milestone/' + str(project_id),
                        auth=(settings.USR, settings.PWD), headers=headers,
                        data=json.dumps(fields))

    return req.json()


def update_milestone(milestone_id, **kwargs):
    """Updates an existing milestone (partial updates are supported, i.e. you can submit and update specific
    fields only)."""
    fields = {}

    for key in kwargs:
        fields[key] = kwargs[key]

    req = requests.post(settings.URL + 'update_milestone/' + str(milestone_id),
                        auth=(settings.USR, settings.PWD), headers=headers,
                        data=json.dumps(fields))

    return req.json()


def delete_milestone(milestone_id):
    """Deletes an existing milestone"""
    req = requests.post(settings.URL + 'delete_milestone/' + str(milestone_id),
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

def add_project(**kwargs):
    """Creates a new project (administrator status required)"""
    fields = {}

    for key in kwargs:
        fields[key] = kwargs[key]

    req = requests.post(settings.URL + 'add_project/',
                        auth=(settings.USR, settings.PWD), headers=headers,
                        data=json.dumps(fields))

    return req.json()

def update_project(project_id, **kwargs):
    """Updates an existing project (partial updates are supported, i.e. you can submit and
    update specific fields only)."""
    fields = {}

    for key in kwargs:
        fields[key] = kwargs[key]

    req = requests.post(settings.URL + 'update_project/' + str(project_id),
                        auth=(settings.USR, settings.PWD), headers=headers,
                        data=json.dumps(fields))

    return req.json()

def delete_project(project_id):
    """Deletes an existing project."""

    req = requests.post(settings.URL + 'delete_project/' + str(project_id),
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


def add_plan(project_id, **kwargs):
    """Creates a new test plan"""
    fields = {}

    for key in kwargs:
        fields[key] = kwargs[key]

    req = requests.post(settings.URL + 'add_plan/' + str(project_id),
                        auth=(settings.USR, settings.PWD), headers=headers,
                        data=json.dumps(fields))

    return req.json()


def add_plan_entry(plan_id, **kwargs):
    """Creates a new test run for a test plan"""
    fields = {}

    for key in kwargs:
        fields[key] = kwargs[key]

    req = requests.post(settings.URL + 'add_plan/' + str(plan_id),
                        auth=(settings.USR, settings.PWD), headers=headers,
                        data=json.dumps(fields))

    return req.json()


def update_plan_entry(plan_id, entry_id, **kwargs):
    """Updates an existing test run in a plan (partial updates are supported, i.e. you can submit and update
    specific fields only)."""
    fields = {}

    for key in kwargs:
        fields[key] = kwargs[key]

    req = requests.post(settings.URL + 'update_plan_entry/' + '%d/%d' % (plan_id, entry_id),
                        auth=(settings.USR, settings.PWD), headers=headers,
                        data=json.dumps(fields))

    return req.json()


def close_plan(plan_id):
    """Closes an existing test plan and archives its test runs & results"""

    req = requests.post(settings.URL + 'close_plan/' + str(plan_id),
                        auth=(settings.USR, settings.PWD), headers=headers)

    return req.json()


def delete_plan(plan_id):
    """Deletes an existing test plan"""

    req = requests.post(settings.URL + 'delete_plan/' + str(plan_id),
                        auth=(settings.USR, settings.PWD), headers=headers)

    return req.json()


def delete_plan_entry(plan_id, entry_id):
    """Deletes an existing test run from a plan"""

    req = requests.post(settings.URL + 'delete_plan_entry/' + '%d/%d' % [plan_id, entry_id],
                        auth=(settings.USR, settings.PWD), headers=headers)

    return req.json()


def get_priorities():
    """Returns a list of available priorities."""

    req = requests.get(settings.URL + 'get_priorities/',
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

def add_run(project_id, **kwargs):
    """Creates a new test run."""
    fields = {}

    for key in kwargs:
        fields[key] = kwargs[key]

    req = requests.post(settings.URL + 'add_run/' + str(project_id),
                        auth=(settings.USR, settings.PWD), headers=headers,
                        data=json.dumps(fields))

    return req

def update_run(run_id, **kwargs):
    """Updates an existing test run (partial updates are supported, i.e. you can submit
    and update specific fields only)."""
    fields = {}

    for key in kwargs:
        fields[key] = kwargs[key]

    req = requests.post(settings.URL + 'update_run/' + str(run_id),
                        auth=(settings.USR, settings.PWD), headers=headers,
                        data=json.dumps(fields))

    return req

def close_run(run_id):
    """Closes an existing test run and archives its tests & results"""
    req = requests.post(settings.URL + 'close_run/' + str(run_id),
                        auth=(settings.USR, settings.PWD), headers=headers)

    return req.json

def delete_run(run_id):
    """Closes an existing test run and archives its tests & results"""
    req = requests.post(settings.URL + 'delete_run/' + str(run_id),
                        auth=(settings.USR, settings.PWD), headers=headers)

    return req.json

def get_section(section_id):
    """Returns an existing section."""
    req = requests.get(settings.URL + 'get_section/' + str(section_id),
                       auth=(settings.USR, settings.PWD), headers=headers)
    return req.json()


def get_sections(project_id, suite_id):
    """Returns a list of sections for a project and test suite."""
    req = requests.get(settings.URL + 'get_sections/%d&suite_id=%d' % (project_id, suite_id,),
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
    req = requests.get(settings.URL + 'get_results_for_case/%d/%d' % (run_id, case_id),
                       auth=(settings.USR, settings.PWD), headers=headers)
    return req.json()

def get_result_fields():
    """Returns a list of available test result custom fields"""
    req = requests.get(settings.URL + 'get_result_fields/',
                       auth=(settings.USR, settings.PWD), headers=headers)

    return req.json()

def add_result(test_id, **kwargs):
    """Creates a new test result."""
    fields = {}

    for key in kwargs:
        fields[key] = kwargs[key]

    req = requests.post(settings.URL + 'add_result/' + str(test_id),
                        auth=(settings.USR, settings.PWD), headers=headers,
                        data=json.dumps(fields))

    return req

def add_result_for_case(run_id, case_id, **kwargs):
    """Creates a new test result for a test run and case combination"""
    fields = {}

    for key in kwargs:
        fields[key] = kwargs[key]

    req = requests.post(settings.URL + 'add_result_for_case/%d/%d' % (run_id, case_id),
                        auth=(settings.USR, settings.PWD), headers=headers)

    return req

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