class VacuumCleaner:
    def __init__(self, location, rooms):
        self.location = location
        self.rooms = rooms

    def clean(self):
        # Perform cleaning and decision-making
        while True:
            current_state = self.rooms[self.location]
            print(f"Vacuum is in room {self.location}, which is {'dirty' if current_state else 'clean'}.")

            if current_state:  # If current room is dirty
                print(f"Cleaning room {self.location}...")
                self.rooms[self.location] = 0  # Clean the room (0 for clean)
                print(f"Room {self.location} is now clean.")
            else:  # Move to the next room
                if self.location == 'A':
                    self.location = 'B'
                else:
                    self.location = 'A'

            # Check if all rooms are clean then stop
            if all(room == 0 for room in self.rooms.values()):
                print("All rooms are clean. Vacuum is shutting down.")
                break

# Example usage:
rooms = {'A': 1, 'B': 0}  # 1 means dirty, 0 means clean
vacuum = VacuumCleaner('A', rooms)
vacuum.clean()
