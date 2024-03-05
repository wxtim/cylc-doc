from enchant.tokenize import Filter

import cylc
import inspect

def recursive_inspect(base):
    results = []
    for _, item in inspect.getmembers(base):
        if inspect.ismodule(item) and item.__name__.startswith('cylc.flow'):
            # breakpoint(header=f'{item}')
            results += recursive_inspect(item)
        elif inspect.isfunction(item):
            results.append(item)

    return results

def get_cylc_jargon():
    jargon = []
    functions = recursive_inspect(cylc)
    for func in functions:
        words = inspect.signature(func).parameters
        for word in words:
            if word not in jargon:
                jargon.append(word.lower())
    return jargon


CYLC_JARGON = get_cylc_jargon()


class CylcJargonFilter(Filter):
    """Ignore words given as arguments to Cylc Functions.
    """

    def _skip(self, word):
        word = word.lower()
        words = word.split('-')
        if len(words) > 1:
            # If any word is skippable.
            return any(self._is_skippable(w) for w in words)
        else:
            return self._is_skippable(word)

    @staticmethod
    def _is_skippable(word):
        return (
            word in CYLC_JARGON
            or word + 's' in CYLC_JARGON
            or word + 'es' in CYLC_JARGON
            or word.endswith('s') and word[:-1] in CYLC_JARGON
        )
