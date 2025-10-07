from unittest.mock import Mock, mock_open, patch

from src.utils import convert_transaction_amount, json_file_reader


@patch("requests.request")
def test_convert_transaction_amount(mock_request):
    mock_response = Mock()
    mock_response.text = '{"result": 123.123}'
    mock_request.return_value = mock_response

    test_transaction = {"operationAmount": {"amount": "123", "currency": {"code": "USD"}}}

    result = convert_transaction_amount(test_transaction)
    assert result == 123.123


@patch("requests.request")
def test_convert_transaction_amount_rub_currency(mock_request):
    test_transaction = {
        "operationAmount": {
            "amount": "1000",
            "currency": {"code": "RUB"}
        }
    }

    result = convert_transaction_amount(test_transaction)
    assert result == 1000.0
    assert not mock_request.called


def test_successful_read():
    mock_data = [{"operationAmount": {"currency": {"code": "USD"}}}]

    with patch("src.utils.open", mock_open()) as mock_file:
        with patch("json.load") as mock_json_load:
            mock_json_load.return_value = mock_data

            result = json_file_reader("test_path.json")

            mock_file.assert_called_with("test_path.json", "r", encoding="utf-8")
            assert result == mock_data


def test_file_not_found():
    with patch("src.utils.open", side_effect=FileNotFoundError):
        result = json_file_reader("nonexistent_file.json")
        assert result == []


def test_file_not_list():
    with patch("src.utils.open", mock_open()):
        with patch("json.load") as mock_json_load:
            mock_json_load.return_value = {"key": "value"}

            result = json_file_reader("not_list.json")
            assert result == []


def test_empty_list():
    with patch("src.utils.open", mock_open()):
        with patch("json.load") as mock_json_load:
            mock_json_load.return_value = []

            result = json_file_reader("empty.json")
            assert result == []


@patch("requests.request")
def test_convert_transaction_amount_api_exception(mock_request):
    """Тест для обработки исключений при запросе к API (покрывает строки 66-68)"""
    mock_request.side_effect = Exception("API недоступно")

    test_transaction = {
        "operationAmount": {
            "amount": "100",
            "currency": {"code": "USD"}
        }
    }

    result = convert_transaction_amount(test_transaction)
    assert "Ошибка: API недоступно" in result
