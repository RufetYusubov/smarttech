from django.shortcuts import render,redirect
from  ultracomp.models import LaptopModel, CommentModel


def home(request):
    laptops = LaptopModel.objects.order_by("price")
    context = {
        "laptops" : laptops,
    }
    return render(request, 'home.html', context)
#----------------------------------------------------------------
def details(request,id):
    laptop = LaptopModel.objects.get(id=id)
    laptop_comments = CommentModel.objects.filter(
        laptop = laptop,
        parent = None
    )

    context = {
        "laptop" : laptop,
        "laptop_comments" : laptop_comments
    }
    
    if request.user.is_authenticated :
         user_comments = CommentModel.objects.filter(
            user = request.user
        ) 
         context["user_comments"] = user_comments


    if request.method == "POST":
        choice = request.POST.get("choice")
        if choice == "comment":
            comment = request.POST.get("comment")
            laptop_id = request.POST.get("laptop_id")

            laptop = LaptopModel.objects.get(id=laptop_id)

            CommentModel.objects.create(
                user = request.user,
                laptop = laptop,
                comment = comment
            )
        elif choice == "reply":
            reply = request.POST.get("reply")
            laptop_id = request.POST.get("laptop_id")

            laptop = LaptopModel.objects.get(id=laptop_id)

            comment_id = request.POST.get("comment_id")
            comment = CommentModel.objects.get(id=comment_id)

            CommentModel.objects.create(
                user = request.user,
                laptop = laptop,
                comment = reply,
                parent = comment
            )
        
        return redirect("details", id=id)
    
    return render(request, 'details.html', context)
#---------------------------------------------------------------------------------
def deleteComment(request,id):
    comment = CommentModel.objects.get(id=id)
    comment.delete()
    return redirect("details", id = comment.laptop.id)
