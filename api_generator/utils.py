import textwrap
from itertools import chain


class Utils:
    @staticmethod
    def wrap_description(text: str, initial_indent: int = 0, subsequent_indent: int = 4, width=0) -> str:
        """Wrap description with indent and width.

        Args:
            text: the description.
            initial_indent: whitespaces before line 1
            subsequent_indent: whitespaces before line 2 and more
            width: line width

        Returns:
            for indent=4 and left=8:
            --------xxxxxxxxxxxxxxxxxxxx
            ------------xxxxxxxxxxxxxxxx
            ------------xxxxxxxxxxxxxxxx
        """
        lines = text.splitlines()
        result = chain.from_iterable(textwrap.wrap(line, width=width, initial_indent=' ' * initial_indent,
                                                   subsequent_indent=' ' * subsequent_indent) for line in lines)
        return '\n'.join(result)
