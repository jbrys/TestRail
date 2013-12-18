"""api.py: api functions for testrail api wrapper"""
import requests

import settings

# Will error without setting the header
headers = {"Content-Type": "application/json"}

def get_case(id):
    """Returns an existing test case."""
    req = requests.get(settings.URL + 'get_case/' + str(id),
                       auth=(settings.USR, settings.PWD), headers=headers)
    return req.json()

def get_cases(id):
    """Returns a list of test cases for a test suite."""
    req = requests.get(settings.URL + 'get_cases/' + str(id),
                       auth=(settings.USR, settings.PWD), headers=headers)
    return req.json()

def get_milestone(id):
    """Returns an existing milestone."""
    req = requests.get(settings.URL + 'get_milestone/' + str(id),
                       auth=(settings.USR, settings.PWD), headers=headers)
    return req.json()

def get_milestones(id):
    """Returns a list of milestones for a project."""
    req = requests.get(settings.URL + 'get_milestones/' + str(id),
                       auth=(settings.USR, settings.PWD), headers=headers)
    return req.json()

def get_project(id):
    """Returns an existing project."""
    req = requests.get(settings.URL + 'get_project/' + str(id),
                       auth=(settings.USR, settings.PWD), headers=headers)
    return req.json()

def get_projects():
    """Returns a list of projects."""
    req = requests.get(settings.URL + 'get_projects/',
                       auth=(settings.USR, settings.PWD), headers=headers)
    return req.json()

def get_plan(id):
    """Returns an existing test plan."""
    req = requests.get(settings.URL + 'get_plan/' + str(id),
                       auth=(settings.USR, settings.PWD), headers=headers)
    return req.json()

def get_plans(id):
    """Returns a list of test plans for a project."""
    req = requests.get(settings.URL + 'get_plans/' + str(id),
                       auth=(settings.USR, settings.PWD), headers=headers)
    return req.json()

def get_run(id):
    """Returns an existing test run."""
    req = requests.get(settings.URL + 'get_run/' + str(id),
                       auth=(settings.USR, settings.PWD), headers=headers)
    return req.json()

def get_runs(id):
    """Returns a list of test runs for a project. Only returns those test runs that are not part of a test plan."""
    req = requests.get(settings.URL + 'get_runs/' + str(id),
                       auth=(settings.USR, settings.PWD), headers=headers)
    return req.json()

def get_section(id):
    """Returns an existing section."""
    req = requests.get(settings.URL + 'get_section/' + str(id),
                       auth=(settings.USR, settings.PWD), headers=headers)
    return req.json()

def get_sections(id):
    """Returns a list of sections for a project and test suite."""
    req = requests.get(settings.URL + 'get_sections/' + str(id),
                       auth=(settings.USR, settings.PWD), headers=headers)
    return req.json()

def get_test(id):
    """Returns an existing test."""
    req = requests.get(settings.URL + 'get_test/' + str(id),
                       auth=(settings.USR, settings.PWD), headers=headers)
    return req.json()

def get_tests(id):
    """Returns a list of tests for a test run."""
    req = requests.get(settings.URL + 'get_tests/' + str(id),
                       auth=(settings.USR, settings.PWD), headers=headers)
    return req.json()

def get_results(id):
    """Returns a list of test results for a test."""
    req = requests.get(settings.URL + 'get_results/' + str(id),
                       auth=(settings.USR, settings.PWD), headers=headers)
    return req.json()
