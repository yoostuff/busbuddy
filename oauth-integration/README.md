# Integrate Okta Auth0 into your application
Auth0 is a flexible, drop-in solution to add authentication and authorization services to your applications. 
Your team and organization can avoid the cost, time, and risk that come with building your own solution to authenticate and authorize users. 
Learn more <a href="https://auth0.com/docs/get-started/auth0-overview">here</a>.

# Running the App locally

To run the sample, make sure you have `python3.10` or <a href="https://www.python.org/downloads/">`higher`</a> and `pip` installed.

Create `.env` and populate it with the Domain, Client ID, Client Secret and Flask Secret_Key.
Update Application URLs, Application login URL, Allowed Callbacks URL and Allowed Logout callback URL in the Okta Dashboard.

Run `pip install -r requirements.txt` to install the dependencies and run `python server.py`.
The app will be served at [http://localhost:3000/]
