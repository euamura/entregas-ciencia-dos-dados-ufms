public class ContaCorrente {

    // Atributos da classe (package private, sem modificador de acesso)
    float juros = 0.01f;
    float saldo;
    float limiteChequeEspecial = -200;
    String nome;
    String sobrenome;
    long numero;

    // Método para depositar um valor na conta
    public void deposito(float valor) {
        saldo = saldo + valor;
    }

    // Método para sacar, verificando o limite do cheque especial
    public void saque(float valor) {
        if ((saldo - valor) >= limiteChequeEspecial) {
            saldo = saldo - valor;
        } else {
            System.out.println("Limite insuficiente!");
        }
    }

    // Método que aplica o rendimento (juros) sobre o saldo, se o saldo for positivo
    public void rendimento() {
        if (saldo >= 0) {
            saldo = saldo + (saldo * juros);
        }
    }

    // Método para exibir o saldo no console
    public void exibirSaldo() {
        System.out.println("Saldo atual: R$" + saldo);
    }

    // Método que retorna o nome completo do cliente
    public String getNome() {
        return nome + " " + sobrenome;
    }

    // Método que retorna o número da conta
    public long getNumero() {
        return numero;
    }

    // Método principal
    public static void main(String[] args) {
        // Criando uma instância da classe ContaCorrente
        ContaCorrente conta = new ContaCorrente();

        // Realizando as operações solicitadas
        conta.deposito(100);
        conta.saque(125);
        conta.rendimento();
        conta.exibirSaldo();
    }
}