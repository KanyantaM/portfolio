from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.core.mail import send_mail
from .models import Blog, BlogComment, Owner, ProjectDetails



# Create your views here.

def index(request):
   owner = Owner.objects.first()
   if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        from_email = request.POST.get('email')
        name = request.POST.get('name')
        
        if subject and message and from_email and name:
            full_message = f"Message from {name} ({from_email}):\n\n{message}"
            try:
                send_mail(subject, full_message, from_email, [f'{owner.email}'])
                return HttpResponse('Email sent successfully')
            except Exception as e:
                return HttpResponse(f'Error sending email: {e}')
        else:
            return HttpResponse('All fields are required')
   return render(request, "home/sections.html",{
      'owner': owner
   })

def blogPost(request, blog_id):
   blog_post = Blog.objects.get(pk = blog_id)
   recent_posts = Blog.objects.exclude(pk = blog_id).all()[:5]

   if request.method == "POST":
      author_name = request.POST["name"]
      author_image = request.POST["image"]
      comment = request.POST["comment"]
      author_email = request.POST["email"]
      new_comment = BlogComment(
         author_name = author_name,
         author_image = author_image,
         comment = comment,
         author_email = author_email,
         blog = blog_post,
         )
      new_comment.save()
      blog_post.comments.add(new_comment)
      return HttpResponseRedirect(reverse("blog-post", args=(blog_id)))

   return render(request, 'blog/blogpost.html', {
      'blog_id' : blog_id,
      'blog_post' : blog_post,
      'comments' : blog_post.comments.all(),
      'recent_posts': recent_posts,
      'tags' : blog_post.tags.all()
   })

def projectDetails(request, project_id):
   project = ProjectDetails.objects.get(pk = project_id)
   return render(request, 'project/portfolio_details.html', {
      'project' : project,
      })


# def digReplies(commentParent):
#    rel = {}
#    def helperComment(comment):
#       if comment not in rel:
#          rel[comment] = []
#       for child in comment.get('replies', []):
#          rel[comment].append(child)
#          helperComment(child)
#    for parent in commentParent:
#       helperComment(parent)
#    return rel

#