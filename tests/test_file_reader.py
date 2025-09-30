from unittest.mock import Mock, patch

from src.file_reader import csv_reader, xlsx_reader


@patch("csv.DictReader")
def test_csv_reader(mock_dict_reader):
    mock_dict_reader.return_value = [{"id": "001"}, {"id": "002"}, {"id": "003"}]

    result = csv_reader()

    assert result == [{"id": "001"}, {"id": "002"}, {"id": "003"}]


@patch("pandas.read_excel")
def test_xlsx_reader(mock_read_excel):
    mock_df = Mock()
    mock_df.to_dict.return_value = [{"id": "001"}, {"id": "002"}, {"id": "003"}]
    mock_read_excel.return_value = mock_df

    result = xlsx_reader()

    assert result == [{"id": "001"}, {"id": "002"}, {"id": "003"}]
