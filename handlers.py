import time
from datetime import datetime

#change state handler
def change_state(user, dst_state_primary, dst_state_secondary):
    user.state = dst_state_primary
    return (user, None)

#start riding handler
def start_riding(user, dst_state_primary, dst_state_secondary):
	# Update battery logic based on requirement
    user.vehicle.batteryLevel = user.vehicle.batteryLevel - 20
	
    current_time = datetime.strftime(datetime.now(),"%I:%M:%S %p")
    print("current_time:",current_time)

    if current_time > "09:30 PM":
       user.state = dst_state_secondary
    else:
      user.state = dst_state_primary

    return (user, None)

#completing the ride handler
def completing_ride(user, dst_state_primary, dst_state_secondary):
    # add battery low check
    # Update battery logic based on requirement
    user.vehicle.batteryLevel = user.vehicle.batteryLevel - 20

    if user.vehicle.batteryLevel < 20:
        user.state=dst_state_secondary
    else:
        user.state = dst_state_primary
    return (user, None)

#ready riding handler
def ready_riding(user,dst_state_primary,dst_state_secondary):

    user.state=dst_state_primary
    user.vehicle.batteryLevel = 100
    return (user,None)
