from statemachine import StateMachine
import time
import handlers
import pdb

fsm = None

#vehicle class for initializing battery level
class Vehicle:
    def __init__(self):
		self.batteryLevel = 100

#user class for the state and type
class User:
    def __init__(self):
        self.state = None
        self.type = None
        self.vehicle = Vehicle()
 
#add transition function       
def initFSM():
    global fsm
    fsm = StateMachine()
    fsm.add_transition("user", "Ready", "execute", "Riding", "Bounty", handlers.start_riding)

    fsm.add_transition("user", "Riding", "execute", "Ready", "Batterylow", handlers.completing_ride)

    fsm.add_transition("hunter","dropped","execute","Ready",None,handlers.ready_riding)

    fsm.add_transition("user", "batterylow", "execute", "bounty", None, handlers.change_state)
    fsm.add_transition("hunter", "bounty", "execute", "collected", None, handlers.change_state)
    fsm.add_transition("hunter","collected","execute","dropped",None,handlers.change_state)


#status of the role state
def print_status(user, error):
    if error == None:
        print ("\n",user.type," is in ", user.state, " state\n")
    else:
        print ("\n",error,"\n")

#for user state
def create_user():
    user = User()
    user.state = "Ready"
    user.type = "user"
    return user

#for hunter state
def create_hunter():
    user = User()
    user.state = "Bounty"
    user.type = "hunter"
    return user
	
#for admin state
def create_admin(state):
    user = User()
    user.state = state
    user.type = "ADMIN"
    return user


#main function where execution starts
if __name__== "__main__":
    initFSM()

    user = create_user()

    hunter = create_hunter()

    print("============================================================")

    user, error = fsm.run(user, "execute")
		
    print_status(user, error)
    print("======================check=======================================")
    
    hunter,error =fsm.run(hunter,"execute")
    print_status(hunter,error)
    hunter,error =fsm.run(hunter,"execute")
    print_status(hunter,error)
    
    print("=================check====================")
	
    
    hunter, error = fsm.run(hunter, "execute")
    print_status(hunter, error)

    print("========================================================")
    #invalid state for hunter
    hunter, error = fsm.run(hunter, "execute")
    print_status(hunter, error)
    print("==========================================================")

    #try out various state changes for admin
    admin = create_admin("READY")
    admin, error = fsm.run(admin, "execute")
    print_status(admin, error)

    admin, error = fsm.run(admin, "execute")
    print_status(admin, error)

    admin, error = fsm.run(admin, "execute")
    print_status(admin, error)

    admin, error = fsm.run(admin, "execute")
    print_status(admin, error)

    admin, error = fsm.run(admin, "execute")
    print_status(admin, error)

    admin, error = fsm.run(admin, "execute")
    print_status(admin, error)

    admin, error = fsm.run(admin, "execute")
    print_status(admin, error)

    admin, error = fsm.run(admin, "execute")
    print_status(admin, error)


    admin, error = fsm.run(admin, "execute")
    print_status(admin, error)

    admin, error = fsm.run(admin, "execute")
    print_status(admin, error)



    admin, error = fsm.run(admin, "execute")
    print_status(admin, error)

    admin, error = fsm.run(admin, "execute")
    print_status(admin, error)

    admin, error = fsm.run(admin, "execute")
    print_status(admin, error)

    admin, error = fsm.run(admin, "execute")
    print_status(admin, error)
