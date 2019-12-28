package powermock;

public class CollaboratorForPartialMocking {
    public static String staticMethod() {
        return "Hello Luke!";
    }

    public final String finalMethod() {
        return "Hello Luke!";
    }

    private String privateMethod() {
        return "Hello Luke!";
    }

    public String privateMethodCaller() {
        return privateMethod() + " Welcome to the Java world.";
    }
}
