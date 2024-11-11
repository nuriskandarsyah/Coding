<?php

require_once '../service/database.php';
require_once '../models/User.php';

class UserController {
    private $user;

    public function __construct($db)
    {
        $this->user = new User($db);
    }

    //show up all the users
    public function index() {
        $stmt = $this->user->read();
        $users = $stmt->fetchall(PDO::FETCH_ASSOC);
        include '../views/user/index.php';
    }

    //add the new user
    public function create() {
        include '../views/user/create.php';
    }

    //save the new user
    public function store() {
        $this->user->name = $_POST['name'];
        $this->user->position = $_POST['position'];
        $this->user->password = $_POST['password'];
        $this->user->contact_person = $_POST['contact_person'];
        $this->user->email = $_POST['email'];

        if ( $this->user->create() ) {
            header("Location: /user/index");
            exit;
        }else {
            echo "Error: Data tidak berhasil ditambahkan.";
        }
    }

    //edit user
    public function edit($id) {
        $this->user->id_user = $id;
        $user = $this->user->read()->fetch(PDO::FETCH_ASSOC);
        include '../views/user/edit.php';
    }

    //saving update user data
    public function update($id) {
        $this->user->id_user; $id;
        $this->user->name = $_POST['name'];
        $this->user->position = $_POST['position'];
        $this->user->password = $_POST['password'];
        $this->user->contact_person = $_POST['contact_person'];
        $this->user->email = $_POST['email'];

        if ($this->user->update()) {
            header("Location: /user/index");
            exit;
        } else {
            echo "Error: Data tidak berhasil diperbarui.";
        }
    }

    //deleting data
    public function delete($id) {
        $this->user->id_user = $id;
        if ($this->user->delete()) {
            header("Location: /user/index");
        }else {
            echo "Error: Data is not deleted";
        }
    }
}

// Routing
if (isset($_Get['action'])) {
    $action = $_GET['action'];
    $controller = new UserController($db);
    
    if ($action == 'index') {
        $controller->index();
    } elseif ($action == 'create') {
        $controller->create();
    } elseif ($action == 'store') {
        $controller->store();
    } elseif ($action == 'edit' && isset($_GET['id'])) {
        $controller->edit($_GET['id']);
    } elseif ($action == 'update' && isset($_GET['id'])) {
        $controller->update($_GET['id']);
    } elseif ($action == 'delete' && isset($_GET['id'])) {
        $controller->delete($_GET['id']);
    }
}