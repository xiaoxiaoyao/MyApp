package main.java;

public class Nine {
	public static void main(String[] arguments) {
		for(int dex = 1; dex <= 900 ; dex++) {
			if(dex % 4 == 1) {
				System.out.println(dex + " continue");
				continue;
			}
			System.out.print(dex + " ");
			dex = (dex % 2 == 0) ? dex*2 : dex *3;
			System.out.println(dex + " ");
			if(dex % 5 == 0) {
				System.out.println(dex + " break");
				break;
			}
		}
	}

}
