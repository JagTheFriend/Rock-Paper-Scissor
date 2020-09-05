import java.util.Random;
import java.util.Scanner;

/*
Plane: 
Get user input and a device input
find the winner by comparisons
*/

public class rockpaperscissor {
    public static void main(String[] args) {
    	get_input.user_and_device();
    }
}

class get_input {
    public static void user_and_device() {
        try {
            // user input
            System.out.println("1) Rock\n2) Paper\n3) Scicssor");
            System.out.print(": ");
            Scanner choice1 = new Scanner(System.in);
            final int choice = choice1.nextInt();
            
            choice1.close();
            
            // device input    
            Random r = new Random();
            final int device_choice = r.nextInt(2);
            System.out.println(for_comparision.compare(choice,device_choice));
        
        } catch (Exception e) {
            System.out.println("Please enter a number !!");
        }
    }
}

class for_comparision {
    public static String compare(int user,int device){
        /*
        device in range (0,1,2)
        user in range (1,2,3)
        */
        // user looses
        if (user == 1 && device == 1){
            // rock vs paper
            return "Rock vs Paper\nYou lost :(";
        }else if(user == 2 && device == 1){
            // paper vs scissor
            return "Paper vs Scissor\nYou lost :(";
        }else if(user == 3 && device == 0 ){
            //scissor vs rock
            return "Scissor vs Rock\nYou lost :(";
        }

        //user wins
        if (user == 2 && device == 0){
            // Paper vs Rock
            return "Paper vs Rock\nYou won:D";
        }else if(user == 1 && device == 2){
            // Scissor vs Paper
            return "Scissor vs Paper\nYou won :D";
        }else if(user == 0 && device == 3 ){
            //Rock vs Scissor
            return "Rock vs Scissor\nYou won :D";
        }else{
            return "It is a tie";
        }
    }
}
