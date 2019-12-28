package calculator;

public class Calculator {
    private NumberSource numberSource;

    public Calculator(final NumberSource numberSource) {
        this.numberSource = numberSource;
    }

    public long addTwoNumbers() {
        return numberSource.fetchNextNumber() + numberSource.fetchNextNumber();
    }
}
