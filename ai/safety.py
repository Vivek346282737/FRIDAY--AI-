class Safety:

    CONFIRMATION_ACTIONS = {

        "SYSTEM",

        "FILE"

    }

    DANGEROUS_KEYWORDS = [

        "shutdown",

        "restart",

        "delete",

        "remove",

        "format",

        "erase"

    ]

    def requires_confirmation(

        self,

        action,

        target

    ):

        if not action:

            return False

        action = str(action).upper()

        target = str(target).lower()

        if action == "SYSTEM":

            return any(

                word in target

                for word in [

                    "shutdown",

                    "restart"

                ]

            )

        if action == "FILE":

            return any(

                word in target

                for word in [

                    "delete",

                    "remove",

                    "format"

                ]

            )

        return False


safety = Safety()
