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

    def __str__(self):
        return self.name


class Cinema(models.Model):
    """
    Represents a cinema (movie theater)
    """
    class Meta:
        verbose_name = 'سینما'
        verbose_name_plural = 'سینما'
    cinema_code = models.IntegerField(primary_key=True,verbose_name='کد سینما')
    name = models.CharField(max_length=50,verbose_name='نام')
    city = models.CharField(max_length=30, default='شیراز',verbose_name='شهر')
    capacity = models.IntegerField(verbose_name='گنجایش')
    phone = models.CharField(max_length=11, blank=True, verbose_name='تلفن')
    address = models.TextField(verbose_name='آدرس')

    def __str__(self):
        return '{} - {}'.format(self.name, self.city)


class ShowTime(models.Model):
    """
    Represents a movie show in a cinema at a specific time
    """
    class Meta:
        verbose_name = 'سانس'
        verbose_name_plural = 'سانس'
    movie = models.ForeignKey(to=Movie, on_delete=models.PROTECT,verbose_name='فیلم')
    cinema = models.ForeignKey(to=Cinema, on_delete=models.PROTECT,verbose_name='سینما')
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
    status = models.IntegerField(choices=status_choices,verbose_name='وضعیت')

    def __str__(self):
        return '{} - {} - {}'.format(self.movie, self.cinema, self.start_time)
