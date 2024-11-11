<?php
// Get the database connection from database.php
$db = require_once '../service/database.php';

class User {
    private $conn;
    private $table_name = "users";

    public $id_user;
    public $name;
    public $position;
    public $password;
    public $contact_person;
    public $email;

    public function __construct($db) {
        // Assign the database connection to $this->conn
        $this->conn = $db;
    }

    // Fungsi untuk menambahkan data pengguna
    public function create() {
        $query = "INSERT INTO " . $this->table_name . " (name, position, password, contact_person, email) 
                  VALUES (:name, :position, :password, :contact_person, :email)";
        $stmt = $this->conn->prepare($query);

        // Sanitasi data
        $this->name = htmlspecialchars(strip_tags($this->name));
        $this->position = htmlspecialchars(strip_tags($this->position));
        $this->password = password_hash($this->password, PASSWORD_BCRYPT); // Hash password
        $this->contact_person = htmlspecialchars(strip_tags($this->contact_person));
        $this->email = htmlspecialchars(strip_tags($this->email));

        // Bind values
        $stmt->bindParam(":name", $this->name);
        $stmt->bindParam(":position", $this->position);
        $stmt->bindParam(":password", $this->password);
        $stmt->bindParam(":contact_person", $this->contact_person);
        $stmt->bindParam(":email", $this->email);

        if($stmt->execute()) {
            return true;
        }
        return false;
    }

    // Fungsi untuk menampilkan daftar pengguna
    public function read() {
        $query = "SELECT id_user, name, position, contact_person, email FROM " . $this->table_name;
        $stmt = $this->conn->prepare($query);
        $stmt->execute();

        return $stmt;
    }

    // Fungsi untuk memperbarui data pengguna
    public function update() {
        $query = "UPDATE " . $this->table_name . " 
                  SET name = :name, position = :position, password = :password, 
                      contact_person = :contact_person, email = :email
                  WHERE id_user = :id_user";
        $stmt = $this->conn->prepare($query);

        // Sanitasi data
        $this->name = htmlspecialchars(strip_tags($this->name));
        $this->position = htmlspecialchars(strip_tags($this->position));
        $this->password = password_hash($this->password, PASSWORD_BCRYPT); // Hash password
        $this->contact_person = htmlspecialchars(strip_tags($this->contact_person));
        $this->email = htmlspecialchars(strip_tags($this->email));
        $this->id_user = htmlspecialchars(strip_tags($this->id_user));

        // Bind values
        $stmt->bindParam(":name", $this->name);
        $stmt->bindParam(":position", $this->position);
        $stmt->bindParam(":password", $this->password);
        $stmt->bindParam(":contact_person", $this->contact_person);
        $stmt->bindParam(":email", $this->email);
        $stmt->bindParam(":id_user", $this->id_user);

        if($stmt->execute()) {
            return true;
        }
        return false;
    }

    // Fungsi untuk menghapus data pengguna
    public function delete() {
        $query = "DELETE FROM " . $this->table_name . " WHERE id_user = :id_user";
        $stmt = $this->conn->prepare($query);

        // Sanitasi data
        $this->id_user = htmlspecialchars(strip_tags($this->id_user));

        // Bind id
        $stmt->bindParam(":id_user", $this->id_user);

        if($stmt->execute()) {
            return true;
        }
        return false;
    }
}
?>
