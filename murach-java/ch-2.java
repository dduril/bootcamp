// public class named InvoiceApp
public class InvoiceApp {
    public static void main(String[] args) {
        System.out.println("Welcome to the Invoice Total Calculator"); 
    } 
}

// declare variables 
int counter = 0;
double unitPrice = 14.95;
        
System.out.println("counter: " + counter);
System.out.println("unitPrice: " + unitPrice);
        
// declare and initialize strings
String firstName = "John";
String lastName = "Smith";
String fullName = firstName + " " + lastName;
       
int departmentCode = 12;
String departmentName = "Human Resources";
      
// common escape characters
"Code: Java\nPrice: $49.50" // newline
"John\tSmith\rKate\tLewis"  // tabs and returns
"Type \"x\" to exit"        // quotation marks
"C:\\development\\java\\"   // backslash
      
// append strings and build display output
// use common escape characters and line continuation 
System.out.println("\nName:\t\t" + fullName + "\nDepartment:\t" 
        + departmentCode + " (" + departmentName + ")");
   
// import a single class from a package
import java.util.Scanner;
import java.util.Date;
import java.text.NumberFormat;

// import all classes in a package
import java.util.*;
import java.text.*;
   
// create an object from a class
Scanner sc = new Scanner(System.in);
Date now = new Date();
        
// call a method from a class
double subtotal = sc.nextDouble();
String currentDate = now.toString();

// call a static method from a class
String priceString = Double.toString(price);
double total = Double.parseDouble(inputStr);

// println() method
System.out.println("Welcome to the Invoice Total Calculator");
System.out.println("Total: " + total);
System.out.println(message);
System.out.println();

// print() method
System.out.print("Total: ");
System.out.print(total);
System.out.print("\n");

// Scanner object
import java.util.*;

// create a Scanner object
Scanner sc = new Scanner(System.in);

// read a string
System.out.println("Enter product code: ");
String produceCode = sc.next();

// read a double value
System.out.println("Enter price: ");
double price = sc.nextDouble();

// read an int value
System.out.println("Enter quantity: ");
int quantity = sc.nextInt();

// perform a calculation and display the result
double total = price * quantity;
System.out.println();
System.out.println(quantity + " " + productCode +
                    " @ " + price + " = " + total);
System.out.println();

// String class comparison
userEntry.equals("Y");
userEntry.equalsIgnoreCase("Y");
!lastName.equals("Smith");
code.equalsIgnoreCase(productCode);

// if statement with an else clause
double discountPercent = 0.0;
if (subtotal >= 100) {
    discountPercent = .2;
} else {
    discountPercent = .1;
}

// if statement with else if and else clauses
double discountPercent = 0.0;
if (customerType.equals("T")) {
    discountPercent = .4;
} else if (customerType.equals("C")) {
    discountPercent = .2;
} else if (subtotal >= 100) {
    discountPercent = .2;
} else {
    discountPercent = .1;
}

// while loop
Scanner sc = new Scanner(System.in);
String choice = "y";
while (choice.equalsIgnoreCase("y")) {

    // todo...

}