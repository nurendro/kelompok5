from django.contrib import admin
from django.utils.html import format_html
# E1E122025_ NUR FADILLAH
from .models import Roti, AishTea, Saguku, Wang, TelaTela

# Uzlah merubah import dan register Menu menjadi Roti dan RotiAdmin sekaligus setting untuk tampilkan gambar di admin
# @admin.register(Roti)
# class RotiAdmin(admin.ModelAdmin):
#     list_display = ['nama_menu', 'deskripsi', 'harga', 'display_image']

#     def display_image(self,obj):
#         return format_html('<img src="{}" width=100 />',obj.gambar.url)

#     display_image.short_description="Gambar"

# @admin.register(AishTea)
# class AishTeaAdmin(admin.ModelAdmin):
#     list_display = ['nama_menu', 'deskripsi', 'harga', 'display_image']

#     def display_image(self,obj):
#         return format_html('<img src="{}" width=100 />',obj.gambar.url)

#     display_image.short_description="Gambar"
    
# # E1E122070_MUHAMMAD RAIHAN PUTRA KHAMIL
# @admin.register(Saguku)
# class SagukuAdmin(admin.ModelAdmin):
#     list_display = ['nama_menu', 'deskripsi', 'harga', 'display_image']

#     def display_image(self,obj):
#         return format_html('<img src="{}" width=100 />',obj.gambar.url)

#     display_image.short_description="Gambar"

# @admin.register(Wang)
# class WangAdmin(admin.ModelAdmin):
#     list_display = ['nama_menu', 'deskripsi', 'harga', 'display_image']

#     def display_image(self,obj):
#         return format_html('<img src="{}" width=100 />',obj.gambar.url)

#     display_image.short_description="Gambar"

# Agar syntaxnya menjadi lebih singkat

#merupakan konsep decorator yang fungsinya untuk mendaftarkan class model di admin interface Django. BaseMenuAdmin adalah class yang memperluas admin.ModelAdmin dan menentukan tata letak tampilan admin untuk model-menu.

admin.site.register(TelaTela)
@admin.register(Roti, AishTea, Saguku, Wang)
class BaseMenuAdmin(admin.ModelAdmin):
    list_display = ["nama_menu","deskripsi","_harga","display_image"]

    def display_image(self,obj):
        return format_html('<img src="{}" width=100 />',obj.gambar.url)

    display_image.short_description="Gambar"


#tina melakukan perubahan