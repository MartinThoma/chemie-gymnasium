<?
header('content-type: text/html; charset=iso-8859-1');
require '../admin/db.inc.php';


$lernen = select_learn($_POST['cat']);
if(urldecode($_POST['output']) != "Klicke auf 'Nächstes' um zu starten"){
    $sql = sprintf("SELECT * FROM summenformeln WHERE summenformel='%s' AND name='%s'",
                   mysqli_real_escape_string($con, urldecode($_POST['output'])),
                   mysqli_real_escape_string($con, urldecode($_POST['answer'])));
    $result = mysqli_query($con, $sql);
    $row = mysqli_fetch_assoc($result);

    if($row['id'] != ''){
    /*$sql = "INSERT INTO `summenformeln_aufrufe` (`summenformel_id` ,`zeit` ,`richtig`)
        VALUES ('".$row['id']."', '3', '1');";
    mysqli_query($sql);*/
    $rest = ";correct;".urldecode($_POST['output'])." ist ".urldecode($_POST['answer']);
    } else {
    $sql = sprintf("SELECT * FROM summenformeln WHERE summenformel='%s'",
                   mysqli_real_escape_string($con, urldecode($_POST['output'])));
    $result = mysqli_query($con, $sql);
    $row = mysqli_fetch_assoc($result);
    /*$sql = "INSERT INTO `summenformeln_aufrufe` (`summenformel_id` ,`zeit` ,`richtig`)
        VALUES ('".$row['id']."', '3', 0);";
    mysqli_query($sql);*/
    $lernen = $row['summenformel'];
    $rest = ";wrong;".urldecode($_POST['output'])." ist ".$row['name']."<br>Sie haben ".str_diff($row['name'], urldecode($_POST['answer']))." eingegeben";
    }
} else {$rest = " ; ; ";}
echo $lernen.$rest;

function select_learn($cat){
    global $con;
    $sql     = "SELECT * FROM summenformeln WHERE 1=1 ";
    $cat = str_replace('cat=', '', $cat);
    if(strpos($cat, '&') !== 0){
    $cat = explode('&', $cat);
    }
    $anzahl    = count($cat);
    if($anzahl === 0){
        $string = 'AND 1 = 2';
    } else {
        for($i=0;$i<$anzahl;$i++){
            if($i > 0) {
                $string .= ' OR cat_id = '.intval($cat[$i]);
            } else {
                $string = ' AND (cat_id = '.intval($cat[0]);
            }
        }
    }
    $string    .= ') ORDER BY RAND() LIMIT 1';
    $sql    .= $string;
    $result  = mysqli_query($con, $sql);
    $row     = mysqli_fetch_assoc($result);
    return $row['summenformel'];
}

function str_diff($str_1, $str_2){
    $strlen = strlen($str_1);
    if(strlen($str_2)<$strlen){$strlen = strlen($str_2);}
    else {
    $end_wrong = '<span style="color: red">'.substr($str_2, strlen($str_1)).'</span>';
    }
    $return = '';
    $wrong = '';
    for($i=0;$i<$strlen;++$i){
    if(substr($str_1, $i ,1) != substr($str_2, $i ,1)){
        $wrong .= substr($str_2, $i ,1);
    }
    else {
        if($wrong != ''){$return .= '<span style="color: red">'.$wrong.'</span>';$wrong='';}
        else {$return .= substr($str_1, $i ,1);}
    }
    }
    if($wrong != ''){$return .= '<span style="color: red">'.$wrong.'</span>';$wrong='';}

    return $return.$end_wrong;
}
?>
