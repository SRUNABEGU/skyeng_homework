from unittest.mock import patch, mock_open, Mock
from src.utils import convert_transaction_amount, transaction_reader


@patch('requests.request')
def test_convert_transaction_amount_simple(mock_request):
    mock_response = Mock()
    mock_response.text = '{"result": 123.123}'
    mock_request.return_value = mock_response

    test_transaction = {
        'operationAmount': {
            'amount': '123',
            'currency': {'code': 'USD'}
        }
    }

    result = convert_transaction_amount(test_transaction)
    assert result == 123.123


def test_successful_read():
    mock_data = [
        {
            'operationAmount': {
                'currency': {
                    'code': 'USD'
                }
            }
        }
    ]


    with patch('src.utils.open', mock_open()) as mock_file:
        with patch('json.load') as mock_json_load:
            mock_json_load.return_value = mock_data

            result = transaction_reader('test_path.json')

            mock_file.assert_called_with('test_path.json', 'r', encoding='utf-8')
            assert result == 'USD'


def test_file_not_found():
    with patch('src.utils.open', side_effect=FileNotFoundError):
        result = transaction_reader('nonexistent_file.json')
        assert result == []


def test_file_not_list():
    with patch('src.utils.open', mock_open()):
        with patch('json.load') as mock_json_load:
            mock_json_load.return_value = {"key": "value"}

            result = transaction_reader('not_list.json')
            assert result == []


def test_empty_list():
    with patch('src.utils.open', mock_open()):
        with patch('json.load') as mock_json_load:
            mock_json_load.return_value = []

            result = transaction_reader('empty.json')
            assert result == []