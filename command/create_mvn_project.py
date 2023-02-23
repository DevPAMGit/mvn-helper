from __future__ import annotations

import os


class CreateSimpleProjectCommand:
    """
    Class that permit to create a simple java maven project.
    """

    def __init__(self, archetype_group_id: str | None, archetype_artifact_id: str, archetype_version: str,
                 group_id: str, artifact_id: str):
        """
        Initialize a new instance of 'CreateSimpleProjectCommand' class.
        :param archetype_group_id: The maven archetype group id.
        :param archetype_group_id: The maven archetype id.
        :param archetype_version: The archetype version.
        :param group_id: The project artifact group id.
        :param artifact_id: The project archetype id.
        """
        self.archetype_artifact_id: str = archetype_artifact_id
        self.archetype_group_id: str | None = archetype_group_id
        self.archetype_version: str = archetype_version
        self.artifact_id: str = artifact_id
        self.group_id: str = group_id

    def execute(self):
        """
        Execute the command.
        """
        if self.__check_precondition() is False:
            return

        to_execute: str = "mvn archetype:generate "
        if self.archetype_group_id is not None:
            to_execute += "-D\"archetypeGroupId=" + self.archetype_group_id + "\" "

        to_execute += "-D\"archetypeArtifactId=" + self.archetype_artifact_id + "\" -D\"archetypeVersion=" + \
                     self.archetype_version + "\" -D\"groupId=" + self.group_id + "\" -D\"artifactId=" + \
                     self.artifact_id + "\" -D\"interactiveMode=false\""

        os.system(to_execute)

    def __check_precondition(self) -> bool:
        if self.archetype_version is None or self.archetype_version.strip().__eq__(""):
            print("Please set the archetype version.")
            return False
        elif ' ' in self.archetype_version:
            print("No space authorize in the archetype version. Thanks.")
            return False

        if self.archetype_artifact_id is None or self.archetype_artifact_id.strip().__eq__(""):
            print("Please set the archetype artifact id.")
            return False
        elif ' ' in self.archetype_artifact_id:
            print("No space authorize in the archetype artifact id. Thanks.")
            return False

        if self.group_id is None or self.group_id.strip().__eq__(""):
            print("Please set the artifact group id.")
            return False

        elif ' ' in self.group_id:
            print("No space authorize in the archetype group id. Thanks.")
            return False

        if self.artifact_id is None or self.artifact_id.strip().__eq__(""):
            print("Please set the artifact id.")
            return False
        elif ' ' in self.artifact_id:
            print("No space authorize in the artifact id. Thanks.")
            return False

        if self.archetype_group_id is not None and self.archetype_group_id.strip().__eq__(""):
            print("The archetype group id is not set.")
            return False

        elif self.archetype_group_id is not None and ' ' in self.archetype_group_id:
            print("No space authorize in the archetype group id.")
            return False

        return True
