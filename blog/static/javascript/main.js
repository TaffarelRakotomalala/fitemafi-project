var x = 0;

function barre(){
    document.getElementById("demo").innerHTML = x+=1;
}

//date

var tableaumois = new Array(
    'Janvier',
    'Février',
    'Mars',
    'Avril',
    'Mai',
    'Juin',
    'Juillet',
    'Août',
    'Septembre',
    'Octobre',
    'Novembre',
    'Décembre'
);

var tableaujour = new Array(
    'Dimanche',
    'Lundi',
    'Mardi',
    'Mercredi',
    'Jeudi',
    'Vendredi',
    'Samedi',
);



function dateheure(){
    var DateGlobal = new Date();
    var annee = DateGlobal.getFullYear();
    var mois = DateGlobal.getMonth();
    var jour = DateGlobal.getDay();
    var numerojour = DateGlobal.getDate()
    var heure = DateGlobal.getHours()
    var minute = DateGlobal.getMinutes()
    var seconde = DateGlobal.getSeconds()

    if (heure < 10){
        heure = "0"+heure;
    }

    if (minute < 10){
        minute = "0"+minute;
    }
    if (seconde < 10){
        seconde = "0"+seconde
    }
 
    mois = tableaumois[mois]
    jour = tableaujour[jour]

    document.getElementById("heure_date").innerHTML = jour+" "+numerojour+ " " +mois+ " " +annee
    +" à "+ heure+ ":"+minute+":"+seconde;
}

function ttdateheure(){
    var delai = 1000;
    dateheure();
    setInterval('dateheure()', delai);
}