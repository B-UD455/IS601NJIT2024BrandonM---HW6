import pytest
from faker import Faker

@pytest.fixture(scope='session')
def faker_instance():
    return Faker()

def pytest_addoption(parser):
    parser.addoption("--num_records", action="store", default=1, help="Number of records to generate")

@pytest.fixture
def generate_records(request, faker_instance):
    num_records = int(request.config.getoption("--num_records"))
    records = []
    for _ in range(num_records):
        a = faker_instance.random_int(min=1, max=100)
        b = faker_instance.random_int(min=1, max=100)
        operation = faker_instance.random_element(elements=('add', 'subtract', 'multiply', 'divide', 'unknown'))
        records.append((a, b, operation))
    return records
