import json
from behave import *
from application import USERS

@given('some users are in the system')
def step_impl(context):
    USERS.update({'jasonb': {'name': 'Jason Bourne'}})

@when(u'I retrieve the customer \'jasonb\'')
def step_impl(context):
    context.page = context.client.get('/users/{}'.format('jasonb'))
    assert context.page

@then(u'I should get a \'200\' response')
def step_impl(context):
    assert context.page.status_code is 200

@then(u'the following user details are returned')
def step_impl(context):
    # assert context.table[0].cells[0] in context.page.text
    assert "Jason Bourne" in context.page.text

#-----------------------------

@given('the user "marty" doesnt exist')
def step_impl(context):
    assert 'marty' not in USERS

@when('I store the custumer "marty"')
def step_impl(context):
    new_user = { 'username' : 'marty',
                 'name' : 'San Martin'
               }
    context.page = context.client.post('/users', data = new_user)
    assert context.page

@then(u'I should get a \'201\' response')
def step_impl(context):
    assert context.page.status_code is 201

@then('"marty" is in the database')
def step_impl(context):
    assert 'marty' in USERS

#-----------------------------

@given('the user "nikk" are in the system')
def step_impl(context):
    USERS.update({'nikk': {'name': 'Nikki Lauda'}})

@when('I update the customer "nikk"')
def step_impl(context):
    payload = { 'username': 'nikk',
                'name': 'Niki Lauda' 
              }
    context.page = context.client.put('/users/{}'.format('nikk'), data = payload)
    assert context.page

@then(u'the system performs the update')
def step_impl(context):
    assert context.page.status_code is 200

@then('the following user details are returned')
def step_impl(context):
    assert "Niki Lauda" in context.page.text

#-----------------------------

@given('the user "goncho" are in the system')
def step_impl(context):
    USERS.update({'goncho': {'name': 'Gonzalo Banzas'}})

@when('the system delete the customer "goncho"')
def step_impl(context, uname):
    context.page = context.client.delete('/users/{}'.format('goncho'))
    assert context.page

@then("the system informs the user was deleted")
def step_impl(context):
    assert context.page.status_code is 200

#-----------------------------

@given('that I have users are in the system')
def step_impl(context):
    USERS.update({'jasonb': {'name': 'Jason Bourne'}})
    USERS.update({'nikk': {'name': 'Niki Lauda'}})
    USERS.update({'goncho': {'name': 'Gonzalo Banzas'}})

@when("I receive a request to show the users list")
def step_impl(context):
    context.page = context.client.get('/users')
    assert context.page

@then("the following user data is returned")
def step_impl(context):
    for row in context.table:
        assert row[0] in context.page.text