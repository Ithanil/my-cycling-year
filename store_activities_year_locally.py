from stravaio import StravaIO
import get_token

client = StravaIO(access_token=get_token.token['access_token'])

# Store Athlete
athlete = client.get_logged_in_athlete()
athlete.store_locally()

# Store Activities
list_activities = client.get_logged_in_athlete_activities(after='last year')
for a in list_activities:
    client.get_activity_by_id(a.id).store_locally()
