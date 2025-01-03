class TripPlannerAgent:
    def __init__(self):
        self.destinations = ["Paris", "New York", "Tokyo", "Sydney"]
        self.accommodations = ["Hotel", "Hostel", "Airbnb"]
        self.activities = ["Sightseeing", "Hiking", "Museum", "Shopping"]

    def plan_trip(self):
        print("Welcome to the Trip Planner Agent!")
        destination = self.choose_destination()
        accommodation = self.choose_accommodation()
        activity = self.choose_activity()
        print(f"Your trip is planned to {destination} with accommodation at a {accommodation} and activities including {activity}.")

    def choose_destination(self):
        print("Available destinations:")
        for i, destination in enumerate(self.destinations, 1):
            print(f"{i}. {destination}")
        choice = int(input("Choose a destination (1-4): "))
        return self.destinations[choice - 1]

    def choose_accommodation(self):
        print("Available accommodations:")
        for i, accommodation in enumerate(self.accommodations, 1):
            print(f"{i}. {accommodation}")
        choice = int(input("Choose an accommodation (1-3): "))
        return self.accommodations[choice - 1]

    def choose_activity(self):
        print("Available activities:")
        for i, activity in enumerate(self.activities, 1):
            print(f"{i}. {activity}")
        choice = int(input("Choose an activity (1-4): "))
        return self.activities[choice - 1]