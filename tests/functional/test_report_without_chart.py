# coding=utf-8
"""Pull request with the report but without the chart feature tests."""

from pytest_bdd import (
    given,
    scenario,
    then,
    when,
)


@scenario('features/report_without_chart.feature', 'Partner submits report without any errors')
def test_partner_submits_report_without_any_errors():
    """Partner submits report without any errors."""


@given('the partner has created a report without any errors')
def the_partner_has_created_a_report_without_any_errors():
    """the partner has created a report without any errors."""
    raise NotImplementedError


@when('the partner sends the pull request with the report')
def the_partner_sends_the_pull_request_with_the_report():
    """the partner sends the pull request with the report."""
    raise NotImplementedError


@then('the index.yaml is updated with a new entry')
def the_indexyaml_is_updated_with_a_new_entry():
    """the index.yaml is updated with a new entry."""
    raise NotImplementedError


@then('the partner should see the pull request getting merged')
def the_partner_should_see_the_pull_request_getting_merged():
    """the partner should see the pull request getting merged."""
    raise NotImplementedError

