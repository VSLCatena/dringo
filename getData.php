<?php

#[[[2, 2, 'ko', False, [0, 0]], ['ka', 'k_', ''], ['ko', 'ko', '']]] naar 
#array[[2,2,ko,False,0,0], [ka,k_,''], [ko, ko, ''] 

$aData=file_get_contents('./dringo_output.txt');
$aData= str_replace("'", "", $aData);
$aData= str_replace(" ", "", $aData);
$aData=substr($aData,3,-3);
$aData=preg_split('/],\[/', $aData);

foreach ($aData as $key=>$value) {

	$aData[$key]=preg_split('/,/', $aData[$key]);
	$aData[$key]=str_replace("]", "", $aData[$key]);
	$aData[$key]=str_replace("[", "", $aData[$key]);
}
	
		#echo("<pre>");
		#print_r($aData);

echo json_encode($aData); 

?>