package forbucle;
import javax.swing.*;
public class NombreEnBinario {
public static void main(String[] args) {
String caracter, binario = "";
float n, coci, resi, residuo;

caracter = JOptionPane.showInputDialog("Digite su nombre");
for (int i = caracter.length() - 1; i >= 0; i--) {
char character = caracter.charAt(i);
while (character > 0) {
binario = character % 2 + binario;
character /= 2;
}
for (int j = 0; j < 9 - binario.length() % 9; j++) {
binario = "0" + binario;
}
binario = ' ' + binario;
}
System.out.println(binario+"\n"+" "
		) ;
}
}
