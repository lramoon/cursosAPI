<?php
// HEADER PARA ENVIAR LA ESTRUCTURA E INTERPRETARLA COMO JSON
header('Content-Type: application/json');
// llamada de archivos
require_once("../config/conexion.php");
require_once("../modelo/Categoria.php");
// llamada de clase
$categoria = new CategoriaModel();

// OBTENER EL DATO CON POST
$body = json_decode(file_get_contents("php://input"), true);

switch ($_GET['op']) {
    case 'GetALL':
        # code...
        $datos = $categoria->getCategorias();
        return json_encode($datos);
        break;
    case 'GetCategoria':
        # code...
        $datos = $categoria->getCategoria($body['cat_id']);
        return json_encode($datos);
        break;
    case 'InsertCategoria':
        # code...
        $datos = $categoria->insertCategoria($body['nombre'], $body['descripcion']);
        return json_encode($datos);
        break;
    case 'UpdateCategoria':
        # code...
        $datos = $categoria->updateCategoria($body['nombre'], $body['descripcion'], $body['cat_id']);
        return json_encode($datos);
        break;
    case 'DeleteCategoria':
        # code...
        $datos = $categoria->deleteCategoria($body['cat_id']);
        return json_encode($datos);
        break;

    default:
        # code...
        break;
}
