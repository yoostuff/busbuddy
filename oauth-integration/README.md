# Integrate Okta Auth0 into your application
Auth0 is a flexible, drop-in solution to add authentication and authorization services to your applications. 
Your team and organization can avoid the cost, time, and risk that come with building your own solution to authenticate and authorize users. 
Learn more <a href="https://auth0.com/docs/get-started/auth0-overview">here</a>.

# Running the App locally

To run the sample, make sure you have `python3.10` or <a href="https://www.python.org/downloads/">`higher`</a> and `pip` installed.

Create `.env` and populate it with the Domain, Client ID, Client Secret and Flask Secret_Key.<br>
Update Application URLs, Application login URL, Allowed Callbacks URL and Allowed Logout callback URL in the <a href="https://manage.auth0.com/">Okta Dashboard</a>. <a href="https://www.okta.com/">Signup</a> for a free trial, and follow the easy steps to create your first web or mobile application. 

1. Download the application generated by Okta. Extract into your project folder
2. Run `pip install -r requirements.txt` to install the dependencies
3. Run `python server.py` or
4. `export FLASk_APP=server.py` initiate `flask run`
5. The app will be served at [http://localhost:3000/] or [http://localhost:5000] depending on your settings.

## What is Auth0?

Auth0 helps you to:

* Add authentication with [multiple authentication sources](https://auth0.com/docs/identityproviders),
either social like **Google, Facebook, Microsoft Account, LinkedIn, GitHub, Twitter, Box, Salesforce, among others**,or
enterprise identity systems like **Windows Azure AD, Google Apps, Active Directory, ADFS or any SAML Identity Provider**.
* Add authentication through more traditional **[username/password databases](https://docs.auth0.com/mysql-connection-tutorial)**.
* Add support for **[linking different user accounts](https://auth0.com/docs/link-accounts)** with the same user.
* Support for generating signed [JSON Web Tokens](https://auth0.com/docs/jwt) to call your APIs and
**flow the user identity** securely.
* Analytics of how, when and where users are logging in.
* Pull data from other sources and add it to the user profile, through [JavaScript rules](https://auth0.com/docs/rules).

## Create a free account in Auth0

1. Go to [Auth0](https://manage.auth0.com/) and click Sign Up.
2. Use Google, GitHub or Microsoft Account to login.
