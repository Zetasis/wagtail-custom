from wagtail.core.models import Page

class HomePage(Page):
	templates = 'home/home.html'
	max_count = 1 # Limit total home page