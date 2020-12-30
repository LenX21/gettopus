from behave import when, then

@then('Verify Login Form is opened')
def login_form_is_shown(context):
    context.app.login_form.verify_login_window_is_shown()