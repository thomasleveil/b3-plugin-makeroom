# -*- encoding: utf-8 -*-


def extends_mock():
    from mock import Mock # http://www.voidspace.org.uk/python/mock/mock.html
    # extend the Mock class
    def assert_was_called_with(self, *args, **kwargs):
        """
        assert that the mock was called with the specified arguments at least once.

        Raises an AssertionError if the args and keyword args passed in are
        different from all calls to the mock.
        """
        if self.call_args is None:
            raise AssertionError('Expected: %s\nNot called' % ((args, kwargs),))
        found = False
        for call_args in self.call_args_list:
            if call_args == (args, kwargs):
                found = True
                break
        if not found:
            raise AssertionError(
                'Expected: %s\nCalled at least once with: %s' % ((args, kwargs), self.call_args_list)
            )
    Mock.assert_was_called_with = assert_was_called_with


def show_player_info(player):
    print "{name:>12} @{id:<3} {group:>10} {level:>5}".format(name=player.name, id=player.id, group=player.maxGroup.name, level="(%s)" % player.maxLevel)