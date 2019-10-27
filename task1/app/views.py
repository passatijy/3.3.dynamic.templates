from django.shortcuts import render
import csv
from collections import OrderedDict

def inflation_view(request):
    template_name = 'inflation_no_google.html'
    file = 'inflation_russia.csv'

    with open(file, encoding = 'UTF8') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=';')
        allstat =[]
        for k in reader:
            allstat.append(dict(k))
    print('stat=',allstat)
    print('stat len', len(allstat))

    for k in allstat:
        print('====')
        print(k)
    # чтение csv-файла и заполнение контекста
    context = { 'mylist': ['one', 'two', 'tree', 'four', 'five'],
                'name': 'Test', 'articles':[
                        {'title':'новости', 'content':'первые новости'},
                        {'title':'старости', 'content':'вторые новости'},
                        {'title':'разное', 'content':'куплю мопед'},
                    ],
                    'allstat': allstat
                }

    return render(request, template_name,
                  context)