if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    
    # remove data with zero passenger count
    data = data[data['passenger_count'] > 0]

    # remove rows with zero trip distance
    data = data[data['trip_distance'] > 0 ]

    # convert lpep_pickup_datetime to a date
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date

    #Rename columns in Camel Case to Snake Case
    def camel_to_snake(column_name):
        result = []
        for i, c in enumerate(column_name):
            if c.isupper() and i > 0 and not column_name[i-1].isupper() and column_name[i-1] != '_':
                result.append('_')
            result.append(c.lower())
        return ''.join(result)

    data.columns = [camel_to_snake(col) for col in data.columns]

    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert 'vendor_id' in output.columns, 'vendor_id does not exist'
    assert output['passenger_count'].isin([0]).sum() == 0 , 'There are rows with zero passenger count'
    assert output['trip_distance'].isin([0]).sum() == 0, 'There are rows with zero trip distance'