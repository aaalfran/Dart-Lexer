//Algoritmo de Aaron


mifuncion(){
  //Probando valores negativos y return 
  var valorNeg = -14.5;
  return valorNeg;
}

miLista(){
  //Probando Casting y Listas
  List<int> valores = [0,1,2,3];
}

miCasting(){
  
  //Probando Casting 
  var x = 1;
  String x_string = x.toString();
  int x_Integer = x.toInt();
  double x_double = x.toDouble();
  
  return x;
}

void main() {
  var a = 0 ;
  var b = 0;
  bool verdad = true;
  bool falso = false;
  String grupo = "Aaron, Pedro, Fabrizzio";
  String com_simpl = 'A';
  int numGrupo = 1;
  
  //Probando Menor que
  while(a<b){
    if(b==0){
      print("a es un numero negativo");
    }else{
      print(a);
      a++;
    }
  }
  if(a==b){
    print(grupo);
    print(numGrupo);
  }
  
  for(int i=0;i<=5;i++){
      print(mifuncion());
  }
  
  //Probando Resta
  print(a-b);
  //Probando Division
  var f = 4;
  var d = 2;
  
  print(f/d);
  
  //Probando Multiplicacion
  
  print(f*d);
  //Probando Mayor que y OR
  if(a>b || falso){
    print("A es mayor que B");
  }
  //Probando AND y Negacion
  if(verdad && verdad){
    print("Es verdad");
    print(!verdad);
  }
}

//Algoritmo de pedro
var precio = 500;
if (precio  == 500) {
  print("Precio promedio");
} else if (precio > 500) {
  print("Precio mayor del promedio");
} else {
  print("Precio comun");
}


//Algoritmo de Fabrizzio
List<int> edades=[10,20,30,18,15,20,8];
for(int edad in edades){
    if (edad>=18){
       print("Es mayor de edad");
    }else{
       print("Es menor de edad");
    }
}


