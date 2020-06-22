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
                form = RulesForm()
                return HttpResponse(doc)   
            else:
                newdoc.save()
                newdoc.tags.set(doc)
                #newdoc.tags.create(name='doc')
                #doc.save()
                #return HttpResponse(doc)     
                return HttpResponseRedirect('')
    else:
        form = RulesForm()

    rules = Rules.objects.all()
    return render(request, 'yararule/Add_Rules.html',
                             {'rules': rules, 'tags': tags, 'form': form}
                              )


#def Index(request):
 #   latest_rules_list = Rules.objects.order_by('id')[:5]
  #  context = {'latest_rules_list': latest_rules_list}
   # return render(request, 'yararule/index.html', context)

def Index(request):
    rules = Rules.objects.all()
    context = {
        'rules': rules
    }
    return render(request, 'yararule/listing.html', context)

def Search(request):
    query = request.GET.get('query')
    if not query:
        rules = Rules.objects.all()
    else:
        # title contains the query and query is not sensitive to case.
        rules = Rules.objects.filter(docfile__icontains=query)

    if not rules.exists():
        rules = Rules.objects.filter(tags__name__icontains=query)
    title = "Résultats pour la requête %s"%query
    context = {
        'rules': rules,
        'title': title
    }
    return render(request, 'yararule/search.html', context)

def AddTags(request):
    if request.method == 'POST':
        form = TagsForm(request.POST, request.FILES)
        if form.is_valid():
            newtags = Tags(name = request.POST['name'])

            newtags.save()
            return HttpResponseRedirect('')
    else:
        form = TagsForm()

    tags = Tags.objects.all()
    
    return render(request, 'yararule/Add_tags.html',
                             {'tags': tags,'form': form}
                              )







   