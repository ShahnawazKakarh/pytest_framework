import pytest


@pytest.fixture(scope='session')
def companies(config):
    return get_companies_data(config.option.company)


def pytest_addoption(parser):
    parser.addoption('--settings', action='store')
    parser.addoption('--company', action='store',
                     help='Number of times to repeat each test', nargs='+')


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "webtest: mark test to run only on named environment webtest"
    )
    config.addinivalue_line(
        "markers", "apitest: run tests marked as apitest"
    )


def pytest_generate_tests(metafunc):
    if metafunc.config.option.company is not None:
        company_codes = metafunc.config.option.company
        metafunc.fixturenames.append('company')
        metafunc.parametrize('company', company_codes)
