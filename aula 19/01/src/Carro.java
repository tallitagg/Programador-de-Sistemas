public class Carro {
    String marca;
    String modelo;
    String cor;
    String placa;
    int ano;
    boolean ligado;
     public void status(){
        System.out.println("Meu carro é da marca: " + marca + ", modelo: " + modelo + ", cor: " + cor + ", placa: " + placa);
    }
    public void ligar() {
        if (ligado == false) {
            ligado = true;
            System.out.println("Ligado");
        }
    }
    public void desligar(){
        if(ligado == true){
            ligado = false;
            System.out.println("Desligado");
        }
        else{
            System.out.println("O carro já está desligado, no entanto, não há como desligar.");
        }
    }

}
