from bluer_options import string


class Specs:
    def __init__(
        self,
        tao: int = 1,
        tac: int = 0,
        tro: int = 3,
        trc: int = 1,
        ta1: int = 30,
        ta2: int = 30,
        tr1: int = 24,
        tr2: int = 36,
    ):
        self.tao = tao
        self.tac = tac
        self.tro = tro
        self.trc = trc

        self.ta1 = ta1
        self.ta2 = ta2
        self.tr1 = tr1
        self.tr2 = tr2

    def as_str(self) -> str:
        return "ta:{} > {} - {} < {} | tr:{} > {} - {} < {}".format(
            string.pretty_minimal_duration(self.tao),
            string.pretty_minimal_duration(self.ta1),
            string.pretty_minimal_duration(self.ta2),
            string.pretty_minimal_duration(self.tac),
            string.pretty_minimal_duration(self.tro),
            string.pretty_minimal_duration(self.tr1),
            string.pretty_minimal_duration(self.tr2),
            string.pretty_minimal_duration(self.trc),
        )
