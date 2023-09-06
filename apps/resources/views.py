from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.db.models import Count, Avg

from .models import Resources, Category, Review, Rating
from apps.user.models import User
from . import utils

# Create your views here.

def home_page(request):
    cnt = Resources.objects.all().count()
    cnt_active_users = User.objects.filter(is_active__iexact='true').count()
    cnt_per_cat = Resources.objects.values('cat_id__cat').annotate(cnt=Count('cat_id'))
    
    context = {
        'cnt':cnt,
        'cnt_active_users': cnt_active_users,
        'cnt_per_cat': cnt_per_cat,
    }
    
    return render(request=request,template_name='resources/home.html', context=context)

def resource_detail(request,id):
    res = (
        Resources.objects.select_related('user_id','cat_id')
        .prefetch_related('tag')
        .get(pk=id)
        )
    review = Review.objects.filter(resources_id_id=id)
    
    avg_rate = Rating.objects.filter(resources_id_id=res.id).aggregate(Avg('rate'))
    #avarage = res.rating_set.aggregrate(Avg('rate'))
    
    context = {
        'res': res,
        'review': review.count(),
        'avg_rate': avg_rate

               }
    return render(request=request, 
                  template_name='resources/resource_details.html',
                  context= context)


def home_page_old(request):
    cnt = Resources.objects.all().count()
    cnt_active_users = User.objects.filter(is_active__iexact='true').count()
    
    # categories = [cate.cat for cate in Category.objects.all()]
    # result_cat = ""
    # for cat in categories:
    #     res = Resources.objects.filter(cat_id__cat=cat).count()
    #     result_cat += f"<li> {cat}: {res}</li>"

    cnt_per_cat = Resources.objects.values('cat_id__cat').annotate(cnt=Count('cat_id'))
    response = f"""
    <html>
    
        <h1>Welcome to ResourceShare</h1>
        <h2> All users:</h2>
        <p>{cnt_active_users} users and counting!</p>
        <h2>Resources per category</h2>
        <ol>
            {utils.generate_count_list(cnt_per_cat)}
        </ol>
 
    </html>
    
    """
    return HttpResponse(response)
    

def resource_detail_old(request, id):
    res = (
        Resources.objects.select_related('user_id','cat_id')
        .prefetch_related('tag')
        .get(pk=id)
        )

    
    response = f"""
        <html>
            <h1>{res.title}</h1>
            <p><b>User:</b> {res.user_id.username}</p>
            <p><b>Link:<b> {res.link}</p>
            <p><b>Description:<b> {res.description}</p>
            <p><b>Category:<b> {res.cat_id.cat}</p>
            <p><b>Tags:<b> {res.all_tags()}</p>
        </html>
    
    """
    return HttpResponse(response)



class HomePage(TemplateView):
    template_name = 'home_page.html'