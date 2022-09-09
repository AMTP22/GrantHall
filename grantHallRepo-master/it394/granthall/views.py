from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import ItemForm
from django.http import HttpResponseRedirect
from .models import Item

def index(request):
    template = loader.get_template('granthall/index.html') #Get the homepage template
    context= {}
    return(HttpResponse(template.render(context, request))) #Render the template with the context

    
def additem(request):
    
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            #Add the item to the database
            newitem = form.save()
            return HttpResponseRedirect('/granthall')
    else:

        form = ItemForm()

    return render(request, 'granthall/additem.html', {'form': form})

def showitems(request):
    items = Item.objects.all()
    context = {'items' : items}
    return render(request, 'granthall/items.html', context)
