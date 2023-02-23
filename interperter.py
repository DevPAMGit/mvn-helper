from command.create_mvn_project import CreateSimpleProjectCommand


class Interpreter:
    """
    Classe permettant d'interpréter les commandes passées en paramètre.
    """

    def __init__(self):
        pass

    @staticmethod
    def interpreter(tokens: [str]):
        """
        Method that interpret the command's token.
        :param tokens: The command token list.
        """
        if len(tokens) < 2:
            print("Vous n'avez pas saisi de commande à executer. merci.")
            return

        # Get the command to execute.
        command: str = tokens[1]
        arguments: [str] = tokens[2:]

        # Check if the command exists.
        if command.__eq__("new_personnal_lib"):
            # Manage the mvn creation with one argument
            if len(arguments).__eq__(1):
                CreateSimpleProjectCommand(None, "maven-archetype-quickstart", "1.4", "baobab.libraries", arguments[0])\
                    .execute()
            else:
                print("There is more than one argument.")

        elif command.__eq__("show_commands"):
            print("new_personal_lib [artifact_id]")

        # Command not exists.
        else:
            print("La commande '" + command + "' n'est pas connue du script.")
