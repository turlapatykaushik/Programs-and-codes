<html>
<body>
<ol>
<?php
$con = mysql_connect('localhost', 'root', '');
mysql_select_db('my_db');

$values = mysql_query('SELECT * FROM persons');

while($row = mysql_fetch_assoc($values)){
	echo '<li>';
	echo $row['name'];
	echo '<br>';
	echo $row['comments'];
	echo '</li>';
	echo '<br>';
}

 
?>
</ol>
<form action="form.php" method="post">
name: <input type="text" name="name"><br>
comments: <textarea type="text" name="comments"></textarea><br>
<input type="submit">
</form>

</body>
</html>
<?php
if(isset($_POST['name'])){
	$con=mysqli_connect("localhost","root","","my_db");
// Check connection
if (mysqli_connect_errno()) {
  echo "Failed to connect to MySQL: " . mysqli_connect_error();
}

// escape variables for security
$name = mysqli_real_escape_string($con, $_POST['name']);
$comments = mysqli_real_escape_string($con, $_POST['comments']);

$sql="INSERT INTO Persons (name, comments)
VALUES ('$name', '$comments')";

if (!mysqli_query($con,$sql)) {
  die('Error: ' . mysqli_error($con));
}
echo "1 record added";

mysqli_close($con);
header('location: form.php');
}

?>