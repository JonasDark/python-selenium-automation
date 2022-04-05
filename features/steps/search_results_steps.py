from behave import given, when, then


@then('Verify {department} department selected')
def verify_correct_department(context, department):
    context.app.search_results_page.verify_correct_department(department)

