import requests
from flask import Flask, request, redirect, render_template

app = Flask(__name__)

# Strava API credentials
CLIENT_ID = '141125'
CLIENT_SECRET = '953e892e5aa3d771df34c27035baa28b547b9cf0'
REDIRECT_URI = 'http://localhost:5000/callback'
TOKEN_URL = 'https://www.strava.com/oauth/token'
ACCESS_TOKEN = 'a78b2100ceae356094fbaa231b7d9c4d90590b80'  # The retrieved access token
ACTIVITIES_URL = 'https://www.strava.com/api/v3/athlete/activities'

# Route to initiate the authorization process and function to handle authorization callback
@app.route('/')
def authorize():
    return redirect(f'https://www.strava.com/oauth/authorize?client_id={CLIENT_ID}&response_type=code&redirect_uri={REDIRECT_URI}&scope=read,activity:read')

@app.route('/callback')
def callback():
    code = request.args.get('code')
    if not code:
        return 'Authorization code not found', 400

    print(f'Received authorization code: {code}')  

    response = requests.post(TOKEN_URL, data={
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'code': code,
        'grant_type': 'authorization_code'
    })
    
    print(f'Token request response status: {response.status_code}')  
    print(response.json())  

    if response.status_code != 200:
        return 'Failed to obtain access token', 400

    tokens = response.json()
    global RETRIEVED_ACCESS_TOKEN
    RETRIEVED_ACCESS_TOKEN = tokens['access_token']
    
    # Print the retrieved access token
    print(f'Retrieved access token: {RETRIEVED_ACCESS_TOKEN}')  

    # Write the access token to a file
    with open('token.txt', 'w') as token_file:
        token_file.write(RETRIEVED_ACCESS_TOKEN)

    return redirect('/dashboard')

# Route to display the dashboard
@app.route('/dashboard')
def dashboard():
    activities = get_activities()
    return render_template('dashboard.html', activities=activities)

# Function to fetch activities
def get_activities():
    headers = {'Authorization': f'Bearer {RETRIEVED_ACCESS_TOKEN}'}
    response = requests.get(ACTIVITIES_URL, headers=headers)
    if response.status_code != 200:
        return {'error': 'Failed to fetch activities'}
    activities = response.json()
    return activities

if __name__ == '__main__':
    app.run(debug=True)
