import time

# Initialize the position of the arrow and the distance to the target
arrow_position = 0
target_distance = 50

# Simulate the flight of the arrow
for time_instant in range(50):
    # Calculate the distance between the arrow and the target
    distance_to_target = target_distance - arrow_position
    
    print(f"Instant {time_instant + 1}: Arrow position = {arrow_position} meters, Distance to target = {distance_to_target} meters")
    
    # Check if the arrow has reached the target
    if distance_to_target <= 0:
        print("Arrow has hit the target!")
        break
    
    # Update the arrow's position (example: The arrow moves 5 meters forward in each instant)
    arrow_position += 5
    
    # Pause for a moment to simulate the flow of time
    time.sleep(1)  # Sleep for 1 second between instants (adjust as needed)
