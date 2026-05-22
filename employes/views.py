from django.shortcuts import render
from .models import Employe

def liste_employes(request):
    employes = Employe.objects.all()
    return render(request, 'employes/liste.html', {'employes': employes})

def ajouter_employe(request):
    if request.method == "POST":
        nom = request.POST.get("nom")
        poste = request.POST.get("poste")
        salaire = request.POST.get("salaire")
        date_embauche = request.POST.get("date_embauche")
        

        Employe.objects.create(
            nom=nom,
            poste=poste,
            salaire=salaire,
            date_embauche=date_embauche,
            
        )

    return redirect('liste_employes')

from django.shortcuts import get_object_or_404, redirect

def modifier_employe(request, id):
    employe = Employe.objects.get(id=id)

    if request.method == "POST":
        employe.nom = request.POST['nom']
        employe.poste = request.POST['poste']
        employe.salaire = request.POST['salaire']
        employe.save()
        return redirect('liste_employes')

    return render(request, 'employes/modifier.html', {'employe': employe})


def supprimer_employe(request, id):
    employe = get_object_or_404(Employe, id=id)

    if request.method == "POST":
        employe.delete()
        return redirect('liste_employes')

    return redirect('liste_employes')