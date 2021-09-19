const d = new Date();

date = d.getDate();
month= d.getMonth()+1;
year= d.getFullYear()
time=d.getHours()+":"+d.getMinutes()+":"+d.getSeconds()

if (new_level>120){
  state="High blood sugar"
}
else if (new_level>80){
  state="Normal"
}
else{
  state="Low Blood sugar"
}
