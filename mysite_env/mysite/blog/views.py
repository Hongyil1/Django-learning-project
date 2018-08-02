from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import Paginator
from .models import Blog, BlogType

# Create your views here.
# 返回列表
def blog_list(request):

    # blogs_all_list = Blog.objects.all()
    # paginator = Paginator(blogs_all_list, 10) # 10 articles per page
    # page_num = request.Get.get("page", 1) # get page number (Get requets)
    # page_of_blogs = paginator.get_page(page_num) # return 1 when invalid input

    context = {}
    context['blogs'] = Blog.objects.all()
    context['blog_types'] = BlogType.objects.all()
    context['blogs_count'] = Blog.objects.all().count()
    return render_to_response('blog/blog_list.html', context=context)

def blog_detail(request, blog_pk):
    context = {}
    context['blog'] = get_object_or_404(Blog, pk=blog_pk)
    return render_to_response('blog/blog_detail.html', context=context)

def blogs_with_type(request, blog_type_pk):
    context = {}
    blog_type = get_object_or_404(BlogType, pk=blog_type_pk)
    context['blog_type'] = blog_type
    context['blogs'] = Blog.objects.filter(blog_type=blog_type)
    context['blog_types'] = BlogType.objects.all()
    return render_to_response('blog/blogs_with_type.html', context=context)
