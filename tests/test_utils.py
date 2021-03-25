import pytest
import utils


def test_function_generate_list_of_duplicate_email_pairs_of_size_is_generating_duplicate_pairs_for_odd_number():
    list_with_odd_number_of_items = utils.create_list_of_duplicate_email_pairs(9)
    assert len(list_with_odd_number_of_items) == 9
    assert len(set(list_with_odd_number_of_items)) == 4
    assert list_with_odd_number_of_items[0] == list_with_odd_number_of_items[-1]

    list_with_odd_number_of_items = utils.create_list_of_duplicate_email_pairs(100001)
    assert len(list_with_odd_number_of_items) == 100001
    assert len(set(list_with_odd_number_of_items)) == 50000
    assert list_with_odd_number_of_items[0] == list_with_odd_number_of_items[-1]


def test_function_generate_list_of_duplicate_email_pairs_of_size_is_generating_duplicate_pairs_for_even_number():
    list_with_even_number_of_items = utils.create_list_of_duplicate_email_pairs(8)
    assert len(list_with_even_number_of_items) == 8
    assert len(set(list_with_even_number_of_items)) == 4

    list_with_even_number_of_items = utils.create_list_of_duplicate_email_pairs(100000)
    assert len(list_with_even_number_of_items) == 100000
    assert len(set(list_with_even_number_of_items)) == 50000


def test_function_returns_value_error_when_invalid_parameter_is_entered():
    with pytest.raises(ValueError):
        utils.create_list_of_duplicate_email_pairs(1)


def test_function_generate_list_of_unique_email_of_size_creates_unique_emails():
    list_with_even_number_of_items = utils.create_list_of_unique_emails(8)
    assert len(list_with_even_number_of_items) == 8
    assert len(set(list_with_even_number_of_items)) == 8

    list_with_even_number_of_items = utils.create_list_of_duplicate_email_pairs(100000)
    assert len(list_with_even_number_of_items) == 100000
    assert len(set(list_with_even_number_of_items)) == 50000


def test_combined_unique_and_duplicate_emails_are_generated_based_on_parameters_provided():
    duplicate_and_unique_emails = utils.create_list_of_unique_and_duplicate_emails(size=1000,
                                                                                   duplicate_percent=.5)
    assert len(set(duplicate_and_unique_emails)) == 750
    assert len(duplicate_and_unique_emails) == 1000

    duplicate_and_unique_emails = utils.create_list_of_unique_and_duplicate_emails(size=1001,
                                                                                   duplicate_percent=.5)
    assert len(set(duplicate_and_unique_emails)) == 751
    assert len(duplicate_and_unique_emails) == 1001


def test_deduplicate_can_remove_duplicates_in_list():
    list_with_duplicates = ['a', 'a', 'a', 'b', 'c']
    assert utils.deduplicate_list(list_with_duplicates) == ['a', 'b', 'c']


def test_deduplicate_with_one_duplicate_in_list():
    list_with_one_duplicate = ['1', '1', '1', '1']
    assert utils.deduplicate_list(list_with_one_duplicate) == ['1']


def test_deduplicate_with_no_duplicates_in_list():
    list_with_no_duplicate = ['1', '2', '3', '4']
    assert utils.deduplicate_list(list_with_no_duplicate) == ['1', '2', '3', '4']


def test_deduplicate_that_order_is_retained_on_list():
    first_instance_is_retained = ['a', 'b', 'c', 'd', 'a']
    assert utils.deduplicate_list(first_instance_is_retained) == ['a', 'b', 'c', 'd']

    duplicate_in_middle = ['a', 'b', 'b', 'c', 'b', 'd']
    assert utils.deduplicate_list(duplicate_in_middle) == ['a', 'b', 'c', 'd']

    duplicate_alternating = ['a', 'b', 'a', 'b', 'c', 'd', 'e']
    assert utils.deduplicate_list(duplicate_alternating) == ['a', 'b', 'c', 'd', 'e']
