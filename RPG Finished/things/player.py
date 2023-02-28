from things.actors import actor
import json
import random


MY_GAME_LOGIC = {}
with open('rpg.json', 'r') as myfile:
    MY_GAME_LOGIC = json.loads(myfile.read())

class player(actor):
    def __init__(self, phone_number):
        super().__init__(phone_number)
        self.score = 0

    def get_output(self,msg_input):
        found_match = False
        output = [  ]
        if type( MY_GAME_LOGIC[ self.state ]['next_state'] ) != str: # we have choices
            for next_state in MY_GAME_LOGIC[ self.state ]['next_state']:
                if msg_input.lower() ==  next_state['input'].lower():
                    self.state = next_state['next_state'] 
                    found_match = True
                    break

            if found_match == False:
                return ['Ooops.. Not a valid choice...']

        while True:
            output.append( MY_GAME_LOGIC[ self.state ]['content'])
            if 'next_state' not in MY_GAME_LOGIC[ self.state ] or type( MY_GAME_LOGIC[ self.state ]['next_state'] ) != str:
                break
            self.state = MY_GAME_LOGIC[ self.state ]['next_state']
        
        return output
