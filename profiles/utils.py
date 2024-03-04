import phonenumbers
import re

def validate_and_classify_phone_number(phone_number):
    """
    Validate the given phone number and classify its type.

    Args:
        phone_number (str): The phone number to be validated.

    Returns:
        tuple: A tuple containing two values:
               - bool: True if the phone number is valid, False otherwise.
               - str: A string indicating the classification ('Valid', 'Cell Phone', or 'Invalid').
    """
    digit_number = re.sub("[^0-9]", "", phone_number)
    try:
        # Attempt to parse the phone number
        parsed_number = phonenumbers.parse(digit_number, None)

    except phonenumbers.phonenumberutil.NumberParseException as e:
        digit_number = "+1" + digit_number

    try:
        # Attempt to parse the phone number
        parsed_number = phonenumbers.parse(digit_number, None)

        # Check if the parsed number is possible and valid
        if phonenumbers.is_possible_number(parsed_number) and phonenumbers.is_valid_number(parsed_number):
            # Check if the number is a mobile/cell phone number
            if phonenumbers.number_type(parsed_number) == phonenumbers.PhoneNumberType.MOBILE:
                return False, 'Cell Phone'
            else:
                return True, 'Valid'
        else:
            return False, 'Invalid'

    except phonenumbers.phonenumberutil.NumberParseException as e:
        # Handle NumberParseException, e.g., log the error
        print(f"NumberParseException: {e}")
        return False, f'{e}'

    except Exception as e:
        # Handle other exceptions, log the error
        print(f"An unexpected error occurred: {e}")
        return False, f'{e}'