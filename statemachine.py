
class StateMachine:

    def __init__(self):
        self.fsm_dict = {}

    def add_transition(self, user_type, src_state, event, dst_state_primary, dst_state_secondary, handler):
        #import pdb; pdb.set_trace()
        src_state = src_state.upper()
        user_type = user_type.upper()
        event = event.upper()

        dst_state_primary = dst_state_primary.upper()

        if dst_state_secondary != None:
             dst_state_secondary = dst_state_secondary.upper()

        event_handler_dict = {"handler": handler, "dst_state_primary": dst_state_primary, "dst_state_secondary": dst_state_secondary}

        tmp_fsm_dict = {user_type + "-" + src_state + "-" + event: event_handler_dict}
        tmp_fsm_dict_admin = {"ADMIN" + "-" + src_state + "-" + event: event_handler_dict}
        self.fsm_dict.update(tmp_fsm_dict)
        self.fsm_dict.update(tmp_fsm_dict_admin)
        # print('temp fsm admin:',tmp_fsm_dict_admin)


    def run(self, user, event):
        try:
            #import pdb; pdb.set_trace()
            handler_dict = self.fsm_dict[user.type.upper() + "-" + user.state.upper() + "-" + event.upper()]
            handler = handler_dict["handler"]
            dst_state_primary = handler_dict["dst_state_primary"]
            dst_state_secondary = handler_dict["dst_state_secondary"]

        except:
            return user, "Error : The device state : " + user.state.upper() + " and event : " + event.upper() + " not part of FSM for the user : " + user.type.upper()

        return handler(user, dst_state_primary, dst_state_secondary)
