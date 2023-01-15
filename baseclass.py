import datetime

class BaseClass():
    
    @staticmethod
    def date_to_str(date: datetime.date)->str:
        if not isinstance(date, datetime.date):
            raise TypeError('entered value is not a datetime.date')
        else: 
            str_year = str(date.year)
            if date.month >= 10:
                str_month = str(date.month)
            else: 
                str_month = "0" + str(date.month)
            if date.day >= 10:
                str_day = str(date.day)
            else: 
                str_day = "0" + str(date.day)
            date_str = str_year + "/" + str_month + "/" + str_day
            return date_str

    @staticmethod
    def str_to_date(str_date:str)->datetime.date:
        try: 
            return datetime.date(int(str_date[0:4]), int(str_date[5:7]),int(str_date[8:10]))
        except: 
            raise ValueError('date (string) is incorrectly formatted for conversion, use YYYY/MM/DD')


def main():
    test_class = BaseClass()
    test_string = '2000/10/10'
    print(test_string)
    print(test_class.str_to_date(test_string))
   



if __name__ == '__main__':
    main()

