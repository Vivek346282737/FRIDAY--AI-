from coding.error_reader import ErrorReader
from coding.patcher import patcher
from coding.verifier import verifier


class SelfHealing:

    def repair(

        self,

        error_text: str

    ):

        error = ErrorReader().parse(

            error_text

        )

        patch = patcher.create_patch(

            error

        )

        result = verifier.verify(

            patch

        )

        return {

            "error": error,

            "patch": patch,

            "verification": result

        }


self_healing = SelfHealing()