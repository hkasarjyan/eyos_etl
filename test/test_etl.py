import pytest

from csv_reader import get_store_from_csv
from db.crud import add_store
from models import Stores


# def test_get_store_from_csv(csv_data):
#     store = get_store_from_csv(csv_data)
#     assert store.store_name == csv_data[0]
#     # assert store.street_name == csv_data[0]
#     # assert store.store_name == csv_data[0]
#     # assert store.store_name == csv_data[0]
#     # assert store.store_name == csv_data[0]


@pytest.mark.parametrize(
    "csv_data1",
    [
        [
            "Testme Store 3",
            "Thailand",
            "85/13 Soi Kamnanmaen Ekachai Road Jomthong",
            "10150",
            "Bangkok",
            "Bangkok",
            "",
        ],
    ],
)
def test_store_code(csv_data1):
    stored_data = add_store(get_store_from_csv(csv_data1))
    assert stored_data.get_store_code() == stored_data.country_code + str(
        stored_data.store_id
    )


@pytest.mark.parametrize(
    "csv_data2",
    [
        [
            "Testme Store 2",
            "India",
            "5531/21, Sh No 7, Harphool Singh Building, Sadar Thana Rd, Chandni Chowk",
            "110006",
            "Delhi",
            "Delhi",
            "",
        ],
    ],
)
def test_comma_in_address(csv_data2):
    stored_data = add_store(get_store_from_csv(csv_data2))
    store = get_store_from_csv(csv_data2)
    assert stored_data.street_name == csv_data2[2]


@pytest.mark.parametrize(
    "csv_data3",
    [
        [
            "Testme Store 1",
            "Indonesia",
            " Jl Ciledug Raya 88, Dki Jakarta",
            "15156",
            "Jakarta",
            "Dki Jakarta",
            "",
        ],
    ],
)
def test_validate_all_values(csv_data3):
    stored_data = add_store(get_store_from_csv(csv_data3))
    store = get_store_from_csv(csv_data3)
    assert stored_data.get_store_code() == stored_data.country_code + str(
        stored_data.store_id
    )
    assert stored_data.street_name == csv_data3[2]
    assert stored_data.country_code == "IND"
    assert stored_data.pin_code == csv_data3[3]
    assert stored_data.lvl1_geog == csv_data3[4]
    assert stored_data.lvl2_geog == csv_data3[5]
    assert stored_data.lvl3_geog == ""
