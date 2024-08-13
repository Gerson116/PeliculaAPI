
from fastapi import APIRouter, Response
from fastapi.responses import JSONResponse

from ..models.usuario import usuario

ROUTER_USUARIO_CONTROLLER = APIRouter()

@ROUTER_USUARIO_CONTROLLER.get('/api/listado-usuario/{pagina_seleccionada}/{pagina_actual}', summary='listarUsuario')
async def listar_usuario(pagina_seleccionada: int, pagina_actual: int):
    return Response(status_code=400)

@ROUTER_USUARIO_CONTROLLER.get('/api/buscar-pelicula-por-id/{pelicula_id}', summary='buscarPeliculaPorId')
async def buscar_pelicula_por_id(pelicula_id: int):
    return Response(status_code=400)

@ROUTER_USUARIO_CONTROLLER.post('/api/agregar_usuario', summary='agregarUsuario')
async def agregar_usuario(pagina_seleccionada: int, pagina_actual: int):
    return Response(status_code=400)

@ROUTER_USUARIO_CONTROLLER.patch('/api/editar-pelicula/{pelicula_id}', summary='editarPelicula')
async def editar_pelicula(pelicula_id: int):
    return Response(status_code=400)

@ROUTER_USUARIO_CONTROLLER.patch('/api/editar-pelicula/{pelicula_id}', summary='editarPelicula')
async def editar_pelicula(pelicula_id: int):
    return Response(status_code=400)