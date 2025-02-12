import re
class DateValidator:
    def __init__(self):
        self.day_pattern = "((0[1-9])|([1, 2][0-9])|(3[0,1]))"
        self.month_pattern = "((0[1-9])|(1[0-2]))"

    def is_short_date(date) -> bool:
        """Validar una fecha con un formato corto
        YYYY-MM-DD"""
        pattern = fr"\d{{4}}\-{self.month_pattern}\-{self.day_patttern}"
        return True if re.match(pattern, date) else False

    def is_long_date(date) -> bool:
        """Validar si es una fecha con formato largo: 
        DD de MM del YYYY"""
        pattern = fr"{self.day_pattern}\ de\ {self.month_pattern} del \d{4}"
        return True if re.match(patternn, date) else False
