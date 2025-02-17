from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone


class Author(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    surname = models.CharField(max_length=100, verbose_name="Surname")
    birth_date = models.DateField(null=True, blank=True, verbose_name="Birth date")
    profile = models.URLField(null=True, blank=True)
    deleted = models.BooleanField(default=False,verbose_name="Profile link" ,help_text='False - active author, True - inactive')
    rate = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)], default=1, verbose_name='Author rate')

    def __str__(self):
        return self.name


class Review(models.Model):
    book = models.ForeignKey('Book', null=True, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.ForeignKey('Member', null=True, on_delete=models.CASCADE, related_name='reviews')
    rating = models.FloatField(null=True, blank=True, validators=[
        MinValueValidator(1),
        MaxValueValidator(5)
    ], verbose_name="Rating")

    def __str__(self):
        return f'{self.reviewer.name}: {self.book.title}'


class Book(models.Model):
    GENRE_CHOICES = [
        ('fiction', 'Fiction'),
        ('non-fiction', 'Non-Fiction'),
        ('science fiction', 'Science Fiction'),
        ('fantasy', 'Fantasy'),
        ('mystery', 'Mystery'),
        ('biography', 'Biography')
    ]
    title = models.CharField(max_length=100, verbose_name="Name")
    category_id = models.ForeignKey('Category', null=True, verbose_name="Category ID", related_name='books', on_delete=models.CASCADE)
    author_id = models.ForeignKey('Author', null=True, on_delete=models.SET_NULL)
    member_id = models.ForeignKey('Member', null=True, on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True, verbose_name="Description")
    genre = models.CharField(max_length=100, default='N/A', choices=GENRE_CHOICES, verbose_name="Genre")
    page_count = models.IntegerField(null=True, blank=True, validators=[
        MinValueValidator(1),
        MaxValueValidator(1000)
    ], verbose_name="Page count")
    pub_date = models.DateField(null=True, blank=True, verbose_name="Pub date")
    library_id = models.ForeignKey('Library', null=True, on_delete=models.CASCADE, related_name='books')

    @property
    def rating(self):
        reviews = self.reviews.all()
        total = reviews.count()
        if total == 0:
            return 0
        total = sum(review for review in reviews)
        avg_rate =  total / total
        return round(avg_rate, 2)


    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=30, unique=True ,verbose_name="Name")

    def __str__(self):
        return self.name


class Library(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    location = models.CharField(max_length=200, verbose_name="Location")
    site = models.URLField(max_length=200, verbose_name="Site", null=True, blank=True)

    def __str__(self):
        return self.name


GENDER_CHOICES=[
    ('male', 'Male'),
    ('female', 'Female'),
]

class Member(models.Model):
    ROLE_CHOICES = [
        ('member', 'Member'),
        ('admin', 'Admin'),
        ('employee', 'Employee'),
    ]
    name = models.CharField(max_length=50, verbose_name="Name")
    surname = models.CharField(max_length=50, verbose_name="Surname")
    email = models.EmailField(max_length=100, verbose_name="Email")
    Gender = models.CharField(max_length=50, verbose_name="Gender")
    birth_date = models.DateField(null=True, blank=True, verbose_name="Birth date")
    age = models.IntegerField(null=True, blank=True,validators=[
        MinValueValidator(6),
        MaxValueValidator(120)
    ] ,verbose_name="Age")
    role = models.CharField(max_length=50, verbose_name="Role", choices=ROLE_CHOICES)
    is_active = models.BooleanField(default=True, verbose_name="Is active")
    library = models.ManyToManyField(Library, related_name='members', verbose_name="Library")
    review_id = models.ForeignKey('Review', null=True, blank=True, verbose_name="Review", on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'member'
        verbose_name = 'Member'
        verbose_name_plural = 'Members',
        get_latest_by = 'birth_date'
        indexes = [
            models.Index(fields=['name', 'surname']),
            models.Index(fields=['birth_date'], name='birth_date_idx'),
        ]






class Posts(models.Model):
    title = models.CharField(max_length=255, unique_for_date='create_date' ,verbose_name="Title")
    text = models.TextField(verbose_name="Text")
    author_id = models.ForeignKey(Author, null=True, on_delete=models.CASCADE, related_name='posts')
    moderated = models.BooleanField(default=False, verbose_name="Moderated")
    library = models.ForeignKey('Library', null=True, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateField()
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'posts'
        verbose_name = 'Posts'
        verbose_name_plural = 'Posts',
        get_latest_by = 'created_at'
        ordering = ['-created_at']


class Borrow(models.Model):
    author_id = models.ForeignKey(Author, null=True, on_delete=models.CASCADE, related_name='borrows')
    book = models.ForeignKey(Book, null=True, on_delete=models.CASCADE, related_name='borrows')
    library = models.ForeignKey('Library', null=True, on_delete=models.CASCADE, related_name='borrows')
    borrow_date = models.DateField(null=True, blank=True, verbose_name="Borrow date")
    return_date = models.DateField(null=True, blank=True, verbose_name="Return date")
    returned = models.BooleanField(default=False, verbose_name="Returned")


    def is_overdue(self):
        if self.returned:
            return False
        return self.borrow_date < timezone.now().date()

    def __str__(self):
        return self.author_id.name

    class Meta:
        db_table = 'borrows'
        verbose_name = 'Borrows'
        verbose_name_plural = 'Borrows',
        get_latest_by = 'created_at'
        ordering = ['-created_at']

class AuthorDetail(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE, related_name='details')
    biography = models.TextField()
    birth_city = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES)

    def __str__(self):
        return self.author.name



class Event(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="Title")
    description = models.TextField(null=True, blank=True, verbose_name="Description")
    date = models.DateField(null=True, blank=True, verbose_name="Date")
    library = models.ForeignKey('Library', null=True, on_delete=models.CASCADE, related_name='events')
    books = models.ManyToManyField(Book, related_name='events')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'events'
        verbose_name = 'Event'
        verbose_name_plural = 'Events',
        get_latest_by = 'date'
        ordering = ['-date']

class EventParticipant(models.Model):
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name='participants')
    member = models.ForeignKey(Member, on_delete=models.CASCADE, related_name='participants')
    registration_date = models.DateField(null=True, blank=True, verbose_name="Registration date")