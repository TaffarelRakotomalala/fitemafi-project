from django.shortcuts import render, redirect
from blog.models import Droit, Membres, Utilisateur
from .forms import FormMembres, FormDroit, UserForm, EditUserForm
from .filters import DroitFilter
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages



def register_user(request):
    sauvegarde = False
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid:
            form.save()
            sauvegarde = True
            return render(request, 'blog/register_user.html', locals())
    else:
        form = UserForm()
    return render(request, 'blog/register_user.html', locals())



def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        membre = authenticate(request, username = username, password = password)
        if membre is not None:
            login(request, membre)
            return redirect(record)
        else:
            a = "Nom d'utilisateur ou Mot de Passe Invalide"
    return render(request, 'blog/login_user.html', locals())

def logout_user(request):
    logout(request)
    return redirect(login_user)


def config_user(request):
    ins = request.user.utilisateur
    if request.method == 'POST':
        form = EditUserForm(request.POST, request.FILES, instance=ins)
        if form.is_valid:
            form.save()
            return redirect(record)
    else:
        form = EditUserForm(instance=ins)
    return render(request, 'blog/config_user.html', locals())

def test(request):
    resultat1 = Droit.objects.all()
    resultat2 = Membres.objects.all()
    for res in resultat1:
        if res.droit_adhension:
            res.droit_adhension = 'P'
        else:
            res.droit_adhension = 'NP'
            
        if res.droit_annuel:
            res.droit_annuel = 'P'
        else:
            res.droit_annuel = 'NP'
        
        if res.droit_reception:
            res.droit_reception = 'P'
        else:
            res.droit_reception = 'NP'
    if request.method == 'POST':
        a = FormDroit(request.POST)
        if a.is_valid:
            ok = True
    else:
        a = FormDroit()
    return render(request, 'blog/test.html', locals())


# ------------ Quelques fonctions ----------------------

#convertion True/False
def convertir(T):
    for res in T:
        if res.droit_adhension:
            res.droit_adhension = 'P'
        else:
            res.droit_adhension = 'NP'
                
        if res.droit_annuel:
            res.droit_annuel = 'P'
        else:
            res.droit_annuel = 'NP'
            
        if res.droit_reception:
            res.droit_reception = 'P'
        else:
            res.droit_reception = 'NP'

#Somme Droit
def somme_droit(L):
    somme1 = 0
    somme2 = 0
    somme3 = 0
    L = Droit.objects.all()
    for s in L:
        if s.droit_adhension:
            somme1 = somme1 + 4000
        else:
            somme1 = somme1
        
        if s.droit_annuel:
            somme2 = somme2 + 3000
        else:
            somme2 = somme2
        
        if s.droit_reception:
            somme3 = somme3 + 5000
        else:
            somme3 = somme3

    return (somme1 + somme2 + somme3)

# effectifs des membres qui ont payé leurs droits.
def da_PNP(L):
    isa1 = 0
    L = Droit.objects.all()
    for s in L:
        if s.droit_adhension:
            isa1 = isa1 + 1
    return isa1

def dan_PNP(L):
    isa2 = 0
    L = Droit.objects.all()
    for s in L:
        if s.droit_annuel:
            isa2 = isa2 + 1
    return isa2

def dr_PNP(L):
    isa3 = 0
    L = Droit.objects.all()
    for s in L:
        if s.droit_reception:
            isa3 = isa3 + 1
    return isa3

#-------------------------------------------------------------------------
@login_required(login_url = '../login_user/')
def record(request):
    resultat1 = Membres.objects.all().order_by('id')
    resultat2 = Droit.objects.all()
    if request.method == 'POST':
        form1 = FormMembres(request.POST)
        if form1.is_valid:
            envoi = True
            form1.save()
            a = len(resultat1)
            messages.success(request, u' Sauvegarde avec succès ! :)')
            return redirect(record)
    else:
        envoi = False
        form1 = FormMembres()
    a = len(resultat1)
    somme = somme_droit(resultat2)
    isa1 = da_PNP(resultat2)
    isa2 = dan_PNP(resultat2)
    isa3 = dr_PNP(resultat2)
    return render(request, 'blog/main.html', locals())

@login_required(login_url = '../login_user/')
def record2(request):
    resultat2 = Droit.objects.all().order_by('id_membres')  
    if request.method == 'POST':
        form2 = FormDroit(request.POST)
        if form2.is_valid:
            ok = True
            form2.save()
            b = len(resultat2)
            messages.success(request, u' Sauvegarde avec succès ! :)')
            return redirect(record2)
    else:
        filtre = DroitFilter(request.GET, queryset=resultat2)
        resultat2 = filtre.qs
        form2 = FormDroit()
    b = len(resultat2)
    convertir(resultat2)
    somme = somme_droit(resultat2)
    isa1 = da_PNP(resultat2)
    isa2 = dan_PNP(resultat2)
    isa3 = dr_PNP(resultat2)
    return render(request, "blog/record.html", locals())

@login_required(login_url = '../login_user/')
def find(request):
    T1 = []
    T2 = []
    T3 = []
    T4 = []
    resultat2 = Droit.objects.all()
    if request.method == "POST":
        rech = request.POST['rchrch']
        resultat1 = Membres.objects.filter(prenoms__contains = '{}'.format(rech))
        for res2 in resultat1:
            resultat2 = Droit.objects.filter(id_membres = res2.id)
            convertir(resultat2)
            for res3 in resultat2:
                T1.append(res3.id_membres)
                T2.append(res3.droit_adhension)
                T3.append(res3.droit_annuel)
                T4.append(res3.droit_reception)
        T = [T1, T2, T3, T4]
        b = len(T1)
        return render(request, "blog/find.html", locals())
    b = len(resultat2)
    somme = somme_droit(resultat2)
    isa1 = da_PNP(resultat2)
    isa2 = dan_PNP(resultat2)
    isa3 = dr_PNP(resultat2)
    convertir(resultat2)
    return render(request, "blog/find.html", locals())

@login_required(login_url = '../login_user/')
def rename(request):
    resultat1 = Membres.objects.all()
    resultat2 = Droit.objects.all()
    if request.method == 'POST':
        #Pour les membres :
        id_mbr = request.POST['id_mbr']
        nom_mbr = request.POST['nom_mbr']
        prenom_mbr = request.POST['prenom_mbr']
        adresse_mbr = request.POST['adresse_mbr']
        Membres.objects.filter(id = id_mbr).update(nom = '{}'.format(nom_mbr), prenoms = '{}'.format(prenom_mbr), adresse = '{}'.format(adresse_mbr))

        #Pour les droits
        da_mbr = request.POST['da_mbr']
        dan_mbr = request.POST['dan_mbr']
        dr_mbr = request.POST['dr_mbr']
        Droit.objects.filter(id_membres = id_mbr).update(droit_adhension = '{}'.format(da_mbr), droit_annuel = '{}'.format(dan_mbr), droit_reception = '{}'.format(dr_mbr))
        resultat1 = Membres.objects.all()
        messages.success(request, u' Edition avec succès  ! :)')
        return redirect(rename)
    a = len(resultat1)
    somme = somme_droit(resultat2)
    isa1 = da_PNP(resultat2)
    isa2 = dan_PNP(resultat2)
    isa3 = dr_PNP(resultat2)
    return render(request, "blog/rename.html", locals())

@login_required(login_url = '../login_user/')
def clean(request):
    resultat2 = Droit.objects.all().order_by('id_membres')
    if request.method == "POST":
        suppr = request.POST["suppr"]
        Membres(suppr).delete()
        #effacer = request.POST["s_tout"]
        #Droit.objects.filter(id_membres = suppr).delete()
        """if effacer == 1:
            membres = Membres.objects.all()
            membres.delete()"""
        resultat2 = Droit.objects.all().order_by('id_membres')
        convertir(resultat2)
        b = len(resultat2)
        messages.success(request, u' Suppression avec succès ! :)')
        return redirect(clean)
    convertir(resultat2)
    b = len(resultat2)
    somme = somme_droit(resultat2)
    isa1 = da_PNP(resultat2)
    isa2 = dan_PNP(resultat2)
    isa3 = dr_PNP(resultat2)
    return render(request, "blog/delete.html", locals())

@login_required(login_url = '../login_user/')
def histogramme(request):
    resultat2 = Droit.objects.all()
    isa1 = da_PNP(resultat2)
    isa2 = dan_PNP(resultat2)
    isa3 = dr_PNP(resultat2)
    data = [isa1, isa2, isa3]
    return render(request, "blog/histo.html", locals())