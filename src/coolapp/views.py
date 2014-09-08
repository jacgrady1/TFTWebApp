from django.shortcuts import render,render_to_response,RequestContext


# Create your views here.
def home(request):
                      
    return render_to_response("home.html",
                              locals(),
                              context_instance=RequestContext(request))
def about(request):
                      
    return render_to_response("about.html",
                              locals(),
                              context_instance=RequestContext(request))
def work(request):
                      
    return render_to_response("work.html",
                              locals(),
                              context_instance=RequestContext(request))
def contact(request):
                      
    return render_to_response("contact.html",
                              locals(),
                              context_instance=RequestContext(request))
def xiaozu(request):
                      
    return render_to_response("xiaozu.html",
                              locals(),
                              context_instance=RequestContext(request))
