from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from yararule.models import Rules, RulesForm, Tags, TagsForm
from django.http import HttpResponse
from django.conf import settings
import os 
import os.path
from django.template import RequestContext
from django.template import loader
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage





def AddRules(request):
    tags = Tags.objects.all()
    if request.method == 'POST':
        form = RulesForm(request.POST, request.FILES)
        if form.is_valid():
            doc = request.POST['tags']
            newdoc = Rules(docfile = request.FILES['docfile'])
            newdocs = format(newdoc.docfile.name)
            #destination = '/home/dethie/rule/rule/media/biblio/'
            destination = settings.MEDIA_ROOT + '/biblio/'
            if os.path.isfile(destination + newdocs):
                message = "existe deja"   
            else:
                message = 'Success ajoute une nouvelle regle'
                newdoc.save()
                newdoc.tags.set(doc)
                #newdoc.tags.create(name='doc')
                #doc.save()
                #return HttpResponse(doc)     
                return HttpResponseRedirect('')
    else:
        form = RulesForm()
        message = 'Upload as many files as you want!'

    rules = Rules.objects.all()
    return render(request, 'yararule/Add_Rules.html',
                             {'message': message, 'rules': rules, 'tags': tags, 'form': form}
                              )


#home
def Index(request):
    rules = Rules.objects.all()
    context = {
        'rules': rules
    }
    return render(request, 'yararule/listing.html', context)



#search by name and tags
def Search(request):
    query = request.GET.get('query')
    if not query:
        rules = Rules.objects.all()
    else:
        # title contains the query and query is not sensitive to case.
        rules = Rules.objects.filter(docfile__icontains=query)

    if not rules.exists():
        rules = Rules.objects.filter(tags__name__icontains=query)
    title = "Resultat de la recherche" 
    context = {
        'rules': rules,
        'title': title
    }
    return render(request,'yararule/search.html', context)



#add tags to the list
def AddTags(request):
    if request.method == 'POST':
        form = TagsForm(request.POST, request.FILES)
        if form.is_valid():
            newtags = Tags(name = request.POST['name'])

            newtags.save()
            return HttpResponseRedirect('../addrules/')
    else:
        form = TagsForm()

    tags = Tags.objects.all()
    
    return render(request, 'yararule/Add_Rules.html',
                             {'tags': tags,'form': form}
                              )



#add tags to a docfile
def Taging(request):
    rules = Rules.objects.all()
    tags = Tags.objects.all()
    
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
    return render(request, 'yararule/taging.html',
                             {'tags': tags,'rules': rules}
                              )



def Upload(request):
    context = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['docfile']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)
    return render(request, 'yararule/upload.html', context)







   