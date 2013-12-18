"""tests.py: tests for testrail api wrapper"""
from nose.tools import with_setup

from src import api

def setup_func():
    pass

@with_setup(setup_func)
def test_get_case():
    """Test get_case function"""
    result = api.get_case(1)
    assert result != ''

@with_setup(setup_func)
def test_get_cases():
    """Test get_cases function"""
    result = api.get_cases(1)
    assert result != ''

@with_setup(setup_func)
def test_get_milestone():
    """Test get_milestone function"""
    result = api.get_milestone(1)
    assert result != ''

@with_setup(setup_func)
def test_get_milestones():
    """Test get_milestones function"""
    result = api.get_milestones(1)
    assert result != ''

@with_setup(setup_func)
def test_get_project():
    """Test get_project function"""
    result = api.get_project(1)
    assert result != ''

@with_setup(setup_func)
def test_get_projects():
    """Test get_projects function"""
    result = api.get_projects()
    assert result != ''

@with_setup(setup_func)
def test_get_plan():
    """Test get_plan function"""
    result = api.get_plan(1)
    assert result != ''

@with_setup(setup_func)
def test_get_plans():
    """Test get_plans function"""
    result = api.get_plans(1)
    assert result != ''

@with_setup(setup_func)
def test_get_run():
    """Test get_run function"""
    result = api.get_run(1)
    assert result != ''

@with_setup(setup_func)
def test_get_runs():
    """Test get_runs function"""
    result = api.get_runs(1)
    assert result != ''

@with_setup(setup_func)
def test_get_section():
    """Test get_section function"""
    result = api.get_section(1)
    assert result != ''

@with_setup(setup_func)
def test_get_sections():
    """Test get_sections function"""
    result = api.get_sections(1)
    assert result != ''

@with_setup(setup_func)
def test_get_test():
    """Test get_test function"""
    result = api.get_test(1)
    assert result != ''

@with_setup(setup_func)
def test_get_tests():
    """Test get_tests function"""
    result = api.get_tests(1)
    assert result != ''

@with_setup(setup_func)
def test_get_results():
    """Test get_results function"""
    result = api.get_results(1)
    assert result != ''
