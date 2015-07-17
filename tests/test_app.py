"""Example to show where to implement tests."""

import pytest
import pandas as pd
import example_conda_app
from sqlalchemy import create_engine, Table, MetaData

table_names = ['example_app_data']

@pytest.fixture
def eng():
    """Generate the database eng object, used for dependency injection."""
    meta = MetaData()
    db_eng = create_engine("mysql+pymysql://root:testing@datadb:3306/test")

    def fin():
        for table_name in table_names:
            tbl = Table(table_name, meta)
            tbl.drop(eng)

    return db_eng

@pytest.fixture
def data():
    """Collect data from the app."""
    return example_conda_app.main()


def test_insert(eng, data):
    """Make assertions about our application."""
    success = False
    try:
        data.to_sql('example_app_data', eng)
        success = True
    except Exception as e:
        raise e
    assert success == True

def test_data(eng, data):
    """Check input vs output data from database."""
    data_in = pd.read_sql_table('example_app_data', eng)
    assert len(data.index)==len(data_in.index)
