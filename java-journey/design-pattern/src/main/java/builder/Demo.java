package builder;

public class Demo {


    public static void main(String[] args) {
        Student student = Student.getBuilder().setId(001).setName("Luke").setAddress("Zhejiang").build();
        System.out.println(student);
    }
}
