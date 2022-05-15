from django.http import HttpResponse
from datetime import datetime
from django.template import Template, Context, loader
from coder_app.models import Group
from Family_db.models import Member


def saludo(request):  # Nuestra primera vista :)
    return HttpResponse("Hola Django - Coder")


def segunda_vista(request):
    return HttpResponse("<br><br>Ya entendimos esto, es muy simple :) ")


def birth_year(self, age):
    current_year = datetime.now().year
    birth_year = current_year - int(age)
    return HttpResponse(f'My year of birth is {birth_year}')


def diaDeHoy(request):
    dia = datetime.now()

    documentoDeTexto = f"Hoy es día: <br> {dia}"

    return HttpResponse(documentoDeTexto)


def miNombreEs(self, nombre):
    documento_de_texto = f"Mi nombre es: <br><br>  {nombre}"

    return HttpResponse(documento_de_texto)


def calculate_age(self, birth):
    birth = datetime.strptime(birth, '%Y-%m-%d')
    print(type(birth))
    delta = datetime.now() - birth
    days_by_year = 365.25

    years = int(delta.days // days_by_year)
    months = int((delta.days % days_by_year) // 30)
    days = int((delta.days % days_by_year) % 30)

    http_response = f'''
        <br><br>
        I'm {years} years, {months} months, and {days} days old.
        '''
    return HttpResponse(http_response)


def probandoTemplate(self):
    miHtml = open('C:/Users/yo/PycharmProjects/Test1.1.1/pycharmtut/pycharmtut/panitllas/plantilla1.html')

    plantilla = Template(miHtml.read())  # Se carga en memoria nuestro documento, template1
    ##OJO importar template y contex, con: from django.template import Template, Context

    miHtml.close()  # Cerramos el archivo

    miContexto = Context()  # EN este caso no hay nada ya que no hay parametros, IGUAL hay que crearlo

    documento = plantilla.render(miContexto)  # Aca renderizamos la plantilla en documento

    return HttpResponse(documento)

def template_using_contxt(self, name: str = 'name', last_name: str = 'Last_name'):
    miHtml = open("C:/Users/yo/PycharmProjects/Test1.1.1/pycharmtut/pycharmtut/panitllas/Template1.html")
    template = Template(miHtml.read())
    miHtml.close()

    context_dict = {
        'name': name,
        'last_name': last_name,
        'now': datetime.now(),
        'grades': [6,4,8,12,7,9,3],
    }

    my_context = Context(context_dict)
    documento = template.render(my_context)

    return HttpResponse(documento)

def template_loader(self, name: str = 'name', last_name: str = 'Last_name'):
    template = loader.get_template('Template2.html')

    context_dict = {
        'name': name,
        'last_name': last_name,
        'now': datetime.now(),
        'grades': [6, 4, 8, 12, 7, 9, 3],
    }
    documento = template.render(context_dict)

    return HttpResponse(documento)


def group_data(self, name: str = 'group', code: int = 0):
    template = loader.get_template('group_template.html')

    group = Group( name=name, code=code)
    group.save()

    context_dict = {
        'group': group
    }
    render = template.render(context_dict)
    return HttpResponse(render)


def new_member(self, name: str = 'name', last_name: str = 'name', birthday: datetime = 1-1-1999, kinship_deg: int = 0, icecream_flavor: str = None):
    template = loader.get_template('group_template.html')

    member = Member(name, last_name, birthday, kinship_deg, icecream_flavor)
    member.save()

    context_dict = {
        'member': member,
    }
    render = template.render(context_dict)
    return HttpResponse(render)
