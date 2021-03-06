from blog.models import Post,Tag,Category
from accounts.models import UserProfileInfo
from backend.models import BlogSettings
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

#Populating dictionary for all_posts, tags, categories, post years
#Will be used in blog sidebar widget
def post_widget(request):
    all_posts = Post.objects.filter(status='published').order_by('published_date')
    years = []
    tags = Tag.objects.all()
    categories = Category.objects.all()

    for post in all_posts :
        year = post.published_date.year

        if year not in years:
            years.append(year)


    return {
    'all_posts':all_posts,
    'years':years,
    'tags':tags,
    'categories':categories
    }

#site settings
def site_settings(request):
    settings = BlogSettings.objects.get(id=1)

    site_icon = settings.site_icon
    site_logo = settings.site_logo
    site_title = settings.site_title
    tagline = settings.tagline
    keywords = settings.keywords
    description = settings.description
    post_per_page = settings.post_per_page

    return {
    'site_icon':site_icon,
    'site_logo':site_logo,
    'site_title':site_title,
    'tagline':tagline,
    'keywords':keywords,
    'description':description,
     'post_per_page':post_per_page
    }


#Return profile picture of current user
def user_profile_info(request):
    profile_pic = ""
    if request.method == 'GET':
        if(request.user.is_authenticated):
            current_user = request.user
            logged_in_user = UserProfileInfo.objects.get(user=current_user)
            profile_pic = logged_in_user.profile_pic

    return{
    'profile_pic':profile_pic
    }
