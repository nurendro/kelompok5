# Nurendro Hardjo_E1E122133
from django.urls import path
from .views import index, roti, aishtea, saguku, wang, telatela
# Uzlah merubah import dan path menu menjadi Roti / roti 
urlpatterns = [
    path('', index, name="index"),
     # Yabrina Angelika Rantelili_E1E122081
    path('roti/', roti, name='roti'),
    path('aishtea/', aishtea, name='aishtea'),
    path('saguku/', saguku, name='saguku'),
    path('wang/', wang, name='wang'),
    path('telatela/', telatela, name='telatela'),
]
