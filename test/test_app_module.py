#!/usr/bin/env python3l
'''
Test main module
'''
import logging
import pytest
from src.app import Main

logger = logging.getLogger(__name__)
logger.setLevel(level=logging.DEBUG)


@pytest.fixture(name="main_set_fixture")
def fixture_main():
    ''' Fixture to guarntee the same increment '''
    msg = 'test'
    return Main(msg, 1)


@pytest.fixture(name="main_param_fixture")
def fixture_param_main(arg):
    ''' Fixture to guarntee the same increment '''
    return Main(arg, 1)


class TestConstructor:
    '''
    First test
    '''
    def test_first(self, main_set_fixture):
        '''
        First test
        '''
        logger.debug('Test')
        assert main_set_fixture is not None

    @pytest.mark.parametrize('arg', ['steve', 'dave'])
    def test_param_constructor(self, main_param_fixture):
        '''
        First test
        '''
        assert main_param_fixture is not None
        msg = main_param_fixture.get_message()
        assert msg.find('Hello') >= 0
