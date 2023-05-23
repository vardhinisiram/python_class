class Person {
    private int age;
    private int height;
    void set_details() {
        this.age = 20;
        this.height= 5;
    }
    void get_details() {
        System.out.println(this.age);
        System.out.println(this.height);
    }
}


class Test {
    public static void main(String args[]){
        Person p = new Person();
        System.out.println(p.age);
        p.set_details();
        p.get_details();
    }
}
