from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
import logging

# Configure logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ExtractFoodEntity(Action):

    def name(self) -> Text:
        return "extract_food_entity"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        foodEntity = tracker.get_slot('food')
        logger.info(f"Extracted food entity: {foodEntity}")
        if foodEntity:
            dispatcher.utter_message(f"You are feeling{foodEntity}")
        else:
            dispatcher.utter_message("I am sorry I could not detect food")

        return []

class setMoodSlot(Action):

    def name(self) -> Text:
        return "extract_mood_entity"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        mood_entities = list(tracker.get_latest_entity_values('mood'))
        logger.info(f"Extracted mood entity: {mood_entities}")

        if mood_entities:
            mood = mood_entities[0]  # get the first mood entity
            logger.info(f"Set mood slot to: {mood}")
            return [SlotSet('mood', mood)]
        else:
            dispatcher.utter_message("I am sorry I could not detect your mood")
            return []
class ExtractMoodSlot(Action):

    def name(self) -> Text:
        return "extract_slot"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        mood_entities = tracker.get_slot('mood')
        logger.info(f"Extracted mood entity: {mood_entities}")
        if mood_entities:
            dispatcher.utter_message(f"Extracted mood entity: {mood_entities}")
        else:
            dispatcher.utter_message("I am sorry I could not detect your mood")

        return [SlotSet('mood', mood_entities)]
