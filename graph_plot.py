import matplotlib.pyplot as plt
from fetch_data import get_activities
from datetime import datetime

def plot_distances(activities):
    activity_names = [activity['name'] for activity in activities]
    distances = [activity['distance'] for activity in activities]

    plt.figure(figsize=(10, 5))
    plt.bar(activity_names, distances, color='blue')
    plt.xlabel('Activity')
    plt.ylabel('Distance (meters)')
    plt.title('Distances of Activities')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('static/activity_distances.png')
    plt.close()

def plot_speeds(activities):
    activity_names = [activity['name'] for activity in activities]
    speeds = [activity['average_speed'] for activity in activities]

    plt.figure(figsize=(10, 5))
    plt.bar(activity_names, speeds, color='green')
    plt.xlabel('Activity')
    plt.ylabel('Average Speed (m/s)')
    plt.title('Average Speeds of Activities')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('static/activity_speeds.png')
    plt.close()

def plot_elevations(activities):
    activity_names = [activity['name'] for activity in activities]
    elevations = [activity['total_elevation_gain'] for activity in activities]

    plt.figure(figsize=(10, 5))
    plt.bar(activity_names, elevations, color='red')
    plt.xlabel('Activity')
    plt.ylabel('Elevation Gain (meters)')
    plt.title('Elevation Gains of Activities')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('static/activity_elevations.png')
    plt.close()

def plot_activity_metrics():
    activities = get_activities()

    # Ensure activities is not empty and is a list
    if not activities or 'error' in activities:
        print('Failed to fetch activities or no activities available')
        return

    if isinstance(activities, dict):
        activities = activities.get('activities', [])  # Adjust based on actual structure

    # Sort activities by start date
    activities.sort(key=lambda x: datetime.strptime(x['start_date'], '%Y-%m-%dT%H:%M:%SZ'))

    # Generate individual plots
    plot_distances(activities)
    plot_speeds(activities)
    plot_elevations(activities)

def regenerate_plot():
    plot_activity_metrics()
    print("Graphs have been regenerated and saved in 'static/' directory")

if __name__ == '__main__':
    regenerate_plot()
