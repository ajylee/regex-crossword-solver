# Added to avoid dependency on nosetests, which doesn't seem to work with
# python 3. This file should be renamed or combined with others when
# more non-nose tests are added.
#
# Tests in here are compatible with pytest.
#
# -- ajl

from ..regex_parser import *
parser = RegexParser()

def assert_parse_results(regex, root, groups=[], backrefs=set()):
    first = parser.parse(regex)
    second = {'groups': groups, 'root': root, 'backrefs': backrefs}
    assert first == second


def test_non_capturing_groups():
    """Test that there is no difference between capturing and non-capturing
    groups.

    """

    regexes = [('(?:x)', '(x)'),
               ('abc(?:spam|[eggs]+)?', 'abc(spam|[eggs]+)?'),
               ('abc(?:spam|[eggs]+)?:xyz', 'abc(spam|[eggs]+)?:xyz'),
               ]

    for non_capturing_regex, capturing_regex in regexes:
        assert_parse_results(non_capturing_regex, **parser.parse(capturing_regex))
