# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


import json
from pathlib import Path
from typing import Any, Text, Dict, List ,Optional
from rasa_sdk.events import AllSlotsReset
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher ,Action
from rasa_sdk.knowledge_base.storage import InMemoryKnowledgeBase
from rasa_sdk.knowledge_base.actions import ActionQueryKnowledgeBase
from rasa_sdk import Tracker
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.events import AllSlotsReset, SlotSet
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.types import DomainDict


# show projects
class ValidateRegisterForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_appointment_form"
    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        return []

    def validate_name(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate slot value."""
        required_slots = ["name" , "age" , "gender" , "place" , "pre_medical"]
        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                return [SlotSet("requested_slot" , slot_name)]
 
        return [SlotSet("requested_slot" , None)]
       # if not slot_value:
       #  return {"name": None}
       # else: 
        # return {"name": slot_value}	
class ActionSubmitProject(Action):
    def name(self) -> Text:
        return "actions_submit_appoint"

    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text, Any]]:
	
        name = tracker.get_slot("name")
        age = tracker.get_slot("age")
        gender = tracker.get_slot("gender")
        place = tracker.get_slot("place")
        pre_medical = tracker.get_slot("pre_medical")
        print("name  is  : ",name) 
        print("date is  is  : ",gender) 
        print("age is " , age)

        if(pre_medical=="High Blood Pressure"):
            dispatcher.utter_message(template="utter_contact_doctor")
            
        elif(pre_medical=="fever" or pre_medical=="cough" or pre_medical=="body ache"):
            if(int(age)>40):
                if(place=="Mumbai"):
                    dispatcher.utter_message(template="utter_check_up_Mumbai")
                if(place=="Pune"):
                    dispatcher.utter_message(template="utter_check_up_Pune")
                if(place=="Manipal"):
                    dispatcher.utter_message(template="utter_check_up_Manipal")
                if(place=="Bangalore"):
                    dispatcher.utter_message(template="utter_check_up_Bangalore")
            else:
                dispatcher.utter_message(template="utter_contact_doctor")
        
        elif(pre_medical=="liver function test"):
            if(place=="Mumbai"):
                dispatcher.utter_message(template="utter_check_LFT_Mumbai")
            if(place=="Pune"):
                dispatcher.utter_message(template="utter_check_LFT_Pune")
            if(place=="Manipal"):
                dispatcher.utter_message(template="utter_check_LFT_Manipal")
            if(place=="Bangalore"):
                dispatcher.utter_message(template="utter_check_LFT_Bangalore")
        
        elif(pre_medical=="ECG"):
            if(place=="Mumbai"):
                dispatcher.utter_message(template="utter_check_ECG_Mumbai")
            if(place=="Pune"):
                dispatcher.utter_message(template="utter_check_ECG_Pune")
            if(place=="Manipal"):
                dispatcher.utter_message(template="utter_check_ECG_Manipal")
            if(place=="Bangalore"):
                dispatcher.utter_message(template="utter_check_ECG_Bangalore")

        elif(pre_medical=="complete blood count" or pre_medical=="blood count"):
            if(place=="Mumbai"):
                dispatcher.utter_message(template="utter_check_BC_Mumbai")
            if(place=="Pune"):
                dispatcher.utter_message(template="utter_check_BC_Pune")
            if(place=="Manipal"):
                dispatcher.utter_message(template="utter_check_BC_Manipal")
            if(place=="Bangalore"):
                dispatcher.utter_message(template="utter_check_BC_Bangalore")
            
        else:
            if(int(age)<=25 and (gender=='M' or gender =='m')):
                dispatcher.utter_message(template="utter_20_M")
            if(int(age)> 25 and int(age)<=50 and (gender=='M' or gender =='m')):
                dispatcher.utter_message(template="utter_40_M")
            if(int(age)> 50 and (gender=='M' or gender =='m')):
                dispatcher.utter_message(template="utter_60_M")
            if(int(age)<=25 and (gender=='F' or gender =='f')):
                dispatcher.utter_message(template="utter_20_F")
            if(int(age)> 25 and int(age)<=50 and (gender=='F' or gender =='f')):
                dispatcher.utter_message(template="utter_40_F")
            if(int(age)> 50 and (gender=='F' or gender =='f')):
                dispatcher.utter_message(template="utter_60_F")
        

        
        #dispatcher.utter_message(template="utter_details_under20")
        return[AllSlotsReset()]





# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []