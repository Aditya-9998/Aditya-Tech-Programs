// file name swap.java
// swap three no using 3 methode

//using temp variable

class Swap {
    public static void main(String[] args) {
        int a = 10, b = 20, c = 30;
        System.out.println("Before swap: a=" + a + ", b=" + b + ", c=" + c);
        
        // Using a temporary variable
        int temp = a;
        a = b;
        b = c;
        c = temp;
        
        System.out.println("After swap using temp variable: a=" + a + ", b=" + b + ", c=" + c);
        
        // Using arithmetic operations
        a = 10; b = 20; c = 30; // Reset values
        System.out.println("Before swap: a=" + a + ", b=" + b + ", c=" + c);
        
        a = a + b; // a becomes 30
        b = a - b; // b becomes 10
        a = a - b; // a becomes 20
        
        System.out.println("After swap using arithmetic operations: a=" + a + ", b=" + b);
        
        // Using bitwise XOR
        a = 10; b = 20; c = 30; // Reset values
        System.out.println("Before swap: a=" + a + ", b=" + b + ", c=" + c);
        
        a = a ^ b; // XOR operation
        b = a ^ b; // XOR operation
        a = a ^ b; // XOR operation
        
        System.out.println("After swap using bitwise XOR: a=" + a + ", b=" + b);
    }
}
