//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {
        Carro c1 = new Carro();
        c1.marca = "Volkswagen";
        c1.modelo = "Fusca";
        c1.ano = 1972;
        c1.cor = "Vermelho";
        c1.placa = "PTD - 2385";
        c1.ligado = false;

        c1.status();
        c1.ligar();
        c1.desligar();

        Carro c2 = new Carro();
        c2.marca = "Fiat";
        c2.modelo = "UNO";
        c2.ano = 1980;
        c2.cor = "Amarelo";
        c2.placa = "TGG - 0505";
        c2.ligado = false;

        c2.status();
        c2.ligar();
        c2.desligar();
    }
}