from django.db import models
#(3) class dan object
class BaseMenu(models.Model):
    nama_menu = models.CharField(max_length=255)
    deskripsi = models.TextField()
    harga = models.DecimalField(max_digits=10, decimal_places=2)
    gambar = models.ImageField(upload_to='img/', null=True)

    # Laode Ikhwanul Uzlah_E1E122017
    class Meta:
        abstract = True
#(2) def_str_(self) merupakan fungsi unutuk mempresentasikan kelas nama_menu dari kelas BaseMenu
    def __str__(self):
        return f"{self.nama_menu}"
# (1)dari class Roti, AishTea, Saguku, dan Wang merupakan penerapan dari inheritance yg konsep OOP yang diturunkan sifatnya atau fiturnya dari kelas BaseMenu
class Roti(BaseMenu):
    pass
class AishTea(BaseMenu):
    pass

class Saguku(BaseMenu):
    pass

class Wang(BaseMenu):
    pass