<?php
$servername = "vm-g23ai2042-2_IP";
$username = "john";
$password = "John@1234";
$dbname = "testdb";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Insert record
if ($_SERVER['REQUEST_METHOD'] == 'POST') {
    $data = $_POST['data'];
    $sql = "INSERT INTO test_table (data) VALUES ('$data')";
    if ($conn->query($sql) === TRUE) {
        echo "New record created successfully";
    } else {
        echo "Error: " . $sql . "<br>" . $conn->error;
    }
}

// Display records
$sql = "SELECT id, data FROM test_table";
$result = $conn->query($sql);
if ($result->num_rows > 0) {
    while($row = $result->fetch_assoc()) {
        echo "id: " . $row["id"]. " - Data: " . $row["data"]. "<br>";
    }
} else {
    echo "0 results";
}

$conn->close();
?>

<form method="POST">
    Data: <input type="text" name="data">
    <input type="submit">
</form>
