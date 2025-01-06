from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Receta, Comentario,Perfil
from django.db.models import Q
from .forms import ComentarioForm



# Presentar el inicio
def inicio(request):
    return render(request, 'inicio.html')
########################################################

def detalle_receta(request, receta_id):
    receta = get_object_or_404(Receta, id=receta_id)
    return render(request, 'detalle_receta.html', {'receta': receta})
############################################################

def comentario_receta(request, receta_id):
    receta = get_object_or_404(Receta, id=receta_id)
    comentarios = Comentario.objects.filter(receta=receta).order_by('-fecha')  

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.receta = receta
            comentario.save()
            return redirect('comentarios', receta_id=receta.id)  

    else:
        form = ComentarioForm()

    return render(request, 'comentarios.html', {
        'receta': receta,
        'comentarios': comentarios,
        'form': form,
    })




####################################3
#Tarejtas Receta
def tarjetas_recetas(request):
    busqueda = request.POST.get("buscar")
    recetas = Receta.objects.all() 

    if busqueda:  # Asegúrate de que hay una condición válida
        recetas = Receta.objects.filter(
            Q(nombre__icontains=busqueda) |
            Q(descripcion__icontains=busqueda) |
            Q(ingredientes__icontains=busqueda) |
            Q(tiempo_preparacion__icontains=busqueda) |
            Q(nivel_dificultad__icontains=busqueda)
        ).distinct()


    return render(request, 'tarjetas_recetas.html', {'recetas': recetas})
#########################################
# Crear receta
def crear_receta(request):
    return render(request, 'crear_receta.html')

###############
# Guardar receta

def guardar_receta(request):
    if request.method == 'POST':
        # Obteniendo los valores de los campos del formulario
        nombre = request.POST['txt_nombre']
        descripcion = request.POST.get('txt_descripcion', '')  
        ingredientes = request.POST['txt_ingredientes']
        instrucciones = request.POST['txt_instrucciones']
        tiempo_preparacion = request.POST['txt_tiempo_preparacion']
        nivel_dificultad = request.POST['nivel_dificultad']
        es_favorita = request.POST['es_favorita'] == 'True' 
        imagen = request.FILES.get('imagen', None)
        

        # Creando la nueva receta
        nuevareceta = Receta.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            ingredientes=ingredientes,
            instrucciones=instrucciones,
            tiempo_preparacion=tiempo_preparacion,
            nivel_dificultad=nivel_dificultad,
            es_favorita=es_favorita,
            imagen=imagen
            
        )

        # Mensaje de éxito
        messages.success(request, "Receta agregada correctamente")
        
        # Redirigir a la lista de recetas
        return redirect('/listado_receta')

######################################
# listar recetas
def listado_receta(request):
    busqueda = request.POST.get("buscar")
    recetasBdd = Receta.objects.all()

    if busqueda:
        recetasBdd = Receta.objects.filter(
            Q(nombre__icontains=busqueda) |
            Q(descripcion__icontains=busqueda) |
            Q(ingredientes__icontains=busqueda) |
            Q(tiempo_preparacion__icontains=busqueda) |
            Q(nivel_dificultad__icontains=busqueda) 
        ).distinct()

    return render(request, 'listado_receta.html', {'recetas': recetasBdd})

################################
#Listar comentario
def listar_comentario(request):
    comentariosBdd = Comentario.objects.all()

    return render(request, 'listar_comentario.html', {'comentarios': comentariosBdd})

##########################################################################

# Editar recetas
def editarreceta(request, id):
    receta = get_object_or_404(Receta, id=id)

    if request.method == 'POST':
        receta.nombre=request.POST['txt_nombre']
        receta.descripcion=request.POST.get('txt_descripcion', '')
        receta.ingredientes=request.POST['txt_ingredientes']
        receta.instrucciones=request.POST['txt_instrucciones']
        receta.tiempo_preparacion=request.POST['txt_tiempo_preparacion']
        receta.nivel_dificultad=request.POST['nivel_dificultad']
        receta.es_favorita=request.POST['es_favorita'] == 'True'
        receta.imagen=request.FILES.get('imagen', None)
        
        
        receta.save()
        messages.success(request, "Receta editado correctamente")
        return redirect('listado_receta')  # Redirige después de guardar

    return render(request, 'editarreceta.html', {'receta': receta})

#######################################################################
#Eliminar Recerta
def eliminar_receta(request, id):
    recetaliminar=Receta.objects.get(id=id)
    recetaliminar.delete()
    messages.success(request,"Receta Eliminada Correctamente")
    return redirect('/listado_receta')

#######################################
#Eliminar comentario
def eliminar_comentario(request, id):
    comentarioeliminar=Comentario.objects.get(id=id)
    comentarioeliminar.delete()
    messages.success(request,"Comentario Eliminado Correctamente")
    return redirect('/listar_comentario')


##########################################################################
#Guardar comentario
def guardar_comentario(request):
    if request.method == 'POST':
        # Obteniendo los valores de los campos del formulario
        autor = request.POST['txt_autor']
        contenido = request.POST['contenido']
        receta_id = request.POST.get('sel_receta')

        #validar
        receta = get_object_or_404(Receta, id=receta_id)


         # Creando la nueva receta
        nuevocomentario = Comentario.objects.create(
            autor=autor,
            contenido=contenido,
            receta=receta

        )

        # Mensaje de éxito
        messages.success(request, "Comenbtario agregada correctamente")
        return redirect('tarjetas_recetas')

#######################################################


# Crear perfil
def crear_perfil(request):
    return render(request, 'crear_perfil.html')

###############
# Guardar perfil

def guardar_perfil(request):
    if request.method == 'POST':
        # Obteniendo los valores de los campos del formulario
        nombre = request.POST['txt_nombre']
        descripcion = request.POST.get('txt_descripcion', '')  
        idioma = request.POST['idioma']
        fecha_caducidad = request.POST['txt_fecha_caducidad']
        creador = request.POST['txt_creador']

        

        # Creando la nueva perfil
        nuevoperfil = Perfil.objects.create(
            nombre=nombre,
            descripcion=descripcion,
            idioma=idioma,
            fecha_caducidad=fecha_caducidad,
            creador=creador
            
        )

        # Mensaje de éxito
        messages.success(request, "Perfil agregado correctamente")
        
        # Redirigir a la lista de recetas
        return redirect('/listado_perfil')

######################################
# listar perfil
def listado_perfil(request):
    busqueda = request.POST.get("buscar")
    perfilBdd = Perfil.objects.all()

    if busqueda:
        perfilsBdd = Perfil.objects.filter(
            Q(nombre__icontains=busqueda) |
            Q(descripcion__icontains=busqueda) |
            Q(idioma__icontains=busqueda) |
            Q(creador__icontains=busqueda) 
        ).distinct()

    return render(request, 'listado_perfil.html', {'perfiles': perfilBdd})

################################
# Editar perfil
def editarperfil(request, id):
    perfil = get_object_or_404(Perfil, id=id)

    if request.method == 'POST':
        perfil.nombre=request.POST['txt_nombre']
        perfil.descripcion=request.POST.get('txt_descripcion', '')
        perfil.idioma=request.POST['idioma']
        perfil.fecha_caducidad =request.POST['txt_fecha_caducidad']
        perfil.creador=request.POST['txt_creador']
        
        
        perfil.save()
        messages.success(request, "Perfil editado correctamente")
        return redirect('listado_perfil')  # Redirige después de guardar

    return render(request, 'editarperfil.html', {'perfil': perfil})

#######################################################################
#Eliminar Recerta
def eliminar_perfil(request, id):
    perfileliminar=Perfil.objects.get(id=id)
    perfileliminar.delete()
    messages.success(request,"Perfil Eliminada Correctamente")
    return redirect('/listado_perfil')

#######################################
