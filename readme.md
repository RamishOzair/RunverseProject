# Sports Data Integration and Display

## Setup Instructions

Step 1: Open the Folder
--------------------------------------

Step 2: Create a Virtual Environment
----------------------------------------
python3 -m venv venv
venv\Scripts\activate

-----------------------------------------
Step 3: Install Necessary Packages
-----------------------------------------
pip install requests Flask matplotlib

-----------------------------------------
Step 4: Stravia account is set up using my credentials already
----------------------------------------
Step 5: Run the app.py to get the access token and replace the already set access token with new generated access token
----------------------------------------------------------------------------------------------
Step 6 : Run python fetch_data.py
--------------------------------------
Step 7 : Run python graph_plot.py
--------------------------------------
Step 8 : Run the app.py again
-----------------------------------
Step 9 : Open your browser and enter: http://localhost:5000/dashboard
----------------------------------------------------------------------
End
-----------------*-----------------*----------------------


Files and Folders
-----------------------------
1. app.py: Flask app to handle authentication and display data

2. fetch_data.py: Script to fetch activity data from Strava

3. plot_data.py: Script to plot data using Matplotlib

4. static/: Folder containing static files (CSS, images)

5. static/styles.css: CSS file for styling the dashboard

6. templates/: Folder containing HTML templates

7. templates/dashboard.html: HTML template for displaying data

8. README.md: Setup instructions and documentation

