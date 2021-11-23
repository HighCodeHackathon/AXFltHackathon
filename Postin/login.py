import requests


POST_LOGIN_URL = 'https://hackathonwa.azurewebsites.net/login'

REQUEST_URL = 'https://hackathonwa.azurewebsites.net/home'


#username-input-name is the "name" tag associated with the username input field of the login form.
#password-input-name is the "name" tag associated with the password input field of the login form.
payload = {
    'serviceNumber1': '30000123',
    'password1': 'p@ssw0rd!'
}
with requests.Session() as session:
    post = session.post(POST_LOGIN_URL, data=payload)
    r = session.get(REQUEST_URL)
    print(r.text)