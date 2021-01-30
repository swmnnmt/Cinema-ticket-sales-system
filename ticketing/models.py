from django.db import models


class Movie(models.Model):
    """
    Represents a movie
    """

    class Meta:
        verbose_name = 'فیلم'
        verbose_name_plural = 'فیلم'

    name = models.CharField(max_length=100, verbose_name='عنوان فیلم')
    director = models.CharField(max_length=50, verbose_name='کارگردان')
    year = models.IntegerField(verbose_name='سال تولید')
    length = models.IntegerField(verbose_name='مدت زمان')
    description = models.TextField(verbose_name='توضیح فیلم')
    poster = models.ImageField(verbose_name='پوستر', upload_to='movie_posters/', null=True, blank=True)

    def __str__(self):
        return self.name


class Cinema(models.Model):
    """
    Represents a cinema (movie theater)
    """

    class Meta:
        verbose_name = 'سینما'
        verbose_name_plural = 'سینما'

    cinema_code = models.IntegerField(primary_key=True, verbose_name='کد سینما')
    name = models.CharField(max_length=50, verbose_name='نام')
    city = models.CharField(max_length=30, default='شیراز', verbose_name='شهر')
    capacity = models.IntegerField(verbose_name='گنجایش')
    phone = models.CharField(max_length=11, blank=True, verbose_name='تلفن')
    address = models.TextField(verbose_name='آدرس')
    image = models.ImageField(verbose_name='تصویر', upload_to='cinema_images/', null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.name)


class ShowTime(models.Model):
    """
    Represents a movie show in a cinema at a specific time
    """

    class Meta:
        verbose_name = 'سانس'
        verbose_name_plural = 'سانس'

    movie = models.ForeignKey(to=Movie, on_delete=models.PROTECT, verbose_name='فیلم')
    cinema = models.ForeignKey(to=Cinema, on_delete=models.PROTECT, verbose_name='سینما')
    start_time = models.DateTimeField(verbose_name='زمان شروع نمایش')
    price = models.IntegerField(verbose_name='قیمت')
    saleable_seats = models.IntegerField(verbose_name='صندلی های قابل فروش')
    free_seats = models.IntegerField(verbose_name='صندلی های خالی')
    SALE_NOT_STARTED = 1
    SALE_OPEN = 2
    TICKETS_SOLD = 3
    SALE_CLOSED = 4
    MOVIE_PLAYED = 5
    SHOW_CANCELED = 6
    status_choices = (
        (SALE_NOT_STARTED, 'فروش آغاز نشده'),
        (SALE_OPEN, 'در حال فروش بلیت'),
        (TICKETS_SOLD, 'بلیت ها تمام شد'),
        (SALE_CLOSED, 'فروش بلیت بسته شد'),
        (MOVIE_PLAYED, 'فیلم پخش شد'),
        (SHOW_CANCELED, 'سانس لغو شد'),
    )
    status = models.IntegerField(choices=status_choices, verbose_name='وضعیت')

    def __str__(self):
        return '{} - {} - {}'.format(self.movie, self.cinema, self.start_time)

    def get_price_display(self):
        return '{} تومان'.format(self.price)

    def is_full(self):
        """
        Returns True if all seats are sold
        """
        return self.free_seats == 0

    def open_sale(self):
        """
        Opens ticket sale
        If sale was opened before, raises an exception
        """
        if self.status == ShowTime.SALE_NOT_STARTED:
            self.status = ShowTime.SALE_OPEN
            self.save()
        else:
            raise Exception('Sale has been started before')

    def close_sale(self):
        """
        Closes ticket sale
        If sale is not open, raises an exception
        """
        if self.status == ShowTime.SALE_OPEN:
            self.status = ShowTime.SALE_CLOSED
            self.save()
        else:
            raise Exception('Sale is not open')

    def expire_showtime(self, is_canceled=False):
        """
        Expires showtime and updates the status
        :param is_canceled: A boolean indicating whether the show is canceled or not, default is False
        """
        if self.status not in (ShowTime.MOVIE_PLAYED, ShowTime.SHOW_CANCELED):
            self.status = ShowTime.SHOW_CANCELED if is_canceled else ShowTime.MOVIE_PLAYED
            self.save()
        else:
            raise Exception('Show has been expired before')

    def reserve_seats(self, seat_count):
        """
        Reserves one or more seats for a customer
        :param seat_count: An integer as the number of seats to be reserved
        """
        assert isinstance(seat_count, int) and seat_count > 0, 'Number of seats should be a positive integer'
        assert self.status == ShowTime.SALE_OPEN, 'Sale is not open'
        assert self.free_seats >= seat_count, 'Not enough free seats'
        self.free_seats -= seat_count
        if self.free_seats == 0:
            self.status = ShowTime.TICKETS_SOLD
        self.save()


class Ticket(models.Model):
    """
    Represents one or more tickets, bought by a user in an order
    """

    class Meta:
        verbose_name = 'بلیت'
        verbose_name_plural = 'بلیت'

    showtime = models.ForeignKey('ShowTime', on_delete=models.PROTECT, verbose_name='سانس')
    customer = models.ForeignKey('accounts.Profile', on_delete=models.PROTECT, verbose_name='خریدار')
    seat_count = models.IntegerField('تعداد صندلی')
    order_time = models.DateTimeField('زمان خرید', auto_now_add=True)

    def __str__(self):
        return "{} بلیت به نام {} برای فیلم {}".format(self.seat_count, self.customer, self.showtime.movie)
