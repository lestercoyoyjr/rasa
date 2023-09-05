import dataclasses
from typing import List, Optional
from rasa.cdu.commands import Command
from rasa.shared.core.flows.flow import FlowsList
from rasa.shared.core.trackers import DialogueStateTracker
from rasa.shared.nlu.training_data.message import Message
from rasa.shared.nlu.constants import COMMANDS


class CommandGenerator:
    """A command generator.

    Parses a message and returns a list of commands. The commands are then
    executed and will lead to tracker state modifications and action
    predictions.
    """

    def process(
        self,
        messages: List[Message],
        tracker: Optional[DialogueStateTracker] = None,
        flows: Optional[FlowsList] = None,
    ) -> List[Message]:
        """Processes a list of messages. For each message predicts commands.

        The result of the prediction is added to the message as a list of
        commands.

        Args:
            message: The message to predict commands for.
            tracker: The tracker containing the conversation history up to now.
            flows: The flows to use for command prediction.

        Returns:
            A list of messages with the predicted commands.
        """
        for message in messages:
            commands = self.predict_commands(message, tracker, flows)
            commands_dicts = [dataclasses.asdict(command) for command in commands]
            message.set(COMMANDS, commands_dicts, add_to_output=True)
        return messages

    def predict_commands(
        self,
        message: Message,
        tracker: Optional[DialogueStateTracker] = None,
        flows: Optional[FlowsList] = None,
    ) -> List[Command]:
        """Predicts commands for a single message.

        Args:
            message: The message to predict commands for.
            tracker: The tracker containing the conversation history up to now.
            flows: The flows to use for command prediction.

        Returns:
            The predicted commands."""
        raise NotImplementedError()
