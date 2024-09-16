from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,"index.html")

def removepunct(request):
    # Get the text
    djtext = request.POST.get('text', 'default')
    removepunct=request.POST.get('removepunct','off')
    capitalize=request.POST.get('capitalize','off')
    extralineremove=request.POST.get('extralineremove','off')
    extraspaceremove=request.POST.get('extraspaceremove','off')


    #Removing Punctuation
    if (removepunct == "on"):
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'removedpunct': 'Removed Punctuations', 'analyzedText': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)


        #Capitalizing
    if (capitalize=="on"):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'removedpunct': 'Change To Uppercase', 'analyzedText': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)


        #Removing Extra Line
    if (extralineremove=="on"):
        analyzed=""
        for char in djtext:
            if char!="\n" and char !='\r':
                analyzed=analyzed+char
        params = {'removedpunct': 'Removed NewLines', 'analyzedText': analyzed}
        # Analyze the text
        djtext=analyzed
        # return render(request, 'analyze.html', params)

        #Removing Extra Space
    if (extraspaceremove == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char
        params = {'removedpunct': 'Remove Extra Space', 'analyzedText': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params)
    if(extraspaceremove == "off" and extralineremove=="off" and capitalize=="off" and removepunct == "off"):
        return HttpResponse("<h1>  Please Select Atleast one Option </h1>")
    return render(request, 'analyze.html', params)
    
    
