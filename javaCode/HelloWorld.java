public class HelloWorld {
    public static void main(String[] args){
        System.out.println("你好，老铁");
    }
}

long gcd(long a, long b) {
    return b == 0 ? a : gcd(b, a % b);
}   
