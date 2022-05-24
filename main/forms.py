from logging import PlaceHolder
from django import forms

class SearchAlgorithm(forms.Form):
    start_city=forms.CharField(label="Start City", max_length=200, widget=forms.TextInput(attrs={'placeholder': 'City1', 'value':'Arad'}))
    
    end_city=forms.CharField(label="End City", max_length=200, widget=forms.TextInput(attrs={'placeholder': 'City2', 'value':'Bucharest'}))
    
class StoreNewCountry(forms.Form):
    cities=forms.CharField(widget=forms.Textarea(attrs={'name':'cities', 'rows':'15', 'cols':'50', 'placeholder':"Arad,Sibiu,140\nArad,Timisoara,118\nArad,Zerind,75\nBucharest,Fagaras,211\nBucharest,Giurgiu,90\nBucharest,Pitesti,101\nBucharest,Urziceni,85\nCraiova,Dobreta,120\nCraiova,Pitesti,138\nCraiova,Rimnicu_Vilcea,146\nDobreta,Mehadia,75\nEforie,Hirsova,86\nFagaras,Sibiu,99\nHirsova,Urziceni,98\nIasi,Neamt,87\nIasi,Vaslui,92\nLugoj,Mehadia,70\nLugoj,Timisoara,111\nOradea,Zerind,71\nOradea,Sibiu,151\nPitesti,Rimnicu_Vilcea,97\nRimnicu_Vilcea,Sibiu,80\nUrziceni,Vaslui,142"})
    ,initial='Arad,Sibiu,140\nArad,Timisoara,118\nArad,Zerind,75\nBucharest,Fagaras,211\nBucharest,Giurgiu,90\nBucharest,Pitesti,101\nBucharest,Urziceni,85\nCraiova,Dobreta,120\nCraiova,Pitesti,138\nCraiova,Rimnicu_Vilcea,146\nDobreta,Mehadia,75\nEforie,Hirsova,86\nFagaras,Sibiu,99\nHirsova,Urziceni,98\nIasi,Neamt,87\nIasi,Vaslui,92\nLugoj,Mehadia,70\nLugoj,Timisoara,111\nOradea,Zerind,71\nOradea,Sibiu,151\nPitesti,Rimnicu_Vilcea,97\nRimnicu_Vilcea,Sibiu,80\nUrziceni,Vaslui,142')
    
    heuristics=forms.CharField(widget=forms.Textarea(attrs={'name':'heuristics', 'rows':'15', 'cols':'50', 'placeholder':"Arad,366\nBucharest,0\nCraiova,160\nDobreta,242\nEforie,161\nFagaras,178\nGiurgiu,77\nHirsova,151\nIasi,226\nLugoj,244\nMehadia,241\nNeamt,234\nOradea,380\nPitesti,98\nRimnicu_Vilcea,193\nSibiu,253\nTimisoara,329\nUrziceni,80\nVaslui,199\nZerind,374"}),initial='Arad,366\nBucharest,0\nCraiova,160\nDobreta,242\nEforie,161\nFagaras,178\nGiurgiu,77\nHirsova,151\nIasi,226\nLugoj,244\nMehadia,241\nNeamt,234\nOradea,380\nPitesti,98\nRimnicu_Vilcea,193\nSibiu,253\nTimisoara,329\nUrziceni,80\nVaslui,199\nZerind,374')