from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template, Context, loader
from family_db.models import Member
from datetime import datetime


def new_member(self, name: str = 'name', last_name: str = 'name', birthday: datetime = 1 - 1 - 1999,
               kinship_deg: int = 0, icecream_flavor: str = None):
    template = loader.get_template('newmember_template.html')

    member = Member(name=name, last_name=last_name, birthday=birthday, kinship_deg=kinship_deg,
                    icecream_flavor=icecream_flavor)
    member.save()

    context_dict = {
        'member': member,
    }
    render = template.render(context_dict)
    return HttpResponse(render)


def members(request):
    template = loader.get_template('members_template.html')
    members = Member.objects.all()

    print('Members', type(members), '\n', members)
    context_dict = {
        'members': members
    }
    return HttpResponse(template.render(context_dict))


def get_member_by_name(self, name: str):
    template = loader.get_template('get_member_by_name.html')
    member = Member.objects.all().filter(name=name)

    context_dict = {
        'member': member
    }
    return HttpResponse(template.render(context_dict))
