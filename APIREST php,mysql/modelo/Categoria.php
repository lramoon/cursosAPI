<?php

class CategoriaModel extends Conectar
{
    public function getCategorias()
    {
        try {
            //code...
            $conectar = parent::conexion();
            parent::set_names();
            $sql = "SELECT * FROM categoria WHERE estado=1 ORDER BY id DESC";
            $sql = $conectar->prepare($sql);
            $sql->execute();
            return $resultado = $sql->fetchAll();
        } catch (Exception $e) {
            //throw $th;            
            print("¡Error BD!: " . $e->getMessage() . "<br/>");
            die();
        }
    }

    public function getCategoria($id)
    {
        try {
            //code...
            $conectar = parent::conexion();
            parent::set_names();
            $sql = "SELECT * FROM categoria WHERE id=? AND estado=1 ORDER BY id DESC";
            $sql = $conectar->prepare($sql);
            $sql->bindValue(1, $id);
            $sql->execute();
            return $resultado = $sql->fetchAll();
        } catch (Exception $e) {
            //throw $th;            
            print("¡Error BD!: " . $e->getMessage() . "<br/>");
            die();
        }
    }

    public function insertCategoria($nombre, $descripcion)
    {
        try {
            //code...
            $conectar = parent::conexion();
            parent::set_names();
            $sql = "INSERT INTO categoria (id,nombre,observacion,estado) VALUES(NULL,?,?,'1')";
            $sql = $conectar->prepare($sql);
            $sql->bindValue(2, $nombre);
            $sql->bindValue(3, $descripcion);
            $sql->execute();
            return $resultado = 'Categoria creada exitosamente';
        } catch (Exception $e) {
            //throw $th;            
            print("¡Error BD!: " . $e->getMessage() . "<br/>");
            die();
        }
    }

    public function updateCategoria($nombre, $descripcion, $categoria_id)
    {
        try {
            //code...
            $conectar = parent::conexion();
            parent::set_names();
            $sql = "UPDATE categoria SET nombre=?,observacion=? WHERE id=?";
            $sql = $conectar->prepare($sql);
            $sql->bindValue(1, $nombre);
            $sql->bindValue(2, $descripcion);
            $sql->bindValue(3, $categoria_id);
            $sql->execute();
            return $resultado = 'Categoria actualizada exitosamente';
        } catch (Exception $e) {
            //throw $th;            
            print("¡Error BD!: " . $e->getMessage() . "<br/>");
            die();
        }
    }

    public function deleteCategoria($categoria_id)
    {
        try {
            //code...
            $conectar = parent::conexion();
            parent::set_names();
            $sql = "UPDATE categoria SET estado=0 WHERE id=?";
            $sql = $conectar->prepare($sql);
            $sql->bindValue(1, $categoria_id);
            $sql->execute();
            return $resultado = 'Categoria actualizada exitosamente';
        } catch (Exception $e) {
            //throw $th;            
            print("¡Error BD!: " . $e->getMessage() . "<br/>");
            die();
        }
    }
}
