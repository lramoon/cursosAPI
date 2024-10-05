<?php

class Conectar
{
    protected $db;

    protected function conexion()
    {
        try {

            return $conectar = $this->db = new PDO('mysql:localhost;dbname=cursoapi', 'root', '');
        } catch (Exception $e) {
            //throw $th;
            print("¡Error BD!: " . $e->getMessage() . "<br/>");
            die();
        }
    }

    public function set_names()
    {
        return $this->db->query("SET NAMES 'utf8'");
    }
}
